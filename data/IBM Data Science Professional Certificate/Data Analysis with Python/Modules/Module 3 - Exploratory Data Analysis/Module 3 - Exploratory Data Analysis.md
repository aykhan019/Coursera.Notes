

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7e6d594d-952e-44b6-97ea-31225882aea6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UC3YYIFY%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T161750Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIB1vm2xr9P77rQdd1j73sRPJSkaweSRSzoyQznfeS3FHAiEA71%2FP93mJFxnvzeZUN%2B22nnxlnJ7GDqiWpdhZEAZ1eEkqiAQIwf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDIhhK%2BxTZX4%2BBS8xHCrcA5fS0d8L6RQ720AoPG2otYT3hZz6E2q6qm9NAGIUPKoM0X2IHQMe3vogxI8CFzNW9vXOoTgtwSEGSW7%2BtKHXOYNmxJSV8G6KhMfQklV6JZE5G71mdKelB3Gbfj6gdriPtO1YBd0ZkXZA1svsEg%2FgmHvE54b7hme8ZtYXKqY3AzTEuWpy8KVMFcgKcPSYh5UMPgNCeondKpLZT5x9oX3EnO742pgD%2FlREiMGD2DyAFbIUcidezXMPBK07FtAwY7zqM%2FFFUoYi5K6nSj8ZvAjuqCGnE26Pq%2Fn2fPtaFBx%2BPiC%2Bi1kEFN3RI0%2BlSVYChInZBkF4lxHH4403leU55qocMz41rQbTJyRveA4u3WQjLiYXITyiSQCP9ZFKQj%2Bp9klNI048wBis8kodJWJpe6X%2BHKiMoLOkifbVuNnYD5%2B%2F%2FAHkB74hzU%2F2w7Eqyg%2Bs6MjrkQNcuzwhp8iOIIKkqIDbhc7xP%2BtRA6E3%2F8mNIQvNjWstCPTc%2BgxgiDh99SRVQgM7WlGpJI06ypcNiml%2FpvuxS5frDhEGbEzg9oOFH8%2FQVzOpXzsR6WJwfUZdCy7KnUpfWGozXNxIlWGxbjN0o7pIerulJtc9grlYSWkUOYgmYtYDmLUCHSYHgqWtklQwMOXq87wGOqUB0rVbwF%2FoyqrVJyu%2B6xfaiC6AdAGyPT71PWfyaelt7Jr%2FaKP0oBwp0Uy%2Bb%2FiF563UuxGVXcOG9VMQcuOAwcFUSPeOYKOduA%2B8nHQyJ%2FbZFN0I%2BCvkVthUevpvfykEVLsg4ZwgrZv3099qmgj9Li9LsXHVf0q1lHXYx9gOOwaLk5RVORDb7HUQX%2FPDL4I45yVEnCg2F5xr34G6W2Xq5divV9TPM0wW&X-Amz-Signature=5d433cb9ff9a436e6bf11004128254f4c53a72ad825ff542deaf25057900727f&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cbfaed9e-b398-4902-8936-dea058b21def/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UC3YYIFY%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T161750Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIB1vm2xr9P77rQdd1j73sRPJSkaweSRSzoyQznfeS3FHAiEA71%2FP93mJFxnvzeZUN%2B22nnxlnJ7GDqiWpdhZEAZ1eEkqiAQIwf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDIhhK%2BxTZX4%2BBS8xHCrcA5fS0d8L6RQ720AoPG2otYT3hZz6E2q6qm9NAGIUPKoM0X2IHQMe3vogxI8CFzNW9vXOoTgtwSEGSW7%2BtKHXOYNmxJSV8G6KhMfQklV6JZE5G71mdKelB3Gbfj6gdriPtO1YBd0ZkXZA1svsEg%2FgmHvE54b7hme8ZtYXKqY3AzTEuWpy8KVMFcgKcPSYh5UMPgNCeondKpLZT5x9oX3EnO742pgD%2FlREiMGD2DyAFbIUcidezXMPBK07FtAwY7zqM%2FFFUoYi5K6nSj8ZvAjuqCGnE26Pq%2Fn2fPtaFBx%2BPiC%2Bi1kEFN3RI0%2BlSVYChInZBkF4lxHH4403leU55qocMz41rQbTJyRveA4u3WQjLiYXITyiSQCP9ZFKQj%2Bp9klNI048wBis8kodJWJpe6X%2BHKiMoLOkifbVuNnYD5%2B%2F%2FAHkB74hzU%2F2w7Eqyg%2Bs6MjrkQNcuzwhp8iOIIKkqIDbhc7xP%2BtRA6E3%2F8mNIQvNjWstCPTc%2BgxgiDh99SRVQgM7WlGpJI06ypcNiml%2FpvuxS5frDhEGbEzg9oOFH8%2FQVzOpXzsR6WJwfUZdCy7KnUpfWGozXNxIlWGxbjN0o7pIerulJtc9grlYSWkUOYgmYtYDmLUCHSYHgqWtklQwMOXq87wGOqUB0rVbwF%2FoyqrVJyu%2B6xfaiC6AdAGyPT71PWfyaelt7Jr%2FaKP0oBwp0Uy%2Bb%2FiF563UuxGVXcOG9VMQcuOAwcFUSPeOYKOduA%2B8nHQyJ%2FbZFN0I%2BCvkVthUevpvfykEVLsg4ZwgrZv3099qmgj9Li9LsXHVf0q1lHXYx9gOOwaLk5RVORDb7HUQX%2FPDL4I45yVEnCg2F5xr34G6W2Xq5divV9TPM0wW&X-Amz-Signature=c83621e50e5607f132398803a1a7b66cc777ac2c56fb4369bfa1ca2593efe13b&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/91181646-b1e0-4433-9711-6259a96a9247/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UC3YYIFY%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T161750Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIB1vm2xr9P77rQdd1j73sRPJSkaweSRSzoyQznfeS3FHAiEA71%2FP93mJFxnvzeZUN%2B22nnxlnJ7GDqiWpdhZEAZ1eEkqiAQIwf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDIhhK%2BxTZX4%2BBS8xHCrcA5fS0d8L6RQ720AoPG2otYT3hZz6E2q6qm9NAGIUPKoM0X2IHQMe3vogxI8CFzNW9vXOoTgtwSEGSW7%2BtKHXOYNmxJSV8G6KhMfQklV6JZE5G71mdKelB3Gbfj6gdriPtO1YBd0ZkXZA1svsEg%2FgmHvE54b7hme8ZtYXKqY3AzTEuWpy8KVMFcgKcPSYh5UMPgNCeondKpLZT5x9oX3EnO742pgD%2FlREiMGD2DyAFbIUcidezXMPBK07FtAwY7zqM%2FFFUoYi5K6nSj8ZvAjuqCGnE26Pq%2Fn2fPtaFBx%2BPiC%2Bi1kEFN3RI0%2BlSVYChInZBkF4lxHH4403leU55qocMz41rQbTJyRveA4u3WQjLiYXITyiSQCP9ZFKQj%2Bp9klNI048wBis8kodJWJpe6X%2BHKiMoLOkifbVuNnYD5%2B%2F%2FAHkB74hzU%2F2w7Eqyg%2Bs6MjrkQNcuzwhp8iOIIKkqIDbhc7xP%2BtRA6E3%2F8mNIQvNjWstCPTc%2BgxgiDh99SRVQgM7WlGpJI06ypcNiml%2FpvuxS5frDhEGbEzg9oOFH8%2FQVzOpXzsR6WJwfUZdCy7KnUpfWGozXNxIlWGxbjN0o7pIerulJtc9grlYSWkUOYgmYtYDmLUCHSYHgqWtklQwMOXq87wGOqUB0rVbwF%2FoyqrVJyu%2B6xfaiC6AdAGyPT71PWfyaelt7Jr%2FaKP0oBwp0Uy%2Bb%2FiF563UuxGVXcOG9VMQcuOAwcFUSPeOYKOduA%2B8nHQyJ%2FbZFN0I%2BCvkVthUevpvfykEVLsg4ZwgrZv3099qmgj9Li9LsXHVf0q1lHXYx9gOOwaLk5RVORDb7HUQX%2FPDL4I45yVEnCg2F5xr34G6W2Xq5divV9TPM0wW&X-Amz-Signature=4ad62218983599aba08779bf8836ebfc1e9fb721b6a1b13a06a2bed83040c69f&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/09aba1c0-0d55-41dd-852a-a04c5b8a3fac/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46627X4SMRC%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T161751Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQC8YHexoNugZ9U4F7d1N18tza5EltvZXaZIdJ%2FNrEAMRwIgdIYbWAVAP3UsBon7qjyPFN4Cq3oAkiGwfLoTbiVL2DYqiAQIwf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNYRCPXApo4PWW%2FbDircA3BCHYQ07loJ%2FG2BwNJxiDsweAyC8JLMrAOlGXwNt8ojfbwz1ce2SmQG4NdgkiSZZm0P0exRAdQYRkFOdGiSkW2FCHUhSUrJzjoO0Dh5epGSQioQY2Few8rTYYlot70EEhOYyvCX11IIruTEind6wVG9dZdJ%2FjjsB6pMyYUclR%2BjSyDkrd8DBCZIHEDCHzzNl1TYCi0hZ%2B8Rkndd8xDV%2Bu7cQBQuNn%2F0S4V34lu%2Fo8teOOWcX%2BZUGPVA%2FsZ8vHr%2FE63oa3bdJbE1H%2BoEYHSh%2BqUHPxvzDoc9bA25Btpd8NQlOGbf310kxh65w5cJ%2Fw97MptHIPn3iJ1crAcab882%2B%2BibTLoDtCpA4EJ4z6OWnRbOhhOb3AjvrKew%2B2ob1zgT65hyyszldyLcirlGOdhqL0d9XSHlSl%2FMrnpoE3FWcKa%2FwBJCtSkvD8jCKuJujW8JteuR97IN1Q%2BLJj0DIP0WW3gLl1vfE1cNPpw9LeAw2Y%2ByTJyBTd4HGcp0aPANkv5PBh8LuFImk9jnba3xjXs48KMCCdfXMmQNftCSKWwNq%2FzzbxgIky3y3DvnbG%2BWtTH1cc4ObEKnQTEXu0f%2Bv%2BgF5t6ST2ym3hlpY2ZTsK14%2FFx%2BEWWybSI4097GLNsIMPjq87wGOqUBtMuBQdKL2J3ALHV1U598J0HZBQ8QLwDV3g5aFO5%2FiIfBpeYYZtzXGAnxneaC5IxQ8yuYojxdsNgNlbhOwHiPpHy2WURWH%2FVPgqDW2M7rkJ2wapwWMpi%2F%2Flt3RAfNIjHlVIsAdIvs5RVOjioCHixBG3nzy4pMfxntkp6vaQr2KTFJIWShUB%2Bte0E9dUZtpoOPrddgHlbos4ZuyTeXjfzS%2FHkFmeGM&X-Amz-Signature=cfba0f057a4f7df677985c30df651bdcc1064d704da98050d9ff349bb79b9afd&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 2. Scatter Plot
Scatter plots present the relationship between two variables in a dataset. It represents data points on a two-dimensional plane. The independent variable or attribute is plotted on the X-axis, while the dependent variable is plotted on the Y-axis.
**Syntax:**
```python
plt.scatter(x, y)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23708af9-659f-4f23-b626-1a4292d7842c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46627X4SMRC%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T161751Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQC8YHexoNugZ9U4F7d1N18tza5EltvZXaZIdJ%2FNrEAMRwIgdIYbWAVAP3UsBon7qjyPFN4Cq3oAkiGwfLoTbiVL2DYqiAQIwf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNYRCPXApo4PWW%2FbDircA3BCHYQ07loJ%2FG2BwNJxiDsweAyC8JLMrAOlGXwNt8ojfbwz1ce2SmQG4NdgkiSZZm0P0exRAdQYRkFOdGiSkW2FCHUhSUrJzjoO0Dh5epGSQioQY2Few8rTYYlot70EEhOYyvCX11IIruTEind6wVG9dZdJ%2FjjsB6pMyYUclR%2BjSyDkrd8DBCZIHEDCHzzNl1TYCi0hZ%2B8Rkndd8xDV%2Bu7cQBQuNn%2F0S4V34lu%2Fo8teOOWcX%2BZUGPVA%2FsZ8vHr%2FE63oa3bdJbE1H%2BoEYHSh%2BqUHPxvzDoc9bA25Btpd8NQlOGbf310kxh65w5cJ%2Fw97MptHIPn3iJ1crAcab882%2B%2BibTLoDtCpA4EJ4z6OWnRbOhhOb3AjvrKew%2B2ob1zgT65hyyszldyLcirlGOdhqL0d9XSHlSl%2FMrnpoE3FWcKa%2FwBJCtSkvD8jCKuJujW8JteuR97IN1Q%2BLJj0DIP0WW3gLl1vfE1cNPpw9LeAw2Y%2ByTJyBTd4HGcp0aPANkv5PBh8LuFImk9jnba3xjXs48KMCCdfXMmQNftCSKWwNq%2FzzbxgIky3y3DvnbG%2BWtTH1cc4ObEKnQTEXu0f%2Bv%2BgF5t6ST2ym3hlpY2ZTsK14%2FFx%2BEWWybSI4097GLNsIMPjq87wGOqUBtMuBQdKL2J3ALHV1U598J0HZBQ8QLwDV3g5aFO5%2FiIfBpeYYZtzXGAnxneaC5IxQ8yuYojxdsNgNlbhOwHiPpHy2WURWH%2FVPgqDW2M7rkJ2wapwWMpi%2F%2Flt3RAfNIjHlVIsAdIvs5RVOjioCHixBG3nzy4pMfxntkp6vaQr2KTFJIWShUB%2Bte0E9dUZtpoOPrddgHlbos4ZuyTeXjfzS%2FHkFmeGM&X-Amz-Signature=2dabaf1869ef6a1ba45d00afb22a8387857372459b1f981063179063a0b75b62&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 3. Histogram
A histogram is an important visual representation of data in categorical form. To view the data in a "Binned" form, use the histogram plot with a number of bins required or with the data points that mark the bin edges. The x-axis represents the data bins, and the y-axis represents the number of elements in each bin.
**Syntax:**
```python
plt.hist(x, bins)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/24e4424a-df87-40a1-b63b-195cbdc2e0ab/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46627X4SMRC%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T161751Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQC8YHexoNugZ9U4F7d1N18tza5EltvZXaZIdJ%2FNrEAMRwIgdIYbWAVAP3UsBon7qjyPFN4Cq3oAkiGwfLoTbiVL2DYqiAQIwf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNYRCPXApo4PWW%2FbDircA3BCHYQ07loJ%2FG2BwNJxiDsweAyC8JLMrAOlGXwNt8ojfbwz1ce2SmQG4NdgkiSZZm0P0exRAdQYRkFOdGiSkW2FCHUhSUrJzjoO0Dh5epGSQioQY2Few8rTYYlot70EEhOYyvCX11IIruTEind6wVG9dZdJ%2FjjsB6pMyYUclR%2BjSyDkrd8DBCZIHEDCHzzNl1TYCi0hZ%2B8Rkndd8xDV%2Bu7cQBQuNn%2F0S4V34lu%2Fo8teOOWcX%2BZUGPVA%2FsZ8vHr%2FE63oa3bdJbE1H%2BoEYHSh%2BqUHPxvzDoc9bA25Btpd8NQlOGbf310kxh65w5cJ%2Fw97MptHIPn3iJ1crAcab882%2B%2BibTLoDtCpA4EJ4z6OWnRbOhhOb3AjvrKew%2B2ob1zgT65hyyszldyLcirlGOdhqL0d9XSHlSl%2FMrnpoE3FWcKa%2FwBJCtSkvD8jCKuJujW8JteuR97IN1Q%2BLJj0DIP0WW3gLl1vfE1cNPpw9LeAw2Y%2ByTJyBTd4HGcp0aPANkv5PBh8LuFImk9jnba3xjXs48KMCCdfXMmQNftCSKWwNq%2FzzbxgIky3y3DvnbG%2BWtTH1cc4ObEKnQTEXu0f%2Bv%2BgF5t6ST2ym3hlpY2ZTsK14%2FFx%2BEWWybSI4097GLNsIMPjq87wGOqUBtMuBQdKL2J3ALHV1U598J0HZBQ8QLwDV3g5aFO5%2FiIfBpeYYZtzXGAnxneaC5IxQ8yuYojxdsNgNlbhOwHiPpHy2WURWH%2FVPgqDW2M7rkJ2wapwWMpi%2F%2Flt3RAfNIjHlVIsAdIvs5RVOjioCHixBG3nzy4pMfxntkp6vaQr2KTFJIWShUB%2Bte0E9dUZtpoOPrddgHlbos4ZuyTeXjfzS%2FHkFmeGM&X-Amz-Signature=24c6343fd7ead781439654470a0b1103a23619da23a9696fe96fb2ae4915876a&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ab5a6dfe-51f5-43ee-bcb3-33dae4a1c7ad/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46627X4SMRC%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T161751Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQC8YHexoNugZ9U4F7d1N18tza5EltvZXaZIdJ%2FNrEAMRwIgdIYbWAVAP3UsBon7qjyPFN4Cq3oAkiGwfLoTbiVL2DYqiAQIwf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNYRCPXApo4PWW%2FbDircA3BCHYQ07loJ%2FG2BwNJxiDsweAyC8JLMrAOlGXwNt8ojfbwz1ce2SmQG4NdgkiSZZm0P0exRAdQYRkFOdGiSkW2FCHUhSUrJzjoO0Dh5epGSQioQY2Few8rTYYlot70EEhOYyvCX11IIruTEind6wVG9dZdJ%2FjjsB6pMyYUclR%2BjSyDkrd8DBCZIHEDCHzzNl1TYCi0hZ%2B8Rkndd8xDV%2Bu7cQBQuNn%2F0S4V34lu%2Fo8teOOWcX%2BZUGPVA%2FsZ8vHr%2FE63oa3bdJbE1H%2BoEYHSh%2BqUHPxvzDoc9bA25Btpd8NQlOGbf310kxh65w5cJ%2Fw97MptHIPn3iJ1crAcab882%2B%2BibTLoDtCpA4EJ4z6OWnRbOhhOb3AjvrKew%2B2ob1zgT65hyyszldyLcirlGOdhqL0d9XSHlSl%2FMrnpoE3FWcKa%2FwBJCtSkvD8jCKuJujW8JteuR97IN1Q%2BLJj0DIP0WW3gLl1vfE1cNPpw9LeAw2Y%2ByTJyBTd4HGcp0aPANkv5PBh8LuFImk9jnba3xjXs48KMCCdfXMmQNftCSKWwNq%2FzzbxgIky3y3DvnbG%2BWtTH1cc4ObEKnQTEXu0f%2Bv%2BgF5t6ST2ym3hlpY2ZTsK14%2FFx%2BEWWybSI4097GLNsIMPjq87wGOqUBtMuBQdKL2J3ALHV1U598J0HZBQ8QLwDV3g5aFO5%2FiIfBpeYYZtzXGAnxneaC5IxQ8yuYojxdsNgNlbhOwHiPpHy2WURWH%2FVPgqDW2M7rkJ2wapwWMpi%2F%2Flt3RAfNIjHlVIsAdIvs5RVOjioCHixBG3nzy4pMfxntkp6vaQr2KTFJIWShUB%2Bte0E9dUZtpoOPrddgHlbos4ZuyTeXjfzS%2FHkFmeGM&X-Amz-Signature=66286926904d8d509888a07f746d80434740103cef60c1644c0576500e1acdaf&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8f1b1d60-cf1b-42b3-9faa-f634c89c3f84/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46627X4SMRC%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T161751Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQC8YHexoNugZ9U4F7d1N18tza5EltvZXaZIdJ%2FNrEAMRwIgdIYbWAVAP3UsBon7qjyPFN4Cq3oAkiGwfLoTbiVL2DYqiAQIwf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNYRCPXApo4PWW%2FbDircA3BCHYQ07loJ%2FG2BwNJxiDsweAyC8JLMrAOlGXwNt8ojfbwz1ce2SmQG4NdgkiSZZm0P0exRAdQYRkFOdGiSkW2FCHUhSUrJzjoO0Dh5epGSQioQY2Few8rTYYlot70EEhOYyvCX11IIruTEind6wVG9dZdJ%2FjjsB6pMyYUclR%2BjSyDkrd8DBCZIHEDCHzzNl1TYCi0hZ%2B8Rkndd8xDV%2Bu7cQBQuNn%2F0S4V34lu%2Fo8teOOWcX%2BZUGPVA%2FsZ8vHr%2FE63oa3bdJbE1H%2BoEYHSh%2BqUHPxvzDoc9bA25Btpd8NQlOGbf310kxh65w5cJ%2Fw97MptHIPn3iJ1crAcab882%2B%2BibTLoDtCpA4EJ4z6OWnRbOhhOb3AjvrKew%2B2ob1zgT65hyyszldyLcirlGOdhqL0d9XSHlSl%2FMrnpoE3FWcKa%2FwBJCtSkvD8jCKuJujW8JteuR97IN1Q%2BLJj0DIP0WW3gLl1vfE1cNPpw9LeAw2Y%2ByTJyBTd4HGcp0aPANkv5PBh8LuFImk9jnba3xjXs48KMCCdfXMmQNftCSKWwNq%2FzzbxgIky3y3DvnbG%2BWtTH1cc4ObEKnQTEXu0f%2Bv%2BgF5t6ST2ym3hlpY2ZTsK14%2FFx%2BEWWybSI4097GLNsIMPjq87wGOqUBtMuBQdKL2J3ALHV1U598J0HZBQ8QLwDV3g5aFO5%2FiIfBpeYYZtzXGAnxneaC5IxQ8yuYojxdsNgNlbhOwHiPpHy2WURWH%2FVPgqDW2M7rkJ2wapwWMpi%2F%2Flt3RAfNIjHlVIsAdIvs5RVOjioCHixBG3nzy4pMfxntkp6vaQr2KTFJIWShUB%2Bte0E9dUZtpoOPrddgHlbos4ZuyTeXjfzS%2FHkFmeGM&X-Amz-Signature=a16b8b243a11e1ee0cd887787f7321dce2d52270b5d1b5b0c026e0cc8667f606&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/13ad0497-05fe-4eaa-984e-707b33e14761/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46627X4SMRC%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T161751Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQC8YHexoNugZ9U4F7d1N18tza5EltvZXaZIdJ%2FNrEAMRwIgdIYbWAVAP3UsBon7qjyPFN4Cq3oAkiGwfLoTbiVL2DYqiAQIwf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNYRCPXApo4PWW%2FbDircA3BCHYQ07loJ%2FG2BwNJxiDsweAyC8JLMrAOlGXwNt8ojfbwz1ce2SmQG4NdgkiSZZm0P0exRAdQYRkFOdGiSkW2FCHUhSUrJzjoO0Dh5epGSQioQY2Few8rTYYlot70EEhOYyvCX11IIruTEind6wVG9dZdJ%2FjjsB6pMyYUclR%2BjSyDkrd8DBCZIHEDCHzzNl1TYCi0hZ%2B8Rkndd8xDV%2Bu7cQBQuNn%2F0S4V34lu%2Fo8teOOWcX%2BZUGPVA%2FsZ8vHr%2FE63oa3bdJbE1H%2BoEYHSh%2BqUHPxvzDoc9bA25Btpd8NQlOGbf310kxh65w5cJ%2Fw97MptHIPn3iJ1crAcab882%2B%2BibTLoDtCpA4EJ4z6OWnRbOhhOb3AjvrKew%2B2ob1zgT65hyyszldyLcirlGOdhqL0d9XSHlSl%2FMrnpoE3FWcKa%2FwBJCtSkvD8jCKuJujW8JteuR97IN1Q%2BLJj0DIP0WW3gLl1vfE1cNPpw9LeAw2Y%2ByTJyBTd4HGcp0aPANkv5PBh8LuFImk9jnba3xjXs48KMCCdfXMmQNftCSKWwNq%2FzzbxgIky3y3DvnbG%2BWtTH1cc4ObEKnQTEXu0f%2Bv%2BgF5t6ST2ym3hlpY2ZTsK14%2FFx%2BEWWybSI4097GLNsIMPjq87wGOqUBtMuBQdKL2J3ALHV1U598J0HZBQ8QLwDV3g5aFO5%2FiIfBpeYYZtzXGAnxneaC5IxQ8yuYojxdsNgNlbhOwHiPpHy2WURWH%2FVPgqDW2M7rkJ2wapwWMpi%2F%2Flt3RAfNIjHlVIsAdIvs5RVOjioCHixBG3nzy4pMfxntkp6vaQr2KTFJIWShUB%2Bte0E9dUZtpoOPrddgHlbos4ZuyTeXjfzS%2FHkFmeGM&X-Amz-Signature=cfe1bcb9dda3a9be02c9d7857a21d31c860389ed0d644e27697f8e79adb67a4c&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 2. Box and Whisker Plot
A box plot shows the distribution of quantitative data in a way that facilitates comparisons between variables or across levels of a categorical variable. The box shows the quartiles of the dataset while the whiskers extend to show the rest of the distribution, except for points that are determined to be "outliers".
**Syntax:**
```python
sns.boxplot(x='header_1', y='header_2', data=df)
```
**Example Output:**


