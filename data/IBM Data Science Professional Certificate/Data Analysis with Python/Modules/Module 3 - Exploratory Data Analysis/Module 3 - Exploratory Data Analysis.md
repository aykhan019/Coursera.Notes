

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7e6d594d-952e-44b6-97ea-31225882aea6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Q5N5AGYY%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T122622Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHQaCXVzLXdlc3QtMiJHMEUCIQC0OVwgpgBJ4D%2FVfboXwlvZ72wEonVUCdmlIexb%2FAAuGwIgTnj3vDG8KpJAMAYv9rVfAi%2Fm1d%2FVJ2AXfNbPgfN7NswqiAQIjf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLuKvhRgL%2FmM6CGU4CrcA66IR%2FYaqDjr9lLoEaM7wbfuZIFJdMK5EO%2FiIkQ%2FUSQaw%2BSd4ggNfeT724r0MbycPCt3BFf0HqUFbUs0JFARHXpygRvC0cccuYPDnYvBaiA%2F9PxVBCSX%2FRWXXokcLhM3HyHuKqcNZI1dlnh6g3LoUmHbRXsaxr%2FfATHjapG%2FP7EJqG3F4EiNVVvzwc2zjIlQ2wAM5vXQWQTXyLC5Gvoox%2Fb4CmnooHw5%2FjpNgWGm4cJWIg7ljH8URis3LvNvPO9aLqfbi%2FcqLHNmibglL8u7r9m7QmiLwA09FVDRoIHZQachRJ7jg%2F9WG4%2F78V2%2F5Ydg0qPnvLDwrUjFAlwDHQc9BW%2BqdRhP8Yt48rIccHx2rIFSFdTtI%2B7JBkhhs5t55zuNZw1zSPTov7kBR1jomYUJd86zqJH8INABRR5NGkCP%2FzTmbT5L%2FTAHjP8iHcLOmHxwiyJF3h0%2F7pUkIMI5rCz7UbVsr%2FxSrQ%2BOTgo0PukC1vHdxmrEfvTQFpna%2BJDhK0bfAwBhwYTNoU3vIDQSfNFsakTKDRa%2B%2FiUvERiz%2FjTBy6jBRkWqKrOzNiGCTpV4uEeiAJucb3O3TJiIDf3t%2BqrM68qdX2u%2B83RX3Zpw7tlX68HQhFu3aYMeuyOhYCSWMIyGnb0GOqUBt5S%2FhCxkR%2B1LU5DdXzcqqWRc2kvbXqIWY0Ix%2B%2BaO%2FgjawUQGwRNYlqR1KOAsyYjeYW1JBpoWz7SQQZWWT7xdi8ruPrKwS9bvf0MYrCpsCJb7G2M3KvpqZGl1GcERu0UwEaX%2F75yAbCajUyej5JAheneQD9YCmteX7Y3sWoxiMqh%2Bu3%2BcPOnimKqQNTW9AUMd2FtCdAyzO0JsGK6chgSBY3x0s5L8&X-Amz-Signature=3499e9452784cbedacbe4b206990c46ef1a563f0728636110c3b32c9724b539b&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cbfaed9e-b398-4902-8936-dea058b21def/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Q5N5AGYY%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T122622Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHQaCXVzLXdlc3QtMiJHMEUCIQC0OVwgpgBJ4D%2FVfboXwlvZ72wEonVUCdmlIexb%2FAAuGwIgTnj3vDG8KpJAMAYv9rVfAi%2Fm1d%2FVJ2AXfNbPgfN7NswqiAQIjf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLuKvhRgL%2FmM6CGU4CrcA66IR%2FYaqDjr9lLoEaM7wbfuZIFJdMK5EO%2FiIkQ%2FUSQaw%2BSd4ggNfeT724r0MbycPCt3BFf0HqUFbUs0JFARHXpygRvC0cccuYPDnYvBaiA%2F9PxVBCSX%2FRWXXokcLhM3HyHuKqcNZI1dlnh6g3LoUmHbRXsaxr%2FfATHjapG%2FP7EJqG3F4EiNVVvzwc2zjIlQ2wAM5vXQWQTXyLC5Gvoox%2Fb4CmnooHw5%2FjpNgWGm4cJWIg7ljH8URis3LvNvPO9aLqfbi%2FcqLHNmibglL8u7r9m7QmiLwA09FVDRoIHZQachRJ7jg%2F9WG4%2F78V2%2F5Ydg0qPnvLDwrUjFAlwDHQc9BW%2BqdRhP8Yt48rIccHx2rIFSFdTtI%2B7JBkhhs5t55zuNZw1zSPTov7kBR1jomYUJd86zqJH8INABRR5NGkCP%2FzTmbT5L%2FTAHjP8iHcLOmHxwiyJF3h0%2F7pUkIMI5rCz7UbVsr%2FxSrQ%2BOTgo0PukC1vHdxmrEfvTQFpna%2BJDhK0bfAwBhwYTNoU3vIDQSfNFsakTKDRa%2B%2FiUvERiz%2FjTBy6jBRkWqKrOzNiGCTpV4uEeiAJucb3O3TJiIDf3t%2BqrM68qdX2u%2B83RX3Zpw7tlX68HQhFu3aYMeuyOhYCSWMIyGnb0GOqUBt5S%2FhCxkR%2B1LU5DdXzcqqWRc2kvbXqIWY0Ix%2B%2BaO%2FgjawUQGwRNYlqR1KOAsyYjeYW1JBpoWz7SQQZWWT7xdi8ruPrKwS9bvf0MYrCpsCJb7G2M3KvpqZGl1GcERu0UwEaX%2F75yAbCajUyej5JAheneQD9YCmteX7Y3sWoxiMqh%2Bu3%2BcPOnimKqQNTW9AUMd2FtCdAyzO0JsGK6chgSBY3x0s5L8&X-Amz-Signature=f1a3bdbfcbaaba87d0abe296f33fde866d9ec52fc9cd0875f08767a045c746a4&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/91181646-b1e0-4433-9711-6259a96a9247/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Q5N5AGYY%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T122622Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHQaCXVzLXdlc3QtMiJHMEUCIQC0OVwgpgBJ4D%2FVfboXwlvZ72wEonVUCdmlIexb%2FAAuGwIgTnj3vDG8KpJAMAYv9rVfAi%2Fm1d%2FVJ2AXfNbPgfN7NswqiAQIjf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLuKvhRgL%2FmM6CGU4CrcA66IR%2FYaqDjr9lLoEaM7wbfuZIFJdMK5EO%2FiIkQ%2FUSQaw%2BSd4ggNfeT724r0MbycPCt3BFf0HqUFbUs0JFARHXpygRvC0cccuYPDnYvBaiA%2F9PxVBCSX%2FRWXXokcLhM3HyHuKqcNZI1dlnh6g3LoUmHbRXsaxr%2FfATHjapG%2FP7EJqG3F4EiNVVvzwc2zjIlQ2wAM5vXQWQTXyLC5Gvoox%2Fb4CmnooHw5%2FjpNgWGm4cJWIg7ljH8URis3LvNvPO9aLqfbi%2FcqLHNmibglL8u7r9m7QmiLwA09FVDRoIHZQachRJ7jg%2F9WG4%2F78V2%2F5Ydg0qPnvLDwrUjFAlwDHQc9BW%2BqdRhP8Yt48rIccHx2rIFSFdTtI%2B7JBkhhs5t55zuNZw1zSPTov7kBR1jomYUJd86zqJH8INABRR5NGkCP%2FzTmbT5L%2FTAHjP8iHcLOmHxwiyJF3h0%2F7pUkIMI5rCz7UbVsr%2FxSrQ%2BOTgo0PukC1vHdxmrEfvTQFpna%2BJDhK0bfAwBhwYTNoU3vIDQSfNFsakTKDRa%2B%2FiUvERiz%2FjTBy6jBRkWqKrOzNiGCTpV4uEeiAJucb3O3TJiIDf3t%2BqrM68qdX2u%2B83RX3Zpw7tlX68HQhFu3aYMeuyOhYCSWMIyGnb0GOqUBt5S%2FhCxkR%2B1LU5DdXzcqqWRc2kvbXqIWY0Ix%2B%2BaO%2FgjawUQGwRNYlqR1KOAsyYjeYW1JBpoWz7SQQZWWT7xdi8ruPrKwS9bvf0MYrCpsCJb7G2M3KvpqZGl1GcERu0UwEaX%2F75yAbCajUyej5JAheneQD9YCmteX7Y3sWoxiMqh%2Bu3%2BcPOnimKqQNTW9AUMd2FtCdAyzO0JsGK6chgSBY3x0s5L8&X-Amz-Signature=aa7b4485beee6c5d97e72a9407e61f1c3cda7c3f8391a892fbfa451135b28e97&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/09aba1c0-0d55-41dd-852a-a04c5b8a3fac/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QVN3ATEB%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T122623Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHQaCXVzLXdlc3QtMiJHMEUCIHkXKTAofNVzcPMLjyro46eCZx3sc%2BI9rSPfuqMiTy8mAiEAsmamMuiRtmTrKZnrw7hng10r0tm6k1xRGlaDAd3G7KoqiAQIjf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPzSSSUigFlm8HaPpSrcA5tBiMHqrOps4x7xMsxdtYaMQ2Hn9reo7%2BLW1%2B3g7rM5dCL8RzmQZVlZbMo8osWiQoAty8IizCItlhm9IAzNR89d1fOwmrmCAOJqM2MwuHLLiOsiO%2F4cl%2FEV71WCtlaYM8RzQB688v1VZfN9DBxq93IFKHnVmzO0T487jttVNqqGBcKSA7Zx7JPm4oxrRJL847a50UA2DP%2BzP%2FlsTPY8ijHQKG99m1RUsZTtwpBhpIfW107bpqzIOsEqbysb8UrKHL6qrce%2BNSxluZ8IQh8GiXHkqIVcdUYw2ttWhQWFvaGWeFCEt8E21j9ocxWkfNEaYtR3KfAo4c98erprm1WdYHpzZgDsUvffgcM3SX6vnCGh7yr%2BmGrqMfDZA12S7eaTv9oplkaHe6Aa0pc0pL1DvjIPDCUqOtaMraQapa3Hp0kQV4rt%2F5CzcHYCeUuyfNNZK1Bgh4yMbnvgWDPIuwVo%2FRKUE8rkFYaRN9%2BmmtvLVhcC3RCfgA1p0H%2BDDlfp5DqvUAm%2F85v8oqjIneA7OOzFH5kt8Y%2BGoidLfzE%2F97Nxe3mWdSPvMUbQ%2BXuxYgVbEbq6fvjfNLTgFTmY%2B%2BPIU%2BKioYJHZgxQrIch4TkautLHxSTU7EeO5RhUbWhkKEqXMPaFnb0GOqUBhH2UUqYFjVWBizGi8YmJXRGZfpnf5aXMpkXmJzwRI3p96lbv9wF%2BSvwGfrLosCauP9i3JrcuZY%2BuRFeaPc61jyE650qVb3NOCmxoS1qY69GzRDT1zICK5Ya1xrGkfh5KHBDYK8stkGGgGN9JAX2732wuOzYIhEeCh%2BGi8GS%2BC6XKGHvmmsmwt7cj%2FJgyK5Lxe2QNWcdJ2ffHjWwy1AxaVQoaxD7g&X-Amz-Signature=901b014375470904212678ca1c93db562320b269731a9e9f37157731fadcdb0a&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 2. Scatter Plot
Scatter plots present the relationship between two variables in a dataset. It represents data points on a two-dimensional plane. The independent variable or attribute is plotted on the X-axis, while the dependent variable is plotted on the Y-axis.
**Syntax:**
```python
plt.scatter(x, y)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23708af9-659f-4f23-b626-1a4292d7842c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QVN3ATEB%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T122623Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHQaCXVzLXdlc3QtMiJHMEUCIHkXKTAofNVzcPMLjyro46eCZx3sc%2BI9rSPfuqMiTy8mAiEAsmamMuiRtmTrKZnrw7hng10r0tm6k1xRGlaDAd3G7KoqiAQIjf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPzSSSUigFlm8HaPpSrcA5tBiMHqrOps4x7xMsxdtYaMQ2Hn9reo7%2BLW1%2B3g7rM5dCL8RzmQZVlZbMo8osWiQoAty8IizCItlhm9IAzNR89d1fOwmrmCAOJqM2MwuHLLiOsiO%2F4cl%2FEV71WCtlaYM8RzQB688v1VZfN9DBxq93IFKHnVmzO0T487jttVNqqGBcKSA7Zx7JPm4oxrRJL847a50UA2DP%2BzP%2FlsTPY8ijHQKG99m1RUsZTtwpBhpIfW107bpqzIOsEqbysb8UrKHL6qrce%2BNSxluZ8IQh8GiXHkqIVcdUYw2ttWhQWFvaGWeFCEt8E21j9ocxWkfNEaYtR3KfAo4c98erprm1WdYHpzZgDsUvffgcM3SX6vnCGh7yr%2BmGrqMfDZA12S7eaTv9oplkaHe6Aa0pc0pL1DvjIPDCUqOtaMraQapa3Hp0kQV4rt%2F5CzcHYCeUuyfNNZK1Bgh4yMbnvgWDPIuwVo%2FRKUE8rkFYaRN9%2BmmtvLVhcC3RCfgA1p0H%2BDDlfp5DqvUAm%2F85v8oqjIneA7OOzFH5kt8Y%2BGoidLfzE%2F97Nxe3mWdSPvMUbQ%2BXuxYgVbEbq6fvjfNLTgFTmY%2B%2BPIU%2BKioYJHZgxQrIch4TkautLHxSTU7EeO5RhUbWhkKEqXMPaFnb0GOqUBhH2UUqYFjVWBizGi8YmJXRGZfpnf5aXMpkXmJzwRI3p96lbv9wF%2BSvwGfrLosCauP9i3JrcuZY%2BuRFeaPc61jyE650qVb3NOCmxoS1qY69GzRDT1zICK5Ya1xrGkfh5KHBDYK8stkGGgGN9JAX2732wuOzYIhEeCh%2BGi8GS%2BC6XKGHvmmsmwt7cj%2FJgyK5Lxe2QNWcdJ2ffHjWwy1AxaVQoaxD7g&X-Amz-Signature=21f1bf68794ad4c7aabc42bd0787dfaa7f6cf4f2425df056463d1447bc64c14c&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 3. Histogram
A histogram is an important visual representation of data in categorical form. To view the data in a "Binned" form, use the histogram plot with a number of bins required or with the data points that mark the bin edges. The x-axis represents the data bins, and the y-axis represents the number of elements in each bin.
**Syntax:**
```python
plt.hist(x, bins)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/24e4424a-df87-40a1-b63b-195cbdc2e0ab/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QVN3ATEB%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T122623Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHQaCXVzLXdlc3QtMiJHMEUCIHkXKTAofNVzcPMLjyro46eCZx3sc%2BI9rSPfuqMiTy8mAiEAsmamMuiRtmTrKZnrw7hng10r0tm6k1xRGlaDAd3G7KoqiAQIjf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPzSSSUigFlm8HaPpSrcA5tBiMHqrOps4x7xMsxdtYaMQ2Hn9reo7%2BLW1%2B3g7rM5dCL8RzmQZVlZbMo8osWiQoAty8IizCItlhm9IAzNR89d1fOwmrmCAOJqM2MwuHLLiOsiO%2F4cl%2FEV71WCtlaYM8RzQB688v1VZfN9DBxq93IFKHnVmzO0T487jttVNqqGBcKSA7Zx7JPm4oxrRJL847a50UA2DP%2BzP%2FlsTPY8ijHQKG99m1RUsZTtwpBhpIfW107bpqzIOsEqbysb8UrKHL6qrce%2BNSxluZ8IQh8GiXHkqIVcdUYw2ttWhQWFvaGWeFCEt8E21j9ocxWkfNEaYtR3KfAo4c98erprm1WdYHpzZgDsUvffgcM3SX6vnCGh7yr%2BmGrqMfDZA12S7eaTv9oplkaHe6Aa0pc0pL1DvjIPDCUqOtaMraQapa3Hp0kQV4rt%2F5CzcHYCeUuyfNNZK1Bgh4yMbnvgWDPIuwVo%2FRKUE8rkFYaRN9%2BmmtvLVhcC3RCfgA1p0H%2BDDlfp5DqvUAm%2F85v8oqjIneA7OOzFH5kt8Y%2BGoidLfzE%2F97Nxe3mWdSPvMUbQ%2BXuxYgVbEbq6fvjfNLTgFTmY%2B%2BPIU%2BKioYJHZgxQrIch4TkautLHxSTU7EeO5RhUbWhkKEqXMPaFnb0GOqUBhH2UUqYFjVWBizGi8YmJXRGZfpnf5aXMpkXmJzwRI3p96lbv9wF%2BSvwGfrLosCauP9i3JrcuZY%2BuRFeaPc61jyE650qVb3NOCmxoS1qY69GzRDT1zICK5Ya1xrGkfh5KHBDYK8stkGGgGN9JAX2732wuOzYIhEeCh%2BGi8GS%2BC6XKGHvmmsmwt7cj%2FJgyK5Lxe2QNWcdJ2ffHjWwy1AxaVQoaxD7g&X-Amz-Signature=b70514dc8484eeb6f2aeda8d6b4a2f40b31afb3eb60083ae25b93a945c776cbf&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ab5a6dfe-51f5-43ee-bcb3-33dae4a1c7ad/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QVN3ATEB%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T122623Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHQaCXVzLXdlc3QtMiJHMEUCIHkXKTAofNVzcPMLjyro46eCZx3sc%2BI9rSPfuqMiTy8mAiEAsmamMuiRtmTrKZnrw7hng10r0tm6k1xRGlaDAd3G7KoqiAQIjf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPzSSSUigFlm8HaPpSrcA5tBiMHqrOps4x7xMsxdtYaMQ2Hn9reo7%2BLW1%2B3g7rM5dCL8RzmQZVlZbMo8osWiQoAty8IizCItlhm9IAzNR89d1fOwmrmCAOJqM2MwuHLLiOsiO%2F4cl%2FEV71WCtlaYM8RzQB688v1VZfN9DBxq93IFKHnVmzO0T487jttVNqqGBcKSA7Zx7JPm4oxrRJL847a50UA2DP%2BzP%2FlsTPY8ijHQKG99m1RUsZTtwpBhpIfW107bpqzIOsEqbysb8UrKHL6qrce%2BNSxluZ8IQh8GiXHkqIVcdUYw2ttWhQWFvaGWeFCEt8E21j9ocxWkfNEaYtR3KfAo4c98erprm1WdYHpzZgDsUvffgcM3SX6vnCGh7yr%2BmGrqMfDZA12S7eaTv9oplkaHe6Aa0pc0pL1DvjIPDCUqOtaMraQapa3Hp0kQV4rt%2F5CzcHYCeUuyfNNZK1Bgh4yMbnvgWDPIuwVo%2FRKUE8rkFYaRN9%2BmmtvLVhcC3RCfgA1p0H%2BDDlfp5DqvUAm%2F85v8oqjIneA7OOzFH5kt8Y%2BGoidLfzE%2F97Nxe3mWdSPvMUbQ%2BXuxYgVbEbq6fvjfNLTgFTmY%2B%2BPIU%2BKioYJHZgxQrIch4TkautLHxSTU7EeO5RhUbWhkKEqXMPaFnb0GOqUBhH2UUqYFjVWBizGi8YmJXRGZfpnf5aXMpkXmJzwRI3p96lbv9wF%2BSvwGfrLosCauP9i3JrcuZY%2BuRFeaPc61jyE650qVb3NOCmxoS1qY69GzRDT1zICK5Ya1xrGkfh5KHBDYK8stkGGgGN9JAX2732wuOzYIhEeCh%2BGi8GS%2BC6XKGHvmmsmwt7cj%2FJgyK5Lxe2QNWcdJ2ffHjWwy1AxaVQoaxD7g&X-Amz-Signature=86806e2c96373234403c2adc89dd279336101ad035c4d74c9c36055e5df69906&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8f1b1d60-cf1b-42b3-9faa-f634c89c3f84/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QVN3ATEB%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T122623Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHQaCXVzLXdlc3QtMiJHMEUCIHkXKTAofNVzcPMLjyro46eCZx3sc%2BI9rSPfuqMiTy8mAiEAsmamMuiRtmTrKZnrw7hng10r0tm6k1xRGlaDAd3G7KoqiAQIjf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPzSSSUigFlm8HaPpSrcA5tBiMHqrOps4x7xMsxdtYaMQ2Hn9reo7%2BLW1%2B3g7rM5dCL8RzmQZVlZbMo8osWiQoAty8IizCItlhm9IAzNR89d1fOwmrmCAOJqM2MwuHLLiOsiO%2F4cl%2FEV71WCtlaYM8RzQB688v1VZfN9DBxq93IFKHnVmzO0T487jttVNqqGBcKSA7Zx7JPm4oxrRJL847a50UA2DP%2BzP%2FlsTPY8ijHQKG99m1RUsZTtwpBhpIfW107bpqzIOsEqbysb8UrKHL6qrce%2BNSxluZ8IQh8GiXHkqIVcdUYw2ttWhQWFvaGWeFCEt8E21j9ocxWkfNEaYtR3KfAo4c98erprm1WdYHpzZgDsUvffgcM3SX6vnCGh7yr%2BmGrqMfDZA12S7eaTv9oplkaHe6Aa0pc0pL1DvjIPDCUqOtaMraQapa3Hp0kQV4rt%2F5CzcHYCeUuyfNNZK1Bgh4yMbnvgWDPIuwVo%2FRKUE8rkFYaRN9%2BmmtvLVhcC3RCfgA1p0H%2BDDlfp5DqvUAm%2F85v8oqjIneA7OOzFH5kt8Y%2BGoidLfzE%2F97Nxe3mWdSPvMUbQ%2BXuxYgVbEbq6fvjfNLTgFTmY%2B%2BPIU%2BKioYJHZgxQrIch4TkautLHxSTU7EeO5RhUbWhkKEqXMPaFnb0GOqUBhH2UUqYFjVWBizGi8YmJXRGZfpnf5aXMpkXmJzwRI3p96lbv9wF%2BSvwGfrLosCauP9i3JrcuZY%2BuRFeaPc61jyE650qVb3NOCmxoS1qY69GzRDT1zICK5Ya1xrGkfh5KHBDYK8stkGGgGN9JAX2732wuOzYIhEeCh%2BGi8GS%2BC6XKGHvmmsmwt7cj%2FJgyK5Lxe2QNWcdJ2ffHjWwy1AxaVQoaxD7g&X-Amz-Signature=2eb651edc6f1bd20d993ab0cdd2c840aba4a46aa9942797f29d0edb9b13fd2e6&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/13ad0497-05fe-4eaa-984e-707b33e14761/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QVN3ATEB%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T122623Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHQaCXVzLXdlc3QtMiJHMEUCIHkXKTAofNVzcPMLjyro46eCZx3sc%2BI9rSPfuqMiTy8mAiEAsmamMuiRtmTrKZnrw7hng10r0tm6k1xRGlaDAd3G7KoqiAQIjf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPzSSSUigFlm8HaPpSrcA5tBiMHqrOps4x7xMsxdtYaMQ2Hn9reo7%2BLW1%2B3g7rM5dCL8RzmQZVlZbMo8osWiQoAty8IizCItlhm9IAzNR89d1fOwmrmCAOJqM2MwuHLLiOsiO%2F4cl%2FEV71WCtlaYM8RzQB688v1VZfN9DBxq93IFKHnVmzO0T487jttVNqqGBcKSA7Zx7JPm4oxrRJL847a50UA2DP%2BzP%2FlsTPY8ijHQKG99m1RUsZTtwpBhpIfW107bpqzIOsEqbysb8UrKHL6qrce%2BNSxluZ8IQh8GiXHkqIVcdUYw2ttWhQWFvaGWeFCEt8E21j9ocxWkfNEaYtR3KfAo4c98erprm1WdYHpzZgDsUvffgcM3SX6vnCGh7yr%2BmGrqMfDZA12S7eaTv9oplkaHe6Aa0pc0pL1DvjIPDCUqOtaMraQapa3Hp0kQV4rt%2F5CzcHYCeUuyfNNZK1Bgh4yMbnvgWDPIuwVo%2FRKUE8rkFYaRN9%2BmmtvLVhcC3RCfgA1p0H%2BDDlfp5DqvUAm%2F85v8oqjIneA7OOzFH5kt8Y%2BGoidLfzE%2F97Nxe3mWdSPvMUbQ%2BXuxYgVbEbq6fvjfNLTgFTmY%2B%2BPIU%2BKioYJHZgxQrIch4TkautLHxSTU7EeO5RhUbWhkKEqXMPaFnb0GOqUBhH2UUqYFjVWBizGi8YmJXRGZfpnf5aXMpkXmJzwRI3p96lbv9wF%2BSvwGfrLosCauP9i3JrcuZY%2BuRFeaPc61jyE650qVb3NOCmxoS1qY69GzRDT1zICK5Ya1xrGkfh5KHBDYK8stkGGgGN9JAX2732wuOzYIhEeCh%2BGi8GS%2BC6XKGHvmmsmwt7cj%2FJgyK5Lxe2QNWcdJ2ffHjWwy1AxaVQoaxD7g&X-Amz-Signature=3fd1ecec10a65d5059b6ec4b3cb5dbb97cff2945429ee1e2e06396db0f7f3840&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 2. Box and Whisker Plot
A box plot shows the distribution of quantitative data in a way that facilitates comparisons between variables or across levels of a categorical variable. The box shows the quartiles of the dataset while the whiskers extend to show the rest of the distribution, except for points that are determined to be "outliers".
**Syntax:**
```python
sns.boxplot(x='header_1', y='header_2', data=df)
```
**Example Output:**


