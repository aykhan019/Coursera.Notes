

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7e6d594d-952e-44b6-97ea-31225882aea6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667A57RB3E%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T091651Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGEwYRA27KO3yRF%2BhKW8h0a0kWaW6m7o0dey8SEI95RhAiBN6E0P%2Ba3nm497XrXhnBmsUouqv75IDgBtzvFU4ejJDir%2FAwgREAAaDDYzNzQyMzE4MzgwNSIMhYEMxPi0Pc9oFAPhKtwDVeBCdxmbwgw9qGUpr%2Fy41rAz1V16zCWI4ARIfF3av9WEKEuK8s%2FBVB3sNG4z%2FVWUpv7TQFqp2S5XJ97mXYghhPvRCgHyYWnP%2BVJc79GQwW4%2FKSrlPV%2FqWtZbBkVZ9Vx8U%2FD8wnVRs0wot7SnFoS53n8RKavsRaj8QaAFz97%2FPJRADCagZBKS6I6Qe%2Ft8at0DPV6gniXINPImYeJFXd0I%2F4Y8ef2zMRM0bdsf5tZWEJR2gwDKeCj7m9FmVEe2knKa43hXf90%2Bj8kadlLZ%2Bh3eGXmmuf%2BiFsYl5cj4xyMI8zkZNi405MfOl8gm94W%2BkuXaK9%2B8MoBOtFKSj%2BCAaTKQaKls%2BQkoJ%2Far7NhibuRfoZ7CMYrfQDzAU8F%2BBAJjOMzRryL6mkI3X2xW7Ddf6zRj26gPbq7gc4RdO4uXmrt8lL7FY7Q%2BeXB8qXogfb%2FWjsQH2C%2BIXGUZuab%2FOWqTFcvu8zm%2BrPrVCR3uIvnBlA0WqkH4%2BToLPcExj%2B3JtGI1E5qZkPH0FQQqa16K18mzSYs3LiMswqZKr4IaY45La1nCaWIjzPCSJbMpc8SkfHzLAOKZpQZU7qdvRagnB%2BmUDJUWcYaGp6wswoV6UTABR%2BvZmAop4isIotfKrb0zlw8wjfOBvQY6pgEEtH0%2BTM%2B0gCQ%2FQ%2FJpH8mDleOhywG2WsPEsQBS7cyRiJHM0WyMhNy1R5IqZVdnvwXq%2B6y922SX73GYSGwtAPvjOosL8xhqNINxgp8GZl8UMtfB5Zt5rnx%2FY1lAlTzNg6RqeWD2enw%2F341POpzzzMFLbERuJ%2Ft2cFpEvwZFAk3aFPIEjTKiM%2FBM0eLwnC76i0lLFpxTThXDDz3xL67%2BedwED79HzSac&X-Amz-Signature=58aa516ae602dc8aa6dd6ed516de5737c1e150be3c24325beec590191b601e77&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cbfaed9e-b398-4902-8936-dea058b21def/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667A57RB3E%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T091651Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGEwYRA27KO3yRF%2BhKW8h0a0kWaW6m7o0dey8SEI95RhAiBN6E0P%2Ba3nm497XrXhnBmsUouqv75IDgBtzvFU4ejJDir%2FAwgREAAaDDYzNzQyMzE4MzgwNSIMhYEMxPi0Pc9oFAPhKtwDVeBCdxmbwgw9qGUpr%2Fy41rAz1V16zCWI4ARIfF3av9WEKEuK8s%2FBVB3sNG4z%2FVWUpv7TQFqp2S5XJ97mXYghhPvRCgHyYWnP%2BVJc79GQwW4%2FKSrlPV%2FqWtZbBkVZ9Vx8U%2FD8wnVRs0wot7SnFoS53n8RKavsRaj8QaAFz97%2FPJRADCagZBKS6I6Qe%2Ft8at0DPV6gniXINPImYeJFXd0I%2F4Y8ef2zMRM0bdsf5tZWEJR2gwDKeCj7m9FmVEe2knKa43hXf90%2Bj8kadlLZ%2Bh3eGXmmuf%2BiFsYl5cj4xyMI8zkZNi405MfOl8gm94W%2BkuXaK9%2B8MoBOtFKSj%2BCAaTKQaKls%2BQkoJ%2Far7NhibuRfoZ7CMYrfQDzAU8F%2BBAJjOMzRryL6mkI3X2xW7Ddf6zRj26gPbq7gc4RdO4uXmrt8lL7FY7Q%2BeXB8qXogfb%2FWjsQH2C%2BIXGUZuab%2FOWqTFcvu8zm%2BrPrVCR3uIvnBlA0WqkH4%2BToLPcExj%2B3JtGI1E5qZkPH0FQQqa16K18mzSYs3LiMswqZKr4IaY45La1nCaWIjzPCSJbMpc8SkfHzLAOKZpQZU7qdvRagnB%2BmUDJUWcYaGp6wswoV6UTABR%2BvZmAop4isIotfKrb0zlw8wjfOBvQY6pgEEtH0%2BTM%2B0gCQ%2FQ%2FJpH8mDleOhywG2WsPEsQBS7cyRiJHM0WyMhNy1R5IqZVdnvwXq%2B6y922SX73GYSGwtAPvjOosL8xhqNINxgp8GZl8UMtfB5Zt5rnx%2FY1lAlTzNg6RqeWD2enw%2F341POpzzzMFLbERuJ%2Ft2cFpEvwZFAk3aFPIEjTKiM%2FBM0eLwnC76i0lLFpxTThXDDz3xL67%2BedwED79HzSac&X-Amz-Signature=e1abd01463ed117ef983438e64d72ed1b86ef9f50cbca65a52cc696eab9d3c04&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/91181646-b1e0-4433-9711-6259a96a9247/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667A57RB3E%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T091651Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGEwYRA27KO3yRF%2BhKW8h0a0kWaW6m7o0dey8SEI95RhAiBN6E0P%2Ba3nm497XrXhnBmsUouqv75IDgBtzvFU4ejJDir%2FAwgREAAaDDYzNzQyMzE4MzgwNSIMhYEMxPi0Pc9oFAPhKtwDVeBCdxmbwgw9qGUpr%2Fy41rAz1V16zCWI4ARIfF3av9WEKEuK8s%2FBVB3sNG4z%2FVWUpv7TQFqp2S5XJ97mXYghhPvRCgHyYWnP%2BVJc79GQwW4%2FKSrlPV%2FqWtZbBkVZ9Vx8U%2FD8wnVRs0wot7SnFoS53n8RKavsRaj8QaAFz97%2FPJRADCagZBKS6I6Qe%2Ft8at0DPV6gniXINPImYeJFXd0I%2F4Y8ef2zMRM0bdsf5tZWEJR2gwDKeCj7m9FmVEe2knKa43hXf90%2Bj8kadlLZ%2Bh3eGXmmuf%2BiFsYl5cj4xyMI8zkZNi405MfOl8gm94W%2BkuXaK9%2B8MoBOtFKSj%2BCAaTKQaKls%2BQkoJ%2Far7NhibuRfoZ7CMYrfQDzAU8F%2BBAJjOMzRryL6mkI3X2xW7Ddf6zRj26gPbq7gc4RdO4uXmrt8lL7FY7Q%2BeXB8qXogfb%2FWjsQH2C%2BIXGUZuab%2FOWqTFcvu8zm%2BrPrVCR3uIvnBlA0WqkH4%2BToLPcExj%2B3JtGI1E5qZkPH0FQQqa16K18mzSYs3LiMswqZKr4IaY45La1nCaWIjzPCSJbMpc8SkfHzLAOKZpQZU7qdvRagnB%2BmUDJUWcYaGp6wswoV6UTABR%2BvZmAop4isIotfKrb0zlw8wjfOBvQY6pgEEtH0%2BTM%2B0gCQ%2FQ%2FJpH8mDleOhywG2WsPEsQBS7cyRiJHM0WyMhNy1R5IqZVdnvwXq%2B6y922SX73GYSGwtAPvjOosL8xhqNINxgp8GZl8UMtfB5Zt5rnx%2FY1lAlTzNg6RqeWD2enw%2F341POpzzzMFLbERuJ%2Ft2cFpEvwZFAk3aFPIEjTKiM%2FBM0eLwnC76i0lLFpxTThXDDz3xL67%2BedwED79HzSac&X-Amz-Signature=7ae30b49f893973cfd55e7637139abf1235f304b88dc0163191ef345917a1adc&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/09aba1c0-0d55-41dd-852a-a04c5b8a3fac/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WU5LWIB6%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T091652Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCsgxUB49sYS6FK%2F6gZ3nqgrChINS5FEj%2FeXAyICueSSAIgN3AKptThuorvFyTR2Q9MBxhgcQ%2FgvUZrqWN8JUAcSjkq%2FwMIERAAGgw2Mzc0MjMxODM4MDUiDMjJCIKejHnlYmE0pCrcAzhOoyDt4ZXpDTLFYfoLC%2B60OvXm9bebpZBB%2FsvU20zjgUS4I6CHrOA3zvTmMjhVGZ%2BGoFTkaK54cvDXGQHn%2FS4Em253rZEiN%2BMIcVJ2lGn7NtlR%2B%2F7qQpU4utf9dJUor%2FojYf3wWje4uAkREKsicQ%2FWvGOzue9K3gMN8zHQn6l%2FCUPRz1Gs3mo7ffTai%2BdMo1sor8jcOJ230e5vSvQQ34NBGU5FsFlVbEFf6lCZD5Dj4Ig6C8xPBiw9%2F4hSil8RlAkIakIPykaTzGf2GqYRt23nHZIL3Pgv6XWYcTz82%2FX9Npsg2E%2B5lTp%2BIE1l71rfomoeBkdtXuuFTaUor6ZuyTrcQbKMymTbaOLoifBiHHRMwWFOVSRueLY%2Fxo1pPK6LZNPhHDXlMLaUv1Gg2yyae%2Fh6DuVRBDzMVS0WYUzEtTNAYbkvTQOm4%2FESQuGkNVSAiIOC7ABxy1QByMI6RsQf2%2F%2BDHOupR1J83Na%2FBk9BkWAPXULoVXlrEroDlGBdLK5hFVowF36fJ8PpC4%2FhEx1NZJ3PlEVahVV%2Fg5usiPALQF63hgs2QBqbNBnDCNUw0BW1TAcnNtGXfkzymeSZII5wQc13y3M07OjWmTIGtm87HaB%2FRxc71LRG5TAwvHboMI7zgb0GOqUBtpGICe2Evwi%2Bx%2BUgO876ZC0jeZ7GT6sOgalUtyPGTWnZ%2FmhVdcLnYv0gzR2o9xQlONsjScoWptLFb3L3W9jTcrOqdb5Q6kh8gEyYe7XgByTRclurVUgXW7bWf7F0Oq2QUA6oBmy80xkrPHvdhVxwJQayn6QPu9ln82L3fdB8u%2ByENKh2Y3nzxN4BGM%2BlA85VjMQMFm8%2F%2FYbHehoxIFLkin2R8tZu&X-Amz-Signature=17cecd4fae884a254860b8f06230853b76202ee542e361eec4717c1ad7c12da6&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 2. Scatter Plot
Scatter plots present the relationship between two variables in a dataset. It represents data points on a two-dimensional plane. The independent variable or attribute is plotted on the X-axis, while the dependent variable is plotted on the Y-axis.
**Syntax:**
```python
plt.scatter(x, y)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23708af9-659f-4f23-b626-1a4292d7842c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WU5LWIB6%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T091652Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCsgxUB49sYS6FK%2F6gZ3nqgrChINS5FEj%2FeXAyICueSSAIgN3AKptThuorvFyTR2Q9MBxhgcQ%2FgvUZrqWN8JUAcSjkq%2FwMIERAAGgw2Mzc0MjMxODM4MDUiDMjJCIKejHnlYmE0pCrcAzhOoyDt4ZXpDTLFYfoLC%2B60OvXm9bebpZBB%2FsvU20zjgUS4I6CHrOA3zvTmMjhVGZ%2BGoFTkaK54cvDXGQHn%2FS4Em253rZEiN%2BMIcVJ2lGn7NtlR%2B%2F7qQpU4utf9dJUor%2FojYf3wWje4uAkREKsicQ%2FWvGOzue9K3gMN8zHQn6l%2FCUPRz1Gs3mo7ffTai%2BdMo1sor8jcOJ230e5vSvQQ34NBGU5FsFlVbEFf6lCZD5Dj4Ig6C8xPBiw9%2F4hSil8RlAkIakIPykaTzGf2GqYRt23nHZIL3Pgv6XWYcTz82%2FX9Npsg2E%2B5lTp%2BIE1l71rfomoeBkdtXuuFTaUor6ZuyTrcQbKMymTbaOLoifBiHHRMwWFOVSRueLY%2Fxo1pPK6LZNPhHDXlMLaUv1Gg2yyae%2Fh6DuVRBDzMVS0WYUzEtTNAYbkvTQOm4%2FESQuGkNVSAiIOC7ABxy1QByMI6RsQf2%2F%2BDHOupR1J83Na%2FBk9BkWAPXULoVXlrEroDlGBdLK5hFVowF36fJ8PpC4%2FhEx1NZJ3PlEVahVV%2Fg5usiPALQF63hgs2QBqbNBnDCNUw0BW1TAcnNtGXfkzymeSZII5wQc13y3M07OjWmTIGtm87HaB%2FRxc71LRG5TAwvHboMI7zgb0GOqUBtpGICe2Evwi%2Bx%2BUgO876ZC0jeZ7GT6sOgalUtyPGTWnZ%2FmhVdcLnYv0gzR2o9xQlONsjScoWptLFb3L3W9jTcrOqdb5Q6kh8gEyYe7XgByTRclurVUgXW7bWf7F0Oq2QUA6oBmy80xkrPHvdhVxwJQayn6QPu9ln82L3fdB8u%2ByENKh2Y3nzxN4BGM%2BlA85VjMQMFm8%2F%2FYbHehoxIFLkin2R8tZu&X-Amz-Signature=3b953532db08b1d44109528a64493b89fc18008f4e326fbc1239e62eb0155ee9&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 3. Histogram
A histogram is an important visual representation of data in categorical form. To view the data in a "Binned" form, use the histogram plot with a number of bins required or with the data points that mark the bin edges. The x-axis represents the data bins, and the y-axis represents the number of elements in each bin.
**Syntax:**
```python
plt.hist(x, bins)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/24e4424a-df87-40a1-b63b-195cbdc2e0ab/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WU5LWIB6%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T091652Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCsgxUB49sYS6FK%2F6gZ3nqgrChINS5FEj%2FeXAyICueSSAIgN3AKptThuorvFyTR2Q9MBxhgcQ%2FgvUZrqWN8JUAcSjkq%2FwMIERAAGgw2Mzc0MjMxODM4MDUiDMjJCIKejHnlYmE0pCrcAzhOoyDt4ZXpDTLFYfoLC%2B60OvXm9bebpZBB%2FsvU20zjgUS4I6CHrOA3zvTmMjhVGZ%2BGoFTkaK54cvDXGQHn%2FS4Em253rZEiN%2BMIcVJ2lGn7NtlR%2B%2F7qQpU4utf9dJUor%2FojYf3wWje4uAkREKsicQ%2FWvGOzue9K3gMN8zHQn6l%2FCUPRz1Gs3mo7ffTai%2BdMo1sor8jcOJ230e5vSvQQ34NBGU5FsFlVbEFf6lCZD5Dj4Ig6C8xPBiw9%2F4hSil8RlAkIakIPykaTzGf2GqYRt23nHZIL3Pgv6XWYcTz82%2FX9Npsg2E%2B5lTp%2BIE1l71rfomoeBkdtXuuFTaUor6ZuyTrcQbKMymTbaOLoifBiHHRMwWFOVSRueLY%2Fxo1pPK6LZNPhHDXlMLaUv1Gg2yyae%2Fh6DuVRBDzMVS0WYUzEtTNAYbkvTQOm4%2FESQuGkNVSAiIOC7ABxy1QByMI6RsQf2%2F%2BDHOupR1J83Na%2FBk9BkWAPXULoVXlrEroDlGBdLK5hFVowF36fJ8PpC4%2FhEx1NZJ3PlEVahVV%2Fg5usiPALQF63hgs2QBqbNBnDCNUw0BW1TAcnNtGXfkzymeSZII5wQc13y3M07OjWmTIGtm87HaB%2FRxc71LRG5TAwvHboMI7zgb0GOqUBtpGICe2Evwi%2Bx%2BUgO876ZC0jeZ7GT6sOgalUtyPGTWnZ%2FmhVdcLnYv0gzR2o9xQlONsjScoWptLFb3L3W9jTcrOqdb5Q6kh8gEyYe7XgByTRclurVUgXW7bWf7F0Oq2QUA6oBmy80xkrPHvdhVxwJQayn6QPu9ln82L3fdB8u%2ByENKh2Y3nzxN4BGM%2BlA85VjMQMFm8%2F%2FYbHehoxIFLkin2R8tZu&X-Amz-Signature=3c7926c39696ddbb34c173291bd395377edfd81f1e342d090a38f77aefd8966c&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ab5a6dfe-51f5-43ee-bcb3-33dae4a1c7ad/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WU5LWIB6%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T091652Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCsgxUB49sYS6FK%2F6gZ3nqgrChINS5FEj%2FeXAyICueSSAIgN3AKptThuorvFyTR2Q9MBxhgcQ%2FgvUZrqWN8JUAcSjkq%2FwMIERAAGgw2Mzc0MjMxODM4MDUiDMjJCIKejHnlYmE0pCrcAzhOoyDt4ZXpDTLFYfoLC%2B60OvXm9bebpZBB%2FsvU20zjgUS4I6CHrOA3zvTmMjhVGZ%2BGoFTkaK54cvDXGQHn%2FS4Em253rZEiN%2BMIcVJ2lGn7NtlR%2B%2F7qQpU4utf9dJUor%2FojYf3wWje4uAkREKsicQ%2FWvGOzue9K3gMN8zHQn6l%2FCUPRz1Gs3mo7ffTai%2BdMo1sor8jcOJ230e5vSvQQ34NBGU5FsFlVbEFf6lCZD5Dj4Ig6C8xPBiw9%2F4hSil8RlAkIakIPykaTzGf2GqYRt23nHZIL3Pgv6XWYcTz82%2FX9Npsg2E%2B5lTp%2BIE1l71rfomoeBkdtXuuFTaUor6ZuyTrcQbKMymTbaOLoifBiHHRMwWFOVSRueLY%2Fxo1pPK6LZNPhHDXlMLaUv1Gg2yyae%2Fh6DuVRBDzMVS0WYUzEtTNAYbkvTQOm4%2FESQuGkNVSAiIOC7ABxy1QByMI6RsQf2%2F%2BDHOupR1J83Na%2FBk9BkWAPXULoVXlrEroDlGBdLK5hFVowF36fJ8PpC4%2FhEx1NZJ3PlEVahVV%2Fg5usiPALQF63hgs2QBqbNBnDCNUw0BW1TAcnNtGXfkzymeSZII5wQc13y3M07OjWmTIGtm87HaB%2FRxc71LRG5TAwvHboMI7zgb0GOqUBtpGICe2Evwi%2Bx%2BUgO876ZC0jeZ7GT6sOgalUtyPGTWnZ%2FmhVdcLnYv0gzR2o9xQlONsjScoWptLFb3L3W9jTcrOqdb5Q6kh8gEyYe7XgByTRclurVUgXW7bWf7F0Oq2QUA6oBmy80xkrPHvdhVxwJQayn6QPu9ln82L3fdB8u%2ByENKh2Y3nzxN4BGM%2BlA85VjMQMFm8%2F%2FYbHehoxIFLkin2R8tZu&X-Amz-Signature=43beb50a28b0ad5e81f3840b9ce1b8220abf30936d3ac1644a48a646b546c326&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8f1b1d60-cf1b-42b3-9faa-f634c89c3f84/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WU5LWIB6%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T091652Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCsgxUB49sYS6FK%2F6gZ3nqgrChINS5FEj%2FeXAyICueSSAIgN3AKptThuorvFyTR2Q9MBxhgcQ%2FgvUZrqWN8JUAcSjkq%2FwMIERAAGgw2Mzc0MjMxODM4MDUiDMjJCIKejHnlYmE0pCrcAzhOoyDt4ZXpDTLFYfoLC%2B60OvXm9bebpZBB%2FsvU20zjgUS4I6CHrOA3zvTmMjhVGZ%2BGoFTkaK54cvDXGQHn%2FS4Em253rZEiN%2BMIcVJ2lGn7NtlR%2B%2F7qQpU4utf9dJUor%2FojYf3wWje4uAkREKsicQ%2FWvGOzue9K3gMN8zHQn6l%2FCUPRz1Gs3mo7ffTai%2BdMo1sor8jcOJ230e5vSvQQ34NBGU5FsFlVbEFf6lCZD5Dj4Ig6C8xPBiw9%2F4hSil8RlAkIakIPykaTzGf2GqYRt23nHZIL3Pgv6XWYcTz82%2FX9Npsg2E%2B5lTp%2BIE1l71rfomoeBkdtXuuFTaUor6ZuyTrcQbKMymTbaOLoifBiHHRMwWFOVSRueLY%2Fxo1pPK6LZNPhHDXlMLaUv1Gg2yyae%2Fh6DuVRBDzMVS0WYUzEtTNAYbkvTQOm4%2FESQuGkNVSAiIOC7ABxy1QByMI6RsQf2%2F%2BDHOupR1J83Na%2FBk9BkWAPXULoVXlrEroDlGBdLK5hFVowF36fJ8PpC4%2FhEx1NZJ3PlEVahVV%2Fg5usiPALQF63hgs2QBqbNBnDCNUw0BW1TAcnNtGXfkzymeSZII5wQc13y3M07OjWmTIGtm87HaB%2FRxc71LRG5TAwvHboMI7zgb0GOqUBtpGICe2Evwi%2Bx%2BUgO876ZC0jeZ7GT6sOgalUtyPGTWnZ%2FmhVdcLnYv0gzR2o9xQlONsjScoWptLFb3L3W9jTcrOqdb5Q6kh8gEyYe7XgByTRclurVUgXW7bWf7F0Oq2QUA6oBmy80xkrPHvdhVxwJQayn6QPu9ln82L3fdB8u%2ByENKh2Y3nzxN4BGM%2BlA85VjMQMFm8%2F%2FYbHehoxIFLkin2R8tZu&X-Amz-Signature=30e7a74df2ee24be5a3de4d29c0748763de813f05db318ff90ae3a3906f6c993&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/13ad0497-05fe-4eaa-984e-707b33e14761/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WU5LWIB6%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T091652Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCsgxUB49sYS6FK%2F6gZ3nqgrChINS5FEj%2FeXAyICueSSAIgN3AKptThuorvFyTR2Q9MBxhgcQ%2FgvUZrqWN8JUAcSjkq%2FwMIERAAGgw2Mzc0MjMxODM4MDUiDMjJCIKejHnlYmE0pCrcAzhOoyDt4ZXpDTLFYfoLC%2B60OvXm9bebpZBB%2FsvU20zjgUS4I6CHrOA3zvTmMjhVGZ%2BGoFTkaK54cvDXGQHn%2FS4Em253rZEiN%2BMIcVJ2lGn7NtlR%2B%2F7qQpU4utf9dJUor%2FojYf3wWje4uAkREKsicQ%2FWvGOzue9K3gMN8zHQn6l%2FCUPRz1Gs3mo7ffTai%2BdMo1sor8jcOJ230e5vSvQQ34NBGU5FsFlVbEFf6lCZD5Dj4Ig6C8xPBiw9%2F4hSil8RlAkIakIPykaTzGf2GqYRt23nHZIL3Pgv6XWYcTz82%2FX9Npsg2E%2B5lTp%2BIE1l71rfomoeBkdtXuuFTaUor6ZuyTrcQbKMymTbaOLoifBiHHRMwWFOVSRueLY%2Fxo1pPK6LZNPhHDXlMLaUv1Gg2yyae%2Fh6DuVRBDzMVS0WYUzEtTNAYbkvTQOm4%2FESQuGkNVSAiIOC7ABxy1QByMI6RsQf2%2F%2BDHOupR1J83Na%2FBk9BkWAPXULoVXlrEroDlGBdLK5hFVowF36fJ8PpC4%2FhEx1NZJ3PlEVahVV%2Fg5usiPALQF63hgs2QBqbNBnDCNUw0BW1TAcnNtGXfkzymeSZII5wQc13y3M07OjWmTIGtm87HaB%2FRxc71LRG5TAwvHboMI7zgb0GOqUBtpGICe2Evwi%2Bx%2BUgO876ZC0jeZ7GT6sOgalUtyPGTWnZ%2FmhVdcLnYv0gzR2o9xQlONsjScoWptLFb3L3W9jTcrOqdb5Q6kh8gEyYe7XgByTRclurVUgXW7bWf7F0Oq2QUA6oBmy80xkrPHvdhVxwJQayn6QPu9ln82L3fdB8u%2ByENKh2Y3nzxN4BGM%2BlA85VjMQMFm8%2F%2FYbHehoxIFLkin2R8tZu&X-Amz-Signature=e1331b891d4fe49920b88a3a110ba6906ebdf8d5b85e3f4768e77f582ccabf0b&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 2. Box and Whisker Plot
A box plot shows the distribution of quantitative data in a way that facilitates comparisons between variables or across levels of a categorical variable. The box shows the quartiles of the dataset while the whiskers extend to show the rest of the distribution, except for points that are determined to be "outliers".
**Syntax:**
```python
sns.boxplot(x='header_1', y='header_2', data=df)
```
**Example Output:**


