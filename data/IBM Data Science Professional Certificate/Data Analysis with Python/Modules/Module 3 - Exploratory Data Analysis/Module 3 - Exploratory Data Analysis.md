

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7e6d594d-952e-44b6-97ea-31225882aea6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662DXFQTZ7%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T101401Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHAaCXVzLXdlc3QtMiJIMEYCIQCYMWJi3BaI5DTZVtV5NE6SiWT96UgzedqgtX4HhymnUwIhALaOFXeHkcz5anruct%2Bett0o%2BlXFfUDSmuizGnbI71dzKogECIn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwNKj0whbxhRtzGfX8q3ANpPykwWhYA99rXBpTR%2BTIceHcnlPq0zVbWeifeR2lJSryvvfKTbW0fF2T3KebncaPrsLa7I9tdRQ%2F%2FhfWErjyNlsodS0tlC5dDdXHgQzWL2IsNGAZpwOqh7bdZJGxmaDQ7b%2BuatfRzUxFeNdoeIdHQRkl%2FG1yzXaehbBr2ESPcgcyz9K7GyiYnhYLHPFJw5pkjclR6HBMje1RUCloPdwQ9ue4sEk9fc3aGbdewzkNmOh4A%2FHjE94Fn3NAJ7krp15NVnrr86qXTb6zQBw0d2LdbEgDFeFgngvGX7dBuQ7FtNRrNPpnY%2F%2FKpjS4%2FQsHeAgINOX5FUZQwRxpH4LWLYQ71wHCTW%2BC3MJMT2FFfsy8zdPEEepKSJlLvKB1t4p5FYGFTS1tRly54Eg7z7wAggpF9N9oO38MlRu5zbtzMPtD7Q9ckd3T1n605xgv97CTlib2ECk%2BDsRNehjrpkECE0%2F8G%2FogkuYRqz3%2FVVIiVwHC192MEf8yTtL46bk2JxnR9KTp4%2BcmWfvipWVNCbocUxSEKAmCfF5EpQHdmO2I99pCZQjiZx6PJ%2BF7NRI3AeVZxs45WGZ21NXrckNi4r7J%2FCbPpNdk2oGX5PJpurp%2Fed20rP0sZUpLLIoOMrWMEbjDTjpy9BjqkAbckVav78qTYLG04xfCB4ELzArIpc5Jyjm2pEM98zwZV7UjB%2Fhhsgj5EYo0eB7EZ9MbFtdAH1lzFd6dQ9g%2Bkg6C48DlNBF%2Bt3bcKIYsae6WMBY6gk7yuop2LTlBjChj9Gx3dlRbB6VhggbWRDj77yjsr9alehj0Bb961eDgIq7mqRJ5Sy3CazPQ2yuKxX7%2BKOhN%2BDxzFeOcmj5eKS1XhoLkO%2FbhF&X-Amz-Signature=368975b3596c761bd4552e4f784f10984d61120ff4641dfbf471ff6984e18b8d&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cbfaed9e-b398-4902-8936-dea058b21def/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662DXFQTZ7%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T101401Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHAaCXVzLXdlc3QtMiJIMEYCIQCYMWJi3BaI5DTZVtV5NE6SiWT96UgzedqgtX4HhymnUwIhALaOFXeHkcz5anruct%2Bett0o%2BlXFfUDSmuizGnbI71dzKogECIn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwNKj0whbxhRtzGfX8q3ANpPykwWhYA99rXBpTR%2BTIceHcnlPq0zVbWeifeR2lJSryvvfKTbW0fF2T3KebncaPrsLa7I9tdRQ%2F%2FhfWErjyNlsodS0tlC5dDdXHgQzWL2IsNGAZpwOqh7bdZJGxmaDQ7b%2BuatfRzUxFeNdoeIdHQRkl%2FG1yzXaehbBr2ESPcgcyz9K7GyiYnhYLHPFJw5pkjclR6HBMje1RUCloPdwQ9ue4sEk9fc3aGbdewzkNmOh4A%2FHjE94Fn3NAJ7krp15NVnrr86qXTb6zQBw0d2LdbEgDFeFgngvGX7dBuQ7FtNRrNPpnY%2F%2FKpjS4%2FQsHeAgINOX5FUZQwRxpH4LWLYQ71wHCTW%2BC3MJMT2FFfsy8zdPEEepKSJlLvKB1t4p5FYGFTS1tRly54Eg7z7wAggpF9N9oO38MlRu5zbtzMPtD7Q9ckd3T1n605xgv97CTlib2ECk%2BDsRNehjrpkECE0%2F8G%2FogkuYRqz3%2FVVIiVwHC192MEf8yTtL46bk2JxnR9KTp4%2BcmWfvipWVNCbocUxSEKAmCfF5EpQHdmO2I99pCZQjiZx6PJ%2BF7NRI3AeVZxs45WGZ21NXrckNi4r7J%2FCbPpNdk2oGX5PJpurp%2Fed20rP0sZUpLLIoOMrWMEbjDTjpy9BjqkAbckVav78qTYLG04xfCB4ELzArIpc5Jyjm2pEM98zwZV7UjB%2Fhhsgj5EYo0eB7EZ9MbFtdAH1lzFd6dQ9g%2Bkg6C48DlNBF%2Bt3bcKIYsae6WMBY6gk7yuop2LTlBjChj9Gx3dlRbB6VhggbWRDj77yjsr9alehj0Bb961eDgIq7mqRJ5Sy3CazPQ2yuKxX7%2BKOhN%2BDxzFeOcmj5eKS1XhoLkO%2FbhF&X-Amz-Signature=1f2d96aa78d63e800b243ec74d4c0ddd82cbf50f76c668f147006c0896382c4f&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/91181646-b1e0-4433-9711-6259a96a9247/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662DXFQTZ7%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T101401Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHAaCXVzLXdlc3QtMiJIMEYCIQCYMWJi3BaI5DTZVtV5NE6SiWT96UgzedqgtX4HhymnUwIhALaOFXeHkcz5anruct%2Bett0o%2BlXFfUDSmuizGnbI71dzKogECIn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwNKj0whbxhRtzGfX8q3ANpPykwWhYA99rXBpTR%2BTIceHcnlPq0zVbWeifeR2lJSryvvfKTbW0fF2T3KebncaPrsLa7I9tdRQ%2F%2FhfWErjyNlsodS0tlC5dDdXHgQzWL2IsNGAZpwOqh7bdZJGxmaDQ7b%2BuatfRzUxFeNdoeIdHQRkl%2FG1yzXaehbBr2ESPcgcyz9K7GyiYnhYLHPFJw5pkjclR6HBMje1RUCloPdwQ9ue4sEk9fc3aGbdewzkNmOh4A%2FHjE94Fn3NAJ7krp15NVnrr86qXTb6zQBw0d2LdbEgDFeFgngvGX7dBuQ7FtNRrNPpnY%2F%2FKpjS4%2FQsHeAgINOX5FUZQwRxpH4LWLYQ71wHCTW%2BC3MJMT2FFfsy8zdPEEepKSJlLvKB1t4p5FYGFTS1tRly54Eg7z7wAggpF9N9oO38MlRu5zbtzMPtD7Q9ckd3T1n605xgv97CTlib2ECk%2BDsRNehjrpkECE0%2F8G%2FogkuYRqz3%2FVVIiVwHC192MEf8yTtL46bk2JxnR9KTp4%2BcmWfvipWVNCbocUxSEKAmCfF5EpQHdmO2I99pCZQjiZx6PJ%2BF7NRI3AeVZxs45WGZ21NXrckNi4r7J%2FCbPpNdk2oGX5PJpurp%2Fed20rP0sZUpLLIoOMrWMEbjDTjpy9BjqkAbckVav78qTYLG04xfCB4ELzArIpc5Jyjm2pEM98zwZV7UjB%2Fhhsgj5EYo0eB7EZ9MbFtdAH1lzFd6dQ9g%2Bkg6C48DlNBF%2Bt3bcKIYsae6WMBY6gk7yuop2LTlBjChj9Gx3dlRbB6VhggbWRDj77yjsr9alehj0Bb961eDgIq7mqRJ5Sy3CazPQ2yuKxX7%2BKOhN%2BDxzFeOcmj5eKS1XhoLkO%2FbhF&X-Amz-Signature=82b4b7f4c07dc64f61ac6f99010c3716f2c2002925dffd3d5c570fc5c3553779&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/09aba1c0-0d55-41dd-852a-a04c5b8a3fac/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665IAZ6ULZ%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T101402Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHAaCXVzLXdlc3QtMiJIMEYCIQDpsjtdmNnOAIm8YD0s%2FrNX3t%2FYfFI4hIo2OzNNUPygowIhAJdZHVg0AvRA2Z6t2dVAcofiMHWhmp6jD9yxV0W5ybLcKogECIn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzsP7gmWIHpveq%2B6zcq3AMHS7TigjBY742cQXtgiwGJVRQ%2Fxj%2F4sc02gF9ARLnG5pmmmThEJ9RNhb1nki%2BgO9%2BNoEnLYbe6Ps64oYiwJb%2FzVsU4nLi8MmrCmemT61pdyj5R8SsTS3i5AFj7wf2jHz7wsPDBFhvaV2IgV8VGETCSrm7GFG1pRUiIstDyt8BePGAaBWkdGlIyFxqfmudt7Iecw2iWhzz%2FFn%2FCc3EH7NEyK%2FbaM4afyO9LcvmmedAlys6w6icivvpgPi9hoN9EJl2wyoj3uxjVbAYGSLPt9qtUMNQuqqyTSJHJRNxnyqbi20mvc8Pd7Lzxt0hHNR%2FiM9ZHefTZOv8mKklOoJLSXA7zFhJVVzsKE6rmxfNvCdY74GG%2BRdgTZ28gDqdOIoD8Dla%2Brscba0dXD2gU5L4RzAD6KPIg6FZBSF4ixZKQRB5rKb4hWjztWRdgFc4EU1QEHcJfl%2FhnG37vLvv7fFIRR%2BZ%2BLyvDaqdYYDUtzgl09crfCoJOe5reVgjWsGBTlktXiE61JyYBMcKSy08pMOnrkKBQi0QNS3kl6OZZ51zLRnykbZRCWMNhGC62%2BOLCA%2BeOvGp6G139UsGjkZaSqqmWH%2BLqwbzRaz7XO%2BO7CLPgI7xmBp3YdPGw8vWPFAkWnzDDjpy9BjqkAaV9duKsCoDcTXB4cwCdwlWYq7WGdBAmfaTeCKwBcNFv7wOOqucvQWc68kmSqYnAGY8DivZHqbrJlQZANT%2FWcqFWBWxtx8b211FRxzS47IWuS7wXcL1gxCH9guDrsVdw1GUkM86K%2Fd97bXJRTT0bmvX3WpoU4vQ66%2B6YllbrAlaWLjO3qOKusqKEF4juzIy5zDaWA5wyWeaTZx7YB6XNSlUtLx%2BP&X-Amz-Signature=fbef137035f5ceb1be2f76464cde4f453d83bc445a8e3c3f4f1e414b38bed523&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 2. Scatter Plot
Scatter plots present the relationship between two variables in a dataset. It represents data points on a two-dimensional plane. The independent variable or attribute is plotted on the X-axis, while the dependent variable is plotted on the Y-axis.
**Syntax:**
```python
plt.scatter(x, y)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23708af9-659f-4f23-b626-1a4292d7842c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665IAZ6ULZ%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T101402Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHAaCXVzLXdlc3QtMiJIMEYCIQDpsjtdmNnOAIm8YD0s%2FrNX3t%2FYfFI4hIo2OzNNUPygowIhAJdZHVg0AvRA2Z6t2dVAcofiMHWhmp6jD9yxV0W5ybLcKogECIn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzsP7gmWIHpveq%2B6zcq3AMHS7TigjBY742cQXtgiwGJVRQ%2Fxj%2F4sc02gF9ARLnG5pmmmThEJ9RNhb1nki%2BgO9%2BNoEnLYbe6Ps64oYiwJb%2FzVsU4nLi8MmrCmemT61pdyj5R8SsTS3i5AFj7wf2jHz7wsPDBFhvaV2IgV8VGETCSrm7GFG1pRUiIstDyt8BePGAaBWkdGlIyFxqfmudt7Iecw2iWhzz%2FFn%2FCc3EH7NEyK%2FbaM4afyO9LcvmmedAlys6w6icivvpgPi9hoN9EJl2wyoj3uxjVbAYGSLPt9qtUMNQuqqyTSJHJRNxnyqbi20mvc8Pd7Lzxt0hHNR%2FiM9ZHefTZOv8mKklOoJLSXA7zFhJVVzsKE6rmxfNvCdY74GG%2BRdgTZ28gDqdOIoD8Dla%2Brscba0dXD2gU5L4RzAD6KPIg6FZBSF4ixZKQRB5rKb4hWjztWRdgFc4EU1QEHcJfl%2FhnG37vLvv7fFIRR%2BZ%2BLyvDaqdYYDUtzgl09crfCoJOe5reVgjWsGBTlktXiE61JyYBMcKSy08pMOnrkKBQi0QNS3kl6OZZ51zLRnykbZRCWMNhGC62%2BOLCA%2BeOvGp6G139UsGjkZaSqqmWH%2BLqwbzRaz7XO%2BO7CLPgI7xmBp3YdPGw8vWPFAkWnzDDjpy9BjqkAaV9duKsCoDcTXB4cwCdwlWYq7WGdBAmfaTeCKwBcNFv7wOOqucvQWc68kmSqYnAGY8DivZHqbrJlQZANT%2FWcqFWBWxtx8b211FRxzS47IWuS7wXcL1gxCH9guDrsVdw1GUkM86K%2Fd97bXJRTT0bmvX3WpoU4vQ66%2B6YllbrAlaWLjO3qOKusqKEF4juzIy5zDaWA5wyWeaTZx7YB6XNSlUtLx%2BP&X-Amz-Signature=6542b071fcd05894b834ed3b1007224705f8194dfd65a1e53d5b49cbcf1638ad&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 3. Histogram
A histogram is an important visual representation of data in categorical form. To view the data in a "Binned" form, use the histogram plot with a number of bins required or with the data points that mark the bin edges. The x-axis represents the data bins, and the y-axis represents the number of elements in each bin.
**Syntax:**
```python
plt.hist(x, bins)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/24e4424a-df87-40a1-b63b-195cbdc2e0ab/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665IAZ6ULZ%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T101402Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHAaCXVzLXdlc3QtMiJIMEYCIQDpsjtdmNnOAIm8YD0s%2FrNX3t%2FYfFI4hIo2OzNNUPygowIhAJdZHVg0AvRA2Z6t2dVAcofiMHWhmp6jD9yxV0W5ybLcKogECIn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzsP7gmWIHpveq%2B6zcq3AMHS7TigjBY742cQXtgiwGJVRQ%2Fxj%2F4sc02gF9ARLnG5pmmmThEJ9RNhb1nki%2BgO9%2BNoEnLYbe6Ps64oYiwJb%2FzVsU4nLi8MmrCmemT61pdyj5R8SsTS3i5AFj7wf2jHz7wsPDBFhvaV2IgV8VGETCSrm7GFG1pRUiIstDyt8BePGAaBWkdGlIyFxqfmudt7Iecw2iWhzz%2FFn%2FCc3EH7NEyK%2FbaM4afyO9LcvmmedAlys6w6icivvpgPi9hoN9EJl2wyoj3uxjVbAYGSLPt9qtUMNQuqqyTSJHJRNxnyqbi20mvc8Pd7Lzxt0hHNR%2FiM9ZHefTZOv8mKklOoJLSXA7zFhJVVzsKE6rmxfNvCdY74GG%2BRdgTZ28gDqdOIoD8Dla%2Brscba0dXD2gU5L4RzAD6KPIg6FZBSF4ixZKQRB5rKb4hWjztWRdgFc4EU1QEHcJfl%2FhnG37vLvv7fFIRR%2BZ%2BLyvDaqdYYDUtzgl09crfCoJOe5reVgjWsGBTlktXiE61JyYBMcKSy08pMOnrkKBQi0QNS3kl6OZZ51zLRnykbZRCWMNhGC62%2BOLCA%2BeOvGp6G139UsGjkZaSqqmWH%2BLqwbzRaz7XO%2BO7CLPgI7xmBp3YdPGw8vWPFAkWnzDDjpy9BjqkAaV9duKsCoDcTXB4cwCdwlWYq7WGdBAmfaTeCKwBcNFv7wOOqucvQWc68kmSqYnAGY8DivZHqbrJlQZANT%2FWcqFWBWxtx8b211FRxzS47IWuS7wXcL1gxCH9guDrsVdw1GUkM86K%2Fd97bXJRTT0bmvX3WpoU4vQ66%2B6YllbrAlaWLjO3qOKusqKEF4juzIy5zDaWA5wyWeaTZx7YB6XNSlUtLx%2BP&X-Amz-Signature=198d70d0f46e4077409c47a42af526095c109a2fabfe2aed1bcfd9d9bc8d13b9&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ab5a6dfe-51f5-43ee-bcb3-33dae4a1c7ad/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665IAZ6ULZ%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T101402Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHAaCXVzLXdlc3QtMiJIMEYCIQDpsjtdmNnOAIm8YD0s%2FrNX3t%2FYfFI4hIo2OzNNUPygowIhAJdZHVg0AvRA2Z6t2dVAcofiMHWhmp6jD9yxV0W5ybLcKogECIn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzsP7gmWIHpveq%2B6zcq3AMHS7TigjBY742cQXtgiwGJVRQ%2Fxj%2F4sc02gF9ARLnG5pmmmThEJ9RNhb1nki%2BgO9%2BNoEnLYbe6Ps64oYiwJb%2FzVsU4nLi8MmrCmemT61pdyj5R8SsTS3i5AFj7wf2jHz7wsPDBFhvaV2IgV8VGETCSrm7GFG1pRUiIstDyt8BePGAaBWkdGlIyFxqfmudt7Iecw2iWhzz%2FFn%2FCc3EH7NEyK%2FbaM4afyO9LcvmmedAlys6w6icivvpgPi9hoN9EJl2wyoj3uxjVbAYGSLPt9qtUMNQuqqyTSJHJRNxnyqbi20mvc8Pd7Lzxt0hHNR%2FiM9ZHefTZOv8mKklOoJLSXA7zFhJVVzsKE6rmxfNvCdY74GG%2BRdgTZ28gDqdOIoD8Dla%2Brscba0dXD2gU5L4RzAD6KPIg6FZBSF4ixZKQRB5rKb4hWjztWRdgFc4EU1QEHcJfl%2FhnG37vLvv7fFIRR%2BZ%2BLyvDaqdYYDUtzgl09crfCoJOe5reVgjWsGBTlktXiE61JyYBMcKSy08pMOnrkKBQi0QNS3kl6OZZ51zLRnykbZRCWMNhGC62%2BOLCA%2BeOvGp6G139UsGjkZaSqqmWH%2BLqwbzRaz7XO%2BO7CLPgI7xmBp3YdPGw8vWPFAkWnzDDjpy9BjqkAaV9duKsCoDcTXB4cwCdwlWYq7WGdBAmfaTeCKwBcNFv7wOOqucvQWc68kmSqYnAGY8DivZHqbrJlQZANT%2FWcqFWBWxtx8b211FRxzS47IWuS7wXcL1gxCH9guDrsVdw1GUkM86K%2Fd97bXJRTT0bmvX3WpoU4vQ66%2B6YllbrAlaWLjO3qOKusqKEF4juzIy5zDaWA5wyWeaTZx7YB6XNSlUtLx%2BP&X-Amz-Signature=433d341e73e1b4dacb727b9d37149a79b813dcc9cca125e6581058446b5d85bf&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8f1b1d60-cf1b-42b3-9faa-f634c89c3f84/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665IAZ6ULZ%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T101402Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHAaCXVzLXdlc3QtMiJIMEYCIQDpsjtdmNnOAIm8YD0s%2FrNX3t%2FYfFI4hIo2OzNNUPygowIhAJdZHVg0AvRA2Z6t2dVAcofiMHWhmp6jD9yxV0W5ybLcKogECIn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzsP7gmWIHpveq%2B6zcq3AMHS7TigjBY742cQXtgiwGJVRQ%2Fxj%2F4sc02gF9ARLnG5pmmmThEJ9RNhb1nki%2BgO9%2BNoEnLYbe6Ps64oYiwJb%2FzVsU4nLi8MmrCmemT61pdyj5R8SsTS3i5AFj7wf2jHz7wsPDBFhvaV2IgV8VGETCSrm7GFG1pRUiIstDyt8BePGAaBWkdGlIyFxqfmudt7Iecw2iWhzz%2FFn%2FCc3EH7NEyK%2FbaM4afyO9LcvmmedAlys6w6icivvpgPi9hoN9EJl2wyoj3uxjVbAYGSLPt9qtUMNQuqqyTSJHJRNxnyqbi20mvc8Pd7Lzxt0hHNR%2FiM9ZHefTZOv8mKklOoJLSXA7zFhJVVzsKE6rmxfNvCdY74GG%2BRdgTZ28gDqdOIoD8Dla%2Brscba0dXD2gU5L4RzAD6KPIg6FZBSF4ixZKQRB5rKb4hWjztWRdgFc4EU1QEHcJfl%2FhnG37vLvv7fFIRR%2BZ%2BLyvDaqdYYDUtzgl09crfCoJOe5reVgjWsGBTlktXiE61JyYBMcKSy08pMOnrkKBQi0QNS3kl6OZZ51zLRnykbZRCWMNhGC62%2BOLCA%2BeOvGp6G139UsGjkZaSqqmWH%2BLqwbzRaz7XO%2BO7CLPgI7xmBp3YdPGw8vWPFAkWnzDDjpy9BjqkAaV9duKsCoDcTXB4cwCdwlWYq7WGdBAmfaTeCKwBcNFv7wOOqucvQWc68kmSqYnAGY8DivZHqbrJlQZANT%2FWcqFWBWxtx8b211FRxzS47IWuS7wXcL1gxCH9guDrsVdw1GUkM86K%2Fd97bXJRTT0bmvX3WpoU4vQ66%2B6YllbrAlaWLjO3qOKusqKEF4juzIy5zDaWA5wyWeaTZx7YB6XNSlUtLx%2BP&X-Amz-Signature=32dcbb723e7ca2bee663159173e8cab3b1a1343f0ad52f87be02bdcf3fae5948&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/13ad0497-05fe-4eaa-984e-707b33e14761/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665IAZ6ULZ%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T101402Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHAaCXVzLXdlc3QtMiJIMEYCIQDpsjtdmNnOAIm8YD0s%2FrNX3t%2FYfFI4hIo2OzNNUPygowIhAJdZHVg0AvRA2Z6t2dVAcofiMHWhmp6jD9yxV0W5ybLcKogECIn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzsP7gmWIHpveq%2B6zcq3AMHS7TigjBY742cQXtgiwGJVRQ%2Fxj%2F4sc02gF9ARLnG5pmmmThEJ9RNhb1nki%2BgO9%2BNoEnLYbe6Ps64oYiwJb%2FzVsU4nLi8MmrCmemT61pdyj5R8SsTS3i5AFj7wf2jHz7wsPDBFhvaV2IgV8VGETCSrm7GFG1pRUiIstDyt8BePGAaBWkdGlIyFxqfmudt7Iecw2iWhzz%2FFn%2FCc3EH7NEyK%2FbaM4afyO9LcvmmedAlys6w6icivvpgPi9hoN9EJl2wyoj3uxjVbAYGSLPt9qtUMNQuqqyTSJHJRNxnyqbi20mvc8Pd7Lzxt0hHNR%2FiM9ZHefTZOv8mKklOoJLSXA7zFhJVVzsKE6rmxfNvCdY74GG%2BRdgTZ28gDqdOIoD8Dla%2Brscba0dXD2gU5L4RzAD6KPIg6FZBSF4ixZKQRB5rKb4hWjztWRdgFc4EU1QEHcJfl%2FhnG37vLvv7fFIRR%2BZ%2BLyvDaqdYYDUtzgl09crfCoJOe5reVgjWsGBTlktXiE61JyYBMcKSy08pMOnrkKBQi0QNS3kl6OZZ51zLRnykbZRCWMNhGC62%2BOLCA%2BeOvGp6G139UsGjkZaSqqmWH%2BLqwbzRaz7XO%2BO7CLPgI7xmBp3YdPGw8vWPFAkWnzDDjpy9BjqkAaV9duKsCoDcTXB4cwCdwlWYq7WGdBAmfaTeCKwBcNFv7wOOqucvQWc68kmSqYnAGY8DivZHqbrJlQZANT%2FWcqFWBWxtx8b211FRxzS47IWuS7wXcL1gxCH9guDrsVdw1GUkM86K%2Fd97bXJRTT0bmvX3WpoU4vQ66%2B6YllbrAlaWLjO3qOKusqKEF4juzIy5zDaWA5wyWeaTZx7YB6XNSlUtLx%2BP&X-Amz-Signature=88a896b62ae3867f03c15ba2a98ca2d021f896b19ed60f0395c9b79e4ccf46d6&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 2. Box and Whisker Plot
A box plot shows the distribution of quantitative data in a way that facilitates comparisons between variables or across levels of a categorical variable. The box shows the quartiles of the dataset while the whiskers extend to show the rest of the distribution, except for points that are determined to be "outliers".
**Syntax:**
```python
sns.boxplot(x='header_1', y='header_2', data=df)
```
**Example Output:**


