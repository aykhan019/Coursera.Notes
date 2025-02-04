

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7e6d594d-952e-44b6-97ea-31225882aea6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RYSQHGTV%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T211341Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEB0aCXVzLXdlc3QtMiJIMEYCIQCpqLta5TLvSh9ZXOXNHv%2BdAfhoXpn89HcVsh%2FjnggR2wIhAOXEUskKA%2BSrbe8JTYCo9un0p5KMelHJ148nfOJfZx6sKv8DCDYQABoMNjM3NDIzMTgzODA1IgzzftOO3VUxWlD%2FGmMq3AOeZ3ftZPG%2B%2Fb16f4njavr3V40peynkje1hOIjivkg%2FNOgogHg9PtgU6xlZyny1zhFoSVZyOxucWdVA9hwKF7OTJ9f3V60nynC7ZpO1puaVEhihYHzt89Pwb%2BTGboXIY2df0QkCr88sy%2BZUzG1ZtGEGZa%2B%2Bo0rflhk7%2FJQdRyKqoC6wIijsRtFH7Wul4sWWFEc5Z3KBPrlmpmofzuof3MGmHM6uHrN5l5SYp9A22RkoTl08Gk8YETC5xBFapvmkHMRw1GgTo5bX5%2B7QoaTf6%2B%2BqJlbNk7U1pZ7heuhgKjuNbN1swvGO5rCjhOgB2HB5uqxGr4lhabAkqW7pZ6nzg0qKX7KODRtWgoN1udEj7v9ULImsCQJ5mg%2FOweikiJVhvK5AFUg9QBosvM3a1ekkW%2BgFPOdTslEkCE3kLU%2FrEXgGrrH97qibQ1b8HSILWkeysNvTk5Rf5nt8W1YE8ZrEEiZriSpkl3SCjvVNRVdof1cMOngw6%2BvW1Ww5UAo4ZmCO4eOdp8LSjQSkeBzqca1W9bVfea4RSK0wnMuj0VzRJlmXETpptPeZg2hhBodOCMcRfEzewtee8FRnv9ZHyxiZyOQnxLhaV61iAcnSwXcqcCfovoDbRt12r0Wf77SyNDCv%2FYm9BjqkAZcos1040lkF26qZFHGrUXVk8PQZuiUZ9P6zy%2FMCo%2BySau%2FGnWFqO9loiIvZdhD7lZV%2BSj1d6SmM9ixqmfb78cdL46hZ41SOOGsct8CiuSqB7EFJ0zHlqScvRYRgOdUoreNMjJ8dguDTblnfpX9qdstFqd4fXAZ2mC4VRa7h5gwsexC6fyhIsxVNJRNRD5Hhm2BYgPd%2BEiXJSmDpCTKR7jCmY1mk&X-Amz-Signature=d317e9b395f96cbb5270474f9bd99902e05caf8a0b29d5a40ea0916214e9e4c6&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cbfaed9e-b398-4902-8936-dea058b21def/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RYSQHGTV%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T211341Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEB0aCXVzLXdlc3QtMiJIMEYCIQCpqLta5TLvSh9ZXOXNHv%2BdAfhoXpn89HcVsh%2FjnggR2wIhAOXEUskKA%2BSrbe8JTYCo9un0p5KMelHJ148nfOJfZx6sKv8DCDYQABoMNjM3NDIzMTgzODA1IgzzftOO3VUxWlD%2FGmMq3AOeZ3ftZPG%2B%2Fb16f4njavr3V40peynkje1hOIjivkg%2FNOgogHg9PtgU6xlZyny1zhFoSVZyOxucWdVA9hwKF7OTJ9f3V60nynC7ZpO1puaVEhihYHzt89Pwb%2BTGboXIY2df0QkCr88sy%2BZUzG1ZtGEGZa%2B%2Bo0rflhk7%2FJQdRyKqoC6wIijsRtFH7Wul4sWWFEc5Z3KBPrlmpmofzuof3MGmHM6uHrN5l5SYp9A22RkoTl08Gk8YETC5xBFapvmkHMRw1GgTo5bX5%2B7QoaTf6%2B%2BqJlbNk7U1pZ7heuhgKjuNbN1swvGO5rCjhOgB2HB5uqxGr4lhabAkqW7pZ6nzg0qKX7KODRtWgoN1udEj7v9ULImsCQJ5mg%2FOweikiJVhvK5AFUg9QBosvM3a1ekkW%2BgFPOdTslEkCE3kLU%2FrEXgGrrH97qibQ1b8HSILWkeysNvTk5Rf5nt8W1YE8ZrEEiZriSpkl3SCjvVNRVdof1cMOngw6%2BvW1Ww5UAo4ZmCO4eOdp8LSjQSkeBzqca1W9bVfea4RSK0wnMuj0VzRJlmXETpptPeZg2hhBodOCMcRfEzewtee8FRnv9ZHyxiZyOQnxLhaV61iAcnSwXcqcCfovoDbRt12r0Wf77SyNDCv%2FYm9BjqkAZcos1040lkF26qZFHGrUXVk8PQZuiUZ9P6zy%2FMCo%2BySau%2FGnWFqO9loiIvZdhD7lZV%2BSj1d6SmM9ixqmfb78cdL46hZ41SOOGsct8CiuSqB7EFJ0zHlqScvRYRgOdUoreNMjJ8dguDTblnfpX9qdstFqd4fXAZ2mC4VRa7h5gwsexC6fyhIsxVNJRNRD5Hhm2BYgPd%2BEiXJSmDpCTKR7jCmY1mk&X-Amz-Signature=62f49c96b6fe30295a961b8fccf1e90facf428c0dd4c880762505161a0555d78&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/91181646-b1e0-4433-9711-6259a96a9247/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RYSQHGTV%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T211341Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEB0aCXVzLXdlc3QtMiJIMEYCIQCpqLta5TLvSh9ZXOXNHv%2BdAfhoXpn89HcVsh%2FjnggR2wIhAOXEUskKA%2BSrbe8JTYCo9un0p5KMelHJ148nfOJfZx6sKv8DCDYQABoMNjM3NDIzMTgzODA1IgzzftOO3VUxWlD%2FGmMq3AOeZ3ftZPG%2B%2Fb16f4njavr3V40peynkje1hOIjivkg%2FNOgogHg9PtgU6xlZyny1zhFoSVZyOxucWdVA9hwKF7OTJ9f3V60nynC7ZpO1puaVEhihYHzt89Pwb%2BTGboXIY2df0QkCr88sy%2BZUzG1ZtGEGZa%2B%2Bo0rflhk7%2FJQdRyKqoC6wIijsRtFH7Wul4sWWFEc5Z3KBPrlmpmofzuof3MGmHM6uHrN5l5SYp9A22RkoTl08Gk8YETC5xBFapvmkHMRw1GgTo5bX5%2B7QoaTf6%2B%2BqJlbNk7U1pZ7heuhgKjuNbN1swvGO5rCjhOgB2HB5uqxGr4lhabAkqW7pZ6nzg0qKX7KODRtWgoN1udEj7v9ULImsCQJ5mg%2FOweikiJVhvK5AFUg9QBosvM3a1ekkW%2BgFPOdTslEkCE3kLU%2FrEXgGrrH97qibQ1b8HSILWkeysNvTk5Rf5nt8W1YE8ZrEEiZriSpkl3SCjvVNRVdof1cMOngw6%2BvW1Ww5UAo4ZmCO4eOdp8LSjQSkeBzqca1W9bVfea4RSK0wnMuj0VzRJlmXETpptPeZg2hhBodOCMcRfEzewtee8FRnv9ZHyxiZyOQnxLhaV61iAcnSwXcqcCfovoDbRt12r0Wf77SyNDCv%2FYm9BjqkAZcos1040lkF26qZFHGrUXVk8PQZuiUZ9P6zy%2FMCo%2BySau%2FGnWFqO9loiIvZdhD7lZV%2BSj1d6SmM9ixqmfb78cdL46hZ41SOOGsct8CiuSqB7EFJ0zHlqScvRYRgOdUoreNMjJ8dguDTblnfpX9qdstFqd4fXAZ2mC4VRa7h5gwsexC6fyhIsxVNJRNRD5Hhm2BYgPd%2BEiXJSmDpCTKR7jCmY1mk&X-Amz-Signature=41e1dc981e457cc590923c1c357b2e9fd45b58f29500e80398ce4eabcbc1ee62&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/09aba1c0-0d55-41dd-852a-a04c5b8a3fac/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46665ERDIUK%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T211342Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEB0aCXVzLXdlc3QtMiJIMEYCIQC3QOobjk4WOQwmA92aHDe7%2F6Wvk4iYNq0d0VhD4MMicgIhAPv7BVmiXe6ToqjWK684qVtcqv05DmIqaLTEAn%2FV5brzKv8DCDYQABoMNjM3NDIzMTgzODA1IgziUvrcHHm0%2FGvQHAsq3APj115%2B3N4X%2BIPJ2Dkroh6QJYjh2%2FK6n2%2FNDI2uBykDq799wzFwaa008AeyigfcH99Cj%2Fit0KMd%2Bpbi6QNdhGgGCCYlRzxYqtIXq4WOwFuePOz%2Bad%2B%2Bkoj4Hc4ZbbHB2t57Z6zB01BMPfZ94IjYa3RYeQXFXbiJvTVs5Vq%2F5oeH0vSNLx1rnJ9vbXcDCOsrBbsPXd%2FAeJfGHU2BTdks%2FYClDe7Mc2Xk0815FeQ7qLoTNtBHA5IkuW9LgMUscR1TEEOe2RkZl4ORm4LE1K66vp6LRPEM1yCXMACKSterSlsVzGuPuJSy9NJfoN%2FR26H9jKaosUMOM3GyUsdP236LcfxX5KD%2B0kjXcF2BLWSyTxnIxWYba2cF%2BBB5enr39zK8uZSd9mOjQbY1b7w37dpZYY9LUEUTKRPDCh%2FAknaORWT6kypmZO1uCn08gluDJPKxGflhcHv34rxuGEIdltB3uaxEuoG18dkKrJppUi9gQqh9OggRB%2FehcU%2FA%2FbS9LrEPLvyTb%2BhLfKaqUpF%2Fg35iwJ1o2h5nuimzY2qBVNGEXcqq7SIi0uKrWq4fLIy310Yjyw7zSFQB0Oe39suyF4t%2Bhp0olHZqbhQNdEVZLidv%2FisRozg2UZbhTpmMbUrP6TDE%2FYm9BjqkAQcNshZw9LnRY4uHY572SDSEb3UxDH0KleWqaCHhnG4TL8W7LKUNp5g1V%2BuriD5PiWNfbK9lasL%2BbZpCVtu3jobDn4aIDoEGx0PJoRgwoPbjtIFH0EuFispI%2BVs02qPvhYao82TbaJ01ZebhUujEIuaR4Gc3T56n%2BV3MuDQ%2BhNyP5AeU54qLkiLh6lDT1jLWm8HZluTbI6NZc4pC58Zjx5MuKpQs&X-Amz-Signature=e6e03c89fd43994b33f2c41a926eb4c52eeb8fb02846bf4f48e7ad7bb658cb06&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 2. Scatter Plot
Scatter plots present the relationship between two variables in a dataset. It represents data points on a two-dimensional plane. The independent variable or attribute is plotted on the X-axis, while the dependent variable is plotted on the Y-axis.
**Syntax:**
```python
plt.scatter(x, y)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23708af9-659f-4f23-b626-1a4292d7842c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46665ERDIUK%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T211342Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEB0aCXVzLXdlc3QtMiJIMEYCIQC3QOobjk4WOQwmA92aHDe7%2F6Wvk4iYNq0d0VhD4MMicgIhAPv7BVmiXe6ToqjWK684qVtcqv05DmIqaLTEAn%2FV5brzKv8DCDYQABoMNjM3NDIzMTgzODA1IgziUvrcHHm0%2FGvQHAsq3APj115%2B3N4X%2BIPJ2Dkroh6QJYjh2%2FK6n2%2FNDI2uBykDq799wzFwaa008AeyigfcH99Cj%2Fit0KMd%2Bpbi6QNdhGgGCCYlRzxYqtIXq4WOwFuePOz%2Bad%2B%2Bkoj4Hc4ZbbHB2t57Z6zB01BMPfZ94IjYa3RYeQXFXbiJvTVs5Vq%2F5oeH0vSNLx1rnJ9vbXcDCOsrBbsPXd%2FAeJfGHU2BTdks%2FYClDe7Mc2Xk0815FeQ7qLoTNtBHA5IkuW9LgMUscR1TEEOe2RkZl4ORm4LE1K66vp6LRPEM1yCXMACKSterSlsVzGuPuJSy9NJfoN%2FR26H9jKaosUMOM3GyUsdP236LcfxX5KD%2B0kjXcF2BLWSyTxnIxWYba2cF%2BBB5enr39zK8uZSd9mOjQbY1b7w37dpZYY9LUEUTKRPDCh%2FAknaORWT6kypmZO1uCn08gluDJPKxGflhcHv34rxuGEIdltB3uaxEuoG18dkKrJppUi9gQqh9OggRB%2FehcU%2FA%2FbS9LrEPLvyTb%2BhLfKaqUpF%2Fg35iwJ1o2h5nuimzY2qBVNGEXcqq7SIi0uKrWq4fLIy310Yjyw7zSFQB0Oe39suyF4t%2Bhp0olHZqbhQNdEVZLidv%2FisRozg2UZbhTpmMbUrP6TDE%2FYm9BjqkAQcNshZw9LnRY4uHY572SDSEb3UxDH0KleWqaCHhnG4TL8W7LKUNp5g1V%2BuriD5PiWNfbK9lasL%2BbZpCVtu3jobDn4aIDoEGx0PJoRgwoPbjtIFH0EuFispI%2BVs02qPvhYao82TbaJ01ZebhUujEIuaR4Gc3T56n%2BV3MuDQ%2BhNyP5AeU54qLkiLh6lDT1jLWm8HZluTbI6NZc4pC58Zjx5MuKpQs&X-Amz-Signature=7971e060c39f6f33288e2f655f47b388fe9ea592888ecfece61fdf96cadd3310&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 3. Histogram
A histogram is an important visual representation of data in categorical form. To view the data in a "Binned" form, use the histogram plot with a number of bins required or with the data points that mark the bin edges. The x-axis represents the data bins, and the y-axis represents the number of elements in each bin.
**Syntax:**
```python
plt.hist(x, bins)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/24e4424a-df87-40a1-b63b-195cbdc2e0ab/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46665ERDIUK%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T211342Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEB0aCXVzLXdlc3QtMiJIMEYCIQC3QOobjk4WOQwmA92aHDe7%2F6Wvk4iYNq0d0VhD4MMicgIhAPv7BVmiXe6ToqjWK684qVtcqv05DmIqaLTEAn%2FV5brzKv8DCDYQABoMNjM3NDIzMTgzODA1IgziUvrcHHm0%2FGvQHAsq3APj115%2B3N4X%2BIPJ2Dkroh6QJYjh2%2FK6n2%2FNDI2uBykDq799wzFwaa008AeyigfcH99Cj%2Fit0KMd%2Bpbi6QNdhGgGCCYlRzxYqtIXq4WOwFuePOz%2Bad%2B%2Bkoj4Hc4ZbbHB2t57Z6zB01BMPfZ94IjYa3RYeQXFXbiJvTVs5Vq%2F5oeH0vSNLx1rnJ9vbXcDCOsrBbsPXd%2FAeJfGHU2BTdks%2FYClDe7Mc2Xk0815FeQ7qLoTNtBHA5IkuW9LgMUscR1TEEOe2RkZl4ORm4LE1K66vp6LRPEM1yCXMACKSterSlsVzGuPuJSy9NJfoN%2FR26H9jKaosUMOM3GyUsdP236LcfxX5KD%2B0kjXcF2BLWSyTxnIxWYba2cF%2BBB5enr39zK8uZSd9mOjQbY1b7w37dpZYY9LUEUTKRPDCh%2FAknaORWT6kypmZO1uCn08gluDJPKxGflhcHv34rxuGEIdltB3uaxEuoG18dkKrJppUi9gQqh9OggRB%2FehcU%2FA%2FbS9LrEPLvyTb%2BhLfKaqUpF%2Fg35iwJ1o2h5nuimzY2qBVNGEXcqq7SIi0uKrWq4fLIy310Yjyw7zSFQB0Oe39suyF4t%2Bhp0olHZqbhQNdEVZLidv%2FisRozg2UZbhTpmMbUrP6TDE%2FYm9BjqkAQcNshZw9LnRY4uHY572SDSEb3UxDH0KleWqaCHhnG4TL8W7LKUNp5g1V%2BuriD5PiWNfbK9lasL%2BbZpCVtu3jobDn4aIDoEGx0PJoRgwoPbjtIFH0EuFispI%2BVs02qPvhYao82TbaJ01ZebhUujEIuaR4Gc3T56n%2BV3MuDQ%2BhNyP5AeU54qLkiLh6lDT1jLWm8HZluTbI6NZc4pC58Zjx5MuKpQs&X-Amz-Signature=4bc1f34b13af7b28af591df98c86f4bb19d2d8bdb5208113dde7a32fab04d424&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ab5a6dfe-51f5-43ee-bcb3-33dae4a1c7ad/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46665ERDIUK%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T211342Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEB0aCXVzLXdlc3QtMiJIMEYCIQC3QOobjk4WOQwmA92aHDe7%2F6Wvk4iYNq0d0VhD4MMicgIhAPv7BVmiXe6ToqjWK684qVtcqv05DmIqaLTEAn%2FV5brzKv8DCDYQABoMNjM3NDIzMTgzODA1IgziUvrcHHm0%2FGvQHAsq3APj115%2B3N4X%2BIPJ2Dkroh6QJYjh2%2FK6n2%2FNDI2uBykDq799wzFwaa008AeyigfcH99Cj%2Fit0KMd%2Bpbi6QNdhGgGCCYlRzxYqtIXq4WOwFuePOz%2Bad%2B%2Bkoj4Hc4ZbbHB2t57Z6zB01BMPfZ94IjYa3RYeQXFXbiJvTVs5Vq%2F5oeH0vSNLx1rnJ9vbXcDCOsrBbsPXd%2FAeJfGHU2BTdks%2FYClDe7Mc2Xk0815FeQ7qLoTNtBHA5IkuW9LgMUscR1TEEOe2RkZl4ORm4LE1K66vp6LRPEM1yCXMACKSterSlsVzGuPuJSy9NJfoN%2FR26H9jKaosUMOM3GyUsdP236LcfxX5KD%2B0kjXcF2BLWSyTxnIxWYba2cF%2BBB5enr39zK8uZSd9mOjQbY1b7w37dpZYY9LUEUTKRPDCh%2FAknaORWT6kypmZO1uCn08gluDJPKxGflhcHv34rxuGEIdltB3uaxEuoG18dkKrJppUi9gQqh9OggRB%2FehcU%2FA%2FbS9LrEPLvyTb%2BhLfKaqUpF%2Fg35iwJ1o2h5nuimzY2qBVNGEXcqq7SIi0uKrWq4fLIy310Yjyw7zSFQB0Oe39suyF4t%2Bhp0olHZqbhQNdEVZLidv%2FisRozg2UZbhTpmMbUrP6TDE%2FYm9BjqkAQcNshZw9LnRY4uHY572SDSEb3UxDH0KleWqaCHhnG4TL8W7LKUNp5g1V%2BuriD5PiWNfbK9lasL%2BbZpCVtu3jobDn4aIDoEGx0PJoRgwoPbjtIFH0EuFispI%2BVs02qPvhYao82TbaJ01ZebhUujEIuaR4Gc3T56n%2BV3MuDQ%2BhNyP5AeU54qLkiLh6lDT1jLWm8HZluTbI6NZc4pC58Zjx5MuKpQs&X-Amz-Signature=54c50f6278420038d5fb3aa19c2c788a279e98243121ab5502c3cce98133cb48&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8f1b1d60-cf1b-42b3-9faa-f634c89c3f84/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46665ERDIUK%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T211342Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEB0aCXVzLXdlc3QtMiJIMEYCIQC3QOobjk4WOQwmA92aHDe7%2F6Wvk4iYNq0d0VhD4MMicgIhAPv7BVmiXe6ToqjWK684qVtcqv05DmIqaLTEAn%2FV5brzKv8DCDYQABoMNjM3NDIzMTgzODA1IgziUvrcHHm0%2FGvQHAsq3APj115%2B3N4X%2BIPJ2Dkroh6QJYjh2%2FK6n2%2FNDI2uBykDq799wzFwaa008AeyigfcH99Cj%2Fit0KMd%2Bpbi6QNdhGgGCCYlRzxYqtIXq4WOwFuePOz%2Bad%2B%2Bkoj4Hc4ZbbHB2t57Z6zB01BMPfZ94IjYa3RYeQXFXbiJvTVs5Vq%2F5oeH0vSNLx1rnJ9vbXcDCOsrBbsPXd%2FAeJfGHU2BTdks%2FYClDe7Mc2Xk0815FeQ7qLoTNtBHA5IkuW9LgMUscR1TEEOe2RkZl4ORm4LE1K66vp6LRPEM1yCXMACKSterSlsVzGuPuJSy9NJfoN%2FR26H9jKaosUMOM3GyUsdP236LcfxX5KD%2B0kjXcF2BLWSyTxnIxWYba2cF%2BBB5enr39zK8uZSd9mOjQbY1b7w37dpZYY9LUEUTKRPDCh%2FAknaORWT6kypmZO1uCn08gluDJPKxGflhcHv34rxuGEIdltB3uaxEuoG18dkKrJppUi9gQqh9OggRB%2FehcU%2FA%2FbS9LrEPLvyTb%2BhLfKaqUpF%2Fg35iwJ1o2h5nuimzY2qBVNGEXcqq7SIi0uKrWq4fLIy310Yjyw7zSFQB0Oe39suyF4t%2Bhp0olHZqbhQNdEVZLidv%2FisRozg2UZbhTpmMbUrP6TDE%2FYm9BjqkAQcNshZw9LnRY4uHY572SDSEb3UxDH0KleWqaCHhnG4TL8W7LKUNp5g1V%2BuriD5PiWNfbK9lasL%2BbZpCVtu3jobDn4aIDoEGx0PJoRgwoPbjtIFH0EuFispI%2BVs02qPvhYao82TbaJ01ZebhUujEIuaR4Gc3T56n%2BV3MuDQ%2BhNyP5AeU54qLkiLh6lDT1jLWm8HZluTbI6NZc4pC58Zjx5MuKpQs&X-Amz-Signature=a96feca4744a59b185d613d82a4dc8c63f2370c5fab64eb5580597a03f68add7&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/13ad0497-05fe-4eaa-984e-707b33e14761/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46665ERDIUK%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T211342Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEB0aCXVzLXdlc3QtMiJIMEYCIQC3QOobjk4WOQwmA92aHDe7%2F6Wvk4iYNq0d0VhD4MMicgIhAPv7BVmiXe6ToqjWK684qVtcqv05DmIqaLTEAn%2FV5brzKv8DCDYQABoMNjM3NDIzMTgzODA1IgziUvrcHHm0%2FGvQHAsq3APj115%2B3N4X%2BIPJ2Dkroh6QJYjh2%2FK6n2%2FNDI2uBykDq799wzFwaa008AeyigfcH99Cj%2Fit0KMd%2Bpbi6QNdhGgGCCYlRzxYqtIXq4WOwFuePOz%2Bad%2B%2Bkoj4Hc4ZbbHB2t57Z6zB01BMPfZ94IjYa3RYeQXFXbiJvTVs5Vq%2F5oeH0vSNLx1rnJ9vbXcDCOsrBbsPXd%2FAeJfGHU2BTdks%2FYClDe7Mc2Xk0815FeQ7qLoTNtBHA5IkuW9LgMUscR1TEEOe2RkZl4ORm4LE1K66vp6LRPEM1yCXMACKSterSlsVzGuPuJSy9NJfoN%2FR26H9jKaosUMOM3GyUsdP236LcfxX5KD%2B0kjXcF2BLWSyTxnIxWYba2cF%2BBB5enr39zK8uZSd9mOjQbY1b7w37dpZYY9LUEUTKRPDCh%2FAknaORWT6kypmZO1uCn08gluDJPKxGflhcHv34rxuGEIdltB3uaxEuoG18dkKrJppUi9gQqh9OggRB%2FehcU%2FA%2FbS9LrEPLvyTb%2BhLfKaqUpF%2Fg35iwJ1o2h5nuimzY2qBVNGEXcqq7SIi0uKrWq4fLIy310Yjyw7zSFQB0Oe39suyF4t%2Bhp0olHZqbhQNdEVZLidv%2FisRozg2UZbhTpmMbUrP6TDE%2FYm9BjqkAQcNshZw9LnRY4uHY572SDSEb3UxDH0KleWqaCHhnG4TL8W7LKUNp5g1V%2BuriD5PiWNfbK9lasL%2BbZpCVtu3jobDn4aIDoEGx0PJoRgwoPbjtIFH0EuFispI%2BVs02qPvhYao82TbaJ01ZebhUujEIuaR4Gc3T56n%2BV3MuDQ%2BhNyP5AeU54qLkiLh6lDT1jLWm8HZluTbI6NZc4pC58Zjx5MuKpQs&X-Amz-Signature=f0bd3ae48ca94be0c3e8ddb6b52ec90defd418346bbee2f5fb6b946cb5ccc864&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 2. Box and Whisker Plot
A box plot shows the distribution of quantitative data in a way that facilitates comparisons between variables or across levels of a categorical variable. The box shows the quartiles of the dataset while the whiskers extend to show the rest of the distribution, except for points that are determined to be "outliers".
**Syntax:**
```python
sns.boxplot(x='header_1', y='header_2', data=df)
```
**Example Output:**


