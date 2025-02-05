

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7e6d594d-952e-44b6-97ea-31225882aea6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663UNLLDWK%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T051459Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECUaCXVzLXdlc3QtMiJHMEUCIQC1i%2FQeiSAEYRL%2FZC3SZt2%2FuWFuAz9n1RBOinMKGYCQmQIgAmAVtVDDd4TJG3YSqMHIKZHyINQ2YtaUNJoxafoO%2FNEq%2FwMIPhAAGgw2Mzc0MjMxODM4MDUiDOcd24ME7z0Ekqa8pCrcA6lyXsu9dYXTwLDvB7%2B6mtP4%2FaWwSIA2x6TSM9%2FogaGh5qzBoqoCi9%2BKF8M4aljkPUPBxof6kcKrMxzsg4eY%2BgdIfsqDIbVccsWnLOBspICT8VoRNB%2Fh9xpafdfCRYN%2FfrtzjFbUtytCleA4eMOUXgkM%2B2XZraIbvwNoL2oYQM3vfJ8kPt2%2BzqCM8e0QXZzhOkPR%2BUNGuMh%2BjIMaiqvJ6wERuR90yBOSz7yZMOWv38JhiyvMZUI1a81AmBL3M2A9Bjs4EBhaqWCM6juCrdI81ayQ2yBOzfFBNP5S30YIs4rC9RnNB60V2w244uf3EgChzSnnSg7GUIkwMkN2BqZ1d8jPzMSt8rrOP22%2BSEASzZdci8sCDYWrp4jSr37HObsAuZfvWATKIjGL2xY5Q3NPdjSsNhgld15AU9h1d4UZmON7GLp90cS186M2ZYkxErJuBfwx8OrT8JsMP9RWUojvAEyhgdATW3tMPa6S%2FtJ9Hh0fyWyLAspH3zHmt4FBNgcWJqZVYlE%2BTXXyZx%2BKt93CQC5zHkTlp1Xo4c0NpS5LeieLCQH3qhi1giDRLRhD4op0VEx3cOpv7DyzmZF8h2%2F83QUaKHysSnPWT7%2BOmnb93gwsipI16qs8kEtZiaOIMOzdi70GOqUBeNYGusPH5hdH0Ks6BV2MeGul5FGg%2B4Fe0lil3PqoREy7AHZT6yp0QdhIpyd4SrO3OGpyn3VMjno8hNKNhltRRbcsgvPzrYsFQuVA6x9ulo7Su1%2BauATda66l4Chwcui1qhwBMNKNoFHWKI3HaPdjsYxQUSLq39DQvOFaQkXu7BjcYcHJMq2tr0r7dp2Ftc9RkpUxbAMPezV%2BeNZjTnj%2FlLH3NjL6&X-Amz-Signature=3640f989d16df49736b0f119c25ad59d45578d4b251480e5e5792f8c22fe35ae&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cbfaed9e-b398-4902-8936-dea058b21def/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663UNLLDWK%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T051459Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECUaCXVzLXdlc3QtMiJHMEUCIQC1i%2FQeiSAEYRL%2FZC3SZt2%2FuWFuAz9n1RBOinMKGYCQmQIgAmAVtVDDd4TJG3YSqMHIKZHyINQ2YtaUNJoxafoO%2FNEq%2FwMIPhAAGgw2Mzc0MjMxODM4MDUiDOcd24ME7z0Ekqa8pCrcA6lyXsu9dYXTwLDvB7%2B6mtP4%2FaWwSIA2x6TSM9%2FogaGh5qzBoqoCi9%2BKF8M4aljkPUPBxof6kcKrMxzsg4eY%2BgdIfsqDIbVccsWnLOBspICT8VoRNB%2Fh9xpafdfCRYN%2FfrtzjFbUtytCleA4eMOUXgkM%2B2XZraIbvwNoL2oYQM3vfJ8kPt2%2BzqCM8e0QXZzhOkPR%2BUNGuMh%2BjIMaiqvJ6wERuR90yBOSz7yZMOWv38JhiyvMZUI1a81AmBL3M2A9Bjs4EBhaqWCM6juCrdI81ayQ2yBOzfFBNP5S30YIs4rC9RnNB60V2w244uf3EgChzSnnSg7GUIkwMkN2BqZ1d8jPzMSt8rrOP22%2BSEASzZdci8sCDYWrp4jSr37HObsAuZfvWATKIjGL2xY5Q3NPdjSsNhgld15AU9h1d4UZmON7GLp90cS186M2ZYkxErJuBfwx8OrT8JsMP9RWUojvAEyhgdATW3tMPa6S%2FtJ9Hh0fyWyLAspH3zHmt4FBNgcWJqZVYlE%2BTXXyZx%2BKt93CQC5zHkTlp1Xo4c0NpS5LeieLCQH3qhi1giDRLRhD4op0VEx3cOpv7DyzmZF8h2%2F83QUaKHysSnPWT7%2BOmnb93gwsipI16qs8kEtZiaOIMOzdi70GOqUBeNYGusPH5hdH0Ks6BV2MeGul5FGg%2B4Fe0lil3PqoREy7AHZT6yp0QdhIpyd4SrO3OGpyn3VMjno8hNKNhltRRbcsgvPzrYsFQuVA6x9ulo7Su1%2BauATda66l4Chwcui1qhwBMNKNoFHWKI3HaPdjsYxQUSLq39DQvOFaQkXu7BjcYcHJMq2tr0r7dp2Ftc9RkpUxbAMPezV%2BeNZjTnj%2FlLH3NjL6&X-Amz-Signature=7e589d4eb36e05532a7e06e2fe25b2cd7eb317a9af1310861de15e595559ab53&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/91181646-b1e0-4433-9711-6259a96a9247/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663UNLLDWK%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T051459Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECUaCXVzLXdlc3QtMiJHMEUCIQC1i%2FQeiSAEYRL%2FZC3SZt2%2FuWFuAz9n1RBOinMKGYCQmQIgAmAVtVDDd4TJG3YSqMHIKZHyINQ2YtaUNJoxafoO%2FNEq%2FwMIPhAAGgw2Mzc0MjMxODM4MDUiDOcd24ME7z0Ekqa8pCrcA6lyXsu9dYXTwLDvB7%2B6mtP4%2FaWwSIA2x6TSM9%2FogaGh5qzBoqoCi9%2BKF8M4aljkPUPBxof6kcKrMxzsg4eY%2BgdIfsqDIbVccsWnLOBspICT8VoRNB%2Fh9xpafdfCRYN%2FfrtzjFbUtytCleA4eMOUXgkM%2B2XZraIbvwNoL2oYQM3vfJ8kPt2%2BzqCM8e0QXZzhOkPR%2BUNGuMh%2BjIMaiqvJ6wERuR90yBOSz7yZMOWv38JhiyvMZUI1a81AmBL3M2A9Bjs4EBhaqWCM6juCrdI81ayQ2yBOzfFBNP5S30YIs4rC9RnNB60V2w244uf3EgChzSnnSg7GUIkwMkN2BqZ1d8jPzMSt8rrOP22%2BSEASzZdci8sCDYWrp4jSr37HObsAuZfvWATKIjGL2xY5Q3NPdjSsNhgld15AU9h1d4UZmON7GLp90cS186M2ZYkxErJuBfwx8OrT8JsMP9RWUojvAEyhgdATW3tMPa6S%2FtJ9Hh0fyWyLAspH3zHmt4FBNgcWJqZVYlE%2BTXXyZx%2BKt93CQC5zHkTlp1Xo4c0NpS5LeieLCQH3qhi1giDRLRhD4op0VEx3cOpv7DyzmZF8h2%2F83QUaKHysSnPWT7%2BOmnb93gwsipI16qs8kEtZiaOIMOzdi70GOqUBeNYGusPH5hdH0Ks6BV2MeGul5FGg%2B4Fe0lil3PqoREy7AHZT6yp0QdhIpyd4SrO3OGpyn3VMjno8hNKNhltRRbcsgvPzrYsFQuVA6x9ulo7Su1%2BauATda66l4Chwcui1qhwBMNKNoFHWKI3HaPdjsYxQUSLq39DQvOFaQkXu7BjcYcHJMq2tr0r7dp2Ftc9RkpUxbAMPezV%2BeNZjTnj%2FlLH3NjL6&X-Amz-Signature=b9baf36551495ea7ac50a1c12b0eabdfe53ba9b5a44d257f65ef9eb546d14d86&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/09aba1c0-0d55-41dd-852a-a04c5b8a3fac/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665TYXJGYP%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T051459Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECUaCXVzLXdlc3QtMiJGMEQCIEpGZJ2xyBaW%2BPjYk%2BZZ0RteS1xsUkZdA99hPWzMCvDSAiAy%2FAjmWX78NXZqoTNysyodPsrWcSW9BMrFzn%2B0Zi%2BEyir%2FAwg%2BEAAaDDYzNzQyMzE4MzgwNSIMiQPTwgMkDv%2FwSjMsKtwDTs9uzxbKvB97BYseXxGIPCKnYLcAXyPbIBPNRA%2Bg8p0AKKw0bPUgZUjWvs7vuE5fLuLPW6hHp3UQbGKcrmXraDKo1QdsMZ19iPxtKAiWYqJXZm23IoN8AMGp2Cx9YzUjNAQaNXyex0TszfCxqW0LSsr0E%2FW0Ksqv33BGZ%2FG94DHHh9u3juHA%2FYUsy%2B%2FIWd1HANPsYGOqGwZ4cfh1SF9k7tf82Uv7eadWJREQcX5qnyxGzVMN7W679nm6XFhLAPl7C7EjiL4Rdwk49H7kYqD%2BRuutB7gaYJ0m9MMJSfm4d0kZ7Y5pRMppEobQACX0azeq6U5ALBeoETZ5Gx9%2FLRJb8x8a%2BGIKqYX%2BRBvDSDrcao%2F9dKH6KVHwHbcdCc5Jz5at3GekOXvtrim6nqSnleE5rzOa2LwXG3XpcmYb3C2GR60a5p15uGi3CcRBN6aHjCiyyWt757sH7WB%2BncaRE4GbST5z14L%2BV1C9mxg2yw3bh5XaZAWqQ9xapUWJpEL89rMisnxbPPlc0Rb0bU%2B%2BxP3xdaNydQEKwSksss5XHtfpk9fmbX%2B%2Bt6uXqSBEWZO9d%2BmSl2MOOEyA1trQH7D6b9kcEwEPo85a733griPkGzKtVr%2B338iiyaLiMPx23WEwqN%2BLvQY6pgEtPCftQsnaYe7kp2N5RB16%2FCJCxqAyVCsqQwew7qc345WgeEsas%2BAywU%2BPogBgPktXP5C6tzHyaWnWAhbxXjDijMEjGzeTk9PHuP5E%2FksUBnK7weNuvh%2BbWKsaWFmYGaXlRyYTB7VkV%2F3iFgLK6FSRYQyLtShlYntbbrKvM61t7hhrDLzygV7VzAfgLvXfbd%2FVV1yf6Pfl5QMeE3t1ZDSEnGGXNMN0&X-Amz-Signature=aa4356df9e2a72a34b7c25898e77a9c06f71536ba3ff8f0384ebf8e7a5c640f0&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 2. Scatter Plot
Scatter plots present the relationship between two variables in a dataset. It represents data points on a two-dimensional plane. The independent variable or attribute is plotted on the X-axis, while the dependent variable is plotted on the Y-axis.
**Syntax:**
```python
plt.scatter(x, y)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23708af9-659f-4f23-b626-1a4292d7842c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665TYXJGYP%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T051459Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECUaCXVzLXdlc3QtMiJGMEQCIEpGZJ2xyBaW%2BPjYk%2BZZ0RteS1xsUkZdA99hPWzMCvDSAiAy%2FAjmWX78NXZqoTNysyodPsrWcSW9BMrFzn%2B0Zi%2BEyir%2FAwg%2BEAAaDDYzNzQyMzE4MzgwNSIMiQPTwgMkDv%2FwSjMsKtwDTs9uzxbKvB97BYseXxGIPCKnYLcAXyPbIBPNRA%2Bg8p0AKKw0bPUgZUjWvs7vuE5fLuLPW6hHp3UQbGKcrmXraDKo1QdsMZ19iPxtKAiWYqJXZm23IoN8AMGp2Cx9YzUjNAQaNXyex0TszfCxqW0LSsr0E%2FW0Ksqv33BGZ%2FG94DHHh9u3juHA%2FYUsy%2B%2FIWd1HANPsYGOqGwZ4cfh1SF9k7tf82Uv7eadWJREQcX5qnyxGzVMN7W679nm6XFhLAPl7C7EjiL4Rdwk49H7kYqD%2BRuutB7gaYJ0m9MMJSfm4d0kZ7Y5pRMppEobQACX0azeq6U5ALBeoETZ5Gx9%2FLRJb8x8a%2BGIKqYX%2BRBvDSDrcao%2F9dKH6KVHwHbcdCc5Jz5at3GekOXvtrim6nqSnleE5rzOa2LwXG3XpcmYb3C2GR60a5p15uGi3CcRBN6aHjCiyyWt757sH7WB%2BncaRE4GbST5z14L%2BV1C9mxg2yw3bh5XaZAWqQ9xapUWJpEL89rMisnxbPPlc0Rb0bU%2B%2BxP3xdaNydQEKwSksss5XHtfpk9fmbX%2B%2Bt6uXqSBEWZO9d%2BmSl2MOOEyA1trQH7D6b9kcEwEPo85a733griPkGzKtVr%2B338iiyaLiMPx23WEwqN%2BLvQY6pgEtPCftQsnaYe7kp2N5RB16%2FCJCxqAyVCsqQwew7qc345WgeEsas%2BAywU%2BPogBgPktXP5C6tzHyaWnWAhbxXjDijMEjGzeTk9PHuP5E%2FksUBnK7weNuvh%2BbWKsaWFmYGaXlRyYTB7VkV%2F3iFgLK6FSRYQyLtShlYntbbrKvM61t7hhrDLzygV7VzAfgLvXfbd%2FVV1yf6Pfl5QMeE3t1ZDSEnGGXNMN0&X-Amz-Signature=69f41d567a2eca34ab5a16e8c9d607db808551d87d4d355fab1f0eb6b3160c49&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 3. Histogram
A histogram is an important visual representation of data in categorical form. To view the data in a "Binned" form, use the histogram plot with a number of bins required or with the data points that mark the bin edges. The x-axis represents the data bins, and the y-axis represents the number of elements in each bin.
**Syntax:**
```python
plt.hist(x, bins)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/24e4424a-df87-40a1-b63b-195cbdc2e0ab/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665TYXJGYP%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T051459Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECUaCXVzLXdlc3QtMiJGMEQCIEpGZJ2xyBaW%2BPjYk%2BZZ0RteS1xsUkZdA99hPWzMCvDSAiAy%2FAjmWX78NXZqoTNysyodPsrWcSW9BMrFzn%2B0Zi%2BEyir%2FAwg%2BEAAaDDYzNzQyMzE4MzgwNSIMiQPTwgMkDv%2FwSjMsKtwDTs9uzxbKvB97BYseXxGIPCKnYLcAXyPbIBPNRA%2Bg8p0AKKw0bPUgZUjWvs7vuE5fLuLPW6hHp3UQbGKcrmXraDKo1QdsMZ19iPxtKAiWYqJXZm23IoN8AMGp2Cx9YzUjNAQaNXyex0TszfCxqW0LSsr0E%2FW0Ksqv33BGZ%2FG94DHHh9u3juHA%2FYUsy%2B%2FIWd1HANPsYGOqGwZ4cfh1SF9k7tf82Uv7eadWJREQcX5qnyxGzVMN7W679nm6XFhLAPl7C7EjiL4Rdwk49H7kYqD%2BRuutB7gaYJ0m9MMJSfm4d0kZ7Y5pRMppEobQACX0azeq6U5ALBeoETZ5Gx9%2FLRJb8x8a%2BGIKqYX%2BRBvDSDrcao%2F9dKH6KVHwHbcdCc5Jz5at3GekOXvtrim6nqSnleE5rzOa2LwXG3XpcmYb3C2GR60a5p15uGi3CcRBN6aHjCiyyWt757sH7WB%2BncaRE4GbST5z14L%2BV1C9mxg2yw3bh5XaZAWqQ9xapUWJpEL89rMisnxbPPlc0Rb0bU%2B%2BxP3xdaNydQEKwSksss5XHtfpk9fmbX%2B%2Bt6uXqSBEWZO9d%2BmSl2MOOEyA1trQH7D6b9kcEwEPo85a733griPkGzKtVr%2B338iiyaLiMPx23WEwqN%2BLvQY6pgEtPCftQsnaYe7kp2N5RB16%2FCJCxqAyVCsqQwew7qc345WgeEsas%2BAywU%2BPogBgPktXP5C6tzHyaWnWAhbxXjDijMEjGzeTk9PHuP5E%2FksUBnK7weNuvh%2BbWKsaWFmYGaXlRyYTB7VkV%2F3iFgLK6FSRYQyLtShlYntbbrKvM61t7hhrDLzygV7VzAfgLvXfbd%2FVV1yf6Pfl5QMeE3t1ZDSEnGGXNMN0&X-Amz-Signature=c2856190620bc92aa4500fe5be65918b45e8451258602efc5405cb66fa971ffe&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ab5a6dfe-51f5-43ee-bcb3-33dae4a1c7ad/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665TYXJGYP%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T051459Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECUaCXVzLXdlc3QtMiJGMEQCIEpGZJ2xyBaW%2BPjYk%2BZZ0RteS1xsUkZdA99hPWzMCvDSAiAy%2FAjmWX78NXZqoTNysyodPsrWcSW9BMrFzn%2B0Zi%2BEyir%2FAwg%2BEAAaDDYzNzQyMzE4MzgwNSIMiQPTwgMkDv%2FwSjMsKtwDTs9uzxbKvB97BYseXxGIPCKnYLcAXyPbIBPNRA%2Bg8p0AKKw0bPUgZUjWvs7vuE5fLuLPW6hHp3UQbGKcrmXraDKo1QdsMZ19iPxtKAiWYqJXZm23IoN8AMGp2Cx9YzUjNAQaNXyex0TszfCxqW0LSsr0E%2FW0Ksqv33BGZ%2FG94DHHh9u3juHA%2FYUsy%2B%2FIWd1HANPsYGOqGwZ4cfh1SF9k7tf82Uv7eadWJREQcX5qnyxGzVMN7W679nm6XFhLAPl7C7EjiL4Rdwk49H7kYqD%2BRuutB7gaYJ0m9MMJSfm4d0kZ7Y5pRMppEobQACX0azeq6U5ALBeoETZ5Gx9%2FLRJb8x8a%2BGIKqYX%2BRBvDSDrcao%2F9dKH6KVHwHbcdCc5Jz5at3GekOXvtrim6nqSnleE5rzOa2LwXG3XpcmYb3C2GR60a5p15uGi3CcRBN6aHjCiyyWt757sH7WB%2BncaRE4GbST5z14L%2BV1C9mxg2yw3bh5XaZAWqQ9xapUWJpEL89rMisnxbPPlc0Rb0bU%2B%2BxP3xdaNydQEKwSksss5XHtfpk9fmbX%2B%2Bt6uXqSBEWZO9d%2BmSl2MOOEyA1trQH7D6b9kcEwEPo85a733griPkGzKtVr%2B338iiyaLiMPx23WEwqN%2BLvQY6pgEtPCftQsnaYe7kp2N5RB16%2FCJCxqAyVCsqQwew7qc345WgeEsas%2BAywU%2BPogBgPktXP5C6tzHyaWnWAhbxXjDijMEjGzeTk9PHuP5E%2FksUBnK7weNuvh%2BbWKsaWFmYGaXlRyYTB7VkV%2F3iFgLK6FSRYQyLtShlYntbbrKvM61t7hhrDLzygV7VzAfgLvXfbd%2FVV1yf6Pfl5QMeE3t1ZDSEnGGXNMN0&X-Amz-Signature=5dd9bf8d15fa24a96f7a0bd3645c3de7cf2d73d5c96a0cd0a469134584b647fd&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8f1b1d60-cf1b-42b3-9faa-f634c89c3f84/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665TYXJGYP%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T051459Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECUaCXVzLXdlc3QtMiJGMEQCIEpGZJ2xyBaW%2BPjYk%2BZZ0RteS1xsUkZdA99hPWzMCvDSAiAy%2FAjmWX78NXZqoTNysyodPsrWcSW9BMrFzn%2B0Zi%2BEyir%2FAwg%2BEAAaDDYzNzQyMzE4MzgwNSIMiQPTwgMkDv%2FwSjMsKtwDTs9uzxbKvB97BYseXxGIPCKnYLcAXyPbIBPNRA%2Bg8p0AKKw0bPUgZUjWvs7vuE5fLuLPW6hHp3UQbGKcrmXraDKo1QdsMZ19iPxtKAiWYqJXZm23IoN8AMGp2Cx9YzUjNAQaNXyex0TszfCxqW0LSsr0E%2FW0Ksqv33BGZ%2FG94DHHh9u3juHA%2FYUsy%2B%2FIWd1HANPsYGOqGwZ4cfh1SF9k7tf82Uv7eadWJREQcX5qnyxGzVMN7W679nm6XFhLAPl7C7EjiL4Rdwk49H7kYqD%2BRuutB7gaYJ0m9MMJSfm4d0kZ7Y5pRMppEobQACX0azeq6U5ALBeoETZ5Gx9%2FLRJb8x8a%2BGIKqYX%2BRBvDSDrcao%2F9dKH6KVHwHbcdCc5Jz5at3GekOXvtrim6nqSnleE5rzOa2LwXG3XpcmYb3C2GR60a5p15uGi3CcRBN6aHjCiyyWt757sH7WB%2BncaRE4GbST5z14L%2BV1C9mxg2yw3bh5XaZAWqQ9xapUWJpEL89rMisnxbPPlc0Rb0bU%2B%2BxP3xdaNydQEKwSksss5XHtfpk9fmbX%2B%2Bt6uXqSBEWZO9d%2BmSl2MOOEyA1trQH7D6b9kcEwEPo85a733griPkGzKtVr%2B338iiyaLiMPx23WEwqN%2BLvQY6pgEtPCftQsnaYe7kp2N5RB16%2FCJCxqAyVCsqQwew7qc345WgeEsas%2BAywU%2BPogBgPktXP5C6tzHyaWnWAhbxXjDijMEjGzeTk9PHuP5E%2FksUBnK7weNuvh%2BbWKsaWFmYGaXlRyYTB7VkV%2F3iFgLK6FSRYQyLtShlYntbbrKvM61t7hhrDLzygV7VzAfgLvXfbd%2FVV1yf6Pfl5QMeE3t1ZDSEnGGXNMN0&X-Amz-Signature=1b4300515b17192b6f1bd196ae06111286c45cccc06b988a34348384eff017d6&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/13ad0497-05fe-4eaa-984e-707b33e14761/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665TYXJGYP%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T051459Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECUaCXVzLXdlc3QtMiJGMEQCIEpGZJ2xyBaW%2BPjYk%2BZZ0RteS1xsUkZdA99hPWzMCvDSAiAy%2FAjmWX78NXZqoTNysyodPsrWcSW9BMrFzn%2B0Zi%2BEyir%2FAwg%2BEAAaDDYzNzQyMzE4MzgwNSIMiQPTwgMkDv%2FwSjMsKtwDTs9uzxbKvB97BYseXxGIPCKnYLcAXyPbIBPNRA%2Bg8p0AKKw0bPUgZUjWvs7vuE5fLuLPW6hHp3UQbGKcrmXraDKo1QdsMZ19iPxtKAiWYqJXZm23IoN8AMGp2Cx9YzUjNAQaNXyex0TszfCxqW0LSsr0E%2FW0Ksqv33BGZ%2FG94DHHh9u3juHA%2FYUsy%2B%2FIWd1HANPsYGOqGwZ4cfh1SF9k7tf82Uv7eadWJREQcX5qnyxGzVMN7W679nm6XFhLAPl7C7EjiL4Rdwk49H7kYqD%2BRuutB7gaYJ0m9MMJSfm4d0kZ7Y5pRMppEobQACX0azeq6U5ALBeoETZ5Gx9%2FLRJb8x8a%2BGIKqYX%2BRBvDSDrcao%2F9dKH6KVHwHbcdCc5Jz5at3GekOXvtrim6nqSnleE5rzOa2LwXG3XpcmYb3C2GR60a5p15uGi3CcRBN6aHjCiyyWt757sH7WB%2BncaRE4GbST5z14L%2BV1C9mxg2yw3bh5XaZAWqQ9xapUWJpEL89rMisnxbPPlc0Rb0bU%2B%2BxP3xdaNydQEKwSksss5XHtfpk9fmbX%2B%2Bt6uXqSBEWZO9d%2BmSl2MOOEyA1trQH7D6b9kcEwEPo85a733griPkGzKtVr%2B338iiyaLiMPx23WEwqN%2BLvQY6pgEtPCftQsnaYe7kp2N5RB16%2FCJCxqAyVCsqQwew7qc345WgeEsas%2BAywU%2BPogBgPktXP5C6tzHyaWnWAhbxXjDijMEjGzeTk9PHuP5E%2FksUBnK7weNuvh%2BbWKsaWFmYGaXlRyYTB7VkV%2F3iFgLK6FSRYQyLtShlYntbbrKvM61t7hhrDLzygV7VzAfgLvXfbd%2FVV1yf6Pfl5QMeE3t1ZDSEnGGXNMN0&X-Amz-Signature=5e05710dfedab0c42197886e4eaa90994b809a88c9ce55e907843a6a45f31268&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 2. Box and Whisker Plot
A box plot shows the distribution of quantitative data in a way that facilitates comparisons between variables or across levels of a categorical variable. The box shows the quartiles of the dataset while the whiskers extend to show the rest of the distribution, except for points that are determined to be "outliers".
**Syntax:**
```python
sns.boxplot(x='header_1', y='header_2', data=df)
```
**Example Output:**


