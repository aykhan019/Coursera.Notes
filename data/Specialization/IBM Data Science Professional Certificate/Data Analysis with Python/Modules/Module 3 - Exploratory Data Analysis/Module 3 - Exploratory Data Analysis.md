

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7e6d594d-952e-44b6-97ea-31225882aea6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YFBQXEVT%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T141334Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDhIFZiDRPEVm5jtaBFtPUminZSxMfxmOIVdjotJVrHiAIhAPKfDc5lpmOlxjLKniB6tAqywHyF0R3tOrg%2Fp61hKRP1KogECI%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxcB2f2dOa31Iq3HVkq3AMoyN7Ye00bXsCECrV6wNKUdqvmo%2Bm3Z%2BoEZtN1jbPl6fm9pzeIvHkiNOKZ0X%2BkwKr%2BdY7sc%2F8TSTDAau8pEIa4zMmOUDwhvMlF8RVvDX9u8Jd4myL84KyX5SmDCvfP5hupgLEI6PkTC%2BO6fGhpi5P8Nt42qijE2MuFdfHO3yvretSpRiJiyyJFfwgiVjt4MSF%2Fk4Lre573dTqJ6tIMLrGrC9pzuMwUb%2BoV0mNUju3EA%2BLRUMuAdjL5G6lQ0uJQVZe8fSezzUkedQFPnoSZ48N%2F10jLiGauRrDyEXYeNsDpfTVYTUTath%2FTlW44HthIHkMnpXDqvSEzYE9Vsc7uuUvF6aBW%2Fn5gKcjfVGPaXXFc4H28YEbLC67OjyYYwdMfyzMXuiGkxHLCmOJDTG3npK5cztn%2Bi7C%2BjludUyNih%2BDhFC5MCXRQ%2BesuerSWjfOHuBhKRfQO96FbXitdOsLjLLXEeigV18xznS%2F%2B3hJdloXit6wNlA%2FHLCa5jwdORxjk7EFvDFDkCMx92Ga0tvDt%2FeTOH2KigBQ2d7Q2CItOhyZIU4BpYoDT39ge1b0lcB7Im171SexcP4KezQtiofXn%2By9f2N5cVoL84avS5I2IJWcQC3Ld5tK%2BVo1tbCN12DDq5ui8BjqkAYEuN%2FQlmArWYhsdy5JSmYeUZyk3RI1TMUiFA9wkzPkacd78427RYRCpggvELeBqKIE5KCPn3jHmP7LB3yntbxMlxErbQQh%2BUvhq1gJDg%2F1BoowfydgjAF1%2B1lfZDEFBwsxy3uNLPSHjeSFWO1h0aTKXIcALDWtbUeLZ9uzmhveJKvO9rB%2FW8LQm1uNmuMelEcvZxlZrAlxRLbDddMQ1DqTlTr3N&X-Amz-Signature=109f7c0535c8761cb9be841f3904748dc686c33f247bd26c531c6313c9eaf189&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cbfaed9e-b398-4902-8936-dea058b21def/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YFBQXEVT%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T141334Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDhIFZiDRPEVm5jtaBFtPUminZSxMfxmOIVdjotJVrHiAIhAPKfDc5lpmOlxjLKniB6tAqywHyF0R3tOrg%2Fp61hKRP1KogECI%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxcB2f2dOa31Iq3HVkq3AMoyN7Ye00bXsCECrV6wNKUdqvmo%2Bm3Z%2BoEZtN1jbPl6fm9pzeIvHkiNOKZ0X%2BkwKr%2BdY7sc%2F8TSTDAau8pEIa4zMmOUDwhvMlF8RVvDX9u8Jd4myL84KyX5SmDCvfP5hupgLEI6PkTC%2BO6fGhpi5P8Nt42qijE2MuFdfHO3yvretSpRiJiyyJFfwgiVjt4MSF%2Fk4Lre573dTqJ6tIMLrGrC9pzuMwUb%2BoV0mNUju3EA%2BLRUMuAdjL5G6lQ0uJQVZe8fSezzUkedQFPnoSZ48N%2F10jLiGauRrDyEXYeNsDpfTVYTUTath%2FTlW44HthIHkMnpXDqvSEzYE9Vsc7uuUvF6aBW%2Fn5gKcjfVGPaXXFc4H28YEbLC67OjyYYwdMfyzMXuiGkxHLCmOJDTG3npK5cztn%2Bi7C%2BjludUyNih%2BDhFC5MCXRQ%2BesuerSWjfOHuBhKRfQO96FbXitdOsLjLLXEeigV18xznS%2F%2B3hJdloXit6wNlA%2FHLCa5jwdORxjk7EFvDFDkCMx92Ga0tvDt%2FeTOH2KigBQ2d7Q2CItOhyZIU4BpYoDT39ge1b0lcB7Im171SexcP4KezQtiofXn%2By9f2N5cVoL84avS5I2IJWcQC3Ld5tK%2BVo1tbCN12DDq5ui8BjqkAYEuN%2FQlmArWYhsdy5JSmYeUZyk3RI1TMUiFA9wkzPkacd78427RYRCpggvELeBqKIE5KCPn3jHmP7LB3yntbxMlxErbQQh%2BUvhq1gJDg%2F1BoowfydgjAF1%2B1lfZDEFBwsxy3uNLPSHjeSFWO1h0aTKXIcALDWtbUeLZ9uzmhveJKvO9rB%2FW8LQm1uNmuMelEcvZxlZrAlxRLbDddMQ1DqTlTr3N&X-Amz-Signature=6b6b15ce0095f868a4b649b0ca5e3027b32121eac16d70d02a34303fd0dd68b2&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/91181646-b1e0-4433-9711-6259a96a9247/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YFBQXEVT%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T141334Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDhIFZiDRPEVm5jtaBFtPUminZSxMfxmOIVdjotJVrHiAIhAPKfDc5lpmOlxjLKniB6tAqywHyF0R3tOrg%2Fp61hKRP1KogECI%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxcB2f2dOa31Iq3HVkq3AMoyN7Ye00bXsCECrV6wNKUdqvmo%2Bm3Z%2BoEZtN1jbPl6fm9pzeIvHkiNOKZ0X%2BkwKr%2BdY7sc%2F8TSTDAau8pEIa4zMmOUDwhvMlF8RVvDX9u8Jd4myL84KyX5SmDCvfP5hupgLEI6PkTC%2BO6fGhpi5P8Nt42qijE2MuFdfHO3yvretSpRiJiyyJFfwgiVjt4MSF%2Fk4Lre573dTqJ6tIMLrGrC9pzuMwUb%2BoV0mNUju3EA%2BLRUMuAdjL5G6lQ0uJQVZe8fSezzUkedQFPnoSZ48N%2F10jLiGauRrDyEXYeNsDpfTVYTUTath%2FTlW44HthIHkMnpXDqvSEzYE9Vsc7uuUvF6aBW%2Fn5gKcjfVGPaXXFc4H28YEbLC67OjyYYwdMfyzMXuiGkxHLCmOJDTG3npK5cztn%2Bi7C%2BjludUyNih%2BDhFC5MCXRQ%2BesuerSWjfOHuBhKRfQO96FbXitdOsLjLLXEeigV18xznS%2F%2B3hJdloXit6wNlA%2FHLCa5jwdORxjk7EFvDFDkCMx92Ga0tvDt%2FeTOH2KigBQ2d7Q2CItOhyZIU4BpYoDT39ge1b0lcB7Im171SexcP4KezQtiofXn%2By9f2N5cVoL84avS5I2IJWcQC3Ld5tK%2BVo1tbCN12DDq5ui8BjqkAYEuN%2FQlmArWYhsdy5JSmYeUZyk3RI1TMUiFA9wkzPkacd78427RYRCpggvELeBqKIE5KCPn3jHmP7LB3yntbxMlxErbQQh%2BUvhq1gJDg%2F1BoowfydgjAF1%2B1lfZDEFBwsxy3uNLPSHjeSFWO1h0aTKXIcALDWtbUeLZ9uzmhveJKvO9rB%2FW8LQm1uNmuMelEcvZxlZrAlxRLbDddMQ1DqTlTr3N&X-Amz-Signature=d680eee89e5f71af7b6b459524f7507fb61d2d45a558d457387031ca97a40948&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/09aba1c0-0d55-41dd-852a-a04c5b8a3fac/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YOIZMOUK%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T141335Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIEX7S%2BLNH2CTh5i1ofpNsGqLcU0wO9xS0%2Bjuough5AbnAiEA8qTbvf1xSvKhcIXy5uXa%2BJ28Xh53neVM59PX335GW1EqiAQIj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJQUD6FBAuP%2Bw5sJ1ircAw9Yu66MCezosXSuPb2cpGFhX7lkQoJA1CRyOdcS1zisaP5Dre%2F1NqHkhT%2Bz%2Btqkx%2Fyw0TLIVFXcsVqRSVn4w%2FPufqCoE3QprEd948a0fYFdYi69xrpWSuezJo9sCMMbUxdf729engqE8SrpGfK%2FLnq%2F2GXXAilwHO6UZRwT2hdqSQztrdRYG1fRZkkwO0uvp7gtLYumE%2B%2FoAW3%2FiWZVG1pBAmUTZDh1DjwyFn%2FlqWpbZmbFNn6zD9gwWSteYup5jExFbQZhVVk6FXzRDVAZzv%2Frlbael2GhwSCTTSiiL1sAJEBzfY2iEBrxCPmLPf%2B8RBd9Zgxq%2FTLcsoqkqzHHua2eR9%2BXq4km%2FytXGBFjosFOKqBp9CT5EDNKcu6VgQwFTYUfkI%2FdiwhHh%2BCuIc0HR3JEwATD8rR6Ez9a5j8HJPWA2xWSHQkxCAoiS6oeMvPxz%2BkSP2qPynIBDyzw8%2BZ4R0OZ69QrYxY1syXXDXIYIi5ZvtECTr3P9K9dyBz7rSLDXMU9Z%2Fib4KxY8MkRDaRaxkqJ2MDe0g%2FaIP2Y8GNinoJFvQ5kdTKmj5fjB9zvWmY0VvKARr0f9PyIG0Auwc1kyYsJn5LIxR%2BS6niCOeMUj0ypO8KaNG9HzuGdEE5fMIHn6LwGOqUBrx8nVz18DxXu0fCnmIXmSsATTT5BxbCNFh0uMnumVnlLLsFv5kgHz38JNye6dd0u%2FHsk0SbIu%2Bn%2FQsgqfUtd7P5qEDGTqSkdJphY4ZOcAvJTWcZ3%2B9%2BTSKv2fZxV7WogJ00u2w5urk8lIx1Z%2F0v49zcbtLf9cFWyiuDRlZPXM2CvTyphYwNuR1WMcGpAj8HXIX%2FV8o6pIwmYJVEJvLg7MFCjCmfi&X-Amz-Signature=1f6318490187cd66a4f9e67f4412ada83cf0938097cd078a6833302259d00bbf&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 2. Scatter Plot
Scatter plots present the relationship between two variables in a dataset. It represents data points on a two-dimensional plane. The independent variable or attribute is plotted on the X-axis, while the dependent variable is plotted on the Y-axis.
**Syntax:**
```python
plt.scatter(x, y)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23708af9-659f-4f23-b626-1a4292d7842c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YOIZMOUK%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T141335Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIEX7S%2BLNH2CTh5i1ofpNsGqLcU0wO9xS0%2Bjuough5AbnAiEA8qTbvf1xSvKhcIXy5uXa%2BJ28Xh53neVM59PX335GW1EqiAQIj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJQUD6FBAuP%2Bw5sJ1ircAw9Yu66MCezosXSuPb2cpGFhX7lkQoJA1CRyOdcS1zisaP5Dre%2F1NqHkhT%2Bz%2Btqkx%2Fyw0TLIVFXcsVqRSVn4w%2FPufqCoE3QprEd948a0fYFdYi69xrpWSuezJo9sCMMbUxdf729engqE8SrpGfK%2FLnq%2F2GXXAilwHO6UZRwT2hdqSQztrdRYG1fRZkkwO0uvp7gtLYumE%2B%2FoAW3%2FiWZVG1pBAmUTZDh1DjwyFn%2FlqWpbZmbFNn6zD9gwWSteYup5jExFbQZhVVk6FXzRDVAZzv%2Frlbael2GhwSCTTSiiL1sAJEBzfY2iEBrxCPmLPf%2B8RBd9Zgxq%2FTLcsoqkqzHHua2eR9%2BXq4km%2FytXGBFjosFOKqBp9CT5EDNKcu6VgQwFTYUfkI%2FdiwhHh%2BCuIc0HR3JEwATD8rR6Ez9a5j8HJPWA2xWSHQkxCAoiS6oeMvPxz%2BkSP2qPynIBDyzw8%2BZ4R0OZ69QrYxY1syXXDXIYIi5ZvtECTr3P9K9dyBz7rSLDXMU9Z%2Fib4KxY8MkRDaRaxkqJ2MDe0g%2FaIP2Y8GNinoJFvQ5kdTKmj5fjB9zvWmY0VvKARr0f9PyIG0Auwc1kyYsJn5LIxR%2BS6niCOeMUj0ypO8KaNG9HzuGdEE5fMIHn6LwGOqUBrx8nVz18DxXu0fCnmIXmSsATTT5BxbCNFh0uMnumVnlLLsFv5kgHz38JNye6dd0u%2FHsk0SbIu%2Bn%2FQsgqfUtd7P5qEDGTqSkdJphY4ZOcAvJTWcZ3%2B9%2BTSKv2fZxV7WogJ00u2w5urk8lIx1Z%2F0v49zcbtLf9cFWyiuDRlZPXM2CvTyphYwNuR1WMcGpAj8HXIX%2FV8o6pIwmYJVEJvLg7MFCjCmfi&X-Amz-Signature=20de80aad6e102eb5369cf7600c6492e7bba5978c91359dd8b5d29147f52edf8&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 3. Histogram
A histogram is an important visual representation of data in categorical form. To view the data in a "Binned" form, use the histogram plot with a number of bins required or with the data points that mark the bin edges. The x-axis represents the data bins, and the y-axis represents the number of elements in each bin.
**Syntax:**
```python
plt.hist(x, bins)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/24e4424a-df87-40a1-b63b-195cbdc2e0ab/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YOIZMOUK%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T141335Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIEX7S%2BLNH2CTh5i1ofpNsGqLcU0wO9xS0%2Bjuough5AbnAiEA8qTbvf1xSvKhcIXy5uXa%2BJ28Xh53neVM59PX335GW1EqiAQIj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJQUD6FBAuP%2Bw5sJ1ircAw9Yu66MCezosXSuPb2cpGFhX7lkQoJA1CRyOdcS1zisaP5Dre%2F1NqHkhT%2Bz%2Btqkx%2Fyw0TLIVFXcsVqRSVn4w%2FPufqCoE3QprEd948a0fYFdYi69xrpWSuezJo9sCMMbUxdf729engqE8SrpGfK%2FLnq%2F2GXXAilwHO6UZRwT2hdqSQztrdRYG1fRZkkwO0uvp7gtLYumE%2B%2FoAW3%2FiWZVG1pBAmUTZDh1DjwyFn%2FlqWpbZmbFNn6zD9gwWSteYup5jExFbQZhVVk6FXzRDVAZzv%2Frlbael2GhwSCTTSiiL1sAJEBzfY2iEBrxCPmLPf%2B8RBd9Zgxq%2FTLcsoqkqzHHua2eR9%2BXq4km%2FytXGBFjosFOKqBp9CT5EDNKcu6VgQwFTYUfkI%2FdiwhHh%2BCuIc0HR3JEwATD8rR6Ez9a5j8HJPWA2xWSHQkxCAoiS6oeMvPxz%2BkSP2qPynIBDyzw8%2BZ4R0OZ69QrYxY1syXXDXIYIi5ZvtECTr3P9K9dyBz7rSLDXMU9Z%2Fib4KxY8MkRDaRaxkqJ2MDe0g%2FaIP2Y8GNinoJFvQ5kdTKmj5fjB9zvWmY0VvKARr0f9PyIG0Auwc1kyYsJn5LIxR%2BS6niCOeMUj0ypO8KaNG9HzuGdEE5fMIHn6LwGOqUBrx8nVz18DxXu0fCnmIXmSsATTT5BxbCNFh0uMnumVnlLLsFv5kgHz38JNye6dd0u%2FHsk0SbIu%2Bn%2FQsgqfUtd7P5qEDGTqSkdJphY4ZOcAvJTWcZ3%2B9%2BTSKv2fZxV7WogJ00u2w5urk8lIx1Z%2F0v49zcbtLf9cFWyiuDRlZPXM2CvTyphYwNuR1WMcGpAj8HXIX%2FV8o6pIwmYJVEJvLg7MFCjCmfi&X-Amz-Signature=552bb5d06f022c645fca7bc8d48bb2babc963a979440e3aa652d8e372687a256&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ab5a6dfe-51f5-43ee-bcb3-33dae4a1c7ad/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YOIZMOUK%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T141335Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIEX7S%2BLNH2CTh5i1ofpNsGqLcU0wO9xS0%2Bjuough5AbnAiEA8qTbvf1xSvKhcIXy5uXa%2BJ28Xh53neVM59PX335GW1EqiAQIj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJQUD6FBAuP%2Bw5sJ1ircAw9Yu66MCezosXSuPb2cpGFhX7lkQoJA1CRyOdcS1zisaP5Dre%2F1NqHkhT%2Bz%2Btqkx%2Fyw0TLIVFXcsVqRSVn4w%2FPufqCoE3QprEd948a0fYFdYi69xrpWSuezJo9sCMMbUxdf729engqE8SrpGfK%2FLnq%2F2GXXAilwHO6UZRwT2hdqSQztrdRYG1fRZkkwO0uvp7gtLYumE%2B%2FoAW3%2FiWZVG1pBAmUTZDh1DjwyFn%2FlqWpbZmbFNn6zD9gwWSteYup5jExFbQZhVVk6FXzRDVAZzv%2Frlbael2GhwSCTTSiiL1sAJEBzfY2iEBrxCPmLPf%2B8RBd9Zgxq%2FTLcsoqkqzHHua2eR9%2BXq4km%2FytXGBFjosFOKqBp9CT5EDNKcu6VgQwFTYUfkI%2FdiwhHh%2BCuIc0HR3JEwATD8rR6Ez9a5j8HJPWA2xWSHQkxCAoiS6oeMvPxz%2BkSP2qPynIBDyzw8%2BZ4R0OZ69QrYxY1syXXDXIYIi5ZvtECTr3P9K9dyBz7rSLDXMU9Z%2Fib4KxY8MkRDaRaxkqJ2MDe0g%2FaIP2Y8GNinoJFvQ5kdTKmj5fjB9zvWmY0VvKARr0f9PyIG0Auwc1kyYsJn5LIxR%2BS6niCOeMUj0ypO8KaNG9HzuGdEE5fMIHn6LwGOqUBrx8nVz18DxXu0fCnmIXmSsATTT5BxbCNFh0uMnumVnlLLsFv5kgHz38JNye6dd0u%2FHsk0SbIu%2Bn%2FQsgqfUtd7P5qEDGTqSkdJphY4ZOcAvJTWcZ3%2B9%2BTSKv2fZxV7WogJ00u2w5urk8lIx1Z%2F0v49zcbtLf9cFWyiuDRlZPXM2CvTyphYwNuR1WMcGpAj8HXIX%2FV8o6pIwmYJVEJvLg7MFCjCmfi&X-Amz-Signature=bcb1e87a40fed0eba453c933073e80d0d49413accd8013808142a53fe524de36&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8f1b1d60-cf1b-42b3-9faa-f634c89c3f84/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YOIZMOUK%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T141335Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIEX7S%2BLNH2CTh5i1ofpNsGqLcU0wO9xS0%2Bjuough5AbnAiEA8qTbvf1xSvKhcIXy5uXa%2BJ28Xh53neVM59PX335GW1EqiAQIj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJQUD6FBAuP%2Bw5sJ1ircAw9Yu66MCezosXSuPb2cpGFhX7lkQoJA1CRyOdcS1zisaP5Dre%2F1NqHkhT%2Bz%2Btqkx%2Fyw0TLIVFXcsVqRSVn4w%2FPufqCoE3QprEd948a0fYFdYi69xrpWSuezJo9sCMMbUxdf729engqE8SrpGfK%2FLnq%2F2GXXAilwHO6UZRwT2hdqSQztrdRYG1fRZkkwO0uvp7gtLYumE%2B%2FoAW3%2FiWZVG1pBAmUTZDh1DjwyFn%2FlqWpbZmbFNn6zD9gwWSteYup5jExFbQZhVVk6FXzRDVAZzv%2Frlbael2GhwSCTTSiiL1sAJEBzfY2iEBrxCPmLPf%2B8RBd9Zgxq%2FTLcsoqkqzHHua2eR9%2BXq4km%2FytXGBFjosFOKqBp9CT5EDNKcu6VgQwFTYUfkI%2FdiwhHh%2BCuIc0HR3JEwATD8rR6Ez9a5j8HJPWA2xWSHQkxCAoiS6oeMvPxz%2BkSP2qPynIBDyzw8%2BZ4R0OZ69QrYxY1syXXDXIYIi5ZvtECTr3P9K9dyBz7rSLDXMU9Z%2Fib4KxY8MkRDaRaxkqJ2MDe0g%2FaIP2Y8GNinoJFvQ5kdTKmj5fjB9zvWmY0VvKARr0f9PyIG0Auwc1kyYsJn5LIxR%2BS6niCOeMUj0ypO8KaNG9HzuGdEE5fMIHn6LwGOqUBrx8nVz18DxXu0fCnmIXmSsATTT5BxbCNFh0uMnumVnlLLsFv5kgHz38JNye6dd0u%2FHsk0SbIu%2Bn%2FQsgqfUtd7P5qEDGTqSkdJphY4ZOcAvJTWcZ3%2B9%2BTSKv2fZxV7WogJ00u2w5urk8lIx1Z%2F0v49zcbtLf9cFWyiuDRlZPXM2CvTyphYwNuR1WMcGpAj8HXIX%2FV8o6pIwmYJVEJvLg7MFCjCmfi&X-Amz-Signature=400d241f7508d3b1d7cf3db3f4fc2f706c7c1429870e4aad4d50fd6224ccbbe5&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/13ad0497-05fe-4eaa-984e-707b33e14761/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YOIZMOUK%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T141335Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIEX7S%2BLNH2CTh5i1ofpNsGqLcU0wO9xS0%2Bjuough5AbnAiEA8qTbvf1xSvKhcIXy5uXa%2BJ28Xh53neVM59PX335GW1EqiAQIj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJQUD6FBAuP%2Bw5sJ1ircAw9Yu66MCezosXSuPb2cpGFhX7lkQoJA1CRyOdcS1zisaP5Dre%2F1NqHkhT%2Bz%2Btqkx%2Fyw0TLIVFXcsVqRSVn4w%2FPufqCoE3QprEd948a0fYFdYi69xrpWSuezJo9sCMMbUxdf729engqE8SrpGfK%2FLnq%2F2GXXAilwHO6UZRwT2hdqSQztrdRYG1fRZkkwO0uvp7gtLYumE%2B%2FoAW3%2FiWZVG1pBAmUTZDh1DjwyFn%2FlqWpbZmbFNn6zD9gwWSteYup5jExFbQZhVVk6FXzRDVAZzv%2Frlbael2GhwSCTTSiiL1sAJEBzfY2iEBrxCPmLPf%2B8RBd9Zgxq%2FTLcsoqkqzHHua2eR9%2BXq4km%2FytXGBFjosFOKqBp9CT5EDNKcu6VgQwFTYUfkI%2FdiwhHh%2BCuIc0HR3JEwATD8rR6Ez9a5j8HJPWA2xWSHQkxCAoiS6oeMvPxz%2BkSP2qPynIBDyzw8%2BZ4R0OZ69QrYxY1syXXDXIYIi5ZvtECTr3P9K9dyBz7rSLDXMU9Z%2Fib4KxY8MkRDaRaxkqJ2MDe0g%2FaIP2Y8GNinoJFvQ5kdTKmj5fjB9zvWmY0VvKARr0f9PyIG0Auwc1kyYsJn5LIxR%2BS6niCOeMUj0ypO8KaNG9HzuGdEE5fMIHn6LwGOqUBrx8nVz18DxXu0fCnmIXmSsATTT5BxbCNFh0uMnumVnlLLsFv5kgHz38JNye6dd0u%2FHsk0SbIu%2Bn%2FQsgqfUtd7P5qEDGTqSkdJphY4ZOcAvJTWcZ3%2B9%2BTSKv2fZxV7WogJ00u2w5urk8lIx1Z%2F0v49zcbtLf9cFWyiuDRlZPXM2CvTyphYwNuR1WMcGpAj8HXIX%2FV8o6pIwmYJVEJvLg7MFCjCmfi&X-Amz-Signature=b7f4e2253080c8e3cca959f1bf386522df03dc6079766f40c1e9c3d9226c9710&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 2. Box and Whisker Plot
A box plot shows the distribution of quantitative data in a way that facilitates comparisons between variables or across levels of a categorical variable. The box shows the quartiles of the dataset while the whiskers extend to show the rest of the distribution, except for points that are determined to be "outliers".
**Syntax:**
```python
sns.boxplot(x='header_1', y='header_2', data=df)
```
**Example Output:**


