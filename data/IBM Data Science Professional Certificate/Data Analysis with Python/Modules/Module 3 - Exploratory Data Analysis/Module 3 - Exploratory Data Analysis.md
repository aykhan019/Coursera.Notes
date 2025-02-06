

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7e6d594d-952e-44b6-97ea-31225882aea6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665WG2ANRE%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T151608Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEcaCXVzLXdlc3QtMiJHMEUCIQCZuMafl64tJ3IrI3IlNUmnamvXe40fmKe9fBGPvDuKSwIgJNGhSgnJsSG8QHxen96cqD9hkQY5Qb0X5Fq%2FXzQyz5wq%2FwMIYBAAGgw2Mzc0MjMxODM4MDUiDEJWkvTw%2BCt60xP6ISrcA2aRP1Z2ANCu5%2BabKDrfWHyNQ1Sp9jWvs4z6TVY6YdfIhmqNXSoSZrvKqQ6oml6BDJZYFrBnjPjLqrPhyzZQUvINTItSCAVntzcDt6%2FiXJie4qaQtHt%2FQ7xyi5F8JMvFIx76Pkna1PMT5DSfUEZu%2BxzDanqbntZUC05Dp%2FRVFGXLA0H9gzemXkug1N8rlz0oPmInZ2VGr%2BixXt7ocAbjXcLlkph5jFUFkS3UUaF%2FbHKuBVKGmuBffAEWo9kR43hfRo2pa48SF92lTYSsw9ys4iPll90z7l7TcV9s5n6JyXBKcYggDxNtPBKyspFyIPr%2Fd8bQJJ%2F345EOmH137l%2FFbdV26JSCmJbxEl3vdKsaMRPDuDgsdjSnmHM9h3vZDDO%2F06kvS8gG%2FhDVVgduiUcMAQ3M5WdJv3n1jzSHHEBRXQ1jJWB%2BDqRJMDajrT4indMVK7My6O3c%2By3RpDq36FYAD%2FmVlNL4%2B09fiWCpoqHHw6TOgaHFOVpsM44KZGoDgQfjnLI5yjhN1JrsttJQTvNrJSg7jOI4UXVFd7SBVz2ptJzDGZECuvhrxrD6FyRBo1ZvoubIWMeaavYgT9wtgVXYP94YXLhh5E7begjtX17YSSRNvbIBLS23E4WQbY%2FPMO%2Bbk70GOqUBHbJbMueteW4KtJN%2FwxnZ7Y3CBTtPXi8mjdvA1ETe4ENqhTIO5b94QYIeBUtktdB%2BwEA7ub4uC%2Bz7D7zRJrFd48mnbq0hErRZl8QLW6Kk7QvhYTQKBZximN7mgvMJgwHF3vfq6m9csSZQ8HwdWcAx0kb01tM922yhdFLyQNfQZc%2FkjJRTw6FLCYmHm1kGVCZ8XzhowNHzdCOLtaAfcg4%2B5z0qxu%2B8&X-Amz-Signature=bd33a8acba3250eb4594c13c35c4d1065bade7445d26b66c6baf34717a48f011&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cbfaed9e-b398-4902-8936-dea058b21def/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665WG2ANRE%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T151608Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEcaCXVzLXdlc3QtMiJHMEUCIQCZuMafl64tJ3IrI3IlNUmnamvXe40fmKe9fBGPvDuKSwIgJNGhSgnJsSG8QHxen96cqD9hkQY5Qb0X5Fq%2FXzQyz5wq%2FwMIYBAAGgw2Mzc0MjMxODM4MDUiDEJWkvTw%2BCt60xP6ISrcA2aRP1Z2ANCu5%2BabKDrfWHyNQ1Sp9jWvs4z6TVY6YdfIhmqNXSoSZrvKqQ6oml6BDJZYFrBnjPjLqrPhyzZQUvINTItSCAVntzcDt6%2FiXJie4qaQtHt%2FQ7xyi5F8JMvFIx76Pkna1PMT5DSfUEZu%2BxzDanqbntZUC05Dp%2FRVFGXLA0H9gzemXkug1N8rlz0oPmInZ2VGr%2BixXt7ocAbjXcLlkph5jFUFkS3UUaF%2FbHKuBVKGmuBffAEWo9kR43hfRo2pa48SF92lTYSsw9ys4iPll90z7l7TcV9s5n6JyXBKcYggDxNtPBKyspFyIPr%2Fd8bQJJ%2F345EOmH137l%2FFbdV26JSCmJbxEl3vdKsaMRPDuDgsdjSnmHM9h3vZDDO%2F06kvS8gG%2FhDVVgduiUcMAQ3M5WdJv3n1jzSHHEBRXQ1jJWB%2BDqRJMDajrT4indMVK7My6O3c%2By3RpDq36FYAD%2FmVlNL4%2B09fiWCpoqHHw6TOgaHFOVpsM44KZGoDgQfjnLI5yjhN1JrsttJQTvNrJSg7jOI4UXVFd7SBVz2ptJzDGZECuvhrxrD6FyRBo1ZvoubIWMeaavYgT9wtgVXYP94YXLhh5E7begjtX17YSSRNvbIBLS23E4WQbY%2FPMO%2Bbk70GOqUBHbJbMueteW4KtJN%2FwxnZ7Y3CBTtPXi8mjdvA1ETe4ENqhTIO5b94QYIeBUtktdB%2BwEA7ub4uC%2Bz7D7zRJrFd48mnbq0hErRZl8QLW6Kk7QvhYTQKBZximN7mgvMJgwHF3vfq6m9csSZQ8HwdWcAx0kb01tM922yhdFLyQNfQZc%2FkjJRTw6FLCYmHm1kGVCZ8XzhowNHzdCOLtaAfcg4%2B5z0qxu%2B8&X-Amz-Signature=18c44720d5170b32534fa5de2359f316bba03968d1341d91aa048ddbc68a7277&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/91181646-b1e0-4433-9711-6259a96a9247/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665WG2ANRE%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T151608Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEcaCXVzLXdlc3QtMiJHMEUCIQCZuMafl64tJ3IrI3IlNUmnamvXe40fmKe9fBGPvDuKSwIgJNGhSgnJsSG8QHxen96cqD9hkQY5Qb0X5Fq%2FXzQyz5wq%2FwMIYBAAGgw2Mzc0MjMxODM4MDUiDEJWkvTw%2BCt60xP6ISrcA2aRP1Z2ANCu5%2BabKDrfWHyNQ1Sp9jWvs4z6TVY6YdfIhmqNXSoSZrvKqQ6oml6BDJZYFrBnjPjLqrPhyzZQUvINTItSCAVntzcDt6%2FiXJie4qaQtHt%2FQ7xyi5F8JMvFIx76Pkna1PMT5DSfUEZu%2BxzDanqbntZUC05Dp%2FRVFGXLA0H9gzemXkug1N8rlz0oPmInZ2VGr%2BixXt7ocAbjXcLlkph5jFUFkS3UUaF%2FbHKuBVKGmuBffAEWo9kR43hfRo2pa48SF92lTYSsw9ys4iPll90z7l7TcV9s5n6JyXBKcYggDxNtPBKyspFyIPr%2Fd8bQJJ%2F345EOmH137l%2FFbdV26JSCmJbxEl3vdKsaMRPDuDgsdjSnmHM9h3vZDDO%2F06kvS8gG%2FhDVVgduiUcMAQ3M5WdJv3n1jzSHHEBRXQ1jJWB%2BDqRJMDajrT4indMVK7My6O3c%2By3RpDq36FYAD%2FmVlNL4%2B09fiWCpoqHHw6TOgaHFOVpsM44KZGoDgQfjnLI5yjhN1JrsttJQTvNrJSg7jOI4UXVFd7SBVz2ptJzDGZECuvhrxrD6FyRBo1ZvoubIWMeaavYgT9wtgVXYP94YXLhh5E7begjtX17YSSRNvbIBLS23E4WQbY%2FPMO%2Bbk70GOqUBHbJbMueteW4KtJN%2FwxnZ7Y3CBTtPXi8mjdvA1ETe4ENqhTIO5b94QYIeBUtktdB%2BwEA7ub4uC%2Bz7D7zRJrFd48mnbq0hErRZl8QLW6Kk7QvhYTQKBZximN7mgvMJgwHF3vfq6m9csSZQ8HwdWcAx0kb01tM922yhdFLyQNfQZc%2FkjJRTw6FLCYmHm1kGVCZ8XzhowNHzdCOLtaAfcg4%2B5z0qxu%2B8&X-Amz-Signature=d648172fe79bfb531b1553f6443a9c3f18594fa5cbc58e81ede5eaebd088363e&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/09aba1c0-0d55-41dd-852a-a04c5b8a3fac/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZGQIUBIK%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T151609Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEcaCXVzLXdlc3QtMiJIMEYCIQDcQupLkravQMeN%2FGdtPIvwSBsKrGQ80xyCZBX%2BdzhFwAIhANDyLt8yu%2FOiHjSBRmC1q9PV52ZMyv9usNlUO%2BiHwgwcKv8DCGAQABoMNjM3NDIzMTgzODA1IgwQhC8uRg4blzKFL%2BUq3AOt%2F4iA4QAqsBuU7v27MoG0YEUJKf6Idl6BmUzeDkke1S7d0ZNhZL%2BTiQe1%2BtD9uDDgi4Hi7UwcFw6jVvvhd03e0hwgZeShgu1IzRkyjcy3sykNN1gZaRR0q74b1WmvH3ZXfUpIaFva9X4QqeqLSqglZNWm8n267oQ5lNm3th2n3e5LgcmI%2BplQXT9XI0kgSHwSA0rxXQIjAGD15JLYPnpOiSYbRu4PpiAQ4w43eQFJMIqm8Lrpq9vgvRDGuicgwn7K89aZrbUR852yowBD1wdoSCkkbUl6IXXL33K0He6E%2FzVLMnJJ9mD1jqDJakUaABrhXbs2IVstBsCuxbQM71MtMkZjGLGQ6a%2F6xNqHgdRfrEH6bWPlVuiOg3y90Ufb4jDIPvSBkBKtvKEtRP2whCraNh3p3C3l%2FUkhTXabsA82eLncNc%2FRDKeVatDmJqu0TH8CX7YtkweYg4wqUVOtNQZTXTheDB39Dnz8BvkO%2Fz%2BrUTuP2hxwuk%2B9LTwTdYVA2LyMYP%2Bkqt90QLri0sUrv2h7qKhjOrntek3sJdw7UoZDV1d%2BeW%2B3XtWEgechA%2Btcf4xXxZKsYGmkHW%2FR252c%2BdG5T%2BefiXcucm6J0nMHa6VqBfQPd%2ByZQASdiJNVnjDFnJO9BjqkAbHN7HElPGRafPVMgIkDG9QsRwhHcrSWzxQ31AfxD9Lkv%2B2huxr8dOYOy%2FmzvZxBwEx9sSD57pxH6GlaWPZVNsVL%2Ba6n%2FvGFXtrmtAh9vTky2u7ujVNjZfFOUDGtSO83UXsurzQCUWqqJoYrG8MjJr%2FpyaGi8juT3mQa0eaYDHZAvxzepnCfjE1q0KLj0Am3fhv7WzMLoXvlMAapKA2rORLfAFuj&X-Amz-Signature=5b5e808f5aa146a40568a61a410481c155a313cacb518454718d0aa3513811cb&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 2. Scatter Plot
Scatter plots present the relationship between two variables in a dataset. It represents data points on a two-dimensional plane. The independent variable or attribute is plotted on the X-axis, while the dependent variable is plotted on the Y-axis.
**Syntax:**
```python
plt.scatter(x, y)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23708af9-659f-4f23-b626-1a4292d7842c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZGQIUBIK%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T151609Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEcaCXVzLXdlc3QtMiJIMEYCIQDcQupLkravQMeN%2FGdtPIvwSBsKrGQ80xyCZBX%2BdzhFwAIhANDyLt8yu%2FOiHjSBRmC1q9PV52ZMyv9usNlUO%2BiHwgwcKv8DCGAQABoMNjM3NDIzMTgzODA1IgwQhC8uRg4blzKFL%2BUq3AOt%2F4iA4QAqsBuU7v27MoG0YEUJKf6Idl6BmUzeDkke1S7d0ZNhZL%2BTiQe1%2BtD9uDDgi4Hi7UwcFw6jVvvhd03e0hwgZeShgu1IzRkyjcy3sykNN1gZaRR0q74b1WmvH3ZXfUpIaFva9X4QqeqLSqglZNWm8n267oQ5lNm3th2n3e5LgcmI%2BplQXT9XI0kgSHwSA0rxXQIjAGD15JLYPnpOiSYbRu4PpiAQ4w43eQFJMIqm8Lrpq9vgvRDGuicgwn7K89aZrbUR852yowBD1wdoSCkkbUl6IXXL33K0He6E%2FzVLMnJJ9mD1jqDJakUaABrhXbs2IVstBsCuxbQM71MtMkZjGLGQ6a%2F6xNqHgdRfrEH6bWPlVuiOg3y90Ufb4jDIPvSBkBKtvKEtRP2whCraNh3p3C3l%2FUkhTXabsA82eLncNc%2FRDKeVatDmJqu0TH8CX7YtkweYg4wqUVOtNQZTXTheDB39Dnz8BvkO%2Fz%2BrUTuP2hxwuk%2B9LTwTdYVA2LyMYP%2Bkqt90QLri0sUrv2h7qKhjOrntek3sJdw7UoZDV1d%2BeW%2B3XtWEgechA%2Btcf4xXxZKsYGmkHW%2FR252c%2BdG5T%2BefiXcucm6J0nMHa6VqBfQPd%2ByZQASdiJNVnjDFnJO9BjqkAbHN7HElPGRafPVMgIkDG9QsRwhHcrSWzxQ31AfxD9Lkv%2B2huxr8dOYOy%2FmzvZxBwEx9sSD57pxH6GlaWPZVNsVL%2Ba6n%2FvGFXtrmtAh9vTky2u7ujVNjZfFOUDGtSO83UXsurzQCUWqqJoYrG8MjJr%2FpyaGi8juT3mQa0eaYDHZAvxzepnCfjE1q0KLj0Am3fhv7WzMLoXvlMAapKA2rORLfAFuj&X-Amz-Signature=a89697fe017e20fc0a91ba412d194ec85e4ad14fdc4249ea581a2d28a117b3d1&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 3. Histogram
A histogram is an important visual representation of data in categorical form. To view the data in a "Binned" form, use the histogram plot with a number of bins required or with the data points that mark the bin edges. The x-axis represents the data bins, and the y-axis represents the number of elements in each bin.
**Syntax:**
```python
plt.hist(x, bins)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/24e4424a-df87-40a1-b63b-195cbdc2e0ab/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZGQIUBIK%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T151609Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEcaCXVzLXdlc3QtMiJIMEYCIQDcQupLkravQMeN%2FGdtPIvwSBsKrGQ80xyCZBX%2BdzhFwAIhANDyLt8yu%2FOiHjSBRmC1q9PV52ZMyv9usNlUO%2BiHwgwcKv8DCGAQABoMNjM3NDIzMTgzODA1IgwQhC8uRg4blzKFL%2BUq3AOt%2F4iA4QAqsBuU7v27MoG0YEUJKf6Idl6BmUzeDkke1S7d0ZNhZL%2BTiQe1%2BtD9uDDgi4Hi7UwcFw6jVvvhd03e0hwgZeShgu1IzRkyjcy3sykNN1gZaRR0q74b1WmvH3ZXfUpIaFva9X4QqeqLSqglZNWm8n267oQ5lNm3th2n3e5LgcmI%2BplQXT9XI0kgSHwSA0rxXQIjAGD15JLYPnpOiSYbRu4PpiAQ4w43eQFJMIqm8Lrpq9vgvRDGuicgwn7K89aZrbUR852yowBD1wdoSCkkbUl6IXXL33K0He6E%2FzVLMnJJ9mD1jqDJakUaABrhXbs2IVstBsCuxbQM71MtMkZjGLGQ6a%2F6xNqHgdRfrEH6bWPlVuiOg3y90Ufb4jDIPvSBkBKtvKEtRP2whCraNh3p3C3l%2FUkhTXabsA82eLncNc%2FRDKeVatDmJqu0TH8CX7YtkweYg4wqUVOtNQZTXTheDB39Dnz8BvkO%2Fz%2BrUTuP2hxwuk%2B9LTwTdYVA2LyMYP%2Bkqt90QLri0sUrv2h7qKhjOrntek3sJdw7UoZDV1d%2BeW%2B3XtWEgechA%2Btcf4xXxZKsYGmkHW%2FR252c%2BdG5T%2BefiXcucm6J0nMHa6VqBfQPd%2ByZQASdiJNVnjDFnJO9BjqkAbHN7HElPGRafPVMgIkDG9QsRwhHcrSWzxQ31AfxD9Lkv%2B2huxr8dOYOy%2FmzvZxBwEx9sSD57pxH6GlaWPZVNsVL%2Ba6n%2FvGFXtrmtAh9vTky2u7ujVNjZfFOUDGtSO83UXsurzQCUWqqJoYrG8MjJr%2FpyaGi8juT3mQa0eaYDHZAvxzepnCfjE1q0KLj0Am3fhv7WzMLoXvlMAapKA2rORLfAFuj&X-Amz-Signature=2d55ff36c381b3e2eeb51cf16d91fcd7a620dd4595a7985cd7bac800b6d96f78&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ab5a6dfe-51f5-43ee-bcb3-33dae4a1c7ad/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZGQIUBIK%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T151609Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEcaCXVzLXdlc3QtMiJIMEYCIQDcQupLkravQMeN%2FGdtPIvwSBsKrGQ80xyCZBX%2BdzhFwAIhANDyLt8yu%2FOiHjSBRmC1q9PV52ZMyv9usNlUO%2BiHwgwcKv8DCGAQABoMNjM3NDIzMTgzODA1IgwQhC8uRg4blzKFL%2BUq3AOt%2F4iA4QAqsBuU7v27MoG0YEUJKf6Idl6BmUzeDkke1S7d0ZNhZL%2BTiQe1%2BtD9uDDgi4Hi7UwcFw6jVvvhd03e0hwgZeShgu1IzRkyjcy3sykNN1gZaRR0q74b1WmvH3ZXfUpIaFva9X4QqeqLSqglZNWm8n267oQ5lNm3th2n3e5LgcmI%2BplQXT9XI0kgSHwSA0rxXQIjAGD15JLYPnpOiSYbRu4PpiAQ4w43eQFJMIqm8Lrpq9vgvRDGuicgwn7K89aZrbUR852yowBD1wdoSCkkbUl6IXXL33K0He6E%2FzVLMnJJ9mD1jqDJakUaABrhXbs2IVstBsCuxbQM71MtMkZjGLGQ6a%2F6xNqHgdRfrEH6bWPlVuiOg3y90Ufb4jDIPvSBkBKtvKEtRP2whCraNh3p3C3l%2FUkhTXabsA82eLncNc%2FRDKeVatDmJqu0TH8CX7YtkweYg4wqUVOtNQZTXTheDB39Dnz8BvkO%2Fz%2BrUTuP2hxwuk%2B9LTwTdYVA2LyMYP%2Bkqt90QLri0sUrv2h7qKhjOrntek3sJdw7UoZDV1d%2BeW%2B3XtWEgechA%2Btcf4xXxZKsYGmkHW%2FR252c%2BdG5T%2BefiXcucm6J0nMHa6VqBfQPd%2ByZQASdiJNVnjDFnJO9BjqkAbHN7HElPGRafPVMgIkDG9QsRwhHcrSWzxQ31AfxD9Lkv%2B2huxr8dOYOy%2FmzvZxBwEx9sSD57pxH6GlaWPZVNsVL%2Ba6n%2FvGFXtrmtAh9vTky2u7ujVNjZfFOUDGtSO83UXsurzQCUWqqJoYrG8MjJr%2FpyaGi8juT3mQa0eaYDHZAvxzepnCfjE1q0KLj0Am3fhv7WzMLoXvlMAapKA2rORLfAFuj&X-Amz-Signature=402064321cfed07d28c74261fe1a956f531c2ea92097dec67f9c1322daf1a584&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8f1b1d60-cf1b-42b3-9faa-f634c89c3f84/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZGQIUBIK%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T151609Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEcaCXVzLXdlc3QtMiJIMEYCIQDcQupLkravQMeN%2FGdtPIvwSBsKrGQ80xyCZBX%2BdzhFwAIhANDyLt8yu%2FOiHjSBRmC1q9PV52ZMyv9usNlUO%2BiHwgwcKv8DCGAQABoMNjM3NDIzMTgzODA1IgwQhC8uRg4blzKFL%2BUq3AOt%2F4iA4QAqsBuU7v27MoG0YEUJKf6Idl6BmUzeDkke1S7d0ZNhZL%2BTiQe1%2BtD9uDDgi4Hi7UwcFw6jVvvhd03e0hwgZeShgu1IzRkyjcy3sykNN1gZaRR0q74b1WmvH3ZXfUpIaFva9X4QqeqLSqglZNWm8n267oQ5lNm3th2n3e5LgcmI%2BplQXT9XI0kgSHwSA0rxXQIjAGD15JLYPnpOiSYbRu4PpiAQ4w43eQFJMIqm8Lrpq9vgvRDGuicgwn7K89aZrbUR852yowBD1wdoSCkkbUl6IXXL33K0He6E%2FzVLMnJJ9mD1jqDJakUaABrhXbs2IVstBsCuxbQM71MtMkZjGLGQ6a%2F6xNqHgdRfrEH6bWPlVuiOg3y90Ufb4jDIPvSBkBKtvKEtRP2whCraNh3p3C3l%2FUkhTXabsA82eLncNc%2FRDKeVatDmJqu0TH8CX7YtkweYg4wqUVOtNQZTXTheDB39Dnz8BvkO%2Fz%2BrUTuP2hxwuk%2B9LTwTdYVA2LyMYP%2Bkqt90QLri0sUrv2h7qKhjOrntek3sJdw7UoZDV1d%2BeW%2B3XtWEgechA%2Btcf4xXxZKsYGmkHW%2FR252c%2BdG5T%2BefiXcucm6J0nMHa6VqBfQPd%2ByZQASdiJNVnjDFnJO9BjqkAbHN7HElPGRafPVMgIkDG9QsRwhHcrSWzxQ31AfxD9Lkv%2B2huxr8dOYOy%2FmzvZxBwEx9sSD57pxH6GlaWPZVNsVL%2Ba6n%2FvGFXtrmtAh9vTky2u7ujVNjZfFOUDGtSO83UXsurzQCUWqqJoYrG8MjJr%2FpyaGi8juT3mQa0eaYDHZAvxzepnCfjE1q0KLj0Am3fhv7WzMLoXvlMAapKA2rORLfAFuj&X-Amz-Signature=5ccfd4736e98c18f1e134d7e40b03e3e7ec50489b550a84219eb775720225c63&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/13ad0497-05fe-4eaa-984e-707b33e14761/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZGQIUBIK%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T151610Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEcaCXVzLXdlc3QtMiJIMEYCIQDcQupLkravQMeN%2FGdtPIvwSBsKrGQ80xyCZBX%2BdzhFwAIhANDyLt8yu%2FOiHjSBRmC1q9PV52ZMyv9usNlUO%2BiHwgwcKv8DCGAQABoMNjM3NDIzMTgzODA1IgwQhC8uRg4blzKFL%2BUq3AOt%2F4iA4QAqsBuU7v27MoG0YEUJKf6Idl6BmUzeDkke1S7d0ZNhZL%2BTiQe1%2BtD9uDDgi4Hi7UwcFw6jVvvhd03e0hwgZeShgu1IzRkyjcy3sykNN1gZaRR0q74b1WmvH3ZXfUpIaFva9X4QqeqLSqglZNWm8n267oQ5lNm3th2n3e5LgcmI%2BplQXT9XI0kgSHwSA0rxXQIjAGD15JLYPnpOiSYbRu4PpiAQ4w43eQFJMIqm8Lrpq9vgvRDGuicgwn7K89aZrbUR852yowBD1wdoSCkkbUl6IXXL33K0He6E%2FzVLMnJJ9mD1jqDJakUaABrhXbs2IVstBsCuxbQM71MtMkZjGLGQ6a%2F6xNqHgdRfrEH6bWPlVuiOg3y90Ufb4jDIPvSBkBKtvKEtRP2whCraNh3p3C3l%2FUkhTXabsA82eLncNc%2FRDKeVatDmJqu0TH8CX7YtkweYg4wqUVOtNQZTXTheDB39Dnz8BvkO%2Fz%2BrUTuP2hxwuk%2B9LTwTdYVA2LyMYP%2Bkqt90QLri0sUrv2h7qKhjOrntek3sJdw7UoZDV1d%2BeW%2B3XtWEgechA%2Btcf4xXxZKsYGmkHW%2FR252c%2BdG5T%2BefiXcucm6J0nMHa6VqBfQPd%2ByZQASdiJNVnjDFnJO9BjqkAbHN7HElPGRafPVMgIkDG9QsRwhHcrSWzxQ31AfxD9Lkv%2B2huxr8dOYOy%2FmzvZxBwEx9sSD57pxH6GlaWPZVNsVL%2Ba6n%2FvGFXtrmtAh9vTky2u7ujVNjZfFOUDGtSO83UXsurzQCUWqqJoYrG8MjJr%2FpyaGi8juT3mQa0eaYDHZAvxzepnCfjE1q0KLj0Am3fhv7WzMLoXvlMAapKA2rORLfAFuj&X-Amz-Signature=28d980141e79a6c374fb54bd2a1b69031a5421a377472a3f3b486bdab59c9ab9&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 2. Box and Whisker Plot
A box plot shows the distribution of quantitative data in a way that facilitates comparisons between variables or across levels of a categorical variable. The box shows the quartiles of the dataset while the whiskers extend to show the rest of the distribution, except for points that are determined to be "outliers".
**Syntax:**
```python
sns.boxplot(x='header_1', y='header_2', data=df)
```
**Example Output:**


