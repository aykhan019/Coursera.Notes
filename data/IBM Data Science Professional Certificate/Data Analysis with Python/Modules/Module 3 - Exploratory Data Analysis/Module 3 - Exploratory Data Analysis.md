

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7e6d594d-952e-44b6-97ea-31225882aea6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665ZKHTI2C%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T031718Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDRqSgnc44yDU1HNNuwtRD0fyHqFT9JBLJPedxsnaXM0wIgKD9kccrvkeqHXIgmLhbGOSVjDk0aeA3dGBzXESBEphAqiAQI5P%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKtP5%2B6rA7JuB0YNqyrcA8RpH3cdWGqveurk7J9xvD5Qp4kK7ibZyfZuq2N3oRYARrUvYme7nKdtGddTDySY%2BrGewjEQ8lyjsN4opY1alyntxpCCuxG%2BfEgVeTNdkcInJJCBkCJ%2BH4txYgY0capjQz6FKTuYPEmnKBNPEKJavShJu775Pb%2F8e3tkVpiY5%2BYKjWg1hgu3cJM2RzEdZb1wYIxgsoVisOYSZvWRP7XhFMLnuTRJINs2mKtE69klHp5J14d87qaGkga07gwOTK4intSoZTiShzbHucI8XbaK8f45IHnYGs8%2BNtBdB%2FecVGfwG7tNNKhiyCW6SsTXyXeroA2bMWdl%2FecndFE9BTKqfKcwBKvUn1VSnLpq1tWqRdTKuNubfxTrKLQUv1mnZNhAAQ64%2ByLhDXBf8GASushbrc3K%2FE%2BVb4n2ifYwvE7%2FQ9GosT%2FY5lmXNApyJm4sYIXyulk%2Fsk0WZJmWl76gZ6cR1vLbrbEgtk3KJD%2BSFqXvy3skOKJQW4DhsSY4PUhpbmP1aAPNLBSmiaz2TPEvVVm2%2FXAV4Up4cOXN0uzxSm1wDLwelmn8i%2F7%2BFUI%2BjJ%2BLuecFMsbgyV%2FYUm3d2R9idS6QGfs4vSs4wBQH3gbgneWC00Ri1eA6yyjTUH6PI8XmMOe6%2B7wGOqUBRp9Ch1nIGpCqmf4458MWdvNVoLGMC2XsTMYxPMCF3JrdJTCY2e%2Bq4leutTkmb5jIVFK8vE17gCQpjflJ5NJN3jJZ7k7TJKJ2N9WhA2T3s8sQDSlr93qlmS%2Bazn%2F9yPhGs0eQSM3rtj6wuKZLnttkF5xcF3geG%2Fa9I1%2FM2jGyskyZD5mKVDoUf4VHsz4MKd4ueTaFBIqxUyQjkGU3PBjJ9CLIpnEn&X-Amz-Signature=7a3a83ad045429393fb2817c4b0800ddf1e01e635ed6840bb47f4a657d778a39&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cbfaed9e-b398-4902-8936-dea058b21def/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665ZKHTI2C%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T031718Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDRqSgnc44yDU1HNNuwtRD0fyHqFT9JBLJPedxsnaXM0wIgKD9kccrvkeqHXIgmLhbGOSVjDk0aeA3dGBzXESBEphAqiAQI5P%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKtP5%2B6rA7JuB0YNqyrcA8RpH3cdWGqveurk7J9xvD5Qp4kK7ibZyfZuq2N3oRYARrUvYme7nKdtGddTDySY%2BrGewjEQ8lyjsN4opY1alyntxpCCuxG%2BfEgVeTNdkcInJJCBkCJ%2BH4txYgY0capjQz6FKTuYPEmnKBNPEKJavShJu775Pb%2F8e3tkVpiY5%2BYKjWg1hgu3cJM2RzEdZb1wYIxgsoVisOYSZvWRP7XhFMLnuTRJINs2mKtE69klHp5J14d87qaGkga07gwOTK4intSoZTiShzbHucI8XbaK8f45IHnYGs8%2BNtBdB%2FecVGfwG7tNNKhiyCW6SsTXyXeroA2bMWdl%2FecndFE9BTKqfKcwBKvUn1VSnLpq1tWqRdTKuNubfxTrKLQUv1mnZNhAAQ64%2ByLhDXBf8GASushbrc3K%2FE%2BVb4n2ifYwvE7%2FQ9GosT%2FY5lmXNApyJm4sYIXyulk%2Fsk0WZJmWl76gZ6cR1vLbrbEgtk3KJD%2BSFqXvy3skOKJQW4DhsSY4PUhpbmP1aAPNLBSmiaz2TPEvVVm2%2FXAV4Up4cOXN0uzxSm1wDLwelmn8i%2F7%2BFUI%2BjJ%2BLuecFMsbgyV%2FYUm3d2R9idS6QGfs4vSs4wBQH3gbgneWC00Ri1eA6yyjTUH6PI8XmMOe6%2B7wGOqUBRp9Ch1nIGpCqmf4458MWdvNVoLGMC2XsTMYxPMCF3JrdJTCY2e%2Bq4leutTkmb5jIVFK8vE17gCQpjflJ5NJN3jJZ7k7TJKJ2N9WhA2T3s8sQDSlr93qlmS%2Bazn%2F9yPhGs0eQSM3rtj6wuKZLnttkF5xcF3geG%2Fa9I1%2FM2jGyskyZD5mKVDoUf4VHsz4MKd4ueTaFBIqxUyQjkGU3PBjJ9CLIpnEn&X-Amz-Signature=f039328e506f81ee003935fddfaa02082a6ccf7faf475f1a7bea712b35a983bb&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/91181646-b1e0-4433-9711-6259a96a9247/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665ZKHTI2C%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T031718Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDRqSgnc44yDU1HNNuwtRD0fyHqFT9JBLJPedxsnaXM0wIgKD9kccrvkeqHXIgmLhbGOSVjDk0aeA3dGBzXESBEphAqiAQI5P%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKtP5%2B6rA7JuB0YNqyrcA8RpH3cdWGqveurk7J9xvD5Qp4kK7ibZyfZuq2N3oRYARrUvYme7nKdtGddTDySY%2BrGewjEQ8lyjsN4opY1alyntxpCCuxG%2BfEgVeTNdkcInJJCBkCJ%2BH4txYgY0capjQz6FKTuYPEmnKBNPEKJavShJu775Pb%2F8e3tkVpiY5%2BYKjWg1hgu3cJM2RzEdZb1wYIxgsoVisOYSZvWRP7XhFMLnuTRJINs2mKtE69klHp5J14d87qaGkga07gwOTK4intSoZTiShzbHucI8XbaK8f45IHnYGs8%2BNtBdB%2FecVGfwG7tNNKhiyCW6SsTXyXeroA2bMWdl%2FecndFE9BTKqfKcwBKvUn1VSnLpq1tWqRdTKuNubfxTrKLQUv1mnZNhAAQ64%2ByLhDXBf8GASushbrc3K%2FE%2BVb4n2ifYwvE7%2FQ9GosT%2FY5lmXNApyJm4sYIXyulk%2Fsk0WZJmWl76gZ6cR1vLbrbEgtk3KJD%2BSFqXvy3skOKJQW4DhsSY4PUhpbmP1aAPNLBSmiaz2TPEvVVm2%2FXAV4Up4cOXN0uzxSm1wDLwelmn8i%2F7%2BFUI%2BjJ%2BLuecFMsbgyV%2FYUm3d2R9idS6QGfs4vSs4wBQH3gbgneWC00Ri1eA6yyjTUH6PI8XmMOe6%2B7wGOqUBRp9Ch1nIGpCqmf4458MWdvNVoLGMC2XsTMYxPMCF3JrdJTCY2e%2Bq4leutTkmb5jIVFK8vE17gCQpjflJ5NJN3jJZ7k7TJKJ2N9WhA2T3s8sQDSlr93qlmS%2Bazn%2F9yPhGs0eQSM3rtj6wuKZLnttkF5xcF3geG%2Fa9I1%2FM2jGyskyZD5mKVDoUf4VHsz4MKd4ueTaFBIqxUyQjkGU3PBjJ9CLIpnEn&X-Amz-Signature=c05a25dd9ab6eb0f4e3df95b2b672fbb9897c651393533e731d9e6fa56c883cd&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/09aba1c0-0d55-41dd-852a-a04c5b8a3fac/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XEHNYA5Z%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T031719Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCIq0uLq3JkKycv2oojm3s76fg5fgzmcFO%2BexzS9%2FzttAIhALaGshBptnWD1rEg2D2C3RLE6rj%2BsPXDdoEcogGcQYqcKogECOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxpUJY6YLcpL0ZkHc0q3AOtrPGd57tST85OYXG%2Bvf1tmhMg7kEQf3SqI%2F9YqNplR0ytdUo%2FzXWtw34FByV7V5ktlU4y0L4r%2FNytekdU3Xkpk9pcxnE8OuXqBS3ykjpclGK5KWcnIQ%2FWxmp0uW%2BeZODrgrYevj6eK1eHX8ejv5RkHfLv5sxzK5NsWsK3vPMhEDmTTm%2Fnz73C1c3tJNGigbV6JCihN7fauXT9Q1bBzgCbibrhfVGR%2FZO0aTF5IN8V0Rh8Q8iWPz46lC1g0vkRpKXAAtsphDYiwnvsCQdmPFOsMXAelxmv6lIsG0v7Ao6b5feUIXrL6a1wspF7YY8lefPma%2BONV2PpxHzOX95QsTHwPaMHZeys%2FFiFiWdfNkABymQQt9QNvzDk%2BnSB0o33IMuIcFci44lymvENAc2zIVdLiKePa6SNhIGX9qzqyJisGS%2FpkIlOhHJcZSdEtimAhY7DLV6XBgIlLL8amgLiJLw1tuoWDgdxfWtyzCpfQUCx6YIOGff0AeV41fkZHM26bbCCQ0rWwAVEBAo4YDW%2FgVuvWCesUtP%2B%2BilyC%2FIOlQ3bqAXMTII%2BWPu48mvwn2jK%2BioWL5J5oKBzRd8MNHINBWKxziCEQUQxN3yrpWM89Aa4sedpRTizS8K9ShoQJTDLuvu8BjqkAbhbmcURk3JwHQbnaXRSP%2F1dStdkBF03nkW%2BmIpqN9hESsAONtyPanJtWKEzuFjQ2vjhdxyvuttqD6%2FWt9CCEJHPeSq6z3K%2BQPNAb56hVU%2FQkGbFj4IpwtHhxHtO4L87HQHPqsYecqSo3SHnvGvbLladZSaEqJ8vyholgG43DHcJW9ekD9ML1XXJFTWr8DzmjSSyttYzLh4ELUTp1ORABSeVHEgq&X-Amz-Signature=7552723c7dd62de5273d2b672b828637fcac6572578dd0e1777e1995e7ceaef6&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 2. Scatter Plot
Scatter plots present the relationship between two variables in a dataset. It represents data points on a two-dimensional plane. The independent variable or attribute is plotted on the X-axis, while the dependent variable is plotted on the Y-axis.
**Syntax:**
```python
plt.scatter(x, y)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23708af9-659f-4f23-b626-1a4292d7842c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XEHNYA5Z%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T031719Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCIq0uLq3JkKycv2oojm3s76fg5fgzmcFO%2BexzS9%2FzttAIhALaGshBptnWD1rEg2D2C3RLE6rj%2BsPXDdoEcogGcQYqcKogECOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxpUJY6YLcpL0ZkHc0q3AOtrPGd57tST85OYXG%2Bvf1tmhMg7kEQf3SqI%2F9YqNplR0ytdUo%2FzXWtw34FByV7V5ktlU4y0L4r%2FNytekdU3Xkpk9pcxnE8OuXqBS3ykjpclGK5KWcnIQ%2FWxmp0uW%2BeZODrgrYevj6eK1eHX8ejv5RkHfLv5sxzK5NsWsK3vPMhEDmTTm%2Fnz73C1c3tJNGigbV6JCihN7fauXT9Q1bBzgCbibrhfVGR%2FZO0aTF5IN8V0Rh8Q8iWPz46lC1g0vkRpKXAAtsphDYiwnvsCQdmPFOsMXAelxmv6lIsG0v7Ao6b5feUIXrL6a1wspF7YY8lefPma%2BONV2PpxHzOX95QsTHwPaMHZeys%2FFiFiWdfNkABymQQt9QNvzDk%2BnSB0o33IMuIcFci44lymvENAc2zIVdLiKePa6SNhIGX9qzqyJisGS%2FpkIlOhHJcZSdEtimAhY7DLV6XBgIlLL8amgLiJLw1tuoWDgdxfWtyzCpfQUCx6YIOGff0AeV41fkZHM26bbCCQ0rWwAVEBAo4YDW%2FgVuvWCesUtP%2B%2BilyC%2FIOlQ3bqAXMTII%2BWPu48mvwn2jK%2BioWL5J5oKBzRd8MNHINBWKxziCEQUQxN3yrpWM89Aa4sedpRTizS8K9ShoQJTDLuvu8BjqkAbhbmcURk3JwHQbnaXRSP%2F1dStdkBF03nkW%2BmIpqN9hESsAONtyPanJtWKEzuFjQ2vjhdxyvuttqD6%2FWt9CCEJHPeSq6z3K%2BQPNAb56hVU%2FQkGbFj4IpwtHhxHtO4L87HQHPqsYecqSo3SHnvGvbLladZSaEqJ8vyholgG43DHcJW9ekD9ML1XXJFTWr8DzmjSSyttYzLh4ELUTp1ORABSeVHEgq&X-Amz-Signature=f54657a0c832a19284f572489a8811bbd7fcdcf9e7b07e90b88fe2624c468a1c&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 3. Histogram
A histogram is an important visual representation of data in categorical form. To view the data in a "Binned" form, use the histogram plot with a number of bins required or with the data points that mark the bin edges. The x-axis represents the data bins, and the y-axis represents the number of elements in each bin.
**Syntax:**
```python
plt.hist(x, bins)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/24e4424a-df87-40a1-b63b-195cbdc2e0ab/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XEHNYA5Z%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T031719Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCIq0uLq3JkKycv2oojm3s76fg5fgzmcFO%2BexzS9%2FzttAIhALaGshBptnWD1rEg2D2C3RLE6rj%2BsPXDdoEcogGcQYqcKogECOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxpUJY6YLcpL0ZkHc0q3AOtrPGd57tST85OYXG%2Bvf1tmhMg7kEQf3SqI%2F9YqNplR0ytdUo%2FzXWtw34FByV7V5ktlU4y0L4r%2FNytekdU3Xkpk9pcxnE8OuXqBS3ykjpclGK5KWcnIQ%2FWxmp0uW%2BeZODrgrYevj6eK1eHX8ejv5RkHfLv5sxzK5NsWsK3vPMhEDmTTm%2Fnz73C1c3tJNGigbV6JCihN7fauXT9Q1bBzgCbibrhfVGR%2FZO0aTF5IN8V0Rh8Q8iWPz46lC1g0vkRpKXAAtsphDYiwnvsCQdmPFOsMXAelxmv6lIsG0v7Ao6b5feUIXrL6a1wspF7YY8lefPma%2BONV2PpxHzOX95QsTHwPaMHZeys%2FFiFiWdfNkABymQQt9QNvzDk%2BnSB0o33IMuIcFci44lymvENAc2zIVdLiKePa6SNhIGX9qzqyJisGS%2FpkIlOhHJcZSdEtimAhY7DLV6XBgIlLL8amgLiJLw1tuoWDgdxfWtyzCpfQUCx6YIOGff0AeV41fkZHM26bbCCQ0rWwAVEBAo4YDW%2FgVuvWCesUtP%2B%2BilyC%2FIOlQ3bqAXMTII%2BWPu48mvwn2jK%2BioWL5J5oKBzRd8MNHINBWKxziCEQUQxN3yrpWM89Aa4sedpRTizS8K9ShoQJTDLuvu8BjqkAbhbmcURk3JwHQbnaXRSP%2F1dStdkBF03nkW%2BmIpqN9hESsAONtyPanJtWKEzuFjQ2vjhdxyvuttqD6%2FWt9CCEJHPeSq6z3K%2BQPNAb56hVU%2FQkGbFj4IpwtHhxHtO4L87HQHPqsYecqSo3SHnvGvbLladZSaEqJ8vyholgG43DHcJW9ekD9ML1XXJFTWr8DzmjSSyttYzLh4ELUTp1ORABSeVHEgq&X-Amz-Signature=1bd8efc29262ece841af7628b5a15c9386bfeabcfb45e9c1bd7719e4e1dc6658&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ab5a6dfe-51f5-43ee-bcb3-33dae4a1c7ad/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XEHNYA5Z%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T031719Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCIq0uLq3JkKycv2oojm3s76fg5fgzmcFO%2BexzS9%2FzttAIhALaGshBptnWD1rEg2D2C3RLE6rj%2BsPXDdoEcogGcQYqcKogECOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxpUJY6YLcpL0ZkHc0q3AOtrPGd57tST85OYXG%2Bvf1tmhMg7kEQf3SqI%2F9YqNplR0ytdUo%2FzXWtw34FByV7V5ktlU4y0L4r%2FNytekdU3Xkpk9pcxnE8OuXqBS3ykjpclGK5KWcnIQ%2FWxmp0uW%2BeZODrgrYevj6eK1eHX8ejv5RkHfLv5sxzK5NsWsK3vPMhEDmTTm%2Fnz73C1c3tJNGigbV6JCihN7fauXT9Q1bBzgCbibrhfVGR%2FZO0aTF5IN8V0Rh8Q8iWPz46lC1g0vkRpKXAAtsphDYiwnvsCQdmPFOsMXAelxmv6lIsG0v7Ao6b5feUIXrL6a1wspF7YY8lefPma%2BONV2PpxHzOX95QsTHwPaMHZeys%2FFiFiWdfNkABymQQt9QNvzDk%2BnSB0o33IMuIcFci44lymvENAc2zIVdLiKePa6SNhIGX9qzqyJisGS%2FpkIlOhHJcZSdEtimAhY7DLV6XBgIlLL8amgLiJLw1tuoWDgdxfWtyzCpfQUCx6YIOGff0AeV41fkZHM26bbCCQ0rWwAVEBAo4YDW%2FgVuvWCesUtP%2B%2BilyC%2FIOlQ3bqAXMTII%2BWPu48mvwn2jK%2BioWL5J5oKBzRd8MNHINBWKxziCEQUQxN3yrpWM89Aa4sedpRTizS8K9ShoQJTDLuvu8BjqkAbhbmcURk3JwHQbnaXRSP%2F1dStdkBF03nkW%2BmIpqN9hESsAONtyPanJtWKEzuFjQ2vjhdxyvuttqD6%2FWt9CCEJHPeSq6z3K%2BQPNAb56hVU%2FQkGbFj4IpwtHhxHtO4L87HQHPqsYecqSo3SHnvGvbLladZSaEqJ8vyholgG43DHcJW9ekD9ML1XXJFTWr8DzmjSSyttYzLh4ELUTp1ORABSeVHEgq&X-Amz-Signature=2b0492fb20f51cbf57aedbb29b0c3168b6d00592a7afafcf8d561cd47e38dbcb&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8f1b1d60-cf1b-42b3-9faa-f634c89c3f84/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XEHNYA5Z%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T031719Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCIq0uLq3JkKycv2oojm3s76fg5fgzmcFO%2BexzS9%2FzttAIhALaGshBptnWD1rEg2D2C3RLE6rj%2BsPXDdoEcogGcQYqcKogECOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxpUJY6YLcpL0ZkHc0q3AOtrPGd57tST85OYXG%2Bvf1tmhMg7kEQf3SqI%2F9YqNplR0ytdUo%2FzXWtw34FByV7V5ktlU4y0L4r%2FNytekdU3Xkpk9pcxnE8OuXqBS3ykjpclGK5KWcnIQ%2FWxmp0uW%2BeZODrgrYevj6eK1eHX8ejv5RkHfLv5sxzK5NsWsK3vPMhEDmTTm%2Fnz73C1c3tJNGigbV6JCihN7fauXT9Q1bBzgCbibrhfVGR%2FZO0aTF5IN8V0Rh8Q8iWPz46lC1g0vkRpKXAAtsphDYiwnvsCQdmPFOsMXAelxmv6lIsG0v7Ao6b5feUIXrL6a1wspF7YY8lefPma%2BONV2PpxHzOX95QsTHwPaMHZeys%2FFiFiWdfNkABymQQt9QNvzDk%2BnSB0o33IMuIcFci44lymvENAc2zIVdLiKePa6SNhIGX9qzqyJisGS%2FpkIlOhHJcZSdEtimAhY7DLV6XBgIlLL8amgLiJLw1tuoWDgdxfWtyzCpfQUCx6YIOGff0AeV41fkZHM26bbCCQ0rWwAVEBAo4YDW%2FgVuvWCesUtP%2B%2BilyC%2FIOlQ3bqAXMTII%2BWPu48mvwn2jK%2BioWL5J5oKBzRd8MNHINBWKxziCEQUQxN3yrpWM89Aa4sedpRTizS8K9ShoQJTDLuvu8BjqkAbhbmcURk3JwHQbnaXRSP%2F1dStdkBF03nkW%2BmIpqN9hESsAONtyPanJtWKEzuFjQ2vjhdxyvuttqD6%2FWt9CCEJHPeSq6z3K%2BQPNAb56hVU%2FQkGbFj4IpwtHhxHtO4L87HQHPqsYecqSo3SHnvGvbLladZSaEqJ8vyholgG43DHcJW9ekD9ML1XXJFTWr8DzmjSSyttYzLh4ELUTp1ORABSeVHEgq&X-Amz-Signature=54c6ce37d40f2e244e03b013b12c3b4491c3bc2d06605980a027b497d1b35c49&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/13ad0497-05fe-4eaa-984e-707b33e14761/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XEHNYA5Z%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T031719Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCIq0uLq3JkKycv2oojm3s76fg5fgzmcFO%2BexzS9%2FzttAIhALaGshBptnWD1rEg2D2C3RLE6rj%2BsPXDdoEcogGcQYqcKogECOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxpUJY6YLcpL0ZkHc0q3AOtrPGd57tST85OYXG%2Bvf1tmhMg7kEQf3SqI%2F9YqNplR0ytdUo%2FzXWtw34FByV7V5ktlU4y0L4r%2FNytekdU3Xkpk9pcxnE8OuXqBS3ykjpclGK5KWcnIQ%2FWxmp0uW%2BeZODrgrYevj6eK1eHX8ejv5RkHfLv5sxzK5NsWsK3vPMhEDmTTm%2Fnz73C1c3tJNGigbV6JCihN7fauXT9Q1bBzgCbibrhfVGR%2FZO0aTF5IN8V0Rh8Q8iWPz46lC1g0vkRpKXAAtsphDYiwnvsCQdmPFOsMXAelxmv6lIsG0v7Ao6b5feUIXrL6a1wspF7YY8lefPma%2BONV2PpxHzOX95QsTHwPaMHZeys%2FFiFiWdfNkABymQQt9QNvzDk%2BnSB0o33IMuIcFci44lymvENAc2zIVdLiKePa6SNhIGX9qzqyJisGS%2FpkIlOhHJcZSdEtimAhY7DLV6XBgIlLL8amgLiJLw1tuoWDgdxfWtyzCpfQUCx6YIOGff0AeV41fkZHM26bbCCQ0rWwAVEBAo4YDW%2FgVuvWCesUtP%2B%2BilyC%2FIOlQ3bqAXMTII%2BWPu48mvwn2jK%2BioWL5J5oKBzRd8MNHINBWKxziCEQUQxN3yrpWM89Aa4sedpRTizS8K9ShoQJTDLuvu8BjqkAbhbmcURk3JwHQbnaXRSP%2F1dStdkBF03nkW%2BmIpqN9hESsAONtyPanJtWKEzuFjQ2vjhdxyvuttqD6%2FWt9CCEJHPeSq6z3K%2BQPNAb56hVU%2FQkGbFj4IpwtHhxHtO4L87HQHPqsYecqSo3SHnvGvbLladZSaEqJ8vyholgG43DHcJW9ekD9ML1XXJFTWr8DzmjSSyttYzLh4ELUTp1ORABSeVHEgq&X-Amz-Signature=c578740f6d090695b4ec32bbc9cfb574ba90c87a031b8d8001f1c1f4a8d15bd4&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 2. Box and Whisker Plot
A box plot shows the distribution of quantitative data in a way that facilitates comparisons between variables or across levels of a categorical variable. The box shows the quartiles of the dataset while the whiskers extend to show the rest of the distribution, except for points that are determined to be "outliers".
**Syntax:**
```python
sns.boxplot(x='header_1', y='header_2', data=df)
```
**Example Output:**