![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d207ae92-0a7c-4e2f-aa65-0ee5a2c33bf7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UXRBRJ23%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T141337Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDm1j9GAIZmvFDNykp9e6T5F%2B4Ezt1JVELuzPXMvO9OkwIgbQxwVmRrRmVVa2WQWJ2s77IoqOlH1rGHy7T%2FOVlZ6zUqiAQIj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDEPjKKQyz1gtKJNbnircA%2FDMl0S2OOE%2FIisHfwCnN4gTaqMnhYvpRadqYq72l0M%2Fizy7Zppw3aDwDQIgz2taIBMkJtJHX4DaX1J5gfUzHecf2aoPVW%2BdD2Ac0DrMdJzk6goKMjXBQ8%2FQubDvFHUpSWKFfadqT4s1esWrBXBY3bPB3h2ihZ7o5Y0qwlmvPdUn%2BIG7Mmtn4PKr%2B6Y3WQBYk4vcEQxNyoyvoGLu5Js8aVUDoLGGPj26%2BJsS9M%2BwfulSIHn5WyN26FdVYc5T%2BNHrxMEgtuSkvPWJVocJGUVMcArNrsNlJw%2BZYcyCJTFvJaHF5ULUg9YOLxpkKW7f1v337CvwSoEIyqFp9hdF7fhC99tlkBPB5FgufUkqfwc%2BfWH%2BAQvSaH%2FiYxRxPuEsgtxZiqS8IEZ9ZZ2nd4jEulCc1V91d7lrIpFHz9x1Nf3QGnAYRjDzFmLZXlCJV8uOMo7V5iufW9582gGEJ%2BT1qZPgEUpeZAB3Q5i5p8w%2B%2FJHTBy6aobfCSIPRyiAWTm%2FbYgruJXqYzcA9xYPtai8nLJ83e0ZnhQHTcAQ300pdoGI6pCsESKn2ANMRh8l6ruyQ7LgX8OCUnLK3lU2%2BuQDpIJSeFhgZPJEOQpAU3bvinHOb%2BK3jNbYlKMm%2B%2BPsae5MCMKbn6LwGOqUBY0Yp32CG6ZTtCRJDtZO3I0TPsQxK5RubpN%2FwAgeRiouPKM5P2X5ILyQunkEZdopwEyTGncKGx1fpwHrQTCpskZkLAIHRWB9Vgb5gDSwLVnLjikn%2FGwfEQYyqVfWsH7%2FN27sMPzHXdpp1AlKK55JXLFNV1gm89W5KRz%2BGfio4RRW4Re%2FTMk6pTfpada6pXpUeQ2tGCCIQOgi7u6ORvyDdEhf5GC05&X-Amz-Signature=3eaaf72ed0f58933dc8982efaa71cabe3a51c3993b3f15d68092886cfc58915e&X-Amz-SignedHeaders=host&x-id=GetObject)

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0e516edc-7551-4792-ab18-0494db3c4c0c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R7MYSJ7O%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T141336Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICfQW978P%2BXqZHAO83tGXqQ20ZNRICuOIIyI12EkLATyAiAa9d6a2C6IFjUuttr227lJ6EGtua0MCZ%2F0TETlDRzQlCqIBAiP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM92JjqV6tS5o0zVXFKtwDlXCUrv%2Fz2qEuT4kjNFUdR7Uod%2BuxB7Hp2zXoLiyOE2YGhPxkLNXhI%2FVVp2SFp9wI1nLsXOm0JTlq07foT2ANCfE754NXjZt68juVIBeqHYUIgNoJsIewAFOHzWGPvBXMm3%2F2YZx%2B64RviOTA9T8zmP2CYthIcsAo9TzLdGmkth4Ah%2BDW9Sr4ZVBUFf4ynkV%2FzgFii6uZ6xpyrxU2Ehm7fg4Yox0GLsRqWVr9Yxdp3IEqaei9LvQ53UGYvqwpEzf11uHHL4qDhQk7hfm58EmlAny10ZykDuVKVXT%2Bh5PbvGAn8PnUoMquIlKzxyinQTXUsO9Iwgn8ukKhvnGHbBMeA2qGa%2B5sieYR5xC16H6dPyAQWBKC8sd3Gtzn%2FeG35Y%2BoaglU4bd2w5MaVPRqLflpuKE8ZocAvYgxdX23sbzYeJB6JSb1Q17iPKBPx43uyY8e84l8sLjSQc4%2Bj4U3ryF2viES%2BEaaeFGqafZV0YB8TLfNXUdw9e2gEB9kLB3dJ%2B3om5h%2FCb2YD1CtGw6G1fCO4kI8rUGHu70AHewch8gmTeQHPHTGfancl1IU%2FO1qbICPC5J3coVWBjFKdD%2BxF6%2FVYvm1MQW4CgRq89RbTfAKVktgQ%2BgchnGfi2xynigwsOfovAY6pgEuvkMCcagQiVwCELNHD8n97ICbozqckW8U3Q5OrnM%2BxWWeLy8npYI9Q3T1DqOx8vtbsiczuCm7I5TDQ7BTspK0z303ipdORYNiL%2BxY7sR4XQeaGsv00uuhNhMuWbd14zGI2lmtkQknMjDnYpoRqMACa4gxeVWwnXWnxZ2bZ2kTk5CK3fDUBji3fh5MxPew50t%2B20SNcaCgtN7NHPthp2O1eDIRlqmB&X-Amz-Signature=b6589b24d3a8e836b96567617af1aac5e047074b1e576e325b9ab178e7a26ff0&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23a79b9d-2356-49a9-8fd9-65c6b0ab2cc5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YOIZMOUK%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T141335Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIEX7S%2BLNH2CTh5i1ofpNsGqLcU0wO9xS0%2Bjuough5AbnAiEA8qTbvf1xSvKhcIXy5uXa%2BJ28Xh53neVM59PX335GW1EqiAQIj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJQUD6FBAuP%2Bw5sJ1ircAw9Yu66MCezosXSuPb2cpGFhX7lkQoJA1CRyOdcS1zisaP5Dre%2F1NqHkhT%2Bz%2Btqkx%2Fyw0TLIVFXcsVqRSVn4w%2FPufqCoE3QprEd948a0fYFdYi69xrpWSuezJo9sCMMbUxdf729engqE8SrpGfK%2FLnq%2F2GXXAilwHO6UZRwT2hdqSQztrdRYG1fRZkkwO0uvp7gtLYumE%2B%2FoAW3%2FiWZVG1pBAmUTZDh1DjwyFn%2FlqWpbZmbFNn6zD9gwWSteYup5jExFbQZhVVk6FXzRDVAZzv%2Frlbael2GhwSCTTSiiL1sAJEBzfY2iEBrxCPmLPf%2B8RBd9Zgxq%2FTLcsoqkqzHHua2eR9%2BXq4km%2FytXGBFjosFOKqBp9CT5EDNKcu6VgQwFTYUfkI%2FdiwhHh%2BCuIc0HR3JEwATD8rR6Ez9a5j8HJPWA2xWSHQkxCAoiS6oeMvPxz%2BkSP2qPynIBDyzw8%2BZ4R0OZ69QrYxY1syXXDXIYIi5ZvtECTr3P9K9dyBz7rSLDXMU9Z%2Fib4KxY8MkRDaRaxkqJ2MDe0g%2FaIP2Y8GNinoJFvQ5kdTKmj5fjB9zvWmY0VvKARr0f9PyIG0Auwc1kyYsJn5LIxR%2BS6niCOeMUj0ypO8KaNG9HzuGdEE5fMIHn6LwGOqUBrx8nVz18DxXu0fCnmIXmSsATTT5BxbCNFh0uMnumVnlLLsFv5kgHz38JNye6dd0u%2FHsk0SbIu%2Bn%2FQsgqfUtd7P5qEDGTqSkdJphY4ZOcAvJTWcZ3%2B9%2BTSKv2fZxV7WogJ00u2w5urk8lIx1Z%2F0v49zcbtLf9cFWyiuDRlZPXM2CvTyphYwNuR1WMcGpAj8HXIX%2FV8o6pIwmYJVEJvLg7MFCjCmfi&X-Amz-Signature=ee9298ef14ecd2015636371219cff3857876d4d130d1a7a65b5ab3a44c1134a4&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 4. KDE Plot
A Kernel Density Estimate (KDE) plot is a graph that creates a probability distribution curve for the data based upon its likelihood of occurrence on a specific value. This is created for a single vector of information.
**Syntax:**
```python
sns.kdeplot(X) || sns.kdeplot(df['age'])
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0d571213-2a2f-4921-a50b-880847aa05ee/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YOIZMOUK%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T141335Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIEX7S%2BLNH2CTh5i1ofpNsGqLcU0wO9xS0%2Bjuough5AbnAiEA8qTbvf1xSvKhcIXy5uXa%2BJ28Xh53neVM59PX335GW1EqiAQIj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJQUD6FBAuP%2Bw5sJ1ircAw9Yu66MCezosXSuPb2cpGFhX7lkQoJA1CRyOdcS1zisaP5Dre%2F1NqHkhT%2Bz%2Btqkx%2Fyw0TLIVFXcsVqRSVn4w%2FPufqCoE3QprEd948a0fYFdYi69xrpWSuezJo9sCMMbUxdf729engqE8SrpGfK%2FLnq%2F2GXXAilwHO6UZRwT2hdqSQztrdRYG1fRZkkwO0uvp7gtLYumE%2B%2FoAW3%2FiWZVG1pBAmUTZDh1DjwyFn%2FlqWpbZmbFNn6zD9gwWSteYup5jExFbQZhVVk6FXzRDVAZzv%2Frlbael2GhwSCTTSiiL1sAJEBzfY2iEBrxCPmLPf%2B8RBd9Zgxq%2FTLcsoqkqzHHua2eR9%2BXq4km%2FytXGBFjosFOKqBp9CT5EDNKcu6VgQwFTYUfkI%2FdiwhHh%2BCuIc0HR3JEwATD8rR6Ez9a5j8HJPWA2xWSHQkxCAoiS6oeMvPxz%2BkSP2qPynIBDyzw8%2BZ4R0OZ69QrYxY1syXXDXIYIi5ZvtECTr3P9K9dyBz7rSLDXMU9Z%2Fib4KxY8MkRDaRaxkqJ2MDe0g%2FaIP2Y8GNinoJFvQ5kdTKmj5fjB9zvWmY0VvKARr0f9PyIG0Auwc1kyYsJn5LIxR%2BS6niCOeMUj0ypO8KaNG9HzuGdEE5fMIHn6LwGOqUBrx8nVz18DxXu0fCnmIXmSsATTT5BxbCNFh0uMnumVnlLLsFv5kgHz38JNye6dd0u%2FHsk0SbIu%2Bn%2FQsgqfUtd7P5qEDGTqSkdJphY4ZOcAvJTWcZ3%2B9%2BTSKv2fZxV7WogJ00u2w5urk8lIx1Z%2F0v49zcbtLf9cFWyiuDRlZPXM2CvTyphYwNuR1WMcGpAj8HXIX%2FV8o6pIwmYJVEJvLg7MFCjCmfi&X-Amz-Signature=6dbb165e0e21e1d8c501e9fd0ade1dc2004f9e5265e21657694995440c9229db&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/53752550-ef82-4ca9-a01a-09921f0282d0/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YOIZMOUK%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T141335Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIEX7S%2BLNH2CTh5i1ofpNsGqLcU0wO9xS0%2Bjuough5AbnAiEA8qTbvf1xSvKhcIXy5uXa%2BJ28Xh53neVM59PX335GW1EqiAQIj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJQUD6FBAuP%2Bw5sJ1ircAw9Yu66MCezosXSuPb2cpGFhX7lkQoJA1CRyOdcS1zisaP5Dre%2F1NqHkhT%2Bz%2Btqkx%2Fyw0TLIVFXcsVqRSVn4w%2FPufqCoE3QprEd948a0fYFdYi69xrpWSuezJo9sCMMbUxdf729engqE8SrpGfK%2FLnq%2F2GXXAilwHO6UZRwT2hdqSQztrdRYG1fRZkkwO0uvp7gtLYumE%2B%2FoAW3%2FiWZVG1pBAmUTZDh1DjwyFn%2FlqWpbZmbFNn6zD9gwWSteYup5jExFbQZhVVk6FXzRDVAZzv%2Frlbael2GhwSCTTSiiL1sAJEBzfY2iEBrxCPmLPf%2B8RBd9Zgxq%2FTLcsoqkqzHHua2eR9%2BXq4km%2FytXGBFjosFOKqBp9CT5EDNKcu6VgQwFTYUfkI%2FdiwhHh%2BCuIc0HR3JEwATD8rR6Ez9a5j8HJPWA2xWSHQkxCAoiS6oeMvPxz%2BkSP2qPynIBDyzw8%2BZ4R0OZ69QrYxY1syXXDXIYIi5ZvtECTr3P9K9dyBz7rSLDXMU9Z%2Fib4KxY8MkRDaRaxkqJ2MDe0g%2FaIP2Y8GNinoJFvQ5kdTKmj5fjB9zvWmY0VvKARr0f9PyIG0Auwc1kyYsJn5LIxR%2BS6niCOeMUj0ypO8KaNG9HzuGdEE5fMIHn6LwGOqUBrx8nVz18DxXu0fCnmIXmSsATTT5BxbCNFh0uMnumVnlLLsFv5kgHz38JNye6dd0u%2FHsk0SbIu%2Bn%2FQsgqfUtd7P5qEDGTqSkdJphY4ZOcAvJTWcZ3%2B9%2BTSKv2fZxV7WogJ00u2w5urk8lIx1Z%2F0v49zcbtLf9cFWyiuDRlZPXM2CvTyphYwNuR1WMcGpAj8HXIX%2FV8o6pIwmYJVEJvLg7MFCjCmfi&X-Amz-Signature=46b6b72bc0a9a7f03936c7bda03b161500d9f4a25ad1184bf4fbce417d984a48&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
## 4. Correlation Between Variables
Correlation is a statistical measure of the extent to which different variables are interdependent. It indicates how changes in one variable are associated with changes in another variable over time.
### Positive Correlation
Positive correlation indicates that as one variable increases, the other variable also tends to increase.
**Example: Engine Size and Price**
- **Positive Correlation:** Engine size increases, price also increases.
- **Visualization:** Scatter plot with a steep positive slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c7ea9b0-3ef3-4357-a9c3-554fc71b6b15/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SBSC4MYE%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T141337Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIG0LU50Z9Lh9aB5cfaW4HVyhk8w06qNR%2BDB4lk2o80ZAAiBazIn21w0i3jbbA248uWkR09lTGP3oWdbZo8ce9jO7NCqIBAiP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMwcJViJqp1GE1ZOlEKtwDXqT5lLmXt9JuodKX7%2FtnjPIpYk4wzvPcHr%2FKqwE8IYDWV3ExhVVn60B0jIRhZVZGrh7LM53RIq1a4FZmjf8nOg4R%2F2P8Y8wDJX3MivmppwEZAvjqt3HWXiCllUE5tdCZqNygFaJ49KsRbH99zscM0zjAcscc%2B9PIeOWmKHLzipQc4dlt1l4MtqwrwCX0IUD66EaG%2F89%2FuLmixfWjRc6i%2FfBBphfns%2FEAgy69Q8CHt2iIdO%2FXh3ws2OSogYoJgbMmh1YM1PEiHMODgFRk7yyts7tnLT%2FtcmZCPNwQKdUsy5EDl%2BneDgSmfADuzfEmovmq9VcsMRfr7ndkHMAFUXpjHaQqLM7Syx2j2aq0wE1auVPOBULeh9hT0G9y%2BxZW1aql4qdXpgfc18eTLlib6OdKfaYsOq6RcGPS%2FGryGSy%2FhrplXMgRRR5mn%2FFys%2Bgs%2FPKERe%2B144WnLn8Iir7VF5%2BYvkOWCUgziRoS2y2B2o%2BksPcXkBU6zJlsapq%2BHHP3QUHHl40XSvJfgVeV4X2%2FqgkkXtgmOVPdXwhcAnJf7OGRdVqSbRgqJVuAOjXiQLiK%2FaJDT2PxdPEBhMmFDtSn3drQzTUVyUON3U5Azop1sl4twLaKgxi2uXsRuxzSUa4wrufovAY6pgEUhhIClR43LX2eCT2FTePhmdd2ZxdUYM7q191JbtO4ourKpZt3SSbbFy36DDq5nDLa3rVf4sixO9oXK3nRn4TOt5nJ7NIBDiEFt4LI6okjRVyPKS0KvPpcn06Vd%2BLAoVTPLrCx8wyjU9OzibBPTYRX%2FFSZ8kce82WpE%2BqlElKVaxkCp3rwx%2FfR69fuUqVGbew5R8bnXbbCNxuSsq4rfypCBbhKwwDK&X-Amz-Signature=465ccebb39454e3fc6cf497826999d6659cd6de4436839a2285150e911109149&X-Amz-SignedHeaders=host&x-id=GetObject)
**Explanation:** When engine size increases, there is a corresponding increase in the price of the vehicle. This positive correlation suggests that larger engines tend to be associated with higher prices in the market.
___
### Negative Correlation
Negative correlation indicates that as one variable increases, the other variable tends to decrease.
**Example: Highway Miles per Gallon and Price**
- **Negative Correlation:** As highway miles per gallon increases, price decreases.
- **Visualization:** Scatter plot with a steep negative slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/10f1f798-9cc4-4df2-a9c1-5a339f554a0b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466S3TS7CGF%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T141336Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGQZZHea3z9DVjiB%2BcuTUmqnRqqnWEIRWAZYqwblgfbYAiBxZ%2F0E7NIdiYz2mnEgdy7zhU1wVqGHMDL8Rx%2FCalVf%2FCqIBAiP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMM1Aw%2Fi4PYkRiC1DFKtwD9YsihF1LN0ap9IcG16Ra0YtDj4ZpWefYD31hbecVCQtDzjqi539wHxaGG925O6HPrhuvmvt%2B8O47Lh8gnXVIx%2BzNf%2FTCZAxQr6tgy%2BECDsgB%2BYtWlat3Yt1Q2ilFlxTY1i9bK0%2BFGA03gvqnBOWnrCVW0BAgs1nJm5mV0y0dOJhoeokYcvC8yK4CD6lc3R3UujChdfEpKZAldGCt%2BApeC3BKgYc5jkm84X3dXRZK6KlG6DnBQ52jI0pE0rKSanu6W3DIYyqukj%2F0u1TO6ecT5GcIRQkM%2FwuBSzTBIVQjgKDREG0DrsX%2F4EbONbsjNw3JSPAmheB%2BQXw7MZZkmIFe8xg8ize%2Bp87epMbOa2%2F7gN1fICDUipOHldeW19J4A1Pl2WMp%2BOlWHGUzf7iU0DV77mnpaHfhbSEE2IkrzhLpc0mFRZWmxOFxdc8Fa2O%2B2UrgX21%2FoEQHkCu2FC5EvwV6f5g2ndkEEfOfhHjyyRzEzYgMIBcs5biQcrL2dBOgDTjs64LKJsBYL2%2FlNC%2Fx2hlruo%2FNFL1CU07pofxiicWoR4aDcBS7RoSSHSga%2FbSvruHWN00yF1zV9xaOM9Pi9p0x6Z6DkyU6UPmtUkFUKeU0SMqArNr%2F9VJZ7DT%2FNlQwlOfovAY6pgG4ZC0j70O3sd4DSf0K8KGAcWgGEDefTdXj6qjS%2Fp8LwP2c73aBDDyYgs7ejM6HJ5N2oI2iUou4rnY8904hQdFlncWTNDbT6P06fEYZFpmaBYpQ4cvqLTKvKvDRXhiLpLEJqX3PodRtH5C%2BYbVq04Zcnn%2BIQ%2Bk1pKtaLlCoGkBBjPsDC7MoYSz88YPtZN0KEbnrKwU9MVmw40XrT1NjRZYXmdYuWuj4&X-Amz-Signature=09513164e916cf13c03d3c42c643a3ccd16282d6f8d8ff18f5e228a1b3323aad&X-Amz-SignedHeaders=host&x-id=GetObject)
**Explanation:** When highway miles per gallon increases, the price of the vehicle tends to decrease. This negative correlation suggests that cars with higher fuel efficiency (more miles per gallon) are generally priced lower in the market.
___
### Weak Correlation
Weak correlation indicates a lack of strong relationship between the variables.
**Example: RPM and Price**
- **Weak Correlation:** Low and high RPM values show varied prices, indicating no strong predictive relationship.
- **Visualization:** Scatter plot with no clear trend or slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9f914514-8914-4bf4-ac84-d9e3077f6eb1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46657YSZI43%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T141336Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGzwU2xfbbtwdFAUgB3dtjH943QP9%2BX5qE2XktDO7E6TAiEA289Rk1k0wEGc8UCLiuInnhh2DARwofBv0PmCMsnrlAsqiAQIj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHgGjkZJ4P6MVF8MnCrcA494IanRp%2F0yqy%2BWhAfKhxQRuaYuEb9NW%2FAzMU7Ny4F0KtuGMilbr8gzrZ0wteEUhc7rjXeVmHN%2F5e7mM0EvLfrsxyORc1hLuOpU4TpnsWEhdWZLY0z7aHbrKjG6qhQB1OHwn%2BPSaRF4jftcKrtrzI3f9zHRhlmqqppHeX4rM00SHd7kVAY976Yg7WQGutLMQKi03U9ZeulZf1e8sg8VFWYk7Zkc8ey2kFV%2B7GPbQJeU9Wlvdg5rIFKlc0OjHnVK7oVcKQ3KUFNUCH17%2BCiU%2FzfqpolCW3zAoPeXkIBKG3q8hwxZgsMcjIPUJOJZnXVn9IG%2BOKCi8gtSW7ZcPjmCUF21OrnaSBFTFP2E8eF1WvoCL7lT73Tov73S21S4fl0K2O1bFPqqF17hx%2Bo3H7HJpu%2F6%2B2iKuz97tf5oynOd%2FxqRVVnjHXtYa2wOz%2FIgFXihKRCTxFUWVj7Y7DlMZxAnBb9up2Qxncph%2BteXpLMUOFv%2BUzu7EyI%2BqHXvTLd1f%2BfdyHzRjpVOo8JiQ7QspQpMczlJHvEaOYnHR1N7Qmkpq7jjPJfIwTipZIZ7QSID7H0HAvwGEkkStZHzqiyJ8IxqR7VKcf94MgNkSwdy9Fu0wTpiK3vB7jExKW2Xv6nZMKzn6LwGOqUBLe4WW71OF9o24%2F3YEaPNZPvNdvNPTd1WEnMCxwJdkCOh7zEODDegBHvWZz%2B2p1QvUVMoNLolaEz4VYAvQ%2Bbg3uDOGhzXCYcT210O%2B9snQY1vTkl0u7kO5dGKMyCpSON7lYzqKiqJBAYwr9nzy6g1dHnfEwLYa%2F85CohAxWYY9%2BW7xtQUexQESrGanjEZCCYqyFwWdYHu2yBTPKfFocfMowvQqZ3D&X-Amz-Signature=177f5766ce5897c73f7c658d4541289b706a29465b396fbdff9a2f785799ff43&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f18086e5-5b04-4fbf-8309-8944ab20d213/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RGAZZHCO%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T141336Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGN3FLGWIvX63PPUCAMhK4XHlzXScn8JQzjDeT2HzVaOAiAR0aVO%2FBsqIKHE66HXxSuruAoDdBN3CievVkHGbQ%2BjaiqIBAiP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM6kuh0JkSduPS5lxQKtwDMyEfSJmNSBDTyKeWfiKaQswPWLraa1p2cRnpPo6%2B6jdbG5R%2BdCIqjXjAOdidIV34FWgT8AgZfA8aOSz13FDBPitFUBBXCCzfufGrxNAWPOrnC4YDt1dGcq1tbLyhN1bcyVBfGx%2BLQyQBFKVJt4T5CZ0QP3he8oM4daEtjdxjn4KfzKCidIvCHXAJRrcxRCEBgXPgDK5DAcUJuV0hmH9%2BCwQIGk3rZKZzlNYrFYJSOF2MGSp1mPCwnaps9xOA4p3iDqLiN2awMHOVj%2BzAlvQFhVGc1%2FkpfHrVTAe3pXWmZCId064ahbpk8%2F3MDHmkH3bUnFOjyGpwnqwe1Os0Rdutnb5cuepzqkcwxueO%2FHsgvq7jJU2bdPDFPOOri1PQzEfeJETehkVOveNEDpnIB4azqbJWaY8NzQ7e0zSvKk0DCOdiMdz5UTXNbGBxM7rOj2bTL9E%2BUC1YTaJ%2B%2FyYwe6N8CJVShjeKCe8xv2enuBLuE3hbjWWNNUHIXRmbvxu5eMaVa8CzxOU56VSvJx7wHC4hpB3B%2B8mWQWi9Q%2BzOf7YknH17eFhrq6E9aSjAcB%2F7HKJEixtO0TsK%2F5JTEHFznESrr8dzi1m%2FekMZ8wr%2B1%2BIiyWBzGaK8eIaobDxeQF8ws%2BfovAY6pgGcPVkCrA7nNZ93iZB6C%2Fz4uc0zWZKVd%2BmNADRQzi7LuzQJCGCAE8Yo3%2BhumJW2EAIBAq%2FTQGUUdf1YRBqDisYieGScWRlHhUQ0bpCxuHHW2ZK0Gvt%2FIarMfIc5sI9VW%2FfHIk4NFnpHvkn3W%2BDT4OfUz7rFLTOq7s5WpuMqX0dUX7Fjap%2FLyHChOGKNUfH1GWwsCjGoCDlet4WpDSTguc0WpvmWE42v&X-Amz-Signature=b094056b3a62eb3b678741d47d75cb911f07f2c40426b5fe43e351f00ccf256e&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Correlation Plot
Heatmap visualizes correlations among variables. Color scheme indicates Pearson correlation coefficients. Dark red diagonal line shows perfect correlation (value of 1) between variables and themselves.
This heatmap offers overview of variable relationships and their link with price.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cd3b341e-cc1a-45f7-8aec-cdc00436d270/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RGAZZHCO%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T141336Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGN3FLGWIvX63PPUCAMhK4XHlzXScn8JQzjDeT2HzVaOAiAR0aVO%2FBsqIKHE66HXxSuruAoDdBN3CievVkHGbQ%2BjaiqIBAiP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM6kuh0JkSduPS5lxQKtwDMyEfSJmNSBDTyKeWfiKaQswPWLraa1p2cRnpPo6%2B6jdbG5R%2BdCIqjXjAOdidIV34FWgT8AgZfA8aOSz13FDBPitFUBBXCCzfufGrxNAWPOrnC4YDt1dGcq1tbLyhN1bcyVBfGx%2BLQyQBFKVJt4T5CZ0QP3he8oM4daEtjdxjn4KfzKCidIvCHXAJRrcxRCEBgXPgDK5DAcUJuV0hmH9%2BCwQIGk3rZKZzlNYrFYJSOF2MGSp1mPCwnaps9xOA4p3iDqLiN2awMHOVj%2BzAlvQFhVGc1%2FkpfHrVTAe3pXWmZCId064ahbpk8%2F3MDHmkH3bUnFOjyGpwnqwe1Os0Rdutnb5cuepzqkcwxueO%2FHsgvq7jJU2bdPDFPOOri1PQzEfeJETehkVOveNEDpnIB4azqbJWaY8NzQ7e0zSvKk0DCOdiMdz5UTXNbGBxM7rOj2bTL9E%2BUC1YTaJ%2B%2FyYwe6N8CJVShjeKCe8xv2enuBLuE3hbjWWNNUHIXRmbvxu5eMaVa8CzxOU56VSvJx7wHC4hpB3B%2B8mWQWi9Q%2BzOf7YknH17eFhrq6E9aSjAcB%2F7HKJEixtO0TsK%2F5JTEHFznESrr8dzi1m%2FekMZ8wr%2B1%2BIiyWBzGaK8eIaobDxeQF8ws%2BfovAY6pgGcPVkCrA7nNZ93iZB6C%2Fz4uc0zWZKVd%2BmNADRQzi7LuzQJCGCAE8Yo3%2BhumJW2EAIBAq%2FTQGUUdf1YRBqDisYieGScWRlHhUQ0bpCxuHHW2ZK0Gvt%2FIarMfIc5sI9VW%2FfHIk4NFnpHvkn3W%2BDT4OfUz7rFLTOq7s5WpuMqX0dUX7Fjap%2FLyHChOGKNUfH1GWwsCjGoCDlet4WpDSTguc0WpvmWE42v&X-Amz-Signature=c36d2bf4ce11612fcbc300234ea97e1561aba36d5dbdfac22f6a9b1a1c961300&X-Amz-SignedHeaders=host&x-id=GetObject)

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
