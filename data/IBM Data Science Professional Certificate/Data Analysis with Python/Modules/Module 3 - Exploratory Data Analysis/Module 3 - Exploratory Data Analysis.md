

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7e6d594d-952e-44b6-97ea-31225882aea6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TQVD6UPR%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T221427Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCO9XSJyIVADlygD3atvVdKhX64r8M4zcqbVeHZpstpjAIgZLhxJeMrHdtfJEFXxthU23d5lCfsVgIYBewC8AI9SWUqiAQI3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPlVn7SdmjTZqMw5FyrcA4biVRZqh4rxRu7GqF1C957W1LB21hvTXkQMEgAMDXO6AH1xDeqyEZrgyKoNcVaI00l%2BCdHXq5shkK7CJE0h33kuDgP1RAkxTJAzKcCMpgC5s5rELH2i0BqcHIETXEvNntVBmKAF%2BVMH6LRFYyj19i1c6LQoP6VTMNgUf2L6lEyKZ1d5ywuuBIQ124MX%2B5POLr%2BQqiTG4y5%2Bogj5v3K2%2BikStOcmne57f1SBGjk6EX4V1CJF9pnohAHoKXLL0oHiVr%2FH1gt8xHDkahQC8V7hM233oPH%2FYIhOot0nt%2BS1a0GD8k8ej5qxZz%2FGZbdOrDE6evArLnfF88S%2FQc53p00lSIztw73QH9dSD9YJAL1oDZV5ARbfKLrqK8VSCpjJYyHFGpaL85h8rzGHcgBoQe7MVZsygst7KETNc1LDRPVIwEXlKE5zeXJmblAvc5CMFJHNYsGVNM1UYaL73kQLPqcDMlHbha%2FCaAE4S3wTnDYI1jJWd7RJ8u97ndeQMMZciuItvW70Puzq0VBzA2rNXErf%2FAMKzThNhDbhMrndUVUkgEKVCPuZOey9n29x75u5s%2F2RTSN9059sT9fuL4GcLZ65ahPcL2edAkTRRPUO%2BRnsXef8Qebm4VGKut7yzK6wMLOx%2BrwGOqUBmMDmpyUZq9S19XpaWPqSyewEOu%2FevDrRO1JzC0pbnzeg2nPo3OSYkjpXKS75xxZdfPeVfGr%2FWSfygbYWBUUL%2BAWvF0xDpskAhQ3P78UBmqR7GUWNBfNVE%2FkjvnE91Z0wGrAZyo6ur%2BMQGuMui9HE6tyLZYsua1p%2FqlW5U7OP4wMle09iZJrnqw8%2BvzItzP4LtisWUY8q5KoRZq%2BG4sWbn3bQgyOb&X-Amz-Signature=c18a1e68c6cb7200be386ac89e20c61cafa50c41ce455ebdae2f6c2a8c890907&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cbfaed9e-b398-4902-8936-dea058b21def/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TQVD6UPR%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T221427Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCO9XSJyIVADlygD3atvVdKhX64r8M4zcqbVeHZpstpjAIgZLhxJeMrHdtfJEFXxthU23d5lCfsVgIYBewC8AI9SWUqiAQI3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPlVn7SdmjTZqMw5FyrcA4biVRZqh4rxRu7GqF1C957W1LB21hvTXkQMEgAMDXO6AH1xDeqyEZrgyKoNcVaI00l%2BCdHXq5shkK7CJE0h33kuDgP1RAkxTJAzKcCMpgC5s5rELH2i0BqcHIETXEvNntVBmKAF%2BVMH6LRFYyj19i1c6LQoP6VTMNgUf2L6lEyKZ1d5ywuuBIQ124MX%2B5POLr%2BQqiTG4y5%2Bogj5v3K2%2BikStOcmne57f1SBGjk6EX4V1CJF9pnohAHoKXLL0oHiVr%2FH1gt8xHDkahQC8V7hM233oPH%2FYIhOot0nt%2BS1a0GD8k8ej5qxZz%2FGZbdOrDE6evArLnfF88S%2FQc53p00lSIztw73QH9dSD9YJAL1oDZV5ARbfKLrqK8VSCpjJYyHFGpaL85h8rzGHcgBoQe7MVZsygst7KETNc1LDRPVIwEXlKE5zeXJmblAvc5CMFJHNYsGVNM1UYaL73kQLPqcDMlHbha%2FCaAE4S3wTnDYI1jJWd7RJ8u97ndeQMMZciuItvW70Puzq0VBzA2rNXErf%2FAMKzThNhDbhMrndUVUkgEKVCPuZOey9n29x75u5s%2F2RTSN9059sT9fuL4GcLZ65ahPcL2edAkTRRPUO%2BRnsXef8Qebm4VGKut7yzK6wMLOx%2BrwGOqUBmMDmpyUZq9S19XpaWPqSyewEOu%2FevDrRO1JzC0pbnzeg2nPo3OSYkjpXKS75xxZdfPeVfGr%2FWSfygbYWBUUL%2BAWvF0xDpskAhQ3P78UBmqR7GUWNBfNVE%2FkjvnE91Z0wGrAZyo6ur%2BMQGuMui9HE6tyLZYsua1p%2FqlW5U7OP4wMle09iZJrnqw8%2BvzItzP4LtisWUY8q5KoRZq%2BG4sWbn3bQgyOb&X-Amz-Signature=a8dbf51eb5fd09ac4f98ed0f55e13f1c8210afafb323a00bc2c98b529f2746b5&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/91181646-b1e0-4433-9711-6259a96a9247/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TQVD6UPR%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T221427Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCO9XSJyIVADlygD3atvVdKhX64r8M4zcqbVeHZpstpjAIgZLhxJeMrHdtfJEFXxthU23d5lCfsVgIYBewC8AI9SWUqiAQI3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPlVn7SdmjTZqMw5FyrcA4biVRZqh4rxRu7GqF1C957W1LB21hvTXkQMEgAMDXO6AH1xDeqyEZrgyKoNcVaI00l%2BCdHXq5shkK7CJE0h33kuDgP1RAkxTJAzKcCMpgC5s5rELH2i0BqcHIETXEvNntVBmKAF%2BVMH6LRFYyj19i1c6LQoP6VTMNgUf2L6lEyKZ1d5ywuuBIQ124MX%2B5POLr%2BQqiTG4y5%2Bogj5v3K2%2BikStOcmne57f1SBGjk6EX4V1CJF9pnohAHoKXLL0oHiVr%2FH1gt8xHDkahQC8V7hM233oPH%2FYIhOot0nt%2BS1a0GD8k8ej5qxZz%2FGZbdOrDE6evArLnfF88S%2FQc53p00lSIztw73QH9dSD9YJAL1oDZV5ARbfKLrqK8VSCpjJYyHFGpaL85h8rzGHcgBoQe7MVZsygst7KETNc1LDRPVIwEXlKE5zeXJmblAvc5CMFJHNYsGVNM1UYaL73kQLPqcDMlHbha%2FCaAE4S3wTnDYI1jJWd7RJ8u97ndeQMMZciuItvW70Puzq0VBzA2rNXErf%2FAMKzThNhDbhMrndUVUkgEKVCPuZOey9n29x75u5s%2F2RTSN9059sT9fuL4GcLZ65ahPcL2edAkTRRPUO%2BRnsXef8Qebm4VGKut7yzK6wMLOx%2BrwGOqUBmMDmpyUZq9S19XpaWPqSyewEOu%2FevDrRO1JzC0pbnzeg2nPo3OSYkjpXKS75xxZdfPeVfGr%2FWSfygbYWBUUL%2BAWvF0xDpskAhQ3P78UBmqR7GUWNBfNVE%2FkjvnE91Z0wGrAZyo6ur%2BMQGuMui9HE6tyLZYsua1p%2FqlW5U7OP4wMle09iZJrnqw8%2BvzItzP4LtisWUY8q5KoRZq%2BG4sWbn3bQgyOb&X-Amz-Signature=c3d02f2e1a8625a1e74ecfc30d2935dcd7fc51d586abe1abf10b95bd431a3ae6&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/09aba1c0-0d55-41dd-852a-a04c5b8a3fac/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Y35IU6EL%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T221428Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCtmBMmt3JdkdUCAgUAIU5bfktYaDlunUgG%2ByNnKHHEbAIgaK%2Bz0v1iAMqXZiNHuYVn1FZIagp4TkDnOO%2FBhiIZj5EqiAQI3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDCaIekX%2B5T7gkvdysyrcA6Ma4dKFijnTkSmV7H91E4xht9ioKtHWS9EKFBen6RYcn5TlWFPVok4e4DdDNITY28ePYuGJWwmyRXrZxXLTtwla%2FwBIQqwV36pIuNhRsxL3mfp2WkEIGyLk5iFTU%2BJ5T3dQURi%2FZC5Gl7h%2BM6tB0jbDoQUSg644XEBXI0FQjwHacIjxsfi40AlT%2FMFPkF9GQmyImkVm4S7pUkYWaExIVWxpzyueM6GEYHBmCrKqS1bbOg3RuYTc7jC%2FT9sxs5%2BldsEwelYuvV4mfAz7XGJsZ8WkFkBBaGN8PvHFu6QAdkNNBOS07JqQWaQ3qasZpe4bvL7Srt3ds0eTkBs44yLi4m2dgkQVeFFbke3YQ27Ma4lUEvxQIFZ5caQt%2B1pPautd8pTuP6pcCOW7CVPDLgSmq6qWPQmly%2F6wz%2FDRiHXLoYzaaM4gxHI8A4E0%2FRjzCp%2BtYHA6XJLCb9SVBposuY%2Fx6EFl1WoN0dxEJdZM4YGEtO7EIB%2FwgDgsZdawshD4dd5h%2B%2BAcEMmketmSAvZhwGTPrFUu4OJjcUCm1vCvnxlngP%2B8pusTcOqyKYhE4l5YBM645EFBxeKObk70cSat2Ui7CUQ2RHBKchFP6%2BrcrfrbfulEtiiGMjQyvW9xF3zuMJix%2BrwGOqUBjKtegLZ%2BMBGJwtOQ7kXRzUoYKtjJpm0K3lLkuFIzuqXjDRRv2Aa2telPs0KZ1p2kMdyN%2BwWlENjO2HsOnzCXuxruBNjYbfPIQDcVUSYyEheWJpz8n7tfU0fgnwkPYdz4RCZV7P93CwG%2BJHRQWJppaCTFxTCbuy7lwDCWD78X9ShH8j6Un38%2BVjJn6P8WeiSXfIAQ00p5E8NW1NYDqHA%2FMAylZbQD&X-Amz-Signature=0249de28ba843766ae0c59a122205faa61a2e774cce8e257c0e14fb2d7ae625b&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 2. Scatter Plot
Scatter plots present the relationship between two variables in a dataset. It represents data points on a two-dimensional plane. The independent variable or attribute is plotted on the X-axis, while the dependent variable is plotted on the Y-axis.
**Syntax:**
```python
plt.scatter(x, y)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23708af9-659f-4f23-b626-1a4292d7842c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Y35IU6EL%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T221428Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCtmBMmt3JdkdUCAgUAIU5bfktYaDlunUgG%2ByNnKHHEbAIgaK%2Bz0v1iAMqXZiNHuYVn1FZIagp4TkDnOO%2FBhiIZj5EqiAQI3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDCaIekX%2B5T7gkvdysyrcA6Ma4dKFijnTkSmV7H91E4xht9ioKtHWS9EKFBen6RYcn5TlWFPVok4e4DdDNITY28ePYuGJWwmyRXrZxXLTtwla%2FwBIQqwV36pIuNhRsxL3mfp2WkEIGyLk5iFTU%2BJ5T3dQURi%2FZC5Gl7h%2BM6tB0jbDoQUSg644XEBXI0FQjwHacIjxsfi40AlT%2FMFPkF9GQmyImkVm4S7pUkYWaExIVWxpzyueM6GEYHBmCrKqS1bbOg3RuYTc7jC%2FT9sxs5%2BldsEwelYuvV4mfAz7XGJsZ8WkFkBBaGN8PvHFu6QAdkNNBOS07JqQWaQ3qasZpe4bvL7Srt3ds0eTkBs44yLi4m2dgkQVeFFbke3YQ27Ma4lUEvxQIFZ5caQt%2B1pPautd8pTuP6pcCOW7CVPDLgSmq6qWPQmly%2F6wz%2FDRiHXLoYzaaM4gxHI8A4E0%2FRjzCp%2BtYHA6XJLCb9SVBposuY%2Fx6EFl1WoN0dxEJdZM4YGEtO7EIB%2FwgDgsZdawshD4dd5h%2B%2BAcEMmketmSAvZhwGTPrFUu4OJjcUCm1vCvnxlngP%2B8pusTcOqyKYhE4l5YBM645EFBxeKObk70cSat2Ui7CUQ2RHBKchFP6%2BrcrfrbfulEtiiGMjQyvW9xF3zuMJix%2BrwGOqUBjKtegLZ%2BMBGJwtOQ7kXRzUoYKtjJpm0K3lLkuFIzuqXjDRRv2Aa2telPs0KZ1p2kMdyN%2BwWlENjO2HsOnzCXuxruBNjYbfPIQDcVUSYyEheWJpz8n7tfU0fgnwkPYdz4RCZV7P93CwG%2BJHRQWJppaCTFxTCbuy7lwDCWD78X9ShH8j6Un38%2BVjJn6P8WeiSXfIAQ00p5E8NW1NYDqHA%2FMAylZbQD&X-Amz-Signature=60cbbc601256fbe254128b70c229f6da72ef29e3a2c10636550c3cb7f312fa35&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 3. Histogram
A histogram is an important visual representation of data in categorical form. To view the data in a "Binned" form, use the histogram plot with a number of bins required or with the data points that mark the bin edges. The x-axis represents the data bins, and the y-axis represents the number of elements in each bin.
**Syntax:**
```python
plt.hist(x, bins)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/24e4424a-df87-40a1-b63b-195cbdc2e0ab/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Y35IU6EL%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T221428Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCtmBMmt3JdkdUCAgUAIU5bfktYaDlunUgG%2ByNnKHHEbAIgaK%2Bz0v1iAMqXZiNHuYVn1FZIagp4TkDnOO%2FBhiIZj5EqiAQI3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDCaIekX%2B5T7gkvdysyrcA6Ma4dKFijnTkSmV7H91E4xht9ioKtHWS9EKFBen6RYcn5TlWFPVok4e4DdDNITY28ePYuGJWwmyRXrZxXLTtwla%2FwBIQqwV36pIuNhRsxL3mfp2WkEIGyLk5iFTU%2BJ5T3dQURi%2FZC5Gl7h%2BM6tB0jbDoQUSg644XEBXI0FQjwHacIjxsfi40AlT%2FMFPkF9GQmyImkVm4S7pUkYWaExIVWxpzyueM6GEYHBmCrKqS1bbOg3RuYTc7jC%2FT9sxs5%2BldsEwelYuvV4mfAz7XGJsZ8WkFkBBaGN8PvHFu6QAdkNNBOS07JqQWaQ3qasZpe4bvL7Srt3ds0eTkBs44yLi4m2dgkQVeFFbke3YQ27Ma4lUEvxQIFZ5caQt%2B1pPautd8pTuP6pcCOW7CVPDLgSmq6qWPQmly%2F6wz%2FDRiHXLoYzaaM4gxHI8A4E0%2FRjzCp%2BtYHA6XJLCb9SVBposuY%2Fx6EFl1WoN0dxEJdZM4YGEtO7EIB%2FwgDgsZdawshD4dd5h%2B%2BAcEMmketmSAvZhwGTPrFUu4OJjcUCm1vCvnxlngP%2B8pusTcOqyKYhE4l5YBM645EFBxeKObk70cSat2Ui7CUQ2RHBKchFP6%2BrcrfrbfulEtiiGMjQyvW9xF3zuMJix%2BrwGOqUBjKtegLZ%2BMBGJwtOQ7kXRzUoYKtjJpm0K3lLkuFIzuqXjDRRv2Aa2telPs0KZ1p2kMdyN%2BwWlENjO2HsOnzCXuxruBNjYbfPIQDcVUSYyEheWJpz8n7tfU0fgnwkPYdz4RCZV7P93CwG%2BJHRQWJppaCTFxTCbuy7lwDCWD78X9ShH8j6Un38%2BVjJn6P8WeiSXfIAQ00p5E8NW1NYDqHA%2FMAylZbQD&X-Amz-Signature=f346ec07d6370184ebb1db82a3284af60a3d5be3e700991723d89e3d43bf6fdc&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ab5a6dfe-51f5-43ee-bcb3-33dae4a1c7ad/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Y35IU6EL%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T221428Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCtmBMmt3JdkdUCAgUAIU5bfktYaDlunUgG%2ByNnKHHEbAIgaK%2Bz0v1iAMqXZiNHuYVn1FZIagp4TkDnOO%2FBhiIZj5EqiAQI3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDCaIekX%2B5T7gkvdysyrcA6Ma4dKFijnTkSmV7H91E4xht9ioKtHWS9EKFBen6RYcn5TlWFPVok4e4DdDNITY28ePYuGJWwmyRXrZxXLTtwla%2FwBIQqwV36pIuNhRsxL3mfp2WkEIGyLk5iFTU%2BJ5T3dQURi%2FZC5Gl7h%2BM6tB0jbDoQUSg644XEBXI0FQjwHacIjxsfi40AlT%2FMFPkF9GQmyImkVm4S7pUkYWaExIVWxpzyueM6GEYHBmCrKqS1bbOg3RuYTc7jC%2FT9sxs5%2BldsEwelYuvV4mfAz7XGJsZ8WkFkBBaGN8PvHFu6QAdkNNBOS07JqQWaQ3qasZpe4bvL7Srt3ds0eTkBs44yLi4m2dgkQVeFFbke3YQ27Ma4lUEvxQIFZ5caQt%2B1pPautd8pTuP6pcCOW7CVPDLgSmq6qWPQmly%2F6wz%2FDRiHXLoYzaaM4gxHI8A4E0%2FRjzCp%2BtYHA6XJLCb9SVBposuY%2Fx6EFl1WoN0dxEJdZM4YGEtO7EIB%2FwgDgsZdawshD4dd5h%2B%2BAcEMmketmSAvZhwGTPrFUu4OJjcUCm1vCvnxlngP%2B8pusTcOqyKYhE4l5YBM645EFBxeKObk70cSat2Ui7CUQ2RHBKchFP6%2BrcrfrbfulEtiiGMjQyvW9xF3zuMJix%2BrwGOqUBjKtegLZ%2BMBGJwtOQ7kXRzUoYKtjJpm0K3lLkuFIzuqXjDRRv2Aa2telPs0KZ1p2kMdyN%2BwWlENjO2HsOnzCXuxruBNjYbfPIQDcVUSYyEheWJpz8n7tfU0fgnwkPYdz4RCZV7P93CwG%2BJHRQWJppaCTFxTCbuy7lwDCWD78X9ShH8j6Un38%2BVjJn6P8WeiSXfIAQ00p5E8NW1NYDqHA%2FMAylZbQD&X-Amz-Signature=880eb49498237a9b2bc1d1cea28f7e9cc482faab5a0c3c8ade3cfef52b146169&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8f1b1d60-cf1b-42b3-9faa-f634c89c3f84/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Y35IU6EL%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T221428Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCtmBMmt3JdkdUCAgUAIU5bfktYaDlunUgG%2ByNnKHHEbAIgaK%2Bz0v1iAMqXZiNHuYVn1FZIagp4TkDnOO%2FBhiIZj5EqiAQI3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDCaIekX%2B5T7gkvdysyrcA6Ma4dKFijnTkSmV7H91E4xht9ioKtHWS9EKFBen6RYcn5TlWFPVok4e4DdDNITY28ePYuGJWwmyRXrZxXLTtwla%2FwBIQqwV36pIuNhRsxL3mfp2WkEIGyLk5iFTU%2BJ5T3dQURi%2FZC5Gl7h%2BM6tB0jbDoQUSg644XEBXI0FQjwHacIjxsfi40AlT%2FMFPkF9GQmyImkVm4S7pUkYWaExIVWxpzyueM6GEYHBmCrKqS1bbOg3RuYTc7jC%2FT9sxs5%2BldsEwelYuvV4mfAz7XGJsZ8WkFkBBaGN8PvHFu6QAdkNNBOS07JqQWaQ3qasZpe4bvL7Srt3ds0eTkBs44yLi4m2dgkQVeFFbke3YQ27Ma4lUEvxQIFZ5caQt%2B1pPautd8pTuP6pcCOW7CVPDLgSmq6qWPQmly%2F6wz%2FDRiHXLoYzaaM4gxHI8A4E0%2FRjzCp%2BtYHA6XJLCb9SVBposuY%2Fx6EFl1WoN0dxEJdZM4YGEtO7EIB%2FwgDgsZdawshD4dd5h%2B%2BAcEMmketmSAvZhwGTPrFUu4OJjcUCm1vCvnxlngP%2B8pusTcOqyKYhE4l5YBM645EFBxeKObk70cSat2Ui7CUQ2RHBKchFP6%2BrcrfrbfulEtiiGMjQyvW9xF3zuMJix%2BrwGOqUBjKtegLZ%2BMBGJwtOQ7kXRzUoYKtjJpm0K3lLkuFIzuqXjDRRv2Aa2telPs0KZ1p2kMdyN%2BwWlENjO2HsOnzCXuxruBNjYbfPIQDcVUSYyEheWJpz8n7tfU0fgnwkPYdz4RCZV7P93CwG%2BJHRQWJppaCTFxTCbuy7lwDCWD78X9ShH8j6Un38%2BVjJn6P8WeiSXfIAQ00p5E8NW1NYDqHA%2FMAylZbQD&X-Amz-Signature=e30854d8cca599c7f66dfba7f3a76ac1e30a0fba3880cca92c5a5a08c27695dd&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/13ad0497-05fe-4eaa-984e-707b33e14761/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Y35IU6EL%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T221428Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCtmBMmt3JdkdUCAgUAIU5bfktYaDlunUgG%2ByNnKHHEbAIgaK%2Bz0v1iAMqXZiNHuYVn1FZIagp4TkDnOO%2FBhiIZj5EqiAQI3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDCaIekX%2B5T7gkvdysyrcA6Ma4dKFijnTkSmV7H91E4xht9ioKtHWS9EKFBen6RYcn5TlWFPVok4e4DdDNITY28ePYuGJWwmyRXrZxXLTtwla%2FwBIQqwV36pIuNhRsxL3mfp2WkEIGyLk5iFTU%2BJ5T3dQURi%2FZC5Gl7h%2BM6tB0jbDoQUSg644XEBXI0FQjwHacIjxsfi40AlT%2FMFPkF9GQmyImkVm4S7pUkYWaExIVWxpzyueM6GEYHBmCrKqS1bbOg3RuYTc7jC%2FT9sxs5%2BldsEwelYuvV4mfAz7XGJsZ8WkFkBBaGN8PvHFu6QAdkNNBOS07JqQWaQ3qasZpe4bvL7Srt3ds0eTkBs44yLi4m2dgkQVeFFbke3YQ27Ma4lUEvxQIFZ5caQt%2B1pPautd8pTuP6pcCOW7CVPDLgSmq6qWPQmly%2F6wz%2FDRiHXLoYzaaM4gxHI8A4E0%2FRjzCp%2BtYHA6XJLCb9SVBposuY%2Fx6EFl1WoN0dxEJdZM4YGEtO7EIB%2FwgDgsZdawshD4dd5h%2B%2BAcEMmketmSAvZhwGTPrFUu4OJjcUCm1vCvnxlngP%2B8pusTcOqyKYhE4l5YBM645EFBxeKObk70cSat2Ui7CUQ2RHBKchFP6%2BrcrfrbfulEtiiGMjQyvW9xF3zuMJix%2BrwGOqUBjKtegLZ%2BMBGJwtOQ7kXRzUoYKtjJpm0K3lLkuFIzuqXjDRRv2Aa2telPs0KZ1p2kMdyN%2BwWlENjO2HsOnzCXuxruBNjYbfPIQDcVUSYyEheWJpz8n7tfU0fgnwkPYdz4RCZV7P93CwG%2BJHRQWJppaCTFxTCbuy7lwDCWD78X9ShH8j6Un38%2BVjJn6P8WeiSXfIAQ00p5E8NW1NYDqHA%2FMAylZbQD&X-Amz-Signature=c4ac5b822d054202d64680a36c1cd623a26296f5fc0a1e69e103e605c3625454&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 2. Box and Whisker Plot
A box plot shows the distribution of quantitative data in a way that facilitates comparisons between variables or across levels of a categorical variable. The box shows the quartiles of the dataset while the whiskers extend to show the rest of the distribution, except for points that are determined to be "outliers".
**Syntax:**
```python
sns.boxplot(x='header_1', y='header_2', data=df)
```
**Example Output:**


