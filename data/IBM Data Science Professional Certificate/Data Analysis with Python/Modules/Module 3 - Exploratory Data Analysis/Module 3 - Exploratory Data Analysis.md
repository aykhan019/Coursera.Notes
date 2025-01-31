

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7e6d594d-952e-44b6-97ea-31225882aea6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XURCSLNA%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T231314Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEL7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQC4Oq6GLp0EFP3XItDnoVxvPSMo%2BozD5pGClvbtmofO4QIgGhd%2BxUXwIgntbakfW10uJkhT2MUkYPC5TPoR5wSLsqEqiAQIx%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFxBRrCtT1MhHmG25SrcAxEJ8CtkfgyFwX6eTtPUyLLX5yY21MoAAZ00lWykE5fFCOSC6uIPA%2BtvKdvBpHYsvpS588teqmCI9ymXJR0yMW%2B09e2gFxLM2O6TX68tvJ5xCyI5jMaI1jA10U5JbSga8bvR%2Bt7BM%2FJxlP5Vju9Elfm%2BOX3pvTGL49yaTNLjhmBQHpsUvai%2FfqoBoowYXY8wKW4NQO73pIRwywCGTCb%2BLkPl%2BO6WB38B7hi0XkagDv6MkshovPzBjTmMai%2FzmIMVrTaZFzvEoYXDwlCvJRskaoFDZuY6MS0Jpcnn%2BsJCPOWqpgo3zbOKLtfHjtUeiEqegSxkgnGB%2BO%2BMiSLvDquAbeNG2AxP8mXVzDSkbQHX9FnDJbs3ReMu5QqByIKoRCs8alpgJbNRTTpw8gMX%2BpRYCVmWDumGRQ%2Fun8ccgpRYsE1ZhP22JrC7lz8P3S1QQakOZa7vFrYVnf1JOZDi6jk8Uqj5GaRsNAYBZAk7H8uIxmGPIFT5Lr%2Fp1eXMMgS6OVy%2FpReCsk4OaN7zEU4i%2B4uHUvLMTtUzY98C4kwD3KNoQ%2Bz80GtYuZiFK5tv5dEy8wT5iygxwuQhU9Hq9v7purG%2FPA3QumXdKzlMk0JYedErPPaS9LyHtWc1YffErYbGMNWU9bwGOqUBwP0%2FkXnTGk0BSClKjNQhplsIALRhi8DhOypGUGe4G%2BgKZ4O4yFVWuGbv%2FKMys3265d0SPlPFPXoQFFoZX74kkQKRFDcxDouo7xnZPDuOzOYQMvSrhcFSCIrBA21vQRnBjmXNInXgo4RmlXHhbCT%2BW0L5PtmkSAa%2Bg5f0EbxSFkqcGu4l37kY5xRSczOcnDaPIBs4tO1wXLSvkC19sDxrNaXSO2Gz&X-Amz-Signature=dc42a429eebf437474542b8c0f6a1f68221a631069f759168ceeda7153deab66&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cbfaed9e-b398-4902-8936-dea058b21def/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XURCSLNA%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T231314Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEL7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQC4Oq6GLp0EFP3XItDnoVxvPSMo%2BozD5pGClvbtmofO4QIgGhd%2BxUXwIgntbakfW10uJkhT2MUkYPC5TPoR5wSLsqEqiAQIx%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFxBRrCtT1MhHmG25SrcAxEJ8CtkfgyFwX6eTtPUyLLX5yY21MoAAZ00lWykE5fFCOSC6uIPA%2BtvKdvBpHYsvpS588teqmCI9ymXJR0yMW%2B09e2gFxLM2O6TX68tvJ5xCyI5jMaI1jA10U5JbSga8bvR%2Bt7BM%2FJxlP5Vju9Elfm%2BOX3pvTGL49yaTNLjhmBQHpsUvai%2FfqoBoowYXY8wKW4NQO73pIRwywCGTCb%2BLkPl%2BO6WB38B7hi0XkagDv6MkshovPzBjTmMai%2FzmIMVrTaZFzvEoYXDwlCvJRskaoFDZuY6MS0Jpcnn%2BsJCPOWqpgo3zbOKLtfHjtUeiEqegSxkgnGB%2BO%2BMiSLvDquAbeNG2AxP8mXVzDSkbQHX9FnDJbs3ReMu5QqByIKoRCs8alpgJbNRTTpw8gMX%2BpRYCVmWDumGRQ%2Fun8ccgpRYsE1ZhP22JrC7lz8P3S1QQakOZa7vFrYVnf1JOZDi6jk8Uqj5GaRsNAYBZAk7H8uIxmGPIFT5Lr%2Fp1eXMMgS6OVy%2FpReCsk4OaN7zEU4i%2B4uHUvLMTtUzY98C4kwD3KNoQ%2Bz80GtYuZiFK5tv5dEy8wT5iygxwuQhU9Hq9v7purG%2FPA3QumXdKzlMk0JYedErPPaS9LyHtWc1YffErYbGMNWU9bwGOqUBwP0%2FkXnTGk0BSClKjNQhplsIALRhi8DhOypGUGe4G%2BgKZ4O4yFVWuGbv%2FKMys3265d0SPlPFPXoQFFoZX74kkQKRFDcxDouo7xnZPDuOzOYQMvSrhcFSCIrBA21vQRnBjmXNInXgo4RmlXHhbCT%2BW0L5PtmkSAa%2Bg5f0EbxSFkqcGu4l37kY5xRSczOcnDaPIBs4tO1wXLSvkC19sDxrNaXSO2Gz&X-Amz-Signature=78c1d29ca7b869d373a4b1dee198d93b335217187aaf620ae2358ae072448162&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/91181646-b1e0-4433-9711-6259a96a9247/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XURCSLNA%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T231314Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEL7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQC4Oq6GLp0EFP3XItDnoVxvPSMo%2BozD5pGClvbtmofO4QIgGhd%2BxUXwIgntbakfW10uJkhT2MUkYPC5TPoR5wSLsqEqiAQIx%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFxBRrCtT1MhHmG25SrcAxEJ8CtkfgyFwX6eTtPUyLLX5yY21MoAAZ00lWykE5fFCOSC6uIPA%2BtvKdvBpHYsvpS588teqmCI9ymXJR0yMW%2B09e2gFxLM2O6TX68tvJ5xCyI5jMaI1jA10U5JbSga8bvR%2Bt7BM%2FJxlP5Vju9Elfm%2BOX3pvTGL49yaTNLjhmBQHpsUvai%2FfqoBoowYXY8wKW4NQO73pIRwywCGTCb%2BLkPl%2BO6WB38B7hi0XkagDv6MkshovPzBjTmMai%2FzmIMVrTaZFzvEoYXDwlCvJRskaoFDZuY6MS0Jpcnn%2BsJCPOWqpgo3zbOKLtfHjtUeiEqegSxkgnGB%2BO%2BMiSLvDquAbeNG2AxP8mXVzDSkbQHX9FnDJbs3ReMu5QqByIKoRCs8alpgJbNRTTpw8gMX%2BpRYCVmWDumGRQ%2Fun8ccgpRYsE1ZhP22JrC7lz8P3S1QQakOZa7vFrYVnf1JOZDi6jk8Uqj5GaRsNAYBZAk7H8uIxmGPIFT5Lr%2Fp1eXMMgS6OVy%2FpReCsk4OaN7zEU4i%2B4uHUvLMTtUzY98C4kwD3KNoQ%2Bz80GtYuZiFK5tv5dEy8wT5iygxwuQhU9Hq9v7purG%2FPA3QumXdKzlMk0JYedErPPaS9LyHtWc1YffErYbGMNWU9bwGOqUBwP0%2FkXnTGk0BSClKjNQhplsIALRhi8DhOypGUGe4G%2BgKZ4O4yFVWuGbv%2FKMys3265d0SPlPFPXoQFFoZX74kkQKRFDcxDouo7xnZPDuOzOYQMvSrhcFSCIrBA21vQRnBjmXNInXgo4RmlXHhbCT%2BW0L5PtmkSAa%2Bg5f0EbxSFkqcGu4l37kY5xRSczOcnDaPIBs4tO1wXLSvkC19sDxrNaXSO2Gz&X-Amz-Signature=02ee031753dfc26c5e48dc9482396072c71778303bd3e77015ac79ad8ec5aace&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/09aba1c0-0d55-41dd-852a-a04c5b8a3fac/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TQOMR6TS%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T231314Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEL7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCWaw5lIjsWwtzDCjroDB3OOxHpjzN6iPJ%2FPFRHYLNukQIgPDrGMhveefVQldlw36%2BPKKIMVV7GLt62btpTiKanRZEqiAQIx%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFNsSLoO3f9f%2BzEcPircAxyxLrL2sKEW96Gky2aEEfpP0Bwv%2FyS3wHeFiujutkbMK4axhKPylGvX9BF6XIA9ClGi2nQMREkel68nGCnL%2FTCQhFJzeHLCmOkYPogmCDIeqEByjhvyhyLNcQ5KyOv0eqOAVauakPuI2aC4WJxzKKNo7wOBjsaXbVIDpUE9T0Go7nnaHZb0JDJgmr36NJbUmTRcfdxk%2BAI0JmeXOgtKIj7pt6YHn0a1WVBg4iZOIQ0BUYLnxATDJTmSt%2FlDtY38X6AFhMxo1IUZ%2FAcEh8rmDybBSuIzcL7VjBMREhKXsaA%2FWBXCEWOW%2FUJ8FsWzO230a6m4qT8IpfLbSqA%2BOh8g7tuRAYMFYi%2F1oGw2iXgdxZgLcx8YSUupW5zKZZzsd9%2BPjMOMhswqZv6Q53XnZvnYIT%2BjF2Z4g8c2QNvxAR7p2DD09W38tX50AbtEgRzRb3sFjxp6%2Bll8JgUrwLZlnWfhZX%2FsEUhHwQrEvpOj1aLFTrpdU7e3sFv954F0MfOASlJ14c14fESRnWl6MjRJtvy7Dv8VhbN4IvqY6VemZytWikG3EE6U6wmig54vwj%2FJec2Q1sbUlyEkWd4XZqHiFIaj1MSDZGlu6DiuELR1AeQU414h%2F357ggZ7BjsflxYoMNST9bwGOqUBcTLhz7gonY9G%2Bs7z5lM%2FgFJKSdijxgFiIWbxT78hCmUUXZiz4UZV6%2FOICmCGkd%2BGEN7uAvkrouOZB2eFkjroeuT6W5FNhMZ5aNPQqu0tXFaefwMOVIjMeuVmh%2BImaikBatQI8b4NCAlUPA%2F2Rb8UhzB46bnQzLoa0Orh%2B05GgW8TJ2YiJdbpgBhtSRfbpqc2E7rz4e7ig7dunvb7XM%2Fy2Py1gT50&X-Amz-Signature=cc22375da5d367f96abd007db51a66077a421ec248ab90a5f34f98c9cc7d5293&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 2. Scatter Plot
Scatter plots present the relationship between two variables in a dataset. It represents data points on a two-dimensional plane. The independent variable or attribute is plotted on the X-axis, while the dependent variable is plotted on the Y-axis.
**Syntax:**
```python
plt.scatter(x, y)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23708af9-659f-4f23-b626-1a4292d7842c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TQOMR6TS%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T231314Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEL7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCWaw5lIjsWwtzDCjroDB3OOxHpjzN6iPJ%2FPFRHYLNukQIgPDrGMhveefVQldlw36%2BPKKIMVV7GLt62btpTiKanRZEqiAQIx%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFNsSLoO3f9f%2BzEcPircAxyxLrL2sKEW96Gky2aEEfpP0Bwv%2FyS3wHeFiujutkbMK4axhKPylGvX9BF6XIA9ClGi2nQMREkel68nGCnL%2FTCQhFJzeHLCmOkYPogmCDIeqEByjhvyhyLNcQ5KyOv0eqOAVauakPuI2aC4WJxzKKNo7wOBjsaXbVIDpUE9T0Go7nnaHZb0JDJgmr36NJbUmTRcfdxk%2BAI0JmeXOgtKIj7pt6YHn0a1WVBg4iZOIQ0BUYLnxATDJTmSt%2FlDtY38X6AFhMxo1IUZ%2FAcEh8rmDybBSuIzcL7VjBMREhKXsaA%2FWBXCEWOW%2FUJ8FsWzO230a6m4qT8IpfLbSqA%2BOh8g7tuRAYMFYi%2F1oGw2iXgdxZgLcx8YSUupW5zKZZzsd9%2BPjMOMhswqZv6Q53XnZvnYIT%2BjF2Z4g8c2QNvxAR7p2DD09W38tX50AbtEgRzRb3sFjxp6%2Bll8JgUrwLZlnWfhZX%2FsEUhHwQrEvpOj1aLFTrpdU7e3sFv954F0MfOASlJ14c14fESRnWl6MjRJtvy7Dv8VhbN4IvqY6VemZytWikG3EE6U6wmig54vwj%2FJec2Q1sbUlyEkWd4XZqHiFIaj1MSDZGlu6DiuELR1AeQU414h%2F357ggZ7BjsflxYoMNST9bwGOqUBcTLhz7gonY9G%2Bs7z5lM%2FgFJKSdijxgFiIWbxT78hCmUUXZiz4UZV6%2FOICmCGkd%2BGEN7uAvkrouOZB2eFkjroeuT6W5FNhMZ5aNPQqu0tXFaefwMOVIjMeuVmh%2BImaikBatQI8b4NCAlUPA%2F2Rb8UhzB46bnQzLoa0Orh%2B05GgW8TJ2YiJdbpgBhtSRfbpqc2E7rz4e7ig7dunvb7XM%2Fy2Py1gT50&X-Amz-Signature=25057e3a042ddcec19759daddc77ebf351033e406a8de86e53cbe0807dab20ec&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 3. Histogram
A histogram is an important visual representation of data in categorical form. To view the data in a "Binned" form, use the histogram plot with a number of bins required or with the data points that mark the bin edges. The x-axis represents the data bins, and the y-axis represents the number of elements in each bin.
**Syntax:**
```python
plt.hist(x, bins)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/24e4424a-df87-40a1-b63b-195cbdc2e0ab/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TQOMR6TS%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T231314Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEL7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCWaw5lIjsWwtzDCjroDB3OOxHpjzN6iPJ%2FPFRHYLNukQIgPDrGMhveefVQldlw36%2BPKKIMVV7GLt62btpTiKanRZEqiAQIx%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFNsSLoO3f9f%2BzEcPircAxyxLrL2sKEW96Gky2aEEfpP0Bwv%2FyS3wHeFiujutkbMK4axhKPylGvX9BF6XIA9ClGi2nQMREkel68nGCnL%2FTCQhFJzeHLCmOkYPogmCDIeqEByjhvyhyLNcQ5KyOv0eqOAVauakPuI2aC4WJxzKKNo7wOBjsaXbVIDpUE9T0Go7nnaHZb0JDJgmr36NJbUmTRcfdxk%2BAI0JmeXOgtKIj7pt6YHn0a1WVBg4iZOIQ0BUYLnxATDJTmSt%2FlDtY38X6AFhMxo1IUZ%2FAcEh8rmDybBSuIzcL7VjBMREhKXsaA%2FWBXCEWOW%2FUJ8FsWzO230a6m4qT8IpfLbSqA%2BOh8g7tuRAYMFYi%2F1oGw2iXgdxZgLcx8YSUupW5zKZZzsd9%2BPjMOMhswqZv6Q53XnZvnYIT%2BjF2Z4g8c2QNvxAR7p2DD09W38tX50AbtEgRzRb3sFjxp6%2Bll8JgUrwLZlnWfhZX%2FsEUhHwQrEvpOj1aLFTrpdU7e3sFv954F0MfOASlJ14c14fESRnWl6MjRJtvy7Dv8VhbN4IvqY6VemZytWikG3EE6U6wmig54vwj%2FJec2Q1sbUlyEkWd4XZqHiFIaj1MSDZGlu6DiuELR1AeQU414h%2F357ggZ7BjsflxYoMNST9bwGOqUBcTLhz7gonY9G%2Bs7z5lM%2FgFJKSdijxgFiIWbxT78hCmUUXZiz4UZV6%2FOICmCGkd%2BGEN7uAvkrouOZB2eFkjroeuT6W5FNhMZ5aNPQqu0tXFaefwMOVIjMeuVmh%2BImaikBatQI8b4NCAlUPA%2F2Rb8UhzB46bnQzLoa0Orh%2B05GgW8TJ2YiJdbpgBhtSRfbpqc2E7rz4e7ig7dunvb7XM%2Fy2Py1gT50&X-Amz-Signature=c977ac12e891252ac29693002abdde29869a3bcbdf6ee0318609be37e2b148c8&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ab5a6dfe-51f5-43ee-bcb3-33dae4a1c7ad/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TQOMR6TS%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T231314Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEL7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCWaw5lIjsWwtzDCjroDB3OOxHpjzN6iPJ%2FPFRHYLNukQIgPDrGMhveefVQldlw36%2BPKKIMVV7GLt62btpTiKanRZEqiAQIx%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFNsSLoO3f9f%2BzEcPircAxyxLrL2sKEW96Gky2aEEfpP0Bwv%2FyS3wHeFiujutkbMK4axhKPylGvX9BF6XIA9ClGi2nQMREkel68nGCnL%2FTCQhFJzeHLCmOkYPogmCDIeqEByjhvyhyLNcQ5KyOv0eqOAVauakPuI2aC4WJxzKKNo7wOBjsaXbVIDpUE9T0Go7nnaHZb0JDJgmr36NJbUmTRcfdxk%2BAI0JmeXOgtKIj7pt6YHn0a1WVBg4iZOIQ0BUYLnxATDJTmSt%2FlDtY38X6AFhMxo1IUZ%2FAcEh8rmDybBSuIzcL7VjBMREhKXsaA%2FWBXCEWOW%2FUJ8FsWzO230a6m4qT8IpfLbSqA%2BOh8g7tuRAYMFYi%2F1oGw2iXgdxZgLcx8YSUupW5zKZZzsd9%2BPjMOMhswqZv6Q53XnZvnYIT%2BjF2Z4g8c2QNvxAR7p2DD09W38tX50AbtEgRzRb3sFjxp6%2Bll8JgUrwLZlnWfhZX%2FsEUhHwQrEvpOj1aLFTrpdU7e3sFv954F0MfOASlJ14c14fESRnWl6MjRJtvy7Dv8VhbN4IvqY6VemZytWikG3EE6U6wmig54vwj%2FJec2Q1sbUlyEkWd4XZqHiFIaj1MSDZGlu6DiuELR1AeQU414h%2F357ggZ7BjsflxYoMNST9bwGOqUBcTLhz7gonY9G%2Bs7z5lM%2FgFJKSdijxgFiIWbxT78hCmUUXZiz4UZV6%2FOICmCGkd%2BGEN7uAvkrouOZB2eFkjroeuT6W5FNhMZ5aNPQqu0tXFaefwMOVIjMeuVmh%2BImaikBatQI8b4NCAlUPA%2F2Rb8UhzB46bnQzLoa0Orh%2B05GgW8TJ2YiJdbpgBhtSRfbpqc2E7rz4e7ig7dunvb7XM%2Fy2Py1gT50&X-Amz-Signature=085a9446d35433b67d3bf3e152154e1e66c6d455ea687e479432e57f95c23734&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8f1b1d60-cf1b-42b3-9faa-f634c89c3f84/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TQOMR6TS%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T231314Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEL7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCWaw5lIjsWwtzDCjroDB3OOxHpjzN6iPJ%2FPFRHYLNukQIgPDrGMhveefVQldlw36%2BPKKIMVV7GLt62btpTiKanRZEqiAQIx%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFNsSLoO3f9f%2BzEcPircAxyxLrL2sKEW96Gky2aEEfpP0Bwv%2FyS3wHeFiujutkbMK4axhKPylGvX9BF6XIA9ClGi2nQMREkel68nGCnL%2FTCQhFJzeHLCmOkYPogmCDIeqEByjhvyhyLNcQ5KyOv0eqOAVauakPuI2aC4WJxzKKNo7wOBjsaXbVIDpUE9T0Go7nnaHZb0JDJgmr36NJbUmTRcfdxk%2BAI0JmeXOgtKIj7pt6YHn0a1WVBg4iZOIQ0BUYLnxATDJTmSt%2FlDtY38X6AFhMxo1IUZ%2FAcEh8rmDybBSuIzcL7VjBMREhKXsaA%2FWBXCEWOW%2FUJ8FsWzO230a6m4qT8IpfLbSqA%2BOh8g7tuRAYMFYi%2F1oGw2iXgdxZgLcx8YSUupW5zKZZzsd9%2BPjMOMhswqZv6Q53XnZvnYIT%2BjF2Z4g8c2QNvxAR7p2DD09W38tX50AbtEgRzRb3sFjxp6%2Bll8JgUrwLZlnWfhZX%2FsEUhHwQrEvpOj1aLFTrpdU7e3sFv954F0MfOASlJ14c14fESRnWl6MjRJtvy7Dv8VhbN4IvqY6VemZytWikG3EE6U6wmig54vwj%2FJec2Q1sbUlyEkWd4XZqHiFIaj1MSDZGlu6DiuELR1AeQU414h%2F357ggZ7BjsflxYoMNST9bwGOqUBcTLhz7gonY9G%2Bs7z5lM%2FgFJKSdijxgFiIWbxT78hCmUUXZiz4UZV6%2FOICmCGkd%2BGEN7uAvkrouOZB2eFkjroeuT6W5FNhMZ5aNPQqu0tXFaefwMOVIjMeuVmh%2BImaikBatQI8b4NCAlUPA%2F2Rb8UhzB46bnQzLoa0Orh%2B05GgW8TJ2YiJdbpgBhtSRfbpqc2E7rz4e7ig7dunvb7XM%2Fy2Py1gT50&X-Amz-Signature=9257b42444aec9f8a296d30c62283e66625de55656ddf9d15af781bd762116e3&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/13ad0497-05fe-4eaa-984e-707b33e14761/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TQOMR6TS%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T231314Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEL7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCWaw5lIjsWwtzDCjroDB3OOxHpjzN6iPJ%2FPFRHYLNukQIgPDrGMhveefVQldlw36%2BPKKIMVV7GLt62btpTiKanRZEqiAQIx%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFNsSLoO3f9f%2BzEcPircAxyxLrL2sKEW96Gky2aEEfpP0Bwv%2FyS3wHeFiujutkbMK4axhKPylGvX9BF6XIA9ClGi2nQMREkel68nGCnL%2FTCQhFJzeHLCmOkYPogmCDIeqEByjhvyhyLNcQ5KyOv0eqOAVauakPuI2aC4WJxzKKNo7wOBjsaXbVIDpUE9T0Go7nnaHZb0JDJgmr36NJbUmTRcfdxk%2BAI0JmeXOgtKIj7pt6YHn0a1WVBg4iZOIQ0BUYLnxATDJTmSt%2FlDtY38X6AFhMxo1IUZ%2FAcEh8rmDybBSuIzcL7VjBMREhKXsaA%2FWBXCEWOW%2FUJ8FsWzO230a6m4qT8IpfLbSqA%2BOh8g7tuRAYMFYi%2F1oGw2iXgdxZgLcx8YSUupW5zKZZzsd9%2BPjMOMhswqZv6Q53XnZvnYIT%2BjF2Z4g8c2QNvxAR7p2DD09W38tX50AbtEgRzRb3sFjxp6%2Bll8JgUrwLZlnWfhZX%2FsEUhHwQrEvpOj1aLFTrpdU7e3sFv954F0MfOASlJ14c14fESRnWl6MjRJtvy7Dv8VhbN4IvqY6VemZytWikG3EE6U6wmig54vwj%2FJec2Q1sbUlyEkWd4XZqHiFIaj1MSDZGlu6DiuELR1AeQU414h%2F357ggZ7BjsflxYoMNST9bwGOqUBcTLhz7gonY9G%2Bs7z5lM%2FgFJKSdijxgFiIWbxT78hCmUUXZiz4UZV6%2FOICmCGkd%2BGEN7uAvkrouOZB2eFkjroeuT6W5FNhMZ5aNPQqu0tXFaefwMOVIjMeuVmh%2BImaikBatQI8b4NCAlUPA%2F2Rb8UhzB46bnQzLoa0Orh%2B05GgW8TJ2YiJdbpgBhtSRfbpqc2E7rz4e7ig7dunvb7XM%2Fy2Py1gT50&X-Amz-Signature=0ecf28b5a72c4a60be553c938bbcc994a0a85fd170e655da73310ce9c1e41da0&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 2. Box and Whisker Plot
A box plot shows the distribution of quantitative data in a way that facilitates comparisons between variables or across levels of a categorical variable. The box shows the quartiles of the dataset while the whiskers extend to show the rest of the distribution, except for points that are determined to be "outliers".
**Syntax:**
```python
sns.boxplot(x='header_1', y='header_2', data=df)
```
**Example Output:**


