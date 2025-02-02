

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7e6d594d-952e-44b6-97ea-31225882aea6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664NVVQPDO%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T081640Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEN7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAvltayY%2BqykYfNIzwFjtV2y2krYnWwj6rI4XYTD%2BWrCAiEAinxslBpue5S6VvQFlJNgMzuJtVum4e5PWjjlfDgaHJEqiAQI5%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLHGWVbJSKHM6GpM5ircA8D6Rr0UQMS8Tz5idgm70GTcovmzC9DMIc2pLOkAb5X2yL2%2Fx%2BJSqEbRZC0SwoER7RDxbY6GxHf10balzU%2Bnv5w0IgiEnnC1Ue2Vbqw4jL2vq5Cb48ssP7ynRKOefjizxw%2F01GiANqscEQINiil09FG2ePJtgfMzF9VKafhjmGdvAting6WxVH8qUPE0Po1SijAXuuJYDC51T8D85PstDEnA3wN8%2FvQM1Z%2F38N%2FgRqph0TKzRcgn5w6J3mdruwadakavbAl6Hkp8LpVdB25nn8tGbipu%2F2UQ5yNzJUOzz8cp7EnAsqN%2BWbT3V%2B8gtN1bVNm8f8%2F0mDBgh1obK2jh2L7amU2M9Mixn6xBXzLLfRSXG136oJ%2FjikiZWRw3s0skT1qGIj4zcv%2F1lPlQnJPSGoR99n37WXMXXu3NdBT%2FKcbpIq3%2FbbeMxhOIrG4n%2FkKlc0fsZItjvpRD%2FYxxTc2uGcRxpKSb1%2FuhSFSbKDnzt10XulGTXx98nNiiMyD3D0fhP8utARKkqDl6bTYGjwGnZ9CZCMKrl55JFL%2FzimBGzIjgd4khMZOtr4HNpXaYq16vGPVgkA6Cc7IvOdseSdfrEG0jU65g3SHJDVb43CupMdVtoPu8hov7m9m3UkRQMOab%2FLwGOqUBBkSXOkLPEA6I6DarAdVf%2FQNjP7MWTB4Ju%2F0yKh4X1QeQC3ltfJQ5E7VurDzJMtfzqfk5nfVuR5vtQQJgNDKLdVJchk19hkvNgusU7L%2FHfHUb9sP5s2Uxdp7hoWBz%2BudggVCp1xTYqSeoLRTn89OYwJH71nkrU2MtopPcdTKW%2B1EmzDr6tTZ%2F8mWdY%2BJR62wsQE532mr1Ep7Q5X89UOtWSzF72UfK&X-Amz-Signature=b11f4aa5fce95ad20b516216c5f9bf780fdae39ae24bf618b25ee8708fc715d6&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cbfaed9e-b398-4902-8936-dea058b21def/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664NVVQPDO%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T081640Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEN7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAvltayY%2BqykYfNIzwFjtV2y2krYnWwj6rI4XYTD%2BWrCAiEAinxslBpue5S6VvQFlJNgMzuJtVum4e5PWjjlfDgaHJEqiAQI5%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLHGWVbJSKHM6GpM5ircA8D6Rr0UQMS8Tz5idgm70GTcovmzC9DMIc2pLOkAb5X2yL2%2Fx%2BJSqEbRZC0SwoER7RDxbY6GxHf10balzU%2Bnv5w0IgiEnnC1Ue2Vbqw4jL2vq5Cb48ssP7ynRKOefjizxw%2F01GiANqscEQINiil09FG2ePJtgfMzF9VKafhjmGdvAting6WxVH8qUPE0Po1SijAXuuJYDC51T8D85PstDEnA3wN8%2FvQM1Z%2F38N%2FgRqph0TKzRcgn5w6J3mdruwadakavbAl6Hkp8LpVdB25nn8tGbipu%2F2UQ5yNzJUOzz8cp7EnAsqN%2BWbT3V%2B8gtN1bVNm8f8%2F0mDBgh1obK2jh2L7amU2M9Mixn6xBXzLLfRSXG136oJ%2FjikiZWRw3s0skT1qGIj4zcv%2F1lPlQnJPSGoR99n37WXMXXu3NdBT%2FKcbpIq3%2FbbeMxhOIrG4n%2FkKlc0fsZItjvpRD%2FYxxTc2uGcRxpKSb1%2FuhSFSbKDnzt10XulGTXx98nNiiMyD3D0fhP8utARKkqDl6bTYGjwGnZ9CZCMKrl55JFL%2FzimBGzIjgd4khMZOtr4HNpXaYq16vGPVgkA6Cc7IvOdseSdfrEG0jU65g3SHJDVb43CupMdVtoPu8hov7m9m3UkRQMOab%2FLwGOqUBBkSXOkLPEA6I6DarAdVf%2FQNjP7MWTB4Ju%2F0yKh4X1QeQC3ltfJQ5E7VurDzJMtfzqfk5nfVuR5vtQQJgNDKLdVJchk19hkvNgusU7L%2FHfHUb9sP5s2Uxdp7hoWBz%2BudggVCp1xTYqSeoLRTn89OYwJH71nkrU2MtopPcdTKW%2B1EmzDr6tTZ%2F8mWdY%2BJR62wsQE532mr1Ep7Q5X89UOtWSzF72UfK&X-Amz-Signature=2c27d540a00bcece63c73d2dd13f217513fb56c528afb59e42eb52ca8500d5eb&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/91181646-b1e0-4433-9711-6259a96a9247/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664NVVQPDO%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T081640Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEN7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAvltayY%2BqykYfNIzwFjtV2y2krYnWwj6rI4XYTD%2BWrCAiEAinxslBpue5S6VvQFlJNgMzuJtVum4e5PWjjlfDgaHJEqiAQI5%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLHGWVbJSKHM6GpM5ircA8D6Rr0UQMS8Tz5idgm70GTcovmzC9DMIc2pLOkAb5X2yL2%2Fx%2BJSqEbRZC0SwoER7RDxbY6GxHf10balzU%2Bnv5w0IgiEnnC1Ue2Vbqw4jL2vq5Cb48ssP7ynRKOefjizxw%2F01GiANqscEQINiil09FG2ePJtgfMzF9VKafhjmGdvAting6WxVH8qUPE0Po1SijAXuuJYDC51T8D85PstDEnA3wN8%2FvQM1Z%2F38N%2FgRqph0TKzRcgn5w6J3mdruwadakavbAl6Hkp8LpVdB25nn8tGbipu%2F2UQ5yNzJUOzz8cp7EnAsqN%2BWbT3V%2B8gtN1bVNm8f8%2F0mDBgh1obK2jh2L7amU2M9Mixn6xBXzLLfRSXG136oJ%2FjikiZWRw3s0skT1qGIj4zcv%2F1lPlQnJPSGoR99n37WXMXXu3NdBT%2FKcbpIq3%2FbbeMxhOIrG4n%2FkKlc0fsZItjvpRD%2FYxxTc2uGcRxpKSb1%2FuhSFSbKDnzt10XulGTXx98nNiiMyD3D0fhP8utARKkqDl6bTYGjwGnZ9CZCMKrl55JFL%2FzimBGzIjgd4khMZOtr4HNpXaYq16vGPVgkA6Cc7IvOdseSdfrEG0jU65g3SHJDVb43CupMdVtoPu8hov7m9m3UkRQMOab%2FLwGOqUBBkSXOkLPEA6I6DarAdVf%2FQNjP7MWTB4Ju%2F0yKh4X1QeQC3ltfJQ5E7VurDzJMtfzqfk5nfVuR5vtQQJgNDKLdVJchk19hkvNgusU7L%2FHfHUb9sP5s2Uxdp7hoWBz%2BudggVCp1xTYqSeoLRTn89OYwJH71nkrU2MtopPcdTKW%2B1EmzDr6tTZ%2F8mWdY%2BJR62wsQE532mr1Ep7Q5X89UOtWSzF72UfK&X-Amz-Signature=2e70e6418824121d032f521b6f82bfc892e4d033dec5461e93dfeb9f00fb0678&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/09aba1c0-0d55-41dd-852a-a04c5b8a3fac/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46666LZQI4T%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T081641Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEN%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC0acSFFdcJBkBgtCkMKuYT7JgVNlIcjrh9zGDe8N7c%2BQIhAJt72p8FDh8iwgNt%2BeCXtItFJQ5dGEsPlvEwxBC%2BYWISKogECOf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyrPDlphDUJRqYUT8Eq3ANF7ypHmU2vCJxmWo%2BgnnMAVrCIHAPb7F6iwasXqrhC0B09mQ6YhiyBxreISxPrSgR8isJ69stXFfw22C0oCtyZszGHY6A6Tt6etQHe1jYPZr6OUzSEq1lUxgR%2F8XV4XXKp1JMUyusBvp4ALlxrJoaDetds7c87B8yIHb3DXUeczmkfLPAaqzA6xrZZL8BEWscV9jVketsz4f3xaLxRgKJnnyugKAONiB%2FGpU1sOqN8QPzfanE996wMsrFXPg6wzW1iPNHzB%2BW5GsSgVrIS9wjQN2j8T4DaadvfxdSS%2BuxnGFFAcSY5OfToQ5vylZm%2BIP24jmxX0T1nfCR3mHjMunu2xvYzJpuYfpoGFYomyptLgNKOD4MDDGkLYXAKei90wkkAG943lIC9tWS1OQ5eIqNEf9f4fd%2FKa4KWkTqSwJDuhKTJRpfnVX%2F%2BXkQ7HlOVbas9%2F1NH6D%2Ba6bbjr5rCwH6n0Hux0vJz3T4fSKGiMObJjv34WcVYIBErRfZfQSOnsN5SbQJ5krZPcdgyS77hMNYgTqRb7phTVCPcb0D%2Bquvl5LY6lXad%2BXV48lv8f441x84McKICmJ8TWMNIGccT1iSrKlGyiJezrj9PS9AJwf%2F7I1HB0BwqbEWSQkMi1DCznPy8BjqkARSmH6Qy7kD50fWTJm%2BaXSQEYtVydEsCkMuIYGvgyzGSXw9aAa8rnR9SfsYqnqmOzbTv8AM%2FYlBTd%2FvXopqtpE97UwwzAxqP1XmBJX%2BC3s3F5bJNewLz2rz%2BN4wen3%2FW2Mko4QRvqi8gYuvNnlgs3awvqmcQAi9yG7JlTcn8JVHGfOjvxH5fdfvQGkqOqvVyFyXfiub8kVB56dPr6CxbL2lsB%2Ff%2F&X-Amz-Signature=df4c61268c022314e099578887e5ef3eb27d3aad4f8e20f7c87630934a420072&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 2. Scatter Plot
Scatter plots present the relationship between two variables in a dataset. It represents data points on a two-dimensional plane. The independent variable or attribute is plotted on the X-axis, while the dependent variable is plotted on the Y-axis.
**Syntax:**
```python
plt.scatter(x, y)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23708af9-659f-4f23-b626-1a4292d7842c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46666LZQI4T%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T081641Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEN%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC0acSFFdcJBkBgtCkMKuYT7JgVNlIcjrh9zGDe8N7c%2BQIhAJt72p8FDh8iwgNt%2BeCXtItFJQ5dGEsPlvEwxBC%2BYWISKogECOf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyrPDlphDUJRqYUT8Eq3ANF7ypHmU2vCJxmWo%2BgnnMAVrCIHAPb7F6iwasXqrhC0B09mQ6YhiyBxreISxPrSgR8isJ69stXFfw22C0oCtyZszGHY6A6Tt6etQHe1jYPZr6OUzSEq1lUxgR%2F8XV4XXKp1JMUyusBvp4ALlxrJoaDetds7c87B8yIHb3DXUeczmkfLPAaqzA6xrZZL8BEWscV9jVketsz4f3xaLxRgKJnnyugKAONiB%2FGpU1sOqN8QPzfanE996wMsrFXPg6wzW1iPNHzB%2BW5GsSgVrIS9wjQN2j8T4DaadvfxdSS%2BuxnGFFAcSY5OfToQ5vylZm%2BIP24jmxX0T1nfCR3mHjMunu2xvYzJpuYfpoGFYomyptLgNKOD4MDDGkLYXAKei90wkkAG943lIC9tWS1OQ5eIqNEf9f4fd%2FKa4KWkTqSwJDuhKTJRpfnVX%2F%2BXkQ7HlOVbas9%2F1NH6D%2Ba6bbjr5rCwH6n0Hux0vJz3T4fSKGiMObJjv34WcVYIBErRfZfQSOnsN5SbQJ5krZPcdgyS77hMNYgTqRb7phTVCPcb0D%2Bquvl5LY6lXad%2BXV48lv8f441x84McKICmJ8TWMNIGccT1iSrKlGyiJezrj9PS9AJwf%2F7I1HB0BwqbEWSQkMi1DCznPy8BjqkARSmH6Qy7kD50fWTJm%2BaXSQEYtVydEsCkMuIYGvgyzGSXw9aAa8rnR9SfsYqnqmOzbTv8AM%2FYlBTd%2FvXopqtpE97UwwzAxqP1XmBJX%2BC3s3F5bJNewLz2rz%2BN4wen3%2FW2Mko4QRvqi8gYuvNnlgs3awvqmcQAi9yG7JlTcn8JVHGfOjvxH5fdfvQGkqOqvVyFyXfiub8kVB56dPr6CxbL2lsB%2Ff%2F&X-Amz-Signature=a52f6e5db3df95b1ed96878430af02ccc6fa1e509f4c22b58ffc25176dfa3d2b&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 3. Histogram
A histogram is an important visual representation of data in categorical form. To view the data in a "Binned" form, use the histogram plot with a number of bins required or with the data points that mark the bin edges. The x-axis represents the data bins, and the y-axis represents the number of elements in each bin.
**Syntax:**
```python
plt.hist(x, bins)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/24e4424a-df87-40a1-b63b-195cbdc2e0ab/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46666LZQI4T%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T081641Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEN%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC0acSFFdcJBkBgtCkMKuYT7JgVNlIcjrh9zGDe8N7c%2BQIhAJt72p8FDh8iwgNt%2BeCXtItFJQ5dGEsPlvEwxBC%2BYWISKogECOf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyrPDlphDUJRqYUT8Eq3ANF7ypHmU2vCJxmWo%2BgnnMAVrCIHAPb7F6iwasXqrhC0B09mQ6YhiyBxreISxPrSgR8isJ69stXFfw22C0oCtyZszGHY6A6Tt6etQHe1jYPZr6OUzSEq1lUxgR%2F8XV4XXKp1JMUyusBvp4ALlxrJoaDetds7c87B8yIHb3DXUeczmkfLPAaqzA6xrZZL8BEWscV9jVketsz4f3xaLxRgKJnnyugKAONiB%2FGpU1sOqN8QPzfanE996wMsrFXPg6wzW1iPNHzB%2BW5GsSgVrIS9wjQN2j8T4DaadvfxdSS%2BuxnGFFAcSY5OfToQ5vylZm%2BIP24jmxX0T1nfCR3mHjMunu2xvYzJpuYfpoGFYomyptLgNKOD4MDDGkLYXAKei90wkkAG943lIC9tWS1OQ5eIqNEf9f4fd%2FKa4KWkTqSwJDuhKTJRpfnVX%2F%2BXkQ7HlOVbas9%2F1NH6D%2Ba6bbjr5rCwH6n0Hux0vJz3T4fSKGiMObJjv34WcVYIBErRfZfQSOnsN5SbQJ5krZPcdgyS77hMNYgTqRb7phTVCPcb0D%2Bquvl5LY6lXad%2BXV48lv8f441x84McKICmJ8TWMNIGccT1iSrKlGyiJezrj9PS9AJwf%2F7I1HB0BwqbEWSQkMi1DCznPy8BjqkARSmH6Qy7kD50fWTJm%2BaXSQEYtVydEsCkMuIYGvgyzGSXw9aAa8rnR9SfsYqnqmOzbTv8AM%2FYlBTd%2FvXopqtpE97UwwzAxqP1XmBJX%2BC3s3F5bJNewLz2rz%2BN4wen3%2FW2Mko4QRvqi8gYuvNnlgs3awvqmcQAi9yG7JlTcn8JVHGfOjvxH5fdfvQGkqOqvVyFyXfiub8kVB56dPr6CxbL2lsB%2Ff%2F&X-Amz-Signature=4199887e0bd44adfeeb7eff74b7069c5c3398f7019aa8396461da0f0d3410d1b&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ab5a6dfe-51f5-43ee-bcb3-33dae4a1c7ad/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46666LZQI4T%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T081641Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEN%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC0acSFFdcJBkBgtCkMKuYT7JgVNlIcjrh9zGDe8N7c%2BQIhAJt72p8FDh8iwgNt%2BeCXtItFJQ5dGEsPlvEwxBC%2BYWISKogECOf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyrPDlphDUJRqYUT8Eq3ANF7ypHmU2vCJxmWo%2BgnnMAVrCIHAPb7F6iwasXqrhC0B09mQ6YhiyBxreISxPrSgR8isJ69stXFfw22C0oCtyZszGHY6A6Tt6etQHe1jYPZr6OUzSEq1lUxgR%2F8XV4XXKp1JMUyusBvp4ALlxrJoaDetds7c87B8yIHb3DXUeczmkfLPAaqzA6xrZZL8BEWscV9jVketsz4f3xaLxRgKJnnyugKAONiB%2FGpU1sOqN8QPzfanE996wMsrFXPg6wzW1iPNHzB%2BW5GsSgVrIS9wjQN2j8T4DaadvfxdSS%2BuxnGFFAcSY5OfToQ5vylZm%2BIP24jmxX0T1nfCR3mHjMunu2xvYzJpuYfpoGFYomyptLgNKOD4MDDGkLYXAKei90wkkAG943lIC9tWS1OQ5eIqNEf9f4fd%2FKa4KWkTqSwJDuhKTJRpfnVX%2F%2BXkQ7HlOVbas9%2F1NH6D%2Ba6bbjr5rCwH6n0Hux0vJz3T4fSKGiMObJjv34WcVYIBErRfZfQSOnsN5SbQJ5krZPcdgyS77hMNYgTqRb7phTVCPcb0D%2Bquvl5LY6lXad%2BXV48lv8f441x84McKICmJ8TWMNIGccT1iSrKlGyiJezrj9PS9AJwf%2F7I1HB0BwqbEWSQkMi1DCznPy8BjqkARSmH6Qy7kD50fWTJm%2BaXSQEYtVydEsCkMuIYGvgyzGSXw9aAa8rnR9SfsYqnqmOzbTv8AM%2FYlBTd%2FvXopqtpE97UwwzAxqP1XmBJX%2BC3s3F5bJNewLz2rz%2BN4wen3%2FW2Mko4QRvqi8gYuvNnlgs3awvqmcQAi9yG7JlTcn8JVHGfOjvxH5fdfvQGkqOqvVyFyXfiub8kVB56dPr6CxbL2lsB%2Ff%2F&X-Amz-Signature=c8ff572c20ce4f9777153ae9805f5e98dff36151ffecbfab3b73ed930b3b6e2f&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8f1b1d60-cf1b-42b3-9faa-f634c89c3f84/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46666LZQI4T%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T081641Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEN%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC0acSFFdcJBkBgtCkMKuYT7JgVNlIcjrh9zGDe8N7c%2BQIhAJt72p8FDh8iwgNt%2BeCXtItFJQ5dGEsPlvEwxBC%2BYWISKogECOf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyrPDlphDUJRqYUT8Eq3ANF7ypHmU2vCJxmWo%2BgnnMAVrCIHAPb7F6iwasXqrhC0B09mQ6YhiyBxreISxPrSgR8isJ69stXFfw22C0oCtyZszGHY6A6Tt6etQHe1jYPZr6OUzSEq1lUxgR%2F8XV4XXKp1JMUyusBvp4ALlxrJoaDetds7c87B8yIHb3DXUeczmkfLPAaqzA6xrZZL8BEWscV9jVketsz4f3xaLxRgKJnnyugKAONiB%2FGpU1sOqN8QPzfanE996wMsrFXPg6wzW1iPNHzB%2BW5GsSgVrIS9wjQN2j8T4DaadvfxdSS%2BuxnGFFAcSY5OfToQ5vylZm%2BIP24jmxX0T1nfCR3mHjMunu2xvYzJpuYfpoGFYomyptLgNKOD4MDDGkLYXAKei90wkkAG943lIC9tWS1OQ5eIqNEf9f4fd%2FKa4KWkTqSwJDuhKTJRpfnVX%2F%2BXkQ7HlOVbas9%2F1NH6D%2Ba6bbjr5rCwH6n0Hux0vJz3T4fSKGiMObJjv34WcVYIBErRfZfQSOnsN5SbQJ5krZPcdgyS77hMNYgTqRb7phTVCPcb0D%2Bquvl5LY6lXad%2BXV48lv8f441x84McKICmJ8TWMNIGccT1iSrKlGyiJezrj9PS9AJwf%2F7I1HB0BwqbEWSQkMi1DCznPy8BjqkARSmH6Qy7kD50fWTJm%2BaXSQEYtVydEsCkMuIYGvgyzGSXw9aAa8rnR9SfsYqnqmOzbTv8AM%2FYlBTd%2FvXopqtpE97UwwzAxqP1XmBJX%2BC3s3F5bJNewLz2rz%2BN4wen3%2FW2Mko4QRvqi8gYuvNnlgs3awvqmcQAi9yG7JlTcn8JVHGfOjvxH5fdfvQGkqOqvVyFyXfiub8kVB56dPr6CxbL2lsB%2Ff%2F&X-Amz-Signature=bda3296083cc347c188604266072961fd37ebd15c93164ed8ece34ae2718d0d4&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/13ad0497-05fe-4eaa-984e-707b33e14761/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46666LZQI4T%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T081641Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEN%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC0acSFFdcJBkBgtCkMKuYT7JgVNlIcjrh9zGDe8N7c%2BQIhAJt72p8FDh8iwgNt%2BeCXtItFJQ5dGEsPlvEwxBC%2BYWISKogECOf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyrPDlphDUJRqYUT8Eq3ANF7ypHmU2vCJxmWo%2BgnnMAVrCIHAPb7F6iwasXqrhC0B09mQ6YhiyBxreISxPrSgR8isJ69stXFfw22C0oCtyZszGHY6A6Tt6etQHe1jYPZr6OUzSEq1lUxgR%2F8XV4XXKp1JMUyusBvp4ALlxrJoaDetds7c87B8yIHb3DXUeczmkfLPAaqzA6xrZZL8BEWscV9jVketsz4f3xaLxRgKJnnyugKAONiB%2FGpU1sOqN8QPzfanE996wMsrFXPg6wzW1iPNHzB%2BW5GsSgVrIS9wjQN2j8T4DaadvfxdSS%2BuxnGFFAcSY5OfToQ5vylZm%2BIP24jmxX0T1nfCR3mHjMunu2xvYzJpuYfpoGFYomyptLgNKOD4MDDGkLYXAKei90wkkAG943lIC9tWS1OQ5eIqNEf9f4fd%2FKa4KWkTqSwJDuhKTJRpfnVX%2F%2BXkQ7HlOVbas9%2F1NH6D%2Ba6bbjr5rCwH6n0Hux0vJz3T4fSKGiMObJjv34WcVYIBErRfZfQSOnsN5SbQJ5krZPcdgyS77hMNYgTqRb7phTVCPcb0D%2Bquvl5LY6lXad%2BXV48lv8f441x84McKICmJ8TWMNIGccT1iSrKlGyiJezrj9PS9AJwf%2F7I1HB0BwqbEWSQkMi1DCznPy8BjqkARSmH6Qy7kD50fWTJm%2BaXSQEYtVydEsCkMuIYGvgyzGSXw9aAa8rnR9SfsYqnqmOzbTv8AM%2FYlBTd%2FvXopqtpE97UwwzAxqP1XmBJX%2BC3s3F5bJNewLz2rz%2BN4wen3%2FW2Mko4QRvqi8gYuvNnlgs3awvqmcQAi9yG7JlTcn8JVHGfOjvxH5fdfvQGkqOqvVyFyXfiub8kVB56dPr6CxbL2lsB%2Ff%2F&X-Amz-Signature=bfcc07b84bb2ecdf36d0f12e8f6ce49db69e5746ad8ce3e4d3dba02ed491267f&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 2. Box and Whisker Plot
A box plot shows the distribution of quantitative data in a way that facilitates comparisons between variables or across levels of a categorical variable. The box shows the quartiles of the dataset while the whiskers extend to show the rest of the distribution, except for points that are determined to be "outliers".
**Syntax:**
```python
sns.boxplot(x='header_1', y='header_2', data=df)
```
**Example Output:**