![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d207ae92-0a7c-4e2f-aa65-0ee5a2c33bf7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YC4ACJNG%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T122625Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHQaCXVzLXdlc3QtMiJHMEUCIEnqyMiP5Pr23wAUVUZvhmxtMKGVVeDSb%2BB48rsrHaWHAiEAn8X9etC%2FUCLZH6SKVP8o9OpEjysZGG2lmF5mebF1Lg8qiAQIjf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDI7GH4OAs%2FouRQyacyrcA5PWPSpYJjf95OJBcdA8m1uqW7Q6beO0Sz4f%2FrJ%2FNqtAZsW%2B33pwAhrqHF4HEU8PwIia5p5ZW5WlB581tg94sF3Rw7rr2OgH7ApqU4ZFY6518STN7bHHFdgUZGYQV9iwRX8aSCUuweFVzpYO5uijJ9T%2Fm1TbX6CzTRDvPOzHmtU2O9BJCICU7m20NEjVhl%2FRIuBHc3EUc163nhhGQZkl9xTjbmyFE09Vmsex3ue5zZbjZnkfe7qzXjFcdNTV8wci%2BKT8m%2Bm%2FoUOVAEfjOAmyJsaMrt%2BQLLn%2BvX2L2lRLfZlHD4vMuarjAqD5WWL0%2Bfq9I5MNHb%2BPUSSmcE9KiRWq0NYKLbKye3cJpmo2owJK9Fw0xJRXixe3Rz7TvP1g4ZgNqYDk%2B0PecrQS0jY%2B1JYNPSmHc2Snn3Wfhq1%2F87Go42iISMgtfDc6r44oksbUZIPVw5gVF5b0eTBNDy06suT9xhr3fMG8%2Bw%2Bjl%2BMH5BUMzR%2BUXUiC4M8s0ckFRb4VYWfmXKFSp0R8Ol2t%2BWZr5ghNbYwIzbdqYTv4WsB2Dz%2F4NIC9UHzWMvlxMgV0wox%2BI%2FbgAUvsh80scgURVZISUiDxMiY1oopzwqZjeoy1eChHSmzSOsP%2F78k7yeF%2FnQY2ML2Fnb0GOqUBIvrqpwNv3vFoqnJwkjfAKs2oKj%2FS3ceQac4FOiFsjjVZS6mz0e1e%2BFctXXKTB24SnK1q4prRywCMbXWZ4g59dIFOedGLOw21s1Qt6yrU2JIAxQ7BjfYXrhzCR0CF7QyIh%2FbaLCUImq6mnUdbSIuKAYGbjycWsARhHKuJ8Ks%2FPRFYZqiGCk1JBs3uDZdH4b4veHMyyVE65WJaut9z6kOobWuzeNk8&X-Amz-Signature=d8a2ad42dcfc8fb09b520294edbda979ec1e54bc7459ea401a2b637f208cad1f&X-Amz-SignedHeaders=host&x-id=GetObject)

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0e516edc-7551-4792-ab18-0494db3c4c0c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XEYYXA6A%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T122625Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHQaCXVzLXdlc3QtMiJIMEYCIQCpHWLgnCEKvpYZHNC0zhq%2FFmb2LemK%2BDoFHA6j6lQhCwIhAMivcUyPMM%2B30kqejurUUGWHoEp4q3pPippK1enncIF7KogECI3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxasArTqX5kUlbqNdsq3APxRSoYw64kAp3KmvrxZin%2BiHWAQuNDPbFLbTgFy0Mw%2ByEyZ28iwvM2h9K82bP1USRT0Qk5TOcUPvDCkl6%2B2Sv%2BTOD%2F4pT%2BCbVF1ctx2AhP1iLJ5jtFd7nnfd3fAX8sFWgd4hoarWpVXoPnwJ7ydR7X5AWnZDmIlkW%2BPVV40WvdNoM7oo0FMNGc0tkZSKd9r3Af%2BECXVO8ktNA6S2DsMFZt8TgEmJ2daSaPktt8I0P1um7xRa1fKtDGK9cdu664%2BH7OCvI0gX4F10jxbo6e7P6fzh9dsCfhzcfjBPDM8CURlYwj4bnJ9dE4loJA6H9nNRFcdgm5ZQ722YgotQ%2FqTih90ncq5zTLTG9Es2DIosMk2N4k0SIT3Nz6XLrvD%2FJPEHzzf9zgYnP6o3rhmHVE804MXHLCxgSyopBQh%2BdAbodtaZz9NqTc76YofO2eb8DreXscOSrsH9Agp4chAt5JZKcMnnF0YGgnDk%2BZdV0o%2BrXAXOiyerJQW9yaY6Rpq2ScqbrQKZnrILoQiCZ4ERqvW7DpaDgfvCHTRPFJ26Pk9vdtPwOQAs64g9gwO7rgFCqZ2nFU26PN6%2B46vlpK3pIpGjb9q8YEm2gPLVnmyRT1RMooiWn6E4v4eG%2BOGHx2SjCphZ29BjqkASqIiD4cbhfU7ySRGqG3batlhHT5SXzBu6SSAJabky9207Uq6skGB8vkV3w2HuEjaMbO2Yk7MpuktqTP3a%2FdaUTKLwjz0VSBeiMmfD8AZleftszk%2B9Kif15r86arvFabOMV7BbHI7HSWSGHzfhd3IaMlmkh%2BYPBJZm5wIOerLwvndTG3FpI2aKJnkDqiOwEWDFNK81b00e9P6UpjyowzPHE67FB4&X-Amz-Signature=cc5a9e38d0dc45773c21e078faa5805cbe0727e35a308cc580bfdcbc1bd60272&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23a79b9d-2356-49a9-8fd9-65c6b0ab2cc5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QVN3ATEB%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T122623Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHQaCXVzLXdlc3QtMiJHMEUCIHkXKTAofNVzcPMLjyro46eCZx3sc%2BI9rSPfuqMiTy8mAiEAsmamMuiRtmTrKZnrw7hng10r0tm6k1xRGlaDAd3G7KoqiAQIjf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPzSSSUigFlm8HaPpSrcA5tBiMHqrOps4x7xMsxdtYaMQ2Hn9reo7%2BLW1%2B3g7rM5dCL8RzmQZVlZbMo8osWiQoAty8IizCItlhm9IAzNR89d1fOwmrmCAOJqM2MwuHLLiOsiO%2F4cl%2FEV71WCtlaYM8RzQB688v1VZfN9DBxq93IFKHnVmzO0T487jttVNqqGBcKSA7Zx7JPm4oxrRJL847a50UA2DP%2BzP%2FlsTPY8ijHQKG99m1RUsZTtwpBhpIfW107bpqzIOsEqbysb8UrKHL6qrce%2BNSxluZ8IQh8GiXHkqIVcdUYw2ttWhQWFvaGWeFCEt8E21j9ocxWkfNEaYtR3KfAo4c98erprm1WdYHpzZgDsUvffgcM3SX6vnCGh7yr%2BmGrqMfDZA12S7eaTv9oplkaHe6Aa0pc0pL1DvjIPDCUqOtaMraQapa3Hp0kQV4rt%2F5CzcHYCeUuyfNNZK1Bgh4yMbnvgWDPIuwVo%2FRKUE8rkFYaRN9%2BmmtvLVhcC3RCfgA1p0H%2BDDlfp5DqvUAm%2F85v8oqjIneA7OOzFH5kt8Y%2BGoidLfzE%2F97Nxe3mWdSPvMUbQ%2BXuxYgVbEbq6fvjfNLTgFTmY%2B%2BPIU%2BKioYJHZgxQrIch4TkautLHxSTU7EeO5RhUbWhkKEqXMPaFnb0GOqUBhH2UUqYFjVWBizGi8YmJXRGZfpnf5aXMpkXmJzwRI3p96lbv9wF%2BSvwGfrLosCauP9i3JrcuZY%2BuRFeaPc61jyE650qVb3NOCmxoS1qY69GzRDT1zICK5Ya1xrGkfh5KHBDYK8stkGGgGN9JAX2732wuOzYIhEeCh%2BGi8GS%2BC6XKGHvmmsmwt7cj%2FJgyK5Lxe2QNWcdJ2ffHjWwy1AxaVQoaxD7g&X-Amz-Signature=e8e63de4b654e6cfe28bb82e7533fd4c0ec453377092ac7ee8c61911cff22820&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 4. KDE Plot
A Kernel Density Estimate (KDE) plot is a graph that creates a probability distribution curve for the data based upon its likelihood of occurrence on a specific value. This is created for a single vector of information.
**Syntax:**
```python
sns.kdeplot(X) || sns.kdeplot(df['age'])
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0d571213-2a2f-4921-a50b-880847aa05ee/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QVN3ATEB%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T122623Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHQaCXVzLXdlc3QtMiJHMEUCIHkXKTAofNVzcPMLjyro46eCZx3sc%2BI9rSPfuqMiTy8mAiEAsmamMuiRtmTrKZnrw7hng10r0tm6k1xRGlaDAd3G7KoqiAQIjf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPzSSSUigFlm8HaPpSrcA5tBiMHqrOps4x7xMsxdtYaMQ2Hn9reo7%2BLW1%2B3g7rM5dCL8RzmQZVlZbMo8osWiQoAty8IizCItlhm9IAzNR89d1fOwmrmCAOJqM2MwuHLLiOsiO%2F4cl%2FEV71WCtlaYM8RzQB688v1VZfN9DBxq93IFKHnVmzO0T487jttVNqqGBcKSA7Zx7JPm4oxrRJL847a50UA2DP%2BzP%2FlsTPY8ijHQKG99m1RUsZTtwpBhpIfW107bpqzIOsEqbysb8UrKHL6qrce%2BNSxluZ8IQh8GiXHkqIVcdUYw2ttWhQWFvaGWeFCEt8E21j9ocxWkfNEaYtR3KfAo4c98erprm1WdYHpzZgDsUvffgcM3SX6vnCGh7yr%2BmGrqMfDZA12S7eaTv9oplkaHe6Aa0pc0pL1DvjIPDCUqOtaMraQapa3Hp0kQV4rt%2F5CzcHYCeUuyfNNZK1Bgh4yMbnvgWDPIuwVo%2FRKUE8rkFYaRN9%2BmmtvLVhcC3RCfgA1p0H%2BDDlfp5DqvUAm%2F85v8oqjIneA7OOzFH5kt8Y%2BGoidLfzE%2F97Nxe3mWdSPvMUbQ%2BXuxYgVbEbq6fvjfNLTgFTmY%2B%2BPIU%2BKioYJHZgxQrIch4TkautLHxSTU7EeO5RhUbWhkKEqXMPaFnb0GOqUBhH2UUqYFjVWBizGi8YmJXRGZfpnf5aXMpkXmJzwRI3p96lbv9wF%2BSvwGfrLosCauP9i3JrcuZY%2BuRFeaPc61jyE650qVb3NOCmxoS1qY69GzRDT1zICK5Ya1xrGkfh5KHBDYK8stkGGgGN9JAX2732wuOzYIhEeCh%2BGi8GS%2BC6XKGHvmmsmwt7cj%2FJgyK5Lxe2QNWcdJ2ffHjWwy1AxaVQoaxD7g&X-Amz-Signature=b6ce2b8214e7f0f50012e27f3982e7093fcd40e0c916a500ffebcb2d0ab67b74&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/53752550-ef82-4ca9-a01a-09921f0282d0/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QVN3ATEB%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T122624Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHQaCXVzLXdlc3QtMiJHMEUCIHkXKTAofNVzcPMLjyro46eCZx3sc%2BI9rSPfuqMiTy8mAiEAsmamMuiRtmTrKZnrw7hng10r0tm6k1xRGlaDAd3G7KoqiAQIjf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPzSSSUigFlm8HaPpSrcA5tBiMHqrOps4x7xMsxdtYaMQ2Hn9reo7%2BLW1%2B3g7rM5dCL8RzmQZVlZbMo8osWiQoAty8IizCItlhm9IAzNR89d1fOwmrmCAOJqM2MwuHLLiOsiO%2F4cl%2FEV71WCtlaYM8RzQB688v1VZfN9DBxq93IFKHnVmzO0T487jttVNqqGBcKSA7Zx7JPm4oxrRJL847a50UA2DP%2BzP%2FlsTPY8ijHQKG99m1RUsZTtwpBhpIfW107bpqzIOsEqbysb8UrKHL6qrce%2BNSxluZ8IQh8GiXHkqIVcdUYw2ttWhQWFvaGWeFCEt8E21j9ocxWkfNEaYtR3KfAo4c98erprm1WdYHpzZgDsUvffgcM3SX6vnCGh7yr%2BmGrqMfDZA12S7eaTv9oplkaHe6Aa0pc0pL1DvjIPDCUqOtaMraQapa3Hp0kQV4rt%2F5CzcHYCeUuyfNNZK1Bgh4yMbnvgWDPIuwVo%2FRKUE8rkFYaRN9%2BmmtvLVhcC3RCfgA1p0H%2BDDlfp5DqvUAm%2F85v8oqjIneA7OOzFH5kt8Y%2BGoidLfzE%2F97Nxe3mWdSPvMUbQ%2BXuxYgVbEbq6fvjfNLTgFTmY%2B%2BPIU%2BKioYJHZgxQrIch4TkautLHxSTU7EeO5RhUbWhkKEqXMPaFnb0GOqUBhH2UUqYFjVWBizGi8YmJXRGZfpnf5aXMpkXmJzwRI3p96lbv9wF%2BSvwGfrLosCauP9i3JrcuZY%2BuRFeaPc61jyE650qVb3NOCmxoS1qY69GzRDT1zICK5Ya1xrGkfh5KHBDYK8stkGGgGN9JAX2732wuOzYIhEeCh%2BGi8GS%2BC6XKGHvmmsmwt7cj%2FJgyK5Lxe2QNWcdJ2ffHjWwy1AxaVQoaxD7g&X-Amz-Signature=670e618dabb59e1604f7bbe85ca1dcd2f6b3e1f10f41431194ae0f9db8913ccd&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
## 4. Correlation Between Variables
Correlation is a statistical measure of the extent to which different variables are interdependent. It indicates how changes in one variable are associated with changes in another variable over time.
### Positive Correlation
Positive correlation indicates that as one variable increases, the other variable also tends to increase.
**Example: Engine Size and Price**
- **Positive Correlation:** Engine size increases, price also increases.
- **Visualization:** Scatter plot with a steep positive slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c7ea9b0-3ef3-4357-a9c3-554fc71b6b15/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663TQKNBO7%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T122624Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHQaCXVzLXdlc3QtMiJGMEQCIGAAnHLoUiaBdF3s90DaZpRC1kFhgDDNfhe9SSBCQlE5AiAjr3x1CfLrNKTNTgytx50PA19VAeRKvAvJ3wAMUVZmIiqIBAiN%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMILZ2D4G5Ni0tjKt%2FKtwDll1qub8eAGkiVU0mLPUJ%2F%2BJFPaP2khYijIlV27dLNmT%2FEOA69LhUrCIwTQvQFBK%2F5Q1DXW5dl%2F6u1V8GL8QZ3Uy1dkQhp9kDcjtl6EXAi%2BHpEvWvmLze1HX17QBStCaeW%2FRPQ92ojqri52j99d4uyExTdVA%2B2ZaLEmsMa%2FnSbttlI2V%2BxFn7B%2Bj56a%2BOwhnWvxQ1tBVzG9AOGylRXU00u8zr0oipU5m%2FtPEJIem4%2BhQ6hxAf3rl%2BDX0yjavIBp6plwXZAjKumojdr3CJmzn3UpAxG8GJFtQNwBFSqU%2FoVUT1WSJ%2BzLqNOQPuHaAICA8GsI4Pgxq6np13vfL%2BuSf0uUUZcjsRR1cafqYm5E0kBhsNf92g72sKYCwwb5YYPd6%2FXCCWli9UIG87yStHKVQymFMPS28nz1adVLBrzLNhX5cPOMz1CcOa1Oua2Yzzufg7hy6IJQvVUltcu27Kdi5DIBvXuBhyR%2BN2nS9zdM%2Bf4K7g7OW4o%2FhEEhbVzhPmE2diE3dvYkhgPjJ1QuwMl1P6KY9tc2FDmo8%2Bb%2BsWJ9IoNfP5nIk5KoCqT4qCkrWLZYPlRM%2FgpIzfkcctzGClc8luM9wXfjk26hWVtit7v3EZiAUqMD4OKnjoO8TQh8QwqYWdvQY6pgExi4tRVBMRRv5S5C2LtrYM8%2BnRanLz7fridWKEjfU6Ppbnl2yFhsgtlt959irqwdlb5y7op1XeiL%2BWAIHFnw5sj1elcalH5pxVWLeoFCULnHP4ZGpmxxx1GOW%2BPJkjxgEYb106EWWIXsBXXIRV92uELJ8HkYXXYxmNDkn22to6E6AT2udFP6jm%2FapbL9LGNcer%2Flo7nvyoVSgnJjgAUz3Tm1G5HmK5&X-Amz-Signature=ef532d587c564d3225236b83b98f6b67f6ca74b75574c13f2275c5d2d4cf9eb6&X-Amz-SignedHeaders=host&x-id=GetObject)
**Explanation:** When engine size increases, there is a corresponding increase in the price of the vehicle. This positive correlation suggests that larger engines tend to be associated with higher prices in the market.
___
### Negative Correlation
Negative correlation indicates that as one variable increases, the other variable tends to decrease.
**Example: Highway Miles per Gallon and Price**
- **Negative Correlation:** As highway miles per gallon increases, price decreases.
- **Visualization:** Scatter plot with a steep negative slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/10f1f798-9cc4-4df2-a9c1-5a339f554a0b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466227NSXYF%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T122624Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHQaCXVzLXdlc3QtMiJIMEYCIQDpSAD4SO04QhesdOs2EdeStXYqY4WgiUYMZFclMQKCVQIhAIvrXS2xZuEgHpGOZKVV8HvJZe8uFGY2j5uyjNAOIgJpKogECI3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzxR%2F%2B1eWhfPSod1uoq3AMf86I7hKgCSiZp1EXc%2F4o%2Fl1GhzFUefcrwrwAEQWaGkMljvFbMWDz2fVeK5ofNnD4FzAJwIGMQg4Q73qCrZDdV187RPQ6bg1shwFzHN%2BPtx6o1pPASEMvsMGb9tegJof2CCna5hte8IlPJCgwH%2BaQ%2BLFVmlRy5Lq%2FF73MQXZv%2BTWzvBudmk4%2F09DI5umqK3X6UBo%2FjI6OhjK8nRUUwqNmFVAmid3DmnpXnu%2FUEit%2BJJA5QOPHBbeyGZB9hZcl%2BIWdeQRX%2BXR3kYhET5lV9ynOcWUzXFX9KptTMlhCgw5Sp7IE3wDRIcmeopTGzHBzwAy8tip64EoSPRwRxtMBVDXMqi4R4k8%2FDhq2%2FMF3XS5wwZXVmZxp2em7quWyiFE9M9yKIxfbjWZW2ssmHzVIGIo%2BcnogZkM2p3ziHtJx1iBXW1CGOkJ5u1AFJbP0XTnaXvh1BTk888iohoWEDWoiNZl%2F8x1sjjMRR90m9orPIRq9sbDEH5utQc%2B9bFjSigcAmc3s16rIZbVmA7YW%2FNc5nd%2FAf%2FqVMTn%2F3YC1kmz0gE07aYcdg0FiN0GYd%2FSuyjKgxG0fFah7Oaf%2F9NGnzeXX9UOAa9xE2KoXg5U830NYA40udPrL3ZV2qeIKLYbC8ZzCAhZ29BjqkAfgqFfdrV2husgD1IPQz%2F4B3blWbYgYVYgN%2BhT%2B7MOypaGIBaqZJtJF%2Fr6HXiYQbvOkpTzvp%2FOugngkLM02fwLtT%2Fmq5toHUlZDFBA0lDgwyxGC%2BaJaXDtdJjqb7tkmZlFk5dDzTn7MZ0iOOFvJbUh67yPhz1JPFJMO26FH05UU6%2B6Bg%2FaOO30kDcogiRlg1pmYp7O53FgdFCFO3wwPg7B%2Fb87id&X-Amz-Signature=859ef2414ae0b6eae7b92b3afbc74928afe8a8bc61e865758aa63a68f30c4aed&X-Amz-SignedHeaders=host&x-id=GetObject)
**Explanation:** When highway miles per gallon increases, the price of the vehicle tends to decrease. This negative correlation suggests that cars with higher fuel efficiency (more miles per gallon) are generally priced lower in the market.
___
### Weak Correlation
Weak correlation indicates a lack of strong relationship between the variables.
**Example: RPM and Price**
- **Weak Correlation:** Low and high RPM values show varied prices, indicating no strong predictive relationship.
- **Visualization:** Scatter plot with no clear trend or slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9f914514-8914-4bf4-ac84-d9e3077f6eb1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VWFCKWYQ%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T122624Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHQaCXVzLXdlc3QtMiJHMEUCIHxauCjSTjLjU8idTg3vgTtkoyPSnco%2F8oPkGTn4tldOAiEAx2wC44phzq4z0umt8fq2qCFdE90ZcsKyPfyVPPdJdAQqiAQIjf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGgRMECOqkWVXoEOvCrcA6JRvRmvfIExvCsBbMMKC5cIR6WQF1%2FuAwd%2F4muWvH02j3eIhu39XF2KMfnyVSfM%2BMmJbiqpHID%2FM9Cng1hYhXV2z%2Beu6EYIrOMyGeLvHrfBIZmrOcxHSn%2FrYDS1KxHgHkKwCQC5rcPb6aJqALsFGp9qF56y%2BOYlP7amvv1VyujgnZLjK0ZCLZvaR2f0AQP4LJMrUmcs2z8xpHGQnTrtN1g8c58Wek554Rcjt6s3xWk1%2FUIPN5eNEIxldaEGPk3w6Qupkejilee4TGq2AK5D4q30N9Fz4BwqXnYUwR3LN8IPAUW%2Fuo7NK15ld50R06RpKGZVQf2ewVO1XpoDhksCGQV6s8zJU%2F%2BCV7gqc6c%2B42dxQUVSDRJpJx8f1Hj6L3zvAP35BZRgntf4osQeveqGFPvSWYxari4s5BH3963yvkvSGAl7esl%2Bn7Vj2D%2F7HVp0QCw1rUYPL8514r8VIEvRgE5Hg6p3f2Fcct0l6cX0RGz89h0KX6Ejh3Wwmg8G3oFV80hNpqL0CFLsTGKUS6up2T3RqQsD4axBERrGyXiZAU%2Fgm6mUzUziWhvDTznD2hGUP7SXE6KEPirGDOtX3Utl8bjuqL2lyk0vBBo9%2Fcol5wDrjSfxmV0GajbOxpYfMKKFnb0GOqUB0jemHNZMmztSj8YLI%2BzzSqbDUNeiZJwlOLxKKtx3yDKByet3UVJDw4C69uegAEJmSla1OD4iscu%2Bskamw4du2XWKaAA83cEKVfWTz1CQ8ZIwn8LVLNYlLrzcsWQA%2Bob31x8PEdenqluIjvcunJoGCH0s9Rj6OCYBowmvHTmd3cZ%2F%2FaJg4cWxV504x2PWlsgac2nwO37T2v8H%2BKB%2BGr2bpn1kN5Uo&X-Amz-Signature=8e0619e60942b7fc798bb0dca12b8a65c5f5a54503fa6e32e3fa1bc51eb7900b&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f18086e5-5b04-4fbf-8309-8944ab20d213/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UCCTIF6C%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T122624Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHQaCXVzLXdlc3QtMiJHMEUCIQCtFrjDA2%2F1iBv0OCsdTwud9I6IopSZvHF2yDl73KNPTAIgZqy2dPTRg9xTNw1ImbQ18oMHyNRlTelcw4McSvooEagqiAQIjf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDH6fxOJ4UZ%2Fy4FH0ACrcA0khiEczE3elIFU%2BhxXBrDggLF%2Bgc3Pk5sic%2FVJ46OBGlKtcql2TJecHXm%2FFv9Az539haEAvco5blCyYbMPxCUTqd0fqkvk2WD1bLj6PHMqqUg1nlrpmLchn7lt8s%2B83aHn2giPVcqSnyQhRWWQO5bkGX4rgNueB%2Ba8ayi6aOZWaxKa6N%2BuirEQSsJpuBzLCeuzJ6U8jbAfHurCWyMHlldyVDcJwSKuiR3iokfVNEwamVk2GnstTr3zY2zjMpkqbUVs0Qw6p%2BpzUSMOIzBl20CC9XpG5RqMxMqVD7okTvqxMSxMy6nZlKG7E3PF7D1uYHnjgdzpncvlUUBn32cM3BbjgsoSaGwNvA2oHOei6mDiVRFqf%2FKLopXvdY2ZQI8HWK6xo9CG7u6pS8vvrOnRjgUqNtFtd%2Bn04VFtE8y%2BQvIwKK0iSlCWces%2FnofuNsqq8tljrF0xW1817oeYHzJGeUwvk%2BdeoOw4m%2F8B%2BdlVz4EfvmjfM26JeOqYo30a9pjAdQ6Ud355e1xzLvxu8eAkDdIJh0bjojkd2tfHskvrchLcmVS96n4QeHTH0lbmjMce3UCPRMQgzfh88ONDZvMFJSEwDCedExwe%2BaUxDyIPa9zlRu3lUtKvIdj0TqQspMMKFnb0GOqUB1cEdu%2F4S99nIfThWkcXX78Rc7VHpPmv50A4AgYBRhTVXIHE8LD5NXWng1vkb9FJRCWrYmwCDHCVpB%2FtBtyiuNo20deCpjg8K271IesmozEfKnAmjw%2F%2BwqxCSjZAIRRbcnxpEKV9iQ%2FWCZZ9fxY5UBUTjMgaqDtPDA2rXUD3kPIrOjCBrMj5WkWpokhz8QbczNbUm4BOA0DSyRvdKnizyuZtiS8k0&X-Amz-Signature=40797eae84c417bd0cf44f13200564dd7a96c2140967a483a57e9afe31dc9561&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Correlation Plot
Heatmap visualizes correlations among variables. Color scheme indicates Pearson correlation coefficients. Dark red diagonal line shows perfect correlation (value of 1) between variables and themselves.
This heatmap offers overview of variable relationships and their link with price.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cd3b341e-cc1a-45f7-8aec-cdc00436d270/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UCCTIF6C%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T122624Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHQaCXVzLXdlc3QtMiJHMEUCIQCtFrjDA2%2F1iBv0OCsdTwud9I6IopSZvHF2yDl73KNPTAIgZqy2dPTRg9xTNw1ImbQ18oMHyNRlTelcw4McSvooEagqiAQIjf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDH6fxOJ4UZ%2Fy4FH0ACrcA0khiEczE3elIFU%2BhxXBrDggLF%2Bgc3Pk5sic%2FVJ46OBGlKtcql2TJecHXm%2FFv9Az539haEAvco5blCyYbMPxCUTqd0fqkvk2WD1bLj6PHMqqUg1nlrpmLchn7lt8s%2B83aHn2giPVcqSnyQhRWWQO5bkGX4rgNueB%2Ba8ayi6aOZWaxKa6N%2BuirEQSsJpuBzLCeuzJ6U8jbAfHurCWyMHlldyVDcJwSKuiR3iokfVNEwamVk2GnstTr3zY2zjMpkqbUVs0Qw6p%2BpzUSMOIzBl20CC9XpG5RqMxMqVD7okTvqxMSxMy6nZlKG7E3PF7D1uYHnjgdzpncvlUUBn32cM3BbjgsoSaGwNvA2oHOei6mDiVRFqf%2FKLopXvdY2ZQI8HWK6xo9CG7u6pS8vvrOnRjgUqNtFtd%2Bn04VFtE8y%2BQvIwKK0iSlCWces%2FnofuNsqq8tljrF0xW1817oeYHzJGeUwvk%2BdeoOw4m%2F8B%2BdlVz4EfvmjfM26JeOqYo30a9pjAdQ6Ud355e1xzLvxu8eAkDdIJh0bjojkd2tfHskvrchLcmVS96n4QeHTH0lbmjMce3UCPRMQgzfh88ONDZvMFJSEwDCedExwe%2BaUxDyIPa9zlRu3lUtKvIdj0TqQspMMKFnb0GOqUB1cEdu%2F4S99nIfThWkcXX78Rc7VHpPmv50A4AgYBRhTVXIHE8LD5NXWng1vkb9FJRCWrYmwCDHCVpB%2FtBtyiuNo20deCpjg8K271IesmozEfKnAmjw%2F%2BwqxCSjZAIRRbcnxpEKV9iQ%2FWCZZ9fxY5UBUTjMgaqDtPDA2rXUD3kPIrOjCBrMj5WkWpokhz8QbczNbUm4BOA0DSyRvdKnizyuZtiS8k0&X-Amz-Signature=47546cb46e1873d0bf83e34807c35ba7c3868c72fcc84f8412094286e8a99bc3&X-Amz-SignedHeaders=host&x-id=GetObject)

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
