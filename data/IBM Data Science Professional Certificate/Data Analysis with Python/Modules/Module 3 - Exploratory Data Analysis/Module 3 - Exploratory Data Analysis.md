

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7e6d594d-952e-44b6-97ea-31225882aea6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UF6XNEY5%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T051551Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjED0aCXVzLXdlc3QtMiJHMEUCIQDjZD8ze5%2F646xg0sD9810Biw7m6QUhGx5%2BQPHIxM2ViQIgR%2Bvth7RsMiZk%2Fd09%2FHi3JL9Qc6MKdzeYDvJxxiy4KWUq%2FwMIVhAAGgw2Mzc0MjMxODM4MDUiDAWXbv8nxSuEcjdnoCrcA1RMflSXJ7a2fmszdSKQIxI%2FJ1p3PioXaha03ESJV%2FR2HEEXji4tjF4xdNBZgAiAaO2XVEYyHxh%2F62NPUBHdwwCrfFmM6UybR10HNrRtKEIRmaVJL3UYj%2FN4NJcL9NBLlBwiaqzmxUznccyZBSfqaXqu5wRDRMOFYbjnAxBuivJesvJeSYSIrHj6a4taAOHhu1WOWhfDTOU91N11vl6DvS4WttpLTsTecB2%2FbGPRsWpXJXtYt5nKxBmiw8FJimuurcIVwt4f5Ts%2B1QLK0EzUWPmJoSVmc2SmjjJ23eadCjtG16Zyi88XHylmpgYqCmgO6UyB9kXohbOX2mX4SLwuVp8WU8vK%2BjqAeXzr78PtQ7f9PyJun%2BBGorHc57QmYGKL3v%2FIN1F4Gm%2B8MOJeeIdmlwCDxfB98DDxcZOnnHFSK4Wcayktx%2ByOXuREMo4EmCviAhrJCc5u85aD0%2B64hAu0fFjDXTgBi9pLMbxVtWVazoCS8t2vo0zXJyECbsALTy1zD9G47qD2eOYmdGAialLMCKd%2BwR407rZieSTd6UFOPH2f%2BAsR8VDpZ0jfxouzkDAqZR68igMxaBI4iXxcK13LE%2FmfCNt0jj7wsbWsPBwJ0O0F2WJpGSQV%2B1JccCADMPr7kL0GOqUBWSeCV5pM2MMHnyve79XI3ZoipEVjOERXwY%2B%2Bn8PubJUy6hFBGSEswJ4Z5A7SaNHE2OFsDZJ8Ba%2BXMpFrSZ9L0IvlHARYEVtVLtzu5fuGfKCbR0Bpp1DWBWSHVjSIga1qWoUx8YmOi0hJlXoa8ErM6%2B0xoCWX7NVVmVMzYh2KYimeVHsZCahTslQV5btfWKU2yjK%2BtPpYwgjd1ACH5SPq8NoIwaXQ&X-Amz-Signature=13e612ecb059af2859f736a3d5046cb45344af9348cd9fa1c19ca73a828aec73&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cbfaed9e-b398-4902-8936-dea058b21def/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UF6XNEY5%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T051551Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjED0aCXVzLXdlc3QtMiJHMEUCIQDjZD8ze5%2F646xg0sD9810Biw7m6QUhGx5%2BQPHIxM2ViQIgR%2Bvth7RsMiZk%2Fd09%2FHi3JL9Qc6MKdzeYDvJxxiy4KWUq%2FwMIVhAAGgw2Mzc0MjMxODM4MDUiDAWXbv8nxSuEcjdnoCrcA1RMflSXJ7a2fmszdSKQIxI%2FJ1p3PioXaha03ESJV%2FR2HEEXji4tjF4xdNBZgAiAaO2XVEYyHxh%2F62NPUBHdwwCrfFmM6UybR10HNrRtKEIRmaVJL3UYj%2FN4NJcL9NBLlBwiaqzmxUznccyZBSfqaXqu5wRDRMOFYbjnAxBuivJesvJeSYSIrHj6a4taAOHhu1WOWhfDTOU91N11vl6DvS4WttpLTsTecB2%2FbGPRsWpXJXtYt5nKxBmiw8FJimuurcIVwt4f5Ts%2B1QLK0EzUWPmJoSVmc2SmjjJ23eadCjtG16Zyi88XHylmpgYqCmgO6UyB9kXohbOX2mX4SLwuVp8WU8vK%2BjqAeXzr78PtQ7f9PyJun%2BBGorHc57QmYGKL3v%2FIN1F4Gm%2B8MOJeeIdmlwCDxfB98DDxcZOnnHFSK4Wcayktx%2ByOXuREMo4EmCviAhrJCc5u85aD0%2B64hAu0fFjDXTgBi9pLMbxVtWVazoCS8t2vo0zXJyECbsALTy1zD9G47qD2eOYmdGAialLMCKd%2BwR407rZieSTd6UFOPH2f%2BAsR8VDpZ0jfxouzkDAqZR68igMxaBI4iXxcK13LE%2FmfCNt0jj7wsbWsPBwJ0O0F2WJpGSQV%2B1JccCADMPr7kL0GOqUBWSeCV5pM2MMHnyve79XI3ZoipEVjOERXwY%2B%2Bn8PubJUy6hFBGSEswJ4Z5A7SaNHE2OFsDZJ8Ba%2BXMpFrSZ9L0IvlHARYEVtVLtzu5fuGfKCbR0Bpp1DWBWSHVjSIga1qWoUx8YmOi0hJlXoa8ErM6%2B0xoCWX7NVVmVMzYh2KYimeVHsZCahTslQV5btfWKU2yjK%2BtPpYwgjd1ACH5SPq8NoIwaXQ&X-Amz-Signature=9687daa248c6f7ed7cbf418311ba48fbf1b5ce2c1b8ccc9a848d086aebc16f99&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/91181646-b1e0-4433-9711-6259a96a9247/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UF6XNEY5%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T051551Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjED0aCXVzLXdlc3QtMiJHMEUCIQDjZD8ze5%2F646xg0sD9810Biw7m6QUhGx5%2BQPHIxM2ViQIgR%2Bvth7RsMiZk%2Fd09%2FHi3JL9Qc6MKdzeYDvJxxiy4KWUq%2FwMIVhAAGgw2Mzc0MjMxODM4MDUiDAWXbv8nxSuEcjdnoCrcA1RMflSXJ7a2fmszdSKQIxI%2FJ1p3PioXaha03ESJV%2FR2HEEXji4tjF4xdNBZgAiAaO2XVEYyHxh%2F62NPUBHdwwCrfFmM6UybR10HNrRtKEIRmaVJL3UYj%2FN4NJcL9NBLlBwiaqzmxUznccyZBSfqaXqu5wRDRMOFYbjnAxBuivJesvJeSYSIrHj6a4taAOHhu1WOWhfDTOU91N11vl6DvS4WttpLTsTecB2%2FbGPRsWpXJXtYt5nKxBmiw8FJimuurcIVwt4f5Ts%2B1QLK0EzUWPmJoSVmc2SmjjJ23eadCjtG16Zyi88XHylmpgYqCmgO6UyB9kXohbOX2mX4SLwuVp8WU8vK%2BjqAeXzr78PtQ7f9PyJun%2BBGorHc57QmYGKL3v%2FIN1F4Gm%2B8MOJeeIdmlwCDxfB98DDxcZOnnHFSK4Wcayktx%2ByOXuREMo4EmCviAhrJCc5u85aD0%2B64hAu0fFjDXTgBi9pLMbxVtWVazoCS8t2vo0zXJyECbsALTy1zD9G47qD2eOYmdGAialLMCKd%2BwR407rZieSTd6UFOPH2f%2BAsR8VDpZ0jfxouzkDAqZR68igMxaBI4iXxcK13LE%2FmfCNt0jj7wsbWsPBwJ0O0F2WJpGSQV%2B1JccCADMPr7kL0GOqUBWSeCV5pM2MMHnyve79XI3ZoipEVjOERXwY%2B%2Bn8PubJUy6hFBGSEswJ4Z5A7SaNHE2OFsDZJ8Ba%2BXMpFrSZ9L0IvlHARYEVtVLtzu5fuGfKCbR0Bpp1DWBWSHVjSIga1qWoUx8YmOi0hJlXoa8ErM6%2B0xoCWX7NVVmVMzYh2KYimeVHsZCahTslQV5btfWKU2yjK%2BtPpYwgjd1ACH5SPq8NoIwaXQ&X-Amz-Signature=01fe4db8de2cc1fc590d471787ddae45b619d543bc94afeab7dad80e87ae44d4&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/09aba1c0-0d55-41dd-852a-a04c5b8a3fac/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RDOMMUGB%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T051551Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjED0aCXVzLXdlc3QtMiJHMEUCIQDXm46pXRDjj1oyTs9SGWNs0W4m3GP6hXqekqQlqmgAFQIgFyHuoVutoHn60oqRMz4W2g8gINZKAdEOjileuPoUivMq%2FwMIVhAAGgw2Mzc0MjMxODM4MDUiDPDx1EZB1Cnnig946CrcA1LA0ENeJ3Z3R%2F17D0NO5562f8JI%2F4C7PvYpKRigfenpngKAal8meS9pfSMrhZTOB3jgCv1sND5CsM5pkfKf9VK52WAiKN7d9MQtb%2BZhPKb6O9RC6GrHNz6kyG02VEopMlMro6FoP9eoBhkhUT6dTOSPRBnpWokeJvQcm2TAmTm8owl%2BDVu96rcyUWFhIwMH%2B3lRWV%2Brm%2BJhnNm5aaLxsMv%2B4Rs63wn8eTPTwMrWBsCKrlWqNRVvmz%2ForyedGTDixzXvdqtTPxxqkMO3dIMqeW203XuAJbNQ40j4Aa%2BleC6ndz438HAe6aVRNg8HkowRmB3jAdkkqwbnlwjCeiOaWTZJvUjkIuPLTpZ87wGVWw%2FrQRm3smrWZqyU7xri%2Bz2buW2l9PYpUNLf1EHkXt11weHcNo6ErLesyty7FezqBCW6tUtbWlc5jtD%2BbjlYfdBPaydhS9nnDoW2ntPNcZWYe2D%2BNwqOIY6N53%2BXu3u2bx7fEmnB3mcQZgvCk7hvJzl0uYOlzPW%2BUHH5Hnx0BIIC5P3HYh2TCjKhfIajkY8%2BXV4FOngI8cnADZ6mb%2BLnPUk5%2FwWqGGl9uKhCl4fe9mT%2BHd3bZ%2FSSDfOgzZ%2FDwXJBLktMl8QoEHuZxVzO2OfcMN37kL0GOqUBOqjYaM4CafV1j6C2fap5Xcifw8qTguGmhQtnqQDU5VapeiK4kv30NSSt%2F%2BjJfomZJPIRBzxc4VVnveDWmASS7hmSiogNsDe5mWZwyjVtA2VyWhTdsHh61D3hWgnseO%2BloTBQ07eoajpHdWn8lcQlwiTE6Em8%2BNjTibFB5QbDY1LwRun%2BQKKdO0G8Ve64peXz3kNOMSqti5xMWGqmOIKj5dRu5G4R&X-Amz-Signature=24ea30bfcd5a9727a024d31ac80057824f44ba04706003da3b1ad0608a266a63&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 2. Scatter Plot
Scatter plots present the relationship between two variables in a dataset. It represents data points on a two-dimensional plane. The independent variable or attribute is plotted on the X-axis, while the dependent variable is plotted on the Y-axis.
**Syntax:**
```python
plt.scatter(x, y)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23708af9-659f-4f23-b626-1a4292d7842c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RDOMMUGB%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T051551Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjED0aCXVzLXdlc3QtMiJHMEUCIQDXm46pXRDjj1oyTs9SGWNs0W4m3GP6hXqekqQlqmgAFQIgFyHuoVutoHn60oqRMz4W2g8gINZKAdEOjileuPoUivMq%2FwMIVhAAGgw2Mzc0MjMxODM4MDUiDPDx1EZB1Cnnig946CrcA1LA0ENeJ3Z3R%2F17D0NO5562f8JI%2F4C7PvYpKRigfenpngKAal8meS9pfSMrhZTOB3jgCv1sND5CsM5pkfKf9VK52WAiKN7d9MQtb%2BZhPKb6O9RC6GrHNz6kyG02VEopMlMro6FoP9eoBhkhUT6dTOSPRBnpWokeJvQcm2TAmTm8owl%2BDVu96rcyUWFhIwMH%2B3lRWV%2Brm%2BJhnNm5aaLxsMv%2B4Rs63wn8eTPTwMrWBsCKrlWqNRVvmz%2ForyedGTDixzXvdqtTPxxqkMO3dIMqeW203XuAJbNQ40j4Aa%2BleC6ndz438HAe6aVRNg8HkowRmB3jAdkkqwbnlwjCeiOaWTZJvUjkIuPLTpZ87wGVWw%2FrQRm3smrWZqyU7xri%2Bz2buW2l9PYpUNLf1EHkXt11weHcNo6ErLesyty7FezqBCW6tUtbWlc5jtD%2BbjlYfdBPaydhS9nnDoW2ntPNcZWYe2D%2BNwqOIY6N53%2BXu3u2bx7fEmnB3mcQZgvCk7hvJzl0uYOlzPW%2BUHH5Hnx0BIIC5P3HYh2TCjKhfIajkY8%2BXV4FOngI8cnADZ6mb%2BLnPUk5%2FwWqGGl9uKhCl4fe9mT%2BHd3bZ%2FSSDfOgzZ%2FDwXJBLktMl8QoEHuZxVzO2OfcMN37kL0GOqUBOqjYaM4CafV1j6C2fap5Xcifw8qTguGmhQtnqQDU5VapeiK4kv30NSSt%2F%2BjJfomZJPIRBzxc4VVnveDWmASS7hmSiogNsDe5mWZwyjVtA2VyWhTdsHh61D3hWgnseO%2BloTBQ07eoajpHdWn8lcQlwiTE6Em8%2BNjTibFB5QbDY1LwRun%2BQKKdO0G8Ve64peXz3kNOMSqti5xMWGqmOIKj5dRu5G4R&X-Amz-Signature=9142a85f28da98d1b64341fb9103676a38f5f311d11a5b69e50a0a702337c107&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 3. Histogram
A histogram is an important visual representation of data in categorical form. To view the data in a "Binned" form, use the histogram plot with a number of bins required or with the data points that mark the bin edges. The x-axis represents the data bins, and the y-axis represents the number of elements in each bin.
**Syntax:**
```python
plt.hist(x, bins)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/24e4424a-df87-40a1-b63b-195cbdc2e0ab/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RDOMMUGB%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T051551Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjED0aCXVzLXdlc3QtMiJHMEUCIQDXm46pXRDjj1oyTs9SGWNs0W4m3GP6hXqekqQlqmgAFQIgFyHuoVutoHn60oqRMz4W2g8gINZKAdEOjileuPoUivMq%2FwMIVhAAGgw2Mzc0MjMxODM4MDUiDPDx1EZB1Cnnig946CrcA1LA0ENeJ3Z3R%2F17D0NO5562f8JI%2F4C7PvYpKRigfenpngKAal8meS9pfSMrhZTOB3jgCv1sND5CsM5pkfKf9VK52WAiKN7d9MQtb%2BZhPKb6O9RC6GrHNz6kyG02VEopMlMro6FoP9eoBhkhUT6dTOSPRBnpWokeJvQcm2TAmTm8owl%2BDVu96rcyUWFhIwMH%2B3lRWV%2Brm%2BJhnNm5aaLxsMv%2B4Rs63wn8eTPTwMrWBsCKrlWqNRVvmz%2ForyedGTDixzXvdqtTPxxqkMO3dIMqeW203XuAJbNQ40j4Aa%2BleC6ndz438HAe6aVRNg8HkowRmB3jAdkkqwbnlwjCeiOaWTZJvUjkIuPLTpZ87wGVWw%2FrQRm3smrWZqyU7xri%2Bz2buW2l9PYpUNLf1EHkXt11weHcNo6ErLesyty7FezqBCW6tUtbWlc5jtD%2BbjlYfdBPaydhS9nnDoW2ntPNcZWYe2D%2BNwqOIY6N53%2BXu3u2bx7fEmnB3mcQZgvCk7hvJzl0uYOlzPW%2BUHH5Hnx0BIIC5P3HYh2TCjKhfIajkY8%2BXV4FOngI8cnADZ6mb%2BLnPUk5%2FwWqGGl9uKhCl4fe9mT%2BHd3bZ%2FSSDfOgzZ%2FDwXJBLktMl8QoEHuZxVzO2OfcMN37kL0GOqUBOqjYaM4CafV1j6C2fap5Xcifw8qTguGmhQtnqQDU5VapeiK4kv30NSSt%2F%2BjJfomZJPIRBzxc4VVnveDWmASS7hmSiogNsDe5mWZwyjVtA2VyWhTdsHh61D3hWgnseO%2BloTBQ07eoajpHdWn8lcQlwiTE6Em8%2BNjTibFB5QbDY1LwRun%2BQKKdO0G8Ve64peXz3kNOMSqti5xMWGqmOIKj5dRu5G4R&X-Amz-Signature=a489beb03165247f56e467bb8642a6cbc53dd0590f712a059dcbcda8d40bb22c&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ab5a6dfe-51f5-43ee-bcb3-33dae4a1c7ad/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RDOMMUGB%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T051551Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjED0aCXVzLXdlc3QtMiJHMEUCIQDXm46pXRDjj1oyTs9SGWNs0W4m3GP6hXqekqQlqmgAFQIgFyHuoVutoHn60oqRMz4W2g8gINZKAdEOjileuPoUivMq%2FwMIVhAAGgw2Mzc0MjMxODM4MDUiDPDx1EZB1Cnnig946CrcA1LA0ENeJ3Z3R%2F17D0NO5562f8JI%2F4C7PvYpKRigfenpngKAal8meS9pfSMrhZTOB3jgCv1sND5CsM5pkfKf9VK52WAiKN7d9MQtb%2BZhPKb6O9RC6GrHNz6kyG02VEopMlMro6FoP9eoBhkhUT6dTOSPRBnpWokeJvQcm2TAmTm8owl%2BDVu96rcyUWFhIwMH%2B3lRWV%2Brm%2BJhnNm5aaLxsMv%2B4Rs63wn8eTPTwMrWBsCKrlWqNRVvmz%2ForyedGTDixzXvdqtTPxxqkMO3dIMqeW203XuAJbNQ40j4Aa%2BleC6ndz438HAe6aVRNg8HkowRmB3jAdkkqwbnlwjCeiOaWTZJvUjkIuPLTpZ87wGVWw%2FrQRm3smrWZqyU7xri%2Bz2buW2l9PYpUNLf1EHkXt11weHcNo6ErLesyty7FezqBCW6tUtbWlc5jtD%2BbjlYfdBPaydhS9nnDoW2ntPNcZWYe2D%2BNwqOIY6N53%2BXu3u2bx7fEmnB3mcQZgvCk7hvJzl0uYOlzPW%2BUHH5Hnx0BIIC5P3HYh2TCjKhfIajkY8%2BXV4FOngI8cnADZ6mb%2BLnPUk5%2FwWqGGl9uKhCl4fe9mT%2BHd3bZ%2FSSDfOgzZ%2FDwXJBLktMl8QoEHuZxVzO2OfcMN37kL0GOqUBOqjYaM4CafV1j6C2fap5Xcifw8qTguGmhQtnqQDU5VapeiK4kv30NSSt%2F%2BjJfomZJPIRBzxc4VVnveDWmASS7hmSiogNsDe5mWZwyjVtA2VyWhTdsHh61D3hWgnseO%2BloTBQ07eoajpHdWn8lcQlwiTE6Em8%2BNjTibFB5QbDY1LwRun%2BQKKdO0G8Ve64peXz3kNOMSqti5xMWGqmOIKj5dRu5G4R&X-Amz-Signature=529b54411fd7e6196e62939c9b24436256f13900f7e1a2444bd5c33fd3b31dfa&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8f1b1d60-cf1b-42b3-9faa-f634c89c3f84/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RDOMMUGB%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T051551Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjED0aCXVzLXdlc3QtMiJHMEUCIQDXm46pXRDjj1oyTs9SGWNs0W4m3GP6hXqekqQlqmgAFQIgFyHuoVutoHn60oqRMz4W2g8gINZKAdEOjileuPoUivMq%2FwMIVhAAGgw2Mzc0MjMxODM4MDUiDPDx1EZB1Cnnig946CrcA1LA0ENeJ3Z3R%2F17D0NO5562f8JI%2F4C7PvYpKRigfenpngKAal8meS9pfSMrhZTOB3jgCv1sND5CsM5pkfKf9VK52WAiKN7d9MQtb%2BZhPKb6O9RC6GrHNz6kyG02VEopMlMro6FoP9eoBhkhUT6dTOSPRBnpWokeJvQcm2TAmTm8owl%2BDVu96rcyUWFhIwMH%2B3lRWV%2Brm%2BJhnNm5aaLxsMv%2B4Rs63wn8eTPTwMrWBsCKrlWqNRVvmz%2ForyedGTDixzXvdqtTPxxqkMO3dIMqeW203XuAJbNQ40j4Aa%2BleC6ndz438HAe6aVRNg8HkowRmB3jAdkkqwbnlwjCeiOaWTZJvUjkIuPLTpZ87wGVWw%2FrQRm3smrWZqyU7xri%2Bz2buW2l9PYpUNLf1EHkXt11weHcNo6ErLesyty7FezqBCW6tUtbWlc5jtD%2BbjlYfdBPaydhS9nnDoW2ntPNcZWYe2D%2BNwqOIY6N53%2BXu3u2bx7fEmnB3mcQZgvCk7hvJzl0uYOlzPW%2BUHH5Hnx0BIIC5P3HYh2TCjKhfIajkY8%2BXV4FOngI8cnADZ6mb%2BLnPUk5%2FwWqGGl9uKhCl4fe9mT%2BHd3bZ%2FSSDfOgzZ%2FDwXJBLktMl8QoEHuZxVzO2OfcMN37kL0GOqUBOqjYaM4CafV1j6C2fap5Xcifw8qTguGmhQtnqQDU5VapeiK4kv30NSSt%2F%2BjJfomZJPIRBzxc4VVnveDWmASS7hmSiogNsDe5mWZwyjVtA2VyWhTdsHh61D3hWgnseO%2BloTBQ07eoajpHdWn8lcQlwiTE6Em8%2BNjTibFB5QbDY1LwRun%2BQKKdO0G8Ve64peXz3kNOMSqti5xMWGqmOIKj5dRu5G4R&X-Amz-Signature=d9f9f623846f18423032b97dde66b08e65a2e693f090cf544da3c0ccf62bef03&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/13ad0497-05fe-4eaa-984e-707b33e14761/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RDOMMUGB%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T051551Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjED0aCXVzLXdlc3QtMiJHMEUCIQDXm46pXRDjj1oyTs9SGWNs0W4m3GP6hXqekqQlqmgAFQIgFyHuoVutoHn60oqRMz4W2g8gINZKAdEOjileuPoUivMq%2FwMIVhAAGgw2Mzc0MjMxODM4MDUiDPDx1EZB1Cnnig946CrcA1LA0ENeJ3Z3R%2F17D0NO5562f8JI%2F4C7PvYpKRigfenpngKAal8meS9pfSMrhZTOB3jgCv1sND5CsM5pkfKf9VK52WAiKN7d9MQtb%2BZhPKb6O9RC6GrHNz6kyG02VEopMlMro6FoP9eoBhkhUT6dTOSPRBnpWokeJvQcm2TAmTm8owl%2BDVu96rcyUWFhIwMH%2B3lRWV%2Brm%2BJhnNm5aaLxsMv%2B4Rs63wn8eTPTwMrWBsCKrlWqNRVvmz%2ForyedGTDixzXvdqtTPxxqkMO3dIMqeW203XuAJbNQ40j4Aa%2BleC6ndz438HAe6aVRNg8HkowRmB3jAdkkqwbnlwjCeiOaWTZJvUjkIuPLTpZ87wGVWw%2FrQRm3smrWZqyU7xri%2Bz2buW2l9PYpUNLf1EHkXt11weHcNo6ErLesyty7FezqBCW6tUtbWlc5jtD%2BbjlYfdBPaydhS9nnDoW2ntPNcZWYe2D%2BNwqOIY6N53%2BXu3u2bx7fEmnB3mcQZgvCk7hvJzl0uYOlzPW%2BUHH5Hnx0BIIC5P3HYh2TCjKhfIajkY8%2BXV4FOngI8cnADZ6mb%2BLnPUk5%2FwWqGGl9uKhCl4fe9mT%2BHd3bZ%2FSSDfOgzZ%2FDwXJBLktMl8QoEHuZxVzO2OfcMN37kL0GOqUBOqjYaM4CafV1j6C2fap5Xcifw8qTguGmhQtnqQDU5VapeiK4kv30NSSt%2F%2BjJfomZJPIRBzxc4VVnveDWmASS7hmSiogNsDe5mWZwyjVtA2VyWhTdsHh61D3hWgnseO%2BloTBQ07eoajpHdWn8lcQlwiTE6Em8%2BNjTibFB5QbDY1LwRun%2BQKKdO0G8Ve64peXz3kNOMSqti5xMWGqmOIKj5dRu5G4R&X-Amz-Signature=e58c0894b08155d747a8b63c0a27597ab20d2b1c11ea44c2f9343841826eed53&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 2. Box and Whisker Plot
A box plot shows the distribution of quantitative data in a way that facilitates comparisons between variables or across levels of a categorical variable. The box shows the quartiles of the dataset while the whiskers extend to show the rest of the distribution, except for points that are determined to be "outliers".
**Syntax:**
```python
sns.boxplot(x='header_1', y='header_2', data=df)
```
**Example Output:**