![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d207ae92-0a7c-4e2f-aa65-0ee5a2c33bf7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TNHU3A6O%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T231319Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEL7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIG01CcBv67eL6lrvBBVQE7q47ZICm0erDoOl8E9RJ5oGAiEAoLaNGC6w6V2OTBG0VrYH2gF9Snl0rvmDocbAXeBmWzgqiAQIx%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJ5yeQb6lYyXT95zuircA5OTuQAxcgkNSA7luOlRgEW48RbY4WeGnxnxZyemQsypx4sZmJFHscXOtX2mQFzHXdP8d2uYBeW8emhqjSNqejyeEB2rzPBUzHOuZC80U7QEEEpkN4dO2qtI43HPOwWjTmTw9MbZmjFYVqFR3qbOsSHfEAG6CN1%2F7fnmoPoI%2B3GLj6ay0g%2B3Numk59Q2Um0j%2BdgGMYW5Y5ruSrmeGmCtTslhudl%2BNg0MNbwNuy42Yzxe9f1hAn69jjU1ugA9CqJkSywFW3Wem0qyGPLw9dQFYYPFbBBemy8OvpZ5eBuWRlVFAmoAvDg0Ivb15vPvhkDtkv70bC%2F5r3zRlvT%2FJIykcXhC2T25FPRzLMgBwKtv0iZ6AmAUCSfEAvtUTB9CtsF3%2BJqYtPRfKTfaXjlfpl6GKMU2OKKkrD3Z3TRYhNq5uwR0PTqPd5%2F5vw3x2pXLoJFXqruUQjLzcewYCr7L1FzPiQDoi2Ddm0r%2BC5UoSP6LQRe1EsFtFUlYbha1ejXLwPq25A%2FjpxAEsF5Zv2uEOg5MvisI%2BmwBl%2Fl1IyZ%2BXwAYPSZ%2BtdiKYHDUD61uzbXL7omMDmA%2F7UYrI7ChktJN5vDyuJHseccKC3R9uEsn9yIlaMyq4YHAQTVuKCVQleVHMO%2BT9bwGOqUBnmKXYh4jTe9hl7fMoRN6sbcB0DRDH%2BdhA%2BbwMelCg7rb4n8NM%2BxLlEC2sVlorfFfGt6rHjCgGCO5QWxIrsYBN6sAWZhMN3slNEsLpONPTJxwHutdx0d4SP0pyDKMS3AIaMUu0kdVS5e3SxU9fZ1EvAT0%2B4OkQ4%2FvpebAXvSI8BLXFrDWlS8EL9ctNQMT1OyDwbbMU%2Bo4IfqA472VCgec6p2bOgNX&X-Amz-Signature=0125c914e8c90ea958ee7bb4f693b56dff8da7ac953e14a2ecf2c5af0287b293&X-Amz-SignedHeaders=host&x-id=GetObject)

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0e516edc-7551-4792-ab18-0494db3c4c0c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667YAJAT4J%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T231319Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEL7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCZwiLSXBi4cuFctQH5pRO04eQIG0ecpfQF4q%2BCiwBQAgIhAJcmmgPoyNfiUrvYQr%2BJD5qHAAKpwJ%2FMSm782x3pkS0kKogECMf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgySlymNhnYF1S9y%2Bq8q3APz6nJAqW%2FyZv3k3WpHDLh3Pwob0FUq44Vm%2BNhV3ZyDDPkPW7upxz4YGYmI9nyZFJnc5X25IFjAfZAW2dD%2FmIslhHEG3VmlwjX%2F3r%2BQShQ69VGlH4SUeJ9z0YGFZsfxjuMm29MskrSlwVhgWHea9diJCvYXuX%2Bjd%2BG126EQSup%2BqncZ56fBEr9om8TYqK3F0kTjAmSawvUm8frPuxLtXcvFDN7%2Bfi6oVV9vcDaMd7sB6Zuix5tzkZn4qCUv4XRLf%2F4ByBxZXuh%2B4NNkGRLbPg%2FB%2F3Z86hQexypOyKkur8Ll0r6IeA8ElLrUoRdbqEERvEToQleanrriHdkHqN4uMcMq0ClHHuLFhUHJpn98oEGU4Qdb%2Bp6a337SYKD6gQxuTb7XHfc8STmZGh9YZoaeaAmXn55dfwZ5P5FNvAt3H9gTZIpX43YJMJ0fznM%2BiWomRdInUNaXTMX4f%2FbpLMYJ7VXlReHgjFxIgJL9pz5AyWKVHEal3pBF6%2Ffq8AuZW6x4ozvt6f1iPZMhONcxX8xvALiJGE2h0n%2BX0jGRAyM5UtKOstnJEr1trz7pDIAeeHT088D1aFXcDgk8wd0oYumgJS8bfdWF9eNJU3E3WU570EhYT6d%2FtDSNocIDXi2YGDDUlPW8BjqkAXVOHwfEjII0ed4v7DJp4T%2Bv%2B9rI5%2BPqBMvj5WwzDFoh6jKwd%2Febgqso8zcO8EB7%2FzLboSc%2B5TEq38LZBjtXOe0Xr73W2avY72tuosV48%2BLsUiLLbVbsmT9WBraH0Ih8QS2dclR3O3tVQiy7454FX3tFcTqOkR2B46tAVF1kLovJJndt%2BJ6%2FgFKmVlqp%2F5GuBPtEAKntjJRFSVCuk50MdsRoALaH&X-Amz-Signature=c0d2bc8c6880fcd897a139014c300e6e5aca99704f10b37ed4551cfe7538553b&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23a79b9d-2356-49a9-8fd9-65c6b0ab2cc5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TQOMR6TS%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T231314Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEL7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCWaw5lIjsWwtzDCjroDB3OOxHpjzN6iPJ%2FPFRHYLNukQIgPDrGMhveefVQldlw36%2BPKKIMVV7GLt62btpTiKanRZEqiAQIx%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFNsSLoO3f9f%2BzEcPircAxyxLrL2sKEW96Gky2aEEfpP0Bwv%2FyS3wHeFiujutkbMK4axhKPylGvX9BF6XIA9ClGi2nQMREkel68nGCnL%2FTCQhFJzeHLCmOkYPogmCDIeqEByjhvyhyLNcQ5KyOv0eqOAVauakPuI2aC4WJxzKKNo7wOBjsaXbVIDpUE9T0Go7nnaHZb0JDJgmr36NJbUmTRcfdxk%2BAI0JmeXOgtKIj7pt6YHn0a1WVBg4iZOIQ0BUYLnxATDJTmSt%2FlDtY38X6AFhMxo1IUZ%2FAcEh8rmDybBSuIzcL7VjBMREhKXsaA%2FWBXCEWOW%2FUJ8FsWzO230a6m4qT8IpfLbSqA%2BOh8g7tuRAYMFYi%2F1oGw2iXgdxZgLcx8YSUupW5zKZZzsd9%2BPjMOMhswqZv6Q53XnZvnYIT%2BjF2Z4g8c2QNvxAR7p2DD09W38tX50AbtEgRzRb3sFjxp6%2Bll8JgUrwLZlnWfhZX%2FsEUhHwQrEvpOj1aLFTrpdU7e3sFv954F0MfOASlJ14c14fESRnWl6MjRJtvy7Dv8VhbN4IvqY6VemZytWikG3EE6U6wmig54vwj%2FJec2Q1sbUlyEkWd4XZqHiFIaj1MSDZGlu6DiuELR1AeQU414h%2F357ggZ7BjsflxYoMNST9bwGOqUBcTLhz7gonY9G%2Bs7z5lM%2FgFJKSdijxgFiIWbxT78hCmUUXZiz4UZV6%2FOICmCGkd%2BGEN7uAvkrouOZB2eFkjroeuT6W5FNhMZ5aNPQqu0tXFaefwMOVIjMeuVmh%2BImaikBatQI8b4NCAlUPA%2F2Rb8UhzB46bnQzLoa0Orh%2B05GgW8TJ2YiJdbpgBhtSRfbpqc2E7rz4e7ig7dunvb7XM%2Fy2Py1gT50&X-Amz-Signature=37c26217d5d5322ab1daea38926b2aef4d3532f49c6a32b30ce4309fac81985a&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 4. KDE Plot
A Kernel Density Estimate (KDE) plot is a graph that creates a probability distribution curve for the data based upon its likelihood of occurrence on a specific value. This is created for a single vector of information.
**Syntax:**
```python
sns.kdeplot(X) || sns.kdeplot(df['age'])
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0d571213-2a2f-4921-a50b-880847aa05ee/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TQOMR6TS%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T231314Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEL7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCWaw5lIjsWwtzDCjroDB3OOxHpjzN6iPJ%2FPFRHYLNukQIgPDrGMhveefVQldlw36%2BPKKIMVV7GLt62btpTiKanRZEqiAQIx%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFNsSLoO3f9f%2BzEcPircAxyxLrL2sKEW96Gky2aEEfpP0Bwv%2FyS3wHeFiujutkbMK4axhKPylGvX9BF6XIA9ClGi2nQMREkel68nGCnL%2FTCQhFJzeHLCmOkYPogmCDIeqEByjhvyhyLNcQ5KyOv0eqOAVauakPuI2aC4WJxzKKNo7wOBjsaXbVIDpUE9T0Go7nnaHZb0JDJgmr36NJbUmTRcfdxk%2BAI0JmeXOgtKIj7pt6YHn0a1WVBg4iZOIQ0BUYLnxATDJTmSt%2FlDtY38X6AFhMxo1IUZ%2FAcEh8rmDybBSuIzcL7VjBMREhKXsaA%2FWBXCEWOW%2FUJ8FsWzO230a6m4qT8IpfLbSqA%2BOh8g7tuRAYMFYi%2F1oGw2iXgdxZgLcx8YSUupW5zKZZzsd9%2BPjMOMhswqZv6Q53XnZvnYIT%2BjF2Z4g8c2QNvxAR7p2DD09W38tX50AbtEgRzRb3sFjxp6%2Bll8JgUrwLZlnWfhZX%2FsEUhHwQrEvpOj1aLFTrpdU7e3sFv954F0MfOASlJ14c14fESRnWl6MjRJtvy7Dv8VhbN4IvqY6VemZytWikG3EE6U6wmig54vwj%2FJec2Q1sbUlyEkWd4XZqHiFIaj1MSDZGlu6DiuELR1AeQU414h%2F357ggZ7BjsflxYoMNST9bwGOqUBcTLhz7gonY9G%2Bs7z5lM%2FgFJKSdijxgFiIWbxT78hCmUUXZiz4UZV6%2FOICmCGkd%2BGEN7uAvkrouOZB2eFkjroeuT6W5FNhMZ5aNPQqu0tXFaefwMOVIjMeuVmh%2BImaikBatQI8b4NCAlUPA%2F2Rb8UhzB46bnQzLoa0Orh%2B05GgW8TJ2YiJdbpgBhtSRfbpqc2E7rz4e7ig7dunvb7XM%2Fy2Py1gT50&X-Amz-Signature=310fa737b36b691cc811de1087db7f2f648fead95a60dc74fc4a6c4524799d87&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/53752550-ef82-4ca9-a01a-09921f0282d0/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TQOMR6TS%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T231314Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEL7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCWaw5lIjsWwtzDCjroDB3OOxHpjzN6iPJ%2FPFRHYLNukQIgPDrGMhveefVQldlw36%2BPKKIMVV7GLt62btpTiKanRZEqiAQIx%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFNsSLoO3f9f%2BzEcPircAxyxLrL2sKEW96Gky2aEEfpP0Bwv%2FyS3wHeFiujutkbMK4axhKPylGvX9BF6XIA9ClGi2nQMREkel68nGCnL%2FTCQhFJzeHLCmOkYPogmCDIeqEByjhvyhyLNcQ5KyOv0eqOAVauakPuI2aC4WJxzKKNo7wOBjsaXbVIDpUE9T0Go7nnaHZb0JDJgmr36NJbUmTRcfdxk%2BAI0JmeXOgtKIj7pt6YHn0a1WVBg4iZOIQ0BUYLnxATDJTmSt%2FlDtY38X6AFhMxo1IUZ%2FAcEh8rmDybBSuIzcL7VjBMREhKXsaA%2FWBXCEWOW%2FUJ8FsWzO230a6m4qT8IpfLbSqA%2BOh8g7tuRAYMFYi%2F1oGw2iXgdxZgLcx8YSUupW5zKZZzsd9%2BPjMOMhswqZv6Q53XnZvnYIT%2BjF2Z4g8c2QNvxAR7p2DD09W38tX50AbtEgRzRb3sFjxp6%2Bll8JgUrwLZlnWfhZX%2FsEUhHwQrEvpOj1aLFTrpdU7e3sFv954F0MfOASlJ14c14fESRnWl6MjRJtvy7Dv8VhbN4IvqY6VemZytWikG3EE6U6wmig54vwj%2FJec2Q1sbUlyEkWd4XZqHiFIaj1MSDZGlu6DiuELR1AeQU414h%2F357ggZ7BjsflxYoMNST9bwGOqUBcTLhz7gonY9G%2Bs7z5lM%2FgFJKSdijxgFiIWbxT78hCmUUXZiz4UZV6%2FOICmCGkd%2BGEN7uAvkrouOZB2eFkjroeuT6W5FNhMZ5aNPQqu0tXFaefwMOVIjMeuVmh%2BImaikBatQI8b4NCAlUPA%2F2Rb8UhzB46bnQzLoa0Orh%2B05GgW8TJ2YiJdbpgBhtSRfbpqc2E7rz4e7ig7dunvb7XM%2Fy2Py1gT50&X-Amz-Signature=04c92bd837defd3e9cfd97c439a1e021caf9a42e0c1a1988bc6f7d90fa986b36&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
## 4. Correlation Between Variables
Correlation is a statistical measure of the extent to which different variables are interdependent. It indicates how changes in one variable are associated with changes in another variable over time.
### Positive Correlation
Positive correlation indicates that as one variable increases, the other variable also tends to increase.
**Example: Engine Size and Price**
- **Positive Correlation:** Engine size increases, price also increases.
- **Visualization:** Scatter plot with a steep positive slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c7ea9b0-3ef3-4357-a9c3-554fc71b6b15/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VQJ7SCAU%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T231315Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEL7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGnkQa2Ovfc%2F5Fy6U9YvjkCqnsopIknSh9QFrNFk78FWAiEA5V%2B9%2Fhc2j9Lq%2FF1jj5h3xj5UDMAH8JQknq2IFAd8x0sqiAQIx%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKfRL%2F%2B5OpQ%2BwAAI4ircA%2BCJgLOYcAb4gDGR9%2FW4qY%2FcXfqg1ECo19rRig9zlH0HqJIsMixMeYOXMmLCOWZNyVfQFQ2Np9Wpw4LY1hixJKBMg25RBSwoFn4z%2BD3f0%2Fa9YqeurZAIOcItatcQLNt%2BeYMCzdTKulzz6VmpYYuLu9u8LxFGZV7vQD86lpHqb1AoIAMpTI0yOMWI07yLkcPda34AkdOsuUVsd9VhLOTu4ZACt4qm95UsCXene1CF2UebkM11aVdvnbiHqxyozYXW0cTjf%2F8oj2dbk87N2cDTxouJFXRUYIA9sjqozipv8xJxkKpONNiOHrKoKF%2FOxkigjNxy5oCE%2BfDeS0QX8emEQysAedtawboETaR2NV7SYeD2MUxCbCSyrwoa9ay0gQX9I6SdYqkdFR4V%2BWaxINMxLClDOGOBWi5Mx3YIpyIlAY%2BHUxxHIu%2Bej%2BrizF%2FeIJlhfhCXl3lK4DGkDn84np4JNJu2iOZZ%2B6Zru%2F5MjOtcVVTm0Jbzp7AJoOezX8m116iAIMm3q91D%2F7m1Znf6angjFetJ54oFTxYoalCOsrA2Xu8Z0cfaWL1iAj4lsGQZT2KvSC6lEL3wP8og0RnjWjJvv1xLsEu3wwLWtItUexGx9iamvkNPd%2BwSU3QM4uUDMLSU9bwGOqUBvwjB8LQl%2BlUjEtyktcoBdBz%2BoAPebprr9L6KLRX%2FHgOnqZnCVgTLfmtWstn%2F6qQrPVrp3MJP5OvyjB4rD5WpvnKqcG6djzCXjf46h4w92cR6RNK6MXwTwGWoUWju%2BwhUix8RUXXNvUaPcv4yTv2Hai2gjQjrXoJip6IqHlKSjSiYKJfdYxoqO%2BgJxmgbMqRZIR9kHie%2Bvs59c5uu45lQ7yQoPQ0G&X-Amz-Signature=cf7b140df963e583e0a80a3cb5674dec4dd6298db545505632247b08319bde5f&X-Amz-SignedHeaders=host&x-id=GetObject)
**Explanation:** When engine size increases, there is a corresponding increase in the price of the vehicle. This positive correlation suggests that larger engines tend to be associated with higher prices in the market.
___
### Negative Correlation
Negative correlation indicates that as one variable increases, the other variable tends to decrease.
**Example: Highway Miles per Gallon and Price**
- **Negative Correlation:** As highway miles per gallon increases, price decreases.
- **Visualization:** Scatter plot with a steep negative slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/10f1f798-9cc4-4df2-a9c1-5a339f554a0b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665QBEHODC%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T231315Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEL7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCV7GqSpQfOnGTX2OG5fAvj4xow9M2vE3V%2FnvvR33kvqAIgR1jbsUQFUz4p4Dsb6kU7BbjPfhlipOHAnkHpkA7PWFEqiAQIx%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOqxqvbg6R3YCCOqNCrcAzQjwv3lUBtBhUOXKAO3MJBTbszes608H3zjD4e7LZlTTTp25Re4hX4ImyEpA5D7BroJm6xKOmTGWTW38i1OZO5R5%2FcyOYQyybszhmqsPjBwVPK9lIUfkFMtDi5hPeje1%2BMVVU8Wnx%2FOjV8iyqKxDMOK4l5QshVArEO2gvJiAJfX4cEE9UihPiqi%2FeXyJ%2B1kKvX3DpTcYGSr4O2ebikssH6krvgJmblT9owPcQaiDkp45NcNtepgMDvGkhaMXTcMXprfwyb4Vs76Upt0NVqajuQw41%2Bc6hVTN4JotZ%2FOCzsTxvQQj3zDVuPQirx7gSQ5vj9YFe6qQ6m7lMxup8aYM0hR3LCSOYiOrjJAD3FgcQO9L8kSVwNkqf3647kEVxPDSzw6qoXB49xLK8cqnLfTbz8zj697ip4nG9cPJfcIqlPNCOgnKZzyakJvkRKp5Q%2FD7CGtVCDoLpVQMk8XtqpEWbAmoRZ0ypyuZKrglqPb28Q%2FV4RgKnoPncru2tEA%2By%2B2wCx1p3RKI%2Bvy9SWVJpSt4q2RRxRf6%2FqTgOBQPa6ya1PGaiKeIImhzSlXHmw8sLjE9bpThM3nl74mCE3rN5UtmRa4Ml0OoCtbEBtDiMK%2BzRcvcwavsBv5QRem%2FGJsMIqU9bwGOqUBZM6acbZBPugVyYK6oKgi3jx4fTdKdJ7bPmNfufy3XEtCpcqMH%2BUw4W0Unk3vyekiMa0chTZtSpPkAGag0jwqBoJXR0G51usBZv5YPeShddcwzZCU3OH%2BngSjH0%2BfqTp0nBl86Kq6wPpkEajQALopKhUi2agfW%2BpQEbbc6fQHO9KhizRrihQQBqoJBdrfanmzJH6Ex9ZrgnbcSXc6ssgAdQp8enx%2F&X-Amz-Signature=b97d05684d15b12b45dc32feb480bdc7c4ecd1a193443daa20d58a2f915fed8a&X-Amz-SignedHeaders=host&x-id=GetObject)
**Explanation:** When highway miles per gallon increases, the price of the vehicle tends to decrease. This negative correlation suggests that cars with higher fuel efficiency (more miles per gallon) are generally priced lower in the market.
___
### Weak Correlation
Weak correlation indicates a lack of strong relationship between the variables.
**Example: RPM and Price**
- **Weak Correlation:** Low and high RPM values show varied prices, indicating no strong predictive relationship.
- **Visualization:** Scatter plot with no clear trend or slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9f914514-8914-4bf4-ac84-d9e3077f6eb1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TNHU3A6O%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T231315Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEL7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIG01CcBv67eL6lrvBBVQE7q47ZICm0erDoOl8E9RJ5oGAiEAoLaNGC6w6V2OTBG0VrYH2gF9Snl0rvmDocbAXeBmWzgqiAQIx%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJ5yeQb6lYyXT95zuircA5OTuQAxcgkNSA7luOlRgEW48RbY4WeGnxnxZyemQsypx4sZmJFHscXOtX2mQFzHXdP8d2uYBeW8emhqjSNqejyeEB2rzPBUzHOuZC80U7QEEEpkN4dO2qtI43HPOwWjTmTw9MbZmjFYVqFR3qbOsSHfEAG6CN1%2F7fnmoPoI%2B3GLj6ay0g%2B3Numk59Q2Um0j%2BdgGMYW5Y5ruSrmeGmCtTslhudl%2BNg0MNbwNuy42Yzxe9f1hAn69jjU1ugA9CqJkSywFW3Wem0qyGPLw9dQFYYPFbBBemy8OvpZ5eBuWRlVFAmoAvDg0Ivb15vPvhkDtkv70bC%2F5r3zRlvT%2FJIykcXhC2T25FPRzLMgBwKtv0iZ6AmAUCSfEAvtUTB9CtsF3%2BJqYtPRfKTfaXjlfpl6GKMU2OKKkrD3Z3TRYhNq5uwR0PTqPd5%2F5vw3x2pXLoJFXqruUQjLzcewYCr7L1FzPiQDoi2Ddm0r%2BC5UoSP6LQRe1EsFtFUlYbha1ejXLwPq25A%2FjpxAEsF5Zv2uEOg5MvisI%2BmwBl%2Fl1IyZ%2BXwAYPSZ%2BtdiKYHDUD61uzbXL7omMDmA%2F7UYrI7ChktJN5vDyuJHseccKC3R9uEsn9yIlaMyq4YHAQTVuKCVQleVHMO%2BT9bwGOqUBnmKXYh4jTe9hl7fMoRN6sbcB0DRDH%2BdhA%2BbwMelCg7rb4n8NM%2BxLlEC2sVlorfFfGt6rHjCgGCO5QWxIrsYBN6sAWZhMN3slNEsLpONPTJxwHutdx0d4SP0pyDKMS3AIaMUu0kdVS5e3SxU9fZ1EvAT0%2B4OkQ4%2FvpebAXvSI8BLXFrDWlS8EL9ctNQMT1OyDwbbMU%2Bo4IfqA472VCgec6p2bOgNX&X-Amz-Signature=fbd293b879b0211edb3404717e8c21332665a1655f2394b7db5409be431c54e0&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f18086e5-5b04-4fbf-8309-8944ab20d213/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZDLNTQSG%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T231315Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEL7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIAICLuY7mpKIPUX%2FAAuUuMMBaitFnkVOm5vDbcjrtig9AiAdGCuWKryI8n4wgbwfrOU8rzoR90qgrttYmmW%2FY5X46SqIBAjH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM%2FmkYAEsPOvTLB295KtwDJ8PLudNWblo52EBghxZWP6Tk3zkC4iFlrCmVvEYOrSLh9lwge%2BtxdjIEkYc5JgHXzEWR8h14nOxFPJStwh%2BvBaxlHAtKQndjKsXCNYMCEXYhv%2F1lr1RPhqGI9nNMC6qCVn4HBKTsYLd9E2TncH3t0MnbMDZV%2FUoOE5YDvc8YOdQz7LU1bTevkRxR9gPho1A9hENzbYhP8maW9nujjiy1gBbXMpwIyjSlPCMf63nF4bueGrYe69rlDDYy%2B96X0691aSNUAT0ys%2BTYlzCxRHMB2FAVoHysKiVyHigOuN9JS8srVS1uzQGXNAnNHLpsvqKDIU8lAU2NDK203XwhYa3lwzzozW2o4V0byu75BhW7gT0JA6c2GWtdu9CF5IWuqhQm7bIwmqZ0a0DhC656Ztk8p%2BrmM2%2BoGSWNh1X0VLYFuQNEmYO3whEs%2FpwOaoOW7EdvGvul8XJDULI%2BopLkHGJD%2FQcClAb1x55veuGFuu9pYhcpVz%2FyRQJSqKuAXnCIr2Jh454KLoaxtNl9gLbtqeq9l8StLJMfkhH%2FvZIWAS7U4yNCrDV%2B3%2FbqHkoY%2FUkgtn2t5QpH%2FAkNGvVaKozPpzpgPlhDtLmMOuBjyut2DHT%2BGmi7RC5OUt5Jw0jBPH4w75P1vAY6pgHHcJtFgpYM98BeP6%2BzOowf3pCNYLCwy2NLBXrK2O32ay%2Fs83%2FDt0OcS5QPX0qGT0Fg%2BV3IGyT7OlQNEOoMKHbGSZmh%2Fsvg1%2F5h%2FLbiZCdgYshYdVtl791vc%2BIeTKogimkGCuNzgr2bWr5lVAfZbJFrTWrUexZNe4JThaiuJmrKCun9cDf0RxtMTmrMpRav%2BVZ2xnC8NkmdMD%2BDIcLlWHEmGG2hWk9%2B&X-Amz-Signature=be6e4009e6a13df965399d8ed5963dcdd4e0dec3a6a16523cf68639aa9c6d770&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Correlation Plot
Heatmap visualizes correlations among variables. Color scheme indicates Pearson correlation coefficients. Dark red diagonal line shows perfect correlation (value of 1) between variables and themselves.
This heatmap offers overview of variable relationships and their link with price.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cd3b341e-cc1a-45f7-8aec-cdc00436d270/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZDLNTQSG%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T231315Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEL7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIAICLuY7mpKIPUX%2FAAuUuMMBaitFnkVOm5vDbcjrtig9AiAdGCuWKryI8n4wgbwfrOU8rzoR90qgrttYmmW%2FY5X46SqIBAjH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM%2FmkYAEsPOvTLB295KtwDJ8PLudNWblo52EBghxZWP6Tk3zkC4iFlrCmVvEYOrSLh9lwge%2BtxdjIEkYc5JgHXzEWR8h14nOxFPJStwh%2BvBaxlHAtKQndjKsXCNYMCEXYhv%2F1lr1RPhqGI9nNMC6qCVn4HBKTsYLd9E2TncH3t0MnbMDZV%2FUoOE5YDvc8YOdQz7LU1bTevkRxR9gPho1A9hENzbYhP8maW9nujjiy1gBbXMpwIyjSlPCMf63nF4bueGrYe69rlDDYy%2B96X0691aSNUAT0ys%2BTYlzCxRHMB2FAVoHysKiVyHigOuN9JS8srVS1uzQGXNAnNHLpsvqKDIU8lAU2NDK203XwhYa3lwzzozW2o4V0byu75BhW7gT0JA6c2GWtdu9CF5IWuqhQm7bIwmqZ0a0DhC656Ztk8p%2BrmM2%2BoGSWNh1X0VLYFuQNEmYO3whEs%2FpwOaoOW7EdvGvul8XJDULI%2BopLkHGJD%2FQcClAb1x55veuGFuu9pYhcpVz%2FyRQJSqKuAXnCIr2Jh454KLoaxtNl9gLbtqeq9l8StLJMfkhH%2FvZIWAS7U4yNCrDV%2B3%2FbqHkoY%2FUkgtn2t5QpH%2FAkNGvVaKozPpzpgPlhDtLmMOuBjyut2DHT%2BGmi7RC5OUt5Jw0jBPH4w75P1vAY6pgHHcJtFgpYM98BeP6%2BzOowf3pCNYLCwy2NLBXrK2O32ay%2Fs83%2FDt0OcS5QPX0qGT0Fg%2BV3IGyT7OlQNEOoMKHbGSZmh%2Fsvg1%2F5h%2FLbiZCdgYshYdVtl791vc%2BIeTKogimkGCuNzgr2bWr5lVAfZbJFrTWrUexZNe4JThaiuJmrKCun9cDf0RxtMTmrMpRav%2BVZ2xnC8NkmdMD%2BDIcLlWHEmGG2hWk9%2B&X-Amz-Signature=af0d01753fe85f1efa808f5411d4ca3e6f64e86eb67cf2c6de8621347180cf73&X-Amz-SignedHeaders=host&x-id=GetObject)

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
