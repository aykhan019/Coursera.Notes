

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7e6d594d-952e-44b6-97ea-31225882aea6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665JLEQUO7%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T211342Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAUaCXVzLXdlc3QtMiJHMEUCIFFYY6JVwz08%2Bq%2BErM6isE%2BTM2feAZwtPOI5Ke9ItEUsAiEAk4ItCVcz%2Bg1HsjqZhT4MuHqOUa8WvG%2FcQ%2FqL7f5n60Aq%2FwMIHhAAGgw2Mzc0MjMxODM4MDUiDHCV2gBWK5Y8Xt5i6ircA9%2FRbMc0VF%2BLQWtUWlBDHbXYe2eu2Rtq39peBhz3tI2E50dSU0KQt45B0bVDO5K8UTUf4NO7ZlugMKa0RjpLj35F1RAY28JE9KFILBal%2BbKgrZpysyfQJtAd255Y3ovpDVYjqoioYrFmkxs7vkp2SK1MFutRD1tZSogDa7a4e75ymSK%2BaZfuS2zsu6s3N8h%2BhlpItakTNR9DJeC937qonXqVXBx1esfG%2BuMsDXdx0eFRypaxa%2FLdpQ4L0HG5upVZMllNQB2eudiblU%2FGXoTNhwOyAZN6Uvvyjc8iBqH5UCgMYgKPVcmXBoLoXE8CptcLUOJIj9CLrcRCqy8ltVcOKbOsBhpUE8sosNvRj1pGB%2FmOun36oHzTiOYoGkBtb3x43xd%2BefuvORBlIvQpTkBesT4hWhpISSgoJ0rWiz26FYbj%2BPQxgHgqKMAuayr6YYcSb1CoVIb8nlCKVTgKfIMugD1FwGR5zyD8mZbKTUa4qA83SlZJXSkxxXajDWqnZ63pc632i9W1RXrtabnPxLYMS45aPxjMD2AujgSwqSF%2FnrCLdnCIq3VuS%2FZ6T0pW72M8yqYC0xe0VNmR9SDzhZi32IfTxD6XQTYWY4K7bzgh%2BMobmRvFnPiWzG4zosxJMOTZhL0GOqUBRo9tf4tEYzTY9qge%2Fn3U6xNkqj%2BDGedl8iS6X2A%2FO396udP%2B9SKCSm4uLQk2ieP8Y3L2A83xzAAXcus77K%2FpLZvLh7sW9euVhTsoAaD2BD5BlyUy%2F7upBevAq35zUg6cMFHpvTBzvr5P4N9gaOUuHf4qxndJFAJTx%2F8aetuHs51MmL8YG94cJWuctQj%2Fcl40PY3fBnPUO26wdKTCysNgeNCmcEEs&X-Amz-Signature=855b726a42c5fa58c7f021667c907b2fa4a6674aaa93c9035c8d99a8f06ed561&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cbfaed9e-b398-4902-8936-dea058b21def/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665JLEQUO7%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T211342Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAUaCXVzLXdlc3QtMiJHMEUCIFFYY6JVwz08%2Bq%2BErM6isE%2BTM2feAZwtPOI5Ke9ItEUsAiEAk4ItCVcz%2Bg1HsjqZhT4MuHqOUa8WvG%2FcQ%2FqL7f5n60Aq%2FwMIHhAAGgw2Mzc0MjMxODM4MDUiDHCV2gBWK5Y8Xt5i6ircA9%2FRbMc0VF%2BLQWtUWlBDHbXYe2eu2Rtq39peBhz3tI2E50dSU0KQt45B0bVDO5K8UTUf4NO7ZlugMKa0RjpLj35F1RAY28JE9KFILBal%2BbKgrZpysyfQJtAd255Y3ovpDVYjqoioYrFmkxs7vkp2SK1MFutRD1tZSogDa7a4e75ymSK%2BaZfuS2zsu6s3N8h%2BhlpItakTNR9DJeC937qonXqVXBx1esfG%2BuMsDXdx0eFRypaxa%2FLdpQ4L0HG5upVZMllNQB2eudiblU%2FGXoTNhwOyAZN6Uvvyjc8iBqH5UCgMYgKPVcmXBoLoXE8CptcLUOJIj9CLrcRCqy8ltVcOKbOsBhpUE8sosNvRj1pGB%2FmOun36oHzTiOYoGkBtb3x43xd%2BefuvORBlIvQpTkBesT4hWhpISSgoJ0rWiz26FYbj%2BPQxgHgqKMAuayr6YYcSb1CoVIb8nlCKVTgKfIMugD1FwGR5zyD8mZbKTUa4qA83SlZJXSkxxXajDWqnZ63pc632i9W1RXrtabnPxLYMS45aPxjMD2AujgSwqSF%2FnrCLdnCIq3VuS%2FZ6T0pW72M8yqYC0xe0VNmR9SDzhZi32IfTxD6XQTYWY4K7bzgh%2BMobmRvFnPiWzG4zosxJMOTZhL0GOqUBRo9tf4tEYzTY9qge%2Fn3U6xNkqj%2BDGedl8iS6X2A%2FO396udP%2B9SKCSm4uLQk2ieP8Y3L2A83xzAAXcus77K%2FpLZvLh7sW9euVhTsoAaD2BD5BlyUy%2F7upBevAq35zUg6cMFHpvTBzvr5P4N9gaOUuHf4qxndJFAJTx%2F8aetuHs51MmL8YG94cJWuctQj%2Fcl40PY3fBnPUO26wdKTCysNgeNCmcEEs&X-Amz-Signature=d7e2334ad8c1b2caf0679b0388c7957870b26029dc8069fe8d52c45a0538f8ca&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/91181646-b1e0-4433-9711-6259a96a9247/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665JLEQUO7%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T211342Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAUaCXVzLXdlc3QtMiJHMEUCIFFYY6JVwz08%2Bq%2BErM6isE%2BTM2feAZwtPOI5Ke9ItEUsAiEAk4ItCVcz%2Bg1HsjqZhT4MuHqOUa8WvG%2FcQ%2FqL7f5n60Aq%2FwMIHhAAGgw2Mzc0MjMxODM4MDUiDHCV2gBWK5Y8Xt5i6ircA9%2FRbMc0VF%2BLQWtUWlBDHbXYe2eu2Rtq39peBhz3tI2E50dSU0KQt45B0bVDO5K8UTUf4NO7ZlugMKa0RjpLj35F1RAY28JE9KFILBal%2BbKgrZpysyfQJtAd255Y3ovpDVYjqoioYrFmkxs7vkp2SK1MFutRD1tZSogDa7a4e75ymSK%2BaZfuS2zsu6s3N8h%2BhlpItakTNR9DJeC937qonXqVXBx1esfG%2BuMsDXdx0eFRypaxa%2FLdpQ4L0HG5upVZMllNQB2eudiblU%2FGXoTNhwOyAZN6Uvvyjc8iBqH5UCgMYgKPVcmXBoLoXE8CptcLUOJIj9CLrcRCqy8ltVcOKbOsBhpUE8sosNvRj1pGB%2FmOun36oHzTiOYoGkBtb3x43xd%2BefuvORBlIvQpTkBesT4hWhpISSgoJ0rWiz26FYbj%2BPQxgHgqKMAuayr6YYcSb1CoVIb8nlCKVTgKfIMugD1FwGR5zyD8mZbKTUa4qA83SlZJXSkxxXajDWqnZ63pc632i9W1RXrtabnPxLYMS45aPxjMD2AujgSwqSF%2FnrCLdnCIq3VuS%2FZ6T0pW72M8yqYC0xe0VNmR9SDzhZi32IfTxD6XQTYWY4K7bzgh%2BMobmRvFnPiWzG4zosxJMOTZhL0GOqUBRo9tf4tEYzTY9qge%2Fn3U6xNkqj%2BDGedl8iS6X2A%2FO396udP%2B9SKCSm4uLQk2ieP8Y3L2A83xzAAXcus77K%2FpLZvLh7sW9euVhTsoAaD2BD5BlyUy%2F7upBevAq35zUg6cMFHpvTBzvr5P4N9gaOUuHf4qxndJFAJTx%2F8aetuHs51MmL8YG94cJWuctQj%2Fcl40PY3fBnPUO26wdKTCysNgeNCmcEEs&X-Amz-Signature=f80c33812ce7748d98cae62dd11aca9a9fc2f2f509857b34571e704f591ef572&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/09aba1c0-0d55-41dd-852a-a04c5b8a3fac/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RGM46IMC%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T211343Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAUaCXVzLXdlc3QtMiJHMEUCIQCKQq0sGoIaSUk3QYJgkj8nObp3jC36xvpQC80c%2BYZlCAIgMC8rW5yGq6md%2Fp4DgrOaKC81n5wXVIwZNLJWA3PpaNAq%2FwMIHhAAGgw2Mzc0MjMxODM4MDUiDJqsFe80PWXaNs9IdSrcA%2B2rSRPVe4OY%2BDlWTCR6ISDjkkLu3rexxOTmSC6JOGaDroPT0%2FICQiamyfA4Djj56QMYk0GN2k4yqSML99I9Z%2BSPjBTEE16hmAa4joaKLHgSRk3LdIDlBnF%2FFHp5OAQ5UMMEy8U8xhYKHcl05EAwp%2BDlWLJgbDdJilGe4AIJrS8X77Q1SdSy0kyyd61xfyVZc7Y5M4cPOuAWiAkcqwvsgOmcP7xwflzx06FQXaZix6fXgheFqsB7leTMTUaL3BUd06Jq0RpzZnBPxs1weOoD%2FLCL%2BfAzBLUPaUDxzZMjKPwFAwG65TOo%2F2J2E5wW0YxpJzZ3SOXy%2FrSf4BtHqhFwmkuNaNl8lWFcGsLXkBLfCEZCWp9D%2FdnlSQvEHxP61Z5Fhc%2Filg%2BdxY6088Ial9uh7IR2YL5%2BCK1YV%2B66EsKHJS73H4W7KoiaOyXAgCiUj83JFCnlCRwCgOjtfm0qNTj5cv58h1g%2FDuKUWSLtdpey9zI0%2FDEeliOMqHFtv85Ekhm4unhr1LLwYTx8L%2BygHHnXJGWdqqxQsy6M%2F%2B7VfYZDtMd9KRZ3fCLUJH%2BMgwau3vtl%2B4g0nO8qi9wTyPYAPPtCAL6G8n2R4d8iaHxARuvXMZLvdZwO9HtVqJVNSJcqMJLahL0GOqUBr8M0IGJ%2FzbkamOymcaxbamslAq9EXvnsw4myRu2kHJRMckKOTFR5j%2B3FZ8D08oWSvSbNoy2YgABz5a5f0zaYIYX0ButBdVxYGrm2v%2BpUa8ZOJOdynOcomGRDdiqreeaXWRN0CqUW9IdfSfBcNnvXlXiF2x9lHqaIeqAGzc%2BtB5cJKvSJihRKgJdokhwij9uaJScJ2dcp4ZNNx426ECSCSCKN8UvM&X-Amz-Signature=8d75cccf8a291681953e3c459aac320f517329f5d878eadc3fae8fcba370d560&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 2. Scatter Plot
Scatter plots present the relationship between two variables in a dataset. It represents data points on a two-dimensional plane. The independent variable or attribute is plotted on the X-axis, while the dependent variable is plotted on the Y-axis.
**Syntax:**
```python
plt.scatter(x, y)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23708af9-659f-4f23-b626-1a4292d7842c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RGM46IMC%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T211343Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAUaCXVzLXdlc3QtMiJHMEUCIQCKQq0sGoIaSUk3QYJgkj8nObp3jC36xvpQC80c%2BYZlCAIgMC8rW5yGq6md%2Fp4DgrOaKC81n5wXVIwZNLJWA3PpaNAq%2FwMIHhAAGgw2Mzc0MjMxODM4MDUiDJqsFe80PWXaNs9IdSrcA%2B2rSRPVe4OY%2BDlWTCR6ISDjkkLu3rexxOTmSC6JOGaDroPT0%2FICQiamyfA4Djj56QMYk0GN2k4yqSML99I9Z%2BSPjBTEE16hmAa4joaKLHgSRk3LdIDlBnF%2FFHp5OAQ5UMMEy8U8xhYKHcl05EAwp%2BDlWLJgbDdJilGe4AIJrS8X77Q1SdSy0kyyd61xfyVZc7Y5M4cPOuAWiAkcqwvsgOmcP7xwflzx06FQXaZix6fXgheFqsB7leTMTUaL3BUd06Jq0RpzZnBPxs1weOoD%2FLCL%2BfAzBLUPaUDxzZMjKPwFAwG65TOo%2F2J2E5wW0YxpJzZ3SOXy%2FrSf4BtHqhFwmkuNaNl8lWFcGsLXkBLfCEZCWp9D%2FdnlSQvEHxP61Z5Fhc%2Filg%2BdxY6088Ial9uh7IR2YL5%2BCK1YV%2B66EsKHJS73H4W7KoiaOyXAgCiUj83JFCnlCRwCgOjtfm0qNTj5cv58h1g%2FDuKUWSLtdpey9zI0%2FDEeliOMqHFtv85Ekhm4unhr1LLwYTx8L%2BygHHnXJGWdqqxQsy6M%2F%2B7VfYZDtMd9KRZ3fCLUJH%2BMgwau3vtl%2B4g0nO8qi9wTyPYAPPtCAL6G8n2R4d8iaHxARuvXMZLvdZwO9HtVqJVNSJcqMJLahL0GOqUBr8M0IGJ%2FzbkamOymcaxbamslAq9EXvnsw4myRu2kHJRMckKOTFR5j%2B3FZ8D08oWSvSbNoy2YgABz5a5f0zaYIYX0ButBdVxYGrm2v%2BpUa8ZOJOdynOcomGRDdiqreeaXWRN0CqUW9IdfSfBcNnvXlXiF2x9lHqaIeqAGzc%2BtB5cJKvSJihRKgJdokhwij9uaJScJ2dcp4ZNNx426ECSCSCKN8UvM&X-Amz-Signature=4291a756feff8139c6a729144534974124c46b889fe2b908d0c387f0f3bfc330&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 3. Histogram
A histogram is an important visual representation of data in categorical form. To view the data in a "Binned" form, use the histogram plot with a number of bins required or with the data points that mark the bin edges. The x-axis represents the data bins, and the y-axis represents the number of elements in each bin.
**Syntax:**
```python
plt.hist(x, bins)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/24e4424a-df87-40a1-b63b-195cbdc2e0ab/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RGM46IMC%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T211343Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAUaCXVzLXdlc3QtMiJHMEUCIQCKQq0sGoIaSUk3QYJgkj8nObp3jC36xvpQC80c%2BYZlCAIgMC8rW5yGq6md%2Fp4DgrOaKC81n5wXVIwZNLJWA3PpaNAq%2FwMIHhAAGgw2Mzc0MjMxODM4MDUiDJqsFe80PWXaNs9IdSrcA%2B2rSRPVe4OY%2BDlWTCR6ISDjkkLu3rexxOTmSC6JOGaDroPT0%2FICQiamyfA4Djj56QMYk0GN2k4yqSML99I9Z%2BSPjBTEE16hmAa4joaKLHgSRk3LdIDlBnF%2FFHp5OAQ5UMMEy8U8xhYKHcl05EAwp%2BDlWLJgbDdJilGe4AIJrS8X77Q1SdSy0kyyd61xfyVZc7Y5M4cPOuAWiAkcqwvsgOmcP7xwflzx06FQXaZix6fXgheFqsB7leTMTUaL3BUd06Jq0RpzZnBPxs1weOoD%2FLCL%2BfAzBLUPaUDxzZMjKPwFAwG65TOo%2F2J2E5wW0YxpJzZ3SOXy%2FrSf4BtHqhFwmkuNaNl8lWFcGsLXkBLfCEZCWp9D%2FdnlSQvEHxP61Z5Fhc%2Filg%2BdxY6088Ial9uh7IR2YL5%2BCK1YV%2B66EsKHJS73H4W7KoiaOyXAgCiUj83JFCnlCRwCgOjtfm0qNTj5cv58h1g%2FDuKUWSLtdpey9zI0%2FDEeliOMqHFtv85Ekhm4unhr1LLwYTx8L%2BygHHnXJGWdqqxQsy6M%2F%2B7VfYZDtMd9KRZ3fCLUJH%2BMgwau3vtl%2B4g0nO8qi9wTyPYAPPtCAL6G8n2R4d8iaHxARuvXMZLvdZwO9HtVqJVNSJcqMJLahL0GOqUBr8M0IGJ%2FzbkamOymcaxbamslAq9EXvnsw4myRu2kHJRMckKOTFR5j%2B3FZ8D08oWSvSbNoy2YgABz5a5f0zaYIYX0ButBdVxYGrm2v%2BpUa8ZOJOdynOcomGRDdiqreeaXWRN0CqUW9IdfSfBcNnvXlXiF2x9lHqaIeqAGzc%2BtB5cJKvSJihRKgJdokhwij9uaJScJ2dcp4ZNNx426ECSCSCKN8UvM&X-Amz-Signature=cdb444ea2766a38effa955b0be211f02532535644c6de62e5470e7533797a983&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ab5a6dfe-51f5-43ee-bcb3-33dae4a1c7ad/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RGM46IMC%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T211343Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAUaCXVzLXdlc3QtMiJHMEUCIQCKQq0sGoIaSUk3QYJgkj8nObp3jC36xvpQC80c%2BYZlCAIgMC8rW5yGq6md%2Fp4DgrOaKC81n5wXVIwZNLJWA3PpaNAq%2FwMIHhAAGgw2Mzc0MjMxODM4MDUiDJqsFe80PWXaNs9IdSrcA%2B2rSRPVe4OY%2BDlWTCR6ISDjkkLu3rexxOTmSC6JOGaDroPT0%2FICQiamyfA4Djj56QMYk0GN2k4yqSML99I9Z%2BSPjBTEE16hmAa4joaKLHgSRk3LdIDlBnF%2FFHp5OAQ5UMMEy8U8xhYKHcl05EAwp%2BDlWLJgbDdJilGe4AIJrS8X77Q1SdSy0kyyd61xfyVZc7Y5M4cPOuAWiAkcqwvsgOmcP7xwflzx06FQXaZix6fXgheFqsB7leTMTUaL3BUd06Jq0RpzZnBPxs1weOoD%2FLCL%2BfAzBLUPaUDxzZMjKPwFAwG65TOo%2F2J2E5wW0YxpJzZ3SOXy%2FrSf4BtHqhFwmkuNaNl8lWFcGsLXkBLfCEZCWp9D%2FdnlSQvEHxP61Z5Fhc%2Filg%2BdxY6088Ial9uh7IR2YL5%2BCK1YV%2B66EsKHJS73H4W7KoiaOyXAgCiUj83JFCnlCRwCgOjtfm0qNTj5cv58h1g%2FDuKUWSLtdpey9zI0%2FDEeliOMqHFtv85Ekhm4unhr1LLwYTx8L%2BygHHnXJGWdqqxQsy6M%2F%2B7VfYZDtMd9KRZ3fCLUJH%2BMgwau3vtl%2B4g0nO8qi9wTyPYAPPtCAL6G8n2R4d8iaHxARuvXMZLvdZwO9HtVqJVNSJcqMJLahL0GOqUBr8M0IGJ%2FzbkamOymcaxbamslAq9EXvnsw4myRu2kHJRMckKOTFR5j%2B3FZ8D08oWSvSbNoy2YgABz5a5f0zaYIYX0ButBdVxYGrm2v%2BpUa8ZOJOdynOcomGRDdiqreeaXWRN0CqUW9IdfSfBcNnvXlXiF2x9lHqaIeqAGzc%2BtB5cJKvSJihRKgJdokhwij9uaJScJ2dcp4ZNNx426ECSCSCKN8UvM&X-Amz-Signature=5ec0712ae2c2df38383b5b94cdde33419399ef84c8a5df3c1b5ecbd891ab53d3&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8f1b1d60-cf1b-42b3-9faa-f634c89c3f84/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RGM46IMC%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T211343Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAUaCXVzLXdlc3QtMiJHMEUCIQCKQq0sGoIaSUk3QYJgkj8nObp3jC36xvpQC80c%2BYZlCAIgMC8rW5yGq6md%2Fp4DgrOaKC81n5wXVIwZNLJWA3PpaNAq%2FwMIHhAAGgw2Mzc0MjMxODM4MDUiDJqsFe80PWXaNs9IdSrcA%2B2rSRPVe4OY%2BDlWTCR6ISDjkkLu3rexxOTmSC6JOGaDroPT0%2FICQiamyfA4Djj56QMYk0GN2k4yqSML99I9Z%2BSPjBTEE16hmAa4joaKLHgSRk3LdIDlBnF%2FFHp5OAQ5UMMEy8U8xhYKHcl05EAwp%2BDlWLJgbDdJilGe4AIJrS8X77Q1SdSy0kyyd61xfyVZc7Y5M4cPOuAWiAkcqwvsgOmcP7xwflzx06FQXaZix6fXgheFqsB7leTMTUaL3BUd06Jq0RpzZnBPxs1weOoD%2FLCL%2BfAzBLUPaUDxzZMjKPwFAwG65TOo%2F2J2E5wW0YxpJzZ3SOXy%2FrSf4BtHqhFwmkuNaNl8lWFcGsLXkBLfCEZCWp9D%2FdnlSQvEHxP61Z5Fhc%2Filg%2BdxY6088Ial9uh7IR2YL5%2BCK1YV%2B66EsKHJS73H4W7KoiaOyXAgCiUj83JFCnlCRwCgOjtfm0qNTj5cv58h1g%2FDuKUWSLtdpey9zI0%2FDEeliOMqHFtv85Ekhm4unhr1LLwYTx8L%2BygHHnXJGWdqqxQsy6M%2F%2B7VfYZDtMd9KRZ3fCLUJH%2BMgwau3vtl%2B4g0nO8qi9wTyPYAPPtCAL6G8n2R4d8iaHxARuvXMZLvdZwO9HtVqJVNSJcqMJLahL0GOqUBr8M0IGJ%2FzbkamOymcaxbamslAq9EXvnsw4myRu2kHJRMckKOTFR5j%2B3FZ8D08oWSvSbNoy2YgABz5a5f0zaYIYX0ButBdVxYGrm2v%2BpUa8ZOJOdynOcomGRDdiqreeaXWRN0CqUW9IdfSfBcNnvXlXiF2x9lHqaIeqAGzc%2BtB5cJKvSJihRKgJdokhwij9uaJScJ2dcp4ZNNx426ECSCSCKN8UvM&X-Amz-Signature=bb9542e2147deab1dfe8726b80fff11ddc54eb8a00ec9764aa303526de55b5ce&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/13ad0497-05fe-4eaa-984e-707b33e14761/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RGM46IMC%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T211343Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAUaCXVzLXdlc3QtMiJHMEUCIQCKQq0sGoIaSUk3QYJgkj8nObp3jC36xvpQC80c%2BYZlCAIgMC8rW5yGq6md%2Fp4DgrOaKC81n5wXVIwZNLJWA3PpaNAq%2FwMIHhAAGgw2Mzc0MjMxODM4MDUiDJqsFe80PWXaNs9IdSrcA%2B2rSRPVe4OY%2BDlWTCR6ISDjkkLu3rexxOTmSC6JOGaDroPT0%2FICQiamyfA4Djj56QMYk0GN2k4yqSML99I9Z%2BSPjBTEE16hmAa4joaKLHgSRk3LdIDlBnF%2FFHp5OAQ5UMMEy8U8xhYKHcl05EAwp%2BDlWLJgbDdJilGe4AIJrS8X77Q1SdSy0kyyd61xfyVZc7Y5M4cPOuAWiAkcqwvsgOmcP7xwflzx06FQXaZix6fXgheFqsB7leTMTUaL3BUd06Jq0RpzZnBPxs1weOoD%2FLCL%2BfAzBLUPaUDxzZMjKPwFAwG65TOo%2F2J2E5wW0YxpJzZ3SOXy%2FrSf4BtHqhFwmkuNaNl8lWFcGsLXkBLfCEZCWp9D%2FdnlSQvEHxP61Z5Fhc%2Filg%2BdxY6088Ial9uh7IR2YL5%2BCK1YV%2B66EsKHJS73H4W7KoiaOyXAgCiUj83JFCnlCRwCgOjtfm0qNTj5cv58h1g%2FDuKUWSLtdpey9zI0%2FDEeliOMqHFtv85Ekhm4unhr1LLwYTx8L%2BygHHnXJGWdqqxQsy6M%2F%2B7VfYZDtMd9KRZ3fCLUJH%2BMgwau3vtl%2B4g0nO8qi9wTyPYAPPtCAL6G8n2R4d8iaHxARuvXMZLvdZwO9HtVqJVNSJcqMJLahL0GOqUBr8M0IGJ%2FzbkamOymcaxbamslAq9EXvnsw4myRu2kHJRMckKOTFR5j%2B3FZ8D08oWSvSbNoy2YgABz5a5f0zaYIYX0ButBdVxYGrm2v%2BpUa8ZOJOdynOcomGRDdiqreeaXWRN0CqUW9IdfSfBcNnvXlXiF2x9lHqaIeqAGzc%2BtB5cJKvSJihRKgJdokhwij9uaJScJ2dcp4ZNNx426ECSCSCKN8UvM&X-Amz-Signature=2e3739c3d3082ddfe4fc7bc283af3009c4b584dfb631d74096159007edfa6c5d&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 2. Box and Whisker Plot
A box plot shows the distribution of quantitative data in a way that facilitates comparisons between variables or across levels of a categorical variable. The box shows the quartiles of the dataset while the whiskers extend to show the rest of the distribution, except for points that are determined to be "outliers".
**Syntax:**
```python
sns.boxplot(x='header_1', y='header_2', data=df)
```
**Example Output:**


