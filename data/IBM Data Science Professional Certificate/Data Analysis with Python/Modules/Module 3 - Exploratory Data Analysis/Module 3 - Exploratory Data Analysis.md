

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7e6d594d-952e-44b6-97ea-31225882aea6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666Y6JAHAE%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T182003Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAIaCXVzLXdlc3QtMiJIMEYCIQCQGbrTfaR7o7DhGBQE7frs%2BWUkcz6NiCOSveqq9OWgtgIhAKMMI0FUGOb%2B0y3ti6CDPmB2bph60KVEfmzMTr1Vb8I4Kv8DCBsQABoMNjM3NDIzMTgzODA1IgxSSw%2Fe6p6g5E8c0rkq3AMd%2Bgl3SVf0%2FdkWnxOPnv8NqsX%2B6X%2F3O6T4oYE%2BZB4oD1dx73iMeXBhXKtrj34UHk0VvOsZqo2Y0g9s2eqpIkhVB7qH%2BOviINoLmOXzcgoQq0mlHRWUJFHtJeFr5Dlul5qIQBbkD09HhT1Umh4jsNvbShr%2BGImL3p43xVoToJI13%2FWoCZKxneasNHvXWkUiTGxOASgCTUB4btdOfCfdIFIFpBcIjZtjM3x3iFAgjLzNCtrIWdWfd3vnXLbXtHACOc7nwT7cK4bGc%2FfGdpsbb7xKCqJkAsGBZFeqGPOIc5in2thrSm7PgKZSBoFllN3iAS0aa%2Fr8wLoNW70%2FRhmMguheJGCJrOj8PtDpZIMJv1pTrIDlvoHghBjP6Fy2ffD6LdwGskGLIwFQSnQDse8Bc539lLROVPfBJNySaccykVcIx4UXWy6u%2B%2FC424%2FX5KbHUMOcM2ZH8on1ft%2BRWlGWtxGl0uQkvQvZzD7Ans%2B859lHkAMBpVGCOb65lR1L8J5RspcejIJh%2BV48zIRJ2UNbKkNagumhHtSEHIiYwYorPBsqzWd2It%2FRrszT%2BHpJBaO4Uz4CnjSPTwFzzs9vZVtr5V7TEwIhUmSlvlquPR%2Bs61gYpfWoFWHWAtC9fYWoRDCXg4S9BjqkAcsN8i%2F4tK%2FK2fhtbYRXAQ7qROHQrdPmtag9jVL%2BWc4VcWmMj7H3jbaQDPBeNuoZbGNm1A5pRri97eW8H4zA00z%2FbMPJZheUamxoRvxILl3MIz%2FelNxKK8XzMFmYIWU59wZB3kaqy3gDWNS511SBZP%2FR0PeaTen33Cjuyy1LNmlwmTjUxiZrNfPD015PCrYyuH%2Fn76eUaNwR1GHuj09yTKW8HKkY&X-Amz-Signature=7350548be115707d5c076fa8f37ce3a3bead06b8ecdeab688d9f03a8af1b9c65&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cbfaed9e-b398-4902-8936-dea058b21def/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666Y6JAHAE%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T182003Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAIaCXVzLXdlc3QtMiJIMEYCIQCQGbrTfaR7o7DhGBQE7frs%2BWUkcz6NiCOSveqq9OWgtgIhAKMMI0FUGOb%2B0y3ti6CDPmB2bph60KVEfmzMTr1Vb8I4Kv8DCBsQABoMNjM3NDIzMTgzODA1IgxSSw%2Fe6p6g5E8c0rkq3AMd%2Bgl3SVf0%2FdkWnxOPnv8NqsX%2B6X%2F3O6T4oYE%2BZB4oD1dx73iMeXBhXKtrj34UHk0VvOsZqo2Y0g9s2eqpIkhVB7qH%2BOviINoLmOXzcgoQq0mlHRWUJFHtJeFr5Dlul5qIQBbkD09HhT1Umh4jsNvbShr%2BGImL3p43xVoToJI13%2FWoCZKxneasNHvXWkUiTGxOASgCTUB4btdOfCfdIFIFpBcIjZtjM3x3iFAgjLzNCtrIWdWfd3vnXLbXtHACOc7nwT7cK4bGc%2FfGdpsbb7xKCqJkAsGBZFeqGPOIc5in2thrSm7PgKZSBoFllN3iAS0aa%2Fr8wLoNW70%2FRhmMguheJGCJrOj8PtDpZIMJv1pTrIDlvoHghBjP6Fy2ffD6LdwGskGLIwFQSnQDse8Bc539lLROVPfBJNySaccykVcIx4UXWy6u%2B%2FC424%2FX5KbHUMOcM2ZH8on1ft%2BRWlGWtxGl0uQkvQvZzD7Ans%2B859lHkAMBpVGCOb65lR1L8J5RspcejIJh%2BV48zIRJ2UNbKkNagumhHtSEHIiYwYorPBsqzWd2It%2FRrszT%2BHpJBaO4Uz4CnjSPTwFzzs9vZVtr5V7TEwIhUmSlvlquPR%2Bs61gYpfWoFWHWAtC9fYWoRDCXg4S9BjqkAcsN8i%2F4tK%2FK2fhtbYRXAQ7qROHQrdPmtag9jVL%2BWc4VcWmMj7H3jbaQDPBeNuoZbGNm1A5pRri97eW8H4zA00z%2FbMPJZheUamxoRvxILl3MIz%2FelNxKK8XzMFmYIWU59wZB3kaqy3gDWNS511SBZP%2FR0PeaTen33Cjuyy1LNmlwmTjUxiZrNfPD015PCrYyuH%2Fn76eUaNwR1GHuj09yTKW8HKkY&X-Amz-Signature=f616c441c485fc702431e4f54f634ce79a6335a68ade24fcbae5c3a1be9b7f2e&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/91181646-b1e0-4433-9711-6259a96a9247/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666Y6JAHAE%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T182003Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAIaCXVzLXdlc3QtMiJIMEYCIQCQGbrTfaR7o7DhGBQE7frs%2BWUkcz6NiCOSveqq9OWgtgIhAKMMI0FUGOb%2B0y3ti6CDPmB2bph60KVEfmzMTr1Vb8I4Kv8DCBsQABoMNjM3NDIzMTgzODA1IgxSSw%2Fe6p6g5E8c0rkq3AMd%2Bgl3SVf0%2FdkWnxOPnv8NqsX%2B6X%2F3O6T4oYE%2BZB4oD1dx73iMeXBhXKtrj34UHk0VvOsZqo2Y0g9s2eqpIkhVB7qH%2BOviINoLmOXzcgoQq0mlHRWUJFHtJeFr5Dlul5qIQBbkD09HhT1Umh4jsNvbShr%2BGImL3p43xVoToJI13%2FWoCZKxneasNHvXWkUiTGxOASgCTUB4btdOfCfdIFIFpBcIjZtjM3x3iFAgjLzNCtrIWdWfd3vnXLbXtHACOc7nwT7cK4bGc%2FfGdpsbb7xKCqJkAsGBZFeqGPOIc5in2thrSm7PgKZSBoFllN3iAS0aa%2Fr8wLoNW70%2FRhmMguheJGCJrOj8PtDpZIMJv1pTrIDlvoHghBjP6Fy2ffD6LdwGskGLIwFQSnQDse8Bc539lLROVPfBJNySaccykVcIx4UXWy6u%2B%2FC424%2FX5KbHUMOcM2ZH8on1ft%2BRWlGWtxGl0uQkvQvZzD7Ans%2B859lHkAMBpVGCOb65lR1L8J5RspcejIJh%2BV48zIRJ2UNbKkNagumhHtSEHIiYwYorPBsqzWd2It%2FRrszT%2BHpJBaO4Uz4CnjSPTwFzzs9vZVtr5V7TEwIhUmSlvlquPR%2Bs61gYpfWoFWHWAtC9fYWoRDCXg4S9BjqkAcsN8i%2F4tK%2FK2fhtbYRXAQ7qROHQrdPmtag9jVL%2BWc4VcWmMj7H3jbaQDPBeNuoZbGNm1A5pRri97eW8H4zA00z%2FbMPJZheUamxoRvxILl3MIz%2FelNxKK8XzMFmYIWU59wZB3kaqy3gDWNS511SBZP%2FR0PeaTen33Cjuyy1LNmlwmTjUxiZrNfPD015PCrYyuH%2Fn76eUaNwR1GHuj09yTKW8HKkY&X-Amz-Signature=f8784b7fc6f23ffca50a1550c90cef5ce7061daf3eaadba6607b03e0ff9c40c6&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/09aba1c0-0d55-41dd-852a-a04c5b8a3fac/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663ERAC57P%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T182005Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAIaCXVzLXdlc3QtMiJIMEYCIQCVBx%2Frg0AaiAYzYZmLZnAHQKcdZTOOSfv270cda0cRFwIhAP9wjaxl%2FHd4vKAKixnD8iaqCJU0Eu%2FKh41pp4MiMrrDKv8DCBsQABoMNjM3NDIzMTgzODA1IgxX1WglLWmnb3Fahxkq3ANzWukAUeYTz0dMxaNuTEPYN8faL%2B1VxFsXEE4FXvwPnGM1WTNU80WGjbBGDGuTdZTstqeYD50VKwGaeR9GAIA9W1e%2FpCVlBs4lamgCfJxTo8%2FlyMIeOT8Ik9SDyRyh7YT83LEoq2DU46JvU8f86xz1Ef9gpkNcVrwLybIDOLC8pmxAfgkiEpmVJSVHjL4F%2B1LMuIpT4DetiVudiyE74qn5GfXMud0YCaPlmuZICWReVl1nCvMxgXCf%2BCE%2B6nh5pwk%2BjkdLcAYcHBt4ySc0BRQNt4qVSqHvho7BQ8s0WP6NSCepiCImC%2BYYI9EPJAaVb%2B3NXk0rA5SUu8RNVtoBzav1H7%2FJD5c6PeChuyMyvwBAtm61mdpaO7BQZxE5Mk%2FXpucODN8pie8BGBg0TLPUw98kVuK2BzRQU9Kcb7iMhZRIIze6lRHCBpWIKdOiXU3ujnaXUQPYtFzxr1EQnSUEgoybpoYFnmRzj%2F7CvGHa2zOJQy6pBX0SNANpwRoLj%2BP0dYYcev7igzJVD9Bch9%2Bi2UWtIK%2Fhf9S33nv31LpCc3J3mY9NWNW2E2KMVsT75HqaN9msi%2FwWllyJGh%2B7sthD6JxVmDLaFIKGp9B%2B6Kz5jouWjCd%2F1lgYOl13OwstmDCrg4S9BjqkATesBGFe96ieOXWi8nJSdEmiqWS3%2FuGdCiY9k62Hq66Y7pR0Q%2B06J5bncFsRFA66w1wWhInay%2B3lUUN4Jbwy1pGX1NTTTXGgPCVGsheMjoIn989L5pJgx%2FL%2FUQP0tpmqKBYRPHC6JOcq38W3wTol1%2FzWtEs1PUbsEYKjjAsbIs2cKOspF3voip0QtmJwivENupCez7iBBuJYq92s2o49ajTATcpQ&X-Amz-Signature=7f4719e5d2f874fe115c43f7e3feb0141ce8b6cf886f29134c2143e291a9d34a&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 2. Scatter Plot
Scatter plots present the relationship between two variables in a dataset. It represents data points on a two-dimensional plane. The independent variable or attribute is plotted on the X-axis, while the dependent variable is plotted on the Y-axis.
**Syntax:**
```python
plt.scatter(x, y)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23708af9-659f-4f23-b626-1a4292d7842c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663ERAC57P%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T182005Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAIaCXVzLXdlc3QtMiJIMEYCIQCVBx%2Frg0AaiAYzYZmLZnAHQKcdZTOOSfv270cda0cRFwIhAP9wjaxl%2FHd4vKAKixnD8iaqCJU0Eu%2FKh41pp4MiMrrDKv8DCBsQABoMNjM3NDIzMTgzODA1IgxX1WglLWmnb3Fahxkq3ANzWukAUeYTz0dMxaNuTEPYN8faL%2B1VxFsXEE4FXvwPnGM1WTNU80WGjbBGDGuTdZTstqeYD50VKwGaeR9GAIA9W1e%2FpCVlBs4lamgCfJxTo8%2FlyMIeOT8Ik9SDyRyh7YT83LEoq2DU46JvU8f86xz1Ef9gpkNcVrwLybIDOLC8pmxAfgkiEpmVJSVHjL4F%2B1LMuIpT4DetiVudiyE74qn5GfXMud0YCaPlmuZICWReVl1nCvMxgXCf%2BCE%2B6nh5pwk%2BjkdLcAYcHBt4ySc0BRQNt4qVSqHvho7BQ8s0WP6NSCepiCImC%2BYYI9EPJAaVb%2B3NXk0rA5SUu8RNVtoBzav1H7%2FJD5c6PeChuyMyvwBAtm61mdpaO7BQZxE5Mk%2FXpucODN8pie8BGBg0TLPUw98kVuK2BzRQU9Kcb7iMhZRIIze6lRHCBpWIKdOiXU3ujnaXUQPYtFzxr1EQnSUEgoybpoYFnmRzj%2F7CvGHa2zOJQy6pBX0SNANpwRoLj%2BP0dYYcev7igzJVD9Bch9%2Bi2UWtIK%2Fhf9S33nv31LpCc3J3mY9NWNW2E2KMVsT75HqaN9msi%2FwWllyJGh%2B7sthD6JxVmDLaFIKGp9B%2B6Kz5jouWjCd%2F1lgYOl13OwstmDCrg4S9BjqkATesBGFe96ieOXWi8nJSdEmiqWS3%2FuGdCiY9k62Hq66Y7pR0Q%2B06J5bncFsRFA66w1wWhInay%2B3lUUN4Jbwy1pGX1NTTTXGgPCVGsheMjoIn989L5pJgx%2FL%2FUQP0tpmqKBYRPHC6JOcq38W3wTol1%2FzWtEs1PUbsEYKjjAsbIs2cKOspF3voip0QtmJwivENupCez7iBBuJYq92s2o49ajTATcpQ&X-Amz-Signature=3115c6540477c03ad6c1e7c1b4b023a2539d1587d06dae38c85016e254686a27&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 3. Histogram
A histogram is an important visual representation of data in categorical form. To view the data in a "Binned" form, use the histogram plot with a number of bins required or with the data points that mark the bin edges. The x-axis represents the data bins, and the y-axis represents the number of elements in each bin.
**Syntax:**
```python
plt.hist(x, bins)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/24e4424a-df87-40a1-b63b-195cbdc2e0ab/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663ERAC57P%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T182005Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAIaCXVzLXdlc3QtMiJIMEYCIQCVBx%2Frg0AaiAYzYZmLZnAHQKcdZTOOSfv270cda0cRFwIhAP9wjaxl%2FHd4vKAKixnD8iaqCJU0Eu%2FKh41pp4MiMrrDKv8DCBsQABoMNjM3NDIzMTgzODA1IgxX1WglLWmnb3Fahxkq3ANzWukAUeYTz0dMxaNuTEPYN8faL%2B1VxFsXEE4FXvwPnGM1WTNU80WGjbBGDGuTdZTstqeYD50VKwGaeR9GAIA9W1e%2FpCVlBs4lamgCfJxTo8%2FlyMIeOT8Ik9SDyRyh7YT83LEoq2DU46JvU8f86xz1Ef9gpkNcVrwLybIDOLC8pmxAfgkiEpmVJSVHjL4F%2B1LMuIpT4DetiVudiyE74qn5GfXMud0YCaPlmuZICWReVl1nCvMxgXCf%2BCE%2B6nh5pwk%2BjkdLcAYcHBt4ySc0BRQNt4qVSqHvho7BQ8s0WP6NSCepiCImC%2BYYI9EPJAaVb%2B3NXk0rA5SUu8RNVtoBzav1H7%2FJD5c6PeChuyMyvwBAtm61mdpaO7BQZxE5Mk%2FXpucODN8pie8BGBg0TLPUw98kVuK2BzRQU9Kcb7iMhZRIIze6lRHCBpWIKdOiXU3ujnaXUQPYtFzxr1EQnSUEgoybpoYFnmRzj%2F7CvGHa2zOJQy6pBX0SNANpwRoLj%2BP0dYYcev7igzJVD9Bch9%2Bi2UWtIK%2Fhf9S33nv31LpCc3J3mY9NWNW2E2KMVsT75HqaN9msi%2FwWllyJGh%2B7sthD6JxVmDLaFIKGp9B%2B6Kz5jouWjCd%2F1lgYOl13OwstmDCrg4S9BjqkATesBGFe96ieOXWi8nJSdEmiqWS3%2FuGdCiY9k62Hq66Y7pR0Q%2B06J5bncFsRFA66w1wWhInay%2B3lUUN4Jbwy1pGX1NTTTXGgPCVGsheMjoIn989L5pJgx%2FL%2FUQP0tpmqKBYRPHC6JOcq38W3wTol1%2FzWtEs1PUbsEYKjjAsbIs2cKOspF3voip0QtmJwivENupCez7iBBuJYq92s2o49ajTATcpQ&X-Amz-Signature=b4fcdffa59bb1f4ad3857b29c6f4f5c60b7e9ba882598c5691e5353086650722&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ab5a6dfe-51f5-43ee-bcb3-33dae4a1c7ad/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663ERAC57P%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T182005Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAIaCXVzLXdlc3QtMiJIMEYCIQCVBx%2Frg0AaiAYzYZmLZnAHQKcdZTOOSfv270cda0cRFwIhAP9wjaxl%2FHd4vKAKixnD8iaqCJU0Eu%2FKh41pp4MiMrrDKv8DCBsQABoMNjM3NDIzMTgzODA1IgxX1WglLWmnb3Fahxkq3ANzWukAUeYTz0dMxaNuTEPYN8faL%2B1VxFsXEE4FXvwPnGM1WTNU80WGjbBGDGuTdZTstqeYD50VKwGaeR9GAIA9W1e%2FpCVlBs4lamgCfJxTo8%2FlyMIeOT8Ik9SDyRyh7YT83LEoq2DU46JvU8f86xz1Ef9gpkNcVrwLybIDOLC8pmxAfgkiEpmVJSVHjL4F%2B1LMuIpT4DetiVudiyE74qn5GfXMud0YCaPlmuZICWReVl1nCvMxgXCf%2BCE%2B6nh5pwk%2BjkdLcAYcHBt4ySc0BRQNt4qVSqHvho7BQ8s0WP6NSCepiCImC%2BYYI9EPJAaVb%2B3NXk0rA5SUu8RNVtoBzav1H7%2FJD5c6PeChuyMyvwBAtm61mdpaO7BQZxE5Mk%2FXpucODN8pie8BGBg0TLPUw98kVuK2BzRQU9Kcb7iMhZRIIze6lRHCBpWIKdOiXU3ujnaXUQPYtFzxr1EQnSUEgoybpoYFnmRzj%2F7CvGHa2zOJQy6pBX0SNANpwRoLj%2BP0dYYcev7igzJVD9Bch9%2Bi2UWtIK%2Fhf9S33nv31LpCc3J3mY9NWNW2E2KMVsT75HqaN9msi%2FwWllyJGh%2B7sthD6JxVmDLaFIKGp9B%2B6Kz5jouWjCd%2F1lgYOl13OwstmDCrg4S9BjqkATesBGFe96ieOXWi8nJSdEmiqWS3%2FuGdCiY9k62Hq66Y7pR0Q%2B06J5bncFsRFA66w1wWhInay%2B3lUUN4Jbwy1pGX1NTTTXGgPCVGsheMjoIn989L5pJgx%2FL%2FUQP0tpmqKBYRPHC6JOcq38W3wTol1%2FzWtEs1PUbsEYKjjAsbIs2cKOspF3voip0QtmJwivENupCez7iBBuJYq92s2o49ajTATcpQ&X-Amz-Signature=e6d263badf9db1281c7afac536b2f6de1f0040a9af52e5c6e45eda557da093d3&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8f1b1d60-cf1b-42b3-9faa-f634c89c3f84/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663ERAC57P%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T182005Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAIaCXVzLXdlc3QtMiJIMEYCIQCVBx%2Frg0AaiAYzYZmLZnAHQKcdZTOOSfv270cda0cRFwIhAP9wjaxl%2FHd4vKAKixnD8iaqCJU0Eu%2FKh41pp4MiMrrDKv8DCBsQABoMNjM3NDIzMTgzODA1IgxX1WglLWmnb3Fahxkq3ANzWukAUeYTz0dMxaNuTEPYN8faL%2B1VxFsXEE4FXvwPnGM1WTNU80WGjbBGDGuTdZTstqeYD50VKwGaeR9GAIA9W1e%2FpCVlBs4lamgCfJxTo8%2FlyMIeOT8Ik9SDyRyh7YT83LEoq2DU46JvU8f86xz1Ef9gpkNcVrwLybIDOLC8pmxAfgkiEpmVJSVHjL4F%2B1LMuIpT4DetiVudiyE74qn5GfXMud0YCaPlmuZICWReVl1nCvMxgXCf%2BCE%2B6nh5pwk%2BjkdLcAYcHBt4ySc0BRQNt4qVSqHvho7BQ8s0WP6NSCepiCImC%2BYYI9EPJAaVb%2B3NXk0rA5SUu8RNVtoBzav1H7%2FJD5c6PeChuyMyvwBAtm61mdpaO7BQZxE5Mk%2FXpucODN8pie8BGBg0TLPUw98kVuK2BzRQU9Kcb7iMhZRIIze6lRHCBpWIKdOiXU3ujnaXUQPYtFzxr1EQnSUEgoybpoYFnmRzj%2F7CvGHa2zOJQy6pBX0SNANpwRoLj%2BP0dYYcev7igzJVD9Bch9%2Bi2UWtIK%2Fhf9S33nv31LpCc3J3mY9NWNW2E2KMVsT75HqaN9msi%2FwWllyJGh%2B7sthD6JxVmDLaFIKGp9B%2B6Kz5jouWjCd%2F1lgYOl13OwstmDCrg4S9BjqkATesBGFe96ieOXWi8nJSdEmiqWS3%2FuGdCiY9k62Hq66Y7pR0Q%2B06J5bncFsRFA66w1wWhInay%2B3lUUN4Jbwy1pGX1NTTTXGgPCVGsheMjoIn989L5pJgx%2FL%2FUQP0tpmqKBYRPHC6JOcq38W3wTol1%2FzWtEs1PUbsEYKjjAsbIs2cKOspF3voip0QtmJwivENupCez7iBBuJYq92s2o49ajTATcpQ&X-Amz-Signature=250d17a9640307f92ba00ce2aeea0b10b1068e5108d43b922cf48616c55a914a&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/13ad0497-05fe-4eaa-984e-707b33e14761/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663ERAC57P%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T182005Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAIaCXVzLXdlc3QtMiJIMEYCIQCVBx%2Frg0AaiAYzYZmLZnAHQKcdZTOOSfv270cda0cRFwIhAP9wjaxl%2FHd4vKAKixnD8iaqCJU0Eu%2FKh41pp4MiMrrDKv8DCBsQABoMNjM3NDIzMTgzODA1IgxX1WglLWmnb3Fahxkq3ANzWukAUeYTz0dMxaNuTEPYN8faL%2B1VxFsXEE4FXvwPnGM1WTNU80WGjbBGDGuTdZTstqeYD50VKwGaeR9GAIA9W1e%2FpCVlBs4lamgCfJxTo8%2FlyMIeOT8Ik9SDyRyh7YT83LEoq2DU46JvU8f86xz1Ef9gpkNcVrwLybIDOLC8pmxAfgkiEpmVJSVHjL4F%2B1LMuIpT4DetiVudiyE74qn5GfXMud0YCaPlmuZICWReVl1nCvMxgXCf%2BCE%2B6nh5pwk%2BjkdLcAYcHBt4ySc0BRQNt4qVSqHvho7BQ8s0WP6NSCepiCImC%2BYYI9EPJAaVb%2B3NXk0rA5SUu8RNVtoBzav1H7%2FJD5c6PeChuyMyvwBAtm61mdpaO7BQZxE5Mk%2FXpucODN8pie8BGBg0TLPUw98kVuK2BzRQU9Kcb7iMhZRIIze6lRHCBpWIKdOiXU3ujnaXUQPYtFzxr1EQnSUEgoybpoYFnmRzj%2F7CvGHa2zOJQy6pBX0SNANpwRoLj%2BP0dYYcev7igzJVD9Bch9%2Bi2UWtIK%2Fhf9S33nv31LpCc3J3mY9NWNW2E2KMVsT75HqaN9msi%2FwWllyJGh%2B7sthD6JxVmDLaFIKGp9B%2B6Kz5jouWjCd%2F1lgYOl13OwstmDCrg4S9BjqkATesBGFe96ieOXWi8nJSdEmiqWS3%2FuGdCiY9k62Hq66Y7pR0Q%2B06J5bncFsRFA66w1wWhInay%2B3lUUN4Jbwy1pGX1NTTTXGgPCVGsheMjoIn989L5pJgx%2FL%2FUQP0tpmqKBYRPHC6JOcq38W3wTol1%2FzWtEs1PUbsEYKjjAsbIs2cKOspF3voip0QtmJwivENupCez7iBBuJYq92s2o49ajTATcpQ&X-Amz-Signature=6f67e1289b7d88179cc9e3bb1dcc6ffdf2981efe041573e835678b59b484a45a&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 2. Box and Whisker Plot
A box plot shows the distribution of quantitative data in a way that facilitates comparisons between variables or across levels of a categorical variable. The box shows the quartiles of the dataset while the whiskers extend to show the rest of the distribution, except for points that are determined to be "outliers".
**Syntax:**
```python
sns.boxplot(x='header_1', y='header_2', data=df)
```
**Example Output:**


