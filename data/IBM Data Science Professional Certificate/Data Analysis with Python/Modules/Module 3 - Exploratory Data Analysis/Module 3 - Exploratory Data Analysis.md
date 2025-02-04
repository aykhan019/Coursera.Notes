

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7e6d594d-952e-44b6-97ea-31225882aea6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UTBNELRD%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T010832Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAkaCXVzLXdlc3QtMiJHMEUCIG4mrxU9mEJ3kywpL4N3h2pXetm%2B%2FxBh6Wjo8Tp9UEcxAiEAyJoJkHrgpVMtanKWSSKtu37IZ5mL1vlv0UcfSCh4zFEq%2FwMIIhAAGgw2Mzc0MjMxODM4MDUiDI06vge4%2Bx3BqNdeqCrcA6Eg9Hk15tzlfeRxLycr3F8Q3yhfSdm2ihq2MtLnbth%2Ff7KEL661ZhmJdGI7Zz9kyL9TH8gw3qRtRT%2BJHpiOBkNCbqupimj8mgvTdbxSf84%2BWP%2B%2FGiGZVpIbH7%2BTvSueOu4QxKuUZ0yECB%2BUiguziTFu9Hx2MlJZa%2BmXusyI5DTcuXPPi%2BjbZfhASK7exbw3siWOu3A7kqCoFStrgnLn9ISyBZ1Vzt8kOZTi9par1L6jm8AMDLF6V3TkN6H8jIRKIBJCWJr61aKEzI3MAo0HmMrxSpDTGziZ47E7WFR5X9GvRAJSRKJ4eNRjw05zS5%2FykWGpo2Kr0I5sH7O%2FsmH9IgJxkj3SDcoPWFIRFygjAuvuVFo0dwvM3r%2FOHxhwweeLMYhNEBX5ExYwYYOOO%2F5Yqv75Y5T1SUAN62dRyWTYvj2%2FsyMJJXeGkl5cBS82YCwCL2rM8DWmq0Gdnol8n5shD%2BKPNut6%2FhXDK4OnQPKhTGojh3txLILV9jDpUB7ztognAXsDEhlDMZSJfZuuTcEkLGBFSVQLM6S0enK0jfztj8WgTmnbHugIDRYdr%2F2qMZH5DGG6xSAApOtG3a8GuF%2BfDPy0Te811uO9jTeBNo5RM5fGynb%2BC63dXoalg7SfMMTMhb0GOqUBeQHwcpnQpSrfmfQHehPC%2FnaKbXZXLuN1PXk5AsHM8dTDSCIEnQyQFfrzpYo4haCF5F1sNosEnvR1j2jyTNRH%2BJ0yhC0oykBBg1fuE%2Fqhdovust75ye%2BB%2Br0ZLu3C2sdrtH9kUgsglYKI0i1%2FwKsWLMe1ErmVTllGUHgL5SMqk0a1ic6HKMYJw4FQqAN1yTHyBIR%2ButRGD9HeDt3ienAeXg0PPlWt&X-Amz-Signature=e7f29fa8354b71be323ed06ce6ac30c482d145b9556af65d4435302f0882cb3c&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cbfaed9e-b398-4902-8936-dea058b21def/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UTBNELRD%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T010832Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAkaCXVzLXdlc3QtMiJHMEUCIG4mrxU9mEJ3kywpL4N3h2pXetm%2B%2FxBh6Wjo8Tp9UEcxAiEAyJoJkHrgpVMtanKWSSKtu37IZ5mL1vlv0UcfSCh4zFEq%2FwMIIhAAGgw2Mzc0MjMxODM4MDUiDI06vge4%2Bx3BqNdeqCrcA6Eg9Hk15tzlfeRxLycr3F8Q3yhfSdm2ihq2MtLnbth%2Ff7KEL661ZhmJdGI7Zz9kyL9TH8gw3qRtRT%2BJHpiOBkNCbqupimj8mgvTdbxSf84%2BWP%2B%2FGiGZVpIbH7%2BTvSueOu4QxKuUZ0yECB%2BUiguziTFu9Hx2MlJZa%2BmXusyI5DTcuXPPi%2BjbZfhASK7exbw3siWOu3A7kqCoFStrgnLn9ISyBZ1Vzt8kOZTi9par1L6jm8AMDLF6V3TkN6H8jIRKIBJCWJr61aKEzI3MAo0HmMrxSpDTGziZ47E7WFR5X9GvRAJSRKJ4eNRjw05zS5%2FykWGpo2Kr0I5sH7O%2FsmH9IgJxkj3SDcoPWFIRFygjAuvuVFo0dwvM3r%2FOHxhwweeLMYhNEBX5ExYwYYOOO%2F5Yqv75Y5T1SUAN62dRyWTYvj2%2FsyMJJXeGkl5cBS82YCwCL2rM8DWmq0Gdnol8n5shD%2BKPNut6%2FhXDK4OnQPKhTGojh3txLILV9jDpUB7ztognAXsDEhlDMZSJfZuuTcEkLGBFSVQLM6S0enK0jfztj8WgTmnbHugIDRYdr%2F2qMZH5DGG6xSAApOtG3a8GuF%2BfDPy0Te811uO9jTeBNo5RM5fGynb%2BC63dXoalg7SfMMTMhb0GOqUBeQHwcpnQpSrfmfQHehPC%2FnaKbXZXLuN1PXk5AsHM8dTDSCIEnQyQFfrzpYo4haCF5F1sNosEnvR1j2jyTNRH%2BJ0yhC0oykBBg1fuE%2Fqhdovust75ye%2BB%2Br0ZLu3C2sdrtH9kUgsglYKI0i1%2FwKsWLMe1ErmVTllGUHgL5SMqk0a1ic6HKMYJw4FQqAN1yTHyBIR%2ButRGD9HeDt3ienAeXg0PPlWt&X-Amz-Signature=f07dc32a8efb86dfb4a371470262ec00cb1b8f19c744f0052cbc295361f962e7&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/91181646-b1e0-4433-9711-6259a96a9247/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UTBNELRD%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T010832Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAkaCXVzLXdlc3QtMiJHMEUCIG4mrxU9mEJ3kywpL4N3h2pXetm%2B%2FxBh6Wjo8Tp9UEcxAiEAyJoJkHrgpVMtanKWSSKtu37IZ5mL1vlv0UcfSCh4zFEq%2FwMIIhAAGgw2Mzc0MjMxODM4MDUiDI06vge4%2Bx3BqNdeqCrcA6Eg9Hk15tzlfeRxLycr3F8Q3yhfSdm2ihq2MtLnbth%2Ff7KEL661ZhmJdGI7Zz9kyL9TH8gw3qRtRT%2BJHpiOBkNCbqupimj8mgvTdbxSf84%2BWP%2B%2FGiGZVpIbH7%2BTvSueOu4QxKuUZ0yECB%2BUiguziTFu9Hx2MlJZa%2BmXusyI5DTcuXPPi%2BjbZfhASK7exbw3siWOu3A7kqCoFStrgnLn9ISyBZ1Vzt8kOZTi9par1L6jm8AMDLF6V3TkN6H8jIRKIBJCWJr61aKEzI3MAo0HmMrxSpDTGziZ47E7WFR5X9GvRAJSRKJ4eNRjw05zS5%2FykWGpo2Kr0I5sH7O%2FsmH9IgJxkj3SDcoPWFIRFygjAuvuVFo0dwvM3r%2FOHxhwweeLMYhNEBX5ExYwYYOOO%2F5Yqv75Y5T1SUAN62dRyWTYvj2%2FsyMJJXeGkl5cBS82YCwCL2rM8DWmq0Gdnol8n5shD%2BKPNut6%2FhXDK4OnQPKhTGojh3txLILV9jDpUB7ztognAXsDEhlDMZSJfZuuTcEkLGBFSVQLM6S0enK0jfztj8WgTmnbHugIDRYdr%2F2qMZH5DGG6xSAApOtG3a8GuF%2BfDPy0Te811uO9jTeBNo5RM5fGynb%2BC63dXoalg7SfMMTMhb0GOqUBeQHwcpnQpSrfmfQHehPC%2FnaKbXZXLuN1PXk5AsHM8dTDSCIEnQyQFfrzpYo4haCF5F1sNosEnvR1j2jyTNRH%2BJ0yhC0oykBBg1fuE%2Fqhdovust75ye%2BB%2Br0ZLu3C2sdrtH9kUgsglYKI0i1%2FwKsWLMe1ErmVTllGUHgL5SMqk0a1ic6HKMYJw4FQqAN1yTHyBIR%2ButRGD9HeDt3ienAeXg0PPlWt&X-Amz-Signature=d26a3eb0f673530b48cdd695903b2a551e1c69a5ca0da1b0a62d28ff91bb54f8&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/09aba1c0-0d55-41dd-852a-a04c5b8a3fac/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZMMXBKXM%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T010832Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAkaCXVzLXdlc3QtMiJGMEQCIFVBGePdkAtgBVBThe8G%2F%2BSNYyuVgawTWceQPXCq6%2BWaAiA0Om7FaTiht1x%2FyobWMLzHmFM%2FUia0z1igEfmBGDUvUSr%2FAwgiEAAaDDYzNzQyMzE4MzgwNSIMo9kUIRc3M8hrVdajKtwDuVZSVhvTnIipldJvJbcIg7cp9oAAPOw8zhVE0zXtPC4188M1LTJuJvTrnCho5jn84ChuNGtrQRuGmNIabrN4UB%2BstFGfCduuNoiE2ROxEMUgUomeilT4lQeRVuL08UciZxxcGtAdcZgFdkQuL6nJKurEXCgobTqIcMluzN0nvvkg5aoIWPyjazaXyP0ToHGoPPEzRA36Tu%2B%2FRxWzydeh%2FH7dHGGPrmcS9gRKDTfsOSyD2u6AwcUxaytaJw2D%2FuNAoEhunr1SRekWSXHcCviSTnvJcZlfqoONZaLHHZY8o8F%2FT51Mgj%2F5tzVjv6BMexc8YN7XWFfZAlUWbKI0rPdxKNrPJwXQpyN0VBhaRrKu0SxnJ8zXVUxQEMqHoBOe4je%2FLpyPa%2F7KErN1LJr7oRPUv2mi9G%2Be8qBTK1xaLBtc%2F14yMi5ic64BwQZZUpdaY2GlnGxsyUhA67ZUhM5KKaF7PfO2UvN%2FyfPecRYn%2F992d5zbwmPdqqckM6AVw97hXXJH1oUVc%2B3iHQQc%2FDwVUK67G4UWrJI7YsWyKVpK8tslEjdqzgZaNeNfES4uWVOIxiK%2BDD6dLEeRvEWf1HvbUhL916k%2FCRGeQYVknmtgRZOQSFkFsF1bOvH%2Fjgb434cw6cyFvQY6pgH%2B54BFH51ALsvW%2FTmSSarU0GOPCJNiYpPypzT666u1%2FqItwL%2Fr299raQ1c%2BOEuzzL4q40mrPIBbLKl6i%2BfyPtxgm69KKhkW8M02KE0yZWT3lGR1WxOECM4qULwfsEvamMdiOJhefhjoI4szye5i1hXRsPTgU8%2BEHXXNRJH06P0fo9AznURolVgM6JULTCJP4i4dZ4tqHMLOzgkp8RsF4AP86cugatk&X-Amz-Signature=0e52a8e8d8b71470b88bf329fd2e0f8afb003d274fe02a8b8cd1388be5ff2468&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 2. Scatter Plot
Scatter plots present the relationship between two variables in a dataset. It represents data points on a two-dimensional plane. The independent variable or attribute is plotted on the X-axis, while the dependent variable is plotted on the Y-axis.
**Syntax:**
```python
plt.scatter(x, y)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23708af9-659f-4f23-b626-1a4292d7842c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZMMXBKXM%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T010832Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAkaCXVzLXdlc3QtMiJGMEQCIFVBGePdkAtgBVBThe8G%2F%2BSNYyuVgawTWceQPXCq6%2BWaAiA0Om7FaTiht1x%2FyobWMLzHmFM%2FUia0z1igEfmBGDUvUSr%2FAwgiEAAaDDYzNzQyMzE4MzgwNSIMo9kUIRc3M8hrVdajKtwDuVZSVhvTnIipldJvJbcIg7cp9oAAPOw8zhVE0zXtPC4188M1LTJuJvTrnCho5jn84ChuNGtrQRuGmNIabrN4UB%2BstFGfCduuNoiE2ROxEMUgUomeilT4lQeRVuL08UciZxxcGtAdcZgFdkQuL6nJKurEXCgobTqIcMluzN0nvvkg5aoIWPyjazaXyP0ToHGoPPEzRA36Tu%2B%2FRxWzydeh%2FH7dHGGPrmcS9gRKDTfsOSyD2u6AwcUxaytaJw2D%2FuNAoEhunr1SRekWSXHcCviSTnvJcZlfqoONZaLHHZY8o8F%2FT51Mgj%2F5tzVjv6BMexc8YN7XWFfZAlUWbKI0rPdxKNrPJwXQpyN0VBhaRrKu0SxnJ8zXVUxQEMqHoBOe4je%2FLpyPa%2F7KErN1LJr7oRPUv2mi9G%2Be8qBTK1xaLBtc%2F14yMi5ic64BwQZZUpdaY2GlnGxsyUhA67ZUhM5KKaF7PfO2UvN%2FyfPecRYn%2F992d5zbwmPdqqckM6AVw97hXXJH1oUVc%2B3iHQQc%2FDwVUK67G4UWrJI7YsWyKVpK8tslEjdqzgZaNeNfES4uWVOIxiK%2BDD6dLEeRvEWf1HvbUhL916k%2FCRGeQYVknmtgRZOQSFkFsF1bOvH%2Fjgb434cw6cyFvQY6pgH%2B54BFH51ALsvW%2FTmSSarU0GOPCJNiYpPypzT666u1%2FqItwL%2Fr299raQ1c%2BOEuzzL4q40mrPIBbLKl6i%2BfyPtxgm69KKhkW8M02KE0yZWT3lGR1WxOECM4qULwfsEvamMdiOJhefhjoI4szye5i1hXRsPTgU8%2BEHXXNRJH06P0fo9AznURolVgM6JULTCJP4i4dZ4tqHMLOzgkp8RsF4AP86cugatk&X-Amz-Signature=21b7973bb8714a034409f5907e693979d3638f4a7ee79cba2d95bf692c0411dc&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 3. Histogram
A histogram is an important visual representation of data in categorical form. To view the data in a "Binned" form, use the histogram plot with a number of bins required or with the data points that mark the bin edges. The x-axis represents the data bins, and the y-axis represents the number of elements in each bin.
**Syntax:**
```python
plt.hist(x, bins)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/24e4424a-df87-40a1-b63b-195cbdc2e0ab/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZMMXBKXM%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T010832Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAkaCXVzLXdlc3QtMiJGMEQCIFVBGePdkAtgBVBThe8G%2F%2BSNYyuVgawTWceQPXCq6%2BWaAiA0Om7FaTiht1x%2FyobWMLzHmFM%2FUia0z1igEfmBGDUvUSr%2FAwgiEAAaDDYzNzQyMzE4MzgwNSIMo9kUIRc3M8hrVdajKtwDuVZSVhvTnIipldJvJbcIg7cp9oAAPOw8zhVE0zXtPC4188M1LTJuJvTrnCho5jn84ChuNGtrQRuGmNIabrN4UB%2BstFGfCduuNoiE2ROxEMUgUomeilT4lQeRVuL08UciZxxcGtAdcZgFdkQuL6nJKurEXCgobTqIcMluzN0nvvkg5aoIWPyjazaXyP0ToHGoPPEzRA36Tu%2B%2FRxWzydeh%2FH7dHGGPrmcS9gRKDTfsOSyD2u6AwcUxaytaJw2D%2FuNAoEhunr1SRekWSXHcCviSTnvJcZlfqoONZaLHHZY8o8F%2FT51Mgj%2F5tzVjv6BMexc8YN7XWFfZAlUWbKI0rPdxKNrPJwXQpyN0VBhaRrKu0SxnJ8zXVUxQEMqHoBOe4je%2FLpyPa%2F7KErN1LJr7oRPUv2mi9G%2Be8qBTK1xaLBtc%2F14yMi5ic64BwQZZUpdaY2GlnGxsyUhA67ZUhM5KKaF7PfO2UvN%2FyfPecRYn%2F992d5zbwmPdqqckM6AVw97hXXJH1oUVc%2B3iHQQc%2FDwVUK67G4UWrJI7YsWyKVpK8tslEjdqzgZaNeNfES4uWVOIxiK%2BDD6dLEeRvEWf1HvbUhL916k%2FCRGeQYVknmtgRZOQSFkFsF1bOvH%2Fjgb434cw6cyFvQY6pgH%2B54BFH51ALsvW%2FTmSSarU0GOPCJNiYpPypzT666u1%2FqItwL%2Fr299raQ1c%2BOEuzzL4q40mrPIBbLKl6i%2BfyPtxgm69KKhkW8M02KE0yZWT3lGR1WxOECM4qULwfsEvamMdiOJhefhjoI4szye5i1hXRsPTgU8%2BEHXXNRJH06P0fo9AznURolVgM6JULTCJP4i4dZ4tqHMLOzgkp8RsF4AP86cugatk&X-Amz-Signature=51283cfdf485f4e490e18bed1793d5b921949de7037e605f463691043d8d1b29&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ab5a6dfe-51f5-43ee-bcb3-33dae4a1c7ad/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZMMXBKXM%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T010832Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAkaCXVzLXdlc3QtMiJGMEQCIFVBGePdkAtgBVBThe8G%2F%2BSNYyuVgawTWceQPXCq6%2BWaAiA0Om7FaTiht1x%2FyobWMLzHmFM%2FUia0z1igEfmBGDUvUSr%2FAwgiEAAaDDYzNzQyMzE4MzgwNSIMo9kUIRc3M8hrVdajKtwDuVZSVhvTnIipldJvJbcIg7cp9oAAPOw8zhVE0zXtPC4188M1LTJuJvTrnCho5jn84ChuNGtrQRuGmNIabrN4UB%2BstFGfCduuNoiE2ROxEMUgUomeilT4lQeRVuL08UciZxxcGtAdcZgFdkQuL6nJKurEXCgobTqIcMluzN0nvvkg5aoIWPyjazaXyP0ToHGoPPEzRA36Tu%2B%2FRxWzydeh%2FH7dHGGPrmcS9gRKDTfsOSyD2u6AwcUxaytaJw2D%2FuNAoEhunr1SRekWSXHcCviSTnvJcZlfqoONZaLHHZY8o8F%2FT51Mgj%2F5tzVjv6BMexc8YN7XWFfZAlUWbKI0rPdxKNrPJwXQpyN0VBhaRrKu0SxnJ8zXVUxQEMqHoBOe4je%2FLpyPa%2F7KErN1LJr7oRPUv2mi9G%2Be8qBTK1xaLBtc%2F14yMi5ic64BwQZZUpdaY2GlnGxsyUhA67ZUhM5KKaF7PfO2UvN%2FyfPecRYn%2F992d5zbwmPdqqckM6AVw97hXXJH1oUVc%2B3iHQQc%2FDwVUK67G4UWrJI7YsWyKVpK8tslEjdqzgZaNeNfES4uWVOIxiK%2BDD6dLEeRvEWf1HvbUhL916k%2FCRGeQYVknmtgRZOQSFkFsF1bOvH%2Fjgb434cw6cyFvQY6pgH%2B54BFH51ALsvW%2FTmSSarU0GOPCJNiYpPypzT666u1%2FqItwL%2Fr299raQ1c%2BOEuzzL4q40mrPIBbLKl6i%2BfyPtxgm69KKhkW8M02KE0yZWT3lGR1WxOECM4qULwfsEvamMdiOJhefhjoI4szye5i1hXRsPTgU8%2BEHXXNRJH06P0fo9AznURolVgM6JULTCJP4i4dZ4tqHMLOzgkp8RsF4AP86cugatk&X-Amz-Signature=2856a0183c4f15a4a52d6910416294b68d1053b769e944c3485f4c2580873b2d&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8f1b1d60-cf1b-42b3-9faa-f634c89c3f84/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZMMXBKXM%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T010832Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAkaCXVzLXdlc3QtMiJGMEQCIFVBGePdkAtgBVBThe8G%2F%2BSNYyuVgawTWceQPXCq6%2BWaAiA0Om7FaTiht1x%2FyobWMLzHmFM%2FUia0z1igEfmBGDUvUSr%2FAwgiEAAaDDYzNzQyMzE4MzgwNSIMo9kUIRc3M8hrVdajKtwDuVZSVhvTnIipldJvJbcIg7cp9oAAPOw8zhVE0zXtPC4188M1LTJuJvTrnCho5jn84ChuNGtrQRuGmNIabrN4UB%2BstFGfCduuNoiE2ROxEMUgUomeilT4lQeRVuL08UciZxxcGtAdcZgFdkQuL6nJKurEXCgobTqIcMluzN0nvvkg5aoIWPyjazaXyP0ToHGoPPEzRA36Tu%2B%2FRxWzydeh%2FH7dHGGPrmcS9gRKDTfsOSyD2u6AwcUxaytaJw2D%2FuNAoEhunr1SRekWSXHcCviSTnvJcZlfqoONZaLHHZY8o8F%2FT51Mgj%2F5tzVjv6BMexc8YN7XWFfZAlUWbKI0rPdxKNrPJwXQpyN0VBhaRrKu0SxnJ8zXVUxQEMqHoBOe4je%2FLpyPa%2F7KErN1LJr7oRPUv2mi9G%2Be8qBTK1xaLBtc%2F14yMi5ic64BwQZZUpdaY2GlnGxsyUhA67ZUhM5KKaF7PfO2UvN%2FyfPecRYn%2F992d5zbwmPdqqckM6AVw97hXXJH1oUVc%2B3iHQQc%2FDwVUK67G4UWrJI7YsWyKVpK8tslEjdqzgZaNeNfES4uWVOIxiK%2BDD6dLEeRvEWf1HvbUhL916k%2FCRGeQYVknmtgRZOQSFkFsF1bOvH%2Fjgb434cw6cyFvQY6pgH%2B54BFH51ALsvW%2FTmSSarU0GOPCJNiYpPypzT666u1%2FqItwL%2Fr299raQ1c%2BOEuzzL4q40mrPIBbLKl6i%2BfyPtxgm69KKhkW8M02KE0yZWT3lGR1WxOECM4qULwfsEvamMdiOJhefhjoI4szye5i1hXRsPTgU8%2BEHXXNRJH06P0fo9AznURolVgM6JULTCJP4i4dZ4tqHMLOzgkp8RsF4AP86cugatk&X-Amz-Signature=d87cfa69decd985bf6aa04deec8ef1fe0f8209c780d6e3ca7852d048c8c9192d&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/13ad0497-05fe-4eaa-984e-707b33e14761/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZMMXBKXM%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T010832Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAkaCXVzLXdlc3QtMiJGMEQCIFVBGePdkAtgBVBThe8G%2F%2BSNYyuVgawTWceQPXCq6%2BWaAiA0Om7FaTiht1x%2FyobWMLzHmFM%2FUia0z1igEfmBGDUvUSr%2FAwgiEAAaDDYzNzQyMzE4MzgwNSIMo9kUIRc3M8hrVdajKtwDuVZSVhvTnIipldJvJbcIg7cp9oAAPOw8zhVE0zXtPC4188M1LTJuJvTrnCho5jn84ChuNGtrQRuGmNIabrN4UB%2BstFGfCduuNoiE2ROxEMUgUomeilT4lQeRVuL08UciZxxcGtAdcZgFdkQuL6nJKurEXCgobTqIcMluzN0nvvkg5aoIWPyjazaXyP0ToHGoPPEzRA36Tu%2B%2FRxWzydeh%2FH7dHGGPrmcS9gRKDTfsOSyD2u6AwcUxaytaJw2D%2FuNAoEhunr1SRekWSXHcCviSTnvJcZlfqoONZaLHHZY8o8F%2FT51Mgj%2F5tzVjv6BMexc8YN7XWFfZAlUWbKI0rPdxKNrPJwXQpyN0VBhaRrKu0SxnJ8zXVUxQEMqHoBOe4je%2FLpyPa%2F7KErN1LJr7oRPUv2mi9G%2Be8qBTK1xaLBtc%2F14yMi5ic64BwQZZUpdaY2GlnGxsyUhA67ZUhM5KKaF7PfO2UvN%2FyfPecRYn%2F992d5zbwmPdqqckM6AVw97hXXJH1oUVc%2B3iHQQc%2FDwVUK67G4UWrJI7YsWyKVpK8tslEjdqzgZaNeNfES4uWVOIxiK%2BDD6dLEeRvEWf1HvbUhL916k%2FCRGeQYVknmtgRZOQSFkFsF1bOvH%2Fjgb434cw6cyFvQY6pgH%2B54BFH51ALsvW%2FTmSSarU0GOPCJNiYpPypzT666u1%2FqItwL%2Fr299raQ1c%2BOEuzzL4q40mrPIBbLKl6i%2BfyPtxgm69KKhkW8M02KE0yZWT3lGR1WxOECM4qULwfsEvamMdiOJhefhjoI4szye5i1hXRsPTgU8%2BEHXXNRJH06P0fo9AznURolVgM6JULTCJP4i4dZ4tqHMLOzgkp8RsF4AP86cugatk&X-Amz-Signature=d959b07b32afd94d5b07cdf41750aceeb6106050649dadb90943436ba97297a5&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 2. Box and Whisker Plot
A box plot shows the distribution of quantitative data in a way that facilitates comparisons between variables or across levels of a categorical variable. The box shows the quartiles of the dataset while the whiskers extend to show the rest of the distribution, except for points that are determined to be "outliers".
**Syntax:**
```python
sns.boxplot(x='header_1', y='header_2', data=df)
```
**Example Output:**


