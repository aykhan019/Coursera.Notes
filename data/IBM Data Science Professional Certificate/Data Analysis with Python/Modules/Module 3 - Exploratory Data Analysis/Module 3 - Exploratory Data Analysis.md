

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7e6d594d-952e-44b6-97ea-31225882aea6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XSLCAHWL%2F20250223%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250223T004150Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDJy2kX5HYjIrO%2Fo5zvlvOi8EzMSMoSPn0%2BL6EixVC8ogIgUExz%2FQYH80uRNcmR5awBNHK5EW9ZCuy6jhVv2SKemTkqiAQI%2BP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDL1usXtv%2Bgdl8o8N2ircA7FdPfRW39ZyT6nVq8bJxxOvAsgTpMTMGy%2BFLchCu6BQUeSO6un3UIwVW0cJdl%2BFjXpkjuuyeOQQn0%2FFGg%2FXgCHF59A7OGmi4nbjujR8CFBmPju7f8YIJdUyKWPWXTSZpy0kyH2Idlg76xAPmDVAWATgqO91fwFrLtkfUnl8cZD%2FsIgofkXo3uRu5MakS3nBEDy4CY4ox2Gk50K8O2wYnG95cNAI7p%2B3SbwaWkcaUSIpG98yA8FxCf6N%2FuUJikxEA8kIh52PtvHGl%2B0cCA8Rc58OkMnfPVs%2BN5rxIBF2tWtFgDKaZs75gnDuuswYaU8x9K0ex0ptYKvlWmJ6mMv4MLlOb%2FRg6h50gyF6SmC1Byy2YfytleO9LghC2tyC1FoiHaIKQUKJrxPHdBeDioF511Y5NRf8r05t3kSpN%2F2dxxgG45ato9aKcbh7arxfVKaTMORPCBDCfaaltzUfyCI1Yd2IxrPy5bametqAhuThEBYIjHz%2F2%2BLez7bMEqouHpXhxD0BLMqSOyN9oJI5TdgXa5Pnjvj80MiJCGahvJGaiC51irTD8S2UEuWe9L0oVILFtfZ3wFtrFO%2Fln5qMSw0%2F4N9xVl9itS3goLotqPdNHcnvCHFpBLML3NvY0lSvMPat6b0GOqUB%2BsZqblgo87kurhf4UpF1s%2F4mtH01FcFNkN7dEOe2YFUA8CtY7SSBWSYpn02HOjiRTzg1l%2FTaWs5V4A%2FzVsrj4hzz2cdnrkPrKXXq32UdBpqDl2iAfkamu7NqHSIcISIrVWxEAk6ageUiZXXfGyRXTjBScGFXdbnNmxupG2ZNFBB2o%2F7CEf0r%2FwDFpgdLImAJpEI6i7nNgwGtJ04QqfrQLbKoLLCW&X-Amz-Signature=65efe3142310b9b31dbb3cda5c70c6c578522c790e29a86f963d2480dac61243&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cbfaed9e-b398-4902-8936-dea058b21def/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XSLCAHWL%2F20250223%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250223T004150Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDJy2kX5HYjIrO%2Fo5zvlvOi8EzMSMoSPn0%2BL6EixVC8ogIgUExz%2FQYH80uRNcmR5awBNHK5EW9ZCuy6jhVv2SKemTkqiAQI%2BP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDL1usXtv%2Bgdl8o8N2ircA7FdPfRW39ZyT6nVq8bJxxOvAsgTpMTMGy%2BFLchCu6BQUeSO6un3UIwVW0cJdl%2BFjXpkjuuyeOQQn0%2FFGg%2FXgCHF59A7OGmi4nbjujR8CFBmPju7f8YIJdUyKWPWXTSZpy0kyH2Idlg76xAPmDVAWATgqO91fwFrLtkfUnl8cZD%2FsIgofkXo3uRu5MakS3nBEDy4CY4ox2Gk50K8O2wYnG95cNAI7p%2B3SbwaWkcaUSIpG98yA8FxCf6N%2FuUJikxEA8kIh52PtvHGl%2B0cCA8Rc58OkMnfPVs%2BN5rxIBF2tWtFgDKaZs75gnDuuswYaU8x9K0ex0ptYKvlWmJ6mMv4MLlOb%2FRg6h50gyF6SmC1Byy2YfytleO9LghC2tyC1FoiHaIKQUKJrxPHdBeDioF511Y5NRf8r05t3kSpN%2F2dxxgG45ato9aKcbh7arxfVKaTMORPCBDCfaaltzUfyCI1Yd2IxrPy5bametqAhuThEBYIjHz%2F2%2BLez7bMEqouHpXhxD0BLMqSOyN9oJI5TdgXa5Pnjvj80MiJCGahvJGaiC51irTD8S2UEuWe9L0oVILFtfZ3wFtrFO%2Fln5qMSw0%2F4N9xVl9itS3goLotqPdNHcnvCHFpBLML3NvY0lSvMPat6b0GOqUB%2BsZqblgo87kurhf4UpF1s%2F4mtH01FcFNkN7dEOe2YFUA8CtY7SSBWSYpn02HOjiRTzg1l%2FTaWs5V4A%2FzVsrj4hzz2cdnrkPrKXXq32UdBpqDl2iAfkamu7NqHSIcISIrVWxEAk6ageUiZXXfGyRXTjBScGFXdbnNmxupG2ZNFBB2o%2F7CEf0r%2FwDFpgdLImAJpEI6i7nNgwGtJ04QqfrQLbKoLLCW&X-Amz-Signature=2e9b9c1c0d67d7b645b7a3597771e2551d7997a5f094fcfe6f72c15846b531f5&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/91181646-b1e0-4433-9711-6259a96a9247/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XSLCAHWL%2F20250223%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250223T004150Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDJy2kX5HYjIrO%2Fo5zvlvOi8EzMSMoSPn0%2BL6EixVC8ogIgUExz%2FQYH80uRNcmR5awBNHK5EW9ZCuy6jhVv2SKemTkqiAQI%2BP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDL1usXtv%2Bgdl8o8N2ircA7FdPfRW39ZyT6nVq8bJxxOvAsgTpMTMGy%2BFLchCu6BQUeSO6un3UIwVW0cJdl%2BFjXpkjuuyeOQQn0%2FFGg%2FXgCHF59A7OGmi4nbjujR8CFBmPju7f8YIJdUyKWPWXTSZpy0kyH2Idlg76xAPmDVAWATgqO91fwFrLtkfUnl8cZD%2FsIgofkXo3uRu5MakS3nBEDy4CY4ox2Gk50K8O2wYnG95cNAI7p%2B3SbwaWkcaUSIpG98yA8FxCf6N%2FuUJikxEA8kIh52PtvHGl%2B0cCA8Rc58OkMnfPVs%2BN5rxIBF2tWtFgDKaZs75gnDuuswYaU8x9K0ex0ptYKvlWmJ6mMv4MLlOb%2FRg6h50gyF6SmC1Byy2YfytleO9LghC2tyC1FoiHaIKQUKJrxPHdBeDioF511Y5NRf8r05t3kSpN%2F2dxxgG45ato9aKcbh7arxfVKaTMORPCBDCfaaltzUfyCI1Yd2IxrPy5bametqAhuThEBYIjHz%2F2%2BLez7bMEqouHpXhxD0BLMqSOyN9oJI5TdgXa5Pnjvj80MiJCGahvJGaiC51irTD8S2UEuWe9L0oVILFtfZ3wFtrFO%2Fln5qMSw0%2F4N9xVl9itS3goLotqPdNHcnvCHFpBLML3NvY0lSvMPat6b0GOqUB%2BsZqblgo87kurhf4UpF1s%2F4mtH01FcFNkN7dEOe2YFUA8CtY7SSBWSYpn02HOjiRTzg1l%2FTaWs5V4A%2FzVsrj4hzz2cdnrkPrKXXq32UdBpqDl2iAfkamu7NqHSIcISIrVWxEAk6ageUiZXXfGyRXTjBScGFXdbnNmxupG2ZNFBB2o%2F7CEf0r%2FwDFpgdLImAJpEI6i7nNgwGtJ04QqfrQLbKoLLCW&X-Amz-Signature=e4290c4f842ceca22b9adb69aedb01e4273d1e98f65377358a60b770c84dcc1c&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/09aba1c0-0d55-41dd-852a-a04c5b8a3fac/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XNK2HY6D%2F20250223%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250223T004151Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCHqmVWvDCLLv1%2BQfU4JJXncIHrFfoHiUPVop3dkfkRBAIgHtMyh8Hc4Hcs2Z%2Bbhq0aBsn3SOJbeahiIxRAKKcjCLYqiAQI%2BP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDE2G0fBq4OBZ7cDFHSrcA8swNFQP3xT6Spiz0gvGGmU0RR6mQglCFYuMG21TmWZzQczNMDq2RbroDioFEO24M3CGYRm%2FhwO%2BoEVKFPOphFSSJp%2BARB0r%2BTrYwYJMWrBBr02k%2Fa0RvuQbrLEhQchE25kZb7k2Ptjh1ROFRGy8R7aFEmf9JnCf6EK7VQ1RKfDQlW5XoxQpI0lJyHphS1elaeKSc4CHEoupEpHeYDwpLF%2B54k2B85dDFM%2B86ADBUj16SeSqQ%2BsnshC7sQpl4ysZNGNUiKl0cjXdzlK9q6sN1Vc8pLZdphfdi0mSZgUcAIknK2CJp5y4b87Bpa1B9pS%2BZjsSYfKq88PPmvexVojdhI3d540OVB31TUu75MgsjWQCQLylGX%2FxF74dvL5nsuB2cTiNl%2BJS8aVF3mUWAn17%2BRCEbtSSUtA1zxs8379lyEq3hrhEum6qDxjKVNUJYtQGpOxTOgnjxv4XoynjGZvIRTC8Lbphy%2BgfpPe03g7XvZCyygB3xc8UgFIGjA5tKIHzT7KoNZvykyzfnnELl5hNGAGvad0qnohtakDzFu4fbTJORdcWjYX1X28DKlI78%2BoRpZjaGnO9t8PT%2FT%2BirfD4M2XfnydyIfHJxvPjKJMZCaUpUrQHkmXzo9G%2FKXAdMKKy6b0GOqUBl6copEjQsb8%2Bq825fFFiaLQdhNh0GEg97TZXVjPN78Lg9zHmqkQDLz1YzNslDtLsk1l7LKs1hJN7Ith2PcdNCErDCgi4oaDAIz05HG43u7UPe4EV0z1p09eVIB9K3ivZBf%2FWs5hpH%2B%2Fkbqm1ibyYifkAv9WRwl72Gi%2B47y%2FIy9FhMbdCu8KsllcERFc%2Fv4pZqAfhbGRu3Y4T9oUs09vRZweWG8qr&X-Amz-Signature=72a740dfcd5fc359537f6d367b63a69ffde27deddcfcb786adb1d144c183feb6&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 2. Scatter Plot
Scatter plots present the relationship between two variables in a dataset. It represents data points on a two-dimensional plane. The independent variable or attribute is plotted on the X-axis, while the dependent variable is plotted on the Y-axis.
**Syntax:**
```python
plt.scatter(x, y)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23708af9-659f-4f23-b626-1a4292d7842c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XNK2HY6D%2F20250223%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250223T004151Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCHqmVWvDCLLv1%2BQfU4JJXncIHrFfoHiUPVop3dkfkRBAIgHtMyh8Hc4Hcs2Z%2Bbhq0aBsn3SOJbeahiIxRAKKcjCLYqiAQI%2BP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDE2G0fBq4OBZ7cDFHSrcA8swNFQP3xT6Spiz0gvGGmU0RR6mQglCFYuMG21TmWZzQczNMDq2RbroDioFEO24M3CGYRm%2FhwO%2BoEVKFPOphFSSJp%2BARB0r%2BTrYwYJMWrBBr02k%2Fa0RvuQbrLEhQchE25kZb7k2Ptjh1ROFRGy8R7aFEmf9JnCf6EK7VQ1RKfDQlW5XoxQpI0lJyHphS1elaeKSc4CHEoupEpHeYDwpLF%2B54k2B85dDFM%2B86ADBUj16SeSqQ%2BsnshC7sQpl4ysZNGNUiKl0cjXdzlK9q6sN1Vc8pLZdphfdi0mSZgUcAIknK2CJp5y4b87Bpa1B9pS%2BZjsSYfKq88PPmvexVojdhI3d540OVB31TUu75MgsjWQCQLylGX%2FxF74dvL5nsuB2cTiNl%2BJS8aVF3mUWAn17%2BRCEbtSSUtA1zxs8379lyEq3hrhEum6qDxjKVNUJYtQGpOxTOgnjxv4XoynjGZvIRTC8Lbphy%2BgfpPe03g7XvZCyygB3xc8UgFIGjA5tKIHzT7KoNZvykyzfnnELl5hNGAGvad0qnohtakDzFu4fbTJORdcWjYX1X28DKlI78%2BoRpZjaGnO9t8PT%2FT%2BirfD4M2XfnydyIfHJxvPjKJMZCaUpUrQHkmXzo9G%2FKXAdMKKy6b0GOqUBl6copEjQsb8%2Bq825fFFiaLQdhNh0GEg97TZXVjPN78Lg9zHmqkQDLz1YzNslDtLsk1l7LKs1hJN7Ith2PcdNCErDCgi4oaDAIz05HG43u7UPe4EV0z1p09eVIB9K3ivZBf%2FWs5hpH%2B%2Fkbqm1ibyYifkAv9WRwl72Gi%2B47y%2FIy9FhMbdCu8KsllcERFc%2Fv4pZqAfhbGRu3Y4T9oUs09vRZweWG8qr&X-Amz-Signature=9ffe7bccd6dd92daa5094538e425f8a2f85aef1911be24a6edd52e9b68aa021c&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 3. Histogram
A histogram is an important visual representation of data in categorical form. To view the data in a "Binned" form, use the histogram plot with a number of bins required or with the data points that mark the bin edges. The x-axis represents the data bins, and the y-axis represents the number of elements in each bin.
**Syntax:**
```python
plt.hist(x, bins)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/24e4424a-df87-40a1-b63b-195cbdc2e0ab/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XNK2HY6D%2F20250223%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250223T004151Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCHqmVWvDCLLv1%2BQfU4JJXncIHrFfoHiUPVop3dkfkRBAIgHtMyh8Hc4Hcs2Z%2Bbhq0aBsn3SOJbeahiIxRAKKcjCLYqiAQI%2BP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDE2G0fBq4OBZ7cDFHSrcA8swNFQP3xT6Spiz0gvGGmU0RR6mQglCFYuMG21TmWZzQczNMDq2RbroDioFEO24M3CGYRm%2FhwO%2BoEVKFPOphFSSJp%2BARB0r%2BTrYwYJMWrBBr02k%2Fa0RvuQbrLEhQchE25kZb7k2Ptjh1ROFRGy8R7aFEmf9JnCf6EK7VQ1RKfDQlW5XoxQpI0lJyHphS1elaeKSc4CHEoupEpHeYDwpLF%2B54k2B85dDFM%2B86ADBUj16SeSqQ%2BsnshC7sQpl4ysZNGNUiKl0cjXdzlK9q6sN1Vc8pLZdphfdi0mSZgUcAIknK2CJp5y4b87Bpa1B9pS%2BZjsSYfKq88PPmvexVojdhI3d540OVB31TUu75MgsjWQCQLylGX%2FxF74dvL5nsuB2cTiNl%2BJS8aVF3mUWAn17%2BRCEbtSSUtA1zxs8379lyEq3hrhEum6qDxjKVNUJYtQGpOxTOgnjxv4XoynjGZvIRTC8Lbphy%2BgfpPe03g7XvZCyygB3xc8UgFIGjA5tKIHzT7KoNZvykyzfnnELl5hNGAGvad0qnohtakDzFu4fbTJORdcWjYX1X28DKlI78%2BoRpZjaGnO9t8PT%2FT%2BirfD4M2XfnydyIfHJxvPjKJMZCaUpUrQHkmXzo9G%2FKXAdMKKy6b0GOqUBl6copEjQsb8%2Bq825fFFiaLQdhNh0GEg97TZXVjPN78Lg9zHmqkQDLz1YzNslDtLsk1l7LKs1hJN7Ith2PcdNCErDCgi4oaDAIz05HG43u7UPe4EV0z1p09eVIB9K3ivZBf%2FWs5hpH%2B%2Fkbqm1ibyYifkAv9WRwl72Gi%2B47y%2FIy9FhMbdCu8KsllcERFc%2Fv4pZqAfhbGRu3Y4T9oUs09vRZweWG8qr&X-Amz-Signature=0cf574b1ddf4552c3da532ede15360f7c30fab7f4a862bf2360272fb5b6a7814&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ab5a6dfe-51f5-43ee-bcb3-33dae4a1c7ad/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XNK2HY6D%2F20250223%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250223T004151Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCHqmVWvDCLLv1%2BQfU4JJXncIHrFfoHiUPVop3dkfkRBAIgHtMyh8Hc4Hcs2Z%2Bbhq0aBsn3SOJbeahiIxRAKKcjCLYqiAQI%2BP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDE2G0fBq4OBZ7cDFHSrcA8swNFQP3xT6Spiz0gvGGmU0RR6mQglCFYuMG21TmWZzQczNMDq2RbroDioFEO24M3CGYRm%2FhwO%2BoEVKFPOphFSSJp%2BARB0r%2BTrYwYJMWrBBr02k%2Fa0RvuQbrLEhQchE25kZb7k2Ptjh1ROFRGy8R7aFEmf9JnCf6EK7VQ1RKfDQlW5XoxQpI0lJyHphS1elaeKSc4CHEoupEpHeYDwpLF%2B54k2B85dDFM%2B86ADBUj16SeSqQ%2BsnshC7sQpl4ysZNGNUiKl0cjXdzlK9q6sN1Vc8pLZdphfdi0mSZgUcAIknK2CJp5y4b87Bpa1B9pS%2BZjsSYfKq88PPmvexVojdhI3d540OVB31TUu75MgsjWQCQLylGX%2FxF74dvL5nsuB2cTiNl%2BJS8aVF3mUWAn17%2BRCEbtSSUtA1zxs8379lyEq3hrhEum6qDxjKVNUJYtQGpOxTOgnjxv4XoynjGZvIRTC8Lbphy%2BgfpPe03g7XvZCyygB3xc8UgFIGjA5tKIHzT7KoNZvykyzfnnELl5hNGAGvad0qnohtakDzFu4fbTJORdcWjYX1X28DKlI78%2BoRpZjaGnO9t8PT%2FT%2BirfD4M2XfnydyIfHJxvPjKJMZCaUpUrQHkmXzo9G%2FKXAdMKKy6b0GOqUBl6copEjQsb8%2Bq825fFFiaLQdhNh0GEg97TZXVjPN78Lg9zHmqkQDLz1YzNslDtLsk1l7LKs1hJN7Ith2PcdNCErDCgi4oaDAIz05HG43u7UPe4EV0z1p09eVIB9K3ivZBf%2FWs5hpH%2B%2Fkbqm1ibyYifkAv9WRwl72Gi%2B47y%2FIy9FhMbdCu8KsllcERFc%2Fv4pZqAfhbGRu3Y4T9oUs09vRZweWG8qr&X-Amz-Signature=0e3ec87d79a8f581c4d501b8e5ebf29a110a3c198f84765e9daaf84b21ecc49d&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8f1b1d60-cf1b-42b3-9faa-f634c89c3f84/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XNK2HY6D%2F20250223%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250223T004151Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCHqmVWvDCLLv1%2BQfU4JJXncIHrFfoHiUPVop3dkfkRBAIgHtMyh8Hc4Hcs2Z%2Bbhq0aBsn3SOJbeahiIxRAKKcjCLYqiAQI%2BP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDE2G0fBq4OBZ7cDFHSrcA8swNFQP3xT6Spiz0gvGGmU0RR6mQglCFYuMG21TmWZzQczNMDq2RbroDioFEO24M3CGYRm%2FhwO%2BoEVKFPOphFSSJp%2BARB0r%2BTrYwYJMWrBBr02k%2Fa0RvuQbrLEhQchE25kZb7k2Ptjh1ROFRGy8R7aFEmf9JnCf6EK7VQ1RKfDQlW5XoxQpI0lJyHphS1elaeKSc4CHEoupEpHeYDwpLF%2B54k2B85dDFM%2B86ADBUj16SeSqQ%2BsnshC7sQpl4ysZNGNUiKl0cjXdzlK9q6sN1Vc8pLZdphfdi0mSZgUcAIknK2CJp5y4b87Bpa1B9pS%2BZjsSYfKq88PPmvexVojdhI3d540OVB31TUu75MgsjWQCQLylGX%2FxF74dvL5nsuB2cTiNl%2BJS8aVF3mUWAn17%2BRCEbtSSUtA1zxs8379lyEq3hrhEum6qDxjKVNUJYtQGpOxTOgnjxv4XoynjGZvIRTC8Lbphy%2BgfpPe03g7XvZCyygB3xc8UgFIGjA5tKIHzT7KoNZvykyzfnnELl5hNGAGvad0qnohtakDzFu4fbTJORdcWjYX1X28DKlI78%2BoRpZjaGnO9t8PT%2FT%2BirfD4M2XfnydyIfHJxvPjKJMZCaUpUrQHkmXzo9G%2FKXAdMKKy6b0GOqUBl6copEjQsb8%2Bq825fFFiaLQdhNh0GEg97TZXVjPN78Lg9zHmqkQDLz1YzNslDtLsk1l7LKs1hJN7Ith2PcdNCErDCgi4oaDAIz05HG43u7UPe4EV0z1p09eVIB9K3ivZBf%2FWs5hpH%2B%2Fkbqm1ibyYifkAv9WRwl72Gi%2B47y%2FIy9FhMbdCu8KsllcERFc%2Fv4pZqAfhbGRu3Y4T9oUs09vRZweWG8qr&X-Amz-Signature=8e50710790071d5b52603f0117c0eed8a07f10e29b8a8cfa24a40641e430b850&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/13ad0497-05fe-4eaa-984e-707b33e14761/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XNK2HY6D%2F20250223%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250223T004151Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCHqmVWvDCLLv1%2BQfU4JJXncIHrFfoHiUPVop3dkfkRBAIgHtMyh8Hc4Hcs2Z%2Bbhq0aBsn3SOJbeahiIxRAKKcjCLYqiAQI%2BP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDE2G0fBq4OBZ7cDFHSrcA8swNFQP3xT6Spiz0gvGGmU0RR6mQglCFYuMG21TmWZzQczNMDq2RbroDioFEO24M3CGYRm%2FhwO%2BoEVKFPOphFSSJp%2BARB0r%2BTrYwYJMWrBBr02k%2Fa0RvuQbrLEhQchE25kZb7k2Ptjh1ROFRGy8R7aFEmf9JnCf6EK7VQ1RKfDQlW5XoxQpI0lJyHphS1elaeKSc4CHEoupEpHeYDwpLF%2B54k2B85dDFM%2B86ADBUj16SeSqQ%2BsnshC7sQpl4ysZNGNUiKl0cjXdzlK9q6sN1Vc8pLZdphfdi0mSZgUcAIknK2CJp5y4b87Bpa1B9pS%2BZjsSYfKq88PPmvexVojdhI3d540OVB31TUu75MgsjWQCQLylGX%2FxF74dvL5nsuB2cTiNl%2BJS8aVF3mUWAn17%2BRCEbtSSUtA1zxs8379lyEq3hrhEum6qDxjKVNUJYtQGpOxTOgnjxv4XoynjGZvIRTC8Lbphy%2BgfpPe03g7XvZCyygB3xc8UgFIGjA5tKIHzT7KoNZvykyzfnnELl5hNGAGvad0qnohtakDzFu4fbTJORdcWjYX1X28DKlI78%2BoRpZjaGnO9t8PT%2FT%2BirfD4M2XfnydyIfHJxvPjKJMZCaUpUrQHkmXzo9G%2FKXAdMKKy6b0GOqUBl6copEjQsb8%2Bq825fFFiaLQdhNh0GEg97TZXVjPN78Lg9zHmqkQDLz1YzNslDtLsk1l7LKs1hJN7Ith2PcdNCErDCgi4oaDAIz05HG43u7UPe4EV0z1p09eVIB9K3ivZBf%2FWs5hpH%2B%2Fkbqm1ibyYifkAv9WRwl72Gi%2B47y%2FIy9FhMbdCu8KsllcERFc%2Fv4pZqAfhbGRu3Y4T9oUs09vRZweWG8qr&X-Amz-Signature=2321b2a2dba48a0b7579883471431199b6991bc74922f6f1c327ad26d96fb63a&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 2. Box and Whisker Plot
A box plot shows the distribution of quantitative data in a way that facilitates comparisons between variables or across levels of a categorical variable. The box shows the quartiles of the dataset while the whiskers extend to show the rest of the distribution, except for points that are determined to be "outliers".
**Syntax:**
```python
sns.boxplot(x='header_1', y='header_2', data=df)
```
**Example Output:**


