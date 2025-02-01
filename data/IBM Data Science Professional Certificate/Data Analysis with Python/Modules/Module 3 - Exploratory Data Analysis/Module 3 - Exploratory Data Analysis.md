

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7e6d594d-952e-44b6-97ea-31225882aea6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T5RPOR4G%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T051322Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCrRV9RaiHmEhSQINbp1Pfv4%2FQ81J2w7amqY4h%2BhI2BDwIhAMlAeksGi0YDRvq1ASBrKWWePRl2wmG59Iuw519Pfpy0KogECM3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igy7BnTN6Tq1Ve1G02oq3ANplLXNlUmTIHPIOikH0QwLlDbbfmU84vd0QYI3hXGW1OGZp76508zS7VWP7tfXHeJxTGvKESCaV8nGZ05qnu4vH63hLJ%2FbU1Nsj4pbf1cR%2BRWlDv1bYD4Pp9D5tvsk%2B%2BeCiBEnBSrhoPGSGFjru%2FJ5oNQFoQSjc7c6%2F7gCTPozPJ7udya4%2Fu8YlMVhCqJcZ0gSIcXXWqaPoYL9tNev%2FZ3Lys4Q5XmeFgDzvMS3hysmGXJ9glzbpInV5IMBtrJTPci8UonMTThiXgf%2Fz3oQFcvmwwQIIFX2MYFNJzc2AX6xUlDCS2Y2Ju3kblbGL0az4EetszG9rIrsyjCymGzp55Lcjdy3RAA4JTwGdF0LrQXHELTUvvdEAQ%2FOJjDqs8FJEZPCHWFAzCmxyMW%2BkwwqoP28UrBSyuwLmQVFPmj4chqCETqLXoZ0sczPVtf4qatobbcveTJfIIsIBZ1VH6TxV3mTvQEvkABOhfFeBoyi5lRrgMFd01R6C1W7vcPHAqvsmJthtDaM9SpvUHx5XvHh1Mnzy%2FOAOuPPdzrXFjW4%2FAJPeaiBooh11ImbAxyVOuwzzMFmnNXefKXSf6oaPIGsQTUPvVlTQeCtdviVEPyQV5bEGK3r32%2FRLMb029L1CDDPwfa8BjqkATCBPCSr1moNsZMRoOkn7Z4owkYxqlpa51kNY6fdXfcesKcn70pM%2FW5APki2Z8R9w0%2BsJCc1ZlOfLIZS%2FHaT6WM32Q1uAdvPiGuqu6s%2Ftws%2FAWE1t%2FI4zbQfNIRroPQvTxIXwTzaqMg%2BYMoRIfEgc7k0wfY4arX4o61%2FWYntfRGIuOGLIQuP%2BeMd4r0TOol5u9Lm0sHBDL6zjrMYCc4WtNxu7sbU&X-Amz-Signature=e14dc14dbd4195b31f8e65ea4000995260e89876875948645a495d63bdc3c9ed&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cbfaed9e-b398-4902-8936-dea058b21def/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T5RPOR4G%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T051322Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCrRV9RaiHmEhSQINbp1Pfv4%2FQ81J2w7amqY4h%2BhI2BDwIhAMlAeksGi0YDRvq1ASBrKWWePRl2wmG59Iuw519Pfpy0KogECM3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igy7BnTN6Tq1Ve1G02oq3ANplLXNlUmTIHPIOikH0QwLlDbbfmU84vd0QYI3hXGW1OGZp76508zS7VWP7tfXHeJxTGvKESCaV8nGZ05qnu4vH63hLJ%2FbU1Nsj4pbf1cR%2BRWlDv1bYD4Pp9D5tvsk%2B%2BeCiBEnBSrhoPGSGFjru%2FJ5oNQFoQSjc7c6%2F7gCTPozPJ7udya4%2Fu8YlMVhCqJcZ0gSIcXXWqaPoYL9tNev%2FZ3Lys4Q5XmeFgDzvMS3hysmGXJ9glzbpInV5IMBtrJTPci8UonMTThiXgf%2Fz3oQFcvmwwQIIFX2MYFNJzc2AX6xUlDCS2Y2Ju3kblbGL0az4EetszG9rIrsyjCymGzp55Lcjdy3RAA4JTwGdF0LrQXHELTUvvdEAQ%2FOJjDqs8FJEZPCHWFAzCmxyMW%2BkwwqoP28UrBSyuwLmQVFPmj4chqCETqLXoZ0sczPVtf4qatobbcveTJfIIsIBZ1VH6TxV3mTvQEvkABOhfFeBoyi5lRrgMFd01R6C1W7vcPHAqvsmJthtDaM9SpvUHx5XvHh1Mnzy%2FOAOuPPdzrXFjW4%2FAJPeaiBooh11ImbAxyVOuwzzMFmnNXefKXSf6oaPIGsQTUPvVlTQeCtdviVEPyQV5bEGK3r32%2FRLMb029L1CDDPwfa8BjqkATCBPCSr1moNsZMRoOkn7Z4owkYxqlpa51kNY6fdXfcesKcn70pM%2FW5APki2Z8R9w0%2BsJCc1ZlOfLIZS%2FHaT6WM32Q1uAdvPiGuqu6s%2Ftws%2FAWE1t%2FI4zbQfNIRroPQvTxIXwTzaqMg%2BYMoRIfEgc7k0wfY4arX4o61%2FWYntfRGIuOGLIQuP%2BeMd4r0TOol5u9Lm0sHBDL6zjrMYCc4WtNxu7sbU&X-Amz-Signature=72003653c77c730f2ab7021431cf80542c3bca31b0163f5331e5a24d3fc11eed&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/91181646-b1e0-4433-9711-6259a96a9247/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T5RPOR4G%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T051322Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCrRV9RaiHmEhSQINbp1Pfv4%2FQ81J2w7amqY4h%2BhI2BDwIhAMlAeksGi0YDRvq1ASBrKWWePRl2wmG59Iuw519Pfpy0KogECM3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igy7BnTN6Tq1Ve1G02oq3ANplLXNlUmTIHPIOikH0QwLlDbbfmU84vd0QYI3hXGW1OGZp76508zS7VWP7tfXHeJxTGvKESCaV8nGZ05qnu4vH63hLJ%2FbU1Nsj4pbf1cR%2BRWlDv1bYD4Pp9D5tvsk%2B%2BeCiBEnBSrhoPGSGFjru%2FJ5oNQFoQSjc7c6%2F7gCTPozPJ7udya4%2Fu8YlMVhCqJcZ0gSIcXXWqaPoYL9tNev%2FZ3Lys4Q5XmeFgDzvMS3hysmGXJ9glzbpInV5IMBtrJTPci8UonMTThiXgf%2Fz3oQFcvmwwQIIFX2MYFNJzc2AX6xUlDCS2Y2Ju3kblbGL0az4EetszG9rIrsyjCymGzp55Lcjdy3RAA4JTwGdF0LrQXHELTUvvdEAQ%2FOJjDqs8FJEZPCHWFAzCmxyMW%2BkwwqoP28UrBSyuwLmQVFPmj4chqCETqLXoZ0sczPVtf4qatobbcveTJfIIsIBZ1VH6TxV3mTvQEvkABOhfFeBoyi5lRrgMFd01R6C1W7vcPHAqvsmJthtDaM9SpvUHx5XvHh1Mnzy%2FOAOuPPdzrXFjW4%2FAJPeaiBooh11ImbAxyVOuwzzMFmnNXefKXSf6oaPIGsQTUPvVlTQeCtdviVEPyQV5bEGK3r32%2FRLMb029L1CDDPwfa8BjqkATCBPCSr1moNsZMRoOkn7Z4owkYxqlpa51kNY6fdXfcesKcn70pM%2FW5APki2Z8R9w0%2BsJCc1ZlOfLIZS%2FHaT6WM32Q1uAdvPiGuqu6s%2Ftws%2FAWE1t%2FI4zbQfNIRroPQvTxIXwTzaqMg%2BYMoRIfEgc7k0wfY4arX4o61%2FWYntfRGIuOGLIQuP%2BeMd4r0TOol5u9Lm0sHBDL6zjrMYCc4WtNxu7sbU&X-Amz-Signature=6251bc31beeda2fba68a367666ee0432cea316e18a36f499eb8fb84229512fd0&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/09aba1c0-0d55-41dd-852a-a04c5b8a3fac/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SGG3G6KG%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T051322Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIATJCtOGxGWAFAcwqw349FgIu4ih3SimOaN6t%2B3yv0odAiEA%2FAadXT%2Bd%2Bx0CGGXOigiI6W4r1vxOCeHc4KtkD8IspcgqiAQIzf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMLx1z6R07Hf%2F2dYwSrcA4glT9QYlSRroH6B30XTXky1OxklquPVOgJEE%2FxsyJCZFiImBIMSu7srmNAJyzFyKbFAYj56T2H5R604UYZueS%2BmlB%2BU%2Bs2HB5bc8vKNuaIOHrvi1cwbRB1xNc2QlMR0lwd7XczQHFtmrdQYh57F%2F0LwOw6KpqxAn3nN%2FSfH9lLM157OwnnYzrL%2Fn0lGHQQ7bATV%2BbhEOrXqa7vcV4g1Ntj1%2BLRwq2Q9aCyMKj7AbtIFgIS3h1h6qpgWcMFsVKMqtMkWEHjjCGwfQsyNnOmt53fGFoKfUFOw3npcBLbEOVhtD7giKkaWSthYo6Kbh35fm46rLzaXaKktHzHMlfz8CR%2BP0zfqEaJXDhOQq2O2B%2BYyxzrMjDMK20bTNSYFmFvjWlWVstFBC5BBOrYA36cU5%2BkLq6NCfUR0LDOzTU7wQ%2Bg%2BZXMWiB%2BYklu%2B6WmkD6I6Iw%2BcAodHgpjB3F9jXzskT%2BqXe0l6KLc4tYokOAIKIuEWHbO3Gr5ky18qmURgrX%2BhlVjdt8S2lJSOxgN2pJq%2FmSuw2krwyE%2B%2BsGRSCgDoO%2BjGp4Z81C1XT%2FIonyJYOpve%2BR2H8uC15m9IHEOxakYvPxcCmjjTSKzfHwI31ip4DF0XOdarWY3FtzRHfOG%2BMOrB9rwGOqUBBgkWUBP%2BBqA8GqXz1wTjYMU2pRHwCj6APdjJL77QAkVpjxsfkZdFaoic%2FJL92OFnga105BMwkO4HjwpvAb1OFhX3lrrj5DeXSrVOuKZ4Xj4%2BxOb5F2EvQ4u18nsJjqr%2FanNpjdPy%2FSJMEg0t6MY9PhMDDUHGp1EIr%2BbJJa3pA3moGdmsfaQ6eA6Yn2nPrRKvLw7MDJ8P5S%2FGR%2F%2BXF6n0wzfznTFx&X-Amz-Signature=59336598ea4ff2ad1a8e21a2e870be6d0664c14032864a56dd41f98b88bbd789&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 2. Scatter Plot
Scatter plots present the relationship between two variables in a dataset. It represents data points on a two-dimensional plane. The independent variable or attribute is plotted on the X-axis, while the dependent variable is plotted on the Y-axis.
**Syntax:**
```python
plt.scatter(x, y)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23708af9-659f-4f23-b626-1a4292d7842c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SGG3G6KG%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T051323Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIATJCtOGxGWAFAcwqw349FgIu4ih3SimOaN6t%2B3yv0odAiEA%2FAadXT%2Bd%2Bx0CGGXOigiI6W4r1vxOCeHc4KtkD8IspcgqiAQIzf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMLx1z6R07Hf%2F2dYwSrcA4glT9QYlSRroH6B30XTXky1OxklquPVOgJEE%2FxsyJCZFiImBIMSu7srmNAJyzFyKbFAYj56T2H5R604UYZueS%2BmlB%2BU%2Bs2HB5bc8vKNuaIOHrvi1cwbRB1xNc2QlMR0lwd7XczQHFtmrdQYh57F%2F0LwOw6KpqxAn3nN%2FSfH9lLM157OwnnYzrL%2Fn0lGHQQ7bATV%2BbhEOrXqa7vcV4g1Ntj1%2BLRwq2Q9aCyMKj7AbtIFgIS3h1h6qpgWcMFsVKMqtMkWEHjjCGwfQsyNnOmt53fGFoKfUFOw3npcBLbEOVhtD7giKkaWSthYo6Kbh35fm46rLzaXaKktHzHMlfz8CR%2BP0zfqEaJXDhOQq2O2B%2BYyxzrMjDMK20bTNSYFmFvjWlWVstFBC5BBOrYA36cU5%2BkLq6NCfUR0LDOzTU7wQ%2Bg%2BZXMWiB%2BYklu%2B6WmkD6I6Iw%2BcAodHgpjB3F9jXzskT%2BqXe0l6KLc4tYokOAIKIuEWHbO3Gr5ky18qmURgrX%2BhlVjdt8S2lJSOxgN2pJq%2FmSuw2krwyE%2B%2BsGRSCgDoO%2BjGp4Z81C1XT%2FIonyJYOpve%2BR2H8uC15m9IHEOxakYvPxcCmjjTSKzfHwI31ip4DF0XOdarWY3FtzRHfOG%2BMOrB9rwGOqUBBgkWUBP%2BBqA8GqXz1wTjYMU2pRHwCj6APdjJL77QAkVpjxsfkZdFaoic%2FJL92OFnga105BMwkO4HjwpvAb1OFhX3lrrj5DeXSrVOuKZ4Xj4%2BxOb5F2EvQ4u18nsJjqr%2FanNpjdPy%2FSJMEg0t6MY9PhMDDUHGp1EIr%2BbJJa3pA3moGdmsfaQ6eA6Yn2nPrRKvLw7MDJ8P5S%2FGR%2F%2BXF6n0wzfznTFx&X-Amz-Signature=1b9782f48051d85f35b8c70d331283996d41d4de4d9e68f7b36ed45129daee0f&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 3. Histogram
A histogram is an important visual representation of data in categorical form. To view the data in a "Binned" form, use the histogram plot with a number of bins required or with the data points that mark the bin edges. The x-axis represents the data bins, and the y-axis represents the number of elements in each bin.
**Syntax:**
```python
plt.hist(x, bins)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/24e4424a-df87-40a1-b63b-195cbdc2e0ab/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SGG3G6KG%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T051323Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIATJCtOGxGWAFAcwqw349FgIu4ih3SimOaN6t%2B3yv0odAiEA%2FAadXT%2Bd%2Bx0CGGXOigiI6W4r1vxOCeHc4KtkD8IspcgqiAQIzf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMLx1z6R07Hf%2F2dYwSrcA4glT9QYlSRroH6B30XTXky1OxklquPVOgJEE%2FxsyJCZFiImBIMSu7srmNAJyzFyKbFAYj56T2H5R604UYZueS%2BmlB%2BU%2Bs2HB5bc8vKNuaIOHrvi1cwbRB1xNc2QlMR0lwd7XczQHFtmrdQYh57F%2F0LwOw6KpqxAn3nN%2FSfH9lLM157OwnnYzrL%2Fn0lGHQQ7bATV%2BbhEOrXqa7vcV4g1Ntj1%2BLRwq2Q9aCyMKj7AbtIFgIS3h1h6qpgWcMFsVKMqtMkWEHjjCGwfQsyNnOmt53fGFoKfUFOw3npcBLbEOVhtD7giKkaWSthYo6Kbh35fm46rLzaXaKktHzHMlfz8CR%2BP0zfqEaJXDhOQq2O2B%2BYyxzrMjDMK20bTNSYFmFvjWlWVstFBC5BBOrYA36cU5%2BkLq6NCfUR0LDOzTU7wQ%2Bg%2BZXMWiB%2BYklu%2B6WmkD6I6Iw%2BcAodHgpjB3F9jXzskT%2BqXe0l6KLc4tYokOAIKIuEWHbO3Gr5ky18qmURgrX%2BhlVjdt8S2lJSOxgN2pJq%2FmSuw2krwyE%2B%2BsGRSCgDoO%2BjGp4Z81C1XT%2FIonyJYOpve%2BR2H8uC15m9IHEOxakYvPxcCmjjTSKzfHwI31ip4DF0XOdarWY3FtzRHfOG%2BMOrB9rwGOqUBBgkWUBP%2BBqA8GqXz1wTjYMU2pRHwCj6APdjJL77QAkVpjxsfkZdFaoic%2FJL92OFnga105BMwkO4HjwpvAb1OFhX3lrrj5DeXSrVOuKZ4Xj4%2BxOb5F2EvQ4u18nsJjqr%2FanNpjdPy%2FSJMEg0t6MY9PhMDDUHGp1EIr%2BbJJa3pA3moGdmsfaQ6eA6Yn2nPrRKvLw7MDJ8P5S%2FGR%2F%2BXF6n0wzfznTFx&X-Amz-Signature=e0741570c2bb1965ba2daae4b58640f3d9b0a45e93103876f790c767d476b2f7&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ab5a6dfe-51f5-43ee-bcb3-33dae4a1c7ad/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SGG3G6KG%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T051322Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIATJCtOGxGWAFAcwqw349FgIu4ih3SimOaN6t%2B3yv0odAiEA%2FAadXT%2Bd%2Bx0CGGXOigiI6W4r1vxOCeHc4KtkD8IspcgqiAQIzf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMLx1z6R07Hf%2F2dYwSrcA4glT9QYlSRroH6B30XTXky1OxklquPVOgJEE%2FxsyJCZFiImBIMSu7srmNAJyzFyKbFAYj56T2H5R604UYZueS%2BmlB%2BU%2Bs2HB5bc8vKNuaIOHrvi1cwbRB1xNc2QlMR0lwd7XczQHFtmrdQYh57F%2F0LwOw6KpqxAn3nN%2FSfH9lLM157OwnnYzrL%2Fn0lGHQQ7bATV%2BbhEOrXqa7vcV4g1Ntj1%2BLRwq2Q9aCyMKj7AbtIFgIS3h1h6qpgWcMFsVKMqtMkWEHjjCGwfQsyNnOmt53fGFoKfUFOw3npcBLbEOVhtD7giKkaWSthYo6Kbh35fm46rLzaXaKktHzHMlfz8CR%2BP0zfqEaJXDhOQq2O2B%2BYyxzrMjDMK20bTNSYFmFvjWlWVstFBC5BBOrYA36cU5%2BkLq6NCfUR0LDOzTU7wQ%2Bg%2BZXMWiB%2BYklu%2B6WmkD6I6Iw%2BcAodHgpjB3F9jXzskT%2BqXe0l6KLc4tYokOAIKIuEWHbO3Gr5ky18qmURgrX%2BhlVjdt8S2lJSOxgN2pJq%2FmSuw2krwyE%2B%2BsGRSCgDoO%2BjGp4Z81C1XT%2FIonyJYOpve%2BR2H8uC15m9IHEOxakYvPxcCmjjTSKzfHwI31ip4DF0XOdarWY3FtzRHfOG%2BMOrB9rwGOqUBBgkWUBP%2BBqA8GqXz1wTjYMU2pRHwCj6APdjJL77QAkVpjxsfkZdFaoic%2FJL92OFnga105BMwkO4HjwpvAb1OFhX3lrrj5DeXSrVOuKZ4Xj4%2BxOb5F2EvQ4u18nsJjqr%2FanNpjdPy%2FSJMEg0t6MY9PhMDDUHGp1EIr%2BbJJa3pA3moGdmsfaQ6eA6Yn2nPrRKvLw7MDJ8P5S%2FGR%2F%2BXF6n0wzfznTFx&X-Amz-Signature=934e4aecc90f52bf9932b235158c2acbc7a8719221666c730919c2b9091a1b60&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8f1b1d60-cf1b-42b3-9faa-f634c89c3f84/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SGG3G6KG%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T051323Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIATJCtOGxGWAFAcwqw349FgIu4ih3SimOaN6t%2B3yv0odAiEA%2FAadXT%2Bd%2Bx0CGGXOigiI6W4r1vxOCeHc4KtkD8IspcgqiAQIzf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMLx1z6R07Hf%2F2dYwSrcA4glT9QYlSRroH6B30XTXky1OxklquPVOgJEE%2FxsyJCZFiImBIMSu7srmNAJyzFyKbFAYj56T2H5R604UYZueS%2BmlB%2BU%2Bs2HB5bc8vKNuaIOHrvi1cwbRB1xNc2QlMR0lwd7XczQHFtmrdQYh57F%2F0LwOw6KpqxAn3nN%2FSfH9lLM157OwnnYzrL%2Fn0lGHQQ7bATV%2BbhEOrXqa7vcV4g1Ntj1%2BLRwq2Q9aCyMKj7AbtIFgIS3h1h6qpgWcMFsVKMqtMkWEHjjCGwfQsyNnOmt53fGFoKfUFOw3npcBLbEOVhtD7giKkaWSthYo6Kbh35fm46rLzaXaKktHzHMlfz8CR%2BP0zfqEaJXDhOQq2O2B%2BYyxzrMjDMK20bTNSYFmFvjWlWVstFBC5BBOrYA36cU5%2BkLq6NCfUR0LDOzTU7wQ%2Bg%2BZXMWiB%2BYklu%2B6WmkD6I6Iw%2BcAodHgpjB3F9jXzskT%2BqXe0l6KLc4tYokOAIKIuEWHbO3Gr5ky18qmURgrX%2BhlVjdt8S2lJSOxgN2pJq%2FmSuw2krwyE%2B%2BsGRSCgDoO%2BjGp4Z81C1XT%2FIonyJYOpve%2BR2H8uC15m9IHEOxakYvPxcCmjjTSKzfHwI31ip4DF0XOdarWY3FtzRHfOG%2BMOrB9rwGOqUBBgkWUBP%2BBqA8GqXz1wTjYMU2pRHwCj6APdjJL77QAkVpjxsfkZdFaoic%2FJL92OFnga105BMwkO4HjwpvAb1OFhX3lrrj5DeXSrVOuKZ4Xj4%2BxOb5F2EvQ4u18nsJjqr%2FanNpjdPy%2FSJMEg0t6MY9PhMDDUHGp1EIr%2BbJJa3pA3moGdmsfaQ6eA6Yn2nPrRKvLw7MDJ8P5S%2FGR%2F%2BXF6n0wzfznTFx&X-Amz-Signature=b4e41b53f38d639017c7f5668c17d79304f6cb7fd5621e05b89d40d87926b217&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/13ad0497-05fe-4eaa-984e-707b33e14761/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SGG3G6KG%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T051323Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIATJCtOGxGWAFAcwqw349FgIu4ih3SimOaN6t%2B3yv0odAiEA%2FAadXT%2Bd%2Bx0CGGXOigiI6W4r1vxOCeHc4KtkD8IspcgqiAQIzf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMLx1z6R07Hf%2F2dYwSrcA4glT9QYlSRroH6B30XTXky1OxklquPVOgJEE%2FxsyJCZFiImBIMSu7srmNAJyzFyKbFAYj56T2H5R604UYZueS%2BmlB%2BU%2Bs2HB5bc8vKNuaIOHrvi1cwbRB1xNc2QlMR0lwd7XczQHFtmrdQYh57F%2F0LwOw6KpqxAn3nN%2FSfH9lLM157OwnnYzrL%2Fn0lGHQQ7bATV%2BbhEOrXqa7vcV4g1Ntj1%2BLRwq2Q9aCyMKj7AbtIFgIS3h1h6qpgWcMFsVKMqtMkWEHjjCGwfQsyNnOmt53fGFoKfUFOw3npcBLbEOVhtD7giKkaWSthYo6Kbh35fm46rLzaXaKktHzHMlfz8CR%2BP0zfqEaJXDhOQq2O2B%2BYyxzrMjDMK20bTNSYFmFvjWlWVstFBC5BBOrYA36cU5%2BkLq6NCfUR0LDOzTU7wQ%2Bg%2BZXMWiB%2BYklu%2B6WmkD6I6Iw%2BcAodHgpjB3F9jXzskT%2BqXe0l6KLc4tYokOAIKIuEWHbO3Gr5ky18qmURgrX%2BhlVjdt8S2lJSOxgN2pJq%2FmSuw2krwyE%2B%2BsGRSCgDoO%2BjGp4Z81C1XT%2FIonyJYOpve%2BR2H8uC15m9IHEOxakYvPxcCmjjTSKzfHwI31ip4DF0XOdarWY3FtzRHfOG%2BMOrB9rwGOqUBBgkWUBP%2BBqA8GqXz1wTjYMU2pRHwCj6APdjJL77QAkVpjxsfkZdFaoic%2FJL92OFnga105BMwkO4HjwpvAb1OFhX3lrrj5DeXSrVOuKZ4Xj4%2BxOb5F2EvQ4u18nsJjqr%2FanNpjdPy%2FSJMEg0t6MY9PhMDDUHGp1EIr%2BbJJa3pA3moGdmsfaQ6eA6Yn2nPrRKvLw7MDJ8P5S%2FGR%2F%2BXF6n0wzfznTFx&X-Amz-Signature=8dc19dd75f4de4acb76b3b7aaf7fb83a0f6262f23aeec37eebce00a71a91342f&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 2. Box and Whisker Plot
A box plot shows the distribution of quantitative data in a way that facilitates comparisons between variables or across levels of a categorical variable. The box shows the quartiles of the dataset while the whiskers extend to show the rest of the distribution, except for points that are determined to be "outliers".
**Syntax:**
```python
sns.boxplot(x='header_1', y='header_2', data=df)
```
**Example Output:**


