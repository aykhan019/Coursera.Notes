

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7e6d594d-952e-44b6-97ea-31225882aea6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TIOMCLUU%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T221411Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEE0aCXVzLXdlc3QtMiJIMEYCIQCYzQgliwBt6yWYkQu1YTXKzYoolR4WNCo3g4%2BR2n%2FxMQIhAOIlypgU%2F0C4pGr2TaOjtOpCJFg2lXONHoQoQizJmGYQKv8DCGYQABoMNjM3NDIzMTgzODA1Igz%2BmChoZ%2F%2F5uBkhov8q3APsmlKCDTOXfGmc3mtZHCEFJdLI5dd9cWtgeqhJFLHngKRknjv58V%2FkldNEM31erZfRFjVw%2Bit6GFIf1vtNMQqt%2FderqyF2sDKEIzX7nHTSeTvR%2FdI2ACmOkBoGy8l6ZzAL6FG9AOXShdt8w%2F2wn0oHAOcMgjrwgs0S%2BYC6JVNFzsrk45XETRpMmmgDSO5hrX%2BiB%2BC%2B2vS1oPOJ8vas3eomTf9vJelcub88ob1mQlIHyzzwIxaAgIOhcCxbMMRWI4CJ8dD58IKy0xKNGz11dGFTgPHtADoVuyE0MPJ7P%2F1SWlJyrH%2FGxtq09UwlTl1i0zHKPxnVqu85enY%2F3RtGIvxEHCE922NfNVHt2Ul%2FX3MhbfgFQPNvMU09XWuzF%2BG20PRULfEp8%2FuCv%2FoQlkmGTypQwxnQ30dByn03Jcq3zlb2cwrVhW%2FHpaMWedM72X8ibuezMhS%2FEhx8SPvkTkJUf%2BTFWPq8HmSq7dSMeVvLuOnLZ%2FhpjQl17yUqw0qPpQ2XymKoPekls7KyyvO%2FCMVnZdx4VW4sY9qb5PEzWwqu0%2BTcjFVSemZlrdAvagOD7mPTZzw%2BPPpeI9vC%2FTunwH71BPD5wpP86E%2B4VD9n1N51uY4ejXukPalawBeyoFxrkjCUuJS9BjqkAcBJ3qW7cE8keRiO3lrMR7d%2BhtylTICpP9WGomKwAR2YBaxriZzlPKXtTPadYvgc4JiHvwvSkYqOxva%2F4vI9Me6DU%2BbPGIoRJNOjLk7FqMLlFNQ1FGHXWl2mDE0vpttpYDdvruGOJYHFHWfpFOJM7133YtkHd5y8%2F2J4Mwxjb7Wrzvb%2BTv1QRxYdJeRKQ%2FMdaL7lMpUVwg3f9q9EfrLg%2FjFDOKoK&X-Amz-Signature=dfec89d811dd5d0aa1ce89253405ab4423bf22ccaac619340d0e97fa75f60683&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cbfaed9e-b398-4902-8936-dea058b21def/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TIOMCLUU%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T221411Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEE0aCXVzLXdlc3QtMiJIMEYCIQCYzQgliwBt6yWYkQu1YTXKzYoolR4WNCo3g4%2BR2n%2FxMQIhAOIlypgU%2F0C4pGr2TaOjtOpCJFg2lXONHoQoQizJmGYQKv8DCGYQABoMNjM3NDIzMTgzODA1Igz%2BmChoZ%2F%2F5uBkhov8q3APsmlKCDTOXfGmc3mtZHCEFJdLI5dd9cWtgeqhJFLHngKRknjv58V%2FkldNEM31erZfRFjVw%2Bit6GFIf1vtNMQqt%2FderqyF2sDKEIzX7nHTSeTvR%2FdI2ACmOkBoGy8l6ZzAL6FG9AOXShdt8w%2F2wn0oHAOcMgjrwgs0S%2BYC6JVNFzsrk45XETRpMmmgDSO5hrX%2BiB%2BC%2B2vS1oPOJ8vas3eomTf9vJelcub88ob1mQlIHyzzwIxaAgIOhcCxbMMRWI4CJ8dD58IKy0xKNGz11dGFTgPHtADoVuyE0MPJ7P%2F1SWlJyrH%2FGxtq09UwlTl1i0zHKPxnVqu85enY%2F3RtGIvxEHCE922NfNVHt2Ul%2FX3MhbfgFQPNvMU09XWuzF%2BG20PRULfEp8%2FuCv%2FoQlkmGTypQwxnQ30dByn03Jcq3zlb2cwrVhW%2FHpaMWedM72X8ibuezMhS%2FEhx8SPvkTkJUf%2BTFWPq8HmSq7dSMeVvLuOnLZ%2FhpjQl17yUqw0qPpQ2XymKoPekls7KyyvO%2FCMVnZdx4VW4sY9qb5PEzWwqu0%2BTcjFVSemZlrdAvagOD7mPTZzw%2BPPpeI9vC%2FTunwH71BPD5wpP86E%2B4VD9n1N51uY4ejXukPalawBeyoFxrkjCUuJS9BjqkAcBJ3qW7cE8keRiO3lrMR7d%2BhtylTICpP9WGomKwAR2YBaxriZzlPKXtTPadYvgc4JiHvwvSkYqOxva%2F4vI9Me6DU%2BbPGIoRJNOjLk7FqMLlFNQ1FGHXWl2mDE0vpttpYDdvruGOJYHFHWfpFOJM7133YtkHd5y8%2F2J4Mwxjb7Wrzvb%2BTv1QRxYdJeRKQ%2FMdaL7lMpUVwg3f9q9EfrLg%2FjFDOKoK&X-Amz-Signature=33a4686df9df22ba865ea4ed8beb47f6fab48c1688679518805d860d3d015b1c&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/91181646-b1e0-4433-9711-6259a96a9247/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TIOMCLUU%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T221411Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEE0aCXVzLXdlc3QtMiJIMEYCIQCYzQgliwBt6yWYkQu1YTXKzYoolR4WNCo3g4%2BR2n%2FxMQIhAOIlypgU%2F0C4pGr2TaOjtOpCJFg2lXONHoQoQizJmGYQKv8DCGYQABoMNjM3NDIzMTgzODA1Igz%2BmChoZ%2F%2F5uBkhov8q3APsmlKCDTOXfGmc3mtZHCEFJdLI5dd9cWtgeqhJFLHngKRknjv58V%2FkldNEM31erZfRFjVw%2Bit6GFIf1vtNMQqt%2FderqyF2sDKEIzX7nHTSeTvR%2FdI2ACmOkBoGy8l6ZzAL6FG9AOXShdt8w%2F2wn0oHAOcMgjrwgs0S%2BYC6JVNFzsrk45XETRpMmmgDSO5hrX%2BiB%2BC%2B2vS1oPOJ8vas3eomTf9vJelcub88ob1mQlIHyzzwIxaAgIOhcCxbMMRWI4CJ8dD58IKy0xKNGz11dGFTgPHtADoVuyE0MPJ7P%2F1SWlJyrH%2FGxtq09UwlTl1i0zHKPxnVqu85enY%2F3RtGIvxEHCE922NfNVHt2Ul%2FX3MhbfgFQPNvMU09XWuzF%2BG20PRULfEp8%2FuCv%2FoQlkmGTypQwxnQ30dByn03Jcq3zlb2cwrVhW%2FHpaMWedM72X8ibuezMhS%2FEhx8SPvkTkJUf%2BTFWPq8HmSq7dSMeVvLuOnLZ%2FhpjQl17yUqw0qPpQ2XymKoPekls7KyyvO%2FCMVnZdx4VW4sY9qb5PEzWwqu0%2BTcjFVSemZlrdAvagOD7mPTZzw%2BPPpeI9vC%2FTunwH71BPD5wpP86E%2B4VD9n1N51uY4ejXukPalawBeyoFxrkjCUuJS9BjqkAcBJ3qW7cE8keRiO3lrMR7d%2BhtylTICpP9WGomKwAR2YBaxriZzlPKXtTPadYvgc4JiHvwvSkYqOxva%2F4vI9Me6DU%2BbPGIoRJNOjLk7FqMLlFNQ1FGHXWl2mDE0vpttpYDdvruGOJYHFHWfpFOJM7133YtkHd5y8%2F2J4Mwxjb7Wrzvb%2BTv1QRxYdJeRKQ%2FMdaL7lMpUVwg3f9q9EfrLg%2FjFDOKoK&X-Amz-Signature=7984417e541f7e801b89d47b98539aeb2b1a9c1edf15e3c91111e7f4069bfb24&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/09aba1c0-0d55-41dd-852a-a04c5b8a3fac/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662JWTARUW%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T221412Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEE0aCXVzLXdlc3QtMiJHMEUCICahw9bg4DDKIO8yXYm8QiBVyRIw4QdC4qfBoQ9JK5jaAiEAytSCij2OwyKcHoOgPchjPFJbNF%2FvQmXHkgQxpWCDT7Eq%2FwMIZRAAGgw2Mzc0MjMxODM4MDUiDMqTdSAccBbo1t%2F%2B8ircA%2BYc5RtJvNRWJj7aCkQcdUUkNFHHDxnOM5nhDD%2BrMyWTKfuMrPwfgLzK94fokSyX5STENCVqJbERxD%2BwLSvDSirFIUz5F4r2UjW%2FvLI3l9j9zLKIyIJUg%2FTiE9PEv05JbCOCytM7mtInFW%2FMKwPDItaghNqqrEdjkWtY6shGla7iVeff0sRg%2BazLCsLit4X2D6CVFxUfAFz%2BshO50OZg%2Bdqk3B55UYVptI8lDUP%2Fl2oDaOUpOTcVYSUcTjurxi7B1B6wGpZcTD5pm1QcmF0StgaLmPkNkZ54ckR9hm4zWU8cXevbS3tplMVS3z23%2B4ltoUCEw7pzZGbnYEVq57G%2BimQaWjbzBjf%2FFfTw8Mi9fBQfh47EEhLxIiS0G%2FIJL3nnVG%2FKPhPbmFCbvvcu%2Fc5TFY6189laWSQHPJThem9yOj49JlS08T3wSa7RCo1hgGXEIvxaZRTahT5pu5drcAxMqvL7nzdm3BNAWLz%2Bj26YM3m1BnxVgOhVeZTU6ot7PKpvGeJGhOW9BqMTxt7LwagDR7Z%2FfZcG4%2BbARkwMV2unu8vCh%2Bs%2BsEThc8QzQERY9Z54H9Nd91T16mLzZjX2CjvnxMPV4OUyYfXopD802xykYl0x1U1A4O5JXmT7Hm%2FRMO23lL0GOqUBEpd5P%2BkdB%2F%2Bu4R12xlz8UzKX8JLqIF%2BB7ZbMQF4tgviWshi45A9lNSESdkBt4r41iVvDHEu7%2FsvEwLjfNPdcn8xAKC9QEKfTXKO7A7xqGzbRhYBdz03c%2FJrP5tsyIQkhwpoim%2FhDx4lPAVf4FrszMdoFFabe9W8%2BHMYfsKND%2F5wyn7bQL0xckYTm%2FVyMW0bgU89xNfRLX1t4UkeKtVAXK096FO%2BO&X-Amz-Signature=663b7ab86b8212ccf3e558e4201957886c7e57c0240c3415adebe043d25a8eed&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 2. Scatter Plot
Scatter plots present the relationship between two variables in a dataset. It represents data points on a two-dimensional plane. The independent variable or attribute is plotted on the X-axis, while the dependent variable is plotted on the Y-axis.
**Syntax:**
```python
plt.scatter(x, y)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23708af9-659f-4f23-b626-1a4292d7842c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662JWTARUW%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T221412Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEE0aCXVzLXdlc3QtMiJHMEUCICahw9bg4DDKIO8yXYm8QiBVyRIw4QdC4qfBoQ9JK5jaAiEAytSCij2OwyKcHoOgPchjPFJbNF%2FvQmXHkgQxpWCDT7Eq%2FwMIZRAAGgw2Mzc0MjMxODM4MDUiDMqTdSAccBbo1t%2F%2B8ircA%2BYc5RtJvNRWJj7aCkQcdUUkNFHHDxnOM5nhDD%2BrMyWTKfuMrPwfgLzK94fokSyX5STENCVqJbERxD%2BwLSvDSirFIUz5F4r2UjW%2FvLI3l9j9zLKIyIJUg%2FTiE9PEv05JbCOCytM7mtInFW%2FMKwPDItaghNqqrEdjkWtY6shGla7iVeff0sRg%2BazLCsLit4X2D6CVFxUfAFz%2BshO50OZg%2Bdqk3B55UYVptI8lDUP%2Fl2oDaOUpOTcVYSUcTjurxi7B1B6wGpZcTD5pm1QcmF0StgaLmPkNkZ54ckR9hm4zWU8cXevbS3tplMVS3z23%2B4ltoUCEw7pzZGbnYEVq57G%2BimQaWjbzBjf%2FFfTw8Mi9fBQfh47EEhLxIiS0G%2FIJL3nnVG%2FKPhPbmFCbvvcu%2Fc5TFY6189laWSQHPJThem9yOj49JlS08T3wSa7RCo1hgGXEIvxaZRTahT5pu5drcAxMqvL7nzdm3BNAWLz%2Bj26YM3m1BnxVgOhVeZTU6ot7PKpvGeJGhOW9BqMTxt7LwagDR7Z%2FfZcG4%2BbARkwMV2unu8vCh%2Bs%2BsEThc8QzQERY9Z54H9Nd91T16mLzZjX2CjvnxMPV4OUyYfXopD802xykYl0x1U1A4O5JXmT7Hm%2FRMO23lL0GOqUBEpd5P%2BkdB%2F%2Bu4R12xlz8UzKX8JLqIF%2BB7ZbMQF4tgviWshi45A9lNSESdkBt4r41iVvDHEu7%2FsvEwLjfNPdcn8xAKC9QEKfTXKO7A7xqGzbRhYBdz03c%2FJrP5tsyIQkhwpoim%2FhDx4lPAVf4FrszMdoFFabe9W8%2BHMYfsKND%2F5wyn7bQL0xckYTm%2FVyMW0bgU89xNfRLX1t4UkeKtVAXK096FO%2BO&X-Amz-Signature=b020881c8dc4732eed9e3512a2fdc456c848b991d28b216a9d68a20830c954c7&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 3. Histogram
A histogram is an important visual representation of data in categorical form. To view the data in a "Binned" form, use the histogram plot with a number of bins required or with the data points that mark the bin edges. The x-axis represents the data bins, and the y-axis represents the number of elements in each bin.
**Syntax:**
```python
plt.hist(x, bins)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/24e4424a-df87-40a1-b63b-195cbdc2e0ab/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662JWTARUW%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T221412Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEE0aCXVzLXdlc3QtMiJHMEUCICahw9bg4DDKIO8yXYm8QiBVyRIw4QdC4qfBoQ9JK5jaAiEAytSCij2OwyKcHoOgPchjPFJbNF%2FvQmXHkgQxpWCDT7Eq%2FwMIZRAAGgw2Mzc0MjMxODM4MDUiDMqTdSAccBbo1t%2F%2B8ircA%2BYc5RtJvNRWJj7aCkQcdUUkNFHHDxnOM5nhDD%2BrMyWTKfuMrPwfgLzK94fokSyX5STENCVqJbERxD%2BwLSvDSirFIUz5F4r2UjW%2FvLI3l9j9zLKIyIJUg%2FTiE9PEv05JbCOCytM7mtInFW%2FMKwPDItaghNqqrEdjkWtY6shGla7iVeff0sRg%2BazLCsLit4X2D6CVFxUfAFz%2BshO50OZg%2Bdqk3B55UYVptI8lDUP%2Fl2oDaOUpOTcVYSUcTjurxi7B1B6wGpZcTD5pm1QcmF0StgaLmPkNkZ54ckR9hm4zWU8cXevbS3tplMVS3z23%2B4ltoUCEw7pzZGbnYEVq57G%2BimQaWjbzBjf%2FFfTw8Mi9fBQfh47EEhLxIiS0G%2FIJL3nnVG%2FKPhPbmFCbvvcu%2Fc5TFY6189laWSQHPJThem9yOj49JlS08T3wSa7RCo1hgGXEIvxaZRTahT5pu5drcAxMqvL7nzdm3BNAWLz%2Bj26YM3m1BnxVgOhVeZTU6ot7PKpvGeJGhOW9BqMTxt7LwagDR7Z%2FfZcG4%2BbARkwMV2unu8vCh%2Bs%2BsEThc8QzQERY9Z54H9Nd91T16mLzZjX2CjvnxMPV4OUyYfXopD802xykYl0x1U1A4O5JXmT7Hm%2FRMO23lL0GOqUBEpd5P%2BkdB%2F%2Bu4R12xlz8UzKX8JLqIF%2BB7ZbMQF4tgviWshi45A9lNSESdkBt4r41iVvDHEu7%2FsvEwLjfNPdcn8xAKC9QEKfTXKO7A7xqGzbRhYBdz03c%2FJrP5tsyIQkhwpoim%2FhDx4lPAVf4FrszMdoFFabe9W8%2BHMYfsKND%2F5wyn7bQL0xckYTm%2FVyMW0bgU89xNfRLX1t4UkeKtVAXK096FO%2BO&X-Amz-Signature=c968d1ca0c70e597f4bd3d6059e3a0e39c7f65137115d8b784c85e3b95d73fd0&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ab5a6dfe-51f5-43ee-bcb3-33dae4a1c7ad/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662JWTARUW%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T221412Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEE0aCXVzLXdlc3QtMiJHMEUCICahw9bg4DDKIO8yXYm8QiBVyRIw4QdC4qfBoQ9JK5jaAiEAytSCij2OwyKcHoOgPchjPFJbNF%2FvQmXHkgQxpWCDT7Eq%2FwMIZRAAGgw2Mzc0MjMxODM4MDUiDMqTdSAccBbo1t%2F%2B8ircA%2BYc5RtJvNRWJj7aCkQcdUUkNFHHDxnOM5nhDD%2BrMyWTKfuMrPwfgLzK94fokSyX5STENCVqJbERxD%2BwLSvDSirFIUz5F4r2UjW%2FvLI3l9j9zLKIyIJUg%2FTiE9PEv05JbCOCytM7mtInFW%2FMKwPDItaghNqqrEdjkWtY6shGla7iVeff0sRg%2BazLCsLit4X2D6CVFxUfAFz%2BshO50OZg%2Bdqk3B55UYVptI8lDUP%2Fl2oDaOUpOTcVYSUcTjurxi7B1B6wGpZcTD5pm1QcmF0StgaLmPkNkZ54ckR9hm4zWU8cXevbS3tplMVS3z23%2B4ltoUCEw7pzZGbnYEVq57G%2BimQaWjbzBjf%2FFfTw8Mi9fBQfh47EEhLxIiS0G%2FIJL3nnVG%2FKPhPbmFCbvvcu%2Fc5TFY6189laWSQHPJThem9yOj49JlS08T3wSa7RCo1hgGXEIvxaZRTahT5pu5drcAxMqvL7nzdm3BNAWLz%2Bj26YM3m1BnxVgOhVeZTU6ot7PKpvGeJGhOW9BqMTxt7LwagDR7Z%2FfZcG4%2BbARkwMV2unu8vCh%2Bs%2BsEThc8QzQERY9Z54H9Nd91T16mLzZjX2CjvnxMPV4OUyYfXopD802xykYl0x1U1A4O5JXmT7Hm%2FRMO23lL0GOqUBEpd5P%2BkdB%2F%2Bu4R12xlz8UzKX8JLqIF%2BB7ZbMQF4tgviWshi45A9lNSESdkBt4r41iVvDHEu7%2FsvEwLjfNPdcn8xAKC9QEKfTXKO7A7xqGzbRhYBdz03c%2FJrP5tsyIQkhwpoim%2FhDx4lPAVf4FrszMdoFFabe9W8%2BHMYfsKND%2F5wyn7bQL0xckYTm%2FVyMW0bgU89xNfRLX1t4UkeKtVAXK096FO%2BO&X-Amz-Signature=155ead3950521d0a8740bc7b1b89c8eb4b4d174e8f49b5d1156a2affb34f9cdb&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8f1b1d60-cf1b-42b3-9faa-f634c89c3f84/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662JWTARUW%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T221412Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEE0aCXVzLXdlc3QtMiJHMEUCICahw9bg4DDKIO8yXYm8QiBVyRIw4QdC4qfBoQ9JK5jaAiEAytSCij2OwyKcHoOgPchjPFJbNF%2FvQmXHkgQxpWCDT7Eq%2FwMIZRAAGgw2Mzc0MjMxODM4MDUiDMqTdSAccBbo1t%2F%2B8ircA%2BYc5RtJvNRWJj7aCkQcdUUkNFHHDxnOM5nhDD%2BrMyWTKfuMrPwfgLzK94fokSyX5STENCVqJbERxD%2BwLSvDSirFIUz5F4r2UjW%2FvLI3l9j9zLKIyIJUg%2FTiE9PEv05JbCOCytM7mtInFW%2FMKwPDItaghNqqrEdjkWtY6shGla7iVeff0sRg%2BazLCsLit4X2D6CVFxUfAFz%2BshO50OZg%2Bdqk3B55UYVptI8lDUP%2Fl2oDaOUpOTcVYSUcTjurxi7B1B6wGpZcTD5pm1QcmF0StgaLmPkNkZ54ckR9hm4zWU8cXevbS3tplMVS3z23%2B4ltoUCEw7pzZGbnYEVq57G%2BimQaWjbzBjf%2FFfTw8Mi9fBQfh47EEhLxIiS0G%2FIJL3nnVG%2FKPhPbmFCbvvcu%2Fc5TFY6189laWSQHPJThem9yOj49JlS08T3wSa7RCo1hgGXEIvxaZRTahT5pu5drcAxMqvL7nzdm3BNAWLz%2Bj26YM3m1BnxVgOhVeZTU6ot7PKpvGeJGhOW9BqMTxt7LwagDR7Z%2FfZcG4%2BbARkwMV2unu8vCh%2Bs%2BsEThc8QzQERY9Z54H9Nd91T16mLzZjX2CjvnxMPV4OUyYfXopD802xykYl0x1U1A4O5JXmT7Hm%2FRMO23lL0GOqUBEpd5P%2BkdB%2F%2Bu4R12xlz8UzKX8JLqIF%2BB7ZbMQF4tgviWshi45A9lNSESdkBt4r41iVvDHEu7%2FsvEwLjfNPdcn8xAKC9QEKfTXKO7A7xqGzbRhYBdz03c%2FJrP5tsyIQkhwpoim%2FhDx4lPAVf4FrszMdoFFabe9W8%2BHMYfsKND%2F5wyn7bQL0xckYTm%2FVyMW0bgU89xNfRLX1t4UkeKtVAXK096FO%2BO&X-Amz-Signature=334e26e4018289ebaa2a1b1754ef32a4f3b2fc1893e198f50ead56f0a78f8c84&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/13ad0497-05fe-4eaa-984e-707b33e14761/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662JWTARUW%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T221412Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEE0aCXVzLXdlc3QtMiJHMEUCICahw9bg4DDKIO8yXYm8QiBVyRIw4QdC4qfBoQ9JK5jaAiEAytSCij2OwyKcHoOgPchjPFJbNF%2FvQmXHkgQxpWCDT7Eq%2FwMIZRAAGgw2Mzc0MjMxODM4MDUiDMqTdSAccBbo1t%2F%2B8ircA%2BYc5RtJvNRWJj7aCkQcdUUkNFHHDxnOM5nhDD%2BrMyWTKfuMrPwfgLzK94fokSyX5STENCVqJbERxD%2BwLSvDSirFIUz5F4r2UjW%2FvLI3l9j9zLKIyIJUg%2FTiE9PEv05JbCOCytM7mtInFW%2FMKwPDItaghNqqrEdjkWtY6shGla7iVeff0sRg%2BazLCsLit4X2D6CVFxUfAFz%2BshO50OZg%2Bdqk3B55UYVptI8lDUP%2Fl2oDaOUpOTcVYSUcTjurxi7B1B6wGpZcTD5pm1QcmF0StgaLmPkNkZ54ckR9hm4zWU8cXevbS3tplMVS3z23%2B4ltoUCEw7pzZGbnYEVq57G%2BimQaWjbzBjf%2FFfTw8Mi9fBQfh47EEhLxIiS0G%2FIJL3nnVG%2FKPhPbmFCbvvcu%2Fc5TFY6189laWSQHPJThem9yOj49JlS08T3wSa7RCo1hgGXEIvxaZRTahT5pu5drcAxMqvL7nzdm3BNAWLz%2Bj26YM3m1BnxVgOhVeZTU6ot7PKpvGeJGhOW9BqMTxt7LwagDR7Z%2FfZcG4%2BbARkwMV2unu8vCh%2Bs%2BsEThc8QzQERY9Z54H9Nd91T16mLzZjX2CjvnxMPV4OUyYfXopD802xykYl0x1U1A4O5JXmT7Hm%2FRMO23lL0GOqUBEpd5P%2BkdB%2F%2Bu4R12xlz8UzKX8JLqIF%2BB7ZbMQF4tgviWshi45A9lNSESdkBt4r41iVvDHEu7%2FsvEwLjfNPdcn8xAKC9QEKfTXKO7A7xqGzbRhYBdz03c%2FJrP5tsyIQkhwpoim%2FhDx4lPAVf4FrszMdoFFabe9W8%2BHMYfsKND%2F5wyn7bQL0xckYTm%2FVyMW0bgU89xNfRLX1t4UkeKtVAXK096FO%2BO&X-Amz-Signature=aa0c81718a340789955dcd527a50e5340d2b586dfb26004173a6fa82aa3e444d&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 2. Box and Whisker Plot
A box plot shows the distribution of quantitative data in a way that facilitates comparisons between variables or across levels of a categorical variable. The box shows the quartiles of the dataset while the whiskers extend to show the rest of the distribution, except for points that are determined to be "outliers".
**Syntax:**
```python
sns.boxplot(x='header_1', y='header_2', data=df)
```
**Example Output:**


