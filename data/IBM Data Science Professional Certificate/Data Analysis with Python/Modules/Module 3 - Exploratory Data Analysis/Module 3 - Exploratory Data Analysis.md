

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7e6d594d-952e-44b6-97ea-31225882aea6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466X32QT4SW%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T041747Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDwaCXVzLXdlc3QtMiJHMEUCIBjEvNDdqrBq1KvkgfjYwQIgjBHi1Jc13BPk%2FisE9CC8AiEAyuIhFcsp05nke6xTk8C5Rgdsfm1bXc3h4Buq7O5of8Qq%2FwMIVRAAGgw2Mzc0MjMxODM4MDUiDGcWlUjE%2FXBrash%2B%2BircAwQ2lLHrXcNX6FadZgYTTkgd6rPiQN%2F%2FM8f7YujMuOnPBHJf8q2ynby3ItahSf2GLR%2B22hlO5XXf0lQ5h%2FAda0ASNxd%2BLCWLbsYAfb4ZwIXaJMNv%2FWA48Y%2Fmg6TLcuB8rfCg06tCdGF5Y1AnxxDANqOTFXnYDiedmZI3CRIaEJ8cIBDMrPY8Dx4gWZ5bL7yS%2B1L9H%2BcLvuHR8Q%2FIwxTkNjKYccReFEU0V3R9%2BhByUbfp1qbg%2BNq1lbfajmDbebyTJ3c6wZcg0oVdRrLeCxWldF8vhUtbZrPemtnuO%2Fl3KCTVkqy%2F98ibzoZ7Kw04c3io1zKGDC2hSls%2F7itwFsV2viNFyNzrpl3R93Qk61%2Fc229DR67lqFA7oGjU0DK2vqWCDx6xZorkroc%2B4RmaDl2BxqKDegtjkS45qXc9SXAC%2BJInA42runCoQpI%2Ff86f6X1pKPcHfXulmzBCV6Sfy2ozXGraz2mMOd3RrGSp33%2BKPcNixwfft3cvIqT%2FJfzx%2F7AevFaVJQFFjXWX6kEtiACHIW9MKwjArVbcs0m%2BWNWNcgUj5jrN8ye7wrZ5QfpJSmm6uXhkx4axK7xUJU%2Fc2hNBmu%2Fv1AyqntKF8hLbSmczuV2lIK8cJHrWoExKYRJ1MNXfkL0GOqUBNUwNT0%2BSTHcxhdgmQDWF00Ri6IeVMEKNIH2kmdcS0Kx%2FMc7WRgLyMl%2BYkMm7NtiL8QrxbhzeOQOl0Bi7%2BRu21eBJDXxSf51pAe6xI6tq1BjtK7%2BHV4JOMLAt7LVoZvLgKg7xtHfPu5Qg5VXKqBUjPPryUU9Q1ixI2Ss9zbE%2FHVp9Sne0X3KXfBFuRBMgs9jWdeDpi0onDkrZ4AD0rG0gHkzO4u5i&X-Amz-Signature=00ac89e46ea4744a875dd9dd0aad843c420be22133894ca47ad9db94ab7aec3d&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cbfaed9e-b398-4902-8936-dea058b21def/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466X32QT4SW%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T041747Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDwaCXVzLXdlc3QtMiJHMEUCIBjEvNDdqrBq1KvkgfjYwQIgjBHi1Jc13BPk%2FisE9CC8AiEAyuIhFcsp05nke6xTk8C5Rgdsfm1bXc3h4Buq7O5of8Qq%2FwMIVRAAGgw2Mzc0MjMxODM4MDUiDGcWlUjE%2FXBrash%2B%2BircAwQ2lLHrXcNX6FadZgYTTkgd6rPiQN%2F%2FM8f7YujMuOnPBHJf8q2ynby3ItahSf2GLR%2B22hlO5XXf0lQ5h%2FAda0ASNxd%2BLCWLbsYAfb4ZwIXaJMNv%2FWA48Y%2Fmg6TLcuB8rfCg06tCdGF5Y1AnxxDANqOTFXnYDiedmZI3CRIaEJ8cIBDMrPY8Dx4gWZ5bL7yS%2B1L9H%2BcLvuHR8Q%2FIwxTkNjKYccReFEU0V3R9%2BhByUbfp1qbg%2BNq1lbfajmDbebyTJ3c6wZcg0oVdRrLeCxWldF8vhUtbZrPemtnuO%2Fl3KCTVkqy%2F98ibzoZ7Kw04c3io1zKGDC2hSls%2F7itwFsV2viNFyNzrpl3R93Qk61%2Fc229DR67lqFA7oGjU0DK2vqWCDx6xZorkroc%2B4RmaDl2BxqKDegtjkS45qXc9SXAC%2BJInA42runCoQpI%2Ff86f6X1pKPcHfXulmzBCV6Sfy2ozXGraz2mMOd3RrGSp33%2BKPcNixwfft3cvIqT%2FJfzx%2F7AevFaVJQFFjXWX6kEtiACHIW9MKwjArVbcs0m%2BWNWNcgUj5jrN8ye7wrZ5QfpJSmm6uXhkx4axK7xUJU%2Fc2hNBmu%2Fv1AyqntKF8hLbSmczuV2lIK8cJHrWoExKYRJ1MNXfkL0GOqUBNUwNT0%2BSTHcxhdgmQDWF00Ri6IeVMEKNIH2kmdcS0Kx%2FMc7WRgLyMl%2BYkMm7NtiL8QrxbhzeOQOl0Bi7%2BRu21eBJDXxSf51pAe6xI6tq1BjtK7%2BHV4JOMLAt7LVoZvLgKg7xtHfPu5Qg5VXKqBUjPPryUU9Q1ixI2Ss9zbE%2FHVp9Sne0X3KXfBFuRBMgs9jWdeDpi0onDkrZ4AD0rG0gHkzO4u5i&X-Amz-Signature=8bfb30fd6139cfe6a0bde0f6951db1cc3fda217f4c42908f8bd1ee48b909ce55&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/91181646-b1e0-4433-9711-6259a96a9247/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466X32QT4SW%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T041747Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDwaCXVzLXdlc3QtMiJHMEUCIBjEvNDdqrBq1KvkgfjYwQIgjBHi1Jc13BPk%2FisE9CC8AiEAyuIhFcsp05nke6xTk8C5Rgdsfm1bXc3h4Buq7O5of8Qq%2FwMIVRAAGgw2Mzc0MjMxODM4MDUiDGcWlUjE%2FXBrash%2B%2BircAwQ2lLHrXcNX6FadZgYTTkgd6rPiQN%2F%2FM8f7YujMuOnPBHJf8q2ynby3ItahSf2GLR%2B22hlO5XXf0lQ5h%2FAda0ASNxd%2BLCWLbsYAfb4ZwIXaJMNv%2FWA48Y%2Fmg6TLcuB8rfCg06tCdGF5Y1AnxxDANqOTFXnYDiedmZI3CRIaEJ8cIBDMrPY8Dx4gWZ5bL7yS%2B1L9H%2BcLvuHR8Q%2FIwxTkNjKYccReFEU0V3R9%2BhByUbfp1qbg%2BNq1lbfajmDbebyTJ3c6wZcg0oVdRrLeCxWldF8vhUtbZrPemtnuO%2Fl3KCTVkqy%2F98ibzoZ7Kw04c3io1zKGDC2hSls%2F7itwFsV2viNFyNzrpl3R93Qk61%2Fc229DR67lqFA7oGjU0DK2vqWCDx6xZorkroc%2B4RmaDl2BxqKDegtjkS45qXc9SXAC%2BJInA42runCoQpI%2Ff86f6X1pKPcHfXulmzBCV6Sfy2ozXGraz2mMOd3RrGSp33%2BKPcNixwfft3cvIqT%2FJfzx%2F7AevFaVJQFFjXWX6kEtiACHIW9MKwjArVbcs0m%2BWNWNcgUj5jrN8ye7wrZ5QfpJSmm6uXhkx4axK7xUJU%2Fc2hNBmu%2Fv1AyqntKF8hLbSmczuV2lIK8cJHrWoExKYRJ1MNXfkL0GOqUBNUwNT0%2BSTHcxhdgmQDWF00Ri6IeVMEKNIH2kmdcS0Kx%2FMc7WRgLyMl%2BYkMm7NtiL8QrxbhzeOQOl0Bi7%2BRu21eBJDXxSf51pAe6xI6tq1BjtK7%2BHV4JOMLAt7LVoZvLgKg7xtHfPu5Qg5VXKqBUjPPryUU9Q1ixI2Ss9zbE%2FHVp9Sne0X3KXfBFuRBMgs9jWdeDpi0onDkrZ4AD0rG0gHkzO4u5i&X-Amz-Signature=dbd25aa7d82a1e12d395a70266b0a6f251f2a5e53d0d5f835e3efd60a2c59537&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/09aba1c0-0d55-41dd-852a-a04c5b8a3fac/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YZWY3Q6Z%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T041748Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDwaCXVzLXdlc3QtMiJHMEUCIQC8eV3pGVe%2Fn%2F%2BtaUs7U9xgeQx7rv1Feqx8oESh%2F%2BJkugIgbPukS56Q9KeM1kqXuvlagzILuwcBvsEzaC3gcRZ9lWcq%2FwMIVRAAGgw2Mzc0MjMxODM4MDUiDIeXbu5WLgEvG6W0RSrcA6PPZ71qGDD3FR41%2FpWMlGSW4gJ96DAS5276pi2JKFoahJcx8eyxMXbvYlEw9Ydj8ujQx41VslEJO5SE%2FcUbBaP4xd2Ebh1AG3cLys1XzgBVcrMS%2F28%2B2FsdzhUuef%2F7flXc2eqq141Nza84xvdFIwYZCFdmqa1j8v6B7EiwYS6Q67rn34JweLKvpjg3MFQDfpsEEAVmpolM7wg9GrbFNVkWbo8UVjf0Rh7eXcuSU9UyN5xHVAqexY5TcTItHYzHGRlYIX%2BR2%2FTO%2Fxu1cz0Ys50kz8Pu9n5rhqMdIoF9C1CNt9SSTI%2FoSNJwWOgPQbFdZBJPq%2BHAY%2FA2i%2BRGYmzXg6VqlZxvRhSRV%2B%2FjFPJE5ODWYlXqcFfX1xFCXkwhJwjKSdpxWQBPs%2BrJZmPf%2FVrHeCqgxSzH2wtfkxhZ8hUmnVBYfmr1rGxFNO%2BS1Ufb9%2BhbR6%2FpS4%2BDcUxeFarZo0RU%2FgYp4Jlo8KXXMudCBrDJkhwJWrpglFdYn0P7FSbHoHUa8FrKhv5FTSCsJbfZ4uvMebk%2B3MQoa4u4QPbV9%2F2vjqWQyjGP7BwkYO292V%2FyD81g8r85TSLHCd407aLduC6AigLQxieJWXypNUWUeb7PLx6kokMwH%2F7swH8pl8qMMOnfkL0GOqUBLjnpso9ASO1WlKoiYeaB6KaznEBfiPvsylAN8PxkL9l2gAj%2F%2B%2BRhTwEX6b%2Bsp2Dyr0znm0EDlhWZp%2BSRw%2BaSzjsnYspUcuv3tcsSV5Qhb7HWqfdhBW5BD3hPVvi0Doiw%2BuiP2dEImpES6AJor6KSMQIfE%2F1IT%2FJu0iCaCwAbiwRnxF2IFbREu6Su6YwIIfQxj5oiMTDDBZlntQByQnxmOGoYmWJV&X-Amz-Signature=74f5a4a9b345d64c2e472ee7e3a1640b23484c03c4e0618185cd0eb3c08c5084&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 2. Scatter Plot
Scatter plots present the relationship between two variables in a dataset. It represents data points on a two-dimensional plane. The independent variable or attribute is plotted on the X-axis, while the dependent variable is plotted on the Y-axis.
**Syntax:**
```python
plt.scatter(x, y)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23708af9-659f-4f23-b626-1a4292d7842c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YZWY3Q6Z%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T041748Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDwaCXVzLXdlc3QtMiJHMEUCIQC8eV3pGVe%2Fn%2F%2BtaUs7U9xgeQx7rv1Feqx8oESh%2F%2BJkugIgbPukS56Q9KeM1kqXuvlagzILuwcBvsEzaC3gcRZ9lWcq%2FwMIVRAAGgw2Mzc0MjMxODM4MDUiDIeXbu5WLgEvG6W0RSrcA6PPZ71qGDD3FR41%2FpWMlGSW4gJ96DAS5276pi2JKFoahJcx8eyxMXbvYlEw9Ydj8ujQx41VslEJO5SE%2FcUbBaP4xd2Ebh1AG3cLys1XzgBVcrMS%2F28%2B2FsdzhUuef%2F7flXc2eqq141Nza84xvdFIwYZCFdmqa1j8v6B7EiwYS6Q67rn34JweLKvpjg3MFQDfpsEEAVmpolM7wg9GrbFNVkWbo8UVjf0Rh7eXcuSU9UyN5xHVAqexY5TcTItHYzHGRlYIX%2BR2%2FTO%2Fxu1cz0Ys50kz8Pu9n5rhqMdIoF9C1CNt9SSTI%2FoSNJwWOgPQbFdZBJPq%2BHAY%2FA2i%2BRGYmzXg6VqlZxvRhSRV%2B%2FjFPJE5ODWYlXqcFfX1xFCXkwhJwjKSdpxWQBPs%2BrJZmPf%2FVrHeCqgxSzH2wtfkxhZ8hUmnVBYfmr1rGxFNO%2BS1Ufb9%2BhbR6%2FpS4%2BDcUxeFarZo0RU%2FgYp4Jlo8KXXMudCBrDJkhwJWrpglFdYn0P7FSbHoHUa8FrKhv5FTSCsJbfZ4uvMebk%2B3MQoa4u4QPbV9%2F2vjqWQyjGP7BwkYO292V%2FyD81g8r85TSLHCd407aLduC6AigLQxieJWXypNUWUeb7PLx6kokMwH%2F7swH8pl8qMMOnfkL0GOqUBLjnpso9ASO1WlKoiYeaB6KaznEBfiPvsylAN8PxkL9l2gAj%2F%2B%2BRhTwEX6b%2Bsp2Dyr0znm0EDlhWZp%2BSRw%2BaSzjsnYspUcuv3tcsSV5Qhb7HWqfdhBW5BD3hPVvi0Doiw%2BuiP2dEImpES6AJor6KSMQIfE%2F1IT%2FJu0iCaCwAbiwRnxF2IFbREu6Su6YwIIfQxj5oiMTDDBZlntQByQnxmOGoYmWJV&X-Amz-Signature=e029988229e1eadb53c8a489cf8b7302e1b5f8574d5e25fe2353f410fd991f22&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 3. Histogram
A histogram is an important visual representation of data in categorical form. To view the data in a "Binned" form, use the histogram plot with a number of bins required or with the data points that mark the bin edges. The x-axis represents the data bins, and the y-axis represents the number of elements in each bin.
**Syntax:**
```python
plt.hist(x, bins)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/24e4424a-df87-40a1-b63b-195cbdc2e0ab/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YZWY3Q6Z%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T041748Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDwaCXVzLXdlc3QtMiJHMEUCIQC8eV3pGVe%2Fn%2F%2BtaUs7U9xgeQx7rv1Feqx8oESh%2F%2BJkugIgbPukS56Q9KeM1kqXuvlagzILuwcBvsEzaC3gcRZ9lWcq%2FwMIVRAAGgw2Mzc0MjMxODM4MDUiDIeXbu5WLgEvG6W0RSrcA6PPZ71qGDD3FR41%2FpWMlGSW4gJ96DAS5276pi2JKFoahJcx8eyxMXbvYlEw9Ydj8ujQx41VslEJO5SE%2FcUbBaP4xd2Ebh1AG3cLys1XzgBVcrMS%2F28%2B2FsdzhUuef%2F7flXc2eqq141Nza84xvdFIwYZCFdmqa1j8v6B7EiwYS6Q67rn34JweLKvpjg3MFQDfpsEEAVmpolM7wg9GrbFNVkWbo8UVjf0Rh7eXcuSU9UyN5xHVAqexY5TcTItHYzHGRlYIX%2BR2%2FTO%2Fxu1cz0Ys50kz8Pu9n5rhqMdIoF9C1CNt9SSTI%2FoSNJwWOgPQbFdZBJPq%2BHAY%2FA2i%2BRGYmzXg6VqlZxvRhSRV%2B%2FjFPJE5ODWYlXqcFfX1xFCXkwhJwjKSdpxWQBPs%2BrJZmPf%2FVrHeCqgxSzH2wtfkxhZ8hUmnVBYfmr1rGxFNO%2BS1Ufb9%2BhbR6%2FpS4%2BDcUxeFarZo0RU%2FgYp4Jlo8KXXMudCBrDJkhwJWrpglFdYn0P7FSbHoHUa8FrKhv5FTSCsJbfZ4uvMebk%2B3MQoa4u4QPbV9%2F2vjqWQyjGP7BwkYO292V%2FyD81g8r85TSLHCd407aLduC6AigLQxieJWXypNUWUeb7PLx6kokMwH%2F7swH8pl8qMMOnfkL0GOqUBLjnpso9ASO1WlKoiYeaB6KaznEBfiPvsylAN8PxkL9l2gAj%2F%2B%2BRhTwEX6b%2Bsp2Dyr0znm0EDlhWZp%2BSRw%2BaSzjsnYspUcuv3tcsSV5Qhb7HWqfdhBW5BD3hPVvi0Doiw%2BuiP2dEImpES6AJor6KSMQIfE%2F1IT%2FJu0iCaCwAbiwRnxF2IFbREu6Su6YwIIfQxj5oiMTDDBZlntQByQnxmOGoYmWJV&X-Amz-Signature=e2800c08ae7f424344aa266d78be2bd0e28a74a374ad231f6af7769076be1d59&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ab5a6dfe-51f5-43ee-bcb3-33dae4a1c7ad/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YZWY3Q6Z%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T041748Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDwaCXVzLXdlc3QtMiJHMEUCIQC8eV3pGVe%2Fn%2F%2BtaUs7U9xgeQx7rv1Feqx8oESh%2F%2BJkugIgbPukS56Q9KeM1kqXuvlagzILuwcBvsEzaC3gcRZ9lWcq%2FwMIVRAAGgw2Mzc0MjMxODM4MDUiDIeXbu5WLgEvG6W0RSrcA6PPZ71qGDD3FR41%2FpWMlGSW4gJ96DAS5276pi2JKFoahJcx8eyxMXbvYlEw9Ydj8ujQx41VslEJO5SE%2FcUbBaP4xd2Ebh1AG3cLys1XzgBVcrMS%2F28%2B2FsdzhUuef%2F7flXc2eqq141Nza84xvdFIwYZCFdmqa1j8v6B7EiwYS6Q67rn34JweLKvpjg3MFQDfpsEEAVmpolM7wg9GrbFNVkWbo8UVjf0Rh7eXcuSU9UyN5xHVAqexY5TcTItHYzHGRlYIX%2BR2%2FTO%2Fxu1cz0Ys50kz8Pu9n5rhqMdIoF9C1CNt9SSTI%2FoSNJwWOgPQbFdZBJPq%2BHAY%2FA2i%2BRGYmzXg6VqlZxvRhSRV%2B%2FjFPJE5ODWYlXqcFfX1xFCXkwhJwjKSdpxWQBPs%2BrJZmPf%2FVrHeCqgxSzH2wtfkxhZ8hUmnVBYfmr1rGxFNO%2BS1Ufb9%2BhbR6%2FpS4%2BDcUxeFarZo0RU%2FgYp4Jlo8KXXMudCBrDJkhwJWrpglFdYn0P7FSbHoHUa8FrKhv5FTSCsJbfZ4uvMebk%2B3MQoa4u4QPbV9%2F2vjqWQyjGP7BwkYO292V%2FyD81g8r85TSLHCd407aLduC6AigLQxieJWXypNUWUeb7PLx6kokMwH%2F7swH8pl8qMMOnfkL0GOqUBLjnpso9ASO1WlKoiYeaB6KaznEBfiPvsylAN8PxkL9l2gAj%2F%2B%2BRhTwEX6b%2Bsp2Dyr0znm0EDlhWZp%2BSRw%2BaSzjsnYspUcuv3tcsSV5Qhb7HWqfdhBW5BD3hPVvi0Doiw%2BuiP2dEImpES6AJor6KSMQIfE%2F1IT%2FJu0iCaCwAbiwRnxF2IFbREu6Su6YwIIfQxj5oiMTDDBZlntQByQnxmOGoYmWJV&X-Amz-Signature=769a223dc238f4e94e6e6e43cb99b782545deb120116cbefbc6e7ed5f23799b1&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8f1b1d60-cf1b-42b3-9faa-f634c89c3f84/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YZWY3Q6Z%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T041748Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDwaCXVzLXdlc3QtMiJHMEUCIQC8eV3pGVe%2Fn%2F%2BtaUs7U9xgeQx7rv1Feqx8oESh%2F%2BJkugIgbPukS56Q9KeM1kqXuvlagzILuwcBvsEzaC3gcRZ9lWcq%2FwMIVRAAGgw2Mzc0MjMxODM4MDUiDIeXbu5WLgEvG6W0RSrcA6PPZ71qGDD3FR41%2FpWMlGSW4gJ96DAS5276pi2JKFoahJcx8eyxMXbvYlEw9Ydj8ujQx41VslEJO5SE%2FcUbBaP4xd2Ebh1AG3cLys1XzgBVcrMS%2F28%2B2FsdzhUuef%2F7flXc2eqq141Nza84xvdFIwYZCFdmqa1j8v6B7EiwYS6Q67rn34JweLKvpjg3MFQDfpsEEAVmpolM7wg9GrbFNVkWbo8UVjf0Rh7eXcuSU9UyN5xHVAqexY5TcTItHYzHGRlYIX%2BR2%2FTO%2Fxu1cz0Ys50kz8Pu9n5rhqMdIoF9C1CNt9SSTI%2FoSNJwWOgPQbFdZBJPq%2BHAY%2FA2i%2BRGYmzXg6VqlZxvRhSRV%2B%2FjFPJE5ODWYlXqcFfX1xFCXkwhJwjKSdpxWQBPs%2BrJZmPf%2FVrHeCqgxSzH2wtfkxhZ8hUmnVBYfmr1rGxFNO%2BS1Ufb9%2BhbR6%2FpS4%2BDcUxeFarZo0RU%2FgYp4Jlo8KXXMudCBrDJkhwJWrpglFdYn0P7FSbHoHUa8FrKhv5FTSCsJbfZ4uvMebk%2B3MQoa4u4QPbV9%2F2vjqWQyjGP7BwkYO292V%2FyD81g8r85TSLHCd407aLduC6AigLQxieJWXypNUWUeb7PLx6kokMwH%2F7swH8pl8qMMOnfkL0GOqUBLjnpso9ASO1WlKoiYeaB6KaznEBfiPvsylAN8PxkL9l2gAj%2F%2B%2BRhTwEX6b%2Bsp2Dyr0znm0EDlhWZp%2BSRw%2BaSzjsnYspUcuv3tcsSV5Qhb7HWqfdhBW5BD3hPVvi0Doiw%2BuiP2dEImpES6AJor6KSMQIfE%2F1IT%2FJu0iCaCwAbiwRnxF2IFbREu6Su6YwIIfQxj5oiMTDDBZlntQByQnxmOGoYmWJV&X-Amz-Signature=a394316b4ffc9a0007ca174881815c4aac682317d68966f62806a5489c6c16f3&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/13ad0497-05fe-4eaa-984e-707b33e14761/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YZWY3Q6Z%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T041748Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDwaCXVzLXdlc3QtMiJHMEUCIQC8eV3pGVe%2Fn%2F%2BtaUs7U9xgeQx7rv1Feqx8oESh%2F%2BJkugIgbPukS56Q9KeM1kqXuvlagzILuwcBvsEzaC3gcRZ9lWcq%2FwMIVRAAGgw2Mzc0MjMxODM4MDUiDIeXbu5WLgEvG6W0RSrcA6PPZ71qGDD3FR41%2FpWMlGSW4gJ96DAS5276pi2JKFoahJcx8eyxMXbvYlEw9Ydj8ujQx41VslEJO5SE%2FcUbBaP4xd2Ebh1AG3cLys1XzgBVcrMS%2F28%2B2FsdzhUuef%2F7flXc2eqq141Nza84xvdFIwYZCFdmqa1j8v6B7EiwYS6Q67rn34JweLKvpjg3MFQDfpsEEAVmpolM7wg9GrbFNVkWbo8UVjf0Rh7eXcuSU9UyN5xHVAqexY5TcTItHYzHGRlYIX%2BR2%2FTO%2Fxu1cz0Ys50kz8Pu9n5rhqMdIoF9C1CNt9SSTI%2FoSNJwWOgPQbFdZBJPq%2BHAY%2FA2i%2BRGYmzXg6VqlZxvRhSRV%2B%2FjFPJE5ODWYlXqcFfX1xFCXkwhJwjKSdpxWQBPs%2BrJZmPf%2FVrHeCqgxSzH2wtfkxhZ8hUmnVBYfmr1rGxFNO%2BS1Ufb9%2BhbR6%2FpS4%2BDcUxeFarZo0RU%2FgYp4Jlo8KXXMudCBrDJkhwJWrpglFdYn0P7FSbHoHUa8FrKhv5FTSCsJbfZ4uvMebk%2B3MQoa4u4QPbV9%2F2vjqWQyjGP7BwkYO292V%2FyD81g8r85TSLHCd407aLduC6AigLQxieJWXypNUWUeb7PLx6kokMwH%2F7swH8pl8qMMOnfkL0GOqUBLjnpso9ASO1WlKoiYeaB6KaznEBfiPvsylAN8PxkL9l2gAj%2F%2B%2BRhTwEX6b%2Bsp2Dyr0znm0EDlhWZp%2BSRw%2BaSzjsnYspUcuv3tcsSV5Qhb7HWqfdhBW5BD3hPVvi0Doiw%2BuiP2dEImpES6AJor6KSMQIfE%2F1IT%2FJu0iCaCwAbiwRnxF2IFbREu6Su6YwIIfQxj5oiMTDDBZlntQByQnxmOGoYmWJV&X-Amz-Signature=ac0df755737022858bd872167cfe58a8f39da0386e31bfee80831d5bc6f79dc2&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 2. Box and Whisker Plot
A box plot shows the distribution of quantitative data in a way that facilitates comparisons between variables or across levels of a categorical variable. The box shows the quartiles of the dataset while the whiskers extend to show the rest of the distribution, except for points that are determined to be "outliers".
**Syntax:**
```python
sns.boxplot(x='header_1', y='header_2', data=df)
```
**Example Output:**


