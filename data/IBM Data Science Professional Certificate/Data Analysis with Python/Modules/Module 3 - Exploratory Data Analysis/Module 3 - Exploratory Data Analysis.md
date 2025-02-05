

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7e6d594d-952e-44b6-97ea-31225882aea6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WV7TE7TT%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T132043Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECsaCXVzLXdlc3QtMiJHMEUCIQCiQkni6ilbIyEoJKP1rBFipbhPH5eWkJvvHHAoQmcDjgIgKbFwZn6qNkHR%2F09dSZK0O1xhhCXVKjLEJhBG0%2Bk%2Bljoq%2FwMIRBAAGgw2Mzc0MjMxODM4MDUiDLIp42CEc4FeVHlaCCrcA4FB%2BByseO0%2BjUlSKw7kErDyfam%2FP1IvXN1vSVrXUVZcu0LgROhsAtjFNbqJMVnq9LqBzfmP2DUyygXBQZ0cr8z5ltF4g5m%2BEohilua9%2B7N%2FYjVFBQ%2Fju7XrARzZrKhj37HVwZalYS0jZmBsQ%2BUrUYGNLd1r548yUJS%2BZ1LHMPazoLq%2BiNo2fe%2Feapqgl5%2Bd5ze8zLQIOD2kaHFB0GWODF%2FE3aCGzLpO5zUUlE7D8%2BznrEfC9RSMrzx3vVCjxufhSczs5Fi89PfbtWvlQYEsz3KxobnOlqxxQhnh17ixyJzWZmg7kHLYkqElvRBSIVNKyoRzrIsjTpIU9wgBe5TTXwKM4Q0uPF5zujU7E7nItR1bkb1tth7YmiSol7qqnkxOV%2F%2F2tPmJOYE0%2FEkQ9z8O2k0kjO5rtrlgVwQEkPowPvU8LVhlJAsBqGZB4uMyVoDFcv3NN5%2FWNSFXTe79bCxQKsOjVtWkpRgfqCKpsdWgSpBG27zYN0mD8KTG%2BWc43vO0RbQi1vN%2F4P8QZRKLfVzDZQSs7Gbe%2B8%2B4QdCavsCKlcuL27wQRE7L7M%2FtSBEDVWbCjf%2FphL%2BfLUz%2FM6djMNsRC2gNki3ShHsDE%2B6Px4swsDraFKlWWBDxfLcfYedCMKyLjb0GOqUBNTYkfyPrq%2Fx54zt1PAclAn%2FCZN7YlJUGiIyUMIvjuO0QReE847DeJH6nsIybfJ%2B4cnCtQ9tHZdoh%2FXJaNbSHS4QW0skLIfCzLXxpSs6c2p6ip538nm4G4m37odKodec5POt9Vu3plW99NOvsmPT2khhbqQf%2F212Pj%2BYETMiNeyi3J2V%2FFGAkRnQ37Xs3LbDTvnc9tNeUcpGyY9opDBAUz7F4HmBv&X-Amz-Signature=83f62c69d4f7af9f36efec8934dc0d04604a6df47c28392c92bbf85d576ae6a7&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cbfaed9e-b398-4902-8936-dea058b21def/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WV7TE7TT%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T132043Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECsaCXVzLXdlc3QtMiJHMEUCIQCiQkni6ilbIyEoJKP1rBFipbhPH5eWkJvvHHAoQmcDjgIgKbFwZn6qNkHR%2F09dSZK0O1xhhCXVKjLEJhBG0%2Bk%2Bljoq%2FwMIRBAAGgw2Mzc0MjMxODM4MDUiDLIp42CEc4FeVHlaCCrcA4FB%2BByseO0%2BjUlSKw7kErDyfam%2FP1IvXN1vSVrXUVZcu0LgROhsAtjFNbqJMVnq9LqBzfmP2DUyygXBQZ0cr8z5ltF4g5m%2BEohilua9%2B7N%2FYjVFBQ%2Fju7XrARzZrKhj37HVwZalYS0jZmBsQ%2BUrUYGNLd1r548yUJS%2BZ1LHMPazoLq%2BiNo2fe%2Feapqgl5%2Bd5ze8zLQIOD2kaHFB0GWODF%2FE3aCGzLpO5zUUlE7D8%2BznrEfC9RSMrzx3vVCjxufhSczs5Fi89PfbtWvlQYEsz3KxobnOlqxxQhnh17ixyJzWZmg7kHLYkqElvRBSIVNKyoRzrIsjTpIU9wgBe5TTXwKM4Q0uPF5zujU7E7nItR1bkb1tth7YmiSol7qqnkxOV%2F%2F2tPmJOYE0%2FEkQ9z8O2k0kjO5rtrlgVwQEkPowPvU8LVhlJAsBqGZB4uMyVoDFcv3NN5%2FWNSFXTe79bCxQKsOjVtWkpRgfqCKpsdWgSpBG27zYN0mD8KTG%2BWc43vO0RbQi1vN%2F4P8QZRKLfVzDZQSs7Gbe%2B8%2B4QdCavsCKlcuL27wQRE7L7M%2FtSBEDVWbCjf%2FphL%2BfLUz%2FM6djMNsRC2gNki3ShHsDE%2B6Px4swsDraFKlWWBDxfLcfYedCMKyLjb0GOqUBNTYkfyPrq%2Fx54zt1PAclAn%2FCZN7YlJUGiIyUMIvjuO0QReE847DeJH6nsIybfJ%2B4cnCtQ9tHZdoh%2FXJaNbSHS4QW0skLIfCzLXxpSs6c2p6ip538nm4G4m37odKodec5POt9Vu3plW99NOvsmPT2khhbqQf%2F212Pj%2BYETMiNeyi3J2V%2FFGAkRnQ37Xs3LbDTvnc9tNeUcpGyY9opDBAUz7F4HmBv&X-Amz-Signature=ff0807be8c3d118d4aa32f3588c0d2bc01a5321704ce43983fd7a9ed33f296e1&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/91181646-b1e0-4433-9711-6259a96a9247/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WV7TE7TT%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T132043Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECsaCXVzLXdlc3QtMiJHMEUCIQCiQkni6ilbIyEoJKP1rBFipbhPH5eWkJvvHHAoQmcDjgIgKbFwZn6qNkHR%2F09dSZK0O1xhhCXVKjLEJhBG0%2Bk%2Bljoq%2FwMIRBAAGgw2Mzc0MjMxODM4MDUiDLIp42CEc4FeVHlaCCrcA4FB%2BByseO0%2BjUlSKw7kErDyfam%2FP1IvXN1vSVrXUVZcu0LgROhsAtjFNbqJMVnq9LqBzfmP2DUyygXBQZ0cr8z5ltF4g5m%2BEohilua9%2B7N%2FYjVFBQ%2Fju7XrARzZrKhj37HVwZalYS0jZmBsQ%2BUrUYGNLd1r548yUJS%2BZ1LHMPazoLq%2BiNo2fe%2Feapqgl5%2Bd5ze8zLQIOD2kaHFB0GWODF%2FE3aCGzLpO5zUUlE7D8%2BznrEfC9RSMrzx3vVCjxufhSczs5Fi89PfbtWvlQYEsz3KxobnOlqxxQhnh17ixyJzWZmg7kHLYkqElvRBSIVNKyoRzrIsjTpIU9wgBe5TTXwKM4Q0uPF5zujU7E7nItR1bkb1tth7YmiSol7qqnkxOV%2F%2F2tPmJOYE0%2FEkQ9z8O2k0kjO5rtrlgVwQEkPowPvU8LVhlJAsBqGZB4uMyVoDFcv3NN5%2FWNSFXTe79bCxQKsOjVtWkpRgfqCKpsdWgSpBG27zYN0mD8KTG%2BWc43vO0RbQi1vN%2F4P8QZRKLfVzDZQSs7Gbe%2B8%2B4QdCavsCKlcuL27wQRE7L7M%2FtSBEDVWbCjf%2FphL%2BfLUz%2FM6djMNsRC2gNki3ShHsDE%2B6Px4swsDraFKlWWBDxfLcfYedCMKyLjb0GOqUBNTYkfyPrq%2Fx54zt1PAclAn%2FCZN7YlJUGiIyUMIvjuO0QReE847DeJH6nsIybfJ%2B4cnCtQ9tHZdoh%2FXJaNbSHS4QW0skLIfCzLXxpSs6c2p6ip538nm4G4m37odKodec5POt9Vu3plW99NOvsmPT2khhbqQf%2F212Pj%2BYETMiNeyi3J2V%2FFGAkRnQ37Xs3LbDTvnc9tNeUcpGyY9opDBAUz7F4HmBv&X-Amz-Signature=83210e2c79fe56c07969def7b481fbb78953d8ffc3d263cb8dda5ca7259a0d2f&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/09aba1c0-0d55-41dd-852a-a04c5b8a3fac/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664USEHF32%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T132043Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECsaCXVzLXdlc3QtMiJHMEUCIFB07acR0y2wmmnr2oi4mucBLP5TAMXxa3fKovJwR%2F%2B4AiEAv5QfgnPOkw0pwCVl4kTsQOe%2F5dGj4SOjvyfwbTVCV7Yq%2FwMIRBAAGgw2Mzc0MjMxODM4MDUiDDY0pwTPlsihuTF4vircA4bIe0cOncP4VkwHv8XfNqb2CjLE4uF84S6sWOuWNk1hwKtBZN4OY51%2Fg92DV1VPpUNzp0VcW3aYxM9X0Z5wrRMOGnUxTnzdLg9zIOj4Lo4wDo9BBbCUwSoa9icIOiOSmYPGtwWVax5h7naFIqLQsrtkhGenHXPptRhH%2BRpQ7LyBxf1vW3Uxsgrt74PJoO6K7a79P2qOZ2qbWOUFzUUl3iH1zMj2ktj8Mmznmjjqg8Qc%2BJzQhoE0tm%2FdyhMMW5QoBIwxUu99rEtR86Apf4WzR17j5j1VX5QpYSUODsrhXsLPNw8o51ESdqFQyz6u%2BOCb44EUCDGUVyXuyUAqeeMu8kokwmwQCr0Dc3M9ARAq2kg6xD60IU%2BtngcG8%2FuVs1%2FtDkkxEsDP273Sgz18840AxCvWUof5KHv07CFEgGmuQeY3d4RYPbsQUm9GEpXl6q7kvZUn9WX3ncv5M8K6xsDBqXmSCS3gnIPwhPEyvGrI9K%2FIz8cG6fzhGF1sn6IQs%2BNgifJMTL9%2FqX4xQtPLMc2u4NDQDbntSS%2BMoHnqb2Myh5RBx2unJ%2F%2FZm788prTbYCTLDuc9gXKUjsnocTLaGBgb2pUqEXCe1FiZx64yxjOM%2BK83v%2B2dOHGkwTDCE3qYMOmKjb0GOqUBRAKNai3e8MxZxhXKiX%2BMzr0HwxecH3cHo7dmxiyhIXufE%2BQXfH%2BDbg%2BbKWSr68yU8vdadJss18ehNx%2F1WCpdD%2BXcEvCUV2EpWt60saLK7weKpLFlhxlfjRoBvDEK%2FDC2rPb%2FGz8jesvu3nJfj7vWaIdmoL9Os5qQbgtyZTW%2F3HkW5p0yo8KQ1%2BYWTJpz%2BShHia02LWSnLnQSOYJGs50Z4nAjSfq2&X-Amz-Signature=d20537c7b789afadbae5f80b017b7cdc0524e9c749d8c6e1d66424315e2dcfe8&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 2. Scatter Plot
Scatter plots present the relationship between two variables in a dataset. It represents data points on a two-dimensional plane. The independent variable or attribute is plotted on the X-axis, while the dependent variable is plotted on the Y-axis.
**Syntax:**
```python
plt.scatter(x, y)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23708af9-659f-4f23-b626-1a4292d7842c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664USEHF32%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T132043Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECsaCXVzLXdlc3QtMiJHMEUCIFB07acR0y2wmmnr2oi4mucBLP5TAMXxa3fKovJwR%2F%2B4AiEAv5QfgnPOkw0pwCVl4kTsQOe%2F5dGj4SOjvyfwbTVCV7Yq%2FwMIRBAAGgw2Mzc0MjMxODM4MDUiDDY0pwTPlsihuTF4vircA4bIe0cOncP4VkwHv8XfNqb2CjLE4uF84S6sWOuWNk1hwKtBZN4OY51%2Fg92DV1VPpUNzp0VcW3aYxM9X0Z5wrRMOGnUxTnzdLg9zIOj4Lo4wDo9BBbCUwSoa9icIOiOSmYPGtwWVax5h7naFIqLQsrtkhGenHXPptRhH%2BRpQ7LyBxf1vW3Uxsgrt74PJoO6K7a79P2qOZ2qbWOUFzUUl3iH1zMj2ktj8Mmznmjjqg8Qc%2BJzQhoE0tm%2FdyhMMW5QoBIwxUu99rEtR86Apf4WzR17j5j1VX5QpYSUODsrhXsLPNw8o51ESdqFQyz6u%2BOCb44EUCDGUVyXuyUAqeeMu8kokwmwQCr0Dc3M9ARAq2kg6xD60IU%2BtngcG8%2FuVs1%2FtDkkxEsDP273Sgz18840AxCvWUof5KHv07CFEgGmuQeY3d4RYPbsQUm9GEpXl6q7kvZUn9WX3ncv5M8K6xsDBqXmSCS3gnIPwhPEyvGrI9K%2FIz8cG6fzhGF1sn6IQs%2BNgifJMTL9%2FqX4xQtPLMc2u4NDQDbntSS%2BMoHnqb2Myh5RBx2unJ%2F%2FZm788prTbYCTLDuc9gXKUjsnocTLaGBgb2pUqEXCe1FiZx64yxjOM%2BK83v%2B2dOHGkwTDCE3qYMOmKjb0GOqUBRAKNai3e8MxZxhXKiX%2BMzr0HwxecH3cHo7dmxiyhIXufE%2BQXfH%2BDbg%2BbKWSr68yU8vdadJss18ehNx%2F1WCpdD%2BXcEvCUV2EpWt60saLK7weKpLFlhxlfjRoBvDEK%2FDC2rPb%2FGz8jesvu3nJfj7vWaIdmoL9Os5qQbgtyZTW%2F3HkW5p0yo8KQ1%2BYWTJpz%2BShHia02LWSnLnQSOYJGs50Z4nAjSfq2&X-Amz-Signature=a0595cb4054543a58d314be9331beda3183a9f94d21278485f4bd371678cd53e&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 3. Histogram
A histogram is an important visual representation of data in categorical form. To view the data in a "Binned" form, use the histogram plot with a number of bins required or with the data points that mark the bin edges. The x-axis represents the data bins, and the y-axis represents the number of elements in each bin.
**Syntax:**
```python
plt.hist(x, bins)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/24e4424a-df87-40a1-b63b-195cbdc2e0ab/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664USEHF32%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T132043Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECsaCXVzLXdlc3QtMiJHMEUCIFB07acR0y2wmmnr2oi4mucBLP5TAMXxa3fKovJwR%2F%2B4AiEAv5QfgnPOkw0pwCVl4kTsQOe%2F5dGj4SOjvyfwbTVCV7Yq%2FwMIRBAAGgw2Mzc0MjMxODM4MDUiDDY0pwTPlsihuTF4vircA4bIe0cOncP4VkwHv8XfNqb2CjLE4uF84S6sWOuWNk1hwKtBZN4OY51%2Fg92DV1VPpUNzp0VcW3aYxM9X0Z5wrRMOGnUxTnzdLg9zIOj4Lo4wDo9BBbCUwSoa9icIOiOSmYPGtwWVax5h7naFIqLQsrtkhGenHXPptRhH%2BRpQ7LyBxf1vW3Uxsgrt74PJoO6K7a79P2qOZ2qbWOUFzUUl3iH1zMj2ktj8Mmznmjjqg8Qc%2BJzQhoE0tm%2FdyhMMW5QoBIwxUu99rEtR86Apf4WzR17j5j1VX5QpYSUODsrhXsLPNw8o51ESdqFQyz6u%2BOCb44EUCDGUVyXuyUAqeeMu8kokwmwQCr0Dc3M9ARAq2kg6xD60IU%2BtngcG8%2FuVs1%2FtDkkxEsDP273Sgz18840AxCvWUof5KHv07CFEgGmuQeY3d4RYPbsQUm9GEpXl6q7kvZUn9WX3ncv5M8K6xsDBqXmSCS3gnIPwhPEyvGrI9K%2FIz8cG6fzhGF1sn6IQs%2BNgifJMTL9%2FqX4xQtPLMc2u4NDQDbntSS%2BMoHnqb2Myh5RBx2unJ%2F%2FZm788prTbYCTLDuc9gXKUjsnocTLaGBgb2pUqEXCe1FiZx64yxjOM%2BK83v%2B2dOHGkwTDCE3qYMOmKjb0GOqUBRAKNai3e8MxZxhXKiX%2BMzr0HwxecH3cHo7dmxiyhIXufE%2BQXfH%2BDbg%2BbKWSr68yU8vdadJss18ehNx%2F1WCpdD%2BXcEvCUV2EpWt60saLK7weKpLFlhxlfjRoBvDEK%2FDC2rPb%2FGz8jesvu3nJfj7vWaIdmoL9Os5qQbgtyZTW%2F3HkW5p0yo8KQ1%2BYWTJpz%2BShHia02LWSnLnQSOYJGs50Z4nAjSfq2&X-Amz-Signature=cc2c04d20ef4b54a73835e0f5f8965058c4f91c33f474a4cedc6da687f274457&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ab5a6dfe-51f5-43ee-bcb3-33dae4a1c7ad/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664USEHF32%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T132043Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECsaCXVzLXdlc3QtMiJHMEUCIFB07acR0y2wmmnr2oi4mucBLP5TAMXxa3fKovJwR%2F%2B4AiEAv5QfgnPOkw0pwCVl4kTsQOe%2F5dGj4SOjvyfwbTVCV7Yq%2FwMIRBAAGgw2Mzc0MjMxODM4MDUiDDY0pwTPlsihuTF4vircA4bIe0cOncP4VkwHv8XfNqb2CjLE4uF84S6sWOuWNk1hwKtBZN4OY51%2Fg92DV1VPpUNzp0VcW3aYxM9X0Z5wrRMOGnUxTnzdLg9zIOj4Lo4wDo9BBbCUwSoa9icIOiOSmYPGtwWVax5h7naFIqLQsrtkhGenHXPptRhH%2BRpQ7LyBxf1vW3Uxsgrt74PJoO6K7a79P2qOZ2qbWOUFzUUl3iH1zMj2ktj8Mmznmjjqg8Qc%2BJzQhoE0tm%2FdyhMMW5QoBIwxUu99rEtR86Apf4WzR17j5j1VX5QpYSUODsrhXsLPNw8o51ESdqFQyz6u%2BOCb44EUCDGUVyXuyUAqeeMu8kokwmwQCr0Dc3M9ARAq2kg6xD60IU%2BtngcG8%2FuVs1%2FtDkkxEsDP273Sgz18840AxCvWUof5KHv07CFEgGmuQeY3d4RYPbsQUm9GEpXl6q7kvZUn9WX3ncv5M8K6xsDBqXmSCS3gnIPwhPEyvGrI9K%2FIz8cG6fzhGF1sn6IQs%2BNgifJMTL9%2FqX4xQtPLMc2u4NDQDbntSS%2BMoHnqb2Myh5RBx2unJ%2F%2FZm788prTbYCTLDuc9gXKUjsnocTLaGBgb2pUqEXCe1FiZx64yxjOM%2BK83v%2B2dOHGkwTDCE3qYMOmKjb0GOqUBRAKNai3e8MxZxhXKiX%2BMzr0HwxecH3cHo7dmxiyhIXufE%2BQXfH%2BDbg%2BbKWSr68yU8vdadJss18ehNx%2F1WCpdD%2BXcEvCUV2EpWt60saLK7weKpLFlhxlfjRoBvDEK%2FDC2rPb%2FGz8jesvu3nJfj7vWaIdmoL9Os5qQbgtyZTW%2F3HkW5p0yo8KQ1%2BYWTJpz%2BShHia02LWSnLnQSOYJGs50Z4nAjSfq2&X-Amz-Signature=516dd36b429cd29491e595dfd4578a6d58b25eca83d9213fed130adf068fc84b&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8f1b1d60-cf1b-42b3-9faa-f634c89c3f84/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664USEHF32%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T132043Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECsaCXVzLXdlc3QtMiJHMEUCIFB07acR0y2wmmnr2oi4mucBLP5TAMXxa3fKovJwR%2F%2B4AiEAv5QfgnPOkw0pwCVl4kTsQOe%2F5dGj4SOjvyfwbTVCV7Yq%2FwMIRBAAGgw2Mzc0MjMxODM4MDUiDDY0pwTPlsihuTF4vircA4bIe0cOncP4VkwHv8XfNqb2CjLE4uF84S6sWOuWNk1hwKtBZN4OY51%2Fg92DV1VPpUNzp0VcW3aYxM9X0Z5wrRMOGnUxTnzdLg9zIOj4Lo4wDo9BBbCUwSoa9icIOiOSmYPGtwWVax5h7naFIqLQsrtkhGenHXPptRhH%2BRpQ7LyBxf1vW3Uxsgrt74PJoO6K7a79P2qOZ2qbWOUFzUUl3iH1zMj2ktj8Mmznmjjqg8Qc%2BJzQhoE0tm%2FdyhMMW5QoBIwxUu99rEtR86Apf4WzR17j5j1VX5QpYSUODsrhXsLPNw8o51ESdqFQyz6u%2BOCb44EUCDGUVyXuyUAqeeMu8kokwmwQCr0Dc3M9ARAq2kg6xD60IU%2BtngcG8%2FuVs1%2FtDkkxEsDP273Sgz18840AxCvWUof5KHv07CFEgGmuQeY3d4RYPbsQUm9GEpXl6q7kvZUn9WX3ncv5M8K6xsDBqXmSCS3gnIPwhPEyvGrI9K%2FIz8cG6fzhGF1sn6IQs%2BNgifJMTL9%2FqX4xQtPLMc2u4NDQDbntSS%2BMoHnqb2Myh5RBx2unJ%2F%2FZm788prTbYCTLDuc9gXKUjsnocTLaGBgb2pUqEXCe1FiZx64yxjOM%2BK83v%2B2dOHGkwTDCE3qYMOmKjb0GOqUBRAKNai3e8MxZxhXKiX%2BMzr0HwxecH3cHo7dmxiyhIXufE%2BQXfH%2BDbg%2BbKWSr68yU8vdadJss18ehNx%2F1WCpdD%2BXcEvCUV2EpWt60saLK7weKpLFlhxlfjRoBvDEK%2FDC2rPb%2FGz8jesvu3nJfj7vWaIdmoL9Os5qQbgtyZTW%2F3HkW5p0yo8KQ1%2BYWTJpz%2BShHia02LWSnLnQSOYJGs50Z4nAjSfq2&X-Amz-Signature=22de749c6b272f4630b60fe02ac3900d9975877b310b3b7e8d1cdc20ee80798f&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/13ad0497-05fe-4eaa-984e-707b33e14761/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664USEHF32%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T132043Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECsaCXVzLXdlc3QtMiJHMEUCIFB07acR0y2wmmnr2oi4mucBLP5TAMXxa3fKovJwR%2F%2B4AiEAv5QfgnPOkw0pwCVl4kTsQOe%2F5dGj4SOjvyfwbTVCV7Yq%2FwMIRBAAGgw2Mzc0MjMxODM4MDUiDDY0pwTPlsihuTF4vircA4bIe0cOncP4VkwHv8XfNqb2CjLE4uF84S6sWOuWNk1hwKtBZN4OY51%2Fg92DV1VPpUNzp0VcW3aYxM9X0Z5wrRMOGnUxTnzdLg9zIOj4Lo4wDo9BBbCUwSoa9icIOiOSmYPGtwWVax5h7naFIqLQsrtkhGenHXPptRhH%2BRpQ7LyBxf1vW3Uxsgrt74PJoO6K7a79P2qOZ2qbWOUFzUUl3iH1zMj2ktj8Mmznmjjqg8Qc%2BJzQhoE0tm%2FdyhMMW5QoBIwxUu99rEtR86Apf4WzR17j5j1VX5QpYSUODsrhXsLPNw8o51ESdqFQyz6u%2BOCb44EUCDGUVyXuyUAqeeMu8kokwmwQCr0Dc3M9ARAq2kg6xD60IU%2BtngcG8%2FuVs1%2FtDkkxEsDP273Sgz18840AxCvWUof5KHv07CFEgGmuQeY3d4RYPbsQUm9GEpXl6q7kvZUn9WX3ncv5M8K6xsDBqXmSCS3gnIPwhPEyvGrI9K%2FIz8cG6fzhGF1sn6IQs%2BNgifJMTL9%2FqX4xQtPLMc2u4NDQDbntSS%2BMoHnqb2Myh5RBx2unJ%2F%2FZm788prTbYCTLDuc9gXKUjsnocTLaGBgb2pUqEXCe1FiZx64yxjOM%2BK83v%2B2dOHGkwTDCE3qYMOmKjb0GOqUBRAKNai3e8MxZxhXKiX%2BMzr0HwxecH3cHo7dmxiyhIXufE%2BQXfH%2BDbg%2BbKWSr68yU8vdadJss18ehNx%2F1WCpdD%2BXcEvCUV2EpWt60saLK7weKpLFlhxlfjRoBvDEK%2FDC2rPb%2FGz8jesvu3nJfj7vWaIdmoL9Os5qQbgtyZTW%2F3HkW5p0yo8KQ1%2BYWTJpz%2BShHia02LWSnLnQSOYJGs50Z4nAjSfq2&X-Amz-Signature=e02e9eaeaf8274e410c0027a54a7d981417bdadcfa2b2e53aa64715bf88f082b&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 2. Box and Whisker Plot
A box plot shows the distribution of quantitative data in a way that facilitates comparisons between variables or across levels of a categorical variable. The box shows the quartiles of the dataset while the whiskers extend to show the rest of the distribution, except for points that are determined to be "outliers".
**Syntax:**
```python
sns.boxplot(x='header_1', y='header_2', data=df)
```
**Example Output:**