![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d207ae92-0a7c-4e2f-aa65-0ee5a2c33bf7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663B22FMW4%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T101403Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHAaCXVzLXdlc3QtMiJGMEQCIHeTbVOiWd5BMVDFUaWhcHJa0M8cbmDp8i3kZ5TAloTjAiAhrD6N6m0SU%2BiXtkx2LWRB1O9epbv0x7xgO6JWJNhdpSqIBAiI%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMaKAZA3bxQnydrVBNKtwDpyG0zbH%2FbvjlJhe5Am5mqdbkT%2FtvV5pZaSwEwpsxLR7HPUjlubGh458Vj74mDzGLiPzL8fX9BTI6k5wOGD%2FbJsd1sVDNxvSB%2FMKVnPG22hPiIn%2BiL%2BG9cdL%2FH457PSR7id8bmC3vqoY0q9VtehPEig5qK5H0mCv5%2BLFYfPtwXwcg4Dr7MklxieD5HZ5Qdlp2Qd%2FunIeTOXGICNXFabo%2B0hlbHdR%2FQQsktwkQ0tL2%2B8mxQTJbXUtyeC8QjtOuZqf00FFUEJfFQxfr5VE6Mq5V38ADKgwFzcAp8VGXNH4eWKJFN7teltNPj4mfB6OA9jLLr7GQI13SeBsBOghZjHvpnrXRwfArnDRJMzY9FG8ii2TFAlFSAiZBAJKR1%2FvSo%2Bah1BrAcFlEGOKRnlJYteewv9Zy56Y66oR0EKJ31UDaLn1lAW9884hgNTI9mpwXkRI2Kpm2w9GD%2BNugunbVmyqMi%2B4G2V%2FZp0IPqH5wwjZcLfdQ83kgTo%2F5MCEs6mOAEhC11MLwbiBNvYHUyl1ZkO2SEakmRNWs2KHCeh%2B0UF73SABJgpaYVcYKz%2BSZVgeA6S4Qmz2%2FK7P3nI0FCZI5CN9G3uR8Qwh7vahGuxpFNM%2FRTh6TOkfNTqMC2r%2B7Ul8w9I6cvQY6pgEE65lQu1qMt67w9DqJiZtjqFdkErU8muBgDRHIFF7yizJrRQ%2B7ZkQHV0aJVaBriX5m4nlEMLiLyuHwQigD3kuQR46pLjF12kinQ%2FhlkdgTBBQq6VGxVTRhI7NAiarirQGiJfV8oFHUi%2BQSZiI7LPLdx11K1A6wJuPnwJtDJl91z%2FkEMA0L9im3lQ7DakzWEY7ekQu9O9qUQ9Y%2FtPakJiXaHjf97CWo&X-Amz-Signature=4e7125c0fc7480196655a7d7a5bd8670e3ec74da4a2020fc405516c110639a58&X-Amz-SignedHeaders=host&x-id=GetObject)

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0e516edc-7551-4792-ab18-0494db3c4c0c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666GKJYUPI%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T101403Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHAaCXVzLXdlc3QtMiJHMEUCIFxSzbJoGnXF99URf9%2FDJGgsW4Bc40ZbjUpwpI%2B%2Fco5sAiEAo3eAvR8PON58LETvNkDc2752onHXVaq2HCV935BfwakqiAQIiP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDK8wmujivUkfEjjGHSrcA97SQeeRz%2BBMfN6cNwWf3hexCu60CPPaxD9FTwDI5gAteRnMHopNYCnv9dlWDCxzgkZ9Vp6lzzcfrqEp7hUVu5%2BXZTq26n08uinOSbOGevi1soqXM8XG4Jde4ZJMNQLq1PK9fqNhWaH5sXfxU735BWEw3BWmqp%2BhG9rY0pka3VK42lIr%2FdDEc58oHTtGNlzRNvMS7HwFYBFfWCI8Uz0KxWuUKLM5VdHqLk%2B3AKtL90sivVBDrMXb4oTjufT4yqjexrQ7K%2BovhAAEA4f%2FuCjTSQOrMI%2FHx1pA7UFqueRgGtem%2BG%2FdXOMb0d1ygoSPbY1%2B7kdmbsqaExpFxsKac1r60dSzi7S5BkSZkMstBNptWnoEYZXFhbiBcfrT7ugN84a%2FN5a2rya3N%2B0jd2qN5U%2BTqdG%2BZgAUhDcnr%2Bp2qBcwpJGuNR27QAH3UpnLN%2FnV2Hkqj7Zs1txneL4J854SY22F2YgiNMKc3vpaZIkDPLdVsVjgRqV%2BXx7N8jDbFWP3QkVMFXd81785MFIBMe6%2BdNG8kL0RcNw1DI1fL0L3Zt%2BlLY2boR4%2BbR0NL752JC7pcNa8PYoFntwDxE21GTEfWC85ID4v5wwa3gONUbslgo3dJJ7SQwX3LIOOutJuQXRQMK2OnL0GOqUBfn7fqEDfy2CAmQ%2BmFn%2FRM7ovguV%2BTayOgZ511kn4LyDBJFIoS%2BLMx4s7ClJH89uXZgpl8%2BMhl02iBaRX6KX%2BSicbjBO3WlYPnkmQKJafb3huKQqZ2LlLu0C6978EtdttDUYouL1AyWe2xa8Ils3C8cJzwHWyN0DuHxo45jtn4F7UAOjkq7E2Sjhp7MEiNbrmBoyOl8o4L69MnWPioD6OtQcs8gER&X-Amz-Signature=c35e62300324524084d6426c5eda444caae8d3b7ed9b2e70afb744feb64af4ba&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23a79b9d-2356-49a9-8fd9-65c6b0ab2cc5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665IAZ6ULZ%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T101402Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHAaCXVzLXdlc3QtMiJIMEYCIQDpsjtdmNnOAIm8YD0s%2FrNX3t%2FYfFI4hIo2OzNNUPygowIhAJdZHVg0AvRA2Z6t2dVAcofiMHWhmp6jD9yxV0W5ybLcKogECIn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzsP7gmWIHpveq%2B6zcq3AMHS7TigjBY742cQXtgiwGJVRQ%2Fxj%2F4sc02gF9ARLnG5pmmmThEJ9RNhb1nki%2BgO9%2BNoEnLYbe6Ps64oYiwJb%2FzVsU4nLi8MmrCmemT61pdyj5R8SsTS3i5AFj7wf2jHz7wsPDBFhvaV2IgV8VGETCSrm7GFG1pRUiIstDyt8BePGAaBWkdGlIyFxqfmudt7Iecw2iWhzz%2FFn%2FCc3EH7NEyK%2FbaM4afyO9LcvmmedAlys6w6icivvpgPi9hoN9EJl2wyoj3uxjVbAYGSLPt9qtUMNQuqqyTSJHJRNxnyqbi20mvc8Pd7Lzxt0hHNR%2FiM9ZHefTZOv8mKklOoJLSXA7zFhJVVzsKE6rmxfNvCdY74GG%2BRdgTZ28gDqdOIoD8Dla%2Brscba0dXD2gU5L4RzAD6KPIg6FZBSF4ixZKQRB5rKb4hWjztWRdgFc4EU1QEHcJfl%2FhnG37vLvv7fFIRR%2BZ%2BLyvDaqdYYDUtzgl09crfCoJOe5reVgjWsGBTlktXiE61JyYBMcKSy08pMOnrkKBQi0QNS3kl6OZZ51zLRnykbZRCWMNhGC62%2BOLCA%2BeOvGp6G139UsGjkZaSqqmWH%2BLqwbzRaz7XO%2BO7CLPgI7xmBp3YdPGw8vWPFAkWnzDDjpy9BjqkAaV9duKsCoDcTXB4cwCdwlWYq7WGdBAmfaTeCKwBcNFv7wOOqucvQWc68kmSqYnAGY8DivZHqbrJlQZANT%2FWcqFWBWxtx8b211FRxzS47IWuS7wXcL1gxCH9guDrsVdw1GUkM86K%2Fd97bXJRTT0bmvX3WpoU4vQ66%2B6YllbrAlaWLjO3qOKusqKEF4juzIy5zDaWA5wyWeaTZx7YB6XNSlUtLx%2BP&X-Amz-Signature=eaa5c24538a07568c27ae8172ac82f0ba4f6a1a970ccb9c3de188f46042254cf&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 4. KDE Plot
A Kernel Density Estimate (KDE) plot is a graph that creates a probability distribution curve for the data based upon its likelihood of occurrence on a specific value. This is created for a single vector of information.
**Syntax:**
```python
sns.kdeplot(X) || sns.kdeplot(df['age'])
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0d571213-2a2f-4921-a50b-880847aa05ee/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665IAZ6ULZ%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T101402Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHAaCXVzLXdlc3QtMiJIMEYCIQDpsjtdmNnOAIm8YD0s%2FrNX3t%2FYfFI4hIo2OzNNUPygowIhAJdZHVg0AvRA2Z6t2dVAcofiMHWhmp6jD9yxV0W5ybLcKogECIn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzsP7gmWIHpveq%2B6zcq3AMHS7TigjBY742cQXtgiwGJVRQ%2Fxj%2F4sc02gF9ARLnG5pmmmThEJ9RNhb1nki%2BgO9%2BNoEnLYbe6Ps64oYiwJb%2FzVsU4nLi8MmrCmemT61pdyj5R8SsTS3i5AFj7wf2jHz7wsPDBFhvaV2IgV8VGETCSrm7GFG1pRUiIstDyt8BePGAaBWkdGlIyFxqfmudt7Iecw2iWhzz%2FFn%2FCc3EH7NEyK%2FbaM4afyO9LcvmmedAlys6w6icivvpgPi9hoN9EJl2wyoj3uxjVbAYGSLPt9qtUMNQuqqyTSJHJRNxnyqbi20mvc8Pd7Lzxt0hHNR%2FiM9ZHefTZOv8mKklOoJLSXA7zFhJVVzsKE6rmxfNvCdY74GG%2BRdgTZ28gDqdOIoD8Dla%2Brscba0dXD2gU5L4RzAD6KPIg6FZBSF4ixZKQRB5rKb4hWjztWRdgFc4EU1QEHcJfl%2FhnG37vLvv7fFIRR%2BZ%2BLyvDaqdYYDUtzgl09crfCoJOe5reVgjWsGBTlktXiE61JyYBMcKSy08pMOnrkKBQi0QNS3kl6OZZ51zLRnykbZRCWMNhGC62%2BOLCA%2BeOvGp6G139UsGjkZaSqqmWH%2BLqwbzRaz7XO%2BO7CLPgI7xmBp3YdPGw8vWPFAkWnzDDjpy9BjqkAaV9duKsCoDcTXB4cwCdwlWYq7WGdBAmfaTeCKwBcNFv7wOOqucvQWc68kmSqYnAGY8DivZHqbrJlQZANT%2FWcqFWBWxtx8b211FRxzS47IWuS7wXcL1gxCH9guDrsVdw1GUkM86K%2Fd97bXJRTT0bmvX3WpoU4vQ66%2B6YllbrAlaWLjO3qOKusqKEF4juzIy5zDaWA5wyWeaTZx7YB6XNSlUtLx%2BP&X-Amz-Signature=65e854bf5ab3b37651731efdfd658d5a7ec829319e58ee8ba2faefcf92310f62&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/53752550-ef82-4ca9-a01a-09921f0282d0/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665IAZ6ULZ%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T101402Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHAaCXVzLXdlc3QtMiJIMEYCIQDpsjtdmNnOAIm8YD0s%2FrNX3t%2FYfFI4hIo2OzNNUPygowIhAJdZHVg0AvRA2Z6t2dVAcofiMHWhmp6jD9yxV0W5ybLcKogECIn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzsP7gmWIHpveq%2B6zcq3AMHS7TigjBY742cQXtgiwGJVRQ%2Fxj%2F4sc02gF9ARLnG5pmmmThEJ9RNhb1nki%2BgO9%2BNoEnLYbe6Ps64oYiwJb%2FzVsU4nLi8MmrCmemT61pdyj5R8SsTS3i5AFj7wf2jHz7wsPDBFhvaV2IgV8VGETCSrm7GFG1pRUiIstDyt8BePGAaBWkdGlIyFxqfmudt7Iecw2iWhzz%2FFn%2FCc3EH7NEyK%2FbaM4afyO9LcvmmedAlys6w6icivvpgPi9hoN9EJl2wyoj3uxjVbAYGSLPt9qtUMNQuqqyTSJHJRNxnyqbi20mvc8Pd7Lzxt0hHNR%2FiM9ZHefTZOv8mKklOoJLSXA7zFhJVVzsKE6rmxfNvCdY74GG%2BRdgTZ28gDqdOIoD8Dla%2Brscba0dXD2gU5L4RzAD6KPIg6FZBSF4ixZKQRB5rKb4hWjztWRdgFc4EU1QEHcJfl%2FhnG37vLvv7fFIRR%2BZ%2BLyvDaqdYYDUtzgl09crfCoJOe5reVgjWsGBTlktXiE61JyYBMcKSy08pMOnrkKBQi0QNS3kl6OZZ51zLRnykbZRCWMNhGC62%2BOLCA%2BeOvGp6G139UsGjkZaSqqmWH%2BLqwbzRaz7XO%2BO7CLPgI7xmBp3YdPGw8vWPFAkWnzDDjpy9BjqkAaV9duKsCoDcTXB4cwCdwlWYq7WGdBAmfaTeCKwBcNFv7wOOqucvQWc68kmSqYnAGY8DivZHqbrJlQZANT%2FWcqFWBWxtx8b211FRxzS47IWuS7wXcL1gxCH9guDrsVdw1GUkM86K%2Fd97bXJRTT0bmvX3WpoU4vQ66%2B6YllbrAlaWLjO3qOKusqKEF4juzIy5zDaWA5wyWeaTZx7YB6XNSlUtLx%2BP&X-Amz-Signature=45fa116a2c84891b8f9235e85f858901a7123725db93780fea139261b5ef4017&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
## 4. Correlation Between Variables
Correlation is a statistical measure of the extent to which different variables are interdependent. It indicates how changes in one variable are associated with changes in another variable over time.
### Positive Correlation
Positive correlation indicates that as one variable increases, the other variable also tends to increase.
**Example: Engine Size and Price**
- **Positive Correlation:** Engine size increases, price also increases.
- **Visualization:** Scatter plot with a steep positive slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c7ea9b0-3ef3-4357-a9c3-554fc71b6b15/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666WHRVAI2%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T101403Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHAaCXVzLXdlc3QtMiJGMEQCIGctMdAmJ8dVWGORheOEFV%2FwaYetBJEdruubbzV%2BuZrJAiAthrWGmIhGoa4CdndUoV5LWignPix9lSmLGY8uHgBdTyqIBAiJ%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMUvs0XO04Wdjho6x1KtwDbSM8v3oIM6IwXlmEJQsaDz3Ub9%2BxoSSGpocRy735Kien%2Be7%2FfiZAudDRUkozIvCYL1%2B%2FfM4Py5o60S9GEfP4u68OQjrb737XSkjRi%2BYVSnGanKPyLi8lDou0CvB0O4qyTifDoc9HWDcnfVLe9r46CuFD9LxB%2FZwuhXJihfuyurBQC6yIpGyp07OwMKC9e78riZsNxPLcByUXmM%2B9naXjjJwtXPVO2WK02PQTMIk6CsYad0Ab%2FiLyssx11hyq%2BKxsM0D05%2FeyZiA%2F%2FTNHhTmSWAiJZwADp2HuO%2FvEQ0YfkAGGs%2FdcP99a9JY0dFyK8jr%2BfmyRSpSD%2BNimyCPgq1N0d%2FU8QjlCMpuhn6xpyc7Tk0WxqgB1HEAJ1FAx6cZmFPFv0qzQNkFXq%2FWbrTdc2cZuGkfoUf30%2Bo7FwSi%2BYLb67XqOjbXUnarUHaRTx%2FTbuiXp7J505zjEqRirv6nOpu3jd%2Bg5e8%2F9IlweDomtcBlwPl5y0MrJD4Ff3kF0cIxFYEBeW3L8X%2BoIlxzEvwzCibraFAEaR9OpvE6%2Bb%2F%2BKP%2Fqh%2Fq3sUxOrnOWCsGazNNV40pidrNQvCqWQ0wFxy%2BaB8W%2BpiG9Jvrs04ayrslHCKpSzQCv5n3Pg1uMC%2B1NVASswyI6cvQY6pgH3f2FqpaexybrIHXiJQmBiG24T0su0QE0jgWz4bVDDEsP878JcEnIr2k0u3QuNrYiYM31pGT2gTtnyUnFXwjyCLhx6UQI9j0f%2F1dUoVoBJ1Uu%2Fy%2BG2cNuPOk7su98PhtvMzaO6QbU477jUF49NSat86F%2B0D4xh%2FkujddhMHY2Sc5b%2FynQCcwkPmwbz1RW4PRqq1RlW9W0DErq%2BrrYdIdw53Bwq6GCV&X-Amz-Signature=6efe08b1297766caae09fec68a0cd3518639a5824afdda2c618864dac3bf6d1e&X-Amz-SignedHeaders=host&x-id=GetObject)
**Explanation:** When engine size increases, there is a corresponding increase in the price of the vehicle. This positive correlation suggests that larger engines tend to be associated with higher prices in the market.
___
### Negative Correlation
Negative correlation indicates that as one variable increases, the other variable tends to decrease.
**Example: Highway Miles per Gallon and Price**
- **Negative Correlation:** As highway miles per gallon increases, price decreases.
- **Visualization:** Scatter plot with a steep negative slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/10f1f798-9cc4-4df2-a9c1-5a339f554a0b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ULR2ZPDC%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T101403Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHAaCXVzLXdlc3QtMiJGMEQCIGNT5k1w9ZJ1nvFSrhSNnqAY93hXjx9SPjeCWNCwCtFdAiBd7r3856uLi7i6GF3G4tgKkGZRehOiSkh7ghbnXc76eSqIBAiJ%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMKuxyJLjaPn%2FyLT9yKtwDymkHlYl%2Fmr1jxdR9G9T06LMgeWXs5IchM1T2JGEMHWhcx83mgaJ09GpXW%2FWgL%2Bw2NOzh1H%2FuBBf%2Ba8OBNarjPyCJ6ZZwvaidlScnrtDLBY79bJdIWhTI1NMjGOe7y8EmUk4aFRwCYdLKiA12lJN7OBAMciIBkg%2FlBwHlyrdSm6Pz7Ky5IxMxhKEwBm94I29RtZ7ECpxxXi89bZ2%2FYOcXou5nQbS3WizXKfL3lj0bqnMSFAfONgeiysUBBUXiRtN7piz8EhFkItz1SN2MBWA9%2B05JQ%2BUhSd9WpnMmEeSbHTf1hfR5ADtDPVgv%2Fi7Jj6uVYo2TolEI3KGWOvcvWAONZH3wqPwmt9YREQn8jQgDkIg%2Bg%2FIbI%2FB8QVJzizqhMAyNHPbqzf1QnB7JXfYCpTfZLVAxnDFnm%2B7ukq73uGovZTNFOJ%2FX2lrqWAMMMJRf%2FPEINbU5ArGAMmqC9icIMMXrsYdO9%2FF3DUTUaXQtAp4aEM8q%2B%2FrRbvLaBCP8ClWzU%2F7XCnhwyFO7O9Aq2fCf%2FScDmaodvMQ2W8XhZSVjFS%2FSEeCxf79YhULoDhjBEW%2BY9Z47KKnTG1UfXDspIidLhll4rs3HjmQ9vzVDMR3eL7xNDMUDv43uXE8C9xJojjowh46cvQY6pgGZtfc%2BR29MizAaGkf4TTUTeVKayvt2LZmuR8eU55lEWtAXNpwYHtQTRxRfcGFQch0gsMwhWnFrtpy1UCSRFdA0fQv0oAzKTqGtwvfOhhbbXT4ScnX2nVJ%2FH8wjr7zfslYDYbdgxznSy1rCdOYrtJQvmZ7hrf3Sbs0WPsc0LucFoq2%2BQJKFlPKC48Krc4KtYb3yUrEM0tqnKksRqpZy7Eh%2BcGOD1Yvo&X-Amz-Signature=eba0997d224c0b1a3e80cd41ba5f38486f51b7b088de21d607d2525604a451df&X-Amz-SignedHeaders=host&x-id=GetObject)
**Explanation:** When highway miles per gallon increases, the price of the vehicle tends to decrease. This negative correlation suggests that cars with higher fuel efficiency (more miles per gallon) are generally priced lower in the market.
___
### Weak Correlation
Weak correlation indicates a lack of strong relationship between the variables.
**Example: RPM and Price**
- **Weak Correlation:** Low and high RPM values show varied prices, indicating no strong predictive relationship.
- **Visualization:** Scatter plot with no clear trend or slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9f914514-8914-4bf4-ac84-d9e3077f6eb1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46647CLSF7U%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T101403Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHAaCXVzLXdlc3QtMiJGMEQCIG1FlOQ0tkr8GxJ552reJ6gz%2FMZmw5G5ZEa24VL0l1bRAiA63nrS7d64VB7CQkKaRHJ7Bxi3Pl5O9DoJDDZTVP%2BT7CqIBAiJ%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMftDxH6e%2FxZmTXJgNKtwDf1XxmbdbDzUuISwsXcYp4I4oXjNCjmyzlTZsWDzJXy7xepToKjPKwcMQuP1KxnChCRMWY3cUE2MtJQByL%2FruZhwyRd%2FTwiuTklZ1b366w8mlVpjNrIkzRIwBalCabJdSRZS8zmBHIs8ivrnThReBCsfxtnodWyeGfEvEcjSAsGKaB2mJ92%2BRpiqMT2dd4P7vWqYJYV0pf10I5cx6pCkE%2Fosx39Zee2nkol%2FBc1GYcd9Ftri%2BXWZowOypyRVNj%2BouoF9XxZA3ezfjv%2F0NNmLDoeiGbyTNSRgmmiqwgCcM1Ib02G0qYUZO4BYstel3UJ8d09xAs%2FoiD6dVESKMDM94EWWz3U%2Bzp04UPcFULSga21MGz005Krlc2fDrGYvTBo8BunBAkp3v3MdLkzvOi8wjGCr9XXSFDAKDBnWlV5PzUDwHIBL6PkfGZ%2Be15uIaw0xZr3Z%2FBZWV2RGYtVuVYdSjCFf1nGi1z3VRdMUcfieBrO1TsVDTx6932%2FdzWLmDsTMDkngmcvF%2FB2vPeEXxZ9ZxU3l9RBTaa8lQLUdc%2Fh8ntH8rUGBtCwe8UuHDJZ8Q5dS1hv7wk1f6MvXkp6K5xYaX%2BcpKp7rL5fm%2Ff9%2BQ5F6x7ipHlyE9%2Bld5E7TI7pMwq46cvQY6pgHx5lYm21hX6VJuEhIaYzbJnVetKiEaOUvIhfHXz5m2hk6rOuKRgutFtCdW3MVrrYiWj7HW4icZy5uVwo7K%2BqBwDpp0SOaMNfX%2F2zYq2XVNKoM8vc23pAywsKnpXL521D0iJkpEKEOlDBgu7tjbU%2FNufzDzQcYfttQUEKglg1tjYxms7tTMuAingOFTZFYfK1bCYpr2K3x%2FNA%2BMgD77fSdgOElS0eQE&X-Amz-Signature=19c5acae80eee84afc3ab40af334d03e49d30d278fe51598a97eef5226d2ccae&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f18086e5-5b04-4fbf-8309-8944ab20d213/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666YOKCKDQ%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T101402Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHAaCXVzLXdlc3QtMiJHMEUCIQDO0iFXxb1bmNSMfZ%2BNrOKMorPslR%2FxGH6VtLL5RCp6gAIgI8SE%2Fq%2Fz9btIlfyl70teNL%2BmI1p1SD97zkf6Ur0so48qiAQIiP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDEESjNJq0PKeAc1riircA6ew2sc9j5R0wL1Z5vYdXKp9iZC7eg%2B4t%2FboI3mDeF3GNYpKZNPnh5w%2BA1fvxqRHJyIrQLMYIxpPkRu65UOH7gX4dDVH5oi1rpwM55wvLAKQzJ2QA1GxqxoRBpXFPhlfbbwTDqhtPpTAADr8aqiFXXeTq0YWDS5hc7hXXe1T5eHR%2FnrfGgTtbk2IgFpxVkcxg0Q2IkQ29O0AWCA3JCw5JrhxE2gb1Kd88AAQ5JJ3VaPa2p45v8KbE9vUfoe4%2BCP7HlY93vfLOv840GU%2BgpYw6YczNgaY%2BXJBw0y17wcEG%2B%2FuzVyiiodbTKSFOviVrDFlAl%2BlJKUN1uD%2FE3TcxJfbcBt6BVgKzP783Rx0WGzetuXWmpAQs%2Fwrsv3HNrtPzHsliLmiqtN3BLJPE6p9jzfzBQi62J7zLRqO5tYoOyRe7t%2FGhC4%2BPJTw7vzoaSAt%2FVrZkEYEDc9e8HaBppv9H5TPgQSqHTOCFxu111Tnn5519c9PFeMXeVotSmr9eIRW7dXldioKgO%2BCzD0GQwiMF6svM0u00%2FL2Oyj8aLfuFwKTUl4JqwDgZa3Fhhj%2FLXIfUmXJTLZd2CVqNhnhtECQfgNFBPBmjioRYDDYJS5vPtcBS8nWrG3DoYiC%2Frqn%2F8vZMImOnL0GOqUBJ0cVVt6S7zFHWc1KJGlQjyskTAQrrgauCgAuL1tsekyjIDW6CdvSXSHRaRGDY3jqlqVYQZt3qRYeP4f5fRrXX1b6FzAK%2FWJvQjJiNlJ7jpc7gAuvG6XhKYhiLh9DYBXuPlBeELajuEL1WSy1x%2BXoTI%2BOxLTQbtIWZ2Z%2B%2B4zA7DD9ZsHE8rjcCQBL1k1SPz5%2BPXx7GkreBFmrD4wQhvseEiQOl5hZ&X-Amz-Signature=01672dd713e936b6880d38f4b895f031931d4f76f84feceb3caa5f50d3beab33&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Correlation Plot
Heatmap visualizes correlations among variables. Color scheme indicates Pearson correlation coefficients. Dark red diagonal line shows perfect correlation (value of 1) between variables and themselves.
This heatmap offers overview of variable relationships and their link with price.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cd3b341e-cc1a-45f7-8aec-cdc00436d270/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666YOKCKDQ%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T101402Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHAaCXVzLXdlc3QtMiJHMEUCIQDO0iFXxb1bmNSMfZ%2BNrOKMorPslR%2FxGH6VtLL5RCp6gAIgI8SE%2Fq%2Fz9btIlfyl70teNL%2BmI1p1SD97zkf6Ur0so48qiAQIiP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDEESjNJq0PKeAc1riircA6ew2sc9j5R0wL1Z5vYdXKp9iZC7eg%2B4t%2FboI3mDeF3GNYpKZNPnh5w%2BA1fvxqRHJyIrQLMYIxpPkRu65UOH7gX4dDVH5oi1rpwM55wvLAKQzJ2QA1GxqxoRBpXFPhlfbbwTDqhtPpTAADr8aqiFXXeTq0YWDS5hc7hXXe1T5eHR%2FnrfGgTtbk2IgFpxVkcxg0Q2IkQ29O0AWCA3JCw5JrhxE2gb1Kd88AAQ5JJ3VaPa2p45v8KbE9vUfoe4%2BCP7HlY93vfLOv840GU%2BgpYw6YczNgaY%2BXJBw0y17wcEG%2B%2FuzVyiiodbTKSFOviVrDFlAl%2BlJKUN1uD%2FE3TcxJfbcBt6BVgKzP783Rx0WGzetuXWmpAQs%2Fwrsv3HNrtPzHsliLmiqtN3BLJPE6p9jzfzBQi62J7zLRqO5tYoOyRe7t%2FGhC4%2BPJTw7vzoaSAt%2FVrZkEYEDc9e8HaBppv9H5TPgQSqHTOCFxu111Tnn5519c9PFeMXeVotSmr9eIRW7dXldioKgO%2BCzD0GQwiMF6svM0u00%2FL2Oyj8aLfuFwKTUl4JqwDgZa3Fhhj%2FLXIfUmXJTLZd2CVqNhnhtECQfgNFBPBmjioRYDDYJS5vPtcBS8nWrG3DoYiC%2Frqn%2F8vZMImOnL0GOqUBJ0cVVt6S7zFHWc1KJGlQjyskTAQrrgauCgAuL1tsekyjIDW6CdvSXSHRaRGDY3jqlqVYQZt3qRYeP4f5fRrXX1b6FzAK%2FWJvQjJiNlJ7jpc7gAuvG6XhKYhiLh9DYBXuPlBeELajuEL1WSy1x%2BXoTI%2BOxLTQbtIWZ2Z%2B%2B4zA7DD9ZsHE8rjcCQBL1k1SPz5%2BPXx7GkreBFmrD4wQhvseEiQOl5hZ&X-Amz-Signature=d4d2b431df66c8a61893f06116c811b3919df6ef6e46eca30f0c5d604b430281&X-Amz-SignedHeaders=host&x-id=GetObject)

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
