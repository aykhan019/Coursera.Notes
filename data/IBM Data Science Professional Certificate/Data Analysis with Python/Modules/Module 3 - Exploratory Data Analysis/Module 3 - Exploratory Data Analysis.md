

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7e6d594d-952e-44b6-97ea-31225882aea6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VST7SMNO%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T141341Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF0aCXVzLXdlc3QtMiJHMEUCIQDWIJweV8TNMe1U5rPCuknWOYhRpJJ2qNQwn8sKSh6hXgIgbTba2DY7m%2BZogRVpA53AB3NkyejgSeB1uefxS7Vsb9wq%2FwMIdhAAGgw2Mzc0MjMxODM4MDUiDMhlOZGcZ1OXROeCvSrcA2BoDv7LE8Zyhh8dVlvPBT%2FKuZ0k76pgWPPdwtD4wNLb%2FvAT0Q5Z2Yke3Rre%2FwA%2Bt7h93ZGXEsj2cjTnZOluK0PysbLoU5w1Os2U9cp%2FMQRigXlMSHfU%2BwT%2B59%2BFxare89jJqy33zYtBoc4sD8m5rErce7dzzuXsYfSPUEj0aB6DcRaLU7OZRORogGTB9e01PJkUECvSGrptK6IIaBE82Wo4apVq%2BsIwgsJbYljFOJAwf%2FBJLPGLYseWCw%2FItS4x4QVeTkXFBAr5bGklONRhQLUqBBv%2Bkp225wI4xaD%2B2IXl3nYJyLvypxZU34clZibJTMq%2FIohACLhLrdLiQ6xZTS5tp4fHw5jfT%2FrvrII1ya1yZ8VzcuK2a%2Fa3MAmvRXOWELg2jm5clrJ8xBdawMAQv3Hec%2F1btFST70%2FuuViSvN%2BJ6iDxF%2Fg8jDFiDiRIuY%2FxIEDPaqyg0bnSxOzkaz8KJcpYItBgYdz9VqyAhS5UPmOjYtC7TpQCQJCOMh2ZWW1yCHYr4%2FalODZiRL8iI02CTpqfhE%2BhvJ0smtUaBTQQOMGsDn7ZrGubier%2FQJB%2Bn5UYfb0aBlwJE0FyvateOPDDjWV890t9InhwNaAfMlFkRy0SO3exh9WRgl6RxOFVMLuLmL0GOqUB64BaOR%2BvFNHhm1ibtBGiVQT%2FroLh4tMCMi2v9%2FU6ee2V1b3GqIOksbCMqjEb23xvMkSBbHfa%2Fb3nojENGNIVhiOOaXdJrRhTjSZuTs9zfjUR5wj0XCv06mgGSOWM24bbGsmNfrYv%2FlVnbW0AdxelU0ls8jIrDidgkW%2FcMPIp2A0gbZHUvhQBYKIMB0LWa5np0PfcAjB0EZmt72WzGOYkqOu0wiMF&X-Amz-Signature=752a170c779bb96a4463f1817003e30b70cbbb650fe213dbf669322880c19247&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cbfaed9e-b398-4902-8936-dea058b21def/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VST7SMNO%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T141341Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF0aCXVzLXdlc3QtMiJHMEUCIQDWIJweV8TNMe1U5rPCuknWOYhRpJJ2qNQwn8sKSh6hXgIgbTba2DY7m%2BZogRVpA53AB3NkyejgSeB1uefxS7Vsb9wq%2FwMIdhAAGgw2Mzc0MjMxODM4MDUiDMhlOZGcZ1OXROeCvSrcA2BoDv7LE8Zyhh8dVlvPBT%2FKuZ0k76pgWPPdwtD4wNLb%2FvAT0Q5Z2Yke3Rre%2FwA%2Bt7h93ZGXEsj2cjTnZOluK0PysbLoU5w1Os2U9cp%2FMQRigXlMSHfU%2BwT%2B59%2BFxare89jJqy33zYtBoc4sD8m5rErce7dzzuXsYfSPUEj0aB6DcRaLU7OZRORogGTB9e01PJkUECvSGrptK6IIaBE82Wo4apVq%2BsIwgsJbYljFOJAwf%2FBJLPGLYseWCw%2FItS4x4QVeTkXFBAr5bGklONRhQLUqBBv%2Bkp225wI4xaD%2B2IXl3nYJyLvypxZU34clZibJTMq%2FIohACLhLrdLiQ6xZTS5tp4fHw5jfT%2FrvrII1ya1yZ8VzcuK2a%2Fa3MAmvRXOWELg2jm5clrJ8xBdawMAQv3Hec%2F1btFST70%2FuuViSvN%2BJ6iDxF%2Fg8jDFiDiRIuY%2FxIEDPaqyg0bnSxOzkaz8KJcpYItBgYdz9VqyAhS5UPmOjYtC7TpQCQJCOMh2ZWW1yCHYr4%2FalODZiRL8iI02CTpqfhE%2BhvJ0smtUaBTQQOMGsDn7ZrGubier%2FQJB%2Bn5UYfb0aBlwJE0FyvateOPDDjWV890t9InhwNaAfMlFkRy0SO3exh9WRgl6RxOFVMLuLmL0GOqUB64BaOR%2BvFNHhm1ibtBGiVQT%2FroLh4tMCMi2v9%2FU6ee2V1b3GqIOksbCMqjEb23xvMkSBbHfa%2Fb3nojENGNIVhiOOaXdJrRhTjSZuTs9zfjUR5wj0XCv06mgGSOWM24bbGsmNfrYv%2FlVnbW0AdxelU0ls8jIrDidgkW%2FcMPIp2A0gbZHUvhQBYKIMB0LWa5np0PfcAjB0EZmt72WzGOYkqOu0wiMF&X-Amz-Signature=d3a46eaf799b5a657cf7e3fcbf7dbd3cf20427c661c1d8471f6cb01a30d41d44&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/91181646-b1e0-4433-9711-6259a96a9247/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VST7SMNO%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T141341Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF0aCXVzLXdlc3QtMiJHMEUCIQDWIJweV8TNMe1U5rPCuknWOYhRpJJ2qNQwn8sKSh6hXgIgbTba2DY7m%2BZogRVpA53AB3NkyejgSeB1uefxS7Vsb9wq%2FwMIdhAAGgw2Mzc0MjMxODM4MDUiDMhlOZGcZ1OXROeCvSrcA2BoDv7LE8Zyhh8dVlvPBT%2FKuZ0k76pgWPPdwtD4wNLb%2FvAT0Q5Z2Yke3Rre%2FwA%2Bt7h93ZGXEsj2cjTnZOluK0PysbLoU5w1Os2U9cp%2FMQRigXlMSHfU%2BwT%2B59%2BFxare89jJqy33zYtBoc4sD8m5rErce7dzzuXsYfSPUEj0aB6DcRaLU7OZRORogGTB9e01PJkUECvSGrptK6IIaBE82Wo4apVq%2BsIwgsJbYljFOJAwf%2FBJLPGLYseWCw%2FItS4x4QVeTkXFBAr5bGklONRhQLUqBBv%2Bkp225wI4xaD%2B2IXl3nYJyLvypxZU34clZibJTMq%2FIohACLhLrdLiQ6xZTS5tp4fHw5jfT%2FrvrII1ya1yZ8VzcuK2a%2Fa3MAmvRXOWELg2jm5clrJ8xBdawMAQv3Hec%2F1btFST70%2FuuViSvN%2BJ6iDxF%2Fg8jDFiDiRIuY%2FxIEDPaqyg0bnSxOzkaz8KJcpYItBgYdz9VqyAhS5UPmOjYtC7TpQCQJCOMh2ZWW1yCHYr4%2FalODZiRL8iI02CTpqfhE%2BhvJ0smtUaBTQQOMGsDn7ZrGubier%2FQJB%2Bn5UYfb0aBlwJE0FyvateOPDDjWV890t9InhwNaAfMlFkRy0SO3exh9WRgl6RxOFVMLuLmL0GOqUB64BaOR%2BvFNHhm1ibtBGiVQT%2FroLh4tMCMi2v9%2FU6ee2V1b3GqIOksbCMqjEb23xvMkSBbHfa%2Fb3nojENGNIVhiOOaXdJrRhTjSZuTs9zfjUR5wj0XCv06mgGSOWM24bbGsmNfrYv%2FlVnbW0AdxelU0ls8jIrDidgkW%2FcMPIp2A0gbZHUvhQBYKIMB0LWa5np0PfcAjB0EZmt72WzGOYkqOu0wiMF&X-Amz-Signature=d462a56e91d4d413c3e4dbff29b86a5e755ded8e283e3ed7419a0e53b7f303b7&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/09aba1c0-0d55-41dd-852a-a04c5b8a3fac/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UKFW563W%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T141341Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF0aCXVzLXdlc3QtMiJHMEUCIQCJWFcv64G82vfJ5xMJ%2FNgqp%2BSQOWv%2BpCyFYjmRYFQvHwIgBKnmPQZe6KkDCA2g8Li77R7akcKdWrwsA64tN6sL4Jkq%2FwMIdhAAGgw2Mzc0MjMxODM4MDUiDBt1GpilGYFwOtkZsSrcA%2FV%2BdEob%2BZS1OnhzwL53p5wBwDwsLkBrbFW93Jnho6W7HZQ1NXI%2F4htbn%2FZXwwzIXukYz%2FTJ6mn3Glo1B232plVCnuKzZ07svIqyzfaZ8BtPy2zUO6fVAPb3emmsZydASSHzPrizo3iNaPoiLR9eBAiAI4XOcUyV7TF4jtQWhUQBKkDam0Xmkli%2Bv%2BBLGUuBqsrTngMcgRMTBeL4tkI12TqzGW1Nkj6kbYblomDUpzqeJFD6KlNhXiA4eKLbJR7teT7DH5ra20azLosbtlPcO%2Fre%2FYzLr0U3MYFwoXuHVfz6XnncfvEvVrsYoOQwVG0Rg1QmyCt4qUrdrAp5DlI%2BXzardjS6L9qyEd3rPxUx3geUoxFetZQk34fDIU81dvqZgQAacRGrV%2B6vL4HWNS3pFPEavQ6yfUIhOye7o1UvMoRiRVi%2BdS5GDuktujQlBe5BwRPBQ1RgTfj9BKVpHpujKpn2oYZ3sTjq%2BkFvc59LahWJVJqgre8JaIFLZaRFBew0tSmUwVv11qQuWqXMFSa1lOzsMgnIdZcIiN0%2B1qoCLlCHWwNHnkNRpWAqv%2FKBUEBIN7zVcd9zkYttbFIFTeUklOuXIwJZO3stgmiDehWvZDQ65cbafybqPCQw3UO2MJ6LmL0GOqUBRzhnHs5KRkRpPz2U4Vmz1%2FhO%2FX%2Bk4XiQFZLzxm6hrUTB%2Bg5qUNBKa%2B3btn0to95mWZCixDEak0OG6QdjGVmu6C0S0G8WSe4Az1g9XQWqOTPuHFVvOKw2%2BexzEd1vgs7rWiQIQmYWnAlO9YkJr8qaZUVSxzg7TAo2HveqqlzaSRXW1rsZeHxJjZqt4XazLINTDcLXgjjdwwyHRgRcubCQdrIhVEuO&X-Amz-Signature=d24a29b70d94e050684de9519fb034fe73b11c7a66b39302d3c3c93a14ba47bd&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 2. Scatter Plot
Scatter plots present the relationship between two variables in a dataset. It represents data points on a two-dimensional plane. The independent variable or attribute is plotted on the X-axis, while the dependent variable is plotted on the Y-axis.
**Syntax:**
```python
plt.scatter(x, y)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23708af9-659f-4f23-b626-1a4292d7842c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UKFW563W%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T141342Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF0aCXVzLXdlc3QtMiJHMEUCIQCJWFcv64G82vfJ5xMJ%2FNgqp%2BSQOWv%2BpCyFYjmRYFQvHwIgBKnmPQZe6KkDCA2g8Li77R7akcKdWrwsA64tN6sL4Jkq%2FwMIdhAAGgw2Mzc0MjMxODM4MDUiDBt1GpilGYFwOtkZsSrcA%2FV%2BdEob%2BZS1OnhzwL53p5wBwDwsLkBrbFW93Jnho6W7HZQ1NXI%2F4htbn%2FZXwwzIXukYz%2FTJ6mn3Glo1B232plVCnuKzZ07svIqyzfaZ8BtPy2zUO6fVAPb3emmsZydASSHzPrizo3iNaPoiLR9eBAiAI4XOcUyV7TF4jtQWhUQBKkDam0Xmkli%2Bv%2BBLGUuBqsrTngMcgRMTBeL4tkI12TqzGW1Nkj6kbYblomDUpzqeJFD6KlNhXiA4eKLbJR7teT7DH5ra20azLosbtlPcO%2Fre%2FYzLr0U3MYFwoXuHVfz6XnncfvEvVrsYoOQwVG0Rg1QmyCt4qUrdrAp5DlI%2BXzardjS6L9qyEd3rPxUx3geUoxFetZQk34fDIU81dvqZgQAacRGrV%2B6vL4HWNS3pFPEavQ6yfUIhOye7o1UvMoRiRVi%2BdS5GDuktujQlBe5BwRPBQ1RgTfj9BKVpHpujKpn2oYZ3sTjq%2BkFvc59LahWJVJqgre8JaIFLZaRFBew0tSmUwVv11qQuWqXMFSa1lOzsMgnIdZcIiN0%2B1qoCLlCHWwNHnkNRpWAqv%2FKBUEBIN7zVcd9zkYttbFIFTeUklOuXIwJZO3stgmiDehWvZDQ65cbafybqPCQw3UO2MJ6LmL0GOqUBRzhnHs5KRkRpPz2U4Vmz1%2FhO%2FX%2Bk4XiQFZLzxm6hrUTB%2Bg5qUNBKa%2B3btn0to95mWZCixDEak0OG6QdjGVmu6C0S0G8WSe4Az1g9XQWqOTPuHFVvOKw2%2BexzEd1vgs7rWiQIQmYWnAlO9YkJr8qaZUVSxzg7TAo2HveqqlzaSRXW1rsZeHxJjZqt4XazLINTDcLXgjjdwwyHRgRcubCQdrIhVEuO&X-Amz-Signature=2346c8192527c59dffecba2745c52ae9f58d55aa1cab06e4fff4597a39d9443b&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 3. Histogram
A histogram is an important visual representation of data in categorical form. To view the data in a "Binned" form, use the histogram plot with a number of bins required or with the data points that mark the bin edges. The x-axis represents the data bins, and the y-axis represents the number of elements in each bin.
**Syntax:**
```python
plt.hist(x, bins)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/24e4424a-df87-40a1-b63b-195cbdc2e0ab/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UKFW563W%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T141342Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF0aCXVzLXdlc3QtMiJHMEUCIQCJWFcv64G82vfJ5xMJ%2FNgqp%2BSQOWv%2BpCyFYjmRYFQvHwIgBKnmPQZe6KkDCA2g8Li77R7akcKdWrwsA64tN6sL4Jkq%2FwMIdhAAGgw2Mzc0MjMxODM4MDUiDBt1GpilGYFwOtkZsSrcA%2FV%2BdEob%2BZS1OnhzwL53p5wBwDwsLkBrbFW93Jnho6W7HZQ1NXI%2F4htbn%2FZXwwzIXukYz%2FTJ6mn3Glo1B232plVCnuKzZ07svIqyzfaZ8BtPy2zUO6fVAPb3emmsZydASSHzPrizo3iNaPoiLR9eBAiAI4XOcUyV7TF4jtQWhUQBKkDam0Xmkli%2Bv%2BBLGUuBqsrTngMcgRMTBeL4tkI12TqzGW1Nkj6kbYblomDUpzqeJFD6KlNhXiA4eKLbJR7teT7DH5ra20azLosbtlPcO%2Fre%2FYzLr0U3MYFwoXuHVfz6XnncfvEvVrsYoOQwVG0Rg1QmyCt4qUrdrAp5DlI%2BXzardjS6L9qyEd3rPxUx3geUoxFetZQk34fDIU81dvqZgQAacRGrV%2B6vL4HWNS3pFPEavQ6yfUIhOye7o1UvMoRiRVi%2BdS5GDuktujQlBe5BwRPBQ1RgTfj9BKVpHpujKpn2oYZ3sTjq%2BkFvc59LahWJVJqgre8JaIFLZaRFBew0tSmUwVv11qQuWqXMFSa1lOzsMgnIdZcIiN0%2B1qoCLlCHWwNHnkNRpWAqv%2FKBUEBIN7zVcd9zkYttbFIFTeUklOuXIwJZO3stgmiDehWvZDQ65cbafybqPCQw3UO2MJ6LmL0GOqUBRzhnHs5KRkRpPz2U4Vmz1%2FhO%2FX%2Bk4XiQFZLzxm6hrUTB%2Bg5qUNBKa%2B3btn0to95mWZCixDEak0OG6QdjGVmu6C0S0G8WSe4Az1g9XQWqOTPuHFVvOKw2%2BexzEd1vgs7rWiQIQmYWnAlO9YkJr8qaZUVSxzg7TAo2HveqqlzaSRXW1rsZeHxJjZqt4XazLINTDcLXgjjdwwyHRgRcubCQdrIhVEuO&X-Amz-Signature=b589e8b779c41156d8c00919a744a6d6d77197da3d1f2606b69580437a7bfd38&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ab5a6dfe-51f5-43ee-bcb3-33dae4a1c7ad/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UKFW563W%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T141341Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF0aCXVzLXdlc3QtMiJHMEUCIQCJWFcv64G82vfJ5xMJ%2FNgqp%2BSQOWv%2BpCyFYjmRYFQvHwIgBKnmPQZe6KkDCA2g8Li77R7akcKdWrwsA64tN6sL4Jkq%2FwMIdhAAGgw2Mzc0MjMxODM4MDUiDBt1GpilGYFwOtkZsSrcA%2FV%2BdEob%2BZS1OnhzwL53p5wBwDwsLkBrbFW93Jnho6W7HZQ1NXI%2F4htbn%2FZXwwzIXukYz%2FTJ6mn3Glo1B232plVCnuKzZ07svIqyzfaZ8BtPy2zUO6fVAPb3emmsZydASSHzPrizo3iNaPoiLR9eBAiAI4XOcUyV7TF4jtQWhUQBKkDam0Xmkli%2Bv%2BBLGUuBqsrTngMcgRMTBeL4tkI12TqzGW1Nkj6kbYblomDUpzqeJFD6KlNhXiA4eKLbJR7teT7DH5ra20azLosbtlPcO%2Fre%2FYzLr0U3MYFwoXuHVfz6XnncfvEvVrsYoOQwVG0Rg1QmyCt4qUrdrAp5DlI%2BXzardjS6L9qyEd3rPxUx3geUoxFetZQk34fDIU81dvqZgQAacRGrV%2B6vL4HWNS3pFPEavQ6yfUIhOye7o1UvMoRiRVi%2BdS5GDuktujQlBe5BwRPBQ1RgTfj9BKVpHpujKpn2oYZ3sTjq%2BkFvc59LahWJVJqgre8JaIFLZaRFBew0tSmUwVv11qQuWqXMFSa1lOzsMgnIdZcIiN0%2B1qoCLlCHWwNHnkNRpWAqv%2FKBUEBIN7zVcd9zkYttbFIFTeUklOuXIwJZO3stgmiDehWvZDQ65cbafybqPCQw3UO2MJ6LmL0GOqUBRzhnHs5KRkRpPz2U4Vmz1%2FhO%2FX%2Bk4XiQFZLzxm6hrUTB%2Bg5qUNBKa%2B3btn0to95mWZCixDEak0OG6QdjGVmu6C0S0G8WSe4Az1g9XQWqOTPuHFVvOKw2%2BexzEd1vgs7rWiQIQmYWnAlO9YkJr8qaZUVSxzg7TAo2HveqqlzaSRXW1rsZeHxJjZqt4XazLINTDcLXgjjdwwyHRgRcubCQdrIhVEuO&X-Amz-Signature=2e4f5d0d2d269e67f5e2c73e1d9214eddfd203cbc0000fdb48251fa863da5e6b&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8f1b1d60-cf1b-42b3-9faa-f634c89c3f84/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UKFW563W%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T141341Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF0aCXVzLXdlc3QtMiJHMEUCIQCJWFcv64G82vfJ5xMJ%2FNgqp%2BSQOWv%2BpCyFYjmRYFQvHwIgBKnmPQZe6KkDCA2g8Li77R7akcKdWrwsA64tN6sL4Jkq%2FwMIdhAAGgw2Mzc0MjMxODM4MDUiDBt1GpilGYFwOtkZsSrcA%2FV%2BdEob%2BZS1OnhzwL53p5wBwDwsLkBrbFW93Jnho6W7HZQ1NXI%2F4htbn%2FZXwwzIXukYz%2FTJ6mn3Glo1B232plVCnuKzZ07svIqyzfaZ8BtPy2zUO6fVAPb3emmsZydASSHzPrizo3iNaPoiLR9eBAiAI4XOcUyV7TF4jtQWhUQBKkDam0Xmkli%2Bv%2BBLGUuBqsrTngMcgRMTBeL4tkI12TqzGW1Nkj6kbYblomDUpzqeJFD6KlNhXiA4eKLbJR7teT7DH5ra20azLosbtlPcO%2Fre%2FYzLr0U3MYFwoXuHVfz6XnncfvEvVrsYoOQwVG0Rg1QmyCt4qUrdrAp5DlI%2BXzardjS6L9qyEd3rPxUx3geUoxFetZQk34fDIU81dvqZgQAacRGrV%2B6vL4HWNS3pFPEavQ6yfUIhOye7o1UvMoRiRVi%2BdS5GDuktujQlBe5BwRPBQ1RgTfj9BKVpHpujKpn2oYZ3sTjq%2BkFvc59LahWJVJqgre8JaIFLZaRFBew0tSmUwVv11qQuWqXMFSa1lOzsMgnIdZcIiN0%2B1qoCLlCHWwNHnkNRpWAqv%2FKBUEBIN7zVcd9zkYttbFIFTeUklOuXIwJZO3stgmiDehWvZDQ65cbafybqPCQw3UO2MJ6LmL0GOqUBRzhnHs5KRkRpPz2U4Vmz1%2FhO%2FX%2Bk4XiQFZLzxm6hrUTB%2Bg5qUNBKa%2B3btn0to95mWZCixDEak0OG6QdjGVmu6C0S0G8WSe4Az1g9XQWqOTPuHFVvOKw2%2BexzEd1vgs7rWiQIQmYWnAlO9YkJr8qaZUVSxzg7TAo2HveqqlzaSRXW1rsZeHxJjZqt4XazLINTDcLXgjjdwwyHRgRcubCQdrIhVEuO&X-Amz-Signature=7860eccca7eca04a0dc94d0c908164ba475d318d30d3901a8108503b53164212&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/13ad0497-05fe-4eaa-984e-707b33e14761/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UKFW563W%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T141342Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF0aCXVzLXdlc3QtMiJHMEUCIQCJWFcv64G82vfJ5xMJ%2FNgqp%2BSQOWv%2BpCyFYjmRYFQvHwIgBKnmPQZe6KkDCA2g8Li77R7akcKdWrwsA64tN6sL4Jkq%2FwMIdhAAGgw2Mzc0MjMxODM4MDUiDBt1GpilGYFwOtkZsSrcA%2FV%2BdEob%2BZS1OnhzwL53p5wBwDwsLkBrbFW93Jnho6W7HZQ1NXI%2F4htbn%2FZXwwzIXukYz%2FTJ6mn3Glo1B232plVCnuKzZ07svIqyzfaZ8BtPy2zUO6fVAPb3emmsZydASSHzPrizo3iNaPoiLR9eBAiAI4XOcUyV7TF4jtQWhUQBKkDam0Xmkli%2Bv%2BBLGUuBqsrTngMcgRMTBeL4tkI12TqzGW1Nkj6kbYblomDUpzqeJFD6KlNhXiA4eKLbJR7teT7DH5ra20azLosbtlPcO%2Fre%2FYzLr0U3MYFwoXuHVfz6XnncfvEvVrsYoOQwVG0Rg1QmyCt4qUrdrAp5DlI%2BXzardjS6L9qyEd3rPxUx3geUoxFetZQk34fDIU81dvqZgQAacRGrV%2B6vL4HWNS3pFPEavQ6yfUIhOye7o1UvMoRiRVi%2BdS5GDuktujQlBe5BwRPBQ1RgTfj9BKVpHpujKpn2oYZ3sTjq%2BkFvc59LahWJVJqgre8JaIFLZaRFBew0tSmUwVv11qQuWqXMFSa1lOzsMgnIdZcIiN0%2B1qoCLlCHWwNHnkNRpWAqv%2FKBUEBIN7zVcd9zkYttbFIFTeUklOuXIwJZO3stgmiDehWvZDQ65cbafybqPCQw3UO2MJ6LmL0GOqUBRzhnHs5KRkRpPz2U4Vmz1%2FhO%2FX%2Bk4XiQFZLzxm6hrUTB%2Bg5qUNBKa%2B3btn0to95mWZCixDEak0OG6QdjGVmu6C0S0G8WSe4Az1g9XQWqOTPuHFVvOKw2%2BexzEd1vgs7rWiQIQmYWnAlO9YkJr8qaZUVSxzg7TAo2HveqqlzaSRXW1rsZeHxJjZqt4XazLINTDcLXgjjdwwyHRgRcubCQdrIhVEuO&X-Amz-Signature=6a6f482f87093e67445ce58c7a22839b2381b445843b9f0219b12c370348fb45&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 2. Box and Whisker Plot
A box plot shows the distribution of quantitative data in a way that facilitates comparisons between variables or across levels of a categorical variable. The box shows the quartiles of the dataset while the whiskers extend to show the rest of the distribution, except for points that are determined to be "outliers".
**Syntax:**
```python
sns.boxplot(x='header_1', y='header_2', data=df)
```
**Example Output:**