![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d207ae92-0a7c-4e2f-aa65-0ee5a2c33bf7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UQXFOK6O%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T221432Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEqDnGaWZvijmkzCUDSSrMzYICMaqrBclBJugqMGwI4bAiAQiM8cvvJSLBLW1myiaxKVs6aQrjBkNJgBHN6Pieqi9SqIBAjf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMaU33RyJOb%2Fvm%2FixDKtwD7LBvM0ESw2e8OPBtLisha%2BTveKusVVlLnM0iVdxzFJ0wbxHbHvLn%2FN1s9FMOiYaP1eTjmpYRbQ4m7gVVWvpARCz5Za0pQm1nSLgny0tqc%2BaHaCgJjwJOP0Rq36PxSQz%2F3i6mKRKEF3XnDbd001FDQDT1L0QHLF0vQfzuZdoAHP36RYGRQDhr3Jdhda66s2mGzjO6OujsDg1SbhrpGs8Jv3fiKZ%2FVav3AzUdsdSPfzj1YETJBslCGHtY21a%2FEysKj57L4FbOj5KsWARotPA8vDZRlLKGnz5PJF1zmCS95csVxFUjKMMKu2fsDneuiQiIicziym8jZ9hSOHX1DPVesc3NgDZWY%2FjY2xiynCmG0MhSwzUpiVIRMg66pB9yOe%2BiLARl%2BJ4ZVCeIsxrSLahcR0PHrwmQnEOccVlJHyS0cZKCllW8IdqyPzABg1UWJ6bSHe0rien69FooJtnx69kiyrzh%2B2s7pWVzp8TMLQT4uw3%2B3jAwzCU4DgiW51ru9pi2UMIDJE546wsTW4lAPQWdlgpv2wsW4LD36fFsIvvUqMFUWR2MXNgVwFAPdQi4o1JwWcOuVDeFdrqc1cJdlnt0se1xJMeqFgWb%2Bq7H0U5UsKEvlvY1ENNiiNrdYRnowyLH6vAY6pgFfGQDR%2BJf%2FQaQ3XCExBExj3aXJG8pkUrDkQDySfQCb%2B8ClOL6b6ji6OjOkEK%2B%2F93iuZFAgXlLrNSUimPrxj2XPGNoDYPp%2Fmg3F87tnOh14L4CG%2BoXVe6H73cVJq27SKLAgrAsuNrAAGKSpJPxdvNROjgs16o0kDZVQ7GDcWHzg6sHlR6euFTWZS9gcvT3OFGK4iRAK4eqkx1V2u7%2B9OVRy%2FUmRjpOB&X-Amz-Signature=94017d00f0feb2523a9d6b268d1eaa8396669310a51e453ba83653d37c1c16ad&X-Amz-SignedHeaders=host&x-id=GetObject)

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0e516edc-7551-4792-ab18-0494db3c4c0c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XEDNJVUJ%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T221431Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDgBcFwCrshTh5ySwzlYVJUe9okAJmB1HndSyTprEBmnAIhAOVRVTj24e9LQbUnYgNoGpZbBpFJH4RV0aYvWLW337avKogECN%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyjuzXc%2BT3i7%2FTM92Aq3ANG00KJNoCP1BcR05r2pF4uxfJNOVepWtnoLZj5O3bjoxlyIw5fQVF6jbmzxiMOzk4tgiLBNRmr3sTXkT8I6fHZRCfQPDzWjINeOPQk8tO7h7R5aVUigh8AtOpCfxazGYxj6YzVMwilr05Smf6ZBjz%2FeSAzyJVe6Qu4kPjOixqewzfmS8D27nN0FkeXrGn12rnUI0KtFrUq84fYtEOhxbo8gmrnVeE6YdbfNGmQ6skkr6DLbecn0SkXO9AhJqpqeeXtc2r%2BPKDI0ZgedtF44zeh0ZMEMf339M4hd1abEHUEWJvhC3I15L3L2bSx8XicT8wLEAPd0f%2B%2B7bfb2visyVPSfn795e5vwLsO0HKkmGDuzBVu6AznJycQyCJge76aDjEQxX%2FvPsIr3ujW5LNifUhCw%2Fmd4z8XlUsYlBdxBdrm%2FFVRslNhbFcz1OdG4Pn1AIBVOvGGfTM51aHj6o2liZ%2FIFkJjlFF4kgJGFIhif%2Fr%2Fuq0LZay5bt8QRczW7hvzRgwdp4O3wUKg0gtVAKqq7Fip8cVhfddaynyEVOufJOqFLVJprUbNQXP2BjUpB78YLUrrLI5Pwbxw3d%2B77FV8Ka8xOavTjKJU%2BRUpA7Hm5N2WMLMYKSlml5HTW7lvpzC4sfq8BjqkAScFZlmaj%2B%2BVlnz7Xfv%2BD0%2Bb2xL8w2FhoEMv0XXm2AcDY0J%2BkFKnPZr%2BRrg79RzzbrimWhblagvto0P6%2FE627PGHvbB3x1Fh%2B0G09IuqHkWgDN1kscpQs9yf5yo8%2F9xpCwCfYkjZO7eejBK1h0csfX0rSTKI8%2Bq0MyrSLbQZ0OGEDCCeL%2FMyLdGHLPtAllV%2FRm2PDAudXaK5pB6quVhyobA%2Btydg&X-Amz-Signature=50bc0cce53bc13f9ce11da27e51d9c340e36f21097c12dbe4fc1cc62412c2404&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23a79b9d-2356-49a9-8fd9-65c6b0ab2cc5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Y35IU6EL%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T221428Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCtmBMmt3JdkdUCAgUAIU5bfktYaDlunUgG%2ByNnKHHEbAIgaK%2Bz0v1iAMqXZiNHuYVn1FZIagp4TkDnOO%2FBhiIZj5EqiAQI3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDCaIekX%2B5T7gkvdysyrcA6Ma4dKFijnTkSmV7H91E4xht9ioKtHWS9EKFBen6RYcn5TlWFPVok4e4DdDNITY28ePYuGJWwmyRXrZxXLTtwla%2FwBIQqwV36pIuNhRsxL3mfp2WkEIGyLk5iFTU%2BJ5T3dQURi%2FZC5Gl7h%2BM6tB0jbDoQUSg644XEBXI0FQjwHacIjxsfi40AlT%2FMFPkF9GQmyImkVm4S7pUkYWaExIVWxpzyueM6GEYHBmCrKqS1bbOg3RuYTc7jC%2FT9sxs5%2BldsEwelYuvV4mfAz7XGJsZ8WkFkBBaGN8PvHFu6QAdkNNBOS07JqQWaQ3qasZpe4bvL7Srt3ds0eTkBs44yLi4m2dgkQVeFFbke3YQ27Ma4lUEvxQIFZ5caQt%2B1pPautd8pTuP6pcCOW7CVPDLgSmq6qWPQmly%2F6wz%2FDRiHXLoYzaaM4gxHI8A4E0%2FRjzCp%2BtYHA6XJLCb9SVBposuY%2Fx6EFl1WoN0dxEJdZM4YGEtO7EIB%2FwgDgsZdawshD4dd5h%2B%2BAcEMmketmSAvZhwGTPrFUu4OJjcUCm1vCvnxlngP%2B8pusTcOqyKYhE4l5YBM645EFBxeKObk70cSat2Ui7CUQ2RHBKchFP6%2BrcrfrbfulEtiiGMjQyvW9xF3zuMJix%2BrwGOqUBjKtegLZ%2BMBGJwtOQ7kXRzUoYKtjJpm0K3lLkuFIzuqXjDRRv2Aa2telPs0KZ1p2kMdyN%2BwWlENjO2HsOnzCXuxruBNjYbfPIQDcVUSYyEheWJpz8n7tfU0fgnwkPYdz4RCZV7P93CwG%2BJHRQWJppaCTFxTCbuy7lwDCWD78X9ShH8j6Un38%2BVjJn6P8WeiSXfIAQ00p5E8NW1NYDqHA%2FMAylZbQD&X-Amz-Signature=6992dc598155c975a8f806cd9da344c301892956d1462d02e0f4cd626a07bfee&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 4. KDE Plot
A Kernel Density Estimate (KDE) plot is a graph that creates a probability distribution curve for the data based upon its likelihood of occurrence on a specific value. This is created for a single vector of information.
**Syntax:**
```python
sns.kdeplot(X) || sns.kdeplot(df['age'])
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0d571213-2a2f-4921-a50b-880847aa05ee/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Y35IU6EL%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T221429Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCtmBMmt3JdkdUCAgUAIU5bfktYaDlunUgG%2ByNnKHHEbAIgaK%2Bz0v1iAMqXZiNHuYVn1FZIagp4TkDnOO%2FBhiIZj5EqiAQI3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDCaIekX%2B5T7gkvdysyrcA6Ma4dKFijnTkSmV7H91E4xht9ioKtHWS9EKFBen6RYcn5TlWFPVok4e4DdDNITY28ePYuGJWwmyRXrZxXLTtwla%2FwBIQqwV36pIuNhRsxL3mfp2WkEIGyLk5iFTU%2BJ5T3dQURi%2FZC5Gl7h%2BM6tB0jbDoQUSg644XEBXI0FQjwHacIjxsfi40AlT%2FMFPkF9GQmyImkVm4S7pUkYWaExIVWxpzyueM6GEYHBmCrKqS1bbOg3RuYTc7jC%2FT9sxs5%2BldsEwelYuvV4mfAz7XGJsZ8WkFkBBaGN8PvHFu6QAdkNNBOS07JqQWaQ3qasZpe4bvL7Srt3ds0eTkBs44yLi4m2dgkQVeFFbke3YQ27Ma4lUEvxQIFZ5caQt%2B1pPautd8pTuP6pcCOW7CVPDLgSmq6qWPQmly%2F6wz%2FDRiHXLoYzaaM4gxHI8A4E0%2FRjzCp%2BtYHA6XJLCb9SVBposuY%2Fx6EFl1WoN0dxEJdZM4YGEtO7EIB%2FwgDgsZdawshD4dd5h%2B%2BAcEMmketmSAvZhwGTPrFUu4OJjcUCm1vCvnxlngP%2B8pusTcOqyKYhE4l5YBM645EFBxeKObk70cSat2Ui7CUQ2RHBKchFP6%2BrcrfrbfulEtiiGMjQyvW9xF3zuMJix%2BrwGOqUBjKtegLZ%2BMBGJwtOQ7kXRzUoYKtjJpm0K3lLkuFIzuqXjDRRv2Aa2telPs0KZ1p2kMdyN%2BwWlENjO2HsOnzCXuxruBNjYbfPIQDcVUSYyEheWJpz8n7tfU0fgnwkPYdz4RCZV7P93CwG%2BJHRQWJppaCTFxTCbuy7lwDCWD78X9ShH8j6Un38%2BVjJn6P8WeiSXfIAQ00p5E8NW1NYDqHA%2FMAylZbQD&X-Amz-Signature=b9f0775df78d1bb022b33f48b6a0d1b8c56d0cbde41e80abe9dba6fa9ef0fbcf&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/53752550-ef82-4ca9-a01a-09921f0282d0/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Y35IU6EL%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T221429Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCtmBMmt3JdkdUCAgUAIU5bfktYaDlunUgG%2ByNnKHHEbAIgaK%2Bz0v1iAMqXZiNHuYVn1FZIagp4TkDnOO%2FBhiIZj5EqiAQI3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDCaIekX%2B5T7gkvdysyrcA6Ma4dKFijnTkSmV7H91E4xht9ioKtHWS9EKFBen6RYcn5TlWFPVok4e4DdDNITY28ePYuGJWwmyRXrZxXLTtwla%2FwBIQqwV36pIuNhRsxL3mfp2WkEIGyLk5iFTU%2BJ5T3dQURi%2FZC5Gl7h%2BM6tB0jbDoQUSg644XEBXI0FQjwHacIjxsfi40AlT%2FMFPkF9GQmyImkVm4S7pUkYWaExIVWxpzyueM6GEYHBmCrKqS1bbOg3RuYTc7jC%2FT9sxs5%2BldsEwelYuvV4mfAz7XGJsZ8WkFkBBaGN8PvHFu6QAdkNNBOS07JqQWaQ3qasZpe4bvL7Srt3ds0eTkBs44yLi4m2dgkQVeFFbke3YQ27Ma4lUEvxQIFZ5caQt%2B1pPautd8pTuP6pcCOW7CVPDLgSmq6qWPQmly%2F6wz%2FDRiHXLoYzaaM4gxHI8A4E0%2FRjzCp%2BtYHA6XJLCb9SVBposuY%2Fx6EFl1WoN0dxEJdZM4YGEtO7EIB%2FwgDgsZdawshD4dd5h%2B%2BAcEMmketmSAvZhwGTPrFUu4OJjcUCm1vCvnxlngP%2B8pusTcOqyKYhE4l5YBM645EFBxeKObk70cSat2Ui7CUQ2RHBKchFP6%2BrcrfrbfulEtiiGMjQyvW9xF3zuMJix%2BrwGOqUBjKtegLZ%2BMBGJwtOQ7kXRzUoYKtjJpm0K3lLkuFIzuqXjDRRv2Aa2telPs0KZ1p2kMdyN%2BwWlENjO2HsOnzCXuxruBNjYbfPIQDcVUSYyEheWJpz8n7tfU0fgnwkPYdz4RCZV7P93CwG%2BJHRQWJppaCTFxTCbuy7lwDCWD78X9ShH8j6Un38%2BVjJn6P8WeiSXfIAQ00p5E8NW1NYDqHA%2FMAylZbQD&X-Amz-Signature=1266eff919079862a9de69c3e5df5d10811c2ed311fac3fe7da744c9a73ddbac&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
## 4. Correlation Between Variables
Correlation is a statistical measure of the extent to which different variables are interdependent. It indicates how changes in one variable are associated with changes in another variable over time.
### Positive Correlation
Positive correlation indicates that as one variable increases, the other variable also tends to increase.
**Example: Engine Size and Price**
- **Positive Correlation:** Engine size increases, price also increases.
- **Visualization:** Scatter plot with a steep positive slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c7ea9b0-3ef3-4357-a9c3-554fc71b6b15/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662BQYMFX6%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T221430Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC%2FI6ET%2BiDVOCQBbuF05LWyJdU40uyziV%2FHXk7Y0aVjiwIhAMkz0FUV3yY%2F1MecAF2ozwg2ljPzpOgmEtw3fQmNBl0mKogECN%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxwIWwUz7QL9pl9P9sq3AMWUwzZWc4QxM9NsmbnvdiE3COh3m%2BEM4wj49lDiMyHoSz%2FkdVikSoqe4B%2BPDzEyuvDtjEOlj5W4wlxW5TZeasuXKALlbMIBRIeU5PmUEIZVHHb%2FwrgwctVcnz4bTjgtwAc40orQ%2BFj5NNvuJ4o9INxhJnv68z7YBx7RAmBVIwhpn%2B5wr5FhotoT%2FKrcu8nESn44xwH7vbkgb3GbQ8wu6Yt0yOhcustA2krjNzkmOSX0tUN2ULnUuQ8LTI%2Fk5aQTGDq3GTsB%2FeKh0GrtxCqOGKOiYLV%2FH%2F5H71%2Bn01XBmQcIqxWrBEm0QCyAG5Jt6PrBQGxq4OyEzQKx103SAeAQOYsHNOkm%2BxR%2BxExh%2FZT2zjpxD0SxQ6UYErxJD5WUATBB%2Bz47pXqhwn9A9%2Bubk57eVwJGbJV45666CFQHgVsQroRCgyVVrxzzpaPLQBXthYY3GC04sIFQ2mUf3WHhVhZCx3KppEQdlpIExb314Dbfj%2BWtwIubBgTTjvcvYhvfNreH3gUyR3%2FRUV67ofgrUDUzgQQiai%2BHryg6XPuY0v4qx2XZJ7M1D2ukhue6nLtDpXB%2B049PMeJDou%2Bl%2FsBE64IG5LbEgw4L7AxU4jOp8DbdcYbDaKbE5kfzSZGVHOq2TC5sfq8BjqkAbB1QSK6J2rvUeAdlP7t654F19oJMUkyPLmiLIokZvZ9Kr4xck3vwXRrh%2FFKQ%2F2rwznqXvp4K8M5po%2F8TeHQNYGiA9eijDRt2HkxS5f7OIGwSFLMDEfbWWAX%2BXtK1pXAV5LEACciWE19ZthzqqYt5d6nY6mkTbuhXxBX59LfYFVCl4j4Nk1HNcNy8ZY1l7RMA9cd86wm9XN4MCqfCQ0Kcl9ZUQdC&X-Amz-Signature=b523e2c18b6b924f1719b2e51157362e978a708785d82f367ce023ffb6e74938&X-Amz-SignedHeaders=host&x-id=GetObject)
**Explanation:** When engine size increases, there is a corresponding increase in the price of the vehicle. This positive correlation suggests that larger engines tend to be associated with higher prices in the market.
___
### Negative Correlation
Negative correlation indicates that as one variable increases, the other variable tends to decrease.
**Example: Highway Miles per Gallon and Price**
- **Negative Correlation:** As highway miles per gallon increases, price decreases.
- **Visualization:** Scatter plot with a steep negative slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/10f1f798-9cc4-4df2-a9c1-5a339f554a0b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662TPZ7ZGX%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T221430Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBtEw9Y9YlrgDDgFNZU%2BF5ZITMM8aiO4b7zzZqoaeMAcAiBCuU3loVXqO2T2T5npW1JgjvtiYPBzrwx0LHX8%2FqwAIyqIBAjf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM7v6OmcboEZikn8SeKtwDHE7mzzCxURxivhGvBvKKsLr4l4z47dWthv8OLvRt2HqvMXkr%2F4299IdFm%2FHF3fKJuuCF1ELsWa555dgM6jsakC3P%2B4L43Tq1QMOJgc1ctpugDGE2ImUExj8FBVTgLRFXhehTLIscz1WevyytaKasikrZkDzu7QvtriG31dOkryqTkpspYjD3Xm7houPQNwiGMMoz%2Bk%2BR703%2FyMSyUZFlcfszxnCJeZCaaYWgT7S5DkDwhrhzCIEBfG07509T%2Fss3To78jpfKpt7R78By1cdTcON4EoIK%2Fmokk8gNpXYZHsNvbBO3nG3Nh2AUTZ0iYhLC3xc%2FL6WQ11G7Dsyp7AW8nWP86XWjKGE%2BBflNo7rPKVfedNrzmLzk5vFwR0KPKo%2B28cDpxVDtJ3Mi3Im3o5Eb2HU92GmcVIi9EQ2cZn6erIckxbDv3G04%2FEJxdIV%2Bbwvno%2FJnFCh5JyIUYvmM1j6sDHo6D4qa%2BYNhWyEb4%2BA6JtUvcigVmspw21T6qRULHQ%2FIdJZHJci%2FT8aL3t3NbHxDlDiDuSWNCzsa%2FJsxo%2BtEqUByvWd19x7vEl2zPv17cfue6O3JHECy3aIK3SH8Z8eWfDzH4mAoAM2s9f8FG5uFmG98aL2Y8U%2FnrTrpmeYwoLH6vAY6pgFTc7Pj3lhIlh7GOB5CsyKEMBoaF1CEPG7MOeySEnw06WFPnmtsU2P%2F9KXrUFPlFXxnXAW1EwnUCKbQaonXSzkRE%2FPh83vc167zidntIE5%2FklVb4ts32zhGmossNQxuUtbJi5JzUBngS2ulFnfyn9tqGjtPlpv3m1%2FLdNSlb296s03kgN1Juw5VSYtAyA%2BP9RNDb7B4C446WNybIU3dIG4hA0iP8B32&X-Amz-Signature=49257990dc2b7e9bc9393777f02db3f692c518357b39b3cd93bcb3e9cb26b708&X-Amz-SignedHeaders=host&x-id=GetObject)
**Explanation:** When highway miles per gallon increases, the price of the vehicle tends to decrease. This negative correlation suggests that cars with higher fuel efficiency (more miles per gallon) are generally priced lower in the market.
___
### Weak Correlation
Weak correlation indicates a lack of strong relationship between the variables.
**Example: RPM and Price**
- **Weak Correlation:** Low and high RPM values show varied prices, indicating no strong predictive relationship.
- **Visualization:** Scatter plot with no clear trend or slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9f914514-8914-4bf4-ac84-d9e3077f6eb1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UOA5QOF4%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T221430Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD23b9Wg2f9y5ak5DhFYxvnZkTnOSrW9gIMfcbKvv07QQIgRKLWD3n8IKHlFBsGHYndmDeZefxkdIi306ky6%2FscTsAqiAQI3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDsyI00O1uoSsVZUACrcAzrtH8%2F%2Fko8MAQDRzqAgHzi3WWeVdTuPFuR3pSywcKHI0q9dZ8Z9pkmr07eFLVTug67nPVxCzEfuu9e0VIMotMLtn6CV63hfazwIV%2BpGdHsPNjS1VKZZo0%2FaVpUf8efRVqPjPvlzd3yc8DJh2RxnEWTuqQkcA2YmDyiNMw%2FInUEt7emKkuqSGIw%2Fqj2D5meKrVLrDLZ595sA4pzwn4kYSM8%2Ft9KwnzfNXwQOrgKfg9i%2BgXq3KcUSsILWUUMzaENblmXmZumnZMEoX02wwVXgTg0vdDHElj1TTv%2FjE8h7vR%2FPvqH6WhXWu91hbWipSIdu8W0FSQSHjJUnCj4CWjLBgJ%2Fmwy%2BKs0VKHqlu%2B%2Bap2Zi46557HKgVh%2BaMacf3csSxMDeOxBmpxhJyROPxnKU58rapJnuN7tZW1qlZUAuoOfGhf6SHpHE6f5HJtd3%2F6JwuJvu2900X8UTtsI6q04DYJ16W79w7zDbwXRwuEQmJClP459fndtqSc7fMUd2SWcYq6OvsDaDMOqdKQgW0NrcZjmccIcWIFfJ3DYJaAZS3e60r47I5427DilP9EKCxBuFU%2BijHaV6PDzCeQtO6pP8wb27whqIWQsrqSWyyUQdpVN%2Bojr%2FXYZNkoFGQNL23MI2x%2BrwGOqUBVVxCtCDinVyN4kbOee60aAeiKuuve3zsIvTxYdtZIVVgTK4jKCrVYrf1SaTaKU%2Fn2uNNkjUwrTRfRL6eiv26%2FbrweEg%2FaYTa92MdkvsatlyIUHmRUjpzr047WO6AsGv7ezBYL09p91Ks8i5maqIOUqZ%2BTFFC0XpiHmLA0%2F9pN9KXTmoL0NAxjdBk0hEJ23dG8usun49x9TZksI4k0lrT4o1BDdWW&X-Amz-Signature=256abe4427424dea239c28432ab1da775d905327d0502a2922033ecd0d7403a6&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f18086e5-5b04-4fbf-8309-8944ab20d213/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46625NBZBYQ%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T221430Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCSD5ynec80ZmwhNZwlmWkEr%2Btxfjyili3UombOfl%2FR%2FQIgbnxAXUbWCbqOdNl%2FYxiR8c%2BRuG8GA1fhM1T9AlnzYqMqiAQI3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMXeFsZ6QS73AvkWjyrcAyXikxlWJxuFxlo4BUO7FBWWx9QnMRnjFFI2l0%2FICIlM%2FJ2D28rZamIFLPnY7yYyXX0dn%2FnqkA1fvpMk4MYcUvG9vSZPd24rqyIiw%2FXkQPutk%2FNydNUP1F8XJBItxL3LUNR%2FLsniZYMKNGZ%2B5Jv85MNaE51F%2BI63Qt%2Bzhud9b1pbc5nsdFcjuoMNgtFvUR7QswRtJBm4VLC5J%2FxmmBaqQN0c8mU1oEkmACkDyZ%2Fny65XzspQORsSPhxsMqwMy73Kxjb9Ey6eiz1lIRAKtl0MpMrjHWR6VMfEaEaEjuCN4b%2FKFo9Luja04imzw1smpOZVQsdAmJlYNi5Ndbd%2BfCIVhqsLxTd2mf9rnybWPRdOw%2BlqbnWQN8AT6zw%2Fd1E3BaUQY8dRXTHdIOhuLI%2Btpwg2FiS11We2o9bIvRVR3FNGxe2P0U0CobTbwKt0R%2BH%2Bxnl78ZzZIH6Vb1RB7SEG23PSkgyOi29Fzayz85Tk6KCGPTiSpJ4echXQ4aZURoLjE0f8mJTn9K%2F9hmyOcdPHAYo7Za1uxQpNblXG3Qk9PyB4t5bmSNusAIjB%2FL%2Bjytbm8DS2cNF4czRCIEBu0yjKarKeve5nY8Iuax%2FFYgtgmh6kp1el8nzpMH7fZ9PNoN0vMICx%2BrwGOqUBuvEt0f1sM0g3iVM2jyljKNerwlNjxAaw3nCakm6XGGsHaj5XIW0yC8PbPeuVUClrSKOBMrZK16aMlf5B3VGJvUqAqrBHGZn62LjKbT9Atd%2BKA1WetanbxVnc175rkxDn4wDCIJAtCjtx5uyhbbJcXCgTOJXXtSiwte0y9WS8ZvmEQnzvAkXEB9G4xK8UBONmzXPebGo6vykdHcUMzowG%2F8xwZwFr&X-Amz-Signature=352d4bb9e4d228ca03f69ec89e52fefef17aa2291552c36ec499a91898f42b12&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Correlation Plot
Heatmap visualizes correlations among variables. Color scheme indicates Pearson correlation coefficients. Dark red diagonal line shows perfect correlation (value of 1) between variables and themselves.
This heatmap offers overview of variable relationships and their link with price.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cd3b341e-cc1a-45f7-8aec-cdc00436d270/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46625NBZBYQ%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T221430Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCSD5ynec80ZmwhNZwlmWkEr%2Btxfjyili3UombOfl%2FR%2FQIgbnxAXUbWCbqOdNl%2FYxiR8c%2BRuG8GA1fhM1T9AlnzYqMqiAQI3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMXeFsZ6QS73AvkWjyrcAyXikxlWJxuFxlo4BUO7FBWWx9QnMRnjFFI2l0%2FICIlM%2FJ2D28rZamIFLPnY7yYyXX0dn%2FnqkA1fvpMk4MYcUvG9vSZPd24rqyIiw%2FXkQPutk%2FNydNUP1F8XJBItxL3LUNR%2FLsniZYMKNGZ%2B5Jv85MNaE51F%2BI63Qt%2Bzhud9b1pbc5nsdFcjuoMNgtFvUR7QswRtJBm4VLC5J%2FxmmBaqQN0c8mU1oEkmACkDyZ%2Fny65XzspQORsSPhxsMqwMy73Kxjb9Ey6eiz1lIRAKtl0MpMrjHWR6VMfEaEaEjuCN4b%2FKFo9Luja04imzw1smpOZVQsdAmJlYNi5Ndbd%2BfCIVhqsLxTd2mf9rnybWPRdOw%2BlqbnWQN8AT6zw%2Fd1E3BaUQY8dRXTHdIOhuLI%2Btpwg2FiS11We2o9bIvRVR3FNGxe2P0U0CobTbwKt0R%2BH%2Bxnl78ZzZIH6Vb1RB7SEG23PSkgyOi29Fzayz85Tk6KCGPTiSpJ4echXQ4aZURoLjE0f8mJTn9K%2F9hmyOcdPHAYo7Za1uxQpNblXG3Qk9PyB4t5bmSNusAIjB%2FL%2Bjytbm8DS2cNF4czRCIEBu0yjKarKeve5nY8Iuax%2FFYgtgmh6kp1el8nzpMH7fZ9PNoN0vMICx%2BrwGOqUBuvEt0f1sM0g3iVM2jyljKNerwlNjxAaw3nCakm6XGGsHaj5XIW0yC8PbPeuVUClrSKOBMrZK16aMlf5B3VGJvUqAqrBHGZn62LjKbT9Atd%2BKA1WetanbxVnc175rkxDn4wDCIJAtCjtx5uyhbbJcXCgTOJXXtSiwte0y9WS8ZvmEQnzvAkXEB9G4xK8UBONmzXPebGo6vykdHcUMzowG%2F8xwZwFr&X-Amz-Signature=9b68b80f44498b14fa804067190ee0fc40c4a75da8b96d89db7d1eee49cecbc9&X-Amz-SignedHeaders=host&x-id=GetObject)

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
