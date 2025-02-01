

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7e6d594d-952e-44b6-97ea-31225882aea6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SO5FFQ7R%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T031859Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQC52BUU31NxPrEL6dwfYUj59aRJrpc5SCqqSyaVC0GbggIgKDXLvHGEvqRMyXGJvGprReUyndViPSKhS2fb%2FROQzuIqiAQIyv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDEKUxLsX7H3q9KJfJircA7jwOKpU9RwjHF6fL0QCfkyv257WzEO4kEq40ljBdZmI9TCjSnubF5XAU6xpLdLYns%2FeHgcv6vqptpReyaaE2D3dfNqp9bGuoWJkU0WaOZ04WlXWFH3kzXn432N2gSq7o%2B0DNm5GX55h06P1mDYcs84p9l584WghBGE3P4BmSPy9gjyzGmqD%2B4Dv9bsohTmQW531EdaxoRHcfnpttOj0PDwSwFG1vc9R7QenkdH3wSXvX6C0GDIRQgzUtesQAVEPByfOjIlvZS4eKFkFhpP93o212bY57CktL0iMNgRGkR4%2BXKDRdCK%2ByvHr0sALe%2BtlfurWwTALM6b6UGsABYozv4GLuATFuAqTQrMa4LQaTRiw2lt4FG5LESGsPhESIt%2BwLB6UGNLcsplZ0qNdn%2FIwwW7zzDpTViSgJHSdgb0asLCFgEKYSz%2B8%2BeWy%2BOud%2BeP5ffinEAcG651%2ByxUd0WkpdOH24hk2sRN2RknjrAMDBKqzGq3lCuC%2FbL%2BezCsmEOVYI7%2BTCncfmkB30sRc%2B1xnfJ4UN8tk%2F7e4fFLpjDjcciqVMKVNI53T9InmRuWiHvTT%2BXWPHpSp7Ii%2Fs0WmjD85HMgxVflZ49ZIfOt4T9%2FCV0XOHQ9q9zUlGzoZ3qSbMK3s9bwGOqUB9NovDeLWSQS7vEe%2FR3%2FhhNSV8gKFMtvvRN%2BawriAIJPriQ90rtq6iO4IJSRKlNGTmdl1CukjzgtWhLaWnQMvBzlDurTw8DGWFL7Yg1r92b4YwSsK3q3jv%2BWcMCFVBb6uiA6SSYNAnXJJ1LWMp1tlTaaCY1qKyARt9DQvaeYbIRbOr2EKaJPa926wJVMyMf9zt7MgvW%2BQXFRiavR5Sff4XiesCoR8&X-Amz-Signature=7f919fd66896600eb4127658396c72afe86374d163e45dbfc28e3967ff02ef2f&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cbfaed9e-b398-4902-8936-dea058b21def/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SO5FFQ7R%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T031859Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQC52BUU31NxPrEL6dwfYUj59aRJrpc5SCqqSyaVC0GbggIgKDXLvHGEvqRMyXGJvGprReUyndViPSKhS2fb%2FROQzuIqiAQIyv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDEKUxLsX7H3q9KJfJircA7jwOKpU9RwjHF6fL0QCfkyv257WzEO4kEq40ljBdZmI9TCjSnubF5XAU6xpLdLYns%2FeHgcv6vqptpReyaaE2D3dfNqp9bGuoWJkU0WaOZ04WlXWFH3kzXn432N2gSq7o%2B0DNm5GX55h06P1mDYcs84p9l584WghBGE3P4BmSPy9gjyzGmqD%2B4Dv9bsohTmQW531EdaxoRHcfnpttOj0PDwSwFG1vc9R7QenkdH3wSXvX6C0GDIRQgzUtesQAVEPByfOjIlvZS4eKFkFhpP93o212bY57CktL0iMNgRGkR4%2BXKDRdCK%2ByvHr0sALe%2BtlfurWwTALM6b6UGsABYozv4GLuATFuAqTQrMa4LQaTRiw2lt4FG5LESGsPhESIt%2BwLB6UGNLcsplZ0qNdn%2FIwwW7zzDpTViSgJHSdgb0asLCFgEKYSz%2B8%2BeWy%2BOud%2BeP5ffinEAcG651%2ByxUd0WkpdOH24hk2sRN2RknjrAMDBKqzGq3lCuC%2FbL%2BezCsmEOVYI7%2BTCncfmkB30sRc%2B1xnfJ4UN8tk%2F7e4fFLpjDjcciqVMKVNI53T9InmRuWiHvTT%2BXWPHpSp7Ii%2Fs0WmjD85HMgxVflZ49ZIfOt4T9%2FCV0XOHQ9q9zUlGzoZ3qSbMK3s9bwGOqUB9NovDeLWSQS7vEe%2FR3%2FhhNSV8gKFMtvvRN%2BawriAIJPriQ90rtq6iO4IJSRKlNGTmdl1CukjzgtWhLaWnQMvBzlDurTw8DGWFL7Yg1r92b4YwSsK3q3jv%2BWcMCFVBb6uiA6SSYNAnXJJ1LWMp1tlTaaCY1qKyARt9DQvaeYbIRbOr2EKaJPa926wJVMyMf9zt7MgvW%2BQXFRiavR5Sff4XiesCoR8&X-Amz-Signature=49954f5c44cbc97216085d229176d454ba315403e3978b9d855443f8cddfc239&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/91181646-b1e0-4433-9711-6259a96a9247/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SO5FFQ7R%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T031859Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQC52BUU31NxPrEL6dwfYUj59aRJrpc5SCqqSyaVC0GbggIgKDXLvHGEvqRMyXGJvGprReUyndViPSKhS2fb%2FROQzuIqiAQIyv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDEKUxLsX7H3q9KJfJircA7jwOKpU9RwjHF6fL0QCfkyv257WzEO4kEq40ljBdZmI9TCjSnubF5XAU6xpLdLYns%2FeHgcv6vqptpReyaaE2D3dfNqp9bGuoWJkU0WaOZ04WlXWFH3kzXn432N2gSq7o%2B0DNm5GX55h06P1mDYcs84p9l584WghBGE3P4BmSPy9gjyzGmqD%2B4Dv9bsohTmQW531EdaxoRHcfnpttOj0PDwSwFG1vc9R7QenkdH3wSXvX6C0GDIRQgzUtesQAVEPByfOjIlvZS4eKFkFhpP93o212bY57CktL0iMNgRGkR4%2BXKDRdCK%2ByvHr0sALe%2BtlfurWwTALM6b6UGsABYozv4GLuATFuAqTQrMa4LQaTRiw2lt4FG5LESGsPhESIt%2BwLB6UGNLcsplZ0qNdn%2FIwwW7zzDpTViSgJHSdgb0asLCFgEKYSz%2B8%2BeWy%2BOud%2BeP5ffinEAcG651%2ByxUd0WkpdOH24hk2sRN2RknjrAMDBKqzGq3lCuC%2FbL%2BezCsmEOVYI7%2BTCncfmkB30sRc%2B1xnfJ4UN8tk%2F7e4fFLpjDjcciqVMKVNI53T9InmRuWiHvTT%2BXWPHpSp7Ii%2Fs0WmjD85HMgxVflZ49ZIfOt4T9%2FCV0XOHQ9q9zUlGzoZ3qSbMK3s9bwGOqUB9NovDeLWSQS7vEe%2FR3%2FhhNSV8gKFMtvvRN%2BawriAIJPriQ90rtq6iO4IJSRKlNGTmdl1CukjzgtWhLaWnQMvBzlDurTw8DGWFL7Yg1r92b4YwSsK3q3jv%2BWcMCFVBb6uiA6SSYNAnXJJ1LWMp1tlTaaCY1qKyARt9DQvaeYbIRbOr2EKaJPa926wJVMyMf9zt7MgvW%2BQXFRiavR5Sff4XiesCoR8&X-Amz-Signature=d36b9e79a5f5155ad8bac3e31e5bc66f7284e17db594bc742944a6a75c4d510a&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/09aba1c0-0d55-41dd-852a-a04c5b8a3fac/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Z3YS552C%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T031859Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEML%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCID09DjjXCDHL%2F3E3OOENSeaUJWbYLuu33OxCmd%2F2vp4hAiEAhqGjkenbuRwdBN6W6lM%2FQo78jg8hiDeu4rxRGIK3sJwqiAQIy%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJtf4yG0XJ%2F9w90ZNyrcA2E6sdsyZgtcN5zEe08TE5X3mfzbTWp4DeHX0vH7TittWhCrEJFTcsWB7O9SQhCn%2BB%2FgPPAPNep0nCEB4RqwT23rpVniKiTrrzvnNMwYV98JcoMIjUh3XLBqgcF3ymjGg%2F8uKDjvyoVJK21fLbHOseyPPMKU%2Fl3522TNNw0G1YXZIB3GK2oL6OYqwsPRX2TFdPYOZrb%2Bk9ZtTNYSeRuWvCdDdH%2FuCYU66cV5QhVJxVNmSN8jdhjA6u9A7XZZhp13tEoDzzMn2LRbNIGs9nu2beXbGa%2FQ1xWMi%2BcrWX5qf2o36GqqDQ9FVkN5s7GUhEaw7OzI2MqHSIYBcw5MkpoFMOIQnKnZJ64ucfAw%2Fs6ndms2NYPwP3Vw5Si7B02JrM%2F30RZq%2FgTGRWWSjb41iDhqhRHi1iCZmvIPMxrt9kfuo0YnCSPgYZuYsYSB7Sqzhg0DjFvTLbATirjrDizZIeq0tUtMJDcqzgPTMC7ZpZpvTTH1pwxCLU0vkltUsovMfJxxGI9QqFYC1wPtkku2z1gUXUQs47wXu6gUMX1e53cBl1WWCoTyifKvIDuY3qGN%2FIQxW7WQG5dMrMTNtoKee85QFM52VSpXaYtwT%2BIS8dSexD7fw7wbMdf4Vjmwyd7gMNH49bwGOqUB7Rej7k1yjUj%2B2JKoqrdF0PyznilO4HsKwk5a%2BzIu6%2FXWpf71a%2BY9lvcOuSxby7i9woAepopaNxmrtx3biOo4yJcT3S5aOAmautCCVwUip%2FE1iRv98aJLdyUM1SAeef8rKMYoAuUhoKv%2BTcFJnJzq%2ByIbYz69gFNFm67WvhyUxFKgoHS1UreU4nF74dAvFG9gh5Yif6MWbmwII2GfxpShYi%2BsRbrD&X-Amz-Signature=b7cd4eb29117f6604b9282be20e0e2bff7c081d61cd32254045e49b25c52fd7a&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 2. Scatter Plot
Scatter plots present the relationship between two variables in a dataset. It represents data points on a two-dimensional plane. The independent variable or attribute is plotted on the X-axis, while the dependent variable is plotted on the Y-axis.
**Syntax:**
```python
plt.scatter(x, y)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23708af9-659f-4f23-b626-1a4292d7842c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Z3YS552C%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T031859Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEML%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCID09DjjXCDHL%2F3E3OOENSeaUJWbYLuu33OxCmd%2F2vp4hAiEAhqGjkenbuRwdBN6W6lM%2FQo78jg8hiDeu4rxRGIK3sJwqiAQIy%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJtf4yG0XJ%2F9w90ZNyrcA2E6sdsyZgtcN5zEe08TE5X3mfzbTWp4DeHX0vH7TittWhCrEJFTcsWB7O9SQhCn%2BB%2FgPPAPNep0nCEB4RqwT23rpVniKiTrrzvnNMwYV98JcoMIjUh3XLBqgcF3ymjGg%2F8uKDjvyoVJK21fLbHOseyPPMKU%2Fl3522TNNw0G1YXZIB3GK2oL6OYqwsPRX2TFdPYOZrb%2Bk9ZtTNYSeRuWvCdDdH%2FuCYU66cV5QhVJxVNmSN8jdhjA6u9A7XZZhp13tEoDzzMn2LRbNIGs9nu2beXbGa%2FQ1xWMi%2BcrWX5qf2o36GqqDQ9FVkN5s7GUhEaw7OzI2MqHSIYBcw5MkpoFMOIQnKnZJ64ucfAw%2Fs6ndms2NYPwP3Vw5Si7B02JrM%2F30RZq%2FgTGRWWSjb41iDhqhRHi1iCZmvIPMxrt9kfuo0YnCSPgYZuYsYSB7Sqzhg0DjFvTLbATirjrDizZIeq0tUtMJDcqzgPTMC7ZpZpvTTH1pwxCLU0vkltUsovMfJxxGI9QqFYC1wPtkku2z1gUXUQs47wXu6gUMX1e53cBl1WWCoTyifKvIDuY3qGN%2FIQxW7WQG5dMrMTNtoKee85QFM52VSpXaYtwT%2BIS8dSexD7fw7wbMdf4Vjmwyd7gMNH49bwGOqUB7Rej7k1yjUj%2B2JKoqrdF0PyznilO4HsKwk5a%2BzIu6%2FXWpf71a%2BY9lvcOuSxby7i9woAepopaNxmrtx3biOo4yJcT3S5aOAmautCCVwUip%2FE1iRv98aJLdyUM1SAeef8rKMYoAuUhoKv%2BTcFJnJzq%2ByIbYz69gFNFm67WvhyUxFKgoHS1UreU4nF74dAvFG9gh5Yif6MWbmwII2GfxpShYi%2BsRbrD&X-Amz-Signature=e649d3fb71a4c57cdbb2e8a82f63c7aa4c8efb975184da00bd5b17dfb68b9a0b&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 3. Histogram
A histogram is an important visual representation of data in categorical form. To view the data in a "Binned" form, use the histogram plot with a number of bins required or with the data points that mark the bin edges. The x-axis represents the data bins, and the y-axis represents the number of elements in each bin.
**Syntax:**
```python
plt.hist(x, bins)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/24e4424a-df87-40a1-b63b-195cbdc2e0ab/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Z3YS552C%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T031859Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEML%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCID09DjjXCDHL%2F3E3OOENSeaUJWbYLuu33OxCmd%2F2vp4hAiEAhqGjkenbuRwdBN6W6lM%2FQo78jg8hiDeu4rxRGIK3sJwqiAQIy%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJtf4yG0XJ%2F9w90ZNyrcA2E6sdsyZgtcN5zEe08TE5X3mfzbTWp4DeHX0vH7TittWhCrEJFTcsWB7O9SQhCn%2BB%2FgPPAPNep0nCEB4RqwT23rpVniKiTrrzvnNMwYV98JcoMIjUh3XLBqgcF3ymjGg%2F8uKDjvyoVJK21fLbHOseyPPMKU%2Fl3522TNNw0G1YXZIB3GK2oL6OYqwsPRX2TFdPYOZrb%2Bk9ZtTNYSeRuWvCdDdH%2FuCYU66cV5QhVJxVNmSN8jdhjA6u9A7XZZhp13tEoDzzMn2LRbNIGs9nu2beXbGa%2FQ1xWMi%2BcrWX5qf2o36GqqDQ9FVkN5s7GUhEaw7OzI2MqHSIYBcw5MkpoFMOIQnKnZJ64ucfAw%2Fs6ndms2NYPwP3Vw5Si7B02JrM%2F30RZq%2FgTGRWWSjb41iDhqhRHi1iCZmvIPMxrt9kfuo0YnCSPgYZuYsYSB7Sqzhg0DjFvTLbATirjrDizZIeq0tUtMJDcqzgPTMC7ZpZpvTTH1pwxCLU0vkltUsovMfJxxGI9QqFYC1wPtkku2z1gUXUQs47wXu6gUMX1e53cBl1WWCoTyifKvIDuY3qGN%2FIQxW7WQG5dMrMTNtoKee85QFM52VSpXaYtwT%2BIS8dSexD7fw7wbMdf4Vjmwyd7gMNH49bwGOqUB7Rej7k1yjUj%2B2JKoqrdF0PyznilO4HsKwk5a%2BzIu6%2FXWpf71a%2BY9lvcOuSxby7i9woAepopaNxmrtx3biOo4yJcT3S5aOAmautCCVwUip%2FE1iRv98aJLdyUM1SAeef8rKMYoAuUhoKv%2BTcFJnJzq%2ByIbYz69gFNFm67WvhyUxFKgoHS1UreU4nF74dAvFG9gh5Yif6MWbmwII2GfxpShYi%2BsRbrD&X-Amz-Signature=baecea0d33297c1494cd0645c47a9584924135881763f235176e34c226946e9e&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ab5a6dfe-51f5-43ee-bcb3-33dae4a1c7ad/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Z3YS552C%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T031859Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEML%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCID09DjjXCDHL%2F3E3OOENSeaUJWbYLuu33OxCmd%2F2vp4hAiEAhqGjkenbuRwdBN6W6lM%2FQo78jg8hiDeu4rxRGIK3sJwqiAQIy%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJtf4yG0XJ%2F9w90ZNyrcA2E6sdsyZgtcN5zEe08TE5X3mfzbTWp4DeHX0vH7TittWhCrEJFTcsWB7O9SQhCn%2BB%2FgPPAPNep0nCEB4RqwT23rpVniKiTrrzvnNMwYV98JcoMIjUh3XLBqgcF3ymjGg%2F8uKDjvyoVJK21fLbHOseyPPMKU%2Fl3522TNNw0G1YXZIB3GK2oL6OYqwsPRX2TFdPYOZrb%2Bk9ZtTNYSeRuWvCdDdH%2FuCYU66cV5QhVJxVNmSN8jdhjA6u9A7XZZhp13tEoDzzMn2LRbNIGs9nu2beXbGa%2FQ1xWMi%2BcrWX5qf2o36GqqDQ9FVkN5s7GUhEaw7OzI2MqHSIYBcw5MkpoFMOIQnKnZJ64ucfAw%2Fs6ndms2NYPwP3Vw5Si7B02JrM%2F30RZq%2FgTGRWWSjb41iDhqhRHi1iCZmvIPMxrt9kfuo0YnCSPgYZuYsYSB7Sqzhg0DjFvTLbATirjrDizZIeq0tUtMJDcqzgPTMC7ZpZpvTTH1pwxCLU0vkltUsovMfJxxGI9QqFYC1wPtkku2z1gUXUQs47wXu6gUMX1e53cBl1WWCoTyifKvIDuY3qGN%2FIQxW7WQG5dMrMTNtoKee85QFM52VSpXaYtwT%2BIS8dSexD7fw7wbMdf4Vjmwyd7gMNH49bwGOqUB7Rej7k1yjUj%2B2JKoqrdF0PyznilO4HsKwk5a%2BzIu6%2FXWpf71a%2BY9lvcOuSxby7i9woAepopaNxmrtx3biOo4yJcT3S5aOAmautCCVwUip%2FE1iRv98aJLdyUM1SAeef8rKMYoAuUhoKv%2BTcFJnJzq%2ByIbYz69gFNFm67WvhyUxFKgoHS1UreU4nF74dAvFG9gh5Yif6MWbmwII2GfxpShYi%2BsRbrD&X-Amz-Signature=e709e89e39be8108c70ae88b355891bc566e9238eeb1b4647d38266309a87e31&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8f1b1d60-cf1b-42b3-9faa-f634c89c3f84/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Z3YS552C%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T031859Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEML%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCID09DjjXCDHL%2F3E3OOENSeaUJWbYLuu33OxCmd%2F2vp4hAiEAhqGjkenbuRwdBN6W6lM%2FQo78jg8hiDeu4rxRGIK3sJwqiAQIy%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJtf4yG0XJ%2F9w90ZNyrcA2E6sdsyZgtcN5zEe08TE5X3mfzbTWp4DeHX0vH7TittWhCrEJFTcsWB7O9SQhCn%2BB%2FgPPAPNep0nCEB4RqwT23rpVniKiTrrzvnNMwYV98JcoMIjUh3XLBqgcF3ymjGg%2F8uKDjvyoVJK21fLbHOseyPPMKU%2Fl3522TNNw0G1YXZIB3GK2oL6OYqwsPRX2TFdPYOZrb%2Bk9ZtTNYSeRuWvCdDdH%2FuCYU66cV5QhVJxVNmSN8jdhjA6u9A7XZZhp13tEoDzzMn2LRbNIGs9nu2beXbGa%2FQ1xWMi%2BcrWX5qf2o36GqqDQ9FVkN5s7GUhEaw7OzI2MqHSIYBcw5MkpoFMOIQnKnZJ64ucfAw%2Fs6ndms2NYPwP3Vw5Si7B02JrM%2F30RZq%2FgTGRWWSjb41iDhqhRHi1iCZmvIPMxrt9kfuo0YnCSPgYZuYsYSB7Sqzhg0DjFvTLbATirjrDizZIeq0tUtMJDcqzgPTMC7ZpZpvTTH1pwxCLU0vkltUsovMfJxxGI9QqFYC1wPtkku2z1gUXUQs47wXu6gUMX1e53cBl1WWCoTyifKvIDuY3qGN%2FIQxW7WQG5dMrMTNtoKee85QFM52VSpXaYtwT%2BIS8dSexD7fw7wbMdf4Vjmwyd7gMNH49bwGOqUB7Rej7k1yjUj%2B2JKoqrdF0PyznilO4HsKwk5a%2BzIu6%2FXWpf71a%2BY9lvcOuSxby7i9woAepopaNxmrtx3biOo4yJcT3S5aOAmautCCVwUip%2FE1iRv98aJLdyUM1SAeef8rKMYoAuUhoKv%2BTcFJnJzq%2ByIbYz69gFNFm67WvhyUxFKgoHS1UreU4nF74dAvFG9gh5Yif6MWbmwII2GfxpShYi%2BsRbrD&X-Amz-Signature=9a64715a0336fdb329e3de48196bf5c692936e7f33346c8c9ed4e4b7ef556967&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/13ad0497-05fe-4eaa-984e-707b33e14761/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Z3YS552C%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T031859Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEML%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCID09DjjXCDHL%2F3E3OOENSeaUJWbYLuu33OxCmd%2F2vp4hAiEAhqGjkenbuRwdBN6W6lM%2FQo78jg8hiDeu4rxRGIK3sJwqiAQIy%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJtf4yG0XJ%2F9w90ZNyrcA2E6sdsyZgtcN5zEe08TE5X3mfzbTWp4DeHX0vH7TittWhCrEJFTcsWB7O9SQhCn%2BB%2FgPPAPNep0nCEB4RqwT23rpVniKiTrrzvnNMwYV98JcoMIjUh3XLBqgcF3ymjGg%2F8uKDjvyoVJK21fLbHOseyPPMKU%2Fl3522TNNw0G1YXZIB3GK2oL6OYqwsPRX2TFdPYOZrb%2Bk9ZtTNYSeRuWvCdDdH%2FuCYU66cV5QhVJxVNmSN8jdhjA6u9A7XZZhp13tEoDzzMn2LRbNIGs9nu2beXbGa%2FQ1xWMi%2BcrWX5qf2o36GqqDQ9FVkN5s7GUhEaw7OzI2MqHSIYBcw5MkpoFMOIQnKnZJ64ucfAw%2Fs6ndms2NYPwP3Vw5Si7B02JrM%2F30RZq%2FgTGRWWSjb41iDhqhRHi1iCZmvIPMxrt9kfuo0YnCSPgYZuYsYSB7Sqzhg0DjFvTLbATirjrDizZIeq0tUtMJDcqzgPTMC7ZpZpvTTH1pwxCLU0vkltUsovMfJxxGI9QqFYC1wPtkku2z1gUXUQs47wXu6gUMX1e53cBl1WWCoTyifKvIDuY3qGN%2FIQxW7WQG5dMrMTNtoKee85QFM52VSpXaYtwT%2BIS8dSexD7fw7wbMdf4Vjmwyd7gMNH49bwGOqUB7Rej7k1yjUj%2B2JKoqrdF0PyznilO4HsKwk5a%2BzIu6%2FXWpf71a%2BY9lvcOuSxby7i9woAepopaNxmrtx3biOo4yJcT3S5aOAmautCCVwUip%2FE1iRv98aJLdyUM1SAeef8rKMYoAuUhoKv%2BTcFJnJzq%2ByIbYz69gFNFm67WvhyUxFKgoHS1UreU4nF74dAvFG9gh5Yif6MWbmwII2GfxpShYi%2BsRbrD&X-Amz-Signature=2db00eca2312870e105301ffa1b28459359f5739054bd48984823fd6c70529d2&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 2. Box and Whisker Plot
A box plot shows the distribution of quantitative data in a way that facilitates comparisons between variables or across levels of a categorical variable. The box shows the quartiles of the dataset while the whiskers extend to show the rest of the distribution, except for points that are determined to be "outliers".
**Syntax:**
```python
sns.boxplot(x='header_1', y='header_2', data=df)
```
**Example Output:**


