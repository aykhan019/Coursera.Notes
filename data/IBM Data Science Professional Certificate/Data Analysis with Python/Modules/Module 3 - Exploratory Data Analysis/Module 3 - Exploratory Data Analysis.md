

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7e6d594d-952e-44b6-97ea-31225882aea6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RVHOXDGB%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T191126Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBsaCXVzLXdlc3QtMiJGMEQCIB00NBVVUZxdxV44w9OOWjpnR79MC5vHMIoXaYwHdtscAiASEiKu0AL2xcZlrSGlAPvbrtGvOnNrLcbtcBQF48c6iSr%2FAwg0EAAaDDYzNzQyMzE4MzgwNSIMzPf%2BTPT8CSMIAKNiKtwDCWwkPGE%2F%2FoBxNhfjJs%2BEfY9%2Bh%2BfIsrM11cQfaU3i%2FueHS2lNXQWy4bnSF9711bzxfXSw92NGICgTt1zGilyF4WjSwiotJkMg8uu9BHf0cwz7BZXtV5LY81PqR3P%2BNPVlFfjOi88AK%2FN1m0nMcxhlsmHs1OhR2t92MoQ7ad5QnDsVBDcavR99BS6FA9SgK4hIFefc1vmdvhFvS68pcIujIr6QA0rQNyrnQV1avpuql1Piq7RIPfh5sKZyUdSZhXO%2Be1ljPBeJeSGssNyfTsSgZoQsAvs35RJPsW%2BNXxIsUVg67G1A8p9HxpKKdj%2BL50LgpJoJeEDUKWgFz3KhjvWl48BaZ%2BWqsbsuVgph1K%2Fi7gNW5pZ%2BQU68EcaGsYSWBxJa9tb3SxUC6UrPFiq431jv5RVel9BpeGOEnuGyBxsaDve4DfCeejAkqHH8yaS31YLYw4RtQ3emCu%2Bggmf9FlYG5fzMlZduXqp26DMdj%2BD8PfRa7Om6wnoOSx8qaq4aP9N55FaHbkd69sWh77crkPIGnVpiCEz8uGkAA%2FclcVix6HsvNtFF4Pj3pF4t1Ngl8MY9MM3NWOW0ip2X9A1NjTyFWWjdcKfSJUXQWnU7GfmKGmjAFAv7MFSbYCfQjfkw87yJvQY6pgG1FemlBu4rN8hoQ8oj3gEgT5ww7%2B8L1biAVWDXVyyC4D2ipq4no5rlM0K%2BZ6ZNV57l1PZYJEx8TtTt4b74rs25CZJXaLHdNGfGWEMiKgbXTAoVRBRkTDU%2FPm3KB9aEAPHS%2Ffg1lmnK7PZQf6gE1gbZU0QSavEfTqNfTV2A0B81d4wE30y1GCfcoVzx8Ipe6%2FYdQAzAjfIeRDXX%2B6Mn2d4G8qtA3qVt&X-Amz-Signature=8a74c71213e53bc039b61ba988d1df225222529e6c1395f34b699ff928c975de&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cbfaed9e-b398-4902-8936-dea058b21def/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RVHOXDGB%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T191126Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBsaCXVzLXdlc3QtMiJGMEQCIB00NBVVUZxdxV44w9OOWjpnR79MC5vHMIoXaYwHdtscAiASEiKu0AL2xcZlrSGlAPvbrtGvOnNrLcbtcBQF48c6iSr%2FAwg0EAAaDDYzNzQyMzE4MzgwNSIMzPf%2BTPT8CSMIAKNiKtwDCWwkPGE%2F%2FoBxNhfjJs%2BEfY9%2Bh%2BfIsrM11cQfaU3i%2FueHS2lNXQWy4bnSF9711bzxfXSw92NGICgTt1zGilyF4WjSwiotJkMg8uu9BHf0cwz7BZXtV5LY81PqR3P%2BNPVlFfjOi88AK%2FN1m0nMcxhlsmHs1OhR2t92MoQ7ad5QnDsVBDcavR99BS6FA9SgK4hIFefc1vmdvhFvS68pcIujIr6QA0rQNyrnQV1avpuql1Piq7RIPfh5sKZyUdSZhXO%2Be1ljPBeJeSGssNyfTsSgZoQsAvs35RJPsW%2BNXxIsUVg67G1A8p9HxpKKdj%2BL50LgpJoJeEDUKWgFz3KhjvWl48BaZ%2BWqsbsuVgph1K%2Fi7gNW5pZ%2BQU68EcaGsYSWBxJa9tb3SxUC6UrPFiq431jv5RVel9BpeGOEnuGyBxsaDve4DfCeejAkqHH8yaS31YLYw4RtQ3emCu%2Bggmf9FlYG5fzMlZduXqp26DMdj%2BD8PfRa7Om6wnoOSx8qaq4aP9N55FaHbkd69sWh77crkPIGnVpiCEz8uGkAA%2FclcVix6HsvNtFF4Pj3pF4t1Ngl8MY9MM3NWOW0ip2X9A1NjTyFWWjdcKfSJUXQWnU7GfmKGmjAFAv7MFSbYCfQjfkw87yJvQY6pgG1FemlBu4rN8hoQ8oj3gEgT5ww7%2B8L1biAVWDXVyyC4D2ipq4no5rlM0K%2BZ6ZNV57l1PZYJEx8TtTt4b74rs25CZJXaLHdNGfGWEMiKgbXTAoVRBRkTDU%2FPm3KB9aEAPHS%2Ffg1lmnK7PZQf6gE1gbZU0QSavEfTqNfTV2A0B81d4wE30y1GCfcoVzx8Ipe6%2FYdQAzAjfIeRDXX%2B6Mn2d4G8qtA3qVt&X-Amz-Signature=d2f16113c31f5d9ae41f744ae3301656e96760c6838a371995f20862cf2af3c4&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/91181646-b1e0-4433-9711-6259a96a9247/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RVHOXDGB%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T191126Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBsaCXVzLXdlc3QtMiJGMEQCIB00NBVVUZxdxV44w9OOWjpnR79MC5vHMIoXaYwHdtscAiASEiKu0AL2xcZlrSGlAPvbrtGvOnNrLcbtcBQF48c6iSr%2FAwg0EAAaDDYzNzQyMzE4MzgwNSIMzPf%2BTPT8CSMIAKNiKtwDCWwkPGE%2F%2FoBxNhfjJs%2BEfY9%2Bh%2BfIsrM11cQfaU3i%2FueHS2lNXQWy4bnSF9711bzxfXSw92NGICgTt1zGilyF4WjSwiotJkMg8uu9BHf0cwz7BZXtV5LY81PqR3P%2BNPVlFfjOi88AK%2FN1m0nMcxhlsmHs1OhR2t92MoQ7ad5QnDsVBDcavR99BS6FA9SgK4hIFefc1vmdvhFvS68pcIujIr6QA0rQNyrnQV1avpuql1Piq7RIPfh5sKZyUdSZhXO%2Be1ljPBeJeSGssNyfTsSgZoQsAvs35RJPsW%2BNXxIsUVg67G1A8p9HxpKKdj%2BL50LgpJoJeEDUKWgFz3KhjvWl48BaZ%2BWqsbsuVgph1K%2Fi7gNW5pZ%2BQU68EcaGsYSWBxJa9tb3SxUC6UrPFiq431jv5RVel9BpeGOEnuGyBxsaDve4DfCeejAkqHH8yaS31YLYw4RtQ3emCu%2Bggmf9FlYG5fzMlZduXqp26DMdj%2BD8PfRa7Om6wnoOSx8qaq4aP9N55FaHbkd69sWh77crkPIGnVpiCEz8uGkAA%2FclcVix6HsvNtFF4Pj3pF4t1Ngl8MY9MM3NWOW0ip2X9A1NjTyFWWjdcKfSJUXQWnU7GfmKGmjAFAv7MFSbYCfQjfkw87yJvQY6pgG1FemlBu4rN8hoQ8oj3gEgT5ww7%2B8L1biAVWDXVyyC4D2ipq4no5rlM0K%2BZ6ZNV57l1PZYJEx8TtTt4b74rs25CZJXaLHdNGfGWEMiKgbXTAoVRBRkTDU%2FPm3KB9aEAPHS%2Ffg1lmnK7PZQf6gE1gbZU0QSavEfTqNfTV2A0B81d4wE30y1GCfcoVzx8Ipe6%2FYdQAzAjfIeRDXX%2B6Mn2d4G8qtA3qVt&X-Amz-Signature=29cd316146c0739938dbf57cb2d193159cdba2a52255ed4ac4cbb0e78437fe09&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/09aba1c0-0d55-41dd-852a-a04c5b8a3fac/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VQ2TJLKF%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T191127Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBsaCXVzLXdlc3QtMiJHMEUCIHjy5bYBS1IZ%2FQywOnPYUIb0fMri1XOLgtsHYAkNbBk%2BAiEArnfOkR9CRribj%2FzTNhF2RXi0rjMsWUGtemEV0IiyFI0q%2FwMINBAAGgw2Mzc0MjMxODM4MDUiDBycxV15OSp0HV973CrcA7OoLCn%2BDIhdkLuMOa0Md2c%2BC%2BI6UrrnC%2BSzfZRuKVpLhTSFt8eFH4qFIp%2Fpb78JhR7DKI%2BbDP3ArxBsEA%2B3KCs5aluYmzu%2Bp01w%2BG%2BvMtmDdDB6%2Fiym20CTr9f5J5qg7Uj2n1N4iARRMgEBxxWPbgwDtmC%2BEkFx60KbiCgP19%2BChaW38WhTkaWQiBr9HqaVgntsIidiD%2F9k9xIwOCyMv7BO5GawvQue9ro1TW0e6NDnHWGba%2BsPeieqJGVVuRosvHbSgP4X590jeG3OumX2bt8vZ8ShtIh9pmZCnQdZQYCk2lbU8JEAbrjwBifSVX7UPmRz40St1TQvYaBKPL0vZlCmb%2FbA1CQCri7vjHhMBJsMJWuCEmn0ziyZGnQNWjpbOS7O11FQ44ZSRrwfFMr0fennj3GQhsw4fBIqBGCxurZF%2Bj6y4oYro2xgTOSQWuOWamvfG6QuYYOYQaOdsvmAPhVHmH02wT%2BCxgMlcsbLCtfpwJEDW6vfe5B84lpDvsX6Tl%2FvphkF4HHVu0gywfv7QGYdGVTIldNeSKTYMLWYg1WqUg5zHovPAcRd3gKVYnFsNGXKMO6eDQ6UIC8aRMwtswLzJtzzZAmiXgwAjiKAnlEzHvWhyhkK1tWHfWYOMOq8ib0GOqUBWK6sDTRUUJrvFMwYlKyN8cmXGB7vxjgMJuMZqPDv8kfHaWiqjBlVEtIOpw406c3zmzs0cdiITowQHHNEh9Zshs%2Bf8P1g2VcVdcRefBjqAa0cYDv77Gv5TDUltinV1lzLoGpjjj%2BDABh0DDQWKw%2BhJTdjEGbgu7zWU7sUT3WdxgqgJhP%2BxHkZ4KINfIPI6fEKovC%2FmZVxurwnVUgqx3AZpMpabpA5&X-Amz-Signature=9c33e340437d21bfa6346a3a63cae8b0da2cd845dd05c933b45497e8cc0fafe8&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 2. Scatter Plot
Scatter plots present the relationship between two variables in a dataset. It represents data points on a two-dimensional plane. The independent variable or attribute is plotted on the X-axis, while the dependent variable is plotted on the Y-axis.
**Syntax:**
```python
plt.scatter(x, y)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23708af9-659f-4f23-b626-1a4292d7842c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VQ2TJLKF%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T191127Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBsaCXVzLXdlc3QtMiJHMEUCIHjy5bYBS1IZ%2FQywOnPYUIb0fMri1XOLgtsHYAkNbBk%2BAiEArnfOkR9CRribj%2FzTNhF2RXi0rjMsWUGtemEV0IiyFI0q%2FwMINBAAGgw2Mzc0MjMxODM4MDUiDBycxV15OSp0HV973CrcA7OoLCn%2BDIhdkLuMOa0Md2c%2BC%2BI6UrrnC%2BSzfZRuKVpLhTSFt8eFH4qFIp%2Fpb78JhR7DKI%2BbDP3ArxBsEA%2B3KCs5aluYmzu%2Bp01w%2BG%2BvMtmDdDB6%2Fiym20CTr9f5J5qg7Uj2n1N4iARRMgEBxxWPbgwDtmC%2BEkFx60KbiCgP19%2BChaW38WhTkaWQiBr9HqaVgntsIidiD%2F9k9xIwOCyMv7BO5GawvQue9ro1TW0e6NDnHWGba%2BsPeieqJGVVuRosvHbSgP4X590jeG3OumX2bt8vZ8ShtIh9pmZCnQdZQYCk2lbU8JEAbrjwBifSVX7UPmRz40St1TQvYaBKPL0vZlCmb%2FbA1CQCri7vjHhMBJsMJWuCEmn0ziyZGnQNWjpbOS7O11FQ44ZSRrwfFMr0fennj3GQhsw4fBIqBGCxurZF%2Bj6y4oYro2xgTOSQWuOWamvfG6QuYYOYQaOdsvmAPhVHmH02wT%2BCxgMlcsbLCtfpwJEDW6vfe5B84lpDvsX6Tl%2FvphkF4HHVu0gywfv7QGYdGVTIldNeSKTYMLWYg1WqUg5zHovPAcRd3gKVYnFsNGXKMO6eDQ6UIC8aRMwtswLzJtzzZAmiXgwAjiKAnlEzHvWhyhkK1tWHfWYOMOq8ib0GOqUBWK6sDTRUUJrvFMwYlKyN8cmXGB7vxjgMJuMZqPDv8kfHaWiqjBlVEtIOpw406c3zmzs0cdiITowQHHNEh9Zshs%2Bf8P1g2VcVdcRefBjqAa0cYDv77Gv5TDUltinV1lzLoGpjjj%2BDABh0DDQWKw%2BhJTdjEGbgu7zWU7sUT3WdxgqgJhP%2BxHkZ4KINfIPI6fEKovC%2FmZVxurwnVUgqx3AZpMpabpA5&X-Amz-Signature=6307cae975490532e2b6a820b995f392568edd8b6cb72203fe2f606e25644aa9&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 3. Histogram
A histogram is an important visual representation of data in categorical form. To view the data in a "Binned" form, use the histogram plot with a number of bins required or with the data points that mark the bin edges. The x-axis represents the data bins, and the y-axis represents the number of elements in each bin.
**Syntax:**
```python
plt.hist(x, bins)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/24e4424a-df87-40a1-b63b-195cbdc2e0ab/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VQ2TJLKF%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T191127Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBsaCXVzLXdlc3QtMiJHMEUCIHjy5bYBS1IZ%2FQywOnPYUIb0fMri1XOLgtsHYAkNbBk%2BAiEArnfOkR9CRribj%2FzTNhF2RXi0rjMsWUGtemEV0IiyFI0q%2FwMINBAAGgw2Mzc0MjMxODM4MDUiDBycxV15OSp0HV973CrcA7OoLCn%2BDIhdkLuMOa0Md2c%2BC%2BI6UrrnC%2BSzfZRuKVpLhTSFt8eFH4qFIp%2Fpb78JhR7DKI%2BbDP3ArxBsEA%2B3KCs5aluYmzu%2Bp01w%2BG%2BvMtmDdDB6%2Fiym20CTr9f5J5qg7Uj2n1N4iARRMgEBxxWPbgwDtmC%2BEkFx60KbiCgP19%2BChaW38WhTkaWQiBr9HqaVgntsIidiD%2F9k9xIwOCyMv7BO5GawvQue9ro1TW0e6NDnHWGba%2BsPeieqJGVVuRosvHbSgP4X590jeG3OumX2bt8vZ8ShtIh9pmZCnQdZQYCk2lbU8JEAbrjwBifSVX7UPmRz40St1TQvYaBKPL0vZlCmb%2FbA1CQCri7vjHhMBJsMJWuCEmn0ziyZGnQNWjpbOS7O11FQ44ZSRrwfFMr0fennj3GQhsw4fBIqBGCxurZF%2Bj6y4oYro2xgTOSQWuOWamvfG6QuYYOYQaOdsvmAPhVHmH02wT%2BCxgMlcsbLCtfpwJEDW6vfe5B84lpDvsX6Tl%2FvphkF4HHVu0gywfv7QGYdGVTIldNeSKTYMLWYg1WqUg5zHovPAcRd3gKVYnFsNGXKMO6eDQ6UIC8aRMwtswLzJtzzZAmiXgwAjiKAnlEzHvWhyhkK1tWHfWYOMOq8ib0GOqUBWK6sDTRUUJrvFMwYlKyN8cmXGB7vxjgMJuMZqPDv8kfHaWiqjBlVEtIOpw406c3zmzs0cdiITowQHHNEh9Zshs%2Bf8P1g2VcVdcRefBjqAa0cYDv77Gv5TDUltinV1lzLoGpjjj%2BDABh0DDQWKw%2BhJTdjEGbgu7zWU7sUT3WdxgqgJhP%2BxHkZ4KINfIPI6fEKovC%2FmZVxurwnVUgqx3AZpMpabpA5&X-Amz-Signature=139c8156daa7ddbfeb510cd1bda6b49244e1535b618cd74b4ff8558c9a9361fc&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ab5a6dfe-51f5-43ee-bcb3-33dae4a1c7ad/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VQ2TJLKF%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T191127Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBsaCXVzLXdlc3QtMiJHMEUCIHjy5bYBS1IZ%2FQywOnPYUIb0fMri1XOLgtsHYAkNbBk%2BAiEArnfOkR9CRribj%2FzTNhF2RXi0rjMsWUGtemEV0IiyFI0q%2FwMINBAAGgw2Mzc0MjMxODM4MDUiDBycxV15OSp0HV973CrcA7OoLCn%2BDIhdkLuMOa0Md2c%2BC%2BI6UrrnC%2BSzfZRuKVpLhTSFt8eFH4qFIp%2Fpb78JhR7DKI%2BbDP3ArxBsEA%2B3KCs5aluYmzu%2Bp01w%2BG%2BvMtmDdDB6%2Fiym20CTr9f5J5qg7Uj2n1N4iARRMgEBxxWPbgwDtmC%2BEkFx60KbiCgP19%2BChaW38WhTkaWQiBr9HqaVgntsIidiD%2F9k9xIwOCyMv7BO5GawvQue9ro1TW0e6NDnHWGba%2BsPeieqJGVVuRosvHbSgP4X590jeG3OumX2bt8vZ8ShtIh9pmZCnQdZQYCk2lbU8JEAbrjwBifSVX7UPmRz40St1TQvYaBKPL0vZlCmb%2FbA1CQCri7vjHhMBJsMJWuCEmn0ziyZGnQNWjpbOS7O11FQ44ZSRrwfFMr0fennj3GQhsw4fBIqBGCxurZF%2Bj6y4oYro2xgTOSQWuOWamvfG6QuYYOYQaOdsvmAPhVHmH02wT%2BCxgMlcsbLCtfpwJEDW6vfe5B84lpDvsX6Tl%2FvphkF4HHVu0gywfv7QGYdGVTIldNeSKTYMLWYg1WqUg5zHovPAcRd3gKVYnFsNGXKMO6eDQ6UIC8aRMwtswLzJtzzZAmiXgwAjiKAnlEzHvWhyhkK1tWHfWYOMOq8ib0GOqUBWK6sDTRUUJrvFMwYlKyN8cmXGB7vxjgMJuMZqPDv8kfHaWiqjBlVEtIOpw406c3zmzs0cdiITowQHHNEh9Zshs%2Bf8P1g2VcVdcRefBjqAa0cYDv77Gv5TDUltinV1lzLoGpjjj%2BDABh0DDQWKw%2BhJTdjEGbgu7zWU7sUT3WdxgqgJhP%2BxHkZ4KINfIPI6fEKovC%2FmZVxurwnVUgqx3AZpMpabpA5&X-Amz-Signature=4c9a104f00d7cbab688b41a000f53c25827dae21544c292c600a856ebcf350a6&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8f1b1d60-cf1b-42b3-9faa-f634c89c3f84/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VQ2TJLKF%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T191127Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBsaCXVzLXdlc3QtMiJHMEUCIHjy5bYBS1IZ%2FQywOnPYUIb0fMri1XOLgtsHYAkNbBk%2BAiEArnfOkR9CRribj%2FzTNhF2RXi0rjMsWUGtemEV0IiyFI0q%2FwMINBAAGgw2Mzc0MjMxODM4MDUiDBycxV15OSp0HV973CrcA7OoLCn%2BDIhdkLuMOa0Md2c%2BC%2BI6UrrnC%2BSzfZRuKVpLhTSFt8eFH4qFIp%2Fpb78JhR7DKI%2BbDP3ArxBsEA%2B3KCs5aluYmzu%2Bp01w%2BG%2BvMtmDdDB6%2Fiym20CTr9f5J5qg7Uj2n1N4iARRMgEBxxWPbgwDtmC%2BEkFx60KbiCgP19%2BChaW38WhTkaWQiBr9HqaVgntsIidiD%2F9k9xIwOCyMv7BO5GawvQue9ro1TW0e6NDnHWGba%2BsPeieqJGVVuRosvHbSgP4X590jeG3OumX2bt8vZ8ShtIh9pmZCnQdZQYCk2lbU8JEAbrjwBifSVX7UPmRz40St1TQvYaBKPL0vZlCmb%2FbA1CQCri7vjHhMBJsMJWuCEmn0ziyZGnQNWjpbOS7O11FQ44ZSRrwfFMr0fennj3GQhsw4fBIqBGCxurZF%2Bj6y4oYro2xgTOSQWuOWamvfG6QuYYOYQaOdsvmAPhVHmH02wT%2BCxgMlcsbLCtfpwJEDW6vfe5B84lpDvsX6Tl%2FvphkF4HHVu0gywfv7QGYdGVTIldNeSKTYMLWYg1WqUg5zHovPAcRd3gKVYnFsNGXKMO6eDQ6UIC8aRMwtswLzJtzzZAmiXgwAjiKAnlEzHvWhyhkK1tWHfWYOMOq8ib0GOqUBWK6sDTRUUJrvFMwYlKyN8cmXGB7vxjgMJuMZqPDv8kfHaWiqjBlVEtIOpw406c3zmzs0cdiITowQHHNEh9Zshs%2Bf8P1g2VcVdcRefBjqAa0cYDv77Gv5TDUltinV1lzLoGpjjj%2BDABh0DDQWKw%2BhJTdjEGbgu7zWU7sUT3WdxgqgJhP%2BxHkZ4KINfIPI6fEKovC%2FmZVxurwnVUgqx3AZpMpabpA5&X-Amz-Signature=fd69389e30fb30e3f05c03536be9db0fac46204d75849add84e47216dfba0b7c&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/13ad0497-05fe-4eaa-984e-707b33e14761/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VQ2TJLKF%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T191127Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBsaCXVzLXdlc3QtMiJHMEUCIHjy5bYBS1IZ%2FQywOnPYUIb0fMri1XOLgtsHYAkNbBk%2BAiEArnfOkR9CRribj%2FzTNhF2RXi0rjMsWUGtemEV0IiyFI0q%2FwMINBAAGgw2Mzc0MjMxODM4MDUiDBycxV15OSp0HV973CrcA7OoLCn%2BDIhdkLuMOa0Md2c%2BC%2BI6UrrnC%2BSzfZRuKVpLhTSFt8eFH4qFIp%2Fpb78JhR7DKI%2BbDP3ArxBsEA%2B3KCs5aluYmzu%2Bp01w%2BG%2BvMtmDdDB6%2Fiym20CTr9f5J5qg7Uj2n1N4iARRMgEBxxWPbgwDtmC%2BEkFx60KbiCgP19%2BChaW38WhTkaWQiBr9HqaVgntsIidiD%2F9k9xIwOCyMv7BO5GawvQue9ro1TW0e6NDnHWGba%2BsPeieqJGVVuRosvHbSgP4X590jeG3OumX2bt8vZ8ShtIh9pmZCnQdZQYCk2lbU8JEAbrjwBifSVX7UPmRz40St1TQvYaBKPL0vZlCmb%2FbA1CQCri7vjHhMBJsMJWuCEmn0ziyZGnQNWjpbOS7O11FQ44ZSRrwfFMr0fennj3GQhsw4fBIqBGCxurZF%2Bj6y4oYro2xgTOSQWuOWamvfG6QuYYOYQaOdsvmAPhVHmH02wT%2BCxgMlcsbLCtfpwJEDW6vfe5B84lpDvsX6Tl%2FvphkF4HHVu0gywfv7QGYdGVTIldNeSKTYMLWYg1WqUg5zHovPAcRd3gKVYnFsNGXKMO6eDQ6UIC8aRMwtswLzJtzzZAmiXgwAjiKAnlEzHvWhyhkK1tWHfWYOMOq8ib0GOqUBWK6sDTRUUJrvFMwYlKyN8cmXGB7vxjgMJuMZqPDv8kfHaWiqjBlVEtIOpw406c3zmzs0cdiITowQHHNEh9Zshs%2Bf8P1g2VcVdcRefBjqAa0cYDv77Gv5TDUltinV1lzLoGpjjj%2BDABh0DDQWKw%2BhJTdjEGbgu7zWU7sUT3WdxgqgJhP%2BxHkZ4KINfIPI6fEKovC%2FmZVxurwnVUgqx3AZpMpabpA5&X-Amz-Signature=17066c0992945bdcfb26c7fe49ce67d0f2b5291cb547ab33466d7218ec78d091&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 2. Box and Whisker Plot
A box plot shows the distribution of quantitative data in a way that facilitates comparisons between variables or across levels of a categorical variable. The box shows the quartiles of the dataset while the whiskers extend to show the rest of the distribution, except for points that are determined to be "outliers".
**Syntax:**
```python
sns.boxplot(x='header_1', y='header_2', data=df)
```
**Example Output:**