![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d207ae92-0a7c-4e2f-aa65-0ee5a2c33bf7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R2CDIV2L%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T151612Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEcaCXVzLXdlc3QtMiJGMEQCIFZ5kC88BVxSasHJLzv6PM4CRyJTzolOkaHuFOjuMkksAiA5hgDT2uHsEOoQ3OjZR57SBJZXj4ZISGtwdjh2Hm8G4Cr%2FAwhgEAAaDDYzNzQyMzE4MzgwNSIMqcxJ%2BJlZs%2B5rwxRWKtwDj%2FYukTDIJImasXhdFm58a0LSUam0s9ujMk4WT9oL2kKjE6zq%2FV93E32P397j2U%2B%2FakZ%2BQRqYce6QJTX7XLuKT86EM3OGIoP%2BW1DrMi0%2BiUY3MVwJlcYJL1lH7hKoqu%2FkzNrQLzdAI4zKmiss5L2mjNIeQPynH6UvO4r%2BNNxWM5VhUF7Gmyvj5SLGs%2FqtKxOBt2H5WbZ34iS5ccoe2sfCRF7Vcqqu%2FP7%2FkIvrRDwrRqXcDYEuhzBUKdhrbVvUaCmXO6I5%2BjDaspjInWPP%2Bw9n9ik6r6HnvJvAI2RX6T7ecCKmH0dB09GAIAg3PYEu05W%2BYvvFcRqlfys%2BJ6nTX3GeW9y8RqG5OuaiDW6EuX5I5iAqrzIkrcM4LdAmgtV1y0ZzioZXK4Eojx3tpj1zbdrKt9oUi3TDjG33JWaamZsmNadNOMSbkiJAPTriorxR%2BIWUgffWGc%2BIiU32A33SnNO33YOmLEXov8gtblFqxeotdENtCkpLZF1YwBExsVvel%2BzbLgb6JcjotCudUW%2BJoGuLiFG%2BNE5MaBKust%2BtfrUYUIQdfbAxRmxR%2BzJmOmH1vF3um7DfQVZmzjil3qcG0WGg9zW259L2krvVy3PKCW11ORVnVpcHO5JYIbgQP5wwjZyTvQY6pgHvwZbSZ%2Fs5oa%2FjEYJxUIgzf0E%2FzvrUYP4h2tVBvPZG9CUZWOjCOfinF4RdQTe2nqfaJKXUleTwuUz83Lij%2FsPpYNwfsxz1jgE23hq0FR%2FE9eEb0rWHEeHBBdkwPu%2FM186EQF93Oh0yC4VP7OHN2pN3sUQAjUAzX690MoEjfSgTi4xOMq0HHwQr4rTxy2wy1tX97BEC7V56YYqG4foTLM%2F7bcPGCNq4&X-Amz-Signature=52827700dd44f79700ce3a2db5dbbcda688a9925e7f00f8e9a7875f0a9b48009&X-Amz-SignedHeaders=host&x-id=GetObject)

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0e516edc-7551-4792-ab18-0494db3c4c0c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VSSRMZAB%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T151612Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEcaCXVzLXdlc3QtMiJHMEUCIQDWkoNxIacFgD8FqgL18bJ2jZ9XmVeusl2NGd9nBqd%2FYwIgbxA5BYu%2FAczRVHofZcxVAP4vXUYazAimGvKFd3zKjNEq%2FwMIYBAAGgw2Mzc0MjMxODM4MDUiDBEro4JKPbQE25%2Bo0SrcA9Ew0qlaQCeow1bjCxrzWmqXk99419enuqsFf68IwblB7Cad2zb3iAQhk2znw7dqK%2B1H2DSAPc8ssAVHEGyd0Lbse%2BXdr4Gw8j9kuLhqcYRuGeSy9VKL4eY9XtEM8Gj8LNZpwBp4bjCP4W4ZKySpH1mlevYXMG0%2F9BMUHIzGnRhl%2FUuEcq37dJjkkhgcKynerOKzWhnLng97RZpKn81803%2BTIfgygBzw0SkjfTeuXb3n0iKkck2KGGqSMyN4CdGaQYUxPWgM5ffAEISIaCPCvSO%2F3o%2BwlAJJqgK9zUXZyknBMTqE%2FYu8JO5tGwS%2BqBVtgVYcenjEN80bdZxxiDPD5gTm92t29DSBQQZQQBNxq6SExlLkyOPy2s57v6eBHkdrU5KvuSnobUTPQB9VAFzHTC%2BQEu3WhAfr82iwjpp0TRIhU8jQC0zJWGl3R%2FmjrmjiHWfRxgtbQCYETWuMf%2FiDAeMVQKiil1ml2kQjid3lBpxFxOBuq84qkoFeopEzhJ97E70M%2FTIhtl%2Fh%2BkLQZ17p0vfADB9mPml551pb%2FYZD%2FBbEyZ53HngMpwxY%2BvAWT7IDjtT9yB2Fo9tnp%2FlyaDbfRLTu%2FUogUZ2hA%2BF9RUZLXGDesDoWVwCxbA9hZc1LMOubk70GOqUBqkRQcqOGkF58l8mmil2jGzj6AFo4PMXThSY%2FCxQVR4zyXsNVEswAiOuzJS73useuF4POu8Gmcm11sBpTkOmaWy1laQh1hbcw52IbCCataB0MXKcU4QBBFEHu4uxaw9zItC%2BfTaYjRsG%2FvYBhkJDZ1rM6XoqjPdg6agnzTuZMYoeBymDU3YT%2B5hW8GmF%2BDHfRaSJdOGj9Vjb28zM51NptJFMinhT2&X-Amz-Signature=935b734eb72a7e71d1bd071f7091dcb14e925de2456a24429bace64cea3c544b&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23a79b9d-2356-49a9-8fd9-65c6b0ab2cc5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZGQIUBIK%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T151610Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEcaCXVzLXdlc3QtMiJIMEYCIQDcQupLkravQMeN%2FGdtPIvwSBsKrGQ80xyCZBX%2BdzhFwAIhANDyLt8yu%2FOiHjSBRmC1q9PV52ZMyv9usNlUO%2BiHwgwcKv8DCGAQABoMNjM3NDIzMTgzODA1IgwQhC8uRg4blzKFL%2BUq3AOt%2F4iA4QAqsBuU7v27MoG0YEUJKf6Idl6BmUzeDkke1S7d0ZNhZL%2BTiQe1%2BtD9uDDgi4Hi7UwcFw6jVvvhd03e0hwgZeShgu1IzRkyjcy3sykNN1gZaRR0q74b1WmvH3ZXfUpIaFva9X4QqeqLSqglZNWm8n267oQ5lNm3th2n3e5LgcmI%2BplQXT9XI0kgSHwSA0rxXQIjAGD15JLYPnpOiSYbRu4PpiAQ4w43eQFJMIqm8Lrpq9vgvRDGuicgwn7K89aZrbUR852yowBD1wdoSCkkbUl6IXXL33K0He6E%2FzVLMnJJ9mD1jqDJakUaABrhXbs2IVstBsCuxbQM71MtMkZjGLGQ6a%2F6xNqHgdRfrEH6bWPlVuiOg3y90Ufb4jDIPvSBkBKtvKEtRP2whCraNh3p3C3l%2FUkhTXabsA82eLncNc%2FRDKeVatDmJqu0TH8CX7YtkweYg4wqUVOtNQZTXTheDB39Dnz8BvkO%2Fz%2BrUTuP2hxwuk%2B9LTwTdYVA2LyMYP%2Bkqt90QLri0sUrv2h7qKhjOrntek3sJdw7UoZDV1d%2BeW%2B3XtWEgechA%2Btcf4xXxZKsYGmkHW%2FR252c%2BdG5T%2BefiXcucm6J0nMHa6VqBfQPd%2ByZQASdiJNVnjDFnJO9BjqkAbHN7HElPGRafPVMgIkDG9QsRwhHcrSWzxQ31AfxD9Lkv%2B2huxr8dOYOy%2FmzvZxBwEx9sSD57pxH6GlaWPZVNsVL%2Ba6n%2FvGFXtrmtAh9vTky2u7ujVNjZfFOUDGtSO83UXsurzQCUWqqJoYrG8MjJr%2FpyaGi8juT3mQa0eaYDHZAvxzepnCfjE1q0KLj0Am3fhv7WzMLoXvlMAapKA2rORLfAFuj&X-Amz-Signature=a5ec851c19526631cf2926d3abe6d781536ab2d8fd3ead5fcac9837fcc1fa3d7&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 4. KDE Plot
A Kernel Density Estimate (KDE) plot is a graph that creates a probability distribution curve for the data based upon its likelihood of occurrence on a specific value. This is created for a single vector of information.
**Syntax:**
```python
sns.kdeplot(X) || sns.kdeplot(df['age'])
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0d571213-2a2f-4921-a50b-880847aa05ee/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZGQIUBIK%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T151610Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEcaCXVzLXdlc3QtMiJIMEYCIQDcQupLkravQMeN%2FGdtPIvwSBsKrGQ80xyCZBX%2BdzhFwAIhANDyLt8yu%2FOiHjSBRmC1q9PV52ZMyv9usNlUO%2BiHwgwcKv8DCGAQABoMNjM3NDIzMTgzODA1IgwQhC8uRg4blzKFL%2BUq3AOt%2F4iA4QAqsBuU7v27MoG0YEUJKf6Idl6BmUzeDkke1S7d0ZNhZL%2BTiQe1%2BtD9uDDgi4Hi7UwcFw6jVvvhd03e0hwgZeShgu1IzRkyjcy3sykNN1gZaRR0q74b1WmvH3ZXfUpIaFva9X4QqeqLSqglZNWm8n267oQ5lNm3th2n3e5LgcmI%2BplQXT9XI0kgSHwSA0rxXQIjAGD15JLYPnpOiSYbRu4PpiAQ4w43eQFJMIqm8Lrpq9vgvRDGuicgwn7K89aZrbUR852yowBD1wdoSCkkbUl6IXXL33K0He6E%2FzVLMnJJ9mD1jqDJakUaABrhXbs2IVstBsCuxbQM71MtMkZjGLGQ6a%2F6xNqHgdRfrEH6bWPlVuiOg3y90Ufb4jDIPvSBkBKtvKEtRP2whCraNh3p3C3l%2FUkhTXabsA82eLncNc%2FRDKeVatDmJqu0TH8CX7YtkweYg4wqUVOtNQZTXTheDB39Dnz8BvkO%2Fz%2BrUTuP2hxwuk%2B9LTwTdYVA2LyMYP%2Bkqt90QLri0sUrv2h7qKhjOrntek3sJdw7UoZDV1d%2BeW%2B3XtWEgechA%2Btcf4xXxZKsYGmkHW%2FR252c%2BdG5T%2BefiXcucm6J0nMHa6VqBfQPd%2ByZQASdiJNVnjDFnJO9BjqkAbHN7HElPGRafPVMgIkDG9QsRwhHcrSWzxQ31AfxD9Lkv%2B2huxr8dOYOy%2FmzvZxBwEx9sSD57pxH6GlaWPZVNsVL%2Ba6n%2FvGFXtrmtAh9vTky2u7ujVNjZfFOUDGtSO83UXsurzQCUWqqJoYrG8MjJr%2FpyaGi8juT3mQa0eaYDHZAvxzepnCfjE1q0KLj0Am3fhv7WzMLoXvlMAapKA2rORLfAFuj&X-Amz-Signature=aecf6d52d944f3f1e12d68e0b6785f6c8da1265423f7cdb69ee08452364ca45c&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/53752550-ef82-4ca9-a01a-09921f0282d0/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZGQIUBIK%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T151610Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEcaCXVzLXdlc3QtMiJIMEYCIQDcQupLkravQMeN%2FGdtPIvwSBsKrGQ80xyCZBX%2BdzhFwAIhANDyLt8yu%2FOiHjSBRmC1q9PV52ZMyv9usNlUO%2BiHwgwcKv8DCGAQABoMNjM3NDIzMTgzODA1IgwQhC8uRg4blzKFL%2BUq3AOt%2F4iA4QAqsBuU7v27MoG0YEUJKf6Idl6BmUzeDkke1S7d0ZNhZL%2BTiQe1%2BtD9uDDgi4Hi7UwcFw6jVvvhd03e0hwgZeShgu1IzRkyjcy3sykNN1gZaRR0q74b1WmvH3ZXfUpIaFva9X4QqeqLSqglZNWm8n267oQ5lNm3th2n3e5LgcmI%2BplQXT9XI0kgSHwSA0rxXQIjAGD15JLYPnpOiSYbRu4PpiAQ4w43eQFJMIqm8Lrpq9vgvRDGuicgwn7K89aZrbUR852yowBD1wdoSCkkbUl6IXXL33K0He6E%2FzVLMnJJ9mD1jqDJakUaABrhXbs2IVstBsCuxbQM71MtMkZjGLGQ6a%2F6xNqHgdRfrEH6bWPlVuiOg3y90Ufb4jDIPvSBkBKtvKEtRP2whCraNh3p3C3l%2FUkhTXabsA82eLncNc%2FRDKeVatDmJqu0TH8CX7YtkweYg4wqUVOtNQZTXTheDB39Dnz8BvkO%2Fz%2BrUTuP2hxwuk%2B9LTwTdYVA2LyMYP%2Bkqt90QLri0sUrv2h7qKhjOrntek3sJdw7UoZDV1d%2BeW%2B3XtWEgechA%2Btcf4xXxZKsYGmkHW%2FR252c%2BdG5T%2BefiXcucm6J0nMHa6VqBfQPd%2ByZQASdiJNVnjDFnJO9BjqkAbHN7HElPGRafPVMgIkDG9QsRwhHcrSWzxQ31AfxD9Lkv%2B2huxr8dOYOy%2FmzvZxBwEx9sSD57pxH6GlaWPZVNsVL%2Ba6n%2FvGFXtrmtAh9vTky2u7ujVNjZfFOUDGtSO83UXsurzQCUWqqJoYrG8MjJr%2FpyaGi8juT3mQa0eaYDHZAvxzepnCfjE1q0KLj0Am3fhv7WzMLoXvlMAapKA2rORLfAFuj&X-Amz-Signature=dce89a81029848f5ebd5c5c0d77b2e62c7e7d1de6b91de236a5c88ab49ccf398&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
## 4. Correlation Between Variables
Correlation is a statistical measure of the extent to which different variables are interdependent. It indicates how changes in one variable are associated with changes in another variable over time.
### Positive Correlation
Positive correlation indicates that as one variable increases, the other variable also tends to increase.
**Example: Engine Size and Price**
- **Positive Correlation:** Engine size increases, price also increases.
- **Visualization:** Scatter plot with a steep positive slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c7ea9b0-3ef3-4357-a9c3-554fc71b6b15/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XYXIHWJX%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T151612Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEcaCXVzLXdlc3QtMiJIMEYCIQCGANUKS%2FzucVMDL0FYscLikayJKkWqu%2FxFCbaDwHffwAIhAMCBzpKDKsUPTVnlLICNlpENX2DpT%2FxVBPSZbM8sS2EpKv8DCGAQABoMNjM3NDIzMTgzODA1IgxypbDci%2FvlQVGVFU8q3APVZ9nYOjBGBZ%2F%2BDGo6MvUbv9tiH72CWjdDX%2BclE4RlWr4kOp8Gtl15eHPJsMO40EbZyLz7Ex5dz2FhD1yCCvLWCF4eef8LlQ5h7eO7ZeH%2BeWo%2FXEzLUH4A%2BVHzJPkVF4Bm1tTQVeYW7XX45PKMTXHgVxPFA8GJBcMFW10cX4ehYgjxTnJ%2B6DNb71oIHFXgVTDb3Jfd1aysj2L1cLZxVsG4jmlU6ns8lFCGy%2Bhv4ifXmpCC%2FyQikrGypbns%2Bq8Fmqe7kcpcz3ebqLXgvMciazejJh7UKyVlrOIWuTuhTOzBWt1o4W6dxyJ6fCX6i4z5GD3kCProlzsGfzEvzR8CTs19iJLYwG12uIpvzitlJNbVAD%2BpyGKXgqbIp9788BQb%2Fu0g90u2Om4D6t0GAk1lBP78LBNC132XB0kXOiDa7Pt77UP24Aui43LhZA%2FLFpIUhSE20UnR955DajNakkKWkXEhSsAHkNagonBzH3FT9UMzrotWhgKnoiSnlGkW1T7fpCsE774D9r3jvNW1Z2CCERWhwKBKRD4rzEvmfM9Jb%2Bj%2FeA9DkmL3gj9Jj9SwQwEuLDwC4x1nX2PXT%2Bs%2F%2FCockgv6jAKAZq2eeKS5Ai0JoJvU6S4wCPN3%2FmJvcsswnDDcnJO9BjqkATgQKnxo6pXF9bGZjxZrmcIWsSuoFWaJHzNXherSdcUFCaoiRZa8Tqj8Zec1oz4YW%2FGcODU1TT%2FZ3M%2FqrJ1%2F8tpniFjN%2FUOjYTQR96YCmY%2F1ccC3rzlabTIK2kOypsWxlaJ%2Bw7091OMRUh0LDQ5h%2BKj0IN3vBcgSkVrLQFs8RrlVnMwLXPJEe5jxOf5NwaRSyVjy13Q8olr16%2BurHasd1deyHcKN&X-Amz-Signature=44813f3c919d1b9e32637dcfc225eff02660957d1db2b2504eeb160f25933321&X-Amz-SignedHeaders=host&x-id=GetObject)
**Explanation:** When engine size increases, there is a corresponding increase in the price of the vehicle. This positive correlation suggests that larger engines tend to be associated with higher prices in the market.
___
### Negative Correlation
Negative correlation indicates that as one variable increases, the other variable tends to decrease.
**Example: Highway Miles per Gallon and Price**
- **Negative Correlation:** As highway miles per gallon increases, price decreases.
- **Visualization:** Scatter plot with a steep negative slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/10f1f798-9cc4-4df2-a9c1-5a339f554a0b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TIOMKQNU%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T151612Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEcaCXVzLXdlc3QtMiJGMEQCIBz0vD7lf%2BEOA824q621Nl%2BWdfolNcP98SUH6b3FnwJTAiBf2zYhcpHmWSBYtkjpR15WulcMx6dUb7vjQacWMbL4%2BSr%2FAwhgEAAaDDYzNzQyMzE4MzgwNSIMg9S7ei31TooVGhl4KtwDQYRnCSfIW%2FX3laRpLwnEMYRv1J8apW8ZQDh9ZPFOn5wZnDVf%2FE9o%2B%2BPAcMqW4x5I%2BrfjjVgK8Vi%2FKMjRsLaicI8%2BrDPwjJLMqfl07pRfqPBObTZ%2FGsOV560ZK9zKS87eNNJ1Q8MANdRHwit%2Bka2cEIxJB7JaaTbood85X0oSnXRh2EZdMQyx9ppPS5gj9seRCp3tOD0ZMfwXqXCefhN2JZSVVsDfOU7wDm0FcYmWX18nt6fXGIg4XobLPr2HN%2FeheMu4zP0eZYAi5xzXApMpPwCbeGhHseLxEBflO5eZecZN%2F%2Bt49LFKTsTR2n3kR6xy5Wjx0c1jHk%2BZ%2BNT1aZV9ulz8fcmf4NGoyppZZgD%2FTXM4yTc8Ai0lxAb1hHW2TwvGR6Zbtv2Wl2uTPcWnuvo2N83y8bO7U53POslszd9lQ5ICd50pmVWT2rOG2BLXbb2RtiXvve4O5anPlmdGaLm%2BVdykTU1a4EHCpRSjP%2F5S13FeXJh4i4rg9JsnzNOfhllicaV0Bj3uoFowqx0VhipJrW0gjoypQy6bSetettHBq5RfG4eELbV31qEVrM91b%2F%2BenGsndUTehYHcaUyggKq%2FIUsVbGsNp%2BeJWTr742iN2puk5sJMRPcI5V2mVzwwxpyTvQY6pgFgg46kKXHwL%2B%2FmR%2Bvm9Zr%2BfA4SK00unG1CXFMvXQD%2FYe9f4v437RfF8O56ycuT%2BGUAvikjhfV0TR3YI3yjPWAEYBjoyYLptDEgDj4rRW56uXTSoC%2F2J1n%2FdJZFL1n%2ByGgykp4QiOU4r0bQfz%2Bgnv5Aru3tWSEzM34PO%2FOsgjh%2FsOu7ZeXzP96G2r7H6xB3yBo24Ns2VxBYeUi2NB7jY2GgaEupd%2Bvc&X-Amz-Signature=b94338616bccc81d4a43d404496835167077040728d6e64a7dc69d96a41f6e1c&X-Amz-SignedHeaders=host&x-id=GetObject)
**Explanation:** When highway miles per gallon increases, the price of the vehicle tends to decrease. This negative correlation suggests that cars with higher fuel efficiency (more miles per gallon) are generally priced lower in the market.
___
### Weak Correlation
Weak correlation indicates a lack of strong relationship between the variables.
**Example: RPM and Price**
- **Weak Correlation:** Low and high RPM values show varied prices, indicating no strong predictive relationship.
- **Visualization:** Scatter plot with no clear trend or slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9f914514-8914-4bf4-ac84-d9e3077f6eb1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666RO3SN22%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T151612Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEcaCXVzLXdlc3QtMiJIMEYCIQDFtWBu%2BUYiSNmtjFu6WzuGvVYbSEMv3wNTqQ8Yy02rgQIhAMf6YSgdj1nBNqEVe%2FaPr377eLDisr6zyvdVd8DR%2BL12Kv8DCGAQABoMNjM3NDIzMTgzODA1Igy4HUBFATtKEnA%2Fiqcq3ANZLmKNHNnKTXHr2b5VaITeu4dILuluuBGVWPhJOuf9Nctr%2FuS0Tu67LF8xbTTBgLOikq%2FePaEqBQVfO1vHUa%2FU%2BtYQszjb6RGGwh1sR6Lwb5gkbVkxRg8RYVMxeMUkUk5VWDbRwZ%2FZZoym0TTUk01L87cEvMSXimc70I5NZQTcf4KAKeuhllUH8d5wdbKKkShjrEidBRBiiLB%2FkvXg98Sfh7uyMugfARAAgpE%2B2oMaHEYt5xlycH0rnYr14bSqv8i%2B%2FrpdKnXBQRITosOHZ%2BNgWjEQmRrlyM0eexrBr9ofjOU25OOQ6rQD63H0qxqoQ%2Fu3l%2B2tKw0IyESOx84xXKI%2BVZ3nioQw2AgJCKLm5QbAwtXzQVKMoYpPKdOviWFsID0pvoPpRd5JwZGPc5%2BN4OmnQ0ot%2Bh16yX2pkxi%2Fv8oZWp63zJgCAelmvxIXEAz7Pa6yntNZACkBkVELhGK6TSb5Pfn3MojYUM%2Blpq8Igh6pKtpzhGaKWH1u2HqKuzbVGIuv1NihUVQcHoO1B7MgqPvGs3j39rSXjPvgCPnk8Cc7f%2FzHwezwW%2B5DwV4TiU217RjWUgsohTi8kHReIyqWfRMQ906eXPPB3kydsHmg8Isa5pgW81ILAecMaMnvZzDHnJO9BjqkAQ3UqWxtWqKZIaMaSczepZHsBBEe1V37SZVrtj9kp9IRakei3MU9raNsGV636wVsK6BmxVG6D3bGuruzQ3DUpl97ZrgMmxOLwAGSuqynK4oLmWtqT2gw53rAzqptzHoDhuU%2BuqVxYKE5JXvJrSXaSKshTwThYOpYfbR2E%2B55jhZVKF88d%2FLc%2Fa4y9nYPPovbCQP4o5sgADnFNUemikgHeYoBCdxy&X-Amz-Signature=fdc7937ca982d97a7983091f24b67c0f33669b3e65705b542e7869c1c54a38b5&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f18086e5-5b04-4fbf-8309-8944ab20d213/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZHYAYBKR%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T151612Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEcaCXVzLXdlc3QtMiJGMEQCIFA9abCUhzwYD6VJnA7BXo1koP0Ms7NWXiiOfdRPSTxFAiBM0hrW3X%2Bwa%2FQ7dW%2Bd3QiRQRkPLZTiAFG4O20SJwKfnyr%2FAwhgEAAaDDYzNzQyMzE4MzgwNSIMYNMgLLYCs7vATRpEKtwDLYiUtK2i0RxvupAGG8E35oeR3ibmNSINcO9yR3OahiMcafCFZAzBf3kGF8dKFIe4zUZrLPGcnhCiQKF%2BwGyi3LwqfavNYvCU4dBwjqQHe2od7bfOqzZk5al1ccY24TqwzSx%2F%2FG9vGCQVsupN80o%2BL5fvjCzeYtZAPgW2PH7a3lAnd%2BvOETv76yG7yslKQYIe4Gky4RutigXaxrpSW7nEsWqDaOKfFrG3xGQmfOOCCvZAhe3ZMcSZkkjtvUu42pKz7U8n5YECAGdUzDnFAmc3tWrI1O3ifOAh6GzhPk9DY5%2BChWV5PTDfb3f%2F4anTMU42mG1olfQRv5%2FiFaYSoxKbzZzRH8hoYjXBMFp3albth73zjeBH%2BnVP49WgVRYEkmq8Pit11MIjgVA5Gb9gy03UmsMQG4DWl%2BXj6S1Tot8u5VIWNV8aDJboAmw1HdFZrhKrzmTziMx%2BmZ3lDwP2ayyRWhTDK7hfLIUXrpN5L7jVj0TVpbipvFt9EdD86vTmifVec8i2AotG8%2BCobWDLw6xoAvKBwrKoOPg5NpMnZGwKCMUb%2FFma2zgLUGGdOGMk3kwLGRA11Efe1zEwMOrw2WA1PGeRUS7ZH8Yj88HnISdohJ2HqgoG0rNnUVtq144wxpyTvQY6pgGXN0MMTue1%2FkZxlH13F9k6GDrieeNsXmLEQgIEAfVyeG4xfz9xr8tDChiiCFQsrCTZePtQ6hGleXWgcCldWtQPK3yVy1fayXY370t4Oh5hA3zsyaw3Wb24NrAbGtYdTSqkTwOXgBHiOen6mBdfTPQHrSKHOd9JV%2F%2B0P6VBkOiTzm0tr4ffIZ6QRaPbKknuPyKw4XX5mm7kkqFscRc9TWVHbkHqka0o&X-Amz-Signature=78756d32267fc050f2be61ed1c94d3d210d17829ca9f712847c3d607e57a6065&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Correlation Plot
Heatmap visualizes correlations among variables. Color scheme indicates Pearson correlation coefficients. Dark red diagonal line shows perfect correlation (value of 1) between variables and themselves.
This heatmap offers overview of variable relationships and their link with price.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cd3b341e-cc1a-45f7-8aec-cdc00436d270/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZHYAYBKR%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T151612Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEcaCXVzLXdlc3QtMiJGMEQCIFA9abCUhzwYD6VJnA7BXo1koP0Ms7NWXiiOfdRPSTxFAiBM0hrW3X%2Bwa%2FQ7dW%2Bd3QiRQRkPLZTiAFG4O20SJwKfnyr%2FAwhgEAAaDDYzNzQyMzE4MzgwNSIMYNMgLLYCs7vATRpEKtwDLYiUtK2i0RxvupAGG8E35oeR3ibmNSINcO9yR3OahiMcafCFZAzBf3kGF8dKFIe4zUZrLPGcnhCiQKF%2BwGyi3LwqfavNYvCU4dBwjqQHe2od7bfOqzZk5al1ccY24TqwzSx%2F%2FG9vGCQVsupN80o%2BL5fvjCzeYtZAPgW2PH7a3lAnd%2BvOETv76yG7yslKQYIe4Gky4RutigXaxrpSW7nEsWqDaOKfFrG3xGQmfOOCCvZAhe3ZMcSZkkjtvUu42pKz7U8n5YECAGdUzDnFAmc3tWrI1O3ifOAh6GzhPk9DY5%2BChWV5PTDfb3f%2F4anTMU42mG1olfQRv5%2FiFaYSoxKbzZzRH8hoYjXBMFp3albth73zjeBH%2BnVP49WgVRYEkmq8Pit11MIjgVA5Gb9gy03UmsMQG4DWl%2BXj6S1Tot8u5VIWNV8aDJboAmw1HdFZrhKrzmTziMx%2BmZ3lDwP2ayyRWhTDK7hfLIUXrpN5L7jVj0TVpbipvFt9EdD86vTmifVec8i2AotG8%2BCobWDLw6xoAvKBwrKoOPg5NpMnZGwKCMUb%2FFma2zgLUGGdOGMk3kwLGRA11Efe1zEwMOrw2WA1PGeRUS7ZH8Yj88HnISdohJ2HqgoG0rNnUVtq144wxpyTvQY6pgGXN0MMTue1%2FkZxlH13F9k6GDrieeNsXmLEQgIEAfVyeG4xfz9xr8tDChiiCFQsrCTZePtQ6hGleXWgcCldWtQPK3yVy1fayXY370t4Oh5hA3zsyaw3Wb24NrAbGtYdTSqkTwOXgBHiOen6mBdfTPQHrSKHOd9JV%2F%2B0P6VBkOiTzm0tr4ffIZ6QRaPbKknuPyKw4XX5mm7kkqFscRc9TWVHbkHqka0o&X-Amz-Signature=6b0417cc4c65566d07b1e1379f963a61fb76fe2e8d44c84eec8d9efe835c6bdc&X-Amz-SignedHeaders=host&x-id=GetObject)

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
