

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7e6d594d-952e-44b6-97ea-31225882aea6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UVHZYSAZ%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T171223Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIG2mK2%2F2yCXtlpPVIBO1a178XEfPjzrLjIuL2JNZZTUvAiEAguEFglelDeTZYtUc31DDeJ89n720BQa7HV8jN8butjYqiAQIwf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNfwiLw%2BpW%2BmSHudjyrcA7J4EyUqyPwZB5nHr8sUQjvId%2FU0X%2FCyZqaKol8%2F0jIjfh7J0EXRLEQu8%2FBUNrtTr6YgrfEmuwd5HqTxHHwrE7wmqK%2FpRPACGoGI92fMiVt2u637yLHre5jNVcq8sGWm2362euVVXYgcpekOMPifropD%2Bsq%2FBlBdB868JWzB2ovSEJxQV86zT%2Bn3Mbsq06PpfBP4qc34wJDop%2FlroD7ZhcXgUmv0goGoIhdxAaLRXR9sgjHBRMovJhY5ekWU5ibYECD2fGokv9c4w3q1bgwl%2FqPwd3KyMRBLXQvRgbSD2JrarP673nNiF2JQKS%2FIur6ngCWaOS15nD9b%2FLhu9IVUd3gMZ71D%2F1Y%2B50Zl8ZREfUC7IozaOzGWfd54Y9Cr1qXvIVcWDhN5H3LgRE64XZ%2BjbfTKycm2EddPVuklSEY%2F9I1InflVW5jNB%2BK3iwTGWPcXoh%2B%2BJG9WctccIFsmjC%2B0Mp7Bs2Qs29cD36E8j2M%2BeU%2FSUThkEmYrzJ5KXnvdO4Uk5IadpjyfAMlAjz63p6fVUgHD0wZ8V6yZ%2Fdn66n2HW9iy8DrrJ8B1siupcE%2B4FMc7fVr3X%2FvK56hW5PBlaCZCi37hJQo85F0URcD7zJXPPFUQpMRTmXMGgJoKBw0EMJDr87wGOqUBy6XF1sfcSSVPIjyc51IBOg8Lv6zfos6I%2Fz262jPZIox8tGpeEjnvnBo%2B%2FAAeJL1G7KdjSMdcBlPZQVE7ZhtGr4Ntl%2FRhugFIGG%2B4BGX%2FK%2F%2BNEK45%2FVXu1cghftcW6AwLgv0uBuEqvqN7SjzqH%2B21TRcz9LRW%2B09mD6ODpC%2BzmXRhFSVLCWgX6YMvl5%2BI3EX8h6VdxGZ4k61WKy6Mz52YT8OdKIiG&X-Amz-Signature=26c7ff37c1eb0b54c4a34fe7fe9176c0e3d259fd95420b160212bd5260ad0ec5&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cbfaed9e-b398-4902-8936-dea058b21def/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UVHZYSAZ%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T171223Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIG2mK2%2F2yCXtlpPVIBO1a178XEfPjzrLjIuL2JNZZTUvAiEAguEFglelDeTZYtUc31DDeJ89n720BQa7HV8jN8butjYqiAQIwf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNfwiLw%2BpW%2BmSHudjyrcA7J4EyUqyPwZB5nHr8sUQjvId%2FU0X%2FCyZqaKol8%2F0jIjfh7J0EXRLEQu8%2FBUNrtTr6YgrfEmuwd5HqTxHHwrE7wmqK%2FpRPACGoGI92fMiVt2u637yLHre5jNVcq8sGWm2362euVVXYgcpekOMPifropD%2Bsq%2FBlBdB868JWzB2ovSEJxQV86zT%2Bn3Mbsq06PpfBP4qc34wJDop%2FlroD7ZhcXgUmv0goGoIhdxAaLRXR9sgjHBRMovJhY5ekWU5ibYECD2fGokv9c4w3q1bgwl%2FqPwd3KyMRBLXQvRgbSD2JrarP673nNiF2JQKS%2FIur6ngCWaOS15nD9b%2FLhu9IVUd3gMZ71D%2F1Y%2B50Zl8ZREfUC7IozaOzGWfd54Y9Cr1qXvIVcWDhN5H3LgRE64XZ%2BjbfTKycm2EddPVuklSEY%2F9I1InflVW5jNB%2BK3iwTGWPcXoh%2B%2BJG9WctccIFsmjC%2B0Mp7Bs2Qs29cD36E8j2M%2BeU%2FSUThkEmYrzJ5KXnvdO4Uk5IadpjyfAMlAjz63p6fVUgHD0wZ8V6yZ%2Fdn66n2HW9iy8DrrJ8B1siupcE%2B4FMc7fVr3X%2FvK56hW5PBlaCZCi37hJQo85F0URcD7zJXPPFUQpMRTmXMGgJoKBw0EMJDr87wGOqUBy6XF1sfcSSVPIjyc51IBOg8Lv6zfos6I%2Fz262jPZIox8tGpeEjnvnBo%2B%2FAAeJL1G7KdjSMdcBlPZQVE7ZhtGr4Ntl%2FRhugFIGG%2B4BGX%2FK%2F%2BNEK45%2FVXu1cghftcW6AwLgv0uBuEqvqN7SjzqH%2B21TRcz9LRW%2B09mD6ODpC%2BzmXRhFSVLCWgX6YMvl5%2BI3EX8h6VdxGZ4k61WKy6Mz52YT8OdKIiG&X-Amz-Signature=565184c99ffc2545d27202029d6ff9c06943c6a5b2a94f53ae8fefbcf6f484f5&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/91181646-b1e0-4433-9711-6259a96a9247/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UVHZYSAZ%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T171223Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIG2mK2%2F2yCXtlpPVIBO1a178XEfPjzrLjIuL2JNZZTUvAiEAguEFglelDeTZYtUc31DDeJ89n720BQa7HV8jN8butjYqiAQIwf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNfwiLw%2BpW%2BmSHudjyrcA7J4EyUqyPwZB5nHr8sUQjvId%2FU0X%2FCyZqaKol8%2F0jIjfh7J0EXRLEQu8%2FBUNrtTr6YgrfEmuwd5HqTxHHwrE7wmqK%2FpRPACGoGI92fMiVt2u637yLHre5jNVcq8sGWm2362euVVXYgcpekOMPifropD%2Bsq%2FBlBdB868JWzB2ovSEJxQV86zT%2Bn3Mbsq06PpfBP4qc34wJDop%2FlroD7ZhcXgUmv0goGoIhdxAaLRXR9sgjHBRMovJhY5ekWU5ibYECD2fGokv9c4w3q1bgwl%2FqPwd3KyMRBLXQvRgbSD2JrarP673nNiF2JQKS%2FIur6ngCWaOS15nD9b%2FLhu9IVUd3gMZ71D%2F1Y%2B50Zl8ZREfUC7IozaOzGWfd54Y9Cr1qXvIVcWDhN5H3LgRE64XZ%2BjbfTKycm2EddPVuklSEY%2F9I1InflVW5jNB%2BK3iwTGWPcXoh%2B%2BJG9WctccIFsmjC%2B0Mp7Bs2Qs29cD36E8j2M%2BeU%2FSUThkEmYrzJ5KXnvdO4Uk5IadpjyfAMlAjz63p6fVUgHD0wZ8V6yZ%2Fdn66n2HW9iy8DrrJ8B1siupcE%2B4FMc7fVr3X%2FvK56hW5PBlaCZCi37hJQo85F0URcD7zJXPPFUQpMRTmXMGgJoKBw0EMJDr87wGOqUBy6XF1sfcSSVPIjyc51IBOg8Lv6zfos6I%2Fz262jPZIox8tGpeEjnvnBo%2B%2FAAeJL1G7KdjSMdcBlPZQVE7ZhtGr4Ntl%2FRhugFIGG%2B4BGX%2FK%2F%2BNEK45%2FVXu1cghftcW6AwLgv0uBuEqvqN7SjzqH%2B21TRcz9LRW%2B09mD6ODpC%2BzmXRhFSVLCWgX6YMvl5%2BI3EX8h6VdxGZ4k61WKy6Mz52YT8OdKIiG&X-Amz-Signature=1d6f59855931f597b3389eba7f0c714cdeb2b65a3d156e4c2411ad01160db06b&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/09aba1c0-0d55-41dd-852a-a04c5b8a3fac/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RQUBMKUP%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T171224Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIAtHQFbv%2F3qeRI7fyY1sUXKgmRJor3tltR0bYQsPMSiDAiAJI%2F8zgNAmgXfKxZ9EP5oy1uzy8YOd2fEOp%2FMwMIuqdSqIBAjC%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM08UShLwHVQU5zDkZKtwD1iZilh1%2FWOi%2BaByuZQpmNP9SE3SvU%2FHGSYFMuISuTBhOmOorKVXydALmORm5vJbDvuEg%2BHYwiMyQubDitHd%2FUkeU2NBj64xaLaG4iWeFfigClmSwNuil%2FoxjmCcKl6Y1HEzFPwWoZznB%2FVbXTAKJ0M%2BW2d5iHuAEWSSuSmR9I7p%2BJWGnY3qqXII88TAczlWTZbzmv%2Fu7hGygga7La6hMY9HjyW%2B%2FaPJ%2Bcd8PFPVLZ95TEjKyDWhF0EvGF9SOWcZ2VqLkdcD6oM0ShQWXTArHTqiFtqYGEMcBvErCWJmUETHv%2FxdUhRQOSXkiX62JNW1TN2xhOcdisHUBTQPq6D2EbMGAQtYxP3svdA%2F7pP5A0mKis7eRZC6Qbn6zJXQwmEol9ebGXVtuje4Kxr8ap5umHdQcnYViqcOVlBfpWs35yTi%2FD0ePtuQ25sKv1m2obX6TIrEV%2FQyx3yikd2lnMw7A1AVpT%2F5z0tSwI0DMRzVq%2FVQZ0t3AMmpYDu2h%2Fhxqdbtmi0eBMSHsuZ9phWUPAkYFJUClg2asay6ydn%2B0qKMJRudmVQJlxvDmlpr3LZDBKwZHxE7Ea6D4wBuw90j7iB7eMbtnIx5OHqoThfjx0689z8E8u2tSTCi4UMsD7gkw5Yf0vAY6pgFM3%2B2FCO7Rb%2BWl6N5GVtY5%2FvBRViPxS%2B1GhFY6VDgn%2BL5cgxsSWWIA4xCQym4GJZEu8l59OvANDmZj6O3puTsa7fb6Ihg78l2UHWyl8gXWTutx5awa9C0fYrc%2FALk1GdiwtuLoEK9R%2BI0wVwfDaWDxP72U4h37pwQfcZEeQWpKGxoyinaIadB6WyrFa7zKHxaHLQvGgpd8hHpJASe98moM7lcgoAxu&X-Amz-Signature=22b5fb42a6917ccab5f4413292c475cfc4e7813850b98bc908fd3c3b9cacfa22&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 2. Scatter Plot
Scatter plots present the relationship between two variables in a dataset. It represents data points on a two-dimensional plane. The independent variable or attribute is plotted on the X-axis, while the dependent variable is plotted on the Y-axis.
**Syntax:**
```python
plt.scatter(x, y)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23708af9-659f-4f23-b626-1a4292d7842c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RQUBMKUP%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T171224Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIAtHQFbv%2F3qeRI7fyY1sUXKgmRJor3tltR0bYQsPMSiDAiAJI%2F8zgNAmgXfKxZ9EP5oy1uzy8YOd2fEOp%2FMwMIuqdSqIBAjC%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM08UShLwHVQU5zDkZKtwD1iZilh1%2FWOi%2BaByuZQpmNP9SE3SvU%2FHGSYFMuISuTBhOmOorKVXydALmORm5vJbDvuEg%2BHYwiMyQubDitHd%2FUkeU2NBj64xaLaG4iWeFfigClmSwNuil%2FoxjmCcKl6Y1HEzFPwWoZznB%2FVbXTAKJ0M%2BW2d5iHuAEWSSuSmR9I7p%2BJWGnY3qqXII88TAczlWTZbzmv%2Fu7hGygga7La6hMY9HjyW%2B%2FaPJ%2Bcd8PFPVLZ95TEjKyDWhF0EvGF9SOWcZ2VqLkdcD6oM0ShQWXTArHTqiFtqYGEMcBvErCWJmUETHv%2FxdUhRQOSXkiX62JNW1TN2xhOcdisHUBTQPq6D2EbMGAQtYxP3svdA%2F7pP5A0mKis7eRZC6Qbn6zJXQwmEol9ebGXVtuje4Kxr8ap5umHdQcnYViqcOVlBfpWs35yTi%2FD0ePtuQ25sKv1m2obX6TIrEV%2FQyx3yikd2lnMw7A1AVpT%2F5z0tSwI0DMRzVq%2FVQZ0t3AMmpYDu2h%2Fhxqdbtmi0eBMSHsuZ9phWUPAkYFJUClg2asay6ydn%2B0qKMJRudmVQJlxvDmlpr3LZDBKwZHxE7Ea6D4wBuw90j7iB7eMbtnIx5OHqoThfjx0689z8E8u2tSTCi4UMsD7gkw5Yf0vAY6pgFM3%2B2FCO7Rb%2BWl6N5GVtY5%2FvBRViPxS%2B1GhFY6VDgn%2BL5cgxsSWWIA4xCQym4GJZEu8l59OvANDmZj6O3puTsa7fb6Ihg78l2UHWyl8gXWTutx5awa9C0fYrc%2FALk1GdiwtuLoEK9R%2BI0wVwfDaWDxP72U4h37pwQfcZEeQWpKGxoyinaIadB6WyrFa7zKHxaHLQvGgpd8hHpJASe98moM7lcgoAxu&X-Amz-Signature=0a988f6a85a756b3885eef1365427a6837c9fd7fce40857a6f6df2af7d357781&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 3. Histogram
A histogram is an important visual representation of data in categorical form. To view the data in a "Binned" form, use the histogram plot with a number of bins required or with the data points that mark the bin edges. The x-axis represents the data bins, and the y-axis represents the number of elements in each bin.
**Syntax:**
```python
plt.hist(x, bins)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/24e4424a-df87-40a1-b63b-195cbdc2e0ab/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RQUBMKUP%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T171224Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIAtHQFbv%2F3qeRI7fyY1sUXKgmRJor3tltR0bYQsPMSiDAiAJI%2F8zgNAmgXfKxZ9EP5oy1uzy8YOd2fEOp%2FMwMIuqdSqIBAjC%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM08UShLwHVQU5zDkZKtwD1iZilh1%2FWOi%2BaByuZQpmNP9SE3SvU%2FHGSYFMuISuTBhOmOorKVXydALmORm5vJbDvuEg%2BHYwiMyQubDitHd%2FUkeU2NBj64xaLaG4iWeFfigClmSwNuil%2FoxjmCcKl6Y1HEzFPwWoZznB%2FVbXTAKJ0M%2BW2d5iHuAEWSSuSmR9I7p%2BJWGnY3qqXII88TAczlWTZbzmv%2Fu7hGygga7La6hMY9HjyW%2B%2FaPJ%2Bcd8PFPVLZ95TEjKyDWhF0EvGF9SOWcZ2VqLkdcD6oM0ShQWXTArHTqiFtqYGEMcBvErCWJmUETHv%2FxdUhRQOSXkiX62JNW1TN2xhOcdisHUBTQPq6D2EbMGAQtYxP3svdA%2F7pP5A0mKis7eRZC6Qbn6zJXQwmEol9ebGXVtuje4Kxr8ap5umHdQcnYViqcOVlBfpWs35yTi%2FD0ePtuQ25sKv1m2obX6TIrEV%2FQyx3yikd2lnMw7A1AVpT%2F5z0tSwI0DMRzVq%2FVQZ0t3AMmpYDu2h%2Fhxqdbtmi0eBMSHsuZ9phWUPAkYFJUClg2asay6ydn%2B0qKMJRudmVQJlxvDmlpr3LZDBKwZHxE7Ea6D4wBuw90j7iB7eMbtnIx5OHqoThfjx0689z8E8u2tSTCi4UMsD7gkw5Yf0vAY6pgFM3%2B2FCO7Rb%2BWl6N5GVtY5%2FvBRViPxS%2B1GhFY6VDgn%2BL5cgxsSWWIA4xCQym4GJZEu8l59OvANDmZj6O3puTsa7fb6Ihg78l2UHWyl8gXWTutx5awa9C0fYrc%2FALk1GdiwtuLoEK9R%2BI0wVwfDaWDxP72U4h37pwQfcZEeQWpKGxoyinaIadB6WyrFa7zKHxaHLQvGgpd8hHpJASe98moM7lcgoAxu&X-Amz-Signature=8280fd6afe0af075356c080e234c3c304b5246175573e7966f73e079cf2afa21&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ab5a6dfe-51f5-43ee-bcb3-33dae4a1c7ad/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RQUBMKUP%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T171224Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIAtHQFbv%2F3qeRI7fyY1sUXKgmRJor3tltR0bYQsPMSiDAiAJI%2F8zgNAmgXfKxZ9EP5oy1uzy8YOd2fEOp%2FMwMIuqdSqIBAjC%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM08UShLwHVQU5zDkZKtwD1iZilh1%2FWOi%2BaByuZQpmNP9SE3SvU%2FHGSYFMuISuTBhOmOorKVXydALmORm5vJbDvuEg%2BHYwiMyQubDitHd%2FUkeU2NBj64xaLaG4iWeFfigClmSwNuil%2FoxjmCcKl6Y1HEzFPwWoZznB%2FVbXTAKJ0M%2BW2d5iHuAEWSSuSmR9I7p%2BJWGnY3qqXII88TAczlWTZbzmv%2Fu7hGygga7La6hMY9HjyW%2B%2FaPJ%2Bcd8PFPVLZ95TEjKyDWhF0EvGF9SOWcZ2VqLkdcD6oM0ShQWXTArHTqiFtqYGEMcBvErCWJmUETHv%2FxdUhRQOSXkiX62JNW1TN2xhOcdisHUBTQPq6D2EbMGAQtYxP3svdA%2F7pP5A0mKis7eRZC6Qbn6zJXQwmEol9ebGXVtuje4Kxr8ap5umHdQcnYViqcOVlBfpWs35yTi%2FD0ePtuQ25sKv1m2obX6TIrEV%2FQyx3yikd2lnMw7A1AVpT%2F5z0tSwI0DMRzVq%2FVQZ0t3AMmpYDu2h%2Fhxqdbtmi0eBMSHsuZ9phWUPAkYFJUClg2asay6ydn%2B0qKMJRudmVQJlxvDmlpr3LZDBKwZHxE7Ea6D4wBuw90j7iB7eMbtnIx5OHqoThfjx0689z8E8u2tSTCi4UMsD7gkw5Yf0vAY6pgFM3%2B2FCO7Rb%2BWl6N5GVtY5%2FvBRViPxS%2B1GhFY6VDgn%2BL5cgxsSWWIA4xCQym4GJZEu8l59OvANDmZj6O3puTsa7fb6Ihg78l2UHWyl8gXWTutx5awa9C0fYrc%2FALk1GdiwtuLoEK9R%2BI0wVwfDaWDxP72U4h37pwQfcZEeQWpKGxoyinaIadB6WyrFa7zKHxaHLQvGgpd8hHpJASe98moM7lcgoAxu&X-Amz-Signature=a8c5650e89011005795af535955d0fe007cbda4a66c9d49dfefe4c1d1743f35c&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8f1b1d60-cf1b-42b3-9faa-f634c89c3f84/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RQUBMKUP%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T171224Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIAtHQFbv%2F3qeRI7fyY1sUXKgmRJor3tltR0bYQsPMSiDAiAJI%2F8zgNAmgXfKxZ9EP5oy1uzy8YOd2fEOp%2FMwMIuqdSqIBAjC%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM08UShLwHVQU5zDkZKtwD1iZilh1%2FWOi%2BaByuZQpmNP9SE3SvU%2FHGSYFMuISuTBhOmOorKVXydALmORm5vJbDvuEg%2BHYwiMyQubDitHd%2FUkeU2NBj64xaLaG4iWeFfigClmSwNuil%2FoxjmCcKl6Y1HEzFPwWoZznB%2FVbXTAKJ0M%2BW2d5iHuAEWSSuSmR9I7p%2BJWGnY3qqXII88TAczlWTZbzmv%2Fu7hGygga7La6hMY9HjyW%2B%2FaPJ%2Bcd8PFPVLZ95TEjKyDWhF0EvGF9SOWcZ2VqLkdcD6oM0ShQWXTArHTqiFtqYGEMcBvErCWJmUETHv%2FxdUhRQOSXkiX62JNW1TN2xhOcdisHUBTQPq6D2EbMGAQtYxP3svdA%2F7pP5A0mKis7eRZC6Qbn6zJXQwmEol9ebGXVtuje4Kxr8ap5umHdQcnYViqcOVlBfpWs35yTi%2FD0ePtuQ25sKv1m2obX6TIrEV%2FQyx3yikd2lnMw7A1AVpT%2F5z0tSwI0DMRzVq%2FVQZ0t3AMmpYDu2h%2Fhxqdbtmi0eBMSHsuZ9phWUPAkYFJUClg2asay6ydn%2B0qKMJRudmVQJlxvDmlpr3LZDBKwZHxE7Ea6D4wBuw90j7iB7eMbtnIx5OHqoThfjx0689z8E8u2tSTCi4UMsD7gkw5Yf0vAY6pgFM3%2B2FCO7Rb%2BWl6N5GVtY5%2FvBRViPxS%2B1GhFY6VDgn%2BL5cgxsSWWIA4xCQym4GJZEu8l59OvANDmZj6O3puTsa7fb6Ihg78l2UHWyl8gXWTutx5awa9C0fYrc%2FALk1GdiwtuLoEK9R%2BI0wVwfDaWDxP72U4h37pwQfcZEeQWpKGxoyinaIadB6WyrFa7zKHxaHLQvGgpd8hHpJASe98moM7lcgoAxu&X-Amz-Signature=93aa2a662f4932d8715df16a2628ad1d77d36e43775119ff6f226de6ac1cf05b&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/13ad0497-05fe-4eaa-984e-707b33e14761/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RQUBMKUP%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T171224Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIAtHQFbv%2F3qeRI7fyY1sUXKgmRJor3tltR0bYQsPMSiDAiAJI%2F8zgNAmgXfKxZ9EP5oy1uzy8YOd2fEOp%2FMwMIuqdSqIBAjC%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM08UShLwHVQU5zDkZKtwD1iZilh1%2FWOi%2BaByuZQpmNP9SE3SvU%2FHGSYFMuISuTBhOmOorKVXydALmORm5vJbDvuEg%2BHYwiMyQubDitHd%2FUkeU2NBj64xaLaG4iWeFfigClmSwNuil%2FoxjmCcKl6Y1HEzFPwWoZznB%2FVbXTAKJ0M%2BW2d5iHuAEWSSuSmR9I7p%2BJWGnY3qqXII88TAczlWTZbzmv%2Fu7hGygga7La6hMY9HjyW%2B%2FaPJ%2Bcd8PFPVLZ95TEjKyDWhF0EvGF9SOWcZ2VqLkdcD6oM0ShQWXTArHTqiFtqYGEMcBvErCWJmUETHv%2FxdUhRQOSXkiX62JNW1TN2xhOcdisHUBTQPq6D2EbMGAQtYxP3svdA%2F7pP5A0mKis7eRZC6Qbn6zJXQwmEol9ebGXVtuje4Kxr8ap5umHdQcnYViqcOVlBfpWs35yTi%2FD0ePtuQ25sKv1m2obX6TIrEV%2FQyx3yikd2lnMw7A1AVpT%2F5z0tSwI0DMRzVq%2FVQZ0t3AMmpYDu2h%2Fhxqdbtmi0eBMSHsuZ9phWUPAkYFJUClg2asay6ydn%2B0qKMJRudmVQJlxvDmlpr3LZDBKwZHxE7Ea6D4wBuw90j7iB7eMbtnIx5OHqoThfjx0689z8E8u2tSTCi4UMsD7gkw5Yf0vAY6pgFM3%2B2FCO7Rb%2BWl6N5GVtY5%2FvBRViPxS%2B1GhFY6VDgn%2BL5cgxsSWWIA4xCQym4GJZEu8l59OvANDmZj6O3puTsa7fb6Ihg78l2UHWyl8gXWTutx5awa9C0fYrc%2FALk1GdiwtuLoEK9R%2BI0wVwfDaWDxP72U4h37pwQfcZEeQWpKGxoyinaIadB6WyrFa7zKHxaHLQvGgpd8hHpJASe98moM7lcgoAxu&X-Amz-Signature=68bbdee03366acbe07391963b0d82e59116201c8074ca2a86ecbbc8d4e821f66&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 2. Box and Whisker Plot
A box plot shows the distribution of quantitative data in a way that facilitates comparisons between variables or across levels of a categorical variable. The box shows the quartiles of the dataset while the whiskers extend to show the rest of the distribution, except for points that are determined to be "outliers".
**Syntax:**
```python
sns.boxplot(x='header_1', y='header_2', data=df)
```
**Example Output:**


