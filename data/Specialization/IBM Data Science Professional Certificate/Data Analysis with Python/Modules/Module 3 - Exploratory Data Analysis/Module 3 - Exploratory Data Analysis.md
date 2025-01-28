

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7e6d594d-952e-44b6-97ea-31225882aea6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666VFYJAX5%2F20250128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250128T211334Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHUaCXVzLXdlc3QtMiJHMEUCIGw%2F4OYuUt0vhlJe8GJcW5gZDsL6Mg2JpS3%2FCF3UG34aAiEAhRMay47HY9GzA%2F5Q8zcNfEAjowD1sidGiQLvyYWK8TIq%2FwMIfhAAGgw2Mzc0MjMxODM4MDUiDH52Mo%2BOJ8OzR%2F5PIyrcA9D7ujrfDOKQIQIlVWaHXNzcfYUCNmA0fWa60UNV6czWTk%2B%2BTGWWn3fjnXtbMxoRH08QlMPSv91f7duQu341S1Uhxt3XUYueQ0OY4peS49CcgvEh1wPSoc1%2BFqbTOHNsac4CrYzQoDRdACPovaJZ2Auwqwc5N7IUPEJ0DVoITuSkAnH%2FyTLz92U64vXW4lzUvlx9snFVYgX81VDWnUlFnINu52OPRXkNdz6%2BOxSYk2pVTQhssbrmmlYRI574ArumJmDKY5u7YPdDXNPafC%2BZo8aa9GLyG9S9%2Bp3%2B50cWB55Ewi9XRMSvqqywlCFrLBaKr5xmrp0dh4b0pccsFH8XoRTkaRJCg7YP7WPFasUKSZiy3x1XJ5qWhlLIcPIVv5ZbelotHI7f7OVH7fUzSFcG2hJGEDiPj1flBs4oQNi48bwSrLK5FpLqVv8kbgMqvDlnyYMyWfaH2ofwD934U9QBMZgcUyc5z1LQrvtXEPmwPbzh1VbFv%2B%2FY8QHscNcp0FqmvFkoT8C4%2B2hmDbQw1UfazoEuETjXYxdAMGGE%2BtRbCkusr7KOjXVDXAZO%2BWhSj8UnJCNnwDYGRFLUtLdPPb3d5Vf2RSIVMHKJFRn731DrQvQWaiwKLjKwOalWp7KQMNP55LwGOqUB6H4eDYDBYzBfkWyacg2gjBW%2BAaJO2YMgyVV8d0qc%2B72IKLi%2BpCJOsMXEJBICrg3IyA2jRHyShDwFX6aSDnhm1ICymUQG46ZPNepBzxI%2BoSx5FgkmEXy%2BpiSGYfD%2FYDSqHao93zEAgwGePehuMIgWOQzGVzYj%2BmuQ%2F%2BKoaCZlvDJRQ7yFIgwRb9eQG3Y%2BZKt4wWTCOD3Xa3lAv15vF4QCXPHW2tlK&X-Amz-Signature=0c8193cb7a34979b4f6f261eb79e40f3f85476c28bc56d8a57ba7586c0fcf596&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cbfaed9e-b398-4902-8936-dea058b21def/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666VFYJAX5%2F20250128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250128T211334Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHUaCXVzLXdlc3QtMiJHMEUCIGw%2F4OYuUt0vhlJe8GJcW5gZDsL6Mg2JpS3%2FCF3UG34aAiEAhRMay47HY9GzA%2F5Q8zcNfEAjowD1sidGiQLvyYWK8TIq%2FwMIfhAAGgw2Mzc0MjMxODM4MDUiDH52Mo%2BOJ8OzR%2F5PIyrcA9D7ujrfDOKQIQIlVWaHXNzcfYUCNmA0fWa60UNV6czWTk%2B%2BTGWWn3fjnXtbMxoRH08QlMPSv91f7duQu341S1Uhxt3XUYueQ0OY4peS49CcgvEh1wPSoc1%2BFqbTOHNsac4CrYzQoDRdACPovaJZ2Auwqwc5N7IUPEJ0DVoITuSkAnH%2FyTLz92U64vXW4lzUvlx9snFVYgX81VDWnUlFnINu52OPRXkNdz6%2BOxSYk2pVTQhssbrmmlYRI574ArumJmDKY5u7YPdDXNPafC%2BZo8aa9GLyG9S9%2Bp3%2B50cWB55Ewi9XRMSvqqywlCFrLBaKr5xmrp0dh4b0pccsFH8XoRTkaRJCg7YP7WPFasUKSZiy3x1XJ5qWhlLIcPIVv5ZbelotHI7f7OVH7fUzSFcG2hJGEDiPj1flBs4oQNi48bwSrLK5FpLqVv8kbgMqvDlnyYMyWfaH2ofwD934U9QBMZgcUyc5z1LQrvtXEPmwPbzh1VbFv%2B%2FY8QHscNcp0FqmvFkoT8C4%2B2hmDbQw1UfazoEuETjXYxdAMGGE%2BtRbCkusr7KOjXVDXAZO%2BWhSj8UnJCNnwDYGRFLUtLdPPb3d5Vf2RSIVMHKJFRn731DrQvQWaiwKLjKwOalWp7KQMNP55LwGOqUB6H4eDYDBYzBfkWyacg2gjBW%2BAaJO2YMgyVV8d0qc%2B72IKLi%2BpCJOsMXEJBICrg3IyA2jRHyShDwFX6aSDnhm1ICymUQG46ZPNepBzxI%2BoSx5FgkmEXy%2BpiSGYfD%2FYDSqHao93zEAgwGePehuMIgWOQzGVzYj%2BmuQ%2F%2BKoaCZlvDJRQ7yFIgwRb9eQG3Y%2BZKt4wWTCOD3Xa3lAv15vF4QCXPHW2tlK&X-Amz-Signature=0b6d81d65840997cf638b739a087105e7a82e994a931900b9fac27cecac9d6fb&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/91181646-b1e0-4433-9711-6259a96a9247/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666VFYJAX5%2F20250128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250128T211335Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHUaCXVzLXdlc3QtMiJHMEUCIGw%2F4OYuUt0vhlJe8GJcW5gZDsL6Mg2JpS3%2FCF3UG34aAiEAhRMay47HY9GzA%2F5Q8zcNfEAjowD1sidGiQLvyYWK8TIq%2FwMIfhAAGgw2Mzc0MjMxODM4MDUiDH52Mo%2BOJ8OzR%2F5PIyrcA9D7ujrfDOKQIQIlVWaHXNzcfYUCNmA0fWa60UNV6czWTk%2B%2BTGWWn3fjnXtbMxoRH08QlMPSv91f7duQu341S1Uhxt3XUYueQ0OY4peS49CcgvEh1wPSoc1%2BFqbTOHNsac4CrYzQoDRdACPovaJZ2Auwqwc5N7IUPEJ0DVoITuSkAnH%2FyTLz92U64vXW4lzUvlx9snFVYgX81VDWnUlFnINu52OPRXkNdz6%2BOxSYk2pVTQhssbrmmlYRI574ArumJmDKY5u7YPdDXNPafC%2BZo8aa9GLyG9S9%2Bp3%2B50cWB55Ewi9XRMSvqqywlCFrLBaKr5xmrp0dh4b0pccsFH8XoRTkaRJCg7YP7WPFasUKSZiy3x1XJ5qWhlLIcPIVv5ZbelotHI7f7OVH7fUzSFcG2hJGEDiPj1flBs4oQNi48bwSrLK5FpLqVv8kbgMqvDlnyYMyWfaH2ofwD934U9QBMZgcUyc5z1LQrvtXEPmwPbzh1VbFv%2B%2FY8QHscNcp0FqmvFkoT8C4%2B2hmDbQw1UfazoEuETjXYxdAMGGE%2BtRbCkusr7KOjXVDXAZO%2BWhSj8UnJCNnwDYGRFLUtLdPPb3d5Vf2RSIVMHKJFRn731DrQvQWaiwKLjKwOalWp7KQMNP55LwGOqUB6H4eDYDBYzBfkWyacg2gjBW%2BAaJO2YMgyVV8d0qc%2B72IKLi%2BpCJOsMXEJBICrg3IyA2jRHyShDwFX6aSDnhm1ICymUQG46ZPNepBzxI%2BoSx5FgkmEXy%2BpiSGYfD%2FYDSqHao93zEAgwGePehuMIgWOQzGVzYj%2BmuQ%2F%2BKoaCZlvDJRQ7yFIgwRb9eQG3Y%2BZKt4wWTCOD3Xa3lAv15vF4QCXPHW2tlK&X-Amz-Signature=185538855e71b9c886d572e2630cc987091ee1acc159ea0b58f768653204491b&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/09aba1c0-0d55-41dd-852a-a04c5b8a3fac/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WG7HB6QH%2F20250128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250128T211335Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHUaCXVzLXdlc3QtMiJIMEYCIQCsiV0EzAyJ1pDQ6D%2B8abgQl%2Bfrf6s1ZdVlxCy4A54i%2BQIhAPKDKhVCv0AWMiWiR8c6NwhEasvdmluYH3iLuJUkhvlsKv8DCH4QABoMNjM3NDIzMTgzODA1IgwMVKlq9BtutMizZjoq3APWJIsLmA7PIl0sc8hLh3SvoO9XtHPdEU0cTOj3rjIHnUfbk0qX%2FPhxKy02T%2BUGX%2F2b98T4QzF5sdenhn%2BY7L6A3zdVckEfLse%2FILSP9WccOO3gTjy69hfs5pvnGJKaLwhfjkDKou4ag7T17UBIjgJ1apDhVyY9uOKVSQOvR61XK3yxWEHgR%2BXeDz8ivctW44np6Bjv5UzTTeStP1YFUjzYZrlGUAsUOOzwgBvqypN9eIpNnq3s5M%2FK4qbBgrK9YvvyF%2B72HKE%2FO6maGWibcufM6aMsLDHw6WUHIEH8%2Bfr8jTnYVsHIpFm2VMQU66rHwI0CVRD%2FJJ4g0qcTYJtRABTwcw4EFSs5U9K9Fhq%2B9vmvm7gYSZayB5zx56NAQxtLia3mjchC1rkBXKHQ7BIBoeJALuMvq1miwFWWXwZZOqOMNO9%2BG8yPl9ph9Xp9Mem%2FG8l2S0Es9fehnyKDofnb51o91EQHgvIMU3bz6xLsKqdpnlnW%2BKncR%2B2XZ1mfN73ej6RtCedg76IzXrmGGX1wMmmP%2F22R4oybf7Egm2hkEceAzNDiIdD5DUPgpo2N2vTQ8nGI1b0ZZxOCLN5T9QePjOTc%2FQcXtlCQGdiapeH6ifYR%2Bjv5WmUNnBU86%2B0%2FPjCz%2B%2BS8BjqkATjvePQDWCxiKayZezpZvMU%2BZ0CQnnWTUtSnwPBHv6B7ot04dQyl4yxUffHg3cXVfhexTcUmpB71Pqd9GCZ1%2Fr5gzMzA0l8hue8lqbRVUJy1IYlK%2BZxFxErqWOh8%2FlehvXvJXBkTOULPaQvkmY7At0s4maj1kHkpiP83A%2FqX0Dxi3EtoddISPaay9N9dujbFIP%2BFE0tA3Ln2VoZU5fVfKjqgzByb&X-Amz-Signature=7db4601ca313de1891780936f2cefa55c6d0f39af09c28d2cc5165c234594470&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 2. Scatter Plot
Scatter plots present the relationship between two variables in a dataset. It represents data points on a two-dimensional plane. The independent variable or attribute is plotted on the X-axis, while the dependent variable is plotted on the Y-axis.
**Syntax:**
```python
plt.scatter(x, y)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23708af9-659f-4f23-b626-1a4292d7842c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WG7HB6QH%2F20250128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250128T211335Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHUaCXVzLXdlc3QtMiJIMEYCIQCsiV0EzAyJ1pDQ6D%2B8abgQl%2Bfrf6s1ZdVlxCy4A54i%2BQIhAPKDKhVCv0AWMiWiR8c6NwhEasvdmluYH3iLuJUkhvlsKv8DCH4QABoMNjM3NDIzMTgzODA1IgwMVKlq9BtutMizZjoq3APWJIsLmA7PIl0sc8hLh3SvoO9XtHPdEU0cTOj3rjIHnUfbk0qX%2FPhxKy02T%2BUGX%2F2b98T4QzF5sdenhn%2BY7L6A3zdVckEfLse%2FILSP9WccOO3gTjy69hfs5pvnGJKaLwhfjkDKou4ag7T17UBIjgJ1apDhVyY9uOKVSQOvR61XK3yxWEHgR%2BXeDz8ivctW44np6Bjv5UzTTeStP1YFUjzYZrlGUAsUOOzwgBvqypN9eIpNnq3s5M%2FK4qbBgrK9YvvyF%2B72HKE%2FO6maGWibcufM6aMsLDHw6WUHIEH8%2Bfr8jTnYVsHIpFm2VMQU66rHwI0CVRD%2FJJ4g0qcTYJtRABTwcw4EFSs5U9K9Fhq%2B9vmvm7gYSZayB5zx56NAQxtLia3mjchC1rkBXKHQ7BIBoeJALuMvq1miwFWWXwZZOqOMNO9%2BG8yPl9ph9Xp9Mem%2FG8l2S0Es9fehnyKDofnb51o91EQHgvIMU3bz6xLsKqdpnlnW%2BKncR%2B2XZ1mfN73ej6RtCedg76IzXrmGGX1wMmmP%2F22R4oybf7Egm2hkEceAzNDiIdD5DUPgpo2N2vTQ8nGI1b0ZZxOCLN5T9QePjOTc%2FQcXtlCQGdiapeH6ifYR%2Bjv5WmUNnBU86%2B0%2FPjCz%2B%2BS8BjqkATjvePQDWCxiKayZezpZvMU%2BZ0CQnnWTUtSnwPBHv6B7ot04dQyl4yxUffHg3cXVfhexTcUmpB71Pqd9GCZ1%2Fr5gzMzA0l8hue8lqbRVUJy1IYlK%2BZxFxErqWOh8%2FlehvXvJXBkTOULPaQvkmY7At0s4maj1kHkpiP83A%2FqX0Dxi3EtoddISPaay9N9dujbFIP%2BFE0tA3Ln2VoZU5fVfKjqgzByb&X-Amz-Signature=785836855c7524d98ac46c46826ece6838ecb6991ec77dcfe007c133c7000b9b&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 3. Histogram
A histogram is an important visual representation of data in categorical form. To view the data in a "Binned" form, use the histogram plot with a number of bins required or with the data points that mark the bin edges. The x-axis represents the data bins, and the y-axis represents the number of elements in each bin.
**Syntax:**
```python
plt.hist(x, bins)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/24e4424a-df87-40a1-b63b-195cbdc2e0ab/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WG7HB6QH%2F20250128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250128T211335Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHUaCXVzLXdlc3QtMiJIMEYCIQCsiV0EzAyJ1pDQ6D%2B8abgQl%2Bfrf6s1ZdVlxCy4A54i%2BQIhAPKDKhVCv0AWMiWiR8c6NwhEasvdmluYH3iLuJUkhvlsKv8DCH4QABoMNjM3NDIzMTgzODA1IgwMVKlq9BtutMizZjoq3APWJIsLmA7PIl0sc8hLh3SvoO9XtHPdEU0cTOj3rjIHnUfbk0qX%2FPhxKy02T%2BUGX%2F2b98T4QzF5sdenhn%2BY7L6A3zdVckEfLse%2FILSP9WccOO3gTjy69hfs5pvnGJKaLwhfjkDKou4ag7T17UBIjgJ1apDhVyY9uOKVSQOvR61XK3yxWEHgR%2BXeDz8ivctW44np6Bjv5UzTTeStP1YFUjzYZrlGUAsUOOzwgBvqypN9eIpNnq3s5M%2FK4qbBgrK9YvvyF%2B72HKE%2FO6maGWibcufM6aMsLDHw6WUHIEH8%2Bfr8jTnYVsHIpFm2VMQU66rHwI0CVRD%2FJJ4g0qcTYJtRABTwcw4EFSs5U9K9Fhq%2B9vmvm7gYSZayB5zx56NAQxtLia3mjchC1rkBXKHQ7BIBoeJALuMvq1miwFWWXwZZOqOMNO9%2BG8yPl9ph9Xp9Mem%2FG8l2S0Es9fehnyKDofnb51o91EQHgvIMU3bz6xLsKqdpnlnW%2BKncR%2B2XZ1mfN73ej6RtCedg76IzXrmGGX1wMmmP%2F22R4oybf7Egm2hkEceAzNDiIdD5DUPgpo2N2vTQ8nGI1b0ZZxOCLN5T9QePjOTc%2FQcXtlCQGdiapeH6ifYR%2Bjv5WmUNnBU86%2B0%2FPjCz%2B%2BS8BjqkATjvePQDWCxiKayZezpZvMU%2BZ0CQnnWTUtSnwPBHv6B7ot04dQyl4yxUffHg3cXVfhexTcUmpB71Pqd9GCZ1%2Fr5gzMzA0l8hue8lqbRVUJy1IYlK%2BZxFxErqWOh8%2FlehvXvJXBkTOULPaQvkmY7At0s4maj1kHkpiP83A%2FqX0Dxi3EtoddISPaay9N9dujbFIP%2BFE0tA3Ln2VoZU5fVfKjqgzByb&X-Amz-Signature=512017178ae0aeef3c4a9a4a77849bb6336614ac08d0c9f41b44ca5c615c5629&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ab5a6dfe-51f5-43ee-bcb3-33dae4a1c7ad/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WG7HB6QH%2F20250128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250128T211335Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHUaCXVzLXdlc3QtMiJIMEYCIQCsiV0EzAyJ1pDQ6D%2B8abgQl%2Bfrf6s1ZdVlxCy4A54i%2BQIhAPKDKhVCv0AWMiWiR8c6NwhEasvdmluYH3iLuJUkhvlsKv8DCH4QABoMNjM3NDIzMTgzODA1IgwMVKlq9BtutMizZjoq3APWJIsLmA7PIl0sc8hLh3SvoO9XtHPdEU0cTOj3rjIHnUfbk0qX%2FPhxKy02T%2BUGX%2F2b98T4QzF5sdenhn%2BY7L6A3zdVckEfLse%2FILSP9WccOO3gTjy69hfs5pvnGJKaLwhfjkDKou4ag7T17UBIjgJ1apDhVyY9uOKVSQOvR61XK3yxWEHgR%2BXeDz8ivctW44np6Bjv5UzTTeStP1YFUjzYZrlGUAsUOOzwgBvqypN9eIpNnq3s5M%2FK4qbBgrK9YvvyF%2B72HKE%2FO6maGWibcufM6aMsLDHw6WUHIEH8%2Bfr8jTnYVsHIpFm2VMQU66rHwI0CVRD%2FJJ4g0qcTYJtRABTwcw4EFSs5U9K9Fhq%2B9vmvm7gYSZayB5zx56NAQxtLia3mjchC1rkBXKHQ7BIBoeJALuMvq1miwFWWXwZZOqOMNO9%2BG8yPl9ph9Xp9Mem%2FG8l2S0Es9fehnyKDofnb51o91EQHgvIMU3bz6xLsKqdpnlnW%2BKncR%2B2XZ1mfN73ej6RtCedg76IzXrmGGX1wMmmP%2F22R4oybf7Egm2hkEceAzNDiIdD5DUPgpo2N2vTQ8nGI1b0ZZxOCLN5T9QePjOTc%2FQcXtlCQGdiapeH6ifYR%2Bjv5WmUNnBU86%2B0%2FPjCz%2B%2BS8BjqkATjvePQDWCxiKayZezpZvMU%2BZ0CQnnWTUtSnwPBHv6B7ot04dQyl4yxUffHg3cXVfhexTcUmpB71Pqd9GCZ1%2Fr5gzMzA0l8hue8lqbRVUJy1IYlK%2BZxFxErqWOh8%2FlehvXvJXBkTOULPaQvkmY7At0s4maj1kHkpiP83A%2FqX0Dxi3EtoddISPaay9N9dujbFIP%2BFE0tA3Ln2VoZU5fVfKjqgzByb&X-Amz-Signature=e31639bbb4753452e71010fb2d0f0becd17c4aae565baf9cfae83df238e16099&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8f1b1d60-cf1b-42b3-9faa-f634c89c3f84/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WG7HB6QH%2F20250128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250128T211335Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHUaCXVzLXdlc3QtMiJIMEYCIQCsiV0EzAyJ1pDQ6D%2B8abgQl%2Bfrf6s1ZdVlxCy4A54i%2BQIhAPKDKhVCv0AWMiWiR8c6NwhEasvdmluYH3iLuJUkhvlsKv8DCH4QABoMNjM3NDIzMTgzODA1IgwMVKlq9BtutMizZjoq3APWJIsLmA7PIl0sc8hLh3SvoO9XtHPdEU0cTOj3rjIHnUfbk0qX%2FPhxKy02T%2BUGX%2F2b98T4QzF5sdenhn%2BY7L6A3zdVckEfLse%2FILSP9WccOO3gTjy69hfs5pvnGJKaLwhfjkDKou4ag7T17UBIjgJ1apDhVyY9uOKVSQOvR61XK3yxWEHgR%2BXeDz8ivctW44np6Bjv5UzTTeStP1YFUjzYZrlGUAsUOOzwgBvqypN9eIpNnq3s5M%2FK4qbBgrK9YvvyF%2B72HKE%2FO6maGWibcufM6aMsLDHw6WUHIEH8%2Bfr8jTnYVsHIpFm2VMQU66rHwI0CVRD%2FJJ4g0qcTYJtRABTwcw4EFSs5U9K9Fhq%2B9vmvm7gYSZayB5zx56NAQxtLia3mjchC1rkBXKHQ7BIBoeJALuMvq1miwFWWXwZZOqOMNO9%2BG8yPl9ph9Xp9Mem%2FG8l2S0Es9fehnyKDofnb51o91EQHgvIMU3bz6xLsKqdpnlnW%2BKncR%2B2XZ1mfN73ej6RtCedg76IzXrmGGX1wMmmP%2F22R4oybf7Egm2hkEceAzNDiIdD5DUPgpo2N2vTQ8nGI1b0ZZxOCLN5T9QePjOTc%2FQcXtlCQGdiapeH6ifYR%2Bjv5WmUNnBU86%2B0%2FPjCz%2B%2BS8BjqkATjvePQDWCxiKayZezpZvMU%2BZ0CQnnWTUtSnwPBHv6B7ot04dQyl4yxUffHg3cXVfhexTcUmpB71Pqd9GCZ1%2Fr5gzMzA0l8hue8lqbRVUJy1IYlK%2BZxFxErqWOh8%2FlehvXvJXBkTOULPaQvkmY7At0s4maj1kHkpiP83A%2FqX0Dxi3EtoddISPaay9N9dujbFIP%2BFE0tA3Ln2VoZU5fVfKjqgzByb&X-Amz-Signature=08198e307ab29718dea63b3558a08258e14148ae72ac94f373dd85d3cca4886b&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/13ad0497-05fe-4eaa-984e-707b33e14761/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WG7HB6QH%2F20250128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250128T211335Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHUaCXVzLXdlc3QtMiJIMEYCIQCsiV0EzAyJ1pDQ6D%2B8abgQl%2Bfrf6s1ZdVlxCy4A54i%2BQIhAPKDKhVCv0AWMiWiR8c6NwhEasvdmluYH3iLuJUkhvlsKv8DCH4QABoMNjM3NDIzMTgzODA1IgwMVKlq9BtutMizZjoq3APWJIsLmA7PIl0sc8hLh3SvoO9XtHPdEU0cTOj3rjIHnUfbk0qX%2FPhxKy02T%2BUGX%2F2b98T4QzF5sdenhn%2BY7L6A3zdVckEfLse%2FILSP9WccOO3gTjy69hfs5pvnGJKaLwhfjkDKou4ag7T17UBIjgJ1apDhVyY9uOKVSQOvR61XK3yxWEHgR%2BXeDz8ivctW44np6Bjv5UzTTeStP1YFUjzYZrlGUAsUOOzwgBvqypN9eIpNnq3s5M%2FK4qbBgrK9YvvyF%2B72HKE%2FO6maGWibcufM6aMsLDHw6WUHIEH8%2Bfr8jTnYVsHIpFm2VMQU66rHwI0CVRD%2FJJ4g0qcTYJtRABTwcw4EFSs5U9K9Fhq%2B9vmvm7gYSZayB5zx56NAQxtLia3mjchC1rkBXKHQ7BIBoeJALuMvq1miwFWWXwZZOqOMNO9%2BG8yPl9ph9Xp9Mem%2FG8l2S0Es9fehnyKDofnb51o91EQHgvIMU3bz6xLsKqdpnlnW%2BKncR%2B2XZ1mfN73ej6RtCedg76IzXrmGGX1wMmmP%2F22R4oybf7Egm2hkEceAzNDiIdD5DUPgpo2N2vTQ8nGI1b0ZZxOCLN5T9QePjOTc%2FQcXtlCQGdiapeH6ifYR%2Bjv5WmUNnBU86%2B0%2FPjCz%2B%2BS8BjqkATjvePQDWCxiKayZezpZvMU%2BZ0CQnnWTUtSnwPBHv6B7ot04dQyl4yxUffHg3cXVfhexTcUmpB71Pqd9GCZ1%2Fr5gzMzA0l8hue8lqbRVUJy1IYlK%2BZxFxErqWOh8%2FlehvXvJXBkTOULPaQvkmY7At0s4maj1kHkpiP83A%2FqX0Dxi3EtoddISPaay9N9dujbFIP%2BFE0tA3Ln2VoZU5fVfKjqgzByb&X-Amz-Signature=cfecc7943a140d7db25154d411a0592abb0bb8c36bf8d67fa2bf95e8a916a86b&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 2. Box and Whisker Plot
A box plot shows the distribution of quantitative data in a way that facilitates comparisons between variables or across levels of a categorical variable. The box shows the quartiles of the dataset while the whiskers extend to show the rest of the distribution, except for points that are determined to be "outliers".
**Syntax:**
```python
sns.boxplot(x='header_1', y='header_2', data=df)
```
**Example Output:**


