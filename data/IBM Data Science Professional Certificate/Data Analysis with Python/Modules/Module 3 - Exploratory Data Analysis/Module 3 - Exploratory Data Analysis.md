

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7e6d594d-952e-44b6-97ea-31225882aea6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665CSKYY6O%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T221331Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEL7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQC%2F5umbaDh9N3e8w5TzK%2BHAkEFtlDtCgGza751Xv9h0FAIgQzT9T8keMRXLZrFKlxVpYap70OXVRpVJWkrdKGwtCVcqiAQIx%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDD3ZI1HCB2G9Iwh2DyrcA%2F%2Bwtl3Qm75mhP%2BX9KVwdiOfBYVSRUw0ENi0pnfz8sh67yPCkjo95%2FBBt4naaz4T3wuBruHAPHOm2EdrQwNapJJ69d1SI4QXtOWCYXWzmVT3bmyT70fA%2Fcgq3azTaGZwE2AetbZw61Oihfe9fDBctVGzWjiaWqXejXbziRmfqyy%2BT9mjxYZckoywRbajm0JIzksW3WRTSCiwymSQHNC4zfi0UmLyzGo0oXflBefPV4qD6crbCxpHdGPgl0eN4crB6FrDKUgpx%2FL3jOkpcZ59topkdJrLtUA85zjWhVTE9etIvmP1ksxj3xfeo0wS0wzg4Ms2YJVEQbN2phVcXoxRyjb%2Btv4ojrmTTreJvCmwwhf99RggIQGXtawtZ4VSMpey0WirA24ReU1NFU2nt%2BBXawSdR9KuaVXyDRy4PuGQxap6GGh6spYPC6djBtmPmKC4ZTJwccMIAoi1BcHUy%2BsSgGb%2BJrVwMAAeMTOKGQjBF7680lW6%2FvOupx17%2B6LeZCeuf%2F0mqLa7pHBL8lWhT1uV2DZoSYHVk8BCnXI%2BUYhcjHyZ%2FU%2FPmCYR5%2BPor7C9T5Xt07W8%2Bev2h5bIWgoh8FlslS7%2FZvazdMt3S8aheRjPXco1digi7g5OctGopeprMNSU9bwGOqUBXBl1jvVcsIpWUAAXMjpnEiWRX%2FMuuU7vnGRUJCKf%2F6UCkl1jFsCxLQJGi1E70LENSd9aXdTI82ztCdzXCTX7Ag6tgNP1gBx1i1zL1YxTCSKb9IdiIYVKeFovF94VXQHzzAOCspJ5l%2BYpAa4nqoTm%2BImexUnxK5lgcCRr50CPTwzW2h1iT2XGvYrjx6mLQBj92UPiEKOvGsxZlNn70z63q5h7XHnH&X-Amz-Signature=d451524103c0701b513f005946cc37f8b01bd0cdb570938b09f79df628f89a9f&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cbfaed9e-b398-4902-8936-dea058b21def/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665CSKYY6O%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T221331Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEL7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQC%2F5umbaDh9N3e8w5TzK%2BHAkEFtlDtCgGza751Xv9h0FAIgQzT9T8keMRXLZrFKlxVpYap70OXVRpVJWkrdKGwtCVcqiAQIx%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDD3ZI1HCB2G9Iwh2DyrcA%2F%2Bwtl3Qm75mhP%2BX9KVwdiOfBYVSRUw0ENi0pnfz8sh67yPCkjo95%2FBBt4naaz4T3wuBruHAPHOm2EdrQwNapJJ69d1SI4QXtOWCYXWzmVT3bmyT70fA%2Fcgq3azTaGZwE2AetbZw61Oihfe9fDBctVGzWjiaWqXejXbziRmfqyy%2BT9mjxYZckoywRbajm0JIzksW3WRTSCiwymSQHNC4zfi0UmLyzGo0oXflBefPV4qD6crbCxpHdGPgl0eN4crB6FrDKUgpx%2FL3jOkpcZ59topkdJrLtUA85zjWhVTE9etIvmP1ksxj3xfeo0wS0wzg4Ms2YJVEQbN2phVcXoxRyjb%2Btv4ojrmTTreJvCmwwhf99RggIQGXtawtZ4VSMpey0WirA24ReU1NFU2nt%2BBXawSdR9KuaVXyDRy4PuGQxap6GGh6spYPC6djBtmPmKC4ZTJwccMIAoi1BcHUy%2BsSgGb%2BJrVwMAAeMTOKGQjBF7680lW6%2FvOupx17%2B6LeZCeuf%2F0mqLa7pHBL8lWhT1uV2DZoSYHVk8BCnXI%2BUYhcjHyZ%2FU%2FPmCYR5%2BPor7C9T5Xt07W8%2Bev2h5bIWgoh8FlslS7%2FZvazdMt3S8aheRjPXco1digi7g5OctGopeprMNSU9bwGOqUBXBl1jvVcsIpWUAAXMjpnEiWRX%2FMuuU7vnGRUJCKf%2F6UCkl1jFsCxLQJGi1E70LENSd9aXdTI82ztCdzXCTX7Ag6tgNP1gBx1i1zL1YxTCSKb9IdiIYVKeFovF94VXQHzzAOCspJ5l%2BYpAa4nqoTm%2BImexUnxK5lgcCRr50CPTwzW2h1iT2XGvYrjx6mLQBj92UPiEKOvGsxZlNn70z63q5h7XHnH&X-Amz-Signature=a23488e9dbd8d6d17976f50d41236da154df8688d88ada2adb12c70f23c83e8c&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/91181646-b1e0-4433-9711-6259a96a9247/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665CSKYY6O%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T221331Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEL7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQC%2F5umbaDh9N3e8w5TzK%2BHAkEFtlDtCgGza751Xv9h0FAIgQzT9T8keMRXLZrFKlxVpYap70OXVRpVJWkrdKGwtCVcqiAQIx%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDD3ZI1HCB2G9Iwh2DyrcA%2F%2Bwtl3Qm75mhP%2BX9KVwdiOfBYVSRUw0ENi0pnfz8sh67yPCkjo95%2FBBt4naaz4T3wuBruHAPHOm2EdrQwNapJJ69d1SI4QXtOWCYXWzmVT3bmyT70fA%2Fcgq3azTaGZwE2AetbZw61Oihfe9fDBctVGzWjiaWqXejXbziRmfqyy%2BT9mjxYZckoywRbajm0JIzksW3WRTSCiwymSQHNC4zfi0UmLyzGo0oXflBefPV4qD6crbCxpHdGPgl0eN4crB6FrDKUgpx%2FL3jOkpcZ59topkdJrLtUA85zjWhVTE9etIvmP1ksxj3xfeo0wS0wzg4Ms2YJVEQbN2phVcXoxRyjb%2Btv4ojrmTTreJvCmwwhf99RggIQGXtawtZ4VSMpey0WirA24ReU1NFU2nt%2BBXawSdR9KuaVXyDRy4PuGQxap6GGh6spYPC6djBtmPmKC4ZTJwccMIAoi1BcHUy%2BsSgGb%2BJrVwMAAeMTOKGQjBF7680lW6%2FvOupx17%2B6LeZCeuf%2F0mqLa7pHBL8lWhT1uV2DZoSYHVk8BCnXI%2BUYhcjHyZ%2FU%2FPmCYR5%2BPor7C9T5Xt07W8%2Bev2h5bIWgoh8FlslS7%2FZvazdMt3S8aheRjPXco1digi7g5OctGopeprMNSU9bwGOqUBXBl1jvVcsIpWUAAXMjpnEiWRX%2FMuuU7vnGRUJCKf%2F6UCkl1jFsCxLQJGi1E70LENSd9aXdTI82ztCdzXCTX7Ag6tgNP1gBx1i1zL1YxTCSKb9IdiIYVKeFovF94VXQHzzAOCspJ5l%2BYpAa4nqoTm%2BImexUnxK5lgcCRr50CPTwzW2h1iT2XGvYrjx6mLQBj92UPiEKOvGsxZlNn70z63q5h7XHnH&X-Amz-Signature=0488a1a62cb6c2930b13dbec44cef8c64af18e1ebdc6c3bfb62c45d661a56292&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/09aba1c0-0d55-41dd-852a-a04c5b8a3fac/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TJBXFT5R%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T221332Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEL7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDEKBya64mC6moaj8h394WHoCGuV25gx4amgLO7Vlr2VgIgE7i12lw%2FbePdIBnNCFOAyW59KeNc%2FLOKR9HiBsw5wfMqiAQIx%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDI2rMCf90137jbBOpircA6lFVHDrAVIdHEVMqDiEPmXntWB3luSrKgq7OzOo5ov6IxHrX4TF%2Fp5SvXqTznZyfIu0v702ff7%2FmnlxFrB8fbAcHiBDgXAm8jhubcwVUmomdkgBytJqwNEHrP7nsdYxtpZ%2B573CsPSbnG8wbjrE79CixvCAw%2FJZC9K562DrHw1ifQhV3hm%2B17b%2F6N%2BZibTjCRmyvoII9NNSJkJUcpCSmuVxu5L6To30EFXW2Ud05Bg%2B9cJy5QlpyngfBVc803o71HvzHEWPBx40dWGB8XNtZLuUG7slfkxqcvHjVEjhOtjLgw14XG0YTtL1K13mxoSTdzGeSL87bZjf2MFixEIIh5G%2Fl6ntLvROGgPMnxHDKvbDl73ZCW8sDTgq3xS9mTwBOfywilEEmVQ4C04apDfC9BoFVbtp1zDrEZ5u5XqSW4vSAoa%2FcfIAOpwEpZ4anJzH41Wf%2BkYf7FHdDejmN06H99y1I4jAypIYGiuTQ%2FHBvVx5W02Sn85imZaRwo%2Fac6JBmbsqDWNxdK899WbgM6Szvey4xManA3yOdoal3AIxRUZVP8InABi173ol1NsnxoqFcyLyVu%2FS8u70aXPxnfdhrDIpmpgvZmDWWnFVu%2B1DpCoz0Jp5u3RzND2yvX4nMKuU9bwGOqUB6fjC%2FvL9f8M9yFcFQhnYtVod9Rbo7zSKL7ZKxeVAFrWldy44cTGaBkNvYzpOCZun%2BTbtaT6Cx7FpvNIMUt3w5w8s%2BiRArsmXWIhg9mzkFggudWAvVgiCQW3BpLoAgR3Jj%2B16c8keMdCaFVwh%2FVpdl2dgxHGzY9sxHAVnKnR6dRX%2FRHDTvRJJxdUsTTndVZoOF1t6hEkcfgzjU5wRRYcTt8a2HXIC&X-Amz-Signature=3827bff7c6c4066d15a54ef6872b7906a7e42a1ad652b6217a6a5cbebbc63177&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 2. Scatter Plot
Scatter plots present the relationship between two variables in a dataset. It represents data points on a two-dimensional plane. The independent variable or attribute is plotted on the X-axis, while the dependent variable is plotted on the Y-axis.
**Syntax:**
```python
plt.scatter(x, y)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23708af9-659f-4f23-b626-1a4292d7842c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TJBXFT5R%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T221332Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEL7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDEKBya64mC6moaj8h394WHoCGuV25gx4amgLO7Vlr2VgIgE7i12lw%2FbePdIBnNCFOAyW59KeNc%2FLOKR9HiBsw5wfMqiAQIx%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDI2rMCf90137jbBOpircA6lFVHDrAVIdHEVMqDiEPmXntWB3luSrKgq7OzOo5ov6IxHrX4TF%2Fp5SvXqTznZyfIu0v702ff7%2FmnlxFrB8fbAcHiBDgXAm8jhubcwVUmomdkgBytJqwNEHrP7nsdYxtpZ%2B573CsPSbnG8wbjrE79CixvCAw%2FJZC9K562DrHw1ifQhV3hm%2B17b%2F6N%2BZibTjCRmyvoII9NNSJkJUcpCSmuVxu5L6To30EFXW2Ud05Bg%2B9cJy5QlpyngfBVc803o71HvzHEWPBx40dWGB8XNtZLuUG7slfkxqcvHjVEjhOtjLgw14XG0YTtL1K13mxoSTdzGeSL87bZjf2MFixEIIh5G%2Fl6ntLvROGgPMnxHDKvbDl73ZCW8sDTgq3xS9mTwBOfywilEEmVQ4C04apDfC9BoFVbtp1zDrEZ5u5XqSW4vSAoa%2FcfIAOpwEpZ4anJzH41Wf%2BkYf7FHdDejmN06H99y1I4jAypIYGiuTQ%2FHBvVx5W02Sn85imZaRwo%2Fac6JBmbsqDWNxdK899WbgM6Szvey4xManA3yOdoal3AIxRUZVP8InABi173ol1NsnxoqFcyLyVu%2FS8u70aXPxnfdhrDIpmpgvZmDWWnFVu%2B1DpCoz0Jp5u3RzND2yvX4nMKuU9bwGOqUB6fjC%2FvL9f8M9yFcFQhnYtVod9Rbo7zSKL7ZKxeVAFrWldy44cTGaBkNvYzpOCZun%2BTbtaT6Cx7FpvNIMUt3w5w8s%2BiRArsmXWIhg9mzkFggudWAvVgiCQW3BpLoAgR3Jj%2B16c8keMdCaFVwh%2FVpdl2dgxHGzY9sxHAVnKnR6dRX%2FRHDTvRJJxdUsTTndVZoOF1t6hEkcfgzjU5wRRYcTt8a2HXIC&X-Amz-Signature=c25ef62ed3e283e1df5f2d3f462c0b440c6e9731c3a25bf7971ede12fb517a7e&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 3. Histogram
A histogram is an important visual representation of data in categorical form. To view the data in a "Binned" form, use the histogram plot with a number of bins required or with the data points that mark the bin edges. The x-axis represents the data bins, and the y-axis represents the number of elements in each bin.
**Syntax:**
```python
plt.hist(x, bins)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/24e4424a-df87-40a1-b63b-195cbdc2e0ab/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TJBXFT5R%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T221332Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEL7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDEKBya64mC6moaj8h394WHoCGuV25gx4amgLO7Vlr2VgIgE7i12lw%2FbePdIBnNCFOAyW59KeNc%2FLOKR9HiBsw5wfMqiAQIx%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDI2rMCf90137jbBOpircA6lFVHDrAVIdHEVMqDiEPmXntWB3luSrKgq7OzOo5ov6IxHrX4TF%2Fp5SvXqTznZyfIu0v702ff7%2FmnlxFrB8fbAcHiBDgXAm8jhubcwVUmomdkgBytJqwNEHrP7nsdYxtpZ%2B573CsPSbnG8wbjrE79CixvCAw%2FJZC9K562DrHw1ifQhV3hm%2B17b%2F6N%2BZibTjCRmyvoII9NNSJkJUcpCSmuVxu5L6To30EFXW2Ud05Bg%2B9cJy5QlpyngfBVc803o71HvzHEWPBx40dWGB8XNtZLuUG7slfkxqcvHjVEjhOtjLgw14XG0YTtL1K13mxoSTdzGeSL87bZjf2MFixEIIh5G%2Fl6ntLvROGgPMnxHDKvbDl73ZCW8sDTgq3xS9mTwBOfywilEEmVQ4C04apDfC9BoFVbtp1zDrEZ5u5XqSW4vSAoa%2FcfIAOpwEpZ4anJzH41Wf%2BkYf7FHdDejmN06H99y1I4jAypIYGiuTQ%2FHBvVx5W02Sn85imZaRwo%2Fac6JBmbsqDWNxdK899WbgM6Szvey4xManA3yOdoal3AIxRUZVP8InABi173ol1NsnxoqFcyLyVu%2FS8u70aXPxnfdhrDIpmpgvZmDWWnFVu%2B1DpCoz0Jp5u3RzND2yvX4nMKuU9bwGOqUB6fjC%2FvL9f8M9yFcFQhnYtVod9Rbo7zSKL7ZKxeVAFrWldy44cTGaBkNvYzpOCZun%2BTbtaT6Cx7FpvNIMUt3w5w8s%2BiRArsmXWIhg9mzkFggudWAvVgiCQW3BpLoAgR3Jj%2B16c8keMdCaFVwh%2FVpdl2dgxHGzY9sxHAVnKnR6dRX%2FRHDTvRJJxdUsTTndVZoOF1t6hEkcfgzjU5wRRYcTt8a2HXIC&X-Amz-Signature=22c006b7faf79a0dde257ba0d4c730527427f9026065801d244d85afaaf75414&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ab5a6dfe-51f5-43ee-bcb3-33dae4a1c7ad/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TJBXFT5R%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T221332Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEL7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDEKBya64mC6moaj8h394WHoCGuV25gx4amgLO7Vlr2VgIgE7i12lw%2FbePdIBnNCFOAyW59KeNc%2FLOKR9HiBsw5wfMqiAQIx%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDI2rMCf90137jbBOpircA6lFVHDrAVIdHEVMqDiEPmXntWB3luSrKgq7OzOo5ov6IxHrX4TF%2Fp5SvXqTznZyfIu0v702ff7%2FmnlxFrB8fbAcHiBDgXAm8jhubcwVUmomdkgBytJqwNEHrP7nsdYxtpZ%2B573CsPSbnG8wbjrE79CixvCAw%2FJZC9K562DrHw1ifQhV3hm%2B17b%2F6N%2BZibTjCRmyvoII9NNSJkJUcpCSmuVxu5L6To30EFXW2Ud05Bg%2B9cJy5QlpyngfBVc803o71HvzHEWPBx40dWGB8XNtZLuUG7slfkxqcvHjVEjhOtjLgw14XG0YTtL1K13mxoSTdzGeSL87bZjf2MFixEIIh5G%2Fl6ntLvROGgPMnxHDKvbDl73ZCW8sDTgq3xS9mTwBOfywilEEmVQ4C04apDfC9BoFVbtp1zDrEZ5u5XqSW4vSAoa%2FcfIAOpwEpZ4anJzH41Wf%2BkYf7FHdDejmN06H99y1I4jAypIYGiuTQ%2FHBvVx5W02Sn85imZaRwo%2Fac6JBmbsqDWNxdK899WbgM6Szvey4xManA3yOdoal3AIxRUZVP8InABi173ol1NsnxoqFcyLyVu%2FS8u70aXPxnfdhrDIpmpgvZmDWWnFVu%2B1DpCoz0Jp5u3RzND2yvX4nMKuU9bwGOqUB6fjC%2FvL9f8M9yFcFQhnYtVod9Rbo7zSKL7ZKxeVAFrWldy44cTGaBkNvYzpOCZun%2BTbtaT6Cx7FpvNIMUt3w5w8s%2BiRArsmXWIhg9mzkFggudWAvVgiCQW3BpLoAgR3Jj%2B16c8keMdCaFVwh%2FVpdl2dgxHGzY9sxHAVnKnR6dRX%2FRHDTvRJJxdUsTTndVZoOF1t6hEkcfgzjU5wRRYcTt8a2HXIC&X-Amz-Signature=98693c1dc7ea2cd5ef45cde9145ce3df8c3853b1f3f0765188a829e306687b54&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8f1b1d60-cf1b-42b3-9faa-f634c89c3f84/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TJBXFT5R%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T221332Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEL7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDEKBya64mC6moaj8h394WHoCGuV25gx4amgLO7Vlr2VgIgE7i12lw%2FbePdIBnNCFOAyW59KeNc%2FLOKR9HiBsw5wfMqiAQIx%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDI2rMCf90137jbBOpircA6lFVHDrAVIdHEVMqDiEPmXntWB3luSrKgq7OzOo5ov6IxHrX4TF%2Fp5SvXqTznZyfIu0v702ff7%2FmnlxFrB8fbAcHiBDgXAm8jhubcwVUmomdkgBytJqwNEHrP7nsdYxtpZ%2B573CsPSbnG8wbjrE79CixvCAw%2FJZC9K562DrHw1ifQhV3hm%2B17b%2F6N%2BZibTjCRmyvoII9NNSJkJUcpCSmuVxu5L6To30EFXW2Ud05Bg%2B9cJy5QlpyngfBVc803o71HvzHEWPBx40dWGB8XNtZLuUG7slfkxqcvHjVEjhOtjLgw14XG0YTtL1K13mxoSTdzGeSL87bZjf2MFixEIIh5G%2Fl6ntLvROGgPMnxHDKvbDl73ZCW8sDTgq3xS9mTwBOfywilEEmVQ4C04apDfC9BoFVbtp1zDrEZ5u5XqSW4vSAoa%2FcfIAOpwEpZ4anJzH41Wf%2BkYf7FHdDejmN06H99y1I4jAypIYGiuTQ%2FHBvVx5W02Sn85imZaRwo%2Fac6JBmbsqDWNxdK899WbgM6Szvey4xManA3yOdoal3AIxRUZVP8InABi173ol1NsnxoqFcyLyVu%2FS8u70aXPxnfdhrDIpmpgvZmDWWnFVu%2B1DpCoz0Jp5u3RzND2yvX4nMKuU9bwGOqUB6fjC%2FvL9f8M9yFcFQhnYtVod9Rbo7zSKL7ZKxeVAFrWldy44cTGaBkNvYzpOCZun%2BTbtaT6Cx7FpvNIMUt3w5w8s%2BiRArsmXWIhg9mzkFggudWAvVgiCQW3BpLoAgR3Jj%2B16c8keMdCaFVwh%2FVpdl2dgxHGzY9sxHAVnKnR6dRX%2FRHDTvRJJxdUsTTndVZoOF1t6hEkcfgzjU5wRRYcTt8a2HXIC&X-Amz-Signature=a12dd93ac2776967aeb4967e0146589e5423f432ddf6d4329f2c6d8e13b8bca0&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/13ad0497-05fe-4eaa-984e-707b33e14761/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TJBXFT5R%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T221332Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEL7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDEKBya64mC6moaj8h394WHoCGuV25gx4amgLO7Vlr2VgIgE7i12lw%2FbePdIBnNCFOAyW59KeNc%2FLOKR9HiBsw5wfMqiAQIx%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDI2rMCf90137jbBOpircA6lFVHDrAVIdHEVMqDiEPmXntWB3luSrKgq7OzOo5ov6IxHrX4TF%2Fp5SvXqTznZyfIu0v702ff7%2FmnlxFrB8fbAcHiBDgXAm8jhubcwVUmomdkgBytJqwNEHrP7nsdYxtpZ%2B573CsPSbnG8wbjrE79CixvCAw%2FJZC9K562DrHw1ifQhV3hm%2B17b%2F6N%2BZibTjCRmyvoII9NNSJkJUcpCSmuVxu5L6To30EFXW2Ud05Bg%2B9cJy5QlpyngfBVc803o71HvzHEWPBx40dWGB8XNtZLuUG7slfkxqcvHjVEjhOtjLgw14XG0YTtL1K13mxoSTdzGeSL87bZjf2MFixEIIh5G%2Fl6ntLvROGgPMnxHDKvbDl73ZCW8sDTgq3xS9mTwBOfywilEEmVQ4C04apDfC9BoFVbtp1zDrEZ5u5XqSW4vSAoa%2FcfIAOpwEpZ4anJzH41Wf%2BkYf7FHdDejmN06H99y1I4jAypIYGiuTQ%2FHBvVx5W02Sn85imZaRwo%2Fac6JBmbsqDWNxdK899WbgM6Szvey4xManA3yOdoal3AIxRUZVP8InABi173ol1NsnxoqFcyLyVu%2FS8u70aXPxnfdhrDIpmpgvZmDWWnFVu%2B1DpCoz0Jp5u3RzND2yvX4nMKuU9bwGOqUB6fjC%2FvL9f8M9yFcFQhnYtVod9Rbo7zSKL7ZKxeVAFrWldy44cTGaBkNvYzpOCZun%2BTbtaT6Cx7FpvNIMUt3w5w8s%2BiRArsmXWIhg9mzkFggudWAvVgiCQW3BpLoAgR3Jj%2B16c8keMdCaFVwh%2FVpdl2dgxHGzY9sxHAVnKnR6dRX%2FRHDTvRJJxdUsTTndVZoOF1t6hEkcfgzjU5wRRYcTt8a2HXIC&X-Amz-Signature=ca13c423fe2299f33bdb487ddd7326bb2274826a2602fea18f9392ea7852328a&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 2. Box and Whisker Plot
A box plot shows the distribution of quantitative data in a way that facilitates comparisons between variables or across levels of a categorical variable. The box shows the quartiles of the dataset while the whiskers extend to show the rest of the distribution, except for points that are determined to be "outliers".
**Syntax:**
```python
sns.boxplot(x='header_1', y='header_2', data=df)
```
**Example Output:**