![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d207ae92-0a7c-4e2f-aa65-0ee5a2c33bf7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VC6L45UR%2F20250223%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250223T004152Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIArWqYC3XO2lOkyuAkQctoNRLzdperE4dMNfrs6teHUfAiBc4%2BH6%2FVjcHO1V%2Bsq2pqW8rYGNPo81DmiFbtbGH%2Fi65iqIBAj4%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMZSxYji4B1YpRSer4KtwDmVkejN0M%2BgTK9BvV%2BMAuxyKXEDQnK8kiK8YwtJKCzKd6jJWOI2pnLDkfZ69iwwBOOTEElXpRJk2F8CDgSlcfRAnbADwXAAuahm2hFuPnsybV%2Fi8PPxkFONUruIYZJKfh3jWl%2FdGWPaIDkJswYTUDX%2B%2F9EL%2BRxOCZUX2VwTsj1R7V2FwGbHnjis1JfOgqOWh7tiYUgF0pb8jch7Qk5md4kCalg9J1tk4%2F8GDmpkVnHLDwEV7ysjyCHMx9sdPAUnuUzWBjzve2gZAuxnCt73wAFRsjxAwXe78QjrXYMm24ORDHVmHbOmW126bNyIflBVdKUKMQele617gq%2F0Hc%2Fk%2F8YwmeDiAxwHZITYfwvVlkTfVzgHLI538OQ2T%2FfWcp5sBKaZN1HXWsJKrGD3MJFmCN2ZNRsWL96UjVW0fxNYVe8ww0pJ4h%2FQa%2BpPDpmhg%2FOI6%2BJs6sSbuXutm2su6sHQIW%2BLTvXM3xAUQFq5R0oeh5DChYq3L3a97ZBgXctOUIMEJJFn9qNv313AIFp%2Bkfwh8%2FOiTM2wO0QRvov9Eh8dY%2BbWdaTY4gO%2BZ3sH98sgmszT4qNrhiTild9Pnv%2BBaphUO2yvPakKVKmcbboiTEtAe4MwWn4AREF9G2sMzSQ2ow0rLpvQY6pgESBP4sZvugvn6AkGfLNlK%2B1ZG354y1oow%2B76z2hQ3uxXTTtse4lUyL%2BasyCEel7K66aUbFrGTQEr%2FpdysI%2BuQCi5KH3mpr1wmKX9MietJw%2FYBDvwHAtyMmHk0nxD5OfldIQOkFJtBUmTb%2FS5J2ucRt64ioqbhToOER2sfJDUnPOjaDLEcesje7hkbpflo%2BRbEwTf6JOjk9py0V0HF97Az8P%2Bp5Lrfa&X-Amz-Signature=8311b27d5e1046e4dd45ca216670379ccf228e0f971f829503a770ce9fdb7144&X-Amz-SignedHeaders=host&x-id=GetObject)

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0e516edc-7551-4792-ab18-0494db3c4c0c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466U73A6UAM%2F20250223%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250223T004152Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCBzhDKpnWqrjoOjwnBJixECN2vMpu0dGP4B5koU8LfTQIgCBJmYq%2FvkiiOcVvpz%2FHLtLIE9yMUk%2F6QTRXzuGtz8DgqiAQI%2BP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNijQE8BwZJmRjhxWircA2%2FbMcDN6jU700JpLsv48BHy0DgqZazPCyFy6b%2Fa5JlPFHuWxCPPuGD6fkZnkoFxaULJkhKW1Uct%2Bgmi2i6dLqqajR3bNWOfunGrbJCXgTvr4zMDZHGxw3Yug5HAsGiXX4SJmCvEzGYzqwr%2B%2BarpPZdXNdIHyvfXh8t7MY9ln9%2BhY%2BltNeg5hSXC9uQpdWduu%2BLZl%2B3%2BmdAQxza2oJNUR5Q7sLVn7yckxAGB%2FWTlDu5L03Wf6RZPG92p%2BEioD8ejxvW99D83yGDZArQGBsJVaBj%2FIRc0yTull7L8K%2FrlXiij53429h0%2FYyRZdxgvF6dfF%2B2cJaSficfystz6Bjpcgzb41Fszg2WqLoIofabMe64xwBBw5toq61iS9k3NiSzi2Pd9HvE4RuyPnVc2ODPLPn4XaaECc%2F2QmJVCNpsiwXEUGXdHk7xqOgud%2FPt0Xe7T5oLEbiLmvlx38b6m4SL7wFuDuDscyaA9llupBMsVGF6rgXgZItdjB4XTuS5nfrVrbwkWpQgKzq8VKHIGckxJgrQuBbAM42%2FO4CKIRK0GO7Cnp90paVaX%2F310wyDxD1Rj42TWOd%2FqfkrSeiCiPNA4KZUAcpm0EF3If5Z7lfYY4vdRKW%2BYT01hDFzIMCHfMMGq6b0GOqUBcxWpkbGlTYdDl1RLOzzPtnDVvNfckIWsgjVnavnC%2BwX73vqqyMrFpOgpBxLeNxJYT3ML%2B6xZVbBUrdLYcB0BF00dJAlzWLYFaE575xS1SF%2BLsJXTljoDa0jpADgMsNV1H7RgqKoJkUqTZ%2BzGrOoTBs5G8B5bn60tlmc7FwktsHsOkZnwEbnjYbvUUXBegiYSYndUo5nTcRviJf7HGNZUPeDCzSab&X-Amz-Signature=ee8d2b0c607bf3b87d518c8dfaa8d4492d00f49402b99e17c448ba0a1e7a4b6f&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23a79b9d-2356-49a9-8fd9-65c6b0ab2cc5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XNK2HY6D%2F20250223%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250223T004151Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCHqmVWvDCLLv1%2BQfU4JJXncIHrFfoHiUPVop3dkfkRBAIgHtMyh8Hc4Hcs2Z%2Bbhq0aBsn3SOJbeahiIxRAKKcjCLYqiAQI%2BP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDE2G0fBq4OBZ7cDFHSrcA8swNFQP3xT6Spiz0gvGGmU0RR6mQglCFYuMG21TmWZzQczNMDq2RbroDioFEO24M3CGYRm%2FhwO%2BoEVKFPOphFSSJp%2BARB0r%2BTrYwYJMWrBBr02k%2Fa0RvuQbrLEhQchE25kZb7k2Ptjh1ROFRGy8R7aFEmf9JnCf6EK7VQ1RKfDQlW5XoxQpI0lJyHphS1elaeKSc4CHEoupEpHeYDwpLF%2B54k2B85dDFM%2B86ADBUj16SeSqQ%2BsnshC7sQpl4ysZNGNUiKl0cjXdzlK9q6sN1Vc8pLZdphfdi0mSZgUcAIknK2CJp5y4b87Bpa1B9pS%2BZjsSYfKq88PPmvexVojdhI3d540OVB31TUu75MgsjWQCQLylGX%2FxF74dvL5nsuB2cTiNl%2BJS8aVF3mUWAn17%2BRCEbtSSUtA1zxs8379lyEq3hrhEum6qDxjKVNUJYtQGpOxTOgnjxv4XoynjGZvIRTC8Lbphy%2BgfpPe03g7XvZCyygB3xc8UgFIGjA5tKIHzT7KoNZvykyzfnnELl5hNGAGvad0qnohtakDzFu4fbTJORdcWjYX1X28DKlI78%2BoRpZjaGnO9t8PT%2FT%2BirfD4M2XfnydyIfHJxvPjKJMZCaUpUrQHkmXzo9G%2FKXAdMKKy6b0GOqUBl6copEjQsb8%2Bq825fFFiaLQdhNh0GEg97TZXVjPN78Lg9zHmqkQDLz1YzNslDtLsk1l7LKs1hJN7Ith2PcdNCErDCgi4oaDAIz05HG43u7UPe4EV0z1p09eVIB9K3ivZBf%2FWs5hpH%2B%2Fkbqm1ibyYifkAv9WRwl72Gi%2B47y%2FIy9FhMbdCu8KsllcERFc%2Fv4pZqAfhbGRu3Y4T9oUs09vRZweWG8qr&X-Amz-Signature=a9adbd570136f185ba5ce4958e1c74b2e24c66d580b62d322648e72e2a289844&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 4. KDE Plot
A Kernel Density Estimate (KDE) plot is a graph that creates a probability distribution curve for the data based upon its likelihood of occurrence on a specific value. This is created for a single vector of information.
**Syntax:**
```python
sns.kdeplot(X) || sns.kdeplot(df['age'])
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0d571213-2a2f-4921-a50b-880847aa05ee/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XNK2HY6D%2F20250223%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250223T004151Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCHqmVWvDCLLv1%2BQfU4JJXncIHrFfoHiUPVop3dkfkRBAIgHtMyh8Hc4Hcs2Z%2Bbhq0aBsn3SOJbeahiIxRAKKcjCLYqiAQI%2BP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDE2G0fBq4OBZ7cDFHSrcA8swNFQP3xT6Spiz0gvGGmU0RR6mQglCFYuMG21TmWZzQczNMDq2RbroDioFEO24M3CGYRm%2FhwO%2BoEVKFPOphFSSJp%2BARB0r%2BTrYwYJMWrBBr02k%2Fa0RvuQbrLEhQchE25kZb7k2Ptjh1ROFRGy8R7aFEmf9JnCf6EK7VQ1RKfDQlW5XoxQpI0lJyHphS1elaeKSc4CHEoupEpHeYDwpLF%2B54k2B85dDFM%2B86ADBUj16SeSqQ%2BsnshC7sQpl4ysZNGNUiKl0cjXdzlK9q6sN1Vc8pLZdphfdi0mSZgUcAIknK2CJp5y4b87Bpa1B9pS%2BZjsSYfKq88PPmvexVojdhI3d540OVB31TUu75MgsjWQCQLylGX%2FxF74dvL5nsuB2cTiNl%2BJS8aVF3mUWAn17%2BRCEbtSSUtA1zxs8379lyEq3hrhEum6qDxjKVNUJYtQGpOxTOgnjxv4XoynjGZvIRTC8Lbphy%2BgfpPe03g7XvZCyygB3xc8UgFIGjA5tKIHzT7KoNZvykyzfnnELl5hNGAGvad0qnohtakDzFu4fbTJORdcWjYX1X28DKlI78%2BoRpZjaGnO9t8PT%2FT%2BirfD4M2XfnydyIfHJxvPjKJMZCaUpUrQHkmXzo9G%2FKXAdMKKy6b0GOqUBl6copEjQsb8%2Bq825fFFiaLQdhNh0GEg97TZXVjPN78Lg9zHmqkQDLz1YzNslDtLsk1l7LKs1hJN7Ith2PcdNCErDCgi4oaDAIz05HG43u7UPe4EV0z1p09eVIB9K3ivZBf%2FWs5hpH%2B%2Fkbqm1ibyYifkAv9WRwl72Gi%2B47y%2FIy9FhMbdCu8KsllcERFc%2Fv4pZqAfhbGRu3Y4T9oUs09vRZweWG8qr&X-Amz-Signature=b4baa8c008fb20cfebfd3ba660c5f8d0f6843ec6bcdec00b0f92ffc39807c7e1&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/53752550-ef82-4ca9-a01a-09921f0282d0/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XNK2HY6D%2F20250223%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250223T004151Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCHqmVWvDCLLv1%2BQfU4JJXncIHrFfoHiUPVop3dkfkRBAIgHtMyh8Hc4Hcs2Z%2Bbhq0aBsn3SOJbeahiIxRAKKcjCLYqiAQI%2BP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDE2G0fBq4OBZ7cDFHSrcA8swNFQP3xT6Spiz0gvGGmU0RR6mQglCFYuMG21TmWZzQczNMDq2RbroDioFEO24M3CGYRm%2FhwO%2BoEVKFPOphFSSJp%2BARB0r%2BTrYwYJMWrBBr02k%2Fa0RvuQbrLEhQchE25kZb7k2Ptjh1ROFRGy8R7aFEmf9JnCf6EK7VQ1RKfDQlW5XoxQpI0lJyHphS1elaeKSc4CHEoupEpHeYDwpLF%2B54k2B85dDFM%2B86ADBUj16SeSqQ%2BsnshC7sQpl4ysZNGNUiKl0cjXdzlK9q6sN1Vc8pLZdphfdi0mSZgUcAIknK2CJp5y4b87Bpa1B9pS%2BZjsSYfKq88PPmvexVojdhI3d540OVB31TUu75MgsjWQCQLylGX%2FxF74dvL5nsuB2cTiNl%2BJS8aVF3mUWAn17%2BRCEbtSSUtA1zxs8379lyEq3hrhEum6qDxjKVNUJYtQGpOxTOgnjxv4XoynjGZvIRTC8Lbphy%2BgfpPe03g7XvZCyygB3xc8UgFIGjA5tKIHzT7KoNZvykyzfnnELl5hNGAGvad0qnohtakDzFu4fbTJORdcWjYX1X28DKlI78%2BoRpZjaGnO9t8PT%2FT%2BirfD4M2XfnydyIfHJxvPjKJMZCaUpUrQHkmXzo9G%2FKXAdMKKy6b0GOqUBl6copEjQsb8%2Bq825fFFiaLQdhNh0GEg97TZXVjPN78Lg9zHmqkQDLz1YzNslDtLsk1l7LKs1hJN7Ith2PcdNCErDCgi4oaDAIz05HG43u7UPe4EV0z1p09eVIB9K3ivZBf%2FWs5hpH%2B%2Fkbqm1ibyYifkAv9WRwl72Gi%2B47y%2FIy9FhMbdCu8KsllcERFc%2Fv4pZqAfhbGRu3Y4T9oUs09vRZweWG8qr&X-Amz-Signature=0811dc85aeca8e89467f5131deafa19bb33b8c689f849fad23f8b4f46dddf261&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
## 4. Correlation Between Variables
Correlation is a statistical measure of the extent to which different variables are interdependent. It indicates how changes in one variable are associated with changes in another variable over time.
### Positive Correlation
Positive correlation indicates that as one variable increases, the other variable also tends to increase.
**Example: Engine Size and Price**
- **Positive Correlation:** Engine size increases, price also increases.
- **Visualization:** Scatter plot with a steep positive slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c7ea9b0-3ef3-4357-a9c3-554fc71b6b15/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YTEG7UUF%2F20250223%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250223T004152Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIBmRl7FMpqNEUBKYrXam8fcQldGhaoMdxK%2BLwNs6VCHSAiEAuQ4O69yAVcNU5bF5FMxd62fqzXUPrHTG3zRUqYK0VlAqiAQI%2BP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOxnu0v9yL0OXNwhjyrcAxFlwxZnpFhLQ3uisHYaaw5HN%2BJLwc4Pq4ylyMtDSOtdGnHFD1ybgW844garZp65h1kBbkm%2BIx71RN3kLqiMnaYHZw7PXFbIc4ZnFbIvJYFwImqnYV5%2FzsHul7RMMeaeIE5aOWP4mqqQQNyXPyGAz%2BOd54dg4UYQfm0DNkyHfE5BrTYStNRa8sUpwcg91Csppr4tSxSoe8x0WXAatdrTjPy%2BBrg6NkcHzfRxiIQnMP6bCh2lUEvpx3gCQ6nJvg3SYwoVvRan3az6a29FGIgTS3qjAesdsYRPtm3lD%2BVC5Hb0Pxmv1c%2FiR2WiYMiB4sojVipT%2B%2Bx%2BADgTX9AwlE2lUYtSapwpsyHFRunpotpianzNLtvBTq2LmD0jrmG64TChdndIxYBvzj%2BBn6iMJikSej6dU4L%2BwnZK9Lm4CW7leGLE8x48wyXNJgRV4BpWVrw4Zus7PdLx8f4W%2Ba0lxYwln4BOObZ6urQfA90WsxNZWqsD5zkC6rBh%2BAxlMuY%2BEpIPjNRSFTKc65ICc8g8rXES6iYZQGoI%2BYv5KwvZ18hdLfyAAr9YNUJT77ZtF86uAJOuAWnY%2FwPhFdseQlF3HOw07r7XMdOzzseveMyuVYgZXGlQZqqftuDkpBMWpkN0MIqg6b0GOqUBZXEK%2FAdQT9z4puJtAf1paIrCTBaK8ScIYY0PEXtYQb1zDdlkGfcQKK3Q5n3JtATIG1ZBtNm7SWLlB5aHLXCXUiAvBsBT1%2B%2FkywP%2FyUTkASLkVnYcp0TW%2BxcFOR6arJNQN%2FIKtxyWb4nODPVVxF%2Fz0GzGF6o2uoN8gh2Llpei9Nlex%2B20QLQ2CBBD3RuWYln8F7XpwrbWWMmGlXCwUKECsVxuActv&X-Amz-Signature=52b8d9a75285158a8d84dc2d9bed23be59cca623ab8715ecd1c3486cc35089d8&X-Amz-SignedHeaders=host&x-id=GetObject)
**Explanation:** When engine size increases, there is a corresponding increase in the price of the vehicle. This positive correlation suggests that larger engines tend to be associated with higher prices in the market.
___
### Negative Correlation
Negative correlation indicates that as one variable increases, the other variable tends to decrease.
**Example: Highway Miles per Gallon and Price**
- **Negative Correlation:** As highway miles per gallon increases, price decreases.
- **Visualization:** Scatter plot with a steep negative slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/10f1f798-9cc4-4df2-a9c1-5a339f554a0b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466W7PGA7C7%2F20250223%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250223T004152Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEND%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFRvRKVzlQx1vkDMrudMEYz%2Bwwk4xyafFAQhf%2F%2F7UY2aAiAkicc0Ppe2PIPvibh1zWawoiXo02CWlS%2FTuRa3yMUFxiqIBAj5%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMfG2DtYRrBQCozDTWKtwDQyPaGjiqD%2F0AnygsayBHi7SWkTpkSd1laEjldzD4Q3f8Gqb7jOHkLZLGxpP2QrynzScr9D%2BWOcLbn6%2FyPrIFWEHE9%2Bi3%2Brl%2F5NdmnwV%2Fz8GrTfo2T2JNRTf2X9wHZl%2B4UOMWyw4Uxi7xG%2BtoDo%2BoO4NTRAmJ95tmMx45txSLCTw7Tdqo0pklykzkm046EDgbWK9B86z2L%2FV7ufSYfaDc97Tp2qdLyor3zKMlouMOLOGoTG6OZMlYmdazwUf9lKnQHGq6aBbYTtJFQWkK3eFFnJbV692aQyMsockiqHydXwkfkcs1RPQ419R848zhSiqLSM6dcVKJM0XC0zVDqfE%2BZJP7xrmqH3waWA84ZI%2B3roT4nLla25HR0C%2Bn74%2B3D0LIkh%2F29LHHB%2Bxz6vsXiqQwCoMdZ0Nh8rabTQ0hnE3lWmR%2B0HVu7Ref4tSum8p9jJFVnUfS5l03QT4VlnpbqWiARJiu1tQZBEIA74Kc%2F%2BFf%2Bazk7AUheA%2FCejNCqjfRMZGjcTiYLySgM4U2PVKXRQsBlKmkGHoRSjIbtq2%2FZoFVptyARKOjg1OnDDmk2ARrsgzEt6EX11AAiTbDfFTzEEXywAiyhxhk8BZAmdjeyh4MzmeZbDDY7489jxKBuMAwysrpvQY6pgFwSB2%2FDNo7dpYlOagjtUiGzdU1hfGhzFt2oV54vqs5I2Rbw%2BpyyyidzRPlWQxb9h%2BOwCIfisfMFe5zt4IBiNIsO%2FpIesL%2FL3P1w%2FSLxj%2BRkHqQ0SEw2uVygWzIvzUR3lyBrTC%2BrEbNIWnpn%2Behtsg6css%2FRKKdfhkhxkbooJgRkY7IQUcaDEbmu9Lvt5v%2FeIAR4WjLOqW4vBBAiEUZR3zmxB5x2rPH&X-Amz-Signature=0effa6ea8ba26fe37e797cb5387467cc48c7ac06c54c247db50d493c560dabeb&X-Amz-SignedHeaders=host&x-id=GetObject)
**Explanation:** When highway miles per gallon increases, the price of the vehicle tends to decrease. This negative correlation suggests that cars with higher fuel efficiency (more miles per gallon) are generally priced lower in the market.
___
### Weak Correlation
Weak correlation indicates a lack of strong relationship between the variables.
**Example: RPM and Price**
- **Weak Correlation:** Low and high RPM values show varied prices, indicating no strong predictive relationship.
- **Visualization:** Scatter plot with no clear trend or slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9f914514-8914-4bf4-ac84-d9e3077f6eb1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WTKYOP6G%2F20250223%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250223T004152Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHcDrMJbvA2oMyc1X1ZaE1LYdpXpVJ8Q6ccwkO167QOOAiEApxwrqJVd%2BSWxaE4zSebjP59cbVL7VAr5DJh734NR%2BLQqiAQI%2BP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDE9jVW6JBlhWPCY%2BSCrcA3OinYkdjmtkTv5LhH93ThDRKr%2Bnuf%2BCYz5eOSPQ4A6sPoHpdgzYFuK%2BFTYdcI%2BZGGFfIUfQtjaGqMG0SNdbXe%2FeDJxPcYNij8wVWiIogc285921CO7h3EWQnS2lBC0nq%2BUAMj7ek2gD9H9Rf0rzL9jT0HEpsJ%2FI9qz69Mzek2lCXtcKUaNrLGwA%2FEPKyGPsMmwXRxcOsYbxcl5CsdeBnTGST4i6k6qpVu28W0Di%2FBf4vd%2BW%2FNPEXLKd9Pc%2FJk%2B3gCt4oYsD4AIZAs9eVD5dKci%2FIk9CzxmatKvns%2BXCd3Irn0KMPppFwAncbf6VmNSVwW9MaobkxeLTbCqAROz1r77YW%2FhRjDhyL7nsGBHAw%2BSTTVhgxY%2FebqioP1VJVNfer%2Fpws3ZOK8D18kcidr2%2BhmM1EXaKcQC3R5LKqXe93%2B%2F93WH9WOZ7yZpL63xL2ejSdnGEQvDfvDBrfJfJyflI%2FGo5DBlZToUZXV4eN9kOjkTgyM3MY8MzlxHhvB0HotlhiqJxPJqXyXhMVRSh7cnDAYJAj6t5SZev4NhG2KQs8plQ0oc2RuGlOJ7MnRJuh2JOM87%2BTaeoSa2g7b8Q2mr1uKX2ZV2a%2FASlHI9nFnas5BWy3wRS937MLPOPgU6KMPGh6b0GOqUBbwVuGNYme%2FkeOEFqhjkbbKbNeEWkQPKs%2Fv4jeoXCZVnpvbQR7%2FlcqtDCJt97k56AeWg50hk3dpqhe2kAp%2FC%2FMRckaICCZTtlQXL%2FfcWCv3wjc6igsg7mjVasFoluTNozpzNfZTBc6gB8uDiarHp%2FGJMXZVSck8AYj%2BFc8Fa0tK8y5GJLuvPTWdP9ABy2UYlvoQzCCEVykbsNX4%2F3GHeukr3Rt42z&X-Amz-Signature=bcfccd828ab1a9661e16afaaf678cc20bf6de6b5a511a1ec9d3dd720f057066c&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f18086e5-5b04-4fbf-8309-8944ab20d213/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UAGGGX4P%2F20250223%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250223T004152Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCPxvcybKlov9kF0u%2F3xvA2cyCgeyQHIYnOvspg28%2Fm9AIhAPL0SfnP6tIMWBxd1m2Xo3IKJZZNxKM0AyEXMBysTiK%2FKogECPj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igy5pJSg7yvSt3gDwScq3AMFbognBQSlp%2FxT9lR6jokB3J4kFvuDfT0bJEdJyXrV7NtPAEVK4%2BD%2BaxFBdXjesqEBs2E4CY%2BCFPqBNFdF%2FWo5snZpP%2FEkY%2BhqfsPrENFVGMp6IqULpAbDHZ8gRz5xbhYFeBpyOPj2m4N8DHByvc%2BITkqhyWQ4wwSw3WPDQbS7A%2FFtWjRmHM%2BNZ%2BQ5Ta2h5sUPrvocEBqeqGXtlQ9VG%2F1xPsarKMF21fy0cFxF16FyKUHaFAuyiB7UBlfOeS0%2BYvehDDTYwrmbxfXj4Wg7poQPYqd7eIDP8SUuHWnZ9%2BCw26uc0gdIbJwep4x0HwXEQ8PKJsvD%2F3zf2%2BMgHrOBLUMdaX%2BqYzBh82nZlxfJsEF%2FfRVXAD%2FhbhtY1X%2B8R9HfXou7aren0F8LkrFVZ%2BI5r%2F7DNVSxOvDAEIgX9hUiJMc53d3knWK6Ij9VNWsgLp8PZHnXqIWh1UqcWP1NAjF%2B7izLNhikwWDANm9zZeoL0Hp3bQeWJMV%2ByOLAMbLooatbBPQtySo5jNlfyAMk9KtpL2A3U9BNUFFX6lTEh9%2BOItRBxKldIAZ7jEz39U53KILKpCDLVNZOdmbtJDdC8%2FnlMB6KzbiDg%2FC1M0RkZ%2B%2FZgAfsihJZHrYzbJpdHhpJbjDiqOm9BjqkAReLhZ8bU0%2ByqF36AL3ed7WI7WMpfRJlcTvAdZwI9WZYzXyKx0Pkw%2B1ZHRWv2WHT%2BB%2FgdEGa%2FGcydpUmV5%2FSMzjmnBoBnU494xEhcOVvi%2BNHBX7OQ2BUVe0%2Bt04wiphGV4R2ZOUhyHppHsEsRk3FfVbo2SrN1nzsTaaSMUq2Dznrimg82UH4Od8UZ%2Fm%2BGBRrMhWLrFu%2FyTEJcnsOZJdYCFlxejA9&X-Amz-Signature=a65e203cbbb5c19ec89046a4b8809b77ca43ffe35a7e436da6b8161c37a98137&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Correlation Plot
Heatmap visualizes correlations among variables. Color scheme indicates Pearson correlation coefficients. Dark red diagonal line shows perfect correlation (value of 1) between variables and themselves.
This heatmap offers overview of variable relationships and their link with price.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cd3b341e-cc1a-45f7-8aec-cdc00436d270/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UAGGGX4P%2F20250223%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250223T004152Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCPxvcybKlov9kF0u%2F3xvA2cyCgeyQHIYnOvspg28%2Fm9AIhAPL0SfnP6tIMWBxd1m2Xo3IKJZZNxKM0AyEXMBysTiK%2FKogECPj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igy5pJSg7yvSt3gDwScq3AMFbognBQSlp%2FxT9lR6jokB3J4kFvuDfT0bJEdJyXrV7NtPAEVK4%2BD%2BaxFBdXjesqEBs2E4CY%2BCFPqBNFdF%2FWo5snZpP%2FEkY%2BhqfsPrENFVGMp6IqULpAbDHZ8gRz5xbhYFeBpyOPj2m4N8DHByvc%2BITkqhyWQ4wwSw3WPDQbS7A%2FFtWjRmHM%2BNZ%2BQ5Ta2h5sUPrvocEBqeqGXtlQ9VG%2F1xPsarKMF21fy0cFxF16FyKUHaFAuyiB7UBlfOeS0%2BYvehDDTYwrmbxfXj4Wg7poQPYqd7eIDP8SUuHWnZ9%2BCw26uc0gdIbJwep4x0HwXEQ8PKJsvD%2F3zf2%2BMgHrOBLUMdaX%2BqYzBh82nZlxfJsEF%2FfRVXAD%2FhbhtY1X%2B8R9HfXou7aren0F8LkrFVZ%2BI5r%2F7DNVSxOvDAEIgX9hUiJMc53d3knWK6Ij9VNWsgLp8PZHnXqIWh1UqcWP1NAjF%2B7izLNhikwWDANm9zZeoL0Hp3bQeWJMV%2ByOLAMbLooatbBPQtySo5jNlfyAMk9KtpL2A3U9BNUFFX6lTEh9%2BOItRBxKldIAZ7jEz39U53KILKpCDLVNZOdmbtJDdC8%2FnlMB6KzbiDg%2FC1M0RkZ%2B%2FZgAfsihJZHrYzbJpdHhpJbjDiqOm9BjqkAReLhZ8bU0%2ByqF36AL3ed7WI7WMpfRJlcTvAdZwI9WZYzXyKx0Pkw%2B1ZHRWv2WHT%2BB%2FgdEGa%2FGcydpUmV5%2FSMzjmnBoBnU494xEhcOVvi%2BNHBX7OQ2BUVe0%2Bt04wiphGV4R2ZOUhyHppHsEsRk3FfVbo2SrN1nzsTaaSMUq2Dznrimg82UH4Od8UZ%2Fm%2BGBRrMhWLrFu%2FyTEJcnsOZJdYCFlxejA9&X-Amz-Signature=f30ab57db0c30e84b2cd53bcced55858603a443e287cf485d3b886a5290fc678&X-Amz-SignedHeaders=host&x-id=GetObject)

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
