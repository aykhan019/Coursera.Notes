

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7e6d594d-952e-44b6-97ea-31225882aea6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666DBEJ4DW%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T091517Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDiBe5VxKjQR2EBT%2F2uNyHO%2FMUOqsCh7LCDC4Ta%2FfsBOgIhANOKfw4c0EmfJLWY%2Br3oY3PYUOY24c%2Bk%2BOoQh%2BegLW1TKogECIn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxJkqxc3gnomX8wTdIq3APTnTlbZ7R18A5QOCmsIMUGdzBieZXNbhbKvHUkiYv53mSv2aMY%2BgIdlZnZWwZKVyocP5PqV4Z%2BQ2QCaGX99VxIRWoBjVe8f%2BE6zZchwa6HM4G4Uh5OC9PAFWdC413OQ0VYT9UcfhtcQNop1spK5lUa%2Bo%2F0uhSAbXEYPIo%2B%2FBqdooHl%2FQAtwq4ZDmbEIyiuklDQ%2FKOzHtomEBA%2FzmBSPW2JnkbneJHyTmqehriHKbhpzrUonrvT8k9%2FxDAOZX4ddgEqS9%2Fbj4dCwxQF2wzgNQblZ0qMrkj2tVpUATZiN3bh%2FR7wiGox69vxmX2Mat4T2eIQLoGj%2Fts0DpP%2FVNyCczAxXHyEjkF3IY7pUYsYQtR%2FBDerUmFIwtPH%2B7QFDQ0esClmLnkINIMdY2uaPQl5CYfn%2FU4iH9rzA9KkfVzD9IuGaPaCFuQlihbN4Hv2rcMpjz%2FdH1Y1HAb8z6S9aR4WzzCsqA7yInOls%2FNS%2FiYtoIXlS1uqjtAX4fwQ8z8zi0yUYkN2liBUT9Zb%2BVvwAowqK%2FOE9KCpP3n8j4mlq13xz0yNOwpc3lwCPy769pPFtJLJTpP2CBpYOycha9dzkKpqrgHY0gwZEV8ip%2Fr%2BJDXWhORRcUQhnSRMucKs8V2%2FCTDkyOe8BjqkAbePRcTl%2BZbiHmz6a3TMOKffW98fGzp9DpXwIVBh50iIhKzfnBO%2BQtlA%2FPUYDFcVftnEVkjdeiZo65iXRwnr57wRAQzuhMLsrqYerMUWJO3CAdX0%2F0n5o%2BOhG23wYFb%2FrOkfEoA%2BIWmnYXXuHxsSuZOiGSMUHXEGAtzKnCQzFjWn8qgTP1Jcz5fGxh3RLGMTtRr%2FVGaNNNzWHO6v8GOuGpknhYcR&X-Amz-Signature=2f2e11623c22c5932a8256fc8ce27945614be76529f7f867036a597b05ab0786&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cbfaed9e-b398-4902-8936-dea058b21def/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666DBEJ4DW%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T091517Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDiBe5VxKjQR2EBT%2F2uNyHO%2FMUOqsCh7LCDC4Ta%2FfsBOgIhANOKfw4c0EmfJLWY%2Br3oY3PYUOY24c%2Bk%2BOoQh%2BegLW1TKogECIn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxJkqxc3gnomX8wTdIq3APTnTlbZ7R18A5QOCmsIMUGdzBieZXNbhbKvHUkiYv53mSv2aMY%2BgIdlZnZWwZKVyocP5PqV4Z%2BQ2QCaGX99VxIRWoBjVe8f%2BE6zZchwa6HM4G4Uh5OC9PAFWdC413OQ0VYT9UcfhtcQNop1spK5lUa%2Bo%2F0uhSAbXEYPIo%2B%2FBqdooHl%2FQAtwq4ZDmbEIyiuklDQ%2FKOzHtomEBA%2FzmBSPW2JnkbneJHyTmqehriHKbhpzrUonrvT8k9%2FxDAOZX4ddgEqS9%2Fbj4dCwxQF2wzgNQblZ0qMrkj2tVpUATZiN3bh%2FR7wiGox69vxmX2Mat4T2eIQLoGj%2Fts0DpP%2FVNyCczAxXHyEjkF3IY7pUYsYQtR%2FBDerUmFIwtPH%2B7QFDQ0esClmLnkINIMdY2uaPQl5CYfn%2FU4iH9rzA9KkfVzD9IuGaPaCFuQlihbN4Hv2rcMpjz%2FdH1Y1HAb8z6S9aR4WzzCsqA7yInOls%2FNS%2FiYtoIXlS1uqjtAX4fwQ8z8zi0yUYkN2liBUT9Zb%2BVvwAowqK%2FOE9KCpP3n8j4mlq13xz0yNOwpc3lwCPy769pPFtJLJTpP2CBpYOycha9dzkKpqrgHY0gwZEV8ip%2Fr%2BJDXWhORRcUQhnSRMucKs8V2%2FCTDkyOe8BjqkAbePRcTl%2BZbiHmz6a3TMOKffW98fGzp9DpXwIVBh50iIhKzfnBO%2BQtlA%2FPUYDFcVftnEVkjdeiZo65iXRwnr57wRAQzuhMLsrqYerMUWJO3CAdX0%2F0n5o%2BOhG23wYFb%2FrOkfEoA%2BIWmnYXXuHxsSuZOiGSMUHXEGAtzKnCQzFjWn8qgTP1Jcz5fGxh3RLGMTtRr%2FVGaNNNzWHO6v8GOuGpknhYcR&X-Amz-Signature=ec67a9a8baf5f48c8e4b1f0703ce9ba2dd32dafb3007916abaf9cd53562cead7&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/91181646-b1e0-4433-9711-6259a96a9247/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666DBEJ4DW%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T091517Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDiBe5VxKjQR2EBT%2F2uNyHO%2FMUOqsCh7LCDC4Ta%2FfsBOgIhANOKfw4c0EmfJLWY%2Br3oY3PYUOY24c%2Bk%2BOoQh%2BegLW1TKogECIn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxJkqxc3gnomX8wTdIq3APTnTlbZ7R18A5QOCmsIMUGdzBieZXNbhbKvHUkiYv53mSv2aMY%2BgIdlZnZWwZKVyocP5PqV4Z%2BQ2QCaGX99VxIRWoBjVe8f%2BE6zZchwa6HM4G4Uh5OC9PAFWdC413OQ0VYT9UcfhtcQNop1spK5lUa%2Bo%2F0uhSAbXEYPIo%2B%2FBqdooHl%2FQAtwq4ZDmbEIyiuklDQ%2FKOzHtomEBA%2FzmBSPW2JnkbneJHyTmqehriHKbhpzrUonrvT8k9%2FxDAOZX4ddgEqS9%2Fbj4dCwxQF2wzgNQblZ0qMrkj2tVpUATZiN3bh%2FR7wiGox69vxmX2Mat4T2eIQLoGj%2Fts0DpP%2FVNyCczAxXHyEjkF3IY7pUYsYQtR%2FBDerUmFIwtPH%2B7QFDQ0esClmLnkINIMdY2uaPQl5CYfn%2FU4iH9rzA9KkfVzD9IuGaPaCFuQlihbN4Hv2rcMpjz%2FdH1Y1HAb8z6S9aR4WzzCsqA7yInOls%2FNS%2FiYtoIXlS1uqjtAX4fwQ8z8zi0yUYkN2liBUT9Zb%2BVvwAowqK%2FOE9KCpP3n8j4mlq13xz0yNOwpc3lwCPy769pPFtJLJTpP2CBpYOycha9dzkKpqrgHY0gwZEV8ip%2Fr%2BJDXWhORRcUQhnSRMucKs8V2%2FCTDkyOe8BjqkAbePRcTl%2BZbiHmz6a3TMOKffW98fGzp9DpXwIVBh50iIhKzfnBO%2BQtlA%2FPUYDFcVftnEVkjdeiZo65iXRwnr57wRAQzuhMLsrqYerMUWJO3CAdX0%2F0n5o%2BOhG23wYFb%2FrOkfEoA%2BIWmnYXXuHxsSuZOiGSMUHXEGAtzKnCQzFjWn8qgTP1Jcz5fGxh3RLGMTtRr%2FVGaNNNzWHO6v8GOuGpknhYcR&X-Amz-Signature=82013c6776493c0ce4cfa47565700fde0497451af499bb105fb2443b886acb10&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/09aba1c0-0d55-41dd-852a-a04c5b8a3fac/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46622FW363A%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T091519Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEID%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDebFYHAX%2FtVZ3hxrFGIlOgrRa9ZLv3g6x2uFQd2QLCVAIhAI0zRIrjelX8WjwfIPGnJ%2FCyUhpcc5Ppx8v00kobExUwKogECIn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgySSPaR1%2BAwfTPNPvEq3AMCqC9nWD62Fqu5%2BTZHug3E86zGBFynaTHjuQRShA9AldplJwxMpjZuPFbBKrEGE4MYps0HVPlI1lVEdqCLFdeRbOBUr%2B6azEvjp2UkXCGiR8MdD71BLCmYbNzBhTt%2BaLZbQRjC%2Bkfj%2FVzerShGXsyw0Om%2Ftkecuw0R0AmPWEorExoIpcM40AAXAdAwAXgnMUA9U20UIzjDHqu15AN8h8B2rvGVLmheUpV%2FqI4AFglidtBt8tbjVZOomXFoJEyELGyJKz40uZAJLiMzbNsIOAMowLxL6c8ubUIw5qM8sPI1VSyxuJ%2FlsVSgJJ86BnSY8TTDwdjviK%2FTA%2Fi1YAWTaO98sa8%2BxZy9j9p6NWnkHXHEyypfvQNkZjBL9cwyZVYyjK%2Fp85AQufM9jyVAUjvVuHNAnl9OtJSD9CFV2673DeCXccTZ5i8iaDa32Tqwq1HsGPSp9QeZy7hvL8yoscyZqCmtL%2F59IR8KdAUNAHX6o27ixDQPHEYpjMh4yN5aDPR12wFY5465KhXcy5AiMdkw22qyceeWudwlWbxX%2FhLu3bmPGPNY1lKQHC7iaEB6eMKFizan0eSdQh7bxcgG%2B5rsoGmWJzuVkH9ypDWWf4Mn7VezrLNWWt1I%2F8Bd1YL5KjD2x%2Be8BjqkAY%2FiEFv8XV5PSD43tmjn%2Be6MTC7nQ48JyRyn2q2gIGWFTf2jeEIIQc2SLFhEJlgHnPADQFKjZocDRyp9fHLZqsh8XHXSgk2tGZaWmsBrGVRyYA0lE3W5MgH00ku0XkSSYvaRLKQcQbF3nYleuHexg9SkWIJSIllN5SjoN5gaNrss3tKKdYHSbW9PNrMbhxMn8hvccLckT%2BctkjRhgwqGJr3%2BpLg2&X-Amz-Signature=88269e079acd2453a6f83a5273ebb3688553e49ac00cd6a94fab647a8809c9b4&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 2. Scatter Plot
Scatter plots present the relationship between two variables in a dataset. It represents data points on a two-dimensional plane. The independent variable or attribute is plotted on the X-axis, while the dependent variable is plotted on the Y-axis.
**Syntax:**
```python
plt.scatter(x, y)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23708af9-659f-4f23-b626-1a4292d7842c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46622FW363A%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T091519Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEID%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDebFYHAX%2FtVZ3hxrFGIlOgrRa9ZLv3g6x2uFQd2QLCVAIhAI0zRIrjelX8WjwfIPGnJ%2FCyUhpcc5Ppx8v00kobExUwKogECIn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgySSPaR1%2BAwfTPNPvEq3AMCqC9nWD62Fqu5%2BTZHug3E86zGBFynaTHjuQRShA9AldplJwxMpjZuPFbBKrEGE4MYps0HVPlI1lVEdqCLFdeRbOBUr%2B6azEvjp2UkXCGiR8MdD71BLCmYbNzBhTt%2BaLZbQRjC%2Bkfj%2FVzerShGXsyw0Om%2Ftkecuw0R0AmPWEorExoIpcM40AAXAdAwAXgnMUA9U20UIzjDHqu15AN8h8B2rvGVLmheUpV%2FqI4AFglidtBt8tbjVZOomXFoJEyELGyJKz40uZAJLiMzbNsIOAMowLxL6c8ubUIw5qM8sPI1VSyxuJ%2FlsVSgJJ86BnSY8TTDwdjviK%2FTA%2Fi1YAWTaO98sa8%2BxZy9j9p6NWnkHXHEyypfvQNkZjBL9cwyZVYyjK%2Fp85AQufM9jyVAUjvVuHNAnl9OtJSD9CFV2673DeCXccTZ5i8iaDa32Tqwq1HsGPSp9QeZy7hvL8yoscyZqCmtL%2F59IR8KdAUNAHX6o27ixDQPHEYpjMh4yN5aDPR12wFY5465KhXcy5AiMdkw22qyceeWudwlWbxX%2FhLu3bmPGPNY1lKQHC7iaEB6eMKFizan0eSdQh7bxcgG%2B5rsoGmWJzuVkH9ypDWWf4Mn7VezrLNWWt1I%2F8Bd1YL5KjD2x%2Be8BjqkAY%2FiEFv8XV5PSD43tmjn%2Be6MTC7nQ48JyRyn2q2gIGWFTf2jeEIIQc2SLFhEJlgHnPADQFKjZocDRyp9fHLZqsh8XHXSgk2tGZaWmsBrGVRyYA0lE3W5MgH00ku0XkSSYvaRLKQcQbF3nYleuHexg9SkWIJSIllN5SjoN5gaNrss3tKKdYHSbW9PNrMbhxMn8hvccLckT%2BctkjRhgwqGJr3%2BpLg2&X-Amz-Signature=01062b997164998aaef68c9eda878bb18401452faf1579f534a9ce2c9762ef6d&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 3. Histogram
A histogram is an important visual representation of data in categorical form. To view the data in a "Binned" form, use the histogram plot with a number of bins required or with the data points that mark the bin edges. The x-axis represents the data bins, and the y-axis represents the number of elements in each bin.
**Syntax:**
```python
plt.hist(x, bins)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/24e4424a-df87-40a1-b63b-195cbdc2e0ab/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46622FW363A%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T091519Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEID%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDebFYHAX%2FtVZ3hxrFGIlOgrRa9ZLv3g6x2uFQd2QLCVAIhAI0zRIrjelX8WjwfIPGnJ%2FCyUhpcc5Ppx8v00kobExUwKogECIn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgySSPaR1%2BAwfTPNPvEq3AMCqC9nWD62Fqu5%2BTZHug3E86zGBFynaTHjuQRShA9AldplJwxMpjZuPFbBKrEGE4MYps0HVPlI1lVEdqCLFdeRbOBUr%2B6azEvjp2UkXCGiR8MdD71BLCmYbNzBhTt%2BaLZbQRjC%2Bkfj%2FVzerShGXsyw0Om%2Ftkecuw0R0AmPWEorExoIpcM40AAXAdAwAXgnMUA9U20UIzjDHqu15AN8h8B2rvGVLmheUpV%2FqI4AFglidtBt8tbjVZOomXFoJEyELGyJKz40uZAJLiMzbNsIOAMowLxL6c8ubUIw5qM8sPI1VSyxuJ%2FlsVSgJJ86BnSY8TTDwdjviK%2FTA%2Fi1YAWTaO98sa8%2BxZy9j9p6NWnkHXHEyypfvQNkZjBL9cwyZVYyjK%2Fp85AQufM9jyVAUjvVuHNAnl9OtJSD9CFV2673DeCXccTZ5i8iaDa32Tqwq1HsGPSp9QeZy7hvL8yoscyZqCmtL%2F59IR8KdAUNAHX6o27ixDQPHEYpjMh4yN5aDPR12wFY5465KhXcy5AiMdkw22qyceeWudwlWbxX%2FhLu3bmPGPNY1lKQHC7iaEB6eMKFizan0eSdQh7bxcgG%2B5rsoGmWJzuVkH9ypDWWf4Mn7VezrLNWWt1I%2F8Bd1YL5KjD2x%2Be8BjqkAY%2FiEFv8XV5PSD43tmjn%2Be6MTC7nQ48JyRyn2q2gIGWFTf2jeEIIQc2SLFhEJlgHnPADQFKjZocDRyp9fHLZqsh8XHXSgk2tGZaWmsBrGVRyYA0lE3W5MgH00ku0XkSSYvaRLKQcQbF3nYleuHexg9SkWIJSIllN5SjoN5gaNrss3tKKdYHSbW9PNrMbhxMn8hvccLckT%2BctkjRhgwqGJr3%2BpLg2&X-Amz-Signature=aa430ce2b0ca742f091e8021d2b2233d194bc9915feadbf4aa6ec03761b9547c&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ab5a6dfe-51f5-43ee-bcb3-33dae4a1c7ad/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46622FW363A%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T091519Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEID%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDebFYHAX%2FtVZ3hxrFGIlOgrRa9ZLv3g6x2uFQd2QLCVAIhAI0zRIrjelX8WjwfIPGnJ%2FCyUhpcc5Ppx8v00kobExUwKogECIn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgySSPaR1%2BAwfTPNPvEq3AMCqC9nWD62Fqu5%2BTZHug3E86zGBFynaTHjuQRShA9AldplJwxMpjZuPFbBKrEGE4MYps0HVPlI1lVEdqCLFdeRbOBUr%2B6azEvjp2UkXCGiR8MdD71BLCmYbNzBhTt%2BaLZbQRjC%2Bkfj%2FVzerShGXsyw0Om%2Ftkecuw0R0AmPWEorExoIpcM40AAXAdAwAXgnMUA9U20UIzjDHqu15AN8h8B2rvGVLmheUpV%2FqI4AFglidtBt8tbjVZOomXFoJEyELGyJKz40uZAJLiMzbNsIOAMowLxL6c8ubUIw5qM8sPI1VSyxuJ%2FlsVSgJJ86BnSY8TTDwdjviK%2FTA%2Fi1YAWTaO98sa8%2BxZy9j9p6NWnkHXHEyypfvQNkZjBL9cwyZVYyjK%2Fp85AQufM9jyVAUjvVuHNAnl9OtJSD9CFV2673DeCXccTZ5i8iaDa32Tqwq1HsGPSp9QeZy7hvL8yoscyZqCmtL%2F59IR8KdAUNAHX6o27ixDQPHEYpjMh4yN5aDPR12wFY5465KhXcy5AiMdkw22qyceeWudwlWbxX%2FhLu3bmPGPNY1lKQHC7iaEB6eMKFizan0eSdQh7bxcgG%2B5rsoGmWJzuVkH9ypDWWf4Mn7VezrLNWWt1I%2F8Bd1YL5KjD2x%2Be8BjqkAY%2FiEFv8XV5PSD43tmjn%2Be6MTC7nQ48JyRyn2q2gIGWFTf2jeEIIQc2SLFhEJlgHnPADQFKjZocDRyp9fHLZqsh8XHXSgk2tGZaWmsBrGVRyYA0lE3W5MgH00ku0XkSSYvaRLKQcQbF3nYleuHexg9SkWIJSIllN5SjoN5gaNrss3tKKdYHSbW9PNrMbhxMn8hvccLckT%2BctkjRhgwqGJr3%2BpLg2&X-Amz-Signature=bccfb50dcdf691034ea745d116d75f06a49c1f54e8913361d46d7b1ca7430c83&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8f1b1d60-cf1b-42b3-9faa-f634c89c3f84/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46622FW363A%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T091519Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEID%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDebFYHAX%2FtVZ3hxrFGIlOgrRa9ZLv3g6x2uFQd2QLCVAIhAI0zRIrjelX8WjwfIPGnJ%2FCyUhpcc5Ppx8v00kobExUwKogECIn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgySSPaR1%2BAwfTPNPvEq3AMCqC9nWD62Fqu5%2BTZHug3E86zGBFynaTHjuQRShA9AldplJwxMpjZuPFbBKrEGE4MYps0HVPlI1lVEdqCLFdeRbOBUr%2B6azEvjp2UkXCGiR8MdD71BLCmYbNzBhTt%2BaLZbQRjC%2Bkfj%2FVzerShGXsyw0Om%2Ftkecuw0R0AmPWEorExoIpcM40AAXAdAwAXgnMUA9U20UIzjDHqu15AN8h8B2rvGVLmheUpV%2FqI4AFglidtBt8tbjVZOomXFoJEyELGyJKz40uZAJLiMzbNsIOAMowLxL6c8ubUIw5qM8sPI1VSyxuJ%2FlsVSgJJ86BnSY8TTDwdjviK%2FTA%2Fi1YAWTaO98sa8%2BxZy9j9p6NWnkHXHEyypfvQNkZjBL9cwyZVYyjK%2Fp85AQufM9jyVAUjvVuHNAnl9OtJSD9CFV2673DeCXccTZ5i8iaDa32Tqwq1HsGPSp9QeZy7hvL8yoscyZqCmtL%2F59IR8KdAUNAHX6o27ixDQPHEYpjMh4yN5aDPR12wFY5465KhXcy5AiMdkw22qyceeWudwlWbxX%2FhLu3bmPGPNY1lKQHC7iaEB6eMKFizan0eSdQh7bxcgG%2B5rsoGmWJzuVkH9ypDWWf4Mn7VezrLNWWt1I%2F8Bd1YL5KjD2x%2Be8BjqkAY%2FiEFv8XV5PSD43tmjn%2Be6MTC7nQ48JyRyn2q2gIGWFTf2jeEIIQc2SLFhEJlgHnPADQFKjZocDRyp9fHLZqsh8XHXSgk2tGZaWmsBrGVRyYA0lE3W5MgH00ku0XkSSYvaRLKQcQbF3nYleuHexg9SkWIJSIllN5SjoN5gaNrss3tKKdYHSbW9PNrMbhxMn8hvccLckT%2BctkjRhgwqGJr3%2BpLg2&X-Amz-Signature=cec418f5ef0bbce4db3f96938e695a2d9c128703a8c853b79e6e139143c19e4b&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/13ad0497-05fe-4eaa-984e-707b33e14761/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46622FW363A%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T091519Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEID%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDebFYHAX%2FtVZ3hxrFGIlOgrRa9ZLv3g6x2uFQd2QLCVAIhAI0zRIrjelX8WjwfIPGnJ%2FCyUhpcc5Ppx8v00kobExUwKogECIn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgySSPaR1%2BAwfTPNPvEq3AMCqC9nWD62Fqu5%2BTZHug3E86zGBFynaTHjuQRShA9AldplJwxMpjZuPFbBKrEGE4MYps0HVPlI1lVEdqCLFdeRbOBUr%2B6azEvjp2UkXCGiR8MdD71BLCmYbNzBhTt%2BaLZbQRjC%2Bkfj%2FVzerShGXsyw0Om%2Ftkecuw0R0AmPWEorExoIpcM40AAXAdAwAXgnMUA9U20UIzjDHqu15AN8h8B2rvGVLmheUpV%2FqI4AFglidtBt8tbjVZOomXFoJEyELGyJKz40uZAJLiMzbNsIOAMowLxL6c8ubUIw5qM8sPI1VSyxuJ%2FlsVSgJJ86BnSY8TTDwdjviK%2FTA%2Fi1YAWTaO98sa8%2BxZy9j9p6NWnkHXHEyypfvQNkZjBL9cwyZVYyjK%2Fp85AQufM9jyVAUjvVuHNAnl9OtJSD9CFV2673DeCXccTZ5i8iaDa32Tqwq1HsGPSp9QeZy7hvL8yoscyZqCmtL%2F59IR8KdAUNAHX6o27ixDQPHEYpjMh4yN5aDPR12wFY5465KhXcy5AiMdkw22qyceeWudwlWbxX%2FhLu3bmPGPNY1lKQHC7iaEB6eMKFizan0eSdQh7bxcgG%2B5rsoGmWJzuVkH9ypDWWf4Mn7VezrLNWWt1I%2F8Bd1YL5KjD2x%2Be8BjqkAY%2FiEFv8XV5PSD43tmjn%2Be6MTC7nQ48JyRyn2q2gIGWFTf2jeEIIQc2SLFhEJlgHnPADQFKjZocDRyp9fHLZqsh8XHXSgk2tGZaWmsBrGVRyYA0lE3W5MgH00ku0XkSSYvaRLKQcQbF3nYleuHexg9SkWIJSIllN5SjoN5gaNrss3tKKdYHSbW9PNrMbhxMn8hvccLckT%2BctkjRhgwqGJr3%2BpLg2&X-Amz-Signature=53982e82d0e33db4c75d136a15dd43db675f74e05b41c0ee86fd38f6b5aa3f73&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 2. Box and Whisker Plot
A box plot shows the distribution of quantitative data in a way that facilitates comparisons between variables or across levels of a categorical variable. The box shows the quartiles of the dataset while the whiskers extend to show the rest of the distribution, except for points that are determined to be "outliers".
**Syntax:**
```python
sns.boxplot(x='header_1', y='header_2', data=df)
```
**Example Output:**