![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d207ae92-0a7c-4e2f-aa65-0ee5a2c33bf7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SRECI442%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T091653Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDq8TlU%2BAGV%2FDvBhfwCqS9N0s0nF9UoG4OaDGQZuCV35QIgczIIZCOgUPuQTPQKTV184QqqI6I3%2FGjsTPK8YJJzXh8q%2FwMIERAAGgw2Mzc0MjMxODM4MDUiDKnmbVaXyt2r1bhwLSrcA9%2BIw1LSt5kN0r8%2BveT3AXKaPQ9Fexpk72hv4JHYXZXGaWorbjtnAUEmMSaEDK%2BrXRwebJPk4YvpTFp2vpxnccfSbisiZK3r6Ey%2FjGWJvJu0D37wY1hiC%2FOuBJQELsHojwLFQfGY6%2BWRuaUblhha%2BV94qeKmN3Bq1K%2FE3ZfpP0iD29WT8AXT2yu8VZpMHGW05ThDAMzEcDTDuh5cwASzeWHZbY2T2o0bpNFXhuG%2BEUIx%2BW2L1588assPzPIaoTHke2iLoxlFZY6lD3tHNCssDRhjaXRcfQvXy%2BRmCWodJNZvThXhGotiyEyo7%2FMsQH84LTgllDHhhmQ5%2FnAc%2FMM3tJ3tZougVh23ocGzP5Hpgmjg2m2%2BbyWrzZgOzkw2smRB8WZG32Jnxzsg7QM0EumZyFN4oihzSIIqVrY7ZS8E%2BAoPS63Pz%2F3Mn3euCS4fCzhzem6YW6G%2FXwJ8Fgg00uNUSkTK3ruP%2Bhb7OYQKeVt6rgRfs9I7RTtS2lWCc8wAyF97s%2FmTBrsypuNUvIWAx0Qe0M3dTDhsK05FOlXQWegAvC5qMrczMvQ7q8syQBmDnGf%2BrTqu6Hn13tw1OUM3W9kTdakBeD%2BrKdkbA%2B0QjMg%2Fxusd1%2BbIJKmfvQa8AmsXMLfzgb0GOqUBhb3BaW%2FiylRf4aEGtdp6d1acBhCzI9FHb0t54FOIcmby66w4ZZr%2Bq146kfjwO1YnR9UpUvRrHQNbOjpQimMFPNs5jIcdvPFEBXds6IKby6KylBdN%2FRN2qNBVBJwjdKGUK%2FOvAZFtVfCDgCVnQWl2JgDaIZ4hUypunXXF1ixpuWDBLSzvf5JHeP0VHRg6ef2Dvc%2FhpEPOlG64hbiWRGZkunaslemX&X-Amz-Signature=53cb9c40030f4337ac88e2a77e32e17c02f497ce52a053e5fea7c074475aa6d3&X-Amz-SignedHeaders=host&x-id=GetObject)

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0e516edc-7551-4792-ab18-0494db3c4c0c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TQ2XZCMO%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T091653Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDE3v9P%2FTkA%2BMQd60Jfhl1o4n7K1zttU8wq0y7qZ6A7xgIhANnoVt7cE7Z%2Boghb8Q5xHcn6TwnF6KyJGfmj5zjMidMWKv8DCBEQABoMNjM3NDIzMTgzODA1IgwYmbP0cDeV7HTSgpkq3AN9dT%2FH6nbC8ewBKZzGU%2BH1txClVLt9Bt6mC8NGMLhfkadXmbe94FOt8cnbxyHxHrYBrinVgr59gvf%2B1Cbx1hn1zxnTGB9Y%2BQ33sphMaxME%2FDV%2FoPe91QbwnXzKFCk%2B3PRWmcfOvf4p5a0REm3mMQczxJBvEIAri3OrAT9oC0ckwPJixPqMHRxO%2FMQiN6OvgLyEwVUV6kM%2BhP0c35z7oE4%2FucWTyk9txSeCGiUGWDVlS7cv3rOf12JLBmsZSmEZ3gX1%2FV%2BiSVtGf7Kz7xfyZHxjcX8FpLlI2Jva1%2BJD%2BaDDaqGcwYKbfAlONI0N4VY3WCVPFBEp78%2BskKTMNpFEV7uajmBHPCSFbe9jrmOcVdGVp9uDhXi2GTX03XPt6FTSxHwnKaji1TN%2F8pRoSzDmujuoWVAlqnAJwgRuFPqSNlwk3%2B289S80fCHG1RPLfsiu4AdzI3M4OtZujfAOrumsBpNfSFizuaw2q86nfhFitBBD%2FSlLz0INbauoKIYxp1Yu5DKbosA85hVewoeHoanR%2F5wDhEFtwcg74GJaLnBm5ndpGZAIufCfvggfoVrNZZW0sNEyAYPW%2BcN7uLkNJMWRt8TvPlng5iWo%2Bcm9roKmxztcpCysgQpGCMdv9M5stzCi84G9BjqkAWRNhCuuqtC%2Fli29b8Bti7xmdO8uoOx3KgC8n2%2FUNct5zCkGhAkaKNCpXFAo1rxBbFwr8uJ9OCImdFIWz2wsZjo2Iimg005eThtcVZ3UdQpfidkJkjmnqOlO9qpDD%2BeMLKuzB11n1iQt9iWuHsFX26E%2FlNq3GN8UVm%2FaTB1o5NBaHxG4m05c4mIMBJkyThlLwoa2Ba7dI5WwseF9aFpZHPw3ochs&X-Amz-Signature=b954b8591d01c50a70a9bfeb8af839ab9ee6b2f56b26d0b3edd57c26731a0920&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23a79b9d-2356-49a9-8fd9-65c6b0ab2cc5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WU5LWIB6%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T091652Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCsgxUB49sYS6FK%2F6gZ3nqgrChINS5FEj%2FeXAyICueSSAIgN3AKptThuorvFyTR2Q9MBxhgcQ%2FgvUZrqWN8JUAcSjkq%2FwMIERAAGgw2Mzc0MjMxODM4MDUiDMjJCIKejHnlYmE0pCrcAzhOoyDt4ZXpDTLFYfoLC%2B60OvXm9bebpZBB%2FsvU20zjgUS4I6CHrOA3zvTmMjhVGZ%2BGoFTkaK54cvDXGQHn%2FS4Em253rZEiN%2BMIcVJ2lGn7NtlR%2B%2F7qQpU4utf9dJUor%2FojYf3wWje4uAkREKsicQ%2FWvGOzue9K3gMN8zHQn6l%2FCUPRz1Gs3mo7ffTai%2BdMo1sor8jcOJ230e5vSvQQ34NBGU5FsFlVbEFf6lCZD5Dj4Ig6C8xPBiw9%2F4hSil8RlAkIakIPykaTzGf2GqYRt23nHZIL3Pgv6XWYcTz82%2FX9Npsg2E%2B5lTp%2BIE1l71rfomoeBkdtXuuFTaUor6ZuyTrcQbKMymTbaOLoifBiHHRMwWFOVSRueLY%2Fxo1pPK6LZNPhHDXlMLaUv1Gg2yyae%2Fh6DuVRBDzMVS0WYUzEtTNAYbkvTQOm4%2FESQuGkNVSAiIOC7ABxy1QByMI6RsQf2%2F%2BDHOupR1J83Na%2FBk9BkWAPXULoVXlrEroDlGBdLK5hFVowF36fJ8PpC4%2FhEx1NZJ3PlEVahVV%2Fg5usiPALQF63hgs2QBqbNBnDCNUw0BW1TAcnNtGXfkzymeSZII5wQc13y3M07OjWmTIGtm87HaB%2FRxc71LRG5TAwvHboMI7zgb0GOqUBtpGICe2Evwi%2Bx%2BUgO876ZC0jeZ7GT6sOgalUtyPGTWnZ%2FmhVdcLnYv0gzR2o9xQlONsjScoWptLFb3L3W9jTcrOqdb5Q6kh8gEyYe7XgByTRclurVUgXW7bWf7F0Oq2QUA6oBmy80xkrPHvdhVxwJQayn6QPu9ln82L3fdB8u%2ByENKh2Y3nzxN4BGM%2BlA85VjMQMFm8%2F%2FYbHehoxIFLkin2R8tZu&X-Amz-Signature=7dcbec6bbca0cdf410bbb57de54f7bda95c6bffc0ce48388f2338d10da9f47fc&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 4. KDE Plot
A Kernel Density Estimate (KDE) plot is a graph that creates a probability distribution curve for the data based upon its likelihood of occurrence on a specific value. This is created for a single vector of information.
**Syntax:**
```python
sns.kdeplot(X) || sns.kdeplot(df['age'])
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0d571213-2a2f-4921-a50b-880847aa05ee/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WU5LWIB6%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T091652Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCsgxUB49sYS6FK%2F6gZ3nqgrChINS5FEj%2FeXAyICueSSAIgN3AKptThuorvFyTR2Q9MBxhgcQ%2FgvUZrqWN8JUAcSjkq%2FwMIERAAGgw2Mzc0MjMxODM4MDUiDMjJCIKejHnlYmE0pCrcAzhOoyDt4ZXpDTLFYfoLC%2B60OvXm9bebpZBB%2FsvU20zjgUS4I6CHrOA3zvTmMjhVGZ%2BGoFTkaK54cvDXGQHn%2FS4Em253rZEiN%2BMIcVJ2lGn7NtlR%2B%2F7qQpU4utf9dJUor%2FojYf3wWje4uAkREKsicQ%2FWvGOzue9K3gMN8zHQn6l%2FCUPRz1Gs3mo7ffTai%2BdMo1sor8jcOJ230e5vSvQQ34NBGU5FsFlVbEFf6lCZD5Dj4Ig6C8xPBiw9%2F4hSil8RlAkIakIPykaTzGf2GqYRt23nHZIL3Pgv6XWYcTz82%2FX9Npsg2E%2B5lTp%2BIE1l71rfomoeBkdtXuuFTaUor6ZuyTrcQbKMymTbaOLoifBiHHRMwWFOVSRueLY%2Fxo1pPK6LZNPhHDXlMLaUv1Gg2yyae%2Fh6DuVRBDzMVS0WYUzEtTNAYbkvTQOm4%2FESQuGkNVSAiIOC7ABxy1QByMI6RsQf2%2F%2BDHOupR1J83Na%2FBk9BkWAPXULoVXlrEroDlGBdLK5hFVowF36fJ8PpC4%2FhEx1NZJ3PlEVahVV%2Fg5usiPALQF63hgs2QBqbNBnDCNUw0BW1TAcnNtGXfkzymeSZII5wQc13y3M07OjWmTIGtm87HaB%2FRxc71LRG5TAwvHboMI7zgb0GOqUBtpGICe2Evwi%2Bx%2BUgO876ZC0jeZ7GT6sOgalUtyPGTWnZ%2FmhVdcLnYv0gzR2o9xQlONsjScoWptLFb3L3W9jTcrOqdb5Q6kh8gEyYe7XgByTRclurVUgXW7bWf7F0Oq2QUA6oBmy80xkrPHvdhVxwJQayn6QPu9ln82L3fdB8u%2ByENKh2Y3nzxN4BGM%2BlA85VjMQMFm8%2F%2FYbHehoxIFLkin2R8tZu&X-Amz-Signature=ea682c4d9a372ba7cbedc7055d6410d560f360e9a920fbdff8796a9c744094f5&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/53752550-ef82-4ca9-a01a-09921f0282d0/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WU5LWIB6%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T091652Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCsgxUB49sYS6FK%2F6gZ3nqgrChINS5FEj%2FeXAyICueSSAIgN3AKptThuorvFyTR2Q9MBxhgcQ%2FgvUZrqWN8JUAcSjkq%2FwMIERAAGgw2Mzc0MjMxODM4MDUiDMjJCIKejHnlYmE0pCrcAzhOoyDt4ZXpDTLFYfoLC%2B60OvXm9bebpZBB%2FsvU20zjgUS4I6CHrOA3zvTmMjhVGZ%2BGoFTkaK54cvDXGQHn%2FS4Em253rZEiN%2BMIcVJ2lGn7NtlR%2B%2F7qQpU4utf9dJUor%2FojYf3wWje4uAkREKsicQ%2FWvGOzue9K3gMN8zHQn6l%2FCUPRz1Gs3mo7ffTai%2BdMo1sor8jcOJ230e5vSvQQ34NBGU5FsFlVbEFf6lCZD5Dj4Ig6C8xPBiw9%2F4hSil8RlAkIakIPykaTzGf2GqYRt23nHZIL3Pgv6XWYcTz82%2FX9Npsg2E%2B5lTp%2BIE1l71rfomoeBkdtXuuFTaUor6ZuyTrcQbKMymTbaOLoifBiHHRMwWFOVSRueLY%2Fxo1pPK6LZNPhHDXlMLaUv1Gg2yyae%2Fh6DuVRBDzMVS0WYUzEtTNAYbkvTQOm4%2FESQuGkNVSAiIOC7ABxy1QByMI6RsQf2%2F%2BDHOupR1J83Na%2FBk9BkWAPXULoVXlrEroDlGBdLK5hFVowF36fJ8PpC4%2FhEx1NZJ3PlEVahVV%2Fg5usiPALQF63hgs2QBqbNBnDCNUw0BW1TAcnNtGXfkzymeSZII5wQc13y3M07OjWmTIGtm87HaB%2FRxc71LRG5TAwvHboMI7zgb0GOqUBtpGICe2Evwi%2Bx%2BUgO876ZC0jeZ7GT6sOgalUtyPGTWnZ%2FmhVdcLnYv0gzR2o9xQlONsjScoWptLFb3L3W9jTcrOqdb5Q6kh8gEyYe7XgByTRclurVUgXW7bWf7F0Oq2QUA6oBmy80xkrPHvdhVxwJQayn6QPu9ln82L3fdB8u%2ByENKh2Y3nzxN4BGM%2BlA85VjMQMFm8%2F%2FYbHehoxIFLkin2R8tZu&X-Amz-Signature=5dd46a1b5b74a9a2fdeb7b0f1153fa347b9804b4724033d8c6857f55c37c2867&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
## 4. Correlation Between Variables
Correlation is a statistical measure of the extent to which different variables are interdependent. It indicates how changes in one variable are associated with changes in another variable over time.
### Positive Correlation
Positive correlation indicates that as one variable increases, the other variable also tends to increase.
**Example: Engine Size and Price**
- **Positive Correlation:** Engine size increases, price also increases.
- **Visualization:** Scatter plot with a steep positive slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c7ea9b0-3ef3-4357-a9c3-554fc71b6b15/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RJRT3WJV%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T091653Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCs%2FFSvVW%2BhYZguH8k7fsE39Xst6tiuaN8uVkWdMkF0AQIhANJgORbzAQJ3252h5pXmZK6hWPpfBAy9NlSwgSVP90VcKv8DCBEQABoMNjM3NDIzMTgzODA1IgyBRG%2F%2B8cDULAw1LPQq3AMCDkwT7Eqz9%2FHxwY91mFuXgZsede4f3fOrU0wiGko%2BHBcLrrre73JKV0UjG%2B5uCS3nRLuKgFywanvOrLbhOqNxlmDhHqx82JjDaYB7U603Yd0drj%2Fah5VrvKxxj4Ko71MgmKPvx8rdXnY70SP2G%2BIy%2F2Jow8edKdiGdC2I1zO25q5BibXa2XdQlX%2F6BLZolTcO1K6W3%2F3c1IFna2WrkJE6qXCVj3FdRi6dUFg8xq%2BSkIUuXkBSYsHJ7rns3igcPPJEiFupOnacXypcfFONoO%2BfIX0A%2F4DMW2mGgrMvITULO6z%2BXodrr1s53Ny6IhDEMbv20foDdxgJMK0XTbCp16podzSsgm9Zx9Rj9aflsIXqSqHkqI6kUOkmees70Br4yXCij6SdmI4VQgw%2BRtlYG05XAMorZq2HwvGB0Yz18g1%2BPg3icFC%2B%2B7cQzQhEcOdaLoDdhpavLreA8Ho81TzDvJ1WXPi%2FHc10bl6KV2qp20JAegt272843473JL64SN4CSeIjfq7wkMa8W78ndZFI9xDu7TicgSLlY%2FqgshvR2e%2Bowh%2FxgFAqjcOsINZ3OKVVgfHSk%2FK9%2Fky65G38eOPwr3TFXe%2BItvjQWqJSRnN7zGlTIO8t6jpTGf%2FU3mE%2F8TDz8oG9BjqkAZ7UXZ6x29kNx5qPoGmpY5CjUyUq39zZYW7AH426kEz%2FHLneOpqOyJHjdnJA4UAMioKnfrRJ%2Bw1%2BYMvz9oDehEimsiYRqX6tvxzTm2qG9eTtftho2ptM%2FtogUCDbivFZN8DcbmDPlpXZPuLD%2BCpl8u7W2%2B%2BBeZgRxyczF%2B5m5y2hR7o3lBJ%2BUb6ZoKOqy83Sb09w2DhTU6dfx3mTDxMEVaeifwpC&X-Amz-Signature=862654066d6d058da1a446f705cdffaa75f1baa0bc1b0bf144604259a3253958&X-Amz-SignedHeaders=host&x-id=GetObject)
**Explanation:** When engine size increases, there is a corresponding increase in the price of the vehicle. This positive correlation suggests that larger engines tend to be associated with higher prices in the market.
___
### Negative Correlation
Negative correlation indicates that as one variable increases, the other variable tends to decrease.
**Example: Highway Miles per Gallon and Price**
- **Negative Correlation:** As highway miles per gallon increases, price decreases.
- **Visualization:** Scatter plot with a steep negative slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/10f1f798-9cc4-4df2-a9c1-5a339f554a0b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662VVSLUSP%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T091653Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQChZ4g7tosnsCqovkc0IosRdZfJZygXog%2F5tgsVKy22RgIhAMn4iSJlZ5m5xbwkq2mmXXdu6yplbB3KlRDntBfVZz8vKv8DCBEQABoMNjM3NDIzMTgzODA1IgzhYua%2FhI%2Fvhj20saoq3APvskyNuUygoizFN6g2dc6qzG2fL1zS472ZQqCZw6rccRTJIQKOIxarMEcUsJla99SIEgAizxlQqo1SrOF6rw8o%2FTOOpVDQUcGsTljSnQW9Fplgb%2FhPKj4jeCyvOni0hFR%2FKoZaokG7LZ7NixuKVkfMcbqEI4CrLbdWtyU7s0c5YPjzh5uYTbiyfAG7BtZ4HHrwejXr7C9R0snMEHRoK%2Fr6yiYAoG0JG%2BJ8VY9wKSUw1ZaAOb4copZquLr%2BgYlytepae7PeBoF0L0Cb%2Btq31LrOs8arsotv1DUwPlsbSbj3bVlWtcofDVlxsLq642dHSvG%2FV%2Fm4slWdWmNa4qg9pIlvSik4dkK7WhSwyD3hsTsBma1JyM%2FKxxRyqHsLKmH6Ayr3r8FdPCh9EaaWfF5TR0gen4Zd5udAu6hbBpk%2F0Ctq%2BSz3tNpfTNsn6xAq6WDH%2Bpi5yezTIYMVRr9vGfIl5Iawhxt7IHfwHM8DaEUcqyAOgETg%2B3h%2FIVLzFnuo%2F4nthzF2NZJdj4t1P3e5PrSEbQyQCbtaoF6Tmphd%2BD1LQsK5ht89P04kglyoWuuv60tfCBzD3AfxN2ZL7vMlQXTXPV9pqHsZaWLw2wUZ5eenvV7iFJDOs5FbsvV9n2fIcTCR84G9BjqkAaPya0PkZwqIhHwj5AhGXnlqJk1bf3YyfAqrlVtfv85DzpfXE17pp%2FD3r%2FNwDLP6NQ9VlS1TrPLaER84ZhibAQq6oh7jrftEGG%2FAawNRJhZHlQ6AlICMftaLIc8O%2BBFcaehwaRYKC%2BrajM6W5gozA4KfDutXI%2FBa%2FHVIc93z%2FlAN7e%2FI1NPbhqH6CtGh5nOqZ25yXquuWNuywy75lt6btpFqpkpM&X-Amz-Signature=cabd6fe46ae961ac37692149f543ab08680b519b921c912c7f174a19ca1b29d3&X-Amz-SignedHeaders=host&x-id=GetObject)
**Explanation:** When highway miles per gallon increases, the price of the vehicle tends to decrease. This negative correlation suggests that cars with higher fuel efficiency (more miles per gallon) are generally priced lower in the market.
___
### Weak Correlation
Weak correlation indicates a lack of strong relationship between the variables.
**Example: RPM and Price**
- **Weak Correlation:** Low and high RPM values show varied prices, indicating no strong predictive relationship.
- **Visualization:** Scatter plot with no clear trend or slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9f914514-8914-4bf4-ac84-d9e3077f6eb1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466X5PAY5RB%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T091653Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDty%2BYWKpSZ8DqF7ipeLEtFFhqGVA8kcTvjZpiAsv7fRAIgb6oab%2F6hVRlG5yg319YilTmVnb6gpbT9XPp7fnbDxMwq%2FwMIERAAGgw2Mzc0MjMxODM4MDUiDL98eH0dvrivITyx%2ByrcA2xvzHUBJEkSXPyrmCKXrjz7ncyVIWipqWW2rM%2BmPszPDaEXOMbvJOxqp%2BCJmro1P3qNRhDIIT%2BGvE6gefHrr7Tk2tr3iNlLUZ9iXPpCc3cSCqXEsYExAWpK2F%2F1amtVRptsqZm%2FfklAHfx0dGrUr8hItL1vzfA7PtSpGvyOL1zwFou%2BrkRHJ598%2B3ttzbV5OtMlZ2bp4wNo495dkY1nJQCQm6VOJf2oYjhyr0PXk1vTrehiCsvlepyHlKteRGY6ScmGt49C2OzGgPuC2tYz9aoGJSayYEd2iuFZSwB0SMsyU7VDPfBOSTJZEuzaAZsW8yxZqbjOLPWEt2Fe7ySNH1udP8YJ7bzLjxzhSKakIslIXnk1Bnxk7p1I24gnqyIOZmhfPevkBWmMT2igaK5FrvphXrfY9falSyCwjR3TBJtwC1MFanp0JBD5AcBqaVhbk4G08Iu7fzw3%2BfcUrdr9uKD%2F%2BQIzsY5OQ%2F%2B7WHEwLVJRG0qRUxokE6JhmCItXPQ%2Fs3Ua%2BGPOa5v6JS4EsnfsoM8dgvvtSvBoUoEkkP4kF%2BvqaFWrnwlkz%2Fv6rRQnV0dKkrgP5xX7IqoJJO2uF8z8aoPbG6hTu206vIK3m8%2BRRztC3oh%2FPLYs2esTERZPMObygb0GOqUBYkmeYXCoFyBcbRZB5%2FZav4Yqm3RYg3rx9GX09kVEOKrgnOtRSuBfKVgU6Q3JSKv7rbZGm8FAeJdvNbRa5%2ByJBh86pQOv8cw%2B3TobBvcDJnNceENjaut8hLMVc%2B37JyT%2Fc34OhJyoGlmyzNm0Zhwl%2FjL9dbxJk1Zzx0pOelQgMquRb0zuOcRzkkD19XsFWwdHfT7ZSSjpfybgUuA84k8y0uscerfD&X-Amz-Signature=9e34df2bc8677394087057e079b42e1008bfb6851c658175178270c41905cbc8&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f18086e5-5b04-4fbf-8309-8944ab20d213/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665SZRYF44%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T091653Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDYrGPHS9kxe7PrL403hEbJbLy0kuipiAm4zExg3KK3ywIgI3G3oqdfS5VsJ1OJuhugFGIkY4neOK3OJ2I6jAL7QD4q%2FwMIERAAGgw2Mzc0MjMxODM4MDUiDEX8a4sUkNrVORRtxSrcA1hQAqy16zVbeBMXwaoTizQtaobQVOwPH5WeJz2zse86WxD24hiMEpmQExSXvHk1RcFkdZ53E4BZnqUgU%2FxAMHyqHZON7NPAp9LfU8aXLlFsYz%2BtJO3e%2BnITfvrSE8WkfGh449rQ8YNnlG6fsK3cyzOVf%2BBlYbICBA%2Bh71sEy%2BnhpmXabB73gVBhEhYXdRMIvo02a9DeSy0m%2Bd97G2pkmuPspynGLpDndPls48mMA5O1oLbBgDbJ2KwY%2Fbb79dJp7mnjzY%2BL60FBb68kaPaQxBg1Qip4wR9BkCioBcxV3M3X00HMjgcB%2FdolI5jB7hd%2FHjgUJ%2BR%2FWILcE%2Bu578rJrV%2B7Jq7gfzrEdbXp4rj%2FKmv5rFySKeBkrsLfxojFts1IOEiPf3rYlOM8EsdbFke7gvNI15EIm0crBTmA4K%2Fu1SiLlJ7XOnvSsZouNiqAIc7%2B0P3drIHyABP2sX%2FewfxPZlgra976vlNSJKFX0vSO1Xh3bzq4bjEtFkOJlrqYP8iZ%2BOoRKxEyJtYfAs4K%2Fu7lQsd%2BSxKWNxlnLj%2BQe04J0WBKn50mpg0yo3okJYyWxso2ebleiiipHxlve%2FUhhLoyUnCPdtYZeSsVk5Uu0RlLVfUy2lLt5rC8bZttfWVnMOzzgb0GOqUBTHFvoCIuhou4oke%2FgxPzufYmcRebncl05AM%2FmeW8C%2F16jwL3ThiV4NKnVh1xHtmNDjRFAydymkpeJyO9M5n5oonkv1DfQRkvfe5nReDET2QHapd5FjxKgfIVVdmCZJYNnBBkuq3pdem%2B6WgrflMG16Q9d5C47tqbFdz1gV6A80qd0qAQrmCO3roy074HdcZraLtLeOcis6jERuDWaGYEP1JyWUKO&X-Amz-Signature=68d06a53673c3ab594e4aef436221483c70994327e94447b0ee4b52e9b156552&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Correlation Plot
Heatmap visualizes correlations among variables. Color scheme indicates Pearson correlation coefficients. Dark red diagonal line shows perfect correlation (value of 1) between variables and themselves.
This heatmap offers overview of variable relationships and their link with price.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cd3b341e-cc1a-45f7-8aec-cdc00436d270/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665SZRYF44%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T091653Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDYrGPHS9kxe7PrL403hEbJbLy0kuipiAm4zExg3KK3ywIgI3G3oqdfS5VsJ1OJuhugFGIkY4neOK3OJ2I6jAL7QD4q%2FwMIERAAGgw2Mzc0MjMxODM4MDUiDEX8a4sUkNrVORRtxSrcA1hQAqy16zVbeBMXwaoTizQtaobQVOwPH5WeJz2zse86WxD24hiMEpmQExSXvHk1RcFkdZ53E4BZnqUgU%2FxAMHyqHZON7NPAp9LfU8aXLlFsYz%2BtJO3e%2BnITfvrSE8WkfGh449rQ8YNnlG6fsK3cyzOVf%2BBlYbICBA%2Bh71sEy%2BnhpmXabB73gVBhEhYXdRMIvo02a9DeSy0m%2Bd97G2pkmuPspynGLpDndPls48mMA5O1oLbBgDbJ2KwY%2Fbb79dJp7mnjzY%2BL60FBb68kaPaQxBg1Qip4wR9BkCioBcxV3M3X00HMjgcB%2FdolI5jB7hd%2FHjgUJ%2BR%2FWILcE%2Bu578rJrV%2B7Jq7gfzrEdbXp4rj%2FKmv5rFySKeBkrsLfxojFts1IOEiPf3rYlOM8EsdbFke7gvNI15EIm0crBTmA4K%2Fu1SiLlJ7XOnvSsZouNiqAIc7%2B0P3drIHyABP2sX%2FewfxPZlgra976vlNSJKFX0vSO1Xh3bzq4bjEtFkOJlrqYP8iZ%2BOoRKxEyJtYfAs4K%2Fu7lQsd%2BSxKWNxlnLj%2BQe04J0WBKn50mpg0yo3okJYyWxso2ebleiiipHxlve%2FUhhLoyUnCPdtYZeSsVk5Uu0RlLVfUy2lLt5rC8bZttfWVnMOzzgb0GOqUBTHFvoCIuhou4oke%2FgxPzufYmcRebncl05AM%2FmeW8C%2F16jwL3ThiV4NKnVh1xHtmNDjRFAydymkpeJyO9M5n5oonkv1DfQRkvfe5nReDET2QHapd5FjxKgfIVVdmCZJYNnBBkuq3pdem%2B6WgrflMG16Q9d5C47tqbFdz1gV6A80qd0qAQrmCO3roy074HdcZraLtLeOcis6jERuDWaGYEP1JyWUKO&X-Amz-Signature=c33d1d197b6f62dda0a5dfdc61447e947bf5b255b3c16cae9e8e8a156718e865&X-Amz-SignedHeaders=host&x-id=GetObject)

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