![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d207ae92-0a7c-4e2f-aa65-0ee5a2c33bf7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WWGURFQS%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T141343Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF0aCXVzLXdlc3QtMiJIMEYCIQCmAltcHrrHW4Edn4W9%2BHKfbEqWAiwvx6ICb6fcEpUxCwIhAI%2FzEwfPDW1aGgdAw%2FKbv11gaxXg3TaeUZ5cwvkybGWAKv8DCHYQABoMNjM3NDIzMTgzODA1Igwql6LthXlgdGRbvagq3ANe6uOUPI%2Fuxjqd5Sa%2BEK76nXFLusmFlKEfHqwyxI%2FQeT2%2Bk%2FXsvnaxeZv4lMI3SCQn%2BVwkirJ6TS4ngwDfZbXYbmov7BqhaGVKHUFt2yu9sIRlw8s62aMsEsdU89qcX2Fbn8dU1Nor0fIHkfJYlSFfbIeTnpg8CUcEWMnKDuD4O1P4UYtY5QvC39iJSGSpwEjHzo3lJS9039bKBzOmdGrMLtgwcv5%2BA9YdkzMcTQ26FaRK1otWtkcflG3vxKos%2FYRJuo%2B0gd8aT0fPViROsfG9OkNMNdAS9R6K4BtyE7vcEeyXaBKF7PBY1YLhtIGpyUGYxZqqaJJYnp4TU2lLpLHvIQFazQJgA%2BqQt%2FCfS23UdSHwBczUWb8Kl1izELa%2B%2B2EP3eSboMdlpASookgGl8HYcj4vjZJZkCD6ah9TztgqYwH24T8nU45KYphjKN8pVDS01iOxuk6d2UVjB9kw8QCNYabQVZtUebGZ6gHIGjaj4kKKeVMLplfLo7EdRDNi%2FEGKEh6M84Fffp3Vhr77llyDYFD0L6QlGhNFjRAnPYN2hhOHjbG%2BtlqD6NxrrjIiaO%2BRF9RokYKJ%2FJPtSlhnZvNVbh297%2BeV%2BwOd933C6k5NWGN6l9ro5HA9XrZS%2FTCHi5i9BjqkAYKa1BurqOafC4hPzMCbOLi6le%2BCl4DQ2lvo8y0wKbjXPXEzIZxV%2BDc1r2m1%2FB88JuyBfrG%2BQCiFs6ciE8s2kJq1tvoz%2BjvKRiBPXRwjJTIg0fPymKHXV6CuUwG%2FYRG9JYd1onJBbtOVLGI5al1NXqF46KUZ3Mpfe34UQp0bRgQJDbPc6IEAVNp47B7kEqHdQ%2F38uxsppXueh1TLB3F%2FQOsbaL1P&X-Amz-Signature=93e232a1c7c9fca8d85699bacde92d6a2b783c2239efff381c44521a363bfad8&X-Amz-SignedHeaders=host&x-id=GetObject)

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0e516edc-7551-4792-ab18-0494db3c4c0c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VANTWVSM%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T141343Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF0aCXVzLXdlc3QtMiJHMEUCIQDxZ0hjxr59nyazRuSZbGGm0uQBP2dyWkz5zrtqZpRMgAIgGLicnOTvuZt4%2BNQNgw6iYpKDff58z1lUFDZ2%2FF8jnggq%2FwMIdhAAGgw2Mzc0MjMxODM4MDUiDEIjSo%2FDlJVRBEvYvyrcA23sNl58tDg1Jcu0GbLFWSsn%2Bqj5yn9KPGLFgPCExHDmbmD43DZG7gojTrMAd5xQ9ROCcmXNHE0qDEmNFuuGDxEScdaTqRE9%2BcPI28ouQ4JCtOCN4maL1OTo%2FB9MxqabMZpryGUdtjHC5Im5ec2%2BtO%2B6HyS%2BE69W90jg5e9T3f%2BMBaJZskshCHsiSGzwGSn%2B%2BRVXWCv45AQosJtRClS5X5mrwBf1xO1AbiPPHcWweKB252IUgmcFJX6L4go94rBg6YR6QMmjYUvGhv%2FP326OkIZ40Y4lwNaaUqEk6cvGNX3tFwEdyWQWhPbd3iBbCRnZxKfMHmoeklJGdjagIL%2FriOr8ZaKo2Mkc7vS2UttDeGJ%2BBGXqdr7CVB%2FtrXGxhk217h8uLlJQQYMzRmq%2FgYxHtnsE0bwlHHyA45qDo2qreMJytswnGl7vAW3OhFP1Kqupx6GYaL8xuQxwVvgX5ZjFTfXBGC%2FKWGB8lDXyeeIMzWahKmpbki62KKXQiZ8HMJ7QcBcfRSgCm3WZrlH3nJWAbBodb7tIOgWiwdN%2FE3Vx04mNybyu%2FngFnc3VDbi3UnOEacgiX1kQ2EzMWX0fp5Lahbf5YwtsZaMjRq%2F32etJCyduCUcwQLPk9KgFCzcaMO2KmL0GOqUB8clcMsKE0AhGRm1t2SEDCIYcfJ8v4pfS%2B%2B5CT%2FVrxnL6LvChOWRfqjxqHSEwr2GBetTISGzxws78c%2FdQuEccl9TovHiNxjlsDIDAydHgRXxjjSJ97bKky0FPaaKRUcu7QgBd2HCIuTC66MdtVSvIWJmBBczmKn6vP69q92yaZlYMvR2p7SXtXj3k912B5QqEzWRfUZ92TJBIGDoGDzgjeshw1qNK&X-Amz-Signature=41f3a67d3160e3133b9f1c5c023a4fda7e16667774d505342a984171ef8d6c48&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23a79b9d-2356-49a9-8fd9-65c6b0ab2cc5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UKFW563W%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T141342Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF0aCXVzLXdlc3QtMiJHMEUCIQCJWFcv64G82vfJ5xMJ%2FNgqp%2BSQOWv%2BpCyFYjmRYFQvHwIgBKnmPQZe6KkDCA2g8Li77R7akcKdWrwsA64tN6sL4Jkq%2FwMIdhAAGgw2Mzc0MjMxODM4MDUiDBt1GpilGYFwOtkZsSrcA%2FV%2BdEob%2BZS1OnhzwL53p5wBwDwsLkBrbFW93Jnho6W7HZQ1NXI%2F4htbn%2FZXwwzIXukYz%2FTJ6mn3Glo1B232plVCnuKzZ07svIqyzfaZ8BtPy2zUO6fVAPb3emmsZydASSHzPrizo3iNaPoiLR9eBAiAI4XOcUyV7TF4jtQWhUQBKkDam0Xmkli%2Bv%2BBLGUuBqsrTngMcgRMTBeL4tkI12TqzGW1Nkj6kbYblomDUpzqeJFD6KlNhXiA4eKLbJR7teT7DH5ra20azLosbtlPcO%2Fre%2FYzLr0U3MYFwoXuHVfz6XnncfvEvVrsYoOQwVG0Rg1QmyCt4qUrdrAp5DlI%2BXzardjS6L9qyEd3rPxUx3geUoxFetZQk34fDIU81dvqZgQAacRGrV%2B6vL4HWNS3pFPEavQ6yfUIhOye7o1UvMoRiRVi%2BdS5GDuktujQlBe5BwRPBQ1RgTfj9BKVpHpujKpn2oYZ3sTjq%2BkFvc59LahWJVJqgre8JaIFLZaRFBew0tSmUwVv11qQuWqXMFSa1lOzsMgnIdZcIiN0%2B1qoCLlCHWwNHnkNRpWAqv%2FKBUEBIN7zVcd9zkYttbFIFTeUklOuXIwJZO3stgmiDehWvZDQ65cbafybqPCQw3UO2MJ6LmL0GOqUBRzhnHs5KRkRpPz2U4Vmz1%2FhO%2FX%2Bk4XiQFZLzxm6hrUTB%2Bg5qUNBKa%2B3btn0to95mWZCixDEak0OG6QdjGVmu6C0S0G8WSe4Az1g9XQWqOTPuHFVvOKw2%2BexzEd1vgs7rWiQIQmYWnAlO9YkJr8qaZUVSxzg7TAo2HveqqlzaSRXW1rsZeHxJjZqt4XazLINTDcLXgjjdwwyHRgRcubCQdrIhVEuO&X-Amz-Signature=c9a287293704cc7c794aedadd37edc20b5060343588d27e1ec2fcc108dab3f99&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 4. KDE Plot
A Kernel Density Estimate (KDE) plot is a graph that creates a probability distribution curve for the data based upon its likelihood of occurrence on a specific value. This is created for a single vector of information.
**Syntax:**
```python
sns.kdeplot(X) || sns.kdeplot(df['age'])
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0d571213-2a2f-4921-a50b-880847aa05ee/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UKFW563W%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T141342Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF0aCXVzLXdlc3QtMiJHMEUCIQCJWFcv64G82vfJ5xMJ%2FNgqp%2BSQOWv%2BpCyFYjmRYFQvHwIgBKnmPQZe6KkDCA2g8Li77R7akcKdWrwsA64tN6sL4Jkq%2FwMIdhAAGgw2Mzc0MjMxODM4MDUiDBt1GpilGYFwOtkZsSrcA%2FV%2BdEob%2BZS1OnhzwL53p5wBwDwsLkBrbFW93Jnho6W7HZQ1NXI%2F4htbn%2FZXwwzIXukYz%2FTJ6mn3Glo1B232plVCnuKzZ07svIqyzfaZ8BtPy2zUO6fVAPb3emmsZydASSHzPrizo3iNaPoiLR9eBAiAI4XOcUyV7TF4jtQWhUQBKkDam0Xmkli%2Bv%2BBLGUuBqsrTngMcgRMTBeL4tkI12TqzGW1Nkj6kbYblomDUpzqeJFD6KlNhXiA4eKLbJR7teT7DH5ra20azLosbtlPcO%2Fre%2FYzLr0U3MYFwoXuHVfz6XnncfvEvVrsYoOQwVG0Rg1QmyCt4qUrdrAp5DlI%2BXzardjS6L9qyEd3rPxUx3geUoxFetZQk34fDIU81dvqZgQAacRGrV%2B6vL4HWNS3pFPEavQ6yfUIhOye7o1UvMoRiRVi%2BdS5GDuktujQlBe5BwRPBQ1RgTfj9BKVpHpujKpn2oYZ3sTjq%2BkFvc59LahWJVJqgre8JaIFLZaRFBew0tSmUwVv11qQuWqXMFSa1lOzsMgnIdZcIiN0%2B1qoCLlCHWwNHnkNRpWAqv%2FKBUEBIN7zVcd9zkYttbFIFTeUklOuXIwJZO3stgmiDehWvZDQ65cbafybqPCQw3UO2MJ6LmL0GOqUBRzhnHs5KRkRpPz2U4Vmz1%2FhO%2FX%2Bk4XiQFZLzxm6hrUTB%2Bg5qUNBKa%2B3btn0to95mWZCixDEak0OG6QdjGVmu6C0S0G8WSe4Az1g9XQWqOTPuHFVvOKw2%2BexzEd1vgs7rWiQIQmYWnAlO9YkJr8qaZUVSxzg7TAo2HveqqlzaSRXW1rsZeHxJjZqt4XazLINTDcLXgjjdwwyHRgRcubCQdrIhVEuO&X-Amz-Signature=3e47af6a43c658bb79e9eca9fc9ea02728266199edd7015222021c412bbdd5cc&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/53752550-ef82-4ca9-a01a-09921f0282d0/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UKFW563W%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T141342Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF0aCXVzLXdlc3QtMiJHMEUCIQCJWFcv64G82vfJ5xMJ%2FNgqp%2BSQOWv%2BpCyFYjmRYFQvHwIgBKnmPQZe6KkDCA2g8Li77R7akcKdWrwsA64tN6sL4Jkq%2FwMIdhAAGgw2Mzc0MjMxODM4MDUiDBt1GpilGYFwOtkZsSrcA%2FV%2BdEob%2BZS1OnhzwL53p5wBwDwsLkBrbFW93Jnho6W7HZQ1NXI%2F4htbn%2FZXwwzIXukYz%2FTJ6mn3Glo1B232plVCnuKzZ07svIqyzfaZ8BtPy2zUO6fVAPb3emmsZydASSHzPrizo3iNaPoiLR9eBAiAI4XOcUyV7TF4jtQWhUQBKkDam0Xmkli%2Bv%2BBLGUuBqsrTngMcgRMTBeL4tkI12TqzGW1Nkj6kbYblomDUpzqeJFD6KlNhXiA4eKLbJR7teT7DH5ra20azLosbtlPcO%2Fre%2FYzLr0U3MYFwoXuHVfz6XnncfvEvVrsYoOQwVG0Rg1QmyCt4qUrdrAp5DlI%2BXzardjS6L9qyEd3rPxUx3geUoxFetZQk34fDIU81dvqZgQAacRGrV%2B6vL4HWNS3pFPEavQ6yfUIhOye7o1UvMoRiRVi%2BdS5GDuktujQlBe5BwRPBQ1RgTfj9BKVpHpujKpn2oYZ3sTjq%2BkFvc59LahWJVJqgre8JaIFLZaRFBew0tSmUwVv11qQuWqXMFSa1lOzsMgnIdZcIiN0%2B1qoCLlCHWwNHnkNRpWAqv%2FKBUEBIN7zVcd9zkYttbFIFTeUklOuXIwJZO3stgmiDehWvZDQ65cbafybqPCQw3UO2MJ6LmL0GOqUBRzhnHs5KRkRpPz2U4Vmz1%2FhO%2FX%2Bk4XiQFZLzxm6hrUTB%2Bg5qUNBKa%2B3btn0to95mWZCixDEak0OG6QdjGVmu6C0S0G8WSe4Az1g9XQWqOTPuHFVvOKw2%2BexzEd1vgs7rWiQIQmYWnAlO9YkJr8qaZUVSxzg7TAo2HveqqlzaSRXW1rsZeHxJjZqt4XazLINTDcLXgjjdwwyHRgRcubCQdrIhVEuO&X-Amz-Signature=154524eb5ea48d9472afd7534cb42fd20c48f3b8a117c1d9286d3ef9e518a1bf&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
## 4. Correlation Between Variables
Correlation is a statistical measure of the extent to which different variables are interdependent. It indicates how changes in one variable are associated with changes in another variable over time.
### Positive Correlation
Positive correlation indicates that as one variable increases, the other variable also tends to increase.
**Example: Engine Size and Price**
- **Positive Correlation:** Engine size increases, price also increases.
- **Visualization:** Scatter plot with a steep positive slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c7ea9b0-3ef3-4357-a9c3-554fc71b6b15/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46657YBWDIX%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T141343Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF0aCXVzLXdlc3QtMiJGMEQCID4IVH3dHyukymHaESFdt9XMU2rDYzP3blotlxnsG%2FRCAiBaHJl6Oqp5OQg7xDmbMmvtoGQZi8fAp6JwnWHkNzV0dCr%2FAwh2EAAaDDYzNzQyMzE4MzgwNSIMmGlYSfOoFpoxJ%2FeIKtwDYtEgrbEnqaTGsaapvfxKylWwQrs%2FYtd9XZF%2FFRi%2Fdg4MLxvRo1K3TKudvx1vWo%2FDKLb7UR%2FG6HS6DS3INqfMO1GITJSILL5%2BXExLTH6RtgPDf29ie%2F0tqpUVKeJb%2BMd8DhOLN50NHbqoVveG9NgcJc7BASjb%2FPuafbztAPc9czfsPifiQsQ%2Ffcb126zBcGTu6o2v3QK27wAdy0EY%2BwOXqXUaW2Az2LQtMqQhM0MM%2BM3qcgf%2FF4EtQnnvrIC6yHHpe1sfsXG3upo3Rw3z5JBZjb%2B9Y0cLJFjt%2B613xBU8qRYm7U3yzo5voMirATkwXaRFr%2FeJ0HwHPUs0a%2FYGNDd0L%2Fh9%2BGgy99ZjadxwlWh3vABVf7%2FMa5LktoiN3GwMndyiXQGV8jsHb3gYWhl88GXj2K9Wt4iKbGC43x03JMmFkU6k3kM07QKNXnEVLQVKXcy6nCxl0UceXfPsCE7I0DLJvm0s7Yi8J0cLaaAzp3YqJxS8YFN0AY3G2Hvkq8ym9wobCDkMdMAP3dd9gRylywssgLDHdzdkG4Vbr8nDbR84rimbeSM8XnpkALLj0X2q5n69lTnuM2llJ4vJEZygJsOhp1WfD75KoJYcGQCmqFDr1HheWyoEQT%2F1pvC078ow4IuYvQY6pgGNjBbPoIyt2woszz4skKn0DyWa1WsRIZI8cfheO2tnxIM8AoTf1lyleoyJ5rzGBIEo3YxRUyklsOyO0H8cBYRC38%2Bx%2BRSD3yiZfaV5lKd%2BCk%2BriFrO3pXiqm1KtAGDjpZGdKNkMxbnP9wrlKQ5WCG7izNLyB5p4vlRNCnvseHlg%2Fr5F1Bv%2BgNbaEITn6%2BStmIZXnTPSx%2BHwyvgUTimZOA0ypVH2WW3&X-Amz-Signature=1194a5a26228b1a200340a615e53782ee159bec2de4d5ac1a98c4f02b44e0be2&X-Amz-SignedHeaders=host&x-id=GetObject)
**Explanation:** When engine size increases, there is a corresponding increase in the price of the vehicle. This positive correlation suggests that larger engines tend to be associated with higher prices in the market.
___
### Negative Correlation
Negative correlation indicates that as one variable increases, the other variable tends to decrease.
**Example: Highway Miles per Gallon and Price**
- **Negative Correlation:** As highway miles per gallon increases, price decreases.
- **Visualization:** Scatter plot with a steep negative slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/10f1f798-9cc4-4df2-a9c1-5a339f554a0b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46674B3UP43%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T141343Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF0aCXVzLXdlc3QtMiJHMEUCIQDEZMJcCLWFK3eW04CZk0MtiyY5yw0tEpQ7i2U4dHRxsgIgGn%2Fp7poPJc3dRw4yeR%2FjpXF9%2BOCChhJeEnHHVLQrDzcq%2FwMIdhAAGgw2Mzc0MjMxODM4MDUiDEVVmYXi0cKM7qhQUircAyIOVH9IgvEzuHNXVik9oJIjNeCrdIVM7K%2Bk8haXgK3m2Op03ipWBMQI062Y1tfy%2BwK3RPULxxGEasM0jJa4JeTyy3JQQ43rS9%2F4i8Gec6fcGG23pXtjYyYXgs7T6oI0QwTdINK7DCvGoAAFOYHEySDYvjZaPWAP%2BJhNwZEMrwuve%2FCiJsku0jCXRZBHSXyx1InjoEF65rgK8U4MI4km%2BLOPw%2B%2BJUnMIM3MpgL%2BZYA4ycXqb3ny1QNi1au7bl%2BDCLAcS%2F0iinrv%2BZe0oSHr8slcwusUpNHnPCKl2gvqWz%2FKTYCGNrUAi6%2BoC1MtKtM9JCCwYYjtABucGVw6yWtxIXZkfQlP8sKtxjH0mkMMqwJYihJ65C%2F%2BSZ73QqWJVAl4AtODw1hsnWTin4kwPrJKDCQ7hQPBl4Xp11ZL8c2nNHtPFqbjtaVNoTI3fmr19wxB98iruTflPeY08vFBm1OaUMDL7QZ6dV8YckglL59SQuOlOZ6x8BaUFSobYnCqc7n0w7UDje%2FY%2B3NgPwpZlHiMZ2Ojnk0OwrVO04bpwg9gLHRGoMrsp2YAd3eJZNUhqgaqG%2Bu8o3ZM5NzuNKzMWvabS0s01naWFrOJ0xRSQad6BmOmy6phYe9owMBRE19hTMKqLmL0GOqUB5OFe2O2xrnjMKZqLgjGzM%2BgMKoqDtT5Jbj1hGtlwhDtvzFULkX%2FBnsCftGgGCRx6FaVHNFkXkL6erx5zFiP66ATsEpxT1oNpoMj1beh7ucP4L%2Bnsd4uh6rh8dZQJ3hpTvFo1ZNtxr0l%2F6pma1HdBjOIwlMKeAJgnLsboYOVZsqtDFS5doykQjiH8HRoUFkbqJgojpdn49QxR%2B46TTJPJ%2FmegceSV&X-Amz-Signature=368a3d171be812dafc09090bdacfffe5d4e9e7f0ad0c406bbf050a8c02863506&X-Amz-SignedHeaders=host&x-id=GetObject)
**Explanation:** When highway miles per gallon increases, the price of the vehicle tends to decrease. This negative correlation suggests that cars with higher fuel efficiency (more miles per gallon) are generally priced lower in the market.
___
### Weak Correlation
Weak correlation indicates a lack of strong relationship between the variables.
**Example: RPM and Price**
- **Weak Correlation:** Low and high RPM values show varied prices, indicating no strong predictive relationship.
- **Visualization:** Scatter plot with no clear trend or slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9f914514-8914-4bf4-ac84-d9e3077f6eb1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466X7BLMIOY%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T141343Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF0aCXVzLXdlc3QtMiJHMEUCIQDEa62bJ3VuNJkhBFEt0nFTRFUWS5PNDcbdNanMinJerAIgE35i89lWI2SCRQInu%2FpGAw7t42ELRCnWQX3rn1I5mpsq%2FwMIdhAAGgw2Mzc0MjMxODM4MDUiDDc8HIoI%2BygolygupircA1lP%2FJBSNnJ3OxaSlP82zKjRFz%2F6xKgGGkWd0dnmLNW%2BXjoBHjw0uHjzYTUV2vpLmF57w1Tqzan5SWXBNm0JkS5BoZgecq5GK2GDxY4BFHHJgHPnbeVTV4DXXY70gXsOtjUE5lekNawhb%2Bc9C1pcSH6isz1L4Hf7YpUaqBtiPTiYDHxWxqXppESPCgwQHuq6UMIyWgCKHWgJX%2F8dvyhEyB1h0MkJWwQUrboAzxylzXMdVtE8tJUP0MqLW9M%2BTEDyvqasTfL7vphTMnvQ7RvVKGLOaxJ3rvOjiaJW7GdZ0dE1Y2qUSQlPFDGL%2BBCPr6M9v9cFkk3JgYgOLXm9GtSLzuInvCRGExzouY6ikobnidd7OPSqrC8R2iLugltxlyeE8WndpTQgcfF7QESxvx7rtBzPH4JOsyLgqoWEgA2TXP7wgT28DqffRpGZR2SgnjCYxLZDdKg2Zya9RAoBuaEYIY50FmN3ICyfW1qNPvObuqVnhw%2F64QtWJLDLw6jAiEyvGSiSu97Th8xivwLxpqgB2s79b%2Fwj%2ByGLJwfG52hKWvQ5R%2FpZ6lHaPDtaXIPMdL75Yh%2BWtb2aH0pkcycC1MvnYGzxWE5Pclya9UTUyBQ%2BW2Yy0Z67pMABy6bSg1snMN%2BKmL0GOqUBlWrdKF5QDGn5nP1J3QG3R8YnZqX9d6Da23fkc2r0H4Bv74jbjTTW0Dvnk6gDmvU0dUCO6f2hEKpcKUJMNfI5f3N7fWTsnRhbO532nlfqiQFYJPYeJZs1Q80wq2o8zKiIDuCTQ1QSK0GtuQos%2F%2BfLmqCwZSY6y%2B%2BkiD3eUdw%2BO3iXwjXwn1YE7bRZtRQTMA2F52X0En4i6yOsQwZxiNEwXdJeaULF&X-Amz-Signature=1aee5cd47c7bfd81fc3fdfec3d9f3eeef6e4c753eb4a1d76fdf2ee8e1c27905e&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f18086e5-5b04-4fbf-8309-8944ab20d213/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZT5ZEVK7%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T141342Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF0aCXVzLXdlc3QtMiJHMEUCIQCBTOAQ0cOngDxy9DXqqYBm3DVo07dOPBnsJWBj0NoaJAIgN72VoIzNY%2B0z8a6qDMI%2B%2FLUhOdep8KNHrp%2FosbQjptAq%2FwMIdhAAGgw2Mzc0MjMxODM4MDUiDL1SWo4MDBjhPIPAzircA3z8fL%2Boi6%2FZOku%2BIYnkWwGi54C0hC5p7%2BDM8e42TohMYVn2bxN8%2BvJWd1s9BYqdP7cCgNqfzP3v4y8KedckT9fQ1bTaS4Ae%2FB6A9XS%2BQdsCHFbq2Et1gDUAhlqyTgqmHRs47BHBNx0ZJ0H3cBL38M9OhpRC%2ByHTfhC8x8dqW%2FW4Kp2Vsi%2B0JV9ZG9rH1E2uiz9r2QP7xOtNzyE5WYTH1YiKhsFIeTt7L0qsM39Ep%2B3ubC4K6ebTqYQdJkN0KT%2FQ6CY3ZEr7L4r7FihxuCU%2Bu%2FYuzewhRObBArlLbQuQjlhkQfKrjxtJg06M6ZJE%2BOvu%2FAHv1Ix%2FFNlYOOtIikvK2yZIl%2FKDMImylQNYbhbPvYeDMc%2BWcbuCEUeneEWqIvloWRta6X6VF46RNxq0OGodfCzFbpIdTBLp6%2BRAQs9xBLFCIQgsenL79Rx61i7R3OQg%2FW0TuqGopQMokF6RdeUGjjkwRkzBgwMXQzmt7nL%2F4atxddRO1ZhNO0D3UMfx0Y9pRkgv1VgKGio3NoG9Fy6zd409WewRI%2FCcVdgXnE8ttE65jOmNVgtdG%2Bgf%2FLVK1ESTq9cpWv61rEf1pt1FPwzaOBEZRc3LAFvX4YLYcVq3U%2BodhP1Cfkq9pBxxz81%2BMLaLmL0GOqUBxf%2FZvCkm1d0QoTP%2F0KkhyYlCRm6w51QPZXqqeabW1W1PRjGIXZHmxMqb2AwT9rqKvp6fr0e3w93ePe2KIGMpOWLrth777BK4M0YxNdegWdYDTdAdEANL7lISG7ymLWkQzBQX%2B629O3jF9GWhNw28eokctNwhC3CiL%2BI4SA%2Fa4pAthuZHxIZbUGxJGFoQ39lt94D1dTOTHINusplLHy2LSpElX8FT&X-Amz-Signature=07a302e3264750489a802de45a00e03b3c172342cd0bea0f0aeb84ba249ebd3f&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Correlation Plot
Heatmap visualizes correlations among variables. Color scheme indicates Pearson correlation coefficients. Dark red diagonal line shows perfect correlation (value of 1) between variables and themselves.
This heatmap offers overview of variable relationships and their link with price.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cd3b341e-cc1a-45f7-8aec-cdc00436d270/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZT5ZEVK7%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T141342Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF0aCXVzLXdlc3QtMiJHMEUCIQCBTOAQ0cOngDxy9DXqqYBm3DVo07dOPBnsJWBj0NoaJAIgN72VoIzNY%2B0z8a6qDMI%2B%2FLUhOdep8KNHrp%2FosbQjptAq%2FwMIdhAAGgw2Mzc0MjMxODM4MDUiDL1SWo4MDBjhPIPAzircA3z8fL%2Boi6%2FZOku%2BIYnkWwGi54C0hC5p7%2BDM8e42TohMYVn2bxN8%2BvJWd1s9BYqdP7cCgNqfzP3v4y8KedckT9fQ1bTaS4Ae%2FB6A9XS%2BQdsCHFbq2Et1gDUAhlqyTgqmHRs47BHBNx0ZJ0H3cBL38M9OhpRC%2ByHTfhC8x8dqW%2FW4Kp2Vsi%2B0JV9ZG9rH1E2uiz9r2QP7xOtNzyE5WYTH1YiKhsFIeTt7L0qsM39Ep%2B3ubC4K6ebTqYQdJkN0KT%2FQ6CY3ZEr7L4r7FihxuCU%2Bu%2FYuzewhRObBArlLbQuQjlhkQfKrjxtJg06M6ZJE%2BOvu%2FAHv1Ix%2FFNlYOOtIikvK2yZIl%2FKDMImylQNYbhbPvYeDMc%2BWcbuCEUeneEWqIvloWRta6X6VF46RNxq0OGodfCzFbpIdTBLp6%2BRAQs9xBLFCIQgsenL79Rx61i7R3OQg%2FW0TuqGopQMokF6RdeUGjjkwRkzBgwMXQzmt7nL%2F4atxddRO1ZhNO0D3UMfx0Y9pRkgv1VgKGio3NoG9Fy6zd409WewRI%2FCcVdgXnE8ttE65jOmNVgtdG%2Bgf%2FLVK1ESTq9cpWv61rEf1pt1FPwzaOBEZRc3LAFvX4YLYcVq3U%2BodhP1Cfkq9pBxxz81%2BMLaLmL0GOqUBxf%2FZvCkm1d0QoTP%2F0KkhyYlCRm6w51QPZXqqeabW1W1PRjGIXZHmxMqb2AwT9rqKvp6fr0e3w93ePe2KIGMpOWLrth777BK4M0YxNdegWdYDTdAdEANL7lISG7ymLWkQzBQX%2B629O3jF9GWhNw28eokctNwhC3CiL%2BI4SA%2Fa4pAthuZHxIZbUGxJGFoQ39lt94D1dTOTHINusplLHy2LSpElX8FT&X-Amz-Signature=257039f1c5ae5a0518f57a538301052aa65fe83bf3395929e9dfb29ed566a1c3&X-Amz-SignedHeaders=host&x-id=GetObject)

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
