

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7e6d594d-952e-44b6-97ea-31225882aea6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VTTABGKT%2F20250128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250128T201547Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHQaCXVzLXdlc3QtMiJHMEUCIDGdWlJj%2BOmVNcbFxnRB3HZ8BCscJb7lumGDhNaw3OLcAiEA2VN%2BhMTm6QofayIvK1E8iJlgLfakwV3SyjOX3U5ke6Aq%2FwMIfRAAGgw2Mzc0MjMxODM4MDUiDHeV8q8lF2JoWh1eiircAzPIs09LAr0kFGGfx3Qk7V5IWFbrv7gsxyR%2F3WoL7%2FpYqP1yXsOEpmDozFtj6bwr%2BeUKdACoaiLPtTYRKJGHcbwQpS0zFKeaa%2BxPChSO3yIgHQsAM8cspwaIJbsU50GE7vIoHUUHMuYYbbRZQg9YT6gxPNMrP9%2FTTrLaopo8yiysWZG8GdW8Mh5jWBgcMe%2Fm%2BUn2vAbDjL0EKw6%2FIQXyVpfnxN7e9ZpknyiN%2Fnme5YQu%2BbHAL1jqbBnRyzYd5jxHXPrUwTDut5f0K1mBDj6bV9Wp54Itx1gIt%2FVR0GU4ZONCuunUyUM7Mvky8o3XDhVFH9meU%2FL8NMB5q9W1f3dPhKG5ACafE0aOcLbhMU1ED6vrTy%2FmGB4EOUQRyTOzDePo3anBnjfXf%2FrRF9LXRiqN0KU4j1YUWmU5LCv1yggJy8ZBh%2BeKYAPu%2Bm6oFMehdvK7WMDN7wAocrlGsVffaXgBBW2Fv4XVt2QAQvXHMJDDvZ4z4PVppmYMTT4rklsTTyN6Q82AHU5PzTsE7U3HxNw0TX6Y0jSKdx5%2B0UiSaCCyselCoKLBQ6l6IaeTApWuW48n1YkGzBXjmwgFxYeL4zWoMrlAdmHF68HfmymK8lxMrZosT31G%2BUtvJfE%2BK6egMMfp5LwGOqUBHrAspaLRys2JDx%2BbO3P4FWFYd9FeiZiZoPfegrH%2FUP2kZbERoYABHJEM0OENDigWwr7cHa4h1SslAejQtd3doNl6%2Fu2zr5YMSnjimxqM5uZL47R1Hufhg20sNr6wEA3Vs7EDW%2FB%2B7Ku5dzZKJF7vLjZmk5elqyvNmND%2Fas1zdbnrTYhUPs%2FZ7OYzer4lxsc3LHQHLx50%2F6IuE2H5A5zqzlLhHLza&X-Amz-Signature=84c0127f8f140c657984a5e2241c9d76f0baa9d6f089dd7c4de649e586b5856d&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cbfaed9e-b398-4902-8936-dea058b21def/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VTTABGKT%2F20250128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250128T201547Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHQaCXVzLXdlc3QtMiJHMEUCIDGdWlJj%2BOmVNcbFxnRB3HZ8BCscJb7lumGDhNaw3OLcAiEA2VN%2BhMTm6QofayIvK1E8iJlgLfakwV3SyjOX3U5ke6Aq%2FwMIfRAAGgw2Mzc0MjMxODM4MDUiDHeV8q8lF2JoWh1eiircAzPIs09LAr0kFGGfx3Qk7V5IWFbrv7gsxyR%2F3WoL7%2FpYqP1yXsOEpmDozFtj6bwr%2BeUKdACoaiLPtTYRKJGHcbwQpS0zFKeaa%2BxPChSO3yIgHQsAM8cspwaIJbsU50GE7vIoHUUHMuYYbbRZQg9YT6gxPNMrP9%2FTTrLaopo8yiysWZG8GdW8Mh5jWBgcMe%2Fm%2BUn2vAbDjL0EKw6%2FIQXyVpfnxN7e9ZpknyiN%2Fnme5YQu%2BbHAL1jqbBnRyzYd5jxHXPrUwTDut5f0K1mBDj6bV9Wp54Itx1gIt%2FVR0GU4ZONCuunUyUM7Mvky8o3XDhVFH9meU%2FL8NMB5q9W1f3dPhKG5ACafE0aOcLbhMU1ED6vrTy%2FmGB4EOUQRyTOzDePo3anBnjfXf%2FrRF9LXRiqN0KU4j1YUWmU5LCv1yggJy8ZBh%2BeKYAPu%2Bm6oFMehdvK7WMDN7wAocrlGsVffaXgBBW2Fv4XVt2QAQvXHMJDDvZ4z4PVppmYMTT4rklsTTyN6Q82AHU5PzTsE7U3HxNw0TX6Y0jSKdx5%2B0UiSaCCyselCoKLBQ6l6IaeTApWuW48n1YkGzBXjmwgFxYeL4zWoMrlAdmHF68HfmymK8lxMrZosT31G%2BUtvJfE%2BK6egMMfp5LwGOqUBHrAspaLRys2JDx%2BbO3P4FWFYd9FeiZiZoPfegrH%2FUP2kZbERoYABHJEM0OENDigWwr7cHa4h1SslAejQtd3doNl6%2Fu2zr5YMSnjimxqM5uZL47R1Hufhg20sNr6wEA3Vs7EDW%2FB%2B7Ku5dzZKJF7vLjZmk5elqyvNmND%2Fas1zdbnrTYhUPs%2FZ7OYzer4lxsc3LHQHLx50%2F6IuE2H5A5zqzlLhHLza&X-Amz-Signature=ee86af0e5500917b8ad2afe851a69a7350ea095946ad38a3f853f2b20036b61f&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/91181646-b1e0-4433-9711-6259a96a9247/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VTTABGKT%2F20250128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250128T201547Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHQaCXVzLXdlc3QtMiJHMEUCIDGdWlJj%2BOmVNcbFxnRB3HZ8BCscJb7lumGDhNaw3OLcAiEA2VN%2BhMTm6QofayIvK1E8iJlgLfakwV3SyjOX3U5ke6Aq%2FwMIfRAAGgw2Mzc0MjMxODM4MDUiDHeV8q8lF2JoWh1eiircAzPIs09LAr0kFGGfx3Qk7V5IWFbrv7gsxyR%2F3WoL7%2FpYqP1yXsOEpmDozFtj6bwr%2BeUKdACoaiLPtTYRKJGHcbwQpS0zFKeaa%2BxPChSO3yIgHQsAM8cspwaIJbsU50GE7vIoHUUHMuYYbbRZQg9YT6gxPNMrP9%2FTTrLaopo8yiysWZG8GdW8Mh5jWBgcMe%2Fm%2BUn2vAbDjL0EKw6%2FIQXyVpfnxN7e9ZpknyiN%2Fnme5YQu%2BbHAL1jqbBnRyzYd5jxHXPrUwTDut5f0K1mBDj6bV9Wp54Itx1gIt%2FVR0GU4ZONCuunUyUM7Mvky8o3XDhVFH9meU%2FL8NMB5q9W1f3dPhKG5ACafE0aOcLbhMU1ED6vrTy%2FmGB4EOUQRyTOzDePo3anBnjfXf%2FrRF9LXRiqN0KU4j1YUWmU5LCv1yggJy8ZBh%2BeKYAPu%2Bm6oFMehdvK7WMDN7wAocrlGsVffaXgBBW2Fv4XVt2QAQvXHMJDDvZ4z4PVppmYMTT4rklsTTyN6Q82AHU5PzTsE7U3HxNw0TX6Y0jSKdx5%2B0UiSaCCyselCoKLBQ6l6IaeTApWuW48n1YkGzBXjmwgFxYeL4zWoMrlAdmHF68HfmymK8lxMrZosT31G%2BUtvJfE%2BK6egMMfp5LwGOqUBHrAspaLRys2JDx%2BbO3P4FWFYd9FeiZiZoPfegrH%2FUP2kZbERoYABHJEM0OENDigWwr7cHa4h1SslAejQtd3doNl6%2Fu2zr5YMSnjimxqM5uZL47R1Hufhg20sNr6wEA3Vs7EDW%2FB%2B7Ku5dzZKJF7vLjZmk5elqyvNmND%2Fas1zdbnrTYhUPs%2FZ7OYzer4lxsc3LHQHLx50%2F6IuE2H5A5zqzlLhHLza&X-Amz-Signature=053f8d4522bdc84cc5c85b2934286a2d454da99314bc0637474183e1411360d5&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/09aba1c0-0d55-41dd-852a-a04c5b8a3fac/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UX3WZG2J%2F20250128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250128T201547Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHQaCXVzLXdlc3QtMiJGMEQCIFAez6xuThA4d5l5OMJ2TbSRREajDhml7FphgXPTthzYAiArm65kkubJ1IQF8u4wiw1psQgsLydW5NMoLabwdriZtyr%2FAwh9EAAaDDYzNzQyMzE4MzgwNSIML3Bd3o7aljfdIdhLKtwDufTt2PW%2Bd%2BD8YiGoGWKgYN644YRJJNfiF7WlipyMzBCDsmoPQYcB%2FZSLOgfaF3utzbg%2Fuj8koRmb0iGN0k3M10A%2F8nfVcxPNxsOIiy7X1MWdbE%2B3d7sshv%2BCFZX1iEq%2FDK7mTDaw5c4aHVPiD5i7o9l8fiaOKoKKSgClhkh5RwKa1%2FDffcYmXm55s441BdJLm5vWdKbH%2BUWubDj5Wh8NrpDSNJPmKkEl%2BTZUrb6lXwtteV22lztzeO%2BCBWWkg4DeZYLGRl6ijAaHU0MXoAorY77o9fEP5C2pqqFew5srfk4tfYruVpLWXOg%2F7UFBXnx8NEzQfsw8iuTBCogKBPpBycy3gKipUzdOJFlwDQQRp0h9Q8m%2ByWtU%2BIFvlxalq34Nfsry%2B2mqKz8xpHk16J4YjI%2BgnNNm9FDUpYIKEIPqa2X6MUR%2B6h%2FGq59%2B9N9Pj9dLRki1xm6oYLmmsiHNtR4gQbHbjwNn1K7kVh701OchxxyrBiuIKkQz8vEbbwqU6bOQ52ipkuCRkYq2FoInYx3wJC%2BWB4tGk04adunKLhRUSxB1w0nPsKhkjzOwWhQ881kiBVEZUIy1ik0Vpzhecy5lPfLRbzc3EqXA%2Fvwnz6od%2FmDkvzqyTL3EazV%2BIX8wrefkvAY6pgGx3Pxlo%2FOnTFbUdMERV6UeJaVQiG4z9MFB8lA1KCwpYCEg89lKFe7fjXSH2bK25KtgvdgOi0Cx%2BHhgVD4aM9bChxJoVv3prbreBWtrpjkiugJe7TzPIKHPBfVZP%2FGh%2BrUjEQ%2F8RXM28IW7kY0UtM2v3NWgxrnZHdokrdVmTNo1BBnlsBdfCSycgca8%2Bn5p2MWxElt4wUKym0KxIecVqzyc7SIX1eq6&X-Amz-Signature=cc7f0249d79b9e0a8a16b8ac3e4dcca0d72f045a2f90d4cc4baec8a375b8e787&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 2. Scatter Plot
Scatter plots present the relationship between two variables in a dataset. It represents data points on a two-dimensional plane. The independent variable or attribute is plotted on the X-axis, while the dependent variable is plotted on the Y-axis.
**Syntax:**
```python
plt.scatter(x, y)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23708af9-659f-4f23-b626-1a4292d7842c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UX3WZG2J%2F20250128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250128T201547Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHQaCXVzLXdlc3QtMiJGMEQCIFAez6xuThA4d5l5OMJ2TbSRREajDhml7FphgXPTthzYAiArm65kkubJ1IQF8u4wiw1psQgsLydW5NMoLabwdriZtyr%2FAwh9EAAaDDYzNzQyMzE4MzgwNSIML3Bd3o7aljfdIdhLKtwDufTt2PW%2Bd%2BD8YiGoGWKgYN644YRJJNfiF7WlipyMzBCDsmoPQYcB%2FZSLOgfaF3utzbg%2Fuj8koRmb0iGN0k3M10A%2F8nfVcxPNxsOIiy7X1MWdbE%2B3d7sshv%2BCFZX1iEq%2FDK7mTDaw5c4aHVPiD5i7o9l8fiaOKoKKSgClhkh5RwKa1%2FDffcYmXm55s441BdJLm5vWdKbH%2BUWubDj5Wh8NrpDSNJPmKkEl%2BTZUrb6lXwtteV22lztzeO%2BCBWWkg4DeZYLGRl6ijAaHU0MXoAorY77o9fEP5C2pqqFew5srfk4tfYruVpLWXOg%2F7UFBXnx8NEzQfsw8iuTBCogKBPpBycy3gKipUzdOJFlwDQQRp0h9Q8m%2ByWtU%2BIFvlxalq34Nfsry%2B2mqKz8xpHk16J4YjI%2BgnNNm9FDUpYIKEIPqa2X6MUR%2B6h%2FGq59%2B9N9Pj9dLRki1xm6oYLmmsiHNtR4gQbHbjwNn1K7kVh701OchxxyrBiuIKkQz8vEbbwqU6bOQ52ipkuCRkYq2FoInYx3wJC%2BWB4tGk04adunKLhRUSxB1w0nPsKhkjzOwWhQ881kiBVEZUIy1ik0Vpzhecy5lPfLRbzc3EqXA%2Fvwnz6od%2FmDkvzqyTL3EazV%2BIX8wrefkvAY6pgGx3Pxlo%2FOnTFbUdMERV6UeJaVQiG4z9MFB8lA1KCwpYCEg89lKFe7fjXSH2bK25KtgvdgOi0Cx%2BHhgVD4aM9bChxJoVv3prbreBWtrpjkiugJe7TzPIKHPBfVZP%2FGh%2BrUjEQ%2F8RXM28IW7kY0UtM2v3NWgxrnZHdokrdVmTNo1BBnlsBdfCSycgca8%2Bn5p2MWxElt4wUKym0KxIecVqzyc7SIX1eq6&X-Amz-Signature=a04bb2b882796b7bd08bb1da967fcf90ece92c8d4961e602b51e72b49e3466cd&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 3. Histogram
A histogram is an important visual representation of data in categorical form. To view the data in a "Binned" form, use the histogram plot with a number of bins required or with the data points that mark the bin edges. The x-axis represents the data bins, and the y-axis represents the number of elements in each bin.
**Syntax:**
```python
plt.hist(x, bins)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/24e4424a-df87-40a1-b63b-195cbdc2e0ab/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UX3WZG2J%2F20250128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250128T201547Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHQaCXVzLXdlc3QtMiJGMEQCIFAez6xuThA4d5l5OMJ2TbSRREajDhml7FphgXPTthzYAiArm65kkubJ1IQF8u4wiw1psQgsLydW5NMoLabwdriZtyr%2FAwh9EAAaDDYzNzQyMzE4MzgwNSIML3Bd3o7aljfdIdhLKtwDufTt2PW%2Bd%2BD8YiGoGWKgYN644YRJJNfiF7WlipyMzBCDsmoPQYcB%2FZSLOgfaF3utzbg%2Fuj8koRmb0iGN0k3M10A%2F8nfVcxPNxsOIiy7X1MWdbE%2B3d7sshv%2BCFZX1iEq%2FDK7mTDaw5c4aHVPiD5i7o9l8fiaOKoKKSgClhkh5RwKa1%2FDffcYmXm55s441BdJLm5vWdKbH%2BUWubDj5Wh8NrpDSNJPmKkEl%2BTZUrb6lXwtteV22lztzeO%2BCBWWkg4DeZYLGRl6ijAaHU0MXoAorY77o9fEP5C2pqqFew5srfk4tfYruVpLWXOg%2F7UFBXnx8NEzQfsw8iuTBCogKBPpBycy3gKipUzdOJFlwDQQRp0h9Q8m%2ByWtU%2BIFvlxalq34Nfsry%2B2mqKz8xpHk16J4YjI%2BgnNNm9FDUpYIKEIPqa2X6MUR%2B6h%2FGq59%2B9N9Pj9dLRki1xm6oYLmmsiHNtR4gQbHbjwNn1K7kVh701OchxxyrBiuIKkQz8vEbbwqU6bOQ52ipkuCRkYq2FoInYx3wJC%2BWB4tGk04adunKLhRUSxB1w0nPsKhkjzOwWhQ881kiBVEZUIy1ik0Vpzhecy5lPfLRbzc3EqXA%2Fvwnz6od%2FmDkvzqyTL3EazV%2BIX8wrefkvAY6pgGx3Pxlo%2FOnTFbUdMERV6UeJaVQiG4z9MFB8lA1KCwpYCEg89lKFe7fjXSH2bK25KtgvdgOi0Cx%2BHhgVD4aM9bChxJoVv3prbreBWtrpjkiugJe7TzPIKHPBfVZP%2FGh%2BrUjEQ%2F8RXM28IW7kY0UtM2v3NWgxrnZHdokrdVmTNo1BBnlsBdfCSycgca8%2Bn5p2MWxElt4wUKym0KxIecVqzyc7SIX1eq6&X-Amz-Signature=4bb14237aec191cedd96a532800257e96f42f8dd60fba8d6ca5fc431fdc1acde&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ab5a6dfe-51f5-43ee-bcb3-33dae4a1c7ad/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UX3WZG2J%2F20250128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250128T201547Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHQaCXVzLXdlc3QtMiJGMEQCIFAez6xuThA4d5l5OMJ2TbSRREajDhml7FphgXPTthzYAiArm65kkubJ1IQF8u4wiw1psQgsLydW5NMoLabwdriZtyr%2FAwh9EAAaDDYzNzQyMzE4MzgwNSIML3Bd3o7aljfdIdhLKtwDufTt2PW%2Bd%2BD8YiGoGWKgYN644YRJJNfiF7WlipyMzBCDsmoPQYcB%2FZSLOgfaF3utzbg%2Fuj8koRmb0iGN0k3M10A%2F8nfVcxPNxsOIiy7X1MWdbE%2B3d7sshv%2BCFZX1iEq%2FDK7mTDaw5c4aHVPiD5i7o9l8fiaOKoKKSgClhkh5RwKa1%2FDffcYmXm55s441BdJLm5vWdKbH%2BUWubDj5Wh8NrpDSNJPmKkEl%2BTZUrb6lXwtteV22lztzeO%2BCBWWkg4DeZYLGRl6ijAaHU0MXoAorY77o9fEP5C2pqqFew5srfk4tfYruVpLWXOg%2F7UFBXnx8NEzQfsw8iuTBCogKBPpBycy3gKipUzdOJFlwDQQRp0h9Q8m%2ByWtU%2BIFvlxalq34Nfsry%2B2mqKz8xpHk16J4YjI%2BgnNNm9FDUpYIKEIPqa2X6MUR%2B6h%2FGq59%2B9N9Pj9dLRki1xm6oYLmmsiHNtR4gQbHbjwNn1K7kVh701OchxxyrBiuIKkQz8vEbbwqU6bOQ52ipkuCRkYq2FoInYx3wJC%2BWB4tGk04adunKLhRUSxB1w0nPsKhkjzOwWhQ881kiBVEZUIy1ik0Vpzhecy5lPfLRbzc3EqXA%2Fvwnz6od%2FmDkvzqyTL3EazV%2BIX8wrefkvAY6pgGx3Pxlo%2FOnTFbUdMERV6UeJaVQiG4z9MFB8lA1KCwpYCEg89lKFe7fjXSH2bK25KtgvdgOi0Cx%2BHhgVD4aM9bChxJoVv3prbreBWtrpjkiugJe7TzPIKHPBfVZP%2FGh%2BrUjEQ%2F8RXM28IW7kY0UtM2v3NWgxrnZHdokrdVmTNo1BBnlsBdfCSycgca8%2Bn5p2MWxElt4wUKym0KxIecVqzyc7SIX1eq6&X-Amz-Signature=16fdead79cbb530c7b9a90257b0f5e6c47d333c4c15ebf011ddb0b250ad7bd26&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8f1b1d60-cf1b-42b3-9faa-f634c89c3f84/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UX3WZG2J%2F20250128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250128T201547Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHQaCXVzLXdlc3QtMiJGMEQCIFAez6xuThA4d5l5OMJ2TbSRREajDhml7FphgXPTthzYAiArm65kkubJ1IQF8u4wiw1psQgsLydW5NMoLabwdriZtyr%2FAwh9EAAaDDYzNzQyMzE4MzgwNSIML3Bd3o7aljfdIdhLKtwDufTt2PW%2Bd%2BD8YiGoGWKgYN644YRJJNfiF7WlipyMzBCDsmoPQYcB%2FZSLOgfaF3utzbg%2Fuj8koRmb0iGN0k3M10A%2F8nfVcxPNxsOIiy7X1MWdbE%2B3d7sshv%2BCFZX1iEq%2FDK7mTDaw5c4aHVPiD5i7o9l8fiaOKoKKSgClhkh5RwKa1%2FDffcYmXm55s441BdJLm5vWdKbH%2BUWubDj5Wh8NrpDSNJPmKkEl%2BTZUrb6lXwtteV22lztzeO%2BCBWWkg4DeZYLGRl6ijAaHU0MXoAorY77o9fEP5C2pqqFew5srfk4tfYruVpLWXOg%2F7UFBXnx8NEzQfsw8iuTBCogKBPpBycy3gKipUzdOJFlwDQQRp0h9Q8m%2ByWtU%2BIFvlxalq34Nfsry%2B2mqKz8xpHk16J4YjI%2BgnNNm9FDUpYIKEIPqa2X6MUR%2B6h%2FGq59%2B9N9Pj9dLRki1xm6oYLmmsiHNtR4gQbHbjwNn1K7kVh701OchxxyrBiuIKkQz8vEbbwqU6bOQ52ipkuCRkYq2FoInYx3wJC%2BWB4tGk04adunKLhRUSxB1w0nPsKhkjzOwWhQ881kiBVEZUIy1ik0Vpzhecy5lPfLRbzc3EqXA%2Fvwnz6od%2FmDkvzqyTL3EazV%2BIX8wrefkvAY6pgGx3Pxlo%2FOnTFbUdMERV6UeJaVQiG4z9MFB8lA1KCwpYCEg89lKFe7fjXSH2bK25KtgvdgOi0Cx%2BHhgVD4aM9bChxJoVv3prbreBWtrpjkiugJe7TzPIKHPBfVZP%2FGh%2BrUjEQ%2F8RXM28IW7kY0UtM2v3NWgxrnZHdokrdVmTNo1BBnlsBdfCSycgca8%2Bn5p2MWxElt4wUKym0KxIecVqzyc7SIX1eq6&X-Amz-Signature=eebe915c5e7140b1c4c3ea568b01c662a8a4fab0cb14b6581672fef867c23259&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/13ad0497-05fe-4eaa-984e-707b33e14761/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UX3WZG2J%2F20250128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250128T201548Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHQaCXVzLXdlc3QtMiJGMEQCIFAez6xuThA4d5l5OMJ2TbSRREajDhml7FphgXPTthzYAiArm65kkubJ1IQF8u4wiw1psQgsLydW5NMoLabwdriZtyr%2FAwh9EAAaDDYzNzQyMzE4MzgwNSIML3Bd3o7aljfdIdhLKtwDufTt2PW%2Bd%2BD8YiGoGWKgYN644YRJJNfiF7WlipyMzBCDsmoPQYcB%2FZSLOgfaF3utzbg%2Fuj8koRmb0iGN0k3M10A%2F8nfVcxPNxsOIiy7X1MWdbE%2B3d7sshv%2BCFZX1iEq%2FDK7mTDaw5c4aHVPiD5i7o9l8fiaOKoKKSgClhkh5RwKa1%2FDffcYmXm55s441BdJLm5vWdKbH%2BUWubDj5Wh8NrpDSNJPmKkEl%2BTZUrb6lXwtteV22lztzeO%2BCBWWkg4DeZYLGRl6ijAaHU0MXoAorY77o9fEP5C2pqqFew5srfk4tfYruVpLWXOg%2F7UFBXnx8NEzQfsw8iuTBCogKBPpBycy3gKipUzdOJFlwDQQRp0h9Q8m%2ByWtU%2BIFvlxalq34Nfsry%2B2mqKz8xpHk16J4YjI%2BgnNNm9FDUpYIKEIPqa2X6MUR%2B6h%2FGq59%2B9N9Pj9dLRki1xm6oYLmmsiHNtR4gQbHbjwNn1K7kVh701OchxxyrBiuIKkQz8vEbbwqU6bOQ52ipkuCRkYq2FoInYx3wJC%2BWB4tGk04adunKLhRUSxB1w0nPsKhkjzOwWhQ881kiBVEZUIy1ik0Vpzhecy5lPfLRbzc3EqXA%2Fvwnz6od%2FmDkvzqyTL3EazV%2BIX8wrefkvAY6pgGx3Pxlo%2FOnTFbUdMERV6UeJaVQiG4z9MFB8lA1KCwpYCEg89lKFe7fjXSH2bK25KtgvdgOi0Cx%2BHhgVD4aM9bChxJoVv3prbreBWtrpjkiugJe7TzPIKHPBfVZP%2FGh%2BrUjEQ%2F8RXM28IW7kY0UtM2v3NWgxrnZHdokrdVmTNo1BBnlsBdfCSycgca8%2Bn5p2MWxElt4wUKym0KxIecVqzyc7SIX1eq6&X-Amz-Signature=14248dc66b994b3e1fb69835d10b67ae2745e830948003879bdaaa24d1080dab&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 2. Box and Whisker Plot
A box plot shows the distribution of quantitative data in a way that facilitates comparisons between variables or across levels of a categorical variable. The box shows the quartiles of the dataset while the whiskers extend to show the rest of the distribution, except for points that are determined to be "outliers".
**Syntax:**
```python
sns.boxplot(x='header_1', y='header_2', data=df)
```
**Example Output:**


