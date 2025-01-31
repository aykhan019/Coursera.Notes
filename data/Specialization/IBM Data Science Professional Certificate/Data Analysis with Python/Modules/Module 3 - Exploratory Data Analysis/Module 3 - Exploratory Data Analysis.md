

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7e6d594d-952e-44b6-97ea-31225882aea6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665BZU7N67%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T111211Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCsjeqINUISiQ4myPTcwNtfAfg1wAuPANYg9aFQ4%2F6iUgIhAOKLr%2F3xZkSnIY5jzocEEqd%2BDjJl%2BzJl2Kwp9bNPOZljKogECLz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwK6VlFZ%2BzdabLFur8q3APv6tqmhRlOxSynhjEREgAq9L0VF340n4kjm5anKl90%2BGh5gGsIMcEwA1UACUHZyfR1qOp2rFNSq4NnOqVA%2B5pOCKz82SVcMTJHZgKRkecHl6FQf50fY%2BZqLn1psvAip5sABS3N8Z9aiWkHUaLDBshx2%2BfWNcvJ3xFNF5gKLpscZw8Du5XGrwuXs6xImkgePHsJHQguM3nfmrwCn4WPfwvETeWEVcB%2BvLZ7%2FrvRohgXBSIF3YmPwRZJ5vFG%2FJP5WA25NoGw7ajQOCkGlWC3aO%2Bs%2B4vNHEAsY1zNT0LY4p3O4CormEa8Gmny%2BuZNvAyKBp0BDq6CknCtmBjyND44pndoFMa3mKCGHQnz0ot6m%2FyCg%2FiFbMUNPX7ot874rVysLtLED5Y4ZxMxyE4pEwcrT2P%2FgY88iZyMyQfkQ%2Bn3IeGiPqrsQpCjac0%2Bwdqa5mWhtrd46uQLpzeWND0iCxSOzCftMSYQRCaKR3qT%2B2I85Fw%2FiGI891RALxWQhLseQ4pZEC%2B3gT%2FGpt77cX0pNOIlRnaZr%2BlQgmKObXPC%2FHni%2BLKeP66R93JpCG27gv3oT3LbMtpF2p87UfdzkgdJJYbxI%2FyEsTgC1mf7uRoPAc%2FNpgJgKoCNHizoZPdqb5eG%2BzDa1vK8BjqkAS%2B9mAu9cFfw6XP8oUx%2FhUBe0ggFlvbKOXiA5AU%2FXFoQzQxPWGNi%2Ba1q%2FG9y%2B62sJJJCIIc2%2Bx2eIQVZRd0lXsczZplSu7STM%2FWTR9JhNTLaUCikDgB4ijBtGj558M0ID%2FwE%2FrgHB41EPj4MsmFn1SSuYjRiapBi0PjQpt3LK%2FoeoSvn4aLz4et7ZiUPQaatoG9uemwrMcwYVlOlr3oPmgR5bTmB&X-Amz-Signature=c0a7d036f110c1864e0084f68a86003d8d69639999f5eb168e410bec8ecf3478&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cbfaed9e-b398-4902-8936-dea058b21def/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665BZU7N67%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T111211Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCsjeqINUISiQ4myPTcwNtfAfg1wAuPANYg9aFQ4%2F6iUgIhAOKLr%2F3xZkSnIY5jzocEEqd%2BDjJl%2BzJl2Kwp9bNPOZljKogECLz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwK6VlFZ%2BzdabLFur8q3APv6tqmhRlOxSynhjEREgAq9L0VF340n4kjm5anKl90%2BGh5gGsIMcEwA1UACUHZyfR1qOp2rFNSq4NnOqVA%2B5pOCKz82SVcMTJHZgKRkecHl6FQf50fY%2BZqLn1psvAip5sABS3N8Z9aiWkHUaLDBshx2%2BfWNcvJ3xFNF5gKLpscZw8Du5XGrwuXs6xImkgePHsJHQguM3nfmrwCn4WPfwvETeWEVcB%2BvLZ7%2FrvRohgXBSIF3YmPwRZJ5vFG%2FJP5WA25NoGw7ajQOCkGlWC3aO%2Bs%2B4vNHEAsY1zNT0LY4p3O4CormEa8Gmny%2BuZNvAyKBp0BDq6CknCtmBjyND44pndoFMa3mKCGHQnz0ot6m%2FyCg%2FiFbMUNPX7ot874rVysLtLED5Y4ZxMxyE4pEwcrT2P%2FgY88iZyMyQfkQ%2Bn3IeGiPqrsQpCjac0%2Bwdqa5mWhtrd46uQLpzeWND0iCxSOzCftMSYQRCaKR3qT%2B2I85Fw%2FiGI891RALxWQhLseQ4pZEC%2B3gT%2FGpt77cX0pNOIlRnaZr%2BlQgmKObXPC%2FHni%2BLKeP66R93JpCG27gv3oT3LbMtpF2p87UfdzkgdJJYbxI%2FyEsTgC1mf7uRoPAc%2FNpgJgKoCNHizoZPdqb5eG%2BzDa1vK8BjqkAS%2B9mAu9cFfw6XP8oUx%2FhUBe0ggFlvbKOXiA5AU%2FXFoQzQxPWGNi%2Ba1q%2FG9y%2B62sJJJCIIc2%2Bx2eIQVZRd0lXsczZplSu7STM%2FWTR9JhNTLaUCikDgB4ijBtGj558M0ID%2FwE%2FrgHB41EPj4MsmFn1SSuYjRiapBi0PjQpt3LK%2FoeoSvn4aLz4et7ZiUPQaatoG9uemwrMcwYVlOlr3oPmgR5bTmB&X-Amz-Signature=54eb545ba79864d99a8c9595cab241ff3d7441f56524a8f85e87f4291abdd230&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/91181646-b1e0-4433-9711-6259a96a9247/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665BZU7N67%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T111211Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCsjeqINUISiQ4myPTcwNtfAfg1wAuPANYg9aFQ4%2F6iUgIhAOKLr%2F3xZkSnIY5jzocEEqd%2BDjJl%2BzJl2Kwp9bNPOZljKogECLz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwK6VlFZ%2BzdabLFur8q3APv6tqmhRlOxSynhjEREgAq9L0VF340n4kjm5anKl90%2BGh5gGsIMcEwA1UACUHZyfR1qOp2rFNSq4NnOqVA%2B5pOCKz82SVcMTJHZgKRkecHl6FQf50fY%2BZqLn1psvAip5sABS3N8Z9aiWkHUaLDBshx2%2BfWNcvJ3xFNF5gKLpscZw8Du5XGrwuXs6xImkgePHsJHQguM3nfmrwCn4WPfwvETeWEVcB%2BvLZ7%2FrvRohgXBSIF3YmPwRZJ5vFG%2FJP5WA25NoGw7ajQOCkGlWC3aO%2Bs%2B4vNHEAsY1zNT0LY4p3O4CormEa8Gmny%2BuZNvAyKBp0BDq6CknCtmBjyND44pndoFMa3mKCGHQnz0ot6m%2FyCg%2FiFbMUNPX7ot874rVysLtLED5Y4ZxMxyE4pEwcrT2P%2FgY88iZyMyQfkQ%2Bn3IeGiPqrsQpCjac0%2Bwdqa5mWhtrd46uQLpzeWND0iCxSOzCftMSYQRCaKR3qT%2B2I85Fw%2FiGI891RALxWQhLseQ4pZEC%2B3gT%2FGpt77cX0pNOIlRnaZr%2BlQgmKObXPC%2FHni%2BLKeP66R93JpCG27gv3oT3LbMtpF2p87UfdzkgdJJYbxI%2FyEsTgC1mf7uRoPAc%2FNpgJgKoCNHizoZPdqb5eG%2BzDa1vK8BjqkAS%2B9mAu9cFfw6XP8oUx%2FhUBe0ggFlvbKOXiA5AU%2FXFoQzQxPWGNi%2Ba1q%2FG9y%2B62sJJJCIIc2%2Bx2eIQVZRd0lXsczZplSu7STM%2FWTR9JhNTLaUCikDgB4ijBtGj558M0ID%2FwE%2FrgHB41EPj4MsmFn1SSuYjRiapBi0PjQpt3LK%2FoeoSvn4aLz4et7ZiUPQaatoG9uemwrMcwYVlOlr3oPmgR5bTmB&X-Amz-Signature=7f8c1c1ea560345d76ec978eae3c28323ebdaffdc619e759fb814e84ac2a98e6&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/09aba1c0-0d55-41dd-852a-a04c5b8a3fac/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665XXQ56W5%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T111212Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCNuPynVtQLZH%2FbUsaJYZmSV5q4EVnH4dT0hK8WhhndQQIgBYLo3N7dxUvy0AQXSEMcGd6YaZd5rmyV5jBjdpl1kWUqiAQIvP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMWszeg0JIcdHbmW2SrcA%2Ftxs%2BzySBoBkBf479K2%2Bmom%2F0fXKyygh75TIFRRInok%2FQf%2BAaTHrSO1RkFrVB4J9R%2B7Tyw8tE292vPuHQeoOfPdlr41oWvVT5sA21zmecer4TWwAKSae9u6WeJXC5aYDe%2FxQ6nl4LUYlQvEZmRbXzdYx%2F%2Fq8E0TkiNHRRuf2%2BCQ7um6Du4HGhTMaKbyBTXHTCyffF1SuHUa2IlVmgVPOoFFE2xAwNLzqGket3z3A62wKlpE4Bss4vkD%2Fnb5%2FnTrqLCBSaOH2oR%2FHvist8RSnvX57vcV8hrLjgyd%2BXX46olWZi2z9kCJjlzg5XuaITwzvPUYrb7I%2Fd4Z7aALunaH4EFAcM3dzcV8mB2ZSgXL9D%2Fc2moTXMBYhny%2F5iIFLPqEOh%2Fu9NwUQTOWfyrr1bCx8EEUp%2B%2FoXPCEKD%2Bsi73HzvMN%2BqKcoEkctbdhYeMtoQfJI6T6UQIkmq2NUJBvelUWIDA5cbVm0zHUUt1ncu1vp%2FVTNHygmjB8uNSJKMTWdMQFZxKsT4wrXjxadA1zb%2B9vX5e%2Fd4ixNJLn9yH4z8zWPL0wgLNZRsTBhiZ80ZYRdl%2B8OCvcnFCC3PeFJVUGMXfQt3yu9wR4FmYmrMocAygx7kgtjS%2FVKgReY976n6lMMObW8rwGOqUBPOx2xMxHpIMF0JYNxJFANJii8T0qF1tbww7338W5uUOltlKfKG282dSxR2E1IfJHze4IJHbk%2FOt8RPgNtpLsbpJgdSHuIuL14CtZUcac4ghdgjZ6ss2VqATWl7sS7rqQH2FHshaU4pVimmw0dW8H%2FKbtHfODtNI8u5smVMRXGF%2Bl3teTQDvZNU9JB8%2FyTy2Cvin3bKVOEk5IIBrNiiBraQoWGt%2B3&X-Amz-Signature=652bfce60bcc2e7a309d116924ae80f58649d15fad24e565f158262109436610&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 2. Scatter Plot
Scatter plots present the relationship between two variables in a dataset. It represents data points on a two-dimensional plane. The independent variable or attribute is plotted on the X-axis, while the dependent variable is plotted on the Y-axis.
**Syntax:**
```python
plt.scatter(x, y)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23708af9-659f-4f23-b626-1a4292d7842c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665XXQ56W5%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T111212Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCNuPynVtQLZH%2FbUsaJYZmSV5q4EVnH4dT0hK8WhhndQQIgBYLo3N7dxUvy0AQXSEMcGd6YaZd5rmyV5jBjdpl1kWUqiAQIvP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMWszeg0JIcdHbmW2SrcA%2Ftxs%2BzySBoBkBf479K2%2Bmom%2F0fXKyygh75TIFRRInok%2FQf%2BAaTHrSO1RkFrVB4J9R%2B7Tyw8tE292vPuHQeoOfPdlr41oWvVT5sA21zmecer4TWwAKSae9u6WeJXC5aYDe%2FxQ6nl4LUYlQvEZmRbXzdYx%2F%2Fq8E0TkiNHRRuf2%2BCQ7um6Du4HGhTMaKbyBTXHTCyffF1SuHUa2IlVmgVPOoFFE2xAwNLzqGket3z3A62wKlpE4Bss4vkD%2Fnb5%2FnTrqLCBSaOH2oR%2FHvist8RSnvX57vcV8hrLjgyd%2BXX46olWZi2z9kCJjlzg5XuaITwzvPUYrb7I%2Fd4Z7aALunaH4EFAcM3dzcV8mB2ZSgXL9D%2Fc2moTXMBYhny%2F5iIFLPqEOh%2Fu9NwUQTOWfyrr1bCx8EEUp%2B%2FoXPCEKD%2Bsi73HzvMN%2BqKcoEkctbdhYeMtoQfJI6T6UQIkmq2NUJBvelUWIDA5cbVm0zHUUt1ncu1vp%2FVTNHygmjB8uNSJKMTWdMQFZxKsT4wrXjxadA1zb%2B9vX5e%2Fd4ixNJLn9yH4z8zWPL0wgLNZRsTBhiZ80ZYRdl%2B8OCvcnFCC3PeFJVUGMXfQt3yu9wR4FmYmrMocAygx7kgtjS%2FVKgReY976n6lMMObW8rwGOqUBPOx2xMxHpIMF0JYNxJFANJii8T0qF1tbww7338W5uUOltlKfKG282dSxR2E1IfJHze4IJHbk%2FOt8RPgNtpLsbpJgdSHuIuL14CtZUcac4ghdgjZ6ss2VqATWl7sS7rqQH2FHshaU4pVimmw0dW8H%2FKbtHfODtNI8u5smVMRXGF%2Bl3teTQDvZNU9JB8%2FyTy2Cvin3bKVOEk5IIBrNiiBraQoWGt%2B3&X-Amz-Signature=6390ca8411c4e114609ee84a5aa4dc1768f7f1734aaae3f1ab5ac514a67352a9&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 3. Histogram
A histogram is an important visual representation of data in categorical form. To view the data in a "Binned" form, use the histogram plot with a number of bins required or with the data points that mark the bin edges. The x-axis represents the data bins, and the y-axis represents the number of elements in each bin.
**Syntax:**
```python
plt.hist(x, bins)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/24e4424a-df87-40a1-b63b-195cbdc2e0ab/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665XXQ56W5%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T111212Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCNuPynVtQLZH%2FbUsaJYZmSV5q4EVnH4dT0hK8WhhndQQIgBYLo3N7dxUvy0AQXSEMcGd6YaZd5rmyV5jBjdpl1kWUqiAQIvP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMWszeg0JIcdHbmW2SrcA%2Ftxs%2BzySBoBkBf479K2%2Bmom%2F0fXKyygh75TIFRRInok%2FQf%2BAaTHrSO1RkFrVB4J9R%2B7Tyw8tE292vPuHQeoOfPdlr41oWvVT5sA21zmecer4TWwAKSae9u6WeJXC5aYDe%2FxQ6nl4LUYlQvEZmRbXzdYx%2F%2Fq8E0TkiNHRRuf2%2BCQ7um6Du4HGhTMaKbyBTXHTCyffF1SuHUa2IlVmgVPOoFFE2xAwNLzqGket3z3A62wKlpE4Bss4vkD%2Fnb5%2FnTrqLCBSaOH2oR%2FHvist8RSnvX57vcV8hrLjgyd%2BXX46olWZi2z9kCJjlzg5XuaITwzvPUYrb7I%2Fd4Z7aALunaH4EFAcM3dzcV8mB2ZSgXL9D%2Fc2moTXMBYhny%2F5iIFLPqEOh%2Fu9NwUQTOWfyrr1bCx8EEUp%2B%2FoXPCEKD%2Bsi73HzvMN%2BqKcoEkctbdhYeMtoQfJI6T6UQIkmq2NUJBvelUWIDA5cbVm0zHUUt1ncu1vp%2FVTNHygmjB8uNSJKMTWdMQFZxKsT4wrXjxadA1zb%2B9vX5e%2Fd4ixNJLn9yH4z8zWPL0wgLNZRsTBhiZ80ZYRdl%2B8OCvcnFCC3PeFJVUGMXfQt3yu9wR4FmYmrMocAygx7kgtjS%2FVKgReY976n6lMMObW8rwGOqUBPOx2xMxHpIMF0JYNxJFANJii8T0qF1tbww7338W5uUOltlKfKG282dSxR2E1IfJHze4IJHbk%2FOt8RPgNtpLsbpJgdSHuIuL14CtZUcac4ghdgjZ6ss2VqATWl7sS7rqQH2FHshaU4pVimmw0dW8H%2FKbtHfODtNI8u5smVMRXGF%2Bl3teTQDvZNU9JB8%2FyTy2Cvin3bKVOEk5IIBrNiiBraQoWGt%2B3&X-Amz-Signature=fde7a8a5489bc449ac44d536095219a11e330e122bf76f264e116b2e9a9a22e2&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ab5a6dfe-51f5-43ee-bcb3-33dae4a1c7ad/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665XXQ56W5%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T111212Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCNuPynVtQLZH%2FbUsaJYZmSV5q4EVnH4dT0hK8WhhndQQIgBYLo3N7dxUvy0AQXSEMcGd6YaZd5rmyV5jBjdpl1kWUqiAQIvP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMWszeg0JIcdHbmW2SrcA%2Ftxs%2BzySBoBkBf479K2%2Bmom%2F0fXKyygh75TIFRRInok%2FQf%2BAaTHrSO1RkFrVB4J9R%2B7Tyw8tE292vPuHQeoOfPdlr41oWvVT5sA21zmecer4TWwAKSae9u6WeJXC5aYDe%2FxQ6nl4LUYlQvEZmRbXzdYx%2F%2Fq8E0TkiNHRRuf2%2BCQ7um6Du4HGhTMaKbyBTXHTCyffF1SuHUa2IlVmgVPOoFFE2xAwNLzqGket3z3A62wKlpE4Bss4vkD%2Fnb5%2FnTrqLCBSaOH2oR%2FHvist8RSnvX57vcV8hrLjgyd%2BXX46olWZi2z9kCJjlzg5XuaITwzvPUYrb7I%2Fd4Z7aALunaH4EFAcM3dzcV8mB2ZSgXL9D%2Fc2moTXMBYhny%2F5iIFLPqEOh%2Fu9NwUQTOWfyrr1bCx8EEUp%2B%2FoXPCEKD%2Bsi73HzvMN%2BqKcoEkctbdhYeMtoQfJI6T6UQIkmq2NUJBvelUWIDA5cbVm0zHUUt1ncu1vp%2FVTNHygmjB8uNSJKMTWdMQFZxKsT4wrXjxadA1zb%2B9vX5e%2Fd4ixNJLn9yH4z8zWPL0wgLNZRsTBhiZ80ZYRdl%2B8OCvcnFCC3PeFJVUGMXfQt3yu9wR4FmYmrMocAygx7kgtjS%2FVKgReY976n6lMMObW8rwGOqUBPOx2xMxHpIMF0JYNxJFANJii8T0qF1tbww7338W5uUOltlKfKG282dSxR2E1IfJHze4IJHbk%2FOt8RPgNtpLsbpJgdSHuIuL14CtZUcac4ghdgjZ6ss2VqATWl7sS7rqQH2FHshaU4pVimmw0dW8H%2FKbtHfODtNI8u5smVMRXGF%2Bl3teTQDvZNU9JB8%2FyTy2Cvin3bKVOEk5IIBrNiiBraQoWGt%2B3&X-Amz-Signature=e72d3e04e35ce0e72056cfd144c2cd9b3e6944a79dc30178aa37924f2baa018e&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8f1b1d60-cf1b-42b3-9faa-f634c89c3f84/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665XXQ56W5%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T111212Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCNuPynVtQLZH%2FbUsaJYZmSV5q4EVnH4dT0hK8WhhndQQIgBYLo3N7dxUvy0AQXSEMcGd6YaZd5rmyV5jBjdpl1kWUqiAQIvP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMWszeg0JIcdHbmW2SrcA%2Ftxs%2BzySBoBkBf479K2%2Bmom%2F0fXKyygh75TIFRRInok%2FQf%2BAaTHrSO1RkFrVB4J9R%2B7Tyw8tE292vPuHQeoOfPdlr41oWvVT5sA21zmecer4TWwAKSae9u6WeJXC5aYDe%2FxQ6nl4LUYlQvEZmRbXzdYx%2F%2Fq8E0TkiNHRRuf2%2BCQ7um6Du4HGhTMaKbyBTXHTCyffF1SuHUa2IlVmgVPOoFFE2xAwNLzqGket3z3A62wKlpE4Bss4vkD%2Fnb5%2FnTrqLCBSaOH2oR%2FHvist8RSnvX57vcV8hrLjgyd%2BXX46olWZi2z9kCJjlzg5XuaITwzvPUYrb7I%2Fd4Z7aALunaH4EFAcM3dzcV8mB2ZSgXL9D%2Fc2moTXMBYhny%2F5iIFLPqEOh%2Fu9NwUQTOWfyrr1bCx8EEUp%2B%2FoXPCEKD%2Bsi73HzvMN%2BqKcoEkctbdhYeMtoQfJI6T6UQIkmq2NUJBvelUWIDA5cbVm0zHUUt1ncu1vp%2FVTNHygmjB8uNSJKMTWdMQFZxKsT4wrXjxadA1zb%2B9vX5e%2Fd4ixNJLn9yH4z8zWPL0wgLNZRsTBhiZ80ZYRdl%2B8OCvcnFCC3PeFJVUGMXfQt3yu9wR4FmYmrMocAygx7kgtjS%2FVKgReY976n6lMMObW8rwGOqUBPOx2xMxHpIMF0JYNxJFANJii8T0qF1tbww7338W5uUOltlKfKG282dSxR2E1IfJHze4IJHbk%2FOt8RPgNtpLsbpJgdSHuIuL14CtZUcac4ghdgjZ6ss2VqATWl7sS7rqQH2FHshaU4pVimmw0dW8H%2FKbtHfODtNI8u5smVMRXGF%2Bl3teTQDvZNU9JB8%2FyTy2Cvin3bKVOEk5IIBrNiiBraQoWGt%2B3&X-Amz-Signature=1ba5374da26ab7bb45d2800e2f6668722d3311503166e176e645a455c71950f0&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/13ad0497-05fe-4eaa-984e-707b33e14761/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665XXQ56W5%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T111212Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCNuPynVtQLZH%2FbUsaJYZmSV5q4EVnH4dT0hK8WhhndQQIgBYLo3N7dxUvy0AQXSEMcGd6YaZd5rmyV5jBjdpl1kWUqiAQIvP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMWszeg0JIcdHbmW2SrcA%2Ftxs%2BzySBoBkBf479K2%2Bmom%2F0fXKyygh75TIFRRInok%2FQf%2BAaTHrSO1RkFrVB4J9R%2B7Tyw8tE292vPuHQeoOfPdlr41oWvVT5sA21zmecer4TWwAKSae9u6WeJXC5aYDe%2FxQ6nl4LUYlQvEZmRbXzdYx%2F%2Fq8E0TkiNHRRuf2%2BCQ7um6Du4HGhTMaKbyBTXHTCyffF1SuHUa2IlVmgVPOoFFE2xAwNLzqGket3z3A62wKlpE4Bss4vkD%2Fnb5%2FnTrqLCBSaOH2oR%2FHvist8RSnvX57vcV8hrLjgyd%2BXX46olWZi2z9kCJjlzg5XuaITwzvPUYrb7I%2Fd4Z7aALunaH4EFAcM3dzcV8mB2ZSgXL9D%2Fc2moTXMBYhny%2F5iIFLPqEOh%2Fu9NwUQTOWfyrr1bCx8EEUp%2B%2FoXPCEKD%2Bsi73HzvMN%2BqKcoEkctbdhYeMtoQfJI6T6UQIkmq2NUJBvelUWIDA5cbVm0zHUUt1ncu1vp%2FVTNHygmjB8uNSJKMTWdMQFZxKsT4wrXjxadA1zb%2B9vX5e%2Fd4ixNJLn9yH4z8zWPL0wgLNZRsTBhiZ80ZYRdl%2B8OCvcnFCC3PeFJVUGMXfQt3yu9wR4FmYmrMocAygx7kgtjS%2FVKgReY976n6lMMObW8rwGOqUBPOx2xMxHpIMF0JYNxJFANJii8T0qF1tbww7338W5uUOltlKfKG282dSxR2E1IfJHze4IJHbk%2FOt8RPgNtpLsbpJgdSHuIuL14CtZUcac4ghdgjZ6ss2VqATWl7sS7rqQH2FHshaU4pVimmw0dW8H%2FKbtHfODtNI8u5smVMRXGF%2Bl3teTQDvZNU9JB8%2FyTy2Cvin3bKVOEk5IIBrNiiBraQoWGt%2B3&X-Amz-Signature=0e95112c443163ff22b81621880a480093dcb39ba7a3eab10b464f66b0930297&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 2. Box and Whisker Plot
A box plot shows the distribution of quantitative data in a way that facilitates comparisons between variables or across levels of a categorical variable. The box shows the quartiles of the dataset while the whiskers extend to show the rest of the distribution, except for points that are determined to be "outliers".
**Syntax:**
```python
sns.boxplot(x='header_1', y='header_2', data=df)
```
**Example Output:**


