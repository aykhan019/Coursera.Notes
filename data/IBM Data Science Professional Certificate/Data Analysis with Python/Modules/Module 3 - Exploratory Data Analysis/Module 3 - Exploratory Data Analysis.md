

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7e6d594d-952e-44b6-97ea-31225882aea6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664RJAGYAM%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T091431Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHdXUHNo8qm1iv4ssX1If2k8fjv2mU6QLzbkrD6mk%2FGTAiEAkCumK3dj5CZtXZq55%2Bcoe3XMRGhL94bi%2B4kcQ2%2F1MpMqiAQI0f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDAxclJyakyTjkVWzsCrcAyMQU1AQNz0ZhGWppzCnXs1SHRLfJLMe5PPIeYC%2Fn8qwFeMdMAQk49akDb85S7speIE1la%2BzSmvMftBFPhNMj%2FBZB%2BAdKVeMmfl7h1K9egZTvc9%2B%2FZFGEAj0x5msOcp7jqUiVtk1s45aa%2FuSvlYdnJqnYlM3wcRRXxAoxRrulbpYlpW4tB1zbU1EdAwlI4JmQqcmV%2BNVarWAgbfAvr1Eql6RViq1tcrhFnL%2F%2BOhRpfjN6teqNEsbW78zKWcjINJHwymWBk%2FQcxDcdl9p3t%2BUVEqOlQ0Glzb16qh7VnRj2eHOS8%2F%2BvyJae2m4c9xuUE0sBNoMUHCcEZN7xNtq2Kellhy0keIYMXIRw%2BNWYePFRtOuTVjUZcVVfgB2BIc7PEi76CeiX8yDMf9SnYCVwpCjTTC8PAqHxyXjTUtg8k2Y%2F%2Fs3nXEWNFZFvPvoSB4YcBamu5zGoCZupglM%2FcuK1BVBK0TiqyafYmIoEow6gE7wG1iULc%2BY0G5k7I%2Bc4QvG09%2B14eTMh5WccZykcnXZflnt6qZLHueLS5FKjkm215Kb8vD%2FFN0ldPBC1tQek7XTKY0qwes2uDwQluLAJuvdgFfeX0tPrUNZkiVBmw3Dz7pnOF4N%2F0Cm1C2lnrw8hpq%2BMJ6l97wGOqUBUcmp6mEewbnpsTXVdhMAwW6ADGz0PlWeZXPM%2B6%2F2stncKAevQC7gMNLeyLbi3Syme9009u5XU5cmsENwHKCXuceeDjEzEJagQFkTmGxxL1nwEs8R71PYjKb1fhYalxMpn%2FRAj0QStUM1nlQI23y0JZx5aV9q%2F0Gc5MiFy1sEdebUKu%2BTpHLVItMTCfFTtjhDh4PkxqMu0pHXcs7ebp4id1hxAoV%2F&X-Amz-Signature=d99e476033e32c2aa9f683f46205ca734f2e142da61e28459168e695406b34fa&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cbfaed9e-b398-4902-8936-dea058b21def/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664RJAGYAM%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T091431Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHdXUHNo8qm1iv4ssX1If2k8fjv2mU6QLzbkrD6mk%2FGTAiEAkCumK3dj5CZtXZq55%2Bcoe3XMRGhL94bi%2B4kcQ2%2F1MpMqiAQI0f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDAxclJyakyTjkVWzsCrcAyMQU1AQNz0ZhGWppzCnXs1SHRLfJLMe5PPIeYC%2Fn8qwFeMdMAQk49akDb85S7speIE1la%2BzSmvMftBFPhNMj%2FBZB%2BAdKVeMmfl7h1K9egZTvc9%2B%2FZFGEAj0x5msOcp7jqUiVtk1s45aa%2FuSvlYdnJqnYlM3wcRRXxAoxRrulbpYlpW4tB1zbU1EdAwlI4JmQqcmV%2BNVarWAgbfAvr1Eql6RViq1tcrhFnL%2F%2BOhRpfjN6teqNEsbW78zKWcjINJHwymWBk%2FQcxDcdl9p3t%2BUVEqOlQ0Glzb16qh7VnRj2eHOS8%2F%2BvyJae2m4c9xuUE0sBNoMUHCcEZN7xNtq2Kellhy0keIYMXIRw%2BNWYePFRtOuTVjUZcVVfgB2BIc7PEi76CeiX8yDMf9SnYCVwpCjTTC8PAqHxyXjTUtg8k2Y%2F%2Fs3nXEWNFZFvPvoSB4YcBamu5zGoCZupglM%2FcuK1BVBK0TiqyafYmIoEow6gE7wG1iULc%2BY0G5k7I%2Bc4QvG09%2B14eTMh5WccZykcnXZflnt6qZLHueLS5FKjkm215Kb8vD%2FFN0ldPBC1tQek7XTKY0qwes2uDwQluLAJuvdgFfeX0tPrUNZkiVBmw3Dz7pnOF4N%2F0Cm1C2lnrw8hpq%2BMJ6l97wGOqUBUcmp6mEewbnpsTXVdhMAwW6ADGz0PlWeZXPM%2B6%2F2stncKAevQC7gMNLeyLbi3Syme9009u5XU5cmsENwHKCXuceeDjEzEJagQFkTmGxxL1nwEs8R71PYjKb1fhYalxMpn%2FRAj0QStUM1nlQI23y0JZx5aV9q%2F0Gc5MiFy1sEdebUKu%2BTpHLVItMTCfFTtjhDh4PkxqMu0pHXcs7ebp4id1hxAoV%2F&X-Amz-Signature=9ce29102a63eb5448680338129d328e79d92016071fb01f10d55e4648293d7f8&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/91181646-b1e0-4433-9711-6259a96a9247/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664RJAGYAM%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T091431Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHdXUHNo8qm1iv4ssX1If2k8fjv2mU6QLzbkrD6mk%2FGTAiEAkCumK3dj5CZtXZq55%2Bcoe3XMRGhL94bi%2B4kcQ2%2F1MpMqiAQI0f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDAxclJyakyTjkVWzsCrcAyMQU1AQNz0ZhGWppzCnXs1SHRLfJLMe5PPIeYC%2Fn8qwFeMdMAQk49akDb85S7speIE1la%2BzSmvMftBFPhNMj%2FBZB%2BAdKVeMmfl7h1K9egZTvc9%2B%2FZFGEAj0x5msOcp7jqUiVtk1s45aa%2FuSvlYdnJqnYlM3wcRRXxAoxRrulbpYlpW4tB1zbU1EdAwlI4JmQqcmV%2BNVarWAgbfAvr1Eql6RViq1tcrhFnL%2F%2BOhRpfjN6teqNEsbW78zKWcjINJHwymWBk%2FQcxDcdl9p3t%2BUVEqOlQ0Glzb16qh7VnRj2eHOS8%2F%2BvyJae2m4c9xuUE0sBNoMUHCcEZN7xNtq2Kellhy0keIYMXIRw%2BNWYePFRtOuTVjUZcVVfgB2BIc7PEi76CeiX8yDMf9SnYCVwpCjTTC8PAqHxyXjTUtg8k2Y%2F%2Fs3nXEWNFZFvPvoSB4YcBamu5zGoCZupglM%2FcuK1BVBK0TiqyafYmIoEow6gE7wG1iULc%2BY0G5k7I%2Bc4QvG09%2B14eTMh5WccZykcnXZflnt6qZLHueLS5FKjkm215Kb8vD%2FFN0ldPBC1tQek7XTKY0qwes2uDwQluLAJuvdgFfeX0tPrUNZkiVBmw3Dz7pnOF4N%2F0Cm1C2lnrw8hpq%2BMJ6l97wGOqUBUcmp6mEewbnpsTXVdhMAwW6ADGz0PlWeZXPM%2B6%2F2stncKAevQC7gMNLeyLbi3Syme9009u5XU5cmsENwHKCXuceeDjEzEJagQFkTmGxxL1nwEs8R71PYjKb1fhYalxMpn%2FRAj0QStUM1nlQI23y0JZx5aV9q%2F0Gc5MiFy1sEdebUKu%2BTpHLVItMTCfFTtjhDh4PkxqMu0pHXcs7ebp4id1hxAoV%2F&X-Amz-Signature=75548a4d32864787d5962df0f0f16f90b205530eec64a7f9f3e855dc57b04ea7&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/09aba1c0-0d55-41dd-852a-a04c5b8a3fac/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667DNMW45L%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T091431Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDNcEVT8iilgNTSVEjPhksFeyBvlm5oHdta83T08YlaYQIhANspQzr4ylCWPTu9RgTOc7UHdB76bcBoZ6mTrrpDMWgeKogECNH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igzl7bym4QkhHnegVYsq3APbjFIvchb9T763qFSCKiBd7RfDi1Q1FV1F4E%2Fa1JXjFG0bzLfjvr4B2E6HXAcw9KpDNWELnMaRdwJj23WkpzaGYwjZU%2FWH0GT8guni%2BVhXmhitQtyY%2FpfKfLhJZq%2BXk8YqoPiz0za%2BYofm13gSoTJfrvZV3DvwP40JAkT1q8fDfo1QV0ZTlQT2W%2F5qLZNaM7Kjr2tgtRZBSBeoVCrKeCdy6OnsntvjOUtho1uJ9Boe3G5UbwALn%2BpqL8s6x2s0d7wYAHmnH%2BXk4vA%2FWwV7xwaqEohHKbiSOcZjBkwi7xNSl%2BJWD6KIYKzEWVEXJixjttDdu3fZgivOJZCwOWuErlHEVgk82RdDlq13NyY5onOqA1q9ZV7JdMe1aGssAjOxCd5PEO886rkUU0iKnEfZ6AhPfgUtxgbT35U1X8wmbdms%2BDmEmV9kVFsJUoZboaZU30OP8cWdyrXj0CMFzT1rP9jpyDzwEqa0yWQ8iy3dqznepCv5jEYMcp3UObEXbXHGS5RNbmw2a%2FS1sRPmgAufayXD2zmYEminFxGKNueGrEtDZXu9PZFDAVXcLJgPeAxCize2Tw5pjvmeLT1U%2FGNuYk9JTAUtkJ%2BmPclvqOdU1OBqcCeWJF9bgZjJvZblODCXpfe8BjqkARPNGgvEImjzcUnjUT5k1OaVCb0soGk8bK9YxjU5DdTbzqDFYACP3ZqI4IHE%2BNsZDPI1NJW7sLEG8jZRE%2Bfm%2FHnBKZjJsdZ29IQ08gHE8Vu9NtUm8GnszcshTeIO9C89j0wk9Me7SUhcqylcYPq0cOdrF4yjAllVhOoIKzzdfe8kj4tZWwM6FJsIpQrjjkr4l4xRK6IbPOhMP1GC3FbWMjXYBZaa&X-Amz-Signature=a3e201888f9cb4cf70277dba71a6463eba9dc9f48840d6d5641b006cd08e74c8&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 2. Scatter Plot
Scatter plots present the relationship between two variables in a dataset. It represents data points on a two-dimensional plane. The independent variable or attribute is plotted on the X-axis, while the dependent variable is plotted on the Y-axis.
**Syntax:**
```python
plt.scatter(x, y)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23708af9-659f-4f23-b626-1a4292d7842c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667DNMW45L%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T091431Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDNcEVT8iilgNTSVEjPhksFeyBvlm5oHdta83T08YlaYQIhANspQzr4ylCWPTu9RgTOc7UHdB76bcBoZ6mTrrpDMWgeKogECNH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igzl7bym4QkhHnegVYsq3APbjFIvchb9T763qFSCKiBd7RfDi1Q1FV1F4E%2Fa1JXjFG0bzLfjvr4B2E6HXAcw9KpDNWELnMaRdwJj23WkpzaGYwjZU%2FWH0GT8guni%2BVhXmhitQtyY%2FpfKfLhJZq%2BXk8YqoPiz0za%2BYofm13gSoTJfrvZV3DvwP40JAkT1q8fDfo1QV0ZTlQT2W%2F5qLZNaM7Kjr2tgtRZBSBeoVCrKeCdy6OnsntvjOUtho1uJ9Boe3G5UbwALn%2BpqL8s6x2s0d7wYAHmnH%2BXk4vA%2FWwV7xwaqEohHKbiSOcZjBkwi7xNSl%2BJWD6KIYKzEWVEXJixjttDdu3fZgivOJZCwOWuErlHEVgk82RdDlq13NyY5onOqA1q9ZV7JdMe1aGssAjOxCd5PEO886rkUU0iKnEfZ6AhPfgUtxgbT35U1X8wmbdms%2BDmEmV9kVFsJUoZboaZU30OP8cWdyrXj0CMFzT1rP9jpyDzwEqa0yWQ8iy3dqznepCv5jEYMcp3UObEXbXHGS5RNbmw2a%2FS1sRPmgAufayXD2zmYEminFxGKNueGrEtDZXu9PZFDAVXcLJgPeAxCize2Tw5pjvmeLT1U%2FGNuYk9JTAUtkJ%2BmPclvqOdU1OBqcCeWJF9bgZjJvZblODCXpfe8BjqkARPNGgvEImjzcUnjUT5k1OaVCb0soGk8bK9YxjU5DdTbzqDFYACP3ZqI4IHE%2BNsZDPI1NJW7sLEG8jZRE%2Bfm%2FHnBKZjJsdZ29IQ08gHE8Vu9NtUm8GnszcshTeIO9C89j0wk9Me7SUhcqylcYPq0cOdrF4yjAllVhOoIKzzdfe8kj4tZWwM6FJsIpQrjjkr4l4xRK6IbPOhMP1GC3FbWMjXYBZaa&X-Amz-Signature=4d1221ecd7388854f242976ed4cd5ed7ed5a2140cf7c0f3ac47d1d7a73958783&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 3. Histogram
A histogram is an important visual representation of data in categorical form. To view the data in a "Binned" form, use the histogram plot with a number of bins required or with the data points that mark the bin edges. The x-axis represents the data bins, and the y-axis represents the number of elements in each bin.
**Syntax:**
```python
plt.hist(x, bins)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/24e4424a-df87-40a1-b63b-195cbdc2e0ab/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667DNMW45L%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T091431Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDNcEVT8iilgNTSVEjPhksFeyBvlm5oHdta83T08YlaYQIhANspQzr4ylCWPTu9RgTOc7UHdB76bcBoZ6mTrrpDMWgeKogECNH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igzl7bym4QkhHnegVYsq3APbjFIvchb9T763qFSCKiBd7RfDi1Q1FV1F4E%2Fa1JXjFG0bzLfjvr4B2E6HXAcw9KpDNWELnMaRdwJj23WkpzaGYwjZU%2FWH0GT8guni%2BVhXmhitQtyY%2FpfKfLhJZq%2BXk8YqoPiz0za%2BYofm13gSoTJfrvZV3DvwP40JAkT1q8fDfo1QV0ZTlQT2W%2F5qLZNaM7Kjr2tgtRZBSBeoVCrKeCdy6OnsntvjOUtho1uJ9Boe3G5UbwALn%2BpqL8s6x2s0d7wYAHmnH%2BXk4vA%2FWwV7xwaqEohHKbiSOcZjBkwi7xNSl%2BJWD6KIYKzEWVEXJixjttDdu3fZgivOJZCwOWuErlHEVgk82RdDlq13NyY5onOqA1q9ZV7JdMe1aGssAjOxCd5PEO886rkUU0iKnEfZ6AhPfgUtxgbT35U1X8wmbdms%2BDmEmV9kVFsJUoZboaZU30OP8cWdyrXj0CMFzT1rP9jpyDzwEqa0yWQ8iy3dqznepCv5jEYMcp3UObEXbXHGS5RNbmw2a%2FS1sRPmgAufayXD2zmYEminFxGKNueGrEtDZXu9PZFDAVXcLJgPeAxCize2Tw5pjvmeLT1U%2FGNuYk9JTAUtkJ%2BmPclvqOdU1OBqcCeWJF9bgZjJvZblODCXpfe8BjqkARPNGgvEImjzcUnjUT5k1OaVCb0soGk8bK9YxjU5DdTbzqDFYACP3ZqI4IHE%2BNsZDPI1NJW7sLEG8jZRE%2Bfm%2FHnBKZjJsdZ29IQ08gHE8Vu9NtUm8GnszcshTeIO9C89j0wk9Me7SUhcqylcYPq0cOdrF4yjAllVhOoIKzzdfe8kj4tZWwM6FJsIpQrjjkr4l4xRK6IbPOhMP1GC3FbWMjXYBZaa&X-Amz-Signature=8981728ca1dbcd7ba6c91f0e98ca5353cfb96f08ecd9cab7709af9baee8f1f5d&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ab5a6dfe-51f5-43ee-bcb3-33dae4a1c7ad/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667DNMW45L%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T091431Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDNcEVT8iilgNTSVEjPhksFeyBvlm5oHdta83T08YlaYQIhANspQzr4ylCWPTu9RgTOc7UHdB76bcBoZ6mTrrpDMWgeKogECNH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igzl7bym4QkhHnegVYsq3APbjFIvchb9T763qFSCKiBd7RfDi1Q1FV1F4E%2Fa1JXjFG0bzLfjvr4B2E6HXAcw9KpDNWELnMaRdwJj23WkpzaGYwjZU%2FWH0GT8guni%2BVhXmhitQtyY%2FpfKfLhJZq%2BXk8YqoPiz0za%2BYofm13gSoTJfrvZV3DvwP40JAkT1q8fDfo1QV0ZTlQT2W%2F5qLZNaM7Kjr2tgtRZBSBeoVCrKeCdy6OnsntvjOUtho1uJ9Boe3G5UbwALn%2BpqL8s6x2s0d7wYAHmnH%2BXk4vA%2FWwV7xwaqEohHKbiSOcZjBkwi7xNSl%2BJWD6KIYKzEWVEXJixjttDdu3fZgivOJZCwOWuErlHEVgk82RdDlq13NyY5onOqA1q9ZV7JdMe1aGssAjOxCd5PEO886rkUU0iKnEfZ6AhPfgUtxgbT35U1X8wmbdms%2BDmEmV9kVFsJUoZboaZU30OP8cWdyrXj0CMFzT1rP9jpyDzwEqa0yWQ8iy3dqznepCv5jEYMcp3UObEXbXHGS5RNbmw2a%2FS1sRPmgAufayXD2zmYEminFxGKNueGrEtDZXu9PZFDAVXcLJgPeAxCize2Tw5pjvmeLT1U%2FGNuYk9JTAUtkJ%2BmPclvqOdU1OBqcCeWJF9bgZjJvZblODCXpfe8BjqkARPNGgvEImjzcUnjUT5k1OaVCb0soGk8bK9YxjU5DdTbzqDFYACP3ZqI4IHE%2BNsZDPI1NJW7sLEG8jZRE%2Bfm%2FHnBKZjJsdZ29IQ08gHE8Vu9NtUm8GnszcshTeIO9C89j0wk9Me7SUhcqylcYPq0cOdrF4yjAllVhOoIKzzdfe8kj4tZWwM6FJsIpQrjjkr4l4xRK6IbPOhMP1GC3FbWMjXYBZaa&X-Amz-Signature=3e5adc9e344f15c9c880480c1a5f236cce0c838869cadfda2890cea90dc30bc3&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8f1b1d60-cf1b-42b3-9faa-f634c89c3f84/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667DNMW45L%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T091431Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDNcEVT8iilgNTSVEjPhksFeyBvlm5oHdta83T08YlaYQIhANspQzr4ylCWPTu9RgTOc7UHdB76bcBoZ6mTrrpDMWgeKogECNH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igzl7bym4QkhHnegVYsq3APbjFIvchb9T763qFSCKiBd7RfDi1Q1FV1F4E%2Fa1JXjFG0bzLfjvr4B2E6HXAcw9KpDNWELnMaRdwJj23WkpzaGYwjZU%2FWH0GT8guni%2BVhXmhitQtyY%2FpfKfLhJZq%2BXk8YqoPiz0za%2BYofm13gSoTJfrvZV3DvwP40JAkT1q8fDfo1QV0ZTlQT2W%2F5qLZNaM7Kjr2tgtRZBSBeoVCrKeCdy6OnsntvjOUtho1uJ9Boe3G5UbwALn%2BpqL8s6x2s0d7wYAHmnH%2BXk4vA%2FWwV7xwaqEohHKbiSOcZjBkwi7xNSl%2BJWD6KIYKzEWVEXJixjttDdu3fZgivOJZCwOWuErlHEVgk82RdDlq13NyY5onOqA1q9ZV7JdMe1aGssAjOxCd5PEO886rkUU0iKnEfZ6AhPfgUtxgbT35U1X8wmbdms%2BDmEmV9kVFsJUoZboaZU30OP8cWdyrXj0CMFzT1rP9jpyDzwEqa0yWQ8iy3dqznepCv5jEYMcp3UObEXbXHGS5RNbmw2a%2FS1sRPmgAufayXD2zmYEminFxGKNueGrEtDZXu9PZFDAVXcLJgPeAxCize2Tw5pjvmeLT1U%2FGNuYk9JTAUtkJ%2BmPclvqOdU1OBqcCeWJF9bgZjJvZblODCXpfe8BjqkARPNGgvEImjzcUnjUT5k1OaVCb0soGk8bK9YxjU5DdTbzqDFYACP3ZqI4IHE%2BNsZDPI1NJW7sLEG8jZRE%2Bfm%2FHnBKZjJsdZ29IQ08gHE8Vu9NtUm8GnszcshTeIO9C89j0wk9Me7SUhcqylcYPq0cOdrF4yjAllVhOoIKzzdfe8kj4tZWwM6FJsIpQrjjkr4l4xRK6IbPOhMP1GC3FbWMjXYBZaa&X-Amz-Signature=66830587088671551cbbd7fb3a1a430faf80e937428545c06154ca659d590545&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/13ad0497-05fe-4eaa-984e-707b33e14761/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667DNMW45L%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T091431Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDNcEVT8iilgNTSVEjPhksFeyBvlm5oHdta83T08YlaYQIhANspQzr4ylCWPTu9RgTOc7UHdB76bcBoZ6mTrrpDMWgeKogECNH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igzl7bym4QkhHnegVYsq3APbjFIvchb9T763qFSCKiBd7RfDi1Q1FV1F4E%2Fa1JXjFG0bzLfjvr4B2E6HXAcw9KpDNWELnMaRdwJj23WkpzaGYwjZU%2FWH0GT8guni%2BVhXmhitQtyY%2FpfKfLhJZq%2BXk8YqoPiz0za%2BYofm13gSoTJfrvZV3DvwP40JAkT1q8fDfo1QV0ZTlQT2W%2F5qLZNaM7Kjr2tgtRZBSBeoVCrKeCdy6OnsntvjOUtho1uJ9Boe3G5UbwALn%2BpqL8s6x2s0d7wYAHmnH%2BXk4vA%2FWwV7xwaqEohHKbiSOcZjBkwi7xNSl%2BJWD6KIYKzEWVEXJixjttDdu3fZgivOJZCwOWuErlHEVgk82RdDlq13NyY5onOqA1q9ZV7JdMe1aGssAjOxCd5PEO886rkUU0iKnEfZ6AhPfgUtxgbT35U1X8wmbdms%2BDmEmV9kVFsJUoZboaZU30OP8cWdyrXj0CMFzT1rP9jpyDzwEqa0yWQ8iy3dqznepCv5jEYMcp3UObEXbXHGS5RNbmw2a%2FS1sRPmgAufayXD2zmYEminFxGKNueGrEtDZXu9PZFDAVXcLJgPeAxCize2Tw5pjvmeLT1U%2FGNuYk9JTAUtkJ%2BmPclvqOdU1OBqcCeWJF9bgZjJvZblODCXpfe8BjqkARPNGgvEImjzcUnjUT5k1OaVCb0soGk8bK9YxjU5DdTbzqDFYACP3ZqI4IHE%2BNsZDPI1NJW7sLEG8jZRE%2Bfm%2FHnBKZjJsdZ29IQ08gHE8Vu9NtUm8GnszcshTeIO9C89j0wk9Me7SUhcqylcYPq0cOdrF4yjAllVhOoIKzzdfe8kj4tZWwM6FJsIpQrjjkr4l4xRK6IbPOhMP1GC3FbWMjXYBZaa&X-Amz-Signature=4a219ac739fa0272b273f9fabf7b90b5611844583b76f9356e8c7eb841900739&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 2. Box and Whisker Plot
A box plot shows the distribution of quantitative data in a way that facilitates comparisons between variables or across levels of a categorical variable. The box shows the quartiles of the dataset while the whiskers extend to show the rest of the distribution, except for points that are determined to be "outliers".
**Syntax:**
```python
sns.boxplot(x='header_1', y='header_2', data=df)
```
**Example Output:**


