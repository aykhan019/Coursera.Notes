

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7e6d594d-952e-44b6-97ea-31225882aea6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WGJUTLN5%2F20250330%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250330T004512Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBcaCXVzLXdlc3QtMiJGMEQCIAzx4MjOefboY9GHYQAICIcPHfwyVCE2RnqmBhRKflGnAiAhhHTyA23SGB3k5SFVKo%2FYnAP09Y%2BjWcCMD69BW0ZlzSqIBAiA%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMVZ3RXmeM3jqR%2FwzqKtwDSVnWW0vVUhzoRkvsErbRl%2Blxiiq1AykSn9HhylqzVoh5EK11IWTi4lYW0DKVGsJ88SvlUPXRW%2B6hg9RkQFgWHIJpgisePukQrqYpSnBBVkXehGYHhxAwAPs%2F1z1OielC3is9hG50%2BZ3VUZ1P58I3vORZFHmULWIoawfi19YbkzgOsUla6LZGRSYPDGuPSFVCXWBchWbRg9fTOwVwI7wbY%2F%2FfyucNByITBfx4kNJKMvw55y9h9efPXnwyIo5JKGxZjp4lYUOf63rx5wB2t1DKprgT3f0I7w%2B9MbzXgUEjzWahfIfiDSPNVnLn0%2BeOY6eZsksN0XKm%2BpD%2B43Va%2F6Hj4zRX9VApr5KGfDFay5z3uzR8CoThveNvptCOqDLIBCMJfOz%2FqX0Zhzp5CDeNTcEfPVI5SPHDT7X2LjWWtUyC6OSB%2BdtWqO%2BcItqhL6PrYco8%2BDmhXrnkYoyMsgY%2Fbn8ezCQCv4agadq5j7%2BV9CZ1Cw4A5i2yw%2FC3L9h4OzwO95uwFyo0WEJtTPNbXpFsfQKtLwGUnxUuMXjX2b11%2BjmcUHwh2LW6BtbfhGi04VfMQ5cBKAQhYldlJ0K2Lhu0ea5cxN5XoJUkUPfqB0hw0zly0LmxIxUPgsqa%2FZylLd8wxfyhvwY6pgEVI9M3jF%2Fmf3yTyL8ZJIOFncMEFGFaAmE32NMTcX%2BnX6W1o7BBlWuMTiHyf6Rt8SPF9W0oU8qU0A9%2BwGavoz4BGxj9r0f2Og%2Bwk02KQJ0dFCPXVTORPdPNShDL9efgt1usXzxu5KazwcoptN%2FQXNMprRdxGnq3LTZtqyBQBY93w6riDpS0TVXZG1o63vV1Ex%2BrILCaINP77Fx595ywnIIq0Ft2jHKT&X-Amz-Signature=dedb4a7cef5f806a384f1b434e54119dac94fe6f9c0a0c2c4bcedcf7d91edf76&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cbfaed9e-b398-4902-8936-dea058b21def/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WGJUTLN5%2F20250330%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250330T004512Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBcaCXVzLXdlc3QtMiJGMEQCIAzx4MjOefboY9GHYQAICIcPHfwyVCE2RnqmBhRKflGnAiAhhHTyA23SGB3k5SFVKo%2FYnAP09Y%2BjWcCMD69BW0ZlzSqIBAiA%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMVZ3RXmeM3jqR%2FwzqKtwDSVnWW0vVUhzoRkvsErbRl%2Blxiiq1AykSn9HhylqzVoh5EK11IWTi4lYW0DKVGsJ88SvlUPXRW%2B6hg9RkQFgWHIJpgisePukQrqYpSnBBVkXehGYHhxAwAPs%2F1z1OielC3is9hG50%2BZ3VUZ1P58I3vORZFHmULWIoawfi19YbkzgOsUla6LZGRSYPDGuPSFVCXWBchWbRg9fTOwVwI7wbY%2F%2FfyucNByITBfx4kNJKMvw55y9h9efPXnwyIo5JKGxZjp4lYUOf63rx5wB2t1DKprgT3f0I7w%2B9MbzXgUEjzWahfIfiDSPNVnLn0%2BeOY6eZsksN0XKm%2BpD%2B43Va%2F6Hj4zRX9VApr5KGfDFay5z3uzR8CoThveNvptCOqDLIBCMJfOz%2FqX0Zhzp5CDeNTcEfPVI5SPHDT7X2LjWWtUyC6OSB%2BdtWqO%2BcItqhL6PrYco8%2BDmhXrnkYoyMsgY%2Fbn8ezCQCv4agadq5j7%2BV9CZ1Cw4A5i2yw%2FC3L9h4OzwO95uwFyo0WEJtTPNbXpFsfQKtLwGUnxUuMXjX2b11%2BjmcUHwh2LW6BtbfhGi04VfMQ5cBKAQhYldlJ0K2Lhu0ea5cxN5XoJUkUPfqB0hw0zly0LmxIxUPgsqa%2FZylLd8wxfyhvwY6pgEVI9M3jF%2Fmf3yTyL8ZJIOFncMEFGFaAmE32NMTcX%2BnX6W1o7BBlWuMTiHyf6Rt8SPF9W0oU8qU0A9%2BwGavoz4BGxj9r0f2Og%2Bwk02KQJ0dFCPXVTORPdPNShDL9efgt1usXzxu5KazwcoptN%2FQXNMprRdxGnq3LTZtqyBQBY93w6riDpS0TVXZG1o63vV1Ex%2BrILCaINP77Fx595ywnIIq0Ft2jHKT&X-Amz-Signature=cf670da427cd07769838b71ce84e4e9f7dceedaaa5df6af94d1b614a66da625b&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/91181646-b1e0-4433-9711-6259a96a9247/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WGJUTLN5%2F20250330%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250330T004512Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBcaCXVzLXdlc3QtMiJGMEQCIAzx4MjOefboY9GHYQAICIcPHfwyVCE2RnqmBhRKflGnAiAhhHTyA23SGB3k5SFVKo%2FYnAP09Y%2BjWcCMD69BW0ZlzSqIBAiA%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMVZ3RXmeM3jqR%2FwzqKtwDSVnWW0vVUhzoRkvsErbRl%2Blxiiq1AykSn9HhylqzVoh5EK11IWTi4lYW0DKVGsJ88SvlUPXRW%2B6hg9RkQFgWHIJpgisePukQrqYpSnBBVkXehGYHhxAwAPs%2F1z1OielC3is9hG50%2BZ3VUZ1P58I3vORZFHmULWIoawfi19YbkzgOsUla6LZGRSYPDGuPSFVCXWBchWbRg9fTOwVwI7wbY%2F%2FfyucNByITBfx4kNJKMvw55y9h9efPXnwyIo5JKGxZjp4lYUOf63rx5wB2t1DKprgT3f0I7w%2B9MbzXgUEjzWahfIfiDSPNVnLn0%2BeOY6eZsksN0XKm%2BpD%2B43Va%2F6Hj4zRX9VApr5KGfDFay5z3uzR8CoThveNvptCOqDLIBCMJfOz%2FqX0Zhzp5CDeNTcEfPVI5SPHDT7X2LjWWtUyC6OSB%2BdtWqO%2BcItqhL6PrYco8%2BDmhXrnkYoyMsgY%2Fbn8ezCQCv4agadq5j7%2BV9CZ1Cw4A5i2yw%2FC3L9h4OzwO95uwFyo0WEJtTPNbXpFsfQKtLwGUnxUuMXjX2b11%2BjmcUHwh2LW6BtbfhGi04VfMQ5cBKAQhYldlJ0K2Lhu0ea5cxN5XoJUkUPfqB0hw0zly0LmxIxUPgsqa%2FZylLd8wxfyhvwY6pgEVI9M3jF%2Fmf3yTyL8ZJIOFncMEFGFaAmE32NMTcX%2BnX6W1o7BBlWuMTiHyf6Rt8SPF9W0oU8qU0A9%2BwGavoz4BGxj9r0f2Og%2Bwk02KQJ0dFCPXVTORPdPNShDL9efgt1usXzxu5KazwcoptN%2FQXNMprRdxGnq3LTZtqyBQBY93w6riDpS0TVXZG1o63vV1Ex%2BrILCaINP77Fx595ywnIIq0Ft2jHKT&X-Amz-Signature=ce8fb14d735a5893972e0458de1e37025dd5ef3ff879fc9b23da8634bb100bc4&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/09aba1c0-0d55-41dd-852a-a04c5b8a3fac/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664CPHLRTF%2F20250330%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250330T004512Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBcaCXVzLXdlc3QtMiJIMEYCIQDLjTMAmhN0mraY9W4b4hY7QrTjh57gS%2BxlwDiwBuFMKAIhALVxRfCumOz8zntfx9CaFZF9gw4U274%2BN5O9P62Qb57UKogECID%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxRS%2B79IJ47EEFlDOAq3AP30m0MztDDRGu%2BBPt%2BZ%2Bs9v3xjUDFeCXXM%2BtoG9HmsuRmm8NsRIRWt0oU2m01x2lw6HcM4oR6O2sOORye7UDHf4cd%2BdrlNhU9QBR49Zqg8nm35ywMmuSAQkkIEik48pZoESncpAF%2BcA%2FmK6kiOxUyUfSK2HGs2iDKW1U%2FjKv2Verx%2BFbgBeTNELJCcsA%2FXuSYsHCuOr%2FNMlNIozbleofPgdZOvV8%2FE7nsJWSJxVrQSZkH80pIOlW7%2B2%2FbgP0XTxhlRUH9TzRcS4I%2BkIQ21MYb2DODhacMhmXIQIkiybH%2F9qUpv7sZGMXkXCazSLD5A3xgVdWY%2B%2F8JLlbJd56hcFIeIKbcYEBx2PEyo8eit%2Blls0wQtHbkESAZY3qa0LVMC4LjAzS0BWCgtN7nbQZQO68qSb4CM7Xn84OIFCcXr1M%2F2tQKt85HwMwNaOhLyAWUZqrvTL64NlsxYU3MzTeTbsMr%2FgovPRykBjU6aDyJSQTbIFyV2DMzqC89NWxbQxCgbZZPPeqPdkEsE01J5uWuLI%2BWcbMKaCiX6yLeqlOFKY%2FknVmf%2FgLh8XnGQkvNlY%2FdC6b4wgF%2BHFw9%2F7Kg2DLqYo5hM%2B%2Bvz8p%2Brh4LFPCRUvlrvwp4iqgYaXaTDWv75lDCz%2FKG%2FBjqkAbDENTyQR1r9C3Hsbv3TbW8j%2BBqyVK67jXOXoq1IASQoBMjSWSCtuYXzVxxEurImNCu1Q7rLnF5pUudS%2FPzqiLRKBV3GTBlhhzqw6ASE0FsfvBy%2Fef94U5k7kJQMUd6wfGW2CVKuz5oZtoaHEdIpc9L8fk1ktvmJyGhEzyr%2BNCn0BMGTWNNNmXCH%2F5mPyKloEYtns0QwIx9f4uK9qbObSOeO13Pl&X-Amz-Signature=667a16fd3e884be43a48bf7b5c9158ddadfe133e6edae8df32287cf68b84c23e&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 2. Scatter Plot
Scatter plots present the relationship between two variables in a dataset. It represents data points on a two-dimensional plane. The independent variable or attribute is plotted on the X-axis, while the dependent variable is plotted on the Y-axis.
**Syntax:**
```python
plt.scatter(x, y)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23708af9-659f-4f23-b626-1a4292d7842c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664CPHLRTF%2F20250330%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250330T004513Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBcaCXVzLXdlc3QtMiJIMEYCIQDLjTMAmhN0mraY9W4b4hY7QrTjh57gS%2BxlwDiwBuFMKAIhALVxRfCumOz8zntfx9CaFZF9gw4U274%2BN5O9P62Qb57UKogECID%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxRS%2B79IJ47EEFlDOAq3AP30m0MztDDRGu%2BBPt%2BZ%2Bs9v3xjUDFeCXXM%2BtoG9HmsuRmm8NsRIRWt0oU2m01x2lw6HcM4oR6O2sOORye7UDHf4cd%2BdrlNhU9QBR49Zqg8nm35ywMmuSAQkkIEik48pZoESncpAF%2BcA%2FmK6kiOxUyUfSK2HGs2iDKW1U%2FjKv2Verx%2BFbgBeTNELJCcsA%2FXuSYsHCuOr%2FNMlNIozbleofPgdZOvV8%2FE7nsJWSJxVrQSZkH80pIOlW7%2B2%2FbgP0XTxhlRUH9TzRcS4I%2BkIQ21MYb2DODhacMhmXIQIkiybH%2F9qUpv7sZGMXkXCazSLD5A3xgVdWY%2B%2F8JLlbJd56hcFIeIKbcYEBx2PEyo8eit%2Blls0wQtHbkESAZY3qa0LVMC4LjAzS0BWCgtN7nbQZQO68qSb4CM7Xn84OIFCcXr1M%2F2tQKt85HwMwNaOhLyAWUZqrvTL64NlsxYU3MzTeTbsMr%2FgovPRykBjU6aDyJSQTbIFyV2DMzqC89NWxbQxCgbZZPPeqPdkEsE01J5uWuLI%2BWcbMKaCiX6yLeqlOFKY%2FknVmf%2FgLh8XnGQkvNlY%2FdC6b4wgF%2BHFw9%2F7Kg2DLqYo5hM%2B%2Bvz8p%2Brh4LFPCRUvlrvwp4iqgYaXaTDWv75lDCz%2FKG%2FBjqkAbDENTyQR1r9C3Hsbv3TbW8j%2BBqyVK67jXOXoq1IASQoBMjSWSCtuYXzVxxEurImNCu1Q7rLnF5pUudS%2FPzqiLRKBV3GTBlhhzqw6ASE0FsfvBy%2Fef94U5k7kJQMUd6wfGW2CVKuz5oZtoaHEdIpc9L8fk1ktvmJyGhEzyr%2BNCn0BMGTWNNNmXCH%2F5mPyKloEYtns0QwIx9f4uK9qbObSOeO13Pl&X-Amz-Signature=be9be9292be2b216a3043f67719467f27837e81d9f1521eabd539d43f3326e9d&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 3. Histogram
A histogram is an important visual representation of data in categorical form. To view the data in a "Binned" form, use the histogram plot with a number of bins required or with the data points that mark the bin edges. The x-axis represents the data bins, and the y-axis represents the number of elements in each bin.
**Syntax:**
```python
plt.hist(x, bins)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/24e4424a-df87-40a1-b63b-195cbdc2e0ab/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664CPHLRTF%2F20250330%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250330T004513Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBcaCXVzLXdlc3QtMiJIMEYCIQDLjTMAmhN0mraY9W4b4hY7QrTjh57gS%2BxlwDiwBuFMKAIhALVxRfCumOz8zntfx9CaFZF9gw4U274%2BN5O9P62Qb57UKogECID%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxRS%2B79IJ47EEFlDOAq3AP30m0MztDDRGu%2BBPt%2BZ%2Bs9v3xjUDFeCXXM%2BtoG9HmsuRmm8NsRIRWt0oU2m01x2lw6HcM4oR6O2sOORye7UDHf4cd%2BdrlNhU9QBR49Zqg8nm35ywMmuSAQkkIEik48pZoESncpAF%2BcA%2FmK6kiOxUyUfSK2HGs2iDKW1U%2FjKv2Verx%2BFbgBeTNELJCcsA%2FXuSYsHCuOr%2FNMlNIozbleofPgdZOvV8%2FE7nsJWSJxVrQSZkH80pIOlW7%2B2%2FbgP0XTxhlRUH9TzRcS4I%2BkIQ21MYb2DODhacMhmXIQIkiybH%2F9qUpv7sZGMXkXCazSLD5A3xgVdWY%2B%2F8JLlbJd56hcFIeIKbcYEBx2PEyo8eit%2Blls0wQtHbkESAZY3qa0LVMC4LjAzS0BWCgtN7nbQZQO68qSb4CM7Xn84OIFCcXr1M%2F2tQKt85HwMwNaOhLyAWUZqrvTL64NlsxYU3MzTeTbsMr%2FgovPRykBjU6aDyJSQTbIFyV2DMzqC89NWxbQxCgbZZPPeqPdkEsE01J5uWuLI%2BWcbMKaCiX6yLeqlOFKY%2FknVmf%2FgLh8XnGQkvNlY%2FdC6b4wgF%2BHFw9%2F7Kg2DLqYo5hM%2B%2Bvz8p%2Brh4LFPCRUvlrvwp4iqgYaXaTDWv75lDCz%2FKG%2FBjqkAbDENTyQR1r9C3Hsbv3TbW8j%2BBqyVK67jXOXoq1IASQoBMjSWSCtuYXzVxxEurImNCu1Q7rLnF5pUudS%2FPzqiLRKBV3GTBlhhzqw6ASE0FsfvBy%2Fef94U5k7kJQMUd6wfGW2CVKuz5oZtoaHEdIpc9L8fk1ktvmJyGhEzyr%2BNCn0BMGTWNNNmXCH%2F5mPyKloEYtns0QwIx9f4uK9qbObSOeO13Pl&X-Amz-Signature=a1220ede3c690ad3064840e941862cc3db22cdb93594e24081ade5eafc91ff09&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ab5a6dfe-51f5-43ee-bcb3-33dae4a1c7ad/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664CPHLRTF%2F20250330%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250330T004512Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBcaCXVzLXdlc3QtMiJIMEYCIQDLjTMAmhN0mraY9W4b4hY7QrTjh57gS%2BxlwDiwBuFMKAIhALVxRfCumOz8zntfx9CaFZF9gw4U274%2BN5O9P62Qb57UKogECID%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxRS%2B79IJ47EEFlDOAq3AP30m0MztDDRGu%2BBPt%2BZ%2Bs9v3xjUDFeCXXM%2BtoG9HmsuRmm8NsRIRWt0oU2m01x2lw6HcM4oR6O2sOORye7UDHf4cd%2BdrlNhU9QBR49Zqg8nm35ywMmuSAQkkIEik48pZoESncpAF%2BcA%2FmK6kiOxUyUfSK2HGs2iDKW1U%2FjKv2Verx%2BFbgBeTNELJCcsA%2FXuSYsHCuOr%2FNMlNIozbleofPgdZOvV8%2FE7nsJWSJxVrQSZkH80pIOlW7%2B2%2FbgP0XTxhlRUH9TzRcS4I%2BkIQ21MYb2DODhacMhmXIQIkiybH%2F9qUpv7sZGMXkXCazSLD5A3xgVdWY%2B%2F8JLlbJd56hcFIeIKbcYEBx2PEyo8eit%2Blls0wQtHbkESAZY3qa0LVMC4LjAzS0BWCgtN7nbQZQO68qSb4CM7Xn84OIFCcXr1M%2F2tQKt85HwMwNaOhLyAWUZqrvTL64NlsxYU3MzTeTbsMr%2FgovPRykBjU6aDyJSQTbIFyV2DMzqC89NWxbQxCgbZZPPeqPdkEsE01J5uWuLI%2BWcbMKaCiX6yLeqlOFKY%2FknVmf%2FgLh8XnGQkvNlY%2FdC6b4wgF%2BHFw9%2F7Kg2DLqYo5hM%2B%2Bvz8p%2Brh4LFPCRUvlrvwp4iqgYaXaTDWv75lDCz%2FKG%2FBjqkAbDENTyQR1r9C3Hsbv3TbW8j%2BBqyVK67jXOXoq1IASQoBMjSWSCtuYXzVxxEurImNCu1Q7rLnF5pUudS%2FPzqiLRKBV3GTBlhhzqw6ASE0FsfvBy%2Fef94U5k7kJQMUd6wfGW2CVKuz5oZtoaHEdIpc9L8fk1ktvmJyGhEzyr%2BNCn0BMGTWNNNmXCH%2F5mPyKloEYtns0QwIx9f4uK9qbObSOeO13Pl&X-Amz-Signature=90d74366b12ccbe0f05a2428a38fc4e631f686fa14817f375b5f3b82a5c1bdd7&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8f1b1d60-cf1b-42b3-9faa-f634c89c3f84/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664CPHLRTF%2F20250330%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250330T004512Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBcaCXVzLXdlc3QtMiJIMEYCIQDLjTMAmhN0mraY9W4b4hY7QrTjh57gS%2BxlwDiwBuFMKAIhALVxRfCumOz8zntfx9CaFZF9gw4U274%2BN5O9P62Qb57UKogECID%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxRS%2B79IJ47EEFlDOAq3AP30m0MztDDRGu%2BBPt%2BZ%2Bs9v3xjUDFeCXXM%2BtoG9HmsuRmm8NsRIRWt0oU2m01x2lw6HcM4oR6O2sOORye7UDHf4cd%2BdrlNhU9QBR49Zqg8nm35ywMmuSAQkkIEik48pZoESncpAF%2BcA%2FmK6kiOxUyUfSK2HGs2iDKW1U%2FjKv2Verx%2BFbgBeTNELJCcsA%2FXuSYsHCuOr%2FNMlNIozbleofPgdZOvV8%2FE7nsJWSJxVrQSZkH80pIOlW7%2B2%2FbgP0XTxhlRUH9TzRcS4I%2BkIQ21MYb2DODhacMhmXIQIkiybH%2F9qUpv7sZGMXkXCazSLD5A3xgVdWY%2B%2F8JLlbJd56hcFIeIKbcYEBx2PEyo8eit%2Blls0wQtHbkESAZY3qa0LVMC4LjAzS0BWCgtN7nbQZQO68qSb4CM7Xn84OIFCcXr1M%2F2tQKt85HwMwNaOhLyAWUZqrvTL64NlsxYU3MzTeTbsMr%2FgovPRykBjU6aDyJSQTbIFyV2DMzqC89NWxbQxCgbZZPPeqPdkEsE01J5uWuLI%2BWcbMKaCiX6yLeqlOFKY%2FknVmf%2FgLh8XnGQkvNlY%2FdC6b4wgF%2BHFw9%2F7Kg2DLqYo5hM%2B%2Bvz8p%2Brh4LFPCRUvlrvwp4iqgYaXaTDWv75lDCz%2FKG%2FBjqkAbDENTyQR1r9C3Hsbv3TbW8j%2BBqyVK67jXOXoq1IASQoBMjSWSCtuYXzVxxEurImNCu1Q7rLnF5pUudS%2FPzqiLRKBV3GTBlhhzqw6ASE0FsfvBy%2Fef94U5k7kJQMUd6wfGW2CVKuz5oZtoaHEdIpc9L8fk1ktvmJyGhEzyr%2BNCn0BMGTWNNNmXCH%2F5mPyKloEYtns0QwIx9f4uK9qbObSOeO13Pl&X-Amz-Signature=a12f708ddce6644ecce78f3dd1eac04fd97227dc0b066df3a916bf46e8f7f269&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/13ad0497-05fe-4eaa-984e-707b33e14761/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664CPHLRTF%2F20250330%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250330T004513Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBcaCXVzLXdlc3QtMiJIMEYCIQDLjTMAmhN0mraY9W4b4hY7QrTjh57gS%2BxlwDiwBuFMKAIhALVxRfCumOz8zntfx9CaFZF9gw4U274%2BN5O9P62Qb57UKogECID%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxRS%2B79IJ47EEFlDOAq3AP30m0MztDDRGu%2BBPt%2BZ%2Bs9v3xjUDFeCXXM%2BtoG9HmsuRmm8NsRIRWt0oU2m01x2lw6HcM4oR6O2sOORye7UDHf4cd%2BdrlNhU9QBR49Zqg8nm35ywMmuSAQkkIEik48pZoESncpAF%2BcA%2FmK6kiOxUyUfSK2HGs2iDKW1U%2FjKv2Verx%2BFbgBeTNELJCcsA%2FXuSYsHCuOr%2FNMlNIozbleofPgdZOvV8%2FE7nsJWSJxVrQSZkH80pIOlW7%2B2%2FbgP0XTxhlRUH9TzRcS4I%2BkIQ21MYb2DODhacMhmXIQIkiybH%2F9qUpv7sZGMXkXCazSLD5A3xgVdWY%2B%2F8JLlbJd56hcFIeIKbcYEBx2PEyo8eit%2Blls0wQtHbkESAZY3qa0LVMC4LjAzS0BWCgtN7nbQZQO68qSb4CM7Xn84OIFCcXr1M%2F2tQKt85HwMwNaOhLyAWUZqrvTL64NlsxYU3MzTeTbsMr%2FgovPRykBjU6aDyJSQTbIFyV2DMzqC89NWxbQxCgbZZPPeqPdkEsE01J5uWuLI%2BWcbMKaCiX6yLeqlOFKY%2FknVmf%2FgLh8XnGQkvNlY%2FdC6b4wgF%2BHFw9%2F7Kg2DLqYo5hM%2B%2Bvz8p%2Brh4LFPCRUvlrvwp4iqgYaXaTDWv75lDCz%2FKG%2FBjqkAbDENTyQR1r9C3Hsbv3TbW8j%2BBqyVK67jXOXoq1IASQoBMjSWSCtuYXzVxxEurImNCu1Q7rLnF5pUudS%2FPzqiLRKBV3GTBlhhzqw6ASE0FsfvBy%2Fef94U5k7kJQMUd6wfGW2CVKuz5oZtoaHEdIpc9L8fk1ktvmJyGhEzyr%2BNCn0BMGTWNNNmXCH%2F5mPyKloEYtns0QwIx9f4uK9qbObSOeO13Pl&X-Amz-Signature=7fe77ec2a81777fa7c286d17922b07b83424631982c8f31ca7c026bb97817017&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 2. Box and Whisker Plot
A box plot shows the distribution of quantitative data in a way that facilitates comparisons between variables or across levels of a categorical variable. The box shows the quartiles of the dataset while the whiskers extend to show the rest of the distribution, except for points that are determined to be "outliers".
**Syntax:**
```python
sns.boxplot(x='header_1', y='header_2', data=df)
```
**Example Output:**