![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d207ae92-0a7c-4e2f-aa65-0ee5a2c33bf7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZT3MAUJ4%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T041751Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDwaCXVzLXdlc3QtMiJHMEUCIQCCBeFbtLj7xAJtaPJSPNRtsj%2FWoSf9y5KeffG0KaQBYAIgBJrflWZ4k%2BUj6igNQZ1qGnjgSVNMmDsCvC9U0u7JSPQq%2FwMIVRAAGgw2Mzc0MjMxODM4MDUiDOMPQW3z2RnCIqP15SrcA9iuYiBXjxQAYb6waP%2FDzxMCCNj9T%2Fzr%2FfX5z%2F367dsZ4B6l2fvYk7iyXoXnG9FpKTOo1DNSRueU7l8k5MYpSbGbiCBadfEV6LRFDlIz4%2F4l7ufZPy3z29oSXQWqfNfZoYAyd08WC2DNLwUwcoWSfSEyZTnVc8DeGiboP1SRjieXKRVg3MmS7w6vi9bdpJoyi8SpRzLTA6eMCUC77tsJs%2F%2Fq4uJvbkQnKTact6ZN8GNN0xqrQVU%2BzYLEZtctIVDh0KrlgDqLAxXqAw4vpABVAntU8Nmnyo%2B6nqwTpJmjnutfLsL0JHOK8iSq0dC5JfHNPMMiydj7TyeXdnFqjKgyxqcF90ND9Npi533DFP4g2c5VYoq8sSngG8lP2DZnoBKsTA00cOP%2FHyLKp4CuGOthyFLgzm%2BLUSDvIl7X1GjPUWlhorJiFVCNxyH2IZmsIyCotnKy%2FL1C3woTO%2BFZHSiLyJb4lc0wbgOc6lxbE%2FCOEYGkXAE78hyEhoo1hXMcfYnV01mOEZ01YqbclOO2p1QnOgMmOaGEYHGIUMghnsTL74BNRfC15UBfCBLbQ7Jp6iQ9aCfTR6I%2BQl4rxmrBDd3gD0x93ezatNNFNximW5iGX06KqiZF2Y4KKT7fcp28MPvfkL0GOqUBEew5khLWCt6qL5zDaAnAPRmG6Wy7A5EexqQ6W5uilPUgnf9n9cxkF4XP8mGwDdnNNK8WMecTnMsDfvZDL69Tl%2FOZjiIW3cRMimHLKhn2JZr%2FuHWgBiy55AZtHWfgNKf6IQTUfdTqboHukQqGT9IYZP%2BilqXTzUDAq6bod4bb7Ekam%2BDrtRhnMSgfq0KazPRYh%2FXnF1QF3dtHQ1arjFxpUqdOo%2Bju&X-Amz-Signature=d0cde241b62790380e016e79b3cdf47182b8491d0f967ff2df1569e565cde33b&X-Amz-SignedHeaders=host&x-id=GetObject)

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0e516edc-7551-4792-ab18-0494db3c4c0c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YO3XZ74I%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T041749Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDwaCXVzLXdlc3QtMiJHMEUCIQD1QFTqWuuEtqaMJ%2FJ2emU8BEdfecbga7GvmP4lzepQZwIgWqc32bPEfj4PzRoP8%2FiQ9o%2FH%2FtYJ1LRXiDaOYd7E4gcq%2FwMIVRAAGgw2Mzc0MjMxODM4MDUiDPQEqan%2FtbaS%2BZXDOircA%2BmlT1FPRqXuzUOXVkt8iIGjUi08BkfjRFlNQ3pIjOTvrPh1wZewUmqhAiGKPrH6alWnwGAETezpn6Or4DUFZRlxfpb%2Bczs6WGZmh1MxprVQ1S%2B%2BsL4%2FMN%2B2nizsdYHpR6OGIq4pL9mz06sVMeBqxPsQKu%2BcdTLFwnxe%2BUlfLnDeWurWLSCY4J3%2FzCmSP9lccW7lqAg2%2BVNYnOOhj2XBRqY2bxBgpmtCHi0Wt3rbHmebUuBj3yFclmcTTJiaKT60cxQOCJClM9IO9NOFPL0Ypu5iPOo%2FrdfH0efvDYPI9Mw7x3lIJO0USwqGkEfALiNud0PUqwUT3JX%2FdgdFDWo6fE186B7CEY4jazVv4jqo95%2FGZFSBkRfaguTS4dT%2FTGINBgH7RtzEkg6JUZVy40n7pWN01JncCEkexnXzhzIkrOSAxj8IpFPtWLAgI7A%2FK5jLJD5lJvu6YmsHdhaAFVRvIK1G%2BENrto311GBRU7G3x1eyhIOIjm1d7TdEzZsE6CPGO6ZKX7ti7dQISH9OzUjpJA1YoJwnii4hnNYnZ8%2Ft0qkaPLYT14VS04eu%2BwO%2FF0JyGOwuULgR5EKc%2FJwx3ScUeRjOiX8jBIWvk7rYGpSY4%2BhGOLEO9U3YBgxGmmmOMOPfkL0GOqUBqD%2FZaGqIPDTmFDib5wAsY9hN3cd2IK%2BrBVDoLyouKVfQfmyCVLJPvS0MB3dptVBiocTKAmAlHfjC0j2XaHl6oxv7y%2BAWBkfQshUtCvF0Mb7EBUOreMfHJnBsH1Yr75giO2HCIuvP38oq9EgxHmm4SxEh9gXTk2qqIKcK95MxHegQoI96B%2FmZ%2BroA5%2B1Kc3df%2B39gsKvmpEaf2nRJ8OIcOFlQZVX6&X-Amz-Signature=baff121444654f63f493ffbd14859b46bebad7ed028f4c9ca50e8944ba8923ca&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23a79b9d-2356-49a9-8fd9-65c6b0ab2cc5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YZWY3Q6Z%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T041748Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDwaCXVzLXdlc3QtMiJHMEUCIQC8eV3pGVe%2Fn%2F%2BtaUs7U9xgeQx7rv1Feqx8oESh%2F%2BJkugIgbPukS56Q9KeM1kqXuvlagzILuwcBvsEzaC3gcRZ9lWcq%2FwMIVRAAGgw2Mzc0MjMxODM4MDUiDIeXbu5WLgEvG6W0RSrcA6PPZ71qGDD3FR41%2FpWMlGSW4gJ96DAS5276pi2JKFoahJcx8eyxMXbvYlEw9Ydj8ujQx41VslEJO5SE%2FcUbBaP4xd2Ebh1AG3cLys1XzgBVcrMS%2F28%2B2FsdzhUuef%2F7flXc2eqq141Nza84xvdFIwYZCFdmqa1j8v6B7EiwYS6Q67rn34JweLKvpjg3MFQDfpsEEAVmpolM7wg9GrbFNVkWbo8UVjf0Rh7eXcuSU9UyN5xHVAqexY5TcTItHYzHGRlYIX%2BR2%2FTO%2Fxu1cz0Ys50kz8Pu9n5rhqMdIoF9C1CNt9SSTI%2FoSNJwWOgPQbFdZBJPq%2BHAY%2FA2i%2BRGYmzXg6VqlZxvRhSRV%2B%2FjFPJE5ODWYlXqcFfX1xFCXkwhJwjKSdpxWQBPs%2BrJZmPf%2FVrHeCqgxSzH2wtfkxhZ8hUmnVBYfmr1rGxFNO%2BS1Ufb9%2BhbR6%2FpS4%2BDcUxeFarZo0RU%2FgYp4Jlo8KXXMudCBrDJkhwJWrpglFdYn0P7FSbHoHUa8FrKhv5FTSCsJbfZ4uvMebk%2B3MQoa4u4QPbV9%2F2vjqWQyjGP7BwkYO292V%2FyD81g8r85TSLHCd407aLduC6AigLQxieJWXypNUWUeb7PLx6kokMwH%2F7swH8pl8qMMOnfkL0GOqUBLjnpso9ASO1WlKoiYeaB6KaznEBfiPvsylAN8PxkL9l2gAj%2F%2B%2BRhTwEX6b%2Bsp2Dyr0znm0EDlhWZp%2BSRw%2BaSzjsnYspUcuv3tcsSV5Qhb7HWqfdhBW5BD3hPVvi0Doiw%2BuiP2dEImpES6AJor6KSMQIfE%2F1IT%2FJu0iCaCwAbiwRnxF2IFbREu6Su6YwIIfQxj5oiMTDDBZlntQByQnxmOGoYmWJV&X-Amz-Signature=b9de7272dc65a51bde5512de70b818dd557687ca8f044cdb1ffcf850460e2419&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 4. KDE Plot
A Kernel Density Estimate (KDE) plot is a graph that creates a probability distribution curve for the data based upon its likelihood of occurrence on a specific value. This is created for a single vector of information.
**Syntax:**
```python
sns.kdeplot(X) || sns.kdeplot(df['age'])
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0d571213-2a2f-4921-a50b-880847aa05ee/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YZWY3Q6Z%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T041748Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDwaCXVzLXdlc3QtMiJHMEUCIQC8eV3pGVe%2Fn%2F%2BtaUs7U9xgeQx7rv1Feqx8oESh%2F%2BJkugIgbPukS56Q9KeM1kqXuvlagzILuwcBvsEzaC3gcRZ9lWcq%2FwMIVRAAGgw2Mzc0MjMxODM4MDUiDIeXbu5WLgEvG6W0RSrcA6PPZ71qGDD3FR41%2FpWMlGSW4gJ96DAS5276pi2JKFoahJcx8eyxMXbvYlEw9Ydj8ujQx41VslEJO5SE%2FcUbBaP4xd2Ebh1AG3cLys1XzgBVcrMS%2F28%2B2FsdzhUuef%2F7flXc2eqq141Nza84xvdFIwYZCFdmqa1j8v6B7EiwYS6Q67rn34JweLKvpjg3MFQDfpsEEAVmpolM7wg9GrbFNVkWbo8UVjf0Rh7eXcuSU9UyN5xHVAqexY5TcTItHYzHGRlYIX%2BR2%2FTO%2Fxu1cz0Ys50kz8Pu9n5rhqMdIoF9C1CNt9SSTI%2FoSNJwWOgPQbFdZBJPq%2BHAY%2FA2i%2BRGYmzXg6VqlZxvRhSRV%2B%2FjFPJE5ODWYlXqcFfX1xFCXkwhJwjKSdpxWQBPs%2BrJZmPf%2FVrHeCqgxSzH2wtfkxhZ8hUmnVBYfmr1rGxFNO%2BS1Ufb9%2BhbR6%2FpS4%2BDcUxeFarZo0RU%2FgYp4Jlo8KXXMudCBrDJkhwJWrpglFdYn0P7FSbHoHUa8FrKhv5FTSCsJbfZ4uvMebk%2B3MQoa4u4QPbV9%2F2vjqWQyjGP7BwkYO292V%2FyD81g8r85TSLHCd407aLduC6AigLQxieJWXypNUWUeb7PLx6kokMwH%2F7swH8pl8qMMOnfkL0GOqUBLjnpso9ASO1WlKoiYeaB6KaznEBfiPvsylAN8PxkL9l2gAj%2F%2B%2BRhTwEX6b%2Bsp2Dyr0znm0EDlhWZp%2BSRw%2BaSzjsnYspUcuv3tcsSV5Qhb7HWqfdhBW5BD3hPVvi0Doiw%2BuiP2dEImpES6AJor6KSMQIfE%2F1IT%2FJu0iCaCwAbiwRnxF2IFbREu6Su6YwIIfQxj5oiMTDDBZlntQByQnxmOGoYmWJV&X-Amz-Signature=1680e1a7b188e5f0d8cfab7a9afd4fc47c904a30d526617a1b0a988afc9fc95b&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/53752550-ef82-4ca9-a01a-09921f0282d0/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YZWY3Q6Z%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T041748Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDwaCXVzLXdlc3QtMiJHMEUCIQC8eV3pGVe%2Fn%2F%2BtaUs7U9xgeQx7rv1Feqx8oESh%2F%2BJkugIgbPukS56Q9KeM1kqXuvlagzILuwcBvsEzaC3gcRZ9lWcq%2FwMIVRAAGgw2Mzc0MjMxODM4MDUiDIeXbu5WLgEvG6W0RSrcA6PPZ71qGDD3FR41%2FpWMlGSW4gJ96DAS5276pi2JKFoahJcx8eyxMXbvYlEw9Ydj8ujQx41VslEJO5SE%2FcUbBaP4xd2Ebh1AG3cLys1XzgBVcrMS%2F28%2B2FsdzhUuef%2F7flXc2eqq141Nza84xvdFIwYZCFdmqa1j8v6B7EiwYS6Q67rn34JweLKvpjg3MFQDfpsEEAVmpolM7wg9GrbFNVkWbo8UVjf0Rh7eXcuSU9UyN5xHVAqexY5TcTItHYzHGRlYIX%2BR2%2FTO%2Fxu1cz0Ys50kz8Pu9n5rhqMdIoF9C1CNt9SSTI%2FoSNJwWOgPQbFdZBJPq%2BHAY%2FA2i%2BRGYmzXg6VqlZxvRhSRV%2B%2FjFPJE5ODWYlXqcFfX1xFCXkwhJwjKSdpxWQBPs%2BrJZmPf%2FVrHeCqgxSzH2wtfkxhZ8hUmnVBYfmr1rGxFNO%2BS1Ufb9%2BhbR6%2FpS4%2BDcUxeFarZo0RU%2FgYp4Jlo8KXXMudCBrDJkhwJWrpglFdYn0P7FSbHoHUa8FrKhv5FTSCsJbfZ4uvMebk%2B3MQoa4u4QPbV9%2F2vjqWQyjGP7BwkYO292V%2FyD81g8r85TSLHCd407aLduC6AigLQxieJWXypNUWUeb7PLx6kokMwH%2F7swH8pl8qMMOnfkL0GOqUBLjnpso9ASO1WlKoiYeaB6KaznEBfiPvsylAN8PxkL9l2gAj%2F%2B%2BRhTwEX6b%2Bsp2Dyr0znm0EDlhWZp%2BSRw%2BaSzjsnYspUcuv3tcsSV5Qhb7HWqfdhBW5BD3hPVvi0Doiw%2BuiP2dEImpES6AJor6KSMQIfE%2F1IT%2FJu0iCaCwAbiwRnxF2IFbREu6Su6YwIIfQxj5oiMTDDBZlntQByQnxmOGoYmWJV&X-Amz-Signature=2560114eeab7ea2ba5650f8cc4bd7b2d7bfb2eb1b2e45e0da5930e8d68260438&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
## 4. Correlation Between Variables
Correlation is a statistical measure of the extent to which different variables are interdependent. It indicates how changes in one variable are associated with changes in another variable over time.
### Positive Correlation
Positive correlation indicates that as one variable increases, the other variable also tends to increase.
**Example: Engine Size and Price**
- **Positive Correlation:** Engine size increases, price also increases.
- **Visualization:** Scatter plot with a steep positive slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c7ea9b0-3ef3-4357-a9c3-554fc71b6b15/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662T7RRASK%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T041749Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDwaCXVzLXdlc3QtMiJHMEUCIQDohlJvcw8mWK3hxKsb6hffZRIO%2BAYYcpQdP5%2FOOjd7dQIgeqTbb5qMqSoHF22maNKJeRlNMgnOK%2Ftc5mLbMTXTu6Qq%2FwMIVRAAGgw2Mzc0MjMxODM4MDUiDBLyNG0iRj9xACZLqircA6Y2b563Z7%2Fk42fNuJ8wlNcvbjFya4dR4rSvvuBkN7RuFFufeY14hkvLIvJHCzksDozXZ5DPgNbAvmGiEdNSCIwoQIP1cS0YfN2j45pKYc2Yd0HoCt0gRla6AMXelfOvIh7TS4j7uFH%2FbehPUrxgtHDPHjrOey4quHuL3A2Jvf%2BwSd76tm9o3Aa0LSoYrWhwGntKYve3ZREsWTMCE4jqyv%2BuA4Xq6nGPKT%2FMfr0poCw9iKzXjhrgB%2BmPoRD3IJqKXvNH4%2B4HMh24FvnqdDl1jue9S4OQqHRsvLgrXy6gUWADSFSq6I5kfN3QJm2Gg6WG%2FmH6eoVwx2tYNir2sNJ%2FLGA7E03uqF%2FPIUWAQr5xEpo0DFFarcFeLA%2BSCk5Li6zboHASnnrmxfVQmjboZ5nW0UnuOlzwjboiDlbDfukpcofw%2B0umimbUunr6hNeJcvUBCgfrmx38y%2Bxv5B%2F%2F2andmgMr%2FdGiiFg6SWuMg8oWw4udngtmKT%2BJnaGybv5ZwMvx2irBNQH8QtQEq0DH%2Bw2BRaLqpbjGZ1Lfldaf9QjTZa4bETUqXJHqTrMVqyp%2FOSQxR1KCbKXitfcqBJW%2BWZoJZgKcuFRRwtzG0L9m8BgD8WFycGtCcTMisoyOqoSXMPffkL0GOqUBXBBpwA%2F%2F1w24MPa8wTA5brsXO0sbZD0b4CMuQ4yr%2F4JVwlz2LZb%2FPOMoXTZRrQKhhylBvzUIMOVFHqE%2ByIuDGpr4omH0smO%2B92C%2FNL2DAzzlmif9reyef1ZHC0UzRo%2BBGIDZs9NQu22NDeGuDTqBc9OCN0Gwq9PYQenSJ6%2FZuB1%2B9uEjkht12HBd81g65y4vJH%2FaA5U1%2BbjDd0h8WUr8bJjZpsVX&X-Amz-Signature=6ef2511311c450fc734bbdeebad1df237f22a2892e904791fdb169ae300e7a20&X-Amz-SignedHeaders=host&x-id=GetObject)
**Explanation:** When engine size increases, there is a corresponding increase in the price of the vehicle. This positive correlation suggests that larger engines tend to be associated with higher prices in the market.
___
### Negative Correlation
Negative correlation indicates that as one variable increases, the other variable tends to decrease.
**Example: Highway Miles per Gallon and Price**
- **Negative Correlation:** As highway miles per gallon increases, price decreases.
- **Visualization:** Scatter plot with a steep negative slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/10f1f798-9cc4-4df2-a9c1-5a339f554a0b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46665RLM27K%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T041749Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDwaCXVzLXdlc3QtMiJIMEYCIQDUPywYFA%2FpiU6PvWrZOtzNP3BKu2xKfPeIC%2BF4R1FCMQIhALiDHw5D%2B9DGuSsEm4LStogGdVabLJ13yJvcPTlk1g9sKv8DCFUQABoMNjM3NDIzMTgzODA1IgwpVbe0ckkWFaLCJWwq3APC2qP5fPjeuLn8%2B9h92lHNzxagzJbs9uct78ESBm6ewwqS7GCs3dzUoTCFz6r3B9P2Xyn8l%2Bgl5T7Z9KFEULLs3j8FTjX6INiuvb%2BDrmmRX0To6HRukMLq9ath25sBeF%2F9WAVPTB3rBqJBo3SIMFopP369c45IH7RT841O57tyNYqbnBD4ympTojGKdaxCLX3BVcgZytBZ%2FFPaE9XF2rkUqWK8iuYUo%2FcSAApoJHVGuUK6WlwUMNMZg5zUwlEqB%2FBVNDI8zFRCD77kVV4fFuW%2BB3R1d39n4l3eGY7J3DWTZU6N2LBcIE391LX5%2F7ZnXWL353%2Fw8zmIOYCPZ54ZrT3dF2At5xyQxv7B%2FdjVrXHU4A%2BqAVMOaB%2F0cpaEoSgCOk%2FnLBZ43qcXtldEIbxmRAp0RD8cCWUXf2su%2BO4QGDNKT%2F%2B1B8ZZNfNh1uHLRFan8%2BFzu5TL1u%2BOEZo3HyRvhGnVM6hzcfpX4lPaznRvvHaQMNntn4fekeMkTtkuf8DB9Y%2BOPgXuTl4MwTdbOaYyyspG2QP73YYxd9ADXmCwL7vnifCvAXhN2hi7m9%2FGNz%2BWemXlqVNEpEek10XHtJnwgyz2%2BCdLKGV60nE6uOYMX13xZxnf5y047Xh6JzWcVjDW35C9BjqkAU4OZXzU9zRd3%2BHpUMLKBZjZ4tK1kLke1123h6B9RZ9hq251l5bXsfDTuWdXD6NoNVqw7XljEWUwR3dwH%2F5FVUTJZUd6nIV4TRUkCWBexsqybpPsJDeN7OXcFXo5DKURXpKQev3OIN9r94Y8gaIQ1TJ5zZR5CN4rbYLt4YNU74EIu%2FYReoYFPJ%2FemHIHFpGWlzfnCiINXyma4jt3v954o7HDmJxw&X-Amz-Signature=946a110e5c3d9c8daa33f6e74b684af31af9aec11e286f44cfd5ca25463b4036&X-Amz-SignedHeaders=host&x-id=GetObject)
**Explanation:** When highway miles per gallon increases, the price of the vehicle tends to decrease. This negative correlation suggests that cars with higher fuel efficiency (more miles per gallon) are generally priced lower in the market.
___
### Weak Correlation
Weak correlation indicates a lack of strong relationship between the variables.
**Example: RPM and Price**
- **Weak Correlation:** Low and high RPM values show varied prices, indicating no strong predictive relationship.
- **Visualization:** Scatter plot with no clear trend or slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9f914514-8914-4bf4-ac84-d9e3077f6eb1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QHYAAHUK%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T041749Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDwaCXVzLXdlc3QtMiJGMEQCIC7wJuFsN8w8WW03NZEv72n3vY5i1JbIezk2u9kA8YAtAiArsp2XKvWEbYkQ5gVed%2F7IWcXmcmpST99TYHiUduaujyr%2FAwhVEAAaDDYzNzQyMzE4MzgwNSIM3AyFggK3f0J73TmzKtwDsUogHlgL%2Bek3PWxp4FEorbkxZ6fZMNO%2BmJf0wow5J9ogQaQZs5tY%2FD%2BFGU3Q2p8k1DOFvps1rsYWM1Xz8B1fnSh52wjYVxsw1SV8%2B71IkeWvu8DHbtIKtM1biWIBBUualrSBB0E%2FTzqil%2BdchT3P%2FgvsPkg92%2Fd7W39oFXmwvdcMjTI59J9q%2BVl5NJIiIKTx26Zu%2BTcRsmwtYwL71QzJccMFQKGnO2JiOa3MEbqkyilyg2wiGdiYHqAVuss6CscnchGgOM%2Bt7kxswpCYIBA%2BBlMePxcoOyYK3bP50rGt9hW5TH8JjDz7E2D1h2DEyiVs5EJd5ou2c%2FG0aRSIhnRwcb7RShm10CCLTlZbCj25p23LaB%2FbUFvz28dchMF2rE1lMTAuNagDBohus%2F9HRRR%2FKCb%2Bxvxy3SMg0%2Bn9sXJbYrAAuUXG%2BtIkzkW4DVCt%2B8oXiCIaRcVCdkgk6Jf9EfmBq1vodShMr2E%2BaoUSRYmYOaiDlovwN%2FzdYKYcaeBVVTs5TM%2FcVQ7IUzYqgWVPwgvoDwKNLmL5KfHiipX2BLY3KLJiqs6BXATupFAS0pYuves9nJOZMNUDutr3VMT7rj7xK2cDTeduqirYlAiOMLSCw2LkH6i6hrrG%2FgCp7L4w29%2BQvQY6pgFyUzNOk0ryj%2FN25nmIzilzF2K4M1rjwR8Y0uXJoMQK1dgZVakASe127NdCUUs%2F1dJdR2tvSdixHW0aS3z0TGIsMYYh4lJlm82Xn%2FV7eMyQU%2FO6e2b83J0yiQ3jS4M1DS4WVjLm9WVfK%2FkTtBOPz5z1P%2BVQS3yLo2iH2pK0VgUJ5u3iQYMLY1%2FJ9ELxnbVBatKu7BOfByP2rQj81W01SzGj0GrfvWS3&X-Amz-Signature=3547efbd107647d0f15e0ba1cdaf05230915bfa7381f7ccd7d82bc59a0d5e283&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f18086e5-5b04-4fbf-8309-8944ab20d213/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YRTEJ46P%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T041749Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDwaCXVzLXdlc3QtMiJHMEUCIA3w5%2BecWGKBRNcAOq2YfW1oFzzDqBFGFyjh98RiGpCpAiEAkVXRSTtVBEho%2B8jyjK773i%2BNtGs%2BEpuHwU2V%2BnaxIHoq%2FwMIVRAAGgw2Mzc0MjMxODM4MDUiDBM0hs%2BPjTEhRLQo4yrcA%2BTGTGeem8vEjYP0dUMqB8ZPw9R3l6cIkO8X7tV5ycsi6xWMNlLluREi%2F%2B2h%2FZGWmxUIfVgZ3vWrat4wk84rOEeUZf0MalkOKx%2BEsysCYN51ReBwUbZ4o4wjOTswXkkZiqqWQ9yfqpruI0NqNMja25xmFZDRIYc1KDNvsVpzwBMLg0NsMw9koz7UnPWUJaGfrzc%2FhAvojlp0uHKZdgo%2BUo%2F3QAwy%2BSfkonYSxYAfBb5nmWbnuBhjPJHNPEL%2Bgy8ZisH4pzK%2Fjan3wYumeiFR6DY7I6LSlvU6txRiT8a7mUk8TtjrgTM7U%2Fult3aE8yElLrFTUw0H9mQxmZxYQYMdzj59Ppu4%2Bemkws7se5UCL5P%2BsBAjQPfSfL5kjAVn4wmyv1ksDi9q7UFaE9Pk7ywQ7uFo1GdH0HQVKAYRGvqSi1bb%2FOBVnWMNXP45vIqBXQZwYpKjYWv0il4%2FCI1%2BhIGdvq%2Bsu5G7kPFDwo6%2BGpjmZicyaW1d6OlaLb8fqhWOAwtLfFLlgrb%2Bou%2BFGcQol2eGxZefIRI%2Fs3ne9zksZDVx8IS0ZabXuSm2xE32UKtmkSF6mSHEDtkTF%2BJSy%2BMXCZoPVfna7OeREVZ%2BWAOYPMe62JMC6nXKRUnS%2FqofOMN9MPXfkL0GOqUBL%2BpQeMBPb%2FoNJv4m2fGWcTbHIW453j5W4JyvyoBgz0K40iCSMTGq9BmZZ%2Fcid816TQfV7uQ7vmOklYHApQLPbvwprkS4JPzKGAa%2B7MEV03l54XARwaS4yNp07wZ3ZbdZrjO3Y11WAFHecQOri%2FkjoDI1gcvQ%2F3%2BVNOJtWZC%2FQtENc68eNHkH%2BjQ2l%2FcL9OecDRX7mLCUNu2hj6lSer0Juh1raQbT&X-Amz-Signature=0a88079523e080a71ab3f41bcfe9e697fdcff87929c128926a02cbaed058132c&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Correlation Plot
Heatmap visualizes correlations among variables. Color scheme indicates Pearson correlation coefficients. Dark red diagonal line shows perfect correlation (value of 1) between variables and themselves.
This heatmap offers overview of variable relationships and their link with price.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cd3b341e-cc1a-45f7-8aec-cdc00436d270/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YRTEJ46P%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T041749Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDwaCXVzLXdlc3QtMiJHMEUCIA3w5%2BecWGKBRNcAOq2YfW1oFzzDqBFGFyjh98RiGpCpAiEAkVXRSTtVBEho%2B8jyjK773i%2BNtGs%2BEpuHwU2V%2BnaxIHoq%2FwMIVRAAGgw2Mzc0MjMxODM4MDUiDBM0hs%2BPjTEhRLQo4yrcA%2BTGTGeem8vEjYP0dUMqB8ZPw9R3l6cIkO8X7tV5ycsi6xWMNlLluREi%2F%2B2h%2FZGWmxUIfVgZ3vWrat4wk84rOEeUZf0MalkOKx%2BEsysCYN51ReBwUbZ4o4wjOTswXkkZiqqWQ9yfqpruI0NqNMja25xmFZDRIYc1KDNvsVpzwBMLg0NsMw9koz7UnPWUJaGfrzc%2FhAvojlp0uHKZdgo%2BUo%2F3QAwy%2BSfkonYSxYAfBb5nmWbnuBhjPJHNPEL%2Bgy8ZisH4pzK%2Fjan3wYumeiFR6DY7I6LSlvU6txRiT8a7mUk8TtjrgTM7U%2Fult3aE8yElLrFTUw0H9mQxmZxYQYMdzj59Ppu4%2Bemkws7se5UCL5P%2BsBAjQPfSfL5kjAVn4wmyv1ksDi9q7UFaE9Pk7ywQ7uFo1GdH0HQVKAYRGvqSi1bb%2FOBVnWMNXP45vIqBXQZwYpKjYWv0il4%2FCI1%2BhIGdvq%2Bsu5G7kPFDwo6%2BGpjmZicyaW1d6OlaLb8fqhWOAwtLfFLlgrb%2Bou%2BFGcQol2eGxZefIRI%2Fs3ne9zksZDVx8IS0ZabXuSm2xE32UKtmkSF6mSHEDtkTF%2BJSy%2BMXCZoPVfna7OeREVZ%2BWAOYPMe62JMC6nXKRUnS%2FqofOMN9MPXfkL0GOqUBL%2BpQeMBPb%2FoNJv4m2fGWcTbHIW453j5W4JyvyoBgz0K40iCSMTGq9BmZZ%2Fcid816TQfV7uQ7vmOklYHApQLPbvwprkS4JPzKGAa%2B7MEV03l54XARwaS4yNp07wZ3ZbdZrjO3Y11WAFHecQOri%2FkjoDI1gcvQ%2F3%2BVNOJtWZC%2FQtENc68eNHkH%2BjQ2l%2FcL9OecDRX7mLCUNu2hj6lSer0Juh1raQbT&X-Amz-Signature=a57502cbe56b41dd05702cb469cd62bf83ae9d83f36fd2a5335bd77ec572b1f0&X-Amz-SignedHeaders=host&x-id=GetObject)

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