![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d207ae92-0a7c-4e2f-aa65-0ee5a2c33bf7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665WRADZOQ%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T191128Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBsaCXVzLXdlc3QtMiJHMEUCIAbNaFXdYp2oe7xAVVrQ4CByNXpUX2sI7J0KWOevsN5cAiEA7pybWSyF8YQE1ZcNEIXRb%2FX%2BjAcImNXFxdDdc5LJZwAq%2FwMINBAAGgw2Mzc0MjMxODM4MDUiDNRRC1mDLqhDNaD2dyrcA8J1JoKkGoA6FMwfT4hdjD4LoO6HRW1CUcDsh89DFe3gBqOk3gkOdIHIqxuMf%2FA6oSQA99a2vG4z%2F2pQd3bU4js6wVA%2Fcdagx%2BkEwXXHpdzwsWfB9PuVqBjtLo182hpDWKeJtHLZdTtsNuPwxgYrbm9scTZSG7fX0lpLRDPBEq9%2Fl1wgb1JezHOtDJO7%2F6Y5Sp50Qu1FAyBfxeDL7Rxu6o%2FUDN%2Bgni4qhYpaSm%2FbbnlADBWoD62lmWTgRjayOqU1ilq%2Fm2Kt8dG2I8ozE02ZhsOkK%2FrROIsOmz5Rk0eESyfpImTUPSwFB%2BPglpvaXataze5%2BJlpqE2STECLdI%2BzXdJgTLTTTBGmt1HNVB4hPKMZWOzEs8%2FLqM9QrrMm0844HRCzKOrsKqGfM%2FPjCKU7CG%2FxvZrp2ARTPAR5RYIK9ulKufuHlr7rNI6R44FQHvapxgXDToPjHM%2FUJYpxqCgC6RmQvtwqfwwp1eYtmZ4TEEUHY3EoAovPzzQGZvNqbNQDJ%2Bbd3nRotV2b7bhROrQUx1yCBPzUsiRjCH%2FMqLjL0qaVrL%2BltpKBT8m%2FW%2BWzGlDeZYgL0x1if%2Bw%2FRuIA2CkDd4R%2FeR6dax%2Bd8mFhioP05Q1Wfvx5TTQL6dSio9p8dMOC9ib0GOqUBbpIvkcHGIt5lYfUB5Wf4WyHoaK%2BsXPGIDJJdzTser0y7Oy0QxCl5jcASo10W1T9HfmNRETK%2Blt1Ct4ic%2BCAWAcPICHr2BPrq42uvZ0G%2BIV4Q2Fdu7ImeKe52h1fL3WhqCQg3qcK7vBOPZeQ2eIsgcgMZTploRnYTm8iXUkIglKJNCgYoPstzdGcY0mySrTPDp2zWPdy7E2z%2BBwehGKURXivfd7ZZ&X-Amz-Signature=d845975966675d7ccf5d97fb922ea9a40331da6066e5983897c77f2da546de97&X-Amz-SignedHeaders=host&x-id=GetObject)

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0e516edc-7551-4792-ab18-0494db3c4c0c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RBEM3YKR%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T191128Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBsaCXVzLXdlc3QtMiJHMEUCIGL0DyQuG7Jg59hKBPwb5%2Fd2fN1D9I5Zy%2BYSVSZmennMAiEA2bO51ihOgsTKM9KeArz2ao3yhCwX74BJ1Ofn%2BkeMDq8q%2FwMINBAAGgw2Mzc0MjMxODM4MDUiDEA7uj4%2FWkh5kdLxJyrcA%2B%2F7q2UljUbUVmkgZ0KNsFFlAobNp0XWOvPKnliBu2fmC3wXgZyeyqr4tDa%2F8wPPW2YfQhtlJRBFcRvXhPzDhM8pm1rWCGLTHLWJhI9QFKS%2BpgVon9E2eVClfnMHqCQRDipBncyNnuqNV4UY1t%2FoqcCUb9Cg1CeVwUXF8mbLdQQRA4wphyEcOQkcUZcDtY20gYuR7Z5fTULDKoUeYluL0JEiU4nubjeY9hTpEKtj8Dk1LsaIU%2BsYuhbomHdRFNemj2O5cFsFM%2BXDD0fDsJHlvPGh%2BUnBWh4iW7jMIg0II84WWzCdtn2Yc6A1NFnHZBHPfSQ1ctQn8HKxQAezWIf%2F2vaD7LtXvS5WarUmR6ScKFMVsMHEKFWiF4MJe9fw%2F6P4zAQ1zXD%2BFBghDgcaoZL6Yye%2F9YkagCPwjVur0DjddT5jw%2BiG9F0B5gnoTREA%2B7mNFwcfJA4Khe6V%2F5dKnzMMOm9E00my7wV%2FJyKSwikjPG85rm4UHH9SABWOJ2ikc8bcKjwYi2orD2ksQNWR6PMOixXOahBjgsLwpCNLYYyGqeS%2BvfGGRfh1KiF4GobKQYTQgm8%2BRhHgP8SAluW%2FIs%2BeaV9HeS92GSIciz1%2BP21XxTcpQHtxVPWUeHbeLsqRMJy9ib0GOqUBDXg1sMGgVvoGYPI6qntCHDe3nwf%2BcbcMLWSzgw5pNQGEg5Zq%2BOdLp5DY7gcJ0sSuYbCAMQImyuGIz08PSztMjdPWxt3NEWfcFj9jXRuWT86K1GHaArhXCrVj%2FE6jnFO3mv4DMSv9CMluOenEg0qwL4OSXvsBZG%2F53wT%2Bx4rtBIfZQBgcSfvRwo7MlB%2FPHchajQyvZch%2F3A6vBbzaCfv9vQ1lgoRF&X-Amz-Signature=6e49c597c005c26c1853bf24dd8960e786c14af4d737bdd5c60c150c6c6849d8&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23a79b9d-2356-49a9-8fd9-65c6b0ab2cc5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VQ2TJLKF%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T191127Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBsaCXVzLXdlc3QtMiJHMEUCIHjy5bYBS1IZ%2FQywOnPYUIb0fMri1XOLgtsHYAkNbBk%2BAiEArnfOkR9CRribj%2FzTNhF2RXi0rjMsWUGtemEV0IiyFI0q%2FwMINBAAGgw2Mzc0MjMxODM4MDUiDBycxV15OSp0HV973CrcA7OoLCn%2BDIhdkLuMOa0Md2c%2BC%2BI6UrrnC%2BSzfZRuKVpLhTSFt8eFH4qFIp%2Fpb78JhR7DKI%2BbDP3ArxBsEA%2B3KCs5aluYmzu%2Bp01w%2BG%2BvMtmDdDB6%2Fiym20CTr9f5J5qg7Uj2n1N4iARRMgEBxxWPbgwDtmC%2BEkFx60KbiCgP19%2BChaW38WhTkaWQiBr9HqaVgntsIidiD%2F9k9xIwOCyMv7BO5GawvQue9ro1TW0e6NDnHWGba%2BsPeieqJGVVuRosvHbSgP4X590jeG3OumX2bt8vZ8ShtIh9pmZCnQdZQYCk2lbU8JEAbrjwBifSVX7UPmRz40St1TQvYaBKPL0vZlCmb%2FbA1CQCri7vjHhMBJsMJWuCEmn0ziyZGnQNWjpbOS7O11FQ44ZSRrwfFMr0fennj3GQhsw4fBIqBGCxurZF%2Bj6y4oYro2xgTOSQWuOWamvfG6QuYYOYQaOdsvmAPhVHmH02wT%2BCxgMlcsbLCtfpwJEDW6vfe5B84lpDvsX6Tl%2FvphkF4HHVu0gywfv7QGYdGVTIldNeSKTYMLWYg1WqUg5zHovPAcRd3gKVYnFsNGXKMO6eDQ6UIC8aRMwtswLzJtzzZAmiXgwAjiKAnlEzHvWhyhkK1tWHfWYOMOq8ib0GOqUBWK6sDTRUUJrvFMwYlKyN8cmXGB7vxjgMJuMZqPDv8kfHaWiqjBlVEtIOpw406c3zmzs0cdiITowQHHNEh9Zshs%2Bf8P1g2VcVdcRefBjqAa0cYDv77Gv5TDUltinV1lzLoGpjjj%2BDABh0DDQWKw%2BhJTdjEGbgu7zWU7sUT3WdxgqgJhP%2BxHkZ4KINfIPI6fEKovC%2FmZVxurwnVUgqx3AZpMpabpA5&X-Amz-Signature=fed98da61e168f890074d3f30d880c0880763af5ff7b359b44794da887c453e5&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 4. KDE Plot
A Kernel Density Estimate (KDE) plot is a graph that creates a probability distribution curve for the data based upon its likelihood of occurrence on a specific value. This is created for a single vector of information.
**Syntax:**
```python
sns.kdeplot(X) || sns.kdeplot(df['age'])
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0d571213-2a2f-4921-a50b-880847aa05ee/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VQ2TJLKF%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T191127Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBsaCXVzLXdlc3QtMiJHMEUCIHjy5bYBS1IZ%2FQywOnPYUIb0fMri1XOLgtsHYAkNbBk%2BAiEArnfOkR9CRribj%2FzTNhF2RXi0rjMsWUGtemEV0IiyFI0q%2FwMINBAAGgw2Mzc0MjMxODM4MDUiDBycxV15OSp0HV973CrcA7OoLCn%2BDIhdkLuMOa0Md2c%2BC%2BI6UrrnC%2BSzfZRuKVpLhTSFt8eFH4qFIp%2Fpb78JhR7DKI%2BbDP3ArxBsEA%2B3KCs5aluYmzu%2Bp01w%2BG%2BvMtmDdDB6%2Fiym20CTr9f5J5qg7Uj2n1N4iARRMgEBxxWPbgwDtmC%2BEkFx60KbiCgP19%2BChaW38WhTkaWQiBr9HqaVgntsIidiD%2F9k9xIwOCyMv7BO5GawvQue9ro1TW0e6NDnHWGba%2BsPeieqJGVVuRosvHbSgP4X590jeG3OumX2bt8vZ8ShtIh9pmZCnQdZQYCk2lbU8JEAbrjwBifSVX7UPmRz40St1TQvYaBKPL0vZlCmb%2FbA1CQCri7vjHhMBJsMJWuCEmn0ziyZGnQNWjpbOS7O11FQ44ZSRrwfFMr0fennj3GQhsw4fBIqBGCxurZF%2Bj6y4oYro2xgTOSQWuOWamvfG6QuYYOYQaOdsvmAPhVHmH02wT%2BCxgMlcsbLCtfpwJEDW6vfe5B84lpDvsX6Tl%2FvphkF4HHVu0gywfv7QGYdGVTIldNeSKTYMLWYg1WqUg5zHovPAcRd3gKVYnFsNGXKMO6eDQ6UIC8aRMwtswLzJtzzZAmiXgwAjiKAnlEzHvWhyhkK1tWHfWYOMOq8ib0GOqUBWK6sDTRUUJrvFMwYlKyN8cmXGB7vxjgMJuMZqPDv8kfHaWiqjBlVEtIOpw406c3zmzs0cdiITowQHHNEh9Zshs%2Bf8P1g2VcVdcRefBjqAa0cYDv77Gv5TDUltinV1lzLoGpjjj%2BDABh0DDQWKw%2BhJTdjEGbgu7zWU7sUT3WdxgqgJhP%2BxHkZ4KINfIPI6fEKovC%2FmZVxurwnVUgqx3AZpMpabpA5&X-Amz-Signature=814e7e616f34044581848d8e276eccca4882d8b08440758a3ed21de92760ffcd&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/53752550-ef82-4ca9-a01a-09921f0282d0/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VQ2TJLKF%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T191127Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBsaCXVzLXdlc3QtMiJHMEUCIHjy5bYBS1IZ%2FQywOnPYUIb0fMri1XOLgtsHYAkNbBk%2BAiEArnfOkR9CRribj%2FzTNhF2RXi0rjMsWUGtemEV0IiyFI0q%2FwMINBAAGgw2Mzc0MjMxODM4MDUiDBycxV15OSp0HV973CrcA7OoLCn%2BDIhdkLuMOa0Md2c%2BC%2BI6UrrnC%2BSzfZRuKVpLhTSFt8eFH4qFIp%2Fpb78JhR7DKI%2BbDP3ArxBsEA%2B3KCs5aluYmzu%2Bp01w%2BG%2BvMtmDdDB6%2Fiym20CTr9f5J5qg7Uj2n1N4iARRMgEBxxWPbgwDtmC%2BEkFx60KbiCgP19%2BChaW38WhTkaWQiBr9HqaVgntsIidiD%2F9k9xIwOCyMv7BO5GawvQue9ro1TW0e6NDnHWGba%2BsPeieqJGVVuRosvHbSgP4X590jeG3OumX2bt8vZ8ShtIh9pmZCnQdZQYCk2lbU8JEAbrjwBifSVX7UPmRz40St1TQvYaBKPL0vZlCmb%2FbA1CQCri7vjHhMBJsMJWuCEmn0ziyZGnQNWjpbOS7O11FQ44ZSRrwfFMr0fennj3GQhsw4fBIqBGCxurZF%2Bj6y4oYro2xgTOSQWuOWamvfG6QuYYOYQaOdsvmAPhVHmH02wT%2BCxgMlcsbLCtfpwJEDW6vfe5B84lpDvsX6Tl%2FvphkF4HHVu0gywfv7QGYdGVTIldNeSKTYMLWYg1WqUg5zHovPAcRd3gKVYnFsNGXKMO6eDQ6UIC8aRMwtswLzJtzzZAmiXgwAjiKAnlEzHvWhyhkK1tWHfWYOMOq8ib0GOqUBWK6sDTRUUJrvFMwYlKyN8cmXGB7vxjgMJuMZqPDv8kfHaWiqjBlVEtIOpw406c3zmzs0cdiITowQHHNEh9Zshs%2Bf8P1g2VcVdcRefBjqAa0cYDv77Gv5TDUltinV1lzLoGpjjj%2BDABh0DDQWKw%2BhJTdjEGbgu7zWU7sUT3WdxgqgJhP%2BxHkZ4KINfIPI6fEKovC%2FmZVxurwnVUgqx3AZpMpabpA5&X-Amz-Signature=4a8eedbfed0fe93447d7345f6f53600f1f19f2f8f57a2276fb380f358ac07fd9&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
## 4. Correlation Between Variables
Correlation is a statistical measure of the extent to which different variables are interdependent. It indicates how changes in one variable are associated with changes in another variable over time.
### Positive Correlation
Positive correlation indicates that as one variable increases, the other variable also tends to increase.
**Example: Engine Size and Price**
- **Positive Correlation:** Engine size increases, price also increases.
- **Visualization:** Scatter plot with a steep positive slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c7ea9b0-3ef3-4357-a9c3-554fc71b6b15/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664H73SDFQ%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T191128Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBsaCXVzLXdlc3QtMiJGMEQCIH3OQ0EHyDL6YCd7GOPH1eHmnSuCaXZ2n6AxNhh5woQvAiA0rljeIJ800gARbAxnq7s%2FDWKoYZTuhWplGqo76OD4hir%2FAwg0EAAaDDYzNzQyMzE4MzgwNSIMBfd1chkjHIp1ZcvYKtwD2QZ8ofQnlWYTRTrfrm1AJczrLWbRoyxxoahaGnjJIvVJZi9azEKsWdUx0RPIIV6bhziRtv4rJo3mi6e4e4NO95KbfOQjJouG%2Fl%2FmUcb2F2eF%2BeBOvK9xrXemMiS1vOlJPqsCkkau0VgvSvoyBg%2BEIV1GVatTCT6rx5%2FXwl7dSb%2FVW4OMvelNru510eriYwfJ1OVapJn7XM7uI8hwGGDYS09ZoWr5Nnyknhd1%2BTtNHdV%2FWZlRHLugypkYXOea0DPp7S4s4x177CIQ%2FVNHJB5dxzr%2Bm4XZ3P6C0nc%2FA9DgGwtSASvrvap8p1JZVxdHW%2Fyu9DdhtrAefDYYcKBXzgR5amY92n1lB8Ew1KeRXSmxjHYdbFGMoGAtkdUta3aY46%2BeYsabl6C17D30nMEutI4vO5YLxntkilG8qN%2FKwwgLJhu%2Bo%2B0kbYn0sc%2Fmn9SO2MS1dByTRond0Yau%2BYZZzuW7Bs%2BR9ho70e70Uq%2FO7MYU2u%2Fnzk7LahDaasFZj5zqf46QvKKQmi2fT5NAa8KzR5DzwdIs7ejiESenhV8en3K9wnk4XFgOGG0Id21WUM4WK7stFvGk5WbLDkTl3HQVkk7fRHyx5a8N9lr3BNOwM1Im8EriUpBZaNong33mCwAwkL2JvQY6pgGb60iSzWAPtkrmrrbUUDiFhdir0jKwWnHadFkRUhfEeZy45HZcZSvxPOVTIhk55AlPo8Ns%2BF4MLiDzpLkoM6u1j5rkNBashWs9Mk65qI52njZNqfvqdL30viw%2BTM1meF%2FqHAPyi0cZ3rGD1U2saVRE3YTX%2FZpS5s1dlFrHMMmbV9Ygas%2Fsyc8CZCD5Fq8JUKRew6SB9yt1ThzzLhcJ5UxDW2w3svPo&X-Amz-Signature=0cb3ebd4aa02027bc7418c455ce34dc43eda6986fce9bcb835e63b16521ed6ce&X-Amz-SignedHeaders=host&x-id=GetObject)
**Explanation:** When engine size increases, there is a corresponding increase in the price of the vehicle. This positive correlation suggests that larger engines tend to be associated with higher prices in the market.
___
### Negative Correlation
Negative correlation indicates that as one variable increases, the other variable tends to decrease.
**Example: Highway Miles per Gallon and Price**
- **Negative Correlation:** As highway miles per gallon increases, price decreases.
- **Visualization:** Scatter plot with a steep negative slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/10f1f798-9cc4-4df2-a9c1-5a339f554a0b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YBYSI6RQ%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T191128Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBsaCXVzLXdlc3QtMiJIMEYCIQDtT2zeKrw85VctaI7rjZSz5nFTa1qbR%2FJUiIvNBbj2xgIhAM4GzNvaAUm4QH8Ull8o%2F1B3%2Bzx8H0Q3ZnlzFrk6MHYPKv8DCDQQABoMNjM3NDIzMTgzODA1IgwKQx51Mr4341AD13Mq3AOM2hjkHyDJEOv4QHeHmXfGva7Zyhk5puHSrE7jatpP%2FgFWIse4gC23IDfHHMmfRGWtYfcYw6Q%2BcFUsuGGVKCV%2F5ib5OIFkjlaP360k6Dg4J2ozropSN4uTVnp%2BY%2Bz3FpQIMvLBMhzDxjeBKH13vSOSZ6dXYI9H31rMcbaAiTka%2B8LPEnXTfr85nSYyE4V0Td4SKTKwTG8lX8lNwf3k65W5Q%2FjOv7oOhKk1N65YIUilsu1KY1BgVqHot9GeKimznEt9ZdPg%2B0rhU2Es8ZMhhd5j8%2F5JEwOAEF8D4ughokGPNLtNHhR5wAE9posq1VHSQjk2rfc3YG7MiMOwBKuAC%2BqqjaO3pPLODcVEEf0cX3L5%2FzRfvnC2Z%2FuUcx5Hu6gk4t0hvs1C5iI0%2Fy2UkJjnMdZgdEa73x6FctvsBZwMvaVQZcw3mOZzPLBShM1ukSXxCIYV%2Fl%2BaDpDSf9SXVG3rJz0BTlqELx83t%2FH5GgLz2ngen6ClphhYl6%2Fy2MdS2GavW4W99SQIWWrvT88kY4YXajztBnS%2FBXUa%2F71PUepBA%2B7mX7U1FUAs6g105clnNyy%2BU%2FI5dlZ1LNfq6fGVBBlWuRZ2K7IraOOLPVRv6KDBRQKSI8HoiFuA%2BaBThDVraTD8vIm9BjqkARLDlthWWvxB6jOtyQwPEdwQXmAG%2F5WuFItLM%2B6NMPYqEaWaSQ2jrncM4IYnvzCQGkhKHirHuy3IEHksY%2FM3g9Yf62fuYh%2BGVZXHh1EEJK%2FnVC7TKi%2BlZWnSFy0bmRMcAgJULK5i04zAhlH6NVNFv9XzSQWN%2FsJPMgdBTgxXoNByUcMJdVv9YfE%2Fgsr681FQ4Z3mSNhAYa35V7XRabS5heGz%2FEyK&X-Amz-Signature=1e67d3645b3708abcb4668cb28f25fcf8f1ff81617c747628796c9ba46e8a6ac&X-Amz-SignedHeaders=host&x-id=GetObject)
**Explanation:** When highway miles per gallon increases, the price of the vehicle tends to decrease. This negative correlation suggests that cars with higher fuel efficiency (more miles per gallon) are generally priced lower in the market.
___
### Weak Correlation
Weak correlation indicates a lack of strong relationship between the variables.
**Example: RPM and Price**
- **Weak Correlation:** Low and high RPM values show varied prices, indicating no strong predictive relationship.
- **Visualization:** Scatter plot with no clear trend or slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9f914514-8914-4bf4-ac84-d9e3077f6eb1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SEVROKKS%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T191128Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBsaCXVzLXdlc3QtMiJIMEYCIQDtorFambD1kkd%2BdJAxDMnY%2Bp9T4Fva6rFNlmlGJEhbxwIhAKu%2F4NTJYb2pyz4L7%2B9Og2eMsHEmQd9KeJjTBihZGpPaKv8DCDQQABoMNjM3NDIzMTgzODA1IgyUIdjfRZ57Wrd3d7Eq3APzkB9EzBO%2FGiuwDJz5fBwV8n%2BobbWby6QfRRUxdqUZfsUCbntrBQfcVnamaxOwRpJNRTtTdniG%2FhabvDOj9a%2B31TpX2xYqy4IOTtr%2F795CXZK98Be0DGQiywBb5m87K5EjOidr7RtTVYR0jlBplRI6rRWvgeNeDaDRb%2BUwMGNztI5hzHjMwylzrM0%2FxnF4HS4RUB16L%2BOpIoPpuaeRpkFta2lIRI8%2BtqITuq6ICtC%2BS6bqihOTK%2FLaWDeo93h6XELT1EU%2Bm2RzGZqAcEbHLe0u9HmRWHQT24N2evPzvsUp%2BZtmgqrlibrjLeSNJ1yl60uhObaZBw9BMoqrf8v7lzpFQnAgtG31t9u16uO1JMUTDhB%2Fe8Q9IzyjYA6yM4s%2Bxr%2F%2BG%2FXwUcEZWVgCTdvYcdgXMMWx610hCuhP4OB3SJeCTF9hhtUzyBD5DJcAwAO%2BZWo%2BSsVRD%2B6lB9OrWQmwYBouCjqLd9oQBxAN98p3X5nKw9gfRigxnvkKSIY0iTxPoiYzxw3AU9qKWBhnGcpn9wVCBi5ocfW2uRKjWZG%2FeQf9%2FyiB7nGnQXV%2BRvjuIgyGO%2BzCn%2FJGYD9s9k2sFxpi9cMPUiujn0a7swG3GrGc%2FMNUuQSbu13ZLk5YGFi2EzDNvYm9BjqkAcY974ueVw6hZZINnbTvamFUC4pqTLWbB8XnLMjXNsz0HxUt0LZHXpkZPe5VUUhiHRT7mhsIzcexMlg92pL9zG%2FIZTMa9iGU2fFmsUYspzbSlOQpUdISX0cm6Rh%2BNyr9gDiu%2FAITxtt%2BDOilU4w05apjBBsr608ljVyuyORTcBGqQ8v%2FpHsn7wfvifTVC%2FUdZ7k0JgJA%2B4WddEoLusVPVqoEPiSa&X-Amz-Signature=7d43b5bf0eb4d1d7c244c290b05de34483e2e10886d8da1b7c477ad8a380635b&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f18086e5-5b04-4fbf-8309-8944ab20d213/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666M6Z5KI3%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T191128Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBsaCXVzLXdlc3QtMiJIMEYCIQDfKpUuLlX5Y8YQEte2fv4G1sdOpCQoX4Z5J8jrs%2B6UiAIhALVzw0yyIrVktvJ3phTLWJjk%2B4t0KVkzGKbJY52OqHA2Kv8DCDQQABoMNjM3NDIzMTgzODA1IgxsyOdF6d6PQNDYeV8q3APlgxPk7kVbn0a9mQidL0b0Js9KCZYnTCq656BmeWYRauA9oRWLZ%2FeAdJykJemNtrPjQURLOC3ktkXqWs5%2BD7SYTDmIlQSMQaM%2B0qHw6XwDOq0YSXjZJtxRy%2FBBd%2FhxelRZn58HzNGjXFLv8rTzPF9TDNSCbg1cCO50OGWOcZ0YaVh3jRiyM8Tk1TmVpbshtZAYGRNepU0CwPGw0QzufaY0UZjFVhFdmN6%2B6n1WuS9Fr2fOOUmKZ6LG%2Fi5d95VS6zI5XP5RpJcEgN0P111XIs%2FjzQ9dlol%2BnKLIrP9QZT%2BMPxp6mO51V3ahfX3IjQFLLSer%2FiyCtKUYQHEWGldkdqPjZHKUN8ZdAM1qx9rFfbcuXUP5QCZNPKS%2Flkik3ppYzqOb%2F3MUb7o%2FHFmvFdH20IIDKnX%2FqPUnPurMeNl3%2Bqbg0NVAf9l27CFFs9N45g%2FcuD2QuX4VqRkHdkzMH86lgiVcDQGwZQtqB806GWxpNFSuas1vx7cmC5nkUOqN6x1aKh4D9sphJhh4GB9KHIEWwkGLVGbcFjCbYy2BSKhDDJX%2BNujrwveNtVdaIYFtuXqnhQJAR3aAjhI0Aivhx46ZwT0Od0zO1WTg%2FZInTfQddGe0F834wZmaFwgVUkDSjTD8vIm9BjqkAVuwcNfdkFp%2BjDdO7AwqJXV5r2ianJsvr6sXhev2%2Bbpt%2BWvHeNA1S4%2BrvmipRa6jie9x%2BxxmcPebrbn%2FZq6Ybu8uReI5ft9ZuIyZKs0L3SKk2lRZ%2BLAxF68j%2BJhgtnHCjQJsH8lp69BOpMFfzyPFSfYOVPvIZIOCB649fwDPMLsJFcfh4x1x0E0UpSDlzBxoSw2oxacnr6ba2bezBEVpZALRITrK&X-Amz-Signature=a4a5c19e9f32245e8e182d21a7bc4f6298dbb985f821bc784eb1f1c0aeeee1f6&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Correlation Plot
Heatmap visualizes correlations among variables. Color scheme indicates Pearson correlation coefficients. Dark red diagonal line shows perfect correlation (value of 1) between variables and themselves.
This heatmap offers overview of variable relationships and their link with price.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cd3b341e-cc1a-45f7-8aec-cdc00436d270/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666M6Z5KI3%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T191128Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBsaCXVzLXdlc3QtMiJIMEYCIQDfKpUuLlX5Y8YQEte2fv4G1sdOpCQoX4Z5J8jrs%2B6UiAIhALVzw0yyIrVktvJ3phTLWJjk%2B4t0KVkzGKbJY52OqHA2Kv8DCDQQABoMNjM3NDIzMTgzODA1IgxsyOdF6d6PQNDYeV8q3APlgxPk7kVbn0a9mQidL0b0Js9KCZYnTCq656BmeWYRauA9oRWLZ%2FeAdJykJemNtrPjQURLOC3ktkXqWs5%2BD7SYTDmIlQSMQaM%2B0qHw6XwDOq0YSXjZJtxRy%2FBBd%2FhxelRZn58HzNGjXFLv8rTzPF9TDNSCbg1cCO50OGWOcZ0YaVh3jRiyM8Tk1TmVpbshtZAYGRNepU0CwPGw0QzufaY0UZjFVhFdmN6%2B6n1WuS9Fr2fOOUmKZ6LG%2Fi5d95VS6zI5XP5RpJcEgN0P111XIs%2FjzQ9dlol%2BnKLIrP9QZT%2BMPxp6mO51V3ahfX3IjQFLLSer%2FiyCtKUYQHEWGldkdqPjZHKUN8ZdAM1qx9rFfbcuXUP5QCZNPKS%2Flkik3ppYzqOb%2F3MUb7o%2FHFmvFdH20IIDKnX%2FqPUnPurMeNl3%2Bqbg0NVAf9l27CFFs9N45g%2FcuD2QuX4VqRkHdkzMH86lgiVcDQGwZQtqB806GWxpNFSuas1vx7cmC5nkUOqN6x1aKh4D9sphJhh4GB9KHIEWwkGLVGbcFjCbYy2BSKhDDJX%2BNujrwveNtVdaIYFtuXqnhQJAR3aAjhI0Aivhx46ZwT0Od0zO1WTg%2FZInTfQddGe0F834wZmaFwgVUkDSjTD8vIm9BjqkAVuwcNfdkFp%2BjDdO7AwqJXV5r2ianJsvr6sXhev2%2Bbpt%2BWvHeNA1S4%2BrvmipRa6jie9x%2BxxmcPebrbn%2FZq6Ybu8uReI5ft9ZuIyZKs0L3SKk2lRZ%2BLAxF68j%2BJhgtnHCjQJsH8lp69BOpMFfzyPFSfYOVPvIZIOCB649fwDPMLsJFcfh4x1x0E0UpSDlzBxoSw2oxacnr6ba2bezBEVpZALRITrK&X-Amz-Signature=5ba4675da6e222843ef09e120de7f1f0eb2d49868a373af89f8cea5cb0b93f43&X-Amz-SignedHeaders=host&x-id=GetObject)

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