![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d207ae92-0a7c-4e2f-aa65-0ee5a2c33bf7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466U76ZUEEH%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T211344Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEB0aCXVzLXdlc3QtMiJHMEUCIQCjH0Gl5Qj1Qq8W99XwHw5SP248E65Od3zTn0bHM88bhAIgaqaK8e5qsjZf6nIm93A3%2FV7BujWQw%2FLkR%2FcBZOUhSRkq%2FwMINhAAGgw2Mzc0MjMxODM4MDUiDPSdYGMiE%2FAB2ncrCCrcAy3kMYe%2F4RKG9JftD6WWqMyFuqOergj4ahqHAeb1UH%2FKtbNPJNBXFFybNDffJe3lNmI8mwxTGnHEuYrMmdDGuysdsNCSIRs2gJ7jTPmGKnpumJLTtnMEu46e4YJQRjB4EAemniOaPgjFYT5trrsnOs0YM5Gsp%2F40S8kIKgkOs03t2WNvJeCEc5TOYPm47pQKkFleblujLkyhOa2Rx6BUjGiFIgfvacbusKCc5erbphCwfN8Ej7vt6SzmlakAKscbnaQ469%2FbLosyJ2m%2BWQFIeWHTjO0fun4ls00O3L3GRgfcJpFqYeV0pA6gMk3mk%2BpTIfoW74mK6U6HpU9UHfFrn%2FwFF6S%2FMsrp8QdEUs6Lr8SDH4N8NFh56cXkr%2FjtqUKyqX0HaL7QbEyjmytBVrRsMTD0Jotl%2FFjpv8x02MrAqA5arXLMV%2Bt0tc5M7L8dD6cPVFlFnyczHAqk2p2JXmlQ2Sn28VBhgstjWxnuOclFc16mLvr6%2BUD62b31nszabVvGNm9A8F6C8f7KnN7LykMuwKjS3GFhQ%2BioApm7fuD3nGHMCu7%2BigCq9Q7yhO5ofmJ%2Bxzz0nKpnyOi8s49v%2FYKWG89VuUo9W%2F8TfYi14LEBkthmroQynaRLdSuyEGbqMMX9ib0GOqUBogsuLo9ogaZQ1vI1NlpCG6z0eZIiYUaEtoM54RobXIzcYtolToL%2Fzz5rUVOyuL8jX4c0sSQfHkQFIYUPkVEMSQuIn4XuBtESFWCSvrUUHEoIZz%2BbHjEYAKz17vor77K9IPoeQeBAuy%2FIwywapAJc7CDK4uz2K2vs2MQ%2F7i%2F%2BWghVj8JV7%2FWjkvxQzKdEJNywY9ma5Ys%2BZ9Qo7I5H4sx655uEm%2B9N&X-Amz-Signature=1fe14e23d418313a572bc80cb641ece8b4b5ce1c685f3fa1b5743f6a5d74f1f7&X-Amz-SignedHeaders=host&x-id=GetObject)

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0e516edc-7551-4792-ab18-0494db3c4c0c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46623GON56J%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T211344Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEB0aCXVzLXdlc3QtMiJGMEQCIGlL10oN8Egas9c2d7k4n%2FEYi3CDauJLVrsJpOKKHUakAiAH4MmR65AwBD0pU8sMzgXUDbbxAGnKXEEdUju4YgHa4Sr%2FAwg2EAAaDDYzNzQyMzE4MzgwNSIMhbYNT2E5qkA3OzSKKtwDDT6FqKzL6FnRGHxrEVXB5VoFoHU7vN%2B8MAL9%2FTqG50HefADk0fhNeUyQzYp7RLVc5ptNQwTKxh%2F7ZBUguU3bjwIbiptuSohqP08uTvDwLk9zecijKXPnj4sjTQmgg1uxy5pJJ1n2%2FS95Cu7AWeJJ1bKPoOz1k9LvSUyz%2FAGAlupINbKiSA%2B5x8U%2F%2B9YIepFBjhqhp4OcdmeJ2Bid3z9AZaBFdr50I4J8dUc%2B%2B2IMMEOuXwOQoNgXiHCHgYE8FgyPFJJWyrhpp1C7Wma05YpRUGN2K8nnQ%2BE3PwnLIVmAV%2BDpkjNWo%2Bvj%2BVbiPEmiVZjKl34O%2FdyS97zC9LkZASqKEi2etNNezXrXPydU0Gt7fvo%2FD6po7mEgc7dQfnZwyAvTKC4aeNrVvQQI7s8HmCP9SnQ8jSqzB1yUnXurgfjdWpPgLi2Nm3e0VwgmOOiGRlrTf5bvZtDM30N8Oo7jBzIRnDEHh7cCHvk7k%2BSOGQ3gTMwWEtMfAnJ7yrdHVkAMFViGYjq8sGXlfdtZIImeZxR66XR1yPYD0EydJ0WLxBOiZ2jTFf56gLWllWhKrZsUGrBbTZzCMcno3CWBjQbQ68CbdRbgmH0M59Z9Ak%2BR%2FnTRB4OfOIi%2B74ySRehi0aMwlP2JvQY6pgF9HmWdG4P%2FTvnIsnhZ8rwjxHmxDiiD1q5HAbYGf7Oeakl2IcsBBZX%2B5J0YzoKCI%2Bwt%2F6xvz%2BbXyG0ySi5CFyqxFiNrs0jqlJ%2Bstxrf1gMhBdodY0Pw%2FYPTSXM%2BpvfK9BsJhZGstymYBoq943QImzYc%2B88lNwvkUHyXGMFmbSeeCWFhXD8qPRdGkGq8gGAOYIWi%2F%2F%2FSlUAdJOUBS7JKGc87pP8c%2F9N3&X-Amz-Signature=0d0ceea6f3fba7c01588d65b204cc0439c776699acecb61800c496ecd083d308&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23a79b9d-2356-49a9-8fd9-65c6b0ab2cc5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46665ERDIUK%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T211342Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEB0aCXVzLXdlc3QtMiJIMEYCIQC3QOobjk4WOQwmA92aHDe7%2F6Wvk4iYNq0d0VhD4MMicgIhAPv7BVmiXe6ToqjWK684qVtcqv05DmIqaLTEAn%2FV5brzKv8DCDYQABoMNjM3NDIzMTgzODA1IgziUvrcHHm0%2FGvQHAsq3APj115%2B3N4X%2BIPJ2Dkroh6QJYjh2%2FK6n2%2FNDI2uBykDq799wzFwaa008AeyigfcH99Cj%2Fit0KMd%2Bpbi6QNdhGgGCCYlRzxYqtIXq4WOwFuePOz%2Bad%2B%2Bkoj4Hc4ZbbHB2t57Z6zB01BMPfZ94IjYa3RYeQXFXbiJvTVs5Vq%2F5oeH0vSNLx1rnJ9vbXcDCOsrBbsPXd%2FAeJfGHU2BTdks%2FYClDe7Mc2Xk0815FeQ7qLoTNtBHA5IkuW9LgMUscR1TEEOe2RkZl4ORm4LE1K66vp6LRPEM1yCXMACKSterSlsVzGuPuJSy9NJfoN%2FR26H9jKaosUMOM3GyUsdP236LcfxX5KD%2B0kjXcF2BLWSyTxnIxWYba2cF%2BBB5enr39zK8uZSd9mOjQbY1b7w37dpZYY9LUEUTKRPDCh%2FAknaORWT6kypmZO1uCn08gluDJPKxGflhcHv34rxuGEIdltB3uaxEuoG18dkKrJppUi9gQqh9OggRB%2FehcU%2FA%2FbS9LrEPLvyTb%2BhLfKaqUpF%2Fg35iwJ1o2h5nuimzY2qBVNGEXcqq7SIi0uKrWq4fLIy310Yjyw7zSFQB0Oe39suyF4t%2Bhp0olHZqbhQNdEVZLidv%2FisRozg2UZbhTpmMbUrP6TDE%2FYm9BjqkAQcNshZw9LnRY4uHY572SDSEb3UxDH0KleWqaCHhnG4TL8W7LKUNp5g1V%2BuriD5PiWNfbK9lasL%2BbZpCVtu3jobDn4aIDoEGx0PJoRgwoPbjtIFH0EuFispI%2BVs02qPvhYao82TbaJ01ZebhUujEIuaR4Gc3T56n%2BV3MuDQ%2BhNyP5AeU54qLkiLh6lDT1jLWm8HZluTbI6NZc4pC58Zjx5MuKpQs&X-Amz-Signature=1e88fa7fd1c0d500d466da61ea336e2d59a1e80dede5ae7de59e5de48bd13fa4&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 4. KDE Plot
A Kernel Density Estimate (KDE) plot is a graph that creates a probability distribution curve for the data based upon its likelihood of occurrence on a specific value. This is created for a single vector of information.
**Syntax:**
```python
sns.kdeplot(X) || sns.kdeplot(df['age'])
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0d571213-2a2f-4921-a50b-880847aa05ee/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46665ERDIUK%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T211342Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEB0aCXVzLXdlc3QtMiJIMEYCIQC3QOobjk4WOQwmA92aHDe7%2F6Wvk4iYNq0d0VhD4MMicgIhAPv7BVmiXe6ToqjWK684qVtcqv05DmIqaLTEAn%2FV5brzKv8DCDYQABoMNjM3NDIzMTgzODA1IgziUvrcHHm0%2FGvQHAsq3APj115%2B3N4X%2BIPJ2Dkroh6QJYjh2%2FK6n2%2FNDI2uBykDq799wzFwaa008AeyigfcH99Cj%2Fit0KMd%2Bpbi6QNdhGgGCCYlRzxYqtIXq4WOwFuePOz%2Bad%2B%2Bkoj4Hc4ZbbHB2t57Z6zB01BMPfZ94IjYa3RYeQXFXbiJvTVs5Vq%2F5oeH0vSNLx1rnJ9vbXcDCOsrBbsPXd%2FAeJfGHU2BTdks%2FYClDe7Mc2Xk0815FeQ7qLoTNtBHA5IkuW9LgMUscR1TEEOe2RkZl4ORm4LE1K66vp6LRPEM1yCXMACKSterSlsVzGuPuJSy9NJfoN%2FR26H9jKaosUMOM3GyUsdP236LcfxX5KD%2B0kjXcF2BLWSyTxnIxWYba2cF%2BBB5enr39zK8uZSd9mOjQbY1b7w37dpZYY9LUEUTKRPDCh%2FAknaORWT6kypmZO1uCn08gluDJPKxGflhcHv34rxuGEIdltB3uaxEuoG18dkKrJppUi9gQqh9OggRB%2FehcU%2FA%2FbS9LrEPLvyTb%2BhLfKaqUpF%2Fg35iwJ1o2h5nuimzY2qBVNGEXcqq7SIi0uKrWq4fLIy310Yjyw7zSFQB0Oe39suyF4t%2Bhp0olHZqbhQNdEVZLidv%2FisRozg2UZbhTpmMbUrP6TDE%2FYm9BjqkAQcNshZw9LnRY4uHY572SDSEb3UxDH0KleWqaCHhnG4TL8W7LKUNp5g1V%2BuriD5PiWNfbK9lasL%2BbZpCVtu3jobDn4aIDoEGx0PJoRgwoPbjtIFH0EuFispI%2BVs02qPvhYao82TbaJ01ZebhUujEIuaR4Gc3T56n%2BV3MuDQ%2BhNyP5AeU54qLkiLh6lDT1jLWm8HZluTbI6NZc4pC58Zjx5MuKpQs&X-Amz-Signature=246252fc44edae4fd890481be9d0757f1286429c79907f4432f4830b92657f97&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/53752550-ef82-4ca9-a01a-09921f0282d0/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46665ERDIUK%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T211342Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEB0aCXVzLXdlc3QtMiJIMEYCIQC3QOobjk4WOQwmA92aHDe7%2F6Wvk4iYNq0d0VhD4MMicgIhAPv7BVmiXe6ToqjWK684qVtcqv05DmIqaLTEAn%2FV5brzKv8DCDYQABoMNjM3NDIzMTgzODA1IgziUvrcHHm0%2FGvQHAsq3APj115%2B3N4X%2BIPJ2Dkroh6QJYjh2%2FK6n2%2FNDI2uBykDq799wzFwaa008AeyigfcH99Cj%2Fit0KMd%2Bpbi6QNdhGgGCCYlRzxYqtIXq4WOwFuePOz%2Bad%2B%2Bkoj4Hc4ZbbHB2t57Z6zB01BMPfZ94IjYa3RYeQXFXbiJvTVs5Vq%2F5oeH0vSNLx1rnJ9vbXcDCOsrBbsPXd%2FAeJfGHU2BTdks%2FYClDe7Mc2Xk0815FeQ7qLoTNtBHA5IkuW9LgMUscR1TEEOe2RkZl4ORm4LE1K66vp6LRPEM1yCXMACKSterSlsVzGuPuJSy9NJfoN%2FR26H9jKaosUMOM3GyUsdP236LcfxX5KD%2B0kjXcF2BLWSyTxnIxWYba2cF%2BBB5enr39zK8uZSd9mOjQbY1b7w37dpZYY9LUEUTKRPDCh%2FAknaORWT6kypmZO1uCn08gluDJPKxGflhcHv34rxuGEIdltB3uaxEuoG18dkKrJppUi9gQqh9OggRB%2FehcU%2FA%2FbS9LrEPLvyTb%2BhLfKaqUpF%2Fg35iwJ1o2h5nuimzY2qBVNGEXcqq7SIi0uKrWq4fLIy310Yjyw7zSFQB0Oe39suyF4t%2Bhp0olHZqbhQNdEVZLidv%2FisRozg2UZbhTpmMbUrP6TDE%2FYm9BjqkAQcNshZw9LnRY4uHY572SDSEb3UxDH0KleWqaCHhnG4TL8W7LKUNp5g1V%2BuriD5PiWNfbK9lasL%2BbZpCVtu3jobDn4aIDoEGx0PJoRgwoPbjtIFH0EuFispI%2BVs02qPvhYao82TbaJ01ZebhUujEIuaR4Gc3T56n%2BV3MuDQ%2BhNyP5AeU54qLkiLh6lDT1jLWm8HZluTbI6NZc4pC58Zjx5MuKpQs&X-Amz-Signature=c65be325e17436bd454ce39fde66372215be5f476587f8a379ac93a51bf13fdd&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
## 4. Correlation Between Variables
Correlation is a statistical measure of the extent to which different variables are interdependent. It indicates how changes in one variable are associated with changes in another variable over time.
### Positive Correlation
Positive correlation indicates that as one variable increases, the other variable also tends to increase.
**Example: Engine Size and Price**
- **Positive Correlation:** Engine size increases, price also increases.
- **Visualization:** Scatter plot with a steep positive slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c7ea9b0-3ef3-4357-a9c3-554fc71b6b15/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TQDBIY22%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T211343Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEB0aCXVzLXdlc3QtMiJHMEUCIGSRKDvXqxVYXt8jfKOuPdM14bVWfsyw9NNZMuqfbtR%2BAiEAi67pfC4p%2BNAd1N7wANTAc91NeShA%2BR5Iinbis9NvPfYq%2FwMINhAAGgw2Mzc0MjMxODM4MDUiDGyptO7CB4fNUXFsqircA0x7r%2FLnmO9VQZHnnxMuGwlQwfQVVliN7FK4NPEo%2BWnEX7iM7Qs2ZN1e%2BiVp7en9NWSxHoegbBZXryUDzSpEz1hhfErbczzkJdzEkVhLDR4OqU%2FAbC%2BGTXbjX7MHySQ0m4YFxXssWoQ6w351P121oZaUgvf%2FUXt71RbfLhL1lnEYaBIO%2BUDbKlqb5gCH1h8YnUizKIbBPxfJ85wBMy7zF6ZuWalB08NrFfiEgv3fDKO7NrRbebSHWOc6SYKSONTN6%2FboMTxwhqeSBwpHu6BIrLNn7hw2LTmtdHYs5bGnmOUy6a9ZztbCHATOna%2BwJl%2BpZT9y2qzgjj07ej9Jo0oN5Yg9No%2BmHGOANh7AR4bV4dqmfQytNdicmjGh8ujvtrrD8Qg8G9HS88r58mOYSrq2%2BR5XxdPpNu2kGs5xhvfAq3yfLB0FL%2BWYjtHG2IVpAoQSiFIW7vBfY54L2M9tzK724wMV4GOViBtRiolqgSSDNn1vaRz2vybLVxIRZvnlVTTohETQSoCNy1VDdyJlrvbWOyGSO2xooiNUgzhXSuV8OUcbLoFjPyvsw%2F6RLIWxGRo6qM3Kg9E3al7RdG5Nju8lf7Aft6jIuUcDjSlklqOEYhSrwyuA0cGroO2tA9V4MPb8ib0GOqUBNUDcH9GygVB8nkGZpk4M5NnmmKv4XwFT%2F2QpuelIZEKEj51GEpU56ocfehXpg%2BVkVqqiQokiZ3o%2Bxrsqll518k4mdBJ6nQjSXfSP1oV941MgJEaKHs6k2pWpUsBKvzo2E3AfH22Q5EZTRxVAJmg%2BnhGzHZ6EtjCCWV2jJDbtM7dX3tSeLF5Bb1sfwLxXDWfFz9iXV7eWlDawda5gjNImSQ7qMbjc&X-Amz-Signature=73b4cb22f22599c70712a076c6fcbc0c5e31c4c5777027ded52334a3015b2cf3&X-Amz-SignedHeaders=host&x-id=GetObject)
**Explanation:** When engine size increases, there is a corresponding increase in the price of the vehicle. This positive correlation suggests that larger engines tend to be associated with higher prices in the market.
___
### Negative Correlation
Negative correlation indicates that as one variable increases, the other variable tends to decrease.
**Example: Highway Miles per Gallon and Price**
- **Negative Correlation:** As highway miles per gallon increases, price decreases.
- **Visualization:** Scatter plot with a steep negative slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/10f1f798-9cc4-4df2-a9c1-5a339f554a0b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666MK5EWKU%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T211343Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEB0aCXVzLXdlc3QtMiJHMEUCIE6cFewSoatwvPTraIUPC%2FHELsAIv52bjYlTFln75buKAiEA7KjMLHdE6btuYns8WggWWvIpf2%2Bupoj4YqMaM8eamQkq%2FwMINhAAGgw2Mzc0MjMxODM4MDUiDDOXCfM3vVlPDEPGaCrcA7cvoo1w%2FethWF5aN4YZx0GFexVhqoZofkkFfWAWaRkm2hod1SCjHOPEt62391Bzj1w6B2bWus6zJdi%2Bp89dO%2BUjNyq3GULaExjV1vV6iqIRqps%2FMrS7lul8gKCqVFy%2BQ4WpT2Guir4aj1hrCEYLJ%2BkUDflhtQ%2B7tIiRvmLWHJnoACMDctG4GfOpCSsGgbTQAakGMlmOsMy621holzHVnZRTAfbnmfPEpx3ZgV99OYSXgSLq8tzgmGp2jdMJ5utD2SVVGW70tOQMCNkgcP2hLuSgHYUULyxs7eLN58%2BktVkNIDDOYrJnpQnGEJNDUrZcenPZryv6m1yiUQ70CdU0nRCUhPIknnyyft7hFTz8urRssAdjY0aofzZ6n%2BTq9hQ09BXpNZAx2M91zFaY8lsSDzTBBjh3U8sFH6KexPvxqVmUsTv4P%2BEGH5ZY7c3MOiiDclw%2BWoNWEkLLzf1CmJ04D%2BDOGDr6j1vJLqQ56uZGvLK0ubViyhTqsA1Pc2D6Z2b3u3jCjFwryZZ7qAWtNgm4ASVqJz%2By4ZxsUDJpTc9Ev8FnN%2Fo6AAssuU%2FD9PR%2BuW%2FYfThm28kDwix%2BbOhP239EFafSG7kYaYM%2FvawC53THj%2BErITxpcFx6q13BkhwHMOn9ib0GOqUBjuqLA6w9SAZLF6YF8K5WiVVLXEzDqAFIr%2FEpXmmB49En3sfm3CJjoHTnL4oC7UsI1h1gVrtAXDJYMe4hhvJNfCGfoqUNcswd0m62KvS%2BySMXxX9GQTdH1vajD4NdWrkDuR74smeN0uJUDuJ9Yv%2FNLQ1aAPevAiX2J7BrPwYRenBQ8zZJyTJjpgCc%2FCVzA9I90jEL7PnL0RQrb6UUWGoEFmO64bw%2B&X-Amz-Signature=d7434469ba8e9cc2ffa51157a49dbf49a7837fb4834206e743308a34702fe5d2&X-Amz-SignedHeaders=host&x-id=GetObject)
**Explanation:** When highway miles per gallon increases, the price of the vehicle tends to decrease. This negative correlation suggests that cars with higher fuel efficiency (more miles per gallon) are generally priced lower in the market.
___
### Weak Correlation
Weak correlation indicates a lack of strong relationship between the variables.
**Example: RPM and Price**
- **Weak Correlation:** Low and high RPM values show varied prices, indicating no strong predictive relationship.
- **Visualization:** Scatter plot with no clear trend or slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9f914514-8914-4bf4-ac84-d9e3077f6eb1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665CN3ZCXT%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T211343Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEB0aCXVzLXdlc3QtMiJHMEUCIDMJKxlwmMlus0nUiqhIwLW8luUvHgt4YzbhgxgWKJyhAiEA8ztEeKQ9n4eccElXa%2F%2Fi%2FWLGWT4%2BezEaXpP1m0eFG5oq%2FwMINhAAGgw2Mzc0MjMxODM4MDUiDP%2BoBcKx7U%2FTqjBfDyrcA26vU8r%2BK9OALXYfgOuCrLhRqUsr79IvvXbG4xCQAv5EPoeI0y9%2BnF3CWPapxEi4umpfoEbnsxbdwUKWKPdSG91bqmt1Lh5Of3JT%2BJsxiAO1U8CALzJr5sBprwbM1ISCmo4li2AQMyBkCzjJ1%2BcaD%2F1eJZ49zPGt3STd1qh%2BR5XUKhh3MRxGcmHilYXyFmxPYup9w%2FvDL0vWIzxxpRJc4NcgAf5tiWdRjg0QntYv4pu4WoByeiR1t1vEnLAPxOGbsO6lYucBh7NqQSYKAszT91S95Um8kToTNVNfvQZ0PFjLVLjmXQhSmdRseiuwbFIdYgTI4elBkoFxwqkaXhC5br4Rm9ULWROAd0uWiyD%2FV62tJ4NYtTVYkzME1cwdrfF%2BSiDVEZ2P6O0R8Aqkpt%2BmEpCpWSdrjEbrWSntP9T7JH4DdgqORo3uqX5hA5Swu2i5%2F5EcTRtcQ3tVICuGPWP89TujBOLON9T0SODeIUnA%2FkPJ4ZPoH2lvakGaYdCYgImfbE9Hu0rSOotrpF8tuFloK3%2BzKe5Vitx7Yi0PwWhdG3z1WQ8N6oEWFUro%2BbjFAMvwlDPKo0%2BSZHzKXJ9uHcicqmdZSzRzRQ7dwbCaIWWtLN35YE4E3Bi6USnW8o9wMNX8ib0GOqUB6yH9tuoQG4eL8UAAo4uLOWpP%2F9i%2BV0%2Bv95AqYTBPQtSIxq8L%2Fe9J7CERhrZq92qw1kd03pQ31b2HSH%2F3Qnqgiu9kBXpDs3gzjbh75QozR7QXXVWYLnDKdlagSpfgeHmGOIBi6UN6pWds4FqzcFYnnMDFv4%2FDkEd%2BOYPoOXasLqSg0qdXiwEKB%2FIe%2FX8K0lAIPbUyIkFdungeW4ov9%2FFLIEERxLkm&X-Amz-Signature=aea5ebfc15466735a3d1637423ef63e551658684a295b64f5717a65885c03b16&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f18086e5-5b04-4fbf-8309-8944ab20d213/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664KH7MQPC%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T211343Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEB0aCXVzLXdlc3QtMiJIMEYCIQCA6YLDtf1he264JtUf3Wn7jZCnqcT3ox%2FWlbbJs0dmCwIhALUtnt9FKlELb8U6dUJXEAXUy5RZ98Jf%2FA%2FjBP5si4BXKv8DCDYQABoMNjM3NDIzMTgzODA1IgwcClnr9gUBhBmf2nwq3AMjvyRygXv0hMBmOVDL0MGdpX9kXeuGWRrJ8axoERqTBZbDDlozt9VBHFiYmp16Mszg4GaOuj%2BOZUXSD69gxhFJM66SM%2Fk67%2BHCZJweaX3Xf%2BsBm6D8lkrgKcS4UDBe2HsHk%2Fa8hM9pDtZdA8aBf21PO5am3LbdnElINBnBipLHdVrxFpyrOLc%2Ba7TF%2FwesbmmoltlZ7zP9p4pMvU1yQ%2BJn6czrN4KPUH83EAkjbynYgx4do5HIFizIWO8fcf6BIrFovTOaR14LUyRHhla9UbhVZqqAmhdR3VGbEhaqyKtO405MoaGYHTBCPVDK9ygxfLiqAdIldaGtegtzHCnHeki3oyTAhut3a8W8778tiWUvqi9KzLz8qwVy7O2uIlgt%2BRzVzpVgTEX6kPBz1E%2FmiuvrBMJsg7sKuL%2FPy8fEHUtmohFxBdXI7X0waXY59uiz1L91zW6IaSrsrPOzoybMYC979zuBWQ308paizZmrI1E3OI26Lz0ZLvLibvGyW5Rx96n5W2Ww8VlbcgRc0kLqQ10xfsf987%2BOf74EHtJA4IalEffeDpBTv%2F1DOQ0hnyRYbccOA4rZtw19wormo77pVnAUjO%2BoapVXfwuKebzLmuXjHNfMb4nvBYI9URXJ7zDX%2FIm9BjqkAdFKCAIOXL4oReuCua1SYNvxPO6mGylyMPZ76ZmtFwWwr1Zh0CSmYU5YVaeerre3%2FdCtBAjRWGGiGu7uSFz3gT%2BvJ4VGtZdVzQsSKIyoBystk0nA47q%2FII1rZMc0VTCep8QxsMXOD30zUeGHLuaNvTBak313bodxUI2i%2FcWaSCvy0NLExYMdfOLXmb2yvZn4XtSS8RAZzSWripGaLg8Y1mQJ5woD&X-Amz-Signature=9aa0ac1634811ed3cec99bee18ef5c9659fcd4b2cb5cb7efcbfbf5073292b94c&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Correlation Plot
Heatmap visualizes correlations among variables. Color scheme indicates Pearson correlation coefficients. Dark red diagonal line shows perfect correlation (value of 1) between variables and themselves.
This heatmap offers overview of variable relationships and their link with price.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cd3b341e-cc1a-45f7-8aec-cdc00436d270/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664KH7MQPC%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T211343Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEB0aCXVzLXdlc3QtMiJIMEYCIQCA6YLDtf1he264JtUf3Wn7jZCnqcT3ox%2FWlbbJs0dmCwIhALUtnt9FKlELb8U6dUJXEAXUy5RZ98Jf%2FA%2FjBP5si4BXKv8DCDYQABoMNjM3NDIzMTgzODA1IgwcClnr9gUBhBmf2nwq3AMjvyRygXv0hMBmOVDL0MGdpX9kXeuGWRrJ8axoERqTBZbDDlozt9VBHFiYmp16Mszg4GaOuj%2BOZUXSD69gxhFJM66SM%2Fk67%2BHCZJweaX3Xf%2BsBm6D8lkrgKcS4UDBe2HsHk%2Fa8hM9pDtZdA8aBf21PO5am3LbdnElINBnBipLHdVrxFpyrOLc%2Ba7TF%2FwesbmmoltlZ7zP9p4pMvU1yQ%2BJn6czrN4KPUH83EAkjbynYgx4do5HIFizIWO8fcf6BIrFovTOaR14LUyRHhla9UbhVZqqAmhdR3VGbEhaqyKtO405MoaGYHTBCPVDK9ygxfLiqAdIldaGtegtzHCnHeki3oyTAhut3a8W8778tiWUvqi9KzLz8qwVy7O2uIlgt%2BRzVzpVgTEX6kPBz1E%2FmiuvrBMJsg7sKuL%2FPy8fEHUtmohFxBdXI7X0waXY59uiz1L91zW6IaSrsrPOzoybMYC979zuBWQ308paizZmrI1E3OI26Lz0ZLvLibvGyW5Rx96n5W2Ww8VlbcgRc0kLqQ10xfsf987%2BOf74EHtJA4IalEffeDpBTv%2F1DOQ0hnyRYbccOA4rZtw19wormo77pVnAUjO%2BoapVXfwuKebzLmuXjHNfMb4nvBYI9URXJ7zDX%2FIm9BjqkAdFKCAIOXL4oReuCua1SYNvxPO6mGylyMPZ76ZmtFwWwr1Zh0CSmYU5YVaeerre3%2FdCtBAjRWGGiGu7uSFz3gT%2BvJ4VGtZdVzQsSKIyoBystk0nA47q%2FII1rZMc0VTCep8QxsMXOD30zUeGHLuaNvTBak313bodxUI2i%2FcWaSCvy0NLExYMdfOLXmb2yvZn4XtSS8RAZzSWripGaLg8Y1mQJ5woD&X-Amz-Signature=55b4000542f0ccc8c74ff098c0cdff7fdc07aad1ff028b24674239dad64f6b93&X-Amz-SignedHeaders=host&x-id=GetObject)

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