![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d207ae92-0a7c-4e2f-aa65-0ee5a2c33bf7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UVZ72QEI%2F20250330%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250330T004514Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBcaCXVzLXdlc3QtMiJHMEUCIQCpXhpSiEiIlHarHcgYu3OtCixsZAByt1WqjTS9Hcm1ZgIgG3%2FIN9dhao2LmqVJ21TqZSmnCf9wyruN93IVvhTKeQMqiAQIgP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOLEyYInlGJ1xl%2FiYSrcA25KVDUgVgkpyZCJ5QKaBBZcVMvgwBQdhWbstnBCro8ooYyCE79TxlGQr17nMh8wqQ%2BfoEfIc97du5XbGsNT4O%2FTDWA0A1qWbGk7uEjW30tkkY6RY5twTAwGOq%2FL3sBgfEIZd9ZEmnUVzihdA3lFEXag%2BxI7MXD3NPBNbkbaLrOfs%2Fi1HSchvuMRQGiBPX%2BOyk7P48FkncGragoOKsViV65OUSNbkH%2Bdl8nIAbb3fbKX27DHt9rBsIfB%2BbVco%2BkDt3epTcIf82FUHZJGLFN%2Frd6%2FjYuAm8SLHeaibXil%2BVXQFeBhjr0pvwoQb%2BdR9ziEx3j7nkE11WF8lDPugyfhJ%2ByrxD7BAsF6Pk66bpsI3kLQ3SmEKOpph2PeAyt7%2FnX3VjuAcGl28kX36d%2BcQTkDWIwhVKyh8M3QpIkHe80ToBH2gBYEGTQUW8t5PKeTmOfMNgutKgNWfYC74Rb3SJddt%2FJhh9tgwvhQ4H8HJShZ1igl19FliMyajTS2bjOe%2BMovzR%2FqnUNc1PmVxkXWl7jXFAbH0HYHNFr0uULQ3uXwAjtjyeU%2BPU3daXjxIOxvqj7I61xnR0FK8BvvJ0Wytdpf139rsWmER7GsZGI2FWFH41le8clUs5h%2BKtSL08KtMKX8ob8GOqUBL5cMIoqwMNMQ8fqIyLZoc60Qk1Y8N4wCNHE0VQNowvCPllBJ3yQvnP4ujaOJawP7GMLWZclCOjyF23YNNqP%2BAA4oj8jUUJuBDb6yZFHSWw5alvMmKB2s4fjuirU6dUSH%2BT0qf%2FUe0uwtfpTYAGf1M3IWihu7upbn6617sde7wzef1CWkrbD31LJromyzQMNx1LUwQbWGgpEFZ8Hcbiz%2BlrFT1Oze&X-Amz-Signature=eb8356212bab203be9c96d8af508e9c288628873672cfe9000cf40949c8387e1&X-Amz-SignedHeaders=host&x-id=GetObject)

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0e516edc-7551-4792-ab18-0494db3c4c0c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46624WXQHDB%2F20250330%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250330T004514Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBcaCXVzLXdlc3QtMiJHMEUCICRq8nk26P5bMQ%2F5PIi%2Bepyufh27g%2BoUT6oU%2FqyI0Q9gAiEAksYKkvVRmXjQGCoYUezQea%2Fl7HdpVtzJFjKIugwz36gqiAQIgP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDEi%2FxlBvWme8fadrXyrcA2juf1eBGN4q8top79AHPldcHUsHXlzh8TqMW7mk1LK4htcoaFdmqxMVC48EFbn1lCsAReza5%2FZDSMWfh7NYlfdr%2FELMW2ga6yjJoUKL%2B1Wcui7YMkFFhiE1vebDa68Bx6ub1GMcVNRaDH4L3jgH110a62EgGs72ipA9k0pudkLXQvCpbevvu5Q5kJ%2BY9s1Tw9BSJTg4lR8zbVbUsezXOfP431seTPOXLtFVITBXeeCZ%2FVTXc0FRUbW1VNcz8ZWWeghL0rylKuqbYMG9eEFrKtySJx6Oas5T%2BZH9plQCn1vhL1jmw%2B59z50cV%2F%2FMQl6an1CSG1Tavj8n6wmABzkHfpvJIpbTK2qL9aamtF0bCYqFF9vWL651Nv9ACyA2a8V4y%2F3r2KKvUecWLJ4rWIJGdSMfIuOpPR9PMYS5ao5XD4aROuhltTe1WQO9cpkPWiLN1svr0S637rANcOrdUephG1JmfyRY28mi9YMR1qJqruhILwixlhi64wYj1lXZDa7hACt6v0fzZWp0QrZ7HV2uWhoegWmPmFBt5jLpwfKoYib1ewXzHwIY1Ge3MIRxPSFYMKUaL%2FbmzYPt5xGCFkRcgHa%2Fz1hO6O4knvLFr42SNPu3OUz4%2BJIuniQYOrnBMNT8ob8GOqUBBACbYs2aMkpS7iv%2FTDhOj3joKK%2Fj9prl5feN315jgf2yuBmHKqrxMP%2BI28QmSRUuRBBHSrftE7qAh2D%2F8nmXUV99ojhuDIPaZHx3vws4Fi3eCXD0nZPSjzvlSCdWsK1sfIEk9luvlg%2B0F7SbQCOjX%2BSB2wpI8LINbIcUEgxXTppf28oG0H9R4241iXtIKe9c0%2BQpHJv9grpMwKsUBXFW9b1oNIxr&X-Amz-Signature=158db24f2fecb4ee87621f9ecebdc65e9fa8ddf61a7fc80a9e859b1484138408&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23a79b9d-2356-49a9-8fd9-65c6b0ab2cc5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664CPHLRTF%2F20250330%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250330T004513Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBcaCXVzLXdlc3QtMiJIMEYCIQDLjTMAmhN0mraY9W4b4hY7QrTjh57gS%2BxlwDiwBuFMKAIhALVxRfCumOz8zntfx9CaFZF9gw4U274%2BN5O9P62Qb57UKogECID%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxRS%2B79IJ47EEFlDOAq3AP30m0MztDDRGu%2BBPt%2BZ%2Bs9v3xjUDFeCXXM%2BtoG9HmsuRmm8NsRIRWt0oU2m01x2lw6HcM4oR6O2sOORye7UDHf4cd%2BdrlNhU9QBR49Zqg8nm35ywMmuSAQkkIEik48pZoESncpAF%2BcA%2FmK6kiOxUyUfSK2HGs2iDKW1U%2FjKv2Verx%2BFbgBeTNELJCcsA%2FXuSYsHCuOr%2FNMlNIozbleofPgdZOvV8%2FE7nsJWSJxVrQSZkH80pIOlW7%2B2%2FbgP0XTxhlRUH9TzRcS4I%2BkIQ21MYb2DODhacMhmXIQIkiybH%2F9qUpv7sZGMXkXCazSLD5A3xgVdWY%2B%2F8JLlbJd56hcFIeIKbcYEBx2PEyo8eit%2Blls0wQtHbkESAZY3qa0LVMC4LjAzS0BWCgtN7nbQZQO68qSb4CM7Xn84OIFCcXr1M%2F2tQKt85HwMwNaOhLyAWUZqrvTL64NlsxYU3MzTeTbsMr%2FgovPRykBjU6aDyJSQTbIFyV2DMzqC89NWxbQxCgbZZPPeqPdkEsE01J5uWuLI%2BWcbMKaCiX6yLeqlOFKY%2FknVmf%2FgLh8XnGQkvNlY%2FdC6b4wgF%2BHFw9%2F7Kg2DLqYo5hM%2B%2Bvz8p%2Brh4LFPCRUvlrvwp4iqgYaXaTDWv75lDCz%2FKG%2FBjqkAbDENTyQR1r9C3Hsbv3TbW8j%2BBqyVK67jXOXoq1IASQoBMjSWSCtuYXzVxxEurImNCu1Q7rLnF5pUudS%2FPzqiLRKBV3GTBlhhzqw6ASE0FsfvBy%2Fef94U5k7kJQMUd6wfGW2CVKuz5oZtoaHEdIpc9L8fk1ktvmJyGhEzyr%2BNCn0BMGTWNNNmXCH%2F5mPyKloEYtns0QwIx9f4uK9qbObSOeO13Pl&X-Amz-Signature=e2825e7772cae6407155ed9b16232a63a7f8095dee66b8ee80f0883b8bbb2f76&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 4. KDE Plot
A Kernel Density Estimate (KDE) plot is a graph that creates a probability distribution curve for the data based upon its likelihood of occurrence on a specific value. This is created for a single vector of information.
**Syntax:**
```python
sns.kdeplot(X) || sns.kdeplot(df['age'])
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0d571213-2a2f-4921-a50b-880847aa05ee/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664CPHLRTF%2F20250330%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250330T004513Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBcaCXVzLXdlc3QtMiJIMEYCIQDLjTMAmhN0mraY9W4b4hY7QrTjh57gS%2BxlwDiwBuFMKAIhALVxRfCumOz8zntfx9CaFZF9gw4U274%2BN5O9P62Qb57UKogECID%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxRS%2B79IJ47EEFlDOAq3AP30m0MztDDRGu%2BBPt%2BZ%2Bs9v3xjUDFeCXXM%2BtoG9HmsuRmm8NsRIRWt0oU2m01x2lw6HcM4oR6O2sOORye7UDHf4cd%2BdrlNhU9QBR49Zqg8nm35ywMmuSAQkkIEik48pZoESncpAF%2BcA%2FmK6kiOxUyUfSK2HGs2iDKW1U%2FjKv2Verx%2BFbgBeTNELJCcsA%2FXuSYsHCuOr%2FNMlNIozbleofPgdZOvV8%2FE7nsJWSJxVrQSZkH80pIOlW7%2B2%2FbgP0XTxhlRUH9TzRcS4I%2BkIQ21MYb2DODhacMhmXIQIkiybH%2F9qUpv7sZGMXkXCazSLD5A3xgVdWY%2B%2F8JLlbJd56hcFIeIKbcYEBx2PEyo8eit%2Blls0wQtHbkESAZY3qa0LVMC4LjAzS0BWCgtN7nbQZQO68qSb4CM7Xn84OIFCcXr1M%2F2tQKt85HwMwNaOhLyAWUZqrvTL64NlsxYU3MzTeTbsMr%2FgovPRykBjU6aDyJSQTbIFyV2DMzqC89NWxbQxCgbZZPPeqPdkEsE01J5uWuLI%2BWcbMKaCiX6yLeqlOFKY%2FknVmf%2FgLh8XnGQkvNlY%2FdC6b4wgF%2BHFw9%2F7Kg2DLqYo5hM%2B%2Bvz8p%2Brh4LFPCRUvlrvwp4iqgYaXaTDWv75lDCz%2FKG%2FBjqkAbDENTyQR1r9C3Hsbv3TbW8j%2BBqyVK67jXOXoq1IASQoBMjSWSCtuYXzVxxEurImNCu1Q7rLnF5pUudS%2FPzqiLRKBV3GTBlhhzqw6ASE0FsfvBy%2Fef94U5k7kJQMUd6wfGW2CVKuz5oZtoaHEdIpc9L8fk1ktvmJyGhEzyr%2BNCn0BMGTWNNNmXCH%2F5mPyKloEYtns0QwIx9f4uK9qbObSOeO13Pl&X-Amz-Signature=0634a8b6151061b6a059ebaa4f75840cf08d2baa328bc8ee9bab3c0037ea8349&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/53752550-ef82-4ca9-a01a-09921f0282d0/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664CPHLRTF%2F20250330%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250330T004513Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBcaCXVzLXdlc3QtMiJIMEYCIQDLjTMAmhN0mraY9W4b4hY7QrTjh57gS%2BxlwDiwBuFMKAIhALVxRfCumOz8zntfx9CaFZF9gw4U274%2BN5O9P62Qb57UKogECID%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxRS%2B79IJ47EEFlDOAq3AP30m0MztDDRGu%2BBPt%2BZ%2Bs9v3xjUDFeCXXM%2BtoG9HmsuRmm8NsRIRWt0oU2m01x2lw6HcM4oR6O2sOORye7UDHf4cd%2BdrlNhU9QBR49Zqg8nm35ywMmuSAQkkIEik48pZoESncpAF%2BcA%2FmK6kiOxUyUfSK2HGs2iDKW1U%2FjKv2Verx%2BFbgBeTNELJCcsA%2FXuSYsHCuOr%2FNMlNIozbleofPgdZOvV8%2FE7nsJWSJxVrQSZkH80pIOlW7%2B2%2FbgP0XTxhlRUH9TzRcS4I%2BkIQ21MYb2DODhacMhmXIQIkiybH%2F9qUpv7sZGMXkXCazSLD5A3xgVdWY%2B%2F8JLlbJd56hcFIeIKbcYEBx2PEyo8eit%2Blls0wQtHbkESAZY3qa0LVMC4LjAzS0BWCgtN7nbQZQO68qSb4CM7Xn84OIFCcXr1M%2F2tQKt85HwMwNaOhLyAWUZqrvTL64NlsxYU3MzTeTbsMr%2FgovPRykBjU6aDyJSQTbIFyV2DMzqC89NWxbQxCgbZZPPeqPdkEsE01J5uWuLI%2BWcbMKaCiX6yLeqlOFKY%2FknVmf%2FgLh8XnGQkvNlY%2FdC6b4wgF%2BHFw9%2F7Kg2DLqYo5hM%2B%2Bvz8p%2Brh4LFPCRUvlrvwp4iqgYaXaTDWv75lDCz%2FKG%2FBjqkAbDENTyQR1r9C3Hsbv3TbW8j%2BBqyVK67jXOXoq1IASQoBMjSWSCtuYXzVxxEurImNCu1Q7rLnF5pUudS%2FPzqiLRKBV3GTBlhhzqw6ASE0FsfvBy%2Fef94U5k7kJQMUd6wfGW2CVKuz5oZtoaHEdIpc9L8fk1ktvmJyGhEzyr%2BNCn0BMGTWNNNmXCH%2F5mPyKloEYtns0QwIx9f4uK9qbObSOeO13Pl&X-Amz-Signature=b7e40a3fc2aac902944f347269e69239a7756ef6d1318f82c6b66718170eebdd&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
## 4. Correlation Between Variables
Correlation is a statistical measure of the extent to which different variables are interdependent. It indicates how changes in one variable are associated with changes in another variable over time.
### Positive Correlation
Positive correlation indicates that as one variable increases, the other variable also tends to increase.
**Example: Engine Size and Price**
- **Positive Correlation:** Engine size increases, price also increases.
- **Visualization:** Scatter plot with a steep positive slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c7ea9b0-3ef3-4357-a9c3-554fc71b6b15/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RNR4ODR2%2F20250330%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250330T004514Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBcaCXVzLXdlc3QtMiJHMEUCIQD09%2FEuApJjLQ3IXDrrapHVKD%2FUl9XijKiJEAcRx8cA4gIgNEL52yEPC7NnAa7EMba1jnrJb0VzKnhwhONp0R7g0zwqiAQIgP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDAG2kK5xnywk5vwLACrcA4%2B7iQVi06b0EIMUxpzQP5DIDtahepTPFYka1V%2BIgsgQQNOsvHF8KkIAxf4XuMvgBByn3PKI1c7yhXwoafPFc5iXJ1uvTsTHfm2bskAInGHCvV9QnTQDJwwsdjsiH9QXysqpRZzSM2v62xFCA4jzcfp9R2cvCgs00r7i%2Bt2xvpBLdKfT6fsJGorlqp7SvQNIJejI6bQQdHvocf%2B2f%2BU0Es7MHQjRkNykRP69KgnZemUqUj9%2BIiZi0M9yRTkC0xopFLCOLtXYTyDy9y1EqOb216ZfY7TR8i9grSgdggME%2B01KrH19ypn4lUnfrjN9iIRYH0aW8NRWrEnTz4yjgBNCderLp%2Ff4UqPentk1LtP7hlZ7u9G5tOe%2Bf%2B9EZ9ewCbOMRpsD%2BZNq9zIi9SJLxTUK9DKHCbQGvMcmCCX3uJgDY%2FsUqplt%2BgmbM6iAWCCjz10W%2Fa4GiC42b%2F3ejfTNvKHFEmWWhMnW5qCmUAqLVeM%2FKbtg%2BGCBfjMe%2BpBBhI10jROkXAAXoxj2Zxn72PCpwrLLlOW%2FyIu4npKNYM2LYcdCT8hUNgEmqYDsvtMlCaWYEBPleDzD8MhVkMYWG2SriFg8%2BbdW3GQyL8%2BU7k90%2FUWNXthohPo0EC8CtOl2bqOcMLj8ob8GOqUBULtaEyczkj61k67KXY3pvrqcT7vgN0b%2BZcYXjVpGW8xTPfcy4JEdicVHy%2BcH%2BhLz0G%2FnqMyHRWXGqBmpQYYHEMgq279uUGENZAaOl1rFO3AYyUusHK58bCjHuoBfI54pieahGoYgIekgk6g0E7%2FamnWnA2CVLC8JnsNSE6Co8b3YEWS15ZYDoWCESnKOX9LbRI0aYWL27DrmX68RdzGwJWjJk05L&X-Amz-Signature=757896ff954125d78f00d74ce8de19b138fbff4d29fcbd6a00875dd003d3b705&X-Amz-SignedHeaders=host&x-id=GetObject)
**Explanation:** When engine size increases, there is a corresponding increase in the price of the vehicle. This positive correlation suggests that larger engines tend to be associated with higher prices in the market.
___
### Negative Correlation
Negative correlation indicates that as one variable increases, the other variable tends to decrease.
**Example: Highway Miles per Gallon and Price**
- **Negative Correlation:** As highway miles per gallon increases, price decreases.
- **Visualization:** Scatter plot with a steep negative slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/10f1f798-9cc4-4df2-a9c1-5a339f554a0b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SUTZTKUJ%2F20250330%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250330T004514Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBcaCXVzLXdlc3QtMiJGMEQCIDKvotsX%2BTfsYCctfuNqsS5Ik58nVyQppVucObJxeH2sAiAc71NKQySp%2Fj1lu7IkKOVmbYHjxkXpACiNGPIYIJvlISqIBAiA%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMPwVUA2p9KACc7pTdKtwDzTqVpc7YjMebBLTqpmDSIX9UujxuidxAeoQ1MUcIDpuDS2NlD7NT81IsipaY9kCHfBsDBVMpypeAQ4wis7IEV340QI%2F%2BJNniNZ%2FVHNw9HkVJrFy%2BWqsPhkGq9DP26QeRn1lKXX1tjEgkQnLs9HncsNjNZlIB3TUg%2B09w28ZUxNBJiOWoCyo3kfZC%2B3Um5YwlD8932%2Fw1gP%2FYqMjWM9nUmGgS0T6lz7pp%2BU%2FyDAVdBTJTxATM7BhiErR180uKWXUPjrO8fV9Eq5nivU0vQSkbenXeTopJM%2BeeVoFqSVWt9K3nDj85iWpED00loaEOVNsvHtPg0yBxNsoigvZVn3xg6UNdEhRD9ufbmykdpTTjYgBgpFmN8mBcCTQcqN8msEg2F6kuk5KzeW8tpf6FDCyzS1pqxOV3pc3yJTCd6gJ84BoQQKTI8wrzgVX2ViUIufhviR26KO93Ov4i97gopNX41neuXe1aHqazK4I9%2FpEViGvxMgDDVDckZXMUQBOfJn0sKMfXbeHI5cd%2BLLPA3uQuYfb5%2FXxGp%2BhJUVBYyosre9Xgzl3d7mLWCKAy0wd2r%2Fz%2Fs%2BWdYLFVDMv9JPm9zCuxuGb36HIz4OrA9Vzg2zmwOUWzGH7h4IKDI%2B9e3zIwnPyhvwY6pgEdX9AVz4F2stEdbYLGMKlycmY0q%2FM5o9kv9OnrMQuFRYxgQ07xpa7ccs%2BRDJ%2FBXgbVzYLDg71w4%2FwsjBTlnnknGv%2FbzRwgx0XKCQN2MLEQvOhkF%2FIfDkk0OvSNrniC2Cdt1J5Nb39b%2FI9lpf3sBIROE77tRPg6hvmbWHTzVHgRULTcPngfG1hExnyln6tp2uT7IFnj95qUSmRhnBb4Vbb03A%2Fe71So&X-Amz-Signature=d3c4ee6ad1eb3b45d663365e9d8329db6186b46e98f3695eb226facda730a4d9&X-Amz-SignedHeaders=host&x-id=GetObject)
**Explanation:** When highway miles per gallon increases, the price of the vehicle tends to decrease. This negative correlation suggests that cars with higher fuel efficiency (more miles per gallon) are generally priced lower in the market.
___
### Weak Correlation
Weak correlation indicates a lack of strong relationship between the variables.
**Example: RPM and Price**
- **Weak Correlation:** Low and high RPM values show varied prices, indicating no strong predictive relationship.
- **Visualization:** Scatter plot with no clear trend or slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9f914514-8914-4bf4-ac84-d9e3077f6eb1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46662LOXQ3M%2F20250330%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250330T004514Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBcaCXVzLXdlc3QtMiJHMEUCIQDlxI4gN2hwhmzSkrEB2lSlfosUD5sUhOYKMH8UR5AljwIgHDr5eHjL1Q%2FamRUofyCjzlOxVdod9TSwDQd0xfHaG%2FIqiAQIgP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMEszKRW%2FIYbPsQ4XSrcAwG7PQjRZ%2B0ok%2FuVeL96XLM1tQPMCP%2BWYab2uBgwHUYdKhP0KIusZC2PYYq%2FuQI5j3lDEkN%2BEALupiMfA3X6UUDnbZcym6Yu9AEg5id%2FuwX5XJKeBz7%2FxKrjUBPVfLPlXS%2Bg2hK8FX09Dj8Ke%2BMJH%2BqIKMt8cYf6hr9kbhTHmxbDTp0TLVCkNBK7vPl0TIGyRhIRDDDZmyBxAJD1wu%2B2QqA7mvG%2F4A6bWj56GO0o%2BPuV%2FcqEsIqxqJWOsFYtEDyvRNy8GwF1fCaFoamOGCOXtviL87Skw8FxkDdhxe%2FBSWH2fvkbUewK7Si838cIbu%2F8gwrRKgVQsFaJQDYlpXxn%2FvJtJUspjlbGE5L8XKRUmFJEhjOlqLdt2IEmTEmXGYsa72KulR9DEcSuX14IKKI%2BBJZJ6nID%2BeL%2B6JgOCEQ2Xs5bxyP%2FKGLb4Kl3BQ1KtNfPHttPNueij9wirdgCxOPr%2Fa9uWNgUf%2FMsBsAvXA90RMGJ8KiG9kM%2Fuy2TejPKup%2BFGlUqBHyY%2FtiMzYBTLcLua40S%2BYjYX3bLhp2HZbAAvWvIpjQNhPr4jVcpP%2B6tJstfsCBFX%2FQDesTCW6ahmcs%2FJU6aRGKBZrqipyp5lYvJ9TdxphrFWeZSRm7wkj9UMK%2F8ob8GOqUBcxNe5u6%2FqNftxLAP1TGsaRZ1XS09JbuRhtA3lEHKJokIwcJrsijUrhSiyeD26VDAkd6En1L7IqXeLyuBtLPBtll%2Bzdr3rFFoFAt1TnNh%2BFyNFbpmBHgf286bpqaHh1VIiL3XNCAmuti7yGMF%2BqmCpYF8zb4Ifw3ckxCdQU1ZnIR7EBCcP3kBZVqOxCw6jqHOsY%2Br1522IoSn53vSmJc7l56D2Sv1&X-Amz-Signature=e5789ea11c110f3cfd3f0a05af33739ca66a6cf3550ecbf09f84c7f27fc65a69&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f18086e5-5b04-4fbf-8309-8944ab20d213/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QMX7GSPJ%2F20250330%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250330T004513Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBcaCXVzLXdlc3QtMiJHMEUCIG%2FU9GLBP%2Fcsilcfe1fhGugMOfQ7MPyvAKYkNxErWBJMAiEAuDsfhYq3tzKb%2FHmIBvO0%2FUAivFNiguEXs4jDcb02l9YqiAQIgP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDEm2Gjevag8zPLTSRircA0lbo9V3FXwAMTgbQCPauu0m9NhOKMOCkyrdHpobWe1gxiJO5PM%2FV9t4zRrtjzxi4xPTDRsyGHPtGKbDh1lsbXCHQg2EHDyru7fdZjX6ElIuW2dGk7gl3t7eN3qtheKn0I44Wr%2FiGW%2F5d0w%2Fx%2FkrwritZ6llNN21NpelhirL4sR8CwzBWJav3XbXHuuK%2BYhaVSXRj4Czn%2B3yCwCeS5IlBH4AUPYE6qWMiCNfnfRspemaYu0OClCZSra8s6hG06656yGeu2WnumRJvIdvBVL7YBKndZYtkO%2FmWDVM70%2Bdr%2F%2Fsso4Y%2BgjcuV0ylu4sHAM0KtcYmoNBhtUaNc7omkP4KMWGndlbeJLpQXM8ht83tcyvGFlkXXOjDMmmDiZzhZwebofb78ZpeP5S04lpFodGLuau%2Bi2be9KbyLusmKJkFgiV35Yq38gHkLxUsQyOEHzpPjj2PEowBCUYO34p45ILWqAA99Opo4JAmRCRqG5wjt1ebR6BnfzZBYHd%2BrVIIlIXmmW%2BD3SQWMla3yiE5LO1l8%2BIQWW2h53MRokCPa7yiUYD%2BqAfZOYaCjLiM29oCOIjIuDXHSGuayqMI5hgtflQbmM2TvN36nd9Lj35wSeENBn%2Fy9ltno%2F7d7inZgseMMH8ob8GOqUBe9Wn6XobA%2FNupK2LsGrtolu11ORy6a7Rp5AatNmpyM6AEW59Ogjn8YdNDogbwKI05X93bYzlfRQudL2JFVdirsskjM5P9KQOxn%2Blhw42R0l6fB9bWFQ5JjdhyBgyCzzeNlMSvU9M0mPVI%2BYc%2FBhQu5rodF1%2B6ju5yucz850sBEUmvFKwviVAft%2BeZ0eHjC1n429994yZ3FKhzazTXD5pZQ02KixQ&X-Amz-Signature=25d8510663b9d2c19fc95ab006ac4a90241abb5cc2fd7bc5f56ad6109721a8d0&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Correlation Plot
Heatmap visualizes correlations among variables. Color scheme indicates Pearson correlation coefficients. Dark red diagonal line shows perfect correlation (value of 1) between variables and themselves.
This heatmap offers overview of variable relationships and their link with price.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cd3b341e-cc1a-45f7-8aec-cdc00436d270/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QMX7GSPJ%2F20250330%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250330T004513Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBcaCXVzLXdlc3QtMiJHMEUCIG%2FU9GLBP%2Fcsilcfe1fhGugMOfQ7MPyvAKYkNxErWBJMAiEAuDsfhYq3tzKb%2FHmIBvO0%2FUAivFNiguEXs4jDcb02l9YqiAQIgP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDEm2Gjevag8zPLTSRircA0lbo9V3FXwAMTgbQCPauu0m9NhOKMOCkyrdHpobWe1gxiJO5PM%2FV9t4zRrtjzxi4xPTDRsyGHPtGKbDh1lsbXCHQg2EHDyru7fdZjX6ElIuW2dGk7gl3t7eN3qtheKn0I44Wr%2FiGW%2F5d0w%2Fx%2FkrwritZ6llNN21NpelhirL4sR8CwzBWJav3XbXHuuK%2BYhaVSXRj4Czn%2B3yCwCeS5IlBH4AUPYE6qWMiCNfnfRspemaYu0OClCZSra8s6hG06656yGeu2WnumRJvIdvBVL7YBKndZYtkO%2FmWDVM70%2Bdr%2F%2Fsso4Y%2BgjcuV0ylu4sHAM0KtcYmoNBhtUaNc7omkP4KMWGndlbeJLpQXM8ht83tcyvGFlkXXOjDMmmDiZzhZwebofb78ZpeP5S04lpFodGLuau%2Bi2be9KbyLusmKJkFgiV35Yq38gHkLxUsQyOEHzpPjj2PEowBCUYO34p45ILWqAA99Opo4JAmRCRqG5wjt1ebR6BnfzZBYHd%2BrVIIlIXmmW%2BD3SQWMla3yiE5LO1l8%2BIQWW2h53MRokCPa7yiUYD%2BqAfZOYaCjLiM29oCOIjIuDXHSGuayqMI5hgtflQbmM2TvN36nd9Lj35wSeENBn%2Fy9ltno%2F7d7inZgseMMH8ob8GOqUBe9Wn6XobA%2FNupK2LsGrtolu11ORy6a7Rp5AatNmpyM6AEW59Ogjn8YdNDogbwKI05X93bYzlfRQudL2JFVdirsskjM5P9KQOxn%2Blhw42R0l6fB9bWFQ5JjdhyBgyCzzeNlMSvU9M0mPVI%2BYc%2FBhQu5rodF1%2B6ju5yucz850sBEUmvFKwviVAft%2BeZ0eHjC1n429994yZ3FKhzazTXD5pZQ02KixQ&X-Amz-Signature=0165c7b7c82f1c0f8f3113018ff0cdee16183474cbd203f36d45b591bd35cd01&X-Amz-SignedHeaders=host&x-id=GetObject)

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