![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d207ae92-0a7c-4e2f-aa65-0ee5a2c33bf7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46623ZLY2QG%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T182006Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAIaCXVzLXdlc3QtMiJGMEQCIDdbD%2Fv%2B4DO0%2BoA%2B2LxnOD6JD9dRFfTRrR0TnQBzxx8MAiAWnNfn6Ja%2FpxM8d8jUlE66dBgBsseK98z2q6emRjaRLyr%2FAwgbEAAaDDYzNzQyMzE4MzgwNSIMSANikALxiS1oghIJKtwD%2BsZsm74mFWZtku7FgGs%2BYlwdmWHiVDbl8mocdOAYW4wZJUIERhTEsRB%2FogOiY%2FU7Gol7BEbrEqEeNgM59nCMFhAoNk2DOJDCfGObVRyfHlZ3jTGljp4dPy%2FLSA%2BaHGiMKsYL66IGuVcB2r%2B16e3%2FRCG%2FPFKNV11PBt20r0kALtKao5OqWo%2B6S8bj3elgaheIbCnY0nR70ZFi5owysUu2FVUweeXb5Q28U65eWynChsTMpcB%2FFGQRJOnCBqWCAjDZ%2BipP4BiCGKwhnYKmhAnkmqFMKZNX%2B7w9RuQFJ4BLRXS49XV8%2FCSM2RqXnW9IRebg9rKYqROjx8l4HmYZjSBELjEQcYrw5W%2FauLUamm0yj36U4jC8xL3FWK6ZyPqoKHfgDuZs4S39Qzpy4LkRdsd9TCQTuQMNfXd0qrT9aZ%2BTVMPfrtkDilIuJ80kqIQ8gE3PpeiwgPnnUnDCJ5srXaE05hi%2Bwx7we%2FbSeFEtfoTqwaVmDaB%2Fe0ZywPqHac7JrJD1pGJA0kaXGp2FrUIFfuxWgj2LBpPjdyun34mUwqobUuVILEiK7ep3%2BmkbPuJh7Lzsb%2BMWNb4fhz%2BEXoPP%2FKwavyPctErqgG1hldP97DRyZfkbwmZpiD7vp3PTG24w4oOEvQY6pgHX2OSLh1ngSPX4XnDe2S6%2FGlnDq67PPA17Tb14yzsZF9LJjHCHnS2uYWoz9uhTszaLdvHvBtDqokp8791SKE74qNGqkSofvmVNXmF6PrJLAR%2FS%2B3BmvB8q3NSfc3K5BnKjlLOfmh1FedjTpjCHUHOEbY6TMMPaFLojKIdSfeUlGrZYUN89bJ0GhY7Dm2cbMh%2FH3pdXy2eaPjm4rw5f55739wsQG7D1&X-Amz-Signature=3a421b6f2ead157edac4bbe5dd7f700541eba0c698d8fbc8fb4585f02f71a097&X-Amz-SignedHeaders=host&x-id=GetObject)

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0e516edc-7551-4792-ab18-0494db3c4c0c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZCTRKHPR%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T182006Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAIaCXVzLXdlc3QtMiJIMEYCIQD7ALbP1puKdBWDK%2BPpVfraRiEvZkglLnkL3vevZnNNMQIhAP3sQs4tGkIfyqH3CJA6scs2p%2Bl49Pf070S1SPd2jUYSKv8DCBsQABoMNjM3NDIzMTgzODA1Igx7Ij2CoM4N1MdYkTIq3AN0nIqZTEPlopjJmMJd%2FF9NaaVsc3%2FQeNRVkUU1ZgPrzG6TOOVong40b6xXKN7LdvJf%2BJUGQVsf4BBj4WKyGzz2Gy3q327%2BfmPmllPTlaMWAmEsUIdvVWPCvK2qgXwIFsKiPfbJOx1HDEze81cez6McPAU%2FlK4Ej6h7oiF43k1nAZyRrSGuLV7cQHt1UXPasYoydRT52XQ4MSlaTRuHibZdQd3WW9AZ4iraD3ZxQ9S%2F%2F2%2FU9hOEuwS63XKRt2R0LEPthWMye5k4X7oZkNNdASS1a3Ln9rJuAgjdHIzsmaxpcxoI4vhBABsu4eX4I8UF8TyrElSuPGYiriOO6UcTP9JCSTSXi5dTDPlWlQ5itzSmqOz0dmlZU61KwJKLjS0u9hPMIfRSRG9a0XGAHKdU%2FuTZfOZBkRZKDW9rhpKxyVRN%2FG7OlPgBKY3cDjgFp2aQxzZKDLnTnh7JTJvPPicevyBjBZApUqMfoH7Z5wUr7o04IvRTuQetINutn3ANiJoWj1iHtpbDO1nsCzgY7NPDE2PXFbNsyUHA6KjfgKom0Z7%2Fd%2B%2B3tdEZ3u10NW9Tc18AtuSnh%2BbvtHQ7Bt189PbmtVArwIufnHiJ6Npre8BoRR8KQdDWiKwIPq6c1S2AUzD6g4S9BjqkAYwFvswopEFuNgr9TZKaQoUJ4ZvVPCGDWo0eviWIO1lajPlcyQSnjYktOQHQ0chmTQpky7fVcqmuPJfSA8OtAVosTepbz1p%2F3e94BY1BMeaTmcl%2FrUPo%2FhqEME%2BlPouM8AnZ3N3IEAxAS6lw6WdbunL2IDtCdo%2FhrGYqFxmzZn7mQ6bRzZgSRQwtdRvEvrAFsiFJmFIlP7VPjx0K40NKoG8mnmZK&X-Amz-Signature=e40239c1dab91878ab8bf0a3ec4b8864aefd2be02bcb521fcbd9388144f6d66c&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23a79b9d-2356-49a9-8fd9-65c6b0ab2cc5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663ERAC57P%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T182005Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAIaCXVzLXdlc3QtMiJIMEYCIQCVBx%2Frg0AaiAYzYZmLZnAHQKcdZTOOSfv270cda0cRFwIhAP9wjaxl%2FHd4vKAKixnD8iaqCJU0Eu%2FKh41pp4MiMrrDKv8DCBsQABoMNjM3NDIzMTgzODA1IgxX1WglLWmnb3Fahxkq3ANzWukAUeYTz0dMxaNuTEPYN8faL%2B1VxFsXEE4FXvwPnGM1WTNU80WGjbBGDGuTdZTstqeYD50VKwGaeR9GAIA9W1e%2FpCVlBs4lamgCfJxTo8%2FlyMIeOT8Ik9SDyRyh7YT83LEoq2DU46JvU8f86xz1Ef9gpkNcVrwLybIDOLC8pmxAfgkiEpmVJSVHjL4F%2B1LMuIpT4DetiVudiyE74qn5GfXMud0YCaPlmuZICWReVl1nCvMxgXCf%2BCE%2B6nh5pwk%2BjkdLcAYcHBt4ySc0BRQNt4qVSqHvho7BQ8s0WP6NSCepiCImC%2BYYI9EPJAaVb%2B3NXk0rA5SUu8RNVtoBzav1H7%2FJD5c6PeChuyMyvwBAtm61mdpaO7BQZxE5Mk%2FXpucODN8pie8BGBg0TLPUw98kVuK2BzRQU9Kcb7iMhZRIIze6lRHCBpWIKdOiXU3ujnaXUQPYtFzxr1EQnSUEgoybpoYFnmRzj%2F7CvGHa2zOJQy6pBX0SNANpwRoLj%2BP0dYYcev7igzJVD9Bch9%2Bi2UWtIK%2Fhf9S33nv31LpCc3J3mY9NWNW2E2KMVsT75HqaN9msi%2FwWllyJGh%2B7sthD6JxVmDLaFIKGp9B%2B6Kz5jouWjCd%2F1lgYOl13OwstmDCrg4S9BjqkATesBGFe96ieOXWi8nJSdEmiqWS3%2FuGdCiY9k62Hq66Y7pR0Q%2B06J5bncFsRFA66w1wWhInay%2B3lUUN4Jbwy1pGX1NTTTXGgPCVGsheMjoIn989L5pJgx%2FL%2FUQP0tpmqKBYRPHC6JOcq38W3wTol1%2FzWtEs1PUbsEYKjjAsbIs2cKOspF3voip0QtmJwivENupCez7iBBuJYq92s2o49ajTATcpQ&X-Amz-Signature=d91dc7a78b40ae6f632919ac7398b1bed911833c9657ca6c533cd0fa36660acc&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 4. KDE Plot
A Kernel Density Estimate (KDE) plot is a graph that creates a probability distribution curve for the data based upon its likelihood of occurrence on a specific value. This is created for a single vector of information.
**Syntax:**
```python
sns.kdeplot(X) || sns.kdeplot(df['age'])
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0d571213-2a2f-4921-a50b-880847aa05ee/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663ERAC57P%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T182005Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAIaCXVzLXdlc3QtMiJIMEYCIQCVBx%2Frg0AaiAYzYZmLZnAHQKcdZTOOSfv270cda0cRFwIhAP9wjaxl%2FHd4vKAKixnD8iaqCJU0Eu%2FKh41pp4MiMrrDKv8DCBsQABoMNjM3NDIzMTgzODA1IgxX1WglLWmnb3Fahxkq3ANzWukAUeYTz0dMxaNuTEPYN8faL%2B1VxFsXEE4FXvwPnGM1WTNU80WGjbBGDGuTdZTstqeYD50VKwGaeR9GAIA9W1e%2FpCVlBs4lamgCfJxTo8%2FlyMIeOT8Ik9SDyRyh7YT83LEoq2DU46JvU8f86xz1Ef9gpkNcVrwLybIDOLC8pmxAfgkiEpmVJSVHjL4F%2B1LMuIpT4DetiVudiyE74qn5GfXMud0YCaPlmuZICWReVl1nCvMxgXCf%2BCE%2B6nh5pwk%2BjkdLcAYcHBt4ySc0BRQNt4qVSqHvho7BQ8s0WP6NSCepiCImC%2BYYI9EPJAaVb%2B3NXk0rA5SUu8RNVtoBzav1H7%2FJD5c6PeChuyMyvwBAtm61mdpaO7BQZxE5Mk%2FXpucODN8pie8BGBg0TLPUw98kVuK2BzRQU9Kcb7iMhZRIIze6lRHCBpWIKdOiXU3ujnaXUQPYtFzxr1EQnSUEgoybpoYFnmRzj%2F7CvGHa2zOJQy6pBX0SNANpwRoLj%2BP0dYYcev7igzJVD9Bch9%2Bi2UWtIK%2Fhf9S33nv31LpCc3J3mY9NWNW2E2KMVsT75HqaN9msi%2FwWllyJGh%2B7sthD6JxVmDLaFIKGp9B%2B6Kz5jouWjCd%2F1lgYOl13OwstmDCrg4S9BjqkATesBGFe96ieOXWi8nJSdEmiqWS3%2FuGdCiY9k62Hq66Y7pR0Q%2B06J5bncFsRFA66w1wWhInay%2B3lUUN4Jbwy1pGX1NTTTXGgPCVGsheMjoIn989L5pJgx%2FL%2FUQP0tpmqKBYRPHC6JOcq38W3wTol1%2FzWtEs1PUbsEYKjjAsbIs2cKOspF3voip0QtmJwivENupCez7iBBuJYq92s2o49ajTATcpQ&X-Amz-Signature=2ff11dd3441cd174ae69417bcf3af81510f8635682e08a94fd2028cb617cd774&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/53752550-ef82-4ca9-a01a-09921f0282d0/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663ERAC57P%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T182005Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAIaCXVzLXdlc3QtMiJIMEYCIQCVBx%2Frg0AaiAYzYZmLZnAHQKcdZTOOSfv270cda0cRFwIhAP9wjaxl%2FHd4vKAKixnD8iaqCJU0Eu%2FKh41pp4MiMrrDKv8DCBsQABoMNjM3NDIzMTgzODA1IgxX1WglLWmnb3Fahxkq3ANzWukAUeYTz0dMxaNuTEPYN8faL%2B1VxFsXEE4FXvwPnGM1WTNU80WGjbBGDGuTdZTstqeYD50VKwGaeR9GAIA9W1e%2FpCVlBs4lamgCfJxTo8%2FlyMIeOT8Ik9SDyRyh7YT83LEoq2DU46JvU8f86xz1Ef9gpkNcVrwLybIDOLC8pmxAfgkiEpmVJSVHjL4F%2B1LMuIpT4DetiVudiyE74qn5GfXMud0YCaPlmuZICWReVl1nCvMxgXCf%2BCE%2B6nh5pwk%2BjkdLcAYcHBt4ySc0BRQNt4qVSqHvho7BQ8s0WP6NSCepiCImC%2BYYI9EPJAaVb%2B3NXk0rA5SUu8RNVtoBzav1H7%2FJD5c6PeChuyMyvwBAtm61mdpaO7BQZxE5Mk%2FXpucODN8pie8BGBg0TLPUw98kVuK2BzRQU9Kcb7iMhZRIIze6lRHCBpWIKdOiXU3ujnaXUQPYtFzxr1EQnSUEgoybpoYFnmRzj%2F7CvGHa2zOJQy6pBX0SNANpwRoLj%2BP0dYYcev7igzJVD9Bch9%2Bi2UWtIK%2Fhf9S33nv31LpCc3J3mY9NWNW2E2KMVsT75HqaN9msi%2FwWllyJGh%2B7sthD6JxVmDLaFIKGp9B%2B6Kz5jouWjCd%2F1lgYOl13OwstmDCrg4S9BjqkATesBGFe96ieOXWi8nJSdEmiqWS3%2FuGdCiY9k62Hq66Y7pR0Q%2B06J5bncFsRFA66w1wWhInay%2B3lUUN4Jbwy1pGX1NTTTXGgPCVGsheMjoIn989L5pJgx%2FL%2FUQP0tpmqKBYRPHC6JOcq38W3wTol1%2FzWtEs1PUbsEYKjjAsbIs2cKOspF3voip0QtmJwivENupCez7iBBuJYq92s2o49ajTATcpQ&X-Amz-Signature=969950dc5addd58aa19cc68a49b7379ae257d6f3150316ed0479e0d39d42dcba&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
## 4. Correlation Between Variables
Correlation is a statistical measure of the extent to which different variables are interdependent. It indicates how changes in one variable are associated with changes in another variable over time.
### Positive Correlation
Positive correlation indicates that as one variable increases, the other variable also tends to increase.
**Example: Engine Size and Price**
- **Positive Correlation:** Engine size increases, price also increases.
- **Visualization:** Scatter plot with a steep positive slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c7ea9b0-3ef3-4357-a9c3-554fc71b6b15/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XRU7ZOSN%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T182006Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAIaCXVzLXdlc3QtMiJGMEQCIBS%2FG6XnQWVHz2AAmHsloLGqx8GVF7FMcp%2Bm5WawiszZAiB0074Ae9iH6x58HhP%2B0Pu3nVg0speyA7XIY3Rr0oYHmCr%2FAwgbEAAaDDYzNzQyMzE4MzgwNSIMtdLiN9a%2Brv%2Bz1YrgKtwDKz5Wsq9%2Btu6vMYRzzNKT080T78LG9o4KMV6SWQjkapcJjdhn%2Fa%2B9ikJj%2FBd3C99PM68V59icfhJUaHjardfV5cnhvvqop8YVUGlb47A%2BS7mnSqOc4g96plWvEnwsySyPBCLtoqtJcG2DdzyU3ql9DacvuFmOo3iGPzYPPGgWLPqfrmwxjKBvjP7S0ary56RztAp4AdARXrjAWQAhAI9hv9ThA0oqjwO91L8KpDo%2Bqh0IhhD0b%2B4Kjs8fwQHnM42sdDF6WM3CHAA3FJudUYCeBzZO%2BWUBDvf6rmVmuWpsSBRjDdBs1eFZB6ho45NY2DvNuIs3a6zmLc5p4UZwHMrDw2F7sJZMCdbXPdGcPbIoX1oDPjiNKS%2BvLS4tK0WMjnfaJIcJxvUk1hs0smCpGzRbdDNbJU7AhYBvxdMPz96A2HrR2tTFfPUv3RW8wsyeeYTFB9x0G2zMAOhix7UL05dGtU8hbdr4b7gK%2BHHlZ9Lqs1WVSIqqMAGUWtF9LijgT4QrprKvR2XtBxnG7cOxZmrqY9gxPs8ntpbVp%2BmcJsHeXFkswwsqSshr%2FXoczlL2bLx8JhJj83sjp6l%2F6Zk44KXeRGzGrHym2EMbyp4o8C48bmGmXewrb5HNbGrVDqcw3YOEvQY6pgHtfXPapuOec1E8n4q2yYhPBbMB26X7dzUB8tgzNyjqpxtV2%2BTAxfUha%2F5sp2Lnc%2Bv41m%2BD%2F0yiHHa44yuj3PBt6EdaeJfxRGMrgNCgGuPiAeteJw6p%2BXoP1jZrZ7FS9IqliTWDZAaSaceRR6EY%2FoKgppongtVcUi8xrLP3LZlA37XbrFYYmuEb7fvbea%2FTGZGmpvxS3FalKnRqNjMnvkH8Uio9TTcR&X-Amz-Signature=e63fe56eccb9ffb8d33ca1e1ec19ef0f475549897631313980ce09c6113c17ad&X-Amz-SignedHeaders=host&x-id=GetObject)
**Explanation:** When engine size increases, there is a corresponding increase in the price of the vehicle. This positive correlation suggests that larger engines tend to be associated with higher prices in the market.
___
### Negative Correlation
Negative correlation indicates that as one variable increases, the other variable tends to decrease.
**Example: Highway Miles per Gallon and Price**
- **Negative Correlation:** As highway miles per gallon increases, price decreases.
- **Visualization:** Scatter plot with a steep negative slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/10f1f798-9cc4-4df2-a9c1-5a339f554a0b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SOVHUMAQ%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T182006Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAIaCXVzLXdlc3QtMiJIMEYCIQDvuPqeHNjrbau%2FA4b9GxEJodkvAXbTw2iJ%2BrPynFRpDAIhAIQX8lq%2BNn2OTI0b5uSprmFKtarifjkArTAS16i7eymQKv8DCBsQABoMNjM3NDIzMTgzODA1IgxpW8IzWp3ZQozgQ1Iq3ANCRtsyRJ0k4vHe1NmrttAG1UgsrLs8aS%2FVcK8dG5oSAnFoMchqWOWTSmU%2FsOWtJ55ydZkDTaId0bYJ8eZ7xc7Lq0A%2FrLEdjiZkSvemGQk%2FvsSozNPNvLKiHXQDHxC2p7E4M%2BKB5wDHEgRwDkumLspaU2mZeT0UqnjOR24c7DJOTNo1HABYQcwOWHHYEj3gTLjmcZ6b%2BcPHQSk7Jd5Ay1jP1il3eEb6IANj4sGrDR%2FhdOBZkdCaZd3SREVXix6JumB1GmXvVxHvVyTkEnxMTjGxVHrHVZz2XdwwaCC6eaukyGX2M8%2FogKg6%2FBirFdjOPbFEHNT0a9i8g1tZgmSnDRkMuXp6a7gu2IHGYgO7W9XEypQBSR2v3f%2FuAA85Vo05LqSEhcxxkjOaXc3RyVX0yUu8%2F6zORUeVToupACnf9oimtdGT3X14Zx9bWwLj43jcp3MuJraUUd9hfkayJtbwzgDc10VhUfFQKRJW0kBn%2BDPB2tx0nl7O%2Br50nB%2FA%2B88MgdU76O4bjK2h6a3am%2FpH5nYz9Bb%2Fv%2FpG1JKKPxoJmUcQl0eRpWCvEGSGP4kO2UcwOkiKuPXDCBw9jg64dtJ2DScCnSt%2FtWSnh3NqV%2FuetbOdly09NV0qwocpoM9QzDD%2Bg4S9BjqkARzvVsBXSKkTLAEQKdmEw8jYyaS0qOEDJKCsF149puhk07cHCfYy5CPwLNtqVGZfNUMFkAUiH%2BatXfzemQr9yHU6R3Y4baGv20zDUnskFai6iVUkAAcY8SWWegOccdMcKKi7pHE7xBzrDWDabMzqptOdFB9R4xDF3n0%2Bw4d9sMfs9%2BpxDcUi5IMLJjQb4kKq6pBm4CgTALGIsXUfi4bJTlV1dZPK&X-Amz-Signature=bc7420c91b762b8288f16b8717fb45b16c23309a31e57be3372dfb841744014b&X-Amz-SignedHeaders=host&x-id=GetObject)
**Explanation:** When highway miles per gallon increases, the price of the vehicle tends to decrease. This negative correlation suggests that cars with higher fuel efficiency (more miles per gallon) are generally priced lower in the market.
___
### Weak Correlation
Weak correlation indicates a lack of strong relationship between the variables.
**Example: RPM and Price**
- **Weak Correlation:** Low and high RPM values show varied prices, indicating no strong predictive relationship.
- **Visualization:** Scatter plot with no clear trend or slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9f914514-8914-4bf4-ac84-d9e3077f6eb1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WIFKAZJK%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T182008Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAIaCXVzLXdlc3QtMiJHMEUCIQClKZi9YNz5KLLbEAQKa%2BKPxKBhjnfnBr06Gyub6bjhTwIgDtOmZr1s19UiMr9NGFR9VuS9RSKdxMmD33%2BlgGVdso4q%2FwMIGxAAGgw2Mzc0MjMxODM4MDUiDLvI4Ad6BSgVFoejVircA%2FvWSGg29DuJoiHw1jsM0fw80d6vCGsBTVrYkqK6Gs2o%2B4%2Ft6DmhkdItzmW7VSkudVl2wF2hxWoR6ShSPGdSGn9AOEuhjpuYpFg3I7iJn0ZjUrbS%2FrOUfXuLuXmfvh3SmVXwOmj1Ke5W%2Bmu9sxrkbAcfUHS9FLtxZPePdGtG83JkA9lOprN3QWHGyXsDPnYoxIO%2Fbs1bRsFARkFdTS4eSktCM052episwlbCuEf7JTz7y5rBC0vcOzbmrXBUR0DvTEGIaNqQ2YoLQAK%2F27YsLs0vFzifxRQ8D8BJ97fA17cuN1qaOmMSyRORHDwxK%2Bjpu42gMB9fxSlJTr3MMoHLTBxSXO0yvwnh6%2B103K2ouS2A%2FsT3Tudrzbw4Qh66U1YMuEqjPE3YOBchz%2FXGE0O0pR3ischcdBJhJantgJa0wjv9CLO%2BsF%2FQbhERukQYutBASB9zFR1u1HPJHM2EWHKVyu%2B8Hbryj72E3jIl7%2FiS%2FzLLZz0Az%2FFie5JUPaUOBYcIixd0u6Kt6W%2F51iIEfR3qtMEhOvcwXjhvW80k2OlkNn8bgO9d%2BzkNJGSD1D04d8gGQLuroWMxKn0Xfx68wqZbrZ7sKc1Z9v1Xf93X3RMarm6Jy46XqneSsuHxMVGbMNWDhL0GOqUBtDtYqkQKiQguZcMuKmLA5ZBQCnBrO5PnuxeuYTs0v9g2W%2Fxc5jiELIxmUY1%2B0APSDj5MWeoRKjMTf828XrXdENDMO%2BorzUivVVWcuT%2BwuYu61l18IyeAiSty68%2BVqtmI8fpsmPXaalIfXjwEsjWra2A9zXM2vXfyPCETqTrbsgp0Zj9Q809MRCW27CCF9EX5GugJKfsTmqqfSUmfrIiLIw%2FVmFSf&X-Amz-Signature=c05a741e140152c7058f3ceaa3150067f7f02efc350c96d3d0c4b168d7c5fba8&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f18086e5-5b04-4fbf-8309-8944ab20d213/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662G4OFMO6%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T182006Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAIaCXVzLXdlc3QtMiJGMEQCIA1dLO7JpnXtpzzCO9lOTkmzwr%2FukJspZqMZJ5M2dmI%2BAiBgH%2BOrf5qKrG7xksJ2%2BG9RkcQb9lHnsDcY9oOZxoLdJir%2FAwgbEAAaDDYzNzQyMzE4MzgwNSIMkE8gZTYgStqt7QdIKtwD%2F0KpEbihS4%2BWcD2p%2Bz5UW8X8kH7Zc%2F1L%2BNds%2BxQLWXyczc0GAze4E4tZmctYdACjh6OleyMmmUOoguhHSmVk2F0nPjlhSitkCRtBl6gDVQXa4G0yDg4jDdCuRGCvD15pRp9bSNarrcJ2DJcgGCK9ayU3rupKzK5np0%2FomFpRhnWn2ncCMTX3txu%2Fm688zOmmsCtUG4c0mBVzqYTKWXlTZ2BoU3ObmRy1uUrq2pmo5Kgy31e2%2FGRKHi6vzA0yXqMEIIXMQs4G5ED1%2BPF6FOjttfgswkLlsOuf4NYD%2Fnr1nXIpv6gKbcEb0Jauy%2BA4lD2lK4a0s4QB6kN%2FixEkzaAJqsZHN83%2F2sfGYHKq%2BCuGlq2yrP9ll%2BdBViAkBTw2%2BYFzKWlLru0f%2BLpJDQr8EADDaf9E5pskdijjHFP9s147gzqgazwjrfqW6OCJrcbiLW4naHa3nicSaZsTH3dZId46Z%2FSyIBl%2B%2BehEY6VQU5fw1FZ%2Bd%2BirjbbnYfxwjXZG%2BgCBYPi7aQJniyF4enZiJ5YV5OyggiP73FV14ABzekIzBkCHraycCSHMIEARZIzjIDeZAl%2BFly1OVXAOoRJjjrBu%2BQlCCL1FkoC1z4ygyiSnsvEdKVWY7ICFrqydsEgw4oOEvQY6pgG4LZX0qhvi1aojgLuT1h9Tlpm%2BB0ihdhPp3hoYnG24GWqPUPPo7tGziDzRAyU1ZPVg1ISm1oU%2BOvwBi9uOWc0qZFVfRhZXcNNsxudbdcD9HRCJLS1MO8cwGA%2FPa1pyAut2vUiY3aU6rB4R0XJCALapo1km99TdtjOiCFQHj9dE3fp8JAZd1mEVG41DkN7zQk%2BG0QG4cq5D0mfVkDLVJxlYtKQaf306&X-Amz-Signature=17bbb8bde11932da5884b6ea6f24bce845b022405d2029a569493c02fe3a85f1&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Correlation Plot
Heatmap visualizes correlations among variables. Color scheme indicates Pearson correlation coefficients. Dark red diagonal line shows perfect correlation (value of 1) between variables and themselves.
This heatmap offers overview of variable relationships and their link with price.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cd3b341e-cc1a-45f7-8aec-cdc00436d270/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662G4OFMO6%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T182006Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAIaCXVzLXdlc3QtMiJGMEQCIA1dLO7JpnXtpzzCO9lOTkmzwr%2FukJspZqMZJ5M2dmI%2BAiBgH%2BOrf5qKrG7xksJ2%2BG9RkcQb9lHnsDcY9oOZxoLdJir%2FAwgbEAAaDDYzNzQyMzE4MzgwNSIMkE8gZTYgStqt7QdIKtwD%2F0KpEbihS4%2BWcD2p%2Bz5UW8X8kH7Zc%2F1L%2BNds%2BxQLWXyczc0GAze4E4tZmctYdACjh6OleyMmmUOoguhHSmVk2F0nPjlhSitkCRtBl6gDVQXa4G0yDg4jDdCuRGCvD15pRp9bSNarrcJ2DJcgGCK9ayU3rupKzK5np0%2FomFpRhnWn2ncCMTX3txu%2Fm688zOmmsCtUG4c0mBVzqYTKWXlTZ2BoU3ObmRy1uUrq2pmo5Kgy31e2%2FGRKHi6vzA0yXqMEIIXMQs4G5ED1%2BPF6FOjttfgswkLlsOuf4NYD%2Fnr1nXIpv6gKbcEb0Jauy%2BA4lD2lK4a0s4QB6kN%2FixEkzaAJqsZHN83%2F2sfGYHKq%2BCuGlq2yrP9ll%2BdBViAkBTw2%2BYFzKWlLru0f%2BLpJDQr8EADDaf9E5pskdijjHFP9s147gzqgazwjrfqW6OCJrcbiLW4naHa3nicSaZsTH3dZId46Z%2FSyIBl%2B%2BehEY6VQU5fw1FZ%2Bd%2BirjbbnYfxwjXZG%2BgCBYPi7aQJniyF4enZiJ5YV5OyggiP73FV14ABzekIzBkCHraycCSHMIEARZIzjIDeZAl%2BFly1OVXAOoRJjjrBu%2BQlCCL1FkoC1z4ygyiSnsvEdKVWY7ICFrqydsEgw4oOEvQY6pgG4LZX0qhvi1aojgLuT1h9Tlpm%2BB0ihdhPp3hoYnG24GWqPUPPo7tGziDzRAyU1ZPVg1ISm1oU%2BOvwBi9uOWc0qZFVfRhZXcNNsxudbdcD9HRCJLS1MO8cwGA%2FPa1pyAut2vUiY3aU6rB4R0XJCALapo1km99TdtjOiCFQHj9dE3fp8JAZd1mEVG41DkN7zQk%2BG0QG4cq5D0mfVkDLVJxlYtKQaf306&X-Amz-Signature=5f7c7e4a3f66e21208ab54e015383ee9aeedc9c38c077fd6d9fc3c8e1662409d&X-Amz-SignedHeaders=host&x-id=GetObject)

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
