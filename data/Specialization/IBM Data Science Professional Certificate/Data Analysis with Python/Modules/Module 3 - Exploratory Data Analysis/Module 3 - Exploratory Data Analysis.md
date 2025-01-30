

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7e6d594d-952e-44b6-97ea-31225882aea6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664MZFUPG6%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T031640Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHXmBa%2FOe%2BbNv9cuyWDtDx36o4mH%2BMq4ZuhKUAfcfZKeAiEA8Iukf3%2BtadUhUfLj2r6xkNLbHo4MPBDewgnJ%2FemJPncqiAQInP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLhLkndm8GorWWvGQCrcAyn9dSoD%2FVTRmJL0Slxx5S9y7ERbfKEtF%2FkN4RprpUYPT%2BwJUXVM3VHzUnO5q6EJiOzgZ%2BPQIPqxTjLSHsWKfULMRxx9xd4mrv6jYCSkkkI3m7jCVbXfM6rjL9ANeqRlseCYO2bH6dl8u9uXflQvB552VShy8YNNzMnq142gZbKwTDAfMy6TuSg%2FAuI9Uuxpk3I058ltWghTOQahFhz6LNB9PgGbFPflYN6%2BPLeV6nO%2FhSl9o0OhQ9RPSzle3voUtpdF83A53oLzmRvAm1UnO%2FN6Mm1TKD3rXIvC0mYI%2BdX8lJTI9LXksZ06S4D5vR6uC1Eyvtd7zCFe%2Fr9gW86SL0u%2B6DE%2B9AuFPGFSF4VK8DJLZmmR8XlyIzZBclQ%2FYASTpBjwKnUqJljyrx%2FdSbhWhm%2FTCoPM%2Fl5I3yWGvCHFnhGj1RNXbzkvplf616y2xFVS2UxhJAeOvaTnvFrZe1GfQQZppoIzarco32wE5CWShPp6YuS0c2pYHSnoEJBiYgvPDSzCJikisss8wmGSwE8K0zegsDWfnbLPeK5zTjVX27VZ8NM0dQROzoS0whD3sXT3i8Vj%2F2g9aZt3S4yA%2FgnxhaRYngAkSN2vZ8JN581VWuIQoxO3apbeNOuYgt7sMM3P67wGOqUBHIyjhDGlo%2BukMIsxJpFNI0ZtMEZOMnK1FcS01dYiibBg7p5GxGU2TWsGzxlwET%2FMI25ftf0A8G6CyktodwQHECtCNMrdADvXl7FahtAUcIx5%2BFAShMEJhKzWYZ%2FYtEIJDn%2FoX2Px3coFYFel6%2FnnguO6l9UPgTCorELrn2g3ZVYr56SrfANv1Z50a9v74MxDn9LWprpDTbIsK2FpWEDugGDau%2FI9&X-Amz-Signature=62e05fcd08d7e4ddc44458c42c03032bc6157b1f9ff4ffe4f7e2970e59d00073&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cbfaed9e-b398-4902-8936-dea058b21def/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664MZFUPG6%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T031640Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHXmBa%2FOe%2BbNv9cuyWDtDx36o4mH%2BMq4ZuhKUAfcfZKeAiEA8Iukf3%2BtadUhUfLj2r6xkNLbHo4MPBDewgnJ%2FemJPncqiAQInP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLhLkndm8GorWWvGQCrcAyn9dSoD%2FVTRmJL0Slxx5S9y7ERbfKEtF%2FkN4RprpUYPT%2BwJUXVM3VHzUnO5q6EJiOzgZ%2BPQIPqxTjLSHsWKfULMRxx9xd4mrv6jYCSkkkI3m7jCVbXfM6rjL9ANeqRlseCYO2bH6dl8u9uXflQvB552VShy8YNNzMnq142gZbKwTDAfMy6TuSg%2FAuI9Uuxpk3I058ltWghTOQahFhz6LNB9PgGbFPflYN6%2BPLeV6nO%2FhSl9o0OhQ9RPSzle3voUtpdF83A53oLzmRvAm1UnO%2FN6Mm1TKD3rXIvC0mYI%2BdX8lJTI9LXksZ06S4D5vR6uC1Eyvtd7zCFe%2Fr9gW86SL0u%2B6DE%2B9AuFPGFSF4VK8DJLZmmR8XlyIzZBclQ%2FYASTpBjwKnUqJljyrx%2FdSbhWhm%2FTCoPM%2Fl5I3yWGvCHFnhGj1RNXbzkvplf616y2xFVS2UxhJAeOvaTnvFrZe1GfQQZppoIzarco32wE5CWShPp6YuS0c2pYHSnoEJBiYgvPDSzCJikisss8wmGSwE8K0zegsDWfnbLPeK5zTjVX27VZ8NM0dQROzoS0whD3sXT3i8Vj%2F2g9aZt3S4yA%2FgnxhaRYngAkSN2vZ8JN581VWuIQoxO3apbeNOuYgt7sMM3P67wGOqUBHIyjhDGlo%2BukMIsxJpFNI0ZtMEZOMnK1FcS01dYiibBg7p5GxGU2TWsGzxlwET%2FMI25ftf0A8G6CyktodwQHECtCNMrdADvXl7FahtAUcIx5%2BFAShMEJhKzWYZ%2FYtEIJDn%2FoX2Px3coFYFel6%2FnnguO6l9UPgTCorELrn2g3ZVYr56SrfANv1Z50a9v74MxDn9LWprpDTbIsK2FpWEDugGDau%2FI9&X-Amz-Signature=86807761edea498ae248f1e7e3e9a843f193c825766d6babf7ea74d341d673dc&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/91181646-b1e0-4433-9711-6259a96a9247/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664MZFUPG6%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T031640Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHXmBa%2FOe%2BbNv9cuyWDtDx36o4mH%2BMq4ZuhKUAfcfZKeAiEA8Iukf3%2BtadUhUfLj2r6xkNLbHo4MPBDewgnJ%2FemJPncqiAQInP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLhLkndm8GorWWvGQCrcAyn9dSoD%2FVTRmJL0Slxx5S9y7ERbfKEtF%2FkN4RprpUYPT%2BwJUXVM3VHzUnO5q6EJiOzgZ%2BPQIPqxTjLSHsWKfULMRxx9xd4mrv6jYCSkkkI3m7jCVbXfM6rjL9ANeqRlseCYO2bH6dl8u9uXflQvB552VShy8YNNzMnq142gZbKwTDAfMy6TuSg%2FAuI9Uuxpk3I058ltWghTOQahFhz6LNB9PgGbFPflYN6%2BPLeV6nO%2FhSl9o0OhQ9RPSzle3voUtpdF83A53oLzmRvAm1UnO%2FN6Mm1TKD3rXIvC0mYI%2BdX8lJTI9LXksZ06S4D5vR6uC1Eyvtd7zCFe%2Fr9gW86SL0u%2B6DE%2B9AuFPGFSF4VK8DJLZmmR8XlyIzZBclQ%2FYASTpBjwKnUqJljyrx%2FdSbhWhm%2FTCoPM%2Fl5I3yWGvCHFnhGj1RNXbzkvplf616y2xFVS2UxhJAeOvaTnvFrZe1GfQQZppoIzarco32wE5CWShPp6YuS0c2pYHSnoEJBiYgvPDSzCJikisss8wmGSwE8K0zegsDWfnbLPeK5zTjVX27VZ8NM0dQROzoS0whD3sXT3i8Vj%2F2g9aZt3S4yA%2FgnxhaRYngAkSN2vZ8JN581VWuIQoxO3apbeNOuYgt7sMM3P67wGOqUBHIyjhDGlo%2BukMIsxJpFNI0ZtMEZOMnK1FcS01dYiibBg7p5GxGU2TWsGzxlwET%2FMI25ftf0A8G6CyktodwQHECtCNMrdADvXl7FahtAUcIx5%2BFAShMEJhKzWYZ%2FYtEIJDn%2FoX2Px3coFYFel6%2FnnguO6l9UPgTCorELrn2g3ZVYr56SrfANv1Z50a9v74MxDn9LWprpDTbIsK2FpWEDugGDau%2FI9&X-Amz-Signature=172c37ff1e5e63718b5d4230c75d0b01225f174e56c3e0627d65650b21dd9688&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/09aba1c0-0d55-41dd-852a-a04c5b8a3fac/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SN4CLX2Z%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T031641Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHrjtgPz3jqYFUvf79OKAal2lJ%2FZVo9qFbR53wmp6imWAiAfvozytT2Uf5CRhdsQ4ZrClZqqUyP1FZm4i5ITxNQ9DyqIBAic%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMPrBbWq4jxPz7U49cKtwD6v66We%2BDg8rNoM6pYSj9Ks58cbOFK4oSpDq6PgQC6IkYnQytvZ0JRtvryMmNIMgOSyIv7%2BYa%2FUG9NHcPC8Yq3yvG91N7BjuEuaMsqvUf71J4AVVdLEewLnD%2B3plgLuUeYUSyo1h5smqkYYVLyr9fg3tYe%2FaUSx65h9bxbp%2FNJcB727X7UPn5tVUFJP0c4TsqcoHIW4VbQpjicBNVudLSimCvSyH%2FiEleVPZ8AHU8HehhnPWn9Lk0V4jMrPORPRd2mwqUpKCxtqkudhVAO%2FDYAsB1FErWhb3sEhK98aGHCr3n6RiFfsHxJuCdhpkjRevSahS1MrajqBOrHNj4A2s%2FbB8sizSzI29BJzWPKOI8ZPOdZgnJT0r%2F7sCRSL68ATUWnfm0mmTWSAqSp7xaWxjsGUAZeAM3T1sjclbVbXlcIHY6Ldn1flHW%2BTlAh6naGzHP8F6g%2BemnjT6lumJLLMrl2UBvMl4m%2F6kyxtzZtjcoGkcuexFkqg5yUfyx7NYQ5pRsQZ2xJp6CtYAOJ%2FrCCTWGmUzGgUE9CqehUs4nlAFnTtmHumvX1AcwSvwX4KxSVf7rzRzfsH6gr%2B4ya3kHoajwr4hdfRw%2BFWTdaG5UIvbqli%2BGY5jT%2BRkkLZA%2B81owm87rvAY6pgHuGDGFBysXgiP%2BzgXswq5h7nKbaOJMCYoY4lJSqJCLYgmb1MzVYHivrQ1%2Fp9lnIBqOdgunRh51OsrH2K4dREfr9os5J0tCAbBAno09Ef4ZyrT%2FhbbVUA3UBi2flUGL9oEurXiojrIf0tP%2BnARJGjb6eRrYREXSfNT9E5gkO7y0G0s1rerTyy8MgzjkVT5YQjDtWx568QGQt8Wd4zOI%2F47g7bCg6RZ6&X-Amz-Signature=eea1dece2dee7b126255a5bc43a80ac001183f32874cbacff11cacfe75ed14f9&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 2. Scatter Plot
Scatter plots present the relationship between two variables in a dataset. It represents data points on a two-dimensional plane. The independent variable or attribute is plotted on the X-axis, while the dependent variable is plotted on the Y-axis.
**Syntax:**
```python
plt.scatter(x, y)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23708af9-659f-4f23-b626-1a4292d7842c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SN4CLX2Z%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T031641Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHrjtgPz3jqYFUvf79OKAal2lJ%2FZVo9qFbR53wmp6imWAiAfvozytT2Uf5CRhdsQ4ZrClZqqUyP1FZm4i5ITxNQ9DyqIBAic%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMPrBbWq4jxPz7U49cKtwD6v66We%2BDg8rNoM6pYSj9Ks58cbOFK4oSpDq6PgQC6IkYnQytvZ0JRtvryMmNIMgOSyIv7%2BYa%2FUG9NHcPC8Yq3yvG91N7BjuEuaMsqvUf71J4AVVdLEewLnD%2B3plgLuUeYUSyo1h5smqkYYVLyr9fg3tYe%2FaUSx65h9bxbp%2FNJcB727X7UPn5tVUFJP0c4TsqcoHIW4VbQpjicBNVudLSimCvSyH%2FiEleVPZ8AHU8HehhnPWn9Lk0V4jMrPORPRd2mwqUpKCxtqkudhVAO%2FDYAsB1FErWhb3sEhK98aGHCr3n6RiFfsHxJuCdhpkjRevSahS1MrajqBOrHNj4A2s%2FbB8sizSzI29BJzWPKOI8ZPOdZgnJT0r%2F7sCRSL68ATUWnfm0mmTWSAqSp7xaWxjsGUAZeAM3T1sjclbVbXlcIHY6Ldn1flHW%2BTlAh6naGzHP8F6g%2BemnjT6lumJLLMrl2UBvMl4m%2F6kyxtzZtjcoGkcuexFkqg5yUfyx7NYQ5pRsQZ2xJp6CtYAOJ%2FrCCTWGmUzGgUE9CqehUs4nlAFnTtmHumvX1AcwSvwX4KxSVf7rzRzfsH6gr%2B4ya3kHoajwr4hdfRw%2BFWTdaG5UIvbqli%2BGY5jT%2BRkkLZA%2B81owm87rvAY6pgHuGDGFBysXgiP%2BzgXswq5h7nKbaOJMCYoY4lJSqJCLYgmb1MzVYHivrQ1%2Fp9lnIBqOdgunRh51OsrH2K4dREfr9os5J0tCAbBAno09Ef4ZyrT%2FhbbVUA3UBi2flUGL9oEurXiojrIf0tP%2BnARJGjb6eRrYREXSfNT9E5gkO7y0G0s1rerTyy8MgzjkVT5YQjDtWx568QGQt8Wd4zOI%2F47g7bCg6RZ6&X-Amz-Signature=2f3ca9b947613c0eeabcfd1e37e598a872ae20fcc144c7d0ce38b8021a474dd0&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 3. Histogram
A histogram is an important visual representation of data in categorical form. To view the data in a "Binned" form, use the histogram plot with a number of bins required or with the data points that mark the bin edges. The x-axis represents the data bins, and the y-axis represents the number of elements in each bin.
**Syntax:**
```python
plt.hist(x, bins)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/24e4424a-df87-40a1-b63b-195cbdc2e0ab/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SN4CLX2Z%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T031641Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHrjtgPz3jqYFUvf79OKAal2lJ%2FZVo9qFbR53wmp6imWAiAfvozytT2Uf5CRhdsQ4ZrClZqqUyP1FZm4i5ITxNQ9DyqIBAic%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMPrBbWq4jxPz7U49cKtwD6v66We%2BDg8rNoM6pYSj9Ks58cbOFK4oSpDq6PgQC6IkYnQytvZ0JRtvryMmNIMgOSyIv7%2BYa%2FUG9NHcPC8Yq3yvG91N7BjuEuaMsqvUf71J4AVVdLEewLnD%2B3plgLuUeYUSyo1h5smqkYYVLyr9fg3tYe%2FaUSx65h9bxbp%2FNJcB727X7UPn5tVUFJP0c4TsqcoHIW4VbQpjicBNVudLSimCvSyH%2FiEleVPZ8AHU8HehhnPWn9Lk0V4jMrPORPRd2mwqUpKCxtqkudhVAO%2FDYAsB1FErWhb3sEhK98aGHCr3n6RiFfsHxJuCdhpkjRevSahS1MrajqBOrHNj4A2s%2FbB8sizSzI29BJzWPKOI8ZPOdZgnJT0r%2F7sCRSL68ATUWnfm0mmTWSAqSp7xaWxjsGUAZeAM3T1sjclbVbXlcIHY6Ldn1flHW%2BTlAh6naGzHP8F6g%2BemnjT6lumJLLMrl2UBvMl4m%2F6kyxtzZtjcoGkcuexFkqg5yUfyx7NYQ5pRsQZ2xJp6CtYAOJ%2FrCCTWGmUzGgUE9CqehUs4nlAFnTtmHumvX1AcwSvwX4KxSVf7rzRzfsH6gr%2B4ya3kHoajwr4hdfRw%2BFWTdaG5UIvbqli%2BGY5jT%2BRkkLZA%2B81owm87rvAY6pgHuGDGFBysXgiP%2BzgXswq5h7nKbaOJMCYoY4lJSqJCLYgmb1MzVYHivrQ1%2Fp9lnIBqOdgunRh51OsrH2K4dREfr9os5J0tCAbBAno09Ef4ZyrT%2FhbbVUA3UBi2flUGL9oEurXiojrIf0tP%2BnARJGjb6eRrYREXSfNT9E5gkO7y0G0s1rerTyy8MgzjkVT5YQjDtWx568QGQt8Wd4zOI%2F47g7bCg6RZ6&X-Amz-Signature=f45d7572a6fdf51e29f38e491550be395ffc2ecfc0d4330e32434fe24672b175&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ab5a6dfe-51f5-43ee-bcb3-33dae4a1c7ad/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SN4CLX2Z%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T031641Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHrjtgPz3jqYFUvf79OKAal2lJ%2FZVo9qFbR53wmp6imWAiAfvozytT2Uf5CRhdsQ4ZrClZqqUyP1FZm4i5ITxNQ9DyqIBAic%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMPrBbWq4jxPz7U49cKtwD6v66We%2BDg8rNoM6pYSj9Ks58cbOFK4oSpDq6PgQC6IkYnQytvZ0JRtvryMmNIMgOSyIv7%2BYa%2FUG9NHcPC8Yq3yvG91N7BjuEuaMsqvUf71J4AVVdLEewLnD%2B3plgLuUeYUSyo1h5smqkYYVLyr9fg3tYe%2FaUSx65h9bxbp%2FNJcB727X7UPn5tVUFJP0c4TsqcoHIW4VbQpjicBNVudLSimCvSyH%2FiEleVPZ8AHU8HehhnPWn9Lk0V4jMrPORPRd2mwqUpKCxtqkudhVAO%2FDYAsB1FErWhb3sEhK98aGHCr3n6RiFfsHxJuCdhpkjRevSahS1MrajqBOrHNj4A2s%2FbB8sizSzI29BJzWPKOI8ZPOdZgnJT0r%2F7sCRSL68ATUWnfm0mmTWSAqSp7xaWxjsGUAZeAM3T1sjclbVbXlcIHY6Ldn1flHW%2BTlAh6naGzHP8F6g%2BemnjT6lumJLLMrl2UBvMl4m%2F6kyxtzZtjcoGkcuexFkqg5yUfyx7NYQ5pRsQZ2xJp6CtYAOJ%2FrCCTWGmUzGgUE9CqehUs4nlAFnTtmHumvX1AcwSvwX4KxSVf7rzRzfsH6gr%2B4ya3kHoajwr4hdfRw%2BFWTdaG5UIvbqli%2BGY5jT%2BRkkLZA%2B81owm87rvAY6pgHuGDGFBysXgiP%2BzgXswq5h7nKbaOJMCYoY4lJSqJCLYgmb1MzVYHivrQ1%2Fp9lnIBqOdgunRh51OsrH2K4dREfr9os5J0tCAbBAno09Ef4ZyrT%2FhbbVUA3UBi2flUGL9oEurXiojrIf0tP%2BnARJGjb6eRrYREXSfNT9E5gkO7y0G0s1rerTyy8MgzjkVT5YQjDtWx568QGQt8Wd4zOI%2F47g7bCg6RZ6&X-Amz-Signature=4f5c8cf35ac66d16757c2bba4149a58363ded9c2030433965a7632f9711e1f6b&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8f1b1d60-cf1b-42b3-9faa-f634c89c3f84/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SN4CLX2Z%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T031641Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHrjtgPz3jqYFUvf79OKAal2lJ%2FZVo9qFbR53wmp6imWAiAfvozytT2Uf5CRhdsQ4ZrClZqqUyP1FZm4i5ITxNQ9DyqIBAic%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMPrBbWq4jxPz7U49cKtwD6v66We%2BDg8rNoM6pYSj9Ks58cbOFK4oSpDq6PgQC6IkYnQytvZ0JRtvryMmNIMgOSyIv7%2BYa%2FUG9NHcPC8Yq3yvG91N7BjuEuaMsqvUf71J4AVVdLEewLnD%2B3plgLuUeYUSyo1h5smqkYYVLyr9fg3tYe%2FaUSx65h9bxbp%2FNJcB727X7UPn5tVUFJP0c4TsqcoHIW4VbQpjicBNVudLSimCvSyH%2FiEleVPZ8AHU8HehhnPWn9Lk0V4jMrPORPRd2mwqUpKCxtqkudhVAO%2FDYAsB1FErWhb3sEhK98aGHCr3n6RiFfsHxJuCdhpkjRevSahS1MrajqBOrHNj4A2s%2FbB8sizSzI29BJzWPKOI8ZPOdZgnJT0r%2F7sCRSL68ATUWnfm0mmTWSAqSp7xaWxjsGUAZeAM3T1sjclbVbXlcIHY6Ldn1flHW%2BTlAh6naGzHP8F6g%2BemnjT6lumJLLMrl2UBvMl4m%2F6kyxtzZtjcoGkcuexFkqg5yUfyx7NYQ5pRsQZ2xJp6CtYAOJ%2FrCCTWGmUzGgUE9CqehUs4nlAFnTtmHumvX1AcwSvwX4KxSVf7rzRzfsH6gr%2B4ya3kHoajwr4hdfRw%2BFWTdaG5UIvbqli%2BGY5jT%2BRkkLZA%2B81owm87rvAY6pgHuGDGFBysXgiP%2BzgXswq5h7nKbaOJMCYoY4lJSqJCLYgmb1MzVYHivrQ1%2Fp9lnIBqOdgunRh51OsrH2K4dREfr9os5J0tCAbBAno09Ef4ZyrT%2FhbbVUA3UBi2flUGL9oEurXiojrIf0tP%2BnARJGjb6eRrYREXSfNT9E5gkO7y0G0s1rerTyy8MgzjkVT5YQjDtWx568QGQt8Wd4zOI%2F47g7bCg6RZ6&X-Amz-Signature=1b026482fcee088c5f2c2f94b12e1b3cdea3707dfd0cfe4ab74b67fe2c1777f3&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/13ad0497-05fe-4eaa-984e-707b33e14761/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SN4CLX2Z%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T031641Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHrjtgPz3jqYFUvf79OKAal2lJ%2FZVo9qFbR53wmp6imWAiAfvozytT2Uf5CRhdsQ4ZrClZqqUyP1FZm4i5ITxNQ9DyqIBAic%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMPrBbWq4jxPz7U49cKtwD6v66We%2BDg8rNoM6pYSj9Ks58cbOFK4oSpDq6PgQC6IkYnQytvZ0JRtvryMmNIMgOSyIv7%2BYa%2FUG9NHcPC8Yq3yvG91N7BjuEuaMsqvUf71J4AVVdLEewLnD%2B3plgLuUeYUSyo1h5smqkYYVLyr9fg3tYe%2FaUSx65h9bxbp%2FNJcB727X7UPn5tVUFJP0c4TsqcoHIW4VbQpjicBNVudLSimCvSyH%2FiEleVPZ8AHU8HehhnPWn9Lk0V4jMrPORPRd2mwqUpKCxtqkudhVAO%2FDYAsB1FErWhb3sEhK98aGHCr3n6RiFfsHxJuCdhpkjRevSahS1MrajqBOrHNj4A2s%2FbB8sizSzI29BJzWPKOI8ZPOdZgnJT0r%2F7sCRSL68ATUWnfm0mmTWSAqSp7xaWxjsGUAZeAM3T1sjclbVbXlcIHY6Ldn1flHW%2BTlAh6naGzHP8F6g%2BemnjT6lumJLLMrl2UBvMl4m%2F6kyxtzZtjcoGkcuexFkqg5yUfyx7NYQ5pRsQZ2xJp6CtYAOJ%2FrCCTWGmUzGgUE9CqehUs4nlAFnTtmHumvX1AcwSvwX4KxSVf7rzRzfsH6gr%2B4ya3kHoajwr4hdfRw%2BFWTdaG5UIvbqli%2BGY5jT%2BRkkLZA%2B81owm87rvAY6pgHuGDGFBysXgiP%2BzgXswq5h7nKbaOJMCYoY4lJSqJCLYgmb1MzVYHivrQ1%2Fp9lnIBqOdgunRh51OsrH2K4dREfr9os5J0tCAbBAno09Ef4ZyrT%2FhbbVUA3UBi2flUGL9oEurXiojrIf0tP%2BnARJGjb6eRrYREXSfNT9E5gkO7y0G0s1rerTyy8MgzjkVT5YQjDtWx568QGQt8Wd4zOI%2F47g7bCg6RZ6&X-Amz-Signature=5727bf93a59cd08f8617ac1b971bf6adc874d47a7db53e79712bc34024bdcea9&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 2. Box and Whisker Plot
A box plot shows the distribution of quantitative data in a way that facilitates comparisons between variables or across levels of a categorical variable. The box shows the quartiles of the dataset while the whiskers extend to show the rest of the distribution, except for points that are determined to be "outliers".
**Syntax:**
```python
sns.boxplot(x='header_1', y='header_2', data=df)
```
**Example Output:**