![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d207ae92-0a7c-4e2f-aa65-0ee5a2c33bf7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XRB2GFBX%2F20250128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250128T201549Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHQaCXVzLXdlc3QtMiJHMEUCIQCcz%2FfTlId8t5yA%2Ftnbh7LHcfDNudiQ9kZZss2gVw4xIQIgQqvlAvD10CdShPYXX6wOF2Vd3o5c7wpjGPPMfVH%2Bx2kq%2FwMIfRAAGgw2Mzc0MjMxODM4MDUiDK0q3L%2Fhb%2Fz4Of9vGCrcA%2FpNSNfV%2BenKCKjmfeBe0NUrrtwyTB9V2CA%2FJxuQ3QSmMlJ8qZpz5%2FBpithNrQ3402cWTcG7gxsTVCFJ6MzjFSVBvx1tQOsPONaWJgu0kMKxu7pwEg2wtK61DYaNCF6YAOIfH9C8Y4OF1eYYt3sggYTFLjSdlQFNvDBQF6X7DkrnCnrWIMvpNtHqfTBGESMZ0tUlFuX%2FbvowF27Fud%2F8ZbXJFSZhplxPwRe1hD%2FeICF5D0TU0fP6BoCfqmw0L9xKtN3TwJBPyBODa8CMjJtHgbWgBCqDafl8MFZzqZf9UjDwM5zXD4B2aBpS%2FcZl1YZ2BMzuvDrxlz0mm6Eof1WqAJaG0tsFJxy3FicESBIgHw3RMQZdmjvXawEx3oEijXfg%2BU7v0sjFslSAfJDCd8lPgrgX7yPPc6oRSlIzXPqQzo6J2Hq2eEpeCXEugZft9aCATwkX8HcP32EtvKFzDQq4dIM3LfhgikVfFd1ABmT6iuwctJm3zhizoFJo2wVnycSXqrxZ2uLrOVez87f1sIy4EX0ohS4SZ9%2B%2F0qdZIRkmqo4WO6PiGkQOOmMdlk%2F5TbIebVcoed27UZdf4Xc9zvy0G5D6Bjz%2FjTjRvmhLwRe52QLgnmthL96Z1GFc4FzxMMrm5LwGOqUBTxxDy6EGo8XYWMjg2NhozATuOHEAMZDFj9SkEANitQWV1NeI75FjABdbLbFCrBh38IX1rsAUmRM%2FMASymm4kJF4HGIvSl31v4UytV3bp5FD%2B9SvCmIDIo%2Bk7a4OcDBX75RtvoU3HL4MW3T%2FLEG7hdZgL7Jh%2FAvGLbQhntThcU7l2kQCwSRDg5ekFMWzdlXDn7UiUtjmXDoXkRNzMkT2t8RJNVdQj&X-Amz-Signature=f4b553a794fc81ed0bb00d492ed0e1103c35ab1c3e063d41fff6ec29b9b6c6b5&X-Amz-SignedHeaders=host&x-id=GetObject)

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0e516edc-7551-4792-ab18-0494db3c4c0c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663YMZJQE6%2F20250128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250128T201549Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHQaCXVzLXdlc3QtMiJIMEYCIQDHC93Ee6iFOATMPpI8XHh1%2BML%2BtGe2NM7mtfcaMiAMdgIhAIEPFXkDbsm7PS4zYw8gHo2qRa27vbFvLelZhtigxtd0Kv8DCH0QABoMNjM3NDIzMTgzODA1IgxhAtVmNciVtMbEwXEq3AOqe86WO3UjzXJYhNdGR4qfWzPV2h1U8WwkQ%2FkIrpCJb4mzICTUerABk5kYv0vRgCXGiZ8VeAYqXMtL5rdMfYBUxZnGKhE3xEpSGuBGyu7iaolaSvstchGWQDJszXUNfLKAHs%2BdWCyIwtHx3bn4GD6IIAqpbo3ALxq2033rkLHmTf8WerOIf%2FV2POkPlTCdbmhHIYgmg0%2B5Te0tDqjPkJ08GYx1fhZSxuhLzDGO6u0mWp%2Bu7pV%2BxSqJ2yWg0toZo0yCbYlc%2BKc7tkmtAk2DXRenXb39AQRSskmGEHof7eUZHyU7K3aJKSjlt9LmE0HOVZBXaj6y8U0Cyq7MaMq0AJTcKBaOEs6oFD9KILcaQmJQNwAmp5NCmLl2pGKyihTttiy7DsTEdSGaeSeFMr%2BdQ2FWaGuFfSQclR7KA5XMawvVaoVktcFg4DTLTcxrXigZ0fVikLbnwVBChOaLPZ%2BFIE0q5wQEXhc7EJR9sDeiZnQiCjELDwW734SMcBMY5jClXcsdNb8xHN2VZWBIC%2F8DBpNkjMF9gPjmBTFZSQc7U9DiVVjxlpBIRSb6fXeHILCZG0Z88GpGUWM8Zzf7oQf4Oh94bwXrJ4atJl8xB%2FQ7BY6xvd6rOqstu7tsFSpCXDDC5uS8BjqkAeaiSMBMUmF8jsE0GNe2KBIzVX6Rwx1mUOggAgzZnIhQ3LrFCeY7KpA34nHakOErQ3J1tZ8uv0bVOPgLCH%2Bmo4%2BUGQr2N7xR992iPvkx%2Fkxy4s%2FyQ9io%2BpfO%2BCKgSyP4s7SnRSIBF7yoU1gepJEzOCM9jOt0wWsP0XdfqvGwNQzMt9Q5KTPK82g82PotggpzNxoxb70dUlN58xUSyrkLK91liWe%2B&X-Amz-Signature=ae99aa8310303641823bb4b47d06cf21d418499ff066061de5525c16e591081d&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23a79b9d-2356-49a9-8fd9-65c6b0ab2cc5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UX3WZG2J%2F20250128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250128T201548Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHQaCXVzLXdlc3QtMiJGMEQCIFAez6xuThA4d5l5OMJ2TbSRREajDhml7FphgXPTthzYAiArm65kkubJ1IQF8u4wiw1psQgsLydW5NMoLabwdriZtyr%2FAwh9EAAaDDYzNzQyMzE4MzgwNSIML3Bd3o7aljfdIdhLKtwDufTt2PW%2Bd%2BD8YiGoGWKgYN644YRJJNfiF7WlipyMzBCDsmoPQYcB%2FZSLOgfaF3utzbg%2Fuj8koRmb0iGN0k3M10A%2F8nfVcxPNxsOIiy7X1MWdbE%2B3d7sshv%2BCFZX1iEq%2FDK7mTDaw5c4aHVPiD5i7o9l8fiaOKoKKSgClhkh5RwKa1%2FDffcYmXm55s441BdJLm5vWdKbH%2BUWubDj5Wh8NrpDSNJPmKkEl%2BTZUrb6lXwtteV22lztzeO%2BCBWWkg4DeZYLGRl6ijAaHU0MXoAorY77o9fEP5C2pqqFew5srfk4tfYruVpLWXOg%2F7UFBXnx8NEzQfsw8iuTBCogKBPpBycy3gKipUzdOJFlwDQQRp0h9Q8m%2ByWtU%2BIFvlxalq34Nfsry%2B2mqKz8xpHk16J4YjI%2BgnNNm9FDUpYIKEIPqa2X6MUR%2B6h%2FGq59%2B9N9Pj9dLRki1xm6oYLmmsiHNtR4gQbHbjwNn1K7kVh701OchxxyrBiuIKkQz8vEbbwqU6bOQ52ipkuCRkYq2FoInYx3wJC%2BWB4tGk04adunKLhRUSxB1w0nPsKhkjzOwWhQ881kiBVEZUIy1ik0Vpzhecy5lPfLRbzc3EqXA%2Fvwnz6od%2FmDkvzqyTL3EazV%2BIX8wrefkvAY6pgGx3Pxlo%2FOnTFbUdMERV6UeJaVQiG4z9MFB8lA1KCwpYCEg89lKFe7fjXSH2bK25KtgvdgOi0Cx%2BHhgVD4aM9bChxJoVv3prbreBWtrpjkiugJe7TzPIKHPBfVZP%2FGh%2BrUjEQ%2F8RXM28IW7kY0UtM2v3NWgxrnZHdokrdVmTNo1BBnlsBdfCSycgca8%2Bn5p2MWxElt4wUKym0KxIecVqzyc7SIX1eq6&X-Amz-Signature=e3f94b580d387b3d26d035235beddb2a20359f38fca69dcd70a62eda5b0d7b3f&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 4. KDE Plot
A Kernel Density Estimate (KDE) plot is a graph that creates a probability distribution curve for the data based upon its likelihood of occurrence on a specific value. This is created for a single vector of information.
**Syntax:**
```python
sns.kdeplot(X) || sns.kdeplot(df['age'])
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0d571213-2a2f-4921-a50b-880847aa05ee/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UX3WZG2J%2F20250128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250128T201548Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHQaCXVzLXdlc3QtMiJGMEQCIFAez6xuThA4d5l5OMJ2TbSRREajDhml7FphgXPTthzYAiArm65kkubJ1IQF8u4wiw1psQgsLydW5NMoLabwdriZtyr%2FAwh9EAAaDDYzNzQyMzE4MzgwNSIML3Bd3o7aljfdIdhLKtwDufTt2PW%2Bd%2BD8YiGoGWKgYN644YRJJNfiF7WlipyMzBCDsmoPQYcB%2FZSLOgfaF3utzbg%2Fuj8koRmb0iGN0k3M10A%2F8nfVcxPNxsOIiy7X1MWdbE%2B3d7sshv%2BCFZX1iEq%2FDK7mTDaw5c4aHVPiD5i7o9l8fiaOKoKKSgClhkh5RwKa1%2FDffcYmXm55s441BdJLm5vWdKbH%2BUWubDj5Wh8NrpDSNJPmKkEl%2BTZUrb6lXwtteV22lztzeO%2BCBWWkg4DeZYLGRl6ijAaHU0MXoAorY77o9fEP5C2pqqFew5srfk4tfYruVpLWXOg%2F7UFBXnx8NEzQfsw8iuTBCogKBPpBycy3gKipUzdOJFlwDQQRp0h9Q8m%2ByWtU%2BIFvlxalq34Nfsry%2B2mqKz8xpHk16J4YjI%2BgnNNm9FDUpYIKEIPqa2X6MUR%2B6h%2FGq59%2B9N9Pj9dLRki1xm6oYLmmsiHNtR4gQbHbjwNn1K7kVh701OchxxyrBiuIKkQz8vEbbwqU6bOQ52ipkuCRkYq2FoInYx3wJC%2BWB4tGk04adunKLhRUSxB1w0nPsKhkjzOwWhQ881kiBVEZUIy1ik0Vpzhecy5lPfLRbzc3EqXA%2Fvwnz6od%2FmDkvzqyTL3EazV%2BIX8wrefkvAY6pgGx3Pxlo%2FOnTFbUdMERV6UeJaVQiG4z9MFB8lA1KCwpYCEg89lKFe7fjXSH2bK25KtgvdgOi0Cx%2BHhgVD4aM9bChxJoVv3prbreBWtrpjkiugJe7TzPIKHPBfVZP%2FGh%2BrUjEQ%2F8RXM28IW7kY0UtM2v3NWgxrnZHdokrdVmTNo1BBnlsBdfCSycgca8%2Bn5p2MWxElt4wUKym0KxIecVqzyc7SIX1eq6&X-Amz-Signature=130b9584571832bf5fb05233f958e057d0c3765f2e050ffba8daaff5a4d7e35c&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/53752550-ef82-4ca9-a01a-09921f0282d0/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UX3WZG2J%2F20250128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250128T201548Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHQaCXVzLXdlc3QtMiJGMEQCIFAez6xuThA4d5l5OMJ2TbSRREajDhml7FphgXPTthzYAiArm65kkubJ1IQF8u4wiw1psQgsLydW5NMoLabwdriZtyr%2FAwh9EAAaDDYzNzQyMzE4MzgwNSIML3Bd3o7aljfdIdhLKtwDufTt2PW%2Bd%2BD8YiGoGWKgYN644YRJJNfiF7WlipyMzBCDsmoPQYcB%2FZSLOgfaF3utzbg%2Fuj8koRmb0iGN0k3M10A%2F8nfVcxPNxsOIiy7X1MWdbE%2B3d7sshv%2BCFZX1iEq%2FDK7mTDaw5c4aHVPiD5i7o9l8fiaOKoKKSgClhkh5RwKa1%2FDffcYmXm55s441BdJLm5vWdKbH%2BUWubDj5Wh8NrpDSNJPmKkEl%2BTZUrb6lXwtteV22lztzeO%2BCBWWkg4DeZYLGRl6ijAaHU0MXoAorY77o9fEP5C2pqqFew5srfk4tfYruVpLWXOg%2F7UFBXnx8NEzQfsw8iuTBCogKBPpBycy3gKipUzdOJFlwDQQRp0h9Q8m%2ByWtU%2BIFvlxalq34Nfsry%2B2mqKz8xpHk16J4YjI%2BgnNNm9FDUpYIKEIPqa2X6MUR%2B6h%2FGq59%2B9N9Pj9dLRki1xm6oYLmmsiHNtR4gQbHbjwNn1K7kVh701OchxxyrBiuIKkQz8vEbbwqU6bOQ52ipkuCRkYq2FoInYx3wJC%2BWB4tGk04adunKLhRUSxB1w0nPsKhkjzOwWhQ881kiBVEZUIy1ik0Vpzhecy5lPfLRbzc3EqXA%2Fvwnz6od%2FmDkvzqyTL3EazV%2BIX8wrefkvAY6pgGx3Pxlo%2FOnTFbUdMERV6UeJaVQiG4z9MFB8lA1KCwpYCEg89lKFe7fjXSH2bK25KtgvdgOi0Cx%2BHhgVD4aM9bChxJoVv3prbreBWtrpjkiugJe7TzPIKHPBfVZP%2FGh%2BrUjEQ%2F8RXM28IW7kY0UtM2v3NWgxrnZHdokrdVmTNo1BBnlsBdfCSycgca8%2Bn5p2MWxElt4wUKym0KxIecVqzyc7SIX1eq6&X-Amz-Signature=6342e1051de25fbd2e697fb862d2398f7010540c231215b34886ef09717c2ecf&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
## 4. Correlation Between Variables
Correlation is a statistical measure of the extent to which different variables are interdependent. It indicates how changes in one variable are associated with changes in another variable over time.
### Positive Correlation
Positive correlation indicates that as one variable increases, the other variable also tends to increase.
**Example: Engine Size and Price**
- **Positive Correlation:** Engine size increases, price also increases.
- **Visualization:** Scatter plot with a steep positive slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c7ea9b0-3ef3-4357-a9c3-554fc71b6b15/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667VEDZAUW%2F20250128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250128T201549Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHQaCXVzLXdlc3QtMiJIMEYCIQDnaQEZV%2FJObswaHHHV%2FgrjZ0ipsuytbAP6K2vOhbrvUQIhAO5eEKKqw6FjNFhWTGBlg%2FAjPJLysmOE2x7otwerj65mKv8DCH0QABoMNjM3NDIzMTgzODA1Igw0LIFR5pc%2BhkNo5XAq3APo2TeM7fsFj8P8QUEE51KfgMD6NUezZN5EWv%2BaU92uVHVFumyIYh429SGb4yOOKv4ZxNjwW6XDcikAG4I2MRrtlhC7quBFcJwGjflowxl67nhAuvAadVkBgIJkEtrtxiF9WwxCi6zRoQWcG0u%2F5Bq2Q2W%2FPwmJJkMKBcdnSnq4UwOwal5LCmcaJmi9IoNr%2FN5QAefnTbC4tP63cJyVgOeMTPxk5Mw8YNISZ%2BlsGii9ahfNX5%2FpRRjq5NQZ8mQabX0XcP8Fe9ktVIVnwOPMukDSicjMcBVFth4TYZKV%2FbT5EZZ9TNvJrbR6Z4ShNodJL89dkg1IXGpI7qs4nkqOjTw%2BkjvZVhR3rb%2FxyMg2UVTv7nEua28rEPMyAIxT2oM5kb%2B8sVL1zqbbtmjE3KX5ub8XXeXv8TZTE8Mo3jJ9bfHmLVtLBamIDcXGfgRsGkpuGdhYpRYSfmw%2BZ66N44UL8geH5UTWKAbOGZJBzSQyNuBCMGdcIVvz2drgOKQ64PKPYP%2BFgPDX3sAzP5PdPVqwuO9Hr%2FPQhYWT9X8cdX3V0mLyD%2BUDm09V%2Bha9xO9sVxgIjmFjS0pl8fbQX3cYonaWfs6WknuBGAw%2FXWrmGPDjZvFyCBc6264C0HupJexuIjCW6uS8BjqkAbBZ1evNAeHBnC8Bx%2BFxopjp9AFTYe6Zl7Y0FRbBf9ZuwPbb3kBvjYSMkppvD1%2FBxZ967R%2FjL0RNhxRCheJzlmhdN%2BI7YcLdmPUiZaFOdBpwc87HLqA6BVhP27fErSUnMH1P66RMYiBSYyUYVnId%2FIg7VruWUhpW8GoNZ2jbxp%2FZVszqV3Eequ0kHr0%2BW5W3rRq2%2BS9o5%2FIbhQe76xepExtJkbbF&X-Amz-Signature=ab611b4e17877da920a461022dca4753534a20ac3ab61452c3e1e8d2d5d70df4&X-Amz-SignedHeaders=host&x-id=GetObject)
**Explanation:** When engine size increases, there is a corresponding increase in the price of the vehicle. This positive correlation suggests that larger engines tend to be associated with higher prices in the market.
___
### Negative Correlation
Negative correlation indicates that as one variable increases, the other variable tends to decrease.
**Example: Highway Miles per Gallon and Price**
- **Negative Correlation:** As highway miles per gallon increases, price decreases.
- **Visualization:** Scatter plot with a steep negative slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/10f1f798-9cc4-4df2-a9c1-5a339f554a0b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VUEP3GSF%2F20250128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250128T201549Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHQaCXVzLXdlc3QtMiJHMEUCIQCava4yprVzVY0Kv9td1dYrQeXAwpqLytMHrXh%2Bmv7qnAIgcxIPyeeAlsrfyN8aSgJM98%2FtuKJcsSuKGAicSXXwf5Iq%2FwMIfRAAGgw2Mzc0MjMxODM4MDUiDAoXrLvbG40NShI%2BByrcA8%2F1crEtlWBUyx8VMdw7cHJkBymOg0tZc1W7v8CEGgSVQLb70ZmW8BVRDO%2BYIBur26JUVwOS8wFOhNNWL79rtUgne%2BWTRdRFDdCs6%2BLs6Ec0ts%2BaD0CPkHx%2BeebTA%2BYCpARo4EKG%2FFsBW4oqL3QxO8h1fOL%2BEHGZEOKlEC%2FDX1Whw4Aijl3%2Br0Rwp8ewP7c04JnByyeN%2BKAgo0gmuQ6vn5s%2BEjRZBurVz5q3L7ksB%2F57o6NySAKI3rTucdGExqvtu8IsmQWuRazARcRBH%2BxWF6BN3Yt3%2BV1B07Ze8VeBHp%2FNj7d4q2WouZc%2Fp6pHwQbnG49q5QtDFhGduHHFA9%2FlVUFjDjBmFnCfERqaE0aYnqa4NMiKlxwkd69l0c1H02N3p58f1kraJbXtz1eDkWXfms%2F2Zoc6dftW3NO8qSZ%2FHlRLuSaoJngos3FLdQI91DFoJYnfKbYrKoIn1%2BgtdyXewR6GSsOOvwCR3U1KT54hKVpMC5%2FVo6x6B6SrVVcYofU0%2BGeQ5q3Mumfjpq9tafUMr5BeceZTu%2BUcH0rRKEHdPKoOa3EmePrEn7oVb7o6Pphs%2FMMcJimu7Xa1fn61H0kbtYo0CtjqjQXIlNzuSL%2BjMa%2BHrbr1CkhvIYU6yasuMODg5LwGOqUB9V%2FhtpjDWNMHacWg6R1RxmF%2FIi98iR0%2FXG2NTs%2F%2BjHdTX5lyaDYdY%2Ftx9IxotqDf6KkNyOZyBPC3BEI30aGpXTqJdvwDOtol%2FKg1aT2cCk1%2F%2BHqX19cDgAbCS7JiLPf1fZWmI%2FiasmF5Rjn7Mdoz880wci2y03MbpkUCrDCumXz1d%2BxCdZfnHiQjRSm1TjLKYvAFkImZKsaU%2FHXjBHGcgrlPXYBD&X-Amz-Signature=d35a376626b378ecbdd7bd9c75671da9b9da8b36f31e614042b49c7193b584da&X-Amz-SignedHeaders=host&x-id=GetObject)
**Explanation:** When highway miles per gallon increases, the price of the vehicle tends to decrease. This negative correlation suggests that cars with higher fuel efficiency (more miles per gallon) are generally priced lower in the market.
___
### Weak Correlation
Weak correlation indicates a lack of strong relationship between the variables.
**Example: RPM and Price**
- **Weak Correlation:** Low and high RPM values show varied prices, indicating no strong predictive relationship.
- **Visualization:** Scatter plot with no clear trend or slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9f914514-8914-4bf4-ac84-d9e3077f6eb1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46643LYZ573%2F20250128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250128T201549Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHQaCXVzLXdlc3QtMiJHMEUCIDrq1iBfFdUeCAa8mTlYoI8YjbpRdM0ZxMSN2ATXCa98AiEA4XfO4Z4REdY0PVRM42shGhaIOIDgXkSkosVa9U6qsmUq%2FwMIfRAAGgw2Mzc0MjMxODM4MDUiDD1HO8tUtF01ogfT9SrcA276%2BqS1afLWoRcn9jm%2BTr3YC3C5fGGiOgaoRb3hrNvU4QN3mhBYgeVlKL6JAJtduQn%2Flc5K%2FNGEyWh1K4ZV6itaaHv2xLO0Kwgt%2B3oJ%2FeU3G7Gb6lTHAYlBOqxy9%2BoWv6R5VU7lQBjt77w%2FujDO8nw54jYA%2FVdhP5npZw9iQ39gcCIiTLik8NFjEiwMvodR9PPiB%2BhnSUITpbDGkUrC706LqUbXfYITI9jacV3NuPEF08NFUk%2F6NAhvkKjdHt72XGi0k9o0W4u%2B9d0%2FqUYJJ1Xcbss6enZ0sqhvuoc1xWJjzgYpnerLxPg0tHKU7mwJy0raWGg73llLMty8eJlVuS56BSI9%2FqV0UF%2FDaot2wZtxoXAjlHOS63SAPrHXq8Q9YoYeccLnNkb0jWSdYEZnfgoKZh6pmNL4Vdn01tK%2FNfW1LbzuceGUX7Wurr%2BYXjMlH5cuVtHa%2FEHTKFSmc4Il%2FamjV%2B%2FtjvwiRiFcWvveElnM0nwUbZAyGWOZqSeRjFLp%2BygJfhr7Ca2ZQuCsXBrb%2FM9RywVAgU2YJdjBXRAOEFsQCerIEn9NnmQdEF0zSKOzylP5Wh5fRkIRQI7Bmf5Ry1llpUe%2FyZMJA0FamLOSPl13%2F5c%2BqPGuD%2FPdRW59MKbm5LwGOqUBhJUA1d3r%2B6sxigeMHZoM5KbWd2YNaWrPZMZIJbvk27KZJvdO5ooad6%2BGpIBnfR8N28qxr2tK0rNEChvb8hXf9LLxMFEdHMMcLi0eP9MwLH4PGYG2opdvOjga85G4byMzCgENB%2Ff5dZss5L%2BTH%2BTb5kTHnUlZnvF%2BqNvMeGLWMjo82xY%2Fhx8GgllGTJfKl9BUg4RO%2FRGP%2FWJkduhjIjEOeqRK4Cr6&X-Amz-Signature=f14ca00df79fc5c6bb26a66c7df32ce6f9d7ef47f02037dae78eb6d5a67fe59d&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f18086e5-5b04-4fbf-8309-8944ab20d213/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666GJI6NBN%2F20250128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250128T201548Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHQaCXVzLXdlc3QtMiJHMEUCIDwpzAnYIVUNKoSVofE8yeYohAJ0qgaAPJYKxaXX5lQAAiEAof8vn4TNePgWc1ZIcbk3Lti3e1JY5i%2BGcoeqPOZs9XIq%2FwMIfRAAGgw2Mzc0MjMxODM4MDUiDFWGf1re%2B9MyiBS03yrcAxyx%2F%2B5f60%2FT5cLZdYPN1lqWbA0Q1cKY2BVMRYI0r1SrOhnKjaDy9Q8vdwPx2K5a5XRcRLZHdThsSjd4U63YEtEDoF4WssKveBbHGKIgaHlw%2B%2FTGJ8UzlK%2FqdBLAOlsBAqbT2GcjaOO8QcK3otM0uKncZRf8KeXZKflbroK9bNsRbJ11mgVh2dkY9TsP7CMGe4Z%2F8EXnnizU%2FAln0wjUh%2FTMm7JUDtEiJUKcduZ5086GFTwKs5Oin5hiH%2Bneo4vnlHHVaAb75YjfBoWH%2FRblYIRKdonx9W6E4PGvZnUlxRrIIHhSd6b5Rnma6GLPkLZCrH6IZ%2B0TmUTrRa6g8ZfCHdi%2BCgbojH2aWq1AeY7Y8PEQnFICvDeoZjifwgxd4440eQR32QubZMpO4i5cONLqao%2B8oSMcV2bLg%2FnmTMgUNdZtnspjxVqJ9lTwy2XRzg%2BDvdMjsAogAadORzM3bWoAnzR%2FAXOiRKR4ZJnF9yL4sCL7AzJnuuLuvQuLz4WNQLzdYxhOQGB%2BBjCr5lf6%2Fy0Cjx0KuBgKuLjv23bIoll4i3Szi1vry2xhc3idn%2F4xXdeI9zYfrEmej6Apq0%2FbDjCAtoOngobT7zxbyJOjIMvASdW3czkdvx2ZcoxX5%2B6dMI3o5LwGOqUBpgfcaDNPTzgAX%2BpgxdB7e0olx%2FFSs3DqtvvaUcaaIjgT3QTCIfQZ7nlbAVh1B1Ku7cqAIUDhvjFRpnJmY1Wp%2Bx6lnglkK%2FSvIIKnrt7gH294oHU3roZb8x93i0s%2BKkuisUi6gG7itnTZyF%2Fr5lh4gkP4JwBiOq%2BPQ7knPjsWMLgnYFTdQ8aWQYHw9q2HCkZlNXd%2FOZ67IgZ%2BbvZ8dWEby%2FRkQNPU&X-Amz-Signature=4cb74214a22a59fa370329640c9f258a10c3e8473cd029d0c98383e65438dc39&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Correlation Plot
Heatmap visualizes correlations among variables. Color scheme indicates Pearson correlation coefficients. Dark red diagonal line shows perfect correlation (value of 1) between variables and themselves.
This heatmap offers overview of variable relationships and their link with price.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cd3b341e-cc1a-45f7-8aec-cdc00436d270/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666GJI6NBN%2F20250128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250128T201548Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHQaCXVzLXdlc3QtMiJHMEUCIDwpzAnYIVUNKoSVofE8yeYohAJ0qgaAPJYKxaXX5lQAAiEAof8vn4TNePgWc1ZIcbk3Lti3e1JY5i%2BGcoeqPOZs9XIq%2FwMIfRAAGgw2Mzc0MjMxODM4MDUiDFWGf1re%2B9MyiBS03yrcAxyx%2F%2B5f60%2FT5cLZdYPN1lqWbA0Q1cKY2BVMRYI0r1SrOhnKjaDy9Q8vdwPx2K5a5XRcRLZHdThsSjd4U63YEtEDoF4WssKveBbHGKIgaHlw%2B%2FTGJ8UzlK%2FqdBLAOlsBAqbT2GcjaOO8QcK3otM0uKncZRf8KeXZKflbroK9bNsRbJ11mgVh2dkY9TsP7CMGe4Z%2F8EXnnizU%2FAln0wjUh%2FTMm7JUDtEiJUKcduZ5086GFTwKs5Oin5hiH%2Bneo4vnlHHVaAb75YjfBoWH%2FRblYIRKdonx9W6E4PGvZnUlxRrIIHhSd6b5Rnma6GLPkLZCrH6IZ%2B0TmUTrRa6g8ZfCHdi%2BCgbojH2aWq1AeY7Y8PEQnFICvDeoZjifwgxd4440eQR32QubZMpO4i5cONLqao%2B8oSMcV2bLg%2FnmTMgUNdZtnspjxVqJ9lTwy2XRzg%2BDvdMjsAogAadORzM3bWoAnzR%2FAXOiRKR4ZJnF9yL4sCL7AzJnuuLuvQuLz4WNQLzdYxhOQGB%2BBjCr5lf6%2Fy0Cjx0KuBgKuLjv23bIoll4i3Szi1vry2xhc3idn%2F4xXdeI9zYfrEmej6Apq0%2FbDjCAtoOngobT7zxbyJOjIMvASdW3czkdvx2ZcoxX5%2B6dMI3o5LwGOqUBpgfcaDNPTzgAX%2BpgxdB7e0olx%2FFSs3DqtvvaUcaaIjgT3QTCIfQZ7nlbAVh1B1Ku7cqAIUDhvjFRpnJmY1Wp%2Bx6lnglkK%2FSvIIKnrt7gH294oHU3roZb8x93i0s%2BKkuisUi6gG7itnTZyF%2Fr5lh4gkP4JwBiOq%2BPQ7knPjsWMLgnYFTdQ8aWQYHw9q2HCkZlNXd%2FOZ67IgZ%2BbvZ8dWEby%2FRkQNPU&X-Amz-Signature=f14e8b155696f68847a16a678a0d92ea589534b6ef8a80db321428101fa76ca9&X-Amz-SignedHeaders=host&x-id=GetObject)

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
