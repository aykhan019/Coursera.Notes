

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7e6d594d-952e-44b6-97ea-31225882aea6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TPQYN6VZ%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T010941Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEO%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC4Pqw%2B7lrW7UfAUBPFi%2FhitmyV0n5ZLA%2B%2Bhp%2BspUz1egIhAIvP49l7Pe1Y5CHqjblZiyOhFTU5BgKRjCaNalsjwaAkKogECPf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyXlEq9FiOyEBa9vhEq3AMyJ1bq9Xpm52ZduJkJd5cTSZW1JmNAy%2BNb2Z%2FIZzf1flSmP99bgtMfxDqJZOijzJ3TJkAU0meHcSLwlwSQ9yhmIaONvjL%2B1CfFggDQWQWCkWGHhao7HPgI%2BGApoGSiq90S8FWAu8USdQ5OfaHtUkz8EYxxLbWs%2FAUo5Zu7yfmUwJ%2FfhVm1a55z0T5080WTFgXetR2ftp65NlTxLV%2BNImpWXVoeOWFFILX%2FsqautWPanP4vwpqGtU6EDN5Ywje8mAdnQG51fnxgc9S44b4BZQuMlH%2BZHz8qsbXoUMtVd4fFhoBaKUzT0fiskj%2FmJ%2BGI8Yvff38os4FeqZIO8NBJNoBZI2j0eNlSaRiFvYrt25o0YB%2BCCUg5OA3MiKGOOVHslOAMSL2TojvzMV2rnqHJGtLRu8efL3n9qOIpQlgpjKUHYiCrXIJ38DGMbMDAFkEvndBJc3%2BxBep3yuhUcCsSrQEb8ErHopM%2BT6s2KuXV%2F6dU3xQNPGLCidRGAytDDOsik6PSYcW5w3gj5kZ2nBAT5%2FsaMo5P8ybCO7nTTua7oU905sfX9AtDG88nYp88%2BXlAPgph3cc04xk6A7xAsyFxYYNbKX2QSqym4IRn1V0vPwyc5QDLsZXwp8f%2BiadHEDDO5P%2B8BjqkAXTcYCiX%2FO0EHncemaHzT%2F9V60xX22jlve5hKYxQFtgLkzM8vSTJvGA302FKx0yUloqbzWV1FAiFtTckyH%2BwhUEMzrYbdJAlt0dyrI7BJAOpeV%2FPng4MSpj8zam9Hlmil91e7kdXpeHGuAIPTNcrhB%2FEpT08PbMcfNOIpYkqNH7cyIhuB5O%2BZAMEPXOKP2h4ZSyl7iIqr%2BoFlS%2BywQ3VMNN3Z1aS&X-Amz-Signature=5895a9d9c874ae4a9eb1d03ce79666a3e56235b572506ab669e7a204cba14294&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cbfaed9e-b398-4902-8936-dea058b21def/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TPQYN6VZ%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T010941Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEO%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC4Pqw%2B7lrW7UfAUBPFi%2FhitmyV0n5ZLA%2B%2Bhp%2BspUz1egIhAIvP49l7Pe1Y5CHqjblZiyOhFTU5BgKRjCaNalsjwaAkKogECPf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyXlEq9FiOyEBa9vhEq3AMyJ1bq9Xpm52ZduJkJd5cTSZW1JmNAy%2BNb2Z%2FIZzf1flSmP99bgtMfxDqJZOijzJ3TJkAU0meHcSLwlwSQ9yhmIaONvjL%2B1CfFggDQWQWCkWGHhao7HPgI%2BGApoGSiq90S8FWAu8USdQ5OfaHtUkz8EYxxLbWs%2FAUo5Zu7yfmUwJ%2FfhVm1a55z0T5080WTFgXetR2ftp65NlTxLV%2BNImpWXVoeOWFFILX%2FsqautWPanP4vwpqGtU6EDN5Ywje8mAdnQG51fnxgc9S44b4BZQuMlH%2BZHz8qsbXoUMtVd4fFhoBaKUzT0fiskj%2FmJ%2BGI8Yvff38os4FeqZIO8NBJNoBZI2j0eNlSaRiFvYrt25o0YB%2BCCUg5OA3MiKGOOVHslOAMSL2TojvzMV2rnqHJGtLRu8efL3n9qOIpQlgpjKUHYiCrXIJ38DGMbMDAFkEvndBJc3%2BxBep3yuhUcCsSrQEb8ErHopM%2BT6s2KuXV%2F6dU3xQNPGLCidRGAytDDOsik6PSYcW5w3gj5kZ2nBAT5%2FsaMo5P8ybCO7nTTua7oU905sfX9AtDG88nYp88%2BXlAPgph3cc04xk6A7xAsyFxYYNbKX2QSqym4IRn1V0vPwyc5QDLsZXwp8f%2BiadHEDDO5P%2B8BjqkAXTcYCiX%2FO0EHncemaHzT%2F9V60xX22jlve5hKYxQFtgLkzM8vSTJvGA302FKx0yUloqbzWV1FAiFtTckyH%2BwhUEMzrYbdJAlt0dyrI7BJAOpeV%2FPng4MSpj8zam9Hlmil91e7kdXpeHGuAIPTNcrhB%2FEpT08PbMcfNOIpYkqNH7cyIhuB5O%2BZAMEPXOKP2h4ZSyl7iIqr%2BoFlS%2BywQ3VMNN3Z1aS&X-Amz-Signature=01f735431b60fb6f78cea5f5139bcda5167722386a8849b8e6967bc19e951392&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/91181646-b1e0-4433-9711-6259a96a9247/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TPQYN6VZ%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T010941Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEO%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC4Pqw%2B7lrW7UfAUBPFi%2FhitmyV0n5ZLA%2B%2Bhp%2BspUz1egIhAIvP49l7Pe1Y5CHqjblZiyOhFTU5BgKRjCaNalsjwaAkKogECPf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyXlEq9FiOyEBa9vhEq3AMyJ1bq9Xpm52ZduJkJd5cTSZW1JmNAy%2BNb2Z%2FIZzf1flSmP99bgtMfxDqJZOijzJ3TJkAU0meHcSLwlwSQ9yhmIaONvjL%2B1CfFggDQWQWCkWGHhao7HPgI%2BGApoGSiq90S8FWAu8USdQ5OfaHtUkz8EYxxLbWs%2FAUo5Zu7yfmUwJ%2FfhVm1a55z0T5080WTFgXetR2ftp65NlTxLV%2BNImpWXVoeOWFFILX%2FsqautWPanP4vwpqGtU6EDN5Ywje8mAdnQG51fnxgc9S44b4BZQuMlH%2BZHz8qsbXoUMtVd4fFhoBaKUzT0fiskj%2FmJ%2BGI8Yvff38os4FeqZIO8NBJNoBZI2j0eNlSaRiFvYrt25o0YB%2BCCUg5OA3MiKGOOVHslOAMSL2TojvzMV2rnqHJGtLRu8efL3n9qOIpQlgpjKUHYiCrXIJ38DGMbMDAFkEvndBJc3%2BxBep3yuhUcCsSrQEb8ErHopM%2BT6s2KuXV%2F6dU3xQNPGLCidRGAytDDOsik6PSYcW5w3gj5kZ2nBAT5%2FsaMo5P8ybCO7nTTua7oU905sfX9AtDG88nYp88%2BXlAPgph3cc04xk6A7xAsyFxYYNbKX2QSqym4IRn1V0vPwyc5QDLsZXwp8f%2BiadHEDDO5P%2B8BjqkAXTcYCiX%2FO0EHncemaHzT%2F9V60xX22jlve5hKYxQFtgLkzM8vSTJvGA302FKx0yUloqbzWV1FAiFtTckyH%2BwhUEMzrYbdJAlt0dyrI7BJAOpeV%2FPng4MSpj8zam9Hlmil91e7kdXpeHGuAIPTNcrhB%2FEpT08PbMcfNOIpYkqNH7cyIhuB5O%2BZAMEPXOKP2h4ZSyl7iIqr%2BoFlS%2BywQ3VMNN3Z1aS&X-Amz-Signature=efc64a12ccd0a0d8c33d5bf8a0083348248ea4e427bcd40cfc26289c939b7d2c&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/09aba1c0-0d55-41dd-852a-a04c5b8a3fac/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WQXCFDXO%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T010942Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEO%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIAh%2FeKZNkfzgDKujLcWHozhP3y1aVKocLaxl9Aka%2BhKzAiBToyEsEuorRSlwoIBcYiV2f%2BUzwX5zFRbSUW1yPz0pxyqIBAj4%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMH7AWRquU%2BJFSwORHKtwDf2Sf50eQueYB7N02xP8WKB%2FMPyqMNe8NrUPQXLg1CCjhXR53U3tVfTM%2FzsxyAmoTx4rUUYf7xspohvPAzQv4HkV78xMhyrAY3OGPqQ7rfMNWaMu303NqJCyUq9XnBpMFbfLk1Knc3wQ5feB0ooaLSXT9nAbvVAq9QSjxjrwNaVszkeFvWx5mNpQAwlcW3sww6edx4O%2F%2Fnfj%2BoZjZw6AZ%2FWqaim%2F9cnOdtkqCwMepkAtE3ES3Fh6%2Bt1DSfmMZVN2k3H5F6V8PLr79P32pei8mJEKbplkCAMYn2V5dk2RiIzIX8LVPYnqN%2FXbr1OkBfPRc7SiEzFaQGIZIpgee0JSTOP5q1s4tu%2BY7U7r5OECsQqeqh9NUyS2HsjcR7uDpReuZrb3%2BaHV89Ayzbd1vNwyA7Ol7LWWrRSdXDss6J7imqjsd%2BwyVh2AUhnuLJth%2BpQ4DQpKSn1qLmXEzw0ddaKDwhXsxDD5drZ%2BEy5WoSFUv4T0%2Bv1qmc2Yiym04p%2B73c3xqlKzQJIOf5BzpHa5qcw2aOWUFNwKqE5yorIYWgVBBy%2BYEdnxJqgQVCRGvSkr4fzA%2B%2B7kGPiB2xq7P6LH73OaVBJfc1Zqx5sVI5LXenttaX7kP3fws40RUVLY6irgwiuX%2FvAY6pgGwRehRUQd054mTVWhSMF9MPmpIetzsQdWp7IhYKCMzFreNkrdyXwKsaxfeJJJdu%2F9hI20IuRcdd2kaKrQSr4IF2L189IuCb34ELfdqcOYdgGEm3hhXc8kaaPsI%2FbMPSguN7VBu5T%2FTxNDI5YdejXgkCdIZPjSXnlcGSATgLNrozVPl5kN7ZahJ0k2w2dsx0ObkVA7AlbOsqkQpR00esHYCiRarOrao&X-Amz-Signature=10ce1abd2d60cd4fec135c7c0faafad196dc8f25841189ac0fff3624abb9d7be&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 2. Scatter Plot
Scatter plots present the relationship between two variables in a dataset. It represents data points on a two-dimensional plane. The independent variable or attribute is plotted on the X-axis, while the dependent variable is plotted on the Y-axis.
**Syntax:**
```python
plt.scatter(x, y)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23708af9-659f-4f23-b626-1a4292d7842c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WQXCFDXO%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T010942Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEO%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIAh%2FeKZNkfzgDKujLcWHozhP3y1aVKocLaxl9Aka%2BhKzAiBToyEsEuorRSlwoIBcYiV2f%2BUzwX5zFRbSUW1yPz0pxyqIBAj4%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMH7AWRquU%2BJFSwORHKtwDf2Sf50eQueYB7N02xP8WKB%2FMPyqMNe8NrUPQXLg1CCjhXR53U3tVfTM%2FzsxyAmoTx4rUUYf7xspohvPAzQv4HkV78xMhyrAY3OGPqQ7rfMNWaMu303NqJCyUq9XnBpMFbfLk1Knc3wQ5feB0ooaLSXT9nAbvVAq9QSjxjrwNaVszkeFvWx5mNpQAwlcW3sww6edx4O%2F%2Fnfj%2BoZjZw6AZ%2FWqaim%2F9cnOdtkqCwMepkAtE3ES3Fh6%2Bt1DSfmMZVN2k3H5F6V8PLr79P32pei8mJEKbplkCAMYn2V5dk2RiIzIX8LVPYnqN%2FXbr1OkBfPRc7SiEzFaQGIZIpgee0JSTOP5q1s4tu%2BY7U7r5OECsQqeqh9NUyS2HsjcR7uDpReuZrb3%2BaHV89Ayzbd1vNwyA7Ol7LWWrRSdXDss6J7imqjsd%2BwyVh2AUhnuLJth%2BpQ4DQpKSn1qLmXEzw0ddaKDwhXsxDD5drZ%2BEy5WoSFUv4T0%2Bv1qmc2Yiym04p%2B73c3xqlKzQJIOf5BzpHa5qcw2aOWUFNwKqE5yorIYWgVBBy%2BYEdnxJqgQVCRGvSkr4fzA%2B%2B7kGPiB2xq7P6LH73OaVBJfc1Zqx5sVI5LXenttaX7kP3fws40RUVLY6irgwiuX%2FvAY6pgGwRehRUQd054mTVWhSMF9MPmpIetzsQdWp7IhYKCMzFreNkrdyXwKsaxfeJJJdu%2F9hI20IuRcdd2kaKrQSr4IF2L189IuCb34ELfdqcOYdgGEm3hhXc8kaaPsI%2FbMPSguN7VBu5T%2FTxNDI5YdejXgkCdIZPjSXnlcGSATgLNrozVPl5kN7ZahJ0k2w2dsx0ObkVA7AlbOsqkQpR00esHYCiRarOrao&X-Amz-Signature=ea2b11f3468ff72ab276662a6abbc06079798ea8716e8e57236737dee86bfe86&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 3. Histogram
A histogram is an important visual representation of data in categorical form. To view the data in a "Binned" form, use the histogram plot with a number of bins required or with the data points that mark the bin edges. The x-axis represents the data bins, and the y-axis represents the number of elements in each bin.
**Syntax:**
```python
plt.hist(x, bins)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/24e4424a-df87-40a1-b63b-195cbdc2e0ab/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WQXCFDXO%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T010942Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEO%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIAh%2FeKZNkfzgDKujLcWHozhP3y1aVKocLaxl9Aka%2BhKzAiBToyEsEuorRSlwoIBcYiV2f%2BUzwX5zFRbSUW1yPz0pxyqIBAj4%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMH7AWRquU%2BJFSwORHKtwDf2Sf50eQueYB7N02xP8WKB%2FMPyqMNe8NrUPQXLg1CCjhXR53U3tVfTM%2FzsxyAmoTx4rUUYf7xspohvPAzQv4HkV78xMhyrAY3OGPqQ7rfMNWaMu303NqJCyUq9XnBpMFbfLk1Knc3wQ5feB0ooaLSXT9nAbvVAq9QSjxjrwNaVszkeFvWx5mNpQAwlcW3sww6edx4O%2F%2Fnfj%2BoZjZw6AZ%2FWqaim%2F9cnOdtkqCwMepkAtE3ES3Fh6%2Bt1DSfmMZVN2k3H5F6V8PLr79P32pei8mJEKbplkCAMYn2V5dk2RiIzIX8LVPYnqN%2FXbr1OkBfPRc7SiEzFaQGIZIpgee0JSTOP5q1s4tu%2BY7U7r5OECsQqeqh9NUyS2HsjcR7uDpReuZrb3%2BaHV89Ayzbd1vNwyA7Ol7LWWrRSdXDss6J7imqjsd%2BwyVh2AUhnuLJth%2BpQ4DQpKSn1qLmXEzw0ddaKDwhXsxDD5drZ%2BEy5WoSFUv4T0%2Bv1qmc2Yiym04p%2B73c3xqlKzQJIOf5BzpHa5qcw2aOWUFNwKqE5yorIYWgVBBy%2BYEdnxJqgQVCRGvSkr4fzA%2B%2B7kGPiB2xq7P6LH73OaVBJfc1Zqx5sVI5LXenttaX7kP3fws40RUVLY6irgwiuX%2FvAY6pgGwRehRUQd054mTVWhSMF9MPmpIetzsQdWp7IhYKCMzFreNkrdyXwKsaxfeJJJdu%2F9hI20IuRcdd2kaKrQSr4IF2L189IuCb34ELfdqcOYdgGEm3hhXc8kaaPsI%2FbMPSguN7VBu5T%2FTxNDI5YdejXgkCdIZPjSXnlcGSATgLNrozVPl5kN7ZahJ0k2w2dsx0ObkVA7AlbOsqkQpR00esHYCiRarOrao&X-Amz-Signature=6d114c68f09008b56afa0bae0dc640f80a637a43eaa9d7a7e494ccb3b37aa3af&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ab5a6dfe-51f5-43ee-bcb3-33dae4a1c7ad/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WQXCFDXO%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T010942Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEO%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIAh%2FeKZNkfzgDKujLcWHozhP3y1aVKocLaxl9Aka%2BhKzAiBToyEsEuorRSlwoIBcYiV2f%2BUzwX5zFRbSUW1yPz0pxyqIBAj4%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMH7AWRquU%2BJFSwORHKtwDf2Sf50eQueYB7N02xP8WKB%2FMPyqMNe8NrUPQXLg1CCjhXR53U3tVfTM%2FzsxyAmoTx4rUUYf7xspohvPAzQv4HkV78xMhyrAY3OGPqQ7rfMNWaMu303NqJCyUq9XnBpMFbfLk1Knc3wQ5feB0ooaLSXT9nAbvVAq9QSjxjrwNaVszkeFvWx5mNpQAwlcW3sww6edx4O%2F%2Fnfj%2BoZjZw6AZ%2FWqaim%2F9cnOdtkqCwMepkAtE3ES3Fh6%2Bt1DSfmMZVN2k3H5F6V8PLr79P32pei8mJEKbplkCAMYn2V5dk2RiIzIX8LVPYnqN%2FXbr1OkBfPRc7SiEzFaQGIZIpgee0JSTOP5q1s4tu%2BY7U7r5OECsQqeqh9NUyS2HsjcR7uDpReuZrb3%2BaHV89Ayzbd1vNwyA7Ol7LWWrRSdXDss6J7imqjsd%2BwyVh2AUhnuLJth%2BpQ4DQpKSn1qLmXEzw0ddaKDwhXsxDD5drZ%2BEy5WoSFUv4T0%2Bv1qmc2Yiym04p%2B73c3xqlKzQJIOf5BzpHa5qcw2aOWUFNwKqE5yorIYWgVBBy%2BYEdnxJqgQVCRGvSkr4fzA%2B%2B7kGPiB2xq7P6LH73OaVBJfc1Zqx5sVI5LXenttaX7kP3fws40RUVLY6irgwiuX%2FvAY6pgGwRehRUQd054mTVWhSMF9MPmpIetzsQdWp7IhYKCMzFreNkrdyXwKsaxfeJJJdu%2F9hI20IuRcdd2kaKrQSr4IF2L189IuCb34ELfdqcOYdgGEm3hhXc8kaaPsI%2FbMPSguN7VBu5T%2FTxNDI5YdejXgkCdIZPjSXnlcGSATgLNrozVPl5kN7ZahJ0k2w2dsx0ObkVA7AlbOsqkQpR00esHYCiRarOrao&X-Amz-Signature=094f24a9d269b07b8c43d671b2922e0aa4c59a8fad1491001a3d71572d98e934&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8f1b1d60-cf1b-42b3-9faa-f634c89c3f84/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WQXCFDXO%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T010942Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEO%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIAh%2FeKZNkfzgDKujLcWHozhP3y1aVKocLaxl9Aka%2BhKzAiBToyEsEuorRSlwoIBcYiV2f%2BUzwX5zFRbSUW1yPz0pxyqIBAj4%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMH7AWRquU%2BJFSwORHKtwDf2Sf50eQueYB7N02xP8WKB%2FMPyqMNe8NrUPQXLg1CCjhXR53U3tVfTM%2FzsxyAmoTx4rUUYf7xspohvPAzQv4HkV78xMhyrAY3OGPqQ7rfMNWaMu303NqJCyUq9XnBpMFbfLk1Knc3wQ5feB0ooaLSXT9nAbvVAq9QSjxjrwNaVszkeFvWx5mNpQAwlcW3sww6edx4O%2F%2Fnfj%2BoZjZw6AZ%2FWqaim%2F9cnOdtkqCwMepkAtE3ES3Fh6%2Bt1DSfmMZVN2k3H5F6V8PLr79P32pei8mJEKbplkCAMYn2V5dk2RiIzIX8LVPYnqN%2FXbr1OkBfPRc7SiEzFaQGIZIpgee0JSTOP5q1s4tu%2BY7U7r5OECsQqeqh9NUyS2HsjcR7uDpReuZrb3%2BaHV89Ayzbd1vNwyA7Ol7LWWrRSdXDss6J7imqjsd%2BwyVh2AUhnuLJth%2BpQ4DQpKSn1qLmXEzw0ddaKDwhXsxDD5drZ%2BEy5WoSFUv4T0%2Bv1qmc2Yiym04p%2B73c3xqlKzQJIOf5BzpHa5qcw2aOWUFNwKqE5yorIYWgVBBy%2BYEdnxJqgQVCRGvSkr4fzA%2B%2B7kGPiB2xq7P6LH73OaVBJfc1Zqx5sVI5LXenttaX7kP3fws40RUVLY6irgwiuX%2FvAY6pgGwRehRUQd054mTVWhSMF9MPmpIetzsQdWp7IhYKCMzFreNkrdyXwKsaxfeJJJdu%2F9hI20IuRcdd2kaKrQSr4IF2L189IuCb34ELfdqcOYdgGEm3hhXc8kaaPsI%2FbMPSguN7VBu5T%2FTxNDI5YdejXgkCdIZPjSXnlcGSATgLNrozVPl5kN7ZahJ0k2w2dsx0ObkVA7AlbOsqkQpR00esHYCiRarOrao&X-Amz-Signature=941494951a5478453954c18fd2fe0d2d1d99e3509f032344ec3144e3c46b16bc&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/13ad0497-05fe-4eaa-984e-707b33e14761/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WQXCFDXO%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T010942Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEO%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIAh%2FeKZNkfzgDKujLcWHozhP3y1aVKocLaxl9Aka%2BhKzAiBToyEsEuorRSlwoIBcYiV2f%2BUzwX5zFRbSUW1yPz0pxyqIBAj4%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMH7AWRquU%2BJFSwORHKtwDf2Sf50eQueYB7N02xP8WKB%2FMPyqMNe8NrUPQXLg1CCjhXR53U3tVfTM%2FzsxyAmoTx4rUUYf7xspohvPAzQv4HkV78xMhyrAY3OGPqQ7rfMNWaMu303NqJCyUq9XnBpMFbfLk1Knc3wQ5feB0ooaLSXT9nAbvVAq9QSjxjrwNaVszkeFvWx5mNpQAwlcW3sww6edx4O%2F%2Fnfj%2BoZjZw6AZ%2FWqaim%2F9cnOdtkqCwMepkAtE3ES3Fh6%2Bt1DSfmMZVN2k3H5F6V8PLr79P32pei8mJEKbplkCAMYn2V5dk2RiIzIX8LVPYnqN%2FXbr1OkBfPRc7SiEzFaQGIZIpgee0JSTOP5q1s4tu%2BY7U7r5OECsQqeqh9NUyS2HsjcR7uDpReuZrb3%2BaHV89Ayzbd1vNwyA7Ol7LWWrRSdXDss6J7imqjsd%2BwyVh2AUhnuLJth%2BpQ4DQpKSn1qLmXEzw0ddaKDwhXsxDD5drZ%2BEy5WoSFUv4T0%2Bv1qmc2Yiym04p%2B73c3xqlKzQJIOf5BzpHa5qcw2aOWUFNwKqE5yorIYWgVBBy%2BYEdnxJqgQVCRGvSkr4fzA%2B%2B7kGPiB2xq7P6LH73OaVBJfc1Zqx5sVI5LXenttaX7kP3fws40RUVLY6irgwiuX%2FvAY6pgGwRehRUQd054mTVWhSMF9MPmpIetzsQdWp7IhYKCMzFreNkrdyXwKsaxfeJJJdu%2F9hI20IuRcdd2kaKrQSr4IF2L189IuCb34ELfdqcOYdgGEm3hhXc8kaaPsI%2FbMPSguN7VBu5T%2FTxNDI5YdejXgkCdIZPjSXnlcGSATgLNrozVPl5kN7ZahJ0k2w2dsx0ObkVA7AlbOsqkQpR00esHYCiRarOrao&X-Amz-Signature=828c4b605c548c1897af5f8ce7ede79c8d5a9983dca8bd401a40ea93b21b6cb8&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 2. Box and Whisker Plot
A box plot shows the distribution of quantitative data in a way that facilitates comparisons between variables or across levels of a categorical variable. The box shows the quartiles of the dataset while the whiskers extend to show the rest of the distribution, except for points that are determined to be "outliers".
**Syntax:**
```python
sns.boxplot(x='header_1', y='header_2', data=df)
```
**Example Output:**