![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d207ae92-0a7c-4e2f-aa65-0ee5a2c33bf7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665KB3ENBA%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T221414Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEE0aCXVzLXdlc3QtMiJHMEUCIBM0AyjRtHbhIdNyuGrYoWuq8qCFvpcVRfwLIZaCYsQ1AiEAoXWcT%2FHMtZ8zbLFBT2efTyAna2eqznmMQigba0nnRwYq%2FwMIZhAAGgw2Mzc0MjMxODM4MDUiDLY%2FfHikwnZusL7WfSrcA0z4XG62JMQAKxEjEeUNCNXy7DL1fR9%2Be5%2BaqFwur27QnQ4DtltdtTrDOjZIvJstVDCZpD8RRT29HTbbROzWbs9RyLGmTd4ONVpXHIx8VcsX0kYGhHSsCcFK89WQ3im7J8vkZDYzkwsUMRijuRs2ONngzfqKag%2B%2BwpWr%2BHAFFYA8TKm%2FIuSn71gSQ8n50uDeSOAvBvLooIqeQgE6VajWF4FclV083xVzRB2qPKmRqpLJumLD4PROfTP%2By1g2HUY31pl9cpymiLgDkF3IekFhyKZbNJqTPcYoqNubko04SCDWaoNLwh%2B%2BctXCMNHiQxQ9YUa8lhloUMb5AkYQtE8J1CcDJrFUbAH%2B%2F9xLJUFpfVlNIhC5QoCFg9eVZSf6eZHdvCZMKDNxfwzWSCS1KfrU9Y09qSDZVaGwLu%2F4WEWl9%2FnwNzFmtS2s4NLIk8gd97ubxlxpTTj4XnKfegYvZGBz1KQufq8WIdJRgKMhpCTmJp2vtl2sadKYVX2HLelLRK4x%2Fb6dq6%2F09QOavuMB9esHm40pMi36PlmqnB3eRTyxM9g3brwI%2FGHYigI2GJqEUi79Iv%2BrneDaLYqkIDqKiAKUJuEHPVC3Qb7%2Bd39978DdDhiANcSEs1cDhVs2ZDEGMKG4lL0GOqUBBrkSuxBCqd5r0gfqVJP8L0AUMH6nWEv4a%2FCX9YYba%2Bw3EBhRIQCiwErn29fcrn7YV9W9PQQbdlKO%2BM5cEiuUdG%2Fw%2FjORcdvfiYRBzONOh1XbcCkPP9Eq8dPUaOg80Nw4TfA2VMNzwSw7fXHogj2YXgSIKRP%2Fjdxw0oOGYNF9mEV4WVIMSdsmz1j6%2FPA2ODWofS0hUfnc2%2BFnwJ2Oo1R3frH6QXLm&X-Amz-Signature=89c48ce578d3f43ba974ff67bafc68555ce8d1026431c69478e356114d748dc4&X-Amz-SignedHeaders=host&x-id=GetObject)

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0e516edc-7551-4792-ab18-0494db3c4c0c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466U3OJSLWZ%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T221414Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEE0aCXVzLXdlc3QtMiJIMEYCIQCshMiMIbhs4sq%2B6T0YJ4l99qbOjlyU%2FVx2PZzDJjj9JQIhAKqsHT2twiGLvb7NCvxvdM8k9U%2F%2FXaF8%2FbFmga69alzAKv8DCGYQABoMNjM3NDIzMTgzODA1IgyY0yBOB9vi94XYyucq3AN1Q86CLe%2B4AvlZAlYoWjVyq4TdJjvyORXZXVmpEJ8vlEAV%2B9xjGZEu0H3Qtaqio2c%2BMUfoZfGt78KB0rGRqMaKkJikco%2Fyqmd9wBbdt5rqN9q%2FSKtjqIRhykE6VdAybqYrNBdsHX1A6%2FMN6ijFCQhCrpOhhOLwSwX9YQL10BusMPWFIQ5UHfnLHxVJIlk1FKhB%2FPpkovhG6SJrcUihK8Q9Lvf8oT22KT1Ab39%2B%2F7is44tEKOmeUE%2BYNGY5UXRpMdNjYoCNs7qlxzIIyt4zu8ivXZceEpavl0ESlo5mFcn8Gv2mIH5kUkpfYcU1PJ1t%2FrJvbGkVJela7Z09G4EOi9MCvONdJCN3fi%2FLTWQZXrbXzf79EwKjisOiK09S5U%2FFHiZgEGxqUveqyvaF9kpfK4tiB9WB10IEV68c%2Bxodpt2v2lEpCKF6NtlfasIU%2FXnpO2njxCo84BkdgoDvTyrOjgRZp3Nte9FDnArKmnozybWNSvAI0KbqbxHhyeilpWc4swJbhU%2FAniGxQx5qT1BJSBPJBKy5fEY7W5yKFYVHJK5TLQBIfD92cUjGSNKSQMzGDTkar5qz5YBKyIljI6azC5WdJS5MOmnMT7rDZYmW9brUukDj1v7X2StAosjFFTC1uJS9BjqkAYO0wbcGH0zZBVi2OlQBmbWNYo6KKNPAOdU2p93SClphNUu45quYXHLOoR0KR%2BrysjK59b%2BAnDLz7zTrvWWcMDyxBw%2BxrM%2Bz9HIvQzA3SvAk%2B2pse23jh9QZYGuV5WayE%2BZdhXSmyAVFcKZ7ZdzcX9hiqXEpScEtdA6Kzty%2B6VKzcNMJ%2BSpU5EuPK%2FMScvQQ3Lb9qqODc1LZeftrHpSijSfu%2BabP&X-Amz-Signature=00180075da5b6b9ffe58c5d202068913c78d1a5b88576a920e54fde1944a17ad&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23a79b9d-2356-49a9-8fd9-65c6b0ab2cc5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662JWTARUW%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T221412Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEE0aCXVzLXdlc3QtMiJHMEUCICahw9bg4DDKIO8yXYm8QiBVyRIw4QdC4qfBoQ9JK5jaAiEAytSCij2OwyKcHoOgPchjPFJbNF%2FvQmXHkgQxpWCDT7Eq%2FwMIZRAAGgw2Mzc0MjMxODM4MDUiDMqTdSAccBbo1t%2F%2B8ircA%2BYc5RtJvNRWJj7aCkQcdUUkNFHHDxnOM5nhDD%2BrMyWTKfuMrPwfgLzK94fokSyX5STENCVqJbERxD%2BwLSvDSirFIUz5F4r2UjW%2FvLI3l9j9zLKIyIJUg%2FTiE9PEv05JbCOCytM7mtInFW%2FMKwPDItaghNqqrEdjkWtY6shGla7iVeff0sRg%2BazLCsLit4X2D6CVFxUfAFz%2BshO50OZg%2Bdqk3B55UYVptI8lDUP%2Fl2oDaOUpOTcVYSUcTjurxi7B1B6wGpZcTD5pm1QcmF0StgaLmPkNkZ54ckR9hm4zWU8cXevbS3tplMVS3z23%2B4ltoUCEw7pzZGbnYEVq57G%2BimQaWjbzBjf%2FFfTw8Mi9fBQfh47EEhLxIiS0G%2FIJL3nnVG%2FKPhPbmFCbvvcu%2Fc5TFY6189laWSQHPJThem9yOj49JlS08T3wSa7RCo1hgGXEIvxaZRTahT5pu5drcAxMqvL7nzdm3BNAWLz%2Bj26YM3m1BnxVgOhVeZTU6ot7PKpvGeJGhOW9BqMTxt7LwagDR7Z%2FfZcG4%2BbARkwMV2unu8vCh%2Bs%2BsEThc8QzQERY9Z54H9Nd91T16mLzZjX2CjvnxMPV4OUyYfXopD802xykYl0x1U1A4O5JXmT7Hm%2FRMO23lL0GOqUBEpd5P%2BkdB%2F%2Bu4R12xlz8UzKX8JLqIF%2BB7ZbMQF4tgviWshi45A9lNSESdkBt4r41iVvDHEu7%2FsvEwLjfNPdcn8xAKC9QEKfTXKO7A7xqGzbRhYBdz03c%2FJrP5tsyIQkhwpoim%2FhDx4lPAVf4FrszMdoFFabe9W8%2BHMYfsKND%2F5wyn7bQL0xckYTm%2FVyMW0bgU89xNfRLX1t4UkeKtVAXK096FO%2BO&X-Amz-Signature=2966fd221331a14c51e8a4cbcedb5e054dc192b2241689c9064ebe3c5e325a8b&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 4. KDE Plot
A Kernel Density Estimate (KDE) plot is a graph that creates a probability distribution curve for the data based upon its likelihood of occurrence on a specific value. This is created for a single vector of information.
**Syntax:**
```python
sns.kdeplot(X) || sns.kdeplot(df['age'])
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0d571213-2a2f-4921-a50b-880847aa05ee/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662JWTARUW%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T221412Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEE0aCXVzLXdlc3QtMiJHMEUCICahw9bg4DDKIO8yXYm8QiBVyRIw4QdC4qfBoQ9JK5jaAiEAytSCij2OwyKcHoOgPchjPFJbNF%2FvQmXHkgQxpWCDT7Eq%2FwMIZRAAGgw2Mzc0MjMxODM4MDUiDMqTdSAccBbo1t%2F%2B8ircA%2BYc5RtJvNRWJj7aCkQcdUUkNFHHDxnOM5nhDD%2BrMyWTKfuMrPwfgLzK94fokSyX5STENCVqJbERxD%2BwLSvDSirFIUz5F4r2UjW%2FvLI3l9j9zLKIyIJUg%2FTiE9PEv05JbCOCytM7mtInFW%2FMKwPDItaghNqqrEdjkWtY6shGla7iVeff0sRg%2BazLCsLit4X2D6CVFxUfAFz%2BshO50OZg%2Bdqk3B55UYVptI8lDUP%2Fl2oDaOUpOTcVYSUcTjurxi7B1B6wGpZcTD5pm1QcmF0StgaLmPkNkZ54ckR9hm4zWU8cXevbS3tplMVS3z23%2B4ltoUCEw7pzZGbnYEVq57G%2BimQaWjbzBjf%2FFfTw8Mi9fBQfh47EEhLxIiS0G%2FIJL3nnVG%2FKPhPbmFCbvvcu%2Fc5TFY6189laWSQHPJThem9yOj49JlS08T3wSa7RCo1hgGXEIvxaZRTahT5pu5drcAxMqvL7nzdm3BNAWLz%2Bj26YM3m1BnxVgOhVeZTU6ot7PKpvGeJGhOW9BqMTxt7LwagDR7Z%2FfZcG4%2BbARkwMV2unu8vCh%2Bs%2BsEThc8QzQERY9Z54H9Nd91T16mLzZjX2CjvnxMPV4OUyYfXopD802xykYl0x1U1A4O5JXmT7Hm%2FRMO23lL0GOqUBEpd5P%2BkdB%2F%2Bu4R12xlz8UzKX8JLqIF%2BB7ZbMQF4tgviWshi45A9lNSESdkBt4r41iVvDHEu7%2FsvEwLjfNPdcn8xAKC9QEKfTXKO7A7xqGzbRhYBdz03c%2FJrP5tsyIQkhwpoim%2FhDx4lPAVf4FrszMdoFFabe9W8%2BHMYfsKND%2F5wyn7bQL0xckYTm%2FVyMW0bgU89xNfRLX1t4UkeKtVAXK096FO%2BO&X-Amz-Signature=be707adfde008dd4da55b3a852a829a71f68695bf6a151848d41fb26e00f43d8&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/53752550-ef82-4ca9-a01a-09921f0282d0/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662JWTARUW%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T221412Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEE0aCXVzLXdlc3QtMiJHMEUCICahw9bg4DDKIO8yXYm8QiBVyRIw4QdC4qfBoQ9JK5jaAiEAytSCij2OwyKcHoOgPchjPFJbNF%2FvQmXHkgQxpWCDT7Eq%2FwMIZRAAGgw2Mzc0MjMxODM4MDUiDMqTdSAccBbo1t%2F%2B8ircA%2BYc5RtJvNRWJj7aCkQcdUUkNFHHDxnOM5nhDD%2BrMyWTKfuMrPwfgLzK94fokSyX5STENCVqJbERxD%2BwLSvDSirFIUz5F4r2UjW%2FvLI3l9j9zLKIyIJUg%2FTiE9PEv05JbCOCytM7mtInFW%2FMKwPDItaghNqqrEdjkWtY6shGla7iVeff0sRg%2BazLCsLit4X2D6CVFxUfAFz%2BshO50OZg%2Bdqk3B55UYVptI8lDUP%2Fl2oDaOUpOTcVYSUcTjurxi7B1B6wGpZcTD5pm1QcmF0StgaLmPkNkZ54ckR9hm4zWU8cXevbS3tplMVS3z23%2B4ltoUCEw7pzZGbnYEVq57G%2BimQaWjbzBjf%2FFfTw8Mi9fBQfh47EEhLxIiS0G%2FIJL3nnVG%2FKPhPbmFCbvvcu%2Fc5TFY6189laWSQHPJThem9yOj49JlS08T3wSa7RCo1hgGXEIvxaZRTahT5pu5drcAxMqvL7nzdm3BNAWLz%2Bj26YM3m1BnxVgOhVeZTU6ot7PKpvGeJGhOW9BqMTxt7LwagDR7Z%2FfZcG4%2BbARkwMV2unu8vCh%2Bs%2BsEThc8QzQERY9Z54H9Nd91T16mLzZjX2CjvnxMPV4OUyYfXopD802xykYl0x1U1A4O5JXmT7Hm%2FRMO23lL0GOqUBEpd5P%2BkdB%2F%2Bu4R12xlz8UzKX8JLqIF%2BB7ZbMQF4tgviWshi45A9lNSESdkBt4r41iVvDHEu7%2FsvEwLjfNPdcn8xAKC9QEKfTXKO7A7xqGzbRhYBdz03c%2FJrP5tsyIQkhwpoim%2FhDx4lPAVf4FrszMdoFFabe9W8%2BHMYfsKND%2F5wyn7bQL0xckYTm%2FVyMW0bgU89xNfRLX1t4UkeKtVAXK096FO%2BO&X-Amz-Signature=64a294406e0125e3b7bfaabf2f6c2f60af2fcafa9c4d4c9eae87feed5e482238&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
## 4. Correlation Between Variables
Correlation is a statistical measure of the extent to which different variables are interdependent. It indicates how changes in one variable are associated with changes in another variable over time.
### Positive Correlation
Positive correlation indicates that as one variable increases, the other variable also tends to increase.
**Example: Engine Size and Price**
- **Positive Correlation:** Engine size increases, price also increases.
- **Visualization:** Scatter plot with a steep positive slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c7ea9b0-3ef3-4357-a9c3-554fc71b6b15/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RKSDJESV%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T221413Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEE0aCXVzLXdlc3QtMiJHMEUCIQCm190bPRuqAKBXrjex9q71AuCnQpiU6YecuCBdaxIziQIgDKvm%2BF8rx4iJWxMA67KXCF2cGs5tuMMibEMOkg47Kikq%2FwMIZhAAGgw2Mzc0MjMxODM4MDUiDGHCajKfsYdTXpd%2FzSrcA4bWsw1cttFxNzWz6ORVvn4%2BiXFgLKN06x6d2ybStpv3RPM%2Bvfog5eK5nyt1fv8mBfdhpbF4hrChId2P9636U%2BaPrF3YFwAMGteDeE4o6THSVjC%2BMTRf90E2mc4p4yttRihe7e4TYBTQRfkHtyH5dzChwzhme0Vvf0MerLg17hpDEzXjl2tEb%2BCeGdoePzovdfMPev8tXJmreUgsGRDC1LvC15ujgK8q%2B8SODiI8pDJccHuZJ7P8hbnf6FFJvSZVe9bO%2FbjgsJxbR%2Fvy1oc8cGqN%2FcvFh1pyI06n2lMB1fySex2v74asIw5gykThksRam1Upcx9D7i0sUT%2FKTz%2FKADT1iSta1JJMzz%2BdQJMu7n7N8Uz5fp6n1aavtzUBS45PWHWLpI1ewnEv7%2Fwb8TaKFeLxnI2iP1nhmMiDYpzyjmtbmRw9QYg8fSmbRiiPiuwuoGPJOQobhpmDr0keULYGnRo6jeHWxtKA7z6%2BZjdRC2Tp0GXKDVV%2F5bQWhuvPHzA7YBXdTJUuOH03OXzKVDFnAt5%2Fcr%2BGhMapdwn6lFLV5V6pGN6JD7LXPbX8nT1BMPU7pXgMw1C0LfkXAT235EvnKmutC547VuGNrb5lOwI%2FZibQsc8wzTC6y4sP9qswMI64lL0GOqUBTA4QjIOMUX4YVWQhmajXdjG59d73DQL89mDygBeyfDrtFCjSdPIHTVhofVw8YFtMFSu6M5E9Ice8YiiEvxK%2BLq0Uf%2BG6yu%2BkjL4%2FOMf8OIFvsT0rNOX93H%2F95Y%2BtRha1DnAfe2qpL23Q0vb4WXwodkPytWjQcEzRdQH1zPIsDvM9cjcEj5mdPa8B5lfKOZ9sn2R%2BCYQIPjSfFl2g3j66oDTO7qwI&X-Amz-Signature=3df821eca22707d77f55818aac19d951a3a32b50d99852ac9dc78bd9675493a6&X-Amz-SignedHeaders=host&x-id=GetObject)
**Explanation:** When engine size increases, there is a corresponding increase in the price of the vehicle. This positive correlation suggests that larger engines tend to be associated with higher prices in the market.
___
### Negative Correlation
Negative correlation indicates that as one variable increases, the other variable tends to decrease.
**Example: Highway Miles per Gallon and Price**
- **Negative Correlation:** As highway miles per gallon increases, price decreases.
- **Visualization:** Scatter plot with a steep negative slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/10f1f798-9cc4-4df2-a9c1-5a339f554a0b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RRK5WF3B%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T221413Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEE0aCXVzLXdlc3QtMiJGMEQCIE7Rm0myPQ9sCjktTcj9F4x1Lb99mGf7lOVpt%2FjxVnMcAiA3qj6qcrPES3v3WM94cGr3u2hLPrNEt8mtsXHpp04VCir%2FAwhmEAAaDDYzNzQyMzE4MzgwNSIM9%2FPGgk9lnWBQyO0SKtwD6So2D2UNdLQLDf34hrXR9xkbwhiPCiAhznUperBLaRc8bywas%2Fik%2BRfNU0voUcXeEEfPvfsRctbfBmvKPO%2B59hQjq%2FufxdEYcVC6ciJeRacL9f01%2F6xKpjxkAIexFXzqwMSQgwWMm4KsG1GysBcgVkBO%2BTomj2Uyqzl%2B7dH%2BuNX1j9thOzUVrxGdDl5hbZ9qgwS9QUlH7KFQ3q5GawjIc0NWDe9pYW%2F0ZCRDGdZgBaMc%2Fm4%2FpIIOxH6fSwGsOz7vgn1L3KfFTF8iAQz2%2FRz6HQse5A2roVm%2BtFuffhCynxNDA8D2FJ7YRosxIsLXRki%2BK8z1XAPJkfYthnj4X4Q86Fi79lxrJGoF5nK8426IPqTGinyUvzFPUToYML04kxJhhcUb%2FqoaAMHodDhUmOCSmQIyJ2qtBDvkuPJ4pdspmgupZrE4KvMpGd6i7yHMwU%2B3Dyp5oPgr5FMQvOWXolkF7ZO83nPyNPeLVIK6p3rqXTI%2FHoQHGgIqpS8Q00GKvXM0siOp4ja7aO%2F2YRl%2FDPrCJG%2FmYWBwnvlmbYUBjtAc5dvSQuYZv80EN%2FblH%2FOiH8J3LMDZe1DkmloJGcg%2FYr7B1C8lgxG49C7zO4UOcNi8st12AAXZmzJetgxiPSwwqriUvQY6pgGk%2FUDm%2BxhIZTOTaKrq3EkxDVw1%2F%2BKuxRq8YRGtI%2FwPbXqOdYG1doEjw3%2FLOreuif5JYUNNvASsz9t3C3Bdgr5hwSnSx5PreH1Fo5TUrM6JqCQIgZo0uugKEaXTUeBpeWh8DV8bzY4DHMC17U82Ctc3ckbiwxq%2FZGNu8ZZT1Z8gSmvzbHKnbtbQ%2FMJf%2FOwOmeJ0nXPW0Dj7DByRutIzwNm%2BBvaAPqcz&X-Amz-Signature=8f71ce85a9416b09d430b34e65edfc2f50d0e4c2debb291d140094777fdf6cd6&X-Amz-SignedHeaders=host&x-id=GetObject)
**Explanation:** When highway miles per gallon increases, the price of the vehicle tends to decrease. This negative correlation suggests that cars with higher fuel efficiency (more miles per gallon) are generally priced lower in the market.
___
### Weak Correlation
Weak correlation indicates a lack of strong relationship between the variables.
**Example: RPM and Price**
- **Weak Correlation:** Low and high RPM values show varied prices, indicating no strong predictive relationship.
- **Visualization:** Scatter plot with no clear trend or slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9f914514-8914-4bf4-ac84-d9e3077f6eb1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VGUEEZZT%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T221413Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEE0aCXVzLXdlc3QtMiJIMEYCIQCNPCJlnpbfeC34KdQ0R%2FKZqOmBsqx28j8lWb2h12Qe4gIhAKfrX1Ca%2B9SZQ3u3bNP6s6NOkk8yaLFxk%2Far1HAhYlBuKv8DCGYQABoMNjM3NDIzMTgzODA1IgyVcNQBKqYoIXEqB8kq3AM6JyEzVTvog%2FmSR38N49W6R022OmJaY%2B1dQRL9bmV%2FZ%2Bphlbn5jEepYrs88By7H2DmIFmeCaClmm2JeZ1C2gkLBNDrb5Pkt2VBQb2SZD9Aj2Q2x52FOROu3qIVwngamq49U226cspXemP%2B3MUzdruOv%2Fn964isY0es7rukpduRz9LsCu2RNFzuca7jjlS2UoMrDBcK%2FREJvkZDHDtk8Q8S0N%2BAJ24qZr2TgFNMVa1FGDh9c5kgoCRfmWtYwyZykdqMrweRpFRjgQhUxMRPzLz8lJRrRBqHg4NyuYpUMQPJArQZxzC2ge2GOhVdRdx1wrSGuwuXAp3NkNKbfEuTE3y324340KGk6UlOladXWr%2B9y0dEQy5VjP47c%2FlkgLycknuH8gwmljM8X2F4SbRG7e90Pg3J2Hq23Y5x1Qq4IXUucBolkbz%2FlTXRk9KXXjp0NQCCmCTe48X7vmMIOS0BudtV4JtGvS58NMf6Hyiw%2FVtHta6r%2BRMU1dOKTyll2Ph0qdiHLgDcBJKaTjTOrqVbqDdCxWhXDai0QHlReUSGSVAROH6WyFfi0Ur10QXvTsVGT%2BhDXudkSk3ZkQ6csUctkxUxtx2jy7Sjbv1vOeLSWiP%2Bv5cZkOcWuR9daAGllDCjuJS9BjqkAT5fw5JRWHAj4T%2BpES2HfEi8KNEVctVdLhicpTHHNhdxYMsdZUKTEwKkCHRpaEQ1THZjnaYB0mKn5Ri17MEVC8wRnz5SCG96CKRHoR9KnMTaKtZUBkiWQDlIZapw1SsBwlUoyvapWrSdamWU8chts0Vm0jisz2%2BMlbqUhFp3hlhcdcjS45ia9LiRO6RKk5bu%2FICzI8sum%2Bs15RFRhjjWQ%2FUoPUNQ&X-Amz-Signature=0b32328f19b478da898421adbb37267529888d8c4f0620c215e31f049950c7ac&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f18086e5-5b04-4fbf-8309-8944ab20d213/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665QVXZWAF%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T221413Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEE0aCXVzLXdlc3QtMiJHMEUCIQDTaZj7I5KAO2orW0bSXE7EuAZk3r55jnOaQp5MF6qYYgIgB16YoezDBq51JGZaDznpz8N2F1jmR7fWcLdoB%2FhuZWcq%2FwMIZhAAGgw2Mzc0MjMxODM4MDUiDJZXLl%2BjoIuaApNvuSrcA3C%2BRX51pCwg4SkYpUBwToaYu04Ly9dD5Q%2FYfsktUfM9YiDlIIg9DKIFtwu6UZTlVitpx5%2B2zwXdwMp1Q8d8Lexazn72UTwAfgtoawsybozD3%2B4hV1c3KC1C3g7Me2izTuNrukTYCI6K%2BqUdGoM0DqWCzG8WxABP9x%2ByWsNc9yaMPgc9%2BRUo9Eu%2Fxk%2F1CIUrc6bqWlvBg8oZQM3OhCj0RGQ8uJ37TNRLT78jcHM93kkGOhZmaI9MVgdCm%2FMfGifw0Gis7VqVsNHuqhfxVJkIXZjfw0Nss3Lqh0yhDay4DHaYXCGuKg37VUAsjpmdBcrsYzswUfip2ta49%2BJr0E1v3xxmQj9GoPmpXk7RMdN1aTfXjV0XfTZtVeNHd3sj62KFxgc%2FJrIS98W8WTzysy7KfvXVrUzykhTQXXOApp6pGJ6Fhhlj4h7sE0ZJGB6PIhWf7%2FvZwfU9BlhYwzjLdUG1uoDE6o5A5kDVMoZcRMyOet4WJZysbd9n1XSKccBoWF3LnWesgmRuFCQCmWU1q8Mhszlzy332TTsszt35jlOw6axi0Canb%2B9WapT2Diuk9cKMr2jOtqSAKAzyKMo4V6fOjVx2%2Bz6%2BNgWU8ls7enqljz1sH7vxeGoL6jG5HQ7MMMC4lL0GOqUBMKoHLEGBTO4o7kMr4PZws6abARX67UlohYPwOJ37fzek6oUB93XLiEI4SQUsd8yWWb3tTFLFQmFXMk7xLvCa1gTCsBMukQXe70DMa4C1AhlbBiKFHsj1C6sHS8okIUmLZd3WWwUThA7MLdE6J0TfYEPO51ftyyLGOALYEk%2Fi%2BfTuXythXX7WfFTbeYQz%2BDZtboz2VegJ3lcWDuiBkitjk7KkXw4e&X-Amz-Signature=13e8adc8113a0987bfa724c2571792b28479f5ab0275fb49b013223f5efb6273&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Correlation Plot
Heatmap visualizes correlations among variables. Color scheme indicates Pearson correlation coefficients. Dark red diagonal line shows perfect correlation (value of 1) between variables and themselves.
This heatmap offers overview of variable relationships and their link with price.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cd3b341e-cc1a-45f7-8aec-cdc00436d270/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665QVXZWAF%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T221413Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEE0aCXVzLXdlc3QtMiJHMEUCIQDTaZj7I5KAO2orW0bSXE7EuAZk3r55jnOaQp5MF6qYYgIgB16YoezDBq51JGZaDznpz8N2F1jmR7fWcLdoB%2FhuZWcq%2FwMIZhAAGgw2Mzc0MjMxODM4MDUiDJZXLl%2BjoIuaApNvuSrcA3C%2BRX51pCwg4SkYpUBwToaYu04Ly9dD5Q%2FYfsktUfM9YiDlIIg9DKIFtwu6UZTlVitpx5%2B2zwXdwMp1Q8d8Lexazn72UTwAfgtoawsybozD3%2B4hV1c3KC1C3g7Me2izTuNrukTYCI6K%2BqUdGoM0DqWCzG8WxABP9x%2ByWsNc9yaMPgc9%2BRUo9Eu%2Fxk%2F1CIUrc6bqWlvBg8oZQM3OhCj0RGQ8uJ37TNRLT78jcHM93kkGOhZmaI9MVgdCm%2FMfGifw0Gis7VqVsNHuqhfxVJkIXZjfw0Nss3Lqh0yhDay4DHaYXCGuKg37VUAsjpmdBcrsYzswUfip2ta49%2BJr0E1v3xxmQj9GoPmpXk7RMdN1aTfXjV0XfTZtVeNHd3sj62KFxgc%2FJrIS98W8WTzysy7KfvXVrUzykhTQXXOApp6pGJ6Fhhlj4h7sE0ZJGB6PIhWf7%2FvZwfU9BlhYwzjLdUG1uoDE6o5A5kDVMoZcRMyOet4WJZysbd9n1XSKccBoWF3LnWesgmRuFCQCmWU1q8Mhszlzy332TTsszt35jlOw6axi0Canb%2B9WapT2Diuk9cKMr2jOtqSAKAzyKMo4V6fOjVx2%2Bz6%2BNgWU8ls7enqljz1sH7vxeGoL6jG5HQ7MMMC4lL0GOqUBMKoHLEGBTO4o7kMr4PZws6abARX67UlohYPwOJ37fzek6oUB93XLiEI4SQUsd8yWWb3tTFLFQmFXMk7xLvCa1gTCsBMukQXe70DMa4C1AhlbBiKFHsj1C6sHS8okIUmLZd3WWwUThA7MLdE6J0TfYEPO51ftyyLGOALYEk%2Fi%2BfTuXythXX7WfFTbeYQz%2BDZtboz2VegJ3lcWDuiBkitjk7KkXw4e&X-Amz-Signature=e398fd9b2e16087dc24588fe757cb335ac9e0ef8baf52f419db4c4cfef5785cc&X-Amz-SignedHeaders=host&x-id=GetObject)

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