![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d207ae92-0a7c-4e2f-aa65-0ee5a2c33bf7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663JBBFOBA%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T091521Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEID%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDSOEZVQveSIlthvTZS3hocgHHhbfB5w25rVvqpgf01ewIhAIgqRu1OIFK3WsYwbEvFUO1C8vgelUm1dhemuEZZ%2Bc2IKogECIn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwlOZO2spcQ2V7NZ%2BQq3AO95CsJV33qieFT1Y0sf5dRwXD4uPCw%2FYO6jtYWhQCVDgjm%2BVMrLgF%2BJRhn9G4DBiUCyFnowRwGu67CMpI1Pm2bR3sPxbhgRlO6VlB%2F7ZOTTKliCCsqv%2BzUwBYXXXJ5svzVk%2BrXpNwxLawaeaW4NRBJYHwG1TaYdoxDcjZoCNYQH8qCJxOZMVpA7qidqZewtqR2%2FkkCaVUlZirYTLCQcVGMhlugs26yASErzxd59vQ0FUFPC0c52fKWqUjmGXoec5KRt0Pwhx9XB3haxOQ%2F%2F2idYm164kwxzoKGIZyfa%2Ffk55H%2B5LbvJEsICzQppD7asq5qCZAjuX3ey3d%2FN41wPT5Tu%2FY5Sq1MVp%2FDHAl78x14JCBQLCLus5IZo1cjYC9h3d7MmUumr4L6xOBITLpWgcA01XDL6i60p5W6qwv%2B76zAkog9Rri3%2FWXDGJ0owZ0y0sTZ4ycV3nDw4ZXZ389aww9ON66IFRnPJ49c2u0FmrvcNRT2YIRhR373%2BbuprthsoyEdjBJNfGKOsRdaSEPwsB3tj6zLvDhsuqDU6q%2B4Q8BPFmj0eXQbtbWr7duGGiaj4aIW9DzHYUcIKElLwcV%2FQ9%2Fi6tHw3Y95gJW1QBk0p7H17WaKzLcrO5uIZnI0DjCXx%2Be8BjqkAZox%2FoM0tdXBI5P7PwtwrtrUMSkuQt8ZTD7M0J3BIx1ufd6JRWUbXmmljuOuMWuXZzZkVfysKtDoT5%2B2GNQnQBGLQEdlD%2BRJhIXEiw5bD1NKswJHR9DAM6IBdYj8xDnvtewAVWLs50LlfHBVPNF72CMUb59iK9QKDNAxQ5B7I8a2tTQGMeFogJ40bJRanf3w8jpvEK1A6%2FDgwQHPvAD578myKc0y&X-Amz-Signature=750f8b9ac81c9c0535f4f8b607e8eeaa6b2dc08539030fcdf291f8a76f5392f8&X-Amz-SignedHeaders=host&x-id=GetObject)

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0e516edc-7551-4792-ab18-0494db3c4c0c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QCO7SP35%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T091521Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEID%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFZM5wOCuvs1tHfxfn35cNitndX4loWIjMshNMbhbUNaAiBcz8uMXjlx24J0srqjLAYJ1ocgg4eelF29Vm%2BCCEOvViqIBAiJ%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMfIx6p7XE%2FI%2BKyDAoKtwDMlUGJO6Sw3fMhX3FZvdkoezrk5vzVVtHWdXhFowrw9ZEKJi3%2FxtcawUyR54xk7qNE2O4ryqI55LwZ%2FJ9vC3cijVFEeG26RKz7AvZUd09wGPMfEOV6ItrJFkuAImEWoJwjR4QYXfWaghBwQxAQIsjIExsQnEgSmhX9Ze4EcsF0SHfPyyekrTIEx7v5TG6QlkN1FuT3NRV%2FefYD8thnHVTWq5XRNJbtpNPKf8AHCXI2regptR9zn7SfO9Mfk3hNWLzI7HxNCSNxaZCoortR57zgXZstMd%2BwfqHgBTT%2FvH6dOVI9xx3cMJEC0sl795BHmVQkf6OmCbZasWkJFvofREFjYyiOpWJ0Oir3SHLv8CPbHvFlEsoetvypEchxNsdTAm2iSHhEo4b1rOv%2Fe307LNNAHnOV7YffrKFwH%2BtXB0A8%2B41M5o358ZHEfRCqznjR5J7j5enOQf%2F4Aru%2BaQsbZJV0rolKTAjtBhtPTCRfG7Mn7pzjLkNkb1pbIZ7J2cLBoYr7Sgit7gEtAKzbN604%2BtaYMsy2U7HfxT3Iq2c61yRyaOOKAHBiv3sMKcXEsfN50eVafqmMZITasNjXPcmCOzjbfleqZQRFeqcM3%2FQU8RbBahWA0XDm3LKUwMkzqwwzMfnvAY6pgET9vRqEBnk9wnFpVnC%2BIWYulNlZCZ6jPq3RQjLi%2FK9ERP3bOmQg2Ro54pr9t4O6kmWhxMN8QWAyvIP95r6Du7u2CMrIRy3VHg6ZL%2B8FcoBVhz4w099Jz19IHNSeBeHRQGOlw8C9RK2Gz4nU6sKGgWwQjb%2F7V%2BnhLbtpNbyGorQBFxNdrL1FDN7nK7eeTndiJqEx5RcHaZsYbZZ8BuDZbNaOUjkOFl8&X-Amz-Signature=6d68856d57a651f4f6ea8ad3582a4081fbbf78c322b4cc439a7081f64fe6c1a8&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23a79b9d-2356-49a9-8fd9-65c6b0ab2cc5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46622FW363A%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T091519Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEID%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDebFYHAX%2FtVZ3hxrFGIlOgrRa9ZLv3g6x2uFQd2QLCVAIhAI0zRIrjelX8WjwfIPGnJ%2FCyUhpcc5Ppx8v00kobExUwKogECIn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgySSPaR1%2BAwfTPNPvEq3AMCqC9nWD62Fqu5%2BTZHug3E86zGBFynaTHjuQRShA9AldplJwxMpjZuPFbBKrEGE4MYps0HVPlI1lVEdqCLFdeRbOBUr%2B6azEvjp2UkXCGiR8MdD71BLCmYbNzBhTt%2BaLZbQRjC%2Bkfj%2FVzerShGXsyw0Om%2Ftkecuw0R0AmPWEorExoIpcM40AAXAdAwAXgnMUA9U20UIzjDHqu15AN8h8B2rvGVLmheUpV%2FqI4AFglidtBt8tbjVZOomXFoJEyELGyJKz40uZAJLiMzbNsIOAMowLxL6c8ubUIw5qM8sPI1VSyxuJ%2FlsVSgJJ86BnSY8TTDwdjviK%2FTA%2Fi1YAWTaO98sa8%2BxZy9j9p6NWnkHXHEyypfvQNkZjBL9cwyZVYyjK%2Fp85AQufM9jyVAUjvVuHNAnl9OtJSD9CFV2673DeCXccTZ5i8iaDa32Tqwq1HsGPSp9QeZy7hvL8yoscyZqCmtL%2F59IR8KdAUNAHX6o27ixDQPHEYpjMh4yN5aDPR12wFY5465KhXcy5AiMdkw22qyceeWudwlWbxX%2FhLu3bmPGPNY1lKQHC7iaEB6eMKFizan0eSdQh7bxcgG%2B5rsoGmWJzuVkH9ypDWWf4Mn7VezrLNWWt1I%2F8Bd1YL5KjD2x%2Be8BjqkAY%2FiEFv8XV5PSD43tmjn%2Be6MTC7nQ48JyRyn2q2gIGWFTf2jeEIIQc2SLFhEJlgHnPADQFKjZocDRyp9fHLZqsh8XHXSgk2tGZaWmsBrGVRyYA0lE3W5MgH00ku0XkSSYvaRLKQcQbF3nYleuHexg9SkWIJSIllN5SjoN5gaNrss3tKKdYHSbW9PNrMbhxMn8hvccLckT%2BctkjRhgwqGJr3%2BpLg2&X-Amz-Signature=cdb48f3d1b488879ffb43fbd9b7214037729d6b1c05b88102da6444a1499fb42&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 4. KDE Plot
A Kernel Density Estimate (KDE) plot is a graph that creates a probability distribution curve for the data based upon its likelihood of occurrence on a specific value. This is created for a single vector of information.
**Syntax:**
```python
sns.kdeplot(X) || sns.kdeplot(df['age'])
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0d571213-2a2f-4921-a50b-880847aa05ee/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46622FW363A%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T091519Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEID%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDebFYHAX%2FtVZ3hxrFGIlOgrRa9ZLv3g6x2uFQd2QLCVAIhAI0zRIrjelX8WjwfIPGnJ%2FCyUhpcc5Ppx8v00kobExUwKogECIn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgySSPaR1%2BAwfTPNPvEq3AMCqC9nWD62Fqu5%2BTZHug3E86zGBFynaTHjuQRShA9AldplJwxMpjZuPFbBKrEGE4MYps0HVPlI1lVEdqCLFdeRbOBUr%2B6azEvjp2UkXCGiR8MdD71BLCmYbNzBhTt%2BaLZbQRjC%2Bkfj%2FVzerShGXsyw0Om%2Ftkecuw0R0AmPWEorExoIpcM40AAXAdAwAXgnMUA9U20UIzjDHqu15AN8h8B2rvGVLmheUpV%2FqI4AFglidtBt8tbjVZOomXFoJEyELGyJKz40uZAJLiMzbNsIOAMowLxL6c8ubUIw5qM8sPI1VSyxuJ%2FlsVSgJJ86BnSY8TTDwdjviK%2FTA%2Fi1YAWTaO98sa8%2BxZy9j9p6NWnkHXHEyypfvQNkZjBL9cwyZVYyjK%2Fp85AQufM9jyVAUjvVuHNAnl9OtJSD9CFV2673DeCXccTZ5i8iaDa32Tqwq1HsGPSp9QeZy7hvL8yoscyZqCmtL%2F59IR8KdAUNAHX6o27ixDQPHEYpjMh4yN5aDPR12wFY5465KhXcy5AiMdkw22qyceeWudwlWbxX%2FhLu3bmPGPNY1lKQHC7iaEB6eMKFizan0eSdQh7bxcgG%2B5rsoGmWJzuVkH9ypDWWf4Mn7VezrLNWWt1I%2F8Bd1YL5KjD2x%2Be8BjqkAY%2FiEFv8XV5PSD43tmjn%2Be6MTC7nQ48JyRyn2q2gIGWFTf2jeEIIQc2SLFhEJlgHnPADQFKjZocDRyp9fHLZqsh8XHXSgk2tGZaWmsBrGVRyYA0lE3W5MgH00ku0XkSSYvaRLKQcQbF3nYleuHexg9SkWIJSIllN5SjoN5gaNrss3tKKdYHSbW9PNrMbhxMn8hvccLckT%2BctkjRhgwqGJr3%2BpLg2&X-Amz-Signature=21c17739a96a3fd4c900a7531bf6832364de4fb16ec80789c4c8efd7e05436a3&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/53752550-ef82-4ca9-a01a-09921f0282d0/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46622FW363A%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T091519Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEID%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDebFYHAX%2FtVZ3hxrFGIlOgrRa9ZLv3g6x2uFQd2QLCVAIhAI0zRIrjelX8WjwfIPGnJ%2FCyUhpcc5Ppx8v00kobExUwKogECIn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgySSPaR1%2BAwfTPNPvEq3AMCqC9nWD62Fqu5%2BTZHug3E86zGBFynaTHjuQRShA9AldplJwxMpjZuPFbBKrEGE4MYps0HVPlI1lVEdqCLFdeRbOBUr%2B6azEvjp2UkXCGiR8MdD71BLCmYbNzBhTt%2BaLZbQRjC%2Bkfj%2FVzerShGXsyw0Om%2Ftkecuw0R0AmPWEorExoIpcM40AAXAdAwAXgnMUA9U20UIzjDHqu15AN8h8B2rvGVLmheUpV%2FqI4AFglidtBt8tbjVZOomXFoJEyELGyJKz40uZAJLiMzbNsIOAMowLxL6c8ubUIw5qM8sPI1VSyxuJ%2FlsVSgJJ86BnSY8TTDwdjviK%2FTA%2Fi1YAWTaO98sa8%2BxZy9j9p6NWnkHXHEyypfvQNkZjBL9cwyZVYyjK%2Fp85AQufM9jyVAUjvVuHNAnl9OtJSD9CFV2673DeCXccTZ5i8iaDa32Tqwq1HsGPSp9QeZy7hvL8yoscyZqCmtL%2F59IR8KdAUNAHX6o27ixDQPHEYpjMh4yN5aDPR12wFY5465KhXcy5AiMdkw22qyceeWudwlWbxX%2FhLu3bmPGPNY1lKQHC7iaEB6eMKFizan0eSdQh7bxcgG%2B5rsoGmWJzuVkH9ypDWWf4Mn7VezrLNWWt1I%2F8Bd1YL5KjD2x%2Be8BjqkAY%2FiEFv8XV5PSD43tmjn%2Be6MTC7nQ48JyRyn2q2gIGWFTf2jeEIIQc2SLFhEJlgHnPADQFKjZocDRyp9fHLZqsh8XHXSgk2tGZaWmsBrGVRyYA0lE3W5MgH00ku0XkSSYvaRLKQcQbF3nYleuHexg9SkWIJSIllN5SjoN5gaNrss3tKKdYHSbW9PNrMbhxMn8hvccLckT%2BctkjRhgwqGJr3%2BpLg2&X-Amz-Signature=2135d4deb77a7172bca26ca2d83105a7bbc3165dcef81b855e106bc422d21734&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
## 4. Correlation Between Variables
Correlation is a statistical measure of the extent to which different variables are interdependent. It indicates how changes in one variable are associated with changes in another variable over time.
### Positive Correlation
Positive correlation indicates that as one variable increases, the other variable also tends to increase.
**Example: Engine Size and Price**
- **Positive Correlation:** Engine size increases, price also increases.
- **Visualization:** Scatter plot with a steep positive slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c7ea9b0-3ef3-4357-a9c3-554fc71b6b15/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YXS3LKYF%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T091521Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEID%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDAkVTqP7QA7mEpPnhDLi%2FtJURIS5hGTu98Z3vVjGcm7AIhAK4EeXuWBxxZ5V6QtVriNFeZyxdTVbXBNB7KQGJ7i%2FBiKogECIn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzpxqmJb4AJAMjwvWUq3AMiMP3JhvxJSeMm4j0RG8%2F%2FC4EQe4qC3GOqSlUIlCVtFHqhdXe%2BzSQ85JTRVDCgE13tVkb7Oqj%2Fmz9KXIFplrkTzJo18TQeRUh%2FGa3cXo%2FIU9xc%2BagOdIanek5J9IgkDstwaYFRPZE4KMegiW%2BP2nwcqAhevpiHv5pBbCOQKMxVZtfwnmLnB5PX%2F%2Fu%2BlH%2B1a9TLG0%2Fm3ERsCEe9ud0O5Qbv3SLDv0IbfY8n3VsUf2b0RvIkoLsJCgJVqmZ%2FcQwkV0yfSbZoOvJVQk0p%2FVi%2B0hS%2Bnb%2BS4n39d9vwuXjD%2Flt4TT3HppcvaZUVRY%2FfjoG7gSU558gMMZN5%2B0UL7QesYPZZxOtbSrrGI2Vodjo0rUJZyFnYHRk6UxxRGuDkhWeB4SdyOIjUwwSay6ga42zhAXf8sH212CPPV%2FmIcTc5Ly8TSdh15sEE4X0%2FwR7yAZqFu8yIvXs7LIyVwvJu52dVl93qh4GIDee3J%2FdyZNFiHoB0vak4ABRjDyW8KJ3tdImM6JFFiCfo8%2BLVudywzTeCLDefxCZ90jUEhaw%2FKAh5QevJ1Qy4zKSomniUF7fCR2gxll2pJGeXeefAZ15%2B0A2UJvvaWOfrZu783XlIpOvbJ281fj9AJsguimwDtNeHvzDLx%2Be8BjqkAZDaTwWiYsZ9B3cS5fqd0qNZWCcH64mvBjxrfQZ9h9PXve5UneVWAguBRH5M61UwBpNbBF3JD2C7Lj%2FX6bLuLeHthZFDgjYOKAU%2Bl4q%2FdOWr3qht86wdGCuDR7t2XCyHDMrSW2Z7G5ePGg4xVd9HEu1O%2F4PvQtNq1bV%2FXfZXXB0agDw3jAaDOYGfJ7yC1w%2Ban%2B64cmPn0T4AuDEz5OrYS8oVCLIT&X-Amz-Signature=c18d45ec189be562638347f23e66f781c5df14021ad0b72126393142590ae120&X-Amz-SignedHeaders=host&x-id=GetObject)
**Explanation:** When engine size increases, there is a corresponding increase in the price of the vehicle. This positive correlation suggests that larger engines tend to be associated with higher prices in the market.
___
### Negative Correlation
Negative correlation indicates that as one variable increases, the other variable tends to decrease.
**Example: Highway Miles per Gallon and Price**
- **Negative Correlation:** As highway miles per gallon increases, price decreases.
- **Visualization:** Scatter plot with a steep negative slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/10f1f798-9cc4-4df2-a9c1-5a339f554a0b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667N3ZMBIH%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T091521Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEID%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHpdxzKkZE8nAKSF8ZFwlCqllBOFobDL%2BVU7X1igAXunAiEArbUqvSUoBLYhk7px9VjQ7zoXvw4pidDSQhgaQV3W61AqiAQIif%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDD9Zd91m5ZIy2S2L5ircAw0r4v5PJIwZt6wfsbVm2ZNh%2FDIbzk%2FOhCYzDwlEHCuEl%2FyRUpPKkzjoBErd8b6iOiPo51axkY8HvBQlzGqjwxuB5Zts%2FmD1sejUaVrlDLJqNXI4BpLom3wlS7GGaHip68t9ounG1jTnFzMEIUD%2BRlOOeH8dd5xENtyyDqNQmbg9vTciyH5SnW1gc5DAHvhXu%2FkRlgXK4NJ07JUKj8pJLKRQNmo6GoGkTMF4THMnF4N2Ljuwn3rd9IsoRoa1rhdVFiLfkwI1uKdvCZ9U%2BxSXiPOoAM81jUhNlmG49T%2Bf9mNNu7B%2FwgD9oCJpTK3GaacP4U4L9ZNmrePEh4rFrQNjHiod%2B6ISKyjxI8e1hKNft4uAyuCb%2FXmRRzUiBnlK7Z3%2FMtfm8qsvFORaNnkVYLJDQ8XYEargvUpLtbksv8%2B6g%2FZP9S4goZDtNp6EAN2X5AG%2F2PLvFsBVf9TXar8BOoWPAetfG5WrutChifRg4%2FuhVDl3L%2B7HcVBoL61Ro3GTQfQHUnlp%2BaRa3a9GnRKdq57OOmo2vDWD38boGfiiG%2FZSzQ%2FNauZxxMmMmpExBysZnhM8xBgGfRX2VjUw1PlO5psovIQ5uR4JPmVHiUxRSXPf8k9ZsOicKmmOBLPFB2obMPbH57wGOqUBMQaVNsFeqFleu9P49bOiwBDjAUSZGm%2BVi9D%2FrwzVZt2qEPWiOu4w%2FetrN5E4QC2vGs8BpYH4OFQ4LhwxQnGMqwTInYFFmPFlP8L01yyREJ9QI6LHt%2B7eFe0fbYdRCe%2F2hKNWV5FYXKKCkXWlNIywNy4cq08P6zX1%2F7AkWUHDMIJzHiKWm1Zh%2BHK929ZEOwS2TUJiIsf6M40LA50fUsI5ZYzzlmnI&X-Amz-Signature=a031e36d6a7dde251be8b9af6991076bbe0000b5807c78508e3163c9794c14ee&X-Amz-SignedHeaders=host&x-id=GetObject)
**Explanation:** When highway miles per gallon increases, the price of the vehicle tends to decrease. This negative correlation suggests that cars with higher fuel efficiency (more miles per gallon) are generally priced lower in the market.
___
### Weak Correlation
Weak correlation indicates a lack of strong relationship between the variables.
**Example: RPM and Price**
- **Weak Correlation:** Low and high RPM values show varied prices, indicating no strong predictive relationship.
- **Visualization:** Scatter plot with no clear trend or slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9f914514-8914-4bf4-ac84-d9e3077f6eb1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UQ3W3TXJ%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T091521Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEID%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIBSbBfd9841%2F93icIJBLVGeUnLoWbEomG9fWdfeoPA6wAiEA86hOFeH8NA%2BU5tI2SynRKBRl8cfX3fFv56n7Nt6eD7IqiAQIif%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKwOn0Ol7snsZr2UZyrcA5Y2IJF5b33DTcZbRbpka5p8AqkoKnHXife8xN6cr0JARKFRZo316mU6rR9AhD9VhjO79wo6y%2F4la3zTNWCXti3FeSRAvK2W2kcTmuvszrKP%2BzFtG477rJAVJ%2FJoeS%2BYpnQGbjps4%2B2fQn4gWFfo0GC%2FLsWBdhl3Zu%2BJpFTcEXQSljnD%2BeDVosjO3eL6%2BcNt3f%2BDaLS9HXsjoxMc%2F73Puun8ijbYIxNnvv1js0uxQ%2FhCwgKF63oe%2BuA1Hu8XnO%2F4Tz2TAxwQTjPZew5S3pNkQSXDHmooUKWAuFLka4J5ki74Lozu4oCUzVKnLNVEbF9xo4iEifbDsUQY0W83oJNNCEvDezuvl6Zh%2FuC9w%2BdxEDMw%2BcEFOBdOoEQJTVHZMSMw4%2BJTfvsIFMI8puWJjYhS4lJKjBXEsY6PkGFQ5jhlcJNrjSJUT9IVZYl7KQ%2BrdwV%2BMsom0lw9%2FrGsLRQEhEcXZPnUuayE95neDJc1Lb%2BZM4XbsPJKLDEIr9RKB9RT4JbnD9lNQ5ZECDtcojUgBVk6iTAvPiwzvOVWc2NkjKYJasElhe0RvYVGvH%2FJhg%2B4b3LsX0m0JHZA9J5JTT3zV8vxkMHPU79QSiMfDTVGES5XjCEeacbpnaLkMMfdVX3SMNvH57wGOqUBA8hPcI1D2FGBjaPXGPXp6MTDWC0oGFBv2oZpaQQN2jJEDine9sX6j3wEWp6%2BvLI%2FO0bBotk1c8fw3BApBjo4TfoCuQV%2BYeZ5HdhOeR9thqkq1iKkSKo430x5G9wi0%2FAGr2I%2FI3QIEUwgsMKuQ%2Bdz7ihaa5K9W8RV5ryz7eLuU8Vr4dWpbyXizLBLKaMeaRYIJWYnjK0otaTN%2Bn2d%2B7LJiigNdfzj&X-Amz-Signature=b309575dfc1240dbe7b42b113a3d508208b87fe73a725df0fec020a625716885&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f18086e5-5b04-4fbf-8309-8944ab20d213/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VJ2WDTTS%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T091520Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEID%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGr1rMHXmEaH%2B7DjpIPhjxmZWhefsTKTrIRdfsXTLG2oAiEA33GCRc3MQqGRpM87dQiyMma6OVtROlZsbNkViRy%2FFjAqiAQIif%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDC6eU1Eoa7QK2o1gxyrcA3%2B8caX8t4Jp6PlkrKQRWz1lsgNVPj06wUcG5sV3U20VpaN7i%2BstIFdCz65fOWHSjuicx9F4pVRht5rB6KJkGfOGl9LgWFwPfPiUwGIwLVGpXLz%2BdKaSMm5Cj64zA58SAXH8%2FzUeDAzhKhjVFnslMWoOH4CT66X%2BebPvUeeBnc7%2BbWlUX3L0S6RQOvBbetvtT5kSQufJJVVkzgM2gO59VpifJEH6pa13xFJ7TljKxYfQ33gIQIDJQmdDA0MnenI2Anv1updu2U9LySzw3kZfJ7sl%2BpydUIzM5s1kY7zpb%2B1UwtfjR%2BmuS%2FDxhE3bKDiMJi2xM%2BcBiFxG42WSy9Ds8tHQ7X7S9t%2FaatNIHPdTIw1lUSxGA7uq1bCofPRcmYFTI8PCkHMRUs28qatgy9dT%2B7KSA%2BRFuXb0p5pg2mRSmRWF1vwPAbq%2Bqhd7jMLtO5g5GJ3hLnrGlOE%2F0HVvPikwrUpZJ6DKlTN5qbG2ffQb%2BsG0kdVCVdggzjUA45bVIp0qgGtGaog5v8ulv6rrz1wj%2BAuTh%2BoEoPoocAV%2FdkiYDzVzKXnKq6s9sxzKS3oUb%2BlfkbuYRhNcQ%2BxuGAE1kw21W7eujO2Vmnp1WeLiV98Osb07WLLfGDdeZkFhGtChMMvH57wGOqUBIkS0Pzz2Hv%2FXHyFXhrZ%2BPMhBVLFkw2Hq8kbI3l7efv5IOh4esYHqkNnUO%2BSTb%2BwQofvE7tz0dqWoEhO5Uja56nsc5rj7P3Ie7WlzGjSB8MQ0G1jOObQXSk%2FKwBw9GHIiuNAg%2Fe6r8ytQchnhPEorsb1j94dB0ZvzjCuSIfXWojyiEBQ1sXEOYa6ocK3gn9doAxIwF5DIeihv%2BWU5flz%2B2EiyY8j6&X-Amz-Signature=c9e7b8b1289fe840f4e676aec826ab6366820e8582717d135e7d3f195e476b6d&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Correlation Plot
Heatmap visualizes correlations among variables. Color scheme indicates Pearson correlation coefficients. Dark red diagonal line shows perfect correlation (value of 1) between variables and themselves.
This heatmap offers overview of variable relationships and their link with price.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cd3b341e-cc1a-45f7-8aec-cdc00436d270/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VJ2WDTTS%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T091520Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEID%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGr1rMHXmEaH%2B7DjpIPhjxmZWhefsTKTrIRdfsXTLG2oAiEA33GCRc3MQqGRpM87dQiyMma6OVtROlZsbNkViRy%2FFjAqiAQIif%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDC6eU1Eoa7QK2o1gxyrcA3%2B8caX8t4Jp6PlkrKQRWz1lsgNVPj06wUcG5sV3U20VpaN7i%2BstIFdCz65fOWHSjuicx9F4pVRht5rB6KJkGfOGl9LgWFwPfPiUwGIwLVGpXLz%2BdKaSMm5Cj64zA58SAXH8%2FzUeDAzhKhjVFnslMWoOH4CT66X%2BebPvUeeBnc7%2BbWlUX3L0S6RQOvBbetvtT5kSQufJJVVkzgM2gO59VpifJEH6pa13xFJ7TljKxYfQ33gIQIDJQmdDA0MnenI2Anv1updu2U9LySzw3kZfJ7sl%2BpydUIzM5s1kY7zpb%2B1UwtfjR%2BmuS%2FDxhE3bKDiMJi2xM%2BcBiFxG42WSy9Ds8tHQ7X7S9t%2FaatNIHPdTIw1lUSxGA7uq1bCofPRcmYFTI8PCkHMRUs28qatgy9dT%2B7KSA%2BRFuXb0p5pg2mRSmRWF1vwPAbq%2Bqhd7jMLtO5g5GJ3hLnrGlOE%2F0HVvPikwrUpZJ6DKlTN5qbG2ffQb%2BsG0kdVCVdggzjUA45bVIp0qgGtGaog5v8ulv6rrz1wj%2BAuTh%2BoEoPoocAV%2FdkiYDzVzKXnKq6s9sxzKS3oUb%2BlfkbuYRhNcQ%2BxuGAE1kw21W7eujO2Vmnp1WeLiV98Osb07WLLfGDdeZkFhGtChMMvH57wGOqUBIkS0Pzz2Hv%2FXHyFXhrZ%2BPMhBVLFkw2Hq8kbI3l7efv5IOh4esYHqkNnUO%2BSTb%2BwQofvE7tz0dqWoEhO5Uja56nsc5rj7P3Ie7WlzGjSB8MQ0G1jOObQXSk%2FKwBw9GHIiuNAg%2Fe6r8ytQchnhPEorsb1j94dB0ZvzjCuSIfXWojyiEBQ1sXEOYa6ocK3gn9doAxIwF5DIeihv%2BWU5flz%2B2EiyY8j6&X-Amz-Signature=33f362ae6e5fa5d4c76c285af75975522bf622fb5c2b460060ee08b73716d911&X-Amz-SignedHeaders=host&x-id=GetObject)

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