![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d207ae92-0a7c-4e2f-aa65-0ee5a2c33bf7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666BRGIHJR%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T031901Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHZv5GNr3LPt7KafLvTIhFZNKkjSSWA80acHD4tSdWWuAiBQqopJB5XQg6bhYZPzxIyCAHhP6yEFreXLuM276LJ45iqIBAjK%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMONUP4fagVbC9gd%2FdKtwDuPSxaNPpNuE0dYSqeRIJ1o0Ltt%2FLYeNfflFBKHja0QgtAWohcP9oJpdDjkAW1rXP9FtbZlvoU3Q2%2Fhar8XOUWMR68AUvxAqPybjtu%2Ff2T1XZhSmRi5Lr81eIfa%2FtBdrTTuyLJZ5U7fYruAfNIpKrFFlhYBRPhck8J5VsKQHOAOXnfFz5CQF8hiEOuO0T7brVMfFljMMTE62dvzBWkWIoImuMAA2kN0AGcC7Ybdat8V356%2BIZs8YpvL5usOvMjaPa4kzIrAHzbow0pIvpgyfzsgU18yJ96w2jhag%2BI3oXs7gaQbHRscF0U3GB%2BbifprPbpWS0DPH5R%2F3tCb%2BMPdVgxsTVgJuA6iFkLUtmCsgz16Gih8HL4DV6P4XmD0oMVdaRIValYGn%2Bbl7cp2j6RIkHW%2BU6d7maiopyDpc2iQhLCe5M%2FAOlVFJ1Ws5JlltanFnwz6341Ne%2Bu7bHP74T3t77jKmYIk855pl9Z%2F0qC0qkp%2FatyU35e2Uvam%2Bn9rtNdxFbXZSbxr4z%2BxXcG8TGxgnKmZD19xBW97vrDYZR8dIAwdrJVzIHTcu9%2BvpKXmMFtjZQVEnndZxpgDoMgokt5m9bewhzYXpd%2FbyyneJ2dJWD4V0T1rUQGXr6POhstK8wqOz1vAY6pgHgzUY6%2BY%2F1LuAKMVpqpCQeKjEh7HTpdHA0Hi%2F8wzzLidYgx8g%2B2FHs7li%2BhZR5muwHmbrR04NpAayc4cXQTVlu40slHFfmttSeCdbmEA55A90mIjy%2Fi7kb2Wg73Wg%2BxFRXiOQyfRUyxd%2BAo%2FXl5D9chIPVTXxVbwjSKXmWNwkcbhdWcbpnM78uoFqpLxX2rJGK3ikByDPEngLvhjqttDU7S7bRbTF6&X-Amz-Signature=95567883ae4c329c46f3bb24878c9288553d9061919287535ce3b540754a827a&X-Amz-SignedHeaders=host&x-id=GetObject)

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0e516edc-7551-4792-ab18-0494db3c4c0c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666KJZYIJK%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T031901Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEML%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD2N4mLkK6FDfFxkaMoV04l3BQ2PiGMqgqcvoQ2NaECjQIgfV4cZHOgTZX5eKQcaZ3M4wlRDLcnx7YFcE6ynIqGpnEqiAQIyv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDN2s2WtXJAVT1rzSEyrcAw%2F680iO9L3QdwJOvZOVs4uJ3Xs8%2BmnpfLHNVhcaIiHAZ77RQrqkfUNNUpSdhcwXTPDyvWYwEqgueXyBQLriVPFIBKLi5N9OpOs2te4EuNIkqwrHM%2Bnacbpuh%2BHpUaMdG0At4nh6uGbBCThgjO9gtD2ZVgoA67ffGzpoKsym6ZFW82B9H5RkkfvVXJbGVgwa9YZ%2BH0ws0534CZKdLNBs%2BOn%2BuO%2FyB9R90gS0dOIHsgTz%2B2FlozTolsQNBq%2FNBJsk7Zotm4IW5yCby4hpYyqCdRzLcve3toLMhgzRzVKoXP%2FbRS3TFedZRmITZRCJ%2BSjfeXmmvI%2Bm51jvHccTmw9veB441FMAInUjK8UTq80v8ky0BjedwmPezxIMBoxa5gC89Lapn24%2BefZJpgPSmubwEykXT%2BIjjf52RqP%2FcvhaVana2HVG8e7o3zwH8Ynl48bRJOdRNIsqoTTbslquwEFnfBpRQwWLrtrIgrFQBRJwB%2BXNVDyzHRXxfRJzj%2B5A7SbKGP81LPzR7rLjNb7nIJarUF9b0Wx%2F%2FdhTVp%2B%2FjUU2VteEYW%2BOOgPXFX14oBOATgY2ADqZbfEP32sHwmhkkol1Lqg6ajehvlIiaVVWvsvNIKYTMpq9Q9YUC17TFnC%2FMOXs9bwGOqUBuXMKjlQW87l8nVCixJkxNcCdsjG90AzmdsgJjpfX6oyoD%2F9rw8UhyX8dVID5kTU2oxijCS6NvyWOW70C7KJ7s65oyqD%2B7W5wIZtD0vLmgaap2KCpUqmVO94137PAqhyDif317I%2BuxgWt1aYiUX6pbAOFRjDP4s0dCjtpTfiWMh2tfh5ohq%2BXpyK%2FlC%2BvtIqJWeSHnbj0FI594OZxLFJLg5uoZUMf&X-Amz-Signature=ee84d230f304e5f70c360282ec933de383505d9de2fa6db7e9629126830be32b&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23a79b9d-2356-49a9-8fd9-65c6b0ab2cc5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Z3YS552C%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T031859Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEML%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCID09DjjXCDHL%2F3E3OOENSeaUJWbYLuu33OxCmd%2F2vp4hAiEAhqGjkenbuRwdBN6W6lM%2FQo78jg8hiDeu4rxRGIK3sJwqiAQIy%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJtf4yG0XJ%2F9w90ZNyrcA2E6sdsyZgtcN5zEe08TE5X3mfzbTWp4DeHX0vH7TittWhCrEJFTcsWB7O9SQhCn%2BB%2FgPPAPNep0nCEB4RqwT23rpVniKiTrrzvnNMwYV98JcoMIjUh3XLBqgcF3ymjGg%2F8uKDjvyoVJK21fLbHOseyPPMKU%2Fl3522TNNw0G1YXZIB3GK2oL6OYqwsPRX2TFdPYOZrb%2Bk9ZtTNYSeRuWvCdDdH%2FuCYU66cV5QhVJxVNmSN8jdhjA6u9A7XZZhp13tEoDzzMn2LRbNIGs9nu2beXbGa%2FQ1xWMi%2BcrWX5qf2o36GqqDQ9FVkN5s7GUhEaw7OzI2MqHSIYBcw5MkpoFMOIQnKnZJ64ucfAw%2Fs6ndms2NYPwP3Vw5Si7B02JrM%2F30RZq%2FgTGRWWSjb41iDhqhRHi1iCZmvIPMxrt9kfuo0YnCSPgYZuYsYSB7Sqzhg0DjFvTLbATirjrDizZIeq0tUtMJDcqzgPTMC7ZpZpvTTH1pwxCLU0vkltUsovMfJxxGI9QqFYC1wPtkku2z1gUXUQs47wXu6gUMX1e53cBl1WWCoTyifKvIDuY3qGN%2FIQxW7WQG5dMrMTNtoKee85QFM52VSpXaYtwT%2BIS8dSexD7fw7wbMdf4Vjmwyd7gMNH49bwGOqUB7Rej7k1yjUj%2B2JKoqrdF0PyznilO4HsKwk5a%2BzIu6%2FXWpf71a%2BY9lvcOuSxby7i9woAepopaNxmrtx3biOo4yJcT3S5aOAmautCCVwUip%2FE1iRv98aJLdyUM1SAeef8rKMYoAuUhoKv%2BTcFJnJzq%2ByIbYz69gFNFm67WvhyUxFKgoHS1UreU4nF74dAvFG9gh5Yif6MWbmwII2GfxpShYi%2BsRbrD&X-Amz-Signature=59f82968eb3660c8e72a697179c89180e9991d1cb21b08c1380093f623822c1f&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 4. KDE Plot
A Kernel Density Estimate (KDE) plot is a graph that creates a probability distribution curve for the data based upon its likelihood of occurrence on a specific value. This is created for a single vector of information.
**Syntax:**
```python
sns.kdeplot(X) || sns.kdeplot(df['age'])
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0d571213-2a2f-4921-a50b-880847aa05ee/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Z3YS552C%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T031859Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEML%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCID09DjjXCDHL%2F3E3OOENSeaUJWbYLuu33OxCmd%2F2vp4hAiEAhqGjkenbuRwdBN6W6lM%2FQo78jg8hiDeu4rxRGIK3sJwqiAQIy%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJtf4yG0XJ%2F9w90ZNyrcA2E6sdsyZgtcN5zEe08TE5X3mfzbTWp4DeHX0vH7TittWhCrEJFTcsWB7O9SQhCn%2BB%2FgPPAPNep0nCEB4RqwT23rpVniKiTrrzvnNMwYV98JcoMIjUh3XLBqgcF3ymjGg%2F8uKDjvyoVJK21fLbHOseyPPMKU%2Fl3522TNNw0G1YXZIB3GK2oL6OYqwsPRX2TFdPYOZrb%2Bk9ZtTNYSeRuWvCdDdH%2FuCYU66cV5QhVJxVNmSN8jdhjA6u9A7XZZhp13tEoDzzMn2LRbNIGs9nu2beXbGa%2FQ1xWMi%2BcrWX5qf2o36GqqDQ9FVkN5s7GUhEaw7OzI2MqHSIYBcw5MkpoFMOIQnKnZJ64ucfAw%2Fs6ndms2NYPwP3Vw5Si7B02JrM%2F30RZq%2FgTGRWWSjb41iDhqhRHi1iCZmvIPMxrt9kfuo0YnCSPgYZuYsYSB7Sqzhg0DjFvTLbATirjrDizZIeq0tUtMJDcqzgPTMC7ZpZpvTTH1pwxCLU0vkltUsovMfJxxGI9QqFYC1wPtkku2z1gUXUQs47wXu6gUMX1e53cBl1WWCoTyifKvIDuY3qGN%2FIQxW7WQG5dMrMTNtoKee85QFM52VSpXaYtwT%2BIS8dSexD7fw7wbMdf4Vjmwyd7gMNH49bwGOqUB7Rej7k1yjUj%2B2JKoqrdF0PyznilO4HsKwk5a%2BzIu6%2FXWpf71a%2BY9lvcOuSxby7i9woAepopaNxmrtx3biOo4yJcT3S5aOAmautCCVwUip%2FE1iRv98aJLdyUM1SAeef8rKMYoAuUhoKv%2BTcFJnJzq%2ByIbYz69gFNFm67WvhyUxFKgoHS1UreU4nF74dAvFG9gh5Yif6MWbmwII2GfxpShYi%2BsRbrD&X-Amz-Signature=0732b1aeec36f5c529dcacc83bd7b7ba867293ec0136a2b9dba513a3f1f923b4&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/53752550-ef82-4ca9-a01a-09921f0282d0/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Z3YS552C%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T031859Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEML%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCID09DjjXCDHL%2F3E3OOENSeaUJWbYLuu33OxCmd%2F2vp4hAiEAhqGjkenbuRwdBN6W6lM%2FQo78jg8hiDeu4rxRGIK3sJwqiAQIy%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJtf4yG0XJ%2F9w90ZNyrcA2E6sdsyZgtcN5zEe08TE5X3mfzbTWp4DeHX0vH7TittWhCrEJFTcsWB7O9SQhCn%2BB%2FgPPAPNep0nCEB4RqwT23rpVniKiTrrzvnNMwYV98JcoMIjUh3XLBqgcF3ymjGg%2F8uKDjvyoVJK21fLbHOseyPPMKU%2Fl3522TNNw0G1YXZIB3GK2oL6OYqwsPRX2TFdPYOZrb%2Bk9ZtTNYSeRuWvCdDdH%2FuCYU66cV5QhVJxVNmSN8jdhjA6u9A7XZZhp13tEoDzzMn2LRbNIGs9nu2beXbGa%2FQ1xWMi%2BcrWX5qf2o36GqqDQ9FVkN5s7GUhEaw7OzI2MqHSIYBcw5MkpoFMOIQnKnZJ64ucfAw%2Fs6ndms2NYPwP3Vw5Si7B02JrM%2F30RZq%2FgTGRWWSjb41iDhqhRHi1iCZmvIPMxrt9kfuo0YnCSPgYZuYsYSB7Sqzhg0DjFvTLbATirjrDizZIeq0tUtMJDcqzgPTMC7ZpZpvTTH1pwxCLU0vkltUsovMfJxxGI9QqFYC1wPtkku2z1gUXUQs47wXu6gUMX1e53cBl1WWCoTyifKvIDuY3qGN%2FIQxW7WQG5dMrMTNtoKee85QFM52VSpXaYtwT%2BIS8dSexD7fw7wbMdf4Vjmwyd7gMNH49bwGOqUB7Rej7k1yjUj%2B2JKoqrdF0PyznilO4HsKwk5a%2BzIu6%2FXWpf71a%2BY9lvcOuSxby7i9woAepopaNxmrtx3biOo4yJcT3S5aOAmautCCVwUip%2FE1iRv98aJLdyUM1SAeef8rKMYoAuUhoKv%2BTcFJnJzq%2ByIbYz69gFNFm67WvhyUxFKgoHS1UreU4nF74dAvFG9gh5Yif6MWbmwII2GfxpShYi%2BsRbrD&X-Amz-Signature=a8fa4397de8c7e2eeaedd04928639d66d76bddfc9412507a6ad2537da478efd0&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
## 4. Correlation Between Variables
Correlation is a statistical measure of the extent to which different variables are interdependent. It indicates how changes in one variable are associated with changes in another variable over time.
### Positive Correlation
Positive correlation indicates that as one variable increases, the other variable also tends to increase.
**Example: Engine Size and Price**
- **Positive Correlation:** Engine size increases, price also increases.
- **Visualization:** Scatter plot with a steep positive slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c7ea9b0-3ef3-4357-a9c3-554fc71b6b15/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RNKQHRYU%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T031901Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEML%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDw5pTBWtQak6uch7MvkzzNhv2CmoifY8sHPE1dmpeP0QIhAMWa%2FCOhBNhCP6%2BSecyYRjNjWHrpvVitCjr0%2Bl8Wi9i%2BKogECMr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxWDn50k2Cl8aBKgMUq3AOz%2F%2FVp2nfIRsS58KL994N%2FCmNUJ9Opl9exmQ0nqAvNQI6C2cn386jPib5AnIj9sr2Uz%2FTS2xLF9%2BiAvzdjd7HjKeORYsz%2BMeFeV1qqRMELXkJYX%2FH47j76yXKbUbMZAZW5w%2BR%2FmNidC9PH1ksuhuZd3WDpodX5bjlYoQqJjnvygmfMmd9GqM4q6jEtVEv%2FCTZ8rte5FqgMHJ38JPtoDAbcPox4%2FKdMp1x%2BOJzd0IxPQ%2BrKsXzUJ3Nyxe1ag10TLLmiSRhIJmGXNFH3IemOEn%2F3AnHyn3gbLXjlk3zn4bUkBrM1W3he0HrjZSGa1HWoaYzVA9ndJ8X4aWZU2ZUJB2Qnsw7amPtRQY8k42Lvl1lRScRSEZjtBfVynMlAlY2c23osdjUKwUrdB65uru2oam0FYqt%2BuEAxaGDSFl6%2BvGcMjxoOsmCmOIbrJkXias61KG6jybRbCFCsMK1smnUeVuDdkkO%2BojI8pw2fOlPRaVXxT2m4zt2q9Uj8O%2BsnXmkczA6QN82hYDJa5Hd1F%2F1AWfuabWceTr2%2FI6wWGDdScYZhaMv%2FWZFqRLlKl4fht2DMaVAd73JbS%2FBWj58gF2RSIlH3EREsYolNDuywQfVUQMFun9jeLfv5UQDjILiThzDm7PW8BjqkATeq4P3rkHuSmaWGtsLInX1ADCWl%2BkMhyiEiV3tbaxyrJajO5dq%2BLOGjdjJUzTEuU2%2FOouboEHQ1SP1UhfiHR5ZDi9pAlc1VsbS9OHkxWRi9ZeobZ1cBP%2FmD%2F%2Bjk4C87pyb9otoepWaYSghYXwr0b7VFCrzWaVu3MViBKGmU4hYB2BRdWIb%2FGonsyoXg9cAeCmoJGPz1EBunFNT3J0xGYMBdY7ce&X-Amz-Signature=878660407a0d9cdbceb945ed9d7f56515f4d8319e462d39df4386c5c25644fcf&X-Amz-SignedHeaders=host&x-id=GetObject)
**Explanation:** When engine size increases, there is a corresponding increase in the price of the vehicle. This positive correlation suggests that larger engines tend to be associated with higher prices in the market.
___
### Negative Correlation
Negative correlation indicates that as one variable increases, the other variable tends to decrease.
**Example: Highway Miles per Gallon and Price**
- **Negative Correlation:** As highway miles per gallon increases, price decreases.
- **Visualization:** Scatter plot with a steep negative slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/10f1f798-9cc4-4df2-a9c1-5a339f554a0b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46627ZPT4MO%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T031900Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGOeK8elDo14aK6zIE5KNFKQMi8IVCzpn8ckLZUMZLVyAiEAqUck8D%2F7UWJx4cUClThO168NCPtffLLH6CSwiv4t%2BdQqiAQIyv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMxnif9FvUxkSoOWIyrcA4GkWUNP8TYAMInZ%2FK8MhgGd9XHPPeRcdHNyq9CDx26XQBoIAFYnBH41g4W3cr1nqGEVepJbon1HSLrNvLg0beH0WI7CCxOzlvHH3UEzJAKifwbyfHqb%2Fo9HEudznInTIbqnn%2Bs0l83i8VM1le4W3icArezD6Z47Czf0tx3mypakFliPm8PkIZ%2FxYciKmxHiY%2BTyzTg3hLpt5X4hJ0ZNa3c49bKT%2Be1m8kzK3kdlPt%2BSz1h2SRnIpJ7MVZDP6NppLK7D0jH1nhMVjF8MoEMriq%2FztNL3XyIHuSHEHCfdWW21CGG%2BpFy1%2FRXIz3kD0c2vngulmw6BoHtuHZOfq8CLqUARXwuRiNBm9tjHsDonmN1AjBfMNo5Sjd0%2BqsRxze87goTfOvyW7flBSgkRr4vwhnw1Uo5BJitaJpmumLGgYoPyeE2xKU%2BPYOnE51bqtx1MgY5TJov1yxPzlB%2B%2Bn2Gh%2F1DC0%2F1A7XybvmWy6eDMl5okjVyOIaEvkBsFl9nuhh8XQSnfTDhswcSyeqdoOhoTOo9OA2NRiYGzrqsAfiSBX6PBzAWGMvwgcQl7Dvv3eerPyGyK2b5lKPZ%2FRwMWJDxzrPA5JinQKq1A3NOVFL1O%2BffL7grDhO0BtKkiKuVGMJXs9bwGOqUBjJPRmx2dKoGVtjS9lZX8wiiYJH5uQxXrkNVK%2FWKEMaMlnWyCm%2BytUo7bn5cmlz%2FXMdUNk7H6gsLHssle5oMInHqKUXbkCkVTQ9xpjKaIK0cANfJRuAxNSq73pInqqy%2F2zm7zN%2FGtK1F3uMNJS7PsaLEvhivl627%2BFbcC%2FrW0O7fVoOXiKfPievPcKNBjAtAsbRJuOCJHzNhK84VtrOrLaAVnvNaP&X-Amz-Signature=2ba11eca6bd9353fa4ce961d911c80ab330741375d6fa3119257978edfa9caaa&X-Amz-SignedHeaders=host&x-id=GetObject)
**Explanation:** When highway miles per gallon increases, the price of the vehicle tends to decrease. This negative correlation suggests that cars with higher fuel efficiency (more miles per gallon) are generally priced lower in the market.
___
### Weak Correlation
Weak correlation indicates a lack of strong relationship between the variables.
**Example: RPM and Price**
- **Weak Correlation:** Low and high RPM values show varied prices, indicating no strong predictive relationship.
- **Visualization:** Scatter plot with no clear trend or slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9f914514-8914-4bf4-ac84-d9e3077f6eb1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46652XQEW4M%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T031901Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEML%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCA9%2BZsZsv7XZMzAEpOtBjPX7RxwhDnK702nU6wa0B0bgIgbdXKbYeoMFhclEazTJnP6%2BHOQBzBB4ZnhuJ1z3cXyncqiAQIyv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDS%2FTg3HhA9DQLA%2FxyrcA6MEnsAaXV8xYib4Cgjc7%2BK1RAT1vnAXCrUxjuMzZVCoRr%2Fz09TOb1MgtElAZR4kJY2CtbJoR%2FHl1nqR4MpK7d5JvroIGfZ6FJFsIjO2hXi19QUN8MQtWIuG3XbP0Ne7lcrgRTuJuBCjA5SMqP4ODnm09I2uUB0Z%2FS5RhyrorbTkihKQew%2FXZyZnI7Qeuibt5WyQGFXb59BvIGlOVjI0U3dy1tlg1cQkfocygMJlKkVzUcEl6ShFIcyBItrz9PuJh1Whp4LrenUzdm3SA%2FBxbcba7N0Ateah%2BO1RnrMktoRycpMX7%2Bnd50UU9Mwd4yP3hYVd8doM8%2FOjx76UVlyU77J%2BLUSyJhCYxVLQl1dA0kl6qqBUXYQdI3NCFpljb82i8k3F1QeRNq7oP0S%2BNYSOCC8PgsmhZU1YCTGuGpklpbiQNISAFuK%2F9cHr12vhmcJP7dlvCZWCUeW4q0LmHIkj58HAl9lgHt5qwUeSVvSFg5Wrvm8zvO9D6XLP4xUPCkbo5aiN7sqaoemyFXTkREV7bUnkPS9gIOMY9K0Q1gxwG7lZHdVYpfThVJyIIfBGSK406YgvzYySfX5U%2BFcWWR5uA62kG%2Ba93Egya2sLBo1yNHefJWdqPRdlOypQqmOYMNrs9bwGOqUB4nQlb9f6csJj79rX2EH3ECmhvoVtS6WqxXDg%2FGlxU8nWKW25VXnqC2Bqdbmhx3l3bWXRMeH0jbBCx7yUolUvOiIz%2BeGOGuICfDcnzwaMBj02KiYlQpLeJeLXxEjZhNS1tjQiyH3DjxEY93ABfLIGkPjjMqKk7d8qKFACd3mbFb1sdPkPZuKNzW3rWsxjSxf4CilR2gBySqW3Pe7Kdz5AoyYt9rci&X-Amz-Signature=c833a467fcb7ef351fa4af64039d4d045cab34d9099ebe78c1a559c915be9321&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f18086e5-5b04-4fbf-8309-8944ab20d213/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TPEDT27R%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T031900Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIEiMaQJsG%2FNakitfZukI8hmpHrRbgGWAl9vQOyeiZpJMAiEAytf912pqTepPTHGRQnZ2MCyIc9OtdwGO7n1OECIBLNwqiAQIyv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKys5mcbZXkT3IQIECrcA81lrB1XgOxzpII1CFTe4dBM1DO2Pakvi7BY4fzX3y3VgPVGyg41dlP23y1MMMXLn14fna1eAYkiZQxvagWpfwlzWRJ0%2FSpShi6FU%2B7nmMggI%2Fh5uwgVjtiSmqVRJw5p%2BI9vcEjtcQfIoCJJPtigBM50%2FpKvzQ%2Fxi20CnnE77E7qzsFGjhxiDQOIZp%2Fqdut6%2Bn8iKySy%2F9Doa7NbYKPyWipOEbBmgW1A3kkIav0xRcV9XRfS9nipNBLwRm%2BwaMH8RPruNaJYeTjcPQEUk4BYxAoTWQFR19855sLLbR3MX4ShmhlAiFP%2BGQ13Xss7fA2j4gNdECLAionbGHrnjh3s6uJ7%2BK6TRVRfO%2Blan316CUQfiZHhzrVd4i0m40gj4dhRps1RaUIVjGZJhsXbo9r%2BuFNxlaOyXJJSIR%2BriNc6S6tckXVAe6dgzbgJuH%2FdbLQGTgc%2B7M0GzSELdu15Fsf7elLd%2BmEHnQzbTub8JTY683mZfY7Nfod4IRanjycSRt0%2BVOaetUx7Skv4uVJcJN7ccaO9bm7%2B%2FduKy7he1X7kBuS%2F1XGpGvXNatY30UqJR0wm%2BCeZzuiJoe%2BxICOfQG5AbZ9PuVtpCW4KHO9SEmm35kevQejOL6YQg9kdtD36MK%2Fs9bwGOqUBJjcqJXk2LFkO%2FuktMFQN7jUYj0CFNC2Q3WuT%2FM%2BkgasB9MowpfwOp3wXskCnvs%2FnOP8Lv5lJ7x2UOXTrfp3ev%2BY5hitwO9PltEjBPgVF6zg%2BJkuGFqfMR4vJAzTPH8t1ApmvmyiOfoU87VZ2LpzPjm%2FpHrLT7LdpjPjBCn2ksW1LgsRcoDgqa6WQSGcJAmNejIZemuI08wh93v58VF4qBPi9cMoN&X-Amz-Signature=5e91115d5693d8c9d50ae6b2b1bcde3c4209ac8e503b95c06236401dedb6736d&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Correlation Plot
Heatmap visualizes correlations among variables. Color scheme indicates Pearson correlation coefficients. Dark red diagonal line shows perfect correlation (value of 1) between variables and themselves.
This heatmap offers overview of variable relationships and their link with price.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cd3b341e-cc1a-45f7-8aec-cdc00436d270/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TPEDT27R%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T031900Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIEiMaQJsG%2FNakitfZukI8hmpHrRbgGWAl9vQOyeiZpJMAiEAytf912pqTepPTHGRQnZ2MCyIc9OtdwGO7n1OECIBLNwqiAQIyv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKys5mcbZXkT3IQIECrcA81lrB1XgOxzpII1CFTe4dBM1DO2Pakvi7BY4fzX3y3VgPVGyg41dlP23y1MMMXLn14fna1eAYkiZQxvagWpfwlzWRJ0%2FSpShi6FU%2B7nmMggI%2Fh5uwgVjtiSmqVRJw5p%2BI9vcEjtcQfIoCJJPtigBM50%2FpKvzQ%2Fxi20CnnE77E7qzsFGjhxiDQOIZp%2Fqdut6%2Bn8iKySy%2F9Doa7NbYKPyWipOEbBmgW1A3kkIav0xRcV9XRfS9nipNBLwRm%2BwaMH8RPruNaJYeTjcPQEUk4BYxAoTWQFR19855sLLbR3MX4ShmhlAiFP%2BGQ13Xss7fA2j4gNdECLAionbGHrnjh3s6uJ7%2BK6TRVRfO%2Blan316CUQfiZHhzrVd4i0m40gj4dhRps1RaUIVjGZJhsXbo9r%2BuFNxlaOyXJJSIR%2BriNc6S6tckXVAe6dgzbgJuH%2FdbLQGTgc%2B7M0GzSELdu15Fsf7elLd%2BmEHnQzbTub8JTY683mZfY7Nfod4IRanjycSRt0%2BVOaetUx7Skv4uVJcJN7ccaO9bm7%2B%2FduKy7he1X7kBuS%2F1XGpGvXNatY30UqJR0wm%2BCeZzuiJoe%2BxICOfQG5AbZ9PuVtpCW4KHO9SEmm35kevQejOL6YQg9kdtD36MK%2Fs9bwGOqUBJjcqJXk2LFkO%2FuktMFQN7jUYj0CFNC2Q3WuT%2FM%2BkgasB9MowpfwOp3wXskCnvs%2FnOP8Lv5lJ7x2UOXTrfp3ev%2BY5hitwO9PltEjBPgVF6zg%2BJkuGFqfMR4vJAzTPH8t1ApmvmyiOfoU87VZ2LpzPjm%2FpHrLT7LdpjPjBCn2ksW1LgsRcoDgqa6WQSGcJAmNejIZemuI08wh93v58VF4qBPi9cMoN&X-Amz-Signature=54fc6e36dbf1d4e8ed06347517955edd4fda82ddd1a8f0bd31578be07a575e75&X-Amz-SignedHeaders=host&x-id=GetObject)

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
