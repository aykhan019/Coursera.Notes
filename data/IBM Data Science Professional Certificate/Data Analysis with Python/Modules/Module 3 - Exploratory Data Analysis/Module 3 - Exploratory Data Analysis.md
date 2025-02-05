

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7e6d594d-952e-44b6-97ea-31225882aea6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666D63VJFU%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T171301Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDAaCXVzLXdlc3QtMiJHMEUCIHEU6tT8QFaYvYdDMyjOK1UWNKcaWH42vZFhkulK4DrOAiEApt1YxGCc3MQ4Q1whVlM7go1ImskYIG3Om%2BKJJBrr1I0q%2FwMISRAAGgw2Mzc0MjMxODM4MDUiDCy%2B0L4oi160fhhPYircA%2BV4Kf9ijSDR%2BlqZObzsmbJjZV4liPdgYwcUfb3yj%2Fk%2FJ%2Brwk4BffdG4OnHbkBIStp3Q8XkmtxE4txqdKIVgvgODRbp6zC2om8zRtFcvu0nWRxcBbb8GGGXzBmVRuXK8tY%2BdUy%2F100z8NUPkwL%2BDpTfebEHcBN%2F8Qm8LGy1QU6zhmfxbzQwxcVfbLrO7%2B1eOi3CvLOnVn8k052NQ4MwwI%2FXzP9ttTwjm9TwnczdZjJc2U%2FFtE%2BS83z%2BXtONT%2B3I%2BoVhCaW2MvGAsPTOtWyxQyDaHPonSVaYhWKoWdZT0k%2B3EFD8kezWyVUpzNCkVCL6Ds409gqAaEtkv5%2FwuA%2BeIjnWE0xv4HXIYmgaWKup5YqLBPr47lQwteFZNFGvRgiEGf%2FspLLdUm5q6YCu6JUIN3yO2yAZhXyHpAqN9dSL11KJonpvXF9DYNbvS6Jrxl%2B9FxCwfgOfAbypvK%2F6nMlJtp3520RUtuy%2BcOhGb1p4y1%2FkmqvKTFojDArU9GFSXZX3NH5tVzmrh7SmSIHvvCGeQ90jmH1VNtw9a5%2BXBEZff0i5Gbq1%2FI30UtKGIyXKPMChpEJq5b0l953VCqd0llnt7w2ZIe4kcaxHkhUJI0Xl4O2WTeK5PZOodAC7GIxQMMJydjr0GOqUB670Hutox%2FUCWt2W5lcccV53eiga%2FSSWV0X%2B1za4gmPh5aP6iDmJBV%2BCmPfCqBTRr3KXM3lnUhhyvPjfPYpqkVtThkHf%2F5eNidW93qXiQD9iNp%2Fjj4D%2Bps6FLQikk%2FcHht1T1ry44gUV%2B25Yqainw3p9GNetnIuUcZx2HSO82J1sVMPXMnfKr71U6ChDdvcPoShso3nN80p4bOpGgaQqNmEKhRYiJ&X-Amz-Signature=7720d51f703ab464ebf7bdedb8d45d69909eddc483ce4cc6f68aae1b2d2918d7&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cbfaed9e-b398-4902-8936-dea058b21def/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666D63VJFU%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T171301Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDAaCXVzLXdlc3QtMiJHMEUCIHEU6tT8QFaYvYdDMyjOK1UWNKcaWH42vZFhkulK4DrOAiEApt1YxGCc3MQ4Q1whVlM7go1ImskYIG3Om%2BKJJBrr1I0q%2FwMISRAAGgw2Mzc0MjMxODM4MDUiDCy%2B0L4oi160fhhPYircA%2BV4Kf9ijSDR%2BlqZObzsmbJjZV4liPdgYwcUfb3yj%2Fk%2FJ%2Brwk4BffdG4OnHbkBIStp3Q8XkmtxE4txqdKIVgvgODRbp6zC2om8zRtFcvu0nWRxcBbb8GGGXzBmVRuXK8tY%2BdUy%2F100z8NUPkwL%2BDpTfebEHcBN%2F8Qm8LGy1QU6zhmfxbzQwxcVfbLrO7%2B1eOi3CvLOnVn8k052NQ4MwwI%2FXzP9ttTwjm9TwnczdZjJc2U%2FFtE%2BS83z%2BXtONT%2B3I%2BoVhCaW2MvGAsPTOtWyxQyDaHPonSVaYhWKoWdZT0k%2B3EFD8kezWyVUpzNCkVCL6Ds409gqAaEtkv5%2FwuA%2BeIjnWE0xv4HXIYmgaWKup5YqLBPr47lQwteFZNFGvRgiEGf%2FspLLdUm5q6YCu6JUIN3yO2yAZhXyHpAqN9dSL11KJonpvXF9DYNbvS6Jrxl%2B9FxCwfgOfAbypvK%2F6nMlJtp3520RUtuy%2BcOhGb1p4y1%2FkmqvKTFojDArU9GFSXZX3NH5tVzmrh7SmSIHvvCGeQ90jmH1VNtw9a5%2BXBEZff0i5Gbq1%2FI30UtKGIyXKPMChpEJq5b0l953VCqd0llnt7w2ZIe4kcaxHkhUJI0Xl4O2WTeK5PZOodAC7GIxQMMJydjr0GOqUB670Hutox%2FUCWt2W5lcccV53eiga%2FSSWV0X%2B1za4gmPh5aP6iDmJBV%2BCmPfCqBTRr3KXM3lnUhhyvPjfPYpqkVtThkHf%2F5eNidW93qXiQD9iNp%2Fjj4D%2Bps6FLQikk%2FcHht1T1ry44gUV%2B25Yqainw3p9GNetnIuUcZx2HSO82J1sVMPXMnfKr71U6ChDdvcPoShso3nN80p4bOpGgaQqNmEKhRYiJ&X-Amz-Signature=8ee7b06d267e6b43c5a173f1cba97c7d47c286c7920e58575ea27121c251f2b3&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/91181646-b1e0-4433-9711-6259a96a9247/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666D63VJFU%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T171301Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDAaCXVzLXdlc3QtMiJHMEUCIHEU6tT8QFaYvYdDMyjOK1UWNKcaWH42vZFhkulK4DrOAiEApt1YxGCc3MQ4Q1whVlM7go1ImskYIG3Om%2BKJJBrr1I0q%2FwMISRAAGgw2Mzc0MjMxODM4MDUiDCy%2B0L4oi160fhhPYircA%2BV4Kf9ijSDR%2BlqZObzsmbJjZV4liPdgYwcUfb3yj%2Fk%2FJ%2Brwk4BffdG4OnHbkBIStp3Q8XkmtxE4txqdKIVgvgODRbp6zC2om8zRtFcvu0nWRxcBbb8GGGXzBmVRuXK8tY%2BdUy%2F100z8NUPkwL%2BDpTfebEHcBN%2F8Qm8LGy1QU6zhmfxbzQwxcVfbLrO7%2B1eOi3CvLOnVn8k052NQ4MwwI%2FXzP9ttTwjm9TwnczdZjJc2U%2FFtE%2BS83z%2BXtONT%2B3I%2BoVhCaW2MvGAsPTOtWyxQyDaHPonSVaYhWKoWdZT0k%2B3EFD8kezWyVUpzNCkVCL6Ds409gqAaEtkv5%2FwuA%2BeIjnWE0xv4HXIYmgaWKup5YqLBPr47lQwteFZNFGvRgiEGf%2FspLLdUm5q6YCu6JUIN3yO2yAZhXyHpAqN9dSL11KJonpvXF9DYNbvS6Jrxl%2B9FxCwfgOfAbypvK%2F6nMlJtp3520RUtuy%2BcOhGb1p4y1%2FkmqvKTFojDArU9GFSXZX3NH5tVzmrh7SmSIHvvCGeQ90jmH1VNtw9a5%2BXBEZff0i5Gbq1%2FI30UtKGIyXKPMChpEJq5b0l953VCqd0llnt7w2ZIe4kcaxHkhUJI0Xl4O2WTeK5PZOodAC7GIxQMMJydjr0GOqUB670Hutox%2FUCWt2W5lcccV53eiga%2FSSWV0X%2B1za4gmPh5aP6iDmJBV%2BCmPfCqBTRr3KXM3lnUhhyvPjfPYpqkVtThkHf%2F5eNidW93qXiQD9iNp%2Fjj4D%2Bps6FLQikk%2FcHht1T1ry44gUV%2B25Yqainw3p9GNetnIuUcZx2HSO82J1sVMPXMnfKr71U6ChDdvcPoShso3nN80p4bOpGgaQqNmEKhRYiJ&X-Amz-Signature=76a05447ab30816c924ba9b0470ae6cd1032a6e13755f08adb6a3d30df361b0c&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/09aba1c0-0d55-41dd-852a-a04c5b8a3fac/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664WXJTOUW%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T171302Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDAaCXVzLXdlc3QtMiJGMEQCIB7MnfRZuhdj%2FJmlCk8x9SDAGNabSYT2FLbKDJjxSgj5AiAWeh1qvcfbJmL2%2F%2BTrAIMljeuf75Uaa9JExx%2FqQJ7EhCr%2FAwhJEAAaDDYzNzQyMzE4MzgwNSIMJeMbA8VoY4i8uobzKtwDrQ6OFh8SmjzV90JqFdI2ryN59VFktzgXojv9wbWmbUGeJp3LXW6MUp7kfPrSSuL3j%2BTp326LS4FXjN4pbBIxtkAV8FwjfPZvJrzwpT7qu5nXIM5hMZur6TB2enE7tPL6krXMZ%2FpGYvcYv7qNBE2HdYbT1eMpvivN2bDoJpcDh3Nb%2BS2G5NptMZBBwOR04P3zaM1IACuAJ4DcS1a9jDX07EXKie%2BXHAILDMp4hlc%2BzVL9l5eONZibL4tw8bI9a4Bg3w19%2BRZqC3SdssE0l7DZVVJjf78XoEmbRE78b1MtYIzCUkKFIPVOgOZIFTNoa%2F1X9nU7BlD4Bq0ClCsEHbHnjVt5N0NU4xdItJAXCock3IQjXFvFNOgH8sPYVnQfnw9OFSxdYaqJdaVTEQDMVTgatQj6reCkoK3o%2Fnie7dPrRe9%2BJSrJ7rTJEmr93h%2F%2F%2F6anOHBlFkEo19DxTBJuLFTktnrFCjq20APhZ2SsBgl9CLczZXkf7l1YBvqMx6l%2FNawHH7JZjtVGHqkMBaPDeIyVGN9hTvXDiN8bqNk1X8d4L9ZY%2BOMx%2FtIJ1mV7GstvVduD2qi2i96mZM572l0PbxesTH7f19rUJO8pFuwC4CMZq6oAYdROapQ2qyYUSVcw9p2OvQY6pgGwILK9aUNzQ3N745dZNSa5JFRTXd3KZY4zi%2BcYrXGAOPzKnWgkQvLrG%2B2Uets3A5xfYBVOH8ewA2EUThrTEg5q%2FYR20vfP49pa1LiXGYZpvlJA2t2MWIire7tmKX7Tl2YrFMHOjItarX9XMzalUVWu73ZSSGw3jtZSrNLmHlj8ugyHbY3nU%2BR%2BHxXqBzJpWFPUJCSQtQzDE9PGDpd%2B0FWbY5x%2Fe65U&X-Amz-Signature=5158a203fcff856ef16f3b084973369accdbc299d9ac4d25ecf752573021f241&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 2. Scatter Plot
Scatter plots present the relationship between two variables in a dataset. It represents data points on a two-dimensional plane. The independent variable or attribute is plotted on the X-axis, while the dependent variable is plotted on the Y-axis.
**Syntax:**
```python
plt.scatter(x, y)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23708af9-659f-4f23-b626-1a4292d7842c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664WXJTOUW%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T171302Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDAaCXVzLXdlc3QtMiJGMEQCIB7MnfRZuhdj%2FJmlCk8x9SDAGNabSYT2FLbKDJjxSgj5AiAWeh1qvcfbJmL2%2F%2BTrAIMljeuf75Uaa9JExx%2FqQJ7EhCr%2FAwhJEAAaDDYzNzQyMzE4MzgwNSIMJeMbA8VoY4i8uobzKtwDrQ6OFh8SmjzV90JqFdI2ryN59VFktzgXojv9wbWmbUGeJp3LXW6MUp7kfPrSSuL3j%2BTp326LS4FXjN4pbBIxtkAV8FwjfPZvJrzwpT7qu5nXIM5hMZur6TB2enE7tPL6krXMZ%2FpGYvcYv7qNBE2HdYbT1eMpvivN2bDoJpcDh3Nb%2BS2G5NptMZBBwOR04P3zaM1IACuAJ4DcS1a9jDX07EXKie%2BXHAILDMp4hlc%2BzVL9l5eONZibL4tw8bI9a4Bg3w19%2BRZqC3SdssE0l7DZVVJjf78XoEmbRE78b1MtYIzCUkKFIPVOgOZIFTNoa%2F1X9nU7BlD4Bq0ClCsEHbHnjVt5N0NU4xdItJAXCock3IQjXFvFNOgH8sPYVnQfnw9OFSxdYaqJdaVTEQDMVTgatQj6reCkoK3o%2Fnie7dPrRe9%2BJSrJ7rTJEmr93h%2F%2F%2F6anOHBlFkEo19DxTBJuLFTktnrFCjq20APhZ2SsBgl9CLczZXkf7l1YBvqMx6l%2FNawHH7JZjtVGHqkMBaPDeIyVGN9hTvXDiN8bqNk1X8d4L9ZY%2BOMx%2FtIJ1mV7GstvVduD2qi2i96mZM572l0PbxesTH7f19rUJO8pFuwC4CMZq6oAYdROapQ2qyYUSVcw9p2OvQY6pgGwILK9aUNzQ3N745dZNSa5JFRTXd3KZY4zi%2BcYrXGAOPzKnWgkQvLrG%2B2Uets3A5xfYBVOH8ewA2EUThrTEg5q%2FYR20vfP49pa1LiXGYZpvlJA2t2MWIire7tmKX7Tl2YrFMHOjItarX9XMzalUVWu73ZSSGw3jtZSrNLmHlj8ugyHbY3nU%2BR%2BHxXqBzJpWFPUJCSQtQzDE9PGDpd%2B0FWbY5x%2Fe65U&X-Amz-Signature=501bc8e458773eaaa9b4e1a88d4e7ec403762b0b0003357d79fb8e9c07b43207&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 3. Histogram
A histogram is an important visual representation of data in categorical form. To view the data in a "Binned" form, use the histogram plot with a number of bins required or with the data points that mark the bin edges. The x-axis represents the data bins, and the y-axis represents the number of elements in each bin.
**Syntax:**
```python
plt.hist(x, bins)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/24e4424a-df87-40a1-b63b-195cbdc2e0ab/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664WXJTOUW%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T171302Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDAaCXVzLXdlc3QtMiJGMEQCIB7MnfRZuhdj%2FJmlCk8x9SDAGNabSYT2FLbKDJjxSgj5AiAWeh1qvcfbJmL2%2F%2BTrAIMljeuf75Uaa9JExx%2FqQJ7EhCr%2FAwhJEAAaDDYzNzQyMzE4MzgwNSIMJeMbA8VoY4i8uobzKtwDrQ6OFh8SmjzV90JqFdI2ryN59VFktzgXojv9wbWmbUGeJp3LXW6MUp7kfPrSSuL3j%2BTp326LS4FXjN4pbBIxtkAV8FwjfPZvJrzwpT7qu5nXIM5hMZur6TB2enE7tPL6krXMZ%2FpGYvcYv7qNBE2HdYbT1eMpvivN2bDoJpcDh3Nb%2BS2G5NptMZBBwOR04P3zaM1IACuAJ4DcS1a9jDX07EXKie%2BXHAILDMp4hlc%2BzVL9l5eONZibL4tw8bI9a4Bg3w19%2BRZqC3SdssE0l7DZVVJjf78XoEmbRE78b1MtYIzCUkKFIPVOgOZIFTNoa%2F1X9nU7BlD4Bq0ClCsEHbHnjVt5N0NU4xdItJAXCock3IQjXFvFNOgH8sPYVnQfnw9OFSxdYaqJdaVTEQDMVTgatQj6reCkoK3o%2Fnie7dPrRe9%2BJSrJ7rTJEmr93h%2F%2F%2F6anOHBlFkEo19DxTBJuLFTktnrFCjq20APhZ2SsBgl9CLczZXkf7l1YBvqMx6l%2FNawHH7JZjtVGHqkMBaPDeIyVGN9hTvXDiN8bqNk1X8d4L9ZY%2BOMx%2FtIJ1mV7GstvVduD2qi2i96mZM572l0PbxesTH7f19rUJO8pFuwC4CMZq6oAYdROapQ2qyYUSVcw9p2OvQY6pgGwILK9aUNzQ3N745dZNSa5JFRTXd3KZY4zi%2BcYrXGAOPzKnWgkQvLrG%2B2Uets3A5xfYBVOH8ewA2EUThrTEg5q%2FYR20vfP49pa1LiXGYZpvlJA2t2MWIire7tmKX7Tl2YrFMHOjItarX9XMzalUVWu73ZSSGw3jtZSrNLmHlj8ugyHbY3nU%2BR%2BHxXqBzJpWFPUJCSQtQzDE9PGDpd%2B0FWbY5x%2Fe65U&X-Amz-Signature=244fd8f3d50d3b7e9259b652b7ae93853a27c2ab362e441fa33a209742b4a561&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ab5a6dfe-51f5-43ee-bcb3-33dae4a1c7ad/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664WXJTOUW%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T171302Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDAaCXVzLXdlc3QtMiJGMEQCIB7MnfRZuhdj%2FJmlCk8x9SDAGNabSYT2FLbKDJjxSgj5AiAWeh1qvcfbJmL2%2F%2BTrAIMljeuf75Uaa9JExx%2FqQJ7EhCr%2FAwhJEAAaDDYzNzQyMzE4MzgwNSIMJeMbA8VoY4i8uobzKtwDrQ6OFh8SmjzV90JqFdI2ryN59VFktzgXojv9wbWmbUGeJp3LXW6MUp7kfPrSSuL3j%2BTp326LS4FXjN4pbBIxtkAV8FwjfPZvJrzwpT7qu5nXIM5hMZur6TB2enE7tPL6krXMZ%2FpGYvcYv7qNBE2HdYbT1eMpvivN2bDoJpcDh3Nb%2BS2G5NptMZBBwOR04P3zaM1IACuAJ4DcS1a9jDX07EXKie%2BXHAILDMp4hlc%2BzVL9l5eONZibL4tw8bI9a4Bg3w19%2BRZqC3SdssE0l7DZVVJjf78XoEmbRE78b1MtYIzCUkKFIPVOgOZIFTNoa%2F1X9nU7BlD4Bq0ClCsEHbHnjVt5N0NU4xdItJAXCock3IQjXFvFNOgH8sPYVnQfnw9OFSxdYaqJdaVTEQDMVTgatQj6reCkoK3o%2Fnie7dPrRe9%2BJSrJ7rTJEmr93h%2F%2F%2F6anOHBlFkEo19DxTBJuLFTktnrFCjq20APhZ2SsBgl9CLczZXkf7l1YBvqMx6l%2FNawHH7JZjtVGHqkMBaPDeIyVGN9hTvXDiN8bqNk1X8d4L9ZY%2BOMx%2FtIJ1mV7GstvVduD2qi2i96mZM572l0PbxesTH7f19rUJO8pFuwC4CMZq6oAYdROapQ2qyYUSVcw9p2OvQY6pgGwILK9aUNzQ3N745dZNSa5JFRTXd3KZY4zi%2BcYrXGAOPzKnWgkQvLrG%2B2Uets3A5xfYBVOH8ewA2EUThrTEg5q%2FYR20vfP49pa1LiXGYZpvlJA2t2MWIire7tmKX7Tl2YrFMHOjItarX9XMzalUVWu73ZSSGw3jtZSrNLmHlj8ugyHbY3nU%2BR%2BHxXqBzJpWFPUJCSQtQzDE9PGDpd%2B0FWbY5x%2Fe65U&X-Amz-Signature=360473658b30021e450167a1c96bc603492e54a6dca077b987b0d693b7ba5ded&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8f1b1d60-cf1b-42b3-9faa-f634c89c3f84/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664WXJTOUW%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T171302Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDAaCXVzLXdlc3QtMiJGMEQCIB7MnfRZuhdj%2FJmlCk8x9SDAGNabSYT2FLbKDJjxSgj5AiAWeh1qvcfbJmL2%2F%2BTrAIMljeuf75Uaa9JExx%2FqQJ7EhCr%2FAwhJEAAaDDYzNzQyMzE4MzgwNSIMJeMbA8VoY4i8uobzKtwDrQ6OFh8SmjzV90JqFdI2ryN59VFktzgXojv9wbWmbUGeJp3LXW6MUp7kfPrSSuL3j%2BTp326LS4FXjN4pbBIxtkAV8FwjfPZvJrzwpT7qu5nXIM5hMZur6TB2enE7tPL6krXMZ%2FpGYvcYv7qNBE2HdYbT1eMpvivN2bDoJpcDh3Nb%2BS2G5NptMZBBwOR04P3zaM1IACuAJ4DcS1a9jDX07EXKie%2BXHAILDMp4hlc%2BzVL9l5eONZibL4tw8bI9a4Bg3w19%2BRZqC3SdssE0l7DZVVJjf78XoEmbRE78b1MtYIzCUkKFIPVOgOZIFTNoa%2F1X9nU7BlD4Bq0ClCsEHbHnjVt5N0NU4xdItJAXCock3IQjXFvFNOgH8sPYVnQfnw9OFSxdYaqJdaVTEQDMVTgatQj6reCkoK3o%2Fnie7dPrRe9%2BJSrJ7rTJEmr93h%2F%2F%2F6anOHBlFkEo19DxTBJuLFTktnrFCjq20APhZ2SsBgl9CLczZXkf7l1YBvqMx6l%2FNawHH7JZjtVGHqkMBaPDeIyVGN9hTvXDiN8bqNk1X8d4L9ZY%2BOMx%2FtIJ1mV7GstvVduD2qi2i96mZM572l0PbxesTH7f19rUJO8pFuwC4CMZq6oAYdROapQ2qyYUSVcw9p2OvQY6pgGwILK9aUNzQ3N745dZNSa5JFRTXd3KZY4zi%2BcYrXGAOPzKnWgkQvLrG%2B2Uets3A5xfYBVOH8ewA2EUThrTEg5q%2FYR20vfP49pa1LiXGYZpvlJA2t2MWIire7tmKX7Tl2YrFMHOjItarX9XMzalUVWu73ZSSGw3jtZSrNLmHlj8ugyHbY3nU%2BR%2BHxXqBzJpWFPUJCSQtQzDE9PGDpd%2B0FWbY5x%2Fe65U&X-Amz-Signature=c380607b954ae6e9990d60380f61711aeb538cf23794f02faad176e490ce9370&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/13ad0497-05fe-4eaa-984e-707b33e14761/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664WXJTOUW%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T171303Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDAaCXVzLXdlc3QtMiJGMEQCIB7MnfRZuhdj%2FJmlCk8x9SDAGNabSYT2FLbKDJjxSgj5AiAWeh1qvcfbJmL2%2F%2BTrAIMljeuf75Uaa9JExx%2FqQJ7EhCr%2FAwhJEAAaDDYzNzQyMzE4MzgwNSIMJeMbA8VoY4i8uobzKtwDrQ6OFh8SmjzV90JqFdI2ryN59VFktzgXojv9wbWmbUGeJp3LXW6MUp7kfPrSSuL3j%2BTp326LS4FXjN4pbBIxtkAV8FwjfPZvJrzwpT7qu5nXIM5hMZur6TB2enE7tPL6krXMZ%2FpGYvcYv7qNBE2HdYbT1eMpvivN2bDoJpcDh3Nb%2BS2G5NptMZBBwOR04P3zaM1IACuAJ4DcS1a9jDX07EXKie%2BXHAILDMp4hlc%2BzVL9l5eONZibL4tw8bI9a4Bg3w19%2BRZqC3SdssE0l7DZVVJjf78XoEmbRE78b1MtYIzCUkKFIPVOgOZIFTNoa%2F1X9nU7BlD4Bq0ClCsEHbHnjVt5N0NU4xdItJAXCock3IQjXFvFNOgH8sPYVnQfnw9OFSxdYaqJdaVTEQDMVTgatQj6reCkoK3o%2Fnie7dPrRe9%2BJSrJ7rTJEmr93h%2F%2F%2F6anOHBlFkEo19DxTBJuLFTktnrFCjq20APhZ2SsBgl9CLczZXkf7l1YBvqMx6l%2FNawHH7JZjtVGHqkMBaPDeIyVGN9hTvXDiN8bqNk1X8d4L9ZY%2BOMx%2FtIJ1mV7GstvVduD2qi2i96mZM572l0PbxesTH7f19rUJO8pFuwC4CMZq6oAYdROapQ2qyYUSVcw9p2OvQY6pgGwILK9aUNzQ3N745dZNSa5JFRTXd3KZY4zi%2BcYrXGAOPzKnWgkQvLrG%2B2Uets3A5xfYBVOH8ewA2EUThrTEg5q%2FYR20vfP49pa1LiXGYZpvlJA2t2MWIire7tmKX7Tl2YrFMHOjItarX9XMzalUVWu73ZSSGw3jtZSrNLmHlj8ugyHbY3nU%2BR%2BHxXqBzJpWFPUJCSQtQzDE9PGDpd%2B0FWbY5x%2Fe65U&X-Amz-Signature=a04bf899b86ef4e352603fc3af8ba3610db44f58c1ec3ab34d56f1e1d94a338a&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 2. Box and Whisker Plot
A box plot shows the distribution of quantitative data in a way that facilitates comparisons between variables or across levels of a categorical variable. The box shows the quartiles of the dataset while the whiskers extend to show the rest of the distribution, except for points that are determined to be "outliers".
**Syntax:**
```python
sns.boxplot(x='header_1', y='header_2', data=df)
```
**Example Output:**


