

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7e6d594d-952e-44b6-97ea-31225882aea6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WCLJ7RYD%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T041620Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHZwnlC2veYYOcNFraEm8MzSLjParBtOdM8YBj2YuhYgAiBQdEO0qNtlu2Pd%2FeRx%2BRBs4p12Ah0gHWVbtI5TJty4JCqIBAjl%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMsOtqwAjKyCAHKvhVKtwDtvBSiypfXSzJTwiZFCD%2F5n2O5VphIwLhdeb%2F5S%2BfNX8uyokO2ivA1zfY5T69kJcsC2PdwJ%2BtmEXyObR5teEorimlThDutAuVbrFY97GudmwxnQw%2B28RGtCvYhqgjIOk3XX%2FM%2BCcsB%2FY2PbqqVZNWN8WxaMZc5PoTAmzIW556IrTSRK90IlncLte3QA8meWX64XDz8VkndqE0ejyYJ%2FlD8TVG1rqOFpg%2F4y58jepRafyf9JaCkcqy7agjk1w%2B0JfiRz1xgUe%2BIWE2vxcdEw6pVYxl9PDG4GpSOp%2BwV55zGIXE3JNJPr3J5Ky6LTtaNJGGZiHfMmqPk%2Fhcoe6YsEDsskmLEh10TzlnGvUOhWYKOIefGCs769EyeGBUxgtVOa6U5QjvloZmFJA%2F8M0ZLS0Yaubo8lO%2F0YdG%2B9SEOe%2BIyh3DJO3%2FwU50HpKdUeR5dS28E1i5cFnp3mJMLJX38orWGoUwV3u%2FIa99vZWhwmwktiGH4bRWQ4E4gh64luSDVzXK1NplE66fbe%2BVYUI0nIDuSTNLzyrywm%2FiHnHeklKi%2FQu%2FlXM6VMbXlVJ3T9f2Npj6FqhzwlnJSCU%2BQEG3LTN3FfHTZMHueHzRWbVsbWxQd3JBJ3cONi3yKX1AxZ4wmOH7vAY6pgHQELB%2Bx1368RkKpgiwCrxIR65TXUfqTsUxOLYmCdFEC5%2F4JxNiZaETY4D3U3IQbAeCjl1Syg1iWn6TtGo6LvTVx%2B%2F3ZmC2Xc6i6cLAV5r9OnuWn%2BEJpJfGqYbhQFX%2Fn3gvKDVPtDRInkH80eBEFJzXB%2FobrEd4Ec2pQe2czAOkoTQMSLZjc4D5No59T0POMgbApKk6Ys1LAqNjHBvmZup1enUudTA4&X-Amz-Signature=e6920b38e11b127a47077b08815e447998fb1aafa1d757e1796079433a950945&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cbfaed9e-b398-4902-8936-dea058b21def/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WCLJ7RYD%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T041620Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHZwnlC2veYYOcNFraEm8MzSLjParBtOdM8YBj2YuhYgAiBQdEO0qNtlu2Pd%2FeRx%2BRBs4p12Ah0gHWVbtI5TJty4JCqIBAjl%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMsOtqwAjKyCAHKvhVKtwDtvBSiypfXSzJTwiZFCD%2F5n2O5VphIwLhdeb%2F5S%2BfNX8uyokO2ivA1zfY5T69kJcsC2PdwJ%2BtmEXyObR5teEorimlThDutAuVbrFY97GudmwxnQw%2B28RGtCvYhqgjIOk3XX%2FM%2BCcsB%2FY2PbqqVZNWN8WxaMZc5PoTAmzIW556IrTSRK90IlncLte3QA8meWX64XDz8VkndqE0ejyYJ%2FlD8TVG1rqOFpg%2F4y58jepRafyf9JaCkcqy7agjk1w%2B0JfiRz1xgUe%2BIWE2vxcdEw6pVYxl9PDG4GpSOp%2BwV55zGIXE3JNJPr3J5Ky6LTtaNJGGZiHfMmqPk%2Fhcoe6YsEDsskmLEh10TzlnGvUOhWYKOIefGCs769EyeGBUxgtVOa6U5QjvloZmFJA%2F8M0ZLS0Yaubo8lO%2F0YdG%2B9SEOe%2BIyh3DJO3%2FwU50HpKdUeR5dS28E1i5cFnp3mJMLJX38orWGoUwV3u%2FIa99vZWhwmwktiGH4bRWQ4E4gh64luSDVzXK1NplE66fbe%2BVYUI0nIDuSTNLzyrywm%2FiHnHeklKi%2FQu%2FlXM6VMbXlVJ3T9f2Npj6FqhzwlnJSCU%2BQEG3LTN3FfHTZMHueHzRWbVsbWxQd3JBJ3cONi3yKX1AxZ4wmOH7vAY6pgHQELB%2Bx1368RkKpgiwCrxIR65TXUfqTsUxOLYmCdFEC5%2F4JxNiZaETY4D3U3IQbAeCjl1Syg1iWn6TtGo6LvTVx%2B%2F3ZmC2Xc6i6cLAV5r9OnuWn%2BEJpJfGqYbhQFX%2Fn3gvKDVPtDRInkH80eBEFJzXB%2FobrEd4Ec2pQe2czAOkoTQMSLZjc4D5No59T0POMgbApKk6Ys1LAqNjHBvmZup1enUudTA4&X-Amz-Signature=ab2c1cb3deb9b1ed25abcc38c646339d8f59d8a986cf83e6bd8190bcfa24ba32&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/91181646-b1e0-4433-9711-6259a96a9247/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WCLJ7RYD%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T041620Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHZwnlC2veYYOcNFraEm8MzSLjParBtOdM8YBj2YuhYgAiBQdEO0qNtlu2Pd%2FeRx%2BRBs4p12Ah0gHWVbtI5TJty4JCqIBAjl%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMsOtqwAjKyCAHKvhVKtwDtvBSiypfXSzJTwiZFCD%2F5n2O5VphIwLhdeb%2F5S%2BfNX8uyokO2ivA1zfY5T69kJcsC2PdwJ%2BtmEXyObR5teEorimlThDutAuVbrFY97GudmwxnQw%2B28RGtCvYhqgjIOk3XX%2FM%2BCcsB%2FY2PbqqVZNWN8WxaMZc5PoTAmzIW556IrTSRK90IlncLte3QA8meWX64XDz8VkndqE0ejyYJ%2FlD8TVG1rqOFpg%2F4y58jepRafyf9JaCkcqy7agjk1w%2B0JfiRz1xgUe%2BIWE2vxcdEw6pVYxl9PDG4GpSOp%2BwV55zGIXE3JNJPr3J5Ky6LTtaNJGGZiHfMmqPk%2Fhcoe6YsEDsskmLEh10TzlnGvUOhWYKOIefGCs769EyeGBUxgtVOa6U5QjvloZmFJA%2F8M0ZLS0Yaubo8lO%2F0YdG%2B9SEOe%2BIyh3DJO3%2FwU50HpKdUeR5dS28E1i5cFnp3mJMLJX38orWGoUwV3u%2FIa99vZWhwmwktiGH4bRWQ4E4gh64luSDVzXK1NplE66fbe%2BVYUI0nIDuSTNLzyrywm%2FiHnHeklKi%2FQu%2FlXM6VMbXlVJ3T9f2Npj6FqhzwlnJSCU%2BQEG3LTN3FfHTZMHueHzRWbVsbWxQd3JBJ3cONi3yKX1AxZ4wmOH7vAY6pgHQELB%2Bx1368RkKpgiwCrxIR65TXUfqTsUxOLYmCdFEC5%2F4JxNiZaETY4D3U3IQbAeCjl1Syg1iWn6TtGo6LvTVx%2B%2F3ZmC2Xc6i6cLAV5r9OnuWn%2BEJpJfGqYbhQFX%2Fn3gvKDVPtDRInkH80eBEFJzXB%2FobrEd4Ec2pQe2czAOkoTQMSLZjc4D5No59T0POMgbApKk6Ys1LAqNjHBvmZup1enUudTA4&X-Amz-Signature=16af1d307cd587548280afc3bacb2dbcf835e2c418d2873da5e1cabc12af6745&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/09aba1c0-0d55-41dd-852a-a04c5b8a3fac/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Q6Y5FFKW%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T041620Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCXyih%2F71Zvg50Lq9rQ4CW2C4Qfd8uoyNXOjBgXZ544nwIhAM1j4XhcK3QYm8KW8wR%2Bm96glley%2BTB%2B4AYkEdvrwklbKogECOX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyRQoA2EgRKQz6tIucq3AMfdndtd93mGs78Z7dNgJGLz7kxqwzfHIyl1P2ie%2FC53UtnyBL71UyWCZFtmVeWY6g7YfZN3R4RbBty9bDxYu6rTCfzBM1tZL%2Fn%2Bi7r%2Fb8ofSR4fsAKYpTdRO47Zh6FeF1ci0r%2FaFVkOmyURUFBRVxnt%2BCw9NgTCHYjK3sYrhawyBPmZz7cSFSgyVpA3eiTpAuDnJ2vSdVaX3gtZU9q9J5Onome0OrCNGVWK6nXzYDWrDCeMTaEx9g93zUW5e5xaHHXdH8%2BH0Bs2t3hTNx9GuSMUbv%2BcDniNz%2BIGWj7qCxqL5MN5MRamLpK%2BfuLXHFfts3WNhNRE86KBqTvoai39lKIGgNQEBJwe6mKcw7yMVXcCDFTrBB22gBt79KKi7PlSCqwl%2BWUHXMUElZs9ODpRir9wcTsN32i7N2Q7k25Su9eGR%2FfBSRr9TdTgdCjVHGJoc3qFRvBlTwBefuS3LpTuo651WfOIIbAMuHuTSELggs4Mp1Zl64QWybfIMivTDhh4IDWgNZKEtm0%2FmjnZkTdrXZuS5s5RDazVp7ui2bQ0yhwNooVsj173nmYV82iPEDQjsvFNxjfwhRjc7I7BgbBDMWzFYHWXwpiYjbiUJaSjorI4nDX%2FABzkgMx%2F6L6SjCf4fu8BjqkAbQC4FHnvzZIXxEdcp9y5Syu%2B8mmcp8%2BatRTld3pnPk4NHefsWWd3n47GB9CJmRfmP27rKiqlBBi3%2FPhgXyqjtcSCUGz1wQBlCYvm4hhJSBem8ghthk%2FMH01SX8oqc8iNPvS484qTuyn0Wb2DO3oU5YSPmOx396Tv13l2h9FV1H6I8cRT%2BcsG7rkjYZX7abKvaYivt5C1pGRCwFfHlHN4YzlH4VE&X-Amz-Signature=5f1f64ff4a2ab5245e1547a020124d9ba4b1183d01d49f2ed0bfe8e086888fdf&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 2. Scatter Plot
Scatter plots present the relationship between two variables in a dataset. It represents data points on a two-dimensional plane. The independent variable or attribute is plotted on the X-axis, while the dependent variable is plotted on the Y-axis.
**Syntax:**
```python
plt.scatter(x, y)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23708af9-659f-4f23-b626-1a4292d7842c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Q6Y5FFKW%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T041620Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCXyih%2F71Zvg50Lq9rQ4CW2C4Qfd8uoyNXOjBgXZ544nwIhAM1j4XhcK3QYm8KW8wR%2Bm96glley%2BTB%2B4AYkEdvrwklbKogECOX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyRQoA2EgRKQz6tIucq3AMfdndtd93mGs78Z7dNgJGLz7kxqwzfHIyl1P2ie%2FC53UtnyBL71UyWCZFtmVeWY6g7YfZN3R4RbBty9bDxYu6rTCfzBM1tZL%2Fn%2Bi7r%2Fb8ofSR4fsAKYpTdRO47Zh6FeF1ci0r%2FaFVkOmyURUFBRVxnt%2BCw9NgTCHYjK3sYrhawyBPmZz7cSFSgyVpA3eiTpAuDnJ2vSdVaX3gtZU9q9J5Onome0OrCNGVWK6nXzYDWrDCeMTaEx9g93zUW5e5xaHHXdH8%2BH0Bs2t3hTNx9GuSMUbv%2BcDniNz%2BIGWj7qCxqL5MN5MRamLpK%2BfuLXHFfts3WNhNRE86KBqTvoai39lKIGgNQEBJwe6mKcw7yMVXcCDFTrBB22gBt79KKi7PlSCqwl%2BWUHXMUElZs9ODpRir9wcTsN32i7N2Q7k25Su9eGR%2FfBSRr9TdTgdCjVHGJoc3qFRvBlTwBefuS3LpTuo651WfOIIbAMuHuTSELggs4Mp1Zl64QWybfIMivTDhh4IDWgNZKEtm0%2FmjnZkTdrXZuS5s5RDazVp7ui2bQ0yhwNooVsj173nmYV82iPEDQjsvFNxjfwhRjc7I7BgbBDMWzFYHWXwpiYjbiUJaSjorI4nDX%2FABzkgMx%2F6L6SjCf4fu8BjqkAbQC4FHnvzZIXxEdcp9y5Syu%2B8mmcp8%2BatRTld3pnPk4NHefsWWd3n47GB9CJmRfmP27rKiqlBBi3%2FPhgXyqjtcSCUGz1wQBlCYvm4hhJSBem8ghthk%2FMH01SX8oqc8iNPvS484qTuyn0Wb2DO3oU5YSPmOx396Tv13l2h9FV1H6I8cRT%2BcsG7rkjYZX7abKvaYivt5C1pGRCwFfHlHN4YzlH4VE&X-Amz-Signature=fcd955c526198657eafeb81745c160d0e688f28f02243e2cbf28d3ecb68089ad&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 3. Histogram
A histogram is an important visual representation of data in categorical form. To view the data in a "Binned" form, use the histogram plot with a number of bins required or with the data points that mark the bin edges. The x-axis represents the data bins, and the y-axis represents the number of elements in each bin.
**Syntax:**
```python
plt.hist(x, bins)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/24e4424a-df87-40a1-b63b-195cbdc2e0ab/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Q6Y5FFKW%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T041620Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCXyih%2F71Zvg50Lq9rQ4CW2C4Qfd8uoyNXOjBgXZ544nwIhAM1j4XhcK3QYm8KW8wR%2Bm96glley%2BTB%2B4AYkEdvrwklbKogECOX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyRQoA2EgRKQz6tIucq3AMfdndtd93mGs78Z7dNgJGLz7kxqwzfHIyl1P2ie%2FC53UtnyBL71UyWCZFtmVeWY6g7YfZN3R4RbBty9bDxYu6rTCfzBM1tZL%2Fn%2Bi7r%2Fb8ofSR4fsAKYpTdRO47Zh6FeF1ci0r%2FaFVkOmyURUFBRVxnt%2BCw9NgTCHYjK3sYrhawyBPmZz7cSFSgyVpA3eiTpAuDnJ2vSdVaX3gtZU9q9J5Onome0OrCNGVWK6nXzYDWrDCeMTaEx9g93zUW5e5xaHHXdH8%2BH0Bs2t3hTNx9GuSMUbv%2BcDniNz%2BIGWj7qCxqL5MN5MRamLpK%2BfuLXHFfts3WNhNRE86KBqTvoai39lKIGgNQEBJwe6mKcw7yMVXcCDFTrBB22gBt79KKi7PlSCqwl%2BWUHXMUElZs9ODpRir9wcTsN32i7N2Q7k25Su9eGR%2FfBSRr9TdTgdCjVHGJoc3qFRvBlTwBefuS3LpTuo651WfOIIbAMuHuTSELggs4Mp1Zl64QWybfIMivTDhh4IDWgNZKEtm0%2FmjnZkTdrXZuS5s5RDazVp7ui2bQ0yhwNooVsj173nmYV82iPEDQjsvFNxjfwhRjc7I7BgbBDMWzFYHWXwpiYjbiUJaSjorI4nDX%2FABzkgMx%2F6L6SjCf4fu8BjqkAbQC4FHnvzZIXxEdcp9y5Syu%2B8mmcp8%2BatRTld3pnPk4NHefsWWd3n47GB9CJmRfmP27rKiqlBBi3%2FPhgXyqjtcSCUGz1wQBlCYvm4hhJSBem8ghthk%2FMH01SX8oqc8iNPvS484qTuyn0Wb2DO3oU5YSPmOx396Tv13l2h9FV1H6I8cRT%2BcsG7rkjYZX7abKvaYivt5C1pGRCwFfHlHN4YzlH4VE&X-Amz-Signature=ee960e81bdf5cd30946a581e790acd78c376d2f7976f75df69f470e283ddbca1&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ab5a6dfe-51f5-43ee-bcb3-33dae4a1c7ad/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Q6Y5FFKW%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T041620Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCXyih%2F71Zvg50Lq9rQ4CW2C4Qfd8uoyNXOjBgXZ544nwIhAM1j4XhcK3QYm8KW8wR%2Bm96glley%2BTB%2B4AYkEdvrwklbKogECOX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyRQoA2EgRKQz6tIucq3AMfdndtd93mGs78Z7dNgJGLz7kxqwzfHIyl1P2ie%2FC53UtnyBL71UyWCZFtmVeWY6g7YfZN3R4RbBty9bDxYu6rTCfzBM1tZL%2Fn%2Bi7r%2Fb8ofSR4fsAKYpTdRO47Zh6FeF1ci0r%2FaFVkOmyURUFBRVxnt%2BCw9NgTCHYjK3sYrhawyBPmZz7cSFSgyVpA3eiTpAuDnJ2vSdVaX3gtZU9q9J5Onome0OrCNGVWK6nXzYDWrDCeMTaEx9g93zUW5e5xaHHXdH8%2BH0Bs2t3hTNx9GuSMUbv%2BcDniNz%2BIGWj7qCxqL5MN5MRamLpK%2BfuLXHFfts3WNhNRE86KBqTvoai39lKIGgNQEBJwe6mKcw7yMVXcCDFTrBB22gBt79KKi7PlSCqwl%2BWUHXMUElZs9ODpRir9wcTsN32i7N2Q7k25Su9eGR%2FfBSRr9TdTgdCjVHGJoc3qFRvBlTwBefuS3LpTuo651WfOIIbAMuHuTSELggs4Mp1Zl64QWybfIMivTDhh4IDWgNZKEtm0%2FmjnZkTdrXZuS5s5RDazVp7ui2bQ0yhwNooVsj173nmYV82iPEDQjsvFNxjfwhRjc7I7BgbBDMWzFYHWXwpiYjbiUJaSjorI4nDX%2FABzkgMx%2F6L6SjCf4fu8BjqkAbQC4FHnvzZIXxEdcp9y5Syu%2B8mmcp8%2BatRTld3pnPk4NHefsWWd3n47GB9CJmRfmP27rKiqlBBi3%2FPhgXyqjtcSCUGz1wQBlCYvm4hhJSBem8ghthk%2FMH01SX8oqc8iNPvS484qTuyn0Wb2DO3oU5YSPmOx396Tv13l2h9FV1H6I8cRT%2BcsG7rkjYZX7abKvaYivt5C1pGRCwFfHlHN4YzlH4VE&X-Amz-Signature=e5a40fabbc7d42576e55c984b23e6cf0878ddd6749cf146c21a68976c6d3e56f&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8f1b1d60-cf1b-42b3-9faa-f634c89c3f84/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Q6Y5FFKW%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T041620Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCXyih%2F71Zvg50Lq9rQ4CW2C4Qfd8uoyNXOjBgXZ544nwIhAM1j4XhcK3QYm8KW8wR%2Bm96glley%2BTB%2B4AYkEdvrwklbKogECOX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyRQoA2EgRKQz6tIucq3AMfdndtd93mGs78Z7dNgJGLz7kxqwzfHIyl1P2ie%2FC53UtnyBL71UyWCZFtmVeWY6g7YfZN3R4RbBty9bDxYu6rTCfzBM1tZL%2Fn%2Bi7r%2Fb8ofSR4fsAKYpTdRO47Zh6FeF1ci0r%2FaFVkOmyURUFBRVxnt%2BCw9NgTCHYjK3sYrhawyBPmZz7cSFSgyVpA3eiTpAuDnJ2vSdVaX3gtZU9q9J5Onome0OrCNGVWK6nXzYDWrDCeMTaEx9g93zUW5e5xaHHXdH8%2BH0Bs2t3hTNx9GuSMUbv%2BcDniNz%2BIGWj7qCxqL5MN5MRamLpK%2BfuLXHFfts3WNhNRE86KBqTvoai39lKIGgNQEBJwe6mKcw7yMVXcCDFTrBB22gBt79KKi7PlSCqwl%2BWUHXMUElZs9ODpRir9wcTsN32i7N2Q7k25Su9eGR%2FfBSRr9TdTgdCjVHGJoc3qFRvBlTwBefuS3LpTuo651WfOIIbAMuHuTSELggs4Mp1Zl64QWybfIMivTDhh4IDWgNZKEtm0%2FmjnZkTdrXZuS5s5RDazVp7ui2bQ0yhwNooVsj173nmYV82iPEDQjsvFNxjfwhRjc7I7BgbBDMWzFYHWXwpiYjbiUJaSjorI4nDX%2FABzkgMx%2F6L6SjCf4fu8BjqkAbQC4FHnvzZIXxEdcp9y5Syu%2B8mmcp8%2BatRTld3pnPk4NHefsWWd3n47GB9CJmRfmP27rKiqlBBi3%2FPhgXyqjtcSCUGz1wQBlCYvm4hhJSBem8ghthk%2FMH01SX8oqc8iNPvS484qTuyn0Wb2DO3oU5YSPmOx396Tv13l2h9FV1H6I8cRT%2BcsG7rkjYZX7abKvaYivt5C1pGRCwFfHlHN4YzlH4VE&X-Amz-Signature=43309b64c566d724479ea4efa457a09e4b994d41e842b19a4a27c0873d1f6119&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/13ad0497-05fe-4eaa-984e-707b33e14761/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Q6Y5FFKW%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T041620Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCXyih%2F71Zvg50Lq9rQ4CW2C4Qfd8uoyNXOjBgXZ544nwIhAM1j4XhcK3QYm8KW8wR%2Bm96glley%2BTB%2B4AYkEdvrwklbKogECOX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyRQoA2EgRKQz6tIucq3AMfdndtd93mGs78Z7dNgJGLz7kxqwzfHIyl1P2ie%2FC53UtnyBL71UyWCZFtmVeWY6g7YfZN3R4RbBty9bDxYu6rTCfzBM1tZL%2Fn%2Bi7r%2Fb8ofSR4fsAKYpTdRO47Zh6FeF1ci0r%2FaFVkOmyURUFBRVxnt%2BCw9NgTCHYjK3sYrhawyBPmZz7cSFSgyVpA3eiTpAuDnJ2vSdVaX3gtZU9q9J5Onome0OrCNGVWK6nXzYDWrDCeMTaEx9g93zUW5e5xaHHXdH8%2BH0Bs2t3hTNx9GuSMUbv%2BcDniNz%2BIGWj7qCxqL5MN5MRamLpK%2BfuLXHFfts3WNhNRE86KBqTvoai39lKIGgNQEBJwe6mKcw7yMVXcCDFTrBB22gBt79KKi7PlSCqwl%2BWUHXMUElZs9ODpRir9wcTsN32i7N2Q7k25Su9eGR%2FfBSRr9TdTgdCjVHGJoc3qFRvBlTwBefuS3LpTuo651WfOIIbAMuHuTSELggs4Mp1Zl64QWybfIMivTDhh4IDWgNZKEtm0%2FmjnZkTdrXZuS5s5RDazVp7ui2bQ0yhwNooVsj173nmYV82iPEDQjsvFNxjfwhRjc7I7BgbBDMWzFYHWXwpiYjbiUJaSjorI4nDX%2FABzkgMx%2F6L6SjCf4fu8BjqkAbQC4FHnvzZIXxEdcp9y5Syu%2B8mmcp8%2BatRTld3pnPk4NHefsWWd3n47GB9CJmRfmP27rKiqlBBi3%2FPhgXyqjtcSCUGz1wQBlCYvm4hhJSBem8ghthk%2FMH01SX8oqc8iNPvS484qTuyn0Wb2DO3oU5YSPmOx396Tv13l2h9FV1H6I8cRT%2BcsG7rkjYZX7abKvaYivt5C1pGRCwFfHlHN4YzlH4VE&X-Amz-Signature=b025824b64614056c601499cee177dcd4c7679f524ed30d664e4e3503d6fbcff&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 2. Box and Whisker Plot
A box plot shows the distribution of quantitative data in a way that facilitates comparisons between variables or across levels of a categorical variable. The box shows the quartiles of the dataset while the whiskers extend to show the rest of the distribution, except for points that are determined to be "outliers".
**Syntax:**
```python
sns.boxplot(x='header_1', y='header_2', data=df)
```
**Example Output:**


