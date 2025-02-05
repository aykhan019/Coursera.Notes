

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7e6d594d-952e-44b6-97ea-31225882aea6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R2KEYVTK%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T041753Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECAaCXVzLXdlc3QtMiJHMEUCIQD0s2IxItOyHLT8f0PXU0ueUovbyW3yr4BRqIxOjYi1JgIgWkaoppoRsF8UBnvgWN6wZM1wNmoXBN%2FrvOPdiIG3gSMq%2FwMIORAAGgw2Mzc0MjMxODM4MDUiDIwFu6xVRO5tt2mD8yrcAyqTemomf29UGG%2B6uWlzx37xN1PedJPjV4CDYsrwgerkbdYQ1lr%2FQ95VcPOR%2BjBs5DtaiJxQJ3jRvws%2Bm%2F9xWjYinKh6Q2axPJrgulZylS%2FGJqkqKzEnDRaCDzsyEKNi4nDwILv%2F8nzGUIn8d2LB8%2FfsQ2n4ClhFsaTTPeT10jGVQtQlRuVOOYkBQtVkQiRxSpLJfyWOjuGdlLly8AXoXs3x%2B9ACnysQwr2jIWXDNT4LzvNCgaceBhap%2FQaiZkxFb5gSHOSuTo2VdVemo7VgziDFvWE0X4TJqsPn8LxEHfgFTXUd%2BraU0xeWpqVYljzT0c%2BuPKfza%2FagYZIPjOlVxvvdjgj79PSU0Df9zginZ7OIMxCKurC58ZVZd9%2BgQDvKc%2FvXLN2LZe6BIP8Zg%2FdK%2Fd41p%2FillN6kLYiRFeqXe7ue7wJ%2Fo2xzISLTDJ6bEwLbRkhD%2BQsyEKkWiP0i3e0Dcm%2FgqtlswXGNDQVf2dNVLkpOkV9W2unA4CI0hwVg7wXJDO%2B5YTjzE3c4KzuG0KkHnAm%2BNm0WHE352nmeK5BPeFVMW0d5bUbqEjqJ3AdwBc%2FTDLGe4NzmT1ijL1JDXq9wlEv8vz07EZjPQrdAcv7l0%2FGeuSFV4aB3I%2FwK9GLvMNrNir0GOqUBiurnwpUTDRDXzhHxa%2BYOoFbVmU0KgFW36HCwefShd%2Fjl0YzwtvofTqNUbAonzhl6mec5Ssp%2F8pbl5iJNhU63N3xsicjDSpLKKEL62rdh2mdhZUhJCHgLmLnrVl7rj24ydCIvZ1DkdRvuHrffDyCeOlklnG%2F6SQbNvQqcUTwIEop%2FdN7Vb%2BkAi1HKOje2ki4vLtC3Ju45qUDLbfPjWTbb2YcJ7RHd&X-Amz-Signature=682f737508394b3b060a759c2be55717403c4db467e17181c65e8111394cbb2b&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cbfaed9e-b398-4902-8936-dea058b21def/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R2KEYVTK%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T041753Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECAaCXVzLXdlc3QtMiJHMEUCIQD0s2IxItOyHLT8f0PXU0ueUovbyW3yr4BRqIxOjYi1JgIgWkaoppoRsF8UBnvgWN6wZM1wNmoXBN%2FrvOPdiIG3gSMq%2FwMIORAAGgw2Mzc0MjMxODM4MDUiDIwFu6xVRO5tt2mD8yrcAyqTemomf29UGG%2B6uWlzx37xN1PedJPjV4CDYsrwgerkbdYQ1lr%2FQ95VcPOR%2BjBs5DtaiJxQJ3jRvws%2Bm%2F9xWjYinKh6Q2axPJrgulZylS%2FGJqkqKzEnDRaCDzsyEKNi4nDwILv%2F8nzGUIn8d2LB8%2FfsQ2n4ClhFsaTTPeT10jGVQtQlRuVOOYkBQtVkQiRxSpLJfyWOjuGdlLly8AXoXs3x%2B9ACnysQwr2jIWXDNT4LzvNCgaceBhap%2FQaiZkxFb5gSHOSuTo2VdVemo7VgziDFvWE0X4TJqsPn8LxEHfgFTXUd%2BraU0xeWpqVYljzT0c%2BuPKfza%2FagYZIPjOlVxvvdjgj79PSU0Df9zginZ7OIMxCKurC58ZVZd9%2BgQDvKc%2FvXLN2LZe6BIP8Zg%2FdK%2Fd41p%2FillN6kLYiRFeqXe7ue7wJ%2Fo2xzISLTDJ6bEwLbRkhD%2BQsyEKkWiP0i3e0Dcm%2FgqtlswXGNDQVf2dNVLkpOkV9W2unA4CI0hwVg7wXJDO%2B5YTjzE3c4KzuG0KkHnAm%2BNm0WHE352nmeK5BPeFVMW0d5bUbqEjqJ3AdwBc%2FTDLGe4NzmT1ijL1JDXq9wlEv8vz07EZjPQrdAcv7l0%2FGeuSFV4aB3I%2FwK9GLvMNrNir0GOqUBiurnwpUTDRDXzhHxa%2BYOoFbVmU0KgFW36HCwefShd%2Fjl0YzwtvofTqNUbAonzhl6mec5Ssp%2F8pbl5iJNhU63N3xsicjDSpLKKEL62rdh2mdhZUhJCHgLmLnrVl7rj24ydCIvZ1DkdRvuHrffDyCeOlklnG%2F6SQbNvQqcUTwIEop%2FdN7Vb%2BkAi1HKOje2ki4vLtC3Ju45qUDLbfPjWTbb2YcJ7RHd&X-Amz-Signature=9981d7adcdeacc7c818d91abaae2d7878e0a2c144ebccec0acc5343be9e313fe&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/91181646-b1e0-4433-9711-6259a96a9247/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R2KEYVTK%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T041753Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECAaCXVzLXdlc3QtMiJHMEUCIQD0s2IxItOyHLT8f0PXU0ueUovbyW3yr4BRqIxOjYi1JgIgWkaoppoRsF8UBnvgWN6wZM1wNmoXBN%2FrvOPdiIG3gSMq%2FwMIORAAGgw2Mzc0MjMxODM4MDUiDIwFu6xVRO5tt2mD8yrcAyqTemomf29UGG%2B6uWlzx37xN1PedJPjV4CDYsrwgerkbdYQ1lr%2FQ95VcPOR%2BjBs5DtaiJxQJ3jRvws%2Bm%2F9xWjYinKh6Q2axPJrgulZylS%2FGJqkqKzEnDRaCDzsyEKNi4nDwILv%2F8nzGUIn8d2LB8%2FfsQ2n4ClhFsaTTPeT10jGVQtQlRuVOOYkBQtVkQiRxSpLJfyWOjuGdlLly8AXoXs3x%2B9ACnysQwr2jIWXDNT4LzvNCgaceBhap%2FQaiZkxFb5gSHOSuTo2VdVemo7VgziDFvWE0X4TJqsPn8LxEHfgFTXUd%2BraU0xeWpqVYljzT0c%2BuPKfza%2FagYZIPjOlVxvvdjgj79PSU0Df9zginZ7OIMxCKurC58ZVZd9%2BgQDvKc%2FvXLN2LZe6BIP8Zg%2FdK%2Fd41p%2FillN6kLYiRFeqXe7ue7wJ%2Fo2xzISLTDJ6bEwLbRkhD%2BQsyEKkWiP0i3e0Dcm%2FgqtlswXGNDQVf2dNVLkpOkV9W2unA4CI0hwVg7wXJDO%2B5YTjzE3c4KzuG0KkHnAm%2BNm0WHE352nmeK5BPeFVMW0d5bUbqEjqJ3AdwBc%2FTDLGe4NzmT1ijL1JDXq9wlEv8vz07EZjPQrdAcv7l0%2FGeuSFV4aB3I%2FwK9GLvMNrNir0GOqUBiurnwpUTDRDXzhHxa%2BYOoFbVmU0KgFW36HCwefShd%2Fjl0YzwtvofTqNUbAonzhl6mec5Ssp%2F8pbl5iJNhU63N3xsicjDSpLKKEL62rdh2mdhZUhJCHgLmLnrVl7rj24ydCIvZ1DkdRvuHrffDyCeOlklnG%2F6SQbNvQqcUTwIEop%2FdN7Vb%2BkAi1HKOje2ki4vLtC3Ju45qUDLbfPjWTbb2YcJ7RHd&X-Amz-Signature=fedf68132407448524d9a9ed5ef790f8d96e1ff03ecc59afc0cb7ae1f0c0f520&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/09aba1c0-0d55-41dd-852a-a04c5b8a3fac/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666QKP2FWX%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T041754Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECAaCXVzLXdlc3QtMiJGMEQCIDLDA5TBBw1GFEEsEVpyUL7hjMKxp0ZGYTCwOAh5w%2FXTAiBMq8deDJlg04bsitDwL74AAO4492pgqIC1rNllOR9LKyr%2FAwg5EAAaDDYzNzQyMzE4MzgwNSIMQeCYVANXeN9DzlydKtwDB9oIBzqGJ56ukr0Wjo6C4YgF9df2ALbfRx93HmGM0b0N%2BUpDC%2B0mTmj%2FWQBVFOpg2mnyzSf47hG18uSJ50vCK4QAf%2FtuaRB%2FogqBiNZt1Lz6o8VrpNjwiayAxknlSdVduhtQ3vTF3CUtdJBoVcqSlOKXi8lpPwIo%2BlHgePwIEUNlQUJwdw9ZASbh9r8Aowx8DKSNuNdM7jxpGNAekaeLjPNMV3f5Y5TuIMMN%2FQbssJgR90Zc0cxpac5TaZHRmgryySArxtM0HEESKPnYHjFVfTkOSH1HjjWalJFjhVmr6Pw2bDU4dsKiCdMq62jd8QyXAOKYPSjBQLE7iwKPrCnOs8VQ%2BtpAQbU0rlSZeXfkT43CDaOea%2FH%2BQ2DZXXb9XGqlgjd53dn1Rkt%2F1TqB71FZVj05OZQHL%2BuSDu3pTwjY2lmHkBuZNnjDxVXULV10PVG8NcISi0TNR3DG6Y6pM1MamZjUcMW%2FjL9giu6DZLcoFi7yBLxcW%2FK7%2Burkrk3nGKP%2BXRUOtL2EzSc%2FPcQOLq0ZCRx7UhaV9WC3esx%2FFQRb4wdPKtj8ooObKEsTMuApSz43GFosEe1cMP4hxvQaSQ1BNtPXsfv2UcPwYWmjHrExGTQyptSqxdrzNIUM32Uw8MyKvQY6pgHE7Vg%2FG%2Bunp3C1ZQSnDwbEnR34bPOJSvlR9D5gkdH%2Fia5xddNW07TG%2B0Dmhw0Ei4%2BMg7zyPYI8l%2BX27Fhcdf9Nvs1AUIIqbxznio9CH24QSFHlbfsUo116KnX4uN804GtlOSouGvW1%2F6AgDPONJNpvFm9jw6PaJfm6JXis2zUC2NtL4Tm8Kb53DCC9fQBp24uITlmSyIZ4qwn7JMiDK602xSOMbOsu&X-Amz-Signature=62dbb2b0d5699ff2d8a1667658690bf7319bc3db7b136438826b55a50f1e0bd5&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 2. Scatter Plot
Scatter plots present the relationship between two variables in a dataset. It represents data points on a two-dimensional plane. The independent variable or attribute is plotted on the X-axis, while the dependent variable is plotted on the Y-axis.
**Syntax:**
```python
plt.scatter(x, y)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23708af9-659f-4f23-b626-1a4292d7842c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666QKP2FWX%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T041754Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECAaCXVzLXdlc3QtMiJGMEQCIDLDA5TBBw1GFEEsEVpyUL7hjMKxp0ZGYTCwOAh5w%2FXTAiBMq8deDJlg04bsitDwL74AAO4492pgqIC1rNllOR9LKyr%2FAwg5EAAaDDYzNzQyMzE4MzgwNSIMQeCYVANXeN9DzlydKtwDB9oIBzqGJ56ukr0Wjo6C4YgF9df2ALbfRx93HmGM0b0N%2BUpDC%2B0mTmj%2FWQBVFOpg2mnyzSf47hG18uSJ50vCK4QAf%2FtuaRB%2FogqBiNZt1Lz6o8VrpNjwiayAxknlSdVduhtQ3vTF3CUtdJBoVcqSlOKXi8lpPwIo%2BlHgePwIEUNlQUJwdw9ZASbh9r8Aowx8DKSNuNdM7jxpGNAekaeLjPNMV3f5Y5TuIMMN%2FQbssJgR90Zc0cxpac5TaZHRmgryySArxtM0HEESKPnYHjFVfTkOSH1HjjWalJFjhVmr6Pw2bDU4dsKiCdMq62jd8QyXAOKYPSjBQLE7iwKPrCnOs8VQ%2BtpAQbU0rlSZeXfkT43CDaOea%2FH%2BQ2DZXXb9XGqlgjd53dn1Rkt%2F1TqB71FZVj05OZQHL%2BuSDu3pTwjY2lmHkBuZNnjDxVXULV10PVG8NcISi0TNR3DG6Y6pM1MamZjUcMW%2FjL9giu6DZLcoFi7yBLxcW%2FK7%2Burkrk3nGKP%2BXRUOtL2EzSc%2FPcQOLq0ZCRx7UhaV9WC3esx%2FFQRb4wdPKtj8ooObKEsTMuApSz43GFosEe1cMP4hxvQaSQ1BNtPXsfv2UcPwYWmjHrExGTQyptSqxdrzNIUM32Uw8MyKvQY6pgHE7Vg%2FG%2Bunp3C1ZQSnDwbEnR34bPOJSvlR9D5gkdH%2Fia5xddNW07TG%2B0Dmhw0Ei4%2BMg7zyPYI8l%2BX27Fhcdf9Nvs1AUIIqbxznio9CH24QSFHlbfsUo116KnX4uN804GtlOSouGvW1%2F6AgDPONJNpvFm9jw6PaJfm6JXis2zUC2NtL4Tm8Kb53DCC9fQBp24uITlmSyIZ4qwn7JMiDK602xSOMbOsu&X-Amz-Signature=b254ad20d3a86d1ef1d71099136b23cb316ae0b09fc9399ab58e62f4a89a4acf&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 3. Histogram
A histogram is an important visual representation of data in categorical form. To view the data in a "Binned" form, use the histogram plot with a number of bins required or with the data points that mark the bin edges. The x-axis represents the data bins, and the y-axis represents the number of elements in each bin.
**Syntax:**
```python
plt.hist(x, bins)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/24e4424a-df87-40a1-b63b-195cbdc2e0ab/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666QKP2FWX%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T041754Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECAaCXVzLXdlc3QtMiJGMEQCIDLDA5TBBw1GFEEsEVpyUL7hjMKxp0ZGYTCwOAh5w%2FXTAiBMq8deDJlg04bsitDwL74AAO4492pgqIC1rNllOR9LKyr%2FAwg5EAAaDDYzNzQyMzE4MzgwNSIMQeCYVANXeN9DzlydKtwDB9oIBzqGJ56ukr0Wjo6C4YgF9df2ALbfRx93HmGM0b0N%2BUpDC%2B0mTmj%2FWQBVFOpg2mnyzSf47hG18uSJ50vCK4QAf%2FtuaRB%2FogqBiNZt1Lz6o8VrpNjwiayAxknlSdVduhtQ3vTF3CUtdJBoVcqSlOKXi8lpPwIo%2BlHgePwIEUNlQUJwdw9ZASbh9r8Aowx8DKSNuNdM7jxpGNAekaeLjPNMV3f5Y5TuIMMN%2FQbssJgR90Zc0cxpac5TaZHRmgryySArxtM0HEESKPnYHjFVfTkOSH1HjjWalJFjhVmr6Pw2bDU4dsKiCdMq62jd8QyXAOKYPSjBQLE7iwKPrCnOs8VQ%2BtpAQbU0rlSZeXfkT43CDaOea%2FH%2BQ2DZXXb9XGqlgjd53dn1Rkt%2F1TqB71FZVj05OZQHL%2BuSDu3pTwjY2lmHkBuZNnjDxVXULV10PVG8NcISi0TNR3DG6Y6pM1MamZjUcMW%2FjL9giu6DZLcoFi7yBLxcW%2FK7%2Burkrk3nGKP%2BXRUOtL2EzSc%2FPcQOLq0ZCRx7UhaV9WC3esx%2FFQRb4wdPKtj8ooObKEsTMuApSz43GFosEe1cMP4hxvQaSQ1BNtPXsfv2UcPwYWmjHrExGTQyptSqxdrzNIUM32Uw8MyKvQY6pgHE7Vg%2FG%2Bunp3C1ZQSnDwbEnR34bPOJSvlR9D5gkdH%2Fia5xddNW07TG%2B0Dmhw0Ei4%2BMg7zyPYI8l%2BX27Fhcdf9Nvs1AUIIqbxznio9CH24QSFHlbfsUo116KnX4uN804GtlOSouGvW1%2F6AgDPONJNpvFm9jw6PaJfm6JXis2zUC2NtL4Tm8Kb53DCC9fQBp24uITlmSyIZ4qwn7JMiDK602xSOMbOsu&X-Amz-Signature=c44b4d24e1abdc16cbbf2d41c8bdb657ad57172253e36f87bbc570832e59ab1d&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ab5a6dfe-51f5-43ee-bcb3-33dae4a1c7ad/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666QKP2FWX%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T041754Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECAaCXVzLXdlc3QtMiJGMEQCIDLDA5TBBw1GFEEsEVpyUL7hjMKxp0ZGYTCwOAh5w%2FXTAiBMq8deDJlg04bsitDwL74AAO4492pgqIC1rNllOR9LKyr%2FAwg5EAAaDDYzNzQyMzE4MzgwNSIMQeCYVANXeN9DzlydKtwDB9oIBzqGJ56ukr0Wjo6C4YgF9df2ALbfRx93HmGM0b0N%2BUpDC%2B0mTmj%2FWQBVFOpg2mnyzSf47hG18uSJ50vCK4QAf%2FtuaRB%2FogqBiNZt1Lz6o8VrpNjwiayAxknlSdVduhtQ3vTF3CUtdJBoVcqSlOKXi8lpPwIo%2BlHgePwIEUNlQUJwdw9ZASbh9r8Aowx8DKSNuNdM7jxpGNAekaeLjPNMV3f5Y5TuIMMN%2FQbssJgR90Zc0cxpac5TaZHRmgryySArxtM0HEESKPnYHjFVfTkOSH1HjjWalJFjhVmr6Pw2bDU4dsKiCdMq62jd8QyXAOKYPSjBQLE7iwKPrCnOs8VQ%2BtpAQbU0rlSZeXfkT43CDaOea%2FH%2BQ2DZXXb9XGqlgjd53dn1Rkt%2F1TqB71FZVj05OZQHL%2BuSDu3pTwjY2lmHkBuZNnjDxVXULV10PVG8NcISi0TNR3DG6Y6pM1MamZjUcMW%2FjL9giu6DZLcoFi7yBLxcW%2FK7%2Burkrk3nGKP%2BXRUOtL2EzSc%2FPcQOLq0ZCRx7UhaV9WC3esx%2FFQRb4wdPKtj8ooObKEsTMuApSz43GFosEe1cMP4hxvQaSQ1BNtPXsfv2UcPwYWmjHrExGTQyptSqxdrzNIUM32Uw8MyKvQY6pgHE7Vg%2FG%2Bunp3C1ZQSnDwbEnR34bPOJSvlR9D5gkdH%2Fia5xddNW07TG%2B0Dmhw0Ei4%2BMg7zyPYI8l%2BX27Fhcdf9Nvs1AUIIqbxznio9CH24QSFHlbfsUo116KnX4uN804GtlOSouGvW1%2F6AgDPONJNpvFm9jw6PaJfm6JXis2zUC2NtL4Tm8Kb53DCC9fQBp24uITlmSyIZ4qwn7JMiDK602xSOMbOsu&X-Amz-Signature=f7decda1b3440b22746f1d05178f38d8f24ffdd6329a3fca7301b91864391112&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8f1b1d60-cf1b-42b3-9faa-f634c89c3f84/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666QKP2FWX%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T041754Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECAaCXVzLXdlc3QtMiJGMEQCIDLDA5TBBw1GFEEsEVpyUL7hjMKxp0ZGYTCwOAh5w%2FXTAiBMq8deDJlg04bsitDwL74AAO4492pgqIC1rNllOR9LKyr%2FAwg5EAAaDDYzNzQyMzE4MzgwNSIMQeCYVANXeN9DzlydKtwDB9oIBzqGJ56ukr0Wjo6C4YgF9df2ALbfRx93HmGM0b0N%2BUpDC%2B0mTmj%2FWQBVFOpg2mnyzSf47hG18uSJ50vCK4QAf%2FtuaRB%2FogqBiNZt1Lz6o8VrpNjwiayAxknlSdVduhtQ3vTF3CUtdJBoVcqSlOKXi8lpPwIo%2BlHgePwIEUNlQUJwdw9ZASbh9r8Aowx8DKSNuNdM7jxpGNAekaeLjPNMV3f5Y5TuIMMN%2FQbssJgR90Zc0cxpac5TaZHRmgryySArxtM0HEESKPnYHjFVfTkOSH1HjjWalJFjhVmr6Pw2bDU4dsKiCdMq62jd8QyXAOKYPSjBQLE7iwKPrCnOs8VQ%2BtpAQbU0rlSZeXfkT43CDaOea%2FH%2BQ2DZXXb9XGqlgjd53dn1Rkt%2F1TqB71FZVj05OZQHL%2BuSDu3pTwjY2lmHkBuZNnjDxVXULV10PVG8NcISi0TNR3DG6Y6pM1MamZjUcMW%2FjL9giu6DZLcoFi7yBLxcW%2FK7%2Burkrk3nGKP%2BXRUOtL2EzSc%2FPcQOLq0ZCRx7UhaV9WC3esx%2FFQRb4wdPKtj8ooObKEsTMuApSz43GFosEe1cMP4hxvQaSQ1BNtPXsfv2UcPwYWmjHrExGTQyptSqxdrzNIUM32Uw8MyKvQY6pgHE7Vg%2FG%2Bunp3C1ZQSnDwbEnR34bPOJSvlR9D5gkdH%2Fia5xddNW07TG%2B0Dmhw0Ei4%2BMg7zyPYI8l%2BX27Fhcdf9Nvs1AUIIqbxznio9CH24QSFHlbfsUo116KnX4uN804GtlOSouGvW1%2F6AgDPONJNpvFm9jw6PaJfm6JXis2zUC2NtL4Tm8Kb53DCC9fQBp24uITlmSyIZ4qwn7JMiDK602xSOMbOsu&X-Amz-Signature=0b0dbb1b12b23264a3b4b8efdb603124acf2c335d6ecb3d831ca8ac4b687bdea&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/13ad0497-05fe-4eaa-984e-707b33e14761/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666QKP2FWX%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T041754Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECAaCXVzLXdlc3QtMiJGMEQCIDLDA5TBBw1GFEEsEVpyUL7hjMKxp0ZGYTCwOAh5w%2FXTAiBMq8deDJlg04bsitDwL74AAO4492pgqIC1rNllOR9LKyr%2FAwg5EAAaDDYzNzQyMzE4MzgwNSIMQeCYVANXeN9DzlydKtwDB9oIBzqGJ56ukr0Wjo6C4YgF9df2ALbfRx93HmGM0b0N%2BUpDC%2B0mTmj%2FWQBVFOpg2mnyzSf47hG18uSJ50vCK4QAf%2FtuaRB%2FogqBiNZt1Lz6o8VrpNjwiayAxknlSdVduhtQ3vTF3CUtdJBoVcqSlOKXi8lpPwIo%2BlHgePwIEUNlQUJwdw9ZASbh9r8Aowx8DKSNuNdM7jxpGNAekaeLjPNMV3f5Y5TuIMMN%2FQbssJgR90Zc0cxpac5TaZHRmgryySArxtM0HEESKPnYHjFVfTkOSH1HjjWalJFjhVmr6Pw2bDU4dsKiCdMq62jd8QyXAOKYPSjBQLE7iwKPrCnOs8VQ%2BtpAQbU0rlSZeXfkT43CDaOea%2FH%2BQ2DZXXb9XGqlgjd53dn1Rkt%2F1TqB71FZVj05OZQHL%2BuSDu3pTwjY2lmHkBuZNnjDxVXULV10PVG8NcISi0TNR3DG6Y6pM1MamZjUcMW%2FjL9giu6DZLcoFi7yBLxcW%2FK7%2Burkrk3nGKP%2BXRUOtL2EzSc%2FPcQOLq0ZCRx7UhaV9WC3esx%2FFQRb4wdPKtj8ooObKEsTMuApSz43GFosEe1cMP4hxvQaSQ1BNtPXsfv2UcPwYWmjHrExGTQyptSqxdrzNIUM32Uw8MyKvQY6pgHE7Vg%2FG%2Bunp3C1ZQSnDwbEnR34bPOJSvlR9D5gkdH%2Fia5xddNW07TG%2B0Dmhw0Ei4%2BMg7zyPYI8l%2BX27Fhcdf9Nvs1AUIIqbxznio9CH24QSFHlbfsUo116KnX4uN804GtlOSouGvW1%2F6AgDPONJNpvFm9jw6PaJfm6JXis2zUC2NtL4Tm8Kb53DCC9fQBp24uITlmSyIZ4qwn7JMiDK602xSOMbOsu&X-Amz-Signature=849bcb6cd52adc3da03b7dfb271f7bcef6a669fc42e904ed4bea876ebb01bbb1&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 2. Box and Whisker Plot
A box plot shows the distribution of quantitative data in a way that facilitates comparisons between variables or across levels of a categorical variable. The box shows the quartiles of the dataset while the whiskers extend to show the rest of the distribution, except for points that are determined to be "outliers".
**Syntax:**
```python
sns.boxplot(x='header_1', y='header_2', data=df)
```
**Example Output:**