![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d207ae92-0a7c-4e2f-aa65-0ee5a2c33bf7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466U7UVPFPL%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T081642Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEN%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDVmvCmkCa2j1l%2ByIBsR68zIZ48hI4D72jox%2BCIs2ELtAiEArpQFlC1bRGQWKQj2p0JOJ6%2BEYdQontLu6LI4OxtyhDEqiAQI5%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDM1Bb%2FOjH2svIfhJeyrcAwzlgVrA5dJSvsZnWd0ooWnYEI7RLN7%2FpaJ0WGff1odPYT6Z3tM%2Fs%2BH1XxYj1aRJYCcRu7uEs7zct4oapdo37pJXQI0Z4PID0tWTibSHf%2FGsKepWrg4lZ5NIMxjzH2e0EeX0Gh17oX%2BcCiunYFrv5mb4az%2BiMVYgLPskNkAeCk46iHUhKMdyfN8XJZnAZgVEL59OqpSEE4CJ1XdBvQdKKi0WTwWijsc1kUuiQnH7vtXQnqYVVc1zGX6gT9AtSjPU4Rf50cyRS8nSplhGkKF%2BB8WVh5tL87%2FHudhP9%2FQPCit%2FI6jzw59uahQ88u82Nw6tALNAY7lA5T9ITXYdPda1BfjmloYZv%2BffSGb%2FMe9V24fBSCHYNVFT7T1WpWZXUlGZ3iimxd58VCYMITkYafhOiyr9hiQhQKiyVLH71%2BQ5RYX6gGvdmdkH4%2Fod9hbYV0BeQ8TPau5oQTw%2FSf33YfBP%2BvaPBAYxizYfm9RKfLgCfT2ZmL9e3FVrTkE2OIF7ojlho%2BYeixBMPwUMVkZzsrLd%2BfXe41s%2FndIFMLiXAdfNhKxceBUIy6wMuoqWaGVIcCekp3%2FigNU7l59er4yKixrUG8oXsJ8MGy3BdsSzd9pkK2WC4vVtUjfzNNSjUJizMNac%2FLwGOqUBKc8o4M9hPvd3Qr51w1wfYVzBdlD5Hybfj9zNuogpsIsvWKsLIdSEeioiMj22TpBFO2eT5Ln8VCVxOmM6gl9Xml%2FgXyRPdBj5C0Dqiy3S58ZMGqpvZliv6HGPyrBeO%2FGC%2BCJOCLXZX8juu73LpYwMWLPI00n%2B09YZ19rLbcb69%2FbqM5CWpa1SkQqad%2FJtz3zw81YcrOzR94PGVuhhM6tmNEcYSTbF&X-Amz-Signature=deec9229f3a7e0f10aebb73af8f3e32ec329474d1cf379307a09f477c2bf270c&X-Amz-SignedHeaders=host&x-id=GetObject)

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0e516edc-7551-4792-ab18-0494db3c4c0c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SAGWQYUE%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T081642Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEN%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIDA6pLt5FjXdNDatxqa6GlmSe3u%2Bfolj0lG9z5los6utAiByz9gpLnNYFM7duwrh8eluyKc%2Fb9RqvrjjNBd4XFADVSqIBAjn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMF3O5FVGSYm1ID2i3KtwDIBcdawKcRQSVsVxDKNxeAtTyd3QuCUZjtt1eDAT%2BuF%2Bo1h4Edl5m9nk3zKvId05SxvSFrFT01VYKJP3w1YNpgBdfGi77ndhDuxGas2%2BOjym0kX9gu%2FECY9GgRs1S4J6oihe23DjtMdJWhqhsz6ATqvbpkbaj7I%2FLeMTbaM9Fq7DXM31mMSa%2FVTmr0ngsURcwLLqCFSPxFpRAFvkZSECUcWwxluf4Imp37dDvDpYizO9j5odNIh7fc0Ni9v%2BDTzseSKi48am7LL2wW9ZCwYS8vsbiImhZNeJD%2BjwRsTAit1wJgWasABNlyIwYNXDlXgopEOTLGBeGXFkAY9nChfVxvTQFyTLWqyvwc9WrA%2B%2FfFwGUatuQZHsjxi2OrszlZyEDTu73OP5nrgpNh7utKtz5VPlwKraRX4%2Buf4FYhkOSxzV%2BQnbLkhYZtA5%2F9ZgdsYjZe3IIySlhKIT8TZUM16uvjZf0LaZ4ifFK4dMJ8a%2BOb0iisL%2Bgofc3FoRc3imZ%2BpBEosPcDvnRIxioceddtkxv9FnFFFMSugX6wbmoVixdsW8agidnC9VMUo7560Q2yVaHaee%2FepisPZeyHsTPOLdIP7QF47gMlhj1jm%2BW6m8blNhfibsitaizXMHvkwQws5z8vAY6pgHMiEc%2BbERlMNOZZCCaivVf8uMbSfK%2BmIL6qAjYDocPrACD05XNc4lTSzxRlcdRt7wuxs7vzVFBnqIdv5DpvqIEYLDSkGQTzWcjDVtluwFHU%2FX27oft2TvXJVKP4urm%2F3iu5xBkMyXdeP9WvsfbgEgHkUPfLuFR1Nt3QTagp9fznFaYoALDzEhLMAOa%2FKL3v3pfxRI%2F5%2Bwt4Ql876eanSyCXvBPafI8&X-Amz-Signature=79e057c5629af93e744565d7cd59479e1b0153be574177234711d448138b9b81&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23a79b9d-2356-49a9-8fd9-65c6b0ab2cc5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46666LZQI4T%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T081641Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEN%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC0acSFFdcJBkBgtCkMKuYT7JgVNlIcjrh9zGDe8N7c%2BQIhAJt72p8FDh8iwgNt%2BeCXtItFJQ5dGEsPlvEwxBC%2BYWISKogECOf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyrPDlphDUJRqYUT8Eq3ANF7ypHmU2vCJxmWo%2BgnnMAVrCIHAPb7F6iwasXqrhC0B09mQ6YhiyBxreISxPrSgR8isJ69stXFfw22C0oCtyZszGHY6A6Tt6etQHe1jYPZr6OUzSEq1lUxgR%2F8XV4XXKp1JMUyusBvp4ALlxrJoaDetds7c87B8yIHb3DXUeczmkfLPAaqzA6xrZZL8BEWscV9jVketsz4f3xaLxRgKJnnyugKAONiB%2FGpU1sOqN8QPzfanE996wMsrFXPg6wzW1iPNHzB%2BW5GsSgVrIS9wjQN2j8T4DaadvfxdSS%2BuxnGFFAcSY5OfToQ5vylZm%2BIP24jmxX0T1nfCR3mHjMunu2xvYzJpuYfpoGFYomyptLgNKOD4MDDGkLYXAKei90wkkAG943lIC9tWS1OQ5eIqNEf9f4fd%2FKa4KWkTqSwJDuhKTJRpfnVX%2F%2BXkQ7HlOVbas9%2F1NH6D%2Ba6bbjr5rCwH6n0Hux0vJz3T4fSKGiMObJjv34WcVYIBErRfZfQSOnsN5SbQJ5krZPcdgyS77hMNYgTqRb7phTVCPcb0D%2Bquvl5LY6lXad%2BXV48lv8f441x84McKICmJ8TWMNIGccT1iSrKlGyiJezrj9PS9AJwf%2F7I1HB0BwqbEWSQkMi1DCznPy8BjqkARSmH6Qy7kD50fWTJm%2BaXSQEYtVydEsCkMuIYGvgyzGSXw9aAa8rnR9SfsYqnqmOzbTv8AM%2FYlBTd%2FvXopqtpE97UwwzAxqP1XmBJX%2BC3s3F5bJNewLz2rz%2BN4wen3%2FW2Mko4QRvqi8gYuvNnlgs3awvqmcQAi9yG7JlTcn8JVHGfOjvxH5fdfvQGkqOqvVyFyXfiub8kVB56dPr6CxbL2lsB%2Ff%2F&X-Amz-Signature=c88802e8f08fe195f1e9ad90121f23a5232824158367562390d8dbf3fea37681&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 4. KDE Plot
A Kernel Density Estimate (KDE) plot is a graph that creates a probability distribution curve for the data based upon its likelihood of occurrence on a specific value. This is created for a single vector of information.
**Syntax:**
```python
sns.kdeplot(X) || sns.kdeplot(df['age'])
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0d571213-2a2f-4921-a50b-880847aa05ee/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46666LZQI4T%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T081641Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEN%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC0acSFFdcJBkBgtCkMKuYT7JgVNlIcjrh9zGDe8N7c%2BQIhAJt72p8FDh8iwgNt%2BeCXtItFJQ5dGEsPlvEwxBC%2BYWISKogECOf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyrPDlphDUJRqYUT8Eq3ANF7ypHmU2vCJxmWo%2BgnnMAVrCIHAPb7F6iwasXqrhC0B09mQ6YhiyBxreISxPrSgR8isJ69stXFfw22C0oCtyZszGHY6A6Tt6etQHe1jYPZr6OUzSEq1lUxgR%2F8XV4XXKp1JMUyusBvp4ALlxrJoaDetds7c87B8yIHb3DXUeczmkfLPAaqzA6xrZZL8BEWscV9jVketsz4f3xaLxRgKJnnyugKAONiB%2FGpU1sOqN8QPzfanE996wMsrFXPg6wzW1iPNHzB%2BW5GsSgVrIS9wjQN2j8T4DaadvfxdSS%2BuxnGFFAcSY5OfToQ5vylZm%2BIP24jmxX0T1nfCR3mHjMunu2xvYzJpuYfpoGFYomyptLgNKOD4MDDGkLYXAKei90wkkAG943lIC9tWS1OQ5eIqNEf9f4fd%2FKa4KWkTqSwJDuhKTJRpfnVX%2F%2BXkQ7HlOVbas9%2F1NH6D%2Ba6bbjr5rCwH6n0Hux0vJz3T4fSKGiMObJjv34WcVYIBErRfZfQSOnsN5SbQJ5krZPcdgyS77hMNYgTqRb7phTVCPcb0D%2Bquvl5LY6lXad%2BXV48lv8f441x84McKICmJ8TWMNIGccT1iSrKlGyiJezrj9PS9AJwf%2F7I1HB0BwqbEWSQkMi1DCznPy8BjqkARSmH6Qy7kD50fWTJm%2BaXSQEYtVydEsCkMuIYGvgyzGSXw9aAa8rnR9SfsYqnqmOzbTv8AM%2FYlBTd%2FvXopqtpE97UwwzAxqP1XmBJX%2BC3s3F5bJNewLz2rz%2BN4wen3%2FW2Mko4QRvqi8gYuvNnlgs3awvqmcQAi9yG7JlTcn8JVHGfOjvxH5fdfvQGkqOqvVyFyXfiub8kVB56dPr6CxbL2lsB%2Ff%2F&X-Amz-Signature=426d8912ca998f55b3aa659ab67811be39e0e76e6c3949b5d6b587bf8f2961b9&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/53752550-ef82-4ca9-a01a-09921f0282d0/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46666LZQI4T%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T081641Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEN%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC0acSFFdcJBkBgtCkMKuYT7JgVNlIcjrh9zGDe8N7c%2BQIhAJt72p8FDh8iwgNt%2BeCXtItFJQ5dGEsPlvEwxBC%2BYWISKogECOf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyrPDlphDUJRqYUT8Eq3ANF7ypHmU2vCJxmWo%2BgnnMAVrCIHAPb7F6iwasXqrhC0B09mQ6YhiyBxreISxPrSgR8isJ69stXFfw22C0oCtyZszGHY6A6Tt6etQHe1jYPZr6OUzSEq1lUxgR%2F8XV4XXKp1JMUyusBvp4ALlxrJoaDetds7c87B8yIHb3DXUeczmkfLPAaqzA6xrZZL8BEWscV9jVketsz4f3xaLxRgKJnnyugKAONiB%2FGpU1sOqN8QPzfanE996wMsrFXPg6wzW1iPNHzB%2BW5GsSgVrIS9wjQN2j8T4DaadvfxdSS%2BuxnGFFAcSY5OfToQ5vylZm%2BIP24jmxX0T1nfCR3mHjMunu2xvYzJpuYfpoGFYomyptLgNKOD4MDDGkLYXAKei90wkkAG943lIC9tWS1OQ5eIqNEf9f4fd%2FKa4KWkTqSwJDuhKTJRpfnVX%2F%2BXkQ7HlOVbas9%2F1NH6D%2Ba6bbjr5rCwH6n0Hux0vJz3T4fSKGiMObJjv34WcVYIBErRfZfQSOnsN5SbQJ5krZPcdgyS77hMNYgTqRb7phTVCPcb0D%2Bquvl5LY6lXad%2BXV48lv8f441x84McKICmJ8TWMNIGccT1iSrKlGyiJezrj9PS9AJwf%2F7I1HB0BwqbEWSQkMi1DCznPy8BjqkARSmH6Qy7kD50fWTJm%2BaXSQEYtVydEsCkMuIYGvgyzGSXw9aAa8rnR9SfsYqnqmOzbTv8AM%2FYlBTd%2FvXopqtpE97UwwzAxqP1XmBJX%2BC3s3F5bJNewLz2rz%2BN4wen3%2FW2Mko4QRvqi8gYuvNnlgs3awvqmcQAi9yG7JlTcn8JVHGfOjvxH5fdfvQGkqOqvVyFyXfiub8kVB56dPr6CxbL2lsB%2Ff%2F&X-Amz-Signature=03ced774413e7b5b5409586215807b5eaf652b98ba1b35686d5f6eb52bdbbbac&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
## 4. Correlation Between Variables
Correlation is a statistical measure of the extent to which different variables are interdependent. It indicates how changes in one variable are associated with changes in another variable over time.
### Positive Correlation
Positive correlation indicates that as one variable increases, the other variable also tends to increase.
**Example: Engine Size and Price**
- **Positive Correlation:** Engine size increases, price also increases.
- **Visualization:** Scatter plot with a steep positive slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c7ea9b0-3ef3-4357-a9c3-554fc71b6b15/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662FBSKZID%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T081642Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEN7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCnmAbXGiZljiDAL3AhsZfTFPkk8ujWdpnlywe7DgNVXQIgFmsug%2BpAGvmxCIy%2B6kADrDAg6GMm12Ozs2DsNldwZXEqiAQI5%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDEMr8h4GfoiqwoM8XSrcA7ObHIjl3IaVDbSn4Z2BKzmCRXhRcruxd6LzODCMXlTc2wkrNb%2FNQjzWmmS%2BAV3BgPRY57K4a%2B3GYVHfblngOtpKAZNmWKAMVmjod5zmx8VXPpkL%2BsoGaPvjHuAi%2FwtRwu9KmoGEX9%2BbCy%2FcTU4IuL11q63OeAhDJUn%2BOk6QTZSoLz%2BzC4yCHdmIK2HKAFcxd3Cs4eSFsS3QNjVFwtPNMhORm8rwjxyNXBHiBe0JPpJKYX%2F0B8y5gGBwIN1JI8T6GniQ9yqVs%2BY4P%2Fj6lJdIHPmOghHEgaWKmc6301vADrFUEAGhguC2JPinM7JjlbbKdV9eyN6%2F%2F4ItZ1YeK7tFH%2F6mInAU7j9wUgAMxmd1d%2BRHQMeGP8Hr8Z69NN8OIedsUjTufb%2FrlbZgWeazzu5wWlRLkHDuEiBad8b3DBe9Yhs3FRbjxNOXGvkqNxIm5TBQzchgTUcrUcYMf6Wy3Tp9ceiYvd%2BXR1dMTUDUA5LxRXTrb29hkjSDmUrbIUC5sJXSHisJc36i%2FoGwkMb4rDFFf029zZo6IQzYDj%2F4hCqLgVYJ3yk8Bvv8aXelUy5Awp%2Buik7ZjxxubLKobmC0%2FxA3FKtMgZtPc0WdYLyue7qe0aJkTaGKx1o6UA3ll8WJMPab%2FLwGOqUBN3hT6p%2F3G39JwAEH%2BLhQZP9gE2Zm3uQqOfvlDjwYLoA%2B3QydWlDKcHWsVy29RJtQjIffWOwLJqgKP6gW%2FcgYqVShnFvnvcXlcvaGAMvcHmGOIZ5PeHQqKcB2%2BZalylMOZ4Xrf%2F2%2B1yai%2FZjDIpU5eCT4fP9jjcbJ3cSoiqILjBSiblSqCbp7ko10lflfduQJPj3TlE62d%2FiVhe%2B0f7KMjbnVluk1&X-Amz-Signature=264bef5b0756211949781d49c6bfbf97c8e17d601a8903ca29a95ea86f7ffa5a&X-Amz-SignedHeaders=host&x-id=GetObject)
**Explanation:** When engine size increases, there is a corresponding increase in the price of the vehicle. This positive correlation suggests that larger engines tend to be associated with higher prices in the market.
___
### Negative Correlation
Negative correlation indicates that as one variable increases, the other variable tends to decrease.
**Example: Highway Miles per Gallon and Price**
- **Negative Correlation:** As highway miles per gallon increases, price decreases.
- **Visualization:** Scatter plot with a steep negative slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/10f1f798-9cc4-4df2-a9c1-5a339f554a0b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664P7P3XRH%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T081643Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEN7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIE3p0g8PF%2BRDpIEjUo%2BXh8b1dvyTJLRgaCq3qO%2FiEQx2AiEAntZdEcNUNSxHOklavhDoh%2BHqx2VMWHgl7JPQhEAR9rgqiAQI5%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDIVKFf1oQgNQ20RtIyrcA3u%2BymL3ioRsCBICBOEeQaYzY3N%2Bbbg2RQuso1yr65ZIIihoGaBECwpLCxrUPMjoXanMGHd54TzmZ8dNrV%2FN5ebDHwncLP7Wfvvfk9XIWN904ObZgAv6yvsOAaWlmOXDS0BgcszadkZGP9pEQV7sUL1EW5iLls38fPBSyB0rKpvZ4FGE41lAypbscH%2BbD5LI13otf3dvKf9mffkeFnQpTgDDrjlZ1%2Bg5nsFj1tMWLRFknvxjz9wQNkNYTULJzUoj7D%2BvNwRZ8w3sPOIL6xpLcNYApDubeZMfeOgj7a0QhR9tXSLQ%2FprCChcGa5K9zxZ2Gq%2B4r9UAWZMsz5sK0meHazQGemiH0VVjXMdhio5TNNDhsQwj2FO9oCo1ar%2FP%2BAkfQYvCpD7Msypm3qXWi%2FR4jUarYYrdkUkejLUG3p8%2Bn7rhOXdxkecCh%2BJOJ8YidiD0pIXWIK3KTZi%2FS25Q526wO7MNAgcmfjLqnV6mX0urXQdivHIy%2BQ%2BHpq3jtOrSIBvzjKRMEyx0qKZK2mkZzKpb8J6j%2F6zDpF8NMOUdqH5r6D8ag6Hi%2FL9tbjs8x%2BxoWwdXP%2BeQCFlTUqNOVFyaAfRUOydYxqOFd3%2FTY64lZnGUd93TmQNfoN3IJySwlt0TMO6b%2FLwGOqUBn%2BpYQcZgVqqLvim44oMtk7OUeNdd2g44Z5EPEFN9Xs91BXOGoWjV3OMziuyuAQGd7VpbEnH8x0wbKCstE870sAyiEqCC7ysjXaZ05ToCMvvG1rUnjf1EWJ8KitdJ%2FDrcpT887g6lkAsrbzY%2BTvt4x4UQ4oVwx8yhVnTSvCNdvZJggKw9LdsIn39p2I63%2FVl1zaEBHuWsmURlwoMWSSubuZ6ZG01e&X-Amz-Signature=1355df7f51376c2d6baa8e0887e436c027d54eab09f49d4c44066f8f7398c0a5&X-Amz-SignedHeaders=host&x-id=GetObject)
**Explanation:** When highway miles per gallon increases, the price of the vehicle tends to decrease. This negative correlation suggests that cars with higher fuel efficiency (more miles per gallon) are generally priced lower in the market.
___
### Weak Correlation
Weak correlation indicates a lack of strong relationship between the variables.
**Example: RPM and Price**
- **Weak Correlation:** Low and high RPM values show varied prices, indicating no strong predictive relationship.
- **Visualization:** Scatter plot with no clear trend or slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9f914514-8914-4bf4-ac84-d9e3077f6eb1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662AL43ACI%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T081642Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEN7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCwRvx3A6nsFeHsiV1uekPktuVsNp1XMwpE4q%2F0BJ6VRwIhAPOtg1aD0n5SFr7Fg%2BwJ56KFiRgszsCTmlRdVjxM2E94KogECOf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyNRfjDMUxS%2Fq47JiIq3AM7NDGLB4HToKUXiQvtdpihHG1nZnmEnJV1R6E78cy%2B6ap%2FBoya1CF2hHOfmokcjHnAhAbTz%2BzGZU%2B3hPExgtqaVUEUSPktK4zzcX1ba003nMV0Cvd0mfJb7OFzJyYK6Yma0DWfJT79huxXrLFSbg2b4j1NxDNnrvWhR8dbPiEV2rkv8fUQMLDl3M8Lo4UJ1F7iq44fRRgKzKHh6f8j1YVsABKlavgxtKj7b3k2t6Z%2FWDtsCR3rDFIpFLzQLM4uXbTc%2Bbw5PhgAn8UG2eATPLtg4guGS%2B22NFhHFyjl%2F1qlMjB1QDDO5RJQCPjvP8DZ8uKzYUmBi%2FtWx%2BeCTp4p5T2DqYM7J%2BXBFPbUedkbABQfsl6F04Jw1M7AB6Hw889pj2dNrqxcIGM%2BdS%2BcvNS8iIpv%2FvwKJoSrtv%2BjThVGmAFTSai2L8JEXBy2dSjpKCWmjiqOibtknaERqyB3jkJEla5HDZOg3Ko3OoVpd9%2BDbDynsgVW6hb3hOiP%2BE%2FUxw5oaL54uD8HUPPvxsx4T7V6UL94XAND%2FCZXR1UEQWgXit5mvTq3IK0APm1MhmVbWuwTpvd%2FtsSlDCXHI1QDOMA0pHSg%2B3%2F5wP%2F8ZbTn5V6DifZq9ov722IE24yzX6phLjDjm%2Fy8BjqkAbv%2FZrFn%2FGccM039djZoQHc0GyJvoNO1KYNtCIUUEM8SllbSNlvYURHi8FglP8atoWaFl7XmQOAvP9bKs9%2FzPBu3Sz06F71raBI73t3landt6CUV29wfkxwq5WiUlGEgydsqODqx%2BsjUzqHcDZfMkATHX3%2BDwinTUJycfjzhwxVQMtZEycSjHe3rZi3qeffA%2FMGQCzcLLALfWdI4n3T4ufCyE2hZ&X-Amz-Signature=b5eb644212aceef86b2a19a2d1cd9b468cd356393ff8875d58423330851a82f8&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f18086e5-5b04-4fbf-8309-8944ab20d213/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ULUO2U75%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T081642Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEN7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDDIv%2ByVnA58xDluSi0acHLO13Gayy8%2F76b9aDgsx6PTQIhAN70%2BfVxRE8B2XVmI0gqARa5IXGdJL5mg7WKh80QkiVPKogECOf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxHgD5wUr2ExKWjYmAq3AMRB4xGufnKMrBPi0w8hKXH7uh9bJHrDBtYksvR3y3r%2Far4ec%2Bi8rh4Car5ecmcseXJAuvA%2B52Ht%2Fn62Uzst61eDovgAXcOPKia0%2F4SR5ydabmzIWybbbkc7BXJ57em7apA2BL6S%2Bmj64nXVKKZmNpV19eaAPQlSlFxjbF11y1QG%2FfGbWnq9GtBKacoE6AYlKHBW7SUQQQno56XlDOLTkSFF6%2BITduKYXg4RbZVynlyqbxASooG7XkLPPvF710Ij8%2B%2BA3gfMDAoYkF8ryvbZ5a8KnJi%2FD%2BayMmankZCL8u84nmbSZKSscGdva%2BCQfG%2BWeT88ZjycJET16oXiQ2ROPyCWs8ull5xen9oHH6dypRS0L3cP2Hskbkt49x%2FqND9NghNnpe4lATEiagQs7azwRqlDvzfJQc%2BfIVvwYrZrKBIhJxYpm%2FIejyovzH%2Fw%2FzxfZ%2BJenOuepGDvfzN3AUOHnOY5vH9obizBz0vOnvzxNhquIRBaZTbugAgSdJ%2BqYY7wC9cLGy0XQnagnRMC8V15zpGPhDCIe0Z6OMjCNWPSz3l%2Forl83o9QOAjukRqsNx%2FNm%2BOfxV7%2F%2Fw3UJZKlQNnF5MsDwRSZOJvrDQDb48GDcZfwMHILc28s50icb3OczD3m%2Fy8BjqkAVfB8hUYys7fH9PtbaTLjHSdr8Pt%2F3i%2BaYDJwjVERkatHwuL9P5wuJrXXkKNKrQKd6vx3h7VDQfsKeXJi%2BFQtSYvkSiHzs4nifdPOGlnGWCaRYiLFI9cQiCbaRifKEBCBbNibrGF4DqvGJBWuQRCb7epmw5tV1CUcV%2FXf%2FRfoewIo3Br2fP%2BU8kzs%2FYFO8dyNF%2FPmwQzOkpgPe0um8QMwFRVvbzC&X-Amz-Signature=faaabb773d61371fb3bce73a6f5e7ea3f3d52fd1e81bb14fd338f808f8b99572&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Correlation Plot
Heatmap visualizes correlations among variables. Color scheme indicates Pearson correlation coefficients. Dark red diagonal line shows perfect correlation (value of 1) between variables and themselves.
This heatmap offers overview of variable relationships and their link with price.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cd3b341e-cc1a-45f7-8aec-cdc00436d270/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ULUO2U75%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T081642Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEN7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDDIv%2ByVnA58xDluSi0acHLO13Gayy8%2F76b9aDgsx6PTQIhAN70%2BfVxRE8B2XVmI0gqARa5IXGdJL5mg7WKh80QkiVPKogECOf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxHgD5wUr2ExKWjYmAq3AMRB4xGufnKMrBPi0w8hKXH7uh9bJHrDBtYksvR3y3r%2Far4ec%2Bi8rh4Car5ecmcseXJAuvA%2B52Ht%2Fn62Uzst61eDovgAXcOPKia0%2F4SR5ydabmzIWybbbkc7BXJ57em7apA2BL6S%2Bmj64nXVKKZmNpV19eaAPQlSlFxjbF11y1QG%2FfGbWnq9GtBKacoE6AYlKHBW7SUQQQno56XlDOLTkSFF6%2BITduKYXg4RbZVynlyqbxASooG7XkLPPvF710Ij8%2B%2BA3gfMDAoYkF8ryvbZ5a8KnJi%2FD%2BayMmankZCL8u84nmbSZKSscGdva%2BCQfG%2BWeT88ZjycJET16oXiQ2ROPyCWs8ull5xen9oHH6dypRS0L3cP2Hskbkt49x%2FqND9NghNnpe4lATEiagQs7azwRqlDvzfJQc%2BfIVvwYrZrKBIhJxYpm%2FIejyovzH%2Fw%2FzxfZ%2BJenOuepGDvfzN3AUOHnOY5vH9obizBz0vOnvzxNhquIRBaZTbugAgSdJ%2BqYY7wC9cLGy0XQnagnRMC8V15zpGPhDCIe0Z6OMjCNWPSz3l%2Forl83o9QOAjukRqsNx%2FNm%2BOfxV7%2F%2Fw3UJZKlQNnF5MsDwRSZOJvrDQDb48GDcZfwMHILc28s50icb3OczD3m%2Fy8BjqkAVfB8hUYys7fH9PtbaTLjHSdr8Pt%2F3i%2BaYDJwjVERkatHwuL9P5wuJrXXkKNKrQKd6vx3h7VDQfsKeXJi%2BFQtSYvkSiHzs4nifdPOGlnGWCaRYiLFI9cQiCbaRifKEBCBbNibrGF4DqvGJBWuQRCb7epmw5tV1CUcV%2FXf%2FRfoewIo3Br2fP%2BU8kzs%2FYFO8dyNF%2FPmwQzOkpgPe0um8QMwFRVvbzC&X-Amz-Signature=a7d3c6bda7e533b170b8b96e0afb5233b62853bdf62b4b25ff6f1ed12899ab01&X-Amz-SignedHeaders=host&x-id=GetObject)

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