![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d207ae92-0a7c-4e2f-aa65-0ee5a2c33bf7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YM6WVHVG%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T171225Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDrX4G%2BY8jR9mYpRQNv2NTzdnPhBj8%2BFdQHReCNFFG%2FZAIhAJnWfDraq00HTNQT%2B1MCycaVaxmTrWlP2CJReJReEwrtKogECML%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxqyKHhPWPKQWVkHecq3AO2B%2B9rJdooGJjk4MRQwIytwU%2Fhj%2Fk9SmOQ5MoGPAFpSRbyhUNgbWvh4xel1af3osO1IdFYspE%2BZR%2Bx1W%2BQzuONTRdv%2FFbm6SEbD1YA5R%2BbO41XQxbJLky7GXX4uX1kB1sFZ02HNjup1QOXntORKCKkZq52KahlRKZxICO8LS6G0xeylmqp%2B%2Fll7uftQUrcBfo%2B7LPC4Kewf%2F3JN4ASrwlynI6gJutGCfZ3IA1JAJVDtoIiMOHpmfTIazHgqP9Bh84UwYK6v9za2ThEc8GbSAFLYk6X5NWMyKIl76FhnkZQC8EslVkmbJLpSnfhVWXaizmNNqeL5vJByWjTHzZdxntlK%2FxsjeqOl7RxXIlJMpZqticoIjPVOiAifFjOJ1Qhj7ouNUtdfDoyTSXF%2FvM8sHcOC95K%2FjamyJaEmabNj1Nt2zfWA5prNCcvn6jtBi54f4fzgCvkfglZdh%2FZyQwZG8H4QSWPvHJbk6Ih8HLipQkWIQW5yfsFpufyxstr%2BmZmyvfIZjeO5WAzrsLU0Iu%2FtEMwtadFupNka0RlZROCkV2xDAG6wdxOa0KsmtfmLXEgMQUU9h73Me8msWiDC7AMRT2RQUI6YQfme6Y8KVHyqEmBwasnhlZLrMfh5Bb37TDsh%2FS8BjqkAbd07c7kmcURidnH7gucgLHKGwLvTzKvggMPZLoj2NvNB450EGr5YHnkz5qflSrmZACDD99d9NUeEzao0Slp0vlh0KCTFkTeV13VqeZgj25OFcJ9SWP%2FUF6WvdAjofkELtc9n3z3R0vIdvcMsnz2iJSHqY6bmA8AQQ9DcAbE44PZdSFc48fIUaWtBgsqh%2FuhdYrnkrLRDotz%2F%2B2ca6%2FQxzvzLfu7&X-Amz-Signature=03aa465645e36e28f573a7d272adef2df42b4a6114d13807b2fa0f1c7f1a1051&X-Amz-SignedHeaders=host&x-id=GetObject)

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0e516edc-7551-4792-ab18-0494db3c4c0c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663MFMAGGO%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T171225Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDpYRI0rqN8VkSa48OvCdp2Bu6TwDhW8ByMjYtQeQaYEwIgZvQull3BsPLJsWkt206fn1I0%2BmKMim7%2FU%2BRoySBArysqiAQIwv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDEjtzmkUOtkvHYdELCrcA050Eu4iZaGeUf3PrhZeefZ7A7ahIhod9HDTT5xlJVELLjxAqpINbtF0K723X7jBHQQbFTfdkH0bOCQHWtfNmbUg55puJib4vCU3MDVShoJZFnuNSQPe1xkTW3FmSw71Rt4pts0CFQhLLSGft9MvDlm9eWoHXd%2FqO6NNtF4DNUsblHewPUFitg%2FyuNjxKjEg%2Fmgr04vM%2B6rTs5L0oM0h9RCsXoeJj7eQ9MVE5VB6G%2FhGJDQ3DU5BvAz6WrKi3xidJP7Kf1S%2BSnvFN2Fp08TB7fd9CXXjlUbgjgt4PetLDrl%2Bx0XZ5PVYXEvs5SjgQ5Dx1lbnQbT%2BuDGxnvlUxZM2UWhvb1DeSiES0sY8z0A4%2B0yoXbQGtPzaBW6fb7nKA%2FSuHhPXFOfG2qU4rohH5HKgZ7%2Bz6czdhls2Jo2j0Zb%2BUReRWNXcgOqelqonCAdn3w8WPKoUDSxpBnbjAQbqdLQcTKFdpCyI9%2BtkAEVnmGhP%2B9neM3vf8m19i3T1TTvvU2rU6%2Fz4XsPyYLlW%2BtvcPB8qA4TfmfnsU6FFqb%2Fhnhi5uThxx5jg0f8delvvNemCanGOUMn3lfG9eTtc45pQgNgYX76eF1YI3UDSP%2BSjNH1ksfC%2FQQ0acazptVJ%2Bsjl9MIyI9LwGOqUBiLzQCu9EDss8%2FUAT3j6pfQ4A%2BBAQt1t4oMFjP%2BxqKJIUcRHyDFHZM28QJ6okYAdpPHdBfcFqYooEFCz0jLjiuMzJCfaq7IVeNxhVAEGsreBTzaC5rUFO65tnCJDfqIhTu8ItEMnaqrTZtAZN%2BVRGHC9w9s7bgOI2uLA3gteWY4WPPjJC1x8wcfrx%2Bq6ztm3H0gaaTaQSkvou3XrgTRSmZWxKtEn3&X-Amz-Signature=c80c9cd1ea34a2ddb140c496a6031d11e18d0fb7108df6436932c89168ffc4b6&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23a79b9d-2356-49a9-8fd9-65c6b0ab2cc5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RQUBMKUP%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T171224Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIAtHQFbv%2F3qeRI7fyY1sUXKgmRJor3tltR0bYQsPMSiDAiAJI%2F8zgNAmgXfKxZ9EP5oy1uzy8YOd2fEOp%2FMwMIuqdSqIBAjC%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM08UShLwHVQU5zDkZKtwD1iZilh1%2FWOi%2BaByuZQpmNP9SE3SvU%2FHGSYFMuISuTBhOmOorKVXydALmORm5vJbDvuEg%2BHYwiMyQubDitHd%2FUkeU2NBj64xaLaG4iWeFfigClmSwNuil%2FoxjmCcKl6Y1HEzFPwWoZznB%2FVbXTAKJ0M%2BW2d5iHuAEWSSuSmR9I7p%2BJWGnY3qqXII88TAczlWTZbzmv%2Fu7hGygga7La6hMY9HjyW%2B%2FaPJ%2Bcd8PFPVLZ95TEjKyDWhF0EvGF9SOWcZ2VqLkdcD6oM0ShQWXTArHTqiFtqYGEMcBvErCWJmUETHv%2FxdUhRQOSXkiX62JNW1TN2xhOcdisHUBTQPq6D2EbMGAQtYxP3svdA%2F7pP5A0mKis7eRZC6Qbn6zJXQwmEol9ebGXVtuje4Kxr8ap5umHdQcnYViqcOVlBfpWs35yTi%2FD0ePtuQ25sKv1m2obX6TIrEV%2FQyx3yikd2lnMw7A1AVpT%2F5z0tSwI0DMRzVq%2FVQZ0t3AMmpYDu2h%2Fhxqdbtmi0eBMSHsuZ9phWUPAkYFJUClg2asay6ydn%2B0qKMJRudmVQJlxvDmlpr3LZDBKwZHxE7Ea6D4wBuw90j7iB7eMbtnIx5OHqoThfjx0689z8E8u2tSTCi4UMsD7gkw5Yf0vAY6pgFM3%2B2FCO7Rb%2BWl6N5GVtY5%2FvBRViPxS%2B1GhFY6VDgn%2BL5cgxsSWWIA4xCQym4GJZEu8l59OvANDmZj6O3puTsa7fb6Ihg78l2UHWyl8gXWTutx5awa9C0fYrc%2FALk1GdiwtuLoEK9R%2BI0wVwfDaWDxP72U4h37pwQfcZEeQWpKGxoyinaIadB6WyrFa7zKHxaHLQvGgpd8hHpJASe98moM7lcgoAxu&X-Amz-Signature=e2dc3335d2b92a0417f0bf541bfcf97e5ac4fea0d9224c5291edfc9728883162&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 4. KDE Plot
A Kernel Density Estimate (KDE) plot is a graph that creates a probability distribution curve for the data based upon its likelihood of occurrence on a specific value. This is created for a single vector of information.
**Syntax:**
```python
sns.kdeplot(X) || sns.kdeplot(df['age'])
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0d571213-2a2f-4921-a50b-880847aa05ee/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RQUBMKUP%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T171224Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIAtHQFbv%2F3qeRI7fyY1sUXKgmRJor3tltR0bYQsPMSiDAiAJI%2F8zgNAmgXfKxZ9EP5oy1uzy8YOd2fEOp%2FMwMIuqdSqIBAjC%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM08UShLwHVQU5zDkZKtwD1iZilh1%2FWOi%2BaByuZQpmNP9SE3SvU%2FHGSYFMuISuTBhOmOorKVXydALmORm5vJbDvuEg%2BHYwiMyQubDitHd%2FUkeU2NBj64xaLaG4iWeFfigClmSwNuil%2FoxjmCcKl6Y1HEzFPwWoZznB%2FVbXTAKJ0M%2BW2d5iHuAEWSSuSmR9I7p%2BJWGnY3qqXII88TAczlWTZbzmv%2Fu7hGygga7La6hMY9HjyW%2B%2FaPJ%2Bcd8PFPVLZ95TEjKyDWhF0EvGF9SOWcZ2VqLkdcD6oM0ShQWXTArHTqiFtqYGEMcBvErCWJmUETHv%2FxdUhRQOSXkiX62JNW1TN2xhOcdisHUBTQPq6D2EbMGAQtYxP3svdA%2F7pP5A0mKis7eRZC6Qbn6zJXQwmEol9ebGXVtuje4Kxr8ap5umHdQcnYViqcOVlBfpWs35yTi%2FD0ePtuQ25sKv1m2obX6TIrEV%2FQyx3yikd2lnMw7A1AVpT%2F5z0tSwI0DMRzVq%2FVQZ0t3AMmpYDu2h%2Fhxqdbtmi0eBMSHsuZ9phWUPAkYFJUClg2asay6ydn%2B0qKMJRudmVQJlxvDmlpr3LZDBKwZHxE7Ea6D4wBuw90j7iB7eMbtnIx5OHqoThfjx0689z8E8u2tSTCi4UMsD7gkw5Yf0vAY6pgFM3%2B2FCO7Rb%2BWl6N5GVtY5%2FvBRViPxS%2B1GhFY6VDgn%2BL5cgxsSWWIA4xCQym4GJZEu8l59OvANDmZj6O3puTsa7fb6Ihg78l2UHWyl8gXWTutx5awa9C0fYrc%2FALk1GdiwtuLoEK9R%2BI0wVwfDaWDxP72U4h37pwQfcZEeQWpKGxoyinaIadB6WyrFa7zKHxaHLQvGgpd8hHpJASe98moM7lcgoAxu&X-Amz-Signature=9c1bba5ed4faf6d000071bc566530a918fb7dc85c5d2aa74c59e80ebb285676b&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/53752550-ef82-4ca9-a01a-09921f0282d0/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RQUBMKUP%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T171224Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIAtHQFbv%2F3qeRI7fyY1sUXKgmRJor3tltR0bYQsPMSiDAiAJI%2F8zgNAmgXfKxZ9EP5oy1uzy8YOd2fEOp%2FMwMIuqdSqIBAjC%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM08UShLwHVQU5zDkZKtwD1iZilh1%2FWOi%2BaByuZQpmNP9SE3SvU%2FHGSYFMuISuTBhOmOorKVXydALmORm5vJbDvuEg%2BHYwiMyQubDitHd%2FUkeU2NBj64xaLaG4iWeFfigClmSwNuil%2FoxjmCcKl6Y1HEzFPwWoZznB%2FVbXTAKJ0M%2BW2d5iHuAEWSSuSmR9I7p%2BJWGnY3qqXII88TAczlWTZbzmv%2Fu7hGygga7La6hMY9HjyW%2B%2FaPJ%2Bcd8PFPVLZ95TEjKyDWhF0EvGF9SOWcZ2VqLkdcD6oM0ShQWXTArHTqiFtqYGEMcBvErCWJmUETHv%2FxdUhRQOSXkiX62JNW1TN2xhOcdisHUBTQPq6D2EbMGAQtYxP3svdA%2F7pP5A0mKis7eRZC6Qbn6zJXQwmEol9ebGXVtuje4Kxr8ap5umHdQcnYViqcOVlBfpWs35yTi%2FD0ePtuQ25sKv1m2obX6TIrEV%2FQyx3yikd2lnMw7A1AVpT%2F5z0tSwI0DMRzVq%2FVQZ0t3AMmpYDu2h%2Fhxqdbtmi0eBMSHsuZ9phWUPAkYFJUClg2asay6ydn%2B0qKMJRudmVQJlxvDmlpr3LZDBKwZHxE7Ea6D4wBuw90j7iB7eMbtnIx5OHqoThfjx0689z8E8u2tSTCi4UMsD7gkw5Yf0vAY6pgFM3%2B2FCO7Rb%2BWl6N5GVtY5%2FvBRViPxS%2B1GhFY6VDgn%2BL5cgxsSWWIA4xCQym4GJZEu8l59OvANDmZj6O3puTsa7fb6Ihg78l2UHWyl8gXWTutx5awa9C0fYrc%2FALk1GdiwtuLoEK9R%2BI0wVwfDaWDxP72U4h37pwQfcZEeQWpKGxoyinaIadB6WyrFa7zKHxaHLQvGgpd8hHpJASe98moM7lcgoAxu&X-Amz-Signature=ed42f85c41584cfe4985347cb6021eb5593ee9fd53a8ff46452d533a2b9eb1c1&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
## 4. Correlation Between Variables
Correlation is a statistical measure of the extent to which different variables are interdependent. It indicates how changes in one variable are associated with changes in another variable over time.
### Positive Correlation
Positive correlation indicates that as one variable increases, the other variable also tends to increase.
**Example: Engine Size and Price**
- **Positive Correlation:** Engine size increases, price also increases.
- **Visualization:** Scatter plot with a steep positive slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c7ea9b0-3ef3-4357-a9c3-554fc71b6b15/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665YEOBENO%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T171225Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDH4nNBTffz3BVyZip5Hiv7nHlKGCI%2BP26vISe6%2F%2Bu%2BfQIhAIkINnhheoF2aPe1vfPeYNsmY%2BwAxBYSbX1SIg%2FWECs5KogECML%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwyxTAO9LXJID7I2fIq3AMILpTCbT2LHFoVy97UC13mFAgH3b0BhPvX05SIs8c3j%2BHWeoAkOXA2bgc5adXbmXttEBJkofcBffCiBCYPjIUOlZ%2B57qddGxc1c0ePuNtC1D5szKjfuD0OlqXNVlJPXOBRbByAmRNh7Jvx0vFJPZR8F%2FeBeB6K03IKJs8pUXjrIJ3Bk0UK1ATjZNKV0mE35yoX%2F3ecJZM77CMnH33scZUO1HBY%2Fm7sZMNYn4P0GFdP7miHHUdip9MZzGw2pcyKqDlYa5xnO0SSdcZDmrdV0JLO71buY5New1EXJT%2Fk%2FChpgl69%2BP3K%2B%2Ba3ZXMwVQt5gSYG%2FnZ%2BYp4GqMQSWMz2OfoUs0Bhj1tL1bfRRoND0eNrhCGR9kST9I%2FIPmLG90iBkRp1zDlJ2sVNvMsFTtTg3nvl2E%2FrVaroCEWYILO3SF2lWScfEbSfjknOAf4m%2BkmZvfQIXU1zhvZ6WTT7dTYGzOZgvo7WE1XdKnuFgaCPScRU7jt%2FO3IYjzN46hKzbIrT0g%2FXHS6lg0EnYMHy399nKfv8JHrHN3uKqYlkyiBM23vnCbbHX66w75sgLVviVVxaoOXjiNPoxtoAfwIf5mDXyMIpxa7eLznN%2FkWja30JPVKo3oRl5sXVxwQCMwfCETDkh%2FS8BjqkAbd8rXI57Px4owrRKzs5L2k99j3vw4cPbeqPnA3TXEggppPAIX21woc1%2BubxldBFfIr9%2FWAcKF5mgF2JFmlLyVPzlIWo%2B%2B7cax7NcMVj0AiBahLJ6bb9MNdvCL35AJhiOOM%2F8TfGTx8vaYyIJ6JtXJn3lLuyLsX0VMKT4uKqU6e8G2w9YygLSFPrcO8TkifiyyfmfYsFayHk8g0db97rsGBZE%2FIE&X-Amz-Signature=441dcb06518fa7452030a6d4e2a033fa6e58e7449b044672f2aa484c8776dcce&X-Amz-SignedHeaders=host&x-id=GetObject)
**Explanation:** When engine size increases, there is a corresponding increase in the price of the vehicle. This positive correlation suggests that larger engines tend to be associated with higher prices in the market.
___
### Negative Correlation
Negative correlation indicates that as one variable increases, the other variable tends to decrease.
**Example: Highway Miles per Gallon and Price**
- **Negative Correlation:** As highway miles per gallon increases, price decreases.
- **Visualization:** Scatter plot with a steep negative slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/10f1f798-9cc4-4df2-a9c1-5a339f554a0b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466S5TTD6EZ%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T171225Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCpKgfsS%2FiFiLWykSAr4d%2BkfaVtjwREDJF5y%2BNLbUiLCQIhAIknmGwOPJ67IApJ9tsvf4CPz%2B5QMCg9pRH4yDOu67yiKogECML%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igw9McotAh1Dko8c4E0q3ANze5FViUu5CzTueFVpLN6L1iFv8s5BROZIf1JKrL9oKsIsJt24JoNYh%2BAs3JzyXqSEkKgcxhztF%2FthmfSEAaIUSa%2BmJ4gSeRwnMXjJ%2BN9cVNoUGHxMnbJBIMQP9zBRew2woQrQJ2SZuzmUZ33q0lRVmp%2F6ZsgxHNSPeEgN2cz%2FhYWjHAsUQCRQwmnJRi3sa2rR6icDS5sK4rPZyhxXKOacBcQUK1Ma9%2B5cUYl%2BtpMTXefSZyHdzoD9Ux0MPtN%2BAh2fKHvYmhYP39JjDi1qnjBq4kSI8Hj9MgvY%2FdYbNBhN3R6YAo%2BPNc%2BwosimVG5pJmw6Ajf4lnpuZ0ELUnw4babbH3EiQ%2Fll0fkrv0CjSkp391o%2FTbpMsJuGN3UnlwWhXEyFKWYJnI1Z5EUrvIptU4QVi%2BZ8LefXqf8Oq9dcHiCvVd%2FyRWaLz1OGX5Eudao5tGK67piK1OGNlz72glojqIJgnkBGmLpixF40bbELG6awLLVPj2zIwrqt2pqBWv3WN0P1S%2Fk%2FIoTS1z5UiwdQ7zm%2Fx4qj731jo8mzKXlNL9gzyUWf%2Blo7XqZyeAgbMN8mUqo8UP8EB1qkLNs9zxpEXJfbAygOkhCCCnDbrM0tjttO%2F8nnUVNaiMsAPhKzajDmh%2FS8BjqkAfhSaliNCBdf9xWX1cLJs7CRuq3WBRWW5V25HSfxxwMd3yEbiS9ImSrRIztk51rUTeGGDBa%2Fr7TaQBbFSeW6NUwG5nrS6nleIc0ic7k5GiEABGPBxJNsa3h%2FrFhJmtix8UhgHCt9UYivvLnXqZ5TVaj36yhSCnihEkLDarWRpH%2F0zsfjSAsuo9ddzZECyA5CJApeO1Vscu3y1xvlLSwdRzJ9u3xT&X-Amz-Signature=cf8b0c3b34fafa951b1e84b66192d3e95e84f5a78b1df2d987604e3dfab895bf&X-Amz-SignedHeaders=host&x-id=GetObject)
**Explanation:** When highway miles per gallon increases, the price of the vehicle tends to decrease. This negative correlation suggests that cars with higher fuel efficiency (more miles per gallon) are generally priced lower in the market.
___
### Weak Correlation
Weak correlation indicates a lack of strong relationship between the variables.
**Example: RPM and Price**
- **Weak Correlation:** Low and high RPM values show varied prices, indicating no strong predictive relationship.
- **Visualization:** Scatter plot with no clear trend or slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9f914514-8914-4bf4-ac84-d9e3077f6eb1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663WPXJMQF%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T171225Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCTkjYcAiT%2B7wdKvwlfGE9RS0IUrubEA3pzDM4yXxVgsAIhAMHvdfii3TDKHxjguVVHoSX8g6kNiVbcCyuYkVjsndwXKogECML%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igzgztic7SsCWMuurLcq3AO%2FFNDNuPEGwQ3RBzaZpbEflVNgNq%2FlFQpdKtafoOSN1Ps1jG3%2FaY8AGT2dqlT9wRs4ZnqdYgA%2FiNXkndZ0vuTju41SLRng9fIzMXL4P%2FGS1n6Jg0XoXO9zbF%2Fdl7aRA2%2B%2BHyuGVgNg3DdBQtSpRLsI7PDoXBmvXizoq8Mt8k%2Bi5V46LC2dz6Tyi9bkm4DXYhVPG6rBBAikxY%2F%2B%2FiWyI5yfocpFrUJeYfgr60d4JrjiiuMe4%2B6m9wXpamDyt7Fl8NPRjDPEZPwMLSDCbF1%2FcDgCK8qnyPweND%2Fw%2FuVspfT3wJ8hkFffizT3x8glQWHJvdI69nkFiqPrfZHxKngMskxOfbJekpmdPjVI2QACYbWHe%2Bu1fVR5V3iWsYNxsI11uBhKyQmr7w2W528MkrWlqeOoErFxJ79nIfGQ28xz0K3akSNmXNzU191VCglkQDge0veetyWVKeADW9SuVTsKP12SN0A0FtMg95vTjewO0cX6u8HzhW5NIs5aO9rvxtCW1vWRaSSxswayKQLFKZ3DFTAwTQBfcjD3q2CNBKzJVYN4z3dkaGlf7kuf%2FPQeLsUuE0p4MsRdnSYxTAJZEzZXFGluioQDRBJFvU1K%2FVnvgT1224vNsP%2BFh9fvA8mo%2FDDWh%2FS8BjqkAYDaY4VsqTcak8NW7rdTBMSYQEM9pV7et5CynfFIyfGb93XlLtmCTZ9oFA7OxlvFthjwcsi32SCUdEs245EySHmUaZHkx%2F7bg6ZD4hMbe%2FXvFzihvhs0tDcAAdaa0xAfyse%2FaWa3e6i4kaXZNU%2B6Jvxz%2FR%2Foqlizqvi2MB9DbIBQvo3XK3ywCVvtYQ6bVmbHSixuXrJIpHf9RWC0YNJODuTtB2mk&X-Amz-Signature=0bf0ca3f4e15911f59c52bf0612344eaca9d5645cad401b2e8b1faacb103b0db&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f18086e5-5b04-4fbf-8309-8944ab20d213/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667NADD2EU%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T171225Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHCnW8KWP1KfZMtgkmF4iCUn%2BOnhoj5wJXNyGjHHXBAvAiBO4zGAURisIOyNfRT5frWRNZA5mfwn39Ff3OO9mDIZ6SqIBAjC%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMpdE%2FLHE941FlryiiKtwDFVJZ5lvmQbM0tMHvQKau24bpndVzPnq1HLaZkAXAgw1b%2Be84UREAA3kctoDuA%2BVxJsgYzoNJlBripvylQN9vWisrD62%2FIZU3cxGkpw4ES6X%2F%2B5QUKs0Qenjc5ekcXstOUqnlnJpOClgkPWYo3b1ATIsfgwwLhOg1KXyt%2B2ICSvyLaDb4On8AXdrTF%2Bg3g8Erlnph4NSCJXOxm7b63iQGt9XJWaik20AWygYVTstJYVbbKx8wXP0kI6foMx22Zqv62fMHicawGeC2Ye2lFNOL%2B%2FhhAk4GUgexvNsp20FsOnH2%2BQaXtkUYAu%2B%2BhhcPV%2Bv0nW6WAAXB%2F%2Bzqfk5HZm5TmxIdFHqdBvOd1LrkZBOCjdXfHUBZbRZtlCpdW70vdSSKUSLRsVcIkfgfmpz5czbM%2ByL9RPD5Q%2FDIHJGG7BHiY1HdhdmOpXYufGQlR6Ue5TU%2Fa2PD1J3o7OD0mVshrnHQ5MXke1E1aK9vA5qbhNNRH9Om7Zwh9mbH9Fs3Nu9jy%2F%2BsKYSaCBTBsjNgr132hPNVV8LOTKOOB7FnpHR2vmdPv0V0Tra3ifC32I%2BYXnNsSLPDGoJ1oZ%2FU%2F8BGRysBUGVe11VI1oArz5sJCqonVyQfCROWHIio5pl7WL79DyUw5of0vAY6pgGr4oG97HFj%2FX%2BAp3%2FT871l%2FfEYwoIpOvi5waNaHpEXJyyp28cRRD82vn0dbd3GFDg4qAXZchfk76FOq9ICyreVsHF80tZhI1f9Ki1QsKPLHAJ0IhaDzixeJRXcNixr%2FYk3BJVVfSGsPJOrw0VcEdl9TUCFbdm1lsVsOZGqSOIRWVlCL9geOhUTHFrFByTR6xClb1upjfC3iK6ZNHguzGFcnXiaG0o3&X-Amz-Signature=e44532b58ca833d7ab6d95ca9ffb29d61a7898d3bf265437e7f9cf3521cb081f&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Correlation Plot
Heatmap visualizes correlations among variables. Color scheme indicates Pearson correlation coefficients. Dark red diagonal line shows perfect correlation (value of 1) between variables and themselves.
This heatmap offers overview of variable relationships and their link with price.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cd3b341e-cc1a-45f7-8aec-cdc00436d270/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667NADD2EU%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T171225Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHCnW8KWP1KfZMtgkmF4iCUn%2BOnhoj5wJXNyGjHHXBAvAiBO4zGAURisIOyNfRT5frWRNZA5mfwn39Ff3OO9mDIZ6SqIBAjC%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMpdE%2FLHE941FlryiiKtwDFVJZ5lvmQbM0tMHvQKau24bpndVzPnq1HLaZkAXAgw1b%2Be84UREAA3kctoDuA%2BVxJsgYzoNJlBripvylQN9vWisrD62%2FIZU3cxGkpw4ES6X%2F%2B5QUKs0Qenjc5ekcXstOUqnlnJpOClgkPWYo3b1ATIsfgwwLhOg1KXyt%2B2ICSvyLaDb4On8AXdrTF%2Bg3g8Erlnph4NSCJXOxm7b63iQGt9XJWaik20AWygYVTstJYVbbKx8wXP0kI6foMx22Zqv62fMHicawGeC2Ye2lFNOL%2B%2FhhAk4GUgexvNsp20FsOnH2%2BQaXtkUYAu%2B%2BhhcPV%2Bv0nW6WAAXB%2F%2Bzqfk5HZm5TmxIdFHqdBvOd1LrkZBOCjdXfHUBZbRZtlCpdW70vdSSKUSLRsVcIkfgfmpz5czbM%2ByL9RPD5Q%2FDIHJGG7BHiY1HdhdmOpXYufGQlR6Ue5TU%2Fa2PD1J3o7OD0mVshrnHQ5MXke1E1aK9vA5qbhNNRH9Om7Zwh9mbH9Fs3Nu9jy%2F%2BsKYSaCBTBsjNgr132hPNVV8LOTKOOB7FnpHR2vmdPv0V0Tra3ifC32I%2BYXnNsSLPDGoJ1oZ%2FU%2F8BGRysBUGVe11VI1oArz5sJCqonVyQfCROWHIio5pl7WL79DyUw5of0vAY6pgGr4oG97HFj%2FX%2BAp3%2FT871l%2FfEYwoIpOvi5waNaHpEXJyyp28cRRD82vn0dbd3GFDg4qAXZchfk76FOq9ICyreVsHF80tZhI1f9Ki1QsKPLHAJ0IhaDzixeJRXcNixr%2FYk3BJVVfSGsPJOrw0VcEdl9TUCFbdm1lsVsOZGqSOIRWVlCL9geOhUTHFrFByTR6xClb1upjfC3iK6ZNHguzGFcnXiaG0o3&X-Amz-Signature=121b99c070b9856deb3dbc0c9fd4e8b64485a5c0b853e720a7fd7e9e55162e12&X-Amz-SignedHeaders=host&x-id=GetObject)

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