![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d207ae92-0a7c-4e2f-aa65-0ee5a2c33bf7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667CI7Q26H%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T041755Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECAaCXVzLXdlc3QtMiJHMEUCIQDTC7EkjlQA8YvisLdVylZmFTnq5XpsMlbj2tQ7e4%2B8NQIgZFg2ipt7SATdFG0GgEeoyoP%2FdUzUuzj1U3T8JUQGaHcq%2FwMIORAAGgw2Mzc0MjMxODM4MDUiDCZe%2B2n7YkWXmjd6VyrcA%2BbkvrWmD24pkX%2Fjti%2FilBbrNqJmz07Bm3vIHi0cPUAbjm72gfWdoVvakIjzGWSk1Yl3C731MHZgnsOZYpD9GVk1EfqErHGszHR4%2F1mosYB9gxpvEofBaVyJO4DFyV%2FU1sNC%2BELCTNpJ6Ft9OUx%2FmtAsALos%2BldDhBczyWmSuUBw7DPPat0kON%2Fde6mh5ZXZN%2FaDrVf3XlDYUpnF6yKKiLNpz6Td3sJMVnZ%2B8p38jEjdDjdLYYgK6iUMBkYK%2Bh6QmKmZnSJA1ZLozjYvJR84GB4%2F%2FVABtu1sDxlPFPoKR%2B4%2B5Xld%2BmMWXFxeZNwdZtKhuKHEf4DA6PnBWIyRtEf0CqWrKk5jRjeoTvoCR1XXzDtj%2BH6X7zgf4TAzb3doHFhwdxqJWcsXN5YYaRiilgaWb2bG0MStWLBGqLHtWGAcljLFmq9%2FUaTN5CXCBHv3L%2FmqyVH%2FcqwlVbPZXsxRwTGgFcuMGt09aJHF9d7nEwHRKoxJW1akclVMOjJ4wu3t%2BaBHYbuKT8Abp2nQ2sQaycMoGg5%2F3GpP7HbNdIrXzWBCEPXhfSvaseyhb4GPqb8dQExRV%2B5vmfEn3Zh67N1x7ZuHj0XQK%2Fi6722%2FBYzizsBubsrZXpvSbBDthHzAiRBjMPnMir0GOqUBja23cb2pmAZYHpRzRfMs%2FsSVh5SEM2pKSMgTX6ZdAaQxlxmh93JUb9QC9JiLnY6Y5AuO3TOibo8c6Vc%2BqmzpaZKiM9RTgq3zWvgcASv7TIy1dOKCxd7fwv1RXQ1ItavtflekiEwAkVp9XQOvLxBMxr5txC4pKoXgYhbcPfjk60M3Xv3BjCtczpDKgmp6gzZZlng3Rbr%2BWlt8AGTNL%2BCgaJIKRNHq&X-Amz-Signature=6519231328e26034eb228928251592c43d62daa5a54bdd24a99cef5686debbed&X-Amz-SignedHeaders=host&x-id=GetObject)

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0e516edc-7551-4792-ab18-0494db3c4c0c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YWK6RLTK%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T041755Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECAaCXVzLXdlc3QtMiJGMEQCIFnOmKjJaU7OM03S%2FZM4yIW%2FsBrAwyUabJg8p8LEojnCAiAlsd0LfQiptvNcgujgAdEt770F4xHnwGr%2BVj6CyIKJFir%2FAwg5EAAaDDYzNzQyMzE4MzgwNSIMkKe2ai%2FAoDZaGI7%2BKtwDGxppQRQ7jJh6FpGv3NLB65v8teKkhGRpibFqT475imtJvDFDCAxsCrSqgOfb%2FlnezH%2BlN31%2B6PQWAmfXFuDHdFQ03jZ6YHm3PBW1x%2FLKE4VCNW1I0tQvPUHXQQiyhNDifUAAR02UiVas5kqfLjhJ7%2FWEhBiPzZtoEnCQWVp2PbMBLscVds4RRZs7u1fUEBXFK9SG38kCnZM2ds3NUKgfIPkqkHrB2hiuYKTtibB%2B99eWTA%2FAcm9ha2k%2BK0K%2Bqc0tFHPs5tl2uHi70OaGcZLpAvlR5XOpVZDYVAHNjcvbSRzkHDZcGTG9CCGluJT5PGK5tYMBTY3RIMs7pPhxHYPsT2XKfd%2FmFvWuFEt8lKie%2FrWnIypmMaGj1PlBDOZyLI6t0Qiw3jjfW9LHynP%2FRobtqLGbI%2F1R5jG8%2BM0h9zqBIKheS1vM1oguGgJ1eIytowrbIXgbZbZrkBMvIQ%2B0%2FBGJ9w6%2BdpnFSZeED%2FyVoFnN2VewwylFGxHGaeaXi4cvpyQpPRGXyLZztNL6jFcDPKS1JB2rQx0OQOsbn%2FkVifZJlvU47G16LXhQB4ttuNxZO0J7dlN0lT7rueeQLz2YUa6OEaUgiQ0l8AFNMJTlvETzWauEy4Qxirzb3QHu3mAw%2FcyKvQY6pgGJLxMWYhCTHZ5OA%2BlURZVBx6TBywdZ14ACFnC0Qp6LVYmD2KpREsIzxt1I20TjlDCIB7E1lMMy8p5AUvH0dzp3ARl%2F3ESg3Vx%2BKhfMZRSaUZus13%2Byee0eHjX50hkAnZe7aBVoWeJKp1JmOQgbviVThfQbokPPH%2F7RZRAxNI3OHqmuEU2tqKTPFcq1r%2FLksI1Jawn7NdyAOQGWSRzqww6Ce6BNdshb&X-Amz-Signature=bb6c55ced8af11a55453cf13fef9d46c5ffb6fd3003a30506fe5dba06349f3b7&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23a79b9d-2356-49a9-8fd9-65c6b0ab2cc5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666QKP2FWX%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T041754Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECAaCXVzLXdlc3QtMiJGMEQCIDLDA5TBBw1GFEEsEVpyUL7hjMKxp0ZGYTCwOAh5w%2FXTAiBMq8deDJlg04bsitDwL74AAO4492pgqIC1rNllOR9LKyr%2FAwg5EAAaDDYzNzQyMzE4MzgwNSIMQeCYVANXeN9DzlydKtwDB9oIBzqGJ56ukr0Wjo6C4YgF9df2ALbfRx93HmGM0b0N%2BUpDC%2B0mTmj%2FWQBVFOpg2mnyzSf47hG18uSJ50vCK4QAf%2FtuaRB%2FogqBiNZt1Lz6o8VrpNjwiayAxknlSdVduhtQ3vTF3CUtdJBoVcqSlOKXi8lpPwIo%2BlHgePwIEUNlQUJwdw9ZASbh9r8Aowx8DKSNuNdM7jxpGNAekaeLjPNMV3f5Y5TuIMMN%2FQbssJgR90Zc0cxpac5TaZHRmgryySArxtM0HEESKPnYHjFVfTkOSH1HjjWalJFjhVmr6Pw2bDU4dsKiCdMq62jd8QyXAOKYPSjBQLE7iwKPrCnOs8VQ%2BtpAQbU0rlSZeXfkT43CDaOea%2FH%2BQ2DZXXb9XGqlgjd53dn1Rkt%2F1TqB71FZVj05OZQHL%2BuSDu3pTwjY2lmHkBuZNnjDxVXULV10PVG8NcISi0TNR3DG6Y6pM1MamZjUcMW%2FjL9giu6DZLcoFi7yBLxcW%2FK7%2Burkrk3nGKP%2BXRUOtL2EzSc%2FPcQOLq0ZCRx7UhaV9WC3esx%2FFQRb4wdPKtj8ooObKEsTMuApSz43GFosEe1cMP4hxvQaSQ1BNtPXsfv2UcPwYWmjHrExGTQyptSqxdrzNIUM32Uw8MyKvQY6pgHE7Vg%2FG%2Bunp3C1ZQSnDwbEnR34bPOJSvlR9D5gkdH%2Fia5xddNW07TG%2B0Dmhw0Ei4%2BMg7zyPYI8l%2BX27Fhcdf9Nvs1AUIIqbxznio9CH24QSFHlbfsUo116KnX4uN804GtlOSouGvW1%2F6AgDPONJNpvFm9jw6PaJfm6JXis2zUC2NtL4Tm8Kb53DCC9fQBp24uITlmSyIZ4qwn7JMiDK602xSOMbOsu&X-Amz-Signature=ccf525d0b25826e95eed50f3746d0c469d3525d905cb82af576cc90ae5ac1f4d&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 4. KDE Plot
A Kernel Density Estimate (KDE) plot is a graph that creates a probability distribution curve for the data based upon its likelihood of occurrence on a specific value. This is created for a single vector of information.
**Syntax:**
```python
sns.kdeplot(X) || sns.kdeplot(df['age'])
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0d571213-2a2f-4921-a50b-880847aa05ee/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666QKP2FWX%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T041754Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECAaCXVzLXdlc3QtMiJGMEQCIDLDA5TBBw1GFEEsEVpyUL7hjMKxp0ZGYTCwOAh5w%2FXTAiBMq8deDJlg04bsitDwL74AAO4492pgqIC1rNllOR9LKyr%2FAwg5EAAaDDYzNzQyMzE4MzgwNSIMQeCYVANXeN9DzlydKtwDB9oIBzqGJ56ukr0Wjo6C4YgF9df2ALbfRx93HmGM0b0N%2BUpDC%2B0mTmj%2FWQBVFOpg2mnyzSf47hG18uSJ50vCK4QAf%2FtuaRB%2FogqBiNZt1Lz6o8VrpNjwiayAxknlSdVduhtQ3vTF3CUtdJBoVcqSlOKXi8lpPwIo%2BlHgePwIEUNlQUJwdw9ZASbh9r8Aowx8DKSNuNdM7jxpGNAekaeLjPNMV3f5Y5TuIMMN%2FQbssJgR90Zc0cxpac5TaZHRmgryySArxtM0HEESKPnYHjFVfTkOSH1HjjWalJFjhVmr6Pw2bDU4dsKiCdMq62jd8QyXAOKYPSjBQLE7iwKPrCnOs8VQ%2BtpAQbU0rlSZeXfkT43CDaOea%2FH%2BQ2DZXXb9XGqlgjd53dn1Rkt%2F1TqB71FZVj05OZQHL%2BuSDu3pTwjY2lmHkBuZNnjDxVXULV10PVG8NcISi0TNR3DG6Y6pM1MamZjUcMW%2FjL9giu6DZLcoFi7yBLxcW%2FK7%2Burkrk3nGKP%2BXRUOtL2EzSc%2FPcQOLq0ZCRx7UhaV9WC3esx%2FFQRb4wdPKtj8ooObKEsTMuApSz43GFosEe1cMP4hxvQaSQ1BNtPXsfv2UcPwYWmjHrExGTQyptSqxdrzNIUM32Uw8MyKvQY6pgHE7Vg%2FG%2Bunp3C1ZQSnDwbEnR34bPOJSvlR9D5gkdH%2Fia5xddNW07TG%2B0Dmhw0Ei4%2BMg7zyPYI8l%2BX27Fhcdf9Nvs1AUIIqbxznio9CH24QSFHlbfsUo116KnX4uN804GtlOSouGvW1%2F6AgDPONJNpvFm9jw6PaJfm6JXis2zUC2NtL4Tm8Kb53DCC9fQBp24uITlmSyIZ4qwn7JMiDK602xSOMbOsu&X-Amz-Signature=37e07c5fce6150023d34f8fb58e2e90cc842d68aa68fefafcf85f3086f228aab&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/53752550-ef82-4ca9-a01a-09921f0282d0/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666QKP2FWX%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T041754Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECAaCXVzLXdlc3QtMiJGMEQCIDLDA5TBBw1GFEEsEVpyUL7hjMKxp0ZGYTCwOAh5w%2FXTAiBMq8deDJlg04bsitDwL74AAO4492pgqIC1rNllOR9LKyr%2FAwg5EAAaDDYzNzQyMzE4MzgwNSIMQeCYVANXeN9DzlydKtwDB9oIBzqGJ56ukr0Wjo6C4YgF9df2ALbfRx93HmGM0b0N%2BUpDC%2B0mTmj%2FWQBVFOpg2mnyzSf47hG18uSJ50vCK4QAf%2FtuaRB%2FogqBiNZt1Lz6o8VrpNjwiayAxknlSdVduhtQ3vTF3CUtdJBoVcqSlOKXi8lpPwIo%2BlHgePwIEUNlQUJwdw9ZASbh9r8Aowx8DKSNuNdM7jxpGNAekaeLjPNMV3f5Y5TuIMMN%2FQbssJgR90Zc0cxpac5TaZHRmgryySArxtM0HEESKPnYHjFVfTkOSH1HjjWalJFjhVmr6Pw2bDU4dsKiCdMq62jd8QyXAOKYPSjBQLE7iwKPrCnOs8VQ%2BtpAQbU0rlSZeXfkT43CDaOea%2FH%2BQ2DZXXb9XGqlgjd53dn1Rkt%2F1TqB71FZVj05OZQHL%2BuSDu3pTwjY2lmHkBuZNnjDxVXULV10PVG8NcISi0TNR3DG6Y6pM1MamZjUcMW%2FjL9giu6DZLcoFi7yBLxcW%2FK7%2Burkrk3nGKP%2BXRUOtL2EzSc%2FPcQOLq0ZCRx7UhaV9WC3esx%2FFQRb4wdPKtj8ooObKEsTMuApSz43GFosEe1cMP4hxvQaSQ1BNtPXsfv2UcPwYWmjHrExGTQyptSqxdrzNIUM32Uw8MyKvQY6pgHE7Vg%2FG%2Bunp3C1ZQSnDwbEnR34bPOJSvlR9D5gkdH%2Fia5xddNW07TG%2B0Dmhw0Ei4%2BMg7zyPYI8l%2BX27Fhcdf9Nvs1AUIIqbxznio9CH24QSFHlbfsUo116KnX4uN804GtlOSouGvW1%2F6AgDPONJNpvFm9jw6PaJfm6JXis2zUC2NtL4Tm8Kb53DCC9fQBp24uITlmSyIZ4qwn7JMiDK602xSOMbOsu&X-Amz-Signature=394d01eb6d1a2c91687c4c1b6a944241df9072d22bf441eee2ca602c9a0d0f5e&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
## 4. Correlation Between Variables
Correlation is a statistical measure of the extent to which different variables are interdependent. It indicates how changes in one variable are associated with changes in another variable over time.
### Positive Correlation
Positive correlation indicates that as one variable increases, the other variable also tends to increase.
**Example: Engine Size and Price**
- **Positive Correlation:** Engine size increases, price also increases.
- **Visualization:** Scatter plot with a steep positive slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c7ea9b0-3ef3-4357-a9c3-554fc71b6b15/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667OJKZJKV%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T041754Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECAaCXVzLXdlc3QtMiJHMEUCIQCnPrwKLeY82%2FtfM88jKWdnK31AVk2BLU%2FkwhUxytJx6AIgXiw5U5mvd%2FZrSLxtg%2BpEcC%2Bj83qiCGdZoM4mloWVFNIq%2FwMIORAAGgw2Mzc0MjMxODM4MDUiDOhxREFsbHcVo1uD7SrcA4oPsIo3gAHioikQuAz0RGil7Oqv%2FVTRTcMsftGXEBZrT%2FCeY4AxkyDk%2FMPzdAzPc4zAxDwetrlEMr2uDP3MRJnu%2Fy8usxgLt8IPTh5ZAUTAaHFSFWLq9YZ5AS2NOkLJLM5TozvGOjajFH1qyEbDxTElpcH3KDQuKUPumjfwetOyqdupjFEp2b12x8qjVHg5x2KBt%2FMvhzHDMyhHlR%2BFq4wZ2HYy0JuPAlTn%2BE6EFCD7X1rW68Ktyt3ehnpRnMW%2BVguDbPgj%2BhEogBpTjilXosp9ch2dYuR5umO5%2B4P5EaeXSrzfilEIG3QiAnbAeDzVpN%2FcuTZbqzWRb%2Fz2FUKlN%2B%2FrJ4nxxDGekw6hEi50yqU6NP0nvZ4pWqZvF0KbvDKPPqytUQIlMWVfmARPDGkvnP3704kbV9yYMGqfW%2B2MH3XKRfboprwnrkguxZXRAF62fiVbUuea4sGRcy5E17MJHF6I5HU90z4MsSWbaM0N%2BKJ04RkbQWXJxUkE6t5DKxl5ZQ2ACmGhLolfiF0TwT%2Bo0dJv8I7%2BeCfZjJZHwa3eh3ZUE9H1lZ9ujDf%2FWNM7NTVKh5zLvE%2FEgop6jg8aFpwtrbVKdq9IGsBXoRNECVGCIj%2B%2F6UlcVrpPfe7u2%2FKnMKLNir0GOqUB4Q9Bs%2FbiFL4TYPVj%2FINsiL9RdWr%2FcJ2ZeO7aUUPxFkMl1TQOQ%2F0FK6Tma7244gBuW0HPjM3mWTvuX6LuOirLPWrO2gOsFrROLllhzSh3GWTgSJbHAswo0QDIQ8hfllhzcuJiKdeZtW3gYOhJy9TdaXelujPcqGnRCEKPJN5WTjOjeWJWFjWDHXBG03XLehKEbGSkGvxezthnMwlsVE%2BoXD7FUZhX&X-Amz-Signature=f0ba769697133e70824b0a066963f2956f255bcb6c57fd4e79655d314bf0852d&X-Amz-SignedHeaders=host&x-id=GetObject)
**Explanation:** When engine size increases, there is a corresponding increase in the price of the vehicle. This positive correlation suggests that larger engines tend to be associated with higher prices in the market.
___
### Negative Correlation
Negative correlation indicates that as one variable increases, the other variable tends to decrease.
**Example: Highway Miles per Gallon and Price**
- **Negative Correlation:** As highway miles per gallon increases, price decreases.
- **Visualization:** Scatter plot with a steep negative slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/10f1f798-9cc4-4df2-a9c1-5a339f554a0b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SLVIJHTB%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T041755Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECAaCXVzLXdlc3QtMiJHMEUCIQDoZUPoKOsN%2FJioUgVRjT2WpU585CuRMGkTtJlirca6PwIgWrgQxBtUTjSbSNEu3ehCVzs382P557acPey5oSkRAR0q%2FwMIORAAGgw2Mzc0MjMxODM4MDUiDKMFh2IJyv4PB1LR9yrcA%2F9KILmhJ%2Fj8Bv4WchmbWxC9wAwkL3%2FfW%2FiWPk7mbIxGeDg5somvKd1KFMsa0VAoQTsC%2FUZECignl4ylKXTmc353KlPb1TgD4MV2Vwy%2FESEIfMeYou6ZHkL5yo939%2FMmgAi%2Buks34tlW10jwuaeUOWTJH%2BReS817wnMtatL9P59%2BTOdGBLruS7Pdo3FoPN7fHZZGdvNhkoXsFpfZofTl0249wvezLklTPAFcN7AUc1mA0KOa17riJOI22znJhC4JJq6nb%2BYH88jL3y6%2FNchgqeW77tXxlRC7qDpPU8MhwrwW8tTeLftjPqevrWk6wAB8d4mFGWOp226O1jHW3Lu0Z9xH6rAR9c6bsO2ybP9RZNsV4le3EaSmMzQUI2aMSdrRDrnQrTTXEEHKL9HByalRkB2SqePxLNWmbw7qlxSigwI4pEN2tBGmxaKPJQ8Zu6xuo4h6ALCJE8YEBlf9gp4kCwAbtGBSdMnRmWtG23ywEp%2B7cE78uSth6XBqrzVqUZHJBYCkZuDBtSoG4j6c3iR1QCYpd0DNmbCmCVhgjLEGD3PxwYDCIvXpLeJSX1SPAK%2FpQmqpqwCFhF0CboObAypHu18oe80dV3Y%2BKh1Qrpgy4R0MjEs16wEhtKXk4PuQMKvNir0GOqUBNaX24buUULvoYsXdTb8Bj6L5ScSa7h9745XILPia3aKPwlxjyAmtWDwm4BFGtCQJkVrRqomSTGb9aJczmDaqZdBJJRS82fbLS%2B%2FsrBA%2FiMtuiGqYsTLnragGFrTcO8YuzVtiHGqUsJAiEi9wVnXV29JoDOohuO1E1JXBSPu29bo6IY%2BLi3CTvBaMuBTBoEIPDNj3pa3zCXlCfhDIBvXW0tKszNMA&X-Amz-Signature=b240016a7faf08ad616b8a12e9247857e7c4a1cf2a2d824b422c8bb47127f06a&X-Amz-SignedHeaders=host&x-id=GetObject)
**Explanation:** When highway miles per gallon increases, the price of the vehicle tends to decrease. This negative correlation suggests that cars with higher fuel efficiency (more miles per gallon) are generally priced lower in the market.
___
### Weak Correlation
Weak correlation indicates a lack of strong relationship between the variables.
**Example: RPM and Price**
- **Weak Correlation:** Low and high RPM values show varied prices, indicating no strong predictive relationship.
- **Visualization:** Scatter plot with no clear trend or slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9f914514-8914-4bf4-ac84-d9e3077f6eb1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664Z5UMUG7%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T041754Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECAaCXVzLXdlc3QtMiJHMEUCIQC9igwBPXWpEd9HmJZfF%2BZHlUD7PUi5kVhK3cAFWC4ZoAIgRpGkkPIQQhAeS5y31KE8ZGpcjtk5%2FNe0lkXcQuKK0%2Fkq%2FwMIORAAGgw2Mzc0MjMxODM4MDUiDBOjQWEOgENxxgBdwCrcAyqDx5Uz3qz4amfIUKV4gbafoUT%2BJI3Y52paW75ke%2Fvga8vxCz0iIvGfckj1wXcd2P773LvJBl%2BvYRXdZ4%2BlTjpxBy7rV1uCr5yRR8d4cvrtjFvah5z3ku2HvLrDgWILBkKUUqwkdhBPXv%2BMHHRCzevT82Z4C2nVgB65olocS8whfFPS%2BPi1nXiGquM6cZPSsZxGqjIRR%2B4Ofh0kaAJPKx2pOxQpxQIfZKL0PbSi6U3USv6XlCPnTrJrj49OO5UUtLz7i0no9OouXJFMgh%2F4nkcQEJ%2BzlyLR6BA%2F9h2jaA1%2BxYY02MZmRgxf6HyJl86rb3fHTD2tnZ2rXqZvK4t7SWLsb6No810%2F2R%2B7Vxr9h67jBZMYkuZNJvo%2BPMiGFdOU0MFj1STr4mNUvdD%2FBfbpJSRAeoK76u8jqCBUh2l%2Fkvmy54eIDj8HX7aqygqBAWzw%2FA%2B%2BTZsG96BVQ3gPi%2BaAFdQenQRaPOF%2Fo%2Bil63ghgVS9qGb3bBRCHMLGoQjArqx4%2B2LIAYrd8T0uzgSBNDNa5ybKpnM%2B%2BKXZ1ptv7yHGoaM0Bp2jIztbPf1HbW8%2FH6pQ%2BsJStiiuWHqbPlmsp1EDO%2FxsvvWlz2ahpaRz%2FdqvStHRE34BkBz7Pns3GfjbMKrNir0GOqUBiZShNmU6tITPSCD81RTd3rxz3U5LeGhoxohM7%2B3cwDO9Ce9BAVJFgw6YS1IaEomm6GuHF8YRa7XBSenAlmVAOZHZBc%2F1h%2BA2Dj3F4LJKC1%2Be18niwLyJTJ39vGwMGkzQOGanSHJb11WTRM0V70cBzpdk7d6zsp5YlY7CCWUdBVT5%2Fql37Qr%2FNCMLcvYGpGbtZzmQhRVU1fAuaJ7IgADwu2NmuKq4&X-Amz-Signature=9ed63104205e27f927e1e1b6f3b5b9509605a38381b0177b813e091d2b605878&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f18086e5-5b04-4fbf-8309-8944ab20d213/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R2LXBP7I%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T041754Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECAaCXVzLXdlc3QtMiJGMEQCIAm8OnGLt19D3R8btzFXhSwm%2F8TvKhEjJ3l1P3YZD3sJAiAeJq5tj1jAtcum%2BaWgR85Cnh0d0l8PSM5M26oLp2ho0Cr%2FAwg5EAAaDDYzNzQyMzE4MzgwNSIM1l5cjT2yumqJfKi7KtwDQpvHraCWVbnQQU0S7gw6%2B9Rae5HOY1ZTRs8DZM5E7m9RDMz4kz4R5ahZllGU2WqY7sjlGyCX51xDoDZbG%2FthLF%2FfrPGPMo7XkDdIlSPwZ2QziNVCZ2QplQxgIj7uragZaFxBGgFw7wLFCqNYhaVFuQT%2Bs2yvovDOTjNCo96%2FHj82P5RKINhkJ7p5wQ8aWKisGUewQiwT1Kke4Nv1EurCkbxrFxMmZ9UzBmKl%2BotazMnU3eM91lSVjXq2oA4%2BuDW8iz7afQbnhOMzbQsYJ5PKy7zUAadgQyqYDdpcNtfC9Jk%2F2G9mCWlu7lcPoJ3YFUFAW43PhvOl6siJMYam18FzrFRXeA58rqiudBMYdEBd7oNY73IMBqyvyqWnAudIV7DRJJDHlJT4yh6GshHj32ZXY%2BynlUuNAF%2BFucM%2BmwcR%2FLFb6VcUC0fjsCWh6cp3%2BSq5G8QUOUwd2F2iu7oMOvmmr38zPQuvdbG7pyI5V5wjZBfQZ8w5Aja9%2BS8MhjmLNzEKfS9RLUDNJVjZV2fzjcSkSsSlAPpkY8QSuihgbqzIemxqJNTH3a3KXa68Om%2FJ7DgoYn1BIaLxsh5uevyVniT4oudA3jq8r0I0lMzIVAb%2Be%2B93suRzk%2FMLyoom7dkw5cyKvQY6pgGz%2FutCPvmDdxkukEKcSOtg3vc47dc%2FHWHxFVAA4C6Y%2FU2gT6MJEU2Ki2OKeNSdCyR0fMtPMtWhY4eiocCj%2FSW2EkmDcz78AxNCU6e%2F1lbgzGrKkjh%2FET%2B7LQXVVTr%2B72GjnOGj57bxchxZUI2HzlstTPLZfWxltW44T6sEKSOuQZN4GJZ3BVpFqIUgQxxmAFfZ%2B7zvpmTGWWd3eNnDRFQLzdjeMLjR&X-Amz-Signature=1cee486a2aeed0b9d242da6f1bb1b52194f6dd7c1fed87611eeea6f8a5eaea90&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Correlation Plot
Heatmap visualizes correlations among variables. Color scheme indicates Pearson correlation coefficients. Dark red diagonal line shows perfect correlation (value of 1) between variables and themselves.
This heatmap offers overview of variable relationships and their link with price.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cd3b341e-cc1a-45f7-8aec-cdc00436d270/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R2LXBP7I%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T041754Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECAaCXVzLXdlc3QtMiJGMEQCIAm8OnGLt19D3R8btzFXhSwm%2F8TvKhEjJ3l1P3YZD3sJAiAeJq5tj1jAtcum%2BaWgR85Cnh0d0l8PSM5M26oLp2ho0Cr%2FAwg5EAAaDDYzNzQyMzE4MzgwNSIM1l5cjT2yumqJfKi7KtwDQpvHraCWVbnQQU0S7gw6%2B9Rae5HOY1ZTRs8DZM5E7m9RDMz4kz4R5ahZllGU2WqY7sjlGyCX51xDoDZbG%2FthLF%2FfrPGPMo7XkDdIlSPwZ2QziNVCZ2QplQxgIj7uragZaFxBGgFw7wLFCqNYhaVFuQT%2Bs2yvovDOTjNCo96%2FHj82P5RKINhkJ7p5wQ8aWKisGUewQiwT1Kke4Nv1EurCkbxrFxMmZ9UzBmKl%2BotazMnU3eM91lSVjXq2oA4%2BuDW8iz7afQbnhOMzbQsYJ5PKy7zUAadgQyqYDdpcNtfC9Jk%2F2G9mCWlu7lcPoJ3YFUFAW43PhvOl6siJMYam18FzrFRXeA58rqiudBMYdEBd7oNY73IMBqyvyqWnAudIV7DRJJDHlJT4yh6GshHj32ZXY%2BynlUuNAF%2BFucM%2BmwcR%2FLFb6VcUC0fjsCWh6cp3%2BSq5G8QUOUwd2F2iu7oMOvmmr38zPQuvdbG7pyI5V5wjZBfQZ8w5Aja9%2BS8MhjmLNzEKfS9RLUDNJVjZV2fzjcSkSsSlAPpkY8QSuihgbqzIemxqJNTH3a3KXa68Om%2FJ7DgoYn1BIaLxsh5uevyVniT4oudA3jq8r0I0lMzIVAb%2Be%2B93suRzk%2FMLyoom7dkw5cyKvQY6pgGz%2FutCPvmDdxkukEKcSOtg3vc47dc%2FHWHxFVAA4C6Y%2FU2gT6MJEU2Ki2OKeNSdCyR0fMtPMtWhY4eiocCj%2FSW2EkmDcz78AxNCU6e%2F1lbgzGrKkjh%2FET%2B7LQXVVTr%2B72GjnOGj57bxchxZUI2HzlstTPLZfWxltW44T6sEKSOuQZN4GJZ3BVpFqIUgQxxmAFfZ%2B7zvpmTGWWd3eNnDRFQLzdjeMLjR&X-Amz-Signature=2158068acb99af2f4458643d5746d4da501a4266c200bd247b759d50c3844f92&X-Amz-SignedHeaders=host&x-id=GetObject)

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
