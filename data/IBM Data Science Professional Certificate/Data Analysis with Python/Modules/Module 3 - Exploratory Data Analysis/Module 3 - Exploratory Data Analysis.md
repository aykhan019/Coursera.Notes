

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7e6d594d-952e-44b6-97ea-31225882aea6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XHJM6ROL%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T231257Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEO%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDhwnaMz6B7cynnvcG25S3wUc%2BO1USW4K0rClCrIpO8XwIhAKXkn1%2BQM56UbT9R%2BgtqDby64npTpXvzwlzDZaL3mBOKKogECPj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyGJm7QXP5zopi8eMkq3ANgv2g7IkNKFELXYGZ6nTaTmzOIQ8FQ7L9UnyXEX5cq%2Fqm91D0btxThQOVMO4wiN9oVnYW%2BnpmPAYoxGg32D5HxCvCCoHLK9t%2FJUNVX9kYFn5dH7fRt2zLvZtkT1YQm8GV87KmsV4Lqfqpzj2meR17LmAjPxO8%2BkMTVDiAYytEnzk%2FToIHzjvcMGZNQIxaz9dOPCcnMr3Cb1mXY0XueJlzk8JDQNQNcpwNIq%2BvpD3wOrdMPI0%2F40r8esPGla%2FozzAgGzQR%2FasRZG7VR9QGXIhtnzln%2FqfJqBAv%2BNuGH4QjuuMLQQ9MPEQb6h0HFUvwE1Z%2BLByVuS%2BccBsZagANfMmwJbZZ4WFoSloIvHpGWnw%2BDLFxkj%2BERvmEWvDFbNR8HEYzUcw35GRSptCtRvzwGuMe6201rZ1pxg94OqeDxNywMP%2FU1iTwcqc%2B%2Ff1KVWMb3pOX61RsG5IFbvIHDaFRVmQVsuK8T3wjJcVtaRceMsq21GZWBRgcepwF2OdBJ%2FYR57AI1IzBZB5ezShNmQ2HRyGR02T8iZ3vAtU5ooBwTJ2hiCAGipu8m9FozPgByH8vnnDufFR5dsGM9vWYMWCr%2FZv0rjAcXAJMyDwAZUceeDK7y2yjrHm%2F0cZtrH%2BMAITDF5P%2B8BjqkAdcix6VkMWC5MBW7Wagey%2FWAfThGYEXPlkYoKrBlm0i4AZw%2BkK%2FDP9EvtWsvaLK5L%2BvUjx03gZnYZmnyNi%2FRws6NnnbG8RWAx%2BBiQ1OtXbMRkjB6RcWIpiKTAkajBYhWvD%2FI6sARXaHiXFWEwqk7J%2BwB2HPbN6OPVccderf7PBhS6xUhl9YHmuW6eXfyvC2E2piVmRBld3JnkT2jKT5yWVvAY7Na&X-Amz-Signature=f31398df92a7d4ce1e2ef2efe77e4196c04d35fef1db670cd27475738f83c3cc&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cbfaed9e-b398-4902-8936-dea058b21def/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XHJM6ROL%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T231257Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEO%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDhwnaMz6B7cynnvcG25S3wUc%2BO1USW4K0rClCrIpO8XwIhAKXkn1%2BQM56UbT9R%2BgtqDby64npTpXvzwlzDZaL3mBOKKogECPj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyGJm7QXP5zopi8eMkq3ANgv2g7IkNKFELXYGZ6nTaTmzOIQ8FQ7L9UnyXEX5cq%2Fqm91D0btxThQOVMO4wiN9oVnYW%2BnpmPAYoxGg32D5HxCvCCoHLK9t%2FJUNVX9kYFn5dH7fRt2zLvZtkT1YQm8GV87KmsV4Lqfqpzj2meR17LmAjPxO8%2BkMTVDiAYytEnzk%2FToIHzjvcMGZNQIxaz9dOPCcnMr3Cb1mXY0XueJlzk8JDQNQNcpwNIq%2BvpD3wOrdMPI0%2F40r8esPGla%2FozzAgGzQR%2FasRZG7VR9QGXIhtnzln%2FqfJqBAv%2BNuGH4QjuuMLQQ9MPEQb6h0HFUvwE1Z%2BLByVuS%2BccBsZagANfMmwJbZZ4WFoSloIvHpGWnw%2BDLFxkj%2BERvmEWvDFbNR8HEYzUcw35GRSptCtRvzwGuMe6201rZ1pxg94OqeDxNywMP%2FU1iTwcqc%2B%2Ff1KVWMb3pOX61RsG5IFbvIHDaFRVmQVsuK8T3wjJcVtaRceMsq21GZWBRgcepwF2OdBJ%2FYR57AI1IzBZB5ezShNmQ2HRyGR02T8iZ3vAtU5ooBwTJ2hiCAGipu8m9FozPgByH8vnnDufFR5dsGM9vWYMWCr%2FZv0rjAcXAJMyDwAZUceeDK7y2yjrHm%2F0cZtrH%2BMAITDF5P%2B8BjqkAdcix6VkMWC5MBW7Wagey%2FWAfThGYEXPlkYoKrBlm0i4AZw%2BkK%2FDP9EvtWsvaLK5L%2BvUjx03gZnYZmnyNi%2FRws6NnnbG8RWAx%2BBiQ1OtXbMRkjB6RcWIpiKTAkajBYhWvD%2FI6sARXaHiXFWEwqk7J%2BwB2HPbN6OPVccderf7PBhS6xUhl9YHmuW6eXfyvC2E2piVmRBld3JnkT2jKT5yWVvAY7Na&X-Amz-Signature=1918703d6e634cad2e212eb974f5b2e06b497571ac9124a6cc7e20e8212bf08d&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/91181646-b1e0-4433-9711-6259a96a9247/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XHJM6ROL%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T231257Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEO%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDhwnaMz6B7cynnvcG25S3wUc%2BO1USW4K0rClCrIpO8XwIhAKXkn1%2BQM56UbT9R%2BgtqDby64npTpXvzwlzDZaL3mBOKKogECPj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyGJm7QXP5zopi8eMkq3ANgv2g7IkNKFELXYGZ6nTaTmzOIQ8FQ7L9UnyXEX5cq%2Fqm91D0btxThQOVMO4wiN9oVnYW%2BnpmPAYoxGg32D5HxCvCCoHLK9t%2FJUNVX9kYFn5dH7fRt2zLvZtkT1YQm8GV87KmsV4Lqfqpzj2meR17LmAjPxO8%2BkMTVDiAYytEnzk%2FToIHzjvcMGZNQIxaz9dOPCcnMr3Cb1mXY0XueJlzk8JDQNQNcpwNIq%2BvpD3wOrdMPI0%2F40r8esPGla%2FozzAgGzQR%2FasRZG7VR9QGXIhtnzln%2FqfJqBAv%2BNuGH4QjuuMLQQ9MPEQb6h0HFUvwE1Z%2BLByVuS%2BccBsZagANfMmwJbZZ4WFoSloIvHpGWnw%2BDLFxkj%2BERvmEWvDFbNR8HEYzUcw35GRSptCtRvzwGuMe6201rZ1pxg94OqeDxNywMP%2FU1iTwcqc%2B%2Ff1KVWMb3pOX61RsG5IFbvIHDaFRVmQVsuK8T3wjJcVtaRceMsq21GZWBRgcepwF2OdBJ%2FYR57AI1IzBZB5ezShNmQ2HRyGR02T8iZ3vAtU5ooBwTJ2hiCAGipu8m9FozPgByH8vnnDufFR5dsGM9vWYMWCr%2FZv0rjAcXAJMyDwAZUceeDK7y2yjrHm%2F0cZtrH%2BMAITDF5P%2B8BjqkAdcix6VkMWC5MBW7Wagey%2FWAfThGYEXPlkYoKrBlm0i4AZw%2BkK%2FDP9EvtWsvaLK5L%2BvUjx03gZnYZmnyNi%2FRws6NnnbG8RWAx%2BBiQ1OtXbMRkjB6RcWIpiKTAkajBYhWvD%2FI6sARXaHiXFWEwqk7J%2BwB2HPbN6OPVccderf7PBhS6xUhl9YHmuW6eXfyvC2E2piVmRBld3JnkT2jKT5yWVvAY7Na&X-Amz-Signature=ed083bac3d928912a1087105f56483844d90a26cccb7628e0e73711390ef881a&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/09aba1c0-0d55-41dd-852a-a04c5b8a3fac/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662F5234WL%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T231258Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEO%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCchzXOLv1jyq4Jha1eSuNbHCRICLjfFODWSg7XkNy1ugIgWfd9Bil16ocTbMuiMLmDcUKswpd9fKvP8LlAwxQYR8EqiAQI%2BP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJURBPniWNv1RIKhgSrcA%2BkF6IlyLQj7onHHNdxyLkPK83687%2F1UK9Zjo8HBUT3A4E82DE%2FeFeADVlrV1ML7791%2FIU3j4hFyzex6fi3VTOdhqq%2B%2FPRG%2FPnM0xzIw8Dc1YHTL0PAunpiENZVgYKHGX8rIyb4sSa8k6TMymeBumOQUMgvnjgJyVM2qnX0Iu49FGR%2FsURZb0USqVQDou5HSk4gSeFEge5WgQLITaJXW0ITSgUkQq8e1TtRx5EOhPvLouwy27lZstb5N%2Bj84PtIv%2BW7njzHsklcGlc8GDrXkZcCkYcF0DW9fQp6OqTDWwDyZ4lu8mm%2FrLQh0u2ndEdmFAnO2Fbwn1AlNNWKfxN%2BvsAbxmyvEzzzq%2FBy1eNxHyLIQfHGbLzWzzjKvBmKE1kDcYPBao51L3FADSX4Wbuc%2B19T26fzOZNCjs9rMc0SB7BDIL6hFn0bHn5i6vk8aeNQ6BLqcvYQ3RM1CTwgHuL3ru6AmLFeNnT4WMHBXtfMD0OetSm5kK0mSEEsnLiFZutv8liDnwZDgIW%2FT%2F87E1xbE8TMEKz8tmXc1BRVeIEQRZbtR%2F5mOuV%2BsRJpIeZZHAYrjzpLmiI2%2BP8GFA%2FYGjNS8Z6Bi5n6Kal3UgDc1O0vKwzcCHDvHqIAfEXP07mCMMIjm%2F7wGOqUB2Nw2JILtwJUxDkWCtianLxW89ODy6fP1ppkReC96ZXt4FzKn74GIYRHWp262u2o3dDI0vNHPQZms1GuZFWmaZ%2BSKllLdVYSJKEETYOtIn09ahlrZbbx7jr87TOoLRr9ay1kJnoRw13cf1a5ue%2FVa8LaZ6Nc0w%2Bn%2BG9iGU%2Btyv6pLDm9Qcz5z6AO3e1Ls0q3SjU6ZobA6h8yv0u94Qbv4hrUXp5as&X-Amz-Signature=e6460bf3cf3cfc927e120b9b4774a0e3c46d309cb153f9b34ae7ce0b0335c172&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 2. Scatter Plot
Scatter plots present the relationship between two variables in a dataset. It represents data points on a two-dimensional plane. The independent variable or attribute is plotted on the X-axis, while the dependent variable is plotted on the Y-axis.
**Syntax:**
```python
plt.scatter(x, y)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23708af9-659f-4f23-b626-1a4292d7842c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662F5234WL%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T231258Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEO%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCchzXOLv1jyq4Jha1eSuNbHCRICLjfFODWSg7XkNy1ugIgWfd9Bil16ocTbMuiMLmDcUKswpd9fKvP8LlAwxQYR8EqiAQI%2BP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJURBPniWNv1RIKhgSrcA%2BkF6IlyLQj7onHHNdxyLkPK83687%2F1UK9Zjo8HBUT3A4E82DE%2FeFeADVlrV1ML7791%2FIU3j4hFyzex6fi3VTOdhqq%2B%2FPRG%2FPnM0xzIw8Dc1YHTL0PAunpiENZVgYKHGX8rIyb4sSa8k6TMymeBumOQUMgvnjgJyVM2qnX0Iu49FGR%2FsURZb0USqVQDou5HSk4gSeFEge5WgQLITaJXW0ITSgUkQq8e1TtRx5EOhPvLouwy27lZstb5N%2Bj84PtIv%2BW7njzHsklcGlc8GDrXkZcCkYcF0DW9fQp6OqTDWwDyZ4lu8mm%2FrLQh0u2ndEdmFAnO2Fbwn1AlNNWKfxN%2BvsAbxmyvEzzzq%2FBy1eNxHyLIQfHGbLzWzzjKvBmKE1kDcYPBao51L3FADSX4Wbuc%2B19T26fzOZNCjs9rMc0SB7BDIL6hFn0bHn5i6vk8aeNQ6BLqcvYQ3RM1CTwgHuL3ru6AmLFeNnT4WMHBXtfMD0OetSm5kK0mSEEsnLiFZutv8liDnwZDgIW%2FT%2F87E1xbE8TMEKz8tmXc1BRVeIEQRZbtR%2F5mOuV%2BsRJpIeZZHAYrjzpLmiI2%2BP8GFA%2FYGjNS8Z6Bi5n6Kal3UgDc1O0vKwzcCHDvHqIAfEXP07mCMMIjm%2F7wGOqUB2Nw2JILtwJUxDkWCtianLxW89ODy6fP1ppkReC96ZXt4FzKn74GIYRHWp262u2o3dDI0vNHPQZms1GuZFWmaZ%2BSKllLdVYSJKEETYOtIn09ahlrZbbx7jr87TOoLRr9ay1kJnoRw13cf1a5ue%2FVa8LaZ6Nc0w%2Bn%2BG9iGU%2Btyv6pLDm9Qcz5z6AO3e1Ls0q3SjU6ZobA6h8yv0u94Qbv4hrUXp5as&X-Amz-Signature=aa2020812a7484e57fe9b96da8a3020b6486fa408622906ceaaecaad75a5c567&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 3. Histogram
A histogram is an important visual representation of data in categorical form. To view the data in a "Binned" form, use the histogram plot with a number of bins required or with the data points that mark the bin edges. The x-axis represents the data bins, and the y-axis represents the number of elements in each bin.
**Syntax:**
```python
plt.hist(x, bins)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/24e4424a-df87-40a1-b63b-195cbdc2e0ab/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662F5234WL%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T231258Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEO%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCchzXOLv1jyq4Jha1eSuNbHCRICLjfFODWSg7XkNy1ugIgWfd9Bil16ocTbMuiMLmDcUKswpd9fKvP8LlAwxQYR8EqiAQI%2BP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJURBPniWNv1RIKhgSrcA%2BkF6IlyLQj7onHHNdxyLkPK83687%2F1UK9Zjo8HBUT3A4E82DE%2FeFeADVlrV1ML7791%2FIU3j4hFyzex6fi3VTOdhqq%2B%2FPRG%2FPnM0xzIw8Dc1YHTL0PAunpiENZVgYKHGX8rIyb4sSa8k6TMymeBumOQUMgvnjgJyVM2qnX0Iu49FGR%2FsURZb0USqVQDou5HSk4gSeFEge5WgQLITaJXW0ITSgUkQq8e1TtRx5EOhPvLouwy27lZstb5N%2Bj84PtIv%2BW7njzHsklcGlc8GDrXkZcCkYcF0DW9fQp6OqTDWwDyZ4lu8mm%2FrLQh0u2ndEdmFAnO2Fbwn1AlNNWKfxN%2BvsAbxmyvEzzzq%2FBy1eNxHyLIQfHGbLzWzzjKvBmKE1kDcYPBao51L3FADSX4Wbuc%2B19T26fzOZNCjs9rMc0SB7BDIL6hFn0bHn5i6vk8aeNQ6BLqcvYQ3RM1CTwgHuL3ru6AmLFeNnT4WMHBXtfMD0OetSm5kK0mSEEsnLiFZutv8liDnwZDgIW%2FT%2F87E1xbE8TMEKz8tmXc1BRVeIEQRZbtR%2F5mOuV%2BsRJpIeZZHAYrjzpLmiI2%2BP8GFA%2FYGjNS8Z6Bi5n6Kal3UgDc1O0vKwzcCHDvHqIAfEXP07mCMMIjm%2F7wGOqUB2Nw2JILtwJUxDkWCtianLxW89ODy6fP1ppkReC96ZXt4FzKn74GIYRHWp262u2o3dDI0vNHPQZms1GuZFWmaZ%2BSKllLdVYSJKEETYOtIn09ahlrZbbx7jr87TOoLRr9ay1kJnoRw13cf1a5ue%2FVa8LaZ6Nc0w%2Bn%2BG9iGU%2Btyv6pLDm9Qcz5z6AO3e1Ls0q3SjU6ZobA6h8yv0u94Qbv4hrUXp5as&X-Amz-Signature=61420e8f25a66cf49478f499d5add577638bfb9dff4a56e3b1bb25205dac5bdd&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ab5a6dfe-51f5-43ee-bcb3-33dae4a1c7ad/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662F5234WL%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T231258Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEO%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCchzXOLv1jyq4Jha1eSuNbHCRICLjfFODWSg7XkNy1ugIgWfd9Bil16ocTbMuiMLmDcUKswpd9fKvP8LlAwxQYR8EqiAQI%2BP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJURBPniWNv1RIKhgSrcA%2BkF6IlyLQj7onHHNdxyLkPK83687%2F1UK9Zjo8HBUT3A4E82DE%2FeFeADVlrV1ML7791%2FIU3j4hFyzex6fi3VTOdhqq%2B%2FPRG%2FPnM0xzIw8Dc1YHTL0PAunpiENZVgYKHGX8rIyb4sSa8k6TMymeBumOQUMgvnjgJyVM2qnX0Iu49FGR%2FsURZb0USqVQDou5HSk4gSeFEge5WgQLITaJXW0ITSgUkQq8e1TtRx5EOhPvLouwy27lZstb5N%2Bj84PtIv%2BW7njzHsklcGlc8GDrXkZcCkYcF0DW9fQp6OqTDWwDyZ4lu8mm%2FrLQh0u2ndEdmFAnO2Fbwn1AlNNWKfxN%2BvsAbxmyvEzzzq%2FBy1eNxHyLIQfHGbLzWzzjKvBmKE1kDcYPBao51L3FADSX4Wbuc%2B19T26fzOZNCjs9rMc0SB7BDIL6hFn0bHn5i6vk8aeNQ6BLqcvYQ3RM1CTwgHuL3ru6AmLFeNnT4WMHBXtfMD0OetSm5kK0mSEEsnLiFZutv8liDnwZDgIW%2FT%2F87E1xbE8TMEKz8tmXc1BRVeIEQRZbtR%2F5mOuV%2BsRJpIeZZHAYrjzpLmiI2%2BP8GFA%2FYGjNS8Z6Bi5n6Kal3UgDc1O0vKwzcCHDvHqIAfEXP07mCMMIjm%2F7wGOqUB2Nw2JILtwJUxDkWCtianLxW89ODy6fP1ppkReC96ZXt4FzKn74GIYRHWp262u2o3dDI0vNHPQZms1GuZFWmaZ%2BSKllLdVYSJKEETYOtIn09ahlrZbbx7jr87TOoLRr9ay1kJnoRw13cf1a5ue%2FVa8LaZ6Nc0w%2Bn%2BG9iGU%2Btyv6pLDm9Qcz5z6AO3e1Ls0q3SjU6ZobA6h8yv0u94Qbv4hrUXp5as&X-Amz-Signature=0603d6231d66a770706d51e7b253106f424cdac737dcdd6f497a15060f5c46bf&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8f1b1d60-cf1b-42b3-9faa-f634c89c3f84/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662F5234WL%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T231258Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEO%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCchzXOLv1jyq4Jha1eSuNbHCRICLjfFODWSg7XkNy1ugIgWfd9Bil16ocTbMuiMLmDcUKswpd9fKvP8LlAwxQYR8EqiAQI%2BP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJURBPniWNv1RIKhgSrcA%2BkF6IlyLQj7onHHNdxyLkPK83687%2F1UK9Zjo8HBUT3A4E82DE%2FeFeADVlrV1ML7791%2FIU3j4hFyzex6fi3VTOdhqq%2B%2FPRG%2FPnM0xzIw8Dc1YHTL0PAunpiENZVgYKHGX8rIyb4sSa8k6TMymeBumOQUMgvnjgJyVM2qnX0Iu49FGR%2FsURZb0USqVQDou5HSk4gSeFEge5WgQLITaJXW0ITSgUkQq8e1TtRx5EOhPvLouwy27lZstb5N%2Bj84PtIv%2BW7njzHsklcGlc8GDrXkZcCkYcF0DW9fQp6OqTDWwDyZ4lu8mm%2FrLQh0u2ndEdmFAnO2Fbwn1AlNNWKfxN%2BvsAbxmyvEzzzq%2FBy1eNxHyLIQfHGbLzWzzjKvBmKE1kDcYPBao51L3FADSX4Wbuc%2B19T26fzOZNCjs9rMc0SB7BDIL6hFn0bHn5i6vk8aeNQ6BLqcvYQ3RM1CTwgHuL3ru6AmLFeNnT4WMHBXtfMD0OetSm5kK0mSEEsnLiFZutv8liDnwZDgIW%2FT%2F87E1xbE8TMEKz8tmXc1BRVeIEQRZbtR%2F5mOuV%2BsRJpIeZZHAYrjzpLmiI2%2BP8GFA%2FYGjNS8Z6Bi5n6Kal3UgDc1O0vKwzcCHDvHqIAfEXP07mCMMIjm%2F7wGOqUB2Nw2JILtwJUxDkWCtianLxW89ODy6fP1ppkReC96ZXt4FzKn74GIYRHWp262u2o3dDI0vNHPQZms1GuZFWmaZ%2BSKllLdVYSJKEETYOtIn09ahlrZbbx7jr87TOoLRr9ay1kJnoRw13cf1a5ue%2FVa8LaZ6Nc0w%2Bn%2BG9iGU%2Btyv6pLDm9Qcz5z6AO3e1Ls0q3SjU6ZobA6h8yv0u94Qbv4hrUXp5as&X-Amz-Signature=2c3afc961ea14c8c910debb68e3659144d4670cf3f13c973fe8e716a97ec4ece&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/13ad0497-05fe-4eaa-984e-707b33e14761/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662F5234WL%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T231258Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEO%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCchzXOLv1jyq4Jha1eSuNbHCRICLjfFODWSg7XkNy1ugIgWfd9Bil16ocTbMuiMLmDcUKswpd9fKvP8LlAwxQYR8EqiAQI%2BP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJURBPniWNv1RIKhgSrcA%2BkF6IlyLQj7onHHNdxyLkPK83687%2F1UK9Zjo8HBUT3A4E82DE%2FeFeADVlrV1ML7791%2FIU3j4hFyzex6fi3VTOdhqq%2B%2FPRG%2FPnM0xzIw8Dc1YHTL0PAunpiENZVgYKHGX8rIyb4sSa8k6TMymeBumOQUMgvnjgJyVM2qnX0Iu49FGR%2FsURZb0USqVQDou5HSk4gSeFEge5WgQLITaJXW0ITSgUkQq8e1TtRx5EOhPvLouwy27lZstb5N%2Bj84PtIv%2BW7njzHsklcGlc8GDrXkZcCkYcF0DW9fQp6OqTDWwDyZ4lu8mm%2FrLQh0u2ndEdmFAnO2Fbwn1AlNNWKfxN%2BvsAbxmyvEzzzq%2FBy1eNxHyLIQfHGbLzWzzjKvBmKE1kDcYPBao51L3FADSX4Wbuc%2B19T26fzOZNCjs9rMc0SB7BDIL6hFn0bHn5i6vk8aeNQ6BLqcvYQ3RM1CTwgHuL3ru6AmLFeNnT4WMHBXtfMD0OetSm5kK0mSEEsnLiFZutv8liDnwZDgIW%2FT%2F87E1xbE8TMEKz8tmXc1BRVeIEQRZbtR%2F5mOuV%2BsRJpIeZZHAYrjzpLmiI2%2BP8GFA%2FYGjNS8Z6Bi5n6Kal3UgDc1O0vKwzcCHDvHqIAfEXP07mCMMIjm%2F7wGOqUB2Nw2JILtwJUxDkWCtianLxW89ODy6fP1ppkReC96ZXt4FzKn74GIYRHWp262u2o3dDI0vNHPQZms1GuZFWmaZ%2BSKllLdVYSJKEETYOtIn09ahlrZbbx7jr87TOoLRr9ay1kJnoRw13cf1a5ue%2FVa8LaZ6Nc0w%2Bn%2BG9iGU%2Btyv6pLDm9Qcz5z6AO3e1Ls0q3SjU6ZobA6h8yv0u94Qbv4hrUXp5as&X-Amz-Signature=36ec1a316a946ac4f73d6c3c6b8ca1930681e6033eb8d9f2b650c5c5c551cb2b&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 2. Box and Whisker Plot
A box plot shows the distribution of quantitative data in a way that facilitates comparisons between variables or across levels of a categorical variable. The box shows the quartiles of the dataset while the whiskers extend to show the rest of the distribution, except for points that are determined to be "outliers".
**Syntax:**
```python
sns.boxplot(x='header_1', y='header_2', data=df)
```
**Example Output:**


