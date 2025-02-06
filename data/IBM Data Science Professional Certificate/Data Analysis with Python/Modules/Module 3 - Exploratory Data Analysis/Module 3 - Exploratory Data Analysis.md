

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7e6d594d-952e-44b6-97ea-31225882aea6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663WOO746M%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T031812Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDgaCXVzLXdlc3QtMiJIMEYCIQDTInmJGt2n4fa%2Ff62dktRqL3wxY8Xq1KrPvhJnTc8UWAIhAInzg%2FOIVRWIWo0spR5LIKN5FhLENl17GnKAzErw%2FYSpKv8DCFEQABoMNjM3NDIzMTgzODA1IgwB6O4zE7owFjYD%2BiMq3AN8P2TXp0sfDbV3eQgtEkhQCy%2Bd4T3lKC9ySe%2FKpcenFk%2BK6kJobzim%2B%2FCyl11ESX2LV6rhon2OgvVvP4I0tZeu8M%2BZ1oJAuv7MMHfMgYHp%2B%2FchOAJHjaay7nrlknf6Q2sBXVnCrz%2Ft13A94JdUUw59cWumbHtUmslD7qr%2Bo8w6jD9vPZUetmAmYa9vcI6edS8uoBSShgE01FKNl7ySgpHizmQPMqN8hsCbE7PbfRjdtCALDnQsj%2FA2%2Bkr03KSRatdMDU9yr0AqIuf4nB2pRGcryHY2U8Yy76NhRAi8tL9Hv%2F7cOOBfnMfDB%2FezaLp3VCZzowWSpr0Qyu80xRSm3%2BRFPDH01a21rR7kpxdRGldA588%2FgOFOPbvNJugr2j9OQzL4RgQC1MyefG8K0LNw1Kwvb8Gdp0OzV5ttujDPysNiyHTJOrMeZfOFps6L3xc%2BRnYxIw38%2Bzw02g2vwTHRJgNCLGtzLr6iUuWUbMDnmJRqGEld5jNVoYlITjFC8NW4%2BYQwMYQiGQr%2BGdK4CFi3Uvk4rRyWJLd7bLXMSJuIGmN5jk3vu59pOxGmHIfmWM4F8ST7keSp8WJDOLaVF8rg2E5vFIVU6r2AR7z767LlKcBsQyYoKwUjSkYm2byFszDx6o%2B9BjqkAfMhd0Hgy12zC52u9R65VRFxAiQ8vHofE0IasGkU7FjyIiFcZfoYTWoIyC0nLFtOdf3IXkqjNxSbN2KA35N8FcU4De7UF3qqRJ4XOGjxG42nbzUm40Oy7Mx%2FMvMXMkUP1hY8Wq4mrV7F3ehpxBv5TljKa%2B8adplcXhPBkKG3gzDQEaDBt66LoSLSHoUIcJxZ0Ygb2KRcSsy0ovlw%2Bwa74H%2Bxp789&X-Amz-Signature=ac5b57daf65d1b5a1f0afe50a562fb74228b2d379f4ba72787949c30362d5107&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cbfaed9e-b398-4902-8936-dea058b21def/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663WOO746M%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T031812Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDgaCXVzLXdlc3QtMiJIMEYCIQDTInmJGt2n4fa%2Ff62dktRqL3wxY8Xq1KrPvhJnTc8UWAIhAInzg%2FOIVRWIWo0spR5LIKN5FhLENl17GnKAzErw%2FYSpKv8DCFEQABoMNjM3NDIzMTgzODA1IgwB6O4zE7owFjYD%2BiMq3AN8P2TXp0sfDbV3eQgtEkhQCy%2Bd4T3lKC9ySe%2FKpcenFk%2BK6kJobzim%2B%2FCyl11ESX2LV6rhon2OgvVvP4I0tZeu8M%2BZ1oJAuv7MMHfMgYHp%2B%2FchOAJHjaay7nrlknf6Q2sBXVnCrz%2Ft13A94JdUUw59cWumbHtUmslD7qr%2Bo8w6jD9vPZUetmAmYa9vcI6edS8uoBSShgE01FKNl7ySgpHizmQPMqN8hsCbE7PbfRjdtCALDnQsj%2FA2%2Bkr03KSRatdMDU9yr0AqIuf4nB2pRGcryHY2U8Yy76NhRAi8tL9Hv%2F7cOOBfnMfDB%2FezaLp3VCZzowWSpr0Qyu80xRSm3%2BRFPDH01a21rR7kpxdRGldA588%2FgOFOPbvNJugr2j9OQzL4RgQC1MyefG8K0LNw1Kwvb8Gdp0OzV5ttujDPysNiyHTJOrMeZfOFps6L3xc%2BRnYxIw38%2Bzw02g2vwTHRJgNCLGtzLr6iUuWUbMDnmJRqGEld5jNVoYlITjFC8NW4%2BYQwMYQiGQr%2BGdK4CFi3Uvk4rRyWJLd7bLXMSJuIGmN5jk3vu59pOxGmHIfmWM4F8ST7keSp8WJDOLaVF8rg2E5vFIVU6r2AR7z767LlKcBsQyYoKwUjSkYm2byFszDx6o%2B9BjqkAfMhd0Hgy12zC52u9R65VRFxAiQ8vHofE0IasGkU7FjyIiFcZfoYTWoIyC0nLFtOdf3IXkqjNxSbN2KA35N8FcU4De7UF3qqRJ4XOGjxG42nbzUm40Oy7Mx%2FMvMXMkUP1hY8Wq4mrV7F3ehpxBv5TljKa%2B8adplcXhPBkKG3gzDQEaDBt66LoSLSHoUIcJxZ0Ygb2KRcSsy0ovlw%2Bwa74H%2Bxp789&X-Amz-Signature=b53452004973fa365facb9087b4e03cc14db311a95a13ad695a2436fd2df6be7&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/91181646-b1e0-4433-9711-6259a96a9247/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663WOO746M%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T031812Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDgaCXVzLXdlc3QtMiJIMEYCIQDTInmJGt2n4fa%2Ff62dktRqL3wxY8Xq1KrPvhJnTc8UWAIhAInzg%2FOIVRWIWo0spR5LIKN5FhLENl17GnKAzErw%2FYSpKv8DCFEQABoMNjM3NDIzMTgzODA1IgwB6O4zE7owFjYD%2BiMq3AN8P2TXp0sfDbV3eQgtEkhQCy%2Bd4T3lKC9ySe%2FKpcenFk%2BK6kJobzim%2B%2FCyl11ESX2LV6rhon2OgvVvP4I0tZeu8M%2BZ1oJAuv7MMHfMgYHp%2B%2FchOAJHjaay7nrlknf6Q2sBXVnCrz%2Ft13A94JdUUw59cWumbHtUmslD7qr%2Bo8w6jD9vPZUetmAmYa9vcI6edS8uoBSShgE01FKNl7ySgpHizmQPMqN8hsCbE7PbfRjdtCALDnQsj%2FA2%2Bkr03KSRatdMDU9yr0AqIuf4nB2pRGcryHY2U8Yy76NhRAi8tL9Hv%2F7cOOBfnMfDB%2FezaLp3VCZzowWSpr0Qyu80xRSm3%2BRFPDH01a21rR7kpxdRGldA588%2FgOFOPbvNJugr2j9OQzL4RgQC1MyefG8K0LNw1Kwvb8Gdp0OzV5ttujDPysNiyHTJOrMeZfOFps6L3xc%2BRnYxIw38%2Bzw02g2vwTHRJgNCLGtzLr6iUuWUbMDnmJRqGEld5jNVoYlITjFC8NW4%2BYQwMYQiGQr%2BGdK4CFi3Uvk4rRyWJLd7bLXMSJuIGmN5jk3vu59pOxGmHIfmWM4F8ST7keSp8WJDOLaVF8rg2E5vFIVU6r2AR7z767LlKcBsQyYoKwUjSkYm2byFszDx6o%2B9BjqkAfMhd0Hgy12zC52u9R65VRFxAiQ8vHofE0IasGkU7FjyIiFcZfoYTWoIyC0nLFtOdf3IXkqjNxSbN2KA35N8FcU4De7UF3qqRJ4XOGjxG42nbzUm40Oy7Mx%2FMvMXMkUP1hY8Wq4mrV7F3ehpxBv5TljKa%2B8adplcXhPBkKG3gzDQEaDBt66LoSLSHoUIcJxZ0Ygb2KRcSsy0ovlw%2Bwa74H%2Bxp789&X-Amz-Signature=f640c65421133b468e1dd9b34d93167e1bdd09cb607dcfe21f2b4759e00e6b8d&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/09aba1c0-0d55-41dd-852a-a04c5b8a3fac/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466S23JSOF5%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T031813Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDgaCXVzLXdlc3QtMiJGMEQCIGN49pv%2BGzlDvEcmRHHziJ4uTCJ7T7rj0PUT6XRPaOXQAiA%2BjgQX8%2FTadK212587KT06jJgWio%2F9BcHfHhLWbIN%2FGSr%2FAwhREAAaDDYzNzQyMzE4MzgwNSIMVofCLcg1tIdWrD8FKtwDluDlxj6W3tysxd37QbNBmlL78%2FRRn%2BNaz3N2o4e4O%2Fzb3RUmdwQa5v62Fx8lQ9VZn2W6CRXj9NZkRx2L%2FOjw%2BvB%2FOeWp0cz1Tq3NLJMqiLZkVSNQoa2d%2F1pYNVWSsRh9pGSn7932ot95gxkY9EecQKocR5HFQIeFc1%2BMvAtQVXCRUyr7jgdy4AVJUhjTmFNnGRV0fpTnYvWEmt4JEYcCHtjalHRTwLpofZvO9mk7koJUZs7ztrXTIZjyBwv1gIGAjE2oZihrksPRvMsHKbPmxYv5F%2BXTnAA%2B96Pqypv%2FAI5NO2ADv%2FyNxjZDMJhB0tCMIX%2B0V%2BktgSh%2BmnMzAjnn2TWBeYKiRzPnWcexRXVHmhDf2TzsNe5RC6Elbo31eRa7KQL2cxq6%2BJ4Lw2R7ky0TZ14XBZy8a99nRtPnlsM9t3kfQ0gAz1slJI%2BggdSLK%2Fj%2BHtyoyX%2BcXe23hIz8kKNE%2FktAIEmTsrt2YUOG3igxE%2Fadn5Tlf09NANWBv3BarHitTw9LTL%2BLQsrz6EO3580vXyqBuAiNFJYqbV9YouPCyMYN%2BBmmPJsZJ4JvJaRbI5ZlWQ4qnGLeALgEtWukmQ1tlOD93CwuehXVwOZ%2FcN1vCdnKlZ%2FEDBDVTEzRkx8w7uqPvQY6pgFbohDWGj%2BO42XZv7gaqa6Ppm%2F9Mgxfi%2Byewd8IBNKYYroLfetzDeCqANdtjl8qZP21vRJUinJ%2B7QmfVxLn%2FAlwIfWqS2e%2Bf7iHOUCDE1TA7MJYNaW2h5pQh2r%2BaxXgmjNC6xmHokIEGceI%2FD%2BKPCfITgOYBXBDpumhh2P6hrqsQ21LIUp9ptj%2FkXC65mwXMQfXV54XAP3lqgVUxlXPmfXyXVnSCCLT&X-Amz-Signature=c5eef6c68dc36958e9202ae58e342692e1ba21fe6f9c3d3983bc7cd78ca481cf&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 2. Scatter Plot
Scatter plots present the relationship between two variables in a dataset. It represents data points on a two-dimensional plane. The independent variable or attribute is plotted on the X-axis, while the dependent variable is plotted on the Y-axis.
**Syntax:**
```python
plt.scatter(x, y)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23708af9-659f-4f23-b626-1a4292d7842c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466S23JSOF5%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T031813Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDgaCXVzLXdlc3QtMiJGMEQCIGN49pv%2BGzlDvEcmRHHziJ4uTCJ7T7rj0PUT6XRPaOXQAiA%2BjgQX8%2FTadK212587KT06jJgWio%2F9BcHfHhLWbIN%2FGSr%2FAwhREAAaDDYzNzQyMzE4MzgwNSIMVofCLcg1tIdWrD8FKtwDluDlxj6W3tysxd37QbNBmlL78%2FRRn%2BNaz3N2o4e4O%2Fzb3RUmdwQa5v62Fx8lQ9VZn2W6CRXj9NZkRx2L%2FOjw%2BvB%2FOeWp0cz1Tq3NLJMqiLZkVSNQoa2d%2F1pYNVWSsRh9pGSn7932ot95gxkY9EecQKocR5HFQIeFc1%2BMvAtQVXCRUyr7jgdy4AVJUhjTmFNnGRV0fpTnYvWEmt4JEYcCHtjalHRTwLpofZvO9mk7koJUZs7ztrXTIZjyBwv1gIGAjE2oZihrksPRvMsHKbPmxYv5F%2BXTnAA%2B96Pqypv%2FAI5NO2ADv%2FyNxjZDMJhB0tCMIX%2B0V%2BktgSh%2BmnMzAjnn2TWBeYKiRzPnWcexRXVHmhDf2TzsNe5RC6Elbo31eRa7KQL2cxq6%2BJ4Lw2R7ky0TZ14XBZy8a99nRtPnlsM9t3kfQ0gAz1slJI%2BggdSLK%2Fj%2BHtyoyX%2BcXe23hIz8kKNE%2FktAIEmTsrt2YUOG3igxE%2Fadn5Tlf09NANWBv3BarHitTw9LTL%2BLQsrz6EO3580vXyqBuAiNFJYqbV9YouPCyMYN%2BBmmPJsZJ4JvJaRbI5ZlWQ4qnGLeALgEtWukmQ1tlOD93CwuehXVwOZ%2FcN1vCdnKlZ%2FEDBDVTEzRkx8w7uqPvQY6pgFbohDWGj%2BO42XZv7gaqa6Ppm%2F9Mgxfi%2Byewd8IBNKYYroLfetzDeCqANdtjl8qZP21vRJUinJ%2B7QmfVxLn%2FAlwIfWqS2e%2Bf7iHOUCDE1TA7MJYNaW2h5pQh2r%2BaxXgmjNC6xmHokIEGceI%2FD%2BKPCfITgOYBXBDpumhh2P6hrqsQ21LIUp9ptj%2FkXC65mwXMQfXV54XAP3lqgVUxlXPmfXyXVnSCCLT&X-Amz-Signature=1960928fc68f3e546769cbeef048e9e0fc237a568071fdb997cc90ef53e35271&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 3. Histogram
A histogram is an important visual representation of data in categorical form. To view the data in a "Binned" form, use the histogram plot with a number of bins required or with the data points that mark the bin edges. The x-axis represents the data bins, and the y-axis represents the number of elements in each bin.
**Syntax:**
```python
plt.hist(x, bins)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/24e4424a-df87-40a1-b63b-195cbdc2e0ab/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466S23JSOF5%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T031813Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDgaCXVzLXdlc3QtMiJGMEQCIGN49pv%2BGzlDvEcmRHHziJ4uTCJ7T7rj0PUT6XRPaOXQAiA%2BjgQX8%2FTadK212587KT06jJgWio%2F9BcHfHhLWbIN%2FGSr%2FAwhREAAaDDYzNzQyMzE4MzgwNSIMVofCLcg1tIdWrD8FKtwDluDlxj6W3tysxd37QbNBmlL78%2FRRn%2BNaz3N2o4e4O%2Fzb3RUmdwQa5v62Fx8lQ9VZn2W6CRXj9NZkRx2L%2FOjw%2BvB%2FOeWp0cz1Tq3NLJMqiLZkVSNQoa2d%2F1pYNVWSsRh9pGSn7932ot95gxkY9EecQKocR5HFQIeFc1%2BMvAtQVXCRUyr7jgdy4AVJUhjTmFNnGRV0fpTnYvWEmt4JEYcCHtjalHRTwLpofZvO9mk7koJUZs7ztrXTIZjyBwv1gIGAjE2oZihrksPRvMsHKbPmxYv5F%2BXTnAA%2B96Pqypv%2FAI5NO2ADv%2FyNxjZDMJhB0tCMIX%2B0V%2BktgSh%2BmnMzAjnn2TWBeYKiRzPnWcexRXVHmhDf2TzsNe5RC6Elbo31eRa7KQL2cxq6%2BJ4Lw2R7ky0TZ14XBZy8a99nRtPnlsM9t3kfQ0gAz1slJI%2BggdSLK%2Fj%2BHtyoyX%2BcXe23hIz8kKNE%2FktAIEmTsrt2YUOG3igxE%2Fadn5Tlf09NANWBv3BarHitTw9LTL%2BLQsrz6EO3580vXyqBuAiNFJYqbV9YouPCyMYN%2BBmmPJsZJ4JvJaRbI5ZlWQ4qnGLeALgEtWukmQ1tlOD93CwuehXVwOZ%2FcN1vCdnKlZ%2FEDBDVTEzRkx8w7uqPvQY6pgFbohDWGj%2BO42XZv7gaqa6Ppm%2F9Mgxfi%2Byewd8IBNKYYroLfetzDeCqANdtjl8qZP21vRJUinJ%2B7QmfVxLn%2FAlwIfWqS2e%2Bf7iHOUCDE1TA7MJYNaW2h5pQh2r%2BaxXgmjNC6xmHokIEGceI%2FD%2BKPCfITgOYBXBDpumhh2P6hrqsQ21LIUp9ptj%2FkXC65mwXMQfXV54XAP3lqgVUxlXPmfXyXVnSCCLT&X-Amz-Signature=2cf6225489e512efac3633cbd946c874e4b870c1e393cbd4a3b0a3c5d673f359&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ab5a6dfe-51f5-43ee-bcb3-33dae4a1c7ad/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466S23JSOF5%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T031813Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDgaCXVzLXdlc3QtMiJGMEQCIGN49pv%2BGzlDvEcmRHHziJ4uTCJ7T7rj0PUT6XRPaOXQAiA%2BjgQX8%2FTadK212587KT06jJgWio%2F9BcHfHhLWbIN%2FGSr%2FAwhREAAaDDYzNzQyMzE4MzgwNSIMVofCLcg1tIdWrD8FKtwDluDlxj6W3tysxd37QbNBmlL78%2FRRn%2BNaz3N2o4e4O%2Fzb3RUmdwQa5v62Fx8lQ9VZn2W6CRXj9NZkRx2L%2FOjw%2BvB%2FOeWp0cz1Tq3NLJMqiLZkVSNQoa2d%2F1pYNVWSsRh9pGSn7932ot95gxkY9EecQKocR5HFQIeFc1%2BMvAtQVXCRUyr7jgdy4AVJUhjTmFNnGRV0fpTnYvWEmt4JEYcCHtjalHRTwLpofZvO9mk7koJUZs7ztrXTIZjyBwv1gIGAjE2oZihrksPRvMsHKbPmxYv5F%2BXTnAA%2B96Pqypv%2FAI5NO2ADv%2FyNxjZDMJhB0tCMIX%2B0V%2BktgSh%2BmnMzAjnn2TWBeYKiRzPnWcexRXVHmhDf2TzsNe5RC6Elbo31eRa7KQL2cxq6%2BJ4Lw2R7ky0TZ14XBZy8a99nRtPnlsM9t3kfQ0gAz1slJI%2BggdSLK%2Fj%2BHtyoyX%2BcXe23hIz8kKNE%2FktAIEmTsrt2YUOG3igxE%2Fadn5Tlf09NANWBv3BarHitTw9LTL%2BLQsrz6EO3580vXyqBuAiNFJYqbV9YouPCyMYN%2BBmmPJsZJ4JvJaRbI5ZlWQ4qnGLeALgEtWukmQ1tlOD93CwuehXVwOZ%2FcN1vCdnKlZ%2FEDBDVTEzRkx8w7uqPvQY6pgFbohDWGj%2BO42XZv7gaqa6Ppm%2F9Mgxfi%2Byewd8IBNKYYroLfetzDeCqANdtjl8qZP21vRJUinJ%2B7QmfVxLn%2FAlwIfWqS2e%2Bf7iHOUCDE1TA7MJYNaW2h5pQh2r%2BaxXgmjNC6xmHokIEGceI%2FD%2BKPCfITgOYBXBDpumhh2P6hrqsQ21LIUp9ptj%2FkXC65mwXMQfXV54XAP3lqgVUxlXPmfXyXVnSCCLT&X-Amz-Signature=4b6aaf824015baecfc76f7f44d9ba3521c8110d36976218f28d72438ec94d39e&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8f1b1d60-cf1b-42b3-9faa-f634c89c3f84/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466S23JSOF5%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T031813Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDgaCXVzLXdlc3QtMiJGMEQCIGN49pv%2BGzlDvEcmRHHziJ4uTCJ7T7rj0PUT6XRPaOXQAiA%2BjgQX8%2FTadK212587KT06jJgWio%2F9BcHfHhLWbIN%2FGSr%2FAwhREAAaDDYzNzQyMzE4MzgwNSIMVofCLcg1tIdWrD8FKtwDluDlxj6W3tysxd37QbNBmlL78%2FRRn%2BNaz3N2o4e4O%2Fzb3RUmdwQa5v62Fx8lQ9VZn2W6CRXj9NZkRx2L%2FOjw%2BvB%2FOeWp0cz1Tq3NLJMqiLZkVSNQoa2d%2F1pYNVWSsRh9pGSn7932ot95gxkY9EecQKocR5HFQIeFc1%2BMvAtQVXCRUyr7jgdy4AVJUhjTmFNnGRV0fpTnYvWEmt4JEYcCHtjalHRTwLpofZvO9mk7koJUZs7ztrXTIZjyBwv1gIGAjE2oZihrksPRvMsHKbPmxYv5F%2BXTnAA%2B96Pqypv%2FAI5NO2ADv%2FyNxjZDMJhB0tCMIX%2B0V%2BktgSh%2BmnMzAjnn2TWBeYKiRzPnWcexRXVHmhDf2TzsNe5RC6Elbo31eRa7KQL2cxq6%2BJ4Lw2R7ky0TZ14XBZy8a99nRtPnlsM9t3kfQ0gAz1slJI%2BggdSLK%2Fj%2BHtyoyX%2BcXe23hIz8kKNE%2FktAIEmTsrt2YUOG3igxE%2Fadn5Tlf09NANWBv3BarHitTw9LTL%2BLQsrz6EO3580vXyqBuAiNFJYqbV9YouPCyMYN%2BBmmPJsZJ4JvJaRbI5ZlWQ4qnGLeALgEtWukmQ1tlOD93CwuehXVwOZ%2FcN1vCdnKlZ%2FEDBDVTEzRkx8w7uqPvQY6pgFbohDWGj%2BO42XZv7gaqa6Ppm%2F9Mgxfi%2Byewd8IBNKYYroLfetzDeCqANdtjl8qZP21vRJUinJ%2B7QmfVxLn%2FAlwIfWqS2e%2Bf7iHOUCDE1TA7MJYNaW2h5pQh2r%2BaxXgmjNC6xmHokIEGceI%2FD%2BKPCfITgOYBXBDpumhh2P6hrqsQ21LIUp9ptj%2FkXC65mwXMQfXV54XAP3lqgVUxlXPmfXyXVnSCCLT&X-Amz-Signature=6e7c7fd9e8f2623c3553038ac9c23ceae1efb50add1463480c2b8263b4e25733&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/13ad0497-05fe-4eaa-984e-707b33e14761/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466S23JSOF5%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T031813Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDgaCXVzLXdlc3QtMiJGMEQCIGN49pv%2BGzlDvEcmRHHziJ4uTCJ7T7rj0PUT6XRPaOXQAiA%2BjgQX8%2FTadK212587KT06jJgWio%2F9BcHfHhLWbIN%2FGSr%2FAwhREAAaDDYzNzQyMzE4MzgwNSIMVofCLcg1tIdWrD8FKtwDluDlxj6W3tysxd37QbNBmlL78%2FRRn%2BNaz3N2o4e4O%2Fzb3RUmdwQa5v62Fx8lQ9VZn2W6CRXj9NZkRx2L%2FOjw%2BvB%2FOeWp0cz1Tq3NLJMqiLZkVSNQoa2d%2F1pYNVWSsRh9pGSn7932ot95gxkY9EecQKocR5HFQIeFc1%2BMvAtQVXCRUyr7jgdy4AVJUhjTmFNnGRV0fpTnYvWEmt4JEYcCHtjalHRTwLpofZvO9mk7koJUZs7ztrXTIZjyBwv1gIGAjE2oZihrksPRvMsHKbPmxYv5F%2BXTnAA%2B96Pqypv%2FAI5NO2ADv%2FyNxjZDMJhB0tCMIX%2B0V%2BktgSh%2BmnMzAjnn2TWBeYKiRzPnWcexRXVHmhDf2TzsNe5RC6Elbo31eRa7KQL2cxq6%2BJ4Lw2R7ky0TZ14XBZy8a99nRtPnlsM9t3kfQ0gAz1slJI%2BggdSLK%2Fj%2BHtyoyX%2BcXe23hIz8kKNE%2FktAIEmTsrt2YUOG3igxE%2Fadn5Tlf09NANWBv3BarHitTw9LTL%2BLQsrz6EO3580vXyqBuAiNFJYqbV9YouPCyMYN%2BBmmPJsZJ4JvJaRbI5ZlWQ4qnGLeALgEtWukmQ1tlOD93CwuehXVwOZ%2FcN1vCdnKlZ%2FEDBDVTEzRkx8w7uqPvQY6pgFbohDWGj%2BO42XZv7gaqa6Ppm%2F9Mgxfi%2Byewd8IBNKYYroLfetzDeCqANdtjl8qZP21vRJUinJ%2B7QmfVxLn%2FAlwIfWqS2e%2Bf7iHOUCDE1TA7MJYNaW2h5pQh2r%2BaxXgmjNC6xmHokIEGceI%2FD%2BKPCfITgOYBXBDpumhh2P6hrqsQ21LIUp9ptj%2FkXC65mwXMQfXV54XAP3lqgVUxlXPmfXyXVnSCCLT&X-Amz-Signature=23000d7a58b5d989d0ea4293742a84f68074fa02981ba3551030a91f385e5793&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 2. Box and Whisker Plot
A box plot shows the distribution of quantitative data in a way that facilitates comparisons between variables or across levels of a categorical variable. The box shows the quartiles of the dataset while the whiskers extend to show the rest of the distribution, except for points that are determined to be "outliers".
**Syntax:**
```python
sns.boxplot(x='header_1', y='header_2', data=df)
```
**Example Output:**