![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d207ae92-0a7c-4e2f-aa65-0ee5a2c33bf7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QHYV3VLQ%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T010943Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEO%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDdmbpXJ58sfhObzag1K9XBy3P7WUeMWnzMsx56zCQDfAiEAzwx7OnQ7q3%2FR59gRkEs9oU2qT1A1GS7irHPTKM4x%2B4kqiAQI%2BP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDCinBDOWn%2F3XMp5b4SrcA6PZJOnntKwKOKaB7PA4tc2hbA2NxHgvfw%2BDEu4o%2FJajZex9PKFYwNCJDu99oBLuiTlf%2BmKVnmQcgZr2rlurldt13uIfoj53jx5ETjmiRBLEZ8DJ9586YRaEgQx2P4uy6FgZjbJ1ef05QCJsMLr%2FodPAUWTD9J4WKnj53%2F77goge4Xvv6IbmQlpts5yR55aBjUxsB8dPjX34gjMmAS%2FFHel7qNT5ejFYTX9ik0PAHdRHDot7vJysM4i%2BSlE5xNX%2B5WZ3f52XFlMIshFfxuuzrtfduCsyx0du08Mxi1id6cqmktcZDKBJK%2BEgv9KPBTZqByYcJCkD%2FEuFhsqjx4cn0HC%2F1M%2F%2B0mZUe%2Fhoifn2jd0SysYuVjpVHaDuIIs2qCjQnXBvGYz8%2BQ9xyXGaF25rTw%2BPAZay1ZDYncww6nQ7B7OAwM3J%2FQN7wzVVEF1TIye3OjjduU4ZXcKnfIT%2B8SW2Nz%2BYk5WEXUOhRUMGDRSQooQYlar0BsTtkO5GMXDx0bOM2gKU7Wt2uIb9Oia4oms12q4m6NIcsZmyp5xvVFzWgXA%2BUW0QeCanbhYvF2av%2B%2F7aUFTIjGl1sxlapGRYs8U2GkxnSMtUjUVcl%2FVCnSs%2BqwQ0fWp1ixAwuCDm5dhRMLnk%2F7wGOqUBRs9VaKmaHtFT%2BWaK0iy7aCnJwCc4J%2FPwS0p6s5o8cM0yveCcsYFlWJWb%2B9jtQQAyudN5o9dbyMSThfwrS%2B3WajiZ4danJ%2Bg%2FLPN%2FGhIXF1AuUFA5gHQaoOzpji%2F2n2CnXkegyMxz0qyuAw8C3oiwgOuDqcYurRs%2Fqyw1ElHrKFniR%2BqO7SDh49Yufpm7wSsnMqcZy5J2G%2BfrVKjrDPrh6z%2BucaXz&X-Amz-Signature=7c62b2956927b5a5392fa51f716c7a5a5ad2c21b193e4a48bbfcf16dba72424e&X-Amz-SignedHeaders=host&x-id=GetObject)

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0e516edc-7551-4792-ab18-0494db3c4c0c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QWLO6MFG%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T010943Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEO%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHKkBYFexM7pcoukVTQYfS8p%2F%2FxZfw%2B%2BCRADCiwNFwIJAiAzQ4CyzIVFpxsuEUrU3vz3twXBri39Z6krUSm%2F%2FIV1KCqIBAj4%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMO7sDzjfEs%2FzVzKG0KtwDfHnQcPvm2rVFWqXTMUMCMX%2B54hlNngoAm2XLrFvVPKHd5ubo%2FPVOa%2BF43XqaIO3sCtOH4XYweJwXTmqhI1ZVWSGf7C2PwPsqmSIfW2vmgWZ0azvT7SNP66GPwEmCAGEWWKr1GlMLNYT28kN4H9IzTpQnZv99fQ1mgF5IfitIISMzT82f0GMcT4QFvj2VVvFjzOy%2B9116%2F6jyQDfI2TmZ3i%2B7Y3XJHGlhxhaSPabSvtniWVpJlaeLXIHvdsPYOWN9432T%2BTybKPxPiyUnUXCpb6JTJQTT5B0wYtlVg7YqSrjTAJCYjS5eA9jD%2B1lZAcMeaGhG%2FUUV2efsWTRvBnb1nSxryWcAq1PRakni%2BENpeE%2FbsTl3uBdembFwHlGYwlfvLAFVGFM4zoAMQK8TBwB5Gg6yAaKThguhUvSa4%2BW1LzobisewZb%2BRuhbq2WaynArBsR4lNIrP0fZYZf6EDVuOvHEfTZ1BOP%2BDYvYypQuZy3gUxM6OGYeDAHya7rhcX34g7n8J3F61n8LCT5OOlunjEfIfSGBd0AfC912dLilLEARBs%2F73o49bfaIQaNBYtZfrobq0BFyvNJO15pEk5qlp4%2FfmrGrLFqGOQdDSLxFgDqgS9WJ0xOU%2BKI9CAdEwzuT%2FvAY6pgGOuwH96HB5RVcD7zMvksWfHerkVNgnwBNRSZHdKBtUHcvK6jiVswsnWyVx9NsDgSmVTCahzopVrOuLgbGmOktL5cO6hPrb%2Bzs77PdwZAMkpd%2BKKx7Y%2B7sUD2bnjoC5r6wQegIMP%2FeprwE5CIU9KPEkEVht%2BeqzuQEsi50IxliMvdbkRGO1l2RUjLJykevyBAH%2BpBaA%2BuxYQdyhPHuaE2ky7bXokrrb&X-Amz-Signature=bbeb731f011b466c54128f3470adf32e09e139410a6996622b3776f1e11258b4&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23a79b9d-2356-49a9-8fd9-65c6b0ab2cc5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WQXCFDXO%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T010942Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEO%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIAh%2FeKZNkfzgDKujLcWHozhP3y1aVKocLaxl9Aka%2BhKzAiBToyEsEuorRSlwoIBcYiV2f%2BUzwX5zFRbSUW1yPz0pxyqIBAj4%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMH7AWRquU%2BJFSwORHKtwDf2Sf50eQueYB7N02xP8WKB%2FMPyqMNe8NrUPQXLg1CCjhXR53U3tVfTM%2FzsxyAmoTx4rUUYf7xspohvPAzQv4HkV78xMhyrAY3OGPqQ7rfMNWaMu303NqJCyUq9XnBpMFbfLk1Knc3wQ5feB0ooaLSXT9nAbvVAq9QSjxjrwNaVszkeFvWx5mNpQAwlcW3sww6edx4O%2F%2Fnfj%2BoZjZw6AZ%2FWqaim%2F9cnOdtkqCwMepkAtE3ES3Fh6%2Bt1DSfmMZVN2k3H5F6V8PLr79P32pei8mJEKbplkCAMYn2V5dk2RiIzIX8LVPYnqN%2FXbr1OkBfPRc7SiEzFaQGIZIpgee0JSTOP5q1s4tu%2BY7U7r5OECsQqeqh9NUyS2HsjcR7uDpReuZrb3%2BaHV89Ayzbd1vNwyA7Ol7LWWrRSdXDss6J7imqjsd%2BwyVh2AUhnuLJth%2BpQ4DQpKSn1qLmXEzw0ddaKDwhXsxDD5drZ%2BEy5WoSFUv4T0%2Bv1qmc2Yiym04p%2B73c3xqlKzQJIOf5BzpHa5qcw2aOWUFNwKqE5yorIYWgVBBy%2BYEdnxJqgQVCRGvSkr4fzA%2B%2B7kGPiB2xq7P6LH73OaVBJfc1Zqx5sVI5LXenttaX7kP3fws40RUVLY6irgwiuX%2FvAY6pgGwRehRUQd054mTVWhSMF9MPmpIetzsQdWp7IhYKCMzFreNkrdyXwKsaxfeJJJdu%2F9hI20IuRcdd2kaKrQSr4IF2L189IuCb34ELfdqcOYdgGEm3hhXc8kaaPsI%2FbMPSguN7VBu5T%2FTxNDI5YdejXgkCdIZPjSXnlcGSATgLNrozVPl5kN7ZahJ0k2w2dsx0ObkVA7AlbOsqkQpR00esHYCiRarOrao&X-Amz-Signature=112c31320ccf7ca61c01f2225e81bda099e0c7532b6874a18e5b68cc82285630&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 4. KDE Plot
A Kernel Density Estimate (KDE) plot is a graph that creates a probability distribution curve for the data based upon its likelihood of occurrence on a specific value. This is created for a single vector of information.
**Syntax:**
```python
sns.kdeplot(X) || sns.kdeplot(df['age'])
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0d571213-2a2f-4921-a50b-880847aa05ee/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WQXCFDXO%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T010942Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEO%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIAh%2FeKZNkfzgDKujLcWHozhP3y1aVKocLaxl9Aka%2BhKzAiBToyEsEuorRSlwoIBcYiV2f%2BUzwX5zFRbSUW1yPz0pxyqIBAj4%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMH7AWRquU%2BJFSwORHKtwDf2Sf50eQueYB7N02xP8WKB%2FMPyqMNe8NrUPQXLg1CCjhXR53U3tVfTM%2FzsxyAmoTx4rUUYf7xspohvPAzQv4HkV78xMhyrAY3OGPqQ7rfMNWaMu303NqJCyUq9XnBpMFbfLk1Knc3wQ5feB0ooaLSXT9nAbvVAq9QSjxjrwNaVszkeFvWx5mNpQAwlcW3sww6edx4O%2F%2Fnfj%2BoZjZw6AZ%2FWqaim%2F9cnOdtkqCwMepkAtE3ES3Fh6%2Bt1DSfmMZVN2k3H5F6V8PLr79P32pei8mJEKbplkCAMYn2V5dk2RiIzIX8LVPYnqN%2FXbr1OkBfPRc7SiEzFaQGIZIpgee0JSTOP5q1s4tu%2BY7U7r5OECsQqeqh9NUyS2HsjcR7uDpReuZrb3%2BaHV89Ayzbd1vNwyA7Ol7LWWrRSdXDss6J7imqjsd%2BwyVh2AUhnuLJth%2BpQ4DQpKSn1qLmXEzw0ddaKDwhXsxDD5drZ%2BEy5WoSFUv4T0%2Bv1qmc2Yiym04p%2B73c3xqlKzQJIOf5BzpHa5qcw2aOWUFNwKqE5yorIYWgVBBy%2BYEdnxJqgQVCRGvSkr4fzA%2B%2B7kGPiB2xq7P6LH73OaVBJfc1Zqx5sVI5LXenttaX7kP3fws40RUVLY6irgwiuX%2FvAY6pgGwRehRUQd054mTVWhSMF9MPmpIetzsQdWp7IhYKCMzFreNkrdyXwKsaxfeJJJdu%2F9hI20IuRcdd2kaKrQSr4IF2L189IuCb34ELfdqcOYdgGEm3hhXc8kaaPsI%2FbMPSguN7VBu5T%2FTxNDI5YdejXgkCdIZPjSXnlcGSATgLNrozVPl5kN7ZahJ0k2w2dsx0ObkVA7AlbOsqkQpR00esHYCiRarOrao&X-Amz-Signature=8240e46642a16ce6058160c6a0bfc77cb9ce244c34b2405fbc7f50b7e1eaadf0&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/53752550-ef82-4ca9-a01a-09921f0282d0/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WQXCFDXO%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T010942Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEO%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIAh%2FeKZNkfzgDKujLcWHozhP3y1aVKocLaxl9Aka%2BhKzAiBToyEsEuorRSlwoIBcYiV2f%2BUzwX5zFRbSUW1yPz0pxyqIBAj4%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMH7AWRquU%2BJFSwORHKtwDf2Sf50eQueYB7N02xP8WKB%2FMPyqMNe8NrUPQXLg1CCjhXR53U3tVfTM%2FzsxyAmoTx4rUUYf7xspohvPAzQv4HkV78xMhyrAY3OGPqQ7rfMNWaMu303NqJCyUq9XnBpMFbfLk1Knc3wQ5feB0ooaLSXT9nAbvVAq9QSjxjrwNaVszkeFvWx5mNpQAwlcW3sww6edx4O%2F%2Fnfj%2BoZjZw6AZ%2FWqaim%2F9cnOdtkqCwMepkAtE3ES3Fh6%2Bt1DSfmMZVN2k3H5F6V8PLr79P32pei8mJEKbplkCAMYn2V5dk2RiIzIX8LVPYnqN%2FXbr1OkBfPRc7SiEzFaQGIZIpgee0JSTOP5q1s4tu%2BY7U7r5OECsQqeqh9NUyS2HsjcR7uDpReuZrb3%2BaHV89Ayzbd1vNwyA7Ol7LWWrRSdXDss6J7imqjsd%2BwyVh2AUhnuLJth%2BpQ4DQpKSn1qLmXEzw0ddaKDwhXsxDD5drZ%2BEy5WoSFUv4T0%2Bv1qmc2Yiym04p%2B73c3xqlKzQJIOf5BzpHa5qcw2aOWUFNwKqE5yorIYWgVBBy%2BYEdnxJqgQVCRGvSkr4fzA%2B%2B7kGPiB2xq7P6LH73OaVBJfc1Zqx5sVI5LXenttaX7kP3fws40RUVLY6irgwiuX%2FvAY6pgGwRehRUQd054mTVWhSMF9MPmpIetzsQdWp7IhYKCMzFreNkrdyXwKsaxfeJJJdu%2F9hI20IuRcdd2kaKrQSr4IF2L189IuCb34ELfdqcOYdgGEm3hhXc8kaaPsI%2FbMPSguN7VBu5T%2FTxNDI5YdejXgkCdIZPjSXnlcGSATgLNrozVPl5kN7ZahJ0k2w2dsx0ObkVA7AlbOsqkQpR00esHYCiRarOrao&X-Amz-Signature=3cab8217117fbce0947a7e30e921ea5b9e98a5648c82b1b7babcb91c77db00f7&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
## 4. Correlation Between Variables
Correlation is a statistical measure of the extent to which different variables are interdependent. It indicates how changes in one variable are associated with changes in another variable over time.
### Positive Correlation
Positive correlation indicates that as one variable increases, the other variable also tends to increase.
**Example: Engine Size and Price**
- **Positive Correlation:** Engine size increases, price also increases.
- **Visualization:** Scatter plot with a steep positive slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c7ea9b0-3ef3-4357-a9c3-554fc71b6b15/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QCMSJEKS%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T010943Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEO%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQD4KJ8hx3ZBNu9QNuDstnfEPPNw9UWV%2F0%2FQdag%2Bam6zwwIhAN6HiBRWj8HnSBE%2BgpTDSUOjUz0Je1T7QlmAk6uX6bY8KogECPj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igx8v4CEYmXWvElQXTUq3ANmOBeJJqLdJXH0kUQ0KF%2FiDHMQG3CowSqbJajmQRTvTASiGP7DEpRkhlw2DaWHnqYv9eFNh8QeWk9gDV6xb%2BdhKyaAH0IYvZeyg%2FNisdZvsG15TeDPlvwSiYpVtq3muZ08AYLLpTv46M7aF1poTRmsKkvZEYFtY3z5bjkiwGeLpNFWyAFaYHW2%2F0TYPSQZHzrf53Ff6G%2FyuyanyL2my2niJia%2Fcva%2BEoeT7YLnnwtQj2yRoO%2FjLloj5yqVJrluE%2BBa0GC6zV34vy4VcD37W%2B315O0TotX%2BbvM7T8%2FTHf518WezDaB5UJzRvtXQtSjJiaQJtPPvpigosTuopPJmihdLCK6QqOjdBuZI56crv%2F4Pgmd2KYncoNkqx%2BySKE3aojR2XmkS25KnhaFYSFb7%2FfV1H6ohiqzFbuxSjHtTaa531R82l69H1Ic6Au9YxA95U6UNLNk48ryYxdgufIDQq407zz95zM09zvOId3Ig%2FkmXN2jXRbrjVz3yKVRPyBBnaZCFeOXx8ZboIy8%2ByTB0gR0vtBQ4S69skKWugHGGL6WhAoOMD82Y3CAP48oVY2SUWJczig7aRch1ndosKpGO1p1kL3OSr8iGTu%2B%2Bwms2w%2F9sf8pMF2A47ym3UMxhdDC65P%2B8BjqkAfzwPK5MYDhlXDbz3%2F8JsLrRCVZpIM5MV2agBnA%2FDII9yv6b%2Fq%2BKkM3FfqFiEsI0R93lkCZbu8x3O3SdvjsVAXP2F56ZEWRU8DuXbHnmlG868a8o96Xoro98CBZ51DrJMADMHC0cvNCoeV%2B86E0s%2B3dg9LCbxrLVwL6%2BxUnCsxEr8KXuDuvaRBdp3g56YXciDZoI%2BJXs6rMCQYoDlHZJoIOCw8Tz&X-Amz-Signature=12e7ada64b735734e5ea90cdb4c67ab22bd3ccabe25b2930e7996d73baf250ea&X-Amz-SignedHeaders=host&x-id=GetObject)
**Explanation:** When engine size increases, there is a corresponding increase in the price of the vehicle. This positive correlation suggests that larger engines tend to be associated with higher prices in the market.
___
### Negative Correlation
Negative correlation indicates that as one variable increases, the other variable tends to decrease.
**Example: Highway Miles per Gallon and Price**
- **Negative Correlation:** As highway miles per gallon increases, price decreases.
- **Visualization:** Scatter plot with a steep negative slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/10f1f798-9cc4-4df2-a9c1-5a339f554a0b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RWRDDJAF%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T010943Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEO%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCICXmu%2B%2F6f02EykyJBHY4CKdjdA%2BedwqkcRnPG6Awuz0kAiEA%2FqLz8DlWTZA0jYj0aRTSFqvxRMKMPVjgBEDBEKAJwzwqiAQI%2BP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDN%2Bh2AMgOP7NsxT1HircA8GWlswWSgqRBQzOQ2uOJj0ZQtuUD3kO7AAMh6GVsi04zvwvDPQoSObZajOwx37ujpvuz7wqdShR7Y%2B5%2BDLg6HPWs3yzq9LjJGNSrs3VeOdNozF5cDXdCl%2F7FXsTeEDGn4NA4tqeptPNMfiFCfqXYJstKxNKu7HiLQpa7XqKsY0%2Bxh4VdSF4E1bYUEKa8fzDATsY%2FEPXFovY5tuk5koxtz2gsrX%2BKokPkKLmK%2F6rrJl%2FF64jJGOXpOGo54SxmGMejpzdFR%2FvV0O4mNB1lVbovxLu6OeSKfvoqED2q5w4DSPQhRAh9TQ5ech5eanQxV1nwxyXEYZgbYbosR%2BtQoYSqnCbvBNnqkxWL7EDOstM5zqQ5tx8jmPfdXhz5%2BdC7YzeETAvGNmJOYEGnl8gl3A3%2B6vRzU7U8%2BzHePgsUr5WCdBpjMWf7jM5ueRchwFVv3QZpHqI13EHG1QiNi7qPfJ4c3J5%2FaDZieOVO8p0%2FxJwGOiSTwLUMEvul037tfdGvtfb4CALTEsX%2BZKx43AMFmdwWBiE90e4%2Bm71QTq8Ry3VWyPVUEWUM3dH3Tm36pBCalA8IhyL8%2BM9%2BUB3vXdyPPQ20Vkv7YjW3rWmzi7ZoidOAUN1soadV5S%2BP3KkISltMMLl%2F7wGOqUBrWe2yKALy2JDkqX4OukJ0fqgEXjEAEn%2Frdpae7JZE6LFWn%2BJ7K5o3Pi8sSM0cNVohFscRt%2FcxqFlU6zOiruXfLDvpOQM2MdJSi86Ke8h51k38%2BdNfV6t8Kl0q2QalqiN8W8iCzFm%2Fyljqqgq%2FPZTcJStnm3DgEGSwFprDgG8AEM00KGXxFytNVT%2BFlPqHLvGUHxp9hPav5oRECoBnJEDQwMgoKtt&X-Amz-Signature=9ec6430f87da80c66a89bdde9389303170f03b74eed67accdf13f36d58bd6d1f&X-Amz-SignedHeaders=host&x-id=GetObject)
**Explanation:** When highway miles per gallon increases, the price of the vehicle tends to decrease. This negative correlation suggests that cars with higher fuel efficiency (more miles per gallon) are generally priced lower in the market.
___
### Weak Correlation
Weak correlation indicates a lack of strong relationship between the variables.
**Example: RPM and Price**
- **Weak Correlation:** Low and high RPM values show varied prices, indicating no strong predictive relationship.
- **Visualization:** Scatter plot with no clear trend or slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9f914514-8914-4bf4-ac84-d9e3077f6eb1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664WQ6FOIQ%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T010943Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEO%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDlABNKHXj7%2Fu9PGdJc5rR7%2FH2hvold5HV%2BhS%2B4xYkyugIgbaM81aDx3IJsMzdKBHo5UdabC0D1%2BWiSREuVtUBuGN4qiAQI%2BP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDL93slP6UI%2BirTyFWCrcAyR1S%2BEoMlsuNJax186hdrz0RWjh%2F7qPxPJZCBxIja2%2F8rHkvtUPS5S6DoIUzJ4Ddkk4pCs%2BA1ViaRQJdtvgfxi4quRW4wuFL9hDq5YdenmJAopwwc4rWLYq7sWurmtkjN8dfemy9B%2Bs%2F9zjB8k6CrsX%2BgkAZvTc3mJd2hDPh2QtQI7xDuM%2FZ00cDnkil2c876L%2Bb87ynkFyzT2iV05ZdHoX1L4RGbz%2BML07yMxUyx22FDhyp6Yq8yLP27lXdmjJZVe6MATAU2fCdwgEJrVdM6LU52%2FXDWLOOQOoe3N4K3%2FebNjh6z7wN3NW1K78uVtxOSSgHKDr3ghV1POupQJR2ErAoXDnNVejKoPK%2FGBpEm2%2Fvjw7KbkFH7SP%2B4hN%2FhAfY5XiDY%2FpB156TBnKftreGHAFx2qR4QLIhi9RBkpsrRQ6nNakBPlawDOSqg5jPHJmWw%2F0v6Q2gWEAtWLO4y47idYpxozw1c0o3NcxMML7m3bQlpjJ9YdCpHc%2FDgjdxp%2FMql8BV40NdqrlXpWwTvFOqstF7qKnAddbIBYkAnUrlMgo8pPpiw%2Bm0Z0FMWo8rs%2BolVFSooCg7aTYMU41qLTYeP%2FEHIHgb4%2FEYSF2H4nyxb%2FQb6DM3nyRquG8Bq%2FzMMTk%2F7wGOqUBCZlxTzNuPjZKfhmIN897TVb4A%2Fu9iBuXzIll9OgS160xHHihHkBOxTCvUBEotNrOMo8LUeyEZX1IqD9k%2F0nZ3ljF%2FnVwYoCiaTq5swFmUqJtjMCxUWgXxrAB5urpVltmHB2wpGMOam7Y8gn0sbcraeycd4L%2FzwjW58ExSNuxOJPPXxtOp1u9d02FOvi5PWn3wRNmTapSCKH%2FNKoY45PvtHl2ag%2F1&X-Amz-Signature=efe8b72b4d7a06f60281bf7f0936bd7ed504516052484feab902e9f2b1d6e136&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f18086e5-5b04-4fbf-8309-8944ab20d213/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665NWBKCVZ%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T010942Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEO%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIA6A1xmBdsNFdIzUWqIhKOD8Ir2MHgadj%2Fhikbw733gkAiAPcFUuNymg6EweGK9xrAZ%2BoyS7Ql8J%2BfVM%2FEXaPyUgCSqIBAj4%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMRpxvavxnmtAfsBKoKtwDbvRUWOuwtMulotQfDtkbvS8SkBxBzsb%2BIFhtSE8LK5arFXBYdVeYe5hKD5%2Fzm%2B%2Ffjee%2BQQiOnZWjPtJJnf%2BIM6ZRlWbJCz2mUKEVqvzRwPr0exSGG8b28EILkClXstzgzF3YZ5339E5OJz43dF9mzE3s1UcGSaOVwGwWvJVXLYudlQr8ZxYlOzm%2BeOoblLI2yL%2F1nV93RSw7EktOUNif%2FVrl%2Fnd%2F9gyBgrGya%2FZb5SdmZCGsXzygEcowrc1fwUuj25EIVfocQSyAtAWl8nflPppZ%2BNxa%2F5P%2FxfH7xW9GVGLfqsxMv%2FGlJ8dY2iCTIzlJNJ4KtGjsqHB4jElWe3aXp5J19%2Fca11gGvLB2oL9BfBdgcx6wart1LGwkNpjvtQPtb0mCTc16d9PGvUBr5i3bI2kWYKBkaGn0JUPdiouu1ZzzSmWVD%2FFWKwumUgUfr5jovso6ukO06MW20211fEbIYVJ5UIigyQF%2FzxKOoctNr4JKCeHy%2FmWcN4YP2eYWf2%2BqfXZLplooCHxGkJ1KHqAyCVu22qCwy30y8KM2c9XakrdiN7EBYWIMwdBsMULcE5D%2BBXwD03jky3aU%2FYGgW9ojxI2MOGt6E%2B5dN7ADPo5QFMsOoST%2FzTVeo9t2h8swy%2BT%2FvAY6pgGHbElHBmGj%2FIGYj2T2R%2BBZ8TRkg9WECWvIa1thj07lgsK1nbLWBDRWZ1nHPeL4JGnsRczbjew8ZmCTKLyrPElamidP%2B5B9AD%2F9pJrWZN1dwAD%2FqegJkKGE1kewYagBVGvSXN7XjVQXJIHc79QtOcSeqYWoj7%2BKEr3%2FBOPOcN1Boq96WO3lOVkogtmyOZRdf5UIMYe6t0c9CtMM0y%2Bcw8ZqhwHCHsJv&X-Amz-Signature=d86af5c48a944afbc2078a8dc44d17587b8e3b19b5d7a816571445817efc16d4&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Correlation Plot
Heatmap visualizes correlations among variables. Color scheme indicates Pearson correlation coefficients. Dark red diagonal line shows perfect correlation (value of 1) between variables and themselves.
This heatmap offers overview of variable relationships and their link with price.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cd3b341e-cc1a-45f7-8aec-cdc00436d270/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665NWBKCVZ%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T010942Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEO%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIA6A1xmBdsNFdIzUWqIhKOD8Ir2MHgadj%2Fhikbw733gkAiAPcFUuNymg6EweGK9xrAZ%2BoyS7Ql8J%2BfVM%2FEXaPyUgCSqIBAj4%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMRpxvavxnmtAfsBKoKtwDbvRUWOuwtMulotQfDtkbvS8SkBxBzsb%2BIFhtSE8LK5arFXBYdVeYe5hKD5%2Fzm%2B%2Ffjee%2BQQiOnZWjPtJJnf%2BIM6ZRlWbJCz2mUKEVqvzRwPr0exSGG8b28EILkClXstzgzF3YZ5339E5OJz43dF9mzE3s1UcGSaOVwGwWvJVXLYudlQr8ZxYlOzm%2BeOoblLI2yL%2F1nV93RSw7EktOUNif%2FVrl%2Fnd%2F9gyBgrGya%2FZb5SdmZCGsXzygEcowrc1fwUuj25EIVfocQSyAtAWl8nflPppZ%2BNxa%2F5P%2FxfH7xW9GVGLfqsxMv%2FGlJ8dY2iCTIzlJNJ4KtGjsqHB4jElWe3aXp5J19%2Fca11gGvLB2oL9BfBdgcx6wart1LGwkNpjvtQPtb0mCTc16d9PGvUBr5i3bI2kWYKBkaGn0JUPdiouu1ZzzSmWVD%2FFWKwumUgUfr5jovso6ukO06MW20211fEbIYVJ5UIigyQF%2FzxKOoctNr4JKCeHy%2FmWcN4YP2eYWf2%2BqfXZLplooCHxGkJ1KHqAyCVu22qCwy30y8KM2c9XakrdiN7EBYWIMwdBsMULcE5D%2BBXwD03jky3aU%2FYGgW9ojxI2MOGt6E%2B5dN7ADPo5QFMsOoST%2FzTVeo9t2h8swy%2BT%2FvAY6pgGHbElHBmGj%2FIGYj2T2R%2BBZ8TRkg9WECWvIa1thj07lgsK1nbLWBDRWZ1nHPeL4JGnsRczbjew8ZmCTKLyrPElamidP%2B5B9AD%2F9pJrWZN1dwAD%2FqegJkKGE1kewYagBVGvSXN7XjVQXJIHc79QtOcSeqYWoj7%2BKEr3%2FBOPOcN1Boq96WO3lOVkogtmyOZRdf5UIMYe6t0c9CtMM0y%2Bcw8ZqhwHCHsJv&X-Amz-Signature=ecdcc69e310a73714db9d61b3417ef73e225aac87b34a4fface3e718f93a4855&X-Amz-SignedHeaders=host&x-id=GetObject)

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