![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d207ae92-0a7c-4e2f-aa65-0ee5a2c33bf7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WNBOVXE2%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T031720Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIADy0YFz7QOmiN4pns%2BKWo1Fgzd6MpEv0fBrs1VMhwy%2FAiA3HP6z2iHDp%2B6xjSX3GuwgF1rwZACgEtVKO8PcuWmTziqIBAjk%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMezZMstt%2F4dcQ%2FGfsKtwD6kKJSAhFPqq%2BwWP2yExY9RUAelr7ioUDbmI56GVkp6OaZsjFPOMB1d9OmsQVMh41cRsheVTnxzg8JzW0GL7eoPDpbY5cAyrQ6oDZh4lXvxFPYPtRx3WsiM08l9tdIfa7OP3yL6WGSerLJxec2iQ5Q8LP817IfSBOu%2F0lQN4QMLq62voOavb0w64Z%2FTD9nP0j6ReHGP5R1lHMuILW92tpFWJTLg%2F6Y3yvshugKnBP0FvtR0026ugOZcDugHOCds7576NrpvkInyTyl4w7Qf4NWEsYBhEyvn%2BUE3hzNKVLcShSdmZ8zkDYPBH3Y8Ws2earsc5RZtXFzL1b1wa7x8TLbAEo72TdRlmDRNasnD4eC1uyfrAkhXcp3QX1U88aYs6hi80TwLTkUFp6eHK4Oy3R%2BHE3VE7yjplC7amaRWccC3jLm3IbcUZiJKlh48u4TqwXMtnnyMqDf3JVKvUJtsHbv9iwa%2B8NCYSobnaze2%2Fcb7FXSTrFCOg2cv5BV%2FK9e6buBCgm99QMfZePNmyFuyWvoTvAm5PiF5UUytyyNYRXDf6QaRK%2BFXDao7xcX5Zw6WtB%2FfskPXoynpYLcZInUjaFLKW47Tu6Z%2B7qqYDWuwvGzeuzJPe8iRH236iLpEQw%2F7r7vAY6pgEOx0xABY04NuUfkcrPxTSO8d2rFxvcwHaH%2B71S21QuOHL1EnbRUAoHFpvC7%2BsaR4AACg8tnvBvTYjtqzxgFka2llPbvADxlWMI%2FjCAkhvz%2BZMLj3MAUodB2gc65%2BDcOof%2BN5kVLNcAGfOZnAgzBJIgxSIgKGe8rLPULL8FfyLFM9Fajfk%2B2e1DpUbE%2FHPryjpaAVDUOfbThUPHkbeuCtW1g0tnBm0r&X-Amz-Signature=c97746211bb1453cd8a1d8979e52ff9375f656d409a76c5fd87c9c695fecebec&X-Amz-SignedHeaders=host&x-id=GetObject)

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0e516edc-7551-4792-ab18-0494db3c4c0c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZIPNK4AK%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T031720Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIDdGN6Bgqw9TiPHDUcG7dhctxmcA%2FEjLGAxgp7IQDgc1AiAVX3yfMs2rUjkbgGjlfqqU3e1XuwqGlYG7%2BQxcyAU7NCqIBAjk%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM97FeVOFGawXD17GEKtwDkncU9sNFZMMpNpQXZmaxRcEWfim%2F2oU64rJ9iXJsa47Vj78nncP7V29hd8vSjhuICkg34X1R5s%2FyTV%2B5qmbFCF7ojCqdrlKR1%2F6%2FV7%2B6%2F78RhdpM55o0Es9FmlD4YY9xOq%2FqrU9xO1XdwNWyp3%2BUKw%2F3WocGJfIybiBM8PMEtUYnQluF6VzpxQAEkTGfaLLES9khsk4jVhq%2BGkcitA2C4kadXk0ljmbqzUlAE2U3cDUd5ceAWVWxzga4X3sTiZVR0YmPrxe0Fqeqoy3P%2Btcr6xdb9%2FdYBkSsXplcoxzHmHhbpUGMlQcAWTgFUA6KvvdRIIcKzwXFsk7Ep2F3gCg5KGu03AAZdxV6WeHPC7SKRRVX2Cm7V3CRHwqbDDzblbwxPV3emo14y%2BPH%2B0j%2FDf8%2BCQ8stQqev2P11lJGt90N4%2BkBNKN6NrP5fFsbVm4M%2BCoByhWsAFOmpBcrkX%2FVMk146%2FyQBktgDORm8ZyS8yxTJN4%2B1QlgqObzx%2FkPinLb04gRZ8dcTQNNQr5t2ewDKytANBXIazPNJI4hcM5l5WtU0oREL5byT2aXq0WpsfURCAkJ8GFcS8p9MMX9huRcpgLHmfzvtQzZnsfDAO20FTc54xY%2BxEuEC9aGOkbnqbYw1rr7vAY6pgGKDoYIR3JJi6RZ4jbd%2FvgcL7Yt1UXyUJ%2BayHNKk7SkBB7FPpQPA%2F28wUhBdaEo7NxfyPQvIDIgTYso%2FVaNEk%2BoOHp4wErw3ricYqyaaeyeyWT90v%2BrpRf5BUGiKu0jxjA9vlQDwSq68z8iU99EISpN4yqxq%2Fa4%2FrT4hTEzkP4BTjOWm2dsZmPd34BfuLY5aCggT9jVyBSD2HolRn6e1krzpmrvu4QF&X-Amz-Signature=f56de45e5096709858fd03751a08ef52d464747f24f4d100f3a68f7fdf9d07bf&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23a79b9d-2356-49a9-8fd9-65c6b0ab2cc5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XEHNYA5Z%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T031719Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCIq0uLq3JkKycv2oojm3s76fg5fgzmcFO%2BexzS9%2FzttAIhALaGshBptnWD1rEg2D2C3RLE6rj%2BsPXDdoEcogGcQYqcKogECOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxpUJY6YLcpL0ZkHc0q3AOtrPGd57tST85OYXG%2Bvf1tmhMg7kEQf3SqI%2F9YqNplR0ytdUo%2FzXWtw34FByV7V5ktlU4y0L4r%2FNytekdU3Xkpk9pcxnE8OuXqBS3ykjpclGK5KWcnIQ%2FWxmp0uW%2BeZODrgrYevj6eK1eHX8ejv5RkHfLv5sxzK5NsWsK3vPMhEDmTTm%2Fnz73C1c3tJNGigbV6JCihN7fauXT9Q1bBzgCbibrhfVGR%2FZO0aTF5IN8V0Rh8Q8iWPz46lC1g0vkRpKXAAtsphDYiwnvsCQdmPFOsMXAelxmv6lIsG0v7Ao6b5feUIXrL6a1wspF7YY8lefPma%2BONV2PpxHzOX95QsTHwPaMHZeys%2FFiFiWdfNkABymQQt9QNvzDk%2BnSB0o33IMuIcFci44lymvENAc2zIVdLiKePa6SNhIGX9qzqyJisGS%2FpkIlOhHJcZSdEtimAhY7DLV6XBgIlLL8amgLiJLw1tuoWDgdxfWtyzCpfQUCx6YIOGff0AeV41fkZHM26bbCCQ0rWwAVEBAo4YDW%2FgVuvWCesUtP%2B%2BilyC%2FIOlQ3bqAXMTII%2BWPu48mvwn2jK%2BioWL5J5oKBzRd8MNHINBWKxziCEQUQxN3yrpWM89Aa4sedpRTizS8K9ShoQJTDLuvu8BjqkAbhbmcURk3JwHQbnaXRSP%2F1dStdkBF03nkW%2BmIpqN9hESsAONtyPanJtWKEzuFjQ2vjhdxyvuttqD6%2FWt9CCEJHPeSq6z3K%2BQPNAb56hVU%2FQkGbFj4IpwtHhxHtO4L87HQHPqsYecqSo3SHnvGvbLladZSaEqJ8vyholgG43DHcJW9ekD9ML1XXJFTWr8DzmjSSyttYzLh4ELUTp1ORABSeVHEgq&X-Amz-Signature=2c88a39d708c6a34935e1c8ef1edd1daa060f8bb1ad508eded1b0d25b0862519&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 4. KDE Plot
A Kernel Density Estimate (KDE) plot is a graph that creates a probability distribution curve for the data based upon its likelihood of occurrence on a specific value. This is created for a single vector of information.
**Syntax:**
```python
sns.kdeplot(X) || sns.kdeplot(df['age'])
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0d571213-2a2f-4921-a50b-880847aa05ee/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XEHNYA5Z%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T031719Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCIq0uLq3JkKycv2oojm3s76fg5fgzmcFO%2BexzS9%2FzttAIhALaGshBptnWD1rEg2D2C3RLE6rj%2BsPXDdoEcogGcQYqcKogECOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxpUJY6YLcpL0ZkHc0q3AOtrPGd57tST85OYXG%2Bvf1tmhMg7kEQf3SqI%2F9YqNplR0ytdUo%2FzXWtw34FByV7V5ktlU4y0L4r%2FNytekdU3Xkpk9pcxnE8OuXqBS3ykjpclGK5KWcnIQ%2FWxmp0uW%2BeZODrgrYevj6eK1eHX8ejv5RkHfLv5sxzK5NsWsK3vPMhEDmTTm%2Fnz73C1c3tJNGigbV6JCihN7fauXT9Q1bBzgCbibrhfVGR%2FZO0aTF5IN8V0Rh8Q8iWPz46lC1g0vkRpKXAAtsphDYiwnvsCQdmPFOsMXAelxmv6lIsG0v7Ao6b5feUIXrL6a1wspF7YY8lefPma%2BONV2PpxHzOX95QsTHwPaMHZeys%2FFiFiWdfNkABymQQt9QNvzDk%2BnSB0o33IMuIcFci44lymvENAc2zIVdLiKePa6SNhIGX9qzqyJisGS%2FpkIlOhHJcZSdEtimAhY7DLV6XBgIlLL8amgLiJLw1tuoWDgdxfWtyzCpfQUCx6YIOGff0AeV41fkZHM26bbCCQ0rWwAVEBAo4YDW%2FgVuvWCesUtP%2B%2BilyC%2FIOlQ3bqAXMTII%2BWPu48mvwn2jK%2BioWL5J5oKBzRd8MNHINBWKxziCEQUQxN3yrpWM89Aa4sedpRTizS8K9ShoQJTDLuvu8BjqkAbhbmcURk3JwHQbnaXRSP%2F1dStdkBF03nkW%2BmIpqN9hESsAONtyPanJtWKEzuFjQ2vjhdxyvuttqD6%2FWt9CCEJHPeSq6z3K%2BQPNAb56hVU%2FQkGbFj4IpwtHhxHtO4L87HQHPqsYecqSo3SHnvGvbLladZSaEqJ8vyholgG43DHcJW9ekD9ML1XXJFTWr8DzmjSSyttYzLh4ELUTp1ORABSeVHEgq&X-Amz-Signature=a70b1f72fef31846d2cc7b8ba6b1f5b3d77aea1debf475620e10b9083178c767&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/53752550-ef82-4ca9-a01a-09921f0282d0/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XEHNYA5Z%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T031719Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCIq0uLq3JkKycv2oojm3s76fg5fgzmcFO%2BexzS9%2FzttAIhALaGshBptnWD1rEg2D2C3RLE6rj%2BsPXDdoEcogGcQYqcKogECOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxpUJY6YLcpL0ZkHc0q3AOtrPGd57tST85OYXG%2Bvf1tmhMg7kEQf3SqI%2F9YqNplR0ytdUo%2FzXWtw34FByV7V5ktlU4y0L4r%2FNytekdU3Xkpk9pcxnE8OuXqBS3ykjpclGK5KWcnIQ%2FWxmp0uW%2BeZODrgrYevj6eK1eHX8ejv5RkHfLv5sxzK5NsWsK3vPMhEDmTTm%2Fnz73C1c3tJNGigbV6JCihN7fauXT9Q1bBzgCbibrhfVGR%2FZO0aTF5IN8V0Rh8Q8iWPz46lC1g0vkRpKXAAtsphDYiwnvsCQdmPFOsMXAelxmv6lIsG0v7Ao6b5feUIXrL6a1wspF7YY8lefPma%2BONV2PpxHzOX95QsTHwPaMHZeys%2FFiFiWdfNkABymQQt9QNvzDk%2BnSB0o33IMuIcFci44lymvENAc2zIVdLiKePa6SNhIGX9qzqyJisGS%2FpkIlOhHJcZSdEtimAhY7DLV6XBgIlLL8amgLiJLw1tuoWDgdxfWtyzCpfQUCx6YIOGff0AeV41fkZHM26bbCCQ0rWwAVEBAo4YDW%2FgVuvWCesUtP%2B%2BilyC%2FIOlQ3bqAXMTII%2BWPu48mvwn2jK%2BioWL5J5oKBzRd8MNHINBWKxziCEQUQxN3yrpWM89Aa4sedpRTizS8K9ShoQJTDLuvu8BjqkAbhbmcURk3JwHQbnaXRSP%2F1dStdkBF03nkW%2BmIpqN9hESsAONtyPanJtWKEzuFjQ2vjhdxyvuttqD6%2FWt9CCEJHPeSq6z3K%2BQPNAb56hVU%2FQkGbFj4IpwtHhxHtO4L87HQHPqsYecqSo3SHnvGvbLladZSaEqJ8vyholgG43DHcJW9ekD9ML1XXJFTWr8DzmjSSyttYzLh4ELUTp1ORABSeVHEgq&X-Amz-Signature=09482cfd8098d7accdf7ae59cdaa0abe1384aafcb1c32a05724accb4ab7a7126&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
## 4. Correlation Between Variables
Correlation is a statistical measure of the extent to which different variables are interdependent. It indicates how changes in one variable are associated with changes in another variable over time.
### Positive Correlation
Positive correlation indicates that as one variable increases, the other variable also tends to increase.
**Example: Engine Size and Price**
- **Positive Correlation:** Engine size increases, price also increases.
- **Visualization:** Scatter plot with a steep positive slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c7ea9b0-3ef3-4357-a9c3-554fc71b6b15/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664UGMGS7P%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T031720Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHYknmLkG3IyJ4yD6YUTXo0gBvasDqjfuDqC4e%2FeZUqHAiAAsAAWm16KWxSNRrA1TYUk9KUcYO7%2BYnJA06pRXsyHNCqIBAjk%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMtYeYsd6t3s4L0aE0KtwD8vPVPzLLi%2BNYDIXk2ee2DaHsC6o1a9h8GXK%2FrTGVbXVj1cZPFfLIy9p9W5LUOFEYq8HsLrBLT%2FNFnxWwudEad0jTI5PiAStC%2B23d%2FXlu5M0zqvWrkUhwFnrtWwLDpHx4%2FwzbPD54n%2FDr0Am3853q4ISvTrKf8j00kTZlrKLurLzBcVAnnCEde2fFiLc5bEZugm%2FyyhcjepfIPQ5GDsWaBhQimueuq3cTgv1bnRvv9%2BDkHPkjoLmQIAU1Lehwisp9Cv9lzuYFr4%2FI4PIlei1cr13MC8bdHpNPtt%2FZ7irg7S5l%2Bb1tjdc4oyjQuogW8axUiPVMRqsM5ajCmAqQ%2BfpkZ%2FV2MbmwKLlMreBx2dOemmchlJri8bw99HIzX8AFaVVqelLnbwbs9HPHo43kMm%2FshaO%2BZCvag0yjipkj3F9hLVNzyFkhh8wCs3ho9XDnYcU%2BoClK4QR1dmw6VJ6feKHQX8mNYbhwgvckxC2fawGJyG8eTa0uQC1Bb4UWTi2CMe1r4SZLZyetzVQqJP6E%2BS9GtN629II%2BwvU5rD1NsrLfdvCFr7Q2WCwo2rOnPT7mtaBSmq7qWb9JuQurav4ISvuWcbc2%2FYGrTV%2BnECwdFk%2FjuTnqGeiZtDniaGGJfngw7Lr7vAY6pgFmtBKPyHR0p6pSOIwc6Xy9B%2BfIVTBdaJim5DzylYgwekxe%2FPG62YbSUQj3Fq6FQgfCjal6ItRK%2FlrzOU4jCAbr5grjzHZ9QwpDHf4pfnhCnNZvn%2Bwu%2BxOEjbRYFXriwMLBw0%2FgJ%2F1J0SN0CEVQKeUuITb5RmTkMfrG4wYPt%2Fi4%2BLFAwwWZRKatVUjnM1rSu5FkHnd9wYqQhXzTHk%2FWAld7iYM0%2F%2BU3&X-Amz-Signature=a58f0fc4a1e63c1e768837cf2d76bb74d9c0ece98a123601b4ab1b12b1dd7319&X-Amz-SignedHeaders=host&x-id=GetObject)
**Explanation:** When engine size increases, there is a corresponding increase in the price of the vehicle. This positive correlation suggests that larger engines tend to be associated with higher prices in the market.
___
### Negative Correlation
Negative correlation indicates that as one variable increases, the other variable tends to decrease.
**Example: Highway Miles per Gallon and Price**
- **Negative Correlation:** As highway miles per gallon increases, price decreases.
- **Visualization:** Scatter plot with a steep negative slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/10f1f798-9cc4-4df2-a9c1-5a339f554a0b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UOHWCHIC%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T031720Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFPZkSyxA7Zc6GrJdS8P34ZZOO5l%2B9SlkPg02kOvIE2nAiBmN8LBKOi3cwrIYBbcttkPEe1Bb9yg%2Fce1FngNuok%2F0CqIBAjk%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMZik61TbvfoPoBbUCKtwDeaooAbXAbESwdQYwomB7NX9T0%2BUnDWyQbyB%2FLZLphCPLm%2FOahGY%2B%2F194Nz8pKd9tKA1aTn4cX2qkkQIOEQwWuIFtwI%2BNQf4WI4gy2r8BWdUZc0Tk7HfrY5Qa5pjEO7KWBqx677tfFPS082tCCvKc1siNCpZBbFjSkOTBHuI6yxXTbsadS9JYXVjw9f6hmJY8FjPcKrI9TQpIqAOkGjnSh%2BVY9P1X3rGjUesmAi5Fufc4UV0sBCcnHPzJjAnIqqa1KpdZqx31kGtTohzoFxwkz4r5w53se9ArcIxLq%2BzvW12ArwOmCsMJNkR7ak67iHav2bh%2BtwQQElHsr5VupKQgetiVMuPgLfKetw6o5yj1hXRP1AM2vmsvnAv%2BbXHFp4wLMY%2BW3RIQbxCx%2FFq5RzGNcH5OSOC1O72sfUt%2Fk8%2BY420frQPc0rGIvgrc09XC9%2BTYDVZ%2BLON3YZPyL1fITnHWeMq7kfVhzjK8W5oK3Uiag4lCLQguTvSjQE1o7HzW72S%2BE0x4kdi4xnbL4E19npkauw3Qqxgtlwpt6yFJPU5TjQGf%2FHBPx9SicG4AwdpW25vkPOKlvLW%2FKs45btMKYNr5jwBgxDsvStyX%2FXVBVufD1bEwKSxphkSUVSZFyF8w7Lr7vAY6pgHKBP8o2UEkhyIpu9Toh%2FhELQVNLQ8nNd7Jgj0Fokn3ttF6zF1Q8D3HM%2FGDa46a9NCBCb2R%2F8R9eDmxnimF%2FriscWivIO2CEHB6iE8ZvlJWjOvQcDXBcZv5PzkOSKDxFNEH%2B%2BUwbqW6RHekycerWJDW%2Bsm18q55wc2YAeIGLVPJb2cNBsUXclhRy2Er3I%2BCaJk9jbUJmbdpCiqahAb8pTqOhEKFax6n&X-Amz-Signature=bf74f8886027e89f722cfed86b974f0861be35c502e8bc457b8b55479225811b&X-Amz-SignedHeaders=host&x-id=GetObject)
**Explanation:** When highway miles per gallon increases, the price of the vehicle tends to decrease. This negative correlation suggests that cars with higher fuel efficiency (more miles per gallon) are generally priced lower in the market.
___
### Weak Correlation
Weak correlation indicates a lack of strong relationship between the variables.
**Example: RPM and Price**
- **Weak Correlation:** Low and high RPM values show varied prices, indicating no strong predictive relationship.
- **Visualization:** Scatter plot with no clear trend or slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9f914514-8914-4bf4-ac84-d9e3077f6eb1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663DX6YSUI%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T031720Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBUltq%2BoLclCGt4WcPGZJ3WvMAJoGFM4DtnEojuAgUoGAiA4jrl96mJL3BRfdzgbVh6gHW0%2FR85l1OYa8kGA5AEpxiqIBAjk%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM7MEMR%2FIpJqNMAQrDKtwDH4lIDx24V19laNdTG1Z%2Bz8blOp5dcUoYAsn5WIqG5z5xW66zMUcwmQSoAnjvql9t38nhHHIhAwy8860el%2B8O4moV%2F3Q%2F1z7ca1Ilj9sEPu5orIJ8%2Fltdey9FKsK7gV0RoAOuO6MDz5Qa%2FE5LJdbrxmoCqNgDbHXVpjmj1sklbcwwcl1cTw2jALC5%2F%2BFOkgRmDv7FllNxUKQnPff3f8GfzLa9euyP6wo8mXxxQD8WCZaKj47F9kpLbiEkyan4MsXfiX8lqFjvB%2F7mxHjJ2FlHmGsneAC0qSlaRERIDQApDkZEU2rxlOischYdv4XPRiQiTYda9HIjnOS6s%2BsO4F4%2F2qXCPORwyhtEHpGavaqN5Am%2BtA3FULs73mkOeNbC9h5Af%2FLaZOR%2FrpanWfPFWvCHu8Icp6Czw4tkPj2CWynZNcdPj4NCqOB50%2BTqeJOo9jcZ2b52uXahDjHPQLoRxU6E3VeNGLOz%2F%2FiGVPaXI6FERiWxIr2jXZjAfdCWwKCVdcc%2Bg%2FHdoRei6S5P4tkzyeFxFkdKcOIJ%2BR7G45PQ9edhXLp1o7yJZGQuxXML0UGyOBj5BU1w4dxL9LCYYzuRTRRCzgn9szgYRWBmSTecyDJgEGZeAbL2WRVXVzYRqzEwhrv7vAY6pgG9Fu9EH8AnOLgkHhC57vrUi4CsAgDMUXtgqVErjKeaMjvf%2BvAeU52wsfq7DmotYfMHsdUCeduQE%2FWTZ%2BKHZgoKUzFv0H4hJuwDEOxrOLy2w%2BRu8SaOrG1Xf8E60YoK8scDUVFX15kHfQUKMMYkhtb0PtNgbQqMxdIsRzwhSJAG18CdUfxiD%2FSQAhvLYkhQgkpuPg3uN6ioEplNJKYQ0YYobRv8XUYp&X-Amz-Signature=20b62f94bba000b9492abae09794297a7f2118ef1f8f2282889b2e286c619319&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f18086e5-5b04-4fbf-8309-8944ab20d213/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666B2CW3DG%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T031720Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHucZO%2FhhGJ6SL6dDMyNj2HSnOlubEhfMIQeTi0ejlRjAiEAu9ey7mrNCX9EOsNIyEzYvU3NQMnRkvF6nxlY37m0IcYqiAQI5P%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOXR%2BZCvgbptZiaQdCrcA1JujuVnzgdXG8NCNlSYMwlfPp15FINXgj8DT4IJCJJoLuyN6k%2Fj40B3HXjnhOPDjOff%2B4OSwhU75N1fbS8yUrm4CafgCyCT2r7SYulTBvSA392d%2BWlvpabgXnTTpQkriDbYf5ebZcGSGpYmcq8UhqNLzKQb2k9Y%2BzOD238uJgsUvu1GUujvekFqu8CsnjL%2F5aD1RQp3O51ZEeEbaHHtiA5%2FjAUftbK1V7hQ1v8cnfhhsqI1Xc8PHyXB0Tgcaxmcms0WxQTTA8hgPxTJWtn7j3n9XAjnY6nytulD5fFitBDfCnC0MIuv0XncfAqAutrH2bEdsb6%2BX20WAGo1M10w7G5R4rl7hyNbH4vaj31iZtat0I4p7wMjZFYQRH3Mct69aaAbmTPX5%2ByVqSoLJJmrnKYZZZEa4oRey4tIiJ%2FaVdLBCgCbvxYnyrtTybNRD7J2cWz4FS7tLr41RAWuxE3oYS6x%2BQJ85gmo3XJ9RMBnDOC%2FnD61tJe9ndvNF1FjW159VcCMr1wOoFZfj%2F%2Fz43V188cDOCE6ODw5IpzeENtdOIKK%2FTRR5a8zf5V4SqPQSIbzWm134aNSAd43FU3%2FgFJlhYBE9wywJ6mZpDNeu7wzeZAMd0Hq4sHxNkkoMPWwMKa7%2B7wGOqUBtaEpQVEK%2BkZglg0bk7SQwQbGyeky8MfD3%2BW2eKkAHPlUIzM2TlUukqiHJX8kJmtE1MWJfOKQ4G0wlGOaMT%2FMr63tBK0DH7Av0zxliWNQU4RlXEtHXwQ2ZAknQwoXD4oxQrm0766qGZfT7rOsw3mW1VHTHh7XI%2FQgFrhOvV1r%2F7bfi1%2BmUTPFO3ZijWFUPPM98vRtjNCI6QGDJIdipg%2BdUe%2FEXcsF&X-Amz-Signature=83210f743afbd6fb2a723baddd3dca3799574fcec8d372691465df59fe5b60bc&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Correlation Plot
Heatmap visualizes correlations among variables. Color scheme indicates Pearson correlation coefficients. Dark red diagonal line shows perfect correlation (value of 1) between variables and themselves.
This heatmap offers overview of variable relationships and their link with price.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cd3b341e-cc1a-45f7-8aec-cdc00436d270/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666B2CW3DG%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T031720Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHucZO%2FhhGJ6SL6dDMyNj2HSnOlubEhfMIQeTi0ejlRjAiEAu9ey7mrNCX9EOsNIyEzYvU3NQMnRkvF6nxlY37m0IcYqiAQI5P%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOXR%2BZCvgbptZiaQdCrcA1JujuVnzgdXG8NCNlSYMwlfPp15FINXgj8DT4IJCJJoLuyN6k%2Fj40B3HXjnhOPDjOff%2B4OSwhU75N1fbS8yUrm4CafgCyCT2r7SYulTBvSA392d%2BWlvpabgXnTTpQkriDbYf5ebZcGSGpYmcq8UhqNLzKQb2k9Y%2BzOD238uJgsUvu1GUujvekFqu8CsnjL%2F5aD1RQp3O51ZEeEbaHHtiA5%2FjAUftbK1V7hQ1v8cnfhhsqI1Xc8PHyXB0Tgcaxmcms0WxQTTA8hgPxTJWtn7j3n9XAjnY6nytulD5fFitBDfCnC0MIuv0XncfAqAutrH2bEdsb6%2BX20WAGo1M10w7G5R4rl7hyNbH4vaj31iZtat0I4p7wMjZFYQRH3Mct69aaAbmTPX5%2ByVqSoLJJmrnKYZZZEa4oRey4tIiJ%2FaVdLBCgCbvxYnyrtTybNRD7J2cWz4FS7tLr41RAWuxE3oYS6x%2BQJ85gmo3XJ9RMBnDOC%2FnD61tJe9ndvNF1FjW159VcCMr1wOoFZfj%2F%2Fz43V188cDOCE6ODw5IpzeENtdOIKK%2FTRR5a8zf5V4SqPQSIbzWm134aNSAd43FU3%2FgFJlhYBE9wywJ6mZpDNeu7wzeZAMd0Hq4sHxNkkoMPWwMKa7%2B7wGOqUBtaEpQVEK%2BkZglg0bk7SQwQbGyeky8MfD3%2BW2eKkAHPlUIzM2TlUukqiHJX8kJmtE1MWJfOKQ4G0wlGOaMT%2FMr63tBK0DH7Av0zxliWNQU4RlXEtHXwQ2ZAknQwoXD4oxQrm0766qGZfT7rOsw3mW1VHTHh7XI%2FQgFrhOvV1r%2F7bfi1%2BmUTPFO3ZijWFUPPM98vRtjNCI6QGDJIdipg%2BdUe%2FEXcsF&X-Amz-Signature=73b778bb59248a8bf804172098af09fe7a039307ab3a1f7f495a37f4ef768030&X-Amz-SignedHeaders=host&x-id=GetObject)

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
