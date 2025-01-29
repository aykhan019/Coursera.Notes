

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7e6d594d-952e-44b6-97ea-31225882aea6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZJQZPTSC%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T191057Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAoArC%2BI0Jtc5azvRqapDNQx2L7av%2F%2B1OXOfVWPNg8xFAiEAyTuYz%2FrZNq49KjTwLNP5jlBo7UaWKl3M9f9gbOJr0KYqiAQIlP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDH%2BvP7zpxItURfVomyrcA06gljBCcjESWQTvNGL5xODbOdIZ53IhEkVB2%2FPxz626gCBaTKLVUAqKZTAedtvnzX0U5pr7AtP4xtm4twMG3UwyPfCCYM8NiGX%2BduseuQgIztdOGdgb3tX3HUwoz%2FfpNRSPhvqfTOqYXfGd9DKLG0sElcM09XL9fWfKeje6sgEp1GmHsPNFF4ZgEQYw78J0tQ3IdTxR1izHoGn9twecpt94lLdB3pKhA1N9ZcplD2TgjPkXn5BAyOMWfmuiK5BYp52Y%2Fr%2F2dom7VT4b3kHCrJuRPyXEBs3j%2FY64%2Fe%2BL0vH5Jms5bScrpilRGQXy9TXY7lQnblQniOOtD8JRoPlu5vKX2BhpqSmdSg6uqH4EWZwHhHrZ0pj7qYAJt6NePHElDjnEhmigufAQV1hPSrcg2L%2Fjn850x48%2BcLcAkJaGk2SBIivoF6pfXpctwHSwQFm3l6uJ%2F0dtMWMb4ac2xojz7wOQ2FUI3jQZKRfOfqrwDQ0LV0fJeofNzleBzFNz77fcwq6nIqXw9sAK97ne%2Beicbadjx3OOgdQ02IdwdUnJI3xw%2Fuxfl8nx1Kmf5SGCOTGqu2kUkeWPlg1qh6FPOaBsBj6dvR6YndDpJ%2BIrW5L6pBVILlabllxqexuONSlOML%2F16bwGOqUBnIRwU%2BFlueT3Di3t%2Fxy1TEl2Bq%2ByZtINPRgsiqTRmT%2BjpBk%2BLVKeAhVWo7hiFFvKXeBKF%2BX950DvBkOYNFJgUfiaBnvvrj6m25SUy22cUPwkeqIa2H0pUR3mqQyfgi326L6RRIVGjoxBljO959b7L7rJrVtoBSrtLGC4BGmk1WZSJVNQBqFBZ5rMkItrXLWcBJFw%2FBY%2FSBmiTwKP%2FjvH2%2FNBWnl0&X-Amz-Signature=09fbdabd114587db19905c7ed95e3640ebc89fcdc06ca5101d0b16ddf9caa4c4&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cbfaed9e-b398-4902-8936-dea058b21def/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZJQZPTSC%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T191057Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAoArC%2BI0Jtc5azvRqapDNQx2L7av%2F%2B1OXOfVWPNg8xFAiEAyTuYz%2FrZNq49KjTwLNP5jlBo7UaWKl3M9f9gbOJr0KYqiAQIlP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDH%2BvP7zpxItURfVomyrcA06gljBCcjESWQTvNGL5xODbOdIZ53IhEkVB2%2FPxz626gCBaTKLVUAqKZTAedtvnzX0U5pr7AtP4xtm4twMG3UwyPfCCYM8NiGX%2BduseuQgIztdOGdgb3tX3HUwoz%2FfpNRSPhvqfTOqYXfGd9DKLG0sElcM09XL9fWfKeje6sgEp1GmHsPNFF4ZgEQYw78J0tQ3IdTxR1izHoGn9twecpt94lLdB3pKhA1N9ZcplD2TgjPkXn5BAyOMWfmuiK5BYp52Y%2Fr%2F2dom7VT4b3kHCrJuRPyXEBs3j%2FY64%2Fe%2BL0vH5Jms5bScrpilRGQXy9TXY7lQnblQniOOtD8JRoPlu5vKX2BhpqSmdSg6uqH4EWZwHhHrZ0pj7qYAJt6NePHElDjnEhmigufAQV1hPSrcg2L%2Fjn850x48%2BcLcAkJaGk2SBIivoF6pfXpctwHSwQFm3l6uJ%2F0dtMWMb4ac2xojz7wOQ2FUI3jQZKRfOfqrwDQ0LV0fJeofNzleBzFNz77fcwq6nIqXw9sAK97ne%2Beicbadjx3OOgdQ02IdwdUnJI3xw%2Fuxfl8nx1Kmf5SGCOTGqu2kUkeWPlg1qh6FPOaBsBj6dvR6YndDpJ%2BIrW5L6pBVILlabllxqexuONSlOML%2F16bwGOqUBnIRwU%2BFlueT3Di3t%2Fxy1TEl2Bq%2ByZtINPRgsiqTRmT%2BjpBk%2BLVKeAhVWo7hiFFvKXeBKF%2BX950DvBkOYNFJgUfiaBnvvrj6m25SUy22cUPwkeqIa2H0pUR3mqQyfgi326L6RRIVGjoxBljO959b7L7rJrVtoBSrtLGC4BGmk1WZSJVNQBqFBZ5rMkItrXLWcBJFw%2FBY%2FSBmiTwKP%2FjvH2%2FNBWnl0&X-Amz-Signature=52ea2bf00f3acad798c9815a2db8df1093210c25597b9085a35e9175b78a3ae4&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/91181646-b1e0-4433-9711-6259a96a9247/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZJQZPTSC%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T191057Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAoArC%2BI0Jtc5azvRqapDNQx2L7av%2F%2B1OXOfVWPNg8xFAiEAyTuYz%2FrZNq49KjTwLNP5jlBo7UaWKl3M9f9gbOJr0KYqiAQIlP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDH%2BvP7zpxItURfVomyrcA06gljBCcjESWQTvNGL5xODbOdIZ53IhEkVB2%2FPxz626gCBaTKLVUAqKZTAedtvnzX0U5pr7AtP4xtm4twMG3UwyPfCCYM8NiGX%2BduseuQgIztdOGdgb3tX3HUwoz%2FfpNRSPhvqfTOqYXfGd9DKLG0sElcM09XL9fWfKeje6sgEp1GmHsPNFF4ZgEQYw78J0tQ3IdTxR1izHoGn9twecpt94lLdB3pKhA1N9ZcplD2TgjPkXn5BAyOMWfmuiK5BYp52Y%2Fr%2F2dom7VT4b3kHCrJuRPyXEBs3j%2FY64%2Fe%2BL0vH5Jms5bScrpilRGQXy9TXY7lQnblQniOOtD8JRoPlu5vKX2BhpqSmdSg6uqH4EWZwHhHrZ0pj7qYAJt6NePHElDjnEhmigufAQV1hPSrcg2L%2Fjn850x48%2BcLcAkJaGk2SBIivoF6pfXpctwHSwQFm3l6uJ%2F0dtMWMb4ac2xojz7wOQ2FUI3jQZKRfOfqrwDQ0LV0fJeofNzleBzFNz77fcwq6nIqXw9sAK97ne%2Beicbadjx3OOgdQ02IdwdUnJI3xw%2Fuxfl8nx1Kmf5SGCOTGqu2kUkeWPlg1qh6FPOaBsBj6dvR6YndDpJ%2BIrW5L6pBVILlabllxqexuONSlOML%2F16bwGOqUBnIRwU%2BFlueT3Di3t%2Fxy1TEl2Bq%2ByZtINPRgsiqTRmT%2BjpBk%2BLVKeAhVWo7hiFFvKXeBKF%2BX950DvBkOYNFJgUfiaBnvvrj6m25SUy22cUPwkeqIa2H0pUR3mqQyfgi326L6RRIVGjoxBljO959b7L7rJrVtoBSrtLGC4BGmk1WZSJVNQBqFBZ5rMkItrXLWcBJFw%2FBY%2FSBmiTwKP%2FjvH2%2FNBWnl0&X-Amz-Signature=ea38a82bc52ace12d1d3a1ee1c178d04ed337b19dfb3f19595cadde5ae7e5612&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/09aba1c0-0d55-41dd-852a-a04c5b8a3fac/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667WDC76QX%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T191058Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCVc3%2BPkRc9VPr4sVIuTiRL3TTL8jVIA2TIJ9He0qgyaAIhAI%2B6E9AbpxZC1bX%2Bl%2B0cAWWIoeLJbLD6OuoM%2FVJP5f8yKogECJT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzieGFY%2Fwirb3F4VxEq3ANjPs6dh0%2Fq4WWEnnAcvO4AGAtPcNpm%2FS1DwjfuYQ5PiLALqriR3JQ5CvhdyR7VXXdMOzb%2FO%2FuZt6Z1TudK1t6wy4ZL8%2BoxDEuDdotzy48Ck1AwH2J2Gf90fuUjXg7%2F0KAONSILmJARRye5XLGdAXdkhZ%2F1hR%2B042%2FD2BavyzKKTvdSKMqpEEgYmQZfH4sDyq2%2BYl4AU64%2BtkTawIt6b1WWG2b4YVNZJorR%2Fsgx7roytk1q2opoXxtjgCHbQTD7u5A8j4FsP446L9kTtY7EaPx%2F9TCDc1qArmy798nUB0meA9nmT03G0jlMXUaLuv5m4h2khUmvku6gFnqNDb7X%2F6lMVsXtXsDivRokeCX%2FkvLT09POTF9wC0EuGRYKaueSF1iiJ4zHMZuzPsdl6VwK86lGOLWW2vRV2lHzBOB1SV0ZJf%2FJPNVxuQbsO1qI1chc6fhl31k81x8nLKhV9HPSJsS22Q4Xj%2BW9vr5okR9Yp%2FzMGeW6yVn6Ense7ZhupBLW4sDKEcBpKpDirrjWRGntW6GXlGspLaA%2F%2BEbuxRF0i51aRKBUyXfDTjc1R49I5%2FpJD8rXaszC5btXsC7eq%2BKGDybpdg9yL0Tr2HhF6JmzVrGIRYznvry817T%2BUXf5vzC%2F9em8BjqkARrIKCRfDY%2FGV67d11WUDCi6joDdQhkC4IbWwjcvxVD6KJXsM%2FVxi2rrAk4UaMcuO2z5%2FrijLGVURG2tBD1%2FTEgr0pcL%2FFAU7H4SECNeRdOPl6B%2BeANNnX%2Bb9OxywM%2B4zFI5bLVERofwqCyF50sLaJOiK0EM8XheqwNfuCJvc7aS8mmmz%2BVeDJl9PSZc8V6PdStxihXbItlIo3an8Bqdy9hT8uEw&X-Amz-Signature=feadee1801d27c1585b2a022f654c98fa358df61cb9becad552c8899ce796faf&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 2. Scatter Plot
Scatter plots present the relationship between two variables in a dataset. It represents data points on a two-dimensional plane. The independent variable or attribute is plotted on the X-axis, while the dependent variable is plotted on the Y-axis.
**Syntax:**
```python
plt.scatter(x, y)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23708af9-659f-4f23-b626-1a4292d7842c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667WDC76QX%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T191058Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCVc3%2BPkRc9VPr4sVIuTiRL3TTL8jVIA2TIJ9He0qgyaAIhAI%2B6E9AbpxZC1bX%2Bl%2B0cAWWIoeLJbLD6OuoM%2FVJP5f8yKogECJT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzieGFY%2Fwirb3F4VxEq3ANjPs6dh0%2Fq4WWEnnAcvO4AGAtPcNpm%2FS1DwjfuYQ5PiLALqriR3JQ5CvhdyR7VXXdMOzb%2FO%2FuZt6Z1TudK1t6wy4ZL8%2BoxDEuDdotzy48Ck1AwH2J2Gf90fuUjXg7%2F0KAONSILmJARRye5XLGdAXdkhZ%2F1hR%2B042%2FD2BavyzKKTvdSKMqpEEgYmQZfH4sDyq2%2BYl4AU64%2BtkTawIt6b1WWG2b4YVNZJorR%2Fsgx7roytk1q2opoXxtjgCHbQTD7u5A8j4FsP446L9kTtY7EaPx%2F9TCDc1qArmy798nUB0meA9nmT03G0jlMXUaLuv5m4h2khUmvku6gFnqNDb7X%2F6lMVsXtXsDivRokeCX%2FkvLT09POTF9wC0EuGRYKaueSF1iiJ4zHMZuzPsdl6VwK86lGOLWW2vRV2lHzBOB1SV0ZJf%2FJPNVxuQbsO1qI1chc6fhl31k81x8nLKhV9HPSJsS22Q4Xj%2BW9vr5okR9Yp%2FzMGeW6yVn6Ense7ZhupBLW4sDKEcBpKpDirrjWRGntW6GXlGspLaA%2F%2BEbuxRF0i51aRKBUyXfDTjc1R49I5%2FpJD8rXaszC5btXsC7eq%2BKGDybpdg9yL0Tr2HhF6JmzVrGIRYznvry817T%2BUXf5vzC%2F9em8BjqkARrIKCRfDY%2FGV67d11WUDCi6joDdQhkC4IbWwjcvxVD6KJXsM%2FVxi2rrAk4UaMcuO2z5%2FrijLGVURG2tBD1%2FTEgr0pcL%2FFAU7H4SECNeRdOPl6B%2BeANNnX%2Bb9OxywM%2B4zFI5bLVERofwqCyF50sLaJOiK0EM8XheqwNfuCJvc7aS8mmmz%2BVeDJl9PSZc8V6PdStxihXbItlIo3an8Bqdy9hT8uEw&X-Amz-Signature=8b483fe78a47a56eb6bc90b2d34fb9eb8b4426b200d6b16ec41e209eaf300136&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 3. Histogram
A histogram is an important visual representation of data in categorical form. To view the data in a "Binned" form, use the histogram plot with a number of bins required or with the data points that mark the bin edges. The x-axis represents the data bins, and the y-axis represents the number of elements in each bin.
**Syntax:**
```python
plt.hist(x, bins)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/24e4424a-df87-40a1-b63b-195cbdc2e0ab/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667WDC76QX%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T191058Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCVc3%2BPkRc9VPr4sVIuTiRL3TTL8jVIA2TIJ9He0qgyaAIhAI%2B6E9AbpxZC1bX%2Bl%2B0cAWWIoeLJbLD6OuoM%2FVJP5f8yKogECJT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzieGFY%2Fwirb3F4VxEq3ANjPs6dh0%2Fq4WWEnnAcvO4AGAtPcNpm%2FS1DwjfuYQ5PiLALqriR3JQ5CvhdyR7VXXdMOzb%2FO%2FuZt6Z1TudK1t6wy4ZL8%2BoxDEuDdotzy48Ck1AwH2J2Gf90fuUjXg7%2F0KAONSILmJARRye5XLGdAXdkhZ%2F1hR%2B042%2FD2BavyzKKTvdSKMqpEEgYmQZfH4sDyq2%2BYl4AU64%2BtkTawIt6b1WWG2b4YVNZJorR%2Fsgx7roytk1q2opoXxtjgCHbQTD7u5A8j4FsP446L9kTtY7EaPx%2F9TCDc1qArmy798nUB0meA9nmT03G0jlMXUaLuv5m4h2khUmvku6gFnqNDb7X%2F6lMVsXtXsDivRokeCX%2FkvLT09POTF9wC0EuGRYKaueSF1iiJ4zHMZuzPsdl6VwK86lGOLWW2vRV2lHzBOB1SV0ZJf%2FJPNVxuQbsO1qI1chc6fhl31k81x8nLKhV9HPSJsS22Q4Xj%2BW9vr5okR9Yp%2FzMGeW6yVn6Ense7ZhupBLW4sDKEcBpKpDirrjWRGntW6GXlGspLaA%2F%2BEbuxRF0i51aRKBUyXfDTjc1R49I5%2FpJD8rXaszC5btXsC7eq%2BKGDybpdg9yL0Tr2HhF6JmzVrGIRYznvry817T%2BUXf5vzC%2F9em8BjqkARrIKCRfDY%2FGV67d11WUDCi6joDdQhkC4IbWwjcvxVD6KJXsM%2FVxi2rrAk4UaMcuO2z5%2FrijLGVURG2tBD1%2FTEgr0pcL%2FFAU7H4SECNeRdOPl6B%2BeANNnX%2Bb9OxywM%2B4zFI5bLVERofwqCyF50sLaJOiK0EM8XheqwNfuCJvc7aS8mmmz%2BVeDJl9PSZc8V6PdStxihXbItlIo3an8Bqdy9hT8uEw&X-Amz-Signature=4f94b7061e96665d7dd0d12e613c2cce667497433f2d0a038784e7e4dc026f15&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ab5a6dfe-51f5-43ee-bcb3-33dae4a1c7ad/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667WDC76QX%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T191058Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCVc3%2BPkRc9VPr4sVIuTiRL3TTL8jVIA2TIJ9He0qgyaAIhAI%2B6E9AbpxZC1bX%2Bl%2B0cAWWIoeLJbLD6OuoM%2FVJP5f8yKogECJT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzieGFY%2Fwirb3F4VxEq3ANjPs6dh0%2Fq4WWEnnAcvO4AGAtPcNpm%2FS1DwjfuYQ5PiLALqriR3JQ5CvhdyR7VXXdMOzb%2FO%2FuZt6Z1TudK1t6wy4ZL8%2BoxDEuDdotzy48Ck1AwH2J2Gf90fuUjXg7%2F0KAONSILmJARRye5XLGdAXdkhZ%2F1hR%2B042%2FD2BavyzKKTvdSKMqpEEgYmQZfH4sDyq2%2BYl4AU64%2BtkTawIt6b1WWG2b4YVNZJorR%2Fsgx7roytk1q2opoXxtjgCHbQTD7u5A8j4FsP446L9kTtY7EaPx%2F9TCDc1qArmy798nUB0meA9nmT03G0jlMXUaLuv5m4h2khUmvku6gFnqNDb7X%2F6lMVsXtXsDivRokeCX%2FkvLT09POTF9wC0EuGRYKaueSF1iiJ4zHMZuzPsdl6VwK86lGOLWW2vRV2lHzBOB1SV0ZJf%2FJPNVxuQbsO1qI1chc6fhl31k81x8nLKhV9HPSJsS22Q4Xj%2BW9vr5okR9Yp%2FzMGeW6yVn6Ense7ZhupBLW4sDKEcBpKpDirrjWRGntW6GXlGspLaA%2F%2BEbuxRF0i51aRKBUyXfDTjc1R49I5%2FpJD8rXaszC5btXsC7eq%2BKGDybpdg9yL0Tr2HhF6JmzVrGIRYznvry817T%2BUXf5vzC%2F9em8BjqkARrIKCRfDY%2FGV67d11WUDCi6joDdQhkC4IbWwjcvxVD6KJXsM%2FVxi2rrAk4UaMcuO2z5%2FrijLGVURG2tBD1%2FTEgr0pcL%2FFAU7H4SECNeRdOPl6B%2BeANNnX%2Bb9OxywM%2B4zFI5bLVERofwqCyF50sLaJOiK0EM8XheqwNfuCJvc7aS8mmmz%2BVeDJl9PSZc8V6PdStxihXbItlIo3an8Bqdy9hT8uEw&X-Amz-Signature=03e1f45e6240687828889a36194aeb6f1e40955f44eed75c0d8346b3835e2d2f&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8f1b1d60-cf1b-42b3-9faa-f634c89c3f84/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667WDC76QX%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T191058Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCVc3%2BPkRc9VPr4sVIuTiRL3TTL8jVIA2TIJ9He0qgyaAIhAI%2B6E9AbpxZC1bX%2Bl%2B0cAWWIoeLJbLD6OuoM%2FVJP5f8yKogECJT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzieGFY%2Fwirb3F4VxEq3ANjPs6dh0%2Fq4WWEnnAcvO4AGAtPcNpm%2FS1DwjfuYQ5PiLALqriR3JQ5CvhdyR7VXXdMOzb%2FO%2FuZt6Z1TudK1t6wy4ZL8%2BoxDEuDdotzy48Ck1AwH2J2Gf90fuUjXg7%2F0KAONSILmJARRye5XLGdAXdkhZ%2F1hR%2B042%2FD2BavyzKKTvdSKMqpEEgYmQZfH4sDyq2%2BYl4AU64%2BtkTawIt6b1WWG2b4YVNZJorR%2Fsgx7roytk1q2opoXxtjgCHbQTD7u5A8j4FsP446L9kTtY7EaPx%2F9TCDc1qArmy798nUB0meA9nmT03G0jlMXUaLuv5m4h2khUmvku6gFnqNDb7X%2F6lMVsXtXsDivRokeCX%2FkvLT09POTF9wC0EuGRYKaueSF1iiJ4zHMZuzPsdl6VwK86lGOLWW2vRV2lHzBOB1SV0ZJf%2FJPNVxuQbsO1qI1chc6fhl31k81x8nLKhV9HPSJsS22Q4Xj%2BW9vr5okR9Yp%2FzMGeW6yVn6Ense7ZhupBLW4sDKEcBpKpDirrjWRGntW6GXlGspLaA%2F%2BEbuxRF0i51aRKBUyXfDTjc1R49I5%2FpJD8rXaszC5btXsC7eq%2BKGDybpdg9yL0Tr2HhF6JmzVrGIRYznvry817T%2BUXf5vzC%2F9em8BjqkARrIKCRfDY%2FGV67d11WUDCi6joDdQhkC4IbWwjcvxVD6KJXsM%2FVxi2rrAk4UaMcuO2z5%2FrijLGVURG2tBD1%2FTEgr0pcL%2FFAU7H4SECNeRdOPl6B%2BeANNnX%2Bb9OxywM%2B4zFI5bLVERofwqCyF50sLaJOiK0EM8XheqwNfuCJvc7aS8mmmz%2BVeDJl9PSZc8V6PdStxihXbItlIo3an8Bqdy9hT8uEw&X-Amz-Signature=23d94f6ed413f5e15cd10440666df350102bded4ee531ecb53ca05c51b5e3517&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/13ad0497-05fe-4eaa-984e-707b33e14761/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667WDC76QX%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T191058Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCVc3%2BPkRc9VPr4sVIuTiRL3TTL8jVIA2TIJ9He0qgyaAIhAI%2B6E9AbpxZC1bX%2Bl%2B0cAWWIoeLJbLD6OuoM%2FVJP5f8yKogECJT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzieGFY%2Fwirb3F4VxEq3ANjPs6dh0%2Fq4WWEnnAcvO4AGAtPcNpm%2FS1DwjfuYQ5PiLALqriR3JQ5CvhdyR7VXXdMOzb%2FO%2FuZt6Z1TudK1t6wy4ZL8%2BoxDEuDdotzy48Ck1AwH2J2Gf90fuUjXg7%2F0KAONSILmJARRye5XLGdAXdkhZ%2F1hR%2B042%2FD2BavyzKKTvdSKMqpEEgYmQZfH4sDyq2%2BYl4AU64%2BtkTawIt6b1WWG2b4YVNZJorR%2Fsgx7roytk1q2opoXxtjgCHbQTD7u5A8j4FsP446L9kTtY7EaPx%2F9TCDc1qArmy798nUB0meA9nmT03G0jlMXUaLuv5m4h2khUmvku6gFnqNDb7X%2F6lMVsXtXsDivRokeCX%2FkvLT09POTF9wC0EuGRYKaueSF1iiJ4zHMZuzPsdl6VwK86lGOLWW2vRV2lHzBOB1SV0ZJf%2FJPNVxuQbsO1qI1chc6fhl31k81x8nLKhV9HPSJsS22Q4Xj%2BW9vr5okR9Yp%2FzMGeW6yVn6Ense7ZhupBLW4sDKEcBpKpDirrjWRGntW6GXlGspLaA%2F%2BEbuxRF0i51aRKBUyXfDTjc1R49I5%2FpJD8rXaszC5btXsC7eq%2BKGDybpdg9yL0Tr2HhF6JmzVrGIRYznvry817T%2BUXf5vzC%2F9em8BjqkARrIKCRfDY%2FGV67d11WUDCi6joDdQhkC4IbWwjcvxVD6KJXsM%2FVxi2rrAk4UaMcuO2z5%2FrijLGVURG2tBD1%2FTEgr0pcL%2FFAU7H4SECNeRdOPl6B%2BeANNnX%2Bb9OxywM%2B4zFI5bLVERofwqCyF50sLaJOiK0EM8XheqwNfuCJvc7aS8mmmz%2BVeDJl9PSZc8V6PdStxihXbItlIo3an8Bqdy9hT8uEw&X-Amz-Signature=c94985967b70803212e2dda5c2f665d48526672cd1c142b2d778c1308f572069&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 2. Box and Whisker Plot
A box plot shows the distribution of quantitative data in a way that facilitates comparisons between variables or across levels of a categorical variable. The box shows the quartiles of the dataset while the whiskers extend to show the rest of the distribution, except for points that are determined to be "outliers".
**Syntax:**
```python
sns.boxplot(x='header_1', y='header_2', data=df)
```
**Example Output:**