![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d207ae92-0a7c-4e2f-aa65-0ee5a2c33bf7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RXRVVW24%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T031642Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBjoWbCkjltGwUHlS6RKLgO9UGJRRMI1U3ngsx0Vr7ZFAiAQmtVrekRQWWetUb3Zr4IlwhJ8NptUgZ%2FfAfEGSyAr9SqIBAic%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMiNAnj8bb0vqaLvwmKtwDolaEpq260PcCuepBl9o0n9RHvbzdpVfEZsQBXkmhhYxWKmV19UP5eI0SdKj56ouo4yA%2FjFw2Y27tvmt9KokBiMdXBP6GuLVNy%2F3HKOtGgA5gMZqNG1iDHTkfSAXwnyTbG3nJNn2oxvxhjlVaJGohqNrEP5Do7KUaGPhzpG5ra92Ui9VRjZq4UM6TmrUrU9R8u%2FB%2Ft8IrArB2P8lZ9iM9o5asZAJ4hDgmH1XThQ6rQ0d8FyA29Vb%2FQKbveV5Q%2BY5dnYIo%2Ft%2Fr0UOCAAEas5r3LiKz6%2BiQQ2OxL3AzU1mAMGIiIuB2c8yn5xB8uI9gdd6fMQKvaOGxRX0T8neznkuvnHpDnSsAYf7ZOS0a3m9%2FLkuojoCVf8VRMvRPE3vHAursDri4KVB3eoZIFCKw2Hgg7ps6NDzMcmedzf3anC86sjA4hjBbCN0pZa98jI3YbAOw3Ir2xjFQdpmSJCwW3hUvVzNe0861aI%2FJXeodVob8qUBGNNdz03lcS6CT7Mt5A2yvqFvO0OzQQLvD7BEH79R7ZFVZDBwbkncge7GbCCRXvfTi8GbAkjHdW1wAkGZ9TKPIMqS8M4kocIM04s12uK4uNPJ2vIk2lBZsYi0XS69KKwaGiQKRVhHG6x7ofM8wz87rvAY6pgFJS%2Bb0VvhxNWhdoclZqGD1PFEO%2F6EwYgcinoyqCFKNhllXhaF3wp4uGYF0h0QkaO0ZQS2WKG7BRrRPCmwoPiNPB9totA36BjG%2B8DFt7agWZIrULSp934WntkluTDfak6eGzkVBY%2BDtn8QE9e43H4GrhIqXHpsRa6CO2FJU%2B71rzj0z6TxyanqbxCPVyl%2BmvmO9qcnUBJO0C%2BPBAmDpH6Weis6F%2FaFx&X-Amz-Signature=7d63ae2f8c48c57b795126d47f36db9e49bdd2615c15d4c12addcd6b679c45a3&X-Amz-SignedHeaders=host&x-id=GetObject)

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0e516edc-7551-4792-ab18-0494db3c4c0c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XK5ALSRZ%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T031642Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCG2H8I%2BcEflbADT%2FP6S585oqpgfsjR%2FlqRPZy98Q4eqwIgLD0IMjzCtNQXjd80M8Rza4XJZHv6KUrxglxqdpmvG8AqiAQInP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDH4wX7NE7XbSLIk3wircA6KU1Nj8N32IcdWm4ExMOtg9kd4eChzbRjYZ%2FNKW3VzsJlUIHKemf4wZfdSIdP%2BrGXh2goeMltNNnlqAVWkO1Wqs3D8JHLf82BtPpVafrk9JpJmVjKnjWcjQeJ4Y3TNhfCRkAIt5jCvGOKNpDOOW6mrxk3tdQhEx6ueUraPUfLBsTpYbCRECcOa2UrZwjb9%2BEf5K6suYIGl2M0KpxTFmJIStsMDcibxhYX%2Fu0xNAKfgAQ%2BK%2B7IWbS%2BAq3i9s9QMjqQL3kXuEuHN4%2FnZEsu4Z20mEE8C1Wq0QRd4UtIE0P2A050iWEyjbarNsVvLIWtodYukF50%2B2E0dGOTRp%2BsMblR7Ajpp80BXctGfdVQyemm1TR7oQxQAHEiEigC9VC3pFHzriJirjyn970U49yA9GkxeYCIOQNuLHI1OzGPIYfirzaGShxi0iiLSjXvpcq%2F3h18EpdGABcNFTeokhwfy1rchBJaezflxGXGB0d5pHjcZvfwLRM208PyUkDHD5AU2Kwhr9s9Xsost%2FzKamJiijG4AiF8pAFG8htbcQ0%2F1vh9mAT8vroLiVX2avLxOCp%2FgDt3QNxYqPU843dGzmi2Cd4ir%2Bfojn%2FFdP6QTBXvBW96PMEZNd45H%2FZLQrupzoMMTO67wGOqUB%2BEwhMxQKZlCnXTlufj18j14g8OrRYpNW35oCQNgBc%2FfyxpdZFzWz6sBmXYFlaLY5TF3Z5gfE4rFPSnq7WRdwYE%2FzE%2FLD9sWcypldxsbV576ezfIzqQyLHCyK8kzdYt3NLEo%2BDx298tjHEthiEZGwQ1oNz2Z2nD3oOvdGRXiDwyGmCbmlwoLslI8XliIKOlCeqRvnL3pkMnaCEO%2Bd3iHQcWmslUzc&X-Amz-Signature=3a9318963f15e30ccc55a100eb9f66d53dd9a0452a2654f3d33de7f596d6c4c5&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23a79b9d-2356-49a9-8fd9-65c6b0ab2cc5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SN4CLX2Z%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T031641Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHrjtgPz3jqYFUvf79OKAal2lJ%2FZVo9qFbR53wmp6imWAiAfvozytT2Uf5CRhdsQ4ZrClZqqUyP1FZm4i5ITxNQ9DyqIBAic%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMPrBbWq4jxPz7U49cKtwD6v66We%2BDg8rNoM6pYSj9Ks58cbOFK4oSpDq6PgQC6IkYnQytvZ0JRtvryMmNIMgOSyIv7%2BYa%2FUG9NHcPC8Yq3yvG91N7BjuEuaMsqvUf71J4AVVdLEewLnD%2B3plgLuUeYUSyo1h5smqkYYVLyr9fg3tYe%2FaUSx65h9bxbp%2FNJcB727X7UPn5tVUFJP0c4TsqcoHIW4VbQpjicBNVudLSimCvSyH%2FiEleVPZ8AHU8HehhnPWn9Lk0V4jMrPORPRd2mwqUpKCxtqkudhVAO%2FDYAsB1FErWhb3sEhK98aGHCr3n6RiFfsHxJuCdhpkjRevSahS1MrajqBOrHNj4A2s%2FbB8sizSzI29BJzWPKOI8ZPOdZgnJT0r%2F7sCRSL68ATUWnfm0mmTWSAqSp7xaWxjsGUAZeAM3T1sjclbVbXlcIHY6Ldn1flHW%2BTlAh6naGzHP8F6g%2BemnjT6lumJLLMrl2UBvMl4m%2F6kyxtzZtjcoGkcuexFkqg5yUfyx7NYQ5pRsQZ2xJp6CtYAOJ%2FrCCTWGmUzGgUE9CqehUs4nlAFnTtmHumvX1AcwSvwX4KxSVf7rzRzfsH6gr%2B4ya3kHoajwr4hdfRw%2BFWTdaG5UIvbqli%2BGY5jT%2BRkkLZA%2B81owm87rvAY6pgHuGDGFBysXgiP%2BzgXswq5h7nKbaOJMCYoY4lJSqJCLYgmb1MzVYHivrQ1%2Fp9lnIBqOdgunRh51OsrH2K4dREfr9os5J0tCAbBAno09Ef4ZyrT%2FhbbVUA3UBi2flUGL9oEurXiojrIf0tP%2BnARJGjb6eRrYREXSfNT9E5gkO7y0G0s1rerTyy8MgzjkVT5YQjDtWx568QGQt8Wd4zOI%2F47g7bCg6RZ6&X-Amz-Signature=fe1bba2ac877d5056590e2c560b113d0b61ddc0596e8f4d5a55683b35318ebc7&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 4. KDE Plot
A Kernel Density Estimate (KDE) plot is a graph that creates a probability distribution curve for the data based upon its likelihood of occurrence on a specific value. This is created for a single vector of information.
**Syntax:**
```python
sns.kdeplot(X) || sns.kdeplot(df['age'])
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0d571213-2a2f-4921-a50b-880847aa05ee/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SN4CLX2Z%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T031641Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHrjtgPz3jqYFUvf79OKAal2lJ%2FZVo9qFbR53wmp6imWAiAfvozytT2Uf5CRhdsQ4ZrClZqqUyP1FZm4i5ITxNQ9DyqIBAic%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMPrBbWq4jxPz7U49cKtwD6v66We%2BDg8rNoM6pYSj9Ks58cbOFK4oSpDq6PgQC6IkYnQytvZ0JRtvryMmNIMgOSyIv7%2BYa%2FUG9NHcPC8Yq3yvG91N7BjuEuaMsqvUf71J4AVVdLEewLnD%2B3plgLuUeYUSyo1h5smqkYYVLyr9fg3tYe%2FaUSx65h9bxbp%2FNJcB727X7UPn5tVUFJP0c4TsqcoHIW4VbQpjicBNVudLSimCvSyH%2FiEleVPZ8AHU8HehhnPWn9Lk0V4jMrPORPRd2mwqUpKCxtqkudhVAO%2FDYAsB1FErWhb3sEhK98aGHCr3n6RiFfsHxJuCdhpkjRevSahS1MrajqBOrHNj4A2s%2FbB8sizSzI29BJzWPKOI8ZPOdZgnJT0r%2F7sCRSL68ATUWnfm0mmTWSAqSp7xaWxjsGUAZeAM3T1sjclbVbXlcIHY6Ldn1flHW%2BTlAh6naGzHP8F6g%2BemnjT6lumJLLMrl2UBvMl4m%2F6kyxtzZtjcoGkcuexFkqg5yUfyx7NYQ5pRsQZ2xJp6CtYAOJ%2FrCCTWGmUzGgUE9CqehUs4nlAFnTtmHumvX1AcwSvwX4KxSVf7rzRzfsH6gr%2B4ya3kHoajwr4hdfRw%2BFWTdaG5UIvbqli%2BGY5jT%2BRkkLZA%2B81owm87rvAY6pgHuGDGFBysXgiP%2BzgXswq5h7nKbaOJMCYoY4lJSqJCLYgmb1MzVYHivrQ1%2Fp9lnIBqOdgunRh51OsrH2K4dREfr9os5J0tCAbBAno09Ef4ZyrT%2FhbbVUA3UBi2flUGL9oEurXiojrIf0tP%2BnARJGjb6eRrYREXSfNT9E5gkO7y0G0s1rerTyy8MgzjkVT5YQjDtWx568QGQt8Wd4zOI%2F47g7bCg6RZ6&X-Amz-Signature=d34602a81846f1616155949f83256882df7416ce79ffb6095e1ee998bd397dc3&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/53752550-ef82-4ca9-a01a-09921f0282d0/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SN4CLX2Z%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T031641Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHrjtgPz3jqYFUvf79OKAal2lJ%2FZVo9qFbR53wmp6imWAiAfvozytT2Uf5CRhdsQ4ZrClZqqUyP1FZm4i5ITxNQ9DyqIBAic%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMPrBbWq4jxPz7U49cKtwD6v66We%2BDg8rNoM6pYSj9Ks58cbOFK4oSpDq6PgQC6IkYnQytvZ0JRtvryMmNIMgOSyIv7%2BYa%2FUG9NHcPC8Yq3yvG91N7BjuEuaMsqvUf71J4AVVdLEewLnD%2B3plgLuUeYUSyo1h5smqkYYVLyr9fg3tYe%2FaUSx65h9bxbp%2FNJcB727X7UPn5tVUFJP0c4TsqcoHIW4VbQpjicBNVudLSimCvSyH%2FiEleVPZ8AHU8HehhnPWn9Lk0V4jMrPORPRd2mwqUpKCxtqkudhVAO%2FDYAsB1FErWhb3sEhK98aGHCr3n6RiFfsHxJuCdhpkjRevSahS1MrajqBOrHNj4A2s%2FbB8sizSzI29BJzWPKOI8ZPOdZgnJT0r%2F7sCRSL68ATUWnfm0mmTWSAqSp7xaWxjsGUAZeAM3T1sjclbVbXlcIHY6Ldn1flHW%2BTlAh6naGzHP8F6g%2BemnjT6lumJLLMrl2UBvMl4m%2F6kyxtzZtjcoGkcuexFkqg5yUfyx7NYQ5pRsQZ2xJp6CtYAOJ%2FrCCTWGmUzGgUE9CqehUs4nlAFnTtmHumvX1AcwSvwX4KxSVf7rzRzfsH6gr%2B4ya3kHoajwr4hdfRw%2BFWTdaG5UIvbqli%2BGY5jT%2BRkkLZA%2B81owm87rvAY6pgHuGDGFBysXgiP%2BzgXswq5h7nKbaOJMCYoY4lJSqJCLYgmb1MzVYHivrQ1%2Fp9lnIBqOdgunRh51OsrH2K4dREfr9os5J0tCAbBAno09Ef4ZyrT%2FhbbVUA3UBi2flUGL9oEurXiojrIf0tP%2BnARJGjb6eRrYREXSfNT9E5gkO7y0G0s1rerTyy8MgzjkVT5YQjDtWx568QGQt8Wd4zOI%2F47g7bCg6RZ6&X-Amz-Signature=bfefe8c3c0c62d16d937ffddc92eb9d09d16e8839d2936ae76e6b34759e149b3&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
## 4. Correlation Between Variables
Correlation is a statistical measure of the extent to which different variables are interdependent. It indicates how changes in one variable are associated with changes in another variable over time.
### Positive Correlation
Positive correlation indicates that as one variable increases, the other variable also tends to increase.
**Example: Engine Size and Price**
- **Positive Correlation:** Engine size increases, price also increases.
- **Visualization:** Scatter plot with a steep positive slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c7ea9b0-3ef3-4357-a9c3-554fc71b6b15/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XRSVTTXS%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T031642Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIBKO8G46HvP5YK9IM5LPClQhkYqzibu%2FH1EFH%2BwXiZvhAiEArCWjgROPZSakb7FgNU3kjeUHl%2F7Z6qSTOKYoCewDHMUqiAQInP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGCRiWA5302UF59NrSrcA9pBR4d7lSXzlxiLk1yW%2FVyVL8B%2FM9u5hIqsfriRQbgij9yxnDhHQx0Uql5JeuqhRcgGXIUlSW5n4IWx9xz%2FUgQ89766UoI0QibXiESQLVOyvGqTNrX0CFsBjLPBpT9e%2BS%2F5keOilXUsRFu2FNkWXdlwws0ZForPbUzmFaYD8FoA2FONIRpZTGD12%2F348pImcE1gsLHAV7KkiVLRT8NHAy1%2FN%2Frc9hHaq6S5bhAbXr92y1J%2BYbdyPUocqPj8YOzAvYCBb4XG2FOiq6PP587u%2BxA0xOR7mlJaashNUd8aQ6eC6fQ4B4I%2F4Hr%2Ftvf41CZwZCixQGCgAVqeJXOcnCTUsCckI6QkrXX9q3he8U5LUgkAoPfPhgbOPQ5yYlnRSCJhHTao4booD17iYX3ihCc%2BUiUI16vWk6XAcpHm0aC7QHP5OpJXwmeWJWKkxuSxgqQllwSVOaaf8p%2F3pP6SXSitl7V5qmacvcMYP%2BOY8lb1A5PF5LAqUNcxWSgmyug757VgXLyCuc36kxz%2BdgnV8vQS%2FEGcOuUVPzLTpEGXqD97Lt3jDn91J2NI1xa1J1w6tmycfCtxQNVV37Trti0cXdY8cY8%2FHgK03bAp%2F%2F25vryus594wqiyrECfVk6DuJyQMM%2FO67wGOqUBPo4zm6ovq%2BGYtEgEPAd1YgmQxqZyGRphnCJgxmexQCktNBVGOlwoEqZJHverfuLsXQY6R7BRV6Bx5ixFRKyKMnzkb5GBgTVNaSnTXKdk3pb78CK25D8q2P1ZQubx8ZB0zfDDUYJgVJnaqdN8UTOpeAoXEbHkWuh6X8Qb2PRwzd4KgK%2BHIwx%2FtqQ%2F2d0GxOg%2Fw6DZrlX54zLlplhgXphICASb0WTN&X-Amz-Signature=b57bd6e6fa256ac64653bb03e808cc423d54c447c36180af91a8ccd17e7a8f34&X-Amz-SignedHeaders=host&x-id=GetObject)
**Explanation:** When engine size increases, there is a corresponding increase in the price of the vehicle. This positive correlation suggests that larger engines tend to be associated with higher prices in the market.
___
### Negative Correlation
Negative correlation indicates that as one variable increases, the other variable tends to decrease.
**Example: Highway Miles per Gallon and Price**
- **Negative Correlation:** As highway miles per gallon increases, price decreases.
- **Visualization:** Scatter plot with a steep negative slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/10f1f798-9cc4-4df2-a9c1-5a339f554a0b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TZW23A25%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T031642Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICTw1xHBXC%2Bzc%2FIVtG3R2zBnyhEHjGKxc7SCEP5Rn8dJAiAA2odN3AOWn8MklAOd1YPhOKDW3Al8poJeo%2FoDd2ApySqIBAic%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMsN1Wjn11xE9Tfi51KtwDb0efNPSArcSIo0n6EBhcRHR62K5ZRSFmYAjIH%2Fmw0louBSaK%2BsA5mYDoOybgUbp%2BBmpKVuQFwkRtaL4LZlt2i5fUzNF%2BlrOq3Ac9M8VID1DqkkDK%2BKnBjLGGp3FQg%2B1fjienn8tEPeZaxDklQi5UKpv3FxDGfMGF73zJEp0FyTlq%2FQvK4shNiCZBypwQFI5xc5s3FLaN1TwJawHLlLO67LxLkWQXPVsKVIsURaMPsK5HX7AUNOT%2F97Jd5fVMSLaKZSq%2BPTP8e1%2BVkc4rne9f5vt%2FT47SXPA8gnfXhbg3WEzeq4MMrkjk8NblhtuyShgrqMS48eAqGIUSGh0cX0dlNhhWmd7KSbq0JQQjI0z1Dnepn7BTUfeet6fZzg4T13Q1mmYoOI5Mj1RL8XvspcYalL4kIRpMQE3X2C%2FA%2B529Nchx0Ase7bfXX7ln04y%2B9uJJzbx4GTlwI%2BFPzYBU8euyKXoufhLgD%2BDFtIzhp3lP247%2BH%2BKLs439TlW4wys3da1sMD7ui9CosS0zZbUYTfFK0Y46ClAon4yD%2FswU38jqisOLPAgjaosVgCQsfKvuHwzbcdDoFLLtskfsauOgBRRC6HkMsfbXhawYmNryFIqaLlGb40Y6L0yKpO9tCKMwus7rvAY6pgFBQpsLI%2FBRy1vikYgts3xAiA0ZzkyrGhiL6zA6L4XHhtetLT3%2B0VVwWP4VR%2Bf0J75kRJZmJaXmDokA09UGyC6747%2BSJt8DoZvs5XQqaUXa7UiQ%2BCPUwWh5UbT1jCAuQT1p2t%2F52AagdXQl%2FdgdOREkmlgWtfTHtDsXa4KQunTONwhM395l%2B%2BgXzV%2B8RQN8z612ryhjASELy%2FCUwgW7taWobfr0%2BZRn&X-Amz-Signature=af04364cf876429cff03d7de945a9c66724322528bde507a35fe5ffecdf6bf74&X-Amz-SignedHeaders=host&x-id=GetObject)
**Explanation:** When highway miles per gallon increases, the price of the vehicle tends to decrease. This negative correlation suggests that cars with higher fuel efficiency (more miles per gallon) are generally priced lower in the market.
___
### Weak Correlation
Weak correlation indicates a lack of strong relationship between the variables.
**Example: RPM and Price**
- **Weak Correlation:** Low and high RPM values show varied prices, indicating no strong predictive relationship.
- **Visualization:** Scatter plot with no clear trend or slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9f914514-8914-4bf4-ac84-d9e3077f6eb1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664MZFUPG6%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T031642Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHXmBa%2FOe%2BbNv9cuyWDtDx36o4mH%2BMq4ZuhKUAfcfZKeAiEA8Iukf3%2BtadUhUfLj2r6xkNLbHo4MPBDewgnJ%2FemJPncqiAQInP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLhLkndm8GorWWvGQCrcAyn9dSoD%2FVTRmJL0Slxx5S9y7ERbfKEtF%2FkN4RprpUYPT%2BwJUXVM3VHzUnO5q6EJiOzgZ%2BPQIPqxTjLSHsWKfULMRxx9xd4mrv6jYCSkkkI3m7jCVbXfM6rjL9ANeqRlseCYO2bH6dl8u9uXflQvB552VShy8YNNzMnq142gZbKwTDAfMy6TuSg%2FAuI9Uuxpk3I058ltWghTOQahFhz6LNB9PgGbFPflYN6%2BPLeV6nO%2FhSl9o0OhQ9RPSzle3voUtpdF83A53oLzmRvAm1UnO%2FN6Mm1TKD3rXIvC0mYI%2BdX8lJTI9LXksZ06S4D5vR6uC1Eyvtd7zCFe%2Fr9gW86SL0u%2B6DE%2B9AuFPGFSF4VK8DJLZmmR8XlyIzZBclQ%2FYASTpBjwKnUqJljyrx%2FdSbhWhm%2FTCoPM%2Fl5I3yWGvCHFnhGj1RNXbzkvplf616y2xFVS2UxhJAeOvaTnvFrZe1GfQQZppoIzarco32wE5CWShPp6YuS0c2pYHSnoEJBiYgvPDSzCJikisss8wmGSwE8K0zegsDWfnbLPeK5zTjVX27VZ8NM0dQROzoS0whD3sXT3i8Vj%2F2g9aZt3S4yA%2FgnxhaRYngAkSN2vZ8JN581VWuIQoxO3apbeNOuYgt7sMM3P67wGOqUBHIyjhDGlo%2BukMIsxJpFNI0ZtMEZOMnK1FcS01dYiibBg7p5GxGU2TWsGzxlwET%2FMI25ftf0A8G6CyktodwQHECtCNMrdADvXl7FahtAUcIx5%2BFAShMEJhKzWYZ%2FYtEIJDn%2FoX2Px3coFYFel6%2FnnguO6l9UPgTCorELrn2g3ZVYr56SrfANv1Z50a9v74MxDn9LWprpDTbIsK2FpWEDugGDau%2FI9&X-Amz-Signature=5f2515aa0608eee94be4a1ace69de31ba7d33d4233e84ea7e6efcee0d7258f1b&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f18086e5-5b04-4fbf-8309-8944ab20d213/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663LMQQT7E%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T031641Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDHDpLdcxwwVzCFEQBJEE2lWw6%2F%2Fs47eDUnz947AaZhMQIgF1iKC%2Fr5hwCxm8NV1JqZLX%2Ft%2BgIzPPBQzoysjDLdyu8qiAQInP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDM%2Fq0HArqcVQFBb3GCrcAyEtMQTPTBkSZyOxSxhNpjei8myJ7f6rDRdqUrYimJsp5m0viRtZQEnEQo7oXqjAY2ycmwQNUtrnphTB4lR35eJnorfpcLvNe1whKtqODbZZmmrbSnpoD5mx6ro85VHiVtumavfQfUXJb8KvgxCWPYJtdsAOoOhcaxXsanqP64hOaCWGT73uQKJEtaRYjzoETHKdxG6%2B19xS2ZkvLeu7N9T19mX87Pp6Fme%2Bs%2B2yxszHX7H8jUzQHAqpDO7UxtiMW8OAzWhhuRNyQAbphMSR5XkLFHPBzzTsT4Xd1tuqE7ZZLKWEW04R%2FlKl9myKMSG6HFBryrutrr0PgeuSbKyoqDI7FRUlbsXwOqezMGQbqXISfxlHCDbNq366nvpeZBOXiGl5ScWW10UP4E09T%2FTEGLv7cByIUHcuJj92Gpw%2B6nlZibeoO8BjHsOxM%2Fo7PJewYlImsXNgr5Sux7KwY1dP5%2Bn0ceUQCyJIt1LfL3mS0Cu0JRzcpXioXaPIDM%2B9qxVXLStoRMlMVcfNXrnfbHqHZx3njyRBsyt8QixWJ6j6A09D6jel2Jq94zHZdJUT1p7wDJ9sl9GOL8uPv1ndjub5UWkZKKtweFnhQKR6rMbNH1az1x%2BugmxUC9k4fjJqMJPO67wGOqUBX4sDbjlNUCwkdzJ0H24mdCXkUassqHZ843vdh%2FBuBR3oh7UrdYsRUpMIqn58di%2BUXeKt7gsjMYt1c3%2Fd63R0T6aUduVt3svRwJgewjIUxbRqh%2B4dKxeU5OiX5BBSKebXl8xU9y%2F%2B1PPFAO2gyTSvlEq2gUBv8HX%2BPyPMoiYBDUBTWQ4EQc77nk5dSwhFaHqUJzvB4Pm1eGuq37bosYANpG1%2Bc9Rk&X-Amz-Signature=2b401e41a3905675cba5912e0608be6485818e12762e413a0f908cc898c7fe10&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Correlation Plot
Heatmap visualizes correlations among variables. Color scheme indicates Pearson correlation coefficients. Dark red diagonal line shows perfect correlation (value of 1) between variables and themselves.
This heatmap offers overview of variable relationships and their link with price.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cd3b341e-cc1a-45f7-8aec-cdc00436d270/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663LMQQT7E%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T031641Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDHDpLdcxwwVzCFEQBJEE2lWw6%2F%2Fs47eDUnz947AaZhMQIgF1iKC%2Fr5hwCxm8NV1JqZLX%2Ft%2BgIzPPBQzoysjDLdyu8qiAQInP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDM%2Fq0HArqcVQFBb3GCrcAyEtMQTPTBkSZyOxSxhNpjei8myJ7f6rDRdqUrYimJsp5m0viRtZQEnEQo7oXqjAY2ycmwQNUtrnphTB4lR35eJnorfpcLvNe1whKtqODbZZmmrbSnpoD5mx6ro85VHiVtumavfQfUXJb8KvgxCWPYJtdsAOoOhcaxXsanqP64hOaCWGT73uQKJEtaRYjzoETHKdxG6%2B19xS2ZkvLeu7N9T19mX87Pp6Fme%2Bs%2B2yxszHX7H8jUzQHAqpDO7UxtiMW8OAzWhhuRNyQAbphMSR5XkLFHPBzzTsT4Xd1tuqE7ZZLKWEW04R%2FlKl9myKMSG6HFBryrutrr0PgeuSbKyoqDI7FRUlbsXwOqezMGQbqXISfxlHCDbNq366nvpeZBOXiGl5ScWW10UP4E09T%2FTEGLv7cByIUHcuJj92Gpw%2B6nlZibeoO8BjHsOxM%2Fo7PJewYlImsXNgr5Sux7KwY1dP5%2Bn0ceUQCyJIt1LfL3mS0Cu0JRzcpXioXaPIDM%2B9qxVXLStoRMlMVcfNXrnfbHqHZx3njyRBsyt8QixWJ6j6A09D6jel2Jq94zHZdJUT1p7wDJ9sl9GOL8uPv1ndjub5UWkZKKtweFnhQKR6rMbNH1az1x%2BugmxUC9k4fjJqMJPO67wGOqUBX4sDbjlNUCwkdzJ0H24mdCXkUassqHZ843vdh%2FBuBR3oh7UrdYsRUpMIqn58di%2BUXeKt7gsjMYt1c3%2Fd63R0T6aUduVt3svRwJgewjIUxbRqh%2B4dKxeU5OiX5BBSKebXl8xU9y%2F%2B1PPFAO2gyTSvlEq2gUBv8HX%2BPyPMoiYBDUBTWQ4EQc77nk5dSwhFaHqUJzvB4Pm1eGuq37bosYANpG1%2Bc9Rk&X-Amz-Signature=21739b7c2cf6747e90035d74dafd1e84e3a85c3abc1f713f2069ef64b8e811ed&X-Amz-SignedHeaders=host&x-id=GetObject)

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