![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d207ae92-0a7c-4e2f-aa65-0ee5a2c33bf7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662KDEOFF2%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T051552Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjED0aCXVzLXdlc3QtMiJHMEUCIQCYivSBAGzRXA9BhM8qtvE%2Bjz6oPBQQNtvp%2BrhN9gNLcAIgVB3xt4NAdf3rRsuiWUxNkS4jy4zCMpyZg0EBHviFqPYq%2FwMIVhAAGgw2Mzc0MjMxODM4MDUiDCCP76hPeMPczjhH1SrcAwtx6MivFzVpgYRyapIeoFWsWzEtqcHQL9gFPXkT0h3465m5IPR3BzsgC%2F6whBPOIdercv%2BTRpTRO6pAr8Q2hUqXOsIajQaZinJOIXosJuqlhxvEHr3elWrCBZcarRTOFMAUeYyXFO3unKDNgmYum%2Fj9Jv3zVoVy6P9n8aDbcCB8sVWhReulJDf2fDjrfKW0eS52uH%2FaWTJTa9OK7dNBxA%2F0fmlV2e9yw6OHJQlfpC%2BkPKlkiVDwTAFnMZJl3jHfoXhTGaZ23d6SvnG%2BYYtOJgPitLGGeUpckuc%2BeUy551iBkHyQ8pWBQMkv%2F31vAbeur%2BGxMsGgWfsJrJL98cjZrjuw4QeE042vgGaK%2F345s1GZIwWENCKC7LZPevawGEK4XpLIeuyCJpC3CInvfR8MzXGZI5r%2FEKa%2FQ27qJcAlaNrGun69uUff7UfVghysrhfaHNZ%2BVQnAZ%2Fu80wbC0Mc%2BGluvn5a6O8cjlJDjihYbadiIB%2FTxL%2FvAnjr9pNNx1mIiVUUbhTibAyVDj4bgiHjOWqzE2TML2h3Bz3Zg4rtYuFy3hLKc8I42Uwoc9MXrijYt8y%2Bpz9rCmrbITIPzmovXUM8ckoSVBMzeJCjxF9DTXd0OlEJxatpHdsLbIYaxMPj7kL0GOqUBYbCjBwF8Vd1xv7X%2FA9stnAsw6y0iFxbVzXNIzOJIKA7QJFWt2CGRu1PWWqDkAnsLuazrZphhP8zpLe5O14kHdNuOT8zjRKLdbmdzUB1LVvJQLd89fERkr1g%2FetO6IqL4i82oCxBOYErFP9xTKIEzSk31Ze6hX%2BbbO96lg3%2FwL0NlAOOe9vEGN4Nl641r7cL7Xqfi%2Fzm6Wttquzg4c8omLEybg9Ec&X-Amz-Signature=d854292a526f0a052d46c0081eb59533a012e5ea83077c151ace4d618055fc60&X-Amz-SignedHeaders=host&x-id=GetObject)

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0e516edc-7551-4792-ab18-0494db3c4c0c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664VMEKYQT%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T051552Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjED0aCXVzLXdlc3QtMiJGMEQCIEdSyfmdov6wRC8vH8vjGI6VsvoMkhv0R78GC66xwFSQAiAqbeQRVzHGA%2B95pJwcHPq2uaQavAz3epd4oM3hzZN%2FWCr%2FAwhWEAAaDDYzNzQyMzE4MzgwNSIMAT31b4fYhxilRz5DKtwDk0Lu5%2BxkUa2y2PbWlroU0HOqeXXIfVgbF0pSrmaTX%2B%2B4G8WZvb7KSr%2FDvTpbRkj8joGPlsGG6GhhfFsKkHQ8m4cPBIdu5f7P7%2BC7hnJYujahDFxLj7NSXU2BFlkc7ylrNsJdtCnkVa%2BKZ0hkQ%2FdgzpDSs900ij5IaX6ZPHQGBiQlsZzUvrqOkTcEOWhl2ygiTPQAFvHlGp0cIvNkHxeMNKNf1%2B%2BbPWJdGXUFJ7EvZZYCoAEMkbV95Zi9AKU%2FPAH%2B4S9VYnnQtxhjsl5ts1KC1EKIr5aqir2%2FnT4DGWVBepBkdGMQw72jlWC1CWWKj%2F0bp4wZLVe%2FJ00YLTBAl7M0HN%2Fe%2BsxdFfLeEf9HCvHVksVpV%2BefuQinN0mM%2BhYLtmDb35W2ZgmPZWOH0YhQ8%2FHzK%2FgMTHsOFdU9sNmFsmqFj7ph9NJXrcrZquk7GoUcIsYtLX6Ma%2BeO15jEQRwsY%2B56pzq3nFhWMhUyqVn3GapBX%2F1roxLdiGrWqRLmxqzw6O1B%2BvcQWgzoc92JvKrbFSSYxY22gUvztY6NyueG1TKnUxr%2BZuF3lc3udx14TGwYfAYPsSxpAYsGxfuKjH%2FL2yPFssVG9%2BH0hiObx70C7wXuBWP8eUux4Tg67smFhNow8vuQvQY6pgGhJySBHSf9lKJR7yg2Ir3iVkEoGvRdfAkHlv6iU1mYUwuawU22jFXPm%2B%2B1ByhtsLjSGJbNAFdlJXbCN8NOXnRBTy6rTcxomr0FEf15nEPFcrLi%2FQzuvBsxx0savO5uKtHLQYeSaC3FvGikrhhCvitZFvvy5g%2FYQvtiN1PlNphwEuoATYiLYEdKpaEfuAnf7fUqKsJjL%2FgZiIDbeGrlE%2BvB8%2FfJk%2BKH&X-Amz-Signature=262247d471d840f60495e652d6858848e0d20501d457d529cbddca219d5a244b&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23a79b9d-2356-49a9-8fd9-65c6b0ab2cc5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RDOMMUGB%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T051551Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjED0aCXVzLXdlc3QtMiJHMEUCIQDXm46pXRDjj1oyTs9SGWNs0W4m3GP6hXqekqQlqmgAFQIgFyHuoVutoHn60oqRMz4W2g8gINZKAdEOjileuPoUivMq%2FwMIVhAAGgw2Mzc0MjMxODM4MDUiDPDx1EZB1Cnnig946CrcA1LA0ENeJ3Z3R%2F17D0NO5562f8JI%2F4C7PvYpKRigfenpngKAal8meS9pfSMrhZTOB3jgCv1sND5CsM5pkfKf9VK52WAiKN7d9MQtb%2BZhPKb6O9RC6GrHNz6kyG02VEopMlMro6FoP9eoBhkhUT6dTOSPRBnpWokeJvQcm2TAmTm8owl%2BDVu96rcyUWFhIwMH%2B3lRWV%2Brm%2BJhnNm5aaLxsMv%2B4Rs63wn8eTPTwMrWBsCKrlWqNRVvmz%2ForyedGTDixzXvdqtTPxxqkMO3dIMqeW203XuAJbNQ40j4Aa%2BleC6ndz438HAe6aVRNg8HkowRmB3jAdkkqwbnlwjCeiOaWTZJvUjkIuPLTpZ87wGVWw%2FrQRm3smrWZqyU7xri%2Bz2buW2l9PYpUNLf1EHkXt11weHcNo6ErLesyty7FezqBCW6tUtbWlc5jtD%2BbjlYfdBPaydhS9nnDoW2ntPNcZWYe2D%2BNwqOIY6N53%2BXu3u2bx7fEmnB3mcQZgvCk7hvJzl0uYOlzPW%2BUHH5Hnx0BIIC5P3HYh2TCjKhfIajkY8%2BXV4FOngI8cnADZ6mb%2BLnPUk5%2FwWqGGl9uKhCl4fe9mT%2BHd3bZ%2FSSDfOgzZ%2FDwXJBLktMl8QoEHuZxVzO2OfcMN37kL0GOqUBOqjYaM4CafV1j6C2fap5Xcifw8qTguGmhQtnqQDU5VapeiK4kv30NSSt%2F%2BjJfomZJPIRBzxc4VVnveDWmASS7hmSiogNsDe5mWZwyjVtA2VyWhTdsHh61D3hWgnseO%2BloTBQ07eoajpHdWn8lcQlwiTE6Em8%2BNjTibFB5QbDY1LwRun%2BQKKdO0G8Ve64peXz3kNOMSqti5xMWGqmOIKj5dRu5G4R&X-Amz-Signature=a857fee69c57137d8e87a95c532898992758edcc9a0634f4db4b5f799cf0cf86&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 4. KDE Plot
A Kernel Density Estimate (KDE) plot is a graph that creates a probability distribution curve for the data based upon its likelihood of occurrence on a specific value. This is created for a single vector of information.
**Syntax:**
```python
sns.kdeplot(X) || sns.kdeplot(df['age'])
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0d571213-2a2f-4921-a50b-880847aa05ee/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RDOMMUGB%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T051551Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjED0aCXVzLXdlc3QtMiJHMEUCIQDXm46pXRDjj1oyTs9SGWNs0W4m3GP6hXqekqQlqmgAFQIgFyHuoVutoHn60oqRMz4W2g8gINZKAdEOjileuPoUivMq%2FwMIVhAAGgw2Mzc0MjMxODM4MDUiDPDx1EZB1Cnnig946CrcA1LA0ENeJ3Z3R%2F17D0NO5562f8JI%2F4C7PvYpKRigfenpngKAal8meS9pfSMrhZTOB3jgCv1sND5CsM5pkfKf9VK52WAiKN7d9MQtb%2BZhPKb6O9RC6GrHNz6kyG02VEopMlMro6FoP9eoBhkhUT6dTOSPRBnpWokeJvQcm2TAmTm8owl%2BDVu96rcyUWFhIwMH%2B3lRWV%2Brm%2BJhnNm5aaLxsMv%2B4Rs63wn8eTPTwMrWBsCKrlWqNRVvmz%2ForyedGTDixzXvdqtTPxxqkMO3dIMqeW203XuAJbNQ40j4Aa%2BleC6ndz438HAe6aVRNg8HkowRmB3jAdkkqwbnlwjCeiOaWTZJvUjkIuPLTpZ87wGVWw%2FrQRm3smrWZqyU7xri%2Bz2buW2l9PYpUNLf1EHkXt11weHcNo6ErLesyty7FezqBCW6tUtbWlc5jtD%2BbjlYfdBPaydhS9nnDoW2ntPNcZWYe2D%2BNwqOIY6N53%2BXu3u2bx7fEmnB3mcQZgvCk7hvJzl0uYOlzPW%2BUHH5Hnx0BIIC5P3HYh2TCjKhfIajkY8%2BXV4FOngI8cnADZ6mb%2BLnPUk5%2FwWqGGl9uKhCl4fe9mT%2BHd3bZ%2FSSDfOgzZ%2FDwXJBLktMl8QoEHuZxVzO2OfcMN37kL0GOqUBOqjYaM4CafV1j6C2fap5Xcifw8qTguGmhQtnqQDU5VapeiK4kv30NSSt%2F%2BjJfomZJPIRBzxc4VVnveDWmASS7hmSiogNsDe5mWZwyjVtA2VyWhTdsHh61D3hWgnseO%2BloTBQ07eoajpHdWn8lcQlwiTE6Em8%2BNjTibFB5QbDY1LwRun%2BQKKdO0G8Ve64peXz3kNOMSqti5xMWGqmOIKj5dRu5G4R&X-Amz-Signature=07586dfde85d3e2f05bb946ea7fb51fc0818eb4d1f90dcffc0f0cd980fb57ad6&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/53752550-ef82-4ca9-a01a-09921f0282d0/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RDOMMUGB%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T051551Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjED0aCXVzLXdlc3QtMiJHMEUCIQDXm46pXRDjj1oyTs9SGWNs0W4m3GP6hXqekqQlqmgAFQIgFyHuoVutoHn60oqRMz4W2g8gINZKAdEOjileuPoUivMq%2FwMIVhAAGgw2Mzc0MjMxODM4MDUiDPDx1EZB1Cnnig946CrcA1LA0ENeJ3Z3R%2F17D0NO5562f8JI%2F4C7PvYpKRigfenpngKAal8meS9pfSMrhZTOB3jgCv1sND5CsM5pkfKf9VK52WAiKN7d9MQtb%2BZhPKb6O9RC6GrHNz6kyG02VEopMlMro6FoP9eoBhkhUT6dTOSPRBnpWokeJvQcm2TAmTm8owl%2BDVu96rcyUWFhIwMH%2B3lRWV%2Brm%2BJhnNm5aaLxsMv%2B4Rs63wn8eTPTwMrWBsCKrlWqNRVvmz%2ForyedGTDixzXvdqtTPxxqkMO3dIMqeW203XuAJbNQ40j4Aa%2BleC6ndz438HAe6aVRNg8HkowRmB3jAdkkqwbnlwjCeiOaWTZJvUjkIuPLTpZ87wGVWw%2FrQRm3smrWZqyU7xri%2Bz2buW2l9PYpUNLf1EHkXt11weHcNo6ErLesyty7FezqBCW6tUtbWlc5jtD%2BbjlYfdBPaydhS9nnDoW2ntPNcZWYe2D%2BNwqOIY6N53%2BXu3u2bx7fEmnB3mcQZgvCk7hvJzl0uYOlzPW%2BUHH5Hnx0BIIC5P3HYh2TCjKhfIajkY8%2BXV4FOngI8cnADZ6mb%2BLnPUk5%2FwWqGGl9uKhCl4fe9mT%2BHd3bZ%2FSSDfOgzZ%2FDwXJBLktMl8QoEHuZxVzO2OfcMN37kL0GOqUBOqjYaM4CafV1j6C2fap5Xcifw8qTguGmhQtnqQDU5VapeiK4kv30NSSt%2F%2BjJfomZJPIRBzxc4VVnveDWmASS7hmSiogNsDe5mWZwyjVtA2VyWhTdsHh61D3hWgnseO%2BloTBQ07eoajpHdWn8lcQlwiTE6Em8%2BNjTibFB5QbDY1LwRun%2BQKKdO0G8Ve64peXz3kNOMSqti5xMWGqmOIKj5dRu5G4R&X-Amz-Signature=4b929c68c8aaaea52736d6bea95a1c0c5a5f662c53f8d93e36a9731801927ceb&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
## 4. Correlation Between Variables
Correlation is a statistical measure of the extent to which different variables are interdependent. It indicates how changes in one variable are associated with changes in another variable over time.
### Positive Correlation
Positive correlation indicates that as one variable increases, the other variable also tends to increase.
**Example: Engine Size and Price**
- **Positive Correlation:** Engine size increases, price also increases.
- **Visualization:** Scatter plot with a steep positive slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c7ea9b0-3ef3-4357-a9c3-554fc71b6b15/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SXHSFXL3%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T051552Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjED0aCXVzLXdlc3QtMiJHMEUCIF7VmfsvTs8QWKdEQeWSz4cnAEO2UPp99hl%2FvhRhkp9BAiEAiOX4NT9ZV%2F823WZH8Zr8MuQXcEAMRdpEBxktMumjexUq%2FwMIVhAAGgw2Mzc0MjMxODM4MDUiDM%2BYT39KkK9plFXCPSrcA%2BN3EMn%2BOEQvRIgn%2FKK6DFAX10OX0273Efeg1%2FSbCyAan8lAf5xGMvqoH88%2BOYmmKnxAV3%2FRYylekUprGrPIzgPWWFcL58%2FaPvtULJjV1YUFelZGgM8nNvGu%2BscTr97dSZiOnfgTqWUDFM0J229nyYCsQ9SJrsGENl8r9rR8rtn0sNDwhZxwRw53smd3rnX6PtOzTllBYKwPF0feVqkyFbywmpcaUzZTiavR%2BWHhInp81uXRNg3gqu%2F00STj2eqlqfTNT6cTD%2F3KkCdKdBTELVKl%2FCKADeM0Bw6LZqQ2M17YuL49%2Bxj5P5zLRL%2BfOUxTqTV%2Fd7Ps7%2F4Rk0ZaJ3ueu04mfyrsSbLpkT7aXjkTo0rAKwmoY6q4z1CkMPzqGHgTgpGB7rD7qz%2Bn6NOexUaAeLOQIeruv7hhEUw%2FoQmL5EdqTsRPGtYd7Nqfpqhdp6twGlQF8XhNsqpakogjg%2BrLV2oak0K0CKD5hN%2B9h9WV%2Fzg63cj4pbeYXym6yTwoWwqxhIRByYIu%2FFoILMezJgwhKeEF4MdpvpQFoRN996Gy3nzamznl%2F1Sga85Kzcn7aMU2z%2FBPzCWN1xruSLZbUIdsLyHxye2ULF5fd5PtR6dtPdu3VXE0LjUD5JzCrecCMJv8kL0GOqUBeQ1r0HDy0cd8TRoTty4K%2B2bJvLo0C3k%2BXifvOQdEr0gS3JN1uyRE3ow33lS4Id6OSNcVMGhZNTPmptUQYb0nbPHpfH3Cbycmc3Uig17RIEImNrLsei20e5n3YnQW8ClFawb27WOZtjA6PDRyY4%2BY0fadoAV%2B2Js4V9p3Ak0RxhOgRQsriBIKN3UX4eHwvOHi%2B7m%2B6%2Ft4TfVMUrpvodMCerLMJ%2FoV&X-Amz-Signature=bf02ae3e62e7a9ec526bba3781aa291ea9637d0867b379d3273d766b8ed9c731&X-Amz-SignedHeaders=host&x-id=GetObject)
**Explanation:** When engine size increases, there is a corresponding increase in the price of the vehicle. This positive correlation suggests that larger engines tend to be associated with higher prices in the market.
___
### Negative Correlation
Negative correlation indicates that as one variable increases, the other variable tends to decrease.
**Example: Highway Miles per Gallon and Price**
- **Negative Correlation:** As highway miles per gallon increases, price decreases.
- **Visualization:** Scatter plot with a steep negative slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/10f1f798-9cc4-4df2-a9c1-5a339f554a0b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TJ3ILGMB%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T051552Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjED0aCXVzLXdlc3QtMiJGMEQCIGesBOTqT1xyTLFxR1OM%2FCHb2XEijTQRHWHcXIY2XqzVAiBE7szJRY7BJH2vP6Y5z6K6bb3xjBN5wlFo0G9Qg6PWEir%2FAwhWEAAaDDYzNzQyMzE4MzgwNSIMD%2FMjqTPlhn0BA5JfKtwDIOR%2Fm5dTmH0LhXm7%2BZBm1GCoxYVajiXbyeB0CblhWJvo%2FQnywcak7zKDL5pQS%2F%2BxowLd0GwisGtylstHByjPCL%2BO88YF201jfnldn6XnwoL0BC11BC%2BMYNRrzlYzxCdoQ8oyvhJmBIOpYlfkjthB45uPI1%2BGIbewYOcOrqdjxexYR1uzKPEICHK%2BvDHVJCJHJMv8BNtQ7iyXi%2BNzEvRl3jY6%2B2P3w9x%2F5Hc97tBDo7hilCkjx3ByjOZvQFmpvfydmK8vqu5SYhWSs0goSQQcoFjTFgOJQ%2BtTEDILW2diGx1b2UUxgITn%2FD2%2Fj1W8wb%2BKBZhmjqh7aNYRZzoS0iYdM1w9wMs7ONwaz0LuT1PAwnK1zPq6VsVheedT%2F8bjPzzLtqCjfm%2BYbpwXHVWsmyYaO32VLTPCVAtIegnQAz%2F6tfnbjSw04Ot22KsHabVbIREN94IIz9x4KStneDqBVcrU3LgmP93%2F%2FiubaExd6a77dFsYUQkW%2F3trjZ9v89PmCr1GW8xDe0qeqVZyJ3HA5sU42mdz46kPtR7L82wCNGqLGtT1WATB8cuUSTCLMahWZMbDpzAVrbKTSlYbndWcCrVT2xzgsuqqnsuHbSXnHt3f4EB81l190FdT4crJPxwwmvyQvQY6pgHVubF9mLZitQ%2FRwMyUuI7PVEbxRlLZaXcZ3G2sPwB6xqOcMZPFTlkblUf9TnntrhjsRTtXhSb%2B04eW5FE5MzmD7Hq6b9wn7AC%2FDZxbcj6la1ANr5DeGz9kWAJkE3y%2BWdrBOVZ13zYqgzOqMW69bZYNWjSC8Hd1EweRortajGeRWnuKuPLFBSPIW4DigG%2FLXlX6fhdWPCgpS4W83si45KQY5W6iZRJr&X-Amz-Signature=de35f6f6f4eb58eeb1e7c5c0d005e3ac20aab5d0fd909c9c766d79e6461da5f3&X-Amz-SignedHeaders=host&x-id=GetObject)
**Explanation:** When highway miles per gallon increases, the price of the vehicle tends to decrease. This negative correlation suggests that cars with higher fuel efficiency (more miles per gallon) are generally priced lower in the market.
___
### Weak Correlation
Weak correlation indicates a lack of strong relationship between the variables.
**Example: RPM and Price**
- **Weak Correlation:** Low and high RPM values show varied prices, indicating no strong predictive relationship.
- **Visualization:** Scatter plot with no clear trend or slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9f914514-8914-4bf4-ac84-d9e3077f6eb1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466U5B462XS%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T051552Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjED0aCXVzLXdlc3QtMiJHMEUCICm8fdkXN1ZYcREaoSYkDTlJQsq0dgPBgfp5oSKfbT6nAiEAvbWGBguXcbFBVTZzp5ws3Lmz%2BIK4v97Vi3097tuzB4wq%2FwMIVhAAGgw2Mzc0MjMxODM4MDUiDAnpNRnb9jjDpDASmircA16vQkRIjFtdF3faQG9s2ZMh1ovtuooG7epf%2FldLl86NsJdtVoSQ0gxu2gTuEckQS0yvNsZAH3UMU20jnqcnrJ7OyQvMSCiH8ZF95k0AlOmAHApnKVXCRid1gnbNE9kq%2FV1LAdaKxVuvtSJ0D1rtcElXu7FzM5wUwewo427sE2zF9AbsP%2FxBAVWhUwO1NXG89ISGXtUFKP%2Bx6behMI25EHxEYDj%2BOx5hw%2FLGgUoarhKJx5zcaiMEllPHWf0cjmkYQGPIiEFIEt47rOYMVw4OjLkbUGN3HumzkDkgiCCyvk58flHcWxtf4EJVvDk2yLKFGRXy2Ty5If0Q0HiXB%2BN5aKTWvlrwn8zTz%2F%2FgS5kN7LO6prIzbOKUr5wpKG8vRv%2FqdkAYvJTrd6A8HOAwvYgV9h5TIAYzdbPJybkRxX5HtBt5cwrZBabw4QEiWMvy0GQgLvt5iGaObWQw7lKSGAl393Q8KHjcFU0gas0MOyU%2BPuQBr3AKj97IWdeojqAZvfY94dIC57L%2B4MOPdNF1uSyJrefuFSRI%2FBUrmp8W2wcfzueZSL4lQWylds2pvo%2B9uXDcYZ77Vag0uXusc8VhcUliWwMTA2s65VqcfLgfNsBorzyJhYIb5794sWV1fBgvMJb8kL0GOqUBpt%2FGMPW6%2FIkGkQqsWeYqFUwG9emiwEE3YuWNLOLWoMhi41b6Wy5Ld5G%2FVRpJY8sKrpUSsyyaSXKZIUgKti6Hk3kAIFN0Knkp%2B1OLAEcXnOc7y%2Bp%2B0l1b7pkygIvbDH4PYvSofWKjUEtvLa6Yy54joZyoVmkNH2pU0hArGZVlw5LP9f1i8xbg10B9KPidBgah34lso%2FEF6mI8OXCj5luSPMdQT%2BQt&X-Amz-Signature=f087c611d76f3296d4210f0684fbd67ece2be67d5e6ed72a18062f2ce238d3d5&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f18086e5-5b04-4fbf-8309-8944ab20d213/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664MDFSGQA%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T051552Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjED0aCXVzLXdlc3QtMiJHMEUCICVRD7CSdLPCGF2hPoBMBic0WxiPoSBsr3yrsGJ%2FFUuxAiEA7vCizWpi0RcIcNx3EMN2p5p0LtLA3NFG1FapAC3snUcq%2FwMIVhAAGgw2Mzc0MjMxODM4MDUiDC8oefML0ZAhsYDRfSrcAzd8GgAaPxEoSfpj3Qzyd7d7MkywY8CHCheqORKNRbp2hw%2Byg1j48swhhYqPhOjHEzf1Yn%2BY2ZMbJ3illzXbFJCvsjYjHVl%2BcajXPQBps0CPXVDtDP8aFqTSw7AF7hr2m0EferEpShgqnqffUsUZRFlHlEznToqDUT1eSaq70tcqgfrvvNxX6168V08GcsLTe30pb8kdeD8nHv4%2F39TFLxAwMLDBVS%2BJXMFpx4a%2FAT9TJnUMPqkYVHN8pahDIDA%2B4wy7bNyV2i2vUx4KQx0wvCibX69%2BGXh54hWAYWQfYos9nng4G0jgY4ENf8Xml5TH2VMCHSnbc7Jgg0OCc8RthkgvB%2F5riHvLqpGd63DGL%2FrK4VjxnBSPjM0bbctZytNilK%2F6VJrnyTVptu%2BQTg27HsNXP2cGQvMenoSnjFBjEsoKnS2B54o5y61K51WCJVdS3elgJM%2FuzZn4Jss%2FAmESSJp3mA%2BW7y%2FLKu%2B4gP5BqoCa41Qr7SYt1PcFPfsKkbeA05rc7WeW8e5z6oItbYwa7Yzx1BVMktEJBWAzbmc3PgeMVydW86g%2BaBR5kNOqW8HPDdSSBaiX4Ot66CL5w3SMCCfSBS6W%2BSjrJEX9R4bUMqQMvojmVf1pt%2Fh9IzBIMJ%2F8kL0GOqUBPAm6gbM00e7%2BJCaMro4Kva2GkdyCTGEd9Kyg5vpNlFuta1YLJYKtEqLZenKfPf%2B0OvWYU0RaD2viYC%2BtvuGB3ZiHs6pEHgjeYW9zJjc84y3g4nVs10f13%2F5PJTrkWiMdCSwh%2F0cZx9cHVaL8BilHIK7QJkIQwMEODWkoalempvESZrPvetD1Rn2TZebxjILJJo%2F9384p5I%2BN4WXIJRMl5Ynu3V0m&X-Amz-Signature=10a088f7f5d3ae2286f97efcedd67dcab231e6222cddd9b3cfe8eb0157d528e7&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Correlation Plot
Heatmap visualizes correlations among variables. Color scheme indicates Pearson correlation coefficients. Dark red diagonal line shows perfect correlation (value of 1) between variables and themselves.
This heatmap offers overview of variable relationships and their link with price.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cd3b341e-cc1a-45f7-8aec-cdc00436d270/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664MDFSGQA%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T051552Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjED0aCXVzLXdlc3QtMiJHMEUCICVRD7CSdLPCGF2hPoBMBic0WxiPoSBsr3yrsGJ%2FFUuxAiEA7vCizWpi0RcIcNx3EMN2p5p0LtLA3NFG1FapAC3snUcq%2FwMIVhAAGgw2Mzc0MjMxODM4MDUiDC8oefML0ZAhsYDRfSrcAzd8GgAaPxEoSfpj3Qzyd7d7MkywY8CHCheqORKNRbp2hw%2Byg1j48swhhYqPhOjHEzf1Yn%2BY2ZMbJ3illzXbFJCvsjYjHVl%2BcajXPQBps0CPXVDtDP8aFqTSw7AF7hr2m0EferEpShgqnqffUsUZRFlHlEznToqDUT1eSaq70tcqgfrvvNxX6168V08GcsLTe30pb8kdeD8nHv4%2F39TFLxAwMLDBVS%2BJXMFpx4a%2FAT9TJnUMPqkYVHN8pahDIDA%2B4wy7bNyV2i2vUx4KQx0wvCibX69%2BGXh54hWAYWQfYos9nng4G0jgY4ENf8Xml5TH2VMCHSnbc7Jgg0OCc8RthkgvB%2F5riHvLqpGd63DGL%2FrK4VjxnBSPjM0bbctZytNilK%2F6VJrnyTVptu%2BQTg27HsNXP2cGQvMenoSnjFBjEsoKnS2B54o5y61K51WCJVdS3elgJM%2FuzZn4Jss%2FAmESSJp3mA%2BW7y%2FLKu%2B4gP5BqoCa41Qr7SYt1PcFPfsKkbeA05rc7WeW8e5z6oItbYwa7Yzx1BVMktEJBWAzbmc3PgeMVydW86g%2BaBR5kNOqW8HPDdSSBaiX4Ot66CL5w3SMCCfSBS6W%2BSjrJEX9R4bUMqQMvojmVf1pt%2Fh9IzBIMJ%2F8kL0GOqUBPAm6gbM00e7%2BJCaMro4Kva2GkdyCTGEd9Kyg5vpNlFuta1YLJYKtEqLZenKfPf%2B0OvWYU0RaD2viYC%2BtvuGB3ZiHs6pEHgjeYW9zJjc84y3g4nVs10f13%2F5PJTrkWiMdCSwh%2F0cZx9cHVaL8BilHIK7QJkIQwMEODWkoalempvESZrPvetD1Rn2TZebxjILJJo%2F9384p5I%2BN4WXIJRMl5Ynu3V0m&X-Amz-Signature=e2317f6b1ad80bc682d2d05f07dcad17262b1008139b87b0853e5d887be07919&X-Amz-SignedHeaders=host&x-id=GetObject)

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