![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d207ae92-0a7c-4e2f-aa65-0ee5a2c33bf7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46655XWWCM6%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T091433Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAENIJISA8vlatDdjbobq7MmZjLneNXMgPGrpaIrJKQIAiEA00EE0LA%2FdgbcnjZUcGJJ4uRikuLMXR%2BksMEBZvtlIFcqiAQI0f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDK9NSOZBUcAMiTzZWSrcAyeqRf%2F%2B8RbPSVlPUfaV7WdrBgFtYHpjLLYCWKRzF%2B9b3eFVtRhrq2mYPYvCVzMX5GEK0srId8dBnGdGmsyEe%2FOBcI4Aga7U6wWeGBfakbdWPt9ttABBG7QVXXZsI3Z9jSI%2FLQPOEYfyMYFTHt8NSBMCVNMdmD8dEcZCl3LjsXev4EST9uE6rBcdWkX4R1KCpBrm3aePR0Dhk56II8iQda9ZafE7ieDlTZzpPt5Tu7CZVYas1%2BY46y2hOLUdSzcBQfn7LPniWrN%2FKWYQ2iGVQAiKZbGPhbrvdG2O6YGd2nfTochh0IfpDL5NINKhHORcBj0Ig0rK7%2BJx8Lh970LnQE5WX0NQEPUeEAKvNEybaoxSYLeGpE0YntOzd3SwrkABz4Bn400j%2FDQ5vSHq%2BcgVKjs7dYO3uyZV4TsHl7vUylu0JdPPbOTdmaYFJwFBOixVTVrWYdc15aDnplKP5UnwjbCZWINSVuV0k8JE4DPZLOYTBn2A3A2durfEjxFoqv34svCYgisU%2B23swVgGdKECuoHwNJwV%2B3qmXmRS%2B7eEl%2BVt7yhcQsUuUIKnIyItsOL9lfjT3ZVZUGpPhZl19YGqSE3BSbPs1fkMQIl8k7hYq87cbHllZnu%2FP49l454TMPek97wGOqUBJMYKRdNxHFonGI2TluZh4ImY5VDXXcyU9xtVkej%2BnJYt5opJOCt0IPcJ7aBMM2JfG6Tt7r%2BL%2BE2yswxOdcuOOCDZfdC58giiIyqGVdbY4zpyfqBlZ0mGhM0POxl6vHkpzgAaz%2B8Su2GGsA3Ja%2Fc4wETJ0pug8QjRVopJC%2FntvXR8vZrfDBov84bXRIzW0ZNX%2Fw2%2B5f1VUpRtkFPO9GaNi486oV0q&X-Amz-Signature=f234e17cecc72797aef4f06fe9b29b9e124b9cefdd397ef299762f01e2e482b2&X-Amz-SignedHeaders=host&x-id=GetObject)

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0e516edc-7551-4792-ab18-0494db3c4c0c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UUUV2QSV%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T091433Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIE42nH8Ch49yOygFvnaubbtfLxAgB2w7cExubq40RC3EAiEAnLqJdVl3iKxBgzgCjyzHunMivbhv%2BqGy%2BxIfyDWu66oqiAQI0f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJ8qCUhyzYj70g8wQircA6jYkn6wpE1WYGhx0xrHKYvFVFD9s0ASKfUKuAEx33mfNF77ot%2BPEWtt69F7BSJieSKUDuFrHEdsisk10D0gDb1ToWm5zmrZf3yYX%2FtnZnVmDwEVdCNMmGRI1LZGfFjxxPHd8rYDGdCh8QiB6Y5zAWoqkuT3QyhPURujI9JRrk8BZIxZvH61idg2d8rJfTC4Bgpqt8%2FqmgMR22IoH5Z%2Bb1FTmMBYGvhO9noAQNWZEIr7eukPdxDPHtEXM03kD%2BlENUUJ8m1B5sCToupJOIyvtDDOO%2B7W%2FiWZ7u7BALmHYG1xEFwT%2FjG%2BbXLzj0dXWtKPNkAUfiOCgXDuitodFElTdcSWjVIZ7zG67bdoq5fQ6Zrd4eT5YenH3iqKraXyZoNi59ZNCLM0Hh9Va%2Fa2E5qm%2FVDg40SVvgVNVrDmz7WLo4CQtJshv1WckmttMzGjluIgIVUms%2BBtGswq0%2FU%2B9FQ63pywMmlTMcaj4vue%2FYiyt2fSaxC9p0YhifVOX10wULJT3ae1YgVwtgWQzEJhpKlwOpbNjFa9O9gRufQp%2F%2FH5pxBJHx9PTLXbS9grG0zXxk95Abrw1ISlZPnCNrmO9v9XBOXlh9JYF74R4KvBKkDLD8ik6xvMgW9W6J894WEgMOak97wGOqUBJJhjLrp8VH0x%2BfLAErBcAj0POo6%2BOegn2OxOutk1VjHeQTBxsqJuMMvSoLv7QjehLqjDBjVzdtg2v3v150LXpLXJHdA1dj90oIZfYptdmhf74j3dqhkG7AX26J6c08%2BqOW%2BkESI56P4qnh5PF5%2BJPL48Kll1WfLnzNv8l%2FDfKrmqU9ZbsAdR7P%2FC58pkbipzliyWuYqJceGiCZQR8mnqXSb%2BUHMf&X-Amz-Signature=199dc1ba45087e63e30e0ff23302a044a149455a1fef9cb5d812b76400efb4cb&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23a79b9d-2356-49a9-8fd9-65c6b0ab2cc5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667DNMW45L%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T091431Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDNcEVT8iilgNTSVEjPhksFeyBvlm5oHdta83T08YlaYQIhANspQzr4ylCWPTu9RgTOc7UHdB76bcBoZ6mTrrpDMWgeKogECNH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igzl7bym4QkhHnegVYsq3APbjFIvchb9T763qFSCKiBd7RfDi1Q1FV1F4E%2Fa1JXjFG0bzLfjvr4B2E6HXAcw9KpDNWELnMaRdwJj23WkpzaGYwjZU%2FWH0GT8guni%2BVhXmhitQtyY%2FpfKfLhJZq%2BXk8YqoPiz0za%2BYofm13gSoTJfrvZV3DvwP40JAkT1q8fDfo1QV0ZTlQT2W%2F5qLZNaM7Kjr2tgtRZBSBeoVCrKeCdy6OnsntvjOUtho1uJ9Boe3G5UbwALn%2BpqL8s6x2s0d7wYAHmnH%2BXk4vA%2FWwV7xwaqEohHKbiSOcZjBkwi7xNSl%2BJWD6KIYKzEWVEXJixjttDdu3fZgivOJZCwOWuErlHEVgk82RdDlq13NyY5onOqA1q9ZV7JdMe1aGssAjOxCd5PEO886rkUU0iKnEfZ6AhPfgUtxgbT35U1X8wmbdms%2BDmEmV9kVFsJUoZboaZU30OP8cWdyrXj0CMFzT1rP9jpyDzwEqa0yWQ8iy3dqznepCv5jEYMcp3UObEXbXHGS5RNbmw2a%2FS1sRPmgAufayXD2zmYEminFxGKNueGrEtDZXu9PZFDAVXcLJgPeAxCize2Tw5pjvmeLT1U%2FGNuYk9JTAUtkJ%2BmPclvqOdU1OBqcCeWJF9bgZjJvZblODCXpfe8BjqkARPNGgvEImjzcUnjUT5k1OaVCb0soGk8bK9YxjU5DdTbzqDFYACP3ZqI4IHE%2BNsZDPI1NJW7sLEG8jZRE%2Bfm%2FHnBKZjJsdZ29IQ08gHE8Vu9NtUm8GnszcshTeIO9C89j0wk9Me7SUhcqylcYPq0cOdrF4yjAllVhOoIKzzdfe8kj4tZWwM6FJsIpQrjjkr4l4xRK6IbPOhMP1GC3FbWMjXYBZaa&X-Amz-Signature=09660ff85abfed5f3ca5edb97a4b1447121b3a1fd1d5b37e0c9763b3aa378642&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 4. KDE Plot
A Kernel Density Estimate (KDE) plot is a graph that creates a probability distribution curve for the data based upon its likelihood of occurrence on a specific value. This is created for a single vector of information.
**Syntax:**
```python
sns.kdeplot(X) || sns.kdeplot(df['age'])
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0d571213-2a2f-4921-a50b-880847aa05ee/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667DNMW45L%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T091431Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDNcEVT8iilgNTSVEjPhksFeyBvlm5oHdta83T08YlaYQIhANspQzr4ylCWPTu9RgTOc7UHdB76bcBoZ6mTrrpDMWgeKogECNH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igzl7bym4QkhHnegVYsq3APbjFIvchb9T763qFSCKiBd7RfDi1Q1FV1F4E%2Fa1JXjFG0bzLfjvr4B2E6HXAcw9KpDNWELnMaRdwJj23WkpzaGYwjZU%2FWH0GT8guni%2BVhXmhitQtyY%2FpfKfLhJZq%2BXk8YqoPiz0za%2BYofm13gSoTJfrvZV3DvwP40JAkT1q8fDfo1QV0ZTlQT2W%2F5qLZNaM7Kjr2tgtRZBSBeoVCrKeCdy6OnsntvjOUtho1uJ9Boe3G5UbwALn%2BpqL8s6x2s0d7wYAHmnH%2BXk4vA%2FWwV7xwaqEohHKbiSOcZjBkwi7xNSl%2BJWD6KIYKzEWVEXJixjttDdu3fZgivOJZCwOWuErlHEVgk82RdDlq13NyY5onOqA1q9ZV7JdMe1aGssAjOxCd5PEO886rkUU0iKnEfZ6AhPfgUtxgbT35U1X8wmbdms%2BDmEmV9kVFsJUoZboaZU30OP8cWdyrXj0CMFzT1rP9jpyDzwEqa0yWQ8iy3dqznepCv5jEYMcp3UObEXbXHGS5RNbmw2a%2FS1sRPmgAufayXD2zmYEminFxGKNueGrEtDZXu9PZFDAVXcLJgPeAxCize2Tw5pjvmeLT1U%2FGNuYk9JTAUtkJ%2BmPclvqOdU1OBqcCeWJF9bgZjJvZblODCXpfe8BjqkARPNGgvEImjzcUnjUT5k1OaVCb0soGk8bK9YxjU5DdTbzqDFYACP3ZqI4IHE%2BNsZDPI1NJW7sLEG8jZRE%2Bfm%2FHnBKZjJsdZ29IQ08gHE8Vu9NtUm8GnszcshTeIO9C89j0wk9Me7SUhcqylcYPq0cOdrF4yjAllVhOoIKzzdfe8kj4tZWwM6FJsIpQrjjkr4l4xRK6IbPOhMP1GC3FbWMjXYBZaa&X-Amz-Signature=0e83c3d389c0db6373ad552241c5e1e77de87601bfd5cb466c5c7f3e2cd20353&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/53752550-ef82-4ca9-a01a-09921f0282d0/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667DNMW45L%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T091431Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDNcEVT8iilgNTSVEjPhksFeyBvlm5oHdta83T08YlaYQIhANspQzr4ylCWPTu9RgTOc7UHdB76bcBoZ6mTrrpDMWgeKogECNH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igzl7bym4QkhHnegVYsq3APbjFIvchb9T763qFSCKiBd7RfDi1Q1FV1F4E%2Fa1JXjFG0bzLfjvr4B2E6HXAcw9KpDNWELnMaRdwJj23WkpzaGYwjZU%2FWH0GT8guni%2BVhXmhitQtyY%2FpfKfLhJZq%2BXk8YqoPiz0za%2BYofm13gSoTJfrvZV3DvwP40JAkT1q8fDfo1QV0ZTlQT2W%2F5qLZNaM7Kjr2tgtRZBSBeoVCrKeCdy6OnsntvjOUtho1uJ9Boe3G5UbwALn%2BpqL8s6x2s0d7wYAHmnH%2BXk4vA%2FWwV7xwaqEohHKbiSOcZjBkwi7xNSl%2BJWD6KIYKzEWVEXJixjttDdu3fZgivOJZCwOWuErlHEVgk82RdDlq13NyY5onOqA1q9ZV7JdMe1aGssAjOxCd5PEO886rkUU0iKnEfZ6AhPfgUtxgbT35U1X8wmbdms%2BDmEmV9kVFsJUoZboaZU30OP8cWdyrXj0CMFzT1rP9jpyDzwEqa0yWQ8iy3dqznepCv5jEYMcp3UObEXbXHGS5RNbmw2a%2FS1sRPmgAufayXD2zmYEminFxGKNueGrEtDZXu9PZFDAVXcLJgPeAxCize2Tw5pjvmeLT1U%2FGNuYk9JTAUtkJ%2BmPclvqOdU1OBqcCeWJF9bgZjJvZblODCXpfe8BjqkARPNGgvEImjzcUnjUT5k1OaVCb0soGk8bK9YxjU5DdTbzqDFYACP3ZqI4IHE%2BNsZDPI1NJW7sLEG8jZRE%2Bfm%2FHnBKZjJsdZ29IQ08gHE8Vu9NtUm8GnszcshTeIO9C89j0wk9Me7SUhcqylcYPq0cOdrF4yjAllVhOoIKzzdfe8kj4tZWwM6FJsIpQrjjkr4l4xRK6IbPOhMP1GC3FbWMjXYBZaa&X-Amz-Signature=b5152f3583f063816a10ae1eae5c81467d976694c6bd89d94c4101318fe12405&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
## 4. Correlation Between Variables
Correlation is a statistical measure of the extent to which different variables are interdependent. It indicates how changes in one variable are associated with changes in another variable over time.
### Positive Correlation
Positive correlation indicates that as one variable increases, the other variable also tends to increase.
**Example: Engine Size and Price**
- **Positive Correlation:** Engine size increases, price also increases.
- **Visualization:** Scatter plot with a steep positive slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c7ea9b0-3ef3-4357-a9c3-554fc71b6b15/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664C7VQN75%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T091433Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIDgouWrAuaqb7ihhrKB9%2B0IYysBpYDEqxtbZVTzsgmuIAiABVDwvTS01LLhxdnSt0DJCBDdAXAPyC%2Fdr%2BPO1CbSqWSqIBAjR%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMBdVDFn6n5MXCuQJJKtwDFrz12HicWXlacBV1BbpA9ekwRWqfPH6yZCCvdjXjUncDTjCbRTGiftZ27AkJ0A5jsvhM%2B6VESdJoCYSF%2BEFPUIiiQh3ZwGnKPanWi3hl%2F2f24pYNL30qDBMZnpoq78qgPgQNGGFcY5JTN9OyjZxfOkRORWeqtbecb3KPFwTxeStlffMLbGJ96B%2FQNHNA%2B6ul4p1AHFhXRPR0VBhTTdJ3PppeIWjyOiTRRLUO5xKBKY3Y%2F3XzB%2BMAzLyR%2BMw8Owz2GG%2BrJ091%2FtUgfpoP%2FM382RpMk4EZlbURWzoNIjFhYlP67Bx%2Bweqjl6dNaXsJ3kOLiO5qdM6OND8k%2B%2Bz9E3KRCiavP%2FNbfSApGbYa6zntLiRxLTrR4csETxmRpuPLpt3eSt%2B%2B8McqkX3lIx5MYXCSXo0Gs0VzqdRUDYIgy3XN2rwXISkfb%2B%2BkOPYzo%2BqslTkkQWvSdKw%2FvMzBdhiZb3V4O%2FxqXRv8QY3iDLttzDxOlxzM69d9vOJftcoAle%2FqiH7ewk3cfvafoCTZUZ3xF%2BSD84BbW2P%2BL5vcZ75EGKG24C3JxkD%2F5McH%2F43E89tRQbId8DeK30CldH1JOLF5hN4ySgpdDcGDjlLZ4Xv%2F7%2BRobcbX%2FW3TyOldxxuwgdgw1KT3vAY6pgF55saK%2Fwqr6rvwIYi9vzepLtK4eyP96YaOGCJMWZq3wOSGko8fGu3LSBQwvHjE7%2BrtKyLHdNwHVFfnMBkLbALpw6JT53H9zhpsGG%2FTWxDhpqUMHu0wxjlU0nyxLKqbLGT6OVvUi10TsLYFa45gMjXGAlvrNW6V7KSb0YOLLI1zZRRb2xZOyJJ3kh9XwGTgWgiOiwwal65edGKrkyGADu6JRQS4%2BUgU&X-Amz-Signature=e5c21dbde8d41903ee8dc5af7b47a399051b1faa370e8a1214038e7a0ff2e433&X-Amz-SignedHeaders=host&x-id=GetObject)
**Explanation:** When engine size increases, there is a corresponding increase in the price of the vehicle. This positive correlation suggests that larger engines tend to be associated with higher prices in the market.
___
### Negative Correlation
Negative correlation indicates that as one variable increases, the other variable tends to decrease.
**Example: Highway Miles per Gallon and Price**
- **Negative Correlation:** As highway miles per gallon increases, price decreases.
- **Visualization:** Scatter plot with a steep negative slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/10f1f798-9cc4-4df2-a9c1-5a339f554a0b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664J5P5RMS%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T091434Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIAk2OMBP3K3nwONE4XhQ9ILXAt9njN%2BiYiejsipf44WsAiAouRX%2BYsCm814LxI8NVysUenKIvuixn2fiT87Qi3miJSqIBAjR%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMuMz8mBmLb9BIJTqPKtwDEHUBFN6NiSQwFXGAcEaasTxn1AS3MU26K2fO0lpFbtws1nuGeM%2B%2B6K8jLkmPmfdRFbpo0%2B5cB2xUWETis6LlblLNdvRRzx6JrEx7xBTDPGxuuchFZXVcr0dZStM7kFx5xU6GufVxGylmHP0RYcr%2BFt65gcarpXg0cit9IdM7pUIdC1e3RLnZ2Ysma%2Byjy5rHOxscdzAgteW7H3i%2Fh8S7QSAkZtqj9%2F8T0ui6XAJez%2BZ4Fh61YSHyipoGQ6qmd5EvAIC6yONhLa79st2%2FWHY4oFhsJpYvbN%2BQ%2FBKCK18AuJ1Ta1WC1OmTdsa8rlMiUg%2FqzDkYaJw6qJ6AVTRSeOEw2Ho8VAkFapM3lP1%2Bvl4i8c4ShUrv%2F%2BJO3MgJlV22zwdNlsG8dUTdwLB2nSf6%2BnJv%2BJwGz%2FKeh8do7Hyic%2Fy0g9ZirPdfAXxR28o7zIxfK1dk7Z6qdM2U83mO4od95pKinwV9%2BW9EPM2HV6d%2BJubqNtx2J2dfFVnBpB5HFPlbax1Y3wCxQ3zbCNoWhY53DrQiRIyRNVNBF%2FVdoQfWcPvzdxNR6V9%2BaU9nk3LIMcyEYdi%2F0b3TwKct4IS5ls67Mvyg%2FZrMCUlA%2Bcs9jONaQWPgSQCUbNa9QjfMsJye1f0wqaT3vAY6pgEZWIlv%2Fptjy2tz9e46SArNBu2L2enlYMwWb31dKT3%2FS1QURwbPr9IzAbggyoKvweFuGPKFesqheMW22NQDyP%2FJ4QZDCEEwNgqeVrLYiZjlcBC1j%2BibKcm0lVkgWgFz53dRNlEh75a7MKiNZ5%2Bm%2FqQewjmwOi1251CJyCRXxSXU2SQq8zeOunNAXTveN2ukfHLb%2Bvx6z1W%2Fthhrz9uwhYULtxpzGJkI&X-Amz-Signature=e38478f48e1fe4a9f2503198814cdf0eea2831326177258764554d645a1f674b&X-Amz-SignedHeaders=host&x-id=GetObject)
**Explanation:** When highway miles per gallon increases, the price of the vehicle tends to decrease. This negative correlation suggests that cars with higher fuel efficiency (more miles per gallon) are generally priced lower in the market.
___
### Weak Correlation
Weak correlation indicates a lack of strong relationship between the variables.
**Example: RPM and Price**
- **Weak Correlation:** Low and high RPM values show varied prices, indicating no strong predictive relationship.
- **Visualization:** Scatter plot with no clear trend or slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9f914514-8914-4bf4-ac84-d9e3077f6eb1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZZU3K5ML%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T091433Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQC6KD%2Fw39L%2Bkdb6%2BMa%2BoU6ActbWx6Ad45R3HhewJMILgwIgXxzMOFHrG7Qns5J7dTgPk0svhwmuyZfESdxFn6VR9NEqiAQI0f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDCug61jkPtMNXz3DRCrcA28zK8iEQpQYQe4QN92VFhQtyYJcQR3firWZjoABzXWuvZAiRJinHOO9d9Jt4%2BNqqCec3josDv9Ml0r36JHJDOVaVd3fmapOjMiPgIqlxKbctyystvBggh821bo4BkykMVG1xneN0U727Y5%2B7sWbIBt0nKS2dbIpjjumepovyN3VdK683drab%2FzqR1KYvqcLrkQmPITDwMqYT8WD6zeMUctkZLe2XHJClMYQTIIARBfcJKOkjx4QkMXv%2BaI%2FzlNGMv68CwoDU8p332vcI40iCxH%2FaWqT0NiCL5o8uw9v2M1ZCeyOCQzh0L8TL6NWxxA95nd00rg1kQHwE4VlstZXdWAtSHbVJvKlW2iYz%2BWL976gofNN3R%2BhOB%2Ba%2BfVCZAeofREuadNO6tQFkrT3wQEaw9sAb79uKw5dKOkX6J6vW4KTEnhLjGlsCzOUVbtBUNZBNaqRNFI9sLlAuFbjdk4nIAIKTW%2B7ZUJPKeX%2FL7UfmJcIdZzs2Z2Fb0LxK6lDsT%2BpbvW6jE2g331%2BRf8ex3xrx2spkjVoLLt62QpPJRCCldYw1YLep1tqkGARkLX5mdXSkCva4%2Bbj14yBG20OXKfEO%2FYSuLogzFxuDnKEfeGAMATfLs54Yzoxnp4b%2Bd1qMPCk97wGOqUBhfl%2BITRGz%2FESRbvmdMDq1DV3KTRbWBamRuGBRew0UxvXcu8n3f8G93dLgw2BlfnV8YgXLfzWG4v1H1rdya3%2F1Fk2B8s%2B9QiQCv50W1xy6mkYYgK61ZmImqk74sHbNL9Qen6SU8Nc0G2UzBRkSzSVV6Hhjte3OdYiJ4ExKrKSnF8mmuA7dKDTsSCV4tnb7AYqF4cPAhq%2FUb0D%2FrXD4kXmYfNUAZJb&X-Amz-Signature=3a366f48727725ce0566fbb11a0e5bcee5a7fc5a23239c72923cd30f356fe4e0&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f18086e5-5b04-4fbf-8309-8944ab20d213/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T3PTEB64%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T091432Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDLtF8p%2BnxHy4zz3zxDFoeQyzPr%2B6l4KyikAmJWByHGJwIgNBKAXDmDhILfBuVhHeqyDFJSHo7VYPmAJwYONCQpY38qiAQI0f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDun%2Fk%2Fw89dffs3QGCrcA3yjh1zaJ6tSVZcSIJoXSmVCo1YZ0di6N0G4vSl6ya04PRinIeA01s5%2F3msRleZ19hfN6%2F5hx2EC1tbsG54vRWgjKGGqrdqaqTYb0saRSru0PPRRqHjPJaUH8xBGYftsR5vib7xn6wLzWInbV9vXlbFljBrJXLlv%2B%2FPMsAQJ7FA7GAKJR%2Bjf3vVKrg3QvVy5tPD7%2B4i5HB0ZQ4HoskiS4WHNpEi9%2FGl7aidKyK3XgKffGFdaSmZjhhYU58ebBAQ9UaonY8eDfdC9%2BNyquJp8EBn6TykEHcXEciZxWL9PwIZzPcTc5dCK7NH%2F9ojo9BHMlwRL77EVW%2Bzwsq17VDPmMBu2rToZyfGFWDfDFuNKEhTFsny%2BwvoNKu1o3bHkVMRX3jhi05SC%2Fe7wxp9PJ0txDLd98ITA9bxD9vTMj%2BA3NonNS4GbKW9sSerXpBa%2BGdilnoG5i%2BP3Gz8hxnE18OYbzOCLF6kEpPjypvSrsCIlNVCNRX2BwEtkUiQCc3qVzm1Rvn7txdatnH4FEhu%2BHin%2FnDwfREvN53fHvD6jRF%2F9XFAXF3hjMl3GVUPeUhfcfS%2BnFVBS0g%2FxoAyojTyTf1danj1w%2BJCXFsEJ2JGMJ43OZmF7YRZTuFozxzR%2BzSqmMMik97wGOqUBD1g6b0nQbUfjy2yidqIIgfrPGp9Mz%2FCqkPGelFRzjYEkA4cBNy8och%2FySmnnbJ6yl%2FQvMgs0e894NMllYGgOCos3gx10G7etQDS0ArRt%2F0aGrGP0HrvjRrc7SzEw1DBNSXA3LAzHyJuY4sEVV4MVzY00DWLPgC%2BfZcXxmP5SNlPGnBQZX2f3wKzIgb2y%2BdBET%2BRogjm%2F85z87g45fCWCgQNUvkVu&X-Amz-Signature=e3c376bd593dfe5f2b37f99a3ba14521aae64f89117973a055000db9f088d33c&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Correlation Plot
Heatmap visualizes correlations among variables. Color scheme indicates Pearson correlation coefficients. Dark red diagonal line shows perfect correlation (value of 1) between variables and themselves.
This heatmap offers overview of variable relationships and their link with price.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cd3b341e-cc1a-45f7-8aec-cdc00436d270/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T3PTEB64%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T091432Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDLtF8p%2BnxHy4zz3zxDFoeQyzPr%2B6l4KyikAmJWByHGJwIgNBKAXDmDhILfBuVhHeqyDFJSHo7VYPmAJwYONCQpY38qiAQI0f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDun%2Fk%2Fw89dffs3QGCrcA3yjh1zaJ6tSVZcSIJoXSmVCo1YZ0di6N0G4vSl6ya04PRinIeA01s5%2F3msRleZ19hfN6%2F5hx2EC1tbsG54vRWgjKGGqrdqaqTYb0saRSru0PPRRqHjPJaUH8xBGYftsR5vib7xn6wLzWInbV9vXlbFljBrJXLlv%2B%2FPMsAQJ7FA7GAKJR%2Bjf3vVKrg3QvVy5tPD7%2B4i5HB0ZQ4HoskiS4WHNpEi9%2FGl7aidKyK3XgKffGFdaSmZjhhYU58ebBAQ9UaonY8eDfdC9%2BNyquJp8EBn6TykEHcXEciZxWL9PwIZzPcTc5dCK7NH%2F9ojo9BHMlwRL77EVW%2Bzwsq17VDPmMBu2rToZyfGFWDfDFuNKEhTFsny%2BwvoNKu1o3bHkVMRX3jhi05SC%2Fe7wxp9PJ0txDLd98ITA9bxD9vTMj%2BA3NonNS4GbKW9sSerXpBa%2BGdilnoG5i%2BP3Gz8hxnE18OYbzOCLF6kEpPjypvSrsCIlNVCNRX2BwEtkUiQCc3qVzm1Rvn7txdatnH4FEhu%2BHin%2FnDwfREvN53fHvD6jRF%2F9XFAXF3hjMl3GVUPeUhfcfS%2BnFVBS0g%2FxoAyojTyTf1danj1w%2BJCXFsEJ2JGMJ43OZmF7YRZTuFozxzR%2BzSqmMMik97wGOqUBD1g6b0nQbUfjy2yidqIIgfrPGp9Mz%2FCqkPGelFRzjYEkA4cBNy8och%2FySmnnbJ6yl%2FQvMgs0e894NMllYGgOCos3gx10G7etQDS0ArRt%2F0aGrGP0HrvjRrc7SzEw1DBNSXA3LAzHyJuY4sEVV4MVzY00DWLPgC%2BfZcXxmP5SNlPGnBQZX2f3wKzIgb2y%2BdBET%2BRogjm%2F85z87g45fCWCgQNUvkVu&X-Amz-Signature=e8b40376fefc4710440b576d642907585541e4c091773a57a55d1c825f394809&X-Amz-SignedHeaders=host&x-id=GetObject)

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
