

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7e6d594d-952e-44b6-97ea-31225882aea6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666GXTLJL7%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T181947Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCpB8ndjz9POymC92SlQ718F7Gc2f%2B5HuHHnmM3R1TKsAIhAN6XULiYYgIqkkLzbPenKNg9PY79eWXK7kQ0EjL%2BVzrHKogECKv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igy%2Fvb7iTGMob%2FQmXHgq3APf7ZMelNWwrD4pVMUmcRQji%2Be0FreBC%2F7U%2BJTSrd9v5uMuLlqgvfsvn0ay7FCUoNE1i6BFlK%2FzKkVQmNuPYekQiQ259B28oZ7L31Q9nDXJyVnxu3eNGKIlZMIVvb0NZEiz2U7B1r26Tl%2FEGgrlJyvzmn7OngBiYPY1bVT8pP4iBGYNxGh3yM8rPEabDhDKWOiwqJKUMk7YUacWKm7o4wQnUMvAk38P%2BMZW5MYVufYbnMbpu37eyYRxDqhsLlziEBn0ZhnZniXk8sDtwsC82rwmTTxEvcMEGDuNeAN0lopiGRJUWDMEUDCOBsPpOFV2TwvwkQD60IsQYcpO0znei2OHGmEOIJ8vmmoiTJ9dnvGsQ2WBveVEi3USNv4edakNPOgsLghO3jdSxldmntkwexbgsFM6Jk0dOKOUVQ312ieqxNFuXoboAW3WVbCBEdYoD2UrdTLfjUy5cyK29HvfJPe%2F657%2FbvAxwBwaHtUiV1ORSO47Fona%2FVrLmFnpzhToAo1HGej%2BKBYZo6RlvdOccQktYgGvG2BgKCriXZAj1FYV3g17R8MRY6fKIoYEwXwcDiDe5b1xNbaX%2BtiN73oLq9YFI8EhYp6Wd43pS2cpK%2BnxvOXRX1uBU7nfAnab%2FzCB8%2B68BjqkAdFUiyzUd6VBbwKQHYCn1iREU6YElGRGqkNiAXQdYbNUe7Gl8Y8RntsDYOLk%2F9%2BTZaTh09FwkgnETDoZuOV30F2nV%2B5S9pPWj0doexzfAoR1UMNtg5L5AJaeOq4CI2J5QiPDCDNfdLepgdnbJ%2BDtRTtNq7Qz039%2F44kj6kI5VX4jpiAA04osWJuvNGNQr3ipnyRggOhxYtmtOI%2FnOgDDdmi7lyAh&X-Amz-Signature=1bbcb948531e7b36aab812747898e5c12c277eacc8737f6c00678e0d63e13d4e&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cbfaed9e-b398-4902-8936-dea058b21def/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666GXTLJL7%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T181947Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCpB8ndjz9POymC92SlQ718F7Gc2f%2B5HuHHnmM3R1TKsAIhAN6XULiYYgIqkkLzbPenKNg9PY79eWXK7kQ0EjL%2BVzrHKogECKv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igy%2Fvb7iTGMob%2FQmXHgq3APf7ZMelNWwrD4pVMUmcRQji%2Be0FreBC%2F7U%2BJTSrd9v5uMuLlqgvfsvn0ay7FCUoNE1i6BFlK%2FzKkVQmNuPYekQiQ259B28oZ7L31Q9nDXJyVnxu3eNGKIlZMIVvb0NZEiz2U7B1r26Tl%2FEGgrlJyvzmn7OngBiYPY1bVT8pP4iBGYNxGh3yM8rPEabDhDKWOiwqJKUMk7YUacWKm7o4wQnUMvAk38P%2BMZW5MYVufYbnMbpu37eyYRxDqhsLlziEBn0ZhnZniXk8sDtwsC82rwmTTxEvcMEGDuNeAN0lopiGRJUWDMEUDCOBsPpOFV2TwvwkQD60IsQYcpO0znei2OHGmEOIJ8vmmoiTJ9dnvGsQ2WBveVEi3USNv4edakNPOgsLghO3jdSxldmntkwexbgsFM6Jk0dOKOUVQ312ieqxNFuXoboAW3WVbCBEdYoD2UrdTLfjUy5cyK29HvfJPe%2F657%2FbvAxwBwaHtUiV1ORSO47Fona%2FVrLmFnpzhToAo1HGej%2BKBYZo6RlvdOccQktYgGvG2BgKCriXZAj1FYV3g17R8MRY6fKIoYEwXwcDiDe5b1xNbaX%2BtiN73oLq9YFI8EhYp6Wd43pS2cpK%2BnxvOXRX1uBU7nfAnab%2FzCB8%2B68BjqkAdFUiyzUd6VBbwKQHYCn1iREU6YElGRGqkNiAXQdYbNUe7Gl8Y8RntsDYOLk%2F9%2BTZaTh09FwkgnETDoZuOV30F2nV%2B5S9pPWj0doexzfAoR1UMNtg5L5AJaeOq4CI2J5QiPDCDNfdLepgdnbJ%2BDtRTtNq7Qz039%2F44kj6kI5VX4jpiAA04osWJuvNGNQr3ipnyRggOhxYtmtOI%2FnOgDDdmi7lyAh&X-Amz-Signature=10e259fd30562dc19132a87fa636701cf54f32e9b69b158093d7a5c5634ecf1c&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/91181646-b1e0-4433-9711-6259a96a9247/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666GXTLJL7%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T181947Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCpB8ndjz9POymC92SlQ718F7Gc2f%2B5HuHHnmM3R1TKsAIhAN6XULiYYgIqkkLzbPenKNg9PY79eWXK7kQ0EjL%2BVzrHKogECKv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igy%2Fvb7iTGMob%2FQmXHgq3APf7ZMelNWwrD4pVMUmcRQji%2Be0FreBC%2F7U%2BJTSrd9v5uMuLlqgvfsvn0ay7FCUoNE1i6BFlK%2FzKkVQmNuPYekQiQ259B28oZ7L31Q9nDXJyVnxu3eNGKIlZMIVvb0NZEiz2U7B1r26Tl%2FEGgrlJyvzmn7OngBiYPY1bVT8pP4iBGYNxGh3yM8rPEabDhDKWOiwqJKUMk7YUacWKm7o4wQnUMvAk38P%2BMZW5MYVufYbnMbpu37eyYRxDqhsLlziEBn0ZhnZniXk8sDtwsC82rwmTTxEvcMEGDuNeAN0lopiGRJUWDMEUDCOBsPpOFV2TwvwkQD60IsQYcpO0znei2OHGmEOIJ8vmmoiTJ9dnvGsQ2WBveVEi3USNv4edakNPOgsLghO3jdSxldmntkwexbgsFM6Jk0dOKOUVQ312ieqxNFuXoboAW3WVbCBEdYoD2UrdTLfjUy5cyK29HvfJPe%2F657%2FbvAxwBwaHtUiV1ORSO47Fona%2FVrLmFnpzhToAo1HGej%2BKBYZo6RlvdOccQktYgGvG2BgKCriXZAj1FYV3g17R8MRY6fKIoYEwXwcDiDe5b1xNbaX%2BtiN73oLq9YFI8EhYp6Wd43pS2cpK%2BnxvOXRX1uBU7nfAnab%2FzCB8%2B68BjqkAdFUiyzUd6VBbwKQHYCn1iREU6YElGRGqkNiAXQdYbNUe7Gl8Y8RntsDYOLk%2F9%2BTZaTh09FwkgnETDoZuOV30F2nV%2B5S9pPWj0doexzfAoR1UMNtg5L5AJaeOq4CI2J5QiPDCDNfdLepgdnbJ%2BDtRTtNq7Qz039%2F44kj6kI5VX4jpiAA04osWJuvNGNQr3ipnyRggOhxYtmtOI%2FnOgDDdmi7lyAh&X-Amz-Signature=a0ab4855429e9a4063a44e068d6c801321e7af6181edd40024a0776cadd9c1bb&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/09aba1c0-0d55-41dd-852a-a04c5b8a3fac/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T4PKYTDY%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T181948Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEjDqz%2FJIU%2BjfnfC%2BkL5qXfvzHWeE3OUnlIfU4rowYXBAiBOm%2FAGP8Z6vXaRrS2dDyY9jwMoJW2wWgF1XebxnASakCqIBAir%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMssG4vMTfCCxMyCnvKtwDnEodOjSUfMy2BZOYuvY3k9n4yHIilZ077W1nFsDmO9i2Getc%2BeppSxubHyQXbOtkw5p2kczisqE%2B4%2BU4Zi5G0fJxH%2Bzm6R3DCjQsuq2f4xPyA7aYLCwa0HsclgMVjc1drbvbozFG%2BHCSdLAQEXEd4I7DVD5qXOZfS%2FFOfe1oBdk%2BypIz9n90Y1%2BWXk1G8LjBPsCaWZMJ7gCkqBye%2BXYfWaK6phIlMIr8OxnwPwvrM3R2DvlTMwMcCUTMwnPIXZPGJDKD2mUBf9rXBz4CAj8VxB17rVRr7S%2B3eadhEYpwHmLlcew0KayN%2ByEZidCmqf52IupXPrN8TZwfUZD6UgTdAiUZWaKqMfJjhsPLLHbzQ3P5Jb4l%2FIQdnKkGMD0%2FV7uX4NHBbArm8%2B67zbEL%2Bo9zdkZQQmnLbw4lFKHg4b%2BgIaPSl9K6qd8UNI%2Fx%2FC5GsuFot0Pcm%2BbCub1%2FBqcB8gb3qrEhQqbDgP714tALJtCBaM3D5jTZGS2kFlesnXUzlOMvgmW1nvFwgfwhiAuIvOIv5Q82nH4794y5Q9x0UtJeYAexG84GMUrpqVFDSOzLSlWJK1gYfa4AoW1V02x5zkFicbfz0MolmFFy6uLJN63XZD1QDydqQ0XPA6EsImQwq%2FLuvAY6pgFSOcRP7w1wtH%2FMI4tTEYQAQV%2Bi1Oe%2FKmebp5X5NjlI9BywjRZwuX1smPDNvqttMVAJQlyNeD02g0g%2BB0JCU7I9QeLL11LBm1wPL3zrJD1Ah4BjUPQEHAwo5wLkHZ2KktjSJmRhW9UHzjH0IdHIqkysx9%2FkRs163qPa14SomuQ4KcuksTBear2qWeUA1QoPFSFCEjRIcA3HXZQjk9q2y0GZaVf8jedo&X-Amz-Signature=787a700b7234faed670800095ad290522a08364255a74f44fd59b829dcead9a8&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 2. Scatter Plot
Scatter plots present the relationship between two variables in a dataset. It represents data points on a two-dimensional plane. The independent variable or attribute is plotted on the X-axis, while the dependent variable is plotted on the Y-axis.
**Syntax:**
```python
plt.scatter(x, y)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23708af9-659f-4f23-b626-1a4292d7842c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T4PKYTDY%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T181948Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEjDqz%2FJIU%2BjfnfC%2BkL5qXfvzHWeE3OUnlIfU4rowYXBAiBOm%2FAGP8Z6vXaRrS2dDyY9jwMoJW2wWgF1XebxnASakCqIBAir%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMssG4vMTfCCxMyCnvKtwDnEodOjSUfMy2BZOYuvY3k9n4yHIilZ077W1nFsDmO9i2Getc%2BeppSxubHyQXbOtkw5p2kczisqE%2B4%2BU4Zi5G0fJxH%2Bzm6R3DCjQsuq2f4xPyA7aYLCwa0HsclgMVjc1drbvbozFG%2BHCSdLAQEXEd4I7DVD5qXOZfS%2FFOfe1oBdk%2BypIz9n90Y1%2BWXk1G8LjBPsCaWZMJ7gCkqBye%2BXYfWaK6phIlMIr8OxnwPwvrM3R2DvlTMwMcCUTMwnPIXZPGJDKD2mUBf9rXBz4CAj8VxB17rVRr7S%2B3eadhEYpwHmLlcew0KayN%2ByEZidCmqf52IupXPrN8TZwfUZD6UgTdAiUZWaKqMfJjhsPLLHbzQ3P5Jb4l%2FIQdnKkGMD0%2FV7uX4NHBbArm8%2B67zbEL%2Bo9zdkZQQmnLbw4lFKHg4b%2BgIaPSl9K6qd8UNI%2Fx%2FC5GsuFot0Pcm%2BbCub1%2FBqcB8gb3qrEhQqbDgP714tALJtCBaM3D5jTZGS2kFlesnXUzlOMvgmW1nvFwgfwhiAuIvOIv5Q82nH4794y5Q9x0UtJeYAexG84GMUrpqVFDSOzLSlWJK1gYfa4AoW1V02x5zkFicbfz0MolmFFy6uLJN63XZD1QDydqQ0XPA6EsImQwq%2FLuvAY6pgFSOcRP7w1wtH%2FMI4tTEYQAQV%2Bi1Oe%2FKmebp5X5NjlI9BywjRZwuX1smPDNvqttMVAJQlyNeD02g0g%2BB0JCU7I9QeLL11LBm1wPL3zrJD1Ah4BjUPQEHAwo5wLkHZ2KktjSJmRhW9UHzjH0IdHIqkysx9%2FkRs163qPa14SomuQ4KcuksTBear2qWeUA1QoPFSFCEjRIcA3HXZQjk9q2y0GZaVf8jedo&X-Amz-Signature=49b680195957892cbddacffabfa02a20aaaa1284744cfac96007282f6312a916&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 3. Histogram
A histogram is an important visual representation of data in categorical form. To view the data in a "Binned" form, use the histogram plot with a number of bins required or with the data points that mark the bin edges. The x-axis represents the data bins, and the y-axis represents the number of elements in each bin.
**Syntax:**
```python
plt.hist(x, bins)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/24e4424a-df87-40a1-b63b-195cbdc2e0ab/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T4PKYTDY%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T181948Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEjDqz%2FJIU%2BjfnfC%2BkL5qXfvzHWeE3OUnlIfU4rowYXBAiBOm%2FAGP8Z6vXaRrS2dDyY9jwMoJW2wWgF1XebxnASakCqIBAir%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMssG4vMTfCCxMyCnvKtwDnEodOjSUfMy2BZOYuvY3k9n4yHIilZ077W1nFsDmO9i2Getc%2BeppSxubHyQXbOtkw5p2kczisqE%2B4%2BU4Zi5G0fJxH%2Bzm6R3DCjQsuq2f4xPyA7aYLCwa0HsclgMVjc1drbvbozFG%2BHCSdLAQEXEd4I7DVD5qXOZfS%2FFOfe1oBdk%2BypIz9n90Y1%2BWXk1G8LjBPsCaWZMJ7gCkqBye%2BXYfWaK6phIlMIr8OxnwPwvrM3R2DvlTMwMcCUTMwnPIXZPGJDKD2mUBf9rXBz4CAj8VxB17rVRr7S%2B3eadhEYpwHmLlcew0KayN%2ByEZidCmqf52IupXPrN8TZwfUZD6UgTdAiUZWaKqMfJjhsPLLHbzQ3P5Jb4l%2FIQdnKkGMD0%2FV7uX4NHBbArm8%2B67zbEL%2Bo9zdkZQQmnLbw4lFKHg4b%2BgIaPSl9K6qd8UNI%2Fx%2FC5GsuFot0Pcm%2BbCub1%2FBqcB8gb3qrEhQqbDgP714tALJtCBaM3D5jTZGS2kFlesnXUzlOMvgmW1nvFwgfwhiAuIvOIv5Q82nH4794y5Q9x0UtJeYAexG84GMUrpqVFDSOzLSlWJK1gYfa4AoW1V02x5zkFicbfz0MolmFFy6uLJN63XZD1QDydqQ0XPA6EsImQwq%2FLuvAY6pgFSOcRP7w1wtH%2FMI4tTEYQAQV%2Bi1Oe%2FKmebp5X5NjlI9BywjRZwuX1smPDNvqttMVAJQlyNeD02g0g%2BB0JCU7I9QeLL11LBm1wPL3zrJD1Ah4BjUPQEHAwo5wLkHZ2KktjSJmRhW9UHzjH0IdHIqkysx9%2FkRs163qPa14SomuQ4KcuksTBear2qWeUA1QoPFSFCEjRIcA3HXZQjk9q2y0GZaVf8jedo&X-Amz-Signature=8eb26e9a1e0f472cb7f5e4c7e3de80f6216d5d8762b5c724ee37c46c7f4c0d90&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ab5a6dfe-51f5-43ee-bcb3-33dae4a1c7ad/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T4PKYTDY%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T181948Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEjDqz%2FJIU%2BjfnfC%2BkL5qXfvzHWeE3OUnlIfU4rowYXBAiBOm%2FAGP8Z6vXaRrS2dDyY9jwMoJW2wWgF1XebxnASakCqIBAir%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMssG4vMTfCCxMyCnvKtwDnEodOjSUfMy2BZOYuvY3k9n4yHIilZ077W1nFsDmO9i2Getc%2BeppSxubHyQXbOtkw5p2kczisqE%2B4%2BU4Zi5G0fJxH%2Bzm6R3DCjQsuq2f4xPyA7aYLCwa0HsclgMVjc1drbvbozFG%2BHCSdLAQEXEd4I7DVD5qXOZfS%2FFOfe1oBdk%2BypIz9n90Y1%2BWXk1G8LjBPsCaWZMJ7gCkqBye%2BXYfWaK6phIlMIr8OxnwPwvrM3R2DvlTMwMcCUTMwnPIXZPGJDKD2mUBf9rXBz4CAj8VxB17rVRr7S%2B3eadhEYpwHmLlcew0KayN%2ByEZidCmqf52IupXPrN8TZwfUZD6UgTdAiUZWaKqMfJjhsPLLHbzQ3P5Jb4l%2FIQdnKkGMD0%2FV7uX4NHBbArm8%2B67zbEL%2Bo9zdkZQQmnLbw4lFKHg4b%2BgIaPSl9K6qd8UNI%2Fx%2FC5GsuFot0Pcm%2BbCub1%2FBqcB8gb3qrEhQqbDgP714tALJtCBaM3D5jTZGS2kFlesnXUzlOMvgmW1nvFwgfwhiAuIvOIv5Q82nH4794y5Q9x0UtJeYAexG84GMUrpqVFDSOzLSlWJK1gYfa4AoW1V02x5zkFicbfz0MolmFFy6uLJN63XZD1QDydqQ0XPA6EsImQwq%2FLuvAY6pgFSOcRP7w1wtH%2FMI4tTEYQAQV%2Bi1Oe%2FKmebp5X5NjlI9BywjRZwuX1smPDNvqttMVAJQlyNeD02g0g%2BB0JCU7I9QeLL11LBm1wPL3zrJD1Ah4BjUPQEHAwo5wLkHZ2KktjSJmRhW9UHzjH0IdHIqkysx9%2FkRs163qPa14SomuQ4KcuksTBear2qWeUA1QoPFSFCEjRIcA3HXZQjk9q2y0GZaVf8jedo&X-Amz-Signature=f92061dfa82ebf465f5bba06f5e4cd516c1616f7cee2e404b719ceaf02d99699&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8f1b1d60-cf1b-42b3-9faa-f634c89c3f84/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T4PKYTDY%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T181948Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEjDqz%2FJIU%2BjfnfC%2BkL5qXfvzHWeE3OUnlIfU4rowYXBAiBOm%2FAGP8Z6vXaRrS2dDyY9jwMoJW2wWgF1XebxnASakCqIBAir%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMssG4vMTfCCxMyCnvKtwDnEodOjSUfMy2BZOYuvY3k9n4yHIilZ077W1nFsDmO9i2Getc%2BeppSxubHyQXbOtkw5p2kczisqE%2B4%2BU4Zi5G0fJxH%2Bzm6R3DCjQsuq2f4xPyA7aYLCwa0HsclgMVjc1drbvbozFG%2BHCSdLAQEXEd4I7DVD5qXOZfS%2FFOfe1oBdk%2BypIz9n90Y1%2BWXk1G8LjBPsCaWZMJ7gCkqBye%2BXYfWaK6phIlMIr8OxnwPwvrM3R2DvlTMwMcCUTMwnPIXZPGJDKD2mUBf9rXBz4CAj8VxB17rVRr7S%2B3eadhEYpwHmLlcew0KayN%2ByEZidCmqf52IupXPrN8TZwfUZD6UgTdAiUZWaKqMfJjhsPLLHbzQ3P5Jb4l%2FIQdnKkGMD0%2FV7uX4NHBbArm8%2B67zbEL%2Bo9zdkZQQmnLbw4lFKHg4b%2BgIaPSl9K6qd8UNI%2Fx%2FC5GsuFot0Pcm%2BbCub1%2FBqcB8gb3qrEhQqbDgP714tALJtCBaM3D5jTZGS2kFlesnXUzlOMvgmW1nvFwgfwhiAuIvOIv5Q82nH4794y5Q9x0UtJeYAexG84GMUrpqVFDSOzLSlWJK1gYfa4AoW1V02x5zkFicbfz0MolmFFy6uLJN63XZD1QDydqQ0XPA6EsImQwq%2FLuvAY6pgFSOcRP7w1wtH%2FMI4tTEYQAQV%2Bi1Oe%2FKmebp5X5NjlI9BywjRZwuX1smPDNvqttMVAJQlyNeD02g0g%2BB0JCU7I9QeLL11LBm1wPL3zrJD1Ah4BjUPQEHAwo5wLkHZ2KktjSJmRhW9UHzjH0IdHIqkysx9%2FkRs163qPa14SomuQ4KcuksTBear2qWeUA1QoPFSFCEjRIcA3HXZQjk9q2y0GZaVf8jedo&X-Amz-Signature=e4a99be2db874ebd08299552eb3d97461fb6e310125d45d583e064e9ccb1f22a&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/13ad0497-05fe-4eaa-984e-707b33e14761/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T4PKYTDY%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T181948Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEjDqz%2FJIU%2BjfnfC%2BkL5qXfvzHWeE3OUnlIfU4rowYXBAiBOm%2FAGP8Z6vXaRrS2dDyY9jwMoJW2wWgF1XebxnASakCqIBAir%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMssG4vMTfCCxMyCnvKtwDnEodOjSUfMy2BZOYuvY3k9n4yHIilZ077W1nFsDmO9i2Getc%2BeppSxubHyQXbOtkw5p2kczisqE%2B4%2BU4Zi5G0fJxH%2Bzm6R3DCjQsuq2f4xPyA7aYLCwa0HsclgMVjc1drbvbozFG%2BHCSdLAQEXEd4I7DVD5qXOZfS%2FFOfe1oBdk%2BypIz9n90Y1%2BWXk1G8LjBPsCaWZMJ7gCkqBye%2BXYfWaK6phIlMIr8OxnwPwvrM3R2DvlTMwMcCUTMwnPIXZPGJDKD2mUBf9rXBz4CAj8VxB17rVRr7S%2B3eadhEYpwHmLlcew0KayN%2ByEZidCmqf52IupXPrN8TZwfUZD6UgTdAiUZWaKqMfJjhsPLLHbzQ3P5Jb4l%2FIQdnKkGMD0%2FV7uX4NHBbArm8%2B67zbEL%2Bo9zdkZQQmnLbw4lFKHg4b%2BgIaPSl9K6qd8UNI%2Fx%2FC5GsuFot0Pcm%2BbCub1%2FBqcB8gb3qrEhQqbDgP714tALJtCBaM3D5jTZGS2kFlesnXUzlOMvgmW1nvFwgfwhiAuIvOIv5Q82nH4794y5Q9x0UtJeYAexG84GMUrpqVFDSOzLSlWJK1gYfa4AoW1V02x5zkFicbfz0MolmFFy6uLJN63XZD1QDydqQ0XPA6EsImQwq%2FLuvAY6pgFSOcRP7w1wtH%2FMI4tTEYQAQV%2Bi1Oe%2FKmebp5X5NjlI9BywjRZwuX1smPDNvqttMVAJQlyNeD02g0g%2BB0JCU7I9QeLL11LBm1wPL3zrJD1Ah4BjUPQEHAwo5wLkHZ2KktjSJmRhW9UHzjH0IdHIqkysx9%2FkRs163qPa14SomuQ4KcuksTBear2qWeUA1QoPFSFCEjRIcA3HXZQjk9q2y0GZaVf8jedo&X-Amz-Signature=4ea1faf9039e481fb8fc733c19cb366fa8e50f247f6697c45b68dc8e297a01ab&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 2. Box and Whisker Plot
A box plot shows the distribution of quantitative data in a way that facilitates comparisons between variables or across levels of a categorical variable. The box shows the quartiles of the dataset while the whiskers extend to show the rest of the distribution, except for points that are determined to be "outliers".
**Syntax:**
```python
sns.boxplot(x='header_1', y='header_2', data=df)
```
**Example Output:**