![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d207ae92-0a7c-4e2f-aa65-0ee5a2c33bf7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WUPDR7T6%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T010834Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAkaCXVzLXdlc3QtMiJGMEQCIBH96lwnG1vGM1doL8d8ACcAviKBPRqFz8AJGe0fIeCyAiAipI7OMhKmUcKwFMlwozlkKxkPSZhBHl2K0rhanyWMnSr%2FAwgiEAAaDDYzNzQyMzE4MzgwNSIMFH%2BeQXV2yxpbk7rWKtwDuNEoI3OznORI%2BdJw6Oc61a8pmkJERk05bExmjVRWTmeci3dsfMCNf3T9LenZlbUwYqMZyQZHro%2F%2B%2FSMQlTwMZqsn4UP5h29IjSRB2RQYVCaq%2Fo4ALTE1bYzGkaOlR7KTJHMg5uwnMn1PrbQPI%2BjbvZT%2BBRQsLJdG0UhCjpk8xZWRJY4g4AYgIf4EwHK%2F26YfrNrUCpc8NOFGmdfYeW2RSHkk94RfY%2B4Q3QJpy%2BwqdvyEN0OuBFP6OEAekmzWjcCIon%2BcpkobmIPEHPz3EGHqBP%2FhbPgFGgi%2FHpDyipPRFsRu%2FJbHVR2VbekwjtcotRHupnMchZu1R4vgr1yBmOGUdCFb9HahjZdQXoHdgnUvZBZQ7MmlWpxDYnR8e2wDi1UGFE%2BFAF8gltMtdRP8CXUwP89rQiG71y4O0RpkxYSnr8pA8flaTj%2BzplmbsA4WUpOstTKEQIxS7f%2BnA%2BFApWUDnuL87k4cC9W7jXepI3FmuL%2FT2QsxXG38Ns5QwIeH0eh5WHTUWm8mamjQlZA24Bd5KSVSPBQhXPU1JdCU1rU5MxqIURcTQWUyw1s%2FSDydyDjdSNHXNwOGaJA%2FpKK4YnDq6KfdO0lmeRIu8H%2FGMcG1pl%2FZb50Uj2KsAfr6ja4wj82FvQY6pgGqTpf0KO7N9niG9O%2FjF4Kvd2%2B%2FX6i%2F9rBgB8KExQ%2F99bnoAFHhQTY0flO66Ym3W4EIKjRnThWRYAnJTN%2B%2B6iGbqvpkMVJIdzpg23jZiIuhhSJnqbUmAY4YY0%2BGr9fjCkY83ajGzKJs%2FH1MZnPi8NJ9Nx1CpwzLPLvgmuZ3iRPBI8DYTnE1Q4tW5tdiuCkNP2VeIhW3Lfm7Vgoih%2BdtWsZpmhUDMvax&X-Amz-Signature=446de009f656aa65fd02379497f96a08142e5b1f5b3cc25f38c741781d8f51a3&X-Amz-SignedHeaders=host&x-id=GetObject)

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0e516edc-7551-4792-ab18-0494db3c4c0c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WGE3JSWM%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T010834Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAkaCXVzLXdlc3QtMiJHMEUCIQDx2pQLcjcdUqavHed%2FxkZeosnrzlr3oK6paEJ8QZW43QIgViwoLm6RDkKIH0Miq8KFH6aJtb%2BLPMUsaJNamqo4twMq%2FwMIIhAAGgw2Mzc0MjMxODM4MDUiDMHgnacGHZF%2F73MNQCrcA71DlReFpG76isKuLjDpsN6yXabQRd%2Fi6fM7U6Mt74TOUAoymJ3f1L3Wroexsff24fLPLfKZwxpvvFhq047qxvyQcxFoWyiHQ9KOxberbOcys5TXSjfOCbk6nuVaAV0u2ONCj8AEGcGxNqLJdAwVNAd74Tsm3zpnKpdIFQtR5EpUWTvELlBfCUmNAiTJ1YMU5ZOst0xFaAHfisZpuJt1%2F%2BxLg9AD3DKvnE4iULiDrUzUHV7%2FZ5lyJEHrOyK2ELS0FR1FVumL62mVt6BOO7am1mrl%2FLQw5nf4medPD9oYDbUTNTz1FbUaH5c%2BZ01uTQvOGm%2Fx5Is6sRSt%2F6ZM4rlE7nyPmzEy%2F%2FU6mdYQLQyb8aQmSSv0pU4MJphyDNLfmIjuQq4M%2F6Iqc%2BnwlAw4VQMUsH5BGsr72iSqH5h7zeYTvpa51U9aNkVbx5Ld%2Bhs1SLVWU4EPDwW76RzgTbzxKiHCxKgCBnxUuCX%2FeYbCJD5GWDEHtnCJincfWEx3fR2Oejvs3OSYUfAbeZPhHPbbh49Z4A7Q%2BhfU5SZZiI%2BqGgAlKqif2YWlbM3xQEdDGiMRVf8AYZ0DKv%2BS3QcPnpkKORnOEpkXx8A8WpxBoq8Zj5rjQXzQj7%2Bm6Ccox%2F6wHagvMI%2FNhb0GOqUBJ2IsLo%2FqCETBhPj10qsYEFs8v8qljJWuwE%2FDE3DpZjwTy4eWvRG5hEB2os2W%2B9d5tlCEfj8SBOD3HtuhPAUqGDHSWUUtvppWv1WObJGvFpjtGowH7%2F5evdWMwZluikyVa48uHML1fmCGZClcggtmr%2FBJ0YbwGKKmoQN55hSyFKA5LRo5QePYoLABLyGBVLfPok8Idr8Kg5vJffjEvTi%2BFTjrwJj6&X-Amz-Signature=d0d9895f90f9a5553f2391331bb67aad9ee9af0a2550367b21dae7ecbe416742&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23a79b9d-2356-49a9-8fd9-65c6b0ab2cc5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZMMXBKXM%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T010832Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAkaCXVzLXdlc3QtMiJGMEQCIFVBGePdkAtgBVBThe8G%2F%2BSNYyuVgawTWceQPXCq6%2BWaAiA0Om7FaTiht1x%2FyobWMLzHmFM%2FUia0z1igEfmBGDUvUSr%2FAwgiEAAaDDYzNzQyMzE4MzgwNSIMo9kUIRc3M8hrVdajKtwDuVZSVhvTnIipldJvJbcIg7cp9oAAPOw8zhVE0zXtPC4188M1LTJuJvTrnCho5jn84ChuNGtrQRuGmNIabrN4UB%2BstFGfCduuNoiE2ROxEMUgUomeilT4lQeRVuL08UciZxxcGtAdcZgFdkQuL6nJKurEXCgobTqIcMluzN0nvvkg5aoIWPyjazaXyP0ToHGoPPEzRA36Tu%2B%2FRxWzydeh%2FH7dHGGPrmcS9gRKDTfsOSyD2u6AwcUxaytaJw2D%2FuNAoEhunr1SRekWSXHcCviSTnvJcZlfqoONZaLHHZY8o8F%2FT51Mgj%2F5tzVjv6BMexc8YN7XWFfZAlUWbKI0rPdxKNrPJwXQpyN0VBhaRrKu0SxnJ8zXVUxQEMqHoBOe4je%2FLpyPa%2F7KErN1LJr7oRPUv2mi9G%2Be8qBTK1xaLBtc%2F14yMi5ic64BwQZZUpdaY2GlnGxsyUhA67ZUhM5KKaF7PfO2UvN%2FyfPecRYn%2F992d5zbwmPdqqckM6AVw97hXXJH1oUVc%2B3iHQQc%2FDwVUK67G4UWrJI7YsWyKVpK8tslEjdqzgZaNeNfES4uWVOIxiK%2BDD6dLEeRvEWf1HvbUhL916k%2FCRGeQYVknmtgRZOQSFkFsF1bOvH%2Fjgb434cw6cyFvQY6pgH%2B54BFH51ALsvW%2FTmSSarU0GOPCJNiYpPypzT666u1%2FqItwL%2Fr299raQ1c%2BOEuzzL4q40mrPIBbLKl6i%2BfyPtxgm69KKhkW8M02KE0yZWT3lGR1WxOECM4qULwfsEvamMdiOJhefhjoI4szye5i1hXRsPTgU8%2BEHXXNRJH06P0fo9AznURolVgM6JULTCJP4i4dZ4tqHMLOzgkp8RsF4AP86cugatk&X-Amz-Signature=33469174b8959af8610782ff03664726c71c7423dfd7229f46f62ecb7937ecc1&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 4. KDE Plot
A Kernel Density Estimate (KDE) plot is a graph that creates a probability distribution curve for the data based upon its likelihood of occurrence on a specific value. This is created for a single vector of information.
**Syntax:**
```python
sns.kdeplot(X) || sns.kdeplot(df['age'])
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0d571213-2a2f-4921-a50b-880847aa05ee/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZMMXBKXM%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T010832Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAkaCXVzLXdlc3QtMiJGMEQCIFVBGePdkAtgBVBThe8G%2F%2BSNYyuVgawTWceQPXCq6%2BWaAiA0Om7FaTiht1x%2FyobWMLzHmFM%2FUia0z1igEfmBGDUvUSr%2FAwgiEAAaDDYzNzQyMzE4MzgwNSIMo9kUIRc3M8hrVdajKtwDuVZSVhvTnIipldJvJbcIg7cp9oAAPOw8zhVE0zXtPC4188M1LTJuJvTrnCho5jn84ChuNGtrQRuGmNIabrN4UB%2BstFGfCduuNoiE2ROxEMUgUomeilT4lQeRVuL08UciZxxcGtAdcZgFdkQuL6nJKurEXCgobTqIcMluzN0nvvkg5aoIWPyjazaXyP0ToHGoPPEzRA36Tu%2B%2FRxWzydeh%2FH7dHGGPrmcS9gRKDTfsOSyD2u6AwcUxaytaJw2D%2FuNAoEhunr1SRekWSXHcCviSTnvJcZlfqoONZaLHHZY8o8F%2FT51Mgj%2F5tzVjv6BMexc8YN7XWFfZAlUWbKI0rPdxKNrPJwXQpyN0VBhaRrKu0SxnJ8zXVUxQEMqHoBOe4je%2FLpyPa%2F7KErN1LJr7oRPUv2mi9G%2Be8qBTK1xaLBtc%2F14yMi5ic64BwQZZUpdaY2GlnGxsyUhA67ZUhM5KKaF7PfO2UvN%2FyfPecRYn%2F992d5zbwmPdqqckM6AVw97hXXJH1oUVc%2B3iHQQc%2FDwVUK67G4UWrJI7YsWyKVpK8tslEjdqzgZaNeNfES4uWVOIxiK%2BDD6dLEeRvEWf1HvbUhL916k%2FCRGeQYVknmtgRZOQSFkFsF1bOvH%2Fjgb434cw6cyFvQY6pgH%2B54BFH51ALsvW%2FTmSSarU0GOPCJNiYpPypzT666u1%2FqItwL%2Fr299raQ1c%2BOEuzzL4q40mrPIBbLKl6i%2BfyPtxgm69KKhkW8M02KE0yZWT3lGR1WxOECM4qULwfsEvamMdiOJhefhjoI4szye5i1hXRsPTgU8%2BEHXXNRJH06P0fo9AznURolVgM6JULTCJP4i4dZ4tqHMLOzgkp8RsF4AP86cugatk&X-Amz-Signature=3b59b0a06d3bc1cc3640cd5e1688f7891300502abad3899dc01daf6ec3783eaf&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/53752550-ef82-4ca9-a01a-09921f0282d0/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZMMXBKXM%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T010832Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAkaCXVzLXdlc3QtMiJGMEQCIFVBGePdkAtgBVBThe8G%2F%2BSNYyuVgawTWceQPXCq6%2BWaAiA0Om7FaTiht1x%2FyobWMLzHmFM%2FUia0z1igEfmBGDUvUSr%2FAwgiEAAaDDYzNzQyMzE4MzgwNSIMo9kUIRc3M8hrVdajKtwDuVZSVhvTnIipldJvJbcIg7cp9oAAPOw8zhVE0zXtPC4188M1LTJuJvTrnCho5jn84ChuNGtrQRuGmNIabrN4UB%2BstFGfCduuNoiE2ROxEMUgUomeilT4lQeRVuL08UciZxxcGtAdcZgFdkQuL6nJKurEXCgobTqIcMluzN0nvvkg5aoIWPyjazaXyP0ToHGoPPEzRA36Tu%2B%2FRxWzydeh%2FH7dHGGPrmcS9gRKDTfsOSyD2u6AwcUxaytaJw2D%2FuNAoEhunr1SRekWSXHcCviSTnvJcZlfqoONZaLHHZY8o8F%2FT51Mgj%2F5tzVjv6BMexc8YN7XWFfZAlUWbKI0rPdxKNrPJwXQpyN0VBhaRrKu0SxnJ8zXVUxQEMqHoBOe4je%2FLpyPa%2F7KErN1LJr7oRPUv2mi9G%2Be8qBTK1xaLBtc%2F14yMi5ic64BwQZZUpdaY2GlnGxsyUhA67ZUhM5KKaF7PfO2UvN%2FyfPecRYn%2F992d5zbwmPdqqckM6AVw97hXXJH1oUVc%2B3iHQQc%2FDwVUK67G4UWrJI7YsWyKVpK8tslEjdqzgZaNeNfES4uWVOIxiK%2BDD6dLEeRvEWf1HvbUhL916k%2FCRGeQYVknmtgRZOQSFkFsF1bOvH%2Fjgb434cw6cyFvQY6pgH%2B54BFH51ALsvW%2FTmSSarU0GOPCJNiYpPypzT666u1%2FqItwL%2Fr299raQ1c%2BOEuzzL4q40mrPIBbLKl6i%2BfyPtxgm69KKhkW8M02KE0yZWT3lGR1WxOECM4qULwfsEvamMdiOJhefhjoI4szye5i1hXRsPTgU8%2BEHXXNRJH06P0fo9AznURolVgM6JULTCJP4i4dZ4tqHMLOzgkp8RsF4AP86cugatk&X-Amz-Signature=755f879b29546eb5e4a2fd35ceecca8cb4acf94d48b22385fd58b6ff0b8d4e55&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
## 4. Correlation Between Variables
Correlation is a statistical measure of the extent to which different variables are interdependent. It indicates how changes in one variable are associated with changes in another variable over time.
### Positive Correlation
Positive correlation indicates that as one variable increases, the other variable also tends to increase.
**Example: Engine Size and Price**
- **Positive Correlation:** Engine size increases, price also increases.
- **Visualization:** Scatter plot with a steep positive slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c7ea9b0-3ef3-4357-a9c3-554fc71b6b15/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SZNAZIQY%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T010834Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAkaCXVzLXdlc3QtMiJHMEUCICqC9fmNnwXDLtfESX35iy9qaKLHDMs0YhoBVPNygrL4AiEAqPxOhpukJKzp0HVYth4xYCSNRmwuaQm6%2FF0qXXt9bI0q%2FwMIIhAAGgw2Mzc0MjMxODM4MDUiDAnCbFS80UE%2BIcTe0CrcAw%2B%2BDgePz2vpCxYWqB7Gp0RCqgs5%2BlbZ1lPOi8zSL%2BEWJy20uZLQoxHu2aq3qdu%2FaxK4XzbMu5A6ZybiFCmPX8Z2k060%2FWOmOaFiJio3EqPdSJ0G3D20l2BI68m3Pdi%2BSiWQKZKV2D2AVQP%2FmQ%2BZoVCOvsdlktmelF%2FfKssUfAiH9sTcbCRvKpweVmz%2B%2FPYPDa155GmBgk5bME0Cwv0FUu20pLbTSxHUN5HolFBLmqL1yZ4XyXLKegp7TK8wtdb9JzoAANmXksblTygO0PW8%2BDAEc9el80bTb6aVU5UAjsoub9JPTPt8RVwHzBuBSudVxMNwHGaS6PWl8Lc87jng17OJ5etos5hJ5LI5atG4ork10oLHz85nCnikMs0TW3gl8DOSruC1Z%2F7WcFv5sEBwBn7G%2BjvOVv7YSISWZ0k3vETjU0UCwjU7m%2BlDshOV%2FP%2Fy0jZa8U6Mw5G22gQl1oSanWlJnUUWK92n6blHFcO3mQJp0KUXd%2BidZOWvZ1aEAWQrt5CStj3agXM3RRrkuINnkFqmLBUN9Yaz5RsqaRCmGLFgJS2SXB%2BGTzfb%2BmZMij166t7G1UVH9LckZDpXVQ6XL%2F3aVYu3Xz7ri3mfEXuo5p2dmjzAu%2FO6rlzuoJJAMILNhb0GOqUBFNs3D3R02ueM%2Fc2taoO2HjyufWSG%2FjdpvyJ2tRAGN8ZAjbO2Zkz17nmgmWFqaHD381wqPE4jBrSVU8JTL2TVHdRs7nDN9Oy%2FtHr7%2FewejT%2FMTMA1G4pC%2BfJOssnpdI%2BlmGi%2FP0mvz8HkgQHxWjmwZLtN%2BV%2FOPGZBlYs0b8mA1YMcnG%2FuQo6iRzV%2FzA4KhdIEHYQzMLlelZhD3zlATexO73RyA9Qb&X-Amz-Signature=66afc4fba14be3a416f3aeef4b5b93c8bb6649b557b29c25091860f2ae30d852&X-Amz-SignedHeaders=host&x-id=GetObject)
**Explanation:** When engine size increases, there is a corresponding increase in the price of the vehicle. This positive correlation suggests that larger engines tend to be associated with higher prices in the market.
___
### Negative Correlation
Negative correlation indicates that as one variable increases, the other variable tends to decrease.
**Example: Highway Miles per Gallon and Price**
- **Negative Correlation:** As highway miles per gallon increases, price decreases.
- **Visualization:** Scatter plot with a steep negative slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/10f1f798-9cc4-4df2-a9c1-5a339f554a0b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662RX3SVLV%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T010834Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAkaCXVzLXdlc3QtMiJGMEQCIB%2BK0ioLYeO5j%2FjVDPCzlLxJnOahZJ9ke%2FKnPG9Xe5WtAiAmUzcHL54T678XtcoimGzR5%2BySYIXETFjfpJ0hbqRp6yr%2FAwgiEAAaDDYzNzQyMzE4MzgwNSIMF3qSrAvPaH%2BGtksWKtwDmG6bMIMb65wql%2BryczmuK0fGXM4%2FinYMz1m0bUOTi4ZjKnpxzwiW3nDGAyCuqpUCdf4LxZu53gyqaPAd6c72MTh19mgbsLmbRvoIhDOsGW%2BjAfnMFA8ndZGV5gawtFIIJC9zDKcNlSaDcs9yqCoHOpSgwYpkGYvecHdSrkdKTySZ8YjtkTAdpp3JIhXaV6M4b1iQNP4I53Vi00M2NsPCoyxM3iEMX1XDN%2FzUxPhB9fr7E8ASvZy%2BOC2BP6yMBIu5LlY64JF2T71roZx8b7ZEvAJRgGUjqQ%2FTv%2BjJoxWRjHDTi9ab6SdAf6Ro9J%2BAhokgOxy%2FUwKLusz0RZKAa9pUevb5J%2BEpLF%2Fi0RgMiceAKZnpocTlrRqmNoVF253E3PRbitfUGCGUDQee5Cndcci3DMI3BEZpksG0tog%2BgYFVqMEwga91wRL4cFD0HIaLRLew6wZTFoMglh5K2ko%2BwpCCmy02HBM81a1CgbkY5FjCuqE7gKbpzEVYW1RqNDSrLy44pq3Kmi2lVnp1qoQqHuuryNHtHut3xZ8LFXTiWXpXQ7inkkFGgFhevPFdhHoBXQU7Cz6ISkVx%2F3dSShbfA2rkvK2RCEhOnuAnq55BXb5re4APqoOnv%2BkhWLIGnvgw88yFvQY6pgHJ%2FvG6Pg4IgnJ%2BpVqrdJppo6v9h5sZ1PabyTqtgxaQToRKCJOil8cV8h9wqfkhIIS0ucAzIV8AqZYAvfTYOQBK62iCGDrSg%2FZeRFqzy1FcOBVoURilLAkdpjGOYohj23yCyCKW%2FLjY8YI1zf%2Fj4xhQNglNYu7NVQyVr6LTO3Ok2mFo%2FrtWjJDdHr%2Fwxc6WcigegDNodZSwX4WXIhdxKrcXGOGtJ6Q1&X-Amz-Signature=573eb1112eafde662a40b8181922dba00d4be680cf1e05e663ce7d2ce38c08f3&X-Amz-SignedHeaders=host&x-id=GetObject)
**Explanation:** When highway miles per gallon increases, the price of the vehicle tends to decrease. This negative correlation suggests that cars with higher fuel efficiency (more miles per gallon) are generally priced lower in the market.
___
### Weak Correlation
Weak correlation indicates a lack of strong relationship between the variables.
**Example: RPM and Price**
- **Weak Correlation:** Low and high RPM values show varied prices, indicating no strong predictive relationship.
- **Visualization:** Scatter plot with no clear trend or slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9f914514-8914-4bf4-ac84-d9e3077f6eb1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZGRMQ5B6%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T010834Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAkaCXVzLXdlc3QtMiJHMEUCIA2yE1zXTD4SncnkJi8MGQCBiiyz0QGjh51dRHszUzefAiEAyNJbr99XBeSotf8xulxz48D%2BdeYW9U2v4j5RewiVSNwq%2FwMIIhAAGgw2Mzc0MjMxODM4MDUiDHhqLyMWAt%2FyrQsXMircA5GBRmKQXvAPUX7%2FqnZjQlXMmRG8aSA6o9n1a6kpN%2BApc%2BkdYcQq40Z7VvYuBT%2FmKXm0OJGNzVuBXBr5r1EvFRu4bZ3efeq9W8aTRT8sVfTnhHS%2BJSMGA%2BigpapDgAF2Xck3dX0mW12gD2mXUtBoBqmG4smLVFoKyngrZmJdqctVg8xTDvRxl4Znvsm0%2F%2F0E6C13eMmhpwB7x2WrSk9J0OI8fcRXqCfJBagfXwoG3HJBqbsJkt%2FpTLytCCgJqmoglgikrxGuIiQaUkJEcWJqSx%2BkEBtG%2BKJWiZvHE5d9ezRQ5XiXPrSMN5RuaJl0NNOrrXnB%2F53iXFAYMku5SOe6lLdSxIXFZeZzzN448UupaU6R9XAzsPrzKrE%2BUiUO6EhjxbxDjJGJ%2BMfGHOh4m4j3FgpE71ovTyeVAwqtRN7EuTrn9vCiluALr5uYRbDcWmZOLcaZzRl7Jl%2FxvqSEVIkpZcGSgTfsP1JZhNjmJcap9u0FoXZmEvd8hE2QfDLFT5H7C2dIvah85JmSgTZJm%2FXjhpZa6KD2101AOeoYO43BtdK9Fi9Cxx0p2rjWaR%2BkC7lvrpjaEaSyTdaZIuO5XBOPwGHhSg8rdtWeWF%2BbUWV5ITUdU2SU9CRgKa8QLE4NMKvNhb0GOqUBCa5AKwxRRGlZGej9bfBnrlfhLFPx8DhzMYMzE9e1VO5r5quY60XXmb%2BHiqBRbnJ6MsCXsH7wnPTRT7f0%2B7O0%2BjBuRPPwmZnDngtI8WkVVXKKr6%2FDMw72f1kqgnB6v5ZVHJauP0aelQ5XbxIFKpd4Z3rCGMKaZYRmixx3hG6EVi2hOKT2dEqa6hN%2FgL6y1JOky57afioDt9ljwmDyAwUAkd9xcYpg&X-Amz-Signature=052e744ffd86c71e0e74e89a7ab3897726db8dad355e457319e4f55142ee28ea&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f18086e5-5b04-4fbf-8309-8944ab20d213/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VYKOLHIF%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T010833Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAkaCXVzLXdlc3QtMiJHMEUCIQD24oqYspX5NqB%2Bggktv8F1jZNS9sBmBDneJ3Ne7KZ6oAIgYBPblc5ZFVas5wy2sVNHoTUnW1qqtHUe0zVuRP1s4joq%2FwMIIhAAGgw2Mzc0MjMxODM4MDUiDPaEWzGUZk0ZP7YnQSrcA6PM4eZztX%2BnlC5MFgEeVuvflXiLkMDmggXBIZc1u3iInfmcZS0y4VHNKdXYZgMKgM2po%2BkmVSOB3f3pYA6xfnZJQV4Pat38BwmAxWBve2vdol1NKYqOK0oWQAG239F7BcDbp%2FW7aXU6Nwg5At7BTjvQdeUPDfI6nsCjIUl1KZJAnCQ7rFb%2Fuj4q3GtRpS%2F9e0Y%2FVF5ZoPA%2F9syHuqUBtFAQKVy0MV5pvokXh6FUm7eE5PSwdiImWt7R5EM1QaqLoCZSYO3GRmcCH6v%2FjclJa21h9ALLhl7f10A%2B2rrZss17hCq794oOPKp%2BVR6ywLChMCqRjyDr5klgO%2Bd76O3bFFCCFhq%2FBl9%2B1y6Qs1y3CN2TpFs2YyJLLBt7Rt1VYwSxMULIEP6%2FMhYu7a7Dh3UPfriQIcjX7KtzvBNWmXzckAtwQbZXfBbG%2F7%2F145BePxq1gUk%2FOJVfLK6FZ4nsTsBDSKQ2Ox0w%2F0En55yVsxWmk25ltN5hVlt88DeYU6431nOjDNLLJtCRonstWlBsnhetw8lkBkOwZVVYkuYRAXCmYB6E9O9tfMcrBhKOcKWpsu6Sn04xYdQbirj1gcRs%2FG0Uu9IaW%2B8VHvWWKJLQWSeVxPYhryv0paBFG8w5VfJIMIDOhb0GOqUBwihIOaL8EblH9M5uKcxGlqDC6AZWalEDYFVeoOA%2BrMOYmmK2NNg0%2FEeneo3t3MiAaHo3fO%2BbFcm7v7PaoEYqNyw%2FnZMUGuR5min68bg3c6%2FbINb%2F88SX0NWPftCkAu7K1ugqXDjchCb5iWIe4QU4OtE18ynrRsnIt5Yn54fAc0XVmAGkrzyMtUG5yGXe9W1BjfH%2FLCAZVgbrwpezzHSUAqHfr626&X-Amz-Signature=768c52839d505e05428e29cb4f79d64c3a55114c259f4ca0988bff2e3d87e770&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Correlation Plot
Heatmap visualizes correlations among variables. Color scheme indicates Pearson correlation coefficients. Dark red diagonal line shows perfect correlation (value of 1) between variables and themselves.
This heatmap offers overview of variable relationships and their link with price.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cd3b341e-cc1a-45f7-8aec-cdc00436d270/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VYKOLHIF%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T010833Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAkaCXVzLXdlc3QtMiJHMEUCIQD24oqYspX5NqB%2Bggktv8F1jZNS9sBmBDneJ3Ne7KZ6oAIgYBPblc5ZFVas5wy2sVNHoTUnW1qqtHUe0zVuRP1s4joq%2FwMIIhAAGgw2Mzc0MjMxODM4MDUiDPaEWzGUZk0ZP7YnQSrcA6PM4eZztX%2BnlC5MFgEeVuvflXiLkMDmggXBIZc1u3iInfmcZS0y4VHNKdXYZgMKgM2po%2BkmVSOB3f3pYA6xfnZJQV4Pat38BwmAxWBve2vdol1NKYqOK0oWQAG239F7BcDbp%2FW7aXU6Nwg5At7BTjvQdeUPDfI6nsCjIUl1KZJAnCQ7rFb%2Fuj4q3GtRpS%2F9e0Y%2FVF5ZoPA%2F9syHuqUBtFAQKVy0MV5pvokXh6FUm7eE5PSwdiImWt7R5EM1QaqLoCZSYO3GRmcCH6v%2FjclJa21h9ALLhl7f10A%2B2rrZss17hCq794oOPKp%2BVR6ywLChMCqRjyDr5klgO%2Bd76O3bFFCCFhq%2FBl9%2B1y6Qs1y3CN2TpFs2YyJLLBt7Rt1VYwSxMULIEP6%2FMhYu7a7Dh3UPfriQIcjX7KtzvBNWmXzckAtwQbZXfBbG%2F7%2F145BePxq1gUk%2FOJVfLK6FZ4nsTsBDSKQ2Ox0w%2F0En55yVsxWmk25ltN5hVlt88DeYU6431nOjDNLLJtCRonstWlBsnhetw8lkBkOwZVVYkuYRAXCmYB6E9O9tfMcrBhKOcKWpsu6Sn04xYdQbirj1gcRs%2FG0Uu9IaW%2B8VHvWWKJLQWSeVxPYhryv0paBFG8w5VfJIMIDOhb0GOqUBwihIOaL8EblH9M5uKcxGlqDC6AZWalEDYFVeoOA%2BrMOYmmK2NNg0%2FEeneo3t3MiAaHo3fO%2BbFcm7v7PaoEYqNyw%2FnZMUGuR5min68bg3c6%2FbINb%2F88SX0NWPftCkAu7K1ugqXDjchCb5iWIe4QU4OtE18ynrRsnIt5Yn54fAc0XVmAGkrzyMtUG5yGXe9W1BjfH%2FLCAZVgbrwpezzHSUAqHfr626&X-Amz-Signature=eefad85b88f51564f7dfcc7b08f00ccd33fcedb1e49d5757038f0faf98a354bc&X-Amz-SignedHeaders=host&x-id=GetObject)

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