![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d207ae92-0a7c-4e2f-aa65-0ee5a2c33bf7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466S7QTE5EI%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T221333Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEL7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIDLFQNjsGqx8U1ZOmHaB1hf7022QMCG%2BX0iV6e4fM6BqAiA6h%2Bu97DmYwfj1e3asWGoQ0%2FoV27%2BZ%2FbhXcNTzWl3qwSqIBAjH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM3fGsV9tcd6USbGCBKtwDtV%2BaoeV9dmCzRF%2Fje6ybuqMUI%2FvnQ3KwLyp0EeFOhVvzCT%2BtrDqM5ZBMe%2FC5IN17bfiSJ6%2FAgS8LSl%2F%2F83FxoRxJV6jUmnTja7EK0fG%2FqQIvBqQcLaArDBZgf0rE9WfhPvpW7GgAnu3p1Pxph3eU1H%2Bxf5khkCZRKFtTWmaljVstQyE4zxB8qswfCS9pvSlWypxaSkT88BMsoYz92IehBsbkWQi8lvtYz9NYXF7udYJvInRBfTtctPLYIKiSWRAz9cevyhuyHR9rj2e%2BAOjsf0OYa22xSmk8312CFjHrEP8m7UZsxsNlwxgPyeJqYvBW2rXHdOQsob9vLBOfam8mh%2FrmiymzUpSOWoWAx2u2yFrdwMtNq0HKW8o16CX46Mh88s3itkv2DeUA8YzKfkuqRPerPAQSaX9ka097FbjfNKqfNwXCjuuDc3aw1ItBHJ4vm5zRClq2fKJ8b0SpwAR%2FkzijNGkgnjg%2FMuTrlTwnePT06jZDh8zQkTIHJzbBNYKgEPt6La03wJ%2BpIT83lSmOa716UhEXg4X5SDucRqIeBF9AJ6xNNTnVpn%2BmzKkrcAM034uY%2Fy0h2VQj7xtFKnOO8OIxMIi5NMCh5XlWRVRgZrGKwsNOmvgFHCYDPxkwi5T1vAY6pgF6EtUTXb55GZMff8Zde0832Xf6nnSUNXGPlys6fNHULZoGGqVqDIg9CErnYKeqxLCJUr8g6kWFYB%2FxmDKKqVCXE7NfREsQKKkEQJBjLs4W1UYI0KNUK%2FBBPkRVxJaYEmROYdAZi8RyTdUAtM9B2H%2FZBnf5faMuXZtjqM8hI9UNRaDPMEx54UL4wB94ii2tLZbCo3CcgZBixdjQDNyFxHKrMMoppddY&X-Amz-Signature=1b681e0f972bbefdafa03b725061f7a7d394831d15a4268cb416812b15ced413&X-Amz-SignedHeaders=host&x-id=GetObject)

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0e516edc-7551-4792-ab18-0494db3c4c0c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TJ6KL3DJ%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T221333Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEL7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEojoMhgET3hEqLXG6uBAKhGWnVsq220DtN0DEtKZhhtAiB1QC5%2FMGBJkxPLpJ2m0pVmdXPl3f5pQw5BwxQ61koRcyqIBAjH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIML1oDGKHYGbyxSL8HKtwD%2BDE5SFikp%2BlQleNJDGdV3UcQ7u4d4EloGPbHes%2FP9Hk8nR81WGTezBM%2BVw235YpNgvA5jOUjH2CPYZqpcIcpTTtaLyA7HgZg%2FZ%2B%2FBo6HVkKUeWZOlBF4tmWyiV3DYpD8AAFB5PbiQa3OZWbxUl1SBHNY0rTZItUymQsNAWC7WQpgl02EGSa2a9eBykwt1L9txC78%2FOQogE0Lu6%2BtQp%2FcyO4%2FqAjDxPg2vlozviocOpbfcxumxhcOVuGhkfiSBg99JBfJsPwJdRD1vCMKALlWkLZvbJT%2FSoYnGPLrPIpASG6PcKbPL1Xh8%2B6MeaK6ZGP5%2F%2F3tBs6yrfUck14tJB83ziM9L%2B3p%2BT2BW3uZZFg0RkQFy4l6to52My8uQ6Ej5%2F6OEZh6EIG94wwOXF8ddFqvt99YN2Uy5sYmS4i%2BsRWYS%2FqjadeTBPCQsn80%2BDXqk1qxBYCpB2NPXh31yGcrpgEmSNDYocp8fZTmm8juykiu5NnCFcTESY0Abovnke7LXXIMU3leAre0yHDwsNQEoDXn7gBAMLcyjoJmikBfb3kyb1EdS4dGp3Q%2BzilG%2FYUOzZ1ZLRXMAcF2xzCxAEfyf2BqpV4hW1aQGt9jc7s3YdaKx1d%2BxKtbcLjVSJ9JiXIw7pP1vAY6pgE46C4D%2FhvPpDAFetZwOTYEcv6s7lTudZnWVQPEmyEg%2B5z9DJnLle%2FEYqqplC4FqFMJ1uYIJFVdyNYqt0e%2FsVTXdRNeyKS%2BleYaIxldRTswF81BoIlKWodg21vcx0IRv%2FwK7LAytmgn8S2s90SB%2FBrnkG4A1lJycFZULGIthxbuNyWQ1AaPlN0S0uBnIQlG023HIv8XF8lmcWaHQ9WJlTA7yu3O7JCX&X-Amz-Signature=3e3acec594d09ccfd69ac5e3f30ccf748684b7357d06b5fe01c56fb823550c93&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23a79b9d-2356-49a9-8fd9-65c6b0ab2cc5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TJBXFT5R%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T221332Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEL7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDEKBya64mC6moaj8h394WHoCGuV25gx4amgLO7Vlr2VgIgE7i12lw%2FbePdIBnNCFOAyW59KeNc%2FLOKR9HiBsw5wfMqiAQIx%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDI2rMCf90137jbBOpircA6lFVHDrAVIdHEVMqDiEPmXntWB3luSrKgq7OzOo5ov6IxHrX4TF%2Fp5SvXqTznZyfIu0v702ff7%2FmnlxFrB8fbAcHiBDgXAm8jhubcwVUmomdkgBytJqwNEHrP7nsdYxtpZ%2B573CsPSbnG8wbjrE79CixvCAw%2FJZC9K562DrHw1ifQhV3hm%2B17b%2F6N%2BZibTjCRmyvoII9NNSJkJUcpCSmuVxu5L6To30EFXW2Ud05Bg%2B9cJy5QlpyngfBVc803o71HvzHEWPBx40dWGB8XNtZLuUG7slfkxqcvHjVEjhOtjLgw14XG0YTtL1K13mxoSTdzGeSL87bZjf2MFixEIIh5G%2Fl6ntLvROGgPMnxHDKvbDl73ZCW8sDTgq3xS9mTwBOfywilEEmVQ4C04apDfC9BoFVbtp1zDrEZ5u5XqSW4vSAoa%2FcfIAOpwEpZ4anJzH41Wf%2BkYf7FHdDejmN06H99y1I4jAypIYGiuTQ%2FHBvVx5W02Sn85imZaRwo%2Fac6JBmbsqDWNxdK899WbgM6Szvey4xManA3yOdoal3AIxRUZVP8InABi173ol1NsnxoqFcyLyVu%2FS8u70aXPxnfdhrDIpmpgvZmDWWnFVu%2B1DpCoz0Jp5u3RzND2yvX4nMKuU9bwGOqUB6fjC%2FvL9f8M9yFcFQhnYtVod9Rbo7zSKL7ZKxeVAFrWldy44cTGaBkNvYzpOCZun%2BTbtaT6Cx7FpvNIMUt3w5w8s%2BiRArsmXWIhg9mzkFggudWAvVgiCQW3BpLoAgR3Jj%2B16c8keMdCaFVwh%2FVpdl2dgxHGzY9sxHAVnKnR6dRX%2FRHDTvRJJxdUsTTndVZoOF1t6hEkcfgzjU5wRRYcTt8a2HXIC&X-Amz-Signature=adccabb09f2b0fe892198f732efc5de65bc867e29ed5e93e1f7b0f832bab05d5&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 4. KDE Plot
A Kernel Density Estimate (KDE) plot is a graph that creates a probability distribution curve for the data based upon its likelihood of occurrence on a specific value. This is created for a single vector of information.
**Syntax:**
```python
sns.kdeplot(X) || sns.kdeplot(df['age'])
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0d571213-2a2f-4921-a50b-880847aa05ee/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TJBXFT5R%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T221332Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEL7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDEKBya64mC6moaj8h394WHoCGuV25gx4amgLO7Vlr2VgIgE7i12lw%2FbePdIBnNCFOAyW59KeNc%2FLOKR9HiBsw5wfMqiAQIx%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDI2rMCf90137jbBOpircA6lFVHDrAVIdHEVMqDiEPmXntWB3luSrKgq7OzOo5ov6IxHrX4TF%2Fp5SvXqTznZyfIu0v702ff7%2FmnlxFrB8fbAcHiBDgXAm8jhubcwVUmomdkgBytJqwNEHrP7nsdYxtpZ%2B573CsPSbnG8wbjrE79CixvCAw%2FJZC9K562DrHw1ifQhV3hm%2B17b%2F6N%2BZibTjCRmyvoII9NNSJkJUcpCSmuVxu5L6To30EFXW2Ud05Bg%2B9cJy5QlpyngfBVc803o71HvzHEWPBx40dWGB8XNtZLuUG7slfkxqcvHjVEjhOtjLgw14XG0YTtL1K13mxoSTdzGeSL87bZjf2MFixEIIh5G%2Fl6ntLvROGgPMnxHDKvbDl73ZCW8sDTgq3xS9mTwBOfywilEEmVQ4C04apDfC9BoFVbtp1zDrEZ5u5XqSW4vSAoa%2FcfIAOpwEpZ4anJzH41Wf%2BkYf7FHdDejmN06H99y1I4jAypIYGiuTQ%2FHBvVx5W02Sn85imZaRwo%2Fac6JBmbsqDWNxdK899WbgM6Szvey4xManA3yOdoal3AIxRUZVP8InABi173ol1NsnxoqFcyLyVu%2FS8u70aXPxnfdhrDIpmpgvZmDWWnFVu%2B1DpCoz0Jp5u3RzND2yvX4nMKuU9bwGOqUB6fjC%2FvL9f8M9yFcFQhnYtVod9Rbo7zSKL7ZKxeVAFrWldy44cTGaBkNvYzpOCZun%2BTbtaT6Cx7FpvNIMUt3w5w8s%2BiRArsmXWIhg9mzkFggudWAvVgiCQW3BpLoAgR3Jj%2B16c8keMdCaFVwh%2FVpdl2dgxHGzY9sxHAVnKnR6dRX%2FRHDTvRJJxdUsTTndVZoOF1t6hEkcfgzjU5wRRYcTt8a2HXIC&X-Amz-Signature=b03fc1ac903d5c184c24cb2503c126ad3f9ed7fcfc0fc4c13ecd586ae63b507b&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/53752550-ef82-4ca9-a01a-09921f0282d0/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TJBXFT5R%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T221332Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEL7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDEKBya64mC6moaj8h394WHoCGuV25gx4amgLO7Vlr2VgIgE7i12lw%2FbePdIBnNCFOAyW59KeNc%2FLOKR9HiBsw5wfMqiAQIx%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDI2rMCf90137jbBOpircA6lFVHDrAVIdHEVMqDiEPmXntWB3luSrKgq7OzOo5ov6IxHrX4TF%2Fp5SvXqTznZyfIu0v702ff7%2FmnlxFrB8fbAcHiBDgXAm8jhubcwVUmomdkgBytJqwNEHrP7nsdYxtpZ%2B573CsPSbnG8wbjrE79CixvCAw%2FJZC9K562DrHw1ifQhV3hm%2B17b%2F6N%2BZibTjCRmyvoII9NNSJkJUcpCSmuVxu5L6To30EFXW2Ud05Bg%2B9cJy5QlpyngfBVc803o71HvzHEWPBx40dWGB8XNtZLuUG7slfkxqcvHjVEjhOtjLgw14XG0YTtL1K13mxoSTdzGeSL87bZjf2MFixEIIh5G%2Fl6ntLvROGgPMnxHDKvbDl73ZCW8sDTgq3xS9mTwBOfywilEEmVQ4C04apDfC9BoFVbtp1zDrEZ5u5XqSW4vSAoa%2FcfIAOpwEpZ4anJzH41Wf%2BkYf7FHdDejmN06H99y1I4jAypIYGiuTQ%2FHBvVx5W02Sn85imZaRwo%2Fac6JBmbsqDWNxdK899WbgM6Szvey4xManA3yOdoal3AIxRUZVP8InABi173ol1NsnxoqFcyLyVu%2FS8u70aXPxnfdhrDIpmpgvZmDWWnFVu%2B1DpCoz0Jp5u3RzND2yvX4nMKuU9bwGOqUB6fjC%2FvL9f8M9yFcFQhnYtVod9Rbo7zSKL7ZKxeVAFrWldy44cTGaBkNvYzpOCZun%2BTbtaT6Cx7FpvNIMUt3w5w8s%2BiRArsmXWIhg9mzkFggudWAvVgiCQW3BpLoAgR3Jj%2B16c8keMdCaFVwh%2FVpdl2dgxHGzY9sxHAVnKnR6dRX%2FRHDTvRJJxdUsTTndVZoOF1t6hEkcfgzjU5wRRYcTt8a2HXIC&X-Amz-Signature=fdc40c5341a776990cf671f0cb5822ed8cc565cb993cb1adad15112971b86de8&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
## 4. Correlation Between Variables
Correlation is a statistical measure of the extent to which different variables are interdependent. It indicates how changes in one variable are associated with changes in another variable over time.
### Positive Correlation
Positive correlation indicates that as one variable increases, the other variable also tends to increase.
**Example: Engine Size and Price**
- **Positive Correlation:** Engine size increases, price also increases.
- **Visualization:** Scatter plot with a steep positive slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c7ea9b0-3ef3-4357-a9c3-554fc71b6b15/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RWZSV6ZS%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T221333Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEL7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIA%2FRsW49w3%2BLC62rrStGmtS5L9X0KD292MAgl%2F5gEsMeAiEAp6ykyealrnvPrEoQBmCCzUcNVj3Vycaxh7YYE0l8q%2FoqiAQIx%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDG1SGC1IBDS3DSYknircA%2BJaXrLU%2BR8c879GIQp5QzmtqTeIBgOEthonSLxuq4uPr1G2kRve%2Bp5Fa0a5vfUcRwW1ggBg%2BPPU156UPEFS1r3G3aDynZ%2FDc5XJ%2BN62G6U3GEIYQMKTNyzqf%2FaLVQxQW1HG%2FlaQpd83EcnFdbTYx553iH4MICGWAAXSeoTyny%2F%2Bwfq9%2BonL%2FIJ3HqV0majOudDdaLL1gce0WvhN10pBGeGDa5W5yPIWFBkUOscvGxlS40F97eBvsW2tGFSDXcndA7qKdgZIW8zHE5uutWr2a4eGUo0%2F%2BzqWFDYvM44wsINaWKkXJ%2FVH%2BwiPQIP2CYKDT0bbiRm3zue1Y1uuFWeG%2B%2BA0GGFQElg3boFBrNNvcup4blQX1S%2BWUw4jCm2iyiHsPXHWMTz4biNadAmhKJWAhtL6Y5xILoJiKGMra4LA6KhRZbuHt%2Fe%2FHmTcXJTlUn77ET2mfE%2B0ovwjUH3kb%2F6ADxoYrzoGS4C7RasG6zre44tqYSUOWaJxQ%2FJe5S4pQiUuZoPYEQ1Kc6fRIuR72jGkXR26m0RmkH3bbQikM%2FSkbOyBq1JUB5WnSgwIHailc8BaKl42fvZ8VOUF877IrfjLrcgHQotPq0N5WqAmIYBTNGna3sWkHbBaMHxvxyuEMIyU9bwGOqUBRMNLvg%2BIvw77%2FXs7j1U3ivj4gBUyRByq3UxEQ7%2BoTEgph%2B0eyjUI%2BeeXoECS2%2FDAdDAA8qDg26rGDl%2BPvCrYkFQTMDcZ5NF9cbn%2FjHxDNRALKVJnQbWkRCHV0Vfv6MB8jtKDxVUJUZDWlEpdQJNyXHYlDvMJ1v6s%2BEXuF0G%2FEG2iiYUyKveYAy94QYZytN6V8rGBnVHXfsnxcDGB6b61x66ullzv&X-Amz-Signature=5cd95b0645357b5dd99af29fe000e9d7add10d76ecc995d24db43ec3247ac0ea&X-Amz-SignedHeaders=host&x-id=GetObject)
**Explanation:** When engine size increases, there is a corresponding increase in the price of the vehicle. This positive correlation suggests that larger engines tend to be associated with higher prices in the market.
___
### Negative Correlation
Negative correlation indicates that as one variable increases, the other variable tends to decrease.
**Example: Highway Miles per Gallon and Price**
- **Negative Correlation:** As highway miles per gallon increases, price decreases.
- **Visualization:** Scatter plot with a steep negative slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/10f1f798-9cc4-4df2-a9c1-5a339f554a0b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R5YY5G55%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T221333Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEL7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCICpf0WvRX6cIwyr8llFJjKXDKDPX3BGg0MCLy4RttZDMAiEA1%2BJXXVgZ2SVI%2BAQc0t5xq%2Fceo2aOUUUU7%2FG%2BFzv7AmwqiAQIx%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDCTYcWKojUWj6SWj4CrcAxDdpINoQFS6pkT00vYttbXANOB4tZpDbnyBBnuKgU1wlipO5NZpvV9yPd1j4wkaZ%2F1dSo8ZhIADXpKN5yyeMGs2oFF7aMOoIOkxS%2FhzSvQXvdFwElQpRUyEgwV2YYQ%2BBeKzzSSbUq5f1SorGfqw09ZIdDmv8oyrn64tjp%2FDNZtcrohMNUR99XcO06varJwrtk0E5kLkiAEYVhFQESgum15VCwH5LjOsLO8pnYeoP%2FQ%2FW9a06O9q80XHOVs%2F%2BWrxc226c6uV3vJ4DqsP5vROd2j4RgAVDQUy9g9w0mketwfpu0TxcSI%2BHOSDNckIIlhmK56brLs0X86JJzncXyfK3xbKm3u4AfhDWFUx3BTAAjU5c5Sh%2B5EAsY%2BN7wWYzqJ7Qv3L5BbbMWRfzwCJkY1hcQLD56%2BeUGnIgczmEDxbL9qjHWW%2BIntPWFQGTgbDJDrCO6ESWuwDDl7hcRvyuZ6OjTkB7CWlXAOLVb4kbdOoROqR0KiF5fkW2SsxQcPpQCzbVCJHvyrbNOY%2B4MIay0Q9iatZD3F1dqLRRvmx1tzStTVaEpi0YPYyhwrpN5Lql23vCy53BRoTxY8fhPdbJbNjZJXP4a%2BqSfvsQeIDH9bU8rV%2BJ8zTzl5fO%2BpRReOqMNaT9bwGOqUBLNRWle8DOsibkQNQuBFFlbvO1ODbYbTpp2ZUo52RvUCF7sfer2o3rWmGs8pcMHqodAeva6Ip2SA7N380nPDfJ9TfGpioWXwuEfOCcZ3X%2By0eHJvIMBoO%2FK99b2Wq7DOExglFgZCKa%2BGq4E0dTDaC0hzuSlJix4gPhYuAgAWeLQ2KJs1dj7Ij4s63CZfhm8TukgZa%2FlFcKKSnB2xIW1m4q950MyAs&X-Amz-Signature=0153b13344460371748bc5bcbe30a60f772cc82b860784ca0942d40f22b85759&X-Amz-SignedHeaders=host&x-id=GetObject)
**Explanation:** When highway miles per gallon increases, the price of the vehicle tends to decrease. This negative correlation suggests that cars with higher fuel efficiency (more miles per gallon) are generally priced lower in the market.
___
### Weak Correlation
Weak correlation indicates a lack of strong relationship between the variables.
**Example: RPM and Price**
- **Weak Correlation:** Low and high RPM values show varied prices, indicating no strong predictive relationship.
- **Visualization:** Scatter plot with no clear trend or slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9f914514-8914-4bf4-ac84-d9e3077f6eb1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46673J3KOD7%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T221333Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEL7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCHyhYCB6H%2BOA9%2B6FRFTjxry8igG%2BK0BarMKdMkKr79DQCIQDGZyfqTKHRGKF%2FHAlnY%2B3ibN%2FLzxX48M6gRxfM0XGUMiqIBAjH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMlIV9RxA4McgJObRHKtwDdcL8bhqudx89iSL4R0J0XfRuFzul1EO7mcqY4hBU%2FtQ%2FsHaptJpu5f1yZJqhT02dAmD%2Bju8NboA1Ee1m7vPqH8aPF9mvupMdN%2BFfz0AvyXJzfNUVP%2FVR%2BosvbY7G8q3H7S7RN0LNI2FtFVmT74335EIi4pk%2BH6wvJoDmgR3Faoo9V%2BCpDoy0UPvK6RYSuFx8Z%2F70wHdvaWo4yU%2BrfDOGoCXFDGphtCiHq4BALMKUB3mCPhl8F3FGvmH1JzYZmjPmCKvta3zS2SZyju%2Fi%2F2Cty3WY2IXpZhk4peVc63%2BlahGf0pDVWLyUQCyRR04SBLbSUWnFDhx4zFboI5f6q%2FukJEH6Kzg7t4CiQc110JblQf%2BOftVQifOlFOQzK%2BScxikYmqfJ2Vo3vP48KfXS9Y4diEp9EthWWBxnABecLDvNGvSd4dR6C0m8zhBLlbc0OK7ZXTwfGqFDhPuNUxSoFo6PSYpIOlTgA92hQzc5KDgDX3gF7ThzRx%2F2JXG7Fbqa2fCVdH%2F%2BPBkTY%2BPF977Ff58pyExRPoQ56rSDQWiP9%2BzKuKqgKhMYx0qhifT2IICwC2JDJRzmCoF3YiwuY%2BkIyGFGWIeJ4q0bXn51t8UgLTe%2FVB7unqa1przeazf7nzYwi5T1vAY6pgGmtwReVsQU0UdkPJuc32vJaPa42lMuD1PC0HsQSSMTCI8LUfs7KTxU9tOGfLSZUcxLi2H4iA6s0jcFO0G80Kh%2BeH1byZ9xkgd5Ku%2BO6zKhptUsGaTHN9D03Kb0YXq8uqML47s%2BDbx4X2SM0P9fkr4rEpGhGb0dqpfuQmkYsGuzAz6okkg9QOIZSG5H9mGrAQdlMQpKp8BzuSQCAG4vgCPO44FRsDdT&X-Amz-Signature=c3106b3919297844dab1b63310edfb0f7eda5e618a519f3231aa4ca6b3747c4a&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f18086e5-5b04-4fbf-8309-8944ab20d213/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZFF3AQZT%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T221333Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEL7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEl7vwPNaxzefYKPg54ywl9WKmP7Ip0J%2BBJ5jW8EtWSGAiAtD05JBYguNYDXdGnE8AGnH0N%2Fs3rAVfD%2FO6OewZMhzSqIBAjH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMXP9s3wwFr3N7Hq12KtwDQ%2BdiQs3w8Hc1BRasrWdwevC7ogM92%2F0fQOmBHVelkztYmjxXC6tNmefDnmo372urxru3gIKrCqRqBgTVXZLQw64Sr1iTBPdfIferT9nmDz%2BdW7CMxZbwkOC%2B%2BiMX%2Fc7EpUgvzadnDXyhOvOt%2Bk5MY1pvTombFoOeTq4JJ29RVAxxEosref%2B%2B00qCzFyccjXN3XFoNdHUCoIuMUmxpZuY9MUqa6pWp0WmgV6chAjFmuxewN7A5DJjSxhEDlNFmT6H0hwht7AqKnntTkqfDzH9V0WhJ1Qjg3V76lQkVEEz3zzhpxNWS1jn4VZuW0SNJ%2Fc9FSWxGlAYKITpa8uwnCwnYbtdt6B07mNI6TYAV3%2FHXIzfkk1TuHEF%2Ba3Tswg2%2BkmToTY9yvDsG%2BTDDUVHaMo9N9cre7oRWh3Nigd7vizSnQKjt4q0KvCiW30y49a5iPrVAVXWUaccNxJmb%2FLFZjMTzvS3Rt0XQ3xDv58k7hg467RTNelb2xu%2FMtSYjuwl2v7JKHfma8Uc1ZNCOATCs8QkCZmhsjuz%2BTqwqD94hYurW38ZzcCPK3wknDglPtlPQwK7RKvaNf%2B17Bpo1ZX7Ar7BKmVDA3MiCcKsucrN%2FZxkaqOYp4uvAKqaNnUnOC4wgJX1vAY6pgGTlphElOwSVNXGcBUAVP9iLO6drNmS%2BQSYXUHz5HP9%2BjYv0aspuugf3Cu2%2FxCdpqtiQ%2Fc%2BV0wgXXk98DhPTAJlm%2Bm3fo85UVa%2FkNmlXLwhQ4chfS0AWu7RTx7B6WKdDXQeayvv%2BbYtMOEP0N4F95TnRS8B6%2FIU468ZoC8ixmn5xQhQG3RNPcMrKRBI200cT%2Bfo0ktz%2Boq1gAXvr9GBNgrgi9oq0wa5&X-Amz-Signature=71f09384290e1ee447f004a1397191462fa0c3eac6e3bf32abf4ce50e05cd353&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Correlation Plot
Heatmap visualizes correlations among variables. Color scheme indicates Pearson correlation coefficients. Dark red diagonal line shows perfect correlation (value of 1) between variables and themselves.
This heatmap offers overview of variable relationships and their link with price.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cd3b341e-cc1a-45f7-8aec-cdc00436d270/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZFF3AQZT%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T221333Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEL7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEl7vwPNaxzefYKPg54ywl9WKmP7Ip0J%2BBJ5jW8EtWSGAiAtD05JBYguNYDXdGnE8AGnH0N%2Fs3rAVfD%2FO6OewZMhzSqIBAjH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMXP9s3wwFr3N7Hq12KtwDQ%2BdiQs3w8Hc1BRasrWdwevC7ogM92%2F0fQOmBHVelkztYmjxXC6tNmefDnmo372urxru3gIKrCqRqBgTVXZLQw64Sr1iTBPdfIferT9nmDz%2BdW7CMxZbwkOC%2B%2BiMX%2Fc7EpUgvzadnDXyhOvOt%2Bk5MY1pvTombFoOeTq4JJ29RVAxxEosref%2B%2B00qCzFyccjXN3XFoNdHUCoIuMUmxpZuY9MUqa6pWp0WmgV6chAjFmuxewN7A5DJjSxhEDlNFmT6H0hwht7AqKnntTkqfDzH9V0WhJ1Qjg3V76lQkVEEz3zzhpxNWS1jn4VZuW0SNJ%2Fc9FSWxGlAYKITpa8uwnCwnYbtdt6B07mNI6TYAV3%2FHXIzfkk1TuHEF%2Ba3Tswg2%2BkmToTY9yvDsG%2BTDDUVHaMo9N9cre7oRWh3Nigd7vizSnQKjt4q0KvCiW30y49a5iPrVAVXWUaccNxJmb%2FLFZjMTzvS3Rt0XQ3xDv58k7hg467RTNelb2xu%2FMtSYjuwl2v7JKHfma8Uc1ZNCOATCs8QkCZmhsjuz%2BTqwqD94hYurW38ZzcCPK3wknDglPtlPQwK7RKvaNf%2B17Bpo1ZX7Ar7BKmVDA3MiCcKsucrN%2FZxkaqOYp4uvAKqaNnUnOC4wgJX1vAY6pgGTlphElOwSVNXGcBUAVP9iLO6drNmS%2BQSYXUHz5HP9%2BjYv0aspuugf3Cu2%2FxCdpqtiQ%2Fc%2BV0wgXXk98DhPTAJlm%2Bm3fo85UVa%2FkNmlXLwhQ4chfS0AWu7RTx7B6WKdDXQeayvv%2BbYtMOEP0N4F95TnRS8B6%2FIU468ZoC8ixmn5xQhQG3RNPcMrKRBI200cT%2Bfo0ktz%2Boq1gAXvr9GBNgrgi9oq0wa5&X-Amz-Signature=3b989fdd8770eb707de747a1a86d18755189041214a2430d07226d1559a404dd&X-Amz-SignedHeaders=host&x-id=GetObject)

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