![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d207ae92-0a7c-4e2f-aa65-0ee5a2c33bf7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZFSUFRFL%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T231301Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEO%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIAr43U0qq2XNScTYEjGoSEili%2Fi%2FCI3Nv37hTQBS23MkAiA4nw3a9OQdcD2WQyzQ1om2gJW0OeOyF%2B589wyeUGifyiqIBAj3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM7VutZF8Ars%2FNAZvWKtwD7OHQFTHawBIJmvqdHk2sTouaVth6gqitZfmjaLDzVdSXcWMfktoe0LNmT8PooSRY%2FE1oe0ZGW4UHpARbxcJCTMX1m0efVF6xje%2F%2FgNTfgi2gSZcpIrnG7CH57ku22bt3A5%2FBse0bSwzr%2B3yzmmATxAqGM1Q4I9OgP0nkW9uvADPCgplaXHKsElQNNXiAf4r1IHCyS3HDd4c%2BZ2vFBR%2Fw2rvP4U8t5WqaOL4uXJisx8VjQQHWaiZRM%2Fu2xJJB%2Fh153ZUlfmGdkuSmvgI8DNomgtbLNQA%2F%2BrVqFIRbT98cS4GHe%2BEEc8H7csn%2BHhvQLD16nBGDxwiCgzGgALDniIrrEfabEI54DIZFhX285Iz%2FkRdfgX3jKMzHp%2BdgcnrVv3ZtUX5dkyFvLUq5GuaTC%2FINTOhnu9AoWg4c6W1cmiKYQ4EDZUF2ABBV9Z0Hmbx1Ls3IbdL3pwebAIEDAuXW7q5QOvvD%2FDOhcf8nrX%2B1Fxk0wMpOz4jaRjDD12asX6Is9T1vR40TAJ%2BetsS%2B0ZfLDYRwo5Kw1dLO2D7BUh7ngH5rKw4hHIb0RmFmbhYUoPDDukagxSvZHYaQu4DosrQ1PGN6UATQNGJeDLgcDyyXBTHVGCGMk8ee9KBTLQPwQsEwjOX%2FvAY6pgEXzJ0NeqqMKApnkpYzS6N2UQ4jJLlY5j%2Fcbl5CCYiervQNOD1V7TWQT60h9SRuM%2BQ3WHc1%2BSa%2FDnLeOfRwvb2jihnnneeQ4iW91E5lvaOxQ1C6RSSBHiNnMIecqSWi178HvSBsSpVoTcIwJjxlgpWBLMyGexdcA4ZT6m5mfqoIfprs82MqNkyWDDMtLSiYHv%2B8YP6vEAJOlYuGtu2A5XTPsX4XG17d&X-Amz-Signature=e720a8e0edda43e6b9123dc06ee49ddbaa912115c7f1edcab7435bf740cf8335&X-Amz-SignedHeaders=host&x-id=GetObject)

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0e516edc-7551-4792-ab18-0494db3c4c0c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TRNXM4QM%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T231259Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEO%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBB12OdOZcjIpCxjRunXALJctEJhVf3ffvBP6mlzE2MTAiA35nnhzexSqqegcs%2BupaZZktfXhfYKjALbBtZJ%2BI2DaiqIBAj4%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMqqtEN1XVQQHudbsXKtwDn7GZ2nZx%2BC4mSH4jv%2FM%2B4xzaUeRX67njKEZSs%2BO%2BIW6tocPwIZz%2BSPigq1jroxi8OxCpntV6VdIt0Ac%2B%2FZy8I8kUZNAWjAxuTy7DGXzUH%2FGkZNdQU15bieBIQezuQXLXftXgBclF1iJAJqxbFAEmfgUUI7A%2FLyRNusKpHRE9RgM4DmWJ1X7VOedGaI3ZETIrdR1qbXmiClbswys00aeOqgjIfTIBjqDof1ENfLN6DCHo0tupnxVzcdxVntEPXbvuBhA6mNYtnNFIpdf3Jug8F4xIRlERlRAwk%2BpsvnOo6VRcMg0S0AZ4YnD9n7cPDxbxmypZ5iSHu%2FcfU8s%2FnIMFAkh51a9ozYZD%2FlgyVkhnTJ9a1nrbspC8sD3DOQKXPFdBUUvlAIwgQ%2BeK9AsLzhdJLB4PyTcXllOXjbTfmuAmHTF0KqF8dBKn00q%2FKXWvTspKJV%2FDoYnpZsDLXP0rY9gupNmkMcDwW2CTJZNPbSwXEjpI6Pe0%2FsOgUJ0qmIhbrOrkAuOme9PbNWZT%2BUCs04Qf4hFFFCz3S39CsZPXCBA78%2BFArxz%2BtNEtzpS3NOnGAxH1P7ItCxFEkDtrRiwraSPcFKRJUezUTnh%2BrKdOn3n0Qr1DpKI%2FVss6sr9ktpYwseX%2FvAY6pgFIi9supiiccGMjCDhpHQex%2FUtDfSg%2F8NMY%2B42gg3G1fQ61xlKQPNUtY0qzUpwEYGdZyqiexBzPQAnjlR%2BwgyjXjBwbbqB3sXU1%2FdUsMqSaeTZBsymfxukNO7pYipaP6Kbynbq%2F1tdh5nOOwyF%2Bl8ZTKmD%2BXy8Bxi1CgcrgsrAtKb9mJPEXnNVTaYXyO91uZhrq70hX1Os4Cb4ygQa%2BxgYN9m5E1iub&X-Amz-Signature=96797a7443acbc1c2c02c745f42d1e50811d48e976c91c208ef3e22cc9e99392&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23a79b9d-2356-49a9-8fd9-65c6b0ab2cc5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662F5234WL%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T231258Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEO%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCchzXOLv1jyq4Jha1eSuNbHCRICLjfFODWSg7XkNy1ugIgWfd9Bil16ocTbMuiMLmDcUKswpd9fKvP8LlAwxQYR8EqiAQI%2BP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJURBPniWNv1RIKhgSrcA%2BkF6IlyLQj7onHHNdxyLkPK83687%2F1UK9Zjo8HBUT3A4E82DE%2FeFeADVlrV1ML7791%2FIU3j4hFyzex6fi3VTOdhqq%2B%2FPRG%2FPnM0xzIw8Dc1YHTL0PAunpiENZVgYKHGX8rIyb4sSa8k6TMymeBumOQUMgvnjgJyVM2qnX0Iu49FGR%2FsURZb0USqVQDou5HSk4gSeFEge5WgQLITaJXW0ITSgUkQq8e1TtRx5EOhPvLouwy27lZstb5N%2Bj84PtIv%2BW7njzHsklcGlc8GDrXkZcCkYcF0DW9fQp6OqTDWwDyZ4lu8mm%2FrLQh0u2ndEdmFAnO2Fbwn1AlNNWKfxN%2BvsAbxmyvEzzzq%2FBy1eNxHyLIQfHGbLzWzzjKvBmKE1kDcYPBao51L3FADSX4Wbuc%2B19T26fzOZNCjs9rMc0SB7BDIL6hFn0bHn5i6vk8aeNQ6BLqcvYQ3RM1CTwgHuL3ru6AmLFeNnT4WMHBXtfMD0OetSm5kK0mSEEsnLiFZutv8liDnwZDgIW%2FT%2F87E1xbE8TMEKz8tmXc1BRVeIEQRZbtR%2F5mOuV%2BsRJpIeZZHAYrjzpLmiI2%2BP8GFA%2FYGjNS8Z6Bi5n6Kal3UgDc1O0vKwzcCHDvHqIAfEXP07mCMMIjm%2F7wGOqUB2Nw2JILtwJUxDkWCtianLxW89ODy6fP1ppkReC96ZXt4FzKn74GIYRHWp262u2o3dDI0vNHPQZms1GuZFWmaZ%2BSKllLdVYSJKEETYOtIn09ahlrZbbx7jr87TOoLRr9ay1kJnoRw13cf1a5ue%2FVa8LaZ6Nc0w%2Bn%2BG9iGU%2Btyv6pLDm9Qcz5z6AO3e1Ls0q3SjU6ZobA6h8yv0u94Qbv4hrUXp5as&X-Amz-Signature=9a063e75ff65f4dbea49b8cf195df4d64c898b7d98e6a4b4f523135715a18d6e&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 4. KDE Plot
A Kernel Density Estimate (KDE) plot is a graph that creates a probability distribution curve for the data based upon its likelihood of occurrence on a specific value. This is created for a single vector of information.
**Syntax:**
```python
sns.kdeplot(X) || sns.kdeplot(df['age'])
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0d571213-2a2f-4921-a50b-880847aa05ee/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662F5234WL%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T231258Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEO%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCchzXOLv1jyq4Jha1eSuNbHCRICLjfFODWSg7XkNy1ugIgWfd9Bil16ocTbMuiMLmDcUKswpd9fKvP8LlAwxQYR8EqiAQI%2BP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJURBPniWNv1RIKhgSrcA%2BkF6IlyLQj7onHHNdxyLkPK83687%2F1UK9Zjo8HBUT3A4E82DE%2FeFeADVlrV1ML7791%2FIU3j4hFyzex6fi3VTOdhqq%2B%2FPRG%2FPnM0xzIw8Dc1YHTL0PAunpiENZVgYKHGX8rIyb4sSa8k6TMymeBumOQUMgvnjgJyVM2qnX0Iu49FGR%2FsURZb0USqVQDou5HSk4gSeFEge5WgQLITaJXW0ITSgUkQq8e1TtRx5EOhPvLouwy27lZstb5N%2Bj84PtIv%2BW7njzHsklcGlc8GDrXkZcCkYcF0DW9fQp6OqTDWwDyZ4lu8mm%2FrLQh0u2ndEdmFAnO2Fbwn1AlNNWKfxN%2BvsAbxmyvEzzzq%2FBy1eNxHyLIQfHGbLzWzzjKvBmKE1kDcYPBao51L3FADSX4Wbuc%2B19T26fzOZNCjs9rMc0SB7BDIL6hFn0bHn5i6vk8aeNQ6BLqcvYQ3RM1CTwgHuL3ru6AmLFeNnT4WMHBXtfMD0OetSm5kK0mSEEsnLiFZutv8liDnwZDgIW%2FT%2F87E1xbE8TMEKz8tmXc1BRVeIEQRZbtR%2F5mOuV%2BsRJpIeZZHAYrjzpLmiI2%2BP8GFA%2FYGjNS8Z6Bi5n6Kal3UgDc1O0vKwzcCHDvHqIAfEXP07mCMMIjm%2F7wGOqUB2Nw2JILtwJUxDkWCtianLxW89ODy6fP1ppkReC96ZXt4FzKn74GIYRHWp262u2o3dDI0vNHPQZms1GuZFWmaZ%2BSKllLdVYSJKEETYOtIn09ahlrZbbx7jr87TOoLRr9ay1kJnoRw13cf1a5ue%2FVa8LaZ6Nc0w%2Bn%2BG9iGU%2Btyv6pLDm9Qcz5z6AO3e1Ls0q3SjU6ZobA6h8yv0u94Qbv4hrUXp5as&X-Amz-Signature=7d1059bd5adf677ed2a678e5b335f0a358d2b6c07c06c08d3471b1b1a847cf55&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/53752550-ef82-4ca9-a01a-09921f0282d0/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662F5234WL%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T231258Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEO%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCchzXOLv1jyq4Jha1eSuNbHCRICLjfFODWSg7XkNy1ugIgWfd9Bil16ocTbMuiMLmDcUKswpd9fKvP8LlAwxQYR8EqiAQI%2BP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJURBPniWNv1RIKhgSrcA%2BkF6IlyLQj7onHHNdxyLkPK83687%2F1UK9Zjo8HBUT3A4E82DE%2FeFeADVlrV1ML7791%2FIU3j4hFyzex6fi3VTOdhqq%2B%2FPRG%2FPnM0xzIw8Dc1YHTL0PAunpiENZVgYKHGX8rIyb4sSa8k6TMymeBumOQUMgvnjgJyVM2qnX0Iu49FGR%2FsURZb0USqVQDou5HSk4gSeFEge5WgQLITaJXW0ITSgUkQq8e1TtRx5EOhPvLouwy27lZstb5N%2Bj84PtIv%2BW7njzHsklcGlc8GDrXkZcCkYcF0DW9fQp6OqTDWwDyZ4lu8mm%2FrLQh0u2ndEdmFAnO2Fbwn1AlNNWKfxN%2BvsAbxmyvEzzzq%2FBy1eNxHyLIQfHGbLzWzzjKvBmKE1kDcYPBao51L3FADSX4Wbuc%2B19T26fzOZNCjs9rMc0SB7BDIL6hFn0bHn5i6vk8aeNQ6BLqcvYQ3RM1CTwgHuL3ru6AmLFeNnT4WMHBXtfMD0OetSm5kK0mSEEsnLiFZutv8liDnwZDgIW%2FT%2F87E1xbE8TMEKz8tmXc1BRVeIEQRZbtR%2F5mOuV%2BsRJpIeZZHAYrjzpLmiI2%2BP8GFA%2FYGjNS8Z6Bi5n6Kal3UgDc1O0vKwzcCHDvHqIAfEXP07mCMMIjm%2F7wGOqUB2Nw2JILtwJUxDkWCtianLxW89ODy6fP1ppkReC96ZXt4FzKn74GIYRHWp262u2o3dDI0vNHPQZms1GuZFWmaZ%2BSKllLdVYSJKEETYOtIn09ahlrZbbx7jr87TOoLRr9ay1kJnoRw13cf1a5ue%2FVa8LaZ6Nc0w%2Bn%2BG9iGU%2Btyv6pLDm9Qcz5z6AO3e1Ls0q3SjU6ZobA6h8yv0u94Qbv4hrUXp5as&X-Amz-Signature=d409e8a264effa72b02c297d8e01700657f830e368d9e093a0e6601c3552446f&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
## 4. Correlation Between Variables
Correlation is a statistical measure of the extent to which different variables are interdependent. It indicates how changes in one variable are associated with changes in another variable over time.
### Positive Correlation
Positive correlation indicates that as one variable increases, the other variable also tends to increase.
**Example: Engine Size and Price**
- **Positive Correlation:** Engine size increases, price also increases.
- **Visualization:** Scatter plot with a steep positive slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c7ea9b0-3ef3-4357-a9c3-554fc71b6b15/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662UJSRIFP%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T231259Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEO%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHYfbFBxcTh4tC5li9HUQhifxlZqh0ro85ARKtnKIMy8AiEAmUD%2BjG23KOCNGW6c%2Flu8qDgk8ah2JdYnNETJ%2Buxbx8gqiAQI%2BP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHkMEhOOXeTDp8GmdCrcA04RtWI3FlYUfbzCq9DBcdOdeCjcx7Wr54%2FGhYVe7P%2BjT%2F4QzNxWmpV9%2FcB27ZcI1ZoXVNgXCRRp84%2BH%2Fh0qLeUckNBZ1a4aSAYBhBhoSbm6w7Xl9YA7L3z%2BHikuQLAgDBTwbyz7Yd5s0HDyeMKfz5x3pMpK6xL%2BLGtpv%2BeM2cHYEfuDSq9roNNlbN8293%2F67QizDtiQ%2FoDHsVSBClmLkx%2FzO589tjLP9lgBSUAxfnXFZZZolFSF4BexwZ%2BgELBU1YeRHKPjm5TBJrE4LZHJ%2FKgz9vOk8HFU0IEQZSWHTYgNa9sG7%2Fr6jO3O%2FJq5eknqHBwUV6CVBeItNd2qp3bn8or3%2B97ZLDWYS2Inu%2Bn0LITT6zrXu2uduviMpoqDgjZ8Fq6VUfSBgzQUeLQYr4QrxxqUWYuof217eWouTTozcPmYzcVIIxweW%2BpD48h3JgsKv3sybJEj9GqoAXQHPFZCpXG1bPi0WoW%2F1y06NpjsLisaN9D2Sd4%2FXg%2BSw97BKqQwyyFZ1KfJx%2BM0FPTwrBYOfXwiqaZclAAdEmlWzqaf9DRHfV%2FRkD4eXJ6WkfVShY6hN7kzgr8k7t36T5FnyAfqIRu%2B8vui0m0ZfUwjc3nJ%2FPWo%2FkCDdAQ9Ehg9R52DMMbk%2F7wGOqUBka18nT2rMSx4IAB4q8pfsMJhUhVNU1skx6K7Sp5cjS048IomtXWHyG4pgwklhNWbr7pZFBdJ4Ddt2LOMxeS03he4LtczRdEQ2ZLOXzNeZDgnGcmGrvALwufN7GIUUHf11Wt56TbNIlpIEsJea5vfVwp2YwcuR0hve%2BLX3s5IOyaSwdxu2wAvhzyzEnh0bUj88LiEIiASdbZBHw81JhJE56sgMvmt&X-Amz-Signature=c255ac6fe1cc2e5a769883d0162cdf0410ff0e37669229715d9649da78b8c687&X-Amz-SignedHeaders=host&x-id=GetObject)
**Explanation:** When engine size increases, there is a corresponding increase in the price of the vehicle. This positive correlation suggests that larger engines tend to be associated with higher prices in the market.
___
### Negative Correlation
Negative correlation indicates that as one variable increases, the other variable tends to decrease.
**Example: Highway Miles per Gallon and Price**
- **Negative Correlation:** As highway miles per gallon increases, price decreases.
- **Visualization:** Scatter plot with a steep negative slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/10f1f798-9cc4-4df2-a9c1-5a339f554a0b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WXLJSVBQ%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T231259Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEO%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDxk0Ylq52n96zlvmH5FqjAM%2FCotd1UQMK0gYErb%2FXImAiEA3FxR9lyfEXhYxArrBBP6EDozwxaXx4bfkIpjp9QUd50qiAQI%2BP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOp%2BIY2QZN9SUNWJ6SrcA0tZOT6WwuzZG4kgYCmbXx98pLDyMTGGNMfJ3FHHNdbhUu1TN1I4fzSrn%2Bu4xYyrs6bap8lvnvziCQUL%2FRw0sDSKhn4FvuJuhEFK7g3YB%2BFl%2B47iGYVBdXfl6qvDLYNE%2FG076crF%2BgRjLXVfIqebRdPjEMr4zqVW0ZEJcVsOtUZfWLuAeoCqfKTOjr6aq5JwCyDREkW%2B2mmHsikvbuUZBNmCtDrLxmq%2FP%2BpCiwRv1HZIZApi3reA0aSOkobsOBEQmwL%2F%2BwtHvnoZfVbfzhLjcikenzVqHdoOw9TJJaB%2FL6arXq76ZzSZrGx%2BslGHzlUk3XkuZqy6zvTaZkSjjU0QgFS191Z5smvxYBw9eaDzopx59euwnWUxyhXW2yVUxcV3XueGnlby0whmca6%2BeEmbkH1ryjGlSniZKBQr9KkPa8k9LAvNDLvrF0peFXJZHnpwtis5MyeRdRWvYEzRkt7CTK1MQhZgA9T8EJmhMPvjH02fbnpDOnaO9Fw07AIXCc2dO7AABt5y61xmhcDRKPlXRpy2OchYP4vCAgctjwnFHr8jBgifOX%2BnZv%2BRSb8lcssWVXyuN3%2B%2Ba8RU6Jtt%2Fj%2B%2FfR%2FUUXW4fUFluALyyONJQUuZmlGL%2BqNAFKk8pHeZMIjm%2F7wGOqUBzVjzbysxe0sFzkYvQ0km4obPygSl7FY1fSA%2BlpRmbjZ9znV8Z8fR8YO848ZMXMe4obr%2BgwckDS0LP7OCyO2VQKmHq62J7kNVuTM%2B%2FPrYNTqFGEVaJlXqY0F0U8EGh8Vd2skYLgl2%2BFpYS6LbwTMPDpH39BEeFKOUqVumI6%2BhHUmvimQRQ3lxyGlKyy8ntGNcqijNVj5g22ljIYRF96NcoLeJZqf2&X-Amz-Signature=6935e9dd505189c1552f83d3160ca3eb2883915d9cb6f7fb0b06ec4eae1fd50c&X-Amz-SignedHeaders=host&x-id=GetObject)
**Explanation:** When highway miles per gallon increases, the price of the vehicle tends to decrease. This negative correlation suggests that cars with higher fuel efficiency (more miles per gallon) are generally priced lower in the market.
___
### Weak Correlation
Weak correlation indicates a lack of strong relationship between the variables.
**Example: RPM and Price**
- **Weak Correlation:** Low and high RPM values show varied prices, indicating no strong predictive relationship.
- **Visualization:** Scatter plot with no clear trend or slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9f914514-8914-4bf4-ac84-d9e3077f6eb1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Z5Y6DJHR%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T231259Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEO%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCbJsLtxqlXZ2Oymf28xV%2FCepI%2Bvfm6ZugfbfJlEDTP4wIgazR9l2f3r28dGwPN%2FRlGFeZVHS0ds%2FshDwPYWpjO%2FjEqiAQI%2BP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFmyO%2FoIWLMNswAPmyrcA%2BGCEDi0qQaPtKtmvOtRMqnckdOYOak6BVJE78lbp73ntpYgJAlXXZEwUkuEyHrNbsg9THhXcKYtAE55S360CqpQpA9Xpq6x6mFz7tvfRK3srQvuzs7fqlw6664BqB8YU8Zdna6cod%2FnwVpnDZJ4iL59ZlG5zc0baHCLc0z1jlnjgu52q%2FtJw1VycpZB6cjP%2FZCIlPQ%2F21h%2FpQVCmouEh5v20z%2Fe9CRvGdW%2Fi6EGThe82xquqzNcGMksXh15x6vTiDEvXJkvY%2BJ2mIaP87Vd06kCl6QNWMYJfeYu2nsF5Jst04BDviNoMYHwfPD3mcuk%2FspMZK%2B%2F0T6Y35Hd0QJ1f1h%2FsW8bSlRtCbPyAuC3jFxEESOY1gJE3CIBdK10PgjufX8dqRjv98X6CFgTJFxodYJ4PfgbYIexxaa00ZCcoGLwVC9Tv9wwUBNE5ShE4i61sMJDCBTWM9YMlIQJW4d1Tq3gpcqDLLbKIJ0K9b2enRhA2qFJv%2Ff4dF%2FK00DFTETMbsRV1%2FHfok15JIB%2Fj7rTU2juauZ5AATT2TCHJCUjNHVApo3EC26YXCHFJEWHkLCGt9U7UJPAD9oxzmArEtJxYLx4QsbP8YJZr36vUhVOadBL%2B%2FESMeP%2F%2BFvGG1MnMK7k%2F7wGOqUBvDCHmyjC%2BRKXqr9IpFSCpTYWn6%2BakKy%2BgTXROvYUTVAi7GikekG5sNI15wtCcDQDCt4KQLgeh0rxBPyoSngi1fn8GF25pJ%2BzYtBLCakvAfXuEM4gQ9Iw4O9Ts0XAWizVv%2FNS9tateXMiKTWVTPzXsapJ0FPUr9WFYzWKT88tv7JEREqXVy%2BDRkuy5G8YKUUC1j8UsWISmbC0RyLqL79Am0k46PBy&X-Amz-Signature=8af49b4ad9d3870ba129b96a96b40c14e7b960fd90952da89743ffe9a5aec4f1&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f18086e5-5b04-4fbf-8309-8944ab20d213/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664J2G43PD%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T231259Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEO%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQClCVcO2y4NNhJWIGkDNo%2Fs%2FCzolAvZKqSpltsAy5s3dQIgRxxj6xPlS%2FcboYDzyq0O4RdUlx2jxrGpjZlKyRUIl1wqiAQI%2BP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDEDjryGa1baIW8qVsSrcA5Ijze3YR8z7%2F0XNSNZR3FU0lGiY733ssRePq4HQRZkmoqktX1oQmgoULYxz%2FDxVV4mtAHG1qB2%2F0QQNhGzc%2BHJFKP2etyJTLNW9426hN2Nc0UVVDZctsaRRk5OrsQIXwaKNT2qUVp4eY7o22GWEVa4lFLJGOag%2FYe5IKaNIbemcQaqzbR3i1OoffewlLt22VHrszuHrOaTUbxjC2VXG4w%2FDKNtDZkC7%2FZ%2Bs1iVJgTxRgUDGChEZbypQ%2BUrEFKRo6sFxzZC%2FQWWCiHbu%2F3FPnu5KOmbCgsVwBZBBLawp3tMmPEnwNx%2FHU7lIzM%2F1tDA24779Vdg%2F9YrreSDsMQuRx4OzqSLeHCvJP8ypfoFLT8kBRcLys7BP4giFq37iAMcEOPdr%2FN55K8KDU5ZscE15ZkM2JrLpQ4o7RvSpaVMpquE85qMIzPlZViNcbdrOl5pa8Nh0sLX2bc8o3dglY4XTGiNloEwTaXAWZLYFgwuyXw4dY5NM%2FfDbIyZcN1UcmOPVyuFheO5ljMMdgDV%2Buid6gpb7rdCPSNqZKSuTFFC6%2FIcl1uw5uQSyX6yddMj3gyaUi1fdTeRwLqvdjt0n2Xrh2i8oJahgZNUwZT8T3Q889iDpu65PmPDckAOnu0a2MNXk%2F7wGOqUBfum%2BlV3vywE0uAHtIM57cuhx7GpD8weMz3SMYUtMylkAP4pUQGocP25MUhxR3Paobif3G%2FU8d3Dzs%2BQ%2B8B%2BTbGVsXJuDIR97PHkV3qOcXP1ZBJ%2BDUKbbEVVQlLOIpLtLyHWTOcuHomlClszSpdpNndDvAKZ%2F4uC0NC6Lc6QndRlROrMBbQx0PzHNhpDMrq6r0R7KD4veJH%2Bln%2Fz5jSLlnJQc%2Fv0Q&X-Amz-Signature=323ce2342cc5a53616f0651cb9a379a2c0147e55a7be3334eb503f65cf51d01a&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Correlation Plot
Heatmap visualizes correlations among variables. Color scheme indicates Pearson correlation coefficients. Dark red diagonal line shows perfect correlation (value of 1) between variables and themselves.
This heatmap offers overview of variable relationships and their link with price.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cd3b341e-cc1a-45f7-8aec-cdc00436d270/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664J2G43PD%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T231259Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEO%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQClCVcO2y4NNhJWIGkDNo%2Fs%2FCzolAvZKqSpltsAy5s3dQIgRxxj6xPlS%2FcboYDzyq0O4RdUlx2jxrGpjZlKyRUIl1wqiAQI%2BP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDEDjryGa1baIW8qVsSrcA5Ijze3YR8z7%2F0XNSNZR3FU0lGiY733ssRePq4HQRZkmoqktX1oQmgoULYxz%2FDxVV4mtAHG1qB2%2F0QQNhGzc%2BHJFKP2etyJTLNW9426hN2Nc0UVVDZctsaRRk5OrsQIXwaKNT2qUVp4eY7o22GWEVa4lFLJGOag%2FYe5IKaNIbemcQaqzbR3i1OoffewlLt22VHrszuHrOaTUbxjC2VXG4w%2FDKNtDZkC7%2FZ%2Bs1iVJgTxRgUDGChEZbypQ%2BUrEFKRo6sFxzZC%2FQWWCiHbu%2F3FPnu5KOmbCgsVwBZBBLawp3tMmPEnwNx%2FHU7lIzM%2F1tDA24779Vdg%2F9YrreSDsMQuRx4OzqSLeHCvJP8ypfoFLT8kBRcLys7BP4giFq37iAMcEOPdr%2FN55K8KDU5ZscE15ZkM2JrLpQ4o7RvSpaVMpquE85qMIzPlZViNcbdrOl5pa8Nh0sLX2bc8o3dglY4XTGiNloEwTaXAWZLYFgwuyXw4dY5NM%2FfDbIyZcN1UcmOPVyuFheO5ljMMdgDV%2Buid6gpb7rdCPSNqZKSuTFFC6%2FIcl1uw5uQSyX6yddMj3gyaUi1fdTeRwLqvdjt0n2Xrh2i8oJahgZNUwZT8T3Q889iDpu65PmPDckAOnu0a2MNXk%2F7wGOqUBfum%2BlV3vywE0uAHtIM57cuhx7GpD8weMz3SMYUtMylkAP4pUQGocP25MUhxR3Paobif3G%2FU8d3Dzs%2BQ%2B8B%2BTbGVsXJuDIR97PHkV3qOcXP1ZBJ%2BDUKbbEVVQlLOIpLtLyHWTOcuHomlClszSpdpNndDvAKZ%2F4uC0NC6Lc6QndRlROrMBbQx0PzHNhpDMrq6r0R7KD4veJH%2Bln%2Fz5jSLlnJQc%2Fv0Q&X-Amz-Signature=5223018688587a325685a4c1a32c57635bd2c26ba1d52926ccb68b3046c4ffec&X-Amz-SignedHeaders=host&x-id=GetObject)

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
