

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7e6d594d-952e-44b6-97ea-31225882aea6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UD4WF3U7%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T211353Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEE0aCXVzLXdlc3QtMiJIMEYCIQCiIJrr%2FkWzHD2xsXPOX80%2BtqXGB8OCaU2P4udx%2FdvknQIhAJtPoZViwEYXaXEesGnLLbSIXju%2B6l8DV%2B9c2sicyaaAKv8DCGUQABoMNjM3NDIzMTgzODA1IgxwpJCur28%2BcnU7l6kq3APDMfAoBn9t0m2quSSuKm1W53PdthiK6%2Bja5km8e2PIuZGiWc2waCFl8I%2FnaFFgbBE8Ga9pBro0EvkNj8mOGJB2zQneLodu7k6vFDz8mIIYWudZdf5Amrt3a5BYAXMrprWKAnQh95w%2BFIgpQ7jS7M2OI9zkDeoziVDwItpEsT2Jztw0Ab%2FJJPgwNJdS7cp%2F9X8we598BOK0uaSNUwNeHVJgFKDQ%2F3EiX827wpTP9NQJ%2Ftk2kuVVGLPcV1zlLvx40jZE3Gcoj8SHZGjmkYFyKBrcyG1Erl%2BeMAY%2FIYbJRaer5GKD%2Bp75gWxDv392IrNePmdtTeA0%2FNK2j9%2FlU59oiWMaqeNHKvlaLn2s60bf1f5Wa1jXiosHDPokP72J%2FNplWUr2mLutawkDiKhWt7lVKf5qnr1%2FQyi4LtGJ5EupYHQb6T6nf%2BHxBuIXnMl%2BvS5IBKTpuaLZorAya2LGOFARPyf6ux7RY%2FpHZq7%2FtLay1YRaY8ezO2lmP%2BZ1BPzh%2FPKHlDVEPZDqLSTUVzcQxcnWMyt5Kz%2FqA4RXECjQ%2BQFHNwgVVmHOtj%2BCMtDF0b%2BtoojBPS3%2FI36sZFFF49Igf5wAffkizlW3akKCspw1W3jA%2Bg2Re542r8hCusK9uqbauTDtuJS9BjqkARIXGhTDaXlczXXeVA85jvLPb4xgnD4UadVLjH2uyPBRMYeT5MVW2XLfYTVGmGTiPcSThKA7U33t0qFljxSr9o6mFce7xBLZVuFFkhDcijEHEnsB6sCE9g%2FYIwkSUeJkt2Cpvr%2B4BF0w2RHt5QtjjHMV1fovXVCaG5tTqv6LKaOg5TErGtnN%2FIXLTg8NSbVM3KNFR7Z4dQYc9uahMww%2BpFo6Fq0K&X-Amz-Signature=d87531d0e64d4c95c46ac456851c852af919b94e820b826af6ec6377cdb08c60&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cbfaed9e-b398-4902-8936-dea058b21def/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UD4WF3U7%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T211353Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEE0aCXVzLXdlc3QtMiJIMEYCIQCiIJrr%2FkWzHD2xsXPOX80%2BtqXGB8OCaU2P4udx%2FdvknQIhAJtPoZViwEYXaXEesGnLLbSIXju%2B6l8DV%2B9c2sicyaaAKv8DCGUQABoMNjM3NDIzMTgzODA1IgxwpJCur28%2BcnU7l6kq3APDMfAoBn9t0m2quSSuKm1W53PdthiK6%2Bja5km8e2PIuZGiWc2waCFl8I%2FnaFFgbBE8Ga9pBro0EvkNj8mOGJB2zQneLodu7k6vFDz8mIIYWudZdf5Amrt3a5BYAXMrprWKAnQh95w%2BFIgpQ7jS7M2OI9zkDeoziVDwItpEsT2Jztw0Ab%2FJJPgwNJdS7cp%2F9X8we598BOK0uaSNUwNeHVJgFKDQ%2F3EiX827wpTP9NQJ%2Ftk2kuVVGLPcV1zlLvx40jZE3Gcoj8SHZGjmkYFyKBrcyG1Erl%2BeMAY%2FIYbJRaer5GKD%2Bp75gWxDv392IrNePmdtTeA0%2FNK2j9%2FlU59oiWMaqeNHKvlaLn2s60bf1f5Wa1jXiosHDPokP72J%2FNplWUr2mLutawkDiKhWt7lVKf5qnr1%2FQyi4LtGJ5EupYHQb6T6nf%2BHxBuIXnMl%2BvS5IBKTpuaLZorAya2LGOFARPyf6ux7RY%2FpHZq7%2FtLay1YRaY8ezO2lmP%2BZ1BPzh%2FPKHlDVEPZDqLSTUVzcQxcnWMyt5Kz%2FqA4RXECjQ%2BQFHNwgVVmHOtj%2BCMtDF0b%2BtoojBPS3%2FI36sZFFF49Igf5wAffkizlW3akKCspw1W3jA%2Bg2Re542r8hCusK9uqbauTDtuJS9BjqkARIXGhTDaXlczXXeVA85jvLPb4xgnD4UadVLjH2uyPBRMYeT5MVW2XLfYTVGmGTiPcSThKA7U33t0qFljxSr9o6mFce7xBLZVuFFkhDcijEHEnsB6sCE9g%2FYIwkSUeJkt2Cpvr%2B4BF0w2RHt5QtjjHMV1fovXVCaG5tTqv6LKaOg5TErGtnN%2FIXLTg8NSbVM3KNFR7Z4dQYc9uahMww%2BpFo6Fq0K&X-Amz-Signature=67138e3062c6c883878778d5ca17a9c2ffdaeb02fdcfeccd8b0738c9aaa8e237&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/91181646-b1e0-4433-9711-6259a96a9247/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UD4WF3U7%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T211353Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEE0aCXVzLXdlc3QtMiJIMEYCIQCiIJrr%2FkWzHD2xsXPOX80%2BtqXGB8OCaU2P4udx%2FdvknQIhAJtPoZViwEYXaXEesGnLLbSIXju%2B6l8DV%2B9c2sicyaaAKv8DCGUQABoMNjM3NDIzMTgzODA1IgxwpJCur28%2BcnU7l6kq3APDMfAoBn9t0m2quSSuKm1W53PdthiK6%2Bja5km8e2PIuZGiWc2waCFl8I%2FnaFFgbBE8Ga9pBro0EvkNj8mOGJB2zQneLodu7k6vFDz8mIIYWudZdf5Amrt3a5BYAXMrprWKAnQh95w%2BFIgpQ7jS7M2OI9zkDeoziVDwItpEsT2Jztw0Ab%2FJJPgwNJdS7cp%2F9X8we598BOK0uaSNUwNeHVJgFKDQ%2F3EiX827wpTP9NQJ%2Ftk2kuVVGLPcV1zlLvx40jZE3Gcoj8SHZGjmkYFyKBrcyG1Erl%2BeMAY%2FIYbJRaer5GKD%2Bp75gWxDv392IrNePmdtTeA0%2FNK2j9%2FlU59oiWMaqeNHKvlaLn2s60bf1f5Wa1jXiosHDPokP72J%2FNplWUr2mLutawkDiKhWt7lVKf5qnr1%2FQyi4LtGJ5EupYHQb6T6nf%2BHxBuIXnMl%2BvS5IBKTpuaLZorAya2LGOFARPyf6ux7RY%2FpHZq7%2FtLay1YRaY8ezO2lmP%2BZ1BPzh%2FPKHlDVEPZDqLSTUVzcQxcnWMyt5Kz%2FqA4RXECjQ%2BQFHNwgVVmHOtj%2BCMtDF0b%2BtoojBPS3%2FI36sZFFF49Igf5wAffkizlW3akKCspw1W3jA%2Bg2Re542r8hCusK9uqbauTDtuJS9BjqkARIXGhTDaXlczXXeVA85jvLPb4xgnD4UadVLjH2uyPBRMYeT5MVW2XLfYTVGmGTiPcSThKA7U33t0qFljxSr9o6mFce7xBLZVuFFkhDcijEHEnsB6sCE9g%2FYIwkSUeJkt2Cpvr%2B4BF0w2RHt5QtjjHMV1fovXVCaG5tTqv6LKaOg5TErGtnN%2FIXLTg8NSbVM3KNFR7Z4dQYc9uahMww%2BpFo6Fq0K&X-Amz-Signature=64478e54cf3175075c72cb2b00b6adc8747726cc996585af635e522a817ed29f&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/09aba1c0-0d55-41dd-852a-a04c5b8a3fac/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XG2JVQ3I%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T211356Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEE0aCXVzLXdlc3QtMiJGMEQCIHYvG3KVflQZWCYe1DDDORXkYJb5tuhBOa0G2LtQ56hxAiBufOQtCs0XGrQOqiIOer%2B7XLJMPu6XFyApn%2B2dl0f9lSr%2FAwhmEAAaDDYzNzQyMzE4MzgwNSIMgRvXKFFonkofBsgkKtwDbK4mpyut3iETq8bm%2BiHl6dv3y%2BU53wvPCzngTRfPZ3J0Rt14mLbPbhluxjaX2%2Fv0wi2FPlfMEMOruacb6%2BkK6%2FilGklIqZ6pf1RJqmTCpeUXdCCke0BznZ%2B9eGSJ2bw2SOcPEKSI%2FOWnJB4G5%2B7kg7uwsJYXONP1n7EMT%2FXc%2FIyQBsMzND%2B%2BNAw8zED5rj6h%2FCCu766n8a3wIjFPGe3iIRoAjXxy60pu3JuR1gnHBnKHSNAmIyoQrME%2FTTICaYk4gl88TbBCQKRemhwuDJZAuwUL5jRKQfK5Krzl6DFDz8iddpMXxDxDVm9mxZMevcyiRe0qpMKs%2F0KUQpjAGgPP%2FPSxXhkPSbweMqg0zG2x8VRIk4ev9MIszEt%2FYX8o3s4LwXm%2FuQpwv1pgWhufgn8n2VFty9loVDi0CMadRrQDtq6f2cXlEcRuNFBIJgrV%2BkqGlEaUbCXvwJv6yOqby2jkcYY8rNLD8m49nQyse9aCLp8OYUmkBtBqH3PJAqhX1NOZJw37ENAUglSOw4MlMuUsNZhhZ6auOc4G4mdBsaQA5WSjAns4c0UZEcv%2FdRCWg5LdkG%2FZGHqS%2FB8W3Q11UNzguTReb0mRWM14zOXNQXlq%2Fmxl2ZvvuMUzH3v1mfAwjriUvQY6pgGOxTqgmmBVclwanvLMksPLollVee02tmT8XHx4fr0VwV3ekwPCAXNqkYVuYHMg07xSAUdeMessQbcl2u1C5Famc7pC4DlbLPv3VptnsmQeWjZqpdbmtmkD6vMZtAWRZSlgZ4n7wz%2B6hqLwrw60bFjcd%2FSVQbNiX9JJR70x15ngfyNW%2BV9USOFaS4e6di%2BgcIzM%2BMwuJYmXx13kEkRevy8vj4Omp0%2Bv&X-Amz-Signature=e2b3feb387b4af6ed44629a17935a232a86abe6187eeb0899f07d67bb17763e9&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 2. Scatter Plot
Scatter plots present the relationship between two variables in a dataset. It represents data points on a two-dimensional plane. The independent variable or attribute is plotted on the X-axis, while the dependent variable is plotted on the Y-axis.
**Syntax:**
```python
plt.scatter(x, y)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23708af9-659f-4f23-b626-1a4292d7842c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XG2JVQ3I%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T211356Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEE0aCXVzLXdlc3QtMiJGMEQCIHYvG3KVflQZWCYe1DDDORXkYJb5tuhBOa0G2LtQ56hxAiBufOQtCs0XGrQOqiIOer%2B7XLJMPu6XFyApn%2B2dl0f9lSr%2FAwhmEAAaDDYzNzQyMzE4MzgwNSIMgRvXKFFonkofBsgkKtwDbK4mpyut3iETq8bm%2BiHl6dv3y%2BU53wvPCzngTRfPZ3J0Rt14mLbPbhluxjaX2%2Fv0wi2FPlfMEMOruacb6%2BkK6%2FilGklIqZ6pf1RJqmTCpeUXdCCke0BznZ%2B9eGSJ2bw2SOcPEKSI%2FOWnJB4G5%2B7kg7uwsJYXONP1n7EMT%2FXc%2FIyQBsMzND%2B%2BNAw8zED5rj6h%2FCCu766n8a3wIjFPGe3iIRoAjXxy60pu3JuR1gnHBnKHSNAmIyoQrME%2FTTICaYk4gl88TbBCQKRemhwuDJZAuwUL5jRKQfK5Krzl6DFDz8iddpMXxDxDVm9mxZMevcyiRe0qpMKs%2F0KUQpjAGgPP%2FPSxXhkPSbweMqg0zG2x8VRIk4ev9MIszEt%2FYX8o3s4LwXm%2FuQpwv1pgWhufgn8n2VFty9loVDi0CMadRrQDtq6f2cXlEcRuNFBIJgrV%2BkqGlEaUbCXvwJv6yOqby2jkcYY8rNLD8m49nQyse9aCLp8OYUmkBtBqH3PJAqhX1NOZJw37ENAUglSOw4MlMuUsNZhhZ6auOc4G4mdBsaQA5WSjAns4c0UZEcv%2FdRCWg5LdkG%2FZGHqS%2FB8W3Q11UNzguTReb0mRWM14zOXNQXlq%2Fmxl2ZvvuMUzH3v1mfAwjriUvQY6pgGOxTqgmmBVclwanvLMksPLollVee02tmT8XHx4fr0VwV3ekwPCAXNqkYVuYHMg07xSAUdeMessQbcl2u1C5Famc7pC4DlbLPv3VptnsmQeWjZqpdbmtmkD6vMZtAWRZSlgZ4n7wz%2B6hqLwrw60bFjcd%2FSVQbNiX9JJR70x15ngfyNW%2BV9USOFaS4e6di%2BgcIzM%2BMwuJYmXx13kEkRevy8vj4Omp0%2Bv&X-Amz-Signature=8010372fd9057cdac15bc603e9e67adf71d2995c06e8c12eae5bed0382b95b3e&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 3. Histogram
A histogram is an important visual representation of data in categorical form. To view the data in a "Binned" form, use the histogram plot with a number of bins required or with the data points that mark the bin edges. The x-axis represents the data bins, and the y-axis represents the number of elements in each bin.
**Syntax:**
```python
plt.hist(x, bins)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/24e4424a-df87-40a1-b63b-195cbdc2e0ab/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XG2JVQ3I%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T211356Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEE0aCXVzLXdlc3QtMiJGMEQCIHYvG3KVflQZWCYe1DDDORXkYJb5tuhBOa0G2LtQ56hxAiBufOQtCs0XGrQOqiIOer%2B7XLJMPu6XFyApn%2B2dl0f9lSr%2FAwhmEAAaDDYzNzQyMzE4MzgwNSIMgRvXKFFonkofBsgkKtwDbK4mpyut3iETq8bm%2BiHl6dv3y%2BU53wvPCzngTRfPZ3J0Rt14mLbPbhluxjaX2%2Fv0wi2FPlfMEMOruacb6%2BkK6%2FilGklIqZ6pf1RJqmTCpeUXdCCke0BznZ%2B9eGSJ2bw2SOcPEKSI%2FOWnJB4G5%2B7kg7uwsJYXONP1n7EMT%2FXc%2FIyQBsMzND%2B%2BNAw8zED5rj6h%2FCCu766n8a3wIjFPGe3iIRoAjXxy60pu3JuR1gnHBnKHSNAmIyoQrME%2FTTICaYk4gl88TbBCQKRemhwuDJZAuwUL5jRKQfK5Krzl6DFDz8iddpMXxDxDVm9mxZMevcyiRe0qpMKs%2F0KUQpjAGgPP%2FPSxXhkPSbweMqg0zG2x8VRIk4ev9MIszEt%2FYX8o3s4LwXm%2FuQpwv1pgWhufgn8n2VFty9loVDi0CMadRrQDtq6f2cXlEcRuNFBIJgrV%2BkqGlEaUbCXvwJv6yOqby2jkcYY8rNLD8m49nQyse9aCLp8OYUmkBtBqH3PJAqhX1NOZJw37ENAUglSOw4MlMuUsNZhhZ6auOc4G4mdBsaQA5WSjAns4c0UZEcv%2FdRCWg5LdkG%2FZGHqS%2FB8W3Q11UNzguTReb0mRWM14zOXNQXlq%2Fmxl2ZvvuMUzH3v1mfAwjriUvQY6pgGOxTqgmmBVclwanvLMksPLollVee02tmT8XHx4fr0VwV3ekwPCAXNqkYVuYHMg07xSAUdeMessQbcl2u1C5Famc7pC4DlbLPv3VptnsmQeWjZqpdbmtmkD6vMZtAWRZSlgZ4n7wz%2B6hqLwrw60bFjcd%2FSVQbNiX9JJR70x15ngfyNW%2BV9USOFaS4e6di%2BgcIzM%2BMwuJYmXx13kEkRevy8vj4Omp0%2Bv&X-Amz-Signature=f5c75c2381d9788db9e85ce90136cba37a7922f8714a2d0df67aeda9893a98b7&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ab5a6dfe-51f5-43ee-bcb3-33dae4a1c7ad/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XG2JVQ3I%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T211356Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEE0aCXVzLXdlc3QtMiJGMEQCIHYvG3KVflQZWCYe1DDDORXkYJb5tuhBOa0G2LtQ56hxAiBufOQtCs0XGrQOqiIOer%2B7XLJMPu6XFyApn%2B2dl0f9lSr%2FAwhmEAAaDDYzNzQyMzE4MzgwNSIMgRvXKFFonkofBsgkKtwDbK4mpyut3iETq8bm%2BiHl6dv3y%2BU53wvPCzngTRfPZ3J0Rt14mLbPbhluxjaX2%2Fv0wi2FPlfMEMOruacb6%2BkK6%2FilGklIqZ6pf1RJqmTCpeUXdCCke0BznZ%2B9eGSJ2bw2SOcPEKSI%2FOWnJB4G5%2B7kg7uwsJYXONP1n7EMT%2FXc%2FIyQBsMzND%2B%2BNAw8zED5rj6h%2FCCu766n8a3wIjFPGe3iIRoAjXxy60pu3JuR1gnHBnKHSNAmIyoQrME%2FTTICaYk4gl88TbBCQKRemhwuDJZAuwUL5jRKQfK5Krzl6DFDz8iddpMXxDxDVm9mxZMevcyiRe0qpMKs%2F0KUQpjAGgPP%2FPSxXhkPSbweMqg0zG2x8VRIk4ev9MIszEt%2FYX8o3s4LwXm%2FuQpwv1pgWhufgn8n2VFty9loVDi0CMadRrQDtq6f2cXlEcRuNFBIJgrV%2BkqGlEaUbCXvwJv6yOqby2jkcYY8rNLD8m49nQyse9aCLp8OYUmkBtBqH3PJAqhX1NOZJw37ENAUglSOw4MlMuUsNZhhZ6auOc4G4mdBsaQA5WSjAns4c0UZEcv%2FdRCWg5LdkG%2FZGHqS%2FB8W3Q11UNzguTReb0mRWM14zOXNQXlq%2Fmxl2ZvvuMUzH3v1mfAwjriUvQY6pgGOxTqgmmBVclwanvLMksPLollVee02tmT8XHx4fr0VwV3ekwPCAXNqkYVuYHMg07xSAUdeMessQbcl2u1C5Famc7pC4DlbLPv3VptnsmQeWjZqpdbmtmkD6vMZtAWRZSlgZ4n7wz%2B6hqLwrw60bFjcd%2FSVQbNiX9JJR70x15ngfyNW%2BV9USOFaS4e6di%2BgcIzM%2BMwuJYmXx13kEkRevy8vj4Omp0%2Bv&X-Amz-Signature=31967bfd0a98c58181cb781253fac0390f813e0ae4238543f5212965c739f787&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8f1b1d60-cf1b-42b3-9faa-f634c89c3f84/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XG2JVQ3I%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T211356Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEE0aCXVzLXdlc3QtMiJGMEQCIHYvG3KVflQZWCYe1DDDORXkYJb5tuhBOa0G2LtQ56hxAiBufOQtCs0XGrQOqiIOer%2B7XLJMPu6XFyApn%2B2dl0f9lSr%2FAwhmEAAaDDYzNzQyMzE4MzgwNSIMgRvXKFFonkofBsgkKtwDbK4mpyut3iETq8bm%2BiHl6dv3y%2BU53wvPCzngTRfPZ3J0Rt14mLbPbhluxjaX2%2Fv0wi2FPlfMEMOruacb6%2BkK6%2FilGklIqZ6pf1RJqmTCpeUXdCCke0BznZ%2B9eGSJ2bw2SOcPEKSI%2FOWnJB4G5%2B7kg7uwsJYXONP1n7EMT%2FXc%2FIyQBsMzND%2B%2BNAw8zED5rj6h%2FCCu766n8a3wIjFPGe3iIRoAjXxy60pu3JuR1gnHBnKHSNAmIyoQrME%2FTTICaYk4gl88TbBCQKRemhwuDJZAuwUL5jRKQfK5Krzl6DFDz8iddpMXxDxDVm9mxZMevcyiRe0qpMKs%2F0KUQpjAGgPP%2FPSxXhkPSbweMqg0zG2x8VRIk4ev9MIszEt%2FYX8o3s4LwXm%2FuQpwv1pgWhufgn8n2VFty9loVDi0CMadRrQDtq6f2cXlEcRuNFBIJgrV%2BkqGlEaUbCXvwJv6yOqby2jkcYY8rNLD8m49nQyse9aCLp8OYUmkBtBqH3PJAqhX1NOZJw37ENAUglSOw4MlMuUsNZhhZ6auOc4G4mdBsaQA5WSjAns4c0UZEcv%2FdRCWg5LdkG%2FZGHqS%2FB8W3Q11UNzguTReb0mRWM14zOXNQXlq%2Fmxl2ZvvuMUzH3v1mfAwjriUvQY6pgGOxTqgmmBVclwanvLMksPLollVee02tmT8XHx4fr0VwV3ekwPCAXNqkYVuYHMg07xSAUdeMessQbcl2u1C5Famc7pC4DlbLPv3VptnsmQeWjZqpdbmtmkD6vMZtAWRZSlgZ4n7wz%2B6hqLwrw60bFjcd%2FSVQbNiX9JJR70x15ngfyNW%2BV9USOFaS4e6di%2BgcIzM%2BMwuJYmXx13kEkRevy8vj4Omp0%2Bv&X-Amz-Signature=8928e3a144df303b403061691727bcab836dd0eb542ecc6770ddc31223805aee&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/13ad0497-05fe-4eaa-984e-707b33e14761/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XG2JVQ3I%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T211357Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEE0aCXVzLXdlc3QtMiJGMEQCIHYvG3KVflQZWCYe1DDDORXkYJb5tuhBOa0G2LtQ56hxAiBufOQtCs0XGrQOqiIOer%2B7XLJMPu6XFyApn%2B2dl0f9lSr%2FAwhmEAAaDDYzNzQyMzE4MzgwNSIMgRvXKFFonkofBsgkKtwDbK4mpyut3iETq8bm%2BiHl6dv3y%2BU53wvPCzngTRfPZ3J0Rt14mLbPbhluxjaX2%2Fv0wi2FPlfMEMOruacb6%2BkK6%2FilGklIqZ6pf1RJqmTCpeUXdCCke0BznZ%2B9eGSJ2bw2SOcPEKSI%2FOWnJB4G5%2B7kg7uwsJYXONP1n7EMT%2FXc%2FIyQBsMzND%2B%2BNAw8zED5rj6h%2FCCu766n8a3wIjFPGe3iIRoAjXxy60pu3JuR1gnHBnKHSNAmIyoQrME%2FTTICaYk4gl88TbBCQKRemhwuDJZAuwUL5jRKQfK5Krzl6DFDz8iddpMXxDxDVm9mxZMevcyiRe0qpMKs%2F0KUQpjAGgPP%2FPSxXhkPSbweMqg0zG2x8VRIk4ev9MIszEt%2FYX8o3s4LwXm%2FuQpwv1pgWhufgn8n2VFty9loVDi0CMadRrQDtq6f2cXlEcRuNFBIJgrV%2BkqGlEaUbCXvwJv6yOqby2jkcYY8rNLD8m49nQyse9aCLp8OYUmkBtBqH3PJAqhX1NOZJw37ENAUglSOw4MlMuUsNZhhZ6auOc4G4mdBsaQA5WSjAns4c0UZEcv%2FdRCWg5LdkG%2FZGHqS%2FB8W3Q11UNzguTReb0mRWM14zOXNQXlq%2Fmxl2ZvvuMUzH3v1mfAwjriUvQY6pgGOxTqgmmBVclwanvLMksPLollVee02tmT8XHx4fr0VwV3ekwPCAXNqkYVuYHMg07xSAUdeMessQbcl2u1C5Famc7pC4DlbLPv3VptnsmQeWjZqpdbmtmkD6vMZtAWRZSlgZ4n7wz%2B6hqLwrw60bFjcd%2FSVQbNiX9JJR70x15ngfyNW%2BV9USOFaS4e6di%2BgcIzM%2BMwuJYmXx13kEkRevy8vj4Omp0%2Bv&X-Amz-Signature=96f50f710d29f52f6ee5e901f0ccfdffbecc7a980b3f866c056432cb8fab8f8e&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 2. Box and Whisker Plot
A box plot shows the distribution of quantitative data in a way that facilitates comparisons between variables or across levels of a categorical variable. The box shows the quartiles of the dataset while the whiskers extend to show the rest of the distribution, except for points that are determined to be "outliers".
**Syntax:**
```python
sns.boxplot(x='header_1', y='header_2', data=df)
```
**Example Output:**