![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d207ae92-0a7c-4e2f-aa65-0ee5a2c33bf7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662SAXWHGF%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T171305Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDAaCXVzLXdlc3QtMiJGMEQCICmQwT6aaRgAY9%2BrcGFrwh4WDp9fL74PUnEDhDm%2F3YZgAiBFiPucKxpmHZgcQbMbiRvX4JhEInm6wAfXnsMxqWWwhSr%2FAwhJEAAaDDYzNzQyMzE4MzgwNSIM1vpqCty4lvsfX8NrKtwDXg9O%2FsdhUJY1z7mzhj%2BhVqtQZWn9oy2UQZ6AeDFyOOPNr0gklttOVJ7MpCz3F09iWH5Me177yF7z3mRHYMfgP9usCU3%2BZDB91jr1YAwfuFgpr82hrqv%2BuMOXbjgp8DoZ%2BaGssZxBrvLn%2BiIWdczbdQnmLNL8S5LGxrCFfW3rupary1%2Fy0N1en05iCjoZy5SksyBj8TcdoESm9wj%2FZFWBN8AnzvnmF7pjWYBD8sdJaAc9DkJgj6Lf3L%2BJCVftb55XSHgwhixuaBgkOw01tPFxvM5J3AZnSbz%2FdA0RsQkADaKhIMtmaQ8K50ryY0wt%2FwRYwCCv%2B8HKfWoraqRdlCZE0s7bQ8%2BpwoX8gm9jtT9Ql2tytB4ecFDPAFie8sxgHkYOW4BtyUnfFjJKC91q9wdLJsPQV%2BtawB9xWDjJD6%2BkIXQMu3VwBx%2Fx9vZe8bLlAEn0avWgAf08IwpjmzKxPlM70bHuP9WH17LRD6WAlL1REMjfdF%2Bo2%2BFZL1c81Sf4w8rNaTa1WEqONgIy3BvQeTywHCYUjw%2BOdZmrQFOzR79mQECao%2FpQr8hCWXgJHF%2F%2F251XS0MSznbqd5J%2FKjX2aO2yftk9UL8v8di9bbaaMQfBEgtSbpyezo%2BOQTr%2F%2Bb8w7p2OvQY6pgFYbmhDOrWWArK84sJIrd2gleAhIH62MbgGb4mubnQyF8eb1yn%2FEHWS5HtITvoVIMoBfiMmYimHUizUIyDAzAcZEBxhfKoeOBQtv3AJWjoX1QavcM9AlQxQUlAG6Bauau2nsNWH317saOfttcypq8bOr8t%2BRRLGGDl2437sAKC7JGz2rYt3ELQ9fLrM4eJyqxubS7qMqkFWGsmO%2FMB0s%2FqAT57Ieo26&X-Amz-Signature=e5895a8fd761fd9623be7131dd860896cfb54ee60140bc10132629c4fcc91038&X-Amz-SignedHeaders=host&x-id=GetObject)

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0e516edc-7551-4792-ab18-0494db3c4c0c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664VXEWGZR%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T171305Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDAaCXVzLXdlc3QtMiJGMEQCIHcNEcshQjPGrS8wkJuFHXv2W2mGUHMvxXbpTHDV4KO0AiALaNuyvrmLRx0dlTFGLndW1sYyaBzHNK%2FeI2F%2FjKXoyyr%2FAwhJEAAaDDYzNzQyMzE4MzgwNSIM3BcX8TJGZvmDkut0KtwDIAXGwZSEDZ%2BJPGvDtmm3IrsWZYhhy9bhHk3WruTbGF7OZzdaNpN9jgcyU2YIdbDJ0OvNxC7h2DsCyBkGp13ycMlLFivRe4KxcwLkfYVT2P163wHANtorn%2BGQxjeoZ1UhvK5bzsuhF4UpLkFxAkfZeAqEf25U%2Ft4MNd9gkxTbxMOrxQEEI3H%2BBVW8L5XzK4bn9kPnESX%2BmeoaBDhmXnGmks%2Fh1JQyIaZEkOiUYGXMWMo63Vf28BSwXuLv0OqvEWhXK61SZtrtkLmzP7lc2ewkf4kMjM%2BcWkIglsw95DC0qry56FW%2B3hmitZOH5GloGVa6qiUeiAAK7CZkRuY0mSGsfTofNPon24NFFk9zbZsOhyiK0knooiaL3N5CD3IZoA7vYE0FLDldetxRxkDkUTd7UHkBfJSj2lLAaD%2FlrbIY62JMyRpjj73g3%2Fv59YEymYWS6b19zQ%2B1YMq2B4hU25x9UXtvfq84YlMt8ebAju3E%2B2WJRhZkYiYMpJvOXmuO7DYHlA2B7sCZS50wxTNZGhOquVxNr6IKBlxQPO97I2jwdNq9Nss1rbyd%2B1ra9%2B5syMw5t4oh9dme8kED1uiY7T99yZuJB5jlDgOEF9UD6Si8572pDTjxAAWjMCcC7xkwpZ2OvQY6pgF5N33novAHW4%2FGwxnK5kL2zRW7bGiomoRtL%2BlLwta%2BDKoK8XL%2FjEJF5oeiz4D35NTeyRu5K4C4TD%2B5%2FjNOKMTSGE4p5I6Rli696RNkC2kzK9HI7q6jjbvcXiMH5ObU4zhw6BI16blVzKwt6FadtQhfOJKMnbQFNzck33DW9YN9DNVgUSPiKePoJW5Ckh3BxfOA67jv3GqEnCylbZz6Vlbvvk5YqaWk&X-Amz-Signature=db281f0e6475b7db8bede0a1a3e72f847bf53d1c804885ec75b088d593cefeeb&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23a79b9d-2356-49a9-8fd9-65c6b0ab2cc5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664WXJTOUW%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T171304Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDAaCXVzLXdlc3QtMiJGMEQCIB7MnfRZuhdj%2FJmlCk8x9SDAGNabSYT2FLbKDJjxSgj5AiAWeh1qvcfbJmL2%2F%2BTrAIMljeuf75Uaa9JExx%2FqQJ7EhCr%2FAwhJEAAaDDYzNzQyMzE4MzgwNSIMJeMbA8VoY4i8uobzKtwDrQ6OFh8SmjzV90JqFdI2ryN59VFktzgXojv9wbWmbUGeJp3LXW6MUp7kfPrSSuL3j%2BTp326LS4FXjN4pbBIxtkAV8FwjfPZvJrzwpT7qu5nXIM5hMZur6TB2enE7tPL6krXMZ%2FpGYvcYv7qNBE2HdYbT1eMpvivN2bDoJpcDh3Nb%2BS2G5NptMZBBwOR04P3zaM1IACuAJ4DcS1a9jDX07EXKie%2BXHAILDMp4hlc%2BzVL9l5eONZibL4tw8bI9a4Bg3w19%2BRZqC3SdssE0l7DZVVJjf78XoEmbRE78b1MtYIzCUkKFIPVOgOZIFTNoa%2F1X9nU7BlD4Bq0ClCsEHbHnjVt5N0NU4xdItJAXCock3IQjXFvFNOgH8sPYVnQfnw9OFSxdYaqJdaVTEQDMVTgatQj6reCkoK3o%2Fnie7dPrRe9%2BJSrJ7rTJEmr93h%2F%2F%2F6anOHBlFkEo19DxTBJuLFTktnrFCjq20APhZ2SsBgl9CLczZXkf7l1YBvqMx6l%2FNawHH7JZjtVGHqkMBaPDeIyVGN9hTvXDiN8bqNk1X8d4L9ZY%2BOMx%2FtIJ1mV7GstvVduD2qi2i96mZM572l0PbxesTH7f19rUJO8pFuwC4CMZq6oAYdROapQ2qyYUSVcw9p2OvQY6pgGwILK9aUNzQ3N745dZNSa5JFRTXd3KZY4zi%2BcYrXGAOPzKnWgkQvLrG%2B2Uets3A5xfYBVOH8ewA2EUThrTEg5q%2FYR20vfP49pa1LiXGYZpvlJA2t2MWIire7tmKX7Tl2YrFMHOjItarX9XMzalUVWu73ZSSGw3jtZSrNLmHlj8ugyHbY3nU%2BR%2BHxXqBzJpWFPUJCSQtQzDE9PGDpd%2B0FWbY5x%2Fe65U&X-Amz-Signature=dac836556ec0dc453936e4fa5a2aa4140d798c4fde7db29fb6182c3778644b7d&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 4. KDE Plot
A Kernel Density Estimate (KDE) plot is a graph that creates a probability distribution curve for the data based upon its likelihood of occurrence on a specific value. This is created for a single vector of information.
**Syntax:**
```python
sns.kdeplot(X) || sns.kdeplot(df['age'])
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0d571213-2a2f-4921-a50b-880847aa05ee/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664WXJTOUW%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T171303Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDAaCXVzLXdlc3QtMiJGMEQCIB7MnfRZuhdj%2FJmlCk8x9SDAGNabSYT2FLbKDJjxSgj5AiAWeh1qvcfbJmL2%2F%2BTrAIMljeuf75Uaa9JExx%2FqQJ7EhCr%2FAwhJEAAaDDYzNzQyMzE4MzgwNSIMJeMbA8VoY4i8uobzKtwDrQ6OFh8SmjzV90JqFdI2ryN59VFktzgXojv9wbWmbUGeJp3LXW6MUp7kfPrSSuL3j%2BTp326LS4FXjN4pbBIxtkAV8FwjfPZvJrzwpT7qu5nXIM5hMZur6TB2enE7tPL6krXMZ%2FpGYvcYv7qNBE2HdYbT1eMpvivN2bDoJpcDh3Nb%2BS2G5NptMZBBwOR04P3zaM1IACuAJ4DcS1a9jDX07EXKie%2BXHAILDMp4hlc%2BzVL9l5eONZibL4tw8bI9a4Bg3w19%2BRZqC3SdssE0l7DZVVJjf78XoEmbRE78b1MtYIzCUkKFIPVOgOZIFTNoa%2F1X9nU7BlD4Bq0ClCsEHbHnjVt5N0NU4xdItJAXCock3IQjXFvFNOgH8sPYVnQfnw9OFSxdYaqJdaVTEQDMVTgatQj6reCkoK3o%2Fnie7dPrRe9%2BJSrJ7rTJEmr93h%2F%2F%2F6anOHBlFkEo19DxTBJuLFTktnrFCjq20APhZ2SsBgl9CLczZXkf7l1YBvqMx6l%2FNawHH7JZjtVGHqkMBaPDeIyVGN9hTvXDiN8bqNk1X8d4L9ZY%2BOMx%2FtIJ1mV7GstvVduD2qi2i96mZM572l0PbxesTH7f19rUJO8pFuwC4CMZq6oAYdROapQ2qyYUSVcw9p2OvQY6pgGwILK9aUNzQ3N745dZNSa5JFRTXd3KZY4zi%2BcYrXGAOPzKnWgkQvLrG%2B2Uets3A5xfYBVOH8ewA2EUThrTEg5q%2FYR20vfP49pa1LiXGYZpvlJA2t2MWIire7tmKX7Tl2YrFMHOjItarX9XMzalUVWu73ZSSGw3jtZSrNLmHlj8ugyHbY3nU%2BR%2BHxXqBzJpWFPUJCSQtQzDE9PGDpd%2B0FWbY5x%2Fe65U&X-Amz-Signature=7d0cd1d5e293fb5c4ee4c003fe9e8afd1758559d72fbfccb62953fb33f363cb3&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/53752550-ef82-4ca9-a01a-09921f0282d0/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664WXJTOUW%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T171304Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDAaCXVzLXdlc3QtMiJGMEQCIB7MnfRZuhdj%2FJmlCk8x9SDAGNabSYT2FLbKDJjxSgj5AiAWeh1qvcfbJmL2%2F%2BTrAIMljeuf75Uaa9JExx%2FqQJ7EhCr%2FAwhJEAAaDDYzNzQyMzE4MzgwNSIMJeMbA8VoY4i8uobzKtwDrQ6OFh8SmjzV90JqFdI2ryN59VFktzgXojv9wbWmbUGeJp3LXW6MUp7kfPrSSuL3j%2BTp326LS4FXjN4pbBIxtkAV8FwjfPZvJrzwpT7qu5nXIM5hMZur6TB2enE7tPL6krXMZ%2FpGYvcYv7qNBE2HdYbT1eMpvivN2bDoJpcDh3Nb%2BS2G5NptMZBBwOR04P3zaM1IACuAJ4DcS1a9jDX07EXKie%2BXHAILDMp4hlc%2BzVL9l5eONZibL4tw8bI9a4Bg3w19%2BRZqC3SdssE0l7DZVVJjf78XoEmbRE78b1MtYIzCUkKFIPVOgOZIFTNoa%2F1X9nU7BlD4Bq0ClCsEHbHnjVt5N0NU4xdItJAXCock3IQjXFvFNOgH8sPYVnQfnw9OFSxdYaqJdaVTEQDMVTgatQj6reCkoK3o%2Fnie7dPrRe9%2BJSrJ7rTJEmr93h%2F%2F%2F6anOHBlFkEo19DxTBJuLFTktnrFCjq20APhZ2SsBgl9CLczZXkf7l1YBvqMx6l%2FNawHH7JZjtVGHqkMBaPDeIyVGN9hTvXDiN8bqNk1X8d4L9ZY%2BOMx%2FtIJ1mV7GstvVduD2qi2i96mZM572l0PbxesTH7f19rUJO8pFuwC4CMZq6oAYdROapQ2qyYUSVcw9p2OvQY6pgGwILK9aUNzQ3N745dZNSa5JFRTXd3KZY4zi%2BcYrXGAOPzKnWgkQvLrG%2B2Uets3A5xfYBVOH8ewA2EUThrTEg5q%2FYR20vfP49pa1LiXGYZpvlJA2t2MWIire7tmKX7Tl2YrFMHOjItarX9XMzalUVWu73ZSSGw3jtZSrNLmHlj8ugyHbY3nU%2BR%2BHxXqBzJpWFPUJCSQtQzDE9PGDpd%2B0FWbY5x%2Fe65U&X-Amz-Signature=052c41be91064e40effe271a01db826acb392599d6dc6b23a85a2ce5cab4401f&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
## 4. Correlation Between Variables
Correlation is a statistical measure of the extent to which different variables are interdependent. It indicates how changes in one variable are associated with changes in another variable over time.
### Positive Correlation
Positive correlation indicates that as one variable increases, the other variable also tends to increase.
**Example: Engine Size and Price**
- **Positive Correlation:** Engine size increases, price also increases.
- **Visualization:** Scatter plot with a steep positive slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c7ea9b0-3ef3-4357-a9c3-554fc71b6b15/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SC6DFKVA%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T171305Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDEaCXVzLXdlc3QtMiJHMEUCIQDwT86cdnvekTTR6Rey4VE%2F9By8TiC1q5bJG98aEiDALwIgU7Xy8mDZNNIwhRFnoia1KrvFX5lYJzzQBWyCzl%2FWN8Qq%2FwMISRAAGgw2Mzc0MjMxODM4MDUiDMoaV3VPTht7TxZrySrcAwvfjJvuUZ4nTfy%2FyhpjSvoEe6e8f5fsh8ZHQSdqxCG7XOY1TYZmN%2FHI7%2B7bo1sQvHTl4x4o%2BH6NgRunlDO86uibfzYc8hEDASqE2PwIhVaiyjXPnuVVPzzrhhWOAp4tff%2FKdVLOgfkkyRzTmssrP0h0nZaS9y6Lk79rfUe6d8SWjm1Prb4YgOmaovrWTk%2F0xZEwiqMRolhDJIQRv8P3OCSeoDwdCHb5biNXjuUNdrQQgHv2Vcw9BKYCNzvNwzuxxsNT%2FKbragQiiaDl8k6oceJH7DpyFUrPwrHDYq%2BLbtC08ZNNiCG9FtEdYSIksRfAFJs2QqW7HpszIoGOkAdlfnju6ynXVa7gf2NUceXizJ44WtNR5hIlrpvbWz8x%2Bcn3nAYz%2BRb0Arkv4i6wgMtsKNo%2BUI5wzTmbsGoxl2zlSsgPlR1nwLZIZVsi6uL2qGw7Ej4umFoxPMEmQjQDZSKv3RU7Pl8gJFMgzKqwXHt%2FhesUJ%2BIei6pRmAtRjLZMOhAIq1LVsyn8YIXwbhLlSsgPTWCfSYVibtw6PXszIy8hwIoaukNBqTmhb1u3RwzXAWsOSfpuGvDEqQxdfJWrl49NajYTiPYTs%2Bo3jD9mJFTWwH88rHoMof0r5hUsDo5BMPeejr0GOqUBGHY2yCHYBHfFQulNAru7Bz2r4iIXI9b7xxcVpRXVV%2FTj9gC0mW0zZRuWP%2F3nqW%2BsYZQHQRT%2FRsntkEseh%2FnCIGVHz1ZNXqDshhrxa9u84QS8MImeVZ%2BKD15arr7O1oiEZcTtfquz57wU8ZlLgXzSF%2BOcqQYgkCXBmakHDqMtYP5G%2FnmiNZf4K3WOYbojgeLFTDa2LyYz25AsDHgBpFRHoaIQkY1x&X-Amz-Signature=42fd052c3804dbe5fcf97643b3a4d6e8c81e95e73f19a581910691293b49a4f0&X-Amz-SignedHeaders=host&x-id=GetObject)
**Explanation:** When engine size increases, there is a corresponding increase in the price of the vehicle. This positive correlation suggests that larger engines tend to be associated with higher prices in the market.
___
### Negative Correlation
Negative correlation indicates that as one variable increases, the other variable tends to decrease.
**Example: Highway Miles per Gallon and Price**
- **Negative Correlation:** As highway miles per gallon increases, price decreases.
- **Visualization:** Scatter plot with a steep negative slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/10f1f798-9cc4-4df2-a9c1-5a339f554a0b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WKTAEI76%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T171305Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDAaCXVzLXdlc3QtMiJGMEQCIAE5P1kiRE%2Fvd0Nm3UB4Mhg9FRi%2F6AN%2FU%2FbgyeEcyKIvAiATC0QdKs5I2p29Wq8OB%2FG1Ms9oTbLUiGxaZlCSvlJmACr%2FAwhJEAAaDDYzNzQyMzE4MzgwNSIMO8S4S%2FTp555fubwTKtwDWmOMwCJ%2B2Sur6MIedmtle7AvZ1HJpG%2B%2BKazqWl9qBInooZ7ViiKpBN5vKS1wFKo2pZaR4woy7Q9SiRMnP860UqIuZydxinBcc8ltCETwFKs%2FIjinVi9qeuhjU9GBULPUXPIy8EckU9m3m0RSgLGN5APehRjO3tYj%2BuEJwY5gqfte0JJ0XYz1vLIwLcf%2Fg5cO2RbOUJYdDt1HqpJvoCuJqiMdx3rRHuBAwdsqr5SZSbO4zT6fjsJ557rmaXyHYP442cMWOxvCMEGKQE%2F71nm8Gabn6ChixSHMfVwW08YKrT6%2F5DeO6913fEUP6kbFUvuruDSjzrOFAos4G5G54d0i6IkhtSQiTkqgL0lbXyOE5IUhZUViP95ESjuIgBk2gOdi477SVV1%2BLlLss6o07qkq7UTInT9QLgx1lwJzV2QywBazXMAFMy93pW9VJmnhKnW1JdDtenvpwWg6T9ZETVHBYBhxMmAOaP5OOkTDhvrUEEyq1x8Lu09Ss51cT1x0xv5aBcvU%2FwwMcrlJisSJrnoJVQv2Elg2uxh%2FPUzzKGtUunxdgwbhvJg2TVQc%2Bae7%2FuhZH7JSEhbJ0CczVNyeS%2BhvdJ%2BVzYqj1XEm0HGkJi4S8ORRDtzMn5EfOEnUdhwwwZ2OvQY6pgFKjxP6kxeBUyXj7NyanuxIQAj%2BrNbMAmmAw7j6tUvHj4D5vCH0dFyarDTLjNLjTrUENygefQzwqAFuZ0femYOmWQl%2B3YVyYBW4cx1jnNzKZ2VMWcEDdj9PmmLbAEWZ2tWil%2FELmypokFbrVkQAs4ZRv4%2FfZkzwL%2Bktwaa9sGGO9yhBwCPheY1ZEM4eecr%2F%2BGbEE7mlxSMf7uJOkyTJIdZqLdbcszWp&X-Amz-Signature=338e25677da6d28ad96147b7f512deb9c8b5e1210296ac2d62fc7f98df49ba9d&X-Amz-SignedHeaders=host&x-id=GetObject)
**Explanation:** When highway miles per gallon increases, the price of the vehicle tends to decrease. This negative correlation suggests that cars with higher fuel efficiency (more miles per gallon) are generally priced lower in the market.
___
### Weak Correlation
Weak correlation indicates a lack of strong relationship between the variables.
**Example: RPM and Price**
- **Weak Correlation:** Low and high RPM values show varied prices, indicating no strong predictive relationship.
- **Visualization:** Scatter plot with no clear trend or slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9f914514-8914-4bf4-ac84-d9e3077f6eb1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WP2U3D4S%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T171305Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDAaCXVzLXdlc3QtMiJHMEUCIAyVAEaafgizQN%2B1BWNIg5qk%2FL3DlzExsKu294y2HgKjAiEAsmJ8o8mo%2B2G4baKyO%2BJYeAzLc5aku7Wa80q5NhUSEOYq%2FwMISRAAGgw2Mzc0MjMxODM4MDUiDGl2yWWO7N6%2B%2BbE81SrcA%2FanHoXAaCk8kgZQFQQ2107puEKXdZ2VfOxK9VyC%2BNFGIqy5nLoEvUCYeerPrqrJotzzZsk2TzYcTweUSZ0GcgivXKQuWof%2F7VP1K3EkEk4XYCyZiEiHEwiTZjffHSmDvb47w%2BMIM%2FCTfhbkNDiYtFhVj3D48qKGx19xKvtfGyAsWAeL9BCb4ubFvox0%2FOjLgJ6lLIYN9bIsd8VlsdkNS7aC%2BXd8KBAU2VlG5eBW9jd6tpirpnU4bhenvBLcJIrt3Cj49N5H47qQ5jtn3qsLC%2BlWOktpOXkyKhO9IETFsWMT7YPKGB2hkgMRw9VXxiwa%2BBfP9XXwrVS9yRpICr1vE7P1yhNzhCLE8EFpJE5WdZTNNxpkleNUjJ%2FjAXkh%2BpI5AsfMGI9Rd8hJ1vkxRJMEtQyQ0aoukDvwFPCRdWJsDMG2ANeOJxmDCZM4Xex1d5BXJJ71gCR77RM6bWS5KwTj49fEHn43iHlR%2BE5C7il0CXrQ4uhRVHH8eCx70fLPQnHbc9KYSibpB4XzefkePEtoRouyTF%2FL4wFSWNXvPiIrkJEC%2F8x2e0%2BeiyhB9UOSP296AJQSy%2BQQUMUAu9smotsBoKaW4NeWVHf8fVJ6SPkpDWeUHzl3wEzQIE0zMcjIMOadjr0GOqUBuaeP4To9IiwuHaPCGsfCVwvssV%2B4td3EO9DLhiuv0zgyUTR7fxTfHWLTWV4vW0ejPB1MGlPEGZoOwIxY3xbAI8X%2FSz%2FLILAj4Z49eou7DuchyyY3ZoAUHgoC0bNhBTyhb806Zsog4IX9ZcKmvFi9jlrwMpUMT2TXbhm5bMCiTFTQ3fYjc9ZfXGbrdQeacresaKki3n6FlHwxnoAgG7asYEA5bzTp&X-Amz-Signature=1c1b814bf2296e163bdec7bf36a3c60fec6db35585266c50d8c7dd77c2099497&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f18086e5-5b04-4fbf-8309-8944ab20d213/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RUYUDSVT%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T171305Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDAaCXVzLXdlc3QtMiJHMEUCIQDLied4a3NKVravdwy0C0qtpMD%2FNtr%2BHv%2Bx70n%2FEMmZcAIgCXzh5eCCvppi4CFGkUbJFNeIGjBHpMyMmApMRZw%2BdTAq%2FwMISRAAGgw2Mzc0MjMxODM4MDUiDMpyW09KHU4hIXDxFSrcA4lOoBuHzhPqMe%2Bkwx%2F%2FWdR4tERxw7ln6ebylpnjHl9ChD0uD1jpiVIKyw3eoWM4SFoamcgO7%2FEAyObBJgcIdWc8ovbGrxht4aKp75DHFYuvfge0A88yaaPTp4TUq315jLW2ulKa2CsmEwmKM2w5u7Y%2BPQyRYfB23qUHmcUN5QxKRG4yTUHw%2F7DbiNoPZeTcbCvcPEmMXRzO8MTJYLftR505bJDwgAIeuHT0MPj2xJTromxlOeq%2BqcxanCgXrtSaVJbpVZlE58zPS8y6aURZW%2FiuIW0OhvbgLirLJazh2z%2Fvdb%2FJA4DKaYWWVHLceB5T3bgdF1MgWC8Ko8ER6IZitUblkhacXlaP%2BtHY3eGnCioRR12Xj5HEmhVqdE1e%2BinBDPJ5ezVVoN3uvgD44aO8uKj79jtwh4ogy%2BRdr2wmnB5KSchCXQmfImRQiUzzvBfDjpLlCeBDJklCigZrhPAD9v1AvyH1yIY7hEbfLZ3wYVlPH40J1U4AtoscMrQHm05qDK6T%2B%2FuFwvQ5wFm9dk8R719W8%2B2ssFISPly5SotRel1A9LGnbPtcwzEmafZCU97tSyZ2zK%2FZzSFUQJRqVCiM%2BsBd6Y%2FUl184C67hicudxGv5qgBNRqRGCxljBRFsMPadjr0GOqUBDpUVwZUxy7QbCPjMGqnoTANQVligVhXfHMmAgYbRc7w8%2Fp%2Bw5I%2FO10mp2ZUCWBq%2Be1h%2FrCbcBh8EyQlOAiWJBQM7nHS1zPfIhdFjeLgRXO70kYCZqdtpR%2F0%2BHKT5L7%2FvDo%2F3zcC2iy576UW5YQZDK5bU6SwGqc0e26xAfNqzxZHp3s%2BsoXOVBtlrwd7lPdafOThvMD5WTHJQla0yAFE3uVqB3zZD&X-Amz-Signature=512d9678a5a76552e1d13d9f963e43a09adc779e67b813a9ece29a9228d2128f&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Correlation Plot
Heatmap visualizes correlations among variables. Color scheme indicates Pearson correlation coefficients. Dark red diagonal line shows perfect correlation (value of 1) between variables and themselves.
This heatmap offers overview of variable relationships and their link with price.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cd3b341e-cc1a-45f7-8aec-cdc00436d270/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RUYUDSVT%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T171305Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDAaCXVzLXdlc3QtMiJHMEUCIQDLied4a3NKVravdwy0C0qtpMD%2FNtr%2BHv%2Bx70n%2FEMmZcAIgCXzh5eCCvppi4CFGkUbJFNeIGjBHpMyMmApMRZw%2BdTAq%2FwMISRAAGgw2Mzc0MjMxODM4MDUiDMpyW09KHU4hIXDxFSrcA4lOoBuHzhPqMe%2Bkwx%2F%2FWdR4tERxw7ln6ebylpnjHl9ChD0uD1jpiVIKyw3eoWM4SFoamcgO7%2FEAyObBJgcIdWc8ovbGrxht4aKp75DHFYuvfge0A88yaaPTp4TUq315jLW2ulKa2CsmEwmKM2w5u7Y%2BPQyRYfB23qUHmcUN5QxKRG4yTUHw%2F7DbiNoPZeTcbCvcPEmMXRzO8MTJYLftR505bJDwgAIeuHT0MPj2xJTromxlOeq%2BqcxanCgXrtSaVJbpVZlE58zPS8y6aURZW%2FiuIW0OhvbgLirLJazh2z%2Fvdb%2FJA4DKaYWWVHLceB5T3bgdF1MgWC8Ko8ER6IZitUblkhacXlaP%2BtHY3eGnCioRR12Xj5HEmhVqdE1e%2BinBDPJ5ezVVoN3uvgD44aO8uKj79jtwh4ogy%2BRdr2wmnB5KSchCXQmfImRQiUzzvBfDjpLlCeBDJklCigZrhPAD9v1AvyH1yIY7hEbfLZ3wYVlPH40J1U4AtoscMrQHm05qDK6T%2B%2FuFwvQ5wFm9dk8R719W8%2B2ssFISPly5SotRel1A9LGnbPtcwzEmafZCU97tSyZ2zK%2FZzSFUQJRqVCiM%2BsBd6Y%2FUl184C67hicudxGv5qgBNRqRGCxljBRFsMPadjr0GOqUBDpUVwZUxy7QbCPjMGqnoTANQVligVhXfHMmAgYbRc7w8%2Fp%2Bw5I%2FO10mp2ZUCWBq%2Be1h%2FrCbcBh8EyQlOAiWJBQM7nHS1zPfIhdFjeLgRXO70kYCZqdtpR%2F0%2BHKT5L7%2FvDo%2F3zcC2iy576UW5YQZDK5bU6SwGqc0e26xAfNqzxZHp3s%2BsoXOVBtlrwd7lPdafOThvMD5WTHJQla0yAFE3uVqB3zZD&X-Amz-Signature=2a84d5e9ffc948780151f71e893a1a19842aa84f51ffeff5968bb78a62bd3ec9&X-Amz-SignedHeaders=host&x-id=GetObject)

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