![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d207ae92-0a7c-4e2f-aa65-0ee5a2c33bf7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RYZVVVUI%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T161755Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCP53T7B5mnPb1WFvFJZjbNyI0aBoq%2FMxZgycYbAqXFRAIgJD%2BW1LkU9n9ICL83ZeNGfoEJ2Hjamp5MOmecxsG%2BZdgqiAQIwf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHmoWq8%2FdXP8QPHidSrcA3x1IsRemcOBLZMIIRRuwyyW2csk0SyRQ15VFGi2U0KRNdeVWpgcGfyUG8XvVzcHA%2FQan02hQaRx34ty2bM5TaXy5MnhmOUgiMm9QKr1llurkkaNK4iIfTRkJgHpboC0A%2F3hf6JjKuu55qC%2BHCC8irCttFg9eTLlftK%2BAPWmYoc6zhEZWSI6QLftRYxrucPmthR5ONYPXx7mzsKfXw53dkxpO5DDnOXbgLbQikXWGRhlUb8m%2BOikHDg0nwZkD6h5%2Bj2gWmIdNygaRgVsr89T0E9kTty14ICAitYxVXQR76AIIXyeLW7kKzEWgtfQgxg%2FpzojWe9AHZNKHMDAZKDa%2Bjtn3UXhFMK9T9Byf9yBe9kNo1vrELRG2uYMoseXY7hqlBlFAlhboIStMRrmebYxpbCYDMro9TorhcQwz%2F8mwHFpMSoRmeXRRKBjgRrZvC1qu2clTxn%2FUAxL4em7jYiFH%2BrxKYO3DtYoXmlJsjFtc33kwHDYhnt7Gi6YJipSdvEwDEweIrlYON2WVcT%2BYIbmjjFbN0SljY9d67hajeCtCr5K11bfPZNegsZ9R4AhFbnpCYtCN9SyH9gJU46xD3AsRgu3Qw4QHrGdF%2F7f8EnSBZfdCnbpZ8Mp9GHI0GWlMOXq87wGOqUBbf%2FdIJfl%2Fu5027dWdYB4kvOavWQ%2B8tlxCSPovrh3TsalDAs4d%2BDsDCwSVhPuloLa9Dvnakv%2FuoeN4FKJmaOGA6fZ1atuyKaNpNM3nGVjcJiqZhtXKhmxu%2FHFNxqnWD5D%2Bxp%2FhhKN4irWlc%2BckuehaKsGzD%2B6%2F2ORH%2BrFstrbVUhcfrLyld4Ux2huy%2FkgMt7HJ3dmBFyR7CjvIbBfP2YqKT1nsobZ&X-Amz-Signature=4bf06289dfca6467c228d14762a43fabad30efaa696ea1952438a6e86460c2b5&X-Amz-SignedHeaders=host&x-id=GetObject)

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0e516edc-7551-4792-ab18-0494db3c4c0c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664YNIGE57%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T161756Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFMau9MpLWVyDAV73gHScUW%2BTtcvEf6aYTox47g6uzisAiAhfeOjbf1ZxfN1OyL83IkvNrfMhH7ysYYOwziMX4gXayqIBAjB%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM5%2Ba9QOXLKUntC0SZKtwD70GTPZl5ppL2H4M4CNlH6i%2BK5N1C2kh0qOQk7zf%2BOi9P4lChO99BZxUfevO1xvTVyp9W%2FOTuWc9lAj2rMvX0n%2FSv11tF8ThLdjczpizPKa1%2FqFsVd93wCOjTEERgXrg8zkFvTOuk7BlhE%2Bv9TQpL%2FColeemqcb14bN2I2f5%2BKl3KDXki03SjkuwpYwwFaKlHXrX5KiO%2FE%2FU4jqO8CJWK9e1ZHJrP%2BleSni%2B2Rndx4Ksbx%2FQHoWw5XoEX95ne3I2Km9blDFyuvpuSs6oZh3jxU3s8F%2BI01Vt8Z%2F5VbUM8%2F2zXNh67MS9TzD0KIvI3Gr27812yPxxzChcZ4nU%2FLM5f8VLGG7ecjm1FNXJCrlJ6EAeMHRp6fQZeZ5FCzz1WJt3XX0RdOKidAeL6iBEstDdxuTUmX2fqr2Xa46YXzr5y4sp83KDA%2FsabVza2QPXzBYq5emWFksUDT2Twq%2F%2Bw20vbIAWx1Mlesq%2Fwh6H8l%2FMWMsKuef18xGplkifnz37zRFtPCN37PSXzIMi96R4U6FOEFTjKHP8CU3ao301G5jxHMw6b8l7L6MPSsyUwPyba2CGUg%2F%2FHZAh67EFXCYfiZ6VeC7gd0wA1PxQkJ5NUaPTszQG71Fsc3GNU%2BAn24E8wjuvzvAY6pgEKvX4iv0VRvXMEqiDxvQppDUIi2cmP9XuHAwzolRxwntIlyOxoA1mEIKcjolk5Tu%2FGOQzn7O4UkFoDFveCW0KTs7H9FZfKhtgPBw4cL6EhP3QlZrzaLa8uJu30HBUCBaw%2BByAzRWewnmszn8dEPUG30t4624S5xHzH%2Bo5JWnBiPsY4a0rCOXionqU78N%2FYM%2FJ0X1QJpWBdRJ8cQzAZfNlNwlneEcdO&X-Amz-Signature=cb30760d820a2987b61d186bffa0e433f8e09c96ddca985c20c8e14e71bf060f&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23a79b9d-2356-49a9-8fd9-65c6b0ab2cc5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46627X4SMRC%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T161751Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQC8YHexoNugZ9U4F7d1N18tza5EltvZXaZIdJ%2FNrEAMRwIgdIYbWAVAP3UsBon7qjyPFN4Cq3oAkiGwfLoTbiVL2DYqiAQIwf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNYRCPXApo4PWW%2FbDircA3BCHYQ07loJ%2FG2BwNJxiDsweAyC8JLMrAOlGXwNt8ojfbwz1ce2SmQG4NdgkiSZZm0P0exRAdQYRkFOdGiSkW2FCHUhSUrJzjoO0Dh5epGSQioQY2Few8rTYYlot70EEhOYyvCX11IIruTEind6wVG9dZdJ%2FjjsB6pMyYUclR%2BjSyDkrd8DBCZIHEDCHzzNl1TYCi0hZ%2B8Rkndd8xDV%2Bu7cQBQuNn%2F0S4V34lu%2Fo8teOOWcX%2BZUGPVA%2FsZ8vHr%2FE63oa3bdJbE1H%2BoEYHSh%2BqUHPxvzDoc9bA25Btpd8NQlOGbf310kxh65w5cJ%2Fw97MptHIPn3iJ1crAcab882%2B%2BibTLoDtCpA4EJ4z6OWnRbOhhOb3AjvrKew%2B2ob1zgT65hyyszldyLcirlGOdhqL0d9XSHlSl%2FMrnpoE3FWcKa%2FwBJCtSkvD8jCKuJujW8JteuR97IN1Q%2BLJj0DIP0WW3gLl1vfE1cNPpw9LeAw2Y%2ByTJyBTd4HGcp0aPANkv5PBh8LuFImk9jnba3xjXs48KMCCdfXMmQNftCSKWwNq%2FzzbxgIky3y3DvnbG%2BWtTH1cc4ObEKnQTEXu0f%2Bv%2BgF5t6ST2ym3hlpY2ZTsK14%2FFx%2BEWWybSI4097GLNsIMPjq87wGOqUBtMuBQdKL2J3ALHV1U598J0HZBQ8QLwDV3g5aFO5%2FiIfBpeYYZtzXGAnxneaC5IxQ8yuYojxdsNgNlbhOwHiPpHy2WURWH%2FVPgqDW2M7rkJ2wapwWMpi%2F%2Flt3RAfNIjHlVIsAdIvs5RVOjioCHixBG3nzy4pMfxntkp6vaQr2KTFJIWShUB%2Bte0E9dUZtpoOPrddgHlbos4ZuyTeXjfzS%2FHkFmeGM&X-Amz-Signature=7dee96e74983e4d2224340a11b53d67f6ac45838abce537af60126d30c78671b&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 4. KDE Plot
A Kernel Density Estimate (KDE) plot is a graph that creates a probability distribution curve for the data based upon its likelihood of occurrence on a specific value. This is created for a single vector of information.
**Syntax:**
```python
sns.kdeplot(X) || sns.kdeplot(df['age'])
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0d571213-2a2f-4921-a50b-880847aa05ee/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46627X4SMRC%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T161751Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQC8YHexoNugZ9U4F7d1N18tza5EltvZXaZIdJ%2FNrEAMRwIgdIYbWAVAP3UsBon7qjyPFN4Cq3oAkiGwfLoTbiVL2DYqiAQIwf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNYRCPXApo4PWW%2FbDircA3BCHYQ07loJ%2FG2BwNJxiDsweAyC8JLMrAOlGXwNt8ojfbwz1ce2SmQG4NdgkiSZZm0P0exRAdQYRkFOdGiSkW2FCHUhSUrJzjoO0Dh5epGSQioQY2Few8rTYYlot70EEhOYyvCX11IIruTEind6wVG9dZdJ%2FjjsB6pMyYUclR%2BjSyDkrd8DBCZIHEDCHzzNl1TYCi0hZ%2B8Rkndd8xDV%2Bu7cQBQuNn%2F0S4V34lu%2Fo8teOOWcX%2BZUGPVA%2FsZ8vHr%2FE63oa3bdJbE1H%2BoEYHSh%2BqUHPxvzDoc9bA25Btpd8NQlOGbf310kxh65w5cJ%2Fw97MptHIPn3iJ1crAcab882%2B%2BibTLoDtCpA4EJ4z6OWnRbOhhOb3AjvrKew%2B2ob1zgT65hyyszldyLcirlGOdhqL0d9XSHlSl%2FMrnpoE3FWcKa%2FwBJCtSkvD8jCKuJujW8JteuR97IN1Q%2BLJj0DIP0WW3gLl1vfE1cNPpw9LeAw2Y%2ByTJyBTd4HGcp0aPANkv5PBh8LuFImk9jnba3xjXs48KMCCdfXMmQNftCSKWwNq%2FzzbxgIky3y3DvnbG%2BWtTH1cc4ObEKnQTEXu0f%2Bv%2BgF5t6ST2ym3hlpY2ZTsK14%2FFx%2BEWWybSI4097GLNsIMPjq87wGOqUBtMuBQdKL2J3ALHV1U598J0HZBQ8QLwDV3g5aFO5%2FiIfBpeYYZtzXGAnxneaC5IxQ8yuYojxdsNgNlbhOwHiPpHy2WURWH%2FVPgqDW2M7rkJ2wapwWMpi%2F%2Flt3RAfNIjHlVIsAdIvs5RVOjioCHixBG3nzy4pMfxntkp6vaQr2KTFJIWShUB%2Bte0E9dUZtpoOPrddgHlbos4ZuyTeXjfzS%2FHkFmeGM&X-Amz-Signature=0f801f9e4d60d93b3cc839921ad0ead33fec3f7254ff1d713d8f37e79ebdf231&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/53752550-ef82-4ca9-a01a-09921f0282d0/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46627X4SMRC%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T161751Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQC8YHexoNugZ9U4F7d1N18tza5EltvZXaZIdJ%2FNrEAMRwIgdIYbWAVAP3UsBon7qjyPFN4Cq3oAkiGwfLoTbiVL2DYqiAQIwf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNYRCPXApo4PWW%2FbDircA3BCHYQ07loJ%2FG2BwNJxiDsweAyC8JLMrAOlGXwNt8ojfbwz1ce2SmQG4NdgkiSZZm0P0exRAdQYRkFOdGiSkW2FCHUhSUrJzjoO0Dh5epGSQioQY2Few8rTYYlot70EEhOYyvCX11IIruTEind6wVG9dZdJ%2FjjsB6pMyYUclR%2BjSyDkrd8DBCZIHEDCHzzNl1TYCi0hZ%2B8Rkndd8xDV%2Bu7cQBQuNn%2F0S4V34lu%2Fo8teOOWcX%2BZUGPVA%2FsZ8vHr%2FE63oa3bdJbE1H%2BoEYHSh%2BqUHPxvzDoc9bA25Btpd8NQlOGbf310kxh65w5cJ%2Fw97MptHIPn3iJ1crAcab882%2B%2BibTLoDtCpA4EJ4z6OWnRbOhhOb3AjvrKew%2B2ob1zgT65hyyszldyLcirlGOdhqL0d9XSHlSl%2FMrnpoE3FWcKa%2FwBJCtSkvD8jCKuJujW8JteuR97IN1Q%2BLJj0DIP0WW3gLl1vfE1cNPpw9LeAw2Y%2ByTJyBTd4HGcp0aPANkv5PBh8LuFImk9jnba3xjXs48KMCCdfXMmQNftCSKWwNq%2FzzbxgIky3y3DvnbG%2BWtTH1cc4ObEKnQTEXu0f%2Bv%2BgF5t6ST2ym3hlpY2ZTsK14%2FFx%2BEWWybSI4097GLNsIMPjq87wGOqUBtMuBQdKL2J3ALHV1U598J0HZBQ8QLwDV3g5aFO5%2FiIfBpeYYZtzXGAnxneaC5IxQ8yuYojxdsNgNlbhOwHiPpHy2WURWH%2FVPgqDW2M7rkJ2wapwWMpi%2F%2Flt3RAfNIjHlVIsAdIvs5RVOjioCHixBG3nzy4pMfxntkp6vaQr2KTFJIWShUB%2Bte0E9dUZtpoOPrddgHlbos4ZuyTeXjfzS%2FHkFmeGM&X-Amz-Signature=3fa27e640286585cb82903fe1db011ea17baef011a60bb8049feeea3546625ea&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
## 4. Correlation Between Variables
Correlation is a statistical measure of the extent to which different variables are interdependent. It indicates how changes in one variable are associated with changes in another variable over time.
### Positive Correlation
Positive correlation indicates that as one variable increases, the other variable also tends to increase.
**Example: Engine Size and Price**
- **Positive Correlation:** Engine size increases, price also increases.
- **Visualization:** Scatter plot with a steep positive slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c7ea9b0-3ef3-4357-a9c3-554fc71b6b15/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZDJJSZFI%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T161752Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCue08Jbcj%2FmBjgzwmm9gkWX8uRf6f44MryecCI98uBLAIhAJFNZLn%2Bv%2FoM%2B%2FzPPlZqZHzqlIU%2BykqE%2FWBCmizIyJ4pKogECMH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyHbo2y9Rqt181b7gcq3ANoCQ26lekTkpbVc3aPyS82NdmhNlxWO65qRM6QLBXGEX1V%2FtYuPXrjHh2eSuU3noO6R1nnkI94Yk7POLwwZT7r51yrCn9Fa6ZRzRbNW98AU7ralQRmaAI1W7XkfxeTlVdhYAYQHSA7nDGL9UbVfWXjVKLYzWupqdHhA6WZKlfg6YvtjTMqSc3dk1Sssyqt2mo3LmYohGL6kxdo3AtaosJzn3EGOo6rBHjw1WahR%2BSaOvfMpM0qDJPUGvrgwO21QZWl%2F1aNP6gc5Ae5ZCfs4yHBa4pBb2kcYhEwrosrZSY1XA5XQljdt89L2rjCwUWSAuZ7no5QwyjF9Dy5Fn7SljM%2FNoFMR94JUoa501VPd5nfI2hwzLhgdFG6g1Pkm725FK9AvGX%2FJ85rAGF5mo%2FYaGrXugKdEM%2FF3jjbLXCcltf95AqTLa7Q44QoDvuikYC%2F7ZGV2MPJs%2BQ5m%2FOdOsMO7Izu6O58l8czVzdQXyunyMaM4n2sGMahp1VxX0WTayjWc%2FFM7SYgjJHdFEZH3xyWR4RGjJIIaFCCagwgeQ4FgEASgtP%2BVT93Mc8EQVxxF2cezDWiH%2FA5iO8Qeby8zthCABlI6%2FGMIM9%2Fp1qsuXqGIntDVOiMQ4g8gQRFHdJjuTCh6%2FO8BjqkAffMln3bhC5i6bFd2QZ%2FipZ6IBm6cbqUIkN%2B%2B9mcbpoOO%2BaEj1dwzoIK3YG9%2FxMW%2FPnPh9GI7ta%2BKw2qB9Q1RltrCvn%2ByPKnI63RKRqo6Kfz1Se3soqD3%2FTdtVr14NJAXjVB35etvmRmmvmN60TfBvthoy7Jph7z5VBtJKRs626wrLt0Zkr7tbM37R0heduzFs5LdSH1omztJ6kVRH8FVJc5qo6L&X-Amz-Signature=e3c3bcc49743f625726e9c0d21f525a71f78d61ed10244707852ee66c2d70f2b&X-Amz-SignedHeaders=host&x-id=GetObject)
**Explanation:** When engine size increases, there is a corresponding increase in the price of the vehicle. This positive correlation suggests that larger engines tend to be associated with higher prices in the market.
___
### Negative Correlation
Negative correlation indicates that as one variable increases, the other variable tends to decrease.
**Example: Highway Miles per Gallon and Price**
- **Negative Correlation:** As highway miles per gallon increases, price decreases.
- **Visualization:** Scatter plot with a steep negative slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/10f1f798-9cc4-4df2-a9c1-5a339f554a0b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YF3VH5FT%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T161752Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIBIGIqDcoKDOEgn2DXxylDIusMkTan5m92M%2BEBInaotHAiEAr2O%2FZwNGzxEZO%2BalWJ1CBMuoK2eonaBgzxGLmtpocl0qiAQIwf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKwtrSVbRWIlZNHnvCrcAzZDQbcPSCAJwhVdGugaVmGi8tURK%2Ba1flZtI0uk2MjrK3fvBMXR%2B4orxuwq%2BULFUbO43XMF9XLB74C9TamSZwfsIMXfUhFhZMSYkZyrP5Ves%2F5TpVYg6ofSsJBVM2bjen4vviUWVzsfDOTs2fPlaD9Qo7tL9SjjI%2BGOkw4rSYXSGnA9qPHFQBXiRlEjQft6PkiZlGNEc7fTFZKDQLmlSBhQzAtMi8CimSBEeU8gHucLYhL%2FNrA5u3hovq%2BsIx0kqePIFTbEDGq%2FuvKpaeyfp76PAc0ppOLM6Gta9UKL1VzvmyiRVj13awrw%2FEwMpkkmtmOqWQqnFh4iVQL15x0lMRJlu9lCHzsV9868PP4QFtoGe8q1d%2FpCRCPVul2L7KDFHT6dQnEq2O5NmhHkZvchbggzXdRHcMfsytHmnGVladPtlleHZEFBHYeNdJ0gp15vbpDfDoRzcazAtfWwcGWEU%2BrzEe7SuOkMlEqtH47NzgpGQrIZJ47KCo1YkLVA3IdHIrv9P8ztnAUbGNgtsAAPWK6alkuYgO%2FGpR9mA1oSIgYUFvvl%2BuVNgPLFv8tastSiJO9H0C5O4V49AQLfLVP7nZ74lxmjpOAcq6UAZ9wM9Ws9eP4o%2Btcxt7pwUdMgMLTr87wGOqUBMQRHF1ztjU3icNYJD9N%2BT2Z%2FnZs2ePx5zR%2BuVd8KBhtG2BGA7v%2FW52CJP2y1dInnfuZmn1IKvcfEMfA%2FEl8PLPh5gooW3Akx62sIhYM7daA7vEfVc0wj6fzHE9rGWOgElkTCA%2BGwEDKyp4FLRvwiCzNlGyozaTbw4cJg9NdSeM7O4UfpYbsSsc9iHOkiJ0MScNwe%2FXaZrRwmPKnx1YhgMDEMKPUD&X-Amz-Signature=4a9e5db8b2d8aa0833572d0a74913ff3185f208b09651223facc072eb0109dc4&X-Amz-SignedHeaders=host&x-id=GetObject)
**Explanation:** When highway miles per gallon increases, the price of the vehicle tends to decrease. This negative correlation suggests that cars with higher fuel efficiency (more miles per gallon) are generally priced lower in the market.
___
### Weak Correlation
Weak correlation indicates a lack of strong relationship between the variables.
**Example: RPM and Price**
- **Weak Correlation:** Low and high RPM values show varied prices, indicating no strong predictive relationship.
- **Visualization:** Scatter plot with no clear trend or slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9f914514-8914-4bf4-ac84-d9e3077f6eb1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46677KJUGWI%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T161754Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGMhlZXxOJAFQCPyuH%2FRSI%2BvsnFepolDuEl11KfwLSw%2BAiBSEGqqkBlf3KUROvwjn7OMVK%2F3pSPweC2PJgd2Is%2FSTiqIBAjB%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMpD8AXi4nvlKbDi5HKtwDGM7c9bEsh7OBvAbt6%2F3o5cV626viHdRd8oh%2Bu7mEK77GYkwGHP9uy9rX8LOD1qMEflH%2FtzR8E1aVTpmiNyats%2BTJnowIfqEJ2fFAuP4Ln3LBk7%2B%2Bik1GmmeZFIAZ7YTUJrnjOXGAfolftKxIOGDJ37daa7HMmUK7Wmrd%2B5CNISUu9htdSg%2FZKqCf%2F227p39nnPwAlPbhAc6BRtzku4NpjK4GnIohbNQYIC%2FL5nkja6D7WqEpZ0Sh6x2iQAdBJA%2FIWOy54RvQLtVRQ%2BouwY5xNoZ%2F6ed3kiExVw%2B9ssIZGKjZFAhTxQ%2Bz48FrUH87cLrJ1kfcDctcF%2BWlRjioYMEETtxaQPZNxakHELzhHhrlh9oPp5nEw1tHAippafO2Pctl6jo8ocHEQZdjH2ieneI82agx0yMd8Yb9srenZTgK%2FdELf46bLPtX%2FfzL56UfgqmKfsF48vPR9UBl7dtRt0aUVeAsIgfXTZNJC%2F7WcW8Srb1rHT3l0CvkOX151jeGyb2CTPYdRCBNzf4bZtZn98i2eXCbQjINrOHSEKeFCFoFuzhHuguacS7Keomyxv7UpK3pPqY64uoBUvGPRKobve52wncrtIp6%2FuVZn%2BzPDLolO6ROpSsAX6p%2Bd0WGtikwl%2BvzvAY6pgEzcQgtcb5tWU%2F0nf8tRBi9E9MXSrV5SpEcbbSDMVvv38lylr3PiRaVbxQv5P3hOjMaGQKgOpjzk1bB3ZQEgoYn2HxsI79TOQezcpr7SsTrEzXspzdyOv2VSC4m%2BSCKPZB3d8wdYt9WEbVYyhlntNYV%2FvUU7%2ByVAo1FWgVuFL1%2FF%2BWShPIEsujmP%2Fq6bkkeijZgb1nZTL7u%2FbVwYaDkxI8rw1JF6b%2Fh&X-Amz-Signature=653cf290651f164a1629446af12a04c424cb5038767f9c0d48c59d4008e17ae5&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f18086e5-5b04-4fbf-8309-8944ab20d213/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VWHUFJGQ%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T161752Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCsr8vbj1%2FZowTcXmD%2B3qcYNF5N30NaELXfiAjX%2BuCPQQIgO0JP4%2Bi0BMI2gusnTSdU48hVatyw9DcVl18%2FLkpnXHoqiAQIwf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNU81EoVm5SlzfwPTircA90rUxORW8vl2P%2BWIutrHLIYaxduY8MqUpxUubnMT5qc45vPO84gVRGdzOdggqXlvJYasyOPOnnMAMLzMLSVQ70zUqWyZh0Odp3o7g2Vfc%2BxnOocc3JF1lkRCUEVqtfy%2BD9nHegi4ujazLNqcfyR13276ei%2F0KPqPTAL0AE5n8QNucNNLEEPMML13AJKlIWLam498IQH8l5be8rFVJfuaSLliRq1YekpdaUuXbjpUlNahaBHQ5TO51jJqIE5%2BzOqdIJXaA3ErJrGNkMyH5BO%2BS3T7L0UDm%2BC2AKhaDWS6t9Q3%2FMqpWeG0EQIIvu%2FcWVL3%2BnNtWY51nTFIHgYczyJKjCo3nROlm4rCNHuaKx8iyEBFVv0qQb3CNE3D5ZUydZsZApZnJqODpXdy6jNZAhfx5WV94g7xejm6JimLjMwC56cYCWUXQnCagQSCT0urMCSxIsMgPut0cdIGFWgAwyUWlKgLiQ43JFIFSS3730KThhAjUFB6THReFMjtJTTHNzlAVZB6xbIgaI5ufwfpzNuvimfMb1iIB22x23hvf9QySXYNwPv5TuPelgUZ3qHI8WDodWrlPE80NdGItRFV4RrJRYyBaj1%2BAYKYFDKccngSXp%2FC6RTW%2FhNCmzW0YPYMIbr87wGOqUByzROCf0t6RjUKdtEPgyEfiTdevWdOCp1d6zR%2FS3yy%2BFpTG2pTIweLJSN2LVKjQoiadRPV5TcaLnq24IKVwVZSQ14HDe9N%2Fuozi2zDP7f1OfZbjVOPMksgQ5DWDq9T4dh3TRVT81%2Fq%2FaX3FXWbUAt3SJmV2fNnqGEQ4oswfOC%2F77jPu0Wlfl3XMTvnbTVWToDU4%2Bq8Z78gCbgRKvgFew2hgqNMyKJ&X-Amz-Signature=7091e629028294594399aeed1be4c228ed26dfa388089c84e6667c12782c1f37&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Correlation Plot
Heatmap visualizes correlations among variables. Color scheme indicates Pearson correlation coefficients. Dark red diagonal line shows perfect correlation (value of 1) between variables and themselves.
This heatmap offers overview of variable relationships and their link with price.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cd3b341e-cc1a-45f7-8aec-cdc00436d270/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VWHUFJGQ%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T161752Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCsr8vbj1%2FZowTcXmD%2B3qcYNF5N30NaELXfiAjX%2BuCPQQIgO0JP4%2Bi0BMI2gusnTSdU48hVatyw9DcVl18%2FLkpnXHoqiAQIwf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNU81EoVm5SlzfwPTircA90rUxORW8vl2P%2BWIutrHLIYaxduY8MqUpxUubnMT5qc45vPO84gVRGdzOdggqXlvJYasyOPOnnMAMLzMLSVQ70zUqWyZh0Odp3o7g2Vfc%2BxnOocc3JF1lkRCUEVqtfy%2BD9nHegi4ujazLNqcfyR13276ei%2F0KPqPTAL0AE5n8QNucNNLEEPMML13AJKlIWLam498IQH8l5be8rFVJfuaSLliRq1YekpdaUuXbjpUlNahaBHQ5TO51jJqIE5%2BzOqdIJXaA3ErJrGNkMyH5BO%2BS3T7L0UDm%2BC2AKhaDWS6t9Q3%2FMqpWeG0EQIIvu%2FcWVL3%2BnNtWY51nTFIHgYczyJKjCo3nROlm4rCNHuaKx8iyEBFVv0qQb3CNE3D5ZUydZsZApZnJqODpXdy6jNZAhfx5WV94g7xejm6JimLjMwC56cYCWUXQnCagQSCT0urMCSxIsMgPut0cdIGFWgAwyUWlKgLiQ43JFIFSS3730KThhAjUFB6THReFMjtJTTHNzlAVZB6xbIgaI5ufwfpzNuvimfMb1iIB22x23hvf9QySXYNwPv5TuPelgUZ3qHI8WDodWrlPE80NdGItRFV4RrJRYyBaj1%2BAYKYFDKccngSXp%2FC6RTW%2FhNCmzW0YPYMIbr87wGOqUByzROCf0t6RjUKdtEPgyEfiTdevWdOCp1d6zR%2FS3yy%2BFpTG2pTIweLJSN2LVKjQoiadRPV5TcaLnq24IKVwVZSQ14HDe9N%2Fuozi2zDP7f1OfZbjVOPMksgQ5DWDq9T4dh3TRVT81%2Fq%2FaX3FXWbUAt3SJmV2fNnqGEQ4oswfOC%2F77jPu0Wlfl3XMTvnbTVWToDU4%2Bq8Z78gCbgRKvgFew2hgqNMyKJ&X-Amz-Signature=b7373dd203bb716badfdecdf923f36ecdcdcec7481824b848b8bed5e727d5bac&X-Amz-SignedHeaders=host&x-id=GetObject)

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
