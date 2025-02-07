

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7e6d594d-952e-44b6-97ea-31225882aea6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RJX76GSM%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T051429Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFUaCXVzLXdlc3QtMiJIMEYCIQCTO4D63IKH21EtcjOPde8jtvroNdqAhO8R22TL655chgIhAJS7Z6UavzlCqNH3gId%2BJ2sJjFzlqBWtMkmMTRtwSCcRKv8DCG4QABoMNjM3NDIzMTgzODA1Igx1fmoqPLNxBAjxXkQq3ANKS56s1vjdapcFn%2Fszuy8Ja4qu2BbQ1fnD0x4YkKmuHQ8xkLVMOpdWm9lx6bDMFiPhrKINyV%2F%2Bz0jgOzBakHONLHlzMgakxXql52auLg5%2BNPhT9mpFQEu33AiNs5P85QxiowhdC2nGZxledqnJzs2I9l4aKFgk3jRDv2tJOpBk74eByX5EhsMDrnroBTHl8ycx7C5RztzfDf9AyFy2ExpIqER1M24ESba6wsSrTiq02S06nMiKYHQ04aYt4w%2BJGUZYB7syjEmXSRSEYi067ISlvElYAvJy4caZ77SsswuGiNuDDWknTiw%2Fa1yUB5gKmYkg1RaANxpZFqKaDsbKOGtVof1F7Kh0bKcyaqqmT4L8O5%2FN5EUHvmR6AdLvwU2vEAM%2F7zEGoqcmYUM0oBCkmBT0G4%2BgERRoVGfJpqH4nJrE%2FifSftXvD5tvL5hsiUQ2ub2ou2yPJAvg76NQjmFdbJYNG9rKXrMFJ%2FwmblP8A06B2dMB4nUtIa5GMS5vKNpdBB16Hz9vysmBaEDgAwbE0aFc87gHCGZxOcM%2ByBXPoKlfX24SdEunKfcs8JLh%2FCWWvi4Ox3Eiss%2FW6SDZar3hz69y0cN2%2FS%2Byh01BaOu0y9T1fI3E90%2FKudfB9yby5DC8opa9BjqkAfOdqO00V5zbf%2Fs%2FfeWVaIe%2F4yi8pUb6KlDjYLd79QLbcxDSVm8zAlQvDJpjIMixDWayOhihX1gkptlhKcfzUhYjC9ma7xq1NT3WTtb9nMlKir%2B744uXCxyF9oHCdHZ7vDjgWu4fXAMdyqIndppaHlbOBW6xW%2B0Dd8Kb%2F4suhe5KAm%2BSaU6B7D0hNtivZs0d53INr7wqhdfDZHyh4SPUKAnmekVJ&X-Amz-Signature=bbdb6c26896a360f49b450325899ebc904925f671a6fec47eda31b9a79a49147&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cbfaed9e-b398-4902-8936-dea058b21def/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RJX76GSM%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T051429Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFUaCXVzLXdlc3QtMiJIMEYCIQCTO4D63IKH21EtcjOPde8jtvroNdqAhO8R22TL655chgIhAJS7Z6UavzlCqNH3gId%2BJ2sJjFzlqBWtMkmMTRtwSCcRKv8DCG4QABoMNjM3NDIzMTgzODA1Igx1fmoqPLNxBAjxXkQq3ANKS56s1vjdapcFn%2Fszuy8Ja4qu2BbQ1fnD0x4YkKmuHQ8xkLVMOpdWm9lx6bDMFiPhrKINyV%2F%2Bz0jgOzBakHONLHlzMgakxXql52auLg5%2BNPhT9mpFQEu33AiNs5P85QxiowhdC2nGZxledqnJzs2I9l4aKFgk3jRDv2tJOpBk74eByX5EhsMDrnroBTHl8ycx7C5RztzfDf9AyFy2ExpIqER1M24ESba6wsSrTiq02S06nMiKYHQ04aYt4w%2BJGUZYB7syjEmXSRSEYi067ISlvElYAvJy4caZ77SsswuGiNuDDWknTiw%2Fa1yUB5gKmYkg1RaANxpZFqKaDsbKOGtVof1F7Kh0bKcyaqqmT4L8O5%2FN5EUHvmR6AdLvwU2vEAM%2F7zEGoqcmYUM0oBCkmBT0G4%2BgERRoVGfJpqH4nJrE%2FifSftXvD5tvL5hsiUQ2ub2ou2yPJAvg76NQjmFdbJYNG9rKXrMFJ%2FwmblP8A06B2dMB4nUtIa5GMS5vKNpdBB16Hz9vysmBaEDgAwbE0aFc87gHCGZxOcM%2ByBXPoKlfX24SdEunKfcs8JLh%2FCWWvi4Ox3Eiss%2FW6SDZar3hz69y0cN2%2FS%2Byh01BaOu0y9T1fI3E90%2FKudfB9yby5DC8opa9BjqkAfOdqO00V5zbf%2Fs%2FfeWVaIe%2F4yi8pUb6KlDjYLd79QLbcxDSVm8zAlQvDJpjIMixDWayOhihX1gkptlhKcfzUhYjC9ma7xq1NT3WTtb9nMlKir%2B744uXCxyF9oHCdHZ7vDjgWu4fXAMdyqIndppaHlbOBW6xW%2B0Dd8Kb%2F4suhe5KAm%2BSaU6B7D0hNtivZs0d53INr7wqhdfDZHyh4SPUKAnmekVJ&X-Amz-Signature=6a6913e83cb95e33ed7ccbaa1c681c48e4c52525b0edae6e696f2d33fb4da36a&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/91181646-b1e0-4433-9711-6259a96a9247/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RJX76GSM%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T051429Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFUaCXVzLXdlc3QtMiJIMEYCIQCTO4D63IKH21EtcjOPde8jtvroNdqAhO8R22TL655chgIhAJS7Z6UavzlCqNH3gId%2BJ2sJjFzlqBWtMkmMTRtwSCcRKv8DCG4QABoMNjM3NDIzMTgzODA1Igx1fmoqPLNxBAjxXkQq3ANKS56s1vjdapcFn%2Fszuy8Ja4qu2BbQ1fnD0x4YkKmuHQ8xkLVMOpdWm9lx6bDMFiPhrKINyV%2F%2Bz0jgOzBakHONLHlzMgakxXql52auLg5%2BNPhT9mpFQEu33AiNs5P85QxiowhdC2nGZxledqnJzs2I9l4aKFgk3jRDv2tJOpBk74eByX5EhsMDrnroBTHl8ycx7C5RztzfDf9AyFy2ExpIqER1M24ESba6wsSrTiq02S06nMiKYHQ04aYt4w%2BJGUZYB7syjEmXSRSEYi067ISlvElYAvJy4caZ77SsswuGiNuDDWknTiw%2Fa1yUB5gKmYkg1RaANxpZFqKaDsbKOGtVof1F7Kh0bKcyaqqmT4L8O5%2FN5EUHvmR6AdLvwU2vEAM%2F7zEGoqcmYUM0oBCkmBT0G4%2BgERRoVGfJpqH4nJrE%2FifSftXvD5tvL5hsiUQ2ub2ou2yPJAvg76NQjmFdbJYNG9rKXrMFJ%2FwmblP8A06B2dMB4nUtIa5GMS5vKNpdBB16Hz9vysmBaEDgAwbE0aFc87gHCGZxOcM%2ByBXPoKlfX24SdEunKfcs8JLh%2FCWWvi4Ox3Eiss%2FW6SDZar3hz69y0cN2%2FS%2Byh01BaOu0y9T1fI3E90%2FKudfB9yby5DC8opa9BjqkAfOdqO00V5zbf%2Fs%2FfeWVaIe%2F4yi8pUb6KlDjYLd79QLbcxDSVm8zAlQvDJpjIMixDWayOhihX1gkptlhKcfzUhYjC9ma7xq1NT3WTtb9nMlKir%2B744uXCxyF9oHCdHZ7vDjgWu4fXAMdyqIndppaHlbOBW6xW%2B0Dd8Kb%2F4suhe5KAm%2BSaU6B7D0hNtivZs0d53INr7wqhdfDZHyh4SPUKAnmekVJ&X-Amz-Signature=a0e785174dc1556d66460acbd7dd6fad4c7f17ab1cfa42230fef68fc9a6e32f2&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/09aba1c0-0d55-41dd-852a-a04c5b8a3fac/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RVECKNIO%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T051430Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFUaCXVzLXdlc3QtMiJHMEUCIA%2Frvzde%2BFtudBCTf8PKTpGzIj7AjC8IMYJQUyZCI2bEAiEA6uF5N3yXlQdsw%2FDWGt%2FOPCkImpYW87RaUv3sAM6Hmbkq%2FwMIbhAAGgw2Mzc0MjMxODM4MDUiDIDLpGN95IrFlss4lircAzEOr4DCdUfpgXdcPIyNk6S8Vgk9%2FHxdjXdi4PM4nYKUk1K8iOn31HeiOfqyROcdLD0VG1kHQSXO31zl1YCHezJtAlqQYreGS1b1aWa1WeMiJ2D3FrmqShKX3NFqgfy5Z40LxkyqvA05kU%2BKzBCs7H2HHXFVL%2FC8Mm%2Fll2C8LGKCydBWnok%2BG17FCtMN7mu%2FhmdPSMB7C%2Fj1dyNDZ1DpfKRDNS4h3C0HLMGygSdtiGBoIZH9WZODsB9OdSkwEQK%2F1W00kqrkptmaSweS9FyBG07dBUl%2FTA1NCuy2VSCA7AXyiU1KlpKOwyX5tsIKzEQ8Z3oB%2Fal2Crgk2x0xjCKzJj1IEERZSzNNdYzzpvDGPHtsyfsbZwgAd3eD%2BAhGQHOMwGvOf%2B%2FOQ%2F6M4I%2FCmps0nVFgevLvpqBBqsdDg77uvsToHES7ev0YvXcwDySN3CKvZ1UedVURxISaIDroDZAwKlPJ%2Fgsq2TEaE3kWYGreM%2FeGITanTJ5TEvviFjfbyNlY8ozDfaCAOkiTVx4eA4juqoAMC8Fw1tcDkY4aiaTyAvYTt5e694qMN4dAxRBXia8dG5R8FLB0K1ZOKAEfMDumUR07OW9Frsh7ZFDjrIseT0rYipz3NmlAcu41Nrb6MIehlr0GOqUBcOEuYVE%2FfEnRhV3s9jYkrevH5xgNsTQ1DYpztxk9A%2BRy9%2FXqyiEO%2F2HocWCqbvrTir4S9wC1G7WlJgK2U32dp3WdiRkDLXrlsYLQSiFerqo5cv%2FGji7ha3VlXWYJidFCvWgE6MrUxuT73qBAMaPgKM0Bt4vMnL71OHtNHE4oIE186kM3BD%2Bc%2B7RQUvmwtZBO19LMhJiyUzV46HNDvca8qgWwkdbP&X-Amz-Signature=251f068b59fc51ced17eb4a76a8e6db678ce16df8092d85dc575d0c600a76e37&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 2. Scatter Plot
Scatter plots present the relationship between two variables in a dataset. It represents data points on a two-dimensional plane. The independent variable or attribute is plotted on the X-axis, while the dependent variable is plotted on the Y-axis.
**Syntax:**
```python
plt.scatter(x, y)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23708af9-659f-4f23-b626-1a4292d7842c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RVECKNIO%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T051430Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFUaCXVzLXdlc3QtMiJHMEUCIA%2Frvzde%2BFtudBCTf8PKTpGzIj7AjC8IMYJQUyZCI2bEAiEA6uF5N3yXlQdsw%2FDWGt%2FOPCkImpYW87RaUv3sAM6Hmbkq%2FwMIbhAAGgw2Mzc0MjMxODM4MDUiDIDLpGN95IrFlss4lircAzEOr4DCdUfpgXdcPIyNk6S8Vgk9%2FHxdjXdi4PM4nYKUk1K8iOn31HeiOfqyROcdLD0VG1kHQSXO31zl1YCHezJtAlqQYreGS1b1aWa1WeMiJ2D3FrmqShKX3NFqgfy5Z40LxkyqvA05kU%2BKzBCs7H2HHXFVL%2FC8Mm%2Fll2C8LGKCydBWnok%2BG17FCtMN7mu%2FhmdPSMB7C%2Fj1dyNDZ1DpfKRDNS4h3C0HLMGygSdtiGBoIZH9WZODsB9OdSkwEQK%2F1W00kqrkptmaSweS9FyBG07dBUl%2FTA1NCuy2VSCA7AXyiU1KlpKOwyX5tsIKzEQ8Z3oB%2Fal2Crgk2x0xjCKzJj1IEERZSzNNdYzzpvDGPHtsyfsbZwgAd3eD%2BAhGQHOMwGvOf%2B%2FOQ%2F6M4I%2FCmps0nVFgevLvpqBBqsdDg77uvsToHES7ev0YvXcwDySN3CKvZ1UedVURxISaIDroDZAwKlPJ%2Fgsq2TEaE3kWYGreM%2FeGITanTJ5TEvviFjfbyNlY8ozDfaCAOkiTVx4eA4juqoAMC8Fw1tcDkY4aiaTyAvYTt5e694qMN4dAxRBXia8dG5R8FLB0K1ZOKAEfMDumUR07OW9Frsh7ZFDjrIseT0rYipz3NmlAcu41Nrb6MIehlr0GOqUBcOEuYVE%2FfEnRhV3s9jYkrevH5xgNsTQ1DYpztxk9A%2BRy9%2FXqyiEO%2F2HocWCqbvrTir4S9wC1G7WlJgK2U32dp3WdiRkDLXrlsYLQSiFerqo5cv%2FGji7ha3VlXWYJidFCvWgE6MrUxuT73qBAMaPgKM0Bt4vMnL71OHtNHE4oIE186kM3BD%2Bc%2B7RQUvmwtZBO19LMhJiyUzV46HNDvca8qgWwkdbP&X-Amz-Signature=5800a7ead6a0aedef3d4649ab7dff5f315eae0d61a2993a60ce2bd8f072bdf7d&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 3. Histogram
A histogram is an important visual representation of data in categorical form. To view the data in a "Binned" form, use the histogram plot with a number of bins required or with the data points that mark the bin edges. The x-axis represents the data bins, and the y-axis represents the number of elements in each bin.
**Syntax:**
```python
plt.hist(x, bins)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/24e4424a-df87-40a1-b63b-195cbdc2e0ab/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RVECKNIO%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T051430Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFUaCXVzLXdlc3QtMiJHMEUCIA%2Frvzde%2BFtudBCTf8PKTpGzIj7AjC8IMYJQUyZCI2bEAiEA6uF5N3yXlQdsw%2FDWGt%2FOPCkImpYW87RaUv3sAM6Hmbkq%2FwMIbhAAGgw2Mzc0MjMxODM4MDUiDIDLpGN95IrFlss4lircAzEOr4DCdUfpgXdcPIyNk6S8Vgk9%2FHxdjXdi4PM4nYKUk1K8iOn31HeiOfqyROcdLD0VG1kHQSXO31zl1YCHezJtAlqQYreGS1b1aWa1WeMiJ2D3FrmqShKX3NFqgfy5Z40LxkyqvA05kU%2BKzBCs7H2HHXFVL%2FC8Mm%2Fll2C8LGKCydBWnok%2BG17FCtMN7mu%2FhmdPSMB7C%2Fj1dyNDZ1DpfKRDNS4h3C0HLMGygSdtiGBoIZH9WZODsB9OdSkwEQK%2F1W00kqrkptmaSweS9FyBG07dBUl%2FTA1NCuy2VSCA7AXyiU1KlpKOwyX5tsIKzEQ8Z3oB%2Fal2Crgk2x0xjCKzJj1IEERZSzNNdYzzpvDGPHtsyfsbZwgAd3eD%2BAhGQHOMwGvOf%2B%2FOQ%2F6M4I%2FCmps0nVFgevLvpqBBqsdDg77uvsToHES7ev0YvXcwDySN3CKvZ1UedVURxISaIDroDZAwKlPJ%2Fgsq2TEaE3kWYGreM%2FeGITanTJ5TEvviFjfbyNlY8ozDfaCAOkiTVx4eA4juqoAMC8Fw1tcDkY4aiaTyAvYTt5e694qMN4dAxRBXia8dG5R8FLB0K1ZOKAEfMDumUR07OW9Frsh7ZFDjrIseT0rYipz3NmlAcu41Nrb6MIehlr0GOqUBcOEuYVE%2FfEnRhV3s9jYkrevH5xgNsTQ1DYpztxk9A%2BRy9%2FXqyiEO%2F2HocWCqbvrTir4S9wC1G7WlJgK2U32dp3WdiRkDLXrlsYLQSiFerqo5cv%2FGji7ha3VlXWYJidFCvWgE6MrUxuT73qBAMaPgKM0Bt4vMnL71OHtNHE4oIE186kM3BD%2Bc%2B7RQUvmwtZBO19LMhJiyUzV46HNDvca8qgWwkdbP&X-Amz-Signature=9673d886569ba60d8c3966a145779ffe73ee379b1010a7f28143193ee6cb587a&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ab5a6dfe-51f5-43ee-bcb3-33dae4a1c7ad/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RVECKNIO%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T051430Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFUaCXVzLXdlc3QtMiJHMEUCIA%2Frvzde%2BFtudBCTf8PKTpGzIj7AjC8IMYJQUyZCI2bEAiEA6uF5N3yXlQdsw%2FDWGt%2FOPCkImpYW87RaUv3sAM6Hmbkq%2FwMIbhAAGgw2Mzc0MjMxODM4MDUiDIDLpGN95IrFlss4lircAzEOr4DCdUfpgXdcPIyNk6S8Vgk9%2FHxdjXdi4PM4nYKUk1K8iOn31HeiOfqyROcdLD0VG1kHQSXO31zl1YCHezJtAlqQYreGS1b1aWa1WeMiJ2D3FrmqShKX3NFqgfy5Z40LxkyqvA05kU%2BKzBCs7H2HHXFVL%2FC8Mm%2Fll2C8LGKCydBWnok%2BG17FCtMN7mu%2FhmdPSMB7C%2Fj1dyNDZ1DpfKRDNS4h3C0HLMGygSdtiGBoIZH9WZODsB9OdSkwEQK%2F1W00kqrkptmaSweS9FyBG07dBUl%2FTA1NCuy2VSCA7AXyiU1KlpKOwyX5tsIKzEQ8Z3oB%2Fal2Crgk2x0xjCKzJj1IEERZSzNNdYzzpvDGPHtsyfsbZwgAd3eD%2BAhGQHOMwGvOf%2B%2FOQ%2F6M4I%2FCmps0nVFgevLvpqBBqsdDg77uvsToHES7ev0YvXcwDySN3CKvZ1UedVURxISaIDroDZAwKlPJ%2Fgsq2TEaE3kWYGreM%2FeGITanTJ5TEvviFjfbyNlY8ozDfaCAOkiTVx4eA4juqoAMC8Fw1tcDkY4aiaTyAvYTt5e694qMN4dAxRBXia8dG5R8FLB0K1ZOKAEfMDumUR07OW9Frsh7ZFDjrIseT0rYipz3NmlAcu41Nrb6MIehlr0GOqUBcOEuYVE%2FfEnRhV3s9jYkrevH5xgNsTQ1DYpztxk9A%2BRy9%2FXqyiEO%2F2HocWCqbvrTir4S9wC1G7WlJgK2U32dp3WdiRkDLXrlsYLQSiFerqo5cv%2FGji7ha3VlXWYJidFCvWgE6MrUxuT73qBAMaPgKM0Bt4vMnL71OHtNHE4oIE186kM3BD%2Bc%2B7RQUvmwtZBO19LMhJiyUzV46HNDvca8qgWwkdbP&X-Amz-Signature=552cc331eff05ecdf3f85544278cf56aef9357d382c457eb5c420fadab7407d9&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8f1b1d60-cf1b-42b3-9faa-f634c89c3f84/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RVECKNIO%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T051430Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFUaCXVzLXdlc3QtMiJHMEUCIA%2Frvzde%2BFtudBCTf8PKTpGzIj7AjC8IMYJQUyZCI2bEAiEA6uF5N3yXlQdsw%2FDWGt%2FOPCkImpYW87RaUv3sAM6Hmbkq%2FwMIbhAAGgw2Mzc0MjMxODM4MDUiDIDLpGN95IrFlss4lircAzEOr4DCdUfpgXdcPIyNk6S8Vgk9%2FHxdjXdi4PM4nYKUk1K8iOn31HeiOfqyROcdLD0VG1kHQSXO31zl1YCHezJtAlqQYreGS1b1aWa1WeMiJ2D3FrmqShKX3NFqgfy5Z40LxkyqvA05kU%2BKzBCs7H2HHXFVL%2FC8Mm%2Fll2C8LGKCydBWnok%2BG17FCtMN7mu%2FhmdPSMB7C%2Fj1dyNDZ1DpfKRDNS4h3C0HLMGygSdtiGBoIZH9WZODsB9OdSkwEQK%2F1W00kqrkptmaSweS9FyBG07dBUl%2FTA1NCuy2VSCA7AXyiU1KlpKOwyX5tsIKzEQ8Z3oB%2Fal2Crgk2x0xjCKzJj1IEERZSzNNdYzzpvDGPHtsyfsbZwgAd3eD%2BAhGQHOMwGvOf%2B%2FOQ%2F6M4I%2FCmps0nVFgevLvpqBBqsdDg77uvsToHES7ev0YvXcwDySN3CKvZ1UedVURxISaIDroDZAwKlPJ%2Fgsq2TEaE3kWYGreM%2FeGITanTJ5TEvviFjfbyNlY8ozDfaCAOkiTVx4eA4juqoAMC8Fw1tcDkY4aiaTyAvYTt5e694qMN4dAxRBXia8dG5R8FLB0K1ZOKAEfMDumUR07OW9Frsh7ZFDjrIseT0rYipz3NmlAcu41Nrb6MIehlr0GOqUBcOEuYVE%2FfEnRhV3s9jYkrevH5xgNsTQ1DYpztxk9A%2BRy9%2FXqyiEO%2F2HocWCqbvrTir4S9wC1G7WlJgK2U32dp3WdiRkDLXrlsYLQSiFerqo5cv%2FGji7ha3VlXWYJidFCvWgE6MrUxuT73qBAMaPgKM0Bt4vMnL71OHtNHE4oIE186kM3BD%2Bc%2B7RQUvmwtZBO19LMhJiyUzV46HNDvca8qgWwkdbP&X-Amz-Signature=dd67b32169d361f5d3af7b60de7c00356c3f9f2d46e643fa3988286c16b5fe90&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/13ad0497-05fe-4eaa-984e-707b33e14761/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RVECKNIO%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T051430Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFUaCXVzLXdlc3QtMiJHMEUCIA%2Frvzde%2BFtudBCTf8PKTpGzIj7AjC8IMYJQUyZCI2bEAiEA6uF5N3yXlQdsw%2FDWGt%2FOPCkImpYW87RaUv3sAM6Hmbkq%2FwMIbhAAGgw2Mzc0MjMxODM4MDUiDIDLpGN95IrFlss4lircAzEOr4DCdUfpgXdcPIyNk6S8Vgk9%2FHxdjXdi4PM4nYKUk1K8iOn31HeiOfqyROcdLD0VG1kHQSXO31zl1YCHezJtAlqQYreGS1b1aWa1WeMiJ2D3FrmqShKX3NFqgfy5Z40LxkyqvA05kU%2BKzBCs7H2HHXFVL%2FC8Mm%2Fll2C8LGKCydBWnok%2BG17FCtMN7mu%2FhmdPSMB7C%2Fj1dyNDZ1DpfKRDNS4h3C0HLMGygSdtiGBoIZH9WZODsB9OdSkwEQK%2F1W00kqrkptmaSweS9FyBG07dBUl%2FTA1NCuy2VSCA7AXyiU1KlpKOwyX5tsIKzEQ8Z3oB%2Fal2Crgk2x0xjCKzJj1IEERZSzNNdYzzpvDGPHtsyfsbZwgAd3eD%2BAhGQHOMwGvOf%2B%2FOQ%2F6M4I%2FCmps0nVFgevLvpqBBqsdDg77uvsToHES7ev0YvXcwDySN3CKvZ1UedVURxISaIDroDZAwKlPJ%2Fgsq2TEaE3kWYGreM%2FeGITanTJ5TEvviFjfbyNlY8ozDfaCAOkiTVx4eA4juqoAMC8Fw1tcDkY4aiaTyAvYTt5e694qMN4dAxRBXia8dG5R8FLB0K1ZOKAEfMDumUR07OW9Frsh7ZFDjrIseT0rYipz3NmlAcu41Nrb6MIehlr0GOqUBcOEuYVE%2FfEnRhV3s9jYkrevH5xgNsTQ1DYpztxk9A%2BRy9%2FXqyiEO%2F2HocWCqbvrTir4S9wC1G7WlJgK2U32dp3WdiRkDLXrlsYLQSiFerqo5cv%2FGji7ha3VlXWYJidFCvWgE6MrUxuT73qBAMaPgKM0Bt4vMnL71OHtNHE4oIE186kM3BD%2Bc%2B7RQUvmwtZBO19LMhJiyUzV46HNDvca8qgWwkdbP&X-Amz-Signature=3cd37612f5bfc3a0a6942550d93dfa325a2dbe6122db42c45ed26ed3e27c7904&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 2. Box and Whisker Plot
A box plot shows the distribution of quantitative data in a way that facilitates comparisons between variables or across levels of a categorical variable. The box shows the quartiles of the dataset while the whiskers extend to show the rest of the distribution, except for points that are determined to be "outliers".
**Syntax:**
```python
sns.boxplot(x='header_1', y='header_2', data=df)
```
**Example Output:**