![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d207ae92-0a7c-4e2f-aa65-0ee5a2c33bf7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZIYEOOXY%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T211344Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAUaCXVzLXdlc3QtMiJHMEUCIDi6%2FHNV1n%2BW827zQOw0g%2BwT3vUjqkQGgHK3iKkVufd%2BAiEAtvVlD7kSMhn3h7ZIza5l7bt%2FLaZ8At5Mc0wpvGcWilYq%2FwMIHhAAGgw2Mzc0MjMxODM4MDUiDOfuPsYSU%2BEEGUUQkSrcAzax7M53bOohsCHJFF4aup%2FAUdIOWt1i4NoFzAjQr%2FHNeASdPbWqou4v%2BV9daojLHc2ArKqr%2FcRy0GhTer5Hc%2FDc6DyfzQIQYbDE5RhJOmRqyjVRRw6DYL%2FnPzQ13nctwePhgCk%2BovZDt9w5owSMZzSO69BRT4a%2BjARDnZxKtJT7fv%2FSuTxOJ1sgJ7lKahNhfybXDpMkmPrZOp5sHwMDnM%2BasXgOQlBxYc9zmnHWAnUy5OJp1owtVhWGL%2F%2BcyJ6eYyTX6vZvNPu4bKmY83fRVpttD3uFWqA3wOSvUgJmtlCI2TeeU%2FsmSkQn9eXanb1W%2Bn1hJkILTc5YULNVhSrdhuNSpArxKayQN%2BddZXoXb07cJ5ifuRkZSeAktUx5qPORx16Ydt80BXo1Yc%2FX5iMKsLiYvxqfeSF3exBSaUrv9DaJ9CCLwsgdx9MQPI57K%2FbH0pdFNznUuAqiK0Zb%2F%2BaSmvjtnbkY5i39SedAS756UHFCP%2BZVC3CXy7XOO5iV713yu25CDcTwMqTAwj2Jrbgu3DYk0m9qSz5QEl6deooNXfmLrfQuAq0mLmQ58rYnwXvea%2BkLIyw4cHVtvGAl6uj8ro3LvFcfqWCTqMF%2BwSXmQ5ScalSDsR6jlfUGN79tMJTahL0GOqUBGtIQZv%2Bkx3cj4ailREfaUDutsiZypKMA9SrgbImTEF3MHXF6dquPlv7IIPOrG9dNGRG9fXfsuGbJB854xhU12jvaMWBGVJW63ATLYLZkrdLThGEm3gQJZQp%2B%2Fy%2FxdOGfMVrbffZjSLlHP6%2Fr5kccHA8pcbZMPQzY%2F%2Bg1QgqnaJYDmYCYbvg%2F%2B9SAn%2BOt7knxBTqYrfVSWcMvUUiNOV7Ny%2Frcm15O&X-Amz-Signature=af6d3d2554ec3fa3c84c95d17f135882bfbee1c699aace7090f7a1d40e9aa88a&X-Amz-SignedHeaders=host&x-id=GetObject)

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0e516edc-7551-4792-ab18-0494db3c4c0c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466W5LGEDY7%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T211344Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAUaCXVzLXdlc3QtMiJHMEUCIQCOeVNtKdxPH4ZdEmXzL%2BGj2BPC35w%2BMYsT3cz4%2Fdz9lwIgO8pFYyom7twHd5ZlMmxWivVE8XjWSYMcvmIkKXQXJEMq%2FwMIHhAAGgw2Mzc0MjMxODM4MDUiDB43VeNr4svjZAvJ8yrcA5VBYYsxFKFEMcVHzIiQC0TOJj7So4qm4D5NYPgvMgxvCr4F3dd5HMqNHG5eFZL9VAY1%2FYQ4AGL%2BuOEiN6ZPzmHl3EXAwl9%2BxpSEGr8Wc8z4P3jVsZdetWN7fMc0xy9cgMhqUD02EGP27K3vo4YF57vkz7MN%2Bz93uj8P06PXko60Aee%2BGhijpX9zaj%2B3coKhd8aGz2PYzeCD3fCOMRU4OGdJ9D9KhREmhNO78rzyfZHbV3idDw9ggorD0jm3UPV909TDWTrLq9uQkxPu2AOHOZue%2BT%2F9WCAcktfXPoBwk20WermSDtBKSW4lMbbZLjURkhKu7Pr21eD7qQJz6VrgXatQ%2BdKhssrTo3OkhYQPfUwPA9lmsuKchhdQ2O%2BrKFrJhBbCz%2F%2BwPwvqW6zorsrEK6mqYKsfDIIvFFPav2HOwbvZQ4STj5REl6S0YYRFjDAasRhvZiNyfhUyex3Y1FfCdr7HPCCOAdCLf6RXB9cJIz639G%2FgIQQAWIBmzbShOo0nVK%2F4lAF8%2FBvh7b91GoyAA%2B7IH4riz99LY%2BbKsrpbSyMA2JVhtaqR7r654fm3c%2FCbb1eKhAyyxnErCkaA%2FYNQHYsyVjTWyGAXSAVct%2FMdTDRbSypuTpmSNB9e5GcBMNHZhL0GOqUBCHETrozi9fDZwvXKx8r3oZyJzo7Z6N7LTeSipacETG0hYsT5E0bCn300HltpVwazkZcXnHMRKTJEfJgMjyy4YVr7aSCk2N%2F9%2FAtpAV3LG9S90T9vAL%2BCBMk8796BGH6kwbuL32MXytd2PVT4N62UqdrCW8xZA7ctQSsDRHAuHqrPhH%2BFl%2F2k6I8dhvQFEk8xq0JNKd86yZMrqygzU0i4ZYg3zm%2BY&X-Amz-Signature=dbbe6bc468518eabc8e9812f16d02233fc25c3ee1d72834acaeb11dd93b96af1&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23a79b9d-2356-49a9-8fd9-65c6b0ab2cc5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RGM46IMC%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T211343Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAUaCXVzLXdlc3QtMiJHMEUCIQCKQq0sGoIaSUk3QYJgkj8nObp3jC36xvpQC80c%2BYZlCAIgMC8rW5yGq6md%2Fp4DgrOaKC81n5wXVIwZNLJWA3PpaNAq%2FwMIHhAAGgw2Mzc0MjMxODM4MDUiDJqsFe80PWXaNs9IdSrcA%2B2rSRPVe4OY%2BDlWTCR6ISDjkkLu3rexxOTmSC6JOGaDroPT0%2FICQiamyfA4Djj56QMYk0GN2k4yqSML99I9Z%2BSPjBTEE16hmAa4joaKLHgSRk3LdIDlBnF%2FFHp5OAQ5UMMEy8U8xhYKHcl05EAwp%2BDlWLJgbDdJilGe4AIJrS8X77Q1SdSy0kyyd61xfyVZc7Y5M4cPOuAWiAkcqwvsgOmcP7xwflzx06FQXaZix6fXgheFqsB7leTMTUaL3BUd06Jq0RpzZnBPxs1weOoD%2FLCL%2BfAzBLUPaUDxzZMjKPwFAwG65TOo%2F2J2E5wW0YxpJzZ3SOXy%2FrSf4BtHqhFwmkuNaNl8lWFcGsLXkBLfCEZCWp9D%2FdnlSQvEHxP61Z5Fhc%2Filg%2BdxY6088Ial9uh7IR2YL5%2BCK1YV%2B66EsKHJS73H4W7KoiaOyXAgCiUj83JFCnlCRwCgOjtfm0qNTj5cv58h1g%2FDuKUWSLtdpey9zI0%2FDEeliOMqHFtv85Ekhm4unhr1LLwYTx8L%2BygHHnXJGWdqqxQsy6M%2F%2B7VfYZDtMd9KRZ3fCLUJH%2BMgwau3vtl%2B4g0nO8qi9wTyPYAPPtCAL6G8n2R4d8iaHxARuvXMZLvdZwO9HtVqJVNSJcqMJLahL0GOqUBr8M0IGJ%2FzbkamOymcaxbamslAq9EXvnsw4myRu2kHJRMckKOTFR5j%2B3FZ8D08oWSvSbNoy2YgABz5a5f0zaYIYX0ButBdVxYGrm2v%2BpUa8ZOJOdynOcomGRDdiqreeaXWRN0CqUW9IdfSfBcNnvXlXiF2x9lHqaIeqAGzc%2BtB5cJKvSJihRKgJdokhwij9uaJScJ2dcp4ZNNx426ECSCSCKN8UvM&X-Amz-Signature=004fb822f8d87e7adf3f6591e1f05977fb8ceb9f4490f6f0340f6044a7b2909a&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 4. KDE Plot
A Kernel Density Estimate (KDE) plot is a graph that creates a probability distribution curve for the data based upon its likelihood of occurrence on a specific value. This is created for a single vector of information.
**Syntax:**
```python
sns.kdeplot(X) || sns.kdeplot(df['age'])
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0d571213-2a2f-4921-a50b-880847aa05ee/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RGM46IMC%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T211343Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAUaCXVzLXdlc3QtMiJHMEUCIQCKQq0sGoIaSUk3QYJgkj8nObp3jC36xvpQC80c%2BYZlCAIgMC8rW5yGq6md%2Fp4DgrOaKC81n5wXVIwZNLJWA3PpaNAq%2FwMIHhAAGgw2Mzc0MjMxODM4MDUiDJqsFe80PWXaNs9IdSrcA%2B2rSRPVe4OY%2BDlWTCR6ISDjkkLu3rexxOTmSC6JOGaDroPT0%2FICQiamyfA4Djj56QMYk0GN2k4yqSML99I9Z%2BSPjBTEE16hmAa4joaKLHgSRk3LdIDlBnF%2FFHp5OAQ5UMMEy8U8xhYKHcl05EAwp%2BDlWLJgbDdJilGe4AIJrS8X77Q1SdSy0kyyd61xfyVZc7Y5M4cPOuAWiAkcqwvsgOmcP7xwflzx06FQXaZix6fXgheFqsB7leTMTUaL3BUd06Jq0RpzZnBPxs1weOoD%2FLCL%2BfAzBLUPaUDxzZMjKPwFAwG65TOo%2F2J2E5wW0YxpJzZ3SOXy%2FrSf4BtHqhFwmkuNaNl8lWFcGsLXkBLfCEZCWp9D%2FdnlSQvEHxP61Z5Fhc%2Filg%2BdxY6088Ial9uh7IR2YL5%2BCK1YV%2B66EsKHJS73H4W7KoiaOyXAgCiUj83JFCnlCRwCgOjtfm0qNTj5cv58h1g%2FDuKUWSLtdpey9zI0%2FDEeliOMqHFtv85Ekhm4unhr1LLwYTx8L%2BygHHnXJGWdqqxQsy6M%2F%2B7VfYZDtMd9KRZ3fCLUJH%2BMgwau3vtl%2B4g0nO8qi9wTyPYAPPtCAL6G8n2R4d8iaHxARuvXMZLvdZwO9HtVqJVNSJcqMJLahL0GOqUBr8M0IGJ%2FzbkamOymcaxbamslAq9EXvnsw4myRu2kHJRMckKOTFR5j%2B3FZ8D08oWSvSbNoy2YgABz5a5f0zaYIYX0ButBdVxYGrm2v%2BpUa8ZOJOdynOcomGRDdiqreeaXWRN0CqUW9IdfSfBcNnvXlXiF2x9lHqaIeqAGzc%2BtB5cJKvSJihRKgJdokhwij9uaJScJ2dcp4ZNNx426ECSCSCKN8UvM&X-Amz-Signature=8662572e0fd106771aa874eb46041db06e610eb496d222743c2399eb17a4c51c&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/53752550-ef82-4ca9-a01a-09921f0282d0/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RGM46IMC%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T211343Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAUaCXVzLXdlc3QtMiJHMEUCIQCKQq0sGoIaSUk3QYJgkj8nObp3jC36xvpQC80c%2BYZlCAIgMC8rW5yGq6md%2Fp4DgrOaKC81n5wXVIwZNLJWA3PpaNAq%2FwMIHhAAGgw2Mzc0MjMxODM4MDUiDJqsFe80PWXaNs9IdSrcA%2B2rSRPVe4OY%2BDlWTCR6ISDjkkLu3rexxOTmSC6JOGaDroPT0%2FICQiamyfA4Djj56QMYk0GN2k4yqSML99I9Z%2BSPjBTEE16hmAa4joaKLHgSRk3LdIDlBnF%2FFHp5OAQ5UMMEy8U8xhYKHcl05EAwp%2BDlWLJgbDdJilGe4AIJrS8X77Q1SdSy0kyyd61xfyVZc7Y5M4cPOuAWiAkcqwvsgOmcP7xwflzx06FQXaZix6fXgheFqsB7leTMTUaL3BUd06Jq0RpzZnBPxs1weOoD%2FLCL%2BfAzBLUPaUDxzZMjKPwFAwG65TOo%2F2J2E5wW0YxpJzZ3SOXy%2FrSf4BtHqhFwmkuNaNl8lWFcGsLXkBLfCEZCWp9D%2FdnlSQvEHxP61Z5Fhc%2Filg%2BdxY6088Ial9uh7IR2YL5%2BCK1YV%2B66EsKHJS73H4W7KoiaOyXAgCiUj83JFCnlCRwCgOjtfm0qNTj5cv58h1g%2FDuKUWSLtdpey9zI0%2FDEeliOMqHFtv85Ekhm4unhr1LLwYTx8L%2BygHHnXJGWdqqxQsy6M%2F%2B7VfYZDtMd9KRZ3fCLUJH%2BMgwau3vtl%2B4g0nO8qi9wTyPYAPPtCAL6G8n2R4d8iaHxARuvXMZLvdZwO9HtVqJVNSJcqMJLahL0GOqUBr8M0IGJ%2FzbkamOymcaxbamslAq9EXvnsw4myRu2kHJRMckKOTFR5j%2B3FZ8D08oWSvSbNoy2YgABz5a5f0zaYIYX0ButBdVxYGrm2v%2BpUa8ZOJOdynOcomGRDdiqreeaXWRN0CqUW9IdfSfBcNnvXlXiF2x9lHqaIeqAGzc%2BtB5cJKvSJihRKgJdokhwij9uaJScJ2dcp4ZNNx426ECSCSCKN8UvM&X-Amz-Signature=91975e7fcee1936dae3903950b75608530797d8ee23084b952e03dc2ab4f494c&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
## 4. Correlation Between Variables
Correlation is a statistical measure of the extent to which different variables are interdependent. It indicates how changes in one variable are associated with changes in another variable over time.
### Positive Correlation
Positive correlation indicates that as one variable increases, the other variable also tends to increase.
**Example: Engine Size and Price**
- **Positive Correlation:** Engine size increases, price also increases.
- **Visualization:** Scatter plot with a steep positive slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c7ea9b0-3ef3-4357-a9c3-554fc71b6b15/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UPGCC3YV%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T211344Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAUaCXVzLXdlc3QtMiJIMEYCIQCsDSTb0Bi2blxErzeginRUH2QsBiPl%2FDV8TxWlXW45bQIhAOh8rT76AzH5Pkqj3PLLNUdYltgdMi1rXP2g1Zi8aKESKv8DCB4QABoMNjM3NDIzMTgzODA1Igxhi18ZVWOTG7nF0ZIq3AP2I5acMGe2E5MqY8%2BQbXuag%2BAIumXwFrCo5%2F9jLV837nEmdVHEYnVoNNFvkcryzlla4mnhutT21hkrY8Cmxa5bp2wa5rJiUYrjyYbwbe9TKbNsjyrCTjwzhUoq4lA5Xro%2BsAxPcw6JlhbUUovLppFc0e%2Fg2ISamsgKh4nEVHgSgydUr%2BDpeHrXkuNa8GbaBlX9xR72HSVfUepfWB%2FoMby4kJyejo2tYl1mOAqGDqAJQdCyVM2xGjivOcGfYbSpC88gsT7Kwq%2BOn8e8YhD87Nv3l9xr3GsCYD5VdvuFJf%2F6l0rt8OlOqmc%2FwUitEx131GvWpwiyJ5cvGF8JJ%2B6gLO7TRmaHviRTOzz2uKAm%2FhIdC%2F%2BIAF79sMueKJXyZ10%2FBymGQUQ4oB38W%2FCcqNv60ScIIKrtWmA0n3QFV7XAiJQEeuSILTVXRLs9rdOANOCxgU73d%2FJla2Dj5%2F3FJ14ZuO%2B3DiMAddk%2FReSFsmsORu1Ty3fO3ZaGaMlm2kJlQc8prOyEn0gETDD%2FyntGJmKGOnuUajLBL3khiMgaTZ6szQUltdiSPDY3M%2BeHKo4Vl51%2BpT4K6uQOl0PV1gDdTbU0mp2Hn1gFQncyC%2FSDn3GlWTNFWcZ9khnTYN0ZxqYzezDK2YS9BjqkAUUzlSLZE6dP5iVnfBZAYZFzFCXTqwDI1o9yq%2Fy7505Zdn4oL5kHvLHVOFzTCWWFwzm8B8J3gSyQoKwPJEoF8AEkV%2FbsMPuCuelUc%2BUiThfYeUzK7mAJjfeoou9kWYJ0GkL7cvxsG3uDxsCQpIGH6CNVsPdaMQTm86Xa8cYX66LfpCuMc%2BZKzjNLtVXFOWKhRVGfZyA8qDxLf88syw3kH5FjfOW4&X-Amz-Signature=73950b18efe66f3c55e24257c8fc153d5828b56f181e7ee08ef18f731449faba&X-Amz-SignedHeaders=host&x-id=GetObject)
**Explanation:** When engine size increases, there is a corresponding increase in the price of the vehicle. This positive correlation suggests that larger engines tend to be associated with higher prices in the market.
___
### Negative Correlation
Negative correlation indicates that as one variable increases, the other variable tends to decrease.
**Example: Highway Miles per Gallon and Price**
- **Negative Correlation:** As highway miles per gallon increases, price decreases.
- **Visualization:** Scatter plot with a steep negative slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/10f1f798-9cc4-4df2-a9c1-5a339f554a0b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WFSIWFR2%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T211345Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAUaCXVzLXdlc3QtMiJIMEYCIQDdmYS0QSePUEazqbRoZJTac3HqQMAmFLXoUWSkuYNyuAIhANeZKIvMsKA%2B4oefy9XS1dHZGLdvPehdol6phfwN9RLxKv8DCB4QABoMNjM3NDIzMTgzODA1IgzL2Ie1oSOOqh4jv3Eq3APN93rRsh8hTgffm0kPjXw%2FluYA3jAH%2FgkgKTOqRO4tPcS%2FPXzHPwIw4mvejB07O7aTxoPP9su0s0aAa6q8j%2B2L%2BFHt%2Bh1IeJZwRAIaxhgL4Jun8dMIFvY6cjqkfvlJckh1VEO7feV9j%2BRk4cqhhV9zlWswJHPB6ou36J9ISACFzuL0pgCHgMv%2F%2Fgspul2U3goh8LUq%2Fdd%2BeOOsr25pDTYOa5JUzpWhf%2BdrK7qZQxzaRIA0Ao2pGUcWlZJF29caFWFvOdiRcFH9T2s5fExAg%2FI%2FYo%2FLnEeD2yZAvtZAvla6onzXq0LbbhRFmMDBIwGUF7k9AOgSrXvlSA%2FI6S1wGe1%2FzQF893hy22MGdCD1NbYncCr5yFExOuzBeGSd0nE0aRCkzCaHYMB2Mkajw2K%2BULN232v%2F5cZXRYzNDtgCqj845EeChxGmaHB7ROzCNI9w%2BSiEAm9PL4OmsjU3WECNV2MCFozL5Ixigs8eqhdj9cdJYXcKqmHoJpS%2FzuLNcvomDQRZlbaN3dReCKpyJ7N4vaaF6TZpRKjq6q0GmvL34xs%2BfG0ZIAPR26Waen%2F7YU0t%2BaTc7MSJgyang3e9%2Bvc228wmrgpHeBC6hM2qs3KW1yd2vkfeYbY1piZzjzw8vDDr2YS9BjqkAZgS%2F%2FvZ9akaGkOPfqZ0I0ace2pXk16Q54dqkEi0eue3jIzd86UsJJmj0tppTkjD59zVPdRqTo457YYqR3%2FpcntA5uSQPJtNlZYTq7HjiUdsIllDBaZqbSEtApr4G%2BptPJyxhM%2FBEXkHram%2FnIh1KQ%2BYUpgBSPnoCDHL1eTKYQ9VRX4oxjD0jgMu48acv6NfEqZWwGHMVWOLEESpzFoVRdNYOKl4&X-Amz-Signature=c92873e1f379bc94ffc8fec176dfe1b77d9d7345ab62107975c475d9a4f41d8f&X-Amz-SignedHeaders=host&x-id=GetObject)
**Explanation:** When highway miles per gallon increases, the price of the vehicle tends to decrease. This negative correlation suggests that cars with higher fuel efficiency (more miles per gallon) are generally priced lower in the market.
___
### Weak Correlation
Weak correlation indicates a lack of strong relationship between the variables.
**Example: RPM and Price**
- **Weak Correlation:** Low and high RPM values show varied prices, indicating no strong predictive relationship.
- **Visualization:** Scatter plot with no clear trend or slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9f914514-8914-4bf4-ac84-d9e3077f6eb1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZKAZCUW4%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T211344Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAUaCXVzLXdlc3QtMiJHMEUCIQDXFcApj2SGNi7zm7PAVs%2F3r6UOe%2BB1diHZiuzgbD9gBgIgbrpuCPXx0R4x9T6Mj4jhr66XhkA1yAekQl5ly1iGiGoq%2FwMIHhAAGgw2Mzc0MjMxODM4MDUiDMkFQhrim3fKFczWFyrcA%2FloHYY1IAOXhP4Ka7fqWeBH68P6LFmzQIGCnsAj%2FF10xrLfe%2FNVSfEVUYSUGbenx5Y3W3A4HFVUoSxEvKk4%2FlsaNjXG0vCYyW3BFvKHt5qsjfhgm8CyH%2BnL75sdP42sFFVBANmdyyrk%2FEWqUm%2FufIPpLrVBI%2FXJOB8FCxy3OU%2BcF7khEx4F44GY6vM01wWsR6SOpLKzPTfAcj6aDUhecK9keeu0v1Er8ujRCDUyYv46OTDCzkuFmeb9qB%2FRZxA1WU4CN2kc8UJ95HUONnbjq8%2FtCJ5PRC7iPzNK3t%2FJfAPUP2S3dwBZnwKvcaR3wNqCCfPffS3UnoighgnKKy3ryc2JFfKRlrh%2FWc0Lju%2FnQq%2BqfjEq2S%2Bqvxvdsa%2B5eT8WQ6hyGFw7O%2F9Lft4L0sZ9VbPfxo9k243BJwK%2FbpGtsCdunu4YdhCuIRHIfQ9wI%2FEdzFnqekIOYQDHcWalX%2FWe5E%2FfXd7skkehCRHtPtoZmcJYeOW4cZU3LNOWPtKDiYla6lRsdADjtlw2ow%2FnskMhZycRr9tOsD0zq%2BTqcR52HAnVXW4dywLdrPAxSscWq37Gs1tMKBVlIDZb8XCI256PrM2vs2K9Y3u3gSL%2FIg6bpblhmYpi6IfzJc7OAPbxMMbZhL0GOqUBcvjHxoqulxQLlTdbCUwA7bXIVphBFy01hErU2q64vZvZTq4B4vJa53KLnY7apqMy4ozp45fJyR4GecsfD9Ir%2FPW72bfGEt%2F0Cm1mbZ1joaesT6LIkTthkSTOF9olvjhaYsgYROxVM27MgI1JczW8yV%2BwgkGxYq1d8ucH5DVwFG6VWEfVEfsgJYrU2wIG9vuKt6CzUxhMKJYikEdWtJifx1n4umS4&X-Amz-Signature=1dbe901230c9f3e7efe2dc585fdbb5745253dc93910419cebfa904922c0704ae&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f18086e5-5b04-4fbf-8309-8944ab20d213/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QSM6KKKS%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T211344Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAUaCXVzLXdlc3QtMiJHMEUCIQDIckH2D%2BDFtVhnSM26LGlzsRKpgpuyTgdBEV5YCz5FDwIgI5AYemcMotH61IdJe3Rcq2uESjYUMD20ZAda%2FxQIcP4q%2FwMIHhAAGgw2Mzc0MjMxODM4MDUiDKuLOpSuD3gnmhwuryrcA4Vbk3%2BJLLU5A1EZjh%2Fp1p1lJJR%2Ft4HMP%2Fodo3sVPeWNCnwpGTkNvS6FWmH2oL191FDV1hL%2BhJs4nqmVAXPqa4eVdgQ8BPq8jGzQ3nwY7owceNWefIh%2BsblhX2F9gaXVqJz1%2FJBe3rVNDyRA35aK0ZSGwj6ANW51%2BX2CLHdMZrJpW7siLjn87HeDsKT6GmaL%2BmlltxLAiEXXALBKijPGGm2pVIIOsPtsTEPM5Oicu6EFENBNQMGu%2Fy0x0MgcZOIZYUVspLGEEYXzHrGviGE9o%2FUsFustALifbY3M1XbVpbaQs0QXCqom9Uzu8MV5%2BAuRzmBDNX5yXDjeXi5NDwVto63wNJxGulxhQjP7XE43xtF1ISYEtj3Gqia4nJe%2FADpu1meuzaJ8mk0uTv8RPHMEJ%2FCBwXRs%2FGQIzPjYZgs9SmKjw5j%2BaEwDWHhJLClTSaHL4GpbT3VaF6ArvCZ1c4d1XctIC54qeGbi7mFcHSLvGs9EAYAScJ%2B8drU9pTTppP09%2BoRvtEzrneU5coKqOOj1OEyuVc%2FXiMJGGKkhYMuQuwDCOrWiy6mH3o7BmBxHYBUs%2B%2FJ%2FUU6KmhV5eJm9UbgeEE5A%2FBYIynfbIC9EATi8klsXSPqec7DSc%2FoI9BsgMJHahL0GOqUBC55PLXBVRPqcMvhPU5QzrXzfB7VxUVEw2vxoup%2FWifWNdBc1R36l7nJtm%2F3dML6zhAG7fV6K2h2jPCq3AHA%2BfiWvfq42JA97Rs1FuS8TXHWKsg9aLjzm3L13%2FHlJcMKgunnabWlUnN9Uyqa4Kxdfk39FRlPm1u1cOWH7Liaos7GDi2QEb9KDked7qyVUCNI8lFSkNt%2BCA2ovvP5Q%2FYK155ncxz7k&X-Amz-Signature=d1e9d4260cd689a1a7f849cd31adba97a355730675a7e7ee9760bcd7bdf80145&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Correlation Plot
Heatmap visualizes correlations among variables. Color scheme indicates Pearson correlation coefficients. Dark red diagonal line shows perfect correlation (value of 1) between variables and themselves.
This heatmap offers overview of variable relationships and their link with price.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cd3b341e-cc1a-45f7-8aec-cdc00436d270/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QSM6KKKS%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T211344Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAUaCXVzLXdlc3QtMiJHMEUCIQDIckH2D%2BDFtVhnSM26LGlzsRKpgpuyTgdBEV5YCz5FDwIgI5AYemcMotH61IdJe3Rcq2uESjYUMD20ZAda%2FxQIcP4q%2FwMIHhAAGgw2Mzc0MjMxODM4MDUiDKuLOpSuD3gnmhwuryrcA4Vbk3%2BJLLU5A1EZjh%2Fp1p1lJJR%2Ft4HMP%2Fodo3sVPeWNCnwpGTkNvS6FWmH2oL191FDV1hL%2BhJs4nqmVAXPqa4eVdgQ8BPq8jGzQ3nwY7owceNWefIh%2BsblhX2F9gaXVqJz1%2FJBe3rVNDyRA35aK0ZSGwj6ANW51%2BX2CLHdMZrJpW7siLjn87HeDsKT6GmaL%2BmlltxLAiEXXALBKijPGGm2pVIIOsPtsTEPM5Oicu6EFENBNQMGu%2Fy0x0MgcZOIZYUVspLGEEYXzHrGviGE9o%2FUsFustALifbY3M1XbVpbaQs0QXCqom9Uzu8MV5%2BAuRzmBDNX5yXDjeXi5NDwVto63wNJxGulxhQjP7XE43xtF1ISYEtj3Gqia4nJe%2FADpu1meuzaJ8mk0uTv8RPHMEJ%2FCBwXRs%2FGQIzPjYZgs9SmKjw5j%2BaEwDWHhJLClTSaHL4GpbT3VaF6ArvCZ1c4d1XctIC54qeGbi7mFcHSLvGs9EAYAScJ%2B8drU9pTTppP09%2BoRvtEzrneU5coKqOOj1OEyuVc%2FXiMJGGKkhYMuQuwDCOrWiy6mH3o7BmBxHYBUs%2B%2FJ%2FUU6KmhV5eJm9UbgeEE5A%2FBYIynfbIC9EATi8klsXSPqec7DSc%2FoI9BsgMJHahL0GOqUBC55PLXBVRPqcMvhPU5QzrXzfB7VxUVEw2vxoup%2FWifWNdBc1R36l7nJtm%2F3dML6zhAG7fV6K2h2jPCq3AHA%2BfiWvfq42JA97Rs1FuS8TXHWKsg9aLjzm3L13%2FHlJcMKgunnabWlUnN9Uyqa4Kxdfk39FRlPm1u1cOWH7Liaos7GDi2QEb9KDked7qyVUCNI8lFSkNt%2BCA2ovvP5Q%2FYK155ncxz7k&X-Amz-Signature=b34494a44e2d113a35e752e94633546cad62f7a171fcd707a5714157c06425b2&X-Amz-SignedHeaders=host&x-id=GetObject)

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