![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d207ae92-0a7c-4e2f-aa65-0ee5a2c33bf7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666NCQTGZ2%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T051325Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFAfaq0xLv%2Bo%2FoQfPWIB%2FEvDh51UwCH%2FJrFK090XJvdlAiASk0BKYoy850%2Ft9fpu0gOGpI7b5hDpeB1j0pVdblS2ECqIBAjN%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMZSXYqs9pGi9P2tG2KtwD78V4JMKRMNNzw8xZHs8SbyGzgpBcA9L62EG1rSxm5%2BOYwvMlFuOPaO8%2B2WnqV3wEh56LAzoCrKhh1tksrVSGJ%2FanURDIkaWbiFr5hDxxfxs7ErkCvkjXlxAynzvRLei40vUzEgmqucoJAqx2eDlxJrgj8gIh%2B%2FLFBmmdJKeauSrAFIuVdaNuQ5fRACh7DG0SMnqOPYtH%2FQecK%2FKho9oMj5swW5Z9d8lZqHx8PwUv%2BZ78X4tjtu23PYPJzV8xHiM%2B9xBwxkuAmqdpY%2FqGEV%2BSE7lGP5fe3GEOUSNd05OyAnwqaXp0V3YScbvJNtUnMt4do%2BA%2FRJE%2BCAMSX1VqDoR4eaKBCIeUfrZIBFbyemX3zxD9Ow40srkxjLjdZURyR2H1WAWxMUzEtUb9Q4161h3m0OHKivIjEL0hrlQZOzVVZ98hHsb7OpGt4rYp1hJlTNtX51Dry53adueAwqdyT4Yc%2BmK%2FKHdhKIANKelZmdqi%2BpV425NG448GcMbm%2F8tp0CFNURvEMDqLBhyt0Yjnki1pcJVIdhIWAshizztgxKTQMW74K2G8vohVPomERbYcrZliFeMbMj9MhOxeUNnGFEN3iM8UvdSlez5KvD903DTRF5xFFDtrn2zLYVZ7ORcw4sH2vAY6pgFZY4iapCz9sabQ3ecj6F%2B%2FnNceFJ0NMZ05uoWtezG%2Bsih3HbiZdWwd9dHQD4J20VGz%2FvcVUpIaEdqKW3SXKqpwrv5uLhb4%2Fwm9afoDTAtp9nvGiR2ebAAzZ7hHXZlBv9sjokiR7lpxwxxrdepYvFK%2FGMIYIu3f6R06z5xuScYGUSAoxS8wRaks8S%2Bse7h82CYJBe3BtirwChJzNQp%2FTO8TaAN0yogz&X-Amz-Signature=fefcb9728549f55cedcf77ddaab03eeb4ac7f557132391048f3cc10a8183a447&X-Amz-SignedHeaders=host&x-id=GetObject)

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0e516edc-7551-4792-ab18-0494db3c4c0c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RDJFGMDE%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T051325Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCkRFRyzH6XwPHpCWGDc6vPCoClMANlKwdoDVyx8e15dAIhAJJp42KeBdK4eaJAb7Xh6AKv%2BU5egcIiwhlpg%2BIu%2FliAKogECM3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igy%2BijbQzDXaN%2BE98NQq3AOpRIZefVYAFg2s5M70EW3NQwMwhfq53jJHYR%2FYCqcdtzoSQaF%2Bn4eXICozEwACbe4LcLvScwxqWV3ZGBAD2vSm2yLEx2Xnz%2FEGxH2EHS6wXhOXH65hOWG%2B3mfr%2Bka53tiTwkmsKHX5t%2BtMku7RJhK%2F%2BDHbM%2BiloAAlmjUFHPL8%2BDKNhi9qayEuenkYTk0r%2Bq1xskRC2k0s8wGibEPS1xfFqgEiSDP9AQx%2Fy%2BGaS0QVbx5AnbMO31cLZjw%2FDGP05qr3YNMjfkgPxmhwDczymtT84Bss4jr41TQ1LPKythJ7ibETYYzgIhCD6%2B5pT5JLsfXD6WJvMoJpPiyjOh8noejd95Qzz2%2FKDnu4EoAxJwWnTMCYhUyydpEy7C%2F8Z4nLxy0Hgnvlb3KNjZmTxwICKbzMDCkjAx5g4vHr%2FqsLu5nNQYhrpWnkOvKwpKbHZIXVI0Ol9kOQ9jkQz44nKh2oqurzbeMSi8OHuHeptpOU0Dj0mSqc7Wob4djuOEKk55qU5URfxoruRaOQIq7ozRsnEc04T0FL9hOf79YaWgyGn1hVAzx0oZkwjpeWMBfW2yMYg409sWn1t0%2B%2FPeaBIQxRM7Ioxnu51f39cSZYi02Hw5W8v6y1sYEUPlSyeP%2FbkjDqwfa8BjqkAUu2thEdRErRZJcHC6nkGtY4Ya%2FD3DRzE74c5AaUpkp%2FHzima3dAisprU7yu5JnkNfFuV7jlfjRNPHtNPQBzKEVy9XRWodg6hJcE9gns8NRH53rXHSTfyDfWarofxj6CMsavUB710vj9d%2Ff0iIZvgZ3qUwxEaCbZe1iXcqy2Ln3MRKhz1KaSfU2c2xWt8Ga26rqIwNFhq73M%2FcKA7bJH7YxJg3JQ&X-Amz-Signature=7593ae500ff8c4b77fbf040a278031d68cc8254445fab84cc1cbaeb2dd5fdf77&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23a79b9d-2356-49a9-8fd9-65c6b0ab2cc5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SGG3G6KG%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T051323Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIATJCtOGxGWAFAcwqw349FgIu4ih3SimOaN6t%2B3yv0odAiEA%2FAadXT%2Bd%2Bx0CGGXOigiI6W4r1vxOCeHc4KtkD8IspcgqiAQIzf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMLx1z6R07Hf%2F2dYwSrcA4glT9QYlSRroH6B30XTXky1OxklquPVOgJEE%2FxsyJCZFiImBIMSu7srmNAJyzFyKbFAYj56T2H5R604UYZueS%2BmlB%2BU%2Bs2HB5bc8vKNuaIOHrvi1cwbRB1xNc2QlMR0lwd7XczQHFtmrdQYh57F%2F0LwOw6KpqxAn3nN%2FSfH9lLM157OwnnYzrL%2Fn0lGHQQ7bATV%2BbhEOrXqa7vcV4g1Ntj1%2BLRwq2Q9aCyMKj7AbtIFgIS3h1h6qpgWcMFsVKMqtMkWEHjjCGwfQsyNnOmt53fGFoKfUFOw3npcBLbEOVhtD7giKkaWSthYo6Kbh35fm46rLzaXaKktHzHMlfz8CR%2BP0zfqEaJXDhOQq2O2B%2BYyxzrMjDMK20bTNSYFmFvjWlWVstFBC5BBOrYA36cU5%2BkLq6NCfUR0LDOzTU7wQ%2Bg%2BZXMWiB%2BYklu%2B6WmkD6I6Iw%2BcAodHgpjB3F9jXzskT%2BqXe0l6KLc4tYokOAIKIuEWHbO3Gr5ky18qmURgrX%2BhlVjdt8S2lJSOxgN2pJq%2FmSuw2krwyE%2B%2BsGRSCgDoO%2BjGp4Z81C1XT%2FIonyJYOpve%2BR2H8uC15m9IHEOxakYvPxcCmjjTSKzfHwI31ip4DF0XOdarWY3FtzRHfOG%2BMOrB9rwGOqUBBgkWUBP%2BBqA8GqXz1wTjYMU2pRHwCj6APdjJL77QAkVpjxsfkZdFaoic%2FJL92OFnga105BMwkO4HjwpvAb1OFhX3lrrj5DeXSrVOuKZ4Xj4%2BxOb5F2EvQ4u18nsJjqr%2FanNpjdPy%2FSJMEg0t6MY9PhMDDUHGp1EIr%2BbJJa3pA3moGdmsfaQ6eA6Yn2nPrRKvLw7MDJ8P5S%2FGR%2F%2BXF6n0wzfznTFx&X-Amz-Signature=13649e34f61819c8a96b423619b2f181f2df4e55344db1b5d0ffb44f6f011e81&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 4. KDE Plot
A Kernel Density Estimate (KDE) plot is a graph that creates a probability distribution curve for the data based upon its likelihood of occurrence on a specific value. This is created for a single vector of information.
**Syntax:**
```python
sns.kdeplot(X) || sns.kdeplot(df['age'])
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0d571213-2a2f-4921-a50b-880847aa05ee/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SGG3G6KG%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T051323Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIATJCtOGxGWAFAcwqw349FgIu4ih3SimOaN6t%2B3yv0odAiEA%2FAadXT%2Bd%2Bx0CGGXOigiI6W4r1vxOCeHc4KtkD8IspcgqiAQIzf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMLx1z6R07Hf%2F2dYwSrcA4glT9QYlSRroH6B30XTXky1OxklquPVOgJEE%2FxsyJCZFiImBIMSu7srmNAJyzFyKbFAYj56T2H5R604UYZueS%2BmlB%2BU%2Bs2HB5bc8vKNuaIOHrvi1cwbRB1xNc2QlMR0lwd7XczQHFtmrdQYh57F%2F0LwOw6KpqxAn3nN%2FSfH9lLM157OwnnYzrL%2Fn0lGHQQ7bATV%2BbhEOrXqa7vcV4g1Ntj1%2BLRwq2Q9aCyMKj7AbtIFgIS3h1h6qpgWcMFsVKMqtMkWEHjjCGwfQsyNnOmt53fGFoKfUFOw3npcBLbEOVhtD7giKkaWSthYo6Kbh35fm46rLzaXaKktHzHMlfz8CR%2BP0zfqEaJXDhOQq2O2B%2BYyxzrMjDMK20bTNSYFmFvjWlWVstFBC5BBOrYA36cU5%2BkLq6NCfUR0LDOzTU7wQ%2Bg%2BZXMWiB%2BYklu%2B6WmkD6I6Iw%2BcAodHgpjB3F9jXzskT%2BqXe0l6KLc4tYokOAIKIuEWHbO3Gr5ky18qmURgrX%2BhlVjdt8S2lJSOxgN2pJq%2FmSuw2krwyE%2B%2BsGRSCgDoO%2BjGp4Z81C1XT%2FIonyJYOpve%2BR2H8uC15m9IHEOxakYvPxcCmjjTSKzfHwI31ip4DF0XOdarWY3FtzRHfOG%2BMOrB9rwGOqUBBgkWUBP%2BBqA8GqXz1wTjYMU2pRHwCj6APdjJL77QAkVpjxsfkZdFaoic%2FJL92OFnga105BMwkO4HjwpvAb1OFhX3lrrj5DeXSrVOuKZ4Xj4%2BxOb5F2EvQ4u18nsJjqr%2FanNpjdPy%2FSJMEg0t6MY9PhMDDUHGp1EIr%2BbJJa3pA3moGdmsfaQ6eA6Yn2nPrRKvLw7MDJ8P5S%2FGR%2F%2BXF6n0wzfznTFx&X-Amz-Signature=94d5963670abe4214132617eddcc94b65c5d7bbd3259f6a5a47ee72abb97d49f&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/53752550-ef82-4ca9-a01a-09921f0282d0/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SGG3G6KG%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T051323Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIATJCtOGxGWAFAcwqw349FgIu4ih3SimOaN6t%2B3yv0odAiEA%2FAadXT%2Bd%2Bx0CGGXOigiI6W4r1vxOCeHc4KtkD8IspcgqiAQIzf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMLx1z6R07Hf%2F2dYwSrcA4glT9QYlSRroH6B30XTXky1OxklquPVOgJEE%2FxsyJCZFiImBIMSu7srmNAJyzFyKbFAYj56T2H5R604UYZueS%2BmlB%2BU%2Bs2HB5bc8vKNuaIOHrvi1cwbRB1xNc2QlMR0lwd7XczQHFtmrdQYh57F%2F0LwOw6KpqxAn3nN%2FSfH9lLM157OwnnYzrL%2Fn0lGHQQ7bATV%2BbhEOrXqa7vcV4g1Ntj1%2BLRwq2Q9aCyMKj7AbtIFgIS3h1h6qpgWcMFsVKMqtMkWEHjjCGwfQsyNnOmt53fGFoKfUFOw3npcBLbEOVhtD7giKkaWSthYo6Kbh35fm46rLzaXaKktHzHMlfz8CR%2BP0zfqEaJXDhOQq2O2B%2BYyxzrMjDMK20bTNSYFmFvjWlWVstFBC5BBOrYA36cU5%2BkLq6NCfUR0LDOzTU7wQ%2Bg%2BZXMWiB%2BYklu%2B6WmkD6I6Iw%2BcAodHgpjB3F9jXzskT%2BqXe0l6KLc4tYokOAIKIuEWHbO3Gr5ky18qmURgrX%2BhlVjdt8S2lJSOxgN2pJq%2FmSuw2krwyE%2B%2BsGRSCgDoO%2BjGp4Z81C1XT%2FIonyJYOpve%2BR2H8uC15m9IHEOxakYvPxcCmjjTSKzfHwI31ip4DF0XOdarWY3FtzRHfOG%2BMOrB9rwGOqUBBgkWUBP%2BBqA8GqXz1wTjYMU2pRHwCj6APdjJL77QAkVpjxsfkZdFaoic%2FJL92OFnga105BMwkO4HjwpvAb1OFhX3lrrj5DeXSrVOuKZ4Xj4%2BxOb5F2EvQ4u18nsJjqr%2FanNpjdPy%2FSJMEg0t6MY9PhMDDUHGp1EIr%2BbJJa3pA3moGdmsfaQ6eA6Yn2nPrRKvLw7MDJ8P5S%2FGR%2F%2BXF6n0wzfznTFx&X-Amz-Signature=d0a8edf3bc381e09b017d6bafa646ed2cee0a2b0e2cbc4ee70a059113f63266b&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
## 4. Correlation Between Variables
Correlation is a statistical measure of the extent to which different variables are interdependent. It indicates how changes in one variable are associated with changes in another variable over time.
### Positive Correlation
Positive correlation indicates that as one variable increases, the other variable also tends to increase.
**Example: Engine Size and Price**
- **Positive Correlation:** Engine size increases, price also increases.
- **Visualization:** Scatter plot with a steep positive slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c7ea9b0-3ef3-4357-a9c3-554fc71b6b15/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YSYAIWR2%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T051325Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHyI8Alr%2BojOTGxHo50jn%2BA6kNVqDyuFgoOYEge%2BG7scAiEA29RnimQNdTauHEOZN5sBEd2k%2B1MOQZmXpUHTC2fuB34qiAQIzf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLLUIJu3xarfo8IShSrcAwI%2Fs4bi%2F9lCk6ulnhDMW7j8paceBYg8FpBsLVIrhHbLTWIx0dntbhahZT4GPd1hnZid9vy9CuAz57c%2BhbaoanhpMNCXKruGkwC%2F6HaEVWVOAsJk1qbfu%2FHz745j%2BQujVNVMGC68AVNu52qoe2xXW8WJ1PdBjPL0a98kZPv1O28AiGLlWhCOu0dJa27M1OeeMFhmZTlfzBVcOI1zNFboS9KCpzpGzt%2Bu1Mzegqrajjw1q5XMePiFE6IJErzEIVQKDBazEwPbS5kWs7170aPDIzbgr%2FWycDytN%2Bu0Dx1NRWiTaUggCZJ9ic8gR2qfEoc6Bw%2FD3qkd%2Bae6zg7h6H6BLARhAMSZhgpJAycob%2B85wVcZoxLuZDzVHAequlY4xqGZ6Ym4jrhgu4pJiRm1RWCC8d35BvWl354ReJ9mWXfV08OvL29oR5oxQGOi8HGDib7e6KRua4vGe9PFwPf1nw%2Bp7hHnRsPyVRmCm1S2u0kGO8lKBRzhXJ6KuyIqt57UEVMcmAjDp2kbfmfbSv8V4N5RiR%2FeXlKvPKYwn027GIr%2BNzinrp3nRk9vuPjm%2B5nWRVXXJNqtFLP%2BSAHD5ujaCwJ4lORpZEslh6CI96hAKZcU8gZiIobO8QaJFkd6DmaiMKLB9rwGOqUBhBTv9W2IRf6W5KlnzaCbfLBJ%2Bu%2BduZyPSUbDxLUoH6ovCQ%2B24ylM4tJPzeFUANIspEdiTAWGfQ4AjDmFyPY3AKM7bv1OIOh1dlV2eUdigm3QMHU1JsYN2jYaiwQAUFZpk0vo3yozOLlhiYW0f6qyEkjUZnDDSyXznxVqVuWJkOdxNx%2F4I8fqrl2x68LlBsofmrr9vdvWEobwW1365cGmGLBX2Rer&X-Amz-Signature=39e1a0e94df00b06468e436a5afc416c395d437410ce604b3af256f60e4e9c07&X-Amz-SignedHeaders=host&x-id=GetObject)
**Explanation:** When engine size increases, there is a corresponding increase in the price of the vehicle. This positive correlation suggests that larger engines tend to be associated with higher prices in the market.
___
### Negative Correlation
Negative correlation indicates that as one variable increases, the other variable tends to decrease.
**Example: Highway Miles per Gallon and Price**
- **Negative Correlation:** As highway miles per gallon increases, price decreases.
- **Visualization:** Scatter plot with a steep negative slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/10f1f798-9cc4-4df2-a9c1-5a339f554a0b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RWMZW5GV%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T051326Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICRhn%2Bc9PkKmh5UO%2FTrJEg19urJFRqHZe1wNoNjLV5oJAiBYhsVgCwcrYgc%2BoKKHMb2kqngBXIdOGAmpCYG8HtWt0yqIBAjN%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMXgVfGBwDjRhUxmibKtwD%2FQkHYqeGWB1ZQ84rTG4EPE0XHlPKZ2yFXWIuL%2F2C6WVXJXeg0JdfRpmFl3%2B1Olkjvu767gt9GFXlCy2JEXz%2F%2BryjZ5rsWq4S7pxdKrXKBpn8T%2BwhF88WjTNoyEc49zr9CbLLNPv8fxgm2ZSJO7DI%2BvmVjcO4jYyPYZ2ly6gfNzl5B61e9C2xiDFW2Y1cY1nosZwWGYD6MgCEQvpxPspTEz%2B1zLh5xGdjZQUa67%2Fg5j1LpJe6o%2B69J4hfYQHvrSAXy0%2B6m%2FxS0r3DPRJQ6oiwAdc2hf%2B72I12NG%2FN2FIwjpIToXSAAgne69GBQ4q9DULA1jYtAEKDQ6yKC9B4HCGumwYiJ1rsCG0HQOJL8VsKxIGgo1BYFmFOk6iOgTM5VoKB4heGPfQAyPeaAIybJsUph83IOJVABly9leAdYXoqAke22vmnQVvMUu%2FZYohfW5CglOGWVH%2BM73YNt%2FvxRJF4KFaAgxx9Y0DQpH%2BPe4oEKPtuszdbA0WUWzQaQspMkdapqkeu32T39uPwozyyTZuIQshbR5RrcsGtNUfDCSzXkbibgri%2Fb2Wo2BtNR4W4zPKn8cb43OYPzsourlkNPZBrAAXlsDD%2FJha%2ByGFyURq%2Fgs6iuJL65GwinVVAmAUwj8H2vAY6pgF7pLZizwKG4cobbHvhlHgBP%2BCRlpdPgT%2Fm%2FT35RKwWVJKCLVza4k%2FsdYmFqbwOAikhvj62c3qnwkl65GGC%2BBFYmcZqa1SaoTiLCsOo09Ivx9Yft%2FJUAh1UjGjw%2FhFnptoKSiYBpf0P6Iqg7MwhGBC%2BfqeYmbNV%2BmHEqY9N0LTvAeA6cHEiyitw1k%2BSF7fuOcyxi%2FwzTeVFyFoGoayGj72JEa2XzS6M&X-Amz-Signature=bc74a9d1035eb47b56fc2925826234f572b1995ed5a0a9bee7885496bcacde0d&X-Amz-SignedHeaders=host&x-id=GetObject)
**Explanation:** When highway miles per gallon increases, the price of the vehicle tends to decrease. This negative correlation suggests that cars with higher fuel efficiency (more miles per gallon) are generally priced lower in the market.
___
### Weak Correlation
Weak correlation indicates a lack of strong relationship between the variables.
**Example: RPM and Price**
- **Weak Correlation:** Low and high RPM values show varied prices, indicating no strong predictive relationship.
- **Visualization:** Scatter plot with no clear trend or slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9f914514-8914-4bf4-ac84-d9e3077f6eb1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665QRIQ66H%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T051324Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGy7kefK2N7uDmpD8zJeJNONjerxjO6hSvugZ3kSHGTdAiB8eGKwl949WPbHVVziaz2JwYpjzlyqUu2FLEtaecLDDyqIBAjN%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMCNu4yfZ3htBijTVbKtwDmzaNZH%2Bc34ixtRO64GHWthQjQjsQyVMdawCXBfU4jmQ99QWvCKQjnhcLcCTQeONP44tZ8ENDGuLoMPKnpo9lCtjsjtFRX1W49ju%2FSHwWUhX2J6xTxg01AHgTuYekCUWCN%2FLGwgasQzj%2Bw96wv7qRdUl5PnfKoFaRWjUJX9CnqX%2BQ6o7NLafvvIWvoFefPRQBrED4W2R7LUYqOYBjp%2Bj8WAJ%2Bj37Ib0Sxh14F5P0Gh9lyCznFw%2FE2geUIr3f4eM0mCxtxXuPp8BpvIU6LUk69dVaVtXebMU8hkrGEuAMQNrwWI7nbPqHnlcV%2F1yhy8PxhjP4R6oRIA%2BeabXdFQvmnqNOgvheXfrTB%2BniyF0JRy7exfec%2FyeTKJ1w56y0%2B4t9IZJp6VpsKdZAZzxL%2FcS9YvybURp1gTDlspPgRZ3EQJTT5SFTmAsoWuL3IdCP5i0RWy18m0iTLzkqBmQXG%2FsNBmrzgAx5OjyHQTs2f8YJ8cYc2L5k%2FZozSY31gmsKjIh8CxsUrYq3xtarwiDI4qBjaPJ5tUev8EUXgyEZ9cq4MR6eueNfcJ0d9G9gIIAWIzp05pIBqrb2wTrzMfQ8oxwjUzMH0%2BA4th4bNPGdB77sxEBueIYuk2%2FLN3DnnSp0wmcH2vAY6pgG4d%2F6dfElBuD3N8BOigPGg%2BxteriNTSgxTuqq5XX2jj31ZG070c%2FR3sb9ieUDRKUXtszdjj5Tv2P53q%2BzMkG%2FWWp7iDPCgw65CBuPD3x9Y92Y786tBr20UZht76emFN1jnc5t1F%2B4Nvbto9X0eIQxipTYwYz7Ynev8HtRkVtz7sQQwih1T1h0hFnCdq0h8GQkh6TvrqPglsOo0SHaUGqB9A3HApMGD&X-Amz-Signature=ac9f40f3a48071d458374ed4a2cd9f961ae13de964b51ecad0948468c17875e3&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f18086e5-5b04-4fbf-8309-8944ab20d213/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466445AARTJ%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T051324Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIH%2FnTC896ja0ocRDQMn%2FTuLa1VN28SiZ34eUjYiWPGrAAiEAtk3wlgI1QCSWT93y9brzCaFuGAB6ap0UTgUOF1pqS4cqiAQIzf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLHELOxCRTerCtS2ESrcA9x8SB4jxU3wCOhnU1sRyufKTfGYBfzThzEJgY02oczaIACpTTAz8phJBAu11xfdmnSEa8yfPCENy%2FU90y04wIPWdfiOh6hiPvdmouKR7Yz%2BPmEZCTOrZ87Jhr3Q7zM9WhrNM5DQSFn6s6%2BfM%2B%2B8EdqRqaV7iPkirr6SmLmnXY%2FGZo9qQqWB1oqFecd0%2Fl0CBhMVJGeCkRb3jUHy6gDDCV0FXccT3XEt7RRYrX7guiO0eTLhdjRBNEz%2FyzKglNOu0GmAmrMnzHL4R8EjCpDnwfZ9u8AZzMhmIgIji%2F5o%2Bc6vyHFtboVxEdMLqcy5YXh3Th4x%2BSK%2F7Lubns0ZnCwtn4inIBf%2BQl2DP0Qwk1eiNoDSd5UMOt6zSSbMhOvWcBzskxjSWRuITaT3qD%2BqKDOdipmfCJt8YyQ2lkaK3CkL4hr7R0JXfvoaJ2pHAAVr%2FroinsvfSSzwlj%2BtoDw8TFVEOmZWtGD%2BHoUlqW3l0d2nwTDKbWFUF1OWKOQzzFJY8VAft7wvjBazkSzqCiJchA4Qcrp04kkx9FPv9X7%2FXCA68EAXk6cPWINK%2BuHUjB57XaPYio9GCGokOOUOA5wMAz9qRlyDHFqDADw70XPTgQUXan0SYXSiP%2F%2Bty1LPrPi5MNzB9rwGOqUBOF%2BAp%2BmCz7uUTiN2yhFMM5RNgbK2pWDxiSnyL6uz%2FoQDVRm8u0g9Iw1qkeenXsypTB8wIpDXD3Hr1m2%2BTZ582crhAC4Ub6cjmtgwPw16lLwJSUAIBCjLrrJQkqsPacfSvsyh6xgJipkJq4Y31so8eJ%2FvcTwleaRlcAhcfq0%2FBVLXDmQVGR1MoJn4OmRwYCVUyTos026tiwA6SWNMN%2BBjEZQYBSR5&X-Amz-Signature=32f6aad5467d4731079b6cd4e66911c5dbed57c45254af296a23edb843f89766&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Correlation Plot
Heatmap visualizes correlations among variables. Color scheme indicates Pearson correlation coefficients. Dark red diagonal line shows perfect correlation (value of 1) between variables and themselves.
This heatmap offers overview of variable relationships and their link with price.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cd3b341e-cc1a-45f7-8aec-cdc00436d270/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466445AARTJ%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T051324Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIH%2FnTC896ja0ocRDQMn%2FTuLa1VN28SiZ34eUjYiWPGrAAiEAtk3wlgI1QCSWT93y9brzCaFuGAB6ap0UTgUOF1pqS4cqiAQIzf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLHELOxCRTerCtS2ESrcA9x8SB4jxU3wCOhnU1sRyufKTfGYBfzThzEJgY02oczaIACpTTAz8phJBAu11xfdmnSEa8yfPCENy%2FU90y04wIPWdfiOh6hiPvdmouKR7Yz%2BPmEZCTOrZ87Jhr3Q7zM9WhrNM5DQSFn6s6%2BfM%2B%2B8EdqRqaV7iPkirr6SmLmnXY%2FGZo9qQqWB1oqFecd0%2Fl0CBhMVJGeCkRb3jUHy6gDDCV0FXccT3XEt7RRYrX7guiO0eTLhdjRBNEz%2FyzKglNOu0GmAmrMnzHL4R8EjCpDnwfZ9u8AZzMhmIgIji%2F5o%2Bc6vyHFtboVxEdMLqcy5YXh3Th4x%2BSK%2F7Lubns0ZnCwtn4inIBf%2BQl2DP0Qwk1eiNoDSd5UMOt6zSSbMhOvWcBzskxjSWRuITaT3qD%2BqKDOdipmfCJt8YyQ2lkaK3CkL4hr7R0JXfvoaJ2pHAAVr%2FroinsvfSSzwlj%2BtoDw8TFVEOmZWtGD%2BHoUlqW3l0d2nwTDKbWFUF1OWKOQzzFJY8VAft7wvjBazkSzqCiJchA4Qcrp04kkx9FPv9X7%2FXCA68EAXk6cPWINK%2BuHUjB57XaPYio9GCGokOOUOA5wMAz9qRlyDHFqDADw70XPTgQUXan0SYXSiP%2F%2Bty1LPrPi5MNzB9rwGOqUBOF%2BAp%2BmCz7uUTiN2yhFMM5RNgbK2pWDxiSnyL6uz%2FoQDVRm8u0g9Iw1qkeenXsypTB8wIpDXD3Hr1m2%2BTZ582crhAC4Ub6cjmtgwPw16lLwJSUAIBCjLrrJQkqsPacfSvsyh6xgJipkJq4Y31so8eJ%2FvcTwleaRlcAhcfq0%2FBVLXDmQVGR1MoJn4OmRwYCVUyTos026tiwA6SWNMN%2BBjEZQYBSR5&X-Amz-Signature=9b3e33b3d081883d7489db0aeef479f736c2045a4eecbb2fcb24eae7dfbd7fd6&X-Amz-SignedHeaders=host&x-id=GetObject)

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