![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d207ae92-0a7c-4e2f-aa65-0ee5a2c33bf7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TI6KG6NA%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T191059Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCL95A8MBW7UeCFK%2FnHOOW%2FCOzGKV4H%2BjVHeLrjXZxCQQIgC57lHgPBDtfGxQihttQ5jDW5cJlf%2BRSOgyRAhM6sohwqiAQIlP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHl8dQIm605m%2FqrzZSrcA5POq%2B%2BnyqAWmHCH%2BY%2FhXYjcyqV4CVfIERKEp0b2TPzezUpYLL3yDNmuLtymlk2RfFxrv%2BFD%2Bq%2FuyTyGf%2FZBVS%2BGqj3YA2qvG60i%2FMbcgu7HrozGV3azrLKuerG47YAaFP0zdXHAtrXC2z7bLCAcVcCGnptLffhv0wPJIuHMTrnDsqdPm0iYwk6PUTlwpE3elvP40X0Ki3n9OqIyDRMs7rqRPsCXctfZLSziSqXmmoOKx89rXhP6TLZy2qVmN4TfMg7FLVIpraQPfDd%2B6Xq9zeiGP%2FUxoTcDjdij1bvu9zooMyQ5iIYzGNmaoTMlc%2FyhV%2B4CCYeiod00Khd0dlqYYqmo16TMkQDOycmTyKFuIfHb6TDEtpB2G9f65K4VYMlq7jE%2FeNmsqCzpkVpUXw2PczIDeDuEz%2By6vEBmtW4K3RKCTVXKrNnjeQ5YvwzDd%2BJNqAHxhMZQRJil5Iu4uLrM96nRngH4SdgBH1wY74L1i%2FGSYDHTLuhjOcQ%2BdXnPc%2FQO0WrnBQzgR6DHMhGYLJuMN5IgHc8hju1I88DLzvb0A0tiC%2BlWRLAqmhURRgdqRgJ%2FCS0WOmAL8H85Fk%2FiqMP0ysd3SVoeg9DEEQ6Ncv5k3ZERRw4kQ4dYcUCcz4T7MI316bwGOqUBtdqxl%2FWYHlB4%2B12JLU8VN6U9UjobnAUx6OxukH0XQFYJgzr9k3poeszWFt%2Fs44YEQME6t%2Fbm6F%2BDt6ban1ux%2BlJwPMVg3qo%2Fjpmlu7V74xc5Q2gH4oWpFMo37K%2BHrLz5%2BbPyN0NQwZQMhRNKgJ3CgtOgWDHRSdWAT2K6XOwqlf7LQRveWWgEONPbULLht7Plk4ouu2X%2BxYYctiS2zH%2B35yExyM63&X-Amz-Signature=fa1ffe6178858f9096987dab685bc4352ea987b0d4b8fdec3c3d6c2151cb6aa8&X-Amz-SignedHeaders=host&x-id=GetObject)

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0e516edc-7551-4792-ab18-0494db3c4c0c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TMCSZFBX%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T191059Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHvlWCaMj6rQPlXvW3YXXHnCBW4xfqiKAdw3Tp9CXnbYAiBZsfENxDCJVfArKasbXdaa%2Fi6Zx8S5iwx0hlDxNkOkoSqIBAiU%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMTcHXkidtFtMY%2FfkpKtwDWNHxmb1q8JI9zQXiCb5Jn0vEqycCRdA3qYC7rd7LMW7z0QFQgNc0%2BpzI%2FJ97HfyenxMDLynQ9KuxojtB2BrxvgLL1X5RMt3X8n5o6BeZ43zzCpt8Sle3ND6%2F0%2BNYXrM9YHffWEAot4B4Etz8bnmWhuF5THab6UW7Xjm4RHidtbWmV65Llb66%2F5zfG3I76bkan%2BbiijjZncqSukZteLNgtK4BBypnNfY8BX5rz5IpE15AEa7ZJvHWX2Gcpq8EzsmY6Hibdl9bbSIq5XjKDl47LUdt%2B20%2BjLWYzRZru9fBYA9ngqcpg%2BJUQfR70yA5KcoDr7edu01I%2BznAHSt3jD5sZPkYNEQ%2FXgJrajDxO%2FGG2c%2BxoNALNFLRerPZhLBjX4aipt%2BalL5nQhc4EnUdpje8KI%2BQM4tJJjSouDsvyNJ3VeDFmNvin5VEahQ3D7U9Hu48zc72s3EE5ynHUIWlM6M%2F4yIiPX0BCdkvkI5STL%2F9ecNAf7TpBedPJ%2Bmtbe%2BPd9pKV1EBDWv8TK%2BwMOlG7NFNpoBV8gTIQ2o1gDr9utWxH%2BmGpwM1pPYqgefue2yKKDtK%2BaGfo%2BWjhK5KdJRujEgq9hMNEkyRybrc%2BqYeqPEWLmEJJoD2lJLXdYd4hfAwzvXpvAY6pgFG%2BpLfWoy0oGrUwkNZmAu20txhWwfoToqZNSM%2Fxf5uQudWTTImuRDy0aV0OhQeVE7sBwXoIcRjJKRU7yp57A6fNXq0UYphlWIZsQ0xbPOR%2Fo753qAjDi1jsVz48Nx5%2FtrdA05hg2Dm5Sw0AlXLLXiq7FKbyzmSD2U4B2PDe%2BlGNyYPDQclYDr860G6ctFDocuGZbXNqy3jUfFM%2F4BDEQWymR7%2BmZVf&X-Amz-Signature=91101a9c6bd77147745bffd05e2debc5cdaea6991c948fa37352aa9f6cab0047&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23a79b9d-2356-49a9-8fd9-65c6b0ab2cc5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667WDC76QX%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T191058Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCVc3%2BPkRc9VPr4sVIuTiRL3TTL8jVIA2TIJ9He0qgyaAIhAI%2B6E9AbpxZC1bX%2Bl%2B0cAWWIoeLJbLD6OuoM%2FVJP5f8yKogECJT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzieGFY%2Fwirb3F4VxEq3ANjPs6dh0%2Fq4WWEnnAcvO4AGAtPcNpm%2FS1DwjfuYQ5PiLALqriR3JQ5CvhdyR7VXXdMOzb%2FO%2FuZt6Z1TudK1t6wy4ZL8%2BoxDEuDdotzy48Ck1AwH2J2Gf90fuUjXg7%2F0KAONSILmJARRye5XLGdAXdkhZ%2F1hR%2B042%2FD2BavyzKKTvdSKMqpEEgYmQZfH4sDyq2%2BYl4AU64%2BtkTawIt6b1WWG2b4YVNZJorR%2Fsgx7roytk1q2opoXxtjgCHbQTD7u5A8j4FsP446L9kTtY7EaPx%2F9TCDc1qArmy798nUB0meA9nmT03G0jlMXUaLuv5m4h2khUmvku6gFnqNDb7X%2F6lMVsXtXsDivRokeCX%2FkvLT09POTF9wC0EuGRYKaueSF1iiJ4zHMZuzPsdl6VwK86lGOLWW2vRV2lHzBOB1SV0ZJf%2FJPNVxuQbsO1qI1chc6fhl31k81x8nLKhV9HPSJsS22Q4Xj%2BW9vr5okR9Yp%2FzMGeW6yVn6Ense7ZhupBLW4sDKEcBpKpDirrjWRGntW6GXlGspLaA%2F%2BEbuxRF0i51aRKBUyXfDTjc1R49I5%2FpJD8rXaszC5btXsC7eq%2BKGDybpdg9yL0Tr2HhF6JmzVrGIRYznvry817T%2BUXf5vzC%2F9em8BjqkARrIKCRfDY%2FGV67d11WUDCi6joDdQhkC4IbWwjcvxVD6KJXsM%2FVxi2rrAk4UaMcuO2z5%2FrijLGVURG2tBD1%2FTEgr0pcL%2FFAU7H4SECNeRdOPl6B%2BeANNnX%2Bb9OxywM%2B4zFI5bLVERofwqCyF50sLaJOiK0EM8XheqwNfuCJvc7aS8mmmz%2BVeDJl9PSZc8V6PdStxihXbItlIo3an8Bqdy9hT8uEw&X-Amz-Signature=7274c4601cf275afcc7d74d4766190bac74000793ba9d753c168a1bf9fc26f71&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 4. KDE Plot
A Kernel Density Estimate (KDE) plot is a graph that creates a probability distribution curve for the data based upon its likelihood of occurrence on a specific value. This is created for a single vector of information.
**Syntax:**
```python
sns.kdeplot(X) || sns.kdeplot(df['age'])
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0d571213-2a2f-4921-a50b-880847aa05ee/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667WDC76QX%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T191058Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCVc3%2BPkRc9VPr4sVIuTiRL3TTL8jVIA2TIJ9He0qgyaAIhAI%2B6E9AbpxZC1bX%2Bl%2B0cAWWIoeLJbLD6OuoM%2FVJP5f8yKogECJT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzieGFY%2Fwirb3F4VxEq3ANjPs6dh0%2Fq4WWEnnAcvO4AGAtPcNpm%2FS1DwjfuYQ5PiLALqriR3JQ5CvhdyR7VXXdMOzb%2FO%2FuZt6Z1TudK1t6wy4ZL8%2BoxDEuDdotzy48Ck1AwH2J2Gf90fuUjXg7%2F0KAONSILmJARRye5XLGdAXdkhZ%2F1hR%2B042%2FD2BavyzKKTvdSKMqpEEgYmQZfH4sDyq2%2BYl4AU64%2BtkTawIt6b1WWG2b4YVNZJorR%2Fsgx7roytk1q2opoXxtjgCHbQTD7u5A8j4FsP446L9kTtY7EaPx%2F9TCDc1qArmy798nUB0meA9nmT03G0jlMXUaLuv5m4h2khUmvku6gFnqNDb7X%2F6lMVsXtXsDivRokeCX%2FkvLT09POTF9wC0EuGRYKaueSF1iiJ4zHMZuzPsdl6VwK86lGOLWW2vRV2lHzBOB1SV0ZJf%2FJPNVxuQbsO1qI1chc6fhl31k81x8nLKhV9HPSJsS22Q4Xj%2BW9vr5okR9Yp%2FzMGeW6yVn6Ense7ZhupBLW4sDKEcBpKpDirrjWRGntW6GXlGspLaA%2F%2BEbuxRF0i51aRKBUyXfDTjc1R49I5%2FpJD8rXaszC5btXsC7eq%2BKGDybpdg9yL0Tr2HhF6JmzVrGIRYznvry817T%2BUXf5vzC%2F9em8BjqkARrIKCRfDY%2FGV67d11WUDCi6joDdQhkC4IbWwjcvxVD6KJXsM%2FVxi2rrAk4UaMcuO2z5%2FrijLGVURG2tBD1%2FTEgr0pcL%2FFAU7H4SECNeRdOPl6B%2BeANNnX%2Bb9OxywM%2B4zFI5bLVERofwqCyF50sLaJOiK0EM8XheqwNfuCJvc7aS8mmmz%2BVeDJl9PSZc8V6PdStxihXbItlIo3an8Bqdy9hT8uEw&X-Amz-Signature=09a5d1e9b613f8ec420582d5dde74f16fb4403702b97cb9a3e089a394f74c28a&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/53752550-ef82-4ca9-a01a-09921f0282d0/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667WDC76QX%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T191058Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCVc3%2BPkRc9VPr4sVIuTiRL3TTL8jVIA2TIJ9He0qgyaAIhAI%2B6E9AbpxZC1bX%2Bl%2B0cAWWIoeLJbLD6OuoM%2FVJP5f8yKogECJT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzieGFY%2Fwirb3F4VxEq3ANjPs6dh0%2Fq4WWEnnAcvO4AGAtPcNpm%2FS1DwjfuYQ5PiLALqriR3JQ5CvhdyR7VXXdMOzb%2FO%2FuZt6Z1TudK1t6wy4ZL8%2BoxDEuDdotzy48Ck1AwH2J2Gf90fuUjXg7%2F0KAONSILmJARRye5XLGdAXdkhZ%2F1hR%2B042%2FD2BavyzKKTvdSKMqpEEgYmQZfH4sDyq2%2BYl4AU64%2BtkTawIt6b1WWG2b4YVNZJorR%2Fsgx7roytk1q2opoXxtjgCHbQTD7u5A8j4FsP446L9kTtY7EaPx%2F9TCDc1qArmy798nUB0meA9nmT03G0jlMXUaLuv5m4h2khUmvku6gFnqNDb7X%2F6lMVsXtXsDivRokeCX%2FkvLT09POTF9wC0EuGRYKaueSF1iiJ4zHMZuzPsdl6VwK86lGOLWW2vRV2lHzBOB1SV0ZJf%2FJPNVxuQbsO1qI1chc6fhl31k81x8nLKhV9HPSJsS22Q4Xj%2BW9vr5okR9Yp%2FzMGeW6yVn6Ense7ZhupBLW4sDKEcBpKpDirrjWRGntW6GXlGspLaA%2F%2BEbuxRF0i51aRKBUyXfDTjc1R49I5%2FpJD8rXaszC5btXsC7eq%2BKGDybpdg9yL0Tr2HhF6JmzVrGIRYznvry817T%2BUXf5vzC%2F9em8BjqkARrIKCRfDY%2FGV67d11WUDCi6joDdQhkC4IbWwjcvxVD6KJXsM%2FVxi2rrAk4UaMcuO2z5%2FrijLGVURG2tBD1%2FTEgr0pcL%2FFAU7H4SECNeRdOPl6B%2BeANNnX%2Bb9OxywM%2B4zFI5bLVERofwqCyF50sLaJOiK0EM8XheqwNfuCJvc7aS8mmmz%2BVeDJl9PSZc8V6PdStxihXbItlIo3an8Bqdy9hT8uEw&X-Amz-Signature=97789074c3eda4ab990fcfa932bcc6ef8a0d0f2acfc99f507369441a8b221295&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
## 4. Correlation Between Variables
Correlation is a statistical measure of the extent to which different variables are interdependent. It indicates how changes in one variable are associated with changes in another variable over time.
### Positive Correlation
Positive correlation indicates that as one variable increases, the other variable also tends to increase.
**Example: Engine Size and Price**
- **Positive Correlation:** Engine size increases, price also increases.
- **Visualization:** Scatter plot with a steep positive slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c7ea9b0-3ef3-4357-a9c3-554fc71b6b15/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QRGDAXB3%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T191059Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDg9Wrx57q%2B%2FBCSILNChP3SFGJ%2BhusA3ALBHnfxzSCf%2FAIgZBbqbHp%2Bav2ettlMFE2BgJgevL0uhvAyLX%2BHwZD51RcqiAQIlP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDBXQixLYZ5WcYhxuqSrcA1WHRDUlFocM%2FQD47P%2FQToNe7wlLFlu8QjsXpZXQFbie34LYcksOkso%2Fskl99ZadBhR8brgMdekqZozGofcKxPJGLyFXon65ZakEe0G4h%2BykwFFum2t53%2Foz%2F8IAvIO7cmBX%2B5l3LdPJCk3Lin3dEJurI0V83lrCyVmBDxBQVvZVeBAXGVJe3mzclQ4SDh4hdu7VnORlG%2BqSq2TrBf4LhC%2FwyFRlkCuoKXTfNCkOJVT%2BJdveuUxFljeoyra40DV28ZjL2QRNDyGqEApRSxFUP%2B%2BfHDMUhXl6hdGtv%2BKwxVv4oVOpECS9X0jIe3xKw9zVuR%2BCs093b1s3mr%2BlHTuyxDvZpmX2trl7Utb3MWESWQtz%2FMEAo7XIFZYOolq8sB0kTNvwltlQ36S4Nvfh27fqh4QRLhwxD5S31%2FK2or3i5I3HhoZPIZHmaF9stYMKus4D%2BwNafZwfxWqqKQviDivkjDkc%2FnQF5Ba5KvFdCsOj0n%2BRVfiB25cA3xc8IvdQugRES5b%2F3fHlfXUC3W9%2FOIsJtClXWeLpi5aid%2BPvMxuomtObicKnfp3d%2F8dN4XPtICT8cfYtUM3cZl%2FsifBOojetbf6gyapGxXCJfs8PJPN9NGCtt%2Bdps3uW%2FO30rv5jMOr06bwGOqUBemyGIMEPQf1aPIJ8Zp0zak%2BlKqbc%2Fghu9D%2BwsdYGs0ZL147Iv9B61MIVbRfowbK6gQNSIWHz7OT4ueaALVZ1TwMiv7LtQUVJAWPoIrp%2FSWD2zUXw6tY3amJmOUjqNfcIjz6E2Nmg9DuYbvuJB6RfqqTvE3ehbXSz5tlJemDhdg%2FwZ%2BSQ4EtcCuaubL3ol1vy8p2dcWoSkM6I2thP%2BonaFOp%2B5YZ%2B&X-Amz-Signature=d3822f4a1098d0e619154a3e5f727641e7790d861a3dff6aeb563fc3f1f9edc1&X-Amz-SignedHeaders=host&x-id=GetObject)
**Explanation:** When engine size increases, there is a corresponding increase in the price of the vehicle. This positive correlation suggests that larger engines tend to be associated with higher prices in the market.
___
### Negative Correlation
Negative correlation indicates that as one variable increases, the other variable tends to decrease.
**Example: Highway Miles per Gallon and Price**
- **Negative Correlation:** As highway miles per gallon increases, price decreases.
- **Visualization:** Scatter plot with a steep negative slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/10f1f798-9cc4-4df2-a9c1-5a339f554a0b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665SAJ4TCB%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T191059Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDzK62stkd6XFVXMHltuEQD5WZZtp8%2BhDMRXgktk9kBLgIhANXwhSruhHs21Js2loNF5xy8e8lGzcz%2F94pd0JRP7D9RKogECJT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzZaXC4ZGTU%2BMyZPUMq3AMNMXGr8QtK3rsjQuA%2BHAHFQ0EiBGLAXAXQmCXgROmoWp1cfz%2Fya2cUFAv%2BzkQWadLUwC79EntOhDOAzrOUIn5d%2BquWREtJvR0TqgggYpB9EwS4mq9mMtULFrlNYZXJzhcTtSlg798mTZZxl9CKiIcUYevKlWzQabWdMYsVgyf2L9tn5mdIGSJv2TzDweIDTrx2snyNnskg4pEsxIo%2BPDIk6wtqGQ%2BfxR4Wxx%2B07E17waPMWDRsWr2RbQEIxf59zQPQ9K%2Bwoi13Gpox0L8TYYv9kQwXEG3l%2F6PiDhCB7%2Bvol3a7w9WS8mOKp7PUPkLRICMJmmmoOltAdqAe65ut2OfmFx2buA25nFodZIwMzsINt4FE9QsZ8ioL6h5sIjfkl%2FsuC1plsA3j629nbWc%2BWueVS9cFl7OsHVy0HEAmK4pXk%2Bb1l7%2Fd5lS1TCFwtSWR188JNUNT3g9ReGiTeIj%2BOhrnPavwsb45Jwr4jQ9OMgExq8RqSGzN3z6UyxsS65ZBEI%2F1p9UoTwv8lOnGHlmeKJmq9sf5RijqkdtgrKzQcEwtp7YbOPLoY77yTum07pjfBYMlpV2ImjTGqaUeIhIICTjXouaySBtdwXEkQPQCIXAeqZIWITHqPBIJfwYB7zCZ9em8BjqkAfGKxFz7Mp3g88qwA6NKwGixwuLbW44fjBrxTM5c745nfBDwWDFDC%2FJ0ECj%2B%2FyZ8IdoXd%2BWCAOo3DmttfEdibJIy47PMKS6yNpCVZWo1GQtiDS%2BmDIWEpxlQ0C3CJwBj8QWCyZmGmiEUL%2Fs0wnf6lS3WgzhOWW63rbjN%2FwXVxKBGbnOnG5GfTg8%2F%2BvXmYMDp8bedX6ZX%2BcC8%2BlSrwqTKLDWQUxoc&X-Amz-Signature=1b3ba2c4a6e38fc8dd444702142e926bb89f2aa192ec828cc1a5509c808e16f2&X-Amz-SignedHeaders=host&x-id=GetObject)
**Explanation:** When highway miles per gallon increases, the price of the vehicle tends to decrease. This negative correlation suggests that cars with higher fuel efficiency (more miles per gallon) are generally priced lower in the market.
___
### Weak Correlation
Weak correlation indicates a lack of strong relationship between the variables.
**Example: RPM and Price**
- **Weak Correlation:** Low and high RPM values show varied prices, indicating no strong predictive relationship.
- **Visualization:** Scatter plot with no clear trend or slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9f914514-8914-4bf4-ac84-d9e3077f6eb1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YJHMUJQS%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T191059Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCmnI7uN56Irns91nLqbUne4zMEqkXgyvOeP%2FRbX8LicAIhAJR3v0OfMuUrj40iDfTvdeDj%2BU7W48rRTeeUCSd2vsH7KogECJT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igx0jEhTgvqjwm79F8gq3AMYoqvGKHsWjr3mQ7PVkk8gL5x%2BJh1exfJ2KP0oMJ2aPy7KIzARCKgTAYueCIfyGA0VyLwo5bW043EtOcEs6L4pAPH5090TuleDaF5C1U9ZsYAxJ%2Fw70R%2Fx3FhP90o7%2BUS0BplMQ39RAwnfBkfjLxB5v9flrNp3Di5ZoqqH%2BaJa%2F%2F7sUtlohrK%2BBcjqtcc9AiymefDJXB8FJIESDiot6ATAK2ONXmeaPS5SLX8aY8JR32agb6vEPrXRIQStbnmibhE7ojlwKSI5G%2FbRB4vXm6%2Bwm4dLaI4YiOhePrjzxYFQabk1bq6KTG1yA4eO57GsxUHsSk6M2X%2F47EHgnmaZyOEs%2BmGfZ9GF1iYGM3X2PQnvJGyuQklXYsC383X3LVSVa5BZT93YIX%2F8L7Pg24ChUTFebG0eOt%2BBRWS5Jzic96ybvR5goqTRPeBwldDmgni8JyMRjLaSWj8Q7UbB21KD1wqSqHCNqbqsIR4etlKsYfvMasbGJkw5wKUOhRf6RasIHt3UZg8N7qiRpBQwD6mYlUGKKavmgLveX8yWBIJUTaM0yBHaEgnjjMfs1m7DuTL7uADLfPCp6jYUv2OKQSS7VIvv3%2FC08nB%2B2FmXbVLNomzlqs3NxAktNQ%2FRmYSaUzDg9Om8BjqkAQcLwZclMPZoi1MxEnH0wP1B8%2FJ8Vvz52hSJGtTGSOHo%2Bl80YZLTi9ahQOJR%2FTrNskDRqaVfvCFLst15EllsjZXFIIhn%2FE6TnHBfU8%2FtoqY%2FSxGiVZqwsUZkaswVTb5ufIoPu42RsnZqTvRv%2BLFNOMh5mGFf%2By6HQ%2Bpt3Hur4r0VoR1In9AaK1gI0WgVxs1%2BrlVZLq4frE8ygPa28p92cBbZss%2Ff&X-Amz-Signature=78682fb6b8fd1b4746941a0520d4cc79638d7d1989b7380c0873386ae1b3cf0f&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f18086e5-5b04-4fbf-8309-8944ab20d213/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UYBVOOV2%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T191059Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHWKkPaMVaCeiPcTuj4wBSR9qwFFruDcpIMeNMbqchGuAiEA%2B9okOTk85Vo8xVzc8JNWFyUQlmAVUMuUgdTOw2%2FYkLQqiAQIlP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDefn4WTpckbInONRircA%2FCKFCSlklWC6jxdlymiq4v4CZEBRhW1rcm%2FueT%2FAG3Rvwen%2BhR3I3k5IXjX8JrjvUXquunOKZ4gohRXiHLEasT5kA0YqJ2bzdj3Zcb8tA9MNkLpWHqC5wI54dzyfIhtVEIYi86OgxJOic4kzk8AaP1YRKOTznYMyYBBv3kf4F5d2c2Rfr7jUY995gggFiN3FFtuKwMFZtlqmmLHGLffFw%2FP%2FpZSlEvnFVxtKRfd8dkddRE4CMvfx02AyBmkKbMqqHpUuerhCIxa98eh8siMqv2Zq5r3YIOE48FZceAEy3DZVJxAlD3slRMKL8AdUd0Q%2FKLepoT4fykud4mbSRtZtls8z0RKrdchUKXyUV%2BNFsFjm8SGNzw5BVakIK9uF%2FVBZ9QvY2O7L0ds4PgrdCuj94XpFfUkOVZqbuukjQN9CiN52WPK%2Br1kn4ocw4c5G1oMW9ohPxMqyDFaujPgyA62ZeP2OuNjjK0kL8kwORY6M3TOjzgD0ewq5YxDv3V%2FG%2FQKNf7b5gKrzaZNS6qJnBks%2BGgVvMdh5Tfms1rxrSh3V6eI3jdSpuWZf%2FW7fKuBauqeYDs2ER3DtqdEle33XWRr42ztkWbgFnILIkhZ7ByKBx5AuasMBTIbtlCRNyuVMPf06bwGOqUBrkNeEJSnZ5EMm7z36%2F0Mm0apCn3T8Wntc7VG%2B5VTVyxfCnY2OD9Kf2XnNVym9efqml2PN2s6FtpRFQa9Z0XNMwqW7d%2FkHu8LZ0aSCEus5ZE1y1wfHmaoi93GahjnIRFZXf6qPgfKHh6C1vxxUIksfvY1iVYE%2BDzRO%2BlrcfpH7wNw%2BXGxMHtsNJxo5IlkBMShWoFmBwpBaNQxKeYtELoaWi3jecdA&X-Amz-Signature=e540b8c6001464086c8a2416282d8ba04b58b7b629a9a7f5c3de005bbe812a87&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Correlation Plot
Heatmap visualizes correlations among variables. Color scheme indicates Pearson correlation coefficients. Dark red diagonal line shows perfect correlation (value of 1) between variables and themselves.
This heatmap offers overview of variable relationships and their link with price.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cd3b341e-cc1a-45f7-8aec-cdc00436d270/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UYBVOOV2%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T191059Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHWKkPaMVaCeiPcTuj4wBSR9qwFFruDcpIMeNMbqchGuAiEA%2B9okOTk85Vo8xVzc8JNWFyUQlmAVUMuUgdTOw2%2FYkLQqiAQIlP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDefn4WTpckbInONRircA%2FCKFCSlklWC6jxdlymiq4v4CZEBRhW1rcm%2FueT%2FAG3Rvwen%2BhR3I3k5IXjX8JrjvUXquunOKZ4gohRXiHLEasT5kA0YqJ2bzdj3Zcb8tA9MNkLpWHqC5wI54dzyfIhtVEIYi86OgxJOic4kzk8AaP1YRKOTznYMyYBBv3kf4F5d2c2Rfr7jUY995gggFiN3FFtuKwMFZtlqmmLHGLffFw%2FP%2FpZSlEvnFVxtKRfd8dkddRE4CMvfx02AyBmkKbMqqHpUuerhCIxa98eh8siMqv2Zq5r3YIOE48FZceAEy3DZVJxAlD3slRMKL8AdUd0Q%2FKLepoT4fykud4mbSRtZtls8z0RKrdchUKXyUV%2BNFsFjm8SGNzw5BVakIK9uF%2FVBZ9QvY2O7L0ds4PgrdCuj94XpFfUkOVZqbuukjQN9CiN52WPK%2Br1kn4ocw4c5G1oMW9ohPxMqyDFaujPgyA62ZeP2OuNjjK0kL8kwORY6M3TOjzgD0ewq5YxDv3V%2FG%2FQKNf7b5gKrzaZNS6qJnBks%2BGgVvMdh5Tfms1rxrSh3V6eI3jdSpuWZf%2FW7fKuBauqeYDs2ER3DtqdEle33XWRr42ztkWbgFnILIkhZ7ByKBx5AuasMBTIbtlCRNyuVMPf06bwGOqUBrkNeEJSnZ5EMm7z36%2F0Mm0apCn3T8Wntc7VG%2B5VTVyxfCnY2OD9Kf2XnNVym9efqml2PN2s6FtpRFQa9Z0XNMwqW7d%2FkHu8LZ0aSCEus5ZE1y1wfHmaoi93GahjnIRFZXf6qPgfKHh6C1vxxUIksfvY1iVYE%2BDzRO%2BlrcfpH7wNw%2BXGxMHtsNJxo5IlkBMShWoFmBwpBaNQxKeYtELoaWi3jecdA&X-Amz-Signature=3c24c0b2748e0ae3a7fb695865f4ac28483bc5c51bbc20f9a607254296a03e3c&X-Amz-SignedHeaders=host&x-id=GetObject)

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