![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d207ae92-0a7c-4e2f-aa65-0ee5a2c33bf7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RLF2XKBQ%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T211358Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEE0aCXVzLXdlc3QtMiJIMEYCIQC2LD7gxpSfrrFmkqd1poxq2NZxWexr5FANh7NAytkU2QIhAJV2RqEkyy9jtV%2Bi1b5P3SXmV3gO2lw1DIi4DlGtjWUlKv8DCGYQABoMNjM3NDIzMTgzODA1IgxSr8Yk6oM0WHeUdY8q3AOUje3b3JL%2B1LQRceK7CQWi4knv%2FkUXu2K%2FNvnC0982xSCs99cum2UlcGwW79YrBPVaa9cHkGZPHWFNN%2BhfehkhLGz2zYoOBaqCLNecweYxQapiBGQ8HBYNWzyqkP3ZRmU%2FBVFGnHLMgcQJIWZvFuwY1J9%2FaUB3E36wjxsf52ebIKVjwpWMKXA%2F3qxHfRzFG68Z5jxTKyxN3AwrSJScBjBiUDDb3QNhlSKEk3uifBM7bIOs%2FQN1UkOAzFxmziUwMhfkPMtY9K%2FZwXqnw0FM7VWXkoxQ0MgDnBcB57krNoYEJNNKaDhybH9neDoV5v%2FaVsPthUA3qxtk94wmiABD5MFIqkmKMJ0rRi%2Bk7z4PVrFdrceEcbMLAkeXq0EkltZSgwTiRBnkpXVraxO7JCQFdk7%2BKEiYP%2B8moiV%2BFzuVrCY7jzzUzwnS8UkVWuDyrH6WHIv5kX4gbYoCW8mDCmg3xFYCiuxyKWT%2BeMqiIu%2FU1xh8XulGN9llmhfYg3CmGOyuv2RD4nrLIBQqGNlR%2BixizummzAips833X7MKOcvm8GF%2BMj%2BMnXfPOSdXKVZ3eHhfAalnj%2FhcZaubeijtkwkqFMQn3Id%2Ba4ecYX3A%2FI6G%2Fwsqjwycuzm5oIuJYWlryDCjuJS9BjqkAVXXlXWgq15rBEuh4L7wyuTXtY%2FiGeaxD3yyxZAEqhzpnF45ZcIO6dEqcOEHriggP4FmJ%2B1VREAj%2BzR7Op11aQ3WOPUtUa%2FFA8h8qdHZYmczSyDS4laK3ZisA1cNWHTzGT0Wy%2FOjT6WK6uzyNPR8XCMCmD%2FnojAaCeUxQnkQCOfdjsKSjaXRNMRhUBN3nB0%2FHg4Bk2VkADPSl8fWc87unE1Rmnw7&X-Amz-Signature=93204715ca28b9ef4523d380cbe5284acbca0dc903fdb24c39849c89099fd68c&X-Amz-SignedHeaders=host&x-id=GetObject)

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0e516edc-7551-4792-ab18-0494db3c4c0c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666H56M5D7%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T211358Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEE0aCXVzLXdlc3QtMiJIMEYCIQCcwq7vjg6%2Bs80VyFzz0wDvXV7YvgaVmMz6iW%2B8BVBIkQIhAOizArADw60OGFtsjUAhwCY0Fz7cB8ZOkeIn9Q4kYIyMKv8DCGYQABoMNjM3NDIzMTgzODA1IgwrLBw5hyHOfEu0dwQq3AMM%2BLtVowolV7MjvaOyE5vMfju7GYWxPXf0CAo3LmTVVUFfmvMPI%2BpUY2N66jD7tMSKMyUJoRg80fyGT0uzTtVvQwVxHrsn6TzWgL3UT%2F2dfj0AMmaluluT5ouVo3P2%2BiKu3Yirn3zE5YBMfaSV6LZPqYXul0tRHDyKuzrQtNH2CbRZX9GYtu9fbEZd6G25jE5Z1Uu1PASCivEptlUKMY7Q8cPCBUD6QfY1qsuhGoZkXmqxw4eLIjT9EBwz1uayCSNAH1qQn5ZM%2F0d6lqULjOUPNJMUN0w8xq8SU2EcJk50qwoTTa4LsZfrGA0irKjdD60gC9ehygJtvlx2RAUhWHoLFLUpV2vAZgzVvvIHYHvLTP5ZkoRZqFXMgSAU8nv9DfwSiRbbs55gf4YXolyDZSB2ptmiRKP0caQ1Z4xuwFk0x4F8H8wQrTkUBaevZ4LjemQcxa05jRlj5sIbwH8HdqRVHXqgDFgIRPAju6%2B3lVU4pNg%2FZVlkWbj5Q4LBOxDxJHdBakg5bONwu6RwXGsLm%2BScQF8PXUM%2FHzsG2CuiHessCy4DD8vF85bEvjXsHgoGni9nK%2BifFUBrDuWSE4luIoj2muAdPSeXvaN2yIU8whteVu6m8j%2BfWS350VH8BjDNuJS9BjqkAYIgVZioZphPlfDNswvSX%2B0MvLeaS74uLM%2BwjJWe8ZP2wRSwDC0U7rZWPt7%2FOO8VlXLGd5OjXL542vXgonKjpzEzVbE6p6BlQZN%2BP%2FdcB5lLaF9v3UW5oVL7TqL72gtU1y1wQhwzLinExPbNfFxHuW6Ahic37T54m6fi%2BETcysLblrp%2FNFyntwmxG8IwTHWYOxA0I%2FwjgboFFNnJnybjQhdbbKvy&X-Amz-Signature=bd5c4a131d9cbb2ebbb3f16a1d1653271efd283fb359b2edab936a0806348ba1&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23a79b9d-2356-49a9-8fd9-65c6b0ab2cc5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XG2JVQ3I%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T211357Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEE0aCXVzLXdlc3QtMiJGMEQCIHYvG3KVflQZWCYe1DDDORXkYJb5tuhBOa0G2LtQ56hxAiBufOQtCs0XGrQOqiIOer%2B7XLJMPu6XFyApn%2B2dl0f9lSr%2FAwhmEAAaDDYzNzQyMzE4MzgwNSIMgRvXKFFonkofBsgkKtwDbK4mpyut3iETq8bm%2BiHl6dv3y%2BU53wvPCzngTRfPZ3J0Rt14mLbPbhluxjaX2%2Fv0wi2FPlfMEMOruacb6%2BkK6%2FilGklIqZ6pf1RJqmTCpeUXdCCke0BznZ%2B9eGSJ2bw2SOcPEKSI%2FOWnJB4G5%2B7kg7uwsJYXONP1n7EMT%2FXc%2FIyQBsMzND%2B%2BNAw8zED5rj6h%2FCCu766n8a3wIjFPGe3iIRoAjXxy60pu3JuR1gnHBnKHSNAmIyoQrME%2FTTICaYk4gl88TbBCQKRemhwuDJZAuwUL5jRKQfK5Krzl6DFDz8iddpMXxDxDVm9mxZMevcyiRe0qpMKs%2F0KUQpjAGgPP%2FPSxXhkPSbweMqg0zG2x8VRIk4ev9MIszEt%2FYX8o3s4LwXm%2FuQpwv1pgWhufgn8n2VFty9loVDi0CMadRrQDtq6f2cXlEcRuNFBIJgrV%2BkqGlEaUbCXvwJv6yOqby2jkcYY8rNLD8m49nQyse9aCLp8OYUmkBtBqH3PJAqhX1NOZJw37ENAUglSOw4MlMuUsNZhhZ6auOc4G4mdBsaQA5WSjAns4c0UZEcv%2FdRCWg5LdkG%2FZGHqS%2FB8W3Q11UNzguTReb0mRWM14zOXNQXlq%2Fmxl2ZvvuMUzH3v1mfAwjriUvQY6pgGOxTqgmmBVclwanvLMksPLollVee02tmT8XHx4fr0VwV3ekwPCAXNqkYVuYHMg07xSAUdeMessQbcl2u1C5Famc7pC4DlbLPv3VptnsmQeWjZqpdbmtmkD6vMZtAWRZSlgZ4n7wz%2B6hqLwrw60bFjcd%2FSVQbNiX9JJR70x15ngfyNW%2BV9USOFaS4e6di%2BgcIzM%2BMwuJYmXx13kEkRevy8vj4Omp0%2Bv&X-Amz-Signature=5b5c8ae1c4d1472ad7b545dd17472f9e3949cb7836a537f2e6f439616006a993&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 4. KDE Plot
A Kernel Density Estimate (KDE) plot is a graph that creates a probability distribution curve for the data based upon its likelihood of occurrence on a specific value. This is created for a single vector of information.
**Syntax:**
```python
sns.kdeplot(X) || sns.kdeplot(df['age'])
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0d571213-2a2f-4921-a50b-880847aa05ee/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XG2JVQ3I%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T211357Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEE0aCXVzLXdlc3QtMiJGMEQCIHYvG3KVflQZWCYe1DDDORXkYJb5tuhBOa0G2LtQ56hxAiBufOQtCs0XGrQOqiIOer%2B7XLJMPu6XFyApn%2B2dl0f9lSr%2FAwhmEAAaDDYzNzQyMzE4MzgwNSIMgRvXKFFonkofBsgkKtwDbK4mpyut3iETq8bm%2BiHl6dv3y%2BU53wvPCzngTRfPZ3J0Rt14mLbPbhluxjaX2%2Fv0wi2FPlfMEMOruacb6%2BkK6%2FilGklIqZ6pf1RJqmTCpeUXdCCke0BznZ%2B9eGSJ2bw2SOcPEKSI%2FOWnJB4G5%2B7kg7uwsJYXONP1n7EMT%2FXc%2FIyQBsMzND%2B%2BNAw8zED5rj6h%2FCCu766n8a3wIjFPGe3iIRoAjXxy60pu3JuR1gnHBnKHSNAmIyoQrME%2FTTICaYk4gl88TbBCQKRemhwuDJZAuwUL5jRKQfK5Krzl6DFDz8iddpMXxDxDVm9mxZMevcyiRe0qpMKs%2F0KUQpjAGgPP%2FPSxXhkPSbweMqg0zG2x8VRIk4ev9MIszEt%2FYX8o3s4LwXm%2FuQpwv1pgWhufgn8n2VFty9loVDi0CMadRrQDtq6f2cXlEcRuNFBIJgrV%2BkqGlEaUbCXvwJv6yOqby2jkcYY8rNLD8m49nQyse9aCLp8OYUmkBtBqH3PJAqhX1NOZJw37ENAUglSOw4MlMuUsNZhhZ6auOc4G4mdBsaQA5WSjAns4c0UZEcv%2FdRCWg5LdkG%2FZGHqS%2FB8W3Q11UNzguTReb0mRWM14zOXNQXlq%2Fmxl2ZvvuMUzH3v1mfAwjriUvQY6pgGOxTqgmmBVclwanvLMksPLollVee02tmT8XHx4fr0VwV3ekwPCAXNqkYVuYHMg07xSAUdeMessQbcl2u1C5Famc7pC4DlbLPv3VptnsmQeWjZqpdbmtmkD6vMZtAWRZSlgZ4n7wz%2B6hqLwrw60bFjcd%2FSVQbNiX9JJR70x15ngfyNW%2BV9USOFaS4e6di%2BgcIzM%2BMwuJYmXx13kEkRevy8vj4Omp0%2Bv&X-Amz-Signature=132d8e3d9301cfc014e6880b0f66d91b05fd69a2631c42c373b5aa017ffbe526&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/53752550-ef82-4ca9-a01a-09921f0282d0/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XG2JVQ3I%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T211357Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEE0aCXVzLXdlc3QtMiJGMEQCIHYvG3KVflQZWCYe1DDDORXkYJb5tuhBOa0G2LtQ56hxAiBufOQtCs0XGrQOqiIOer%2B7XLJMPu6XFyApn%2B2dl0f9lSr%2FAwhmEAAaDDYzNzQyMzE4MzgwNSIMgRvXKFFonkofBsgkKtwDbK4mpyut3iETq8bm%2BiHl6dv3y%2BU53wvPCzngTRfPZ3J0Rt14mLbPbhluxjaX2%2Fv0wi2FPlfMEMOruacb6%2BkK6%2FilGklIqZ6pf1RJqmTCpeUXdCCke0BznZ%2B9eGSJ2bw2SOcPEKSI%2FOWnJB4G5%2B7kg7uwsJYXONP1n7EMT%2FXc%2FIyQBsMzND%2B%2BNAw8zED5rj6h%2FCCu766n8a3wIjFPGe3iIRoAjXxy60pu3JuR1gnHBnKHSNAmIyoQrME%2FTTICaYk4gl88TbBCQKRemhwuDJZAuwUL5jRKQfK5Krzl6DFDz8iddpMXxDxDVm9mxZMevcyiRe0qpMKs%2F0KUQpjAGgPP%2FPSxXhkPSbweMqg0zG2x8VRIk4ev9MIszEt%2FYX8o3s4LwXm%2FuQpwv1pgWhufgn8n2VFty9loVDi0CMadRrQDtq6f2cXlEcRuNFBIJgrV%2BkqGlEaUbCXvwJv6yOqby2jkcYY8rNLD8m49nQyse9aCLp8OYUmkBtBqH3PJAqhX1NOZJw37ENAUglSOw4MlMuUsNZhhZ6auOc4G4mdBsaQA5WSjAns4c0UZEcv%2FdRCWg5LdkG%2FZGHqS%2FB8W3Q11UNzguTReb0mRWM14zOXNQXlq%2Fmxl2ZvvuMUzH3v1mfAwjriUvQY6pgGOxTqgmmBVclwanvLMksPLollVee02tmT8XHx4fr0VwV3ekwPCAXNqkYVuYHMg07xSAUdeMessQbcl2u1C5Famc7pC4DlbLPv3VptnsmQeWjZqpdbmtmkD6vMZtAWRZSlgZ4n7wz%2B6hqLwrw60bFjcd%2FSVQbNiX9JJR70x15ngfyNW%2BV9USOFaS4e6di%2BgcIzM%2BMwuJYmXx13kEkRevy8vj4Omp0%2Bv&X-Amz-Signature=bcd93e6c330e0778a83e3a2de6e53d8ca03fe362c78c88cf7373240910c0f90d&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
## 4. Correlation Between Variables
Correlation is a statistical measure of the extent to which different variables are interdependent. It indicates how changes in one variable are associated with changes in another variable over time.
### Positive Correlation
Positive correlation indicates that as one variable increases, the other variable also tends to increase.
**Example: Engine Size and Price**
- **Positive Correlation:** Engine size increases, price also increases.
- **Visualization:** Scatter plot with a steep positive slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c7ea9b0-3ef3-4357-a9c3-554fc71b6b15/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YGPJ6PNH%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T211357Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEE0aCXVzLXdlc3QtMiJHMEUCIDAFJ7MmrmhutIiYae1gsVuzsepsPzOLLk98KqHTCgiuAiEA4u4Jfez9M8kLBexo3dEtlY3RTEW8Zpp8aEKRTM4wQ1Eq%2FwMIZhAAGgw2Mzc0MjMxODM4MDUiDFFWfW8hcpwj%2B4CM5CrcA55ZuJX%2Fb%2FIJfxxeTE6FiDGlnKm%2BJLnIYNEYCXIgDMQVmK8mdwBCq2EqcmtQhJh6a3NG4NjVsmwy4jglBboKUDQFiN8HUcrfGnoPj%2BVnjn48DZLojiUvM4WFIvs3uZXm0zkR4jyK30TnMMwMVVRCuC%2Bxg5TkdZadgEKMY60gF2MboV2ojyJD0if4OCDV8qdpM7iP5emchucRkkHlzBOz%2FrVlb%2Fh6oKstWiuwLgFGoF5%2FhJ8go00GTvYKtEizY%2Fem%2BPZQptsAf4Z1y97Q%2BvX2bVab5ZmqNSeooeapZ874v4w%2BvTg7KD9lDisY8SuFDU4A64HcgHJ4eIh2Uukts%2FiKfdgdR%2FeYvZ92ZgW%2BGBybo%2FIM1a5i8gd4teSc1%2F0kUk5g0qdmQoDuZ%2Fz%2Fc8KObuYPEBws%2F7LWL1lsxC39LQU539HoTyEDqqv8%2FHXEt6lLtl22Usmuu0y6U6czjROEP%2FS8ZfT2G7R8204Rfj%2FGEhgP6RnU3wQtKY%2BhS%2BfKyKF8MsIicnUfWZe%2BQWw9sDvVkccnVy9wFUVO7KgHnf20LENjgvxKOmDJyWYCVZVZF3mXoh1Xtk0EtAukBCAupgUmml4U%2FTuRfVxNa7vu4cjfA2tuhGQSLIto9f6G0%2F8qQTSGMKi4lL0GOqUBSj4Ov02zvXGgOMzWTM2LSbvqjTXm8gSYLCtgdmbeAMTxRmsxhJwNbP6vsMkN417P1sh0ORpjP1hQ7SD2RTMye51CfveTbIkBoWYBGuqOyWRlNXw15rfF%2FvfDAfIOo2Ow2Xc7pHeTcMbnrLpAWMPM33kuFlW20lAz5lE0e8LFXW3UB4yT8xkfYiBBfZdiLwh014SMYgxKYMG69KHDk37ImNoBq6da&X-Amz-Signature=58c5ab339b0e6f9dc35db99ea88c239e2303b45548465a791c64b62470cb6c3d&X-Amz-SignedHeaders=host&x-id=GetObject)
**Explanation:** When engine size increases, there is a corresponding increase in the price of the vehicle. This positive correlation suggests that larger engines tend to be associated with higher prices in the market.
___
### Negative Correlation
Negative correlation indicates that as one variable increases, the other variable tends to decrease.
**Example: Highway Miles per Gallon and Price**
- **Negative Correlation:** As highway miles per gallon increases, price decreases.
- **Visualization:** Scatter plot with a steep negative slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/10f1f798-9cc4-4df2-a9c1-5a339f554a0b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466S66OP4FP%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T211357Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEE0aCXVzLXdlc3QtMiJHMEUCIAHWH7SvshQgCyJuvqZuLYVk8VNE%2BGzST7x2DZobiAzRAiEA5%2BswBiZf8hoTdicCqNk4oHjJDL1uH6BKMzI%2F%2F5R5b60q%2FwMIZhAAGgw2Mzc0MjMxODM4MDUiDJ1VwtOYGowdT1i80ircA9NYUnvTwO2O5gLWoJmn7Hvwva1gwZ9nDD%2BRffA%2BXYJENMWuQecrJtnkuEbFssUwacdF2vk4aww8I5nzCsIpTIKAL6gJrw7MulkndV05EqzckH3kE9tE5hC24xnzfAFbjHAH0hMBM0r%2F6ko%2BN7AP4NT51IxUsCkILp0IuMdICWK51Eh5MSqMnKulHu05QOZ%2BL%2BZ5NV%2Fv%2BYIUaUEfLyMMVtAbIH15GjV1PXOfi%2Brhd8JGJ%2BF4Yez8O1zXn40kKuSLHxsvz%2B8HtBrcXneDoK1xIuUDZf%2FVl6Spf9ryP1LIqNv3lEFCm4%2Fw8yBHvCB8sJC41Y3aE4GzmEzeCwlrculiOFXqacRIke7xxW2SusRS9v0zUBh4p6ClwUkW36nNUK5YEYYMjJZLtWgrtljflRSpqYfpv16n5oPof63C3RICQDfWZhd%2B4t%2F27tWX00Qm60bb0b5ZberIM5slz3Lapr8bfX0dir7IiY6yTLY%2F8ERFMMAsKD28J8uyMPpNA0uUruta3OJnT9bht0mpBffazlXDYT7TF3aJVHDYq1%2Bsu5FKjT48DqeUWB2bwMoB0GMs%2BAd1dTWYFpGrBxE9WZzzxveI1FsELXKucMSrYPyb%2BM%2BXh3ay3kb83ymaKZb9zXg7MO%2B3lL0GOqUBXr5fV4TJ8hItIJnNFs0Dv%2BW8SAObhSIsJ7zHnUxoq6orsm34qpzBa6nyBgOGa6%2FSVaQz7nD3xZiWT1Kyqy%2F6U6o0ItSV2QkWiIzuEHu914mZ4G9K%2BFqTa9pJRr%2B7soplk7FCHZ4rFOGhSERtHUaVb785JGKDGCQjlLtb0U5yXSlqI1DIJQNxmCrqdFIZ7dLe6BqTgeMUdFfnkr9txqcvIheE9MR4&X-Amz-Signature=927a184fe6045d2a6939079a4ab0ab42310557ed6dd94b7bf2e5e78907d17b75&X-Amz-SignedHeaders=host&x-id=GetObject)
**Explanation:** When highway miles per gallon increases, the price of the vehicle tends to decrease. This negative correlation suggests that cars with higher fuel efficiency (more miles per gallon) are generally priced lower in the market.
___
### Weak Correlation
Weak correlation indicates a lack of strong relationship between the variables.
**Example: RPM and Price**
- **Weak Correlation:** Low and high RPM values show varied prices, indicating no strong predictive relationship.
- **Visualization:** Scatter plot with no clear trend or slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9f914514-8914-4bf4-ac84-d9e3077f6eb1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RF7SJWCM%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T211357Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEE0aCXVzLXdlc3QtMiJHMEUCICozjRP5qzgmzu9x5OPXRJCnBWGEE59ynC%2FapYEIWSBfAiEAl9X72QEl5rsWSbNAo4s8Rk7%2FygQ1Z9vxYYWlrzcJeo0q%2FwMIZhAAGgw2Mzc0MjMxODM4MDUiDN4oCUF5STtrwyIn7SrcA3UFYOqRSTzDMlwn9C62MEl5OAaVaH%2FnZPkdCBrTMAmDx%2FY3M%2Bhr16y8L2KUowgMi82pEiGw%2B5KBtTpOeOBhF8i3UNopmFdMYDthC7A6ShAgcTynI%2FvVn2LAj205kYrbqa8axDiV8fjYVb%2BcIBY%2BASRYm0Qwd4QK0eYMAx%2Fe1Q1S47hVg%2Bf7xeHawQ5wZueo6dhEGVFm7gKWhOVKhG3S3Qb3114dJ15gTJe5gMLbq9H63ZdikhM68hiK3moy58PXIV%2F7x8sfeq3j67FRJmFqr8AUZEUp8amATzCS%2Baa6OEA%2FYC%2B%2BeNFwoqTFvkl1tJcMLvTWIXlcaB2QPWrDqjSyw%2FMY9kcPV4GUT%2BqvLBv8MaAJQ8Qskw7sH7wTMCqJlGzYaN0DbS6YYLROftp8cpkTgBtcYsIfCdqT%2F0lN1oPWVL5hyWjGtAhS75jRigF2VY%2Bh%2BXerX0aI%2FZ4K1MAsq6pCb2y20x6FVwQpjSNGV%2BBJARHObKKAxrtVDJIwF7JI9gA7UldzIiuqzlXdGZufecu2EDq%2FpXVmuvuoQJTl05suHbJ1UamUqNaCE0Q7pUD%2FqxsUAL%2BA515jUHDjO0L5hbTInIk28EsvfBUCgg08OUlMJbdUUfpuIW84ABoDBcx1MI64lL0GOqUBmuYB5M0vp9bIMX9p3Zvwds2FDD6eQh8K9Aqbn%2FOh5M%2FUPTiNna2TNk7HdWTHlGzjWjT26MdSyyOGvE2mQWDQMrRYc1Dn%2BfgR8fscsRADtBPKTL2XXKa3Peym7DQLQbJ4eVxnis%2FsUJ7g26bsPt0GJHxZLn%2FxF9snRJTBX6n5%2FmrQ3zk5PH5tMLjgzlFgmzQ0YuE3%2B69fbStsWK%2Be5DFBGxET81wj&X-Amz-Signature=1853d171d19a211ae7d9dd3baf89cf4ed96e9e159c6ce838c17009684c67aa7b&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f18086e5-5b04-4fbf-8309-8944ab20d213/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SHAANBOB%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T211357Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEE0aCXVzLXdlc3QtMiJHMEUCIBHtuIUd0YRDGtNBZnUtTbA9%2Fd5lSJTeTM5oL1G27%2BBlAiEA%2F0R9TJdpEa1DYgcYcdabHhEAOugaFkQhlDueorqoX74q%2FwMIZhAAGgw2Mzc0MjMxODM4MDUiDHhH4Ibfm%2BYOrEv2TSrcA%2FkpHua%2B5gcrUZIBT5j71T77gjFCjOrq%2F5Ej%2F38jVeaqT637An9DCgD5iKvMYD32lMrg0QuDqPvsFlrAiEk4y9yfIYNji774AKuJGHLkNzBD3OmrnQwZzqr4otgrf2RHSvcxO9u%2FprmfVaFmSY14PuOU1u%2FnIUek6GDb6kdq%2FBbiUq02O5nvQhooOGde1GSMOmMBqieNWmwhYl8hh3xPEU31Wkj82g4BQl22cmByMRuSXKnyLun8158fC62vxoPnMwJGpnxuqx%2BqFa5ostbRzlwcDnsVgYMNrnsyFTGbgmdfEpSHCzsfBlefs3mm7Kh7P%2BzSJrbdoeOmgKlyxFmXJnLr4GAEW0U71gu1GbLiaA9%2BfDVE9A2IZwe4Bem2NniyIbVGbUZ9Fu8XBYikUcvJHaCDPjAAp4iKFSsN7nY77j6KhK7M7bTD21G%2FmHCL9QPoY%2BGWn4iP3nkfFjbsa5%2Bper6gaqPlprvEYFJU18JlmT6fo3N7cbBOSjo10TPMIY3gEv5bPqJirrKFARZCh0Tj51PB5fMGCnWKwTf4U%2BltZUUIP4pRPFmGcDftzHYSC0qXx3ff44oQCEw5DyUWnsR2uFor52NnfI6nkvvVv7krI5ElWJ7uqh2%2FDTn7sn1YMI24lL0GOqUBDSKiAXHeXBI5jU65ob19OHFvFzSJsJ46phERWILfM6T8Ghm99XuMQhDTz%2FwMIGLnJSegHfTv3SqWOpuTE8rtmPKRxMzndZp3we5%2F1aCB%2Bfogs64KpsTIwP9cZgeSnK06u6ZoN1AQnLXLCOmo%2BaVl4Ztz7%2B7ci%2BUNlSW%2BRUhOVMjfr5hULSWrwZje8fdZYMiwYoAC9tTOyg5LUSr%2FLF%2BBT6ol4Bvu&X-Amz-Signature=2ec5551f12b451459ef9ec28cae9076b5048f7ca1335fc8966665cbcf7233edb&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Correlation Plot
Heatmap visualizes correlations among variables. Color scheme indicates Pearson correlation coefficients. Dark red diagonal line shows perfect correlation (value of 1) between variables and themselves.
This heatmap offers overview of variable relationships and their link with price.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cd3b341e-cc1a-45f7-8aec-cdc00436d270/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SHAANBOB%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T211357Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEE0aCXVzLXdlc3QtMiJHMEUCIBHtuIUd0YRDGtNBZnUtTbA9%2Fd5lSJTeTM5oL1G27%2BBlAiEA%2F0R9TJdpEa1DYgcYcdabHhEAOugaFkQhlDueorqoX74q%2FwMIZhAAGgw2Mzc0MjMxODM4MDUiDHhH4Ibfm%2BYOrEv2TSrcA%2FkpHua%2B5gcrUZIBT5j71T77gjFCjOrq%2F5Ej%2F38jVeaqT637An9DCgD5iKvMYD32lMrg0QuDqPvsFlrAiEk4y9yfIYNji774AKuJGHLkNzBD3OmrnQwZzqr4otgrf2RHSvcxO9u%2FprmfVaFmSY14PuOU1u%2FnIUek6GDb6kdq%2FBbiUq02O5nvQhooOGde1GSMOmMBqieNWmwhYl8hh3xPEU31Wkj82g4BQl22cmByMRuSXKnyLun8158fC62vxoPnMwJGpnxuqx%2BqFa5ostbRzlwcDnsVgYMNrnsyFTGbgmdfEpSHCzsfBlefs3mm7Kh7P%2BzSJrbdoeOmgKlyxFmXJnLr4GAEW0U71gu1GbLiaA9%2BfDVE9A2IZwe4Bem2NniyIbVGbUZ9Fu8XBYikUcvJHaCDPjAAp4iKFSsN7nY77j6KhK7M7bTD21G%2FmHCL9QPoY%2BGWn4iP3nkfFjbsa5%2Bper6gaqPlprvEYFJU18JlmT6fo3N7cbBOSjo10TPMIY3gEv5bPqJirrKFARZCh0Tj51PB5fMGCnWKwTf4U%2BltZUUIP4pRPFmGcDftzHYSC0qXx3ff44oQCEw5DyUWnsR2uFor52NnfI6nkvvVv7krI5ElWJ7uqh2%2FDTn7sn1YMI24lL0GOqUBDSKiAXHeXBI5jU65ob19OHFvFzSJsJ46phERWILfM6T8Ghm99XuMQhDTz%2FwMIGLnJSegHfTv3SqWOpuTE8rtmPKRxMzndZp3we5%2F1aCB%2Bfogs64KpsTIwP9cZgeSnK06u6ZoN1AQnLXLCOmo%2BaVl4Ztz7%2B7ci%2BUNlSW%2BRUhOVMjfr5hULSWrwZje8fdZYMiwYoAC9tTOyg5LUSr%2FLF%2BBT6ol4Bvu&X-Amz-Signature=1732b694e3f74321e4ee6ee8a76508ab428b4d95f1e3e3671a70e18a22e87934&X-Amz-SignedHeaders=host&x-id=GetObject)

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