![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d207ae92-0a7c-4e2f-aa65-0ee5a2c33bf7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UK7VWRZJ%2F20250128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250128T211336Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHUaCXVzLXdlc3QtMiJHMEUCIBawiImnC8RaVFUnpYez1q%2FUVsXQZQG2Du5NMz%2F1yp2wAiEA1c4BSBPMTII%2B0%2BMfR4%2Fdr1cbrZ04ej%2B0NA3UBdbc6pgq%2FwMIfRAAGgw2Mzc0MjMxODM4MDUiDN%2FajrEPtxCVOuxJrSrcAxfSQkNYioLXNlrCTc7pFDAFVWKUi1hD3aq6KF9uJv786Vp%2BAQA4BQ0ZBTn0pQC4zSj3FvQg10eNyTnb6AwCjMEuPOJjGzNgeXSu1h7RxNsJmdsa0F8H95uATV37BI44JkdmqK4Ls%2FOnUqogGEqEjDBJpWIiml4R%2Fe%2Fg4Y6jLZ2AOCVIfSy9CGOUySb1GQJyzTwzdNh9Kh4%2BfdgFrGfn83IT5TWN8fbdoFpToK8%2BjiU2jmQu2KWUio4NZUj1UTzDyfRBSyiuatAhYYcnytT%2BZ9KMPkY49Sh6z9PMiQT7DcZ0YjNMQF%2B0fubvwjlXlgBdfRZW2cxLWJWi2%2F7X6BTiWqVTpfC7nmQFQklda9Seo0XIOF4nlZxYPYsxNoe6G3C4FsSbdn92GTd7bW0A2MrmSrm2xzk4WNlAnU65dJs2Zo%2B3ZxIvJeO9HARPVD0HNp2%2BB6bShkrTfbZ7FVOkBroHk2Ydru88%2FQS%2FtzYaaaK%2BkgANXRlP3ZQYgtGOjv2FbEhn3YAZ2Z7RBV4BBZMxTtPupvyXWkDM%2F%2BlveZma6b8UXQ4vcytriALIgqdFfjZaxqT38MBC1igjp4gXikSA3rUfI4kFfNrI3Xa%2Bwv%2FsbwWxS0oz6MYlR%2B4vyaRlECF%2FMPr55LwGOqUBgeGK7xDhUGM7pdXuBf2kD1C3ftbDVUfAtW%2Bj9eP0qdlpdJO0j%2B82es5xxxwWGK%2FvHG%2F9EzL1cYlKV0mTp0jM4eU3BY4Tq8vDuHyOwNUK8treypSXyX6qEZTJNhsS90XxyoVQnB3j5y5b%2BpmR6xtejOkKRq2D59uSGB4OoSAr36pfaQ2toz6ef8GxTpEHbFgMjeouxa5xqBBefi8Me22dxlh07c5b&X-Amz-Signature=5cfdd10ab269cb4bc5af491c99449445348cd5fb5ee7f9b5089c9bea070cbab9&X-Amz-SignedHeaders=host&x-id=GetObject)

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0e516edc-7551-4792-ab18-0494db3c4c0c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YN7L5UHM%2F20250128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250128T211337Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHUaCXVzLXdlc3QtMiJHMEUCIG5l83xa2yvETALc7KxJMGk9paAiKoIhEiMi6YfIKAy3AiEA9Rl4QZiOgEGJky7evRlPQaC2CrRays8wrbz%2FMz%2Fg8%2Fkq%2FwMIfhAAGgw2Mzc0MjMxODM4MDUiDJQiNJh%2FU7%2BBcZSj7yrcA%2FiIm9QOc9pNfENQXMX%2BjYwJ3hEm%2BGljGA1w%2BjQqgQxbEzx%2F1lQ3RVz35dZEkaKyNmos7mb80zuhqEr%2FZ37pqoQwj7FyTF8QafWn6zivKfk1xyGHaVF9%2B7y%2FfDeWir8Xcfd48E2KA8dhUZBXNmlnpiWo3kw6n77s4qTzjfvuKsJZ06bJ5THEMN6QuosHHQRBlwJawo%2F3Y6zEz6AWNSVFdqEq9qVT%2FSqybznfSzcv3VwyQJyeJoY97E14qnhK3jKn47q4bWkpudy99CBK7xuqQRnGARNCmnbZEHb1Es2%2Fbs%2F4u9IBHWNhL7gPLIwn7h21FU4fcNJvRPrOaToe3UpVOmEhxtA8fCZEtVgze2n2dBM4xqHhzPBeGc1Uqbco9H4Ge92BTqwwJFkuJM66o4HB1Mzn%2FVGXWnZBH94FFmuofVeTtOAZLQvSDbqncd4g9JD7VH07UXj%2FrDktC6IQnYw2RbAFXEZjWJbTJDgKejvNcSbDJCIPbEXezXNo%2BVWE1xKlDckEDQYDukmRrsmtSWJsL353gyMKV7gUJ%2BZt6IHhLSuG02gx2IWaWbbc5LXavTXsibXGsDHWrXqUS6FlEJ0rJXLOqFpUWCDUySf3o04VNDZNLWdPFxCgvowhaZ1yMOv55LwGOqUBGyQBjS7haIyiGMgDN2bBWuB1m221NWCVEO9ZYXTkimgMQs1ZWs8Los5r2XhaPoNpNmfgFu1HrDSAJTUW7xQGqIOJ%2Fu0tpZu6ogKb4smvArRXxMjyvj3l5qDzCeGiby%2BDRjKWKiMoQMiCGx%2F%2Fgll36HuhAw6hsTc%2BQj3y1H11LpYaFkGY13wIH%2BUTr7GdKSruCeuEuh2%2FnJyOytp8LYmF8%2Fp8bl9A&X-Amz-Signature=778c94e39f5b4616399e7da1c95010cd500efeaa81593de5a5c97dfc321edaed&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23a79b9d-2356-49a9-8fd9-65c6b0ab2cc5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WG7HB6QH%2F20250128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250128T211335Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHUaCXVzLXdlc3QtMiJIMEYCIQCsiV0EzAyJ1pDQ6D%2B8abgQl%2Bfrf6s1ZdVlxCy4A54i%2BQIhAPKDKhVCv0AWMiWiR8c6NwhEasvdmluYH3iLuJUkhvlsKv8DCH4QABoMNjM3NDIzMTgzODA1IgwMVKlq9BtutMizZjoq3APWJIsLmA7PIl0sc8hLh3SvoO9XtHPdEU0cTOj3rjIHnUfbk0qX%2FPhxKy02T%2BUGX%2F2b98T4QzF5sdenhn%2BY7L6A3zdVckEfLse%2FILSP9WccOO3gTjy69hfs5pvnGJKaLwhfjkDKou4ag7T17UBIjgJ1apDhVyY9uOKVSQOvR61XK3yxWEHgR%2BXeDz8ivctW44np6Bjv5UzTTeStP1YFUjzYZrlGUAsUOOzwgBvqypN9eIpNnq3s5M%2FK4qbBgrK9YvvyF%2B72HKE%2FO6maGWibcufM6aMsLDHw6WUHIEH8%2Bfr8jTnYVsHIpFm2VMQU66rHwI0CVRD%2FJJ4g0qcTYJtRABTwcw4EFSs5U9K9Fhq%2B9vmvm7gYSZayB5zx56NAQxtLia3mjchC1rkBXKHQ7BIBoeJALuMvq1miwFWWXwZZOqOMNO9%2BG8yPl9ph9Xp9Mem%2FG8l2S0Es9fehnyKDofnb51o91EQHgvIMU3bz6xLsKqdpnlnW%2BKncR%2B2XZ1mfN73ej6RtCedg76IzXrmGGX1wMmmP%2F22R4oybf7Egm2hkEceAzNDiIdD5DUPgpo2N2vTQ8nGI1b0ZZxOCLN5T9QePjOTc%2FQcXtlCQGdiapeH6ifYR%2Bjv5WmUNnBU86%2B0%2FPjCz%2B%2BS8BjqkATjvePQDWCxiKayZezpZvMU%2BZ0CQnnWTUtSnwPBHv6B7ot04dQyl4yxUffHg3cXVfhexTcUmpB71Pqd9GCZ1%2Fr5gzMzA0l8hue8lqbRVUJy1IYlK%2BZxFxErqWOh8%2FlehvXvJXBkTOULPaQvkmY7At0s4maj1kHkpiP83A%2FqX0Dxi3EtoddISPaay9N9dujbFIP%2BFE0tA3Ln2VoZU5fVfKjqgzByb&X-Amz-Signature=6b1ce1ad1b8e19d94e44e8f9fe112157e4d064883df7e36b78870de6a70c2642&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 4. KDE Plot
A Kernel Density Estimate (KDE) plot is a graph that creates a probability distribution curve for the data based upon its likelihood of occurrence on a specific value. This is created for a single vector of information.
**Syntax:**
```python
sns.kdeplot(X) || sns.kdeplot(df['age'])
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0d571213-2a2f-4921-a50b-880847aa05ee/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WG7HB6QH%2F20250128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250128T211335Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHUaCXVzLXdlc3QtMiJIMEYCIQCsiV0EzAyJ1pDQ6D%2B8abgQl%2Bfrf6s1ZdVlxCy4A54i%2BQIhAPKDKhVCv0AWMiWiR8c6NwhEasvdmluYH3iLuJUkhvlsKv8DCH4QABoMNjM3NDIzMTgzODA1IgwMVKlq9BtutMizZjoq3APWJIsLmA7PIl0sc8hLh3SvoO9XtHPdEU0cTOj3rjIHnUfbk0qX%2FPhxKy02T%2BUGX%2F2b98T4QzF5sdenhn%2BY7L6A3zdVckEfLse%2FILSP9WccOO3gTjy69hfs5pvnGJKaLwhfjkDKou4ag7T17UBIjgJ1apDhVyY9uOKVSQOvR61XK3yxWEHgR%2BXeDz8ivctW44np6Bjv5UzTTeStP1YFUjzYZrlGUAsUOOzwgBvqypN9eIpNnq3s5M%2FK4qbBgrK9YvvyF%2B72HKE%2FO6maGWibcufM6aMsLDHw6WUHIEH8%2Bfr8jTnYVsHIpFm2VMQU66rHwI0CVRD%2FJJ4g0qcTYJtRABTwcw4EFSs5U9K9Fhq%2B9vmvm7gYSZayB5zx56NAQxtLia3mjchC1rkBXKHQ7BIBoeJALuMvq1miwFWWXwZZOqOMNO9%2BG8yPl9ph9Xp9Mem%2FG8l2S0Es9fehnyKDofnb51o91EQHgvIMU3bz6xLsKqdpnlnW%2BKncR%2B2XZ1mfN73ej6RtCedg76IzXrmGGX1wMmmP%2F22R4oybf7Egm2hkEceAzNDiIdD5DUPgpo2N2vTQ8nGI1b0ZZxOCLN5T9QePjOTc%2FQcXtlCQGdiapeH6ifYR%2Bjv5WmUNnBU86%2B0%2FPjCz%2B%2BS8BjqkATjvePQDWCxiKayZezpZvMU%2BZ0CQnnWTUtSnwPBHv6B7ot04dQyl4yxUffHg3cXVfhexTcUmpB71Pqd9GCZ1%2Fr5gzMzA0l8hue8lqbRVUJy1IYlK%2BZxFxErqWOh8%2FlehvXvJXBkTOULPaQvkmY7At0s4maj1kHkpiP83A%2FqX0Dxi3EtoddISPaay9N9dujbFIP%2BFE0tA3Ln2VoZU5fVfKjqgzByb&X-Amz-Signature=ebe672bdf232ba181dce76eb6d7a21722ffdc39d6ea7c6849f45699c6b92c7b1&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/53752550-ef82-4ca9-a01a-09921f0282d0/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WG7HB6QH%2F20250128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250128T211335Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHUaCXVzLXdlc3QtMiJIMEYCIQCsiV0EzAyJ1pDQ6D%2B8abgQl%2Bfrf6s1ZdVlxCy4A54i%2BQIhAPKDKhVCv0AWMiWiR8c6NwhEasvdmluYH3iLuJUkhvlsKv8DCH4QABoMNjM3NDIzMTgzODA1IgwMVKlq9BtutMizZjoq3APWJIsLmA7PIl0sc8hLh3SvoO9XtHPdEU0cTOj3rjIHnUfbk0qX%2FPhxKy02T%2BUGX%2F2b98T4QzF5sdenhn%2BY7L6A3zdVckEfLse%2FILSP9WccOO3gTjy69hfs5pvnGJKaLwhfjkDKou4ag7T17UBIjgJ1apDhVyY9uOKVSQOvR61XK3yxWEHgR%2BXeDz8ivctW44np6Bjv5UzTTeStP1YFUjzYZrlGUAsUOOzwgBvqypN9eIpNnq3s5M%2FK4qbBgrK9YvvyF%2B72HKE%2FO6maGWibcufM6aMsLDHw6WUHIEH8%2Bfr8jTnYVsHIpFm2VMQU66rHwI0CVRD%2FJJ4g0qcTYJtRABTwcw4EFSs5U9K9Fhq%2B9vmvm7gYSZayB5zx56NAQxtLia3mjchC1rkBXKHQ7BIBoeJALuMvq1miwFWWXwZZOqOMNO9%2BG8yPl9ph9Xp9Mem%2FG8l2S0Es9fehnyKDofnb51o91EQHgvIMU3bz6xLsKqdpnlnW%2BKncR%2B2XZ1mfN73ej6RtCedg76IzXrmGGX1wMmmP%2F22R4oybf7Egm2hkEceAzNDiIdD5DUPgpo2N2vTQ8nGI1b0ZZxOCLN5T9QePjOTc%2FQcXtlCQGdiapeH6ifYR%2Bjv5WmUNnBU86%2B0%2FPjCz%2B%2BS8BjqkATjvePQDWCxiKayZezpZvMU%2BZ0CQnnWTUtSnwPBHv6B7ot04dQyl4yxUffHg3cXVfhexTcUmpB71Pqd9GCZ1%2Fr5gzMzA0l8hue8lqbRVUJy1IYlK%2BZxFxErqWOh8%2FlehvXvJXBkTOULPaQvkmY7At0s4maj1kHkpiP83A%2FqX0Dxi3EtoddISPaay9N9dujbFIP%2BFE0tA3Ln2VoZU5fVfKjqgzByb&X-Amz-Signature=4ae4a9536c2c77755682edd149388f5a0640bfe506cedd6dee28f0bc7bf5f869&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
## 4. Correlation Between Variables
Correlation is a statistical measure of the extent to which different variables are interdependent. It indicates how changes in one variable are associated with changes in another variable over time.
### Positive Correlation
Positive correlation indicates that as one variable increases, the other variable also tends to increase.
**Example: Engine Size and Price**
- **Positive Correlation:** Engine size increases, price also increases.
- **Visualization:** Scatter plot with a steep positive slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c7ea9b0-3ef3-4357-a9c3-554fc71b6b15/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XHBRJPQ4%2F20250128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250128T211336Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHUaCXVzLXdlc3QtMiJIMEYCIQDHVH5A%2FF2T7USSNYEph%2BrGl%2BhoWvs2HoCYXjvjkv9G0wIhAM5eitl028rK%2FhYpQyRuhejUv0%2FPy3TCaLYtrunp86v7Kv8DCH4QABoMNjM3NDIzMTgzODA1IgwB1cgsG2BTqJya2PEq3AMeZLmtrlP6UtgnS0Z1EmmLCxX%2FQ4FvS99kAajChE1104pk9dw1TIUVH9UQxCBdlerrTOL%2B%2BCRis13uzYycCjEk12NJPtGWUJF%2BAEIRVnd4mdsKzwFI9Qj%2Feoyyp9Etpk0mwKoNTNyo9j3GcUQyE2o621D6YfaFbyPdAe1CZDuuyk8PMOBXxRpTSTSw4oIGTSNKo4daihnQqy8NSg4jQ%2B6KxcDbF%2FEjvs4od%2BT0HkHqONaq%2BjrXiIn1pII6BccZ%2BlTuMHqbxb%2FOxzfi%2BRH%2Fi9b4ZuEsuxlcm6f3QIFLwSMQlQdzb2X%2BxP3HvWFFyGWJPoXrJRNxBx1JfwZqvO%2Bvof%2F7kna61SFGrtg1%2FsEZAxbYI1tWMmY95kw1dLqf9ZfCovjpBMjYiJO%2BO2BkLLa1UJA2oyUBKEtQMnYt%2BORxI1uVa5uImHmqAV7c6AcHiKuJ98lnk8m%2BRezHDxVRwkiny9DlKO%2FiVMrx0ijgMtF1MGVHZTDF8u5l2Itv5BVFLgLNCtGBg6fJyixqSqym2Lovrdr%2FV6MWaiFswhA6uV1EnVOqrx%2FSmSIYvGQK1J%2Bx9pNEzY%2Fd8qlCgx%2FZ8jgyiHsnPGczqtL%2BlVTqnWwTTQ1tDc1M1WYK8UF8VfhFO1YaLzDJ%2BeS8BjqkAQqrl%2B530Sy6dZ4PJINMw4AFQ2Igi24rFg496dP1wU%2B9geEzyS3d%2F0BXXxKPNhCH7kSS%2B2Peq5MbSDbTWwfJ4qHZjW%2FBUpiBNpdurNlntFV%2BqVtS7M6cpJIZqbcKBBR97m%2BoVSyMyjTI2K9x4zZmwRODeSXI7oarIEZRm9aeVQF2dFP3bYICJkC5Vmvjn8dUFoHteneIthZEYWtMTuwIZ7p4Aiuq&X-Amz-Signature=6776458fd079ec9fd2a4bb569b4d3c276f768833d57e3b27f069592721a7ddc6&X-Amz-SignedHeaders=host&x-id=GetObject)
**Explanation:** When engine size increases, there is a corresponding increase in the price of the vehicle. This positive correlation suggests that larger engines tend to be associated with higher prices in the market.
___
### Negative Correlation
Negative correlation indicates that as one variable increases, the other variable tends to decrease.
**Example: Highway Miles per Gallon and Price**
- **Negative Correlation:** As highway miles per gallon increases, price decreases.
- **Visualization:** Scatter plot with a steep negative slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/10f1f798-9cc4-4df2-a9c1-5a339f554a0b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VX6DAJJB%2F20250128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250128T211336Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHUaCXVzLXdlc3QtMiJHMEUCIQCRBjBYA1SmI%2BChev02G4BO8tbMuQHpK8aKfpqUHqWPWwIgHvCYzvgcZ4hYBEPLH9hkZ8iYU7Lo3KIMDATXh8iDUlkq%2FwMIfhAAGgw2Mzc0MjMxODM4MDUiDHjIQHmxSkNy%2FS6KTCrcA746FmTJ%2FZmy7%2FLq35MwjR59A%2FYxzfRJT6ue3QwVCFQavB%2FH8mixT9M6%2FaszIwN4KW4QCzLBUxKmcqkK5jy4%2B6ukFb7MkrSzGdt3d%2BQWOGl7tlKtPjx49OMo2fBmrhuVezdIDr%2BNTEjq7EQGZXCNcDDgBHMakDtsEVaZ%2BmGROsycWjpjdn5YZhRgbMskLUlsonYsSlDGdzCnNhC4OD3UeqaVjGPyzXbJuqSJevP9xNDgCEm8XSatCs2mh0lgxjKAURsVZ61BFRO4MNZkO%2FfDkRUuRELnh7seCsCv2Ojzo5L4lYHH2U70%2FEEY6X8GbNggy7coG4rOa0oSkAJfUE0tBHRfG9QdQHNlQOQX8JcERsR2btXjviNs33uaJXo0ScQ5wBtcnyy3TUkO9us3%2BXEbbMmfQ53lYpMdmWNMjT0gVlV8Na2l97NX9sfrvihm4gmfHwWh7nBZXcp73rv706QMGd3aKcEF%2BQFQvnByloF%2B8ZATxr9zbygSihHWzSc4ubo1lsmh2i9N9gGIfrcdEfIP7nWoaBFLH6Y65NyTwITz9ge2G7YrjlWJSp8hbXaIUDTmTHx8qOebxTxe5u9IGFLJmxnPEnjAA05AbZ9wzNzpLnvlHKwdKqaztQkCJG8nMKz65LwGOqUBTlsD1bkPwdEf3bdfWjywundhzSt5QIsyMTGwXEO4OGw4l5EG44p0O4VfBoBS86sQqbnQa3v3GcS2UaXQVfmD3DHqfHwFsMsSiW7wuEXGTIeWXxgWWgfd%2BhfdQDCSs3Q2iNo0ijRv1Z3pr87oSshb1pMETBcIUueLi1w04wZ%2Bng0lo2HtJ%2B%2BA0TVxzxW5qhZtPusIfZ6x5IZB0o7gTs%2BmRj1XKexa&X-Amz-Signature=142746403147a855d524497987ef3df13f61de2d7c11ff6fd38208c1d8958eb3&X-Amz-SignedHeaders=host&x-id=GetObject)
**Explanation:** When highway miles per gallon increases, the price of the vehicle tends to decrease. This negative correlation suggests that cars with higher fuel efficiency (more miles per gallon) are generally priced lower in the market.
___
### Weak Correlation
Weak correlation indicates a lack of strong relationship between the variables.
**Example: RPM and Price**
- **Weak Correlation:** Low and high RPM values show varied prices, indicating no strong predictive relationship.
- **Visualization:** Scatter plot with no clear trend or slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9f914514-8914-4bf4-ac84-d9e3077f6eb1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46626LWWLEU%2F20250128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250128T211336Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHUaCXVzLXdlc3QtMiJHMEUCIFxHTKVJXc1uril3tycVREDtYYuv%2Bh7whxRn3J7RM6FMAiEAsiml1sF0lfV7QXbTipv9uRqsif8lr0EKbS1N6sUhp0Qq%2FwMIfhAAGgw2Mzc0MjMxODM4MDUiDOx7MXzVpLFsvr6r8CrcAwmU8zk3XRfgtFys4RkEXCJLehavy5%2Bt%2FHlFpYgBfP3oZTf62izP6qVNFlKm0tPiujg1My8p7Y2qUcewb9oJuWJMlLwhN8FlpNP%2FsagPn1rrnDGihHLyWv2lAiTRQbAk%2F9ndW2iDQG0cHfYIiS1oHWXWWhHAX0P70NdKVZHaO6pO06s4jUHNuPPbg%2B%2B7z0KQOgs%2F6zknTHYUojsmeWaUzQHArrG2YoREafWEbdBy5qLE5HedSFO8f8JeRng3%2FzM6dW%2BM5e3%2Bvd%2FDGTqYLv9gdBGH%2FF25hWYRLg6TEePHaapoFWy6t6zN8apyYJ63oR97lsSTj3uV9yDcUHzRqDKwM9sGvRsXN806nCIcvu4JvCHAfzMFbAv3wNMhH0jpD%2FwM0Z2wir9k3Qd1zF479DJbsUuN7wJzPZEjsLM5uyYmnuKEsWo5yntu%2FJ6lx4algabULztM%2B39t01fiJW%2FAv8izCPfX8TM4Jl2wuwCP5IEoYTLWiRFI41Kq4y7RaeNRx7kpGHY8Yls87bils3W7j7XQ5W0ms27JCGC3DdXVP%2FvryjBJE8IxFLEu2WgQwx3RrIw5e3Tl5g95zKq79nrtwNqybdXGS5xs88am6OJJqFh1gHqCpSFPa9c7fkWeMnUWMOD55LwGOqUBcLZMD4clNnWISCGJpo%2BzvY6SvQ88wsuYjgXFuwZwAGeEVlrCQdPlimHt1POqaDJ7UilqjE%2FTjRiDyrlqmXxXzpiD0fIG2zJ0eo2N8SEOKIwaoq1Qwd4lmcpMmJ2wQJ%2FCqChZd5F2rLDkFn8%2Fb4Bs1wNi3%2FlKKoqmRv5bjcjrGGLDIJlBa57K3RcRdTiok6DB4GEAYpP7dCQUGcTjW45HM3eongD1&X-Amz-Signature=1defb895ade09e8285fd7328ad1b3bb879cc9a7c75e4d839e1864ed7aabb093b&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f18086e5-5b04-4fbf-8309-8944ab20d213/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Y7DOQQQO%2F20250128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250128T211336Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHUaCXVzLXdlc3QtMiJHMEUCIQDf7kKUlRPHv1wYu%2BWwCg3bOmO4X0NGYKGtopqidVB9mwIgVA%2FSdr8VkG0RECjoXlDazM5m27Wtx22iCqxJsX0FOwEq%2FwMIfhAAGgw2Mzc0MjMxODM4MDUiDKccVeRiCCr%2BOpZHJSrcA4eLU76Wb5AcjhP6P1uZJdJsNerKOB9bp2ZQ41dC9sySSx%2FH%2FMY8GCUrhH8puZGfV9dAxAPt53Q5lCqLYM66hKbnUzgMXAbMmcu6C2mxMil%2BoNJ6GHEezj%2Bu3GtFHeK2z72rfd7FxOZZdRs3NbsJzJyTy9Holk3FmDeHUrU9tvSp0Vo1FBKp5o1UXM1GJreqlwvZIYA6tYTfBOfQpK%2F2zNbf5y2ep5q47Ab7mT5WquZ3ikVEfZ0VF79YfPcPk1D03rGgMUP5RfWbJ5uVdByaCwt0MEAcvY2nPaxdaRUfNibIl3Q9JT9XkNJt4YqFEM%2FuG6Vrt0I02Loqm8S5xC5XlwgavQg5zUZ79RfcUcOkoQZv7FZ%2BRDmJFFTig0YP7xY25wsaRnVwaoKa6SLaZEGJok%2FcfX89DVKyCiHJtzBMb7sZ9iDw%2BmrV8D4Uqlxc3MeB49FYGtNYdtE7%2FGhaaJZUoA5MlZjJQaQLvITCKTLHLiA6QXtMfre3F1Ut7ZDMthNwZ%2FbC8jRKQU376UezYXWl2hT1%2B0gyw%2BIQiXEvrS2c%2BEtuJiluVLIDauc8wKL4CCJTC4ALo1tn8EaXtBy26w0868z%2BhNsGKPBuJEBpPFC32DVUdDAIchctEgdgiPLiMJz65LwGOqUBud4TWwmCvoOLVPepa6rfNIDNI3yBhpwy6jzTHxBVQFnKEfctQ471VVxMelHlU2r%2Bg0SN5%2FkLq1jHOMyF9G1DFeH1u%2F99zS6I7%2BfnY9tlSjmacXAIO%2FwpYwco8eAeJkl9O%2BTEOuzLF6pnkd9%2B1GpKWDmmJIrZrzwxzB8wrOVQ5Y79gozYk7SryaQofSGqLPv0VCTGEWL%2BgEWpI%2BIWPwQ%2FTUo0HHoF&X-Amz-Signature=b5b1083cafbed1d7f1baf5581c7167bfbb59f95296ca904c75042181cd35c18c&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Correlation Plot
Heatmap visualizes correlations among variables. Color scheme indicates Pearson correlation coefficients. Dark red diagonal line shows perfect correlation (value of 1) between variables and themselves.
This heatmap offers overview of variable relationships and their link with price.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cd3b341e-cc1a-45f7-8aec-cdc00436d270/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Y7DOQQQO%2F20250128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250128T211336Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHUaCXVzLXdlc3QtMiJHMEUCIQDf7kKUlRPHv1wYu%2BWwCg3bOmO4X0NGYKGtopqidVB9mwIgVA%2FSdr8VkG0RECjoXlDazM5m27Wtx22iCqxJsX0FOwEq%2FwMIfhAAGgw2Mzc0MjMxODM4MDUiDKccVeRiCCr%2BOpZHJSrcA4eLU76Wb5AcjhP6P1uZJdJsNerKOB9bp2ZQ41dC9sySSx%2FH%2FMY8GCUrhH8puZGfV9dAxAPt53Q5lCqLYM66hKbnUzgMXAbMmcu6C2mxMil%2BoNJ6GHEezj%2Bu3GtFHeK2z72rfd7FxOZZdRs3NbsJzJyTy9Holk3FmDeHUrU9tvSp0Vo1FBKp5o1UXM1GJreqlwvZIYA6tYTfBOfQpK%2F2zNbf5y2ep5q47Ab7mT5WquZ3ikVEfZ0VF79YfPcPk1D03rGgMUP5RfWbJ5uVdByaCwt0MEAcvY2nPaxdaRUfNibIl3Q9JT9XkNJt4YqFEM%2FuG6Vrt0I02Loqm8S5xC5XlwgavQg5zUZ79RfcUcOkoQZv7FZ%2BRDmJFFTig0YP7xY25wsaRnVwaoKa6SLaZEGJok%2FcfX89DVKyCiHJtzBMb7sZ9iDw%2BmrV8D4Uqlxc3MeB49FYGtNYdtE7%2FGhaaJZUoA5MlZjJQaQLvITCKTLHLiA6QXtMfre3F1Ut7ZDMthNwZ%2FbC8jRKQU376UezYXWl2hT1%2B0gyw%2BIQiXEvrS2c%2BEtuJiluVLIDauc8wKL4CCJTC4ALo1tn8EaXtBy26w0868z%2BhNsGKPBuJEBpPFC32DVUdDAIchctEgdgiPLiMJz65LwGOqUBud4TWwmCvoOLVPepa6rfNIDNI3yBhpwy6jzTHxBVQFnKEfctQ471VVxMelHlU2r%2Bg0SN5%2FkLq1jHOMyF9G1DFeH1u%2F99zS6I7%2BfnY9tlSjmacXAIO%2FwpYwco8eAeJkl9O%2BTEOuzLF6pnkd9%2B1GpKWDmmJIrZrzwxzB8wrOVQ5Y79gozYk7SryaQofSGqLPv0VCTGEWL%2BgEWpI%2BIWPwQ%2FTUo0HHoF&X-Amz-Signature=02cf39906bdf010cb0eb466c071ce1ed2cef7f5b9376dd725a320f7d3eea3f32&X-Amz-SignedHeaders=host&x-id=GetObject)

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