![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d207ae92-0a7c-4e2f-aa65-0ee5a2c33bf7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XHOXSZWQ%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T041621Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDJRAHtH2uTNONnuWK1a2wvCVlbTqbkiX%2B3XJ%2FVdW1RGwIhAKilcF72unWMjTSKGIT9lnv18TNhhoAoY2InwJ7dOQpDKogECOX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzGS3Ceav3p6zjKfCsq3ANFOZZ1GgqnIBNrPkCJRVRG56aaZb021KLqjvjy6RMQ1mvE6mKv6gRJuXPT4%2BQwuPp%2FEUsYefUyH6q9ddTHTX8VgBt6fBrqwAO%2Bj5e%2Fu9zApArIgjMKC%2FyDKMXhJrU39zCMGrO6HEYPDcPN1vQEOzQ164Sjtuxv1OjH9Wj3XmR7%2BTRWAmra%2FxpFjzhKj1WzVl%2FrTvOfT0L42nAcLlJdzfyG3U04BprR0DQzvSLqeJMFd1hK0gQOafo4CLt6dYvNVQnyfWRF56nMFZ9EySV5X4wgDmvnEC9FL52dELMZOcfiLimV0R9G8gwBbKDOt3cbeh57UdUxPIJhu7hu8TV5NUQGdjbSkAqqpnhhLMUH%2FLca0H2e0CsBa74My07zVLQgCM4Z3rxQ3kNIP9W%2FdF2zDiBiitoHxwkB7FGYJ761KAwwNC72XJlwqZpwG0kzdqOOY5sucWmMjeaEyPJDwQSIqECRB2LJVwnSU%2FrXBgrmPGitxu5r2SnRbt2fBiEC7eOYd9bqPte0Y6QVkDcVqzs0W3gKrCAryUDSB4iPHH96gQ4AyiXdvi0hvwvuG%2B%2B0aEqQ%2Bk9ej1cjX%2Bl28oTxNHq3D5MyiZfzAAH7sC0syR68GB91QRekCbRmJHhgxUBCbDC64fu8BjqkAW1%2BpXXh5xM%2FLbg1TDV5NKTvCFIssc74nkJVcgV8uYrlXGMMCyb4CcjDd5N%2FjSjNjVu2g4InujLNYz4qX51ebCCAHxOMeYN850wVD9sRA9vh%2BQcyikHi6pMN9L3YXtlNCsbcl%2F9in%2FTN5lioRjLPhvpB9XT%2BlG%2B5YA9NlgrcT4e0E9hG4HoNkt0hCMRhqVw8cnY4yCtX7AHoA5Ztfl6JFtlKaHfW&X-Amz-Signature=646ac603ef3c0a83b90806ae8f1e8703fef9b7dace4794871156330a9e816d71&X-Amz-SignedHeaders=host&x-id=GetObject)

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0e516edc-7551-4792-ab18-0494db3c4c0c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YYXBS3IK%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T041621Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDuWKJc46E0XnIvFoR9y6HsWZvASWK2%2FQ5ShhJfhFawFQIgHIffEYFvcnq2JwHeXIA0tDLvb6wZpuNr%2BAQN87A1BNoqiAQI5f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDIxbKaQjhoa6WCkt%2ByrcA2J7GKFEg8ex5tg2PRl%2FEqYPwArashXzbfXMf9lPPME0nDpPsbAYJkFV9PtvuF5Pw6O0IwO8AysSYsKKPRX3n3FHZs1y0Fvap4gzyT7ymkIWSX3eoNMewsp3g5ZNkHhls%2BlP0zwXScOfu2odC8JCd4fQe6Jp9jDjyIrb4OXD9OEmyqlau5iiIYahWa1SzeYmR4VDTjt671LEbfj6DRSPErD3LfTKEbtjiUHEbbCT10Ewy6EyOlEiikuXS8S01C5lRugcx6wu2a6%2BKcfh%2FkE88SYzbnb2yTuutBpKOMbmCYNUuElG5%2BChjcRU1FsUpju3c0V7N5JsK6D8xekq7Oh9YSUrDrc3b%2B8a4gaganRWdL%2FeAT66tjVtD9s%2F9xR1X5C4ciXGNHLtq1mcR8TZ0Ye%2FfRXhwbw0N4NPxKWqS75Tu%2B%2Fmg41srXOyyNznWN4j7%2BFYTZydaymL88vZn4rlFo1Gaewtk%2B9nr7FD0vZZxoHG5VQ3bxuB651rRXCabI1yfSEJb8i%2BVasJdcZ6Hq5MebBEmCH8KVi7xo42Sjs25rvzO%2BV8GZ%2FhAEOYL7YGvBOohsS6C5ekNlylVV5M%2FwTSfJXSgO6dcrFPvYnRP8nplOUdHjpyiRJWMOlAI2dXKCg0MMXh%2B7wGOqUBu%2Fx5g8%2F8sbl25FeQ29wsw55lKXBBsYQG4O8p1BOt57aNI%2FxQilTtqw3JRJNQixiOOz8w3Sowvf6gDGvd1YzlQ2rCvqHKJy2Gwi3ygOhiF9t8eMVHvkmy58Bn6Su9G2t2CMPPkYB1KM55kLsEBDpqPaWJ5QcylcTDkblk2lpk1Ows%2FuCLbytpn1zVhPEurIWKjRCayDyAHVylXHhbRffoyl%2FW3T%2F%2F&X-Amz-Signature=d4502c648ac08a0b045ebf36a054e737b196e9fd9f4201c4676f09c98652f850&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23a79b9d-2356-49a9-8fd9-65c6b0ab2cc5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Q6Y5FFKW%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T041620Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCXyih%2F71Zvg50Lq9rQ4CW2C4Qfd8uoyNXOjBgXZ544nwIhAM1j4XhcK3QYm8KW8wR%2Bm96glley%2BTB%2B4AYkEdvrwklbKogECOX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyRQoA2EgRKQz6tIucq3AMfdndtd93mGs78Z7dNgJGLz7kxqwzfHIyl1P2ie%2FC53UtnyBL71UyWCZFtmVeWY6g7YfZN3R4RbBty9bDxYu6rTCfzBM1tZL%2Fn%2Bi7r%2Fb8ofSR4fsAKYpTdRO47Zh6FeF1ci0r%2FaFVkOmyURUFBRVxnt%2BCw9NgTCHYjK3sYrhawyBPmZz7cSFSgyVpA3eiTpAuDnJ2vSdVaX3gtZU9q9J5Onome0OrCNGVWK6nXzYDWrDCeMTaEx9g93zUW5e5xaHHXdH8%2BH0Bs2t3hTNx9GuSMUbv%2BcDniNz%2BIGWj7qCxqL5MN5MRamLpK%2BfuLXHFfts3WNhNRE86KBqTvoai39lKIGgNQEBJwe6mKcw7yMVXcCDFTrBB22gBt79KKi7PlSCqwl%2BWUHXMUElZs9ODpRir9wcTsN32i7N2Q7k25Su9eGR%2FfBSRr9TdTgdCjVHGJoc3qFRvBlTwBefuS3LpTuo651WfOIIbAMuHuTSELggs4Mp1Zl64QWybfIMivTDhh4IDWgNZKEtm0%2FmjnZkTdrXZuS5s5RDazVp7ui2bQ0yhwNooVsj173nmYV82iPEDQjsvFNxjfwhRjc7I7BgbBDMWzFYHWXwpiYjbiUJaSjorI4nDX%2FABzkgMx%2F6L6SjCf4fu8BjqkAbQC4FHnvzZIXxEdcp9y5Syu%2B8mmcp8%2BatRTld3pnPk4NHefsWWd3n47GB9CJmRfmP27rKiqlBBi3%2FPhgXyqjtcSCUGz1wQBlCYvm4hhJSBem8ghthk%2FMH01SX8oqc8iNPvS484qTuyn0Wb2DO3oU5YSPmOx396Tv13l2h9FV1H6I8cRT%2BcsG7rkjYZX7abKvaYivt5C1pGRCwFfHlHN4YzlH4VE&X-Amz-Signature=56c2879e58613b2ae4a442d68a3efadce67f176642f874bbeabef290f45cf247&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 4. KDE Plot
A Kernel Density Estimate (KDE) plot is a graph that creates a probability distribution curve for the data based upon its likelihood of occurrence on a specific value. This is created for a single vector of information.
**Syntax:**
```python
sns.kdeplot(X) || sns.kdeplot(df['age'])
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0d571213-2a2f-4921-a50b-880847aa05ee/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Q6Y5FFKW%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T041620Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCXyih%2F71Zvg50Lq9rQ4CW2C4Qfd8uoyNXOjBgXZ544nwIhAM1j4XhcK3QYm8KW8wR%2Bm96glley%2BTB%2B4AYkEdvrwklbKogECOX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyRQoA2EgRKQz6tIucq3AMfdndtd93mGs78Z7dNgJGLz7kxqwzfHIyl1P2ie%2FC53UtnyBL71UyWCZFtmVeWY6g7YfZN3R4RbBty9bDxYu6rTCfzBM1tZL%2Fn%2Bi7r%2Fb8ofSR4fsAKYpTdRO47Zh6FeF1ci0r%2FaFVkOmyURUFBRVxnt%2BCw9NgTCHYjK3sYrhawyBPmZz7cSFSgyVpA3eiTpAuDnJ2vSdVaX3gtZU9q9J5Onome0OrCNGVWK6nXzYDWrDCeMTaEx9g93zUW5e5xaHHXdH8%2BH0Bs2t3hTNx9GuSMUbv%2BcDniNz%2BIGWj7qCxqL5MN5MRamLpK%2BfuLXHFfts3WNhNRE86KBqTvoai39lKIGgNQEBJwe6mKcw7yMVXcCDFTrBB22gBt79KKi7PlSCqwl%2BWUHXMUElZs9ODpRir9wcTsN32i7N2Q7k25Su9eGR%2FfBSRr9TdTgdCjVHGJoc3qFRvBlTwBefuS3LpTuo651WfOIIbAMuHuTSELggs4Mp1Zl64QWybfIMivTDhh4IDWgNZKEtm0%2FmjnZkTdrXZuS5s5RDazVp7ui2bQ0yhwNooVsj173nmYV82iPEDQjsvFNxjfwhRjc7I7BgbBDMWzFYHWXwpiYjbiUJaSjorI4nDX%2FABzkgMx%2F6L6SjCf4fu8BjqkAbQC4FHnvzZIXxEdcp9y5Syu%2B8mmcp8%2BatRTld3pnPk4NHefsWWd3n47GB9CJmRfmP27rKiqlBBi3%2FPhgXyqjtcSCUGz1wQBlCYvm4hhJSBem8ghthk%2FMH01SX8oqc8iNPvS484qTuyn0Wb2DO3oU5YSPmOx396Tv13l2h9FV1H6I8cRT%2BcsG7rkjYZX7abKvaYivt5C1pGRCwFfHlHN4YzlH4VE&X-Amz-Signature=728930c6e9ef503dd6975fe5dfaede937d5dd20fbd81574d25fc9d11a7c8c9d6&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/53752550-ef82-4ca9-a01a-09921f0282d0/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Q6Y5FFKW%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T041620Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCXyih%2F71Zvg50Lq9rQ4CW2C4Qfd8uoyNXOjBgXZ544nwIhAM1j4XhcK3QYm8KW8wR%2Bm96glley%2BTB%2B4AYkEdvrwklbKogECOX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyRQoA2EgRKQz6tIucq3AMfdndtd93mGs78Z7dNgJGLz7kxqwzfHIyl1P2ie%2FC53UtnyBL71UyWCZFtmVeWY6g7YfZN3R4RbBty9bDxYu6rTCfzBM1tZL%2Fn%2Bi7r%2Fb8ofSR4fsAKYpTdRO47Zh6FeF1ci0r%2FaFVkOmyURUFBRVxnt%2BCw9NgTCHYjK3sYrhawyBPmZz7cSFSgyVpA3eiTpAuDnJ2vSdVaX3gtZU9q9J5Onome0OrCNGVWK6nXzYDWrDCeMTaEx9g93zUW5e5xaHHXdH8%2BH0Bs2t3hTNx9GuSMUbv%2BcDniNz%2BIGWj7qCxqL5MN5MRamLpK%2BfuLXHFfts3WNhNRE86KBqTvoai39lKIGgNQEBJwe6mKcw7yMVXcCDFTrBB22gBt79KKi7PlSCqwl%2BWUHXMUElZs9ODpRir9wcTsN32i7N2Q7k25Su9eGR%2FfBSRr9TdTgdCjVHGJoc3qFRvBlTwBefuS3LpTuo651WfOIIbAMuHuTSELggs4Mp1Zl64QWybfIMivTDhh4IDWgNZKEtm0%2FmjnZkTdrXZuS5s5RDazVp7ui2bQ0yhwNooVsj173nmYV82iPEDQjsvFNxjfwhRjc7I7BgbBDMWzFYHWXwpiYjbiUJaSjorI4nDX%2FABzkgMx%2F6L6SjCf4fu8BjqkAbQC4FHnvzZIXxEdcp9y5Syu%2B8mmcp8%2BatRTld3pnPk4NHefsWWd3n47GB9CJmRfmP27rKiqlBBi3%2FPhgXyqjtcSCUGz1wQBlCYvm4hhJSBem8ghthk%2FMH01SX8oqc8iNPvS484qTuyn0Wb2DO3oU5YSPmOx396Tv13l2h9FV1H6I8cRT%2BcsG7rkjYZX7abKvaYivt5C1pGRCwFfHlHN4YzlH4VE&X-Amz-Signature=509b197195c0319c1c7913815792095b7934ced2a9b092ad7a369a6b75157e85&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
## 4. Correlation Between Variables
Correlation is a statistical measure of the extent to which different variables are interdependent. It indicates how changes in one variable are associated with changes in another variable over time.
### Positive Correlation
Positive correlation indicates that as one variable increases, the other variable also tends to increase.
**Example: Engine Size and Price**
- **Positive Correlation:** Engine size increases, price also increases.
- **Visualization:** Scatter plot with a steep positive slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c7ea9b0-3ef3-4357-a9c3-554fc71b6b15/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YQBSUTU3%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T041621Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIAu1k9sXxMorXyuavBRgyyL%2B31QpElkXLlitdMPI%2FE3PAiBQxlYKqMSzyUZEEEb23thp79SmQFrxRXZRUpjwIXXmlSqIBAjl%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMjXijOU1VXXDJhWqZKtwDZ3Bc18ItWQ7klkE6DsIRm%2Bi4ZAwVAYznwcdsN9d423SJibaCPaBLc53Lvjbt569qocJ8jjbmuvxCSGTpgE1UGlds4StH5r7SDv98XqaV1ZkiHBNcSZ1wcSg0ONgXW5tA4Se0xqCsqHT7j7iqWWMYd3zIaaMelkzwem5GNzmwEyhcj3pSxYybJRO0yM5MreY8dd1xNRuAAX1bPhjSKWLNwztNbD1eFJQlWv7xZZW5AXucJYqF5uHQL2kenQJvNdjm2yP5eCtRwUjr2Jg6KM9m8pGO7Szti4B4IF2jwgTHc74FiJ9bkw7CbWAuibZKfHZGB64PsvpGpd%2Bw6VImjs435uTc4BAZe8HW7d6QZeR2Q3F0FpjVGCBVTRsrc00%2FHnj2ehnd8%2FIrHA8qZYKmaaZf42GSUlBf%2BeMbNnq39xfOEcc%2FS6ltB6VpWPX8lOQ%2FoJbo5T41jM6PhOZ1BV50sMWlTKN%2BnQzhscCu8ASfGmpwbrShtx8SPmxraCqDN38DEctwVexgJcMskdbTJe3JYP%2BVnx09YFvwSENrHpgkb83Vmp5wV4Wt2Gl6kuN0ieYGIpHSMksSOtIs%2Bq%2BgiIHNef3%2BxrhTyFxbpvi8vEL79zCSwcSD8kWHLBz7cUNSF6wwqeH7vAY6pgFNKVujI1B8P%2Bp5FuMdYSTghFEJesCcpUrO7iZDxkRzaWcNv%2Bi4yM7Ab%2FgQ0TI%2FQFdnJe%2FBdBeh03lu%2BqulSDCckYypLBDibJP4nxIYQ3q%2FJgfmEe%2BktQNy6XZG1TVPQe6rkz7ffgTg06mfExBUOewnJlmNTb43Mja14O%2F5lni%2B4oU72bdajWLjmr2LOwE%2Bpw5CJ9Cr55sMqOEJneW0kDPPdVP4yvvK&X-Amz-Signature=1323fdaa5b3fe22d45a86ba46dd32289264bd87b561bb82af42f473d379eaa98&X-Amz-SignedHeaders=host&x-id=GetObject)
**Explanation:** When engine size increases, there is a corresponding increase in the price of the vehicle. This positive correlation suggests that larger engines tend to be associated with higher prices in the market.
___
### Negative Correlation
Negative correlation indicates that as one variable increases, the other variable tends to decrease.
**Example: Highway Miles per Gallon and Price**
- **Negative Correlation:** As highway miles per gallon increases, price decreases.
- **Visualization:** Scatter plot with a steep negative slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/10f1f798-9cc4-4df2-a9c1-5a339f554a0b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662XKZIFUI%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T041621Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIF%2By5jhcaoGAyl2htIG%2FSDcHqafC5Yzz%2FeOEhj6lf%2BS1AiArgFOIk5LKb2APVtQMs4mJxQjhzxoHcUPsbIoFfKd3MyqIBAjl%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM%2FQitn8Rm5T5oPMqFKtwDQUG5S0IoSk6VjXq%2BA7vIY1crMrR%2B9qgNhXvwOiJq5oOjYAYNA3FE0%2Fr8VDGK9YRhFYcssLBTi82c%2BDgeGHC%2FeNNP8Arkzoj4%2B%2BcVmXhATqEjQt%2BykzpbKsV4PUIRpEfkPAeh%2BgSxmRzAZjtrSmOmaLnqPReRqyu0XoXgUDAFfia50izRoHFVKAcOOON2CrwGEvZ%2B36A1uviGUxNat2X%2Bs0QtZ4ZDYpZJNI2kl0Vvgdpwubypyni%2FSRcwAmCRkGlDkW9VO%2Fzh8CqlkvNCQg%2BHKTVcOAzc9yW%2BHL1B1MGi4Ep7U7g%2BgYknNUpEhsMsP1BR04FsURMzyW3xs%2FCSHItwnvhUqXCkcnsbEXNRtpiw8KqTUH1LXBspfT9ytnTSIhOCrWTP3SVY05G3lFfgYL0eu2%2F8QRXeizh5TH2xNg1dQAC22dFq6shFFZcnUY5AmBQm0gMa1H7uqtxNFo1zAJOEQqnwbPbb3NzNtthwmA%2F2UQ65DP7K4zO%2BefdqkXfFNKILot0neL7TPQ07NJyPvvqcsc%2BhA7rZnLH%2BxBsVw576MYYPHvyhSpU1CTUZQcdeZaRsMWMOrq%2BNsmtFxWq6iYJjf98Zo5XTNAETzDSLTwQ9eHvce9l3Omd7u%2FCkyV4wj%2BH7vAY6pgE5aL9bK9%2B9leLPYTLqsHNlsRSHVuxLd7%2FQ%2FSfHEDdmArXtqzonV5oVVLGgsbubUAhXPFsyAGUzzRwWCWUfXLSuaseCEvSh6mrIdkKYXTrapIyVNQszcNNem1pWsNAZ%2F6rGdb%2F6rrA0HjyWto0I0be8vcVbxxQ84ieYKsGcfuZctFEMhXQwYsx506HdUMxzNMlHkTRBglezVyp0tyBpHdsiLx5w2SrP&X-Amz-Signature=b3516365211a005c95870d76ff6a8df6fdca7acbc259d25e7a945e2ead483b2e&X-Amz-SignedHeaders=host&x-id=GetObject)
**Explanation:** When highway miles per gallon increases, the price of the vehicle tends to decrease. This negative correlation suggests that cars with higher fuel efficiency (more miles per gallon) are generally priced lower in the market.
___
### Weak Correlation
Weak correlation indicates a lack of strong relationship between the variables.
**Example: RPM and Price**
- **Weak Correlation:** Low and high RPM values show varied prices, indicating no strong predictive relationship.
- **Visualization:** Scatter plot with no clear trend or slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9f914514-8914-4bf4-ac84-d9e3077f6eb1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WCLJ7RYD%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T041621Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHZwnlC2veYYOcNFraEm8MzSLjParBtOdM8YBj2YuhYgAiBQdEO0qNtlu2Pd%2FeRx%2BRBs4p12Ah0gHWVbtI5TJty4JCqIBAjl%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMsOtqwAjKyCAHKvhVKtwDtvBSiypfXSzJTwiZFCD%2F5n2O5VphIwLhdeb%2F5S%2BfNX8uyokO2ivA1zfY5T69kJcsC2PdwJ%2BtmEXyObR5teEorimlThDutAuVbrFY97GudmwxnQw%2B28RGtCvYhqgjIOk3XX%2FM%2BCcsB%2FY2PbqqVZNWN8WxaMZc5PoTAmzIW556IrTSRK90IlncLte3QA8meWX64XDz8VkndqE0ejyYJ%2FlD8TVG1rqOFpg%2F4y58jepRafyf9JaCkcqy7agjk1w%2B0JfiRz1xgUe%2BIWE2vxcdEw6pVYxl9PDG4GpSOp%2BwV55zGIXE3JNJPr3J5Ky6LTtaNJGGZiHfMmqPk%2Fhcoe6YsEDsskmLEh10TzlnGvUOhWYKOIefGCs769EyeGBUxgtVOa6U5QjvloZmFJA%2F8M0ZLS0Yaubo8lO%2F0YdG%2B9SEOe%2BIyh3DJO3%2FwU50HpKdUeR5dS28E1i5cFnp3mJMLJX38orWGoUwV3u%2FIa99vZWhwmwktiGH4bRWQ4E4gh64luSDVzXK1NplE66fbe%2BVYUI0nIDuSTNLzyrywm%2FiHnHeklKi%2FQu%2FlXM6VMbXlVJ3T9f2Npj6FqhzwlnJSCU%2BQEG3LTN3FfHTZMHueHzRWbVsbWxQd3JBJ3cONi3yKX1AxZ4wmOH7vAY6pgHQELB%2Bx1368RkKpgiwCrxIR65TXUfqTsUxOLYmCdFEC5%2F4JxNiZaETY4D3U3IQbAeCjl1Syg1iWn6TtGo6LvTVx%2B%2F3ZmC2Xc6i6cLAV5r9OnuWn%2BEJpJfGqYbhQFX%2Fn3gvKDVPtDRInkH80eBEFJzXB%2FobrEd4Ec2pQe2czAOkoTQMSLZjc4D5No59T0POMgbApKk6Ys1LAqNjHBvmZup1enUudTA4&X-Amz-Signature=ae169b654c02b53fa69d8ec8997d811a9a718342e11af71a200fd476c87d013e&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f18086e5-5b04-4fbf-8309-8944ab20d213/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Q2ORAZU2%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T041621Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHt1uCet%2FsF4yZPGVFNSydzjztskjrlVujQZH4leIsRDAiA6U6fW4MN6QU7c33cLYSayRjLKilyNoJcBx7gqQCQ%2BOyqIBAjl%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM3S8c1Z7czM%2BUQQeIKtwD4%2F%2Bi8%2FR5gYzQN%2BHE5dyGzHKfidT1cbJ5dBVrU6bbydHcUfdh%2BXAlPwQvOmCLZEGTzzx1BvypS%2FjKgjjQq0wHL9f41F8mhUDDZvJhESpcEMLKkW8mDrLOH%2By1jS9TF8Zf6woTY1RRhFr9%2FuMTvd30FXjdMxaPapNmoG%2FYSaEJK3YJ7CDzs%2BybxBPdhfdcwcvV7Sw7%2F7hwkTtrmLFnV7Sw8T%2BdiKcLZLBOPt7DMokORzot%2FTY28DEFY4yQyJ%2BW86Y%2Bk7%2B3gKhu7M%2FkYeU8bSHAmaxf%2Fc7R748Dq2Bf%2F1Jn1lzI40zwZ0xxtFvw9jlkW4dAY0agV8PDOu9A2zSEhP%2FE8j3vDAWSW%2Bqjo%2BQf8i5rO%2Bo3qKr6DkP2COh5gmHRoRJu2dNUNwwnJNy4tDvaq%2BgVRbBSrUueKBEYuEpQ%2B16GJKL435%2BIS6JuZOLaFFG9G5YYry9WMheSonVGi1nbe9GwRysjXABK7alHHTXthhwSbTXFTigzJBbQsyu0w26TinElTjoEjMWRvmWtD1g2Zm997K72tpvVLFrKAOEnExPy%2FTRqgV2dEucZbfQ%2FASTDaNfDiy%2FPKq1sDNrFT2XDDr2Fg3Rtc0HK5eBhjiZ1d0seycXActZEcnmLPCKF8jAw1eH7vAY6pgEnp4r43YYY1Wt%2Bt9SdiTM%2FgaZ07UJzna2djNm5ZmpeS4dZY4C7sfbX8BwU12S81Ahgs7A5p3VoYZYE7f4tWsewEzKKP6DsQ8iModbIiuIvwXAFgXCVfh3lVfWNMDqPpc%2Bx23B0dTR3tOW4Bv0dkRVdpOpJARPVELFgo5iVRLK2bPM3X3IOJBGzdCT8jbZvbUhGz7p4QkLCUlRpRH2zk2PJh6WraGXH&X-Amz-Signature=9dd2acb98677944e4de2058592504cce1fe53ac8ec43f18b4dae7265d531c744&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Correlation Plot
Heatmap visualizes correlations among variables. Color scheme indicates Pearson correlation coefficients. Dark red diagonal line shows perfect correlation (value of 1) between variables and themselves.
This heatmap offers overview of variable relationships and their link with price.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cd3b341e-cc1a-45f7-8aec-cdc00436d270/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Q2ORAZU2%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T041621Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHt1uCet%2FsF4yZPGVFNSydzjztskjrlVujQZH4leIsRDAiA6U6fW4MN6QU7c33cLYSayRjLKilyNoJcBx7gqQCQ%2BOyqIBAjl%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM3S8c1Z7czM%2BUQQeIKtwD4%2F%2Bi8%2FR5gYzQN%2BHE5dyGzHKfidT1cbJ5dBVrU6bbydHcUfdh%2BXAlPwQvOmCLZEGTzzx1BvypS%2FjKgjjQq0wHL9f41F8mhUDDZvJhESpcEMLKkW8mDrLOH%2By1jS9TF8Zf6woTY1RRhFr9%2FuMTvd30FXjdMxaPapNmoG%2FYSaEJK3YJ7CDzs%2BybxBPdhfdcwcvV7Sw7%2F7hwkTtrmLFnV7Sw8T%2BdiKcLZLBOPt7DMokORzot%2FTY28DEFY4yQyJ%2BW86Y%2Bk7%2B3gKhu7M%2FkYeU8bSHAmaxf%2Fc7R748Dq2Bf%2F1Jn1lzI40zwZ0xxtFvw9jlkW4dAY0agV8PDOu9A2zSEhP%2FE8j3vDAWSW%2Bqjo%2BQf8i5rO%2Bo3qKr6DkP2COh5gmHRoRJu2dNUNwwnJNy4tDvaq%2BgVRbBSrUueKBEYuEpQ%2B16GJKL435%2BIS6JuZOLaFFG9G5YYry9WMheSonVGi1nbe9GwRysjXABK7alHHTXthhwSbTXFTigzJBbQsyu0w26TinElTjoEjMWRvmWtD1g2Zm997K72tpvVLFrKAOEnExPy%2FTRqgV2dEucZbfQ%2FASTDaNfDiy%2FPKq1sDNrFT2XDDr2Fg3Rtc0HK5eBhjiZ1d0seycXActZEcnmLPCKF8jAw1eH7vAY6pgEnp4r43YYY1Wt%2Bt9SdiTM%2FgaZ07UJzna2djNm5ZmpeS4dZY4C7sfbX8BwU12S81Ahgs7A5p3VoYZYE7f4tWsewEzKKP6DsQ8iModbIiuIvwXAFgXCVfh3lVfWNMDqPpc%2Bx23B0dTR3tOW4Bv0dkRVdpOpJARPVELFgo5iVRLK2bPM3X3IOJBGzdCT8jbZvbUhGz7p4QkLCUlRpRH2zk2PJh6WraGXH&X-Amz-Signature=3f2885d7acabed96805a2148514fd437e443b12c0e9367059cc3021dda7f4ea4&X-Amz-SignedHeaders=host&x-id=GetObject)

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