![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d207ae92-0a7c-4e2f-aa65-0ee5a2c33bf7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UGTWZUTA%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T031814Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDgaCXVzLXdlc3QtMiJGMEQCICaiWMyL5HYbNO%2Bs83dimCn3lTmvxuHupVIfPfFYG4utAiBNcHbSfw2%2FZF3hx7r1iphdPpM1myLh5XLYFlhy%2BiiqYyr%2FAwhREAAaDDYzNzQyMzE4MzgwNSIMMILS3tatI%2B6M15FmKtwDMpDEo3VxmYpuSRC7%2BSvl1ycC4ga3oe0JXrfrVKVCzSNkfvWSWwq1TkQFbhmxzLjt31G0Hf4RYMfpPed6eqth%2Bkx2vil8p87FVJEk3iUiiLwu3ihB7B7Y%2FraaiQtBIKlJDB%2Fhd%2BzaHT1JVXowdBBTMUIcM5OqkRPI036hHe0RRLItGbWMhrjB7GjyDd3dsanmech1J7CDi7N2oTt15FW5PvqnvNpz101o%2BL%2BDg63gHJ5ApLq6HCsBzlJJ%2FZLb7IOqXrmf8PTINY%2FmFGRN%2BzQl8DP2FLVHjNWmsDSHunKYjSzO2LsON54GKFazjlfbzFPhsC%2FjnmxiglKffCPyRhhEZIqukdd5A3j%2FdPu1Fnhrys0u3wXoGW0hDS93VQh7iEV6VnVqH7zjuxSJFBTr43RJVuZ2A%2FVwdgXzArhHDpfkPf2%2Fmoaou1u9jvNb5N8GWdc8U2w0YWL2Q68bZbxdFf%2BzAsWQBp4AIiGLP7JBHAA0BKBiIu3zEBGL1WQjR8%2FhWj2EZGgyuB%2FiGYnhv1TMi2G2jPdEaHC8yleDAMqtBJQgURHTCrS%2FO2z5TlPC3Rs32T3IYTs%2FK2DT267eXYhywQY6M5IMQo5HH3C8HLKAiA03Q0etnt6K4RJlGqNFbzsw8eqPvQY6pgGg%2B9Xjz2x85nFgKq910%2BZJj8tFszz4RKhnqQ23RFfHO3f4hP%2BpJ8eRgpEoTEHFRbXt90t%2B5AKNcOMLFzkY7NrMu9r0x5KzS9bW4rS5byJ7qokS66YKtzseqhiUhpFW%2F1z%2BTN3BDgdZbFsWczts36PUsvO3%2BpVBqI%2FCgWtns0o67IritCnzSTeqAB2zgTzIaAMqfMNkO52AHS2UjNAM55V3UShx347p&X-Amz-Signature=1290f3aac2d387b49fc1dc50fc40418d42fb2fe04ddf2641482cdd6ae9ca44ea&X-Amz-SignedHeaders=host&x-id=GetObject)

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0e516edc-7551-4792-ab18-0494db3c4c0c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667SS5Z7A3%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T031814Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDgaCXVzLXdlc3QtMiJHMEUCIQDENJ266vVFCt7bjc3DzlFK197CTRYINCfMHGiftT3rzwIgaJG%2FbJ90Kk0iyxPGM7nPAxkSaaFNwLQlJCh%2Fapdd0osq%2FwMIURAAGgw2Mzc0MjMxODM4MDUiDKNO8i1%2BVCNYevnjISrcA9FYwcQznyUGLKWwPIj7%2FKyBlvYXSFY27MT0kFeVUZT%2BYl9lmTsyY29bCyzJPQdqYyoCz2btHX53bf3a2DnSCjZVUoZVSg2EJk75jkZmNVclRrVF8AT%2Fzz6Cd4tHnOLe1rDgeXO1EZa7gsZU%2FMKGGlEeI7NMwCYjoUNT9XV0bFOe23SZ0uDegXQztACQkLV0%2FIjDKSyO0n5drcE4WsVdaGHGvJRU79s9huBTj6pDDxjcGdlzrwFX%2Fbr%2F9gEIwPwliuoOtt5I9sEvUjGLuTbmDPVOBoMP3rWwiGbWUzMvlFr%2Bd4EUqxe0ZNt8qNaOD0bnbaVzsf6RnNUxNHbYKCVzGUFeLnM%2FGV690nMgABg7gUv90XRZUDqk3Io00pQppMTLKh6LX3z%2BxqByKHqng7JvRZoke%2FkXFKcMCNWegxYlQoU%2F27LNB1lePiQmu%2FIihCfFORAu%2FyNG9mL6ms%2FKW%2FYN74D9jsSW1%2FcDlaVUE0QjN%2F3A4DvQZlsp7HbmIo4lcDOiAFYy%2B44Fi0n5b96BZP81fRC2EFCP6SWC2lXl7ksq2Un8L%2FABE70JsOa2cApdyZGWSxCTqbyILY%2BzNmmjJX7dNH%2FyyLWkZEJAWN9IH%2FNYblAZRAoCmUN3G9LKcl7iMMrqj70GOqUBojMYTQtSqKCnsPf%2B0yNBZ8cdVezopb82ZZK%2FW6bxHpw2yjh91FECoWHrNAIGgbmgFQi%2Br%2F0m61ooJYCMTxIOmbxRck4dxG0rnNlxQh80yft4a0vBU4uvhKghl4j1T5xRKXa0%2B3AV7CIK2m7GWNK1as86ECP71WJlzz%2F2KHUrhCBh1jnG8U5lurJS40F5%2FEBM%2F8NBk2FAmXKsoYc3Jf0Q7NMBSpUg&X-Amz-Signature=5ec2e0766894f654b8aae55cc631add0d235793fb90ba634cc5d0eb4b4b72f3b&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23a79b9d-2356-49a9-8fd9-65c6b0ab2cc5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466S23JSOF5%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T031813Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDgaCXVzLXdlc3QtMiJGMEQCIGN49pv%2BGzlDvEcmRHHziJ4uTCJ7T7rj0PUT6XRPaOXQAiA%2BjgQX8%2FTadK212587KT06jJgWio%2F9BcHfHhLWbIN%2FGSr%2FAwhREAAaDDYzNzQyMzE4MzgwNSIMVofCLcg1tIdWrD8FKtwDluDlxj6W3tysxd37QbNBmlL78%2FRRn%2BNaz3N2o4e4O%2Fzb3RUmdwQa5v62Fx8lQ9VZn2W6CRXj9NZkRx2L%2FOjw%2BvB%2FOeWp0cz1Tq3NLJMqiLZkVSNQoa2d%2F1pYNVWSsRh9pGSn7932ot95gxkY9EecQKocR5HFQIeFc1%2BMvAtQVXCRUyr7jgdy4AVJUhjTmFNnGRV0fpTnYvWEmt4JEYcCHtjalHRTwLpofZvO9mk7koJUZs7ztrXTIZjyBwv1gIGAjE2oZihrksPRvMsHKbPmxYv5F%2BXTnAA%2B96Pqypv%2FAI5NO2ADv%2FyNxjZDMJhB0tCMIX%2B0V%2BktgSh%2BmnMzAjnn2TWBeYKiRzPnWcexRXVHmhDf2TzsNe5RC6Elbo31eRa7KQL2cxq6%2BJ4Lw2R7ky0TZ14XBZy8a99nRtPnlsM9t3kfQ0gAz1slJI%2BggdSLK%2Fj%2BHtyoyX%2BcXe23hIz8kKNE%2FktAIEmTsrt2YUOG3igxE%2Fadn5Tlf09NANWBv3BarHitTw9LTL%2BLQsrz6EO3580vXyqBuAiNFJYqbV9YouPCyMYN%2BBmmPJsZJ4JvJaRbI5ZlWQ4qnGLeALgEtWukmQ1tlOD93CwuehXVwOZ%2FcN1vCdnKlZ%2FEDBDVTEzRkx8w7uqPvQY6pgFbohDWGj%2BO42XZv7gaqa6Ppm%2F9Mgxfi%2Byewd8IBNKYYroLfetzDeCqANdtjl8qZP21vRJUinJ%2B7QmfVxLn%2FAlwIfWqS2e%2Bf7iHOUCDE1TA7MJYNaW2h5pQh2r%2BaxXgmjNC6xmHokIEGceI%2FD%2BKPCfITgOYBXBDpumhh2P6hrqsQ21LIUp9ptj%2FkXC65mwXMQfXV54XAP3lqgVUxlXPmfXyXVnSCCLT&X-Amz-Signature=604ba9e688eea5417d5a7bda749dfa33a6809f89875a6380b2869f9c834b357d&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 4. KDE Plot
A Kernel Density Estimate (KDE) plot is a graph that creates a probability distribution curve for the data based upon its likelihood of occurrence on a specific value. This is created for a single vector of information.
**Syntax:**
```python
sns.kdeplot(X) || sns.kdeplot(df['age'])
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0d571213-2a2f-4921-a50b-880847aa05ee/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466S23JSOF5%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T031813Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDgaCXVzLXdlc3QtMiJGMEQCIGN49pv%2BGzlDvEcmRHHziJ4uTCJ7T7rj0PUT6XRPaOXQAiA%2BjgQX8%2FTadK212587KT06jJgWio%2F9BcHfHhLWbIN%2FGSr%2FAwhREAAaDDYzNzQyMzE4MzgwNSIMVofCLcg1tIdWrD8FKtwDluDlxj6W3tysxd37QbNBmlL78%2FRRn%2BNaz3N2o4e4O%2Fzb3RUmdwQa5v62Fx8lQ9VZn2W6CRXj9NZkRx2L%2FOjw%2BvB%2FOeWp0cz1Tq3NLJMqiLZkVSNQoa2d%2F1pYNVWSsRh9pGSn7932ot95gxkY9EecQKocR5HFQIeFc1%2BMvAtQVXCRUyr7jgdy4AVJUhjTmFNnGRV0fpTnYvWEmt4JEYcCHtjalHRTwLpofZvO9mk7koJUZs7ztrXTIZjyBwv1gIGAjE2oZihrksPRvMsHKbPmxYv5F%2BXTnAA%2B96Pqypv%2FAI5NO2ADv%2FyNxjZDMJhB0tCMIX%2B0V%2BktgSh%2BmnMzAjnn2TWBeYKiRzPnWcexRXVHmhDf2TzsNe5RC6Elbo31eRa7KQL2cxq6%2BJ4Lw2R7ky0TZ14XBZy8a99nRtPnlsM9t3kfQ0gAz1slJI%2BggdSLK%2Fj%2BHtyoyX%2BcXe23hIz8kKNE%2FktAIEmTsrt2YUOG3igxE%2Fadn5Tlf09NANWBv3BarHitTw9LTL%2BLQsrz6EO3580vXyqBuAiNFJYqbV9YouPCyMYN%2BBmmPJsZJ4JvJaRbI5ZlWQ4qnGLeALgEtWukmQ1tlOD93CwuehXVwOZ%2FcN1vCdnKlZ%2FEDBDVTEzRkx8w7uqPvQY6pgFbohDWGj%2BO42XZv7gaqa6Ppm%2F9Mgxfi%2Byewd8IBNKYYroLfetzDeCqANdtjl8qZP21vRJUinJ%2B7QmfVxLn%2FAlwIfWqS2e%2Bf7iHOUCDE1TA7MJYNaW2h5pQh2r%2BaxXgmjNC6xmHokIEGceI%2FD%2BKPCfITgOYBXBDpumhh2P6hrqsQ21LIUp9ptj%2FkXC65mwXMQfXV54XAP3lqgVUxlXPmfXyXVnSCCLT&X-Amz-Signature=070550f63e7d467fd8828be2cf2c5a5d4046db762d4f0cb2b98cd1b945546059&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/53752550-ef82-4ca9-a01a-09921f0282d0/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466S23JSOF5%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T031813Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDgaCXVzLXdlc3QtMiJGMEQCIGN49pv%2BGzlDvEcmRHHziJ4uTCJ7T7rj0PUT6XRPaOXQAiA%2BjgQX8%2FTadK212587KT06jJgWio%2F9BcHfHhLWbIN%2FGSr%2FAwhREAAaDDYzNzQyMzE4MzgwNSIMVofCLcg1tIdWrD8FKtwDluDlxj6W3tysxd37QbNBmlL78%2FRRn%2BNaz3N2o4e4O%2Fzb3RUmdwQa5v62Fx8lQ9VZn2W6CRXj9NZkRx2L%2FOjw%2BvB%2FOeWp0cz1Tq3NLJMqiLZkVSNQoa2d%2F1pYNVWSsRh9pGSn7932ot95gxkY9EecQKocR5HFQIeFc1%2BMvAtQVXCRUyr7jgdy4AVJUhjTmFNnGRV0fpTnYvWEmt4JEYcCHtjalHRTwLpofZvO9mk7koJUZs7ztrXTIZjyBwv1gIGAjE2oZihrksPRvMsHKbPmxYv5F%2BXTnAA%2B96Pqypv%2FAI5NO2ADv%2FyNxjZDMJhB0tCMIX%2B0V%2BktgSh%2BmnMzAjnn2TWBeYKiRzPnWcexRXVHmhDf2TzsNe5RC6Elbo31eRa7KQL2cxq6%2BJ4Lw2R7ky0TZ14XBZy8a99nRtPnlsM9t3kfQ0gAz1slJI%2BggdSLK%2Fj%2BHtyoyX%2BcXe23hIz8kKNE%2FktAIEmTsrt2YUOG3igxE%2Fadn5Tlf09NANWBv3BarHitTw9LTL%2BLQsrz6EO3580vXyqBuAiNFJYqbV9YouPCyMYN%2BBmmPJsZJ4JvJaRbI5ZlWQ4qnGLeALgEtWukmQ1tlOD93CwuehXVwOZ%2FcN1vCdnKlZ%2FEDBDVTEzRkx8w7uqPvQY6pgFbohDWGj%2BO42XZv7gaqa6Ppm%2F9Mgxfi%2Byewd8IBNKYYroLfetzDeCqANdtjl8qZP21vRJUinJ%2B7QmfVxLn%2FAlwIfWqS2e%2Bf7iHOUCDE1TA7MJYNaW2h5pQh2r%2BaxXgmjNC6xmHokIEGceI%2FD%2BKPCfITgOYBXBDpumhh2P6hrqsQ21LIUp9ptj%2FkXC65mwXMQfXV54XAP3lqgVUxlXPmfXyXVnSCCLT&X-Amz-Signature=01ad09a8a8ac5133871c903668b29272cccfa316225d1ee56fd696582f4d887d&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
## 4. Correlation Between Variables
Correlation is a statistical measure of the extent to which different variables are interdependent. It indicates how changes in one variable are associated with changes in another variable over time.
### Positive Correlation
Positive correlation indicates that as one variable increases, the other variable also tends to increase.
**Example: Engine Size and Price**
- **Positive Correlation:** Engine size increases, price also increases.
- **Visualization:** Scatter plot with a steep positive slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c7ea9b0-3ef3-4357-a9c3-554fc71b6b15/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZXP7QIAH%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T031815Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDgaCXVzLXdlc3QtMiJHMEUCIDy1p7qTCtArkx%2BxZqGH5Et1griG%2Bqu%2BXm0tctII%2BR1jAiEA5See0wpWxnGS%2BEtmJuP5awZvufi5m18Esbd3wNbVHYkq%2FwMIURAAGgw2Mzc0MjMxODM4MDUiDGdq4ucxiBRucEivfCrcA%2BRx0x9GCDNj%2Fs72FT8M35NAiXoG6pZJ0EydC6LuFbiLbSFStxVwxtix4BYWojdgaYP5PFF5HOG0jYXVmgfAgdut04Pf5GiMbidOoBtllFPW%2F6%2FKnf8hI1jaDesIkY3nFXAdIfMHcbsPWWwkvNy3Pt1kS%2FRVm9mhbFbrY54wQ2vTGnTZZPprmO2jnm6O5cOTvbpFa%2FMipoB48FkxBWPHMz7L5EB9vMJ72n7JWdBsKON03m3Y4eQA4pEJCOhAn0vnjfAKrTwaSb1YIM5AYgGiCmdQ%2BLB5K82qmXYZXBnbljeXu%2FlYpGg6GO83Vsk55dEZ%2FFC237ONO6bdpFs%2FgXCQnKdsvXNbdu5dAvCbwwMfyJLcfQU10ujYmCRUQA8tHQmITnT7XgLdY6CovCOtLd03zUz2GYwAGz%2BTFqoIcP%2BJsSe%2Ff1G543ruUiI6wpcygSUp2%2Bx9Yvg%2B72WHDLF6EN9ZcmOP84kwJNQqhP8PjQ0Rkt2pmeUMsvwUmf%2F0Sen00RMsh9fKd5U20dRZ1ABfxABrKGFaPUhB0TB8UFt2PiZ3FR9tRZJ63O9mizz4ueyq0NxpMZhU42x0ZnRer%2Bv6dD5X%2FjbE1WPrK0%2Fi1Tu1mKO5wXgXOxb0Ch6yi7URNc4gMOfqj70GOqUBDThQPhME2%2FboVGwFHO%2FeiAHA2LDKc30TQLQ069lGfVrG%2FF3p8oe13UiSfAmUbcGqD2Rnj85C7dqIkZflrHlR9b%2FqApPjC7lnyrjSRZypMMLMlM8kaGU8LrHZUXLellBW94DucNrKVYiHyNZPKOJb6k5klp%2BpDMbrk8pgaqy8%2FaWs%2BA9Z%2FB6ZzaZqS5LgbehmecO%2FPz1y1iHLS4yYnfSv2JdsWH8J&X-Amz-Signature=a229ed50728618af1343f57d17bb8a87cca927390c9d96e1bc0bedfe3c3e76a6&X-Amz-SignedHeaders=host&x-id=GetObject)
**Explanation:** When engine size increases, there is a corresponding increase in the price of the vehicle. This positive correlation suggests that larger engines tend to be associated with higher prices in the market.
___
### Negative Correlation
Negative correlation indicates that as one variable increases, the other variable tends to decrease.
**Example: Highway Miles per Gallon and Price**
- **Negative Correlation:** As highway miles per gallon increases, price decreases.
- **Visualization:** Scatter plot with a steep negative slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/10f1f798-9cc4-4df2-a9c1-5a339f554a0b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466W5BK6WEP%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T031815Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDgaCXVzLXdlc3QtMiJGMEQCIFZvDgzGKAl1gbXP%2BfLPXqNhc121G4ufikRgFvnol74nAiBCBMz9H9pfLezvyqRcBykxCzMrvP1gTDlEYXZloyKVJyr%2FAwhREAAaDDYzNzQyMzE4MzgwNSIM2O2TrJo53fxdCcGNKtwDPgtFjdNcwqc6Orp6uuG7X9s8vrKpNvfBSUmG8%2BqA27B7vYGp9NgypR940nEmTT%2BoSui1I%2FeBpL787er7Ku9btJtBBORRt5hOa7Ebea6C6L2jqg3SD%2FNQB84fuQuN4alMveTdxguCZl3rAIwWDNjqy0TBfzUQmbrnvZ%2BLOGKg3%2FkxLMv8gX%2FUpcejd3SmxYaVM3t7iNdMP2hbvZcpcjrtPTAzSvAQpQRJ0jyt4glacpjiy7R%2FijwQamyLSUyKSUIjEKd%2F%2BhU%2Fl3W%2B318aID65Dc3E41%2BTRCiyTjznkO711wr3WTGLbFdfroP2jNfAJiYaB3H%2B0teawKAxTXcj8RU%2FvHctIxNRiJLqLRQ8pQgG8KR%2FWFYfgVq0xHA5pbgWwm0dp1ILXQmxfQeaXYn%2FIqHYd2qPx8%2BA%2ByK%2BqO19yrQhrpMF3wD0jpf4r5tojZBMY7J4mPE1woruhO%2FgPPpa25acK7ToFzVsug0H8sYV9ZFGwXBrxKKCyBH3908vOWdpuEBLQlHSJb9bdd1hnpo6FMeUSjxXUl5RtTjhmGRc0QdC5aO%2FOoOVsOZ1vD%2Bn2H0%2BemP3%2BmEBwy12Bh%2Fpw4A18FiG3rC4e9WerzFTFJdJGf4FeE%2Fwfz0GoG3Y24pJgJww5eqPvQY6pgHd6DQhtv5V4vOo8wD%2FpI%2FaQ2QOaYzmwj8%2Bf3BfnAJLmj8s3KH95uges%2B3jFN1CaWB9wH%2FE%2BHe33ZlZmP0%2FLVqwD2c9FE2SPao7b0w3JHQJlxHCOf7WqtVAQp%2BTXIM9TYS9fI0ZqY1cfz6%2FkduZhZnZLxm7q9qgaON1GTDx0VQvLgHHTX4254ieWfvgWAjzD%2BncYN7OttDA6r2m8Z71UhY3pVg0wl6o&X-Amz-Signature=38f97d43e03a6a85afcf621b9356b60a365db9db0437544cbf547a84bd5606d1&X-Amz-SignedHeaders=host&x-id=GetObject)
**Explanation:** When highway miles per gallon increases, the price of the vehicle tends to decrease. This negative correlation suggests that cars with higher fuel efficiency (more miles per gallon) are generally priced lower in the market.
___
### Weak Correlation
Weak correlation indicates a lack of strong relationship between the variables.
**Example: RPM and Price**
- **Weak Correlation:** Low and high RPM values show varied prices, indicating no strong predictive relationship.
- **Visualization:** Scatter plot with no clear trend or slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9f914514-8914-4bf4-ac84-d9e3077f6eb1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZUQTASM4%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T031814Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDgaCXVzLXdlc3QtMiJGMEQCIEgLgXPo9WBG%2BNB4qNno%2F1iDwlmr%2BVTx9wn%2Fv5vghmY%2BAiAp9Vkm8CMUN%2BVHVkd6fpcxIm%2FlMjlkKNku6gQSGMoqbSr%2FAwhREAAaDDYzNzQyMzE4MzgwNSIMk0E9gLYLqRXgqGCSKtwD2CHKRn4LYLKf62ZThIVSYPjXJZotALt74DR3qGD1HqC9ftispsNQWI1%2FztyrAg95zLfU%2B02Ia%2FVvzpe4altbWHd6IKA90uZo314t%2Bzs0AToAL2j1KZ88gYModkn6LEdLCLX%2BU3JVhS%2Fv0qJCECIM9R3AT6dMDwBbp%2FJOtEneDxQL93KC%2BPlKDDpBXao9LO8WXNceInKM0Sx4hljE0tzlmVgnc4EKn6jutKXThHYAMPAOJX18nvUIMkqbeZ4yqCENTvpg9pYy7A37GxCsVMyEK1MzqFoC5KzyW1Zs9pSeWLbts8GQGU4XoCi9hdrCq0Z9wUDacNMbmMB209aQgcx1ploBCOov1Uh1dBeHyx0q180GfeVi553oK%2Bx6kmvbPhkkMbUYQFGFGdcuZcjv%2FzfInfe80NBBQkzRjTX8sLG6UUeOfboPpEWipsI7QVzrNX5n%2BCz56NiVWJQaxrc9soXVcSMiTzsCxZyXVxHi%2FGIih34%2F%2FP63IHs3VC7%2FJ%2FASSeJ%2BhcICNoWSIyp3aYXGCMsBChrBtKfHXRLXLRUBjafE4sjRUCtIAlARlMrfnxznNDDRkADV9OEiXtaNfW9qEJXkJ31f2QSZQ1CkPVZJgdRNljzIBY7oViyuaPGDkVUwleuPvQY6pgEj%2BKYRzvVdX3GfD0zsZnmjcbmWbsrTT%2BXaDa9O1Roy5kZY30HBFRAJ7L%2BA4v0OieoLT9%2BB3%2FYNOOOwVqb5cXFvJ%2FkOHvMCVVD%2B%2BHNpaCeLWtyBf6V5xEG26ZXiZfhQ7jLPhF6yfRFPFlz6wTUY16Zn%2FRkSOeagNJEw6ot6iJNLTcvNiZ0C36jchQpSvhvXF%2BaProhdekkOMUHg4Kb94TbfhqRAX10U&X-Amz-Signature=038e8d0316f7490ed2014a155aff5a85c552e40d30c4c37c53c77e3a0ccf410d&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f18086e5-5b04-4fbf-8309-8944ab20d213/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466X5NJQNWQ%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T031814Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDgaCXVzLXdlc3QtMiJHMEUCIGmPilELLrCTEwqPnCjj3UnWFgnKZrQ86wTgKc1xSQKPAiEA14FQuyNZUBvjW2Hv%2F1HYmUCRz8fYDjC%2BSqjskYfN7Ccq%2FwMIURAAGgw2Mzc0MjMxODM4MDUiDAyzvZ5VVkwt7yNSiyrcA%2FDCUNXK6enfN465iURw5i9Knlbeuj4ovsYNukQ0m5VSTvgylNU0GIZVaOKYRq1PcQmCxCZpVc7ZGmvzMD9jRL%2FMeNvK8TGthwVXccl9P%2F8vx3ZTU%2Fd%2Fhf2%2FLq1Lfde6T229HExQ1jUDJQ4tYMMaEW%2FZagkpiacuXTpQSnBwFFQ9xpn5ySc8ug6lJGqyjnfszToq4KA6nijznykW69zjBo5rvFIR9br6PBlzmrz3uSl5s53HP%2FnFCCJpN16ZZ2iKqm70jw1fjImOBsPMp%2FKADflND9GYQ4kmWuJ2fzxCOCgNDS7sMfTyuWlDFU6OGJS2NzCZymKJATaFOM%2BwwoqabtJwwWAOCDO3OAQL9CFG10M0v6mFREsLkNWtAoi4ezlamqag4IZ5jgMkbh6RYkR1eHB%2BviaMvv7zp2bgFTnAreNoqa8kY%2BLF2MHQxVPPuzVyBWON%2F3Tk1UUrqsIcywxfIM%2FeXxHS0aiW4sNFCXfvlnzqEn1SP0EDEzR43U9EVGROg%2FuSCPHfpgx3DH3QRiJywKALA0W5uYv5i1b%2B1Yf4%2B0WAa4PhTucYnYPhMW8yYr3TwSoqjsjia2eMHZGBLJuPS4FMZMmjCaArF9SgF81Zmu4qrCjdwbOPTAVAm0sLMMzqj70GOqUBkeDihwtT%2FYi9VxTDF16nmplu%2BqMOSR4L3RASN5vfzQiwlwv5wqdnRC2UKQzxOdP7NDr5xBze0hCi4ytEUsA86ajcVH9rr5kGAc5lW%2BS7RGSs%2FXlPstPo0PLaIUBCnyfoGdUgHx9faizLjDdmamYqgsJer4m6avY8k4U31PJWpdLVrg8%2FMwIF9vnm3xynAMqSTATJ3LbfrKPHbqo4yIP%2Bei%2B3B3lK&X-Amz-Signature=e91ce9a8483a277bd6f61121283e99d6ba76f4983e7bfd7b0b8af737be78c1c8&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Correlation Plot
Heatmap visualizes correlations among variables. Color scheme indicates Pearson correlation coefficients. Dark red diagonal line shows perfect correlation (value of 1) between variables and themselves.
This heatmap offers overview of variable relationships and their link with price.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cd3b341e-cc1a-45f7-8aec-cdc00436d270/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466X5NJQNWQ%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T031814Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDgaCXVzLXdlc3QtMiJHMEUCIGmPilELLrCTEwqPnCjj3UnWFgnKZrQ86wTgKc1xSQKPAiEA14FQuyNZUBvjW2Hv%2F1HYmUCRz8fYDjC%2BSqjskYfN7Ccq%2FwMIURAAGgw2Mzc0MjMxODM4MDUiDAyzvZ5VVkwt7yNSiyrcA%2FDCUNXK6enfN465iURw5i9Knlbeuj4ovsYNukQ0m5VSTvgylNU0GIZVaOKYRq1PcQmCxCZpVc7ZGmvzMD9jRL%2FMeNvK8TGthwVXccl9P%2F8vx3ZTU%2Fd%2Fhf2%2FLq1Lfde6T229HExQ1jUDJQ4tYMMaEW%2FZagkpiacuXTpQSnBwFFQ9xpn5ySc8ug6lJGqyjnfszToq4KA6nijznykW69zjBo5rvFIR9br6PBlzmrz3uSl5s53HP%2FnFCCJpN16ZZ2iKqm70jw1fjImOBsPMp%2FKADflND9GYQ4kmWuJ2fzxCOCgNDS7sMfTyuWlDFU6OGJS2NzCZymKJATaFOM%2BwwoqabtJwwWAOCDO3OAQL9CFG10M0v6mFREsLkNWtAoi4ezlamqag4IZ5jgMkbh6RYkR1eHB%2BviaMvv7zp2bgFTnAreNoqa8kY%2BLF2MHQxVPPuzVyBWON%2F3Tk1UUrqsIcywxfIM%2FeXxHS0aiW4sNFCXfvlnzqEn1SP0EDEzR43U9EVGROg%2FuSCPHfpgx3DH3QRiJywKALA0W5uYv5i1b%2B1Yf4%2B0WAa4PhTucYnYPhMW8yYr3TwSoqjsjia2eMHZGBLJuPS4FMZMmjCaArF9SgF81Zmu4qrCjdwbOPTAVAm0sLMMzqj70GOqUBkeDihwtT%2FYi9VxTDF16nmplu%2BqMOSR4L3RASN5vfzQiwlwv5wqdnRC2UKQzxOdP7NDr5xBze0hCi4ytEUsA86ajcVH9rr5kGAc5lW%2BS7RGSs%2FXlPstPo0PLaIUBCnyfoGdUgHx9faizLjDdmamYqgsJer4m6avY8k4U31PJWpdLVrg8%2FMwIF9vnm3xynAMqSTATJ3LbfrKPHbqo4yIP%2Bei%2B3B3lK&X-Amz-Signature=88aa839f408732562531514df1a268f5a7208cc6e1b363f0eeba6ba42c60be98&X-Amz-SignedHeaders=host&x-id=GetObject)

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