![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d207ae92-0a7c-4e2f-aa65-0ee5a2c33bf7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666TTYOSSI%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T111213Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDH2dzGSWsEqNOwZ0x58oj3Rz1vBw8z9yxA5tfJHTgjYAIgZiTDU9JYvswBbqemSSvSNJpfHCA5o9s%2BqSddB0HAOYEqiAQIvP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDIhbcmptK0Q8A8qHhyrcAzg2LtCjHWi%2Bac3eqkUlYAq3i9aAY4u3%2BRCoXIrvcJkn0uxO1WxGU%2B4wBM9G0LTZGuj90TNpCFiPY6VYviFqxy7bPGoJjH2WPB2n%2FWhFdCXZ725oSP9T%2FWLnPMBBDQyIBLgB4%2FzeGtxLHoRSMAtog5uxWFf5IHmDYJyQ0OgFoABCy3E02hFRjg9tAi2rnk7nH5sKKNEBfMaK0V6KCSSvzOFqFiRrjAFhTcYILH8X1W2uwP7IDXabS%2BKoZiFli9HHyYPHLPj4dJKJfrprlHO7XltCvBbsTW%2F%2BUYCtOAA4akmG5wYHZ4F%2BpGLWK7Ae5ZAO7QFEe%2BbIa22GObpFEVAqpJuXfcAVzbWxc9pbqaevu52WmGGc9I4vOzGYGDkFBZa3YkCug80BGr%2BO%2BOIKYoXi%2B4w6VyYwOUbjuz%2BdKs2gITn%2FWK3KQDWDHNIWsEBEV3LGf1is5lAZj0Qs47MNynkgG6zAXUPnZLFdgENV7YA1inpjzCbSyJ4ZI9SaazWruh2qsI8%2FMyJByM9L3ZHkiKp0ji%2BKyQvicj87iEcY9Ug3XHTMEFr9NBf3lkUP%2B3rxEAVk3ytTet5BTcs8EwxyjIgdvcXuhlD%2FYniIQhdF%2Bw6%2FCpYSn5bo%2FIpIvy34G4peMOnW8rwGOqUBaWAj0Gh7gIGjpJ3Kg4cWCZp5jgfskRbxeIbWYZJA214qc70CMtC2A6obyYreb4PFi%2Fb45UP4w%2BnFKimwyyYKNi6nXlFgJqtRnv7La2na5kQe%2BYEAKjXb4wBKm2knDJ3hEVzheoXDFVuB6URbATShT95kpysU5FSNOKPuvFapActhsFkWkq410hMhw8pI9YT8XQiyJVRXedLYWhyjPnLSzfGDj8k0&X-Amz-Signature=d5361a94a554c053a82f98b639a43a59eb7afb366ff93cbf02b39a73fbb57ea3&X-Amz-SignedHeaders=host&x-id=GetObject)

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0e516edc-7551-4792-ab18-0494db3c4c0c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663YU7VMZI%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T111213Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQD2S%2B7IE9HlnrwJxEFLOyZKBsn025Xzd9CF7Bz5lbzxlwIhANjz5rtGz4A6k14%2B3sGPw0VBcBKjpzgh%2F9vqn9puYISdKogECLz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwQJyyPdvj%2FmI%2BeN1kq3APP40nF7Ir88cGJFmrbYbkR1zt64PCHgFwS03edzDh2B9KXFBCSliZ%2Fk9D9DsViC0EJST5JWJgRKi%2Fu0vr7%2FcGtrnSezQ54ojiS%2F7wizksREWcAw95ptjwpAruMV25eK0fqoUqf8oXoXfrTPv9388ELZ4MBMhXLmQFoe70zuLDVNOcPWPkH9eRE0jAMT1YTcKkT3YosHw%2FX8efCDqf1oH9g%2FdGKl9FY7eaBrBV1DXY6iHC2IEfsGqVQXIBwI%2Bg63kCRnKFIi9qUMqY2w%2BZr6%2Fcb%2F8fgiX9gpUFwnubNWSt%2ByXGMneCKKSLna%2BUyM0bBCnU34Qdyj3dYAa87fCGxq3PY4XIsItogcTQR%2BzaTvZ4TQ95Dg65BTJ%2FJVzi2Ha9QEwCBbCCXZ8kehAcHz64cNBaTdTPWYoi1e%2B4JIIIenKr7R0MfKsg4ccFvPYkT1d6PH0zizdn4Aq0%2FbAPoGTQsCNGjsIVPvDqW2Q7BL4la%2BLbRJdpQQG6byOmzgeqmszjGowq5rVnXx8lcPjd7Tn2KDTtj3Xcnjeaanh2cvKl7ytGtzbXL1e9%2FPYwdlkgA84yWqkG%2B4lyR%2Fcr9zUy9yPGocmbOIA05mwhIiK7Fz%2BTJxSRr1l%2F5ec4sNG5zAs1zcTDw1vK8BjqkAWJX8tjlOv5e3ZpBIpY4XQwzPwKGp%2FJ4QnY8Hr1YaapkFRdFLZMSO2MqBTKmgk9jrAxop6FEW6zdvCn01aVpSnzmBSWBxRH7WienxVKAkSQ2tYTfJgWU8d0DAsgL6g%2BmiCX%2FQFtqlH6aNicy2VsPfJx2Wbc0VPfKRX5DKPc244Sde0ZzLAVnaLE%2F%2Fr9KV3VyUs255EgDHcVcipFAeIngo5LKirK6&X-Amz-Signature=a9865b7c0a3a87e38c5a8e080d3e0b34b24979aadd436453dbee4df3473bb125&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23a79b9d-2356-49a9-8fd9-65c6b0ab2cc5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665XXQ56W5%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T111212Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCNuPynVtQLZH%2FbUsaJYZmSV5q4EVnH4dT0hK8WhhndQQIgBYLo3N7dxUvy0AQXSEMcGd6YaZd5rmyV5jBjdpl1kWUqiAQIvP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMWszeg0JIcdHbmW2SrcA%2Ftxs%2BzySBoBkBf479K2%2Bmom%2F0fXKyygh75TIFRRInok%2FQf%2BAaTHrSO1RkFrVB4J9R%2B7Tyw8tE292vPuHQeoOfPdlr41oWvVT5sA21zmecer4TWwAKSae9u6WeJXC5aYDe%2FxQ6nl4LUYlQvEZmRbXzdYx%2F%2Fq8E0TkiNHRRuf2%2BCQ7um6Du4HGhTMaKbyBTXHTCyffF1SuHUa2IlVmgVPOoFFE2xAwNLzqGket3z3A62wKlpE4Bss4vkD%2Fnb5%2FnTrqLCBSaOH2oR%2FHvist8RSnvX57vcV8hrLjgyd%2BXX46olWZi2z9kCJjlzg5XuaITwzvPUYrb7I%2Fd4Z7aALunaH4EFAcM3dzcV8mB2ZSgXL9D%2Fc2moTXMBYhny%2F5iIFLPqEOh%2Fu9NwUQTOWfyrr1bCx8EEUp%2B%2FoXPCEKD%2Bsi73HzvMN%2BqKcoEkctbdhYeMtoQfJI6T6UQIkmq2NUJBvelUWIDA5cbVm0zHUUt1ncu1vp%2FVTNHygmjB8uNSJKMTWdMQFZxKsT4wrXjxadA1zb%2B9vX5e%2Fd4ixNJLn9yH4z8zWPL0wgLNZRsTBhiZ80ZYRdl%2B8OCvcnFCC3PeFJVUGMXfQt3yu9wR4FmYmrMocAygx7kgtjS%2FVKgReY976n6lMMObW8rwGOqUBPOx2xMxHpIMF0JYNxJFANJii8T0qF1tbww7338W5uUOltlKfKG282dSxR2E1IfJHze4IJHbk%2FOt8RPgNtpLsbpJgdSHuIuL14CtZUcac4ghdgjZ6ss2VqATWl7sS7rqQH2FHshaU4pVimmw0dW8H%2FKbtHfODtNI8u5smVMRXGF%2Bl3teTQDvZNU9JB8%2FyTy2Cvin3bKVOEk5IIBrNiiBraQoWGt%2B3&X-Amz-Signature=596a4e8def16dc486b14fda2794c13e6cf45380fee5cc26bc335b6caacd1314c&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 4. KDE Plot
A Kernel Density Estimate (KDE) plot is a graph that creates a probability distribution curve for the data based upon its likelihood of occurrence on a specific value. This is created for a single vector of information.
**Syntax:**
```python
sns.kdeplot(X) || sns.kdeplot(df['age'])
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0d571213-2a2f-4921-a50b-880847aa05ee/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665XXQ56W5%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T111212Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCNuPynVtQLZH%2FbUsaJYZmSV5q4EVnH4dT0hK8WhhndQQIgBYLo3N7dxUvy0AQXSEMcGd6YaZd5rmyV5jBjdpl1kWUqiAQIvP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMWszeg0JIcdHbmW2SrcA%2Ftxs%2BzySBoBkBf479K2%2Bmom%2F0fXKyygh75TIFRRInok%2FQf%2BAaTHrSO1RkFrVB4J9R%2B7Tyw8tE292vPuHQeoOfPdlr41oWvVT5sA21zmecer4TWwAKSae9u6WeJXC5aYDe%2FxQ6nl4LUYlQvEZmRbXzdYx%2F%2Fq8E0TkiNHRRuf2%2BCQ7um6Du4HGhTMaKbyBTXHTCyffF1SuHUa2IlVmgVPOoFFE2xAwNLzqGket3z3A62wKlpE4Bss4vkD%2Fnb5%2FnTrqLCBSaOH2oR%2FHvist8RSnvX57vcV8hrLjgyd%2BXX46olWZi2z9kCJjlzg5XuaITwzvPUYrb7I%2Fd4Z7aALunaH4EFAcM3dzcV8mB2ZSgXL9D%2Fc2moTXMBYhny%2F5iIFLPqEOh%2Fu9NwUQTOWfyrr1bCx8EEUp%2B%2FoXPCEKD%2Bsi73HzvMN%2BqKcoEkctbdhYeMtoQfJI6T6UQIkmq2NUJBvelUWIDA5cbVm0zHUUt1ncu1vp%2FVTNHygmjB8uNSJKMTWdMQFZxKsT4wrXjxadA1zb%2B9vX5e%2Fd4ixNJLn9yH4z8zWPL0wgLNZRsTBhiZ80ZYRdl%2B8OCvcnFCC3PeFJVUGMXfQt3yu9wR4FmYmrMocAygx7kgtjS%2FVKgReY976n6lMMObW8rwGOqUBPOx2xMxHpIMF0JYNxJFANJii8T0qF1tbww7338W5uUOltlKfKG282dSxR2E1IfJHze4IJHbk%2FOt8RPgNtpLsbpJgdSHuIuL14CtZUcac4ghdgjZ6ss2VqATWl7sS7rqQH2FHshaU4pVimmw0dW8H%2FKbtHfODtNI8u5smVMRXGF%2Bl3teTQDvZNU9JB8%2FyTy2Cvin3bKVOEk5IIBrNiiBraQoWGt%2B3&X-Amz-Signature=08353bf2ae8db3e1b58bad351565432401594d046e5eeb40e4dacecbbca17097&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/53752550-ef82-4ca9-a01a-09921f0282d0/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665XXQ56W5%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T111212Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCNuPynVtQLZH%2FbUsaJYZmSV5q4EVnH4dT0hK8WhhndQQIgBYLo3N7dxUvy0AQXSEMcGd6YaZd5rmyV5jBjdpl1kWUqiAQIvP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMWszeg0JIcdHbmW2SrcA%2Ftxs%2BzySBoBkBf479K2%2Bmom%2F0fXKyygh75TIFRRInok%2FQf%2BAaTHrSO1RkFrVB4J9R%2B7Tyw8tE292vPuHQeoOfPdlr41oWvVT5sA21zmecer4TWwAKSae9u6WeJXC5aYDe%2FxQ6nl4LUYlQvEZmRbXzdYx%2F%2Fq8E0TkiNHRRuf2%2BCQ7um6Du4HGhTMaKbyBTXHTCyffF1SuHUa2IlVmgVPOoFFE2xAwNLzqGket3z3A62wKlpE4Bss4vkD%2Fnb5%2FnTrqLCBSaOH2oR%2FHvist8RSnvX57vcV8hrLjgyd%2BXX46olWZi2z9kCJjlzg5XuaITwzvPUYrb7I%2Fd4Z7aALunaH4EFAcM3dzcV8mB2ZSgXL9D%2Fc2moTXMBYhny%2F5iIFLPqEOh%2Fu9NwUQTOWfyrr1bCx8EEUp%2B%2FoXPCEKD%2Bsi73HzvMN%2BqKcoEkctbdhYeMtoQfJI6T6UQIkmq2NUJBvelUWIDA5cbVm0zHUUt1ncu1vp%2FVTNHygmjB8uNSJKMTWdMQFZxKsT4wrXjxadA1zb%2B9vX5e%2Fd4ixNJLn9yH4z8zWPL0wgLNZRsTBhiZ80ZYRdl%2B8OCvcnFCC3PeFJVUGMXfQt3yu9wR4FmYmrMocAygx7kgtjS%2FVKgReY976n6lMMObW8rwGOqUBPOx2xMxHpIMF0JYNxJFANJii8T0qF1tbww7338W5uUOltlKfKG282dSxR2E1IfJHze4IJHbk%2FOt8RPgNtpLsbpJgdSHuIuL14CtZUcac4ghdgjZ6ss2VqATWl7sS7rqQH2FHshaU4pVimmw0dW8H%2FKbtHfODtNI8u5smVMRXGF%2Bl3teTQDvZNU9JB8%2FyTy2Cvin3bKVOEk5IIBrNiiBraQoWGt%2B3&X-Amz-Signature=03034fe17a3f4d675f71b89465269b616366202208d1ced7b1ffbc505622f5f5&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
## 4. Correlation Between Variables
Correlation is a statistical measure of the extent to which different variables are interdependent. It indicates how changes in one variable are associated with changes in another variable over time.
### Positive Correlation
Positive correlation indicates that as one variable increases, the other variable also tends to increase.
**Example: Engine Size and Price**
- **Positive Correlation:** Engine size increases, price also increases.
- **Visualization:** Scatter plot with a steep positive slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c7ea9b0-3ef3-4357-a9c3-554fc71b6b15/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466V7YQ5YBF%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T111213Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAfGfv5gnVe95awWbWS%2BK5iXwQPzACtAB3srUeiynbK3AiEA57TPTQ92Y8NsiiKpBmaFwxRWdUvY76PYw57OANajIGEqiAQIvP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMZ0PLfX9n%2BPgHkJZCrcAxSeFKrfteNKSDv%2Bo6yWLW3jkDpLFBeG9dcfva1KuLiZ%2Fs%2FqS0w8EAauWF%2Fdhn0sOj%2BT6O61rfHc7eaFFxzL%2F3W4RNR3rtKw708CBytGXE5K35FSH49y%2Bgq%2FPEePb8YSSLTWIl%2BsYOQmStlGNddVyB1X6wvDp1k%2BN3Y6Qw9IGjrFh%2F8W0fRUTGJTm5CzbfZvjSbmy%2FVzNzhJBHVoENFKUXhxeD5ZT291Og69csEGrdK4G2RzdJL8x9A6Ml35DPzusKYp%2FDyn34z1PFhad4q%2FH0vK47kF2BUGt%2BV%2FwprY4n307bBPQAMmvxgKzjZJYT5JgH4fB%2BiPhqCezOar4qZtC7Ept5Lp7xDrjaceBA7klmjaHY5nb8naAHrbJkdpRrjWYEA%2Fe%2B9kaG68Fg9YTcpkaXhT5GUkd2Gw5ua%2BjgBV7lWCXwzugUfgvtP5dznTljqizwUSUI689CfHB2kTnx6Hi1M9deVFOvZEyMpVpgLeM2LnBrvkNla2qKjZvA1j70lSMjr8YbRsoyGSJ%2B9rAJq7FBTRsBkYPDjjDTT0%2BxL7l%2F5kUaKKmbxIMSHKwLAYJlaVQjgS6QVMxAHTFnB6CJHj7pj5HsBMlLIAt3LMOifvvILO3UH5yp3uxL%2F58YDmMLrW8rwGOqUBbweA0LDUEPsFHIU%2FG0HZC7E48wckWioLqE%2BPvNTYn%2Fp8xHVWs8IKUNuRLIb4PRy%2FwEKUOzNOhrAidq52O4Y45pFVoUB755Z2xxeZF7i04vECwZYiSaHvHUpgC1KfHTy0RCqxpWyZdMG9E4rkckm%2FPmVXR7aIxhAjJ3u3f5xNMhe2CAxlcRF8pN7aL2bsVWpCIFH2iMgqLKXLKI965VFhEgiUE5dF&X-Amz-Signature=61d5000a5fbec4eb3d33cba38c483849164e35cb33fb4c8cdedb5a425a88ce95&X-Amz-SignedHeaders=host&x-id=GetObject)
**Explanation:** When engine size increases, there is a corresponding increase in the price of the vehicle. This positive correlation suggests that larger engines tend to be associated with higher prices in the market.
___
### Negative Correlation
Negative correlation indicates that as one variable increases, the other variable tends to decrease.
**Example: Highway Miles per Gallon and Price**
- **Negative Correlation:** As highway miles per gallon increases, price decreases.
- **Visualization:** Scatter plot with a steep negative slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/10f1f798-9cc4-4df2-a9c1-5a339f554a0b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SFPRRWNM%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T111213Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQC1bYWlPeMS3PGA8chb4x%2BLw%2FAD%2BvsyojCUelBd1ezRIwIgZFlHyvAvIo8TjaKHVjvBT4KfcnCJ%2BPBjIvRgep7e5H8qiAQIvP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDF5LbFs0FcPorsmVoSrcA6veZPuJ2C6hbDIjIDzTNtjOqeKtrDwGn58DnTmp%2F0qh93sTiM3yYWJljtrnnbD%2B%2Fqrc4GtZI75P%2BjN829IkD5CkQ4Zdz8jJ6J%2B7fIJsHOFGG2yMXtyho2orMXRFPpblPPWcMjGpaNKS7bCRqsbNyaBaUHBttd8ohH3RizMhbFfoF2puqLnU0cPDQMD4ygXgKnYqPG5C2MjLwdKqxJov3VJ76BwEZiJeRxtUn1IZpI1HwgBbo1%2FffZZkIAd5jrkAFraaUtS0j7XMdzN0ioHat%2BhvNq7vHJZ6reP9ovD8qkpSmUkqDNc56ERLrpU5ibkcYDMebqavZXn6uFsdlXNgt0UpVXOzNl%2F2Uvd3qGsOf4fpbRrkoFft6wYtrwvszxdLBnzji3RW6VW7pGDUjsLRKnzkztUIRG%2FtIAua1KQs8KkPI7Bo9Q1c3cP1nsdUKHw1jnApHaG2%2Bz0%2BVWJIV4akn0h%2Bv7tvzNK0awa0lscmAlfeX%2FD%2BOs9T82k2irjanEseFNZt7LFPiJKhJQeGmvrPFsGChJliwV%2B0gYE3i5bLCs3DJ%2Boc1%2FAq5Lo%2Bl4ydP5DOVukJLrpup2WXGzmcN9y6UBfmRCyc8kRWP22j7yYPilk0w88Yft2jmLiak%2FIdMLXW8rwGOqUBC3MZCROBN0iXi%2BLUVgsgO0P7UoOtcHLB7L%2BN9qxRvdhkILiidPLmM4Y4jsunSpCsB8OEeLbKZdpIWlneZh1Yvo0kg0tijOOowkpFYbBSwPVLx2IB74ppQfk6E6MrjNoP8RbY1G4dX%2FlENI%2BPlXvZ1MV570xsuIdDAdblyBix87VJ%2BO4bstB9iiZJZx6ejITI6yLB5xdS9WovA%2BUaYhnWW2hVGg6s&X-Amz-Signature=ef06e97f1db7d6e86d31f95db25635302e1a84dc5412d234b1a795fa8fa4fc8d&X-Amz-SignedHeaders=host&x-id=GetObject)
**Explanation:** When highway miles per gallon increases, the price of the vehicle tends to decrease. This negative correlation suggests that cars with higher fuel efficiency (more miles per gallon) are generally priced lower in the market.
___
### Weak Correlation
Weak correlation indicates a lack of strong relationship between the variables.
**Example: RPM and Price**
- **Weak Correlation:** Low and high RPM values show varied prices, indicating no strong predictive relationship.
- **Visualization:** Scatter plot with no clear trend or slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9f914514-8914-4bf4-ac84-d9e3077f6eb1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466USRDP5AH%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T111213Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHxXwYxCH4lRjoTH03drOSey86IPXGgfXdRVcCRsRasvAiBZZ5c7niBgPvxP58779ZKd%2F5gj%2BH3T4%2BDEYLtsUhuQeCqIBAi8%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMSoygUOjMrnpt5tVsKtwDIXzQiBtFq1G84V3Q504XdWKTC8RtD4aB7JJYtVOyjx2%2FDiNLX1l%2BzqfX1xOWskL0KQuB1vWpfoVhkWFaQjx6nXye2RbpB77ufH5S1vTxzWto6I84Grgx1DtE6YIG9kTc24WFJF%2BXKj0FwuzOtzclbSMFjOQGS%2BBoAfltS3iAoVjSXedGVUBJ2XIVs9QLcymbO4b2sS5c5uLekwG98F88RB2uYTFb2GPZJF3OqMxn3R8nXbkDCMPOkVsRQuZUy94X2ii0iKVxj14AnRxAZkkt8RMaWZcqGWt3nvLZuqGXOppayYqaQd78XBjFWJALMUtegWl%2FhhCGUUQ%2B6wUZdLwfH7HQVmCf5Eg3CYCqOzdbghUkIUyvNutWieQLKOiwp6OLB0M7Mdt3H9wPzSY%2FwSlTx%2FbyPvj1wQjMgtxzzgO4x0iIysfPZo4Hy95eHQTsVnUwsQf4cdm80G0DUphdvw%2B4omuAvkWa3Frh7h0qBKSPGJwCzb8QL4iKZbzhD2UsRNuYfRQ8sLuW%2F7GRKBBZAzNdyYyInbJd%2FHkHPBwB%2FXCWyE%2BVnh%2BcMM0DG6nWPqQh3YscsTJCpWTOR%2FTc9hBSRxZ3ev12Q04a%2BnUo%2FJQ91hPHnYdJZIwORYH6jYN2mHIwt9byvAY6pgFWcTSVzVpLudSKYRV%2BtUWVgUjc2D7I3kBHuFHHEAtBtj1kt5aZ6HeAoFv%2FJh6Ta0liKNu5Gu5%2FiJvCE4pAg5il8x7UhTDPjUQ%2B4kCD0zhzzV9Y945nYzvgeYuqrbWeyQREsjkgBI7HFx5dckxsfD4Nts%2BwyUG9RR1cgPbgiIDI1CfoO%2Bq%2BPYkSiUOK0rQ96f%2BpLBIxA1ZjxMyCbUExAn5i1iCC%2B8RN&X-Amz-Signature=ae77b2142a2c2d3909feab457daaf10b694a9bfc78b956bc2c0c59653edf31ed&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f18086e5-5b04-4fbf-8309-8944ab20d213/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664XJTKHCX%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T111213Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCKp5%2FbfrSmAKtcfumT0m1e6Ew2wfs408S5u%2BzJDekleAIgehWp3azhWwOmLm5u%2BKqe0vDbNnoEPGp9E76uoWNeNeMqiAQIvP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNsl7dYij2%2BpP%2BjoFCrcA8bARMxBPOm9PKgD0zvoL3OP%2BddvWFWJonP6FB1uA%2BKM4vpYkQBy143odL7DoW6NeT0RN%2FOkyYN4XPfUhUcFYcQI8hzYXdi25iaJ18WLlAO8dGVtaq%2FY5D5A3WFhT30L1E%2FDyKhT4sQ2vAbuNTzHb6W7rEFnp9AJif19T1witOHr4P4TPps1EXDY6JeUwzHWem7Vgzg76jANJkh07ymCCgF0Un1dZxADi7zPBUwlhq2pm4qMJYNIptY0drX8Yf0YZILn76q1UxGLHiW4Vh%2B03yEi%2BQInXuCfpnEr4E0PRdyS5vowCMH0wJ6O3IT%2BBjRu9jYJYohmXdWEJ1MqLoDu4LHqimtUpKpu5Lx5ZiU7eoR1fqBKnn%2FNlMU%2BJ3T5Lz3uZkA80fYj%2FjWhb0cBwC4sGpHTKXY16Gxshm5BguqsMl5tnmuFkfIDDcnV%2FaA%2Fxlwm0bd4%2BTeNl4cW1XuvPXzxBV7GgcRYGEG9jX8CvTBmgX26XMRHDN8hehtnGNviMhRtwJWnKtvJ4RRQC5ce3IZ0gyJvvul%2FUztIHaaDNS60yjoI71yaFZgcr%2BspiRiMRIL5u98i%2Ft6KFr%2Fb2yE%2B9cUvmF%2BPvQ1dO5XvEmtRewN%2Birzkm2RTqE3ORpJlHMjsMMzX8rwGOqUBU8JqRbZttZ0ybXQKKE79O8uDQ2zg9tvJ6EkCsZlaILz4uaSonyelxvYxTw9d5iFiKqIm4B%2FT2eY%2Frzd81bv%2BJ0%2B%2BRXkbOnbCv%2BLK0enGZ%2FykndcNJ61hSN%2FE9NvC5TCbF6aQj7E6fkSfalfwCnQGkmsN2KuC%2BKckwzLpsn0jeXMTIXlNTF%2FeCK09B376pgjnBYkBS%2BWASplK67dTjq0jMvvLdcV8&X-Amz-Signature=dcb382dffc2d29e24c6ab3f8dd92c258ddb42c3f03b8652154fc139e88efeb4b&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Correlation Plot
Heatmap visualizes correlations among variables. Color scheme indicates Pearson correlation coefficients. Dark red diagonal line shows perfect correlation (value of 1) between variables and themselves.
This heatmap offers overview of variable relationships and their link with price.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cd3b341e-cc1a-45f7-8aec-cdc00436d270/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664XJTKHCX%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T111213Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCKp5%2FbfrSmAKtcfumT0m1e6Ew2wfs408S5u%2BzJDekleAIgehWp3azhWwOmLm5u%2BKqe0vDbNnoEPGp9E76uoWNeNeMqiAQIvP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNsl7dYij2%2BpP%2BjoFCrcA8bARMxBPOm9PKgD0zvoL3OP%2BddvWFWJonP6FB1uA%2BKM4vpYkQBy143odL7DoW6NeT0RN%2FOkyYN4XPfUhUcFYcQI8hzYXdi25iaJ18WLlAO8dGVtaq%2FY5D5A3WFhT30L1E%2FDyKhT4sQ2vAbuNTzHb6W7rEFnp9AJif19T1witOHr4P4TPps1EXDY6JeUwzHWem7Vgzg76jANJkh07ymCCgF0Un1dZxADi7zPBUwlhq2pm4qMJYNIptY0drX8Yf0YZILn76q1UxGLHiW4Vh%2B03yEi%2BQInXuCfpnEr4E0PRdyS5vowCMH0wJ6O3IT%2BBjRu9jYJYohmXdWEJ1MqLoDu4LHqimtUpKpu5Lx5ZiU7eoR1fqBKnn%2FNlMU%2BJ3T5Lz3uZkA80fYj%2FjWhb0cBwC4sGpHTKXY16Gxshm5BguqsMl5tnmuFkfIDDcnV%2FaA%2Fxlwm0bd4%2BTeNl4cW1XuvPXzxBV7GgcRYGEG9jX8CvTBmgX26XMRHDN8hehtnGNviMhRtwJWnKtvJ4RRQC5ce3IZ0gyJvvul%2FUztIHaaDNS60yjoI71yaFZgcr%2BspiRiMRIL5u98i%2Ft6KFr%2Fb2yE%2B9cUvmF%2BPvQ1dO5XvEmtRewN%2Birzkm2RTqE3ORpJlHMjsMMzX8rwGOqUBU8JqRbZttZ0ybXQKKE79O8uDQ2zg9tvJ6EkCsZlaILz4uaSonyelxvYxTw9d5iFiKqIm4B%2FT2eY%2Frzd81bv%2BJ0%2B%2BRXkbOnbCv%2BLK0enGZ%2FykndcNJ61hSN%2FE9NvC5TCbF6aQj7E6fkSfalfwCnQGkmsN2KuC%2BKckwzLpsn0jeXMTIXlNTF%2FeCK09B376pgjnBYkBS%2BWASplK67dTjq0jMvvLdcV8&X-Amz-Signature=693c41109ca09d23a33a48dcdcf5caa099f60f2c5391e3921a4190606c50d159&X-Amz-SignedHeaders=host&x-id=GetObject)

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