![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d207ae92-0a7c-4e2f-aa65-0ee5a2c33bf7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666ZO2DVEX%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T051431Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFUaCXVzLXdlc3QtMiJHMEUCIQDVnrnb54XZDhJ7iN5%2FWsxCwEpu0uiSrsAyx%2Bp9oCriSgIgdN5z5l%2F0XkxHzpGkiQzUH7RUs29BjbYKBE11savWx5oq%2FwMIbhAAGgw2Mzc0MjMxODM4MDUiDCEvqxLIWgB7ultNSyrcAxNMqzjd9mmRpCL8lyUrm2yPpChUgAuMoxwaUgzshOBvt4Hi5nKvsrvOPVUwQvSMWNCr6hP4xUl4ci8WMCvHID%2BbeINTNnJp1lWheGWCpLy%2F32I9RggeUozk3ehLmq0hgR641TXhu2zGeZCK0N2eH8MBE3vAnvKippekOzJZXQzA2gf4sAmoSDXuynebS3nFv%2FNcTgmh%2BqRXjYOhYRhknk7UoRnc%2BeGLt86xLLV2D27G22vWFwocSB1cM0u7M7IHYhDOxl923XYPLkJTuOTAVq3prlJ6RQSgT4a%2F91BDCJFeAqNntrb4plr2p4CfmMh9NyyNsm%2FX0xIdKUfDmEpEZPu88fC2RXiNDBR1PctvaoM2tKLp490pzwqDCfHNn28oHvOrU6cXU7jjZD%2BdmO0k%2FgqzRlGb%2FYGwh2gW9MH36qDEJJfQ%2BHZ9NpHvpuRGODxll%2Bma71hQTvArrCthH5ye692%2FrEA6DhyJJjquv2iD4YQe5bXWEGxcvBjr37LQ7RjIZRbsO7PVXtHeOherbFZCmStXIO%2Fu8yWULGJgGDWZ2YvIzgAfFBDb%2B4N2R5QRImhVxCRHiO6v4M46wHq9nJOtf%2FwkIkhJbETC2Fgpuypijelf9IFf2P7ARnbEpArhMM%2Bilr0GOqUBK9NV9kcSBjBJ3prXmDl9p1QiFL6FZD%2F9uw7dAi5oXqKXFWi5G1uXNkxeQS8tyn1ZSUUiiAKbsu8NH0GA2c%2FCQ5UPJEBK8GkAPGib8wx%2BnUZR9iQb5yjAY8PfNs88p6fAgFkuFoJLlhrt230mZWPcBUJRxTZ5URWLHXktDyEaZEVaR2ul8hmWrldzunTmaKOEMDT9vOibEF346QQImLEEeOOuwwcC&X-Amz-Signature=57102dbceba00e5d88fdea01cb89e666015db5f5f3c0275fdc1063576e2c2f4d&X-Amz-SignedHeaders=host&x-id=GetObject)

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0e516edc-7551-4792-ab18-0494db3c4c0c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YZXEOFNW%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T051431Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFUaCXVzLXdlc3QtMiJHMEUCIA0iOr1XrthBVvbkgc5uyDbd0SDoAr%2BUNm3S2QLI0fVxAiEAv7L3nQVXaOPqx8fcfOVxRYt2ETj1j6mFuuRqVRtLPkQq%2FwMIbhAAGgw2Mzc0MjMxODM4MDUiDLXLvawHlPh%2ButUO7CrcA9BCYNpg8AEJ6%2BX039pygmQ7AkmBQBMqrKhFz4YUueAOyz2nBtGHWvBfQEr2hVGKtAxznj4jaAt4fNmY88GnbVftGIKoXs8JY5%2B2cyShMgUYtASmo0YvD51jRQvgBok7E%2F2bInmHiUnRSL74w0JiDM%2F2Vp4YsRQ%2FLeJ4%2FsfXBtQdFz%2BPaLnmZxOZl0acuOp3ijHOgT4h0J0I4pEmL6opEcUXt%2BYo%2BnX0EDY1U6bmd5GRDvAWvrdG4Y%2By8t3WZU%2Bciiqso8o9a6dX9VAaUopHrozZET6ro4Fsn8Avzz4LhCPm4FL2acVBzmmTXiGs3HDVm1f3oUypIq95WmwWFtfXuKvbNBsQ1iptX%2BfPL4eeSlMQhCWZJKGW1IB7DxedNNXykbIwl0sQYBap7lty0086MSw3%2FVYwyM%2F0Jj1vb1IICgoBqSrRxMoXorYGJ3%2FKGruutEVknUXE4KnVFFgCD5OCtW10CQKPl3Y4ITJOOa8d92Ub%2B%2BZuS7SBxemjinWe%2FVjMWKaIkTzkjR1ZMFd%2BfvMDfJT0hNnOvTbz%2BDAX5emj8FnLXo1vOW0dbuIbN4zC73PTernOGL%2Ff4e9YJa1ORpQGrXr3h8SHY%2BJn4L3zWGlgTAGd6aXpuNd1ZZP9G8IgMJmhlr0GOqUBQAMb5sRli2XZ9vxNjXtsnq1UHepi6nNFB49%2BVuxtk0tqrBslMtWYxmskBwGvr9nSG4%2B5Uv6Nc%2BBDqZjkm7iNg6TIF3tiuWI9JZ82Vu00%2B6073GRarjMiChXLi7kWPW8bi8wMBETjxfglg1q46ihEtPdbr43hmFiP%2B%2FFah6c4gVI8ExiA7%2BvGplw41xGEJKSIujrn5YGRQh%2BfJl8FcRcIGxP%2BefrJ&X-Amz-Signature=7592a2e694e9a1bfaeb2ca041cd15202a09ca96b20a950c19d7c02253103bae6&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23a79b9d-2356-49a9-8fd9-65c6b0ab2cc5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RVECKNIO%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T051430Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFUaCXVzLXdlc3QtMiJHMEUCIA%2Frvzde%2BFtudBCTf8PKTpGzIj7AjC8IMYJQUyZCI2bEAiEA6uF5N3yXlQdsw%2FDWGt%2FOPCkImpYW87RaUv3sAM6Hmbkq%2FwMIbhAAGgw2Mzc0MjMxODM4MDUiDIDLpGN95IrFlss4lircAzEOr4DCdUfpgXdcPIyNk6S8Vgk9%2FHxdjXdi4PM4nYKUk1K8iOn31HeiOfqyROcdLD0VG1kHQSXO31zl1YCHezJtAlqQYreGS1b1aWa1WeMiJ2D3FrmqShKX3NFqgfy5Z40LxkyqvA05kU%2BKzBCs7H2HHXFVL%2FC8Mm%2Fll2C8LGKCydBWnok%2BG17FCtMN7mu%2FhmdPSMB7C%2Fj1dyNDZ1DpfKRDNS4h3C0HLMGygSdtiGBoIZH9WZODsB9OdSkwEQK%2F1W00kqrkptmaSweS9FyBG07dBUl%2FTA1NCuy2VSCA7AXyiU1KlpKOwyX5tsIKzEQ8Z3oB%2Fal2Crgk2x0xjCKzJj1IEERZSzNNdYzzpvDGPHtsyfsbZwgAd3eD%2BAhGQHOMwGvOf%2B%2FOQ%2F6M4I%2FCmps0nVFgevLvpqBBqsdDg77uvsToHES7ev0YvXcwDySN3CKvZ1UedVURxISaIDroDZAwKlPJ%2Fgsq2TEaE3kWYGreM%2FeGITanTJ5TEvviFjfbyNlY8ozDfaCAOkiTVx4eA4juqoAMC8Fw1tcDkY4aiaTyAvYTt5e694qMN4dAxRBXia8dG5R8FLB0K1ZOKAEfMDumUR07OW9Frsh7ZFDjrIseT0rYipz3NmlAcu41Nrb6MIehlr0GOqUBcOEuYVE%2FfEnRhV3s9jYkrevH5xgNsTQ1DYpztxk9A%2BRy9%2FXqyiEO%2F2HocWCqbvrTir4S9wC1G7WlJgK2U32dp3WdiRkDLXrlsYLQSiFerqo5cv%2FGji7ha3VlXWYJidFCvWgE6MrUxuT73qBAMaPgKM0Bt4vMnL71OHtNHE4oIE186kM3BD%2Bc%2B7RQUvmwtZBO19LMhJiyUzV46HNDvca8qgWwkdbP&X-Amz-Signature=662944d926f8801d7a057dc8e140794830538a87da7ce53a7f14a7ec63657155&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 4. KDE Plot
A Kernel Density Estimate (KDE) plot is a graph that creates a probability distribution curve for the data based upon its likelihood of occurrence on a specific value. This is created for a single vector of information.
**Syntax:**
```python
sns.kdeplot(X) || sns.kdeplot(df['age'])
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0d571213-2a2f-4921-a50b-880847aa05ee/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RVECKNIO%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T051430Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFUaCXVzLXdlc3QtMiJHMEUCIA%2Frvzde%2BFtudBCTf8PKTpGzIj7AjC8IMYJQUyZCI2bEAiEA6uF5N3yXlQdsw%2FDWGt%2FOPCkImpYW87RaUv3sAM6Hmbkq%2FwMIbhAAGgw2Mzc0MjMxODM4MDUiDIDLpGN95IrFlss4lircAzEOr4DCdUfpgXdcPIyNk6S8Vgk9%2FHxdjXdi4PM4nYKUk1K8iOn31HeiOfqyROcdLD0VG1kHQSXO31zl1YCHezJtAlqQYreGS1b1aWa1WeMiJ2D3FrmqShKX3NFqgfy5Z40LxkyqvA05kU%2BKzBCs7H2HHXFVL%2FC8Mm%2Fll2C8LGKCydBWnok%2BG17FCtMN7mu%2FhmdPSMB7C%2Fj1dyNDZ1DpfKRDNS4h3C0HLMGygSdtiGBoIZH9WZODsB9OdSkwEQK%2F1W00kqrkptmaSweS9FyBG07dBUl%2FTA1NCuy2VSCA7AXyiU1KlpKOwyX5tsIKzEQ8Z3oB%2Fal2Crgk2x0xjCKzJj1IEERZSzNNdYzzpvDGPHtsyfsbZwgAd3eD%2BAhGQHOMwGvOf%2B%2FOQ%2F6M4I%2FCmps0nVFgevLvpqBBqsdDg77uvsToHES7ev0YvXcwDySN3CKvZ1UedVURxISaIDroDZAwKlPJ%2Fgsq2TEaE3kWYGreM%2FeGITanTJ5TEvviFjfbyNlY8ozDfaCAOkiTVx4eA4juqoAMC8Fw1tcDkY4aiaTyAvYTt5e694qMN4dAxRBXia8dG5R8FLB0K1ZOKAEfMDumUR07OW9Frsh7ZFDjrIseT0rYipz3NmlAcu41Nrb6MIehlr0GOqUBcOEuYVE%2FfEnRhV3s9jYkrevH5xgNsTQ1DYpztxk9A%2BRy9%2FXqyiEO%2F2HocWCqbvrTir4S9wC1G7WlJgK2U32dp3WdiRkDLXrlsYLQSiFerqo5cv%2FGji7ha3VlXWYJidFCvWgE6MrUxuT73qBAMaPgKM0Bt4vMnL71OHtNHE4oIE186kM3BD%2Bc%2B7RQUvmwtZBO19LMhJiyUzV46HNDvca8qgWwkdbP&X-Amz-Signature=8eabd97c06e87ee6aae3c0919e1a23039392c558e4ac8625062f5fd01896100a&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/53752550-ef82-4ca9-a01a-09921f0282d0/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RVECKNIO%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T051430Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFUaCXVzLXdlc3QtMiJHMEUCIA%2Frvzde%2BFtudBCTf8PKTpGzIj7AjC8IMYJQUyZCI2bEAiEA6uF5N3yXlQdsw%2FDWGt%2FOPCkImpYW87RaUv3sAM6Hmbkq%2FwMIbhAAGgw2Mzc0MjMxODM4MDUiDIDLpGN95IrFlss4lircAzEOr4DCdUfpgXdcPIyNk6S8Vgk9%2FHxdjXdi4PM4nYKUk1K8iOn31HeiOfqyROcdLD0VG1kHQSXO31zl1YCHezJtAlqQYreGS1b1aWa1WeMiJ2D3FrmqShKX3NFqgfy5Z40LxkyqvA05kU%2BKzBCs7H2HHXFVL%2FC8Mm%2Fll2C8LGKCydBWnok%2BG17FCtMN7mu%2FhmdPSMB7C%2Fj1dyNDZ1DpfKRDNS4h3C0HLMGygSdtiGBoIZH9WZODsB9OdSkwEQK%2F1W00kqrkptmaSweS9FyBG07dBUl%2FTA1NCuy2VSCA7AXyiU1KlpKOwyX5tsIKzEQ8Z3oB%2Fal2Crgk2x0xjCKzJj1IEERZSzNNdYzzpvDGPHtsyfsbZwgAd3eD%2BAhGQHOMwGvOf%2B%2FOQ%2F6M4I%2FCmps0nVFgevLvpqBBqsdDg77uvsToHES7ev0YvXcwDySN3CKvZ1UedVURxISaIDroDZAwKlPJ%2Fgsq2TEaE3kWYGreM%2FeGITanTJ5TEvviFjfbyNlY8ozDfaCAOkiTVx4eA4juqoAMC8Fw1tcDkY4aiaTyAvYTt5e694qMN4dAxRBXia8dG5R8FLB0K1ZOKAEfMDumUR07OW9Frsh7ZFDjrIseT0rYipz3NmlAcu41Nrb6MIehlr0GOqUBcOEuYVE%2FfEnRhV3s9jYkrevH5xgNsTQ1DYpztxk9A%2BRy9%2FXqyiEO%2F2HocWCqbvrTir4S9wC1G7WlJgK2U32dp3WdiRkDLXrlsYLQSiFerqo5cv%2FGji7ha3VlXWYJidFCvWgE6MrUxuT73qBAMaPgKM0Bt4vMnL71OHtNHE4oIE186kM3BD%2Bc%2B7RQUvmwtZBO19LMhJiyUzV46HNDvca8qgWwkdbP&X-Amz-Signature=423e3962d0d4998a723995ceffada5e891574ce8f77036b16f1eb2570c9d36b0&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
## 4. Correlation Between Variables
Correlation is a statistical measure of the extent to which different variables are interdependent. It indicates how changes in one variable are associated with changes in another variable over time.
### Positive Correlation
Positive correlation indicates that as one variable increases, the other variable also tends to increase.
**Example: Engine Size and Price**
- **Positive Correlation:** Engine size increases, price also increases.
- **Visualization:** Scatter plot with a steep positive slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c7ea9b0-3ef3-4357-a9c3-554fc71b6b15/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R3XZA6WD%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T051431Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFUaCXVzLXdlc3QtMiJIMEYCIQDIxsrTeeBzUdVbnV%2FEQiYRZ2yKUFUKFH79MYMzEP%2BVMwIhAMSQ2ZrbIxZnp%2BWKXXHbZEMxWqp997bo1xR30BdUpg7rKv8DCG4QABoMNjM3NDIzMTgzODA1IgzD60tYIs%2FZEFKmhP8q3AP7EXbSiZuEA96JGvu%2BSLqGRRU%2FcBKx9%2BmNPsdCkYwPPacHrWfRb1zi7%2Bh2fuaXMjrZTKLPD5n06q7J%2FiBGTkgHK%2FAwNMBEqB1fw5bj30zfMiSY0yCEIQ9ucvRmkJpN1D7cQUiJqGobmL9qwnyNC2upM%2BCKPs%2FyeOPPNbsU%2BkFi6QSBwJNLzXaGiUg1YDD9GqDr2a3e1OYaSrrEWFwjUYYNeJTx1BeObNNwtP8%2Fy6kI5SKcrjwA08H5t0PKrOnopBN5A4NUBSZr3xCO6TouuXKQMiye2nvgwJPCPkUqEyxgnoIfN5XfDObvdlWWWymRfu94surW5xT6omNjUffEoPfKUKi17xBP7l5xU%2F%2FnwFoRb%2Fe6uJBTuG11eJ1mXhDe2fTjjjXNGqIRGoCtaJqxBRMswTrjYCfkLEu1WxC3NvZJTn6Q1S943xXnFVIF6xg1rKmi%2Bx4qC91fiz4I%2BSjUILHgTdrCguJ2ERmZc%2BtPqhjXZooLmlljhZfbHMaETtFolTTuuPHGDw0ArtRkA57QQt6NWmcum5ecm5yHbKI3%2BrhjVsvIQXAitdEiBqlHIT%2BtD4gyQ%2BILsLzVkTNxYKX5IWmU4cSzPWvBBzLKx41tkCVsAHnSJ5FVSKAgHqhEXTDToZa9BjqkAZRLMKqFfeO%2BLn1oeh1RWwQ2Yj5mLoweX%2FA0bWwJ0uYzvTgOheCuS3OzpAlpE2ZbnIuTjpp%2FhInGx3CvZW93GbJo0dDpGw%2FvZkDKPG%2FyaiLZpXK4mgZTkYIqLZoBpLc%2BwcJKTEyTqoeS2DR0fPSg76e4FJX9VhMHXocCLnzTHEts%2BrTDY9mlS3Xy0W9aROYZ0RUcdtBoYgvb4m56iAEQvDO24S1u&X-Amz-Signature=0762b6532fa56ab0ee96ed9b71c9f4c45e3da03acff37890a987d4d1752332ae&X-Amz-SignedHeaders=host&x-id=GetObject)
**Explanation:** When engine size increases, there is a corresponding increase in the price of the vehicle. This positive correlation suggests that larger engines tend to be associated with higher prices in the market.
___
### Negative Correlation
Negative correlation indicates that as one variable increases, the other variable tends to decrease.
**Example: Highway Miles per Gallon and Price**
- **Negative Correlation:** As highway miles per gallon increases, price decreases.
- **Visualization:** Scatter plot with a steep negative slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/10f1f798-9cc4-4df2-a9c1-5a339f554a0b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XN4TG7R7%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T051432Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFUaCXVzLXdlc3QtMiJHMEUCIQC6F92tyjnzNab4FXQxPgkX3Od3%2BoBRIKzKjWhYtvREywIgG12vQ2V3Of3tZ9RWrB%2Fbj59qyOHckVxx7MMGehcIKNkq%2FwMIbhAAGgw2Mzc0MjMxODM4MDUiDADNfzf8dNvIYmPPsSrcA7vnwvUr4YQ2003AGeVUIjz5b%2FfQIbZja0tK%2FDcTqOdCfUZMAvj0oTJBCCG8pYCWIozumFuTEOssoRWUH3eZhLNPircsSduWhFjIs6s57aLaQI79DwO%2BhtisUzjeAJfZioal00vuXIzUyrRUMfvNP32%2F%2BMQyew0PGO5SXyQ0zLmVGdUHbwCBu1WV9X%2FVlJiyyZHjYIRTSi6ext9VP9AXxY21IfXSnL%2FwyFKF4cCmr3SGEUyCxuvs46sqkxGOHYvu6k4sYPMXyi5S%2BQzApt%2Ffw5AKXw5V3q6UqZP2rhpMlT9bJOShGSDeBUaXB0SDoFGBSWCsRAWyu%2BQ%2BbaBevprcFiNAopeOqsMfA4ul8D6DrINzDk62Nq8O4%2FaBW713p5ROvQp2RoEWZ6P5ZdW9c1QhHZnTN1KordYrXw93%2BodirXJ3JGBWPNcGbyL%2FpncM4K8Pw3ZpKai0JG%2BwB3DwBpOmQ2jg8CFLTXro1yiLGSy7xATZzwceqLGTgkJLkVm88rMtKJn8PsAt2osIx4LvrGBxwpZCRHl6PqXt3zVFQRo3ixaQleHWvtLD2sNNzwcj4UE3ooFqflRPIOgoiyfaG5B2SL3i1kD6B7yIaJpdtAwHa0MSLf0HYcdUPIX69CHcMKyhlr0GOqUBaxfdaZfUWcK43nBI2gVz3vgKKXBjtqDAsJzkEuQlxJU03vDUASbvtffFnOIs23pUVXhXaP5lTOSFwwWzQUSqE%2BPoDDJcQYNmoGx9kTS3zk%2B8KByW%2FRXWrm0jS18xcEZ5WfQgnRgbUDKoKO%2BD7G32Lt8%2B7W%2FlM93CpOcQkTEXrAsI3ypdPkRqF82LGkMaJs2YtZfsRjuitqvuotfm%2BIcZjvf0dmlB&X-Amz-Signature=3e9a27a0ed26b380195c0303d369335dc0ab31d5e3408c4a9fb3789adf642f6a&X-Amz-SignedHeaders=host&x-id=GetObject)
**Explanation:** When highway miles per gallon increases, the price of the vehicle tends to decrease. This negative correlation suggests that cars with higher fuel efficiency (more miles per gallon) are generally priced lower in the market.
___
### Weak Correlation
Weak correlation indicates a lack of strong relationship between the variables.
**Example: RPM and Price**
- **Weak Correlation:** Low and high RPM values show varied prices, indicating no strong predictive relationship.
- **Visualization:** Scatter plot with no clear trend or slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9f914514-8914-4bf4-ac84-d9e3077f6eb1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RYDJH7Z6%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T051431Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFUaCXVzLXdlc3QtMiJHMEUCIEPwj03jAxfbHGctBTvtHqfT%2BCULTfgUa%2B8LgiXUekXIAiEAmBard9%2BOGITH4mTuxLIQCydoNrqwvmZkKn8QIOiqJVMq%2FwMIbhAAGgw2Mzc0MjMxODM4MDUiDLBREF39WfgvGhDIiCrcA%2FYWHE1yYod6DsnVKFn3yPFpfl1OzQH%2FpEg2vizqCOyjC576C%2B2TH7Xy3URuycz5h8SPbJWyc3GoY9LB%2Fcp63Cp6TVtSReDCCT8s2yFKptr4QFhBkM%2BkUYYx1Ol33WcYL7QqphMUjW%2F6uj26xWnmmQen39%2BQgys6cwC61sHrL7q%2BRpjkWn8v8gYVL9UNoSm6S9in4O8QIjCcvtoRSytC%2FSrM59%2FnrjuWpW%2BLXosiKMd9pMpDwK5CkegAFg4sMpoaYS9tL9%2BteIjMSXZtifM%2FHPErtk2EPAMCRDWr1q%2B%2F9c%2BDKyoZwUHL04ySYCMFraQLlrgvO1vbSPH0YXFwRdXAt6mCCpvlBn8nLqYrHLNTnT7L52TmKfwXFpaM3kxI9ccANrynYV3925BA4zkO9N06pgoyp11zUZP%2Fq0wCBpXVjXvXcJKSD54A44z%2FqOliQ1JfMNKPFr4Um5NPJOxg0ISIspsPByEqYWQtBHo6ygc7G1AdwAlSPA0%2BF5eV5zmUVK%2FVDZa%2FYuI77rd%2B2n2kD5HQlfJ1XUVGXYWH1Srw%2Ff40KdjTOT5y45IZqkd4Vfcxrq3Dq39em%2FNBL3DOKnMF1gpZmXZh7KfMmeZ9CBX%2B8mNBJ28Sex0mXXD86WvBj9%2FhMKGhlr0GOqUB6vwxgtW5jGuGk9QeoiNyLlhPkKArYfcuFCZ0fk%2B08ZbdPD%2FNWSYO2MM9f8rUNrIRkcJRO2ScpbeeJ4AgQxHuL49Ct7YUD%2FNNp59pXfHh4gc4nCW6%2FYWLTN1p8zJ4rxM6YgrquhSVAcLS26uK76z7n47rjhnDCttgMXv69gibCZj9e0fSsi%2Fuzczqtob%2BWKPghSr86B4ZNlQuYZRBzKkKH0bavw6m&X-Amz-Signature=8be99da63493783f6f57fc9e92a592ca6d4e13faaf30af4fa66ef9b6548d5bbf&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f18086e5-5b04-4fbf-8309-8944ab20d213/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466W465OKWE%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T051430Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFUaCXVzLXdlc3QtMiJHMEUCICd3t8R0zR3ZPBgD%2F5%2Fg3HoxOCapzI2fMNdSyeCzitNKAiEAjatvgVCm1xo4zbwHac%2FzgndCwpwI3E3gy6c5ChiL1CUq%2FwMIbhAAGgw2Mzc0MjMxODM4MDUiDC3egXBdwpBvbVisNCrcA1h5CW1WZ9FS0lKFddPiP%2FUN2ekiOPSoDAbdmMa6HKweZr0LWFIxjMe6qyubY1RFizSChZ8SzQ5WHcb52VLqFEVZ0hKV4tBDnF4jGpagSt%2FPqBeqZUOKKE4q5AKOgT76XUPRj5xPmbnJjj%2FYJAbMvJoShqYSCrbmNFwqAxGNGrZjKOTUcOSOB3rVUCiyiHaltBw9n1TCHTY8b1pLjqC1nhnX19QWbe0W4AieyiPAjF2w4FGuq3hyS97nX0XHxenV4wjgDrOYhiRUFuR25kxo2dUyox6cdcftKlyvZU8G1p2XOZkuqwwsbsl1kj44glwXM7gKKjx3UinKsiAflGJz7jAewJrZeUYWcX1n54lfhi%2FY3fATRKIT6QDHzeTjs7HUCPunOgAZkDjA3wfvpOs3Z2LlLSCIYcPw3kV6K4MvcuxA6xxhivg2nu7NZPjpGZ7iU3JIHwIqtQxgKLeXkspNtpzrDaBflaYvfIX1k6VX1ACQFdkAbOJWX1MDHrR8%2FP115eJU1j2fpAXoeFblsX9h%2FYnGYc8OM9viCH78B%2Bcax6OeOp12tX5XFVkPJABdh12%2FcVId0i%2F4KhwRaAbPskH%2FRrsOq%2B29m68f5ZXdnCgSSV%2Bpd638UxzfdrXsu%2BJvMNOilr0GOqUBD35ef%2BzDipZJOGB0n085ds2CgqlNL54JZ8qVx0w4eQIz%2F198QF8I6QtDlI6a6c1FsJS4cHyIIiPaiMpYt6IPJnfhzFvchvB0%2Fxt%2FnwMskzDIY%2Bkzh%2B%2BpOdt9xmrWyUFQBo7lbBXF2qkYPH%2BXiVEZRQz3SXOhmo0fPgmczZvDzZQeBWh9yrYnnFbDvLKi2o4QkK1BanaTi%2ByD0HiPcsi8wTJLSevn&X-Amz-Signature=4cfe44fc400dbb0c4becb12b8c524ca7ae8aeb0fe8ad6b7e668f32bb767c8cab&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Correlation Plot
Heatmap visualizes correlations among variables. Color scheme indicates Pearson correlation coefficients. Dark red diagonal line shows perfect correlation (value of 1) between variables and themselves.
This heatmap offers overview of variable relationships and their link with price.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cd3b341e-cc1a-45f7-8aec-cdc00436d270/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466W465OKWE%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T051430Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFUaCXVzLXdlc3QtMiJHMEUCICd3t8R0zR3ZPBgD%2F5%2Fg3HoxOCapzI2fMNdSyeCzitNKAiEAjatvgVCm1xo4zbwHac%2FzgndCwpwI3E3gy6c5ChiL1CUq%2FwMIbhAAGgw2Mzc0MjMxODM4MDUiDC3egXBdwpBvbVisNCrcA1h5CW1WZ9FS0lKFddPiP%2FUN2ekiOPSoDAbdmMa6HKweZr0LWFIxjMe6qyubY1RFizSChZ8SzQ5WHcb52VLqFEVZ0hKV4tBDnF4jGpagSt%2FPqBeqZUOKKE4q5AKOgT76XUPRj5xPmbnJjj%2FYJAbMvJoShqYSCrbmNFwqAxGNGrZjKOTUcOSOB3rVUCiyiHaltBw9n1TCHTY8b1pLjqC1nhnX19QWbe0W4AieyiPAjF2w4FGuq3hyS97nX0XHxenV4wjgDrOYhiRUFuR25kxo2dUyox6cdcftKlyvZU8G1p2XOZkuqwwsbsl1kj44glwXM7gKKjx3UinKsiAflGJz7jAewJrZeUYWcX1n54lfhi%2FY3fATRKIT6QDHzeTjs7HUCPunOgAZkDjA3wfvpOs3Z2LlLSCIYcPw3kV6K4MvcuxA6xxhivg2nu7NZPjpGZ7iU3JIHwIqtQxgKLeXkspNtpzrDaBflaYvfIX1k6VX1ACQFdkAbOJWX1MDHrR8%2FP115eJU1j2fpAXoeFblsX9h%2FYnGYc8OM9viCH78B%2Bcax6OeOp12tX5XFVkPJABdh12%2FcVId0i%2F4KhwRaAbPskH%2FRrsOq%2B29m68f5ZXdnCgSSV%2Bpd638UxzfdrXsu%2BJvMNOilr0GOqUBD35ef%2BzDipZJOGB0n085ds2CgqlNL54JZ8qVx0w4eQIz%2F198QF8I6QtDlI6a6c1FsJS4cHyIIiPaiMpYt6IPJnfhzFvchvB0%2Fxt%2FnwMskzDIY%2Bkzh%2B%2BpOdt9xmrWyUFQBo7lbBXF2qkYPH%2BXiVEZRQz3SXOhmo0fPgmczZvDzZQeBWh9yrYnnFbDvLKi2o4QkK1BanaTi%2ByD0HiPcsi8wTJLSevn&X-Amz-Signature=49f6101c70dec1ee365aeeef3416f8352993c411a8616eb9642e2c26da374f0e&X-Amz-SignedHeaders=host&x-id=GetObject)

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