![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d207ae92-0a7c-4e2f-aa65-0ee5a2c33bf7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SUGJSN5X%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T051500Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECUaCXVzLXdlc3QtMiJHMEUCIQDtsxy0HpwC7y66TUPXbOnIPD4O6jHRUw%2BOvcSkhFHsKQIgLdQ0Yz0XpopsxJCixHGkehSZRhHFQd1H8%2FbPP3C%2BTJ0q%2FwMIPhAAGgw2Mzc0MjMxODM4MDUiDKlaBa7OdzK%2BvNs4pyrcA%2FOFxrQuGc9mCIrTpuYtE4JeUeWwvRkZx318EzfsV81U2U2Z1HXgJqjvwozZRHOhY6yRyZhPy0XW2W0qMhSW2Zfa13aRCgY2XlwGcdVgxROTsnZYWtZlIk%2BpyNSBU8SJDPf7m2EKteBaGOlzkvTaWpbHHuOtsZqvLMzYFDlOhsu0HS3BQvHOt2hLhMTPSTUDDHwYpRZFYM6mDcjLLoMqF9t%2BmtstWgyU43sKgfMNzPq%2BiNF2H1VnNhMPedc26FUphxfKBmvb5k4I5azJzNR%2BkPbbYqRBewX7fu4kDpPfROmbddAsaQAJPC21RLhkSp%2F964spLvX6KvmnMb0PNxD5%2Beh0dLF%2Btxdkp9%2F25bq8z0R3YLsnbblfchkfgTv6oIbqFI4CgrjecBdgfQ4soq0XevEEPBd5Jh%2Bp69lAmER16NsUpHfcZhiXDoFmfbn2dD0SpMaxPhmmv%2BlYSeBiSUCFupRcgQrTVQSY1PH0tmt1cznqcXrfqtWwJmeCbi0ARD%2FaVOz%2FK96nJdv1SzjfHolOlu6Ev15VUHi9rqaMg2OHxn2mdQJyjI1SttmyK8XIScYkvboJ2mQgxF%2BduDSj79zKz2fl4Vw6IePrFFmiFgPFEOIvmD8FOAE%2BeqgoUTUvMJDei70GOqUB8WSH9L%2BEZock8lEkJkfzlQGaTzaAX6N1m25xGGqCewwh%2BQzmjRLxKOL6tKLaoK%2F2Pq4R1m8i0oPUYVJxBTtlVjJ1270luzjdYGzko6l9d4qa4fzZ5VY1e5Rh6RgZpofzb%2FOiKOp498sVfVvDcD8iQ0UJuGwMFrNVBjbkf%2FR8%2BAiekcUg42Uvay0%2Bueyqu1qVUAb28ziKJo78%2BqQhFpwxpi0EfZGh&X-Amz-Signature=9cf453a660927604bd84e30e78762d5887a09c7fb39a3ef8b88febe43609524a&X-Amz-SignedHeaders=host&x-id=GetObject)

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0e516edc-7551-4792-ab18-0494db3c4c0c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VHPASTPV%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T051501Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECUaCXVzLXdlc3QtMiJHMEUCIBb7PWMUK6qQkwC7xxhj2%2BpOShfzNUTKSr5AC76J3fauAiEAoHLdeFtx2mKLj6o4ZDWakjkaLazed5vC%2BZOfLHazMKAq%2FwMIPhAAGgw2Mzc0MjMxODM4MDUiDEloBZ9mcTxr60hrbCrcA4tiCpYin75Sax%2F6IeOwx8nmh0drmm9nVWZxK%2F6RVj3vOjyopAhe5fp%2BH6DMJiJognLnBhzbLUs%2BUT8e8bUVfyE9MJj19OEdlWD9%2Fa8bdsI36D44M%2FDqxiGiMzTJumNmY8g4utLA09ffqGq%2BkesEvBUp4Hj453E%2FCBFHznVyIZjPf62g0yx58tLuqzgzbjbYhm%2BPLgz71QsrfDgD6OI9YESRQi4g6p2nOsL3qnRWEkAg8pOakse0p%2BeeXTJXhqcu4KoKA4d8gdxVyhV9Tcp33fwNaCfqDR6bavfGX9Csf2vrOG4oJm610x8qWg8w%2BzdIG7xHr6dnyi%2BmV7HejwU%2Bb%2BQ8z7zPd9XgTGOl1XiWMylMOMVSuB780g4rOkIyw16XOd2jtAHjrbCX%2FX%2BQy6crY7wxK%2BxvmxvEFhAwaP1A8uwmwD7z3s0RkMFaZtnhGyCcOlgjVxYCdc3R39aZi6q1zwdvXyz1NjvoHd3H6lx5%2FdkB0FB0rSmQzxbZdcgancEqf0FWug2YnJq%2F%2FhxtfSl53eAUfkFHZa2G0pfDSFIQB6frn63P1GDXLB9INFAkksUn%2FXTUGpMxaPQCBoaXVek6U6%2FGlYMIJUn%2FEtr7LGlYK%2BUWZN%2BsjTkOnzPDF4UOMOPdi70GOqUBMJ8iYPhZfBdPH7cqq6MsMOK9gKPdBrR8Y2LID7mpkEgdzfZVSZ30yCJub0ALN7P9U%2BzPeZePxruy9%2FlkR7gkP%2FK62g39RIY6x9S2VE65wt8jKT8LJ%2FMt9itncdgdP0eIpmc6T84qnXCuK8y87aqQOBg55pzZUehjXfURzjGzG9zpPM5HWJ44xCiB5F0RBLYvASclMXApfo72dqNJ9EU0iOLWgg5x&X-Amz-Signature=48dbef0e770bd65de011c85b9bf0d2af8d49184e772d9d800809fff1e23963c3&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23a79b9d-2356-49a9-8fd9-65c6b0ab2cc5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665TYXJGYP%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T051459Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECUaCXVzLXdlc3QtMiJGMEQCIEpGZJ2xyBaW%2BPjYk%2BZZ0RteS1xsUkZdA99hPWzMCvDSAiAy%2FAjmWX78NXZqoTNysyodPsrWcSW9BMrFzn%2B0Zi%2BEyir%2FAwg%2BEAAaDDYzNzQyMzE4MzgwNSIMiQPTwgMkDv%2FwSjMsKtwDTs9uzxbKvB97BYseXxGIPCKnYLcAXyPbIBPNRA%2Bg8p0AKKw0bPUgZUjWvs7vuE5fLuLPW6hHp3UQbGKcrmXraDKo1QdsMZ19iPxtKAiWYqJXZm23IoN8AMGp2Cx9YzUjNAQaNXyex0TszfCxqW0LSsr0E%2FW0Ksqv33BGZ%2FG94DHHh9u3juHA%2FYUsy%2B%2FIWd1HANPsYGOqGwZ4cfh1SF9k7tf82Uv7eadWJREQcX5qnyxGzVMN7W679nm6XFhLAPl7C7EjiL4Rdwk49H7kYqD%2BRuutB7gaYJ0m9MMJSfm4d0kZ7Y5pRMppEobQACX0azeq6U5ALBeoETZ5Gx9%2FLRJb8x8a%2BGIKqYX%2BRBvDSDrcao%2F9dKH6KVHwHbcdCc5Jz5at3GekOXvtrim6nqSnleE5rzOa2LwXG3XpcmYb3C2GR60a5p15uGi3CcRBN6aHjCiyyWt757sH7WB%2BncaRE4GbST5z14L%2BV1C9mxg2yw3bh5XaZAWqQ9xapUWJpEL89rMisnxbPPlc0Rb0bU%2B%2BxP3xdaNydQEKwSksss5XHtfpk9fmbX%2B%2Bt6uXqSBEWZO9d%2BmSl2MOOEyA1trQH7D6b9kcEwEPo85a733griPkGzKtVr%2B338iiyaLiMPx23WEwqN%2BLvQY6pgEtPCftQsnaYe7kp2N5RB16%2FCJCxqAyVCsqQwew7qc345WgeEsas%2BAywU%2BPogBgPktXP5C6tzHyaWnWAhbxXjDijMEjGzeTk9PHuP5E%2FksUBnK7weNuvh%2BbWKsaWFmYGaXlRyYTB7VkV%2F3iFgLK6FSRYQyLtShlYntbbrKvM61t7hhrDLzygV7VzAfgLvXfbd%2FVV1yf6Pfl5QMeE3t1ZDSEnGGXNMN0&X-Amz-Signature=7d0282fdad6305f06bf55f615a51ed1093fd0247bcba150b11f26839c4f57a59&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 4. KDE Plot
A Kernel Density Estimate (KDE) plot is a graph that creates a probability distribution curve for the data based upon its likelihood of occurrence on a specific value. This is created for a single vector of information.
**Syntax:**
```python
sns.kdeplot(X) || sns.kdeplot(df['age'])
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0d571213-2a2f-4921-a50b-880847aa05ee/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665TYXJGYP%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T051459Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECUaCXVzLXdlc3QtMiJGMEQCIEpGZJ2xyBaW%2BPjYk%2BZZ0RteS1xsUkZdA99hPWzMCvDSAiAy%2FAjmWX78NXZqoTNysyodPsrWcSW9BMrFzn%2B0Zi%2BEyir%2FAwg%2BEAAaDDYzNzQyMzE4MzgwNSIMiQPTwgMkDv%2FwSjMsKtwDTs9uzxbKvB97BYseXxGIPCKnYLcAXyPbIBPNRA%2Bg8p0AKKw0bPUgZUjWvs7vuE5fLuLPW6hHp3UQbGKcrmXraDKo1QdsMZ19iPxtKAiWYqJXZm23IoN8AMGp2Cx9YzUjNAQaNXyex0TszfCxqW0LSsr0E%2FW0Ksqv33BGZ%2FG94DHHh9u3juHA%2FYUsy%2B%2FIWd1HANPsYGOqGwZ4cfh1SF9k7tf82Uv7eadWJREQcX5qnyxGzVMN7W679nm6XFhLAPl7C7EjiL4Rdwk49H7kYqD%2BRuutB7gaYJ0m9MMJSfm4d0kZ7Y5pRMppEobQACX0azeq6U5ALBeoETZ5Gx9%2FLRJb8x8a%2BGIKqYX%2BRBvDSDrcao%2F9dKH6KVHwHbcdCc5Jz5at3GekOXvtrim6nqSnleE5rzOa2LwXG3XpcmYb3C2GR60a5p15uGi3CcRBN6aHjCiyyWt757sH7WB%2BncaRE4GbST5z14L%2BV1C9mxg2yw3bh5XaZAWqQ9xapUWJpEL89rMisnxbPPlc0Rb0bU%2B%2BxP3xdaNydQEKwSksss5XHtfpk9fmbX%2B%2Bt6uXqSBEWZO9d%2BmSl2MOOEyA1trQH7D6b9kcEwEPo85a733griPkGzKtVr%2B338iiyaLiMPx23WEwqN%2BLvQY6pgEtPCftQsnaYe7kp2N5RB16%2FCJCxqAyVCsqQwew7qc345WgeEsas%2BAywU%2BPogBgPktXP5C6tzHyaWnWAhbxXjDijMEjGzeTk9PHuP5E%2FksUBnK7weNuvh%2BbWKsaWFmYGaXlRyYTB7VkV%2F3iFgLK6FSRYQyLtShlYntbbrKvM61t7hhrDLzygV7VzAfgLvXfbd%2FVV1yf6Pfl5QMeE3t1ZDSEnGGXNMN0&X-Amz-Signature=cbbf214232c9a13c7a25e0ae430e65cf19a9ef62b9cf6e55fae2851bd3cde137&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/53752550-ef82-4ca9-a01a-09921f0282d0/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665TYXJGYP%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T051459Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECUaCXVzLXdlc3QtMiJGMEQCIEpGZJ2xyBaW%2BPjYk%2BZZ0RteS1xsUkZdA99hPWzMCvDSAiAy%2FAjmWX78NXZqoTNysyodPsrWcSW9BMrFzn%2B0Zi%2BEyir%2FAwg%2BEAAaDDYzNzQyMzE4MzgwNSIMiQPTwgMkDv%2FwSjMsKtwDTs9uzxbKvB97BYseXxGIPCKnYLcAXyPbIBPNRA%2Bg8p0AKKw0bPUgZUjWvs7vuE5fLuLPW6hHp3UQbGKcrmXraDKo1QdsMZ19iPxtKAiWYqJXZm23IoN8AMGp2Cx9YzUjNAQaNXyex0TszfCxqW0LSsr0E%2FW0Ksqv33BGZ%2FG94DHHh9u3juHA%2FYUsy%2B%2FIWd1HANPsYGOqGwZ4cfh1SF9k7tf82Uv7eadWJREQcX5qnyxGzVMN7W679nm6XFhLAPl7C7EjiL4Rdwk49H7kYqD%2BRuutB7gaYJ0m9MMJSfm4d0kZ7Y5pRMppEobQACX0azeq6U5ALBeoETZ5Gx9%2FLRJb8x8a%2BGIKqYX%2BRBvDSDrcao%2F9dKH6KVHwHbcdCc5Jz5at3GekOXvtrim6nqSnleE5rzOa2LwXG3XpcmYb3C2GR60a5p15uGi3CcRBN6aHjCiyyWt757sH7WB%2BncaRE4GbST5z14L%2BV1C9mxg2yw3bh5XaZAWqQ9xapUWJpEL89rMisnxbPPlc0Rb0bU%2B%2BxP3xdaNydQEKwSksss5XHtfpk9fmbX%2B%2Bt6uXqSBEWZO9d%2BmSl2MOOEyA1trQH7D6b9kcEwEPo85a733griPkGzKtVr%2B338iiyaLiMPx23WEwqN%2BLvQY6pgEtPCftQsnaYe7kp2N5RB16%2FCJCxqAyVCsqQwew7qc345WgeEsas%2BAywU%2BPogBgPktXP5C6tzHyaWnWAhbxXjDijMEjGzeTk9PHuP5E%2FksUBnK7weNuvh%2BbWKsaWFmYGaXlRyYTB7VkV%2F3iFgLK6FSRYQyLtShlYntbbrKvM61t7hhrDLzygV7VzAfgLvXfbd%2FVV1yf6Pfl5QMeE3t1ZDSEnGGXNMN0&X-Amz-Signature=3f9f7d7c2b7b36f4307f8ca4daf06d4eafc6945775da6976d38f27f308a49a1a&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
## 4. Correlation Between Variables
Correlation is a statistical measure of the extent to which different variables are interdependent. It indicates how changes in one variable are associated with changes in another variable over time.
### Positive Correlation
Positive correlation indicates that as one variable increases, the other variable also tends to increase.
**Example: Engine Size and Price**
- **Positive Correlation:** Engine size increases, price also increases.
- **Visualization:** Scatter plot with a steep positive slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c7ea9b0-3ef3-4357-a9c3-554fc71b6b15/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667HAXHDIF%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T051500Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECUaCXVzLXdlc3QtMiJHMEUCIQDAtg%2FuFjmOzP1JDVBbpk8xQlnyHk5w%2BtZOQBaslMF6tAIgd7ftv31NogE1J71fpFqMnxPjKKmZUmXyxgxl1U9E6wkq%2FwMIPhAAGgw2Mzc0MjMxODM4MDUiDM9%2BEfADq0h67NJcZSrcA2RNtEqtb8eJKlvTt3stfJo4MtgL2VyqLqYX5pm2GYh%2B7UcF4uoQ2d%2B6osHnHpBqXx7Umyf5v3ze%2Fyz1fIocxBRT6RWs3ldvxUlsxY5BGXHHQpT9zE%2BU%2BzGA%2BMT8tY5%2BUaLcg21IA0QNolWWImcCQ%2Bj9mcoLMiJDRap2pIGJrq8239PPegnkYfZv0nIlUEExliEiItqoMu1rom0BcO8xLQLc015XpiMCLgTkT%2BYpM8M5RRcUPOmvodDuJPTO%2FQ2XSgdXQrcHylOLRr5%2BiNYp88DipLo89VLh9KeCZsW5yxg1OYRDumN%2BIdYAP3D0RPcDiUmbkuORM5x2XenHwLukS%2FRkO8M8iys0JfKEp7H78ewvLQUUnm3SzTEmsIKvJo9KF%2Bygnar2QeEWtBYvFADwLo4LZBgh7nNUSSmLP%2F32NPL97Eljit9gFqZz4T%2Felf0NGGdthhyFfHrTn5djz3F80oHN2p3lvirw5%2BuBUfi%2B4tUqJ1vxWHe4tDdHYUB2P8NRNJ4Ywuv4dVMNOnblZDfw%2F6L4JOPcHzWMkeGziimCbuQv09iZnE5oERieiDRuUvIu4OlLFb761hGxR06Msh1oVKy6HGQCDIPf5ipXWY5Q8SFcf9uhdXt%2FpVmTnEh%2FMLbei70GOqUBkRfZw9X8l2fNt3NJWoRn3tE74ugaiT1N%2F9F87KEGNKod%2FeoihaC2LkdUsivwtzZFz0708g7P4ycvrqxaz%2FTK6tNao9g1j%2FqtFJkDQ2SXS%2BR3yLeA9gTULHC5kZkfSIbuM660alwOo45Xp5bxhKewrMfHfnmXSJBhcswNQkpaCZxVWEEDMWBH6SrYEvf3V43cAghfkXmrvrCj9L%2F%2F0Je9JJQ08SFX&X-Amz-Signature=386a00402d6b63fa6fdda09d8a37c3b734af86e22256a30f063dc1d69185d497&X-Amz-SignedHeaders=host&x-id=GetObject)
**Explanation:** When engine size increases, there is a corresponding increase in the price of the vehicle. This positive correlation suggests that larger engines tend to be associated with higher prices in the market.
___
### Negative Correlation
Negative correlation indicates that as one variable increases, the other variable tends to decrease.
**Example: Highway Miles per Gallon and Price**
- **Negative Correlation:** As highway miles per gallon increases, price decreases.
- **Visualization:** Scatter plot with a steep negative slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/10f1f798-9cc4-4df2-a9c1-5a339f554a0b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WXHIN6W5%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T051500Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECUaCXVzLXdlc3QtMiJIMEYCIQCSt%2FJ3moS2w97C%2BQCGPGe236QXq27V2MOmC42T7W8%2FJAIhANsEwfeADq4lCgcp0NWiPigz3Gz%2BOr9cZ4tcrJB6m8hXKv8DCD4QABoMNjM3NDIzMTgzODA1IgzHOcfK%2BrJUH7SShvkq3APvzYXiRidtPibHVbmuBVLjrzZLwYRBMiXx%2FhS3F5c0dpel05YZGDElBMzne%2B71VnucZcHGVtN6YFCuFXDCNe8gvEoUaEi4nmUyHvE%2BBf0JtfNSurnMhX1NycX0djjvWGyFuL7utrKmwzJIWSRBZ%2FHmrJ9j2471aZidUa1jXyNSKp2BeutxvpXeyJPRSuTw6SMxzVy0bmQ1ya8bWKO0zFyRnRTbEHFD9Zycg8TaBXAubftaLJERZJf9VSCKI0CZj%2BVCrpa%2FZFDz4ivl2cL119XfU980Vn8ntU94alODoYlabMABdp4mukgJNzxQfqthCcXnxBsbxf1IDu2UsdH7mpGUR7nv8bCrOgP6BE6ayztt9wxf0ZkRJ%2B2pxILEo%2FlnFnkn0r%2BqRo%2BV2wkRz%2BEKmMTMrjcocyF58rJN1EVLZcjKORCH9I9sRpxjufECiFbg4h3YHWM3NX%2BLTLaUtmLYTHwv92LQJjDyogCa%2FogGemUDUip1JL0XuGMsUP58COw7puHBFALSWoxAC0iFldZYM55lY0N4bbTyEL54JTq4hPehDheCVLkK%2BUsh6H8FgoRDmHMSnfYjaASnG4hpPIXKfw5eSM1bDU6ZlrgKTu16s2cQi8s0q%2BGDS5NYEw4jtzDE3Yu9BjqkAfFuQ%2FR1q0jzjtjkcO%2FmGK7IzpNevdthuJn5yrMAczkfOBT5vuX7%2F79mlER15330AfiWo0oJF30%2FrYKEtZROfJePkrId8W1NBQZtTKFnC1m6QGQM0CnDCGur7q%2BY6iFPzCtl41NQXNb4JRGmEoV7x2Q77zeiysw6tsup0hoAPelcydf0RZBXKsoeYqzurkjuBCT%2B2RZBwIpE3i8G9q0JQX5mV2Em&X-Amz-Signature=b4aae87508af94b72602eb358401b9492bbb512c52581a15e3403117e229ecf3&X-Amz-SignedHeaders=host&x-id=GetObject)
**Explanation:** When highway miles per gallon increases, the price of the vehicle tends to decrease. This negative correlation suggests that cars with higher fuel efficiency (more miles per gallon) are generally priced lower in the market.
___
### Weak Correlation
Weak correlation indicates a lack of strong relationship between the variables.
**Example: RPM and Price**
- **Weak Correlation:** Low and high RPM values show varied prices, indicating no strong predictive relationship.
- **Visualization:** Scatter plot with no clear trend or slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9f914514-8914-4bf4-ac84-d9e3077f6eb1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZMTTG7E2%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T051500Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECUaCXVzLXdlc3QtMiJGMEQCIHma41xhsEtr1cwzXsTx2RqBCdCXgnGPwHli0lGJd8S8AiA%2BcwIDyEJ9DJ7qyZcYZVavW1VWmnLdR2UJ2%2F65%2Bh9jVSr%2FAwg%2BEAAaDDYzNzQyMzE4MzgwNSIMPrVPhBiMDoj8cvwqKtwDPS%2FVCSiNfJkcCshlxnhuEKwhXTDMk2XZIRIRRRTZnCyoPrB5n4fcI3bzndfr%2BZ9KgDEM1Uo5wnk6lIrh2UdC9fZGDg7ZVZRyPaKIlxPeeRWRBzofl%2FQ6FsB16gVjwuH%2F%2FS%2FRIf9%2BsplNC%2FDbjI5YC2iCoIPWouq%2B%2BAIymAkDC8cPXIofpO7iOdcrydgF8PbmnN4fVcenex1dL%2FdFQnYOrtxNTXJbPJTmDIAqvMweJIo%2B8YJGiqFR4qMjb%2Fu7ADwNcwaB6sOUbyWshtYB2H%2BKfJrY3Kjj7X14fWXfa7MHDFZvEVr2e4P95v6CBsllFrBllURiVbcwr%2BU2F%2BqIi8EHWU7qHqDK3OcxD%2B%2Bq%2FokgzTbUGLIPmO9xuJhv7R2aNAI1XScgSHrz935oynFfje7BYolxASetBFvOtEZTcErbPNDhh2%2B%2FtB3gv5zONr0JiPrymBucrEP9KPI%2FDpZhMnEPdD%2FXEJx%2FgOgTIj0qF9HbIK9vm7ywCZnFZp9HVZ%2BlYw%2BA42g1TreRo06O0SB5vH6KOrH0LojdMRaGw%2Bu2XApJg7DL%2FLL0KmRQV9rVv5N20al3fkT9TPEu%2FldDnacvXmS%2BQqRdklYfCyKIukQ6%2BewuWQsINEaY%2BYgOhcJdWTgw6t2LvQY6pgHrYGd0ckZ6lyLQPTOM7Nol91GkA6biJSGL9hiXVxH6NESWJSKiLS%2FgVSiu0wyOjf6cqfJ8YaA4Hb3Ax%2FUwzaj%2BW0Fa1mdvsSaKWlg3y6ELpSQ5hqRiqXFJ8miv%2Fvh5BobfkMHR%2BBCnaK66X5JQiNN7fuw7oUZ4L7W1wxQl1X5Z9NqfA564tVyPvH6ZA35OoEYA65Y0XVurCwF7DTt5Y3zc0fAgbcB%2F&X-Amz-Signature=a48918b069b7e46e5cbbccff9eee8b1209a3dfbd90b3bb831fdaa72fe171afcd&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f18086e5-5b04-4fbf-8309-8944ab20d213/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R3MTMQGZ%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T051500Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECUaCXVzLXdlc3QtMiJHMEUCIF86%2FU4igEycOtqwfdBj9toT3t5cuVERul5Hoyb9cW6zAiEA1BneSf%2BLXZM1Nu4soCbgVJH1cgljVNP9iaHBPmPV0c8q%2FwMIPhAAGgw2Mzc0MjMxODM4MDUiDF9A9JSXzpcACbxXNyrcAwSlWp%2FVML%2FespSmCTnaB6hPm9mbG4%2BSlzivDYvSpqScGl9qTgJ7NzF3UgjY5zH20jQD7sYq5M6kVJr%2BSEV49a7EJrWFCBnVyQBbFFXSs9Y3V%2FrgiPA0FeYdu92eELQVrTB0UiZatqfAPxuVXAps4w45TRhAxevF2ssZDhU1YoEMM9772JJazEgYqa%2BT60Oc%2FIAi3DWVF7GPCh%2FcbON%2FNfb5JYEFKTMCF8ZGb0cxi%2FMr2E7QNH42m26xZctQiPCNuS3b3c5d02iO5OFP%2BV7GFVUidLYbpS6o91p2HVgVFpo88vGpdngXikXCGclblKJQ%2B5%2BHmt4JA%2FojmVXo315XE5DkLLGYJr1vRWv4px3GwmurGpaS%2BDrxSBo%2BJAAls8EnWXyYurNl0Fe1VOPFtMFkoaOB2fpnkrYecQE2X71foCqAoko9Sx35ohD1SAkS6cTvaE%2B7bYP%2Bl%2BHEUjlNAHb3LlYh3qF%2FPo8b8ff0fbs1y6wE1v%2FwCM0c8TbgmjAZCoV3j3JKNpJbImD9vfF3nuswjaDBvTKH8sWjJs40JcMB4D0fD83zjaCjg9H3CR7QbIA6WK5zZ7Q8B2IliRVwY8sur3BUqGTehgafIuoexPKRJbjT4IJt6ziiOtqPrZJwMOTdi70GOqUBReOdjh6oqgWGKJ8sl3LprQsdkaYHpRqKjxsK5N19AJ0AXpNHZ%2BWZJPsueakLNj4WN3Z26qNSmOie4oJ8HzZXwpwJpt6Eoh14z%2FSNR3WdwDu2WwJdZ9%2BC6lex0N5A4XirtpkEQ8UOOHo7GlV%2BIh4H4OKuDcxIN7x%2FXEgmSLERO2nHxzSzhKUeWQCzXZELHChkvBXu%2B2vqN6QX5nFZ95f%2FgJYxgCXP&X-Amz-Signature=c498a9c588364d689c9c1fc5b319952ea82db0d08327c28f439acf6dcf5db840&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Correlation Plot
Heatmap visualizes correlations among variables. Color scheme indicates Pearson correlation coefficients. Dark red diagonal line shows perfect correlation (value of 1) between variables and themselves.
This heatmap offers overview of variable relationships and their link with price.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cd3b341e-cc1a-45f7-8aec-cdc00436d270/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R3MTMQGZ%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T051500Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECUaCXVzLXdlc3QtMiJHMEUCIF86%2FU4igEycOtqwfdBj9toT3t5cuVERul5Hoyb9cW6zAiEA1BneSf%2BLXZM1Nu4soCbgVJH1cgljVNP9iaHBPmPV0c8q%2FwMIPhAAGgw2Mzc0MjMxODM4MDUiDF9A9JSXzpcACbxXNyrcAwSlWp%2FVML%2FespSmCTnaB6hPm9mbG4%2BSlzivDYvSpqScGl9qTgJ7NzF3UgjY5zH20jQD7sYq5M6kVJr%2BSEV49a7EJrWFCBnVyQBbFFXSs9Y3V%2FrgiPA0FeYdu92eELQVrTB0UiZatqfAPxuVXAps4w45TRhAxevF2ssZDhU1YoEMM9772JJazEgYqa%2BT60Oc%2FIAi3DWVF7GPCh%2FcbON%2FNfb5JYEFKTMCF8ZGb0cxi%2FMr2E7QNH42m26xZctQiPCNuS3b3c5d02iO5OFP%2BV7GFVUidLYbpS6o91p2HVgVFpo88vGpdngXikXCGclblKJQ%2B5%2BHmt4JA%2FojmVXo315XE5DkLLGYJr1vRWv4px3GwmurGpaS%2BDrxSBo%2BJAAls8EnWXyYurNl0Fe1VOPFtMFkoaOB2fpnkrYecQE2X71foCqAoko9Sx35ohD1SAkS6cTvaE%2B7bYP%2Bl%2BHEUjlNAHb3LlYh3qF%2FPo8b8ff0fbs1y6wE1v%2FwCM0c8TbgmjAZCoV3j3JKNpJbImD9vfF3nuswjaDBvTKH8sWjJs40JcMB4D0fD83zjaCjg9H3CR7QbIA6WK5zZ7Q8B2IliRVwY8sur3BUqGTehgafIuoexPKRJbjT4IJt6ziiOtqPrZJwMOTdi70GOqUBReOdjh6oqgWGKJ8sl3LprQsdkaYHpRqKjxsK5N19AJ0AXpNHZ%2BWZJPsueakLNj4WN3Z26qNSmOie4oJ8HzZXwpwJpt6Eoh14z%2FSNR3WdwDu2WwJdZ9%2BC6lex0N5A4XirtpkEQ8UOOHo7GlV%2BIh4H4OKuDcxIN7x%2FXEgmSLERO2nHxzSzhKUeWQCzXZELHChkvBXu%2B2vqN6QX5nFZ95f%2FgJYxgCXP&X-Amz-Signature=52f60e290cdd1b9accf22def7b9145d602bb6f89af1b72e45224db6a86b20edc&X-Amz-SignedHeaders=host&x-id=GetObject)

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