![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d207ae92-0a7c-4e2f-aa65-0ee5a2c33bf7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WMCSOX7Y%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T181949Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIB2QY607E76myatLLIZ6Ta4urtS1h3ztAx%2B%2BGwBmdo8qAiEA6ORsX1JZKoIAAXpyhRAiJjO%2FXV8DjBUbMr%2FgUB5SDKQqiAQIq%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNxrfiKzVDcMvJu%2FSyrcA%2FpqoRCW7gYTN98QHSVg36N3T6fZowamAE1SufWwxw3RG27XWNKGSE3YysACjSJtnATqxSKOhPZCCaYLVaBT%2FKGbTDbP55GwkVfo3xO6wVWrb446DNEg%2FocGHMlg1OmkOym6Gv4uu6J7EXV2Pd0tm%2FZqFJkE%2Fq3As6qF1YiGgFlPPAUhIS57OWIPG7XNlSYBeUMNbKq%2FPvmv94RoP33oMGVgzoxd306xXq14zy8hm4vZQcSZKF%2BV7xEzC%2F4%2BkkuNn%2BGnGM6OWcB6SU1p5iVPQt1KThXJiJZBLMGfsqMyN%2F4BcMMlgJnPu1o2YTELdB1Umy8Y9qHjHItmKa3sC8xvJt75cl6HIHEpCPEKB4F1C2LNfWdbIAocKBy270U7MMd6ke8TS9yTIhdRiVpzsRgX9FKmvSSkaYPSyemB4FXlZx8eMSSu08MetRBUAgaFkQ9BMdnLOM1Ie6D87yM8smSFt6wv8wDCZU3vPu1oOoY6sIHiDwEbpJCEjHjfaWJ3GGSOKzOzUC9LiAybt0h%2FnKBQx%2BW6j7bU4YYyd8rcUHg%2BDyTdzRbgxVLyET61BpMks5swDKFzq75tnK84o7r0qGcd8OrcJPEeyQHKuL7SxaBgPA%2BP%2F3LCgUgPxkoI9gRIMOzy7rwGOqUBm0Da8ipPt0DpEoqOnLB%2FDcvZ3aSWqOkIl7NTxi2TcgFh4r0DWtLAw%2F3K8w7qUEqZNbbjtF20sCg9eNnonyoLL18A8dMulZj59szAWIvWohBBbJz%2F36ZaUqAg28tQ0ACfAbWTVrhXnFFO1ps%2FCfP2ZigHF%2BL%2Bbpi3IeeMiw7rrTJz9YIigTwZVnxzHPQgQCqj5x7DkYwmyHhMoVY0fzkzquEmBXUG&X-Amz-Signature=b7e9aee9cdc631b4bce0ca6e7ae205bbdae6213a2a6aa93634ddb179c1278104&X-Amz-SignedHeaders=host&x-id=GetObject)

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0e516edc-7551-4792-ab18-0494db3c4c0c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466STBXDUH4%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T181949Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCycToh3igJvpVOJwPTK2ogQJfsUXvQlGNjXsHJAKrBgAIgMnbMNj5Bk3%2Fy21bMq0LoWGWC7RBAU3dMKWziWaEe5LYqiAQIq%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKXnHXV%2BUskD63jAkCrcAyaPXgvmBVvDVljpalmSQs%2FiuuLLg7qeGTSQUQlEziELXhzbGt3gH%2FgTRTy0waCtZSd0Igs3nDnI56Q2OMIvAfpg8c%2F0gCZMslv9ZsLRhDl3yBB%2FUobj6nTJe9HP2O1D3f3dJvxVHyKhgDNlXUVtJsWrqERsQsgw6IaGllxppIjPQjgLzc4NDmT1KPVXvpJdQ9xFTwpK5jSrt5C0gH0GCrW8Li2PViknjxVYmkS9c1VDQ7FoXaVJvJuxN4nClCIILQ7O5VhHMMC8qV%2BiyhHVO0hhuzZxjhPeNDOMRd4wRRNxZNvhxx3IvGXbY5EA4xq9owIbU%2FW3FKusVirC7rJggZB4if8hnB%2BAK5PikeHjoqT%2Fy1dBKQzKFSsU2yomYPqOMQG9QmxXsQTEpvrRZ%2FQQPVAPdavakc3sbPA1d%2B4HEBrMdHtrs%2FhzRvDSU1LBfIE%2Bfn8BJC7uO%2BR81mLv4iv%2BuKUxOACINhp%2BFj%2B4HtKUZ4JnpUkPMaDOGe7NElCz0XE59728HhvqLttPjEq%2BEZc%2B5U12mByTRQ5mHsd21FOdHt021SegFyQxa9mf%2BptiuvAgwq4KGHXVhPXGNHDbnJ7BJ956sCCfjYoVLqKzU3NcrjnO9UPfWVR1dKbWSjWPMKzy7rwGOqUBRP4cBo8FRBfqxnm%2F%2FjDkzqA9x9ZVeyWd%2FuMZJdM4%2BcUbND9pxzrNdnCs62Iv4%2F0rhCrt90EkFUw63oFvOAMfFoq0ExlsmZ1LYvD7qqjtjraflqL6RQ6Hx8QJFlE%2BI7Ce9wlOl%2FOIWFbHhT10DMqtiDx0Sm5zXA9wR3KJsI2%2FFaBxoUjkHG4m8q2bhafpNzC4yzblG%2BlA4uCceRrR8mgP%2BfHKLhW9&X-Amz-Signature=1b68c1ec64c96d45227ea3bf17500500893197d58286c1b12ab15274d1339159&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23a79b9d-2356-49a9-8fd9-65c6b0ab2cc5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T4PKYTDY%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T181948Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEjDqz%2FJIU%2BjfnfC%2BkL5qXfvzHWeE3OUnlIfU4rowYXBAiBOm%2FAGP8Z6vXaRrS2dDyY9jwMoJW2wWgF1XebxnASakCqIBAir%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMssG4vMTfCCxMyCnvKtwDnEodOjSUfMy2BZOYuvY3k9n4yHIilZ077W1nFsDmO9i2Getc%2BeppSxubHyQXbOtkw5p2kczisqE%2B4%2BU4Zi5G0fJxH%2Bzm6R3DCjQsuq2f4xPyA7aYLCwa0HsclgMVjc1drbvbozFG%2BHCSdLAQEXEd4I7DVD5qXOZfS%2FFOfe1oBdk%2BypIz9n90Y1%2BWXk1G8LjBPsCaWZMJ7gCkqBye%2BXYfWaK6phIlMIr8OxnwPwvrM3R2DvlTMwMcCUTMwnPIXZPGJDKD2mUBf9rXBz4CAj8VxB17rVRr7S%2B3eadhEYpwHmLlcew0KayN%2ByEZidCmqf52IupXPrN8TZwfUZD6UgTdAiUZWaKqMfJjhsPLLHbzQ3P5Jb4l%2FIQdnKkGMD0%2FV7uX4NHBbArm8%2B67zbEL%2Bo9zdkZQQmnLbw4lFKHg4b%2BgIaPSl9K6qd8UNI%2Fx%2FC5GsuFot0Pcm%2BbCub1%2FBqcB8gb3qrEhQqbDgP714tALJtCBaM3D5jTZGS2kFlesnXUzlOMvgmW1nvFwgfwhiAuIvOIv5Q82nH4794y5Q9x0UtJeYAexG84GMUrpqVFDSOzLSlWJK1gYfa4AoW1V02x5zkFicbfz0MolmFFy6uLJN63XZD1QDydqQ0XPA6EsImQwq%2FLuvAY6pgFSOcRP7w1wtH%2FMI4tTEYQAQV%2Bi1Oe%2FKmebp5X5NjlI9BywjRZwuX1smPDNvqttMVAJQlyNeD02g0g%2BB0JCU7I9QeLL11LBm1wPL3zrJD1Ah4BjUPQEHAwo5wLkHZ2KktjSJmRhW9UHzjH0IdHIqkysx9%2FkRs163qPa14SomuQ4KcuksTBear2qWeUA1QoPFSFCEjRIcA3HXZQjk9q2y0GZaVf8jedo&X-Amz-Signature=a4805fd285061507b9d365e3a786609a6b87f06455b858b0a825cf0fcfc9ad07&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 4. KDE Plot
A Kernel Density Estimate (KDE) plot is a graph that creates a probability distribution curve for the data based upon its likelihood of occurrence on a specific value. This is created for a single vector of information.
**Syntax:**
```python
sns.kdeplot(X) || sns.kdeplot(df['age'])
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0d571213-2a2f-4921-a50b-880847aa05ee/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T4PKYTDY%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T181948Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEjDqz%2FJIU%2BjfnfC%2BkL5qXfvzHWeE3OUnlIfU4rowYXBAiBOm%2FAGP8Z6vXaRrS2dDyY9jwMoJW2wWgF1XebxnASakCqIBAir%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMssG4vMTfCCxMyCnvKtwDnEodOjSUfMy2BZOYuvY3k9n4yHIilZ077W1nFsDmO9i2Getc%2BeppSxubHyQXbOtkw5p2kczisqE%2B4%2BU4Zi5G0fJxH%2Bzm6R3DCjQsuq2f4xPyA7aYLCwa0HsclgMVjc1drbvbozFG%2BHCSdLAQEXEd4I7DVD5qXOZfS%2FFOfe1oBdk%2BypIz9n90Y1%2BWXk1G8LjBPsCaWZMJ7gCkqBye%2BXYfWaK6phIlMIr8OxnwPwvrM3R2DvlTMwMcCUTMwnPIXZPGJDKD2mUBf9rXBz4CAj8VxB17rVRr7S%2B3eadhEYpwHmLlcew0KayN%2ByEZidCmqf52IupXPrN8TZwfUZD6UgTdAiUZWaKqMfJjhsPLLHbzQ3P5Jb4l%2FIQdnKkGMD0%2FV7uX4NHBbArm8%2B67zbEL%2Bo9zdkZQQmnLbw4lFKHg4b%2BgIaPSl9K6qd8UNI%2Fx%2FC5GsuFot0Pcm%2BbCub1%2FBqcB8gb3qrEhQqbDgP714tALJtCBaM3D5jTZGS2kFlesnXUzlOMvgmW1nvFwgfwhiAuIvOIv5Q82nH4794y5Q9x0UtJeYAexG84GMUrpqVFDSOzLSlWJK1gYfa4AoW1V02x5zkFicbfz0MolmFFy6uLJN63XZD1QDydqQ0XPA6EsImQwq%2FLuvAY6pgFSOcRP7w1wtH%2FMI4tTEYQAQV%2Bi1Oe%2FKmebp5X5NjlI9BywjRZwuX1smPDNvqttMVAJQlyNeD02g0g%2BB0JCU7I9QeLL11LBm1wPL3zrJD1Ah4BjUPQEHAwo5wLkHZ2KktjSJmRhW9UHzjH0IdHIqkysx9%2FkRs163qPa14SomuQ4KcuksTBear2qWeUA1QoPFSFCEjRIcA3HXZQjk9q2y0GZaVf8jedo&X-Amz-Signature=29e130aee28e6a05c3dd2d932e14273199294a9644ff963c40fef9317098ac30&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/53752550-ef82-4ca9-a01a-09921f0282d0/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T4PKYTDY%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T181948Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEjDqz%2FJIU%2BjfnfC%2BkL5qXfvzHWeE3OUnlIfU4rowYXBAiBOm%2FAGP8Z6vXaRrS2dDyY9jwMoJW2wWgF1XebxnASakCqIBAir%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMssG4vMTfCCxMyCnvKtwDnEodOjSUfMy2BZOYuvY3k9n4yHIilZ077W1nFsDmO9i2Getc%2BeppSxubHyQXbOtkw5p2kczisqE%2B4%2BU4Zi5G0fJxH%2Bzm6R3DCjQsuq2f4xPyA7aYLCwa0HsclgMVjc1drbvbozFG%2BHCSdLAQEXEd4I7DVD5qXOZfS%2FFOfe1oBdk%2BypIz9n90Y1%2BWXk1G8LjBPsCaWZMJ7gCkqBye%2BXYfWaK6phIlMIr8OxnwPwvrM3R2DvlTMwMcCUTMwnPIXZPGJDKD2mUBf9rXBz4CAj8VxB17rVRr7S%2B3eadhEYpwHmLlcew0KayN%2ByEZidCmqf52IupXPrN8TZwfUZD6UgTdAiUZWaKqMfJjhsPLLHbzQ3P5Jb4l%2FIQdnKkGMD0%2FV7uX4NHBbArm8%2B67zbEL%2Bo9zdkZQQmnLbw4lFKHg4b%2BgIaPSl9K6qd8UNI%2Fx%2FC5GsuFot0Pcm%2BbCub1%2FBqcB8gb3qrEhQqbDgP714tALJtCBaM3D5jTZGS2kFlesnXUzlOMvgmW1nvFwgfwhiAuIvOIv5Q82nH4794y5Q9x0UtJeYAexG84GMUrpqVFDSOzLSlWJK1gYfa4AoW1V02x5zkFicbfz0MolmFFy6uLJN63XZD1QDydqQ0XPA6EsImQwq%2FLuvAY6pgFSOcRP7w1wtH%2FMI4tTEYQAQV%2Bi1Oe%2FKmebp5X5NjlI9BywjRZwuX1smPDNvqttMVAJQlyNeD02g0g%2BB0JCU7I9QeLL11LBm1wPL3zrJD1Ah4BjUPQEHAwo5wLkHZ2KktjSJmRhW9UHzjH0IdHIqkysx9%2FkRs163qPa14SomuQ4KcuksTBear2qWeUA1QoPFSFCEjRIcA3HXZQjk9q2y0GZaVf8jedo&X-Amz-Signature=e05da6212bd42b45f2628aa2a51b36b212a2defb2d2dbdf58eeb6554102b6a21&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
## 4. Correlation Between Variables
Correlation is a statistical measure of the extent to which different variables are interdependent. It indicates how changes in one variable are associated with changes in another variable over time.
### Positive Correlation
Positive correlation indicates that as one variable increases, the other variable also tends to increase.
**Example: Engine Size and Price**
- **Positive Correlation:** Engine size increases, price also increases.
- **Visualization:** Scatter plot with a steep positive slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c7ea9b0-3ef3-4357-a9c3-554fc71b6b15/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VXXJ3JSB%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T181949Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIE5bIvy351GABmpTwoXJll5VYmljx961H3jNl2todesPAiATaFId4LSr9u9fA%2B9wChZKnTIpidpWMbyJxFvaIXYeXCqIBAir%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMSRGlSt%2Fb62Y6ovUxKtwDCX347%2FCbAm%2BKyoq55CootWEZH4RRxykfj%2BpnruVuPpjgLAIV2HSzWNQMc05TqkZGlGaIlnT3EPju6fWHOTBOfB9cC31d0o08Ji3%2B4t%2BwrCEhhdghFVbeGQszqlbDV0a876jclqJfSjQSUy6yFBkboTaAS7vsTS61IBI5H2JwNqL3OpppZdnqmMqOIgD%2BCRZB5i53%2BMeT%2FpG%2B6oq18eRDpoyx0Puv7Agw5bN4RzwsKMUjREYJLyIOIHxz6h%2F1N0ZM6RKxVrfLym0ruhx%2F8S03PSLl64gG5x36jWIhi9tAuZzY3oICPiXWAH6MBdWXMJtNxdanvC1%2F6Tj7diIfCgaKNeDxGo0XNYTaKqBF3xPSomvis8I0%2BOC0aPHuJ%2FNCzxzpcV2OrQG3ReLOR5vW9KBpbwVnSaxx%2BMgVSMpZVuy96nYe56QwXVTBlHhDS9d%2BeMblt2lf2SttW2wFYUJKnX7LaWUbHUyc%2BtjLY%2FL%2FYv80mfAgsc6IEvWb7Lc2MFhBhBW3Qlq9kUn9e%2Fgg8OPCOjK0nikMlPa%2Bw9vbi%2FYeDdevEuq9sUoHn%2BrvSgCeINGeKxfRQc9iifDfgtaUEOeqFzDPg1GZEv9LGh6dzpwHFiMiW7eASG8pMODBdm7AmDgwl%2FPuvAY6pgFEJE9Jc%2BOaA1Rw0HfOct%2FKQap0fpoy68ErkM0qpl5Qt0hJTrLt%2Bu%2B9kwGhRw7d%2B2nVj9%2FetoUs01FgpgKjoCIUrXMf063gsK6hoMKSjELPTbsISyZHKsbaiMdeNJ4bo%2BmXDO1kEYTni32EGBByR64d2uxGQQj7bF0j%2BCVpHT95FXFDky9xlGVg9mduHDerhFfHzle1NV5iCIMjQkLgLFaHXJNZBp4W&X-Amz-Signature=750ec0df17f431299dc3cf1df5417c2f9181f86a40ddeea65b887831a079df93&X-Amz-SignedHeaders=host&x-id=GetObject)
**Explanation:** When engine size increases, there is a corresponding increase in the price of the vehicle. This positive correlation suggests that larger engines tend to be associated with higher prices in the market.
___
### Negative Correlation
Negative correlation indicates that as one variable increases, the other variable tends to decrease.
**Example: Highway Miles per Gallon and Price**
- **Negative Correlation:** As highway miles per gallon increases, price decreases.
- **Visualization:** Scatter plot with a steep negative slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/10f1f798-9cc4-4df2-a9c1-5a339f554a0b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663VJLFR36%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T181949Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGzdPYMWzKF0aEC0xqxjKjSfuHXxHH%2FWJsy0RytgDGN3AiEAlMkVL11znJwWxgmQU3q4xeIpxh2YAMR%2B628u3Rsto0QqiAQIq%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGgd70dutGTSKZm6AircA%2BLzOhn1iq1usjxSXjMWrc%2BcKBngK4OtEYzL59zlboBa%2Bmri71lk0fn14lp12DcJ4ohh%2FK168sbIm0yqYmza7rZuCR7akL6IJNbjNXtCt0BeGRKbpjaAUxnjsq%2F0y%2FENp0FE0R0L3g6A6ZuNx0JE82ompN7%2BHfVQtV7zkEmmqKb8lSQ%2B5CArAwYslX6sgManiC7I51GgfwcRjCNdoOgEQRGX77j1QAzsaFn8IQnvhyj64nu8AR67dE5%2FbwBcQhN8Ra27AjSknVSSFxLJ8cR5rkoUT4pi%2BGZFNe38%2BF8qZy7LbBo24fPPYBHZVOakLUM5bFLN%2FViPwB312uA9TsTO3aK4Bg1hUtV9zVUoJru5MBgBcYh0WrufrfEuB33YwJ4HXkK2t3hBEAiUuA7OlCtOTz%2BLnyosCIKMmmtCT%2BFg59Gft2P715U%2BEiwtDCT%2BpyVugqdAS4rSSyTv9S2%2FG2fvXwY5tndpGiX8jA0TMYmHpD2XKdf8eeJm76xZ98h8xVsTxguVsF8gFTWnmr0QaT2yxvA3PFQPo7GjGfpiUASdD%2FPm6g4vUg2r5Jt%2Bn%2FNiLNiBi7BeExWlWjSBeuvaOdokkym%2FoYttJunLIAHWAQOCN%2F54FtZyzzHo3qAFoLbOMIPz7rwGOqUBjMvP6VGeO1MZ0bFl6czklNqhjiNdgh%2BzT4YoJhvsgRy3oPoAkSu6femAE5W%2BtGDI%2F40ScvXA0upaTc%2Bp%2FmZ4f9C%2B%2B33gLVTiH0sOstZEQDE8tlqdCdBFFzFig29DzvOYE2XtqRXxeNbC3Yx1PnhYY4q4vnjBuEgw6Z%2BoUeP%2BLdC8UhUuZRncXejyscNehavWbtT7pdyn9ugqGrn%2BlGz5zJeo9ca9&X-Amz-Signature=98876986f366a1cef66477bfff9b9d33e70935ef44d72adc1e3d826e095cedf0&X-Amz-SignedHeaders=host&x-id=GetObject)
**Explanation:** When highway miles per gallon increases, the price of the vehicle tends to decrease. This negative correlation suggests that cars with higher fuel efficiency (more miles per gallon) are generally priced lower in the market.
___
### Weak Correlation
Weak correlation indicates a lack of strong relationship between the variables.
**Example: RPM and Price**
- **Weak Correlation:** Low and high RPM values show varied prices, indicating no strong predictive relationship.
- **Visualization:** Scatter plot with no clear trend or slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9f914514-8914-4bf4-ac84-d9e3077f6eb1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665AQ2L5XH%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T181949Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDIH8G%2FrZNPX%2BIHIbO8moKwILSzwb5f19xgwgEClN4OqQIgJU%2FV9dL9wmfj8%2FjW%2Fqsic3o0IioE1P0vCSpO5CCF26wqiAQIq%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDP5fXGVndwbTBYMegCrcA43Ecj1fIJTzSGy4czB5v4XflOiJ63oj52dBC3MieHUSaqrzT4xx%2Boxr7FL5ZhD2vuq%2BSd8mmrWzn%2FXLQrKHe3XwIC2aTNthh4eM17GYXWX%2BVSfJaWJx9wjd5Kl26QOVnCQyrAGhCZN%2BwHKd40WM88ctWC6Vit%2F5y4wmtLpPwrDM2qOetFadOJ4%2BfIbcfA4yjwLbOGxHgrisa08F2PH4E%2FjS90wMJpWipcoDllNrHcAXMHfd5PFCTYvKXfbzVn17S83Q4SXBlA2yJo4u9l7A1AoG6ENxEvcjvhdW21Gu%2BptVWRXzXmBLrpo2eO2HDHMZcgP%2B71dG%2B3eDwf5OMAV12lsrJzL9WneD0sVO%2Fw5GGXNd69A7kSGlfQ9Z2KHFnooaBbtELrjEZYcCb7zpCWvgjBnvhzUTYLExpEZp8Q0Q7WH7Ijx7yBxLTYIcy4ieLeGLWbfnFf6fAGZw9z9zlvOmmFLLcr0gzKNHbYVKAk7yTP%2BbpVML1ssLYgs7M42LPY0WaPdPFn93Z%2FJVijsA21RMHzUEgzn%2Fpj3JTow2oaFlp8YIXKZtxdTr9dqzXxPiJKwUU%2FLxadwsYdI647J6hmGBzIuzZqpd5bjVoR3dvKzFyONIRc8E9togWAvaKm5DMJTz7rwGOqUBSeJ66xvcBFeIGVNX8Za2xrDA129cKOHf507KsS4tUnr88Y%2FkPMsc3OBN9mMsN7x0r3MNKcP8DVu9pkoKQ6qUUgqziivU%2Fm1FXrbzeijQIOSpG51wbXWf57%2Ba9vvIqHQbnDKKtzd7YZl8MSDC2i1N1hwOlbTMlkwl3gOWoOFN1yNLifg9UKH7HHuviuXoKgKOM%2BoECf3JRLs24eL1RD6R1drrUcWi&X-Amz-Signature=f7fceed9791a3f08e92ac85ec488e54c2115031439b876837dbcc32fe79883f1&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f18086e5-5b04-4fbf-8309-8944ab20d213/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QG2TSQU2%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T181948Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFxxDMtCIFZQJnMKOD498009WOefpWPc7OFiDOoCxI7yAiEAn3dBiY6kBXmoCw3U2XpGlMtetDOfDJ%2BuyXx0xNRH8rMqiAQIq%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNWlD7DgdUuiDm0iQircA%2FUjZdAUd7PkfDaybNSN3so0VdGLYXREcYO30RWe5E%2Fo4adQv92v3otEpAoLF3m0SGgvZkUHdBKswQNPBFGqOBIZlPU%2Fb7vH%2BLoqnTiRo1ZMJ4C4%2BPho%2F0gxLddqklRACwYHW4ljnlC3CmvWu%2Fw8emCNsgsezyXjGqZIZg%2BiFAM30nL7D7t4xtJWmbVx9NmnfBYWR6GmitpA2NkIz4wdiziWVHFEFLV2PHxFQRvn2G%2F6wQwJXvOih9R0x04CdlbwElEEjQAQ98ZDB1RqWttqowJRUZ5R6bqbKB9l96%2BKy0ViDMtLrBAu1IeNswpSVToHJuFxcdFd5rCp1GOfIYwE0cJCbgofDcGZ48dIldZsHc0JGJ0xsBHdT0%2Fgr%2BQRg8Z4wBP%2BsVf%2FsPZ6rWT1Mnud8iw6Lmd5PrF%2BwHTlvt5TndSe4dC28zwAZRZhZOaFZKq4js6fOtOG9x58xCt4IcClN8O0YEReBnC3sy1oR3VUSD0O6U8Xw3ZHPmTfL8w%2BsmJEwRKKstM4t2S%2BqUa0xGjgtaym1zEkN14InAwJTQze%2BedbGi5IgFoZ5vtQZrJUzvjoptk4UXNoJJRurzt1CDbzF%2BtkPzzr9KGJUuB1x5BC8W9CliD8SmoeK%2BeCaTj0MKDy7rwGOqUB7iv2ULityN7Sp%2FqUZq7HN7rRlPKJlcpWwev570P7kJwHWF2jv4Hnb2lfR00RJGoAX0y3tu7OHJBVeznMKtpxeqkycUAtGdCz2%2BB8n0wrkKb4gVdfhvMNZik0oJhjso00k7hW%2FToN0Nz5pk71b1FCItW4dMnqFZaK%2FG6dFyURqxBf%2BvXNr9u7KsTh%2FGCq2VsC1U2wMS2Rn2kjW09PbPbVD8zYklb6&X-Amz-Signature=78e589958f49e1d3780050aac4fb8d1e58f75101f95fdf5a19569b3341a24257&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Correlation Plot
Heatmap visualizes correlations among variables. Color scheme indicates Pearson correlation coefficients. Dark red diagonal line shows perfect correlation (value of 1) between variables and themselves.
This heatmap offers overview of variable relationships and their link with price.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cd3b341e-cc1a-45f7-8aec-cdc00436d270/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QG2TSQU2%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T181948Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFxxDMtCIFZQJnMKOD498009WOefpWPc7OFiDOoCxI7yAiEAn3dBiY6kBXmoCw3U2XpGlMtetDOfDJ%2BuyXx0xNRH8rMqiAQIq%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNWlD7DgdUuiDm0iQircA%2FUjZdAUd7PkfDaybNSN3so0VdGLYXREcYO30RWe5E%2Fo4adQv92v3otEpAoLF3m0SGgvZkUHdBKswQNPBFGqOBIZlPU%2Fb7vH%2BLoqnTiRo1ZMJ4C4%2BPho%2F0gxLddqklRACwYHW4ljnlC3CmvWu%2Fw8emCNsgsezyXjGqZIZg%2BiFAM30nL7D7t4xtJWmbVx9NmnfBYWR6GmitpA2NkIz4wdiziWVHFEFLV2PHxFQRvn2G%2F6wQwJXvOih9R0x04CdlbwElEEjQAQ98ZDB1RqWttqowJRUZ5R6bqbKB9l96%2BKy0ViDMtLrBAu1IeNswpSVToHJuFxcdFd5rCp1GOfIYwE0cJCbgofDcGZ48dIldZsHc0JGJ0xsBHdT0%2Fgr%2BQRg8Z4wBP%2BsVf%2FsPZ6rWT1Mnud8iw6Lmd5PrF%2BwHTlvt5TndSe4dC28zwAZRZhZOaFZKq4js6fOtOG9x58xCt4IcClN8O0YEReBnC3sy1oR3VUSD0O6U8Xw3ZHPmTfL8w%2BsmJEwRKKstM4t2S%2BqUa0xGjgtaym1zEkN14InAwJTQze%2BedbGi5IgFoZ5vtQZrJUzvjoptk4UXNoJJRurzt1CDbzF%2BtkPzzr9KGJUuB1x5BC8W9CliD8SmoeK%2BeCaTj0MKDy7rwGOqUB7iv2ULityN7Sp%2FqUZq7HN7rRlPKJlcpWwev570P7kJwHWF2jv4Hnb2lfR00RJGoAX0y3tu7OHJBVeznMKtpxeqkycUAtGdCz2%2BB8n0wrkKb4gVdfhvMNZik0oJhjso00k7hW%2FToN0Nz5pk71b1FCItW4dMnqFZaK%2FG6dFyURqxBf%2BvXNr9u7KsTh%2FGCq2VsC1U2wMS2Rn2kjW09PbPbVD8zYklb6&X-Amz-Signature=52d2d90c1383dca9b46deb4bc88c1076aaabd649c5418a65e6151461eee04128&X-Amz-SignedHeaders=host&x-id=GetObject)

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