![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d207ae92-0a7c-4e2f-aa65-0ee5a2c33bf7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46666XO55YA%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T132045Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECsaCXVzLXdlc3QtMiJHMEUCIBsyIZ4t1SouBu2IUtrT6u4NJU%2BqONlpYn8IctmWwtXrAiEA%2FrQoCOI%2Fi%2BzK4%2B9agG2uwnPBw1Fly2z%2FKMN3tBKFmp4q%2FwMIRBAAGgw2Mzc0MjMxODM4MDUiDOktdyWp28ejidNEGSrcA3pjEFKn4VVTNUQszMtvu3MZLUcWBgUXurqRKK9D%2FK90eyDWDaPvDFU8co%2FGTr8FNhGlOEup1WurUyLOhA7X3SlQqziagZ8qDGuqLQsuAHAvC1D98aNZspSZup79rQomH%2F6G1A42%2Fn9lFkSVqeDquvh4PQ18go9l%2BrrGMad2K2avfu%2FTi7Fv0sEtS3cqdI5tfI%2BEGta%2FFL4W7iOXVNt5qkrE6M%2BUjNB34UQF3TPcetz8XiJQia5ceo28Q0hZycdiQwwfPEOIbNdO1L9WNMXEQ9VdVSXeu5Gqzo3EQx8GKu0Y8q7NlgEyI6TditJCysKYPPpeEBmKtjKUk%2FIhujXobJiwRRfLSj71SgaX5XuLBFvDMnzeLhfiX5zp4TP9D2AEwIpJ37l88SWzBEhTi4wQP4SA739zAptVKqgTXEgq9QFR7x7j2i203XNsE%2Fc%2F5rLcfFFTX%2FjhWu3sjN%2Fa%2BQkD84aI8VQ6Ixk2ZHfTMNSJqmRFGvKzKYq9kbjPCA%2BrzXxeiyYFtA7jjB%2Flm%2BBQg%2BY0Gz%2BKSOvZi27gysoT0YxCu0W0hjr3GjV3DiUfCoI8mTG9IZbc1g%2Fv7xr3ozQkYk1fF2WAwO7GWpQ6N7TuZOHStCL4aeutbNAvXOWx3o4NMNSKjb0GOqUBpYo4v2yVrHgG1jcZX2DiV3Ypk9SYCzcFuqrvJn1JL721rgt%2BtgGdhexy3r7HQx1iyZfedZ0ItuW%2BKxxWSUY6y26KScsWya4fkq9CsnGHGjguMXe%2BICw6ecLWPMNyMcl%2BOxXXH9uvgKfho7vWMV10DPrJgZ%2BMJ6effF6AamErujOnrsKEahssVc1z7W378gbJ%2FO%2Fb9SZL7sNhKOetKaGbY64bPS9j&X-Amz-Signature=0c7c57c11a01c75b958c3b76b3b490d933393fa774ea560895b51d509900b8af&X-Amz-SignedHeaders=host&x-id=GetObject)

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0e516edc-7551-4792-ab18-0494db3c4c0c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RUMKQB3J%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T132045Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECsaCXVzLXdlc3QtMiJGMEQCIEgwZ5P5JI4QDZz6udhy7gTvU2v2OQ3rpuELgnemg4vVAiBBPJwzWXtOiLPqs03S1G26m3gFD4y2uwGBF%2BwJrF9eMir%2FAwhEEAAaDDYzNzQyMzE4MzgwNSIM9mGulM3QTcQSMXyYKtwDpZjBcnI7s3RZS%2FXtpy%2FExUckNbbzeazIlj4kChFc1U4vV%2BXsZF7p1SY%2FBaM3tzMczeJbgdwP512viQIuoIn3ruTd%2FneAF5zL1LqE%2BmY0Ji%2BW58cWe9i7I8%2FQp7%2ByzM%2B0WGlPBnimU0R0GRUyOoNmWB1KESyBz25kr0oCmszo4tATx0cpnUClF%2FqsBEOjpbALiJqzDlsryS8cSzq9o37O%2FxUueJlZyhaa79DhAvCnjkBs2LcKQtY%2BuhSjN9oEL2f4YoO%2FdHAgelmNRYAKCY5zPP0R4vQuatY31EdYm3Wed%2BCuPXsL%2FSyPgriMzcr%2FNnoVsHimaCq731pppdSWZ2DB3Dh1MisCg3s0l%2B512hzEhgyC9%2FE6u6g6jaFZ%2BNgXDcillU%2FmDbuhAeew6HtWCoXn1jDVLoUz7zv7Iu8puWZewAEuydBqVEe%2BtTbQKC1CvCdnUv6e8vT9SDjrSlKPizexJMS9nr9YDwWSXZ46OcpAQZL3kfkR%2Bdwn3tZ6%2BRB%2BtHTKO2E2vHkm7FYbwen369BYGj5uctpjl5XYVBbJj9A5fFcZDrdpnTzml5ZXFgJV%2B4ELqOaAEI1RJoNzj5K%2FrLACU9IRmTKWh5NptJp%2BC3Jnrn%2FH8T5GBaQeMXyrWEQw3IqNvQY6pgERueNRvu6kCHWDB%2FfsnUKsM6XWEvwJfSGSf67jVqpmaJrv5nf3ZEjAsjnt%2B8CEchhyDCzI0on7NUJlfRya7%2FBiu5PV7hQtK8Km4QHoRiNt0MnMa85khOulNoTjXxPVX9upW6WZslPjNkJ2SUmHDMKDP8IxJOJvN8pT2KEpRw4QkF44NGSRtt6N4bTLDDk32i1H7dy9xhz9wz0fVDjtFmhqQGGYzubK&X-Amz-Signature=38277d4ac329215afe96b08cf9b7bc92fcba21f301b001577311c5b6c2771499&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23a79b9d-2356-49a9-8fd9-65c6b0ab2cc5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664USEHF32%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T132043Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECsaCXVzLXdlc3QtMiJHMEUCIFB07acR0y2wmmnr2oi4mucBLP5TAMXxa3fKovJwR%2F%2B4AiEAv5QfgnPOkw0pwCVl4kTsQOe%2F5dGj4SOjvyfwbTVCV7Yq%2FwMIRBAAGgw2Mzc0MjMxODM4MDUiDDY0pwTPlsihuTF4vircA4bIe0cOncP4VkwHv8XfNqb2CjLE4uF84S6sWOuWNk1hwKtBZN4OY51%2Fg92DV1VPpUNzp0VcW3aYxM9X0Z5wrRMOGnUxTnzdLg9zIOj4Lo4wDo9BBbCUwSoa9icIOiOSmYPGtwWVax5h7naFIqLQsrtkhGenHXPptRhH%2BRpQ7LyBxf1vW3Uxsgrt74PJoO6K7a79P2qOZ2qbWOUFzUUl3iH1zMj2ktj8Mmznmjjqg8Qc%2BJzQhoE0tm%2FdyhMMW5QoBIwxUu99rEtR86Apf4WzR17j5j1VX5QpYSUODsrhXsLPNw8o51ESdqFQyz6u%2BOCb44EUCDGUVyXuyUAqeeMu8kokwmwQCr0Dc3M9ARAq2kg6xD60IU%2BtngcG8%2FuVs1%2FtDkkxEsDP273Sgz18840AxCvWUof5KHv07CFEgGmuQeY3d4RYPbsQUm9GEpXl6q7kvZUn9WX3ncv5M8K6xsDBqXmSCS3gnIPwhPEyvGrI9K%2FIz8cG6fzhGF1sn6IQs%2BNgifJMTL9%2FqX4xQtPLMc2u4NDQDbntSS%2BMoHnqb2Myh5RBx2unJ%2F%2FZm788prTbYCTLDuc9gXKUjsnocTLaGBgb2pUqEXCe1FiZx64yxjOM%2BK83v%2B2dOHGkwTDCE3qYMOmKjb0GOqUBRAKNai3e8MxZxhXKiX%2BMzr0HwxecH3cHo7dmxiyhIXufE%2BQXfH%2BDbg%2BbKWSr68yU8vdadJss18ehNx%2F1WCpdD%2BXcEvCUV2EpWt60saLK7weKpLFlhxlfjRoBvDEK%2FDC2rPb%2FGz8jesvu3nJfj7vWaIdmoL9Os5qQbgtyZTW%2F3HkW5p0yo8KQ1%2BYWTJpz%2BShHia02LWSnLnQSOYJGs50Z4nAjSfq2&X-Amz-Signature=d906249ffb3652d6b774415aaa21152a7365ac0fe9211eede4ac88344038a148&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 4. KDE Plot
A Kernel Density Estimate (KDE) plot is a graph that creates a probability distribution curve for the data based upon its likelihood of occurrence on a specific value. This is created for a single vector of information.
**Syntax:**
```python
sns.kdeplot(X) || sns.kdeplot(df['age'])
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0d571213-2a2f-4921-a50b-880847aa05ee/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664USEHF32%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T132043Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECsaCXVzLXdlc3QtMiJHMEUCIFB07acR0y2wmmnr2oi4mucBLP5TAMXxa3fKovJwR%2F%2B4AiEAv5QfgnPOkw0pwCVl4kTsQOe%2F5dGj4SOjvyfwbTVCV7Yq%2FwMIRBAAGgw2Mzc0MjMxODM4MDUiDDY0pwTPlsihuTF4vircA4bIe0cOncP4VkwHv8XfNqb2CjLE4uF84S6sWOuWNk1hwKtBZN4OY51%2Fg92DV1VPpUNzp0VcW3aYxM9X0Z5wrRMOGnUxTnzdLg9zIOj4Lo4wDo9BBbCUwSoa9icIOiOSmYPGtwWVax5h7naFIqLQsrtkhGenHXPptRhH%2BRpQ7LyBxf1vW3Uxsgrt74PJoO6K7a79P2qOZ2qbWOUFzUUl3iH1zMj2ktj8Mmznmjjqg8Qc%2BJzQhoE0tm%2FdyhMMW5QoBIwxUu99rEtR86Apf4WzR17j5j1VX5QpYSUODsrhXsLPNw8o51ESdqFQyz6u%2BOCb44EUCDGUVyXuyUAqeeMu8kokwmwQCr0Dc3M9ARAq2kg6xD60IU%2BtngcG8%2FuVs1%2FtDkkxEsDP273Sgz18840AxCvWUof5KHv07CFEgGmuQeY3d4RYPbsQUm9GEpXl6q7kvZUn9WX3ncv5M8K6xsDBqXmSCS3gnIPwhPEyvGrI9K%2FIz8cG6fzhGF1sn6IQs%2BNgifJMTL9%2FqX4xQtPLMc2u4NDQDbntSS%2BMoHnqb2Myh5RBx2unJ%2F%2FZm788prTbYCTLDuc9gXKUjsnocTLaGBgb2pUqEXCe1FiZx64yxjOM%2BK83v%2B2dOHGkwTDCE3qYMOmKjb0GOqUBRAKNai3e8MxZxhXKiX%2BMzr0HwxecH3cHo7dmxiyhIXufE%2BQXfH%2BDbg%2BbKWSr68yU8vdadJss18ehNx%2F1WCpdD%2BXcEvCUV2EpWt60saLK7weKpLFlhxlfjRoBvDEK%2FDC2rPb%2FGz8jesvu3nJfj7vWaIdmoL9Os5qQbgtyZTW%2F3HkW5p0yo8KQ1%2BYWTJpz%2BShHia02LWSnLnQSOYJGs50Z4nAjSfq2&X-Amz-Signature=1f06bc01595d940095df7c3f43b02902d1832f8e198be7e250d03f2edf58ffd2&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/53752550-ef82-4ca9-a01a-09921f0282d0/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664USEHF32%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T132043Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECsaCXVzLXdlc3QtMiJHMEUCIFB07acR0y2wmmnr2oi4mucBLP5TAMXxa3fKovJwR%2F%2B4AiEAv5QfgnPOkw0pwCVl4kTsQOe%2F5dGj4SOjvyfwbTVCV7Yq%2FwMIRBAAGgw2Mzc0MjMxODM4MDUiDDY0pwTPlsihuTF4vircA4bIe0cOncP4VkwHv8XfNqb2CjLE4uF84S6sWOuWNk1hwKtBZN4OY51%2Fg92DV1VPpUNzp0VcW3aYxM9X0Z5wrRMOGnUxTnzdLg9zIOj4Lo4wDo9BBbCUwSoa9icIOiOSmYPGtwWVax5h7naFIqLQsrtkhGenHXPptRhH%2BRpQ7LyBxf1vW3Uxsgrt74PJoO6K7a79P2qOZ2qbWOUFzUUl3iH1zMj2ktj8Mmznmjjqg8Qc%2BJzQhoE0tm%2FdyhMMW5QoBIwxUu99rEtR86Apf4WzR17j5j1VX5QpYSUODsrhXsLPNw8o51ESdqFQyz6u%2BOCb44EUCDGUVyXuyUAqeeMu8kokwmwQCr0Dc3M9ARAq2kg6xD60IU%2BtngcG8%2FuVs1%2FtDkkxEsDP273Sgz18840AxCvWUof5KHv07CFEgGmuQeY3d4RYPbsQUm9GEpXl6q7kvZUn9WX3ncv5M8K6xsDBqXmSCS3gnIPwhPEyvGrI9K%2FIz8cG6fzhGF1sn6IQs%2BNgifJMTL9%2FqX4xQtPLMc2u4NDQDbntSS%2BMoHnqb2Myh5RBx2unJ%2F%2FZm788prTbYCTLDuc9gXKUjsnocTLaGBgb2pUqEXCe1FiZx64yxjOM%2BK83v%2B2dOHGkwTDCE3qYMOmKjb0GOqUBRAKNai3e8MxZxhXKiX%2BMzr0HwxecH3cHo7dmxiyhIXufE%2BQXfH%2BDbg%2BbKWSr68yU8vdadJss18ehNx%2F1WCpdD%2BXcEvCUV2EpWt60saLK7weKpLFlhxlfjRoBvDEK%2FDC2rPb%2FGz8jesvu3nJfj7vWaIdmoL9Os5qQbgtyZTW%2F3HkW5p0yo8KQ1%2BYWTJpz%2BShHia02LWSnLnQSOYJGs50Z4nAjSfq2&X-Amz-Signature=65fd6fe96ca300e27336ed299cab496b848badacd26457ffafaae000b0107b46&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
## 4. Correlation Between Variables
Correlation is a statistical measure of the extent to which different variables are interdependent. It indicates how changes in one variable are associated with changes in another variable over time.
### Positive Correlation
Positive correlation indicates that as one variable increases, the other variable also tends to increase.
**Example: Engine Size and Price**
- **Positive Correlation:** Engine size increases, price also increases.
- **Visualization:** Scatter plot with a steep positive slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c7ea9b0-3ef3-4357-a9c3-554fc71b6b15/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZEKVYOOA%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T132044Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECsaCXVzLXdlc3QtMiJHMEUCIQDDjgA%2FX5dcsLjU6Ysnb8oPGDZHMrH53l%2FaQz8rTC36TgIgIoWVzg7YELbPFZekQU4DIzwupzSskTFGuf4J3t%2B%2FE4Eq%2FwMIRBAAGgw2Mzc0MjMxODM4MDUiDJYQQdQa4bPVCwn9hyrcA9e8agpxrU%2FkgLTPcrKO6vd14fLmf3eqWrkF71W4PXJzd9uF9YwXlS6VGlVZlZU%2Bs8tPoNVOdnzxJlWApyVTdFJ%2BLAUOZWGFxPVrK6gEjf7xb1B5NqGuBoiWU3dcrhFaKKL93bZTzWBKZE95QsS%2FWqomYDdrXePnBVC9zL4DRUPp0Tms5k8%2BmjAcZteMfVZ8m7BOTI3YIMNPBGd7c1WeihS%2BV65iGmKrFroMzSabZ8FkE8JLCP2Yjz4gsQd9i%2FVunpi%2FVip9yu9ERtu52ceVj%2F2UDB4T1ZsEguPBDP9uCa07dGKI1HscXLFpiPpvAgHikdFgU1VKcu8bnZ3m7DRcPWHdGCl9RntC8X3hKqz%2Bn969NLY8PTycLo2caB5O5QgHUxbumKA77HZAZRvRUzf4ge8QVGiJ0oPwPwGdzJButv78boFjfUqAJFLip%2F%2FPPHAH1tCqmOI42UGiuxun1h7IyTWXuxmOUOYBzrsBX0Mvh9JgN3XD2rSqs%2BrN1O75gI9wFa82Iu1yl40FRp5GSggzU8j1m8cjPveZaLbQEUnrRUXA559UsmCTIg3JpzrZFKuLnuVOoOIfMwAZ562RZPQFtu1XwMq5jniG99YIjTwSTgTbUG7HW%2Fk17qU7pGe3MJuLjb0GOqUBTwCuLwvCXZGbxeX9Nfb7HZIqqbVLQdJDtzwTbf2pUoliIRyBfJrfQyGzopTZ%2Fr5tQZwirbM7g5VbhiY73TeA43NTYIxZPqj7bnybNoFwbcQHdNCH07jVH9T6ajE4QUyEMUElVJ3wP5Vgyo6f2tiV8EQjSuh7XVlSQWo6wROAXyRCL3yMz96lAgEzXDzBtKRVfdWre7gOndkutLFd0Ly2If4CPWqg&X-Amz-Signature=aa4d53cc81cd4ae86c58cf1a2becaa5882a8afb1817ab2f940dce12dd434e702&X-Amz-SignedHeaders=host&x-id=GetObject)
**Explanation:** When engine size increases, there is a corresponding increase in the price of the vehicle. This positive correlation suggests that larger engines tend to be associated with higher prices in the market.
___
### Negative Correlation
Negative correlation indicates that as one variable increases, the other variable tends to decrease.
**Example: Highway Miles per Gallon and Price**
- **Negative Correlation:** As highway miles per gallon increases, price decreases.
- **Visualization:** Scatter plot with a steep negative slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/10f1f798-9cc4-4df2-a9c1-5a339f554a0b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SZKRALPW%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T132044Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECsaCXVzLXdlc3QtMiJIMEYCIQCre5hEZWeQOWWJnE%2BjOk7OvsDU9cHuhsLq6nhhjjlxpAIhALhKaDA3esoIRJ4DShVpctgCH439c7lthdI2SszRoRzeKv8DCEQQABoMNjM3NDIzMTgzODA1Igxmh76VEbLUIOGGbWwq3ANHmiFha%2BtycMWWLuSs2Pp%2BS4aoPr0o5B8Ws8N7%2FKvaMIjCPeFpoGC6MFcKpuEzsaFEVpj%2B7BXrdZ7KKVuTLqY%2F4Utc%2B%2FkYclVLw6VVA%2FPO5XcEnkKbIzxkdaMxOg8gLYKEBD1y6VpSYg59DtWPBKR%2FtWvOXiwaIaCeBV0PSLioehdzILg%2BgYkB7uF92EoJvvLdXzXucG16BpA6oIywKmynEc%2FTKNAeAxj7%2Bl1ncQkl5Yj6IPDg4pqFQ%2Fg46o%2B8JEfWbbdEtIBEyNT2b2m68NmuDZ72CTMfkMKFb3BwNOuXzx3%2FfyrKoxI9QiRWAeiEsM15kXqp4ufOss0O%2F4KCNQdkZ19wb7mk2wDUmw6qA5mbT09v0d7A8kldP2ulYwP6IZiy%2B2TQM1XGza289n3WenTIFdv9JqhJf9wYblyLx0o1ON6GV3km6jnV7ddEx3Vbgj9%2BR6Jz07VR2zw9Zh09zGcu8ctu4cZekAx8YvgLaY2pRFppmN7yAtAx4NoFk%2F%2BgaCrQfjKgYOk4Fth5nSV4UZ2TuADLdErf0gO0Fbfy08bjDOY61KxIf5wgBbq6yA2ADU%2FUiq%2BgRFtrgppn78z9Ao4m4KXSZ7BjY7lkO2oLk4%2BuLQHKbcy6oJZKLEYIcTDmio29BjqkAUOMy%2FFQH9Z%2BPnGscLBJby3Q2yejFp1Bp1zgmCg3Zb3hthlFksQXEW7i%2BamtxsjAOXJklVloPjwoPEOJ3VXoD8vO2LZoRcQ8%2BX78CYN3lGZNdk7dUwgQULTS5nkvvtwlYetmNYMHhGpquWgJYij9%2BxsK0522MDASEvTI32kPewSdZkkhBb61c7OTiMOl9apmC8F0IIkMLRSg24srmgPRaFm4qykV&X-Amz-Signature=9fc5239d426a96b8c26595d089f79c4db747dcf7522cb084f67489042c3cd8d9&X-Amz-SignedHeaders=host&x-id=GetObject)
**Explanation:** When highway miles per gallon increases, the price of the vehicle tends to decrease. This negative correlation suggests that cars with higher fuel efficiency (more miles per gallon) are generally priced lower in the market.
___
### Weak Correlation
Weak correlation indicates a lack of strong relationship between the variables.
**Example: RPM and Price**
- **Weak Correlation:** Low and high RPM values show varied prices, indicating no strong predictive relationship.
- **Visualization:** Scatter plot with no clear trend or slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9f914514-8914-4bf4-ac84-d9e3077f6eb1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R6DLP7DA%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T132044Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECsaCXVzLXdlc3QtMiJIMEYCIQCBp2SpMc8hplSZoq10EfMxLuurFvXZ1SiIDSTXechizQIhAJxbCzLR8FfIZpA5pIhhT%2Fn41KXL4uwZXSi3oBipVp6PKv8DCEQQABoMNjM3NDIzMTgzODA1IgxOtnc6B4cmT%2Fx3WSMq3AMRtVw0h272KlF6IOsYYssB8tVjbVBd%2BX1M9Yf5onMDolMRS2uX5Ano2UDVCYBH%2BV%2F7cxYJmXh5zXOMwHRBWLdmHpfx6yu8egMfk46YoYiOlPNaTHAcSLjidqE1LtHwNgPAynVPdLZbREg6RbZ5Dq8fi2Kt2ulHuUarQRYCWqVullWO410O%2FLqyH3Np%2B9%2B7167jlly4zaQiFaZbAhuHehGkW2OeIvZd6vOoOKwZTi1NOug7Lmemd14GkUcw1zAVIzC%2BcQkr3x%2FP9rnlw7C6tJg6aimGoDq8f%2B9sjxnTJ6A4mYrctNyDOmkOvzRgwBgRNzviDWX8E4fVrbZ2aDIXpEGSz1e5rWvClVPDNJ5%2FUspRvjGPVmr1xMnw4TzN%2BeUWVWLnQFs3Ks87RKgrrCnWWXu0ADm0dwDFslYvwHu5pYMOxpyL3R%2BOCtU%2BQL8i0Wch2RUZJO5QzdFiGAyauMQ99W8o9FZjzaWcoELic3BhKnIoE9OOElK86funU5LK30%2BmS3ug4f%2BbO1XfCGseQQ%2F2tMj7l1zA63F85OEo4ULOsWX3%2BIKn1RewvN4lD7qROEYYEywIV4joSA4DjJlgf%2B0M%2Be%2BZArvQA0WnQ5rHPJb3dum9H97p3sXawMxFbAzZkTCdi429BjqkAfLUtbR32EdcBEDPb3l3WcVirGKPtGZri5F6M9D6arKYRSjCjF59CjzL0%2Fn9tfl38PcVD7LZbGv0LWmPs3B1Mmpsbu5WPwcrRl4IqwRweJyaOZk%2BOCSIge%2BmO%2B0uUQl5xC%2FyPb04FbvfmXm1WtjjqCHt7Yd0F6SMW0J4EJO0pvQq3wDqPwJe58PeMiRWKYnzSJT1eXCcQ4yokYSYUE6A4MPaqPXD&X-Amz-Signature=b6739b404f82c4762cc5a27d7a2f2d6aedad907ef5f816159bd1c7ad93d69953&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f18086e5-5b04-4fbf-8309-8944ab20d213/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UMNI27U6%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T132044Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECsaCXVzLXdlc3QtMiJHMEUCIC7Od4nAXINIO2y7rIvt8biN5pDdUIPq2TeLUToiOVklAiEA0nLLFNKWXEkwjyE%2B3JKaiG4J0zVBnA0osoHOcRYHSMgq%2FwMIRBAAGgw2Mzc0MjMxODM4MDUiDF3S4jRb6NYH7%2FWRzCrcA4LXD9IjsTbMNBsxGcc44KcjFvr1H7tSzdfbvSfSB2aechLrePCBPPsQzCZV3YcchZKpBN5cIrl28b0j7dNf7AVQRwEsJzoCTBtxs%2FZ21GgN6XRub426TGSGVUHFBKaHJuzq5zhqmOL6dCucV1v7kXSY%2BY9okKLskRJC9fb50Dl87s3sDCKnW695ojtvimdfnsuQqfIdZK%2BwZF5JM4M3zsO4mJ2N6KQYudXlYvYCL2SEnw8CqM94ErmKeo3af7bi1icJ7Gzhx0L0uWWclIlRAfX1syog3veX4WvIUQSlWZnT939lcRze3gGVpqBk%2BayPEALQzkARCMzFzjuhGs2MAMxPr0yj3HjPYYc73JP9umLzgKkkx0tbr%2FSKeZ1kXU2TFiu21TdC5peCMZDVhKAt5N28x%2F9xaLRv%2BFoUs64Qtd3d8XVV2CE1q2TExc6DuQSnYbcrOyVtbJQ8Uz%2BYi44Bd9fCI39BJV0CtwYmIFOWtwuXwC1aORtp5Hq7K3bQ96J00QwfTlhXfqjqsyrYAJFZKGgawMpXJPVxlwORMLJWsBfk8AaSVtN%2BNLkudIZUo8DtT4%2BdI0kVFjdXzCdDQ0%2FAcy2aL1k0Ie92Fwy1CWgqPZ%2FY99E01E72OawSz41aMJmLjb0GOqUBsOaZ4E1qM6NhZK2FJ5I478WXCMHvlAK2HZXnjd6CodkTrHueKxHEz98q8TKwgzeCmbyAnYNWIhA9De04re%2FR55HaUuUo0JqtRjf8FkyckdHWXyzNWxi3c7wuUYG1rUiWehWWwUh7wHKduqAtqrO88MU0ojnPT1MeiWW9o3BoG1vNbXT8iSYW2l3zAW8SpmM0kicguyDH8pK%2B2rZcPebdzbRezHBz&X-Amz-Signature=0f63611be900e7f6cfcee8ef1907eeb23c8babc5ed1acf2b7d1088cbe20b219c&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Correlation Plot
Heatmap visualizes correlations among variables. Color scheme indicates Pearson correlation coefficients. Dark red diagonal line shows perfect correlation (value of 1) between variables and themselves.
This heatmap offers overview of variable relationships and their link with price.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cd3b341e-cc1a-45f7-8aec-cdc00436d270/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UMNI27U6%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T132044Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECsaCXVzLXdlc3QtMiJHMEUCIC7Od4nAXINIO2y7rIvt8biN5pDdUIPq2TeLUToiOVklAiEA0nLLFNKWXEkwjyE%2B3JKaiG4J0zVBnA0osoHOcRYHSMgq%2FwMIRBAAGgw2Mzc0MjMxODM4MDUiDF3S4jRb6NYH7%2FWRzCrcA4LXD9IjsTbMNBsxGcc44KcjFvr1H7tSzdfbvSfSB2aechLrePCBPPsQzCZV3YcchZKpBN5cIrl28b0j7dNf7AVQRwEsJzoCTBtxs%2FZ21GgN6XRub426TGSGVUHFBKaHJuzq5zhqmOL6dCucV1v7kXSY%2BY9okKLskRJC9fb50Dl87s3sDCKnW695ojtvimdfnsuQqfIdZK%2BwZF5JM4M3zsO4mJ2N6KQYudXlYvYCL2SEnw8CqM94ErmKeo3af7bi1icJ7Gzhx0L0uWWclIlRAfX1syog3veX4WvIUQSlWZnT939lcRze3gGVpqBk%2BayPEALQzkARCMzFzjuhGs2MAMxPr0yj3HjPYYc73JP9umLzgKkkx0tbr%2FSKeZ1kXU2TFiu21TdC5peCMZDVhKAt5N28x%2F9xaLRv%2BFoUs64Qtd3d8XVV2CE1q2TExc6DuQSnYbcrOyVtbJQ8Uz%2BYi44Bd9fCI39BJV0CtwYmIFOWtwuXwC1aORtp5Hq7K3bQ96J00QwfTlhXfqjqsyrYAJFZKGgawMpXJPVxlwORMLJWsBfk8AaSVtN%2BNLkudIZUo8DtT4%2BdI0kVFjdXzCdDQ0%2FAcy2aL1k0Ie92Fwy1CWgqPZ%2FY99E01E72OawSz41aMJmLjb0GOqUBsOaZ4E1qM6NhZK2FJ5I478WXCMHvlAK2HZXnjd6CodkTrHueKxHEz98q8TKwgzeCmbyAnYNWIhA9De04re%2FR55HaUuUo0JqtRjf8FkyckdHWXyzNWxi3c7wuUYG1rUiWehWWwUh7wHKduqAtqrO88MU0ojnPT1MeiWW9o3BoG1vNbXT8iSYW2l3zAW8SpmM0kicguyDH8pK%2B2rZcPebdzbRezHBz&X-Amz-Signature=834cc928a1ed444f8bfa14cad575eb89432235ceb7f279654f49a73a8fa8d1ef&X-Amz-SignedHeaders=host&x-id=GetObject)

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
