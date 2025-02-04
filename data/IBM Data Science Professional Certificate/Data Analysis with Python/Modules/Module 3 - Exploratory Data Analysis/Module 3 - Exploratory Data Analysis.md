

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7e6d594d-952e-44b6-97ea-31225882aea6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UJRXWX4T%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T141400Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBYaCXVzLXdlc3QtMiJHMEUCIQD%2F%2F7NV%2BMuqWv%2FuXKqL9Z4Ht0qHZx9PES5vxTH1WI0PlwIgBVro8sduEnks64k2yuQNCtXiVnKCQItIppkyJTIU2scq%2FwMILxAAGgw2Mzc0MjMxODM4MDUiDBFk2xA%2BUioPfa9R1CrcA9jedmOSEjfJv7YPfZyYseLQIDCwUxgAM%2B0mbmd0tfj2ZRVTxp1NkTCRHNQb4jn0y1bnirYBY%2BvHj0A3QwB0qsAPTwfqO9DCTW%2FDW9ZPO8MRvts6VZLakMRwLsBUy87rj%2FFfh9oUUVtYemEzlyjvqHjs8hBxA%2BpbEmfVMlGlVyqi5YKvZKWHMBiMmTDgaKoxJ8m2SUwtHjJl7vmfRcB0b%2FIoxg%2B%2FK59geVdBhzh2Y8lGTNm%2FXhweRMFFkbLyu2tAuarKDrUesN060lcJyH5DMvZELHsdzTcDbslUWdFhdrlGU1mZgWw2dKnJjeAsuvG0cSGhYaRzRnLn68oTP9VFvjFX%2BqVg6vt%2FqQqbL134dgpQAdYEezea7RhLklEJB54POhlVfVOComRriGnxqG3V0vZ6wu%2FA51jZIlepEBIozGmWDr7gOJpBF8JCFqiLsM75rgrW0CL9hO12n%2Fbo0IEbMiiPjRb%2Bc6BnvEcbf1cgMovTyFO2ERKAlMIH35lLJOAoN9vWwY2rMmr0bgycCsPIEyCwvwybbi4iztbgLo0CrFJFZYFFtLDuldh78vkiI%2BktxhMzvZtrzgzgjHplpPTmn%2BE6Vn2SrkXQMYAmqo0x0Ea6pELVORSsUxS0wUZPMPm8iL0GOqUBYFs1odtVt2iK9YXQe6QC7hOyuWzeSymNWWnhxTYnrQsGunPiXYAhoWUrcWL62Wwj6UtFJoSmehlSU7dN2cuQ4l2VTuxeuR5Dp9hruWAq9E2Ji6fRpCCz7ZEG3c6zDTWfPgrL%2F3zs%2FHVzxHCVgSR6bnNfIamNyXqqI9aLOIP4hBlwhXl1twMV0nzq1gUB2tVWU%2BnlM1RjSFx357TddPfF7bdJVuxF&X-Amz-Signature=eff611a4099a46bbd23dc812ffca01042919d54afee693e306fb83c610c4d9de&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cbfaed9e-b398-4902-8936-dea058b21def/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UJRXWX4T%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T141400Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBYaCXVzLXdlc3QtMiJHMEUCIQD%2F%2F7NV%2BMuqWv%2FuXKqL9Z4Ht0qHZx9PES5vxTH1WI0PlwIgBVro8sduEnks64k2yuQNCtXiVnKCQItIppkyJTIU2scq%2FwMILxAAGgw2Mzc0MjMxODM4MDUiDBFk2xA%2BUioPfa9R1CrcA9jedmOSEjfJv7YPfZyYseLQIDCwUxgAM%2B0mbmd0tfj2ZRVTxp1NkTCRHNQb4jn0y1bnirYBY%2BvHj0A3QwB0qsAPTwfqO9DCTW%2FDW9ZPO8MRvts6VZLakMRwLsBUy87rj%2FFfh9oUUVtYemEzlyjvqHjs8hBxA%2BpbEmfVMlGlVyqi5YKvZKWHMBiMmTDgaKoxJ8m2SUwtHjJl7vmfRcB0b%2FIoxg%2B%2FK59geVdBhzh2Y8lGTNm%2FXhweRMFFkbLyu2tAuarKDrUesN060lcJyH5DMvZELHsdzTcDbslUWdFhdrlGU1mZgWw2dKnJjeAsuvG0cSGhYaRzRnLn68oTP9VFvjFX%2BqVg6vt%2FqQqbL134dgpQAdYEezea7RhLklEJB54POhlVfVOComRriGnxqG3V0vZ6wu%2FA51jZIlepEBIozGmWDr7gOJpBF8JCFqiLsM75rgrW0CL9hO12n%2Fbo0IEbMiiPjRb%2Bc6BnvEcbf1cgMovTyFO2ERKAlMIH35lLJOAoN9vWwY2rMmr0bgycCsPIEyCwvwybbi4iztbgLo0CrFJFZYFFtLDuldh78vkiI%2BktxhMzvZtrzgzgjHplpPTmn%2BE6Vn2SrkXQMYAmqo0x0Ea6pELVORSsUxS0wUZPMPm8iL0GOqUBYFs1odtVt2iK9YXQe6QC7hOyuWzeSymNWWnhxTYnrQsGunPiXYAhoWUrcWL62Wwj6UtFJoSmehlSU7dN2cuQ4l2VTuxeuR5Dp9hruWAq9E2Ji6fRpCCz7ZEG3c6zDTWfPgrL%2F3zs%2FHVzxHCVgSR6bnNfIamNyXqqI9aLOIP4hBlwhXl1twMV0nzq1gUB2tVWU%2BnlM1RjSFx357TddPfF7bdJVuxF&X-Amz-Signature=334d40281a39cfcbbe522b1191fe2bf85c5236b7171435d5996665bda32845a8&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/91181646-b1e0-4433-9711-6259a96a9247/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UJRXWX4T%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T141400Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBYaCXVzLXdlc3QtMiJHMEUCIQD%2F%2F7NV%2BMuqWv%2FuXKqL9Z4Ht0qHZx9PES5vxTH1WI0PlwIgBVro8sduEnks64k2yuQNCtXiVnKCQItIppkyJTIU2scq%2FwMILxAAGgw2Mzc0MjMxODM4MDUiDBFk2xA%2BUioPfa9R1CrcA9jedmOSEjfJv7YPfZyYseLQIDCwUxgAM%2B0mbmd0tfj2ZRVTxp1NkTCRHNQb4jn0y1bnirYBY%2BvHj0A3QwB0qsAPTwfqO9DCTW%2FDW9ZPO8MRvts6VZLakMRwLsBUy87rj%2FFfh9oUUVtYemEzlyjvqHjs8hBxA%2BpbEmfVMlGlVyqi5YKvZKWHMBiMmTDgaKoxJ8m2SUwtHjJl7vmfRcB0b%2FIoxg%2B%2FK59geVdBhzh2Y8lGTNm%2FXhweRMFFkbLyu2tAuarKDrUesN060lcJyH5DMvZELHsdzTcDbslUWdFhdrlGU1mZgWw2dKnJjeAsuvG0cSGhYaRzRnLn68oTP9VFvjFX%2BqVg6vt%2FqQqbL134dgpQAdYEezea7RhLklEJB54POhlVfVOComRriGnxqG3V0vZ6wu%2FA51jZIlepEBIozGmWDr7gOJpBF8JCFqiLsM75rgrW0CL9hO12n%2Fbo0IEbMiiPjRb%2Bc6BnvEcbf1cgMovTyFO2ERKAlMIH35lLJOAoN9vWwY2rMmr0bgycCsPIEyCwvwybbi4iztbgLo0CrFJFZYFFtLDuldh78vkiI%2BktxhMzvZtrzgzgjHplpPTmn%2BE6Vn2SrkXQMYAmqo0x0Ea6pELVORSsUxS0wUZPMPm8iL0GOqUBYFs1odtVt2iK9YXQe6QC7hOyuWzeSymNWWnhxTYnrQsGunPiXYAhoWUrcWL62Wwj6UtFJoSmehlSU7dN2cuQ4l2VTuxeuR5Dp9hruWAq9E2Ji6fRpCCz7ZEG3c6zDTWfPgrL%2F3zs%2FHVzxHCVgSR6bnNfIamNyXqqI9aLOIP4hBlwhXl1twMV0nzq1gUB2tVWU%2BnlM1RjSFx357TddPfF7bdJVuxF&X-Amz-Signature=73122a2bbaeea3320ecdce0eb45db3270d14caba32cad4bc682bbb2159bd0829&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/09aba1c0-0d55-41dd-852a-a04c5b8a3fac/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SIXTCY26%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T141401Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBYaCXVzLXdlc3QtMiJGMEQCIE1QVBPLhOJCMMQdzB4kbQYYcx19t%2B5llXrOmwplkaHpAiA10Jo3IOYPxw%2BulXy83cceVmPXusSO67SlVNMCnwpXCSr%2FAwgvEAAaDDYzNzQyMzE4MzgwNSIMHhhJFcI%2BAja55FrSKtwD4MyyK5ucjJUQc4l6q%2FF2Ot%2F69DwGkoRM8pbnaNV%2FRVGhDnZd42Gdmy0Ssiejim9Api%2BoeVkUj0pCK4BATaC9Ez2Mabmb1D6LNJJQ0k%2BKn%2Bnf1JW6dFVh%2FdBtRK05jArNAYggHwNub6d%2Fgjy7OlFDwcFzFO9zA5AdPN7nfS6zD5Us4woPDjCEzQIL6r%2BR425zMIOWyxSwV01534rl7IuaGk3xeUBCpDvS%2Fd7JC8i%2BkWKicQVDFc%2FTIjnXTuM6h8s6Fn%2BJyegm56ftwA6cupLrc%2FC2OdGMAK5iFSTINujN926S0%2BX8z6uM8Wq%2Bo7pVp7wnML%2BI8zfLuGP%2FcepjqKK1%2BSaUhsoKXXtUxFpplUtcuBPA%2FU%2F2%2BL6%2BF09RRaAEvLk%2BVRyC762W1CBr21NaFu0PKkeW6zvd6gHmmezcuwZarpTAOXL1cD86mbtpbknCF346DdsHGTF%2FB6KiYMIyhUjdy5%2FoAiNhM29frA3GZ6hP9lKZZ6W0OytdxD%2BQxwKqtanEnQ0AmzpgdvJVUTYc6G5n6NQOYGvFGqnNhYRmDSFaybgpJKk5ZA8EUG3cCBLTDLrlAmMmh6g3WTQyCnEQ0%2B7TDCfGAocZ8LdoPlBVM7%2F3QGeBebXJzMxH1%2B%2F4oD0w67yIvQY6pgHK%2BbxOHtINjsCwiEZMRpu5aXQOUDqfFXm0k06J8Fps3njOzdzRimCPxkX6mqnhs3%2Fh5jy1mwpH1%2F8CEYLbXJ0mM%2B9ZAINuXJFtNFgfkEmXKiPwqCjBTBv%2BQUVLe8cPwzlY12G4jZ1fnaoj%2BKsQUtjemg7KwS40knXm4aEcV3JP4y5FcHEaMVrcUKQltrShhZu8PsD9SYixtiFwzg0OsVo4qcjsi75i&X-Amz-Signature=824b00635a194ae53763d3031b365d6e190199dfa5ad4ca9c1345a5b12600f44&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 2. Scatter Plot
Scatter plots present the relationship between two variables in a dataset. It represents data points on a two-dimensional plane. The independent variable or attribute is plotted on the X-axis, while the dependent variable is plotted on the Y-axis.
**Syntax:**
```python
plt.scatter(x, y)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23708af9-659f-4f23-b626-1a4292d7842c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SIXTCY26%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T141401Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBYaCXVzLXdlc3QtMiJGMEQCIE1QVBPLhOJCMMQdzB4kbQYYcx19t%2B5llXrOmwplkaHpAiA10Jo3IOYPxw%2BulXy83cceVmPXusSO67SlVNMCnwpXCSr%2FAwgvEAAaDDYzNzQyMzE4MzgwNSIMHhhJFcI%2BAja55FrSKtwD4MyyK5ucjJUQc4l6q%2FF2Ot%2F69DwGkoRM8pbnaNV%2FRVGhDnZd42Gdmy0Ssiejim9Api%2BoeVkUj0pCK4BATaC9Ez2Mabmb1D6LNJJQ0k%2BKn%2Bnf1JW6dFVh%2FdBtRK05jArNAYggHwNub6d%2Fgjy7OlFDwcFzFO9zA5AdPN7nfS6zD5Us4woPDjCEzQIL6r%2BR425zMIOWyxSwV01534rl7IuaGk3xeUBCpDvS%2Fd7JC8i%2BkWKicQVDFc%2FTIjnXTuM6h8s6Fn%2BJyegm56ftwA6cupLrc%2FC2OdGMAK5iFSTINujN926S0%2BX8z6uM8Wq%2Bo7pVp7wnML%2BI8zfLuGP%2FcepjqKK1%2BSaUhsoKXXtUxFpplUtcuBPA%2FU%2F2%2BL6%2BF09RRaAEvLk%2BVRyC762W1CBr21NaFu0PKkeW6zvd6gHmmezcuwZarpTAOXL1cD86mbtpbknCF346DdsHGTF%2FB6KiYMIyhUjdy5%2FoAiNhM29frA3GZ6hP9lKZZ6W0OytdxD%2BQxwKqtanEnQ0AmzpgdvJVUTYc6G5n6NQOYGvFGqnNhYRmDSFaybgpJKk5ZA8EUG3cCBLTDLrlAmMmh6g3WTQyCnEQ0%2B7TDCfGAocZ8LdoPlBVM7%2F3QGeBebXJzMxH1%2B%2F4oD0w67yIvQY6pgHK%2BbxOHtINjsCwiEZMRpu5aXQOUDqfFXm0k06J8Fps3njOzdzRimCPxkX6mqnhs3%2Fh5jy1mwpH1%2F8CEYLbXJ0mM%2B9ZAINuXJFtNFgfkEmXKiPwqCjBTBv%2BQUVLe8cPwzlY12G4jZ1fnaoj%2BKsQUtjemg7KwS40knXm4aEcV3JP4y5FcHEaMVrcUKQltrShhZu8PsD9SYixtiFwzg0OsVo4qcjsi75i&X-Amz-Signature=82c9fc2f4c6aa9d61b6dfa39e5abe1f596d062b9fe62a0bffa15668e6675e5a9&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 3. Histogram
A histogram is an important visual representation of data in categorical form. To view the data in a "Binned" form, use the histogram plot with a number of bins required or with the data points that mark the bin edges. The x-axis represents the data bins, and the y-axis represents the number of elements in each bin.
**Syntax:**
```python
plt.hist(x, bins)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/24e4424a-df87-40a1-b63b-195cbdc2e0ab/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SIXTCY26%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T141401Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBYaCXVzLXdlc3QtMiJGMEQCIE1QVBPLhOJCMMQdzB4kbQYYcx19t%2B5llXrOmwplkaHpAiA10Jo3IOYPxw%2BulXy83cceVmPXusSO67SlVNMCnwpXCSr%2FAwgvEAAaDDYzNzQyMzE4MzgwNSIMHhhJFcI%2BAja55FrSKtwD4MyyK5ucjJUQc4l6q%2FF2Ot%2F69DwGkoRM8pbnaNV%2FRVGhDnZd42Gdmy0Ssiejim9Api%2BoeVkUj0pCK4BATaC9Ez2Mabmb1D6LNJJQ0k%2BKn%2Bnf1JW6dFVh%2FdBtRK05jArNAYggHwNub6d%2Fgjy7OlFDwcFzFO9zA5AdPN7nfS6zD5Us4woPDjCEzQIL6r%2BR425zMIOWyxSwV01534rl7IuaGk3xeUBCpDvS%2Fd7JC8i%2BkWKicQVDFc%2FTIjnXTuM6h8s6Fn%2BJyegm56ftwA6cupLrc%2FC2OdGMAK5iFSTINujN926S0%2BX8z6uM8Wq%2Bo7pVp7wnML%2BI8zfLuGP%2FcepjqKK1%2BSaUhsoKXXtUxFpplUtcuBPA%2FU%2F2%2BL6%2BF09RRaAEvLk%2BVRyC762W1CBr21NaFu0PKkeW6zvd6gHmmezcuwZarpTAOXL1cD86mbtpbknCF346DdsHGTF%2FB6KiYMIyhUjdy5%2FoAiNhM29frA3GZ6hP9lKZZ6W0OytdxD%2BQxwKqtanEnQ0AmzpgdvJVUTYc6G5n6NQOYGvFGqnNhYRmDSFaybgpJKk5ZA8EUG3cCBLTDLrlAmMmh6g3WTQyCnEQ0%2B7TDCfGAocZ8LdoPlBVM7%2F3QGeBebXJzMxH1%2B%2F4oD0w67yIvQY6pgHK%2BbxOHtINjsCwiEZMRpu5aXQOUDqfFXm0k06J8Fps3njOzdzRimCPxkX6mqnhs3%2Fh5jy1mwpH1%2F8CEYLbXJ0mM%2B9ZAINuXJFtNFgfkEmXKiPwqCjBTBv%2BQUVLe8cPwzlY12G4jZ1fnaoj%2BKsQUtjemg7KwS40knXm4aEcV3JP4y5FcHEaMVrcUKQltrShhZu8PsD9SYixtiFwzg0OsVo4qcjsi75i&X-Amz-Signature=1fdb2a64752066ce29cfa1b801d2620eb625e9eccc77b876beef2f91afa5ebdf&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ab5a6dfe-51f5-43ee-bcb3-33dae4a1c7ad/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SIXTCY26%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T141401Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBYaCXVzLXdlc3QtMiJGMEQCIE1QVBPLhOJCMMQdzB4kbQYYcx19t%2B5llXrOmwplkaHpAiA10Jo3IOYPxw%2BulXy83cceVmPXusSO67SlVNMCnwpXCSr%2FAwgvEAAaDDYzNzQyMzE4MzgwNSIMHhhJFcI%2BAja55FrSKtwD4MyyK5ucjJUQc4l6q%2FF2Ot%2F69DwGkoRM8pbnaNV%2FRVGhDnZd42Gdmy0Ssiejim9Api%2BoeVkUj0pCK4BATaC9Ez2Mabmb1D6LNJJQ0k%2BKn%2Bnf1JW6dFVh%2FdBtRK05jArNAYggHwNub6d%2Fgjy7OlFDwcFzFO9zA5AdPN7nfS6zD5Us4woPDjCEzQIL6r%2BR425zMIOWyxSwV01534rl7IuaGk3xeUBCpDvS%2Fd7JC8i%2BkWKicQVDFc%2FTIjnXTuM6h8s6Fn%2BJyegm56ftwA6cupLrc%2FC2OdGMAK5iFSTINujN926S0%2BX8z6uM8Wq%2Bo7pVp7wnML%2BI8zfLuGP%2FcepjqKK1%2BSaUhsoKXXtUxFpplUtcuBPA%2FU%2F2%2BL6%2BF09RRaAEvLk%2BVRyC762W1CBr21NaFu0PKkeW6zvd6gHmmezcuwZarpTAOXL1cD86mbtpbknCF346DdsHGTF%2FB6KiYMIyhUjdy5%2FoAiNhM29frA3GZ6hP9lKZZ6W0OytdxD%2BQxwKqtanEnQ0AmzpgdvJVUTYc6G5n6NQOYGvFGqnNhYRmDSFaybgpJKk5ZA8EUG3cCBLTDLrlAmMmh6g3WTQyCnEQ0%2B7TDCfGAocZ8LdoPlBVM7%2F3QGeBebXJzMxH1%2B%2F4oD0w67yIvQY6pgHK%2BbxOHtINjsCwiEZMRpu5aXQOUDqfFXm0k06J8Fps3njOzdzRimCPxkX6mqnhs3%2Fh5jy1mwpH1%2F8CEYLbXJ0mM%2B9ZAINuXJFtNFgfkEmXKiPwqCjBTBv%2BQUVLe8cPwzlY12G4jZ1fnaoj%2BKsQUtjemg7KwS40knXm4aEcV3JP4y5FcHEaMVrcUKQltrShhZu8PsD9SYixtiFwzg0OsVo4qcjsi75i&X-Amz-Signature=a612c93227f9397df70c941128a6bcfa785684b98b3524bd16b56eb336ff0378&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8f1b1d60-cf1b-42b3-9faa-f634c89c3f84/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SIXTCY26%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T141401Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBYaCXVzLXdlc3QtMiJGMEQCIE1QVBPLhOJCMMQdzB4kbQYYcx19t%2B5llXrOmwplkaHpAiA10Jo3IOYPxw%2BulXy83cceVmPXusSO67SlVNMCnwpXCSr%2FAwgvEAAaDDYzNzQyMzE4MzgwNSIMHhhJFcI%2BAja55FrSKtwD4MyyK5ucjJUQc4l6q%2FF2Ot%2F69DwGkoRM8pbnaNV%2FRVGhDnZd42Gdmy0Ssiejim9Api%2BoeVkUj0pCK4BATaC9Ez2Mabmb1D6LNJJQ0k%2BKn%2Bnf1JW6dFVh%2FdBtRK05jArNAYggHwNub6d%2Fgjy7OlFDwcFzFO9zA5AdPN7nfS6zD5Us4woPDjCEzQIL6r%2BR425zMIOWyxSwV01534rl7IuaGk3xeUBCpDvS%2Fd7JC8i%2BkWKicQVDFc%2FTIjnXTuM6h8s6Fn%2BJyegm56ftwA6cupLrc%2FC2OdGMAK5iFSTINujN926S0%2BX8z6uM8Wq%2Bo7pVp7wnML%2BI8zfLuGP%2FcepjqKK1%2BSaUhsoKXXtUxFpplUtcuBPA%2FU%2F2%2BL6%2BF09RRaAEvLk%2BVRyC762W1CBr21NaFu0PKkeW6zvd6gHmmezcuwZarpTAOXL1cD86mbtpbknCF346DdsHGTF%2FB6KiYMIyhUjdy5%2FoAiNhM29frA3GZ6hP9lKZZ6W0OytdxD%2BQxwKqtanEnQ0AmzpgdvJVUTYc6G5n6NQOYGvFGqnNhYRmDSFaybgpJKk5ZA8EUG3cCBLTDLrlAmMmh6g3WTQyCnEQ0%2B7TDCfGAocZ8LdoPlBVM7%2F3QGeBebXJzMxH1%2B%2F4oD0w67yIvQY6pgHK%2BbxOHtINjsCwiEZMRpu5aXQOUDqfFXm0k06J8Fps3njOzdzRimCPxkX6mqnhs3%2Fh5jy1mwpH1%2F8CEYLbXJ0mM%2B9ZAINuXJFtNFgfkEmXKiPwqCjBTBv%2BQUVLe8cPwzlY12G4jZ1fnaoj%2BKsQUtjemg7KwS40knXm4aEcV3JP4y5FcHEaMVrcUKQltrShhZu8PsD9SYixtiFwzg0OsVo4qcjsi75i&X-Amz-Signature=679ad220532ae4a0a9680a27abc5436d2785ae7879fe516e5eac0d910fb5fa02&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/13ad0497-05fe-4eaa-984e-707b33e14761/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SIXTCY26%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T141401Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBYaCXVzLXdlc3QtMiJGMEQCIE1QVBPLhOJCMMQdzB4kbQYYcx19t%2B5llXrOmwplkaHpAiA10Jo3IOYPxw%2BulXy83cceVmPXusSO67SlVNMCnwpXCSr%2FAwgvEAAaDDYzNzQyMzE4MzgwNSIMHhhJFcI%2BAja55FrSKtwD4MyyK5ucjJUQc4l6q%2FF2Ot%2F69DwGkoRM8pbnaNV%2FRVGhDnZd42Gdmy0Ssiejim9Api%2BoeVkUj0pCK4BATaC9Ez2Mabmb1D6LNJJQ0k%2BKn%2Bnf1JW6dFVh%2FdBtRK05jArNAYggHwNub6d%2Fgjy7OlFDwcFzFO9zA5AdPN7nfS6zD5Us4woPDjCEzQIL6r%2BR425zMIOWyxSwV01534rl7IuaGk3xeUBCpDvS%2Fd7JC8i%2BkWKicQVDFc%2FTIjnXTuM6h8s6Fn%2BJyegm56ftwA6cupLrc%2FC2OdGMAK5iFSTINujN926S0%2BX8z6uM8Wq%2Bo7pVp7wnML%2BI8zfLuGP%2FcepjqKK1%2BSaUhsoKXXtUxFpplUtcuBPA%2FU%2F2%2BL6%2BF09RRaAEvLk%2BVRyC762W1CBr21NaFu0PKkeW6zvd6gHmmezcuwZarpTAOXL1cD86mbtpbknCF346DdsHGTF%2FB6KiYMIyhUjdy5%2FoAiNhM29frA3GZ6hP9lKZZ6W0OytdxD%2BQxwKqtanEnQ0AmzpgdvJVUTYc6G5n6NQOYGvFGqnNhYRmDSFaybgpJKk5ZA8EUG3cCBLTDLrlAmMmh6g3WTQyCnEQ0%2B7TDCfGAocZ8LdoPlBVM7%2F3QGeBebXJzMxH1%2B%2F4oD0w67yIvQY6pgHK%2BbxOHtINjsCwiEZMRpu5aXQOUDqfFXm0k06J8Fps3njOzdzRimCPxkX6mqnhs3%2Fh5jy1mwpH1%2F8CEYLbXJ0mM%2B9ZAINuXJFtNFgfkEmXKiPwqCjBTBv%2BQUVLe8cPwzlY12G4jZ1fnaoj%2BKsQUtjemg7KwS40knXm4aEcV3JP4y5FcHEaMVrcUKQltrShhZu8PsD9SYixtiFwzg0OsVo4qcjsi75i&X-Amz-Signature=853ddb4f24ed20a557d70d2231d28c21a507acc06e852466e36bf7b034ba779f&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 2. Box and Whisker Plot
A box plot shows the distribution of quantitative data in a way that facilitates comparisons between variables or across levels of a categorical variable. The box shows the quartiles of the dataset while the whiskers extend to show the rest of the distribution, except for points that are determined to be "outliers".
**Syntax:**
```python
sns.boxplot(x='header_1', y='header_2', data=df)
```
**Example Output:**


![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d207ae92-0a7c-4e2f-aa65-0ee5a2c33bf7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663RISFZCM%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T141404Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBYaCXVzLXdlc3QtMiJIMEYCIQDXXR09WEn5lNcF68PsOLnbn%2FhJ1CdDysaYrdAMpEcJCAIhAJT%2F62oMW3qoMOXOJjK41Vrsp9iiQPjpNPB6DKW9DeywKv8DCC8QABoMNjM3NDIzMTgzODA1IgyAwpGVnk3RQjC9718q3ANjpYqi93gBZLCKq3pb9kFyoc7h5rLacU2fYnd3a6mW%2FSGriXIlQjFn72eU38%2BRG8QQwLs7%2BTi7fASZNkSyBr2hu6L8%2BkcHTDW0kTKl1qCrtGWXkZbknvLM0Gb0XPU6S4EpkN6YgI2QjWIXub%2FIII3Y%2Bfk%2FVCQd%2BjrwfHQ%2Bv2AfwZHjP%2BOmwYzourRFw40Bcyc5E%2Fkhw%2B%2FWDoXEXVtAybHvFbqk1sjLyQ3arV8Neej%2FkLQ2LaWUK2PvGKPA7JaOCzRTEyjzuVGqbSA2bUGT78PSY6Ecq9lIxZwlalelK1sO9Ybuif4o%2Bl4%2Bvyw%2BXOZY%2BHVhpdlM66aTNeQ%2FzANQNKzzqfc%2FATC2vyVVyMBLNaSIwtTYNW12jWgB1XRFy3BfPcX4byPaX1DKwUhvHdEcdK7jPP0kxjPoZR9b8RLlPJwO0T9xZoJGtnC%2BzY60jD8pYgvC7bzcNTrpYjp4IbZn9uCDcP8dRCQTA2p4cDL9N1j6Ihwat7PKDJ8QvN4YwD1bzo2WHkorwhBIjx9B5sniR0TYI5okHXgj3wWk3iGzRFFyj%2FJD2lTi1%2B9SzGH%2FPUjMThxqIvS74bV5xHX2Tkh1htNmeRN8SpRVyAyJVO805FU0tjb0Qmnpao7vQWk4fzC2vIi9BjqkAfvSSz2YwagGPQLp6QeQhgrS%2F0IqpStPG8IqGDR7lv9lmEB4v%2FIOUYV69pGcuKNxMeqA%2B%2FHB1i7SWV%2B%2BCj4w1o0Hfdgdp5lzSS3kgjViaEq%2FZR1G4HNCrnqbodK9tcuk1TBNvKlPOSiTIcEusy4impqc9boND7zaYXYvajqkWXLSe415yDL0kzNBoIi9%2FZecp7nuqN54GuYp%2Bnm1lGOSY24qbioi&X-Amz-Signature=925f6b584338d066c5a288bdbf401d37e4585cfb896d2812557486ac003c5d77&X-Amz-SignedHeaders=host&x-id=GetObject)

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0e516edc-7551-4792-ab18-0494db3c4c0c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667FSVHK2R%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T141404Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBYaCXVzLXdlc3QtMiJIMEYCIQDn5zywRmRoCf%2F%2FTiu1dfXol%2F8Plz8CvnYq0HW9md3F9wIhAKOqLvHhltXmghDhakyqcL7H4mf68nqf0di0Tpynx6X8Kv8DCC8QABoMNjM3NDIzMTgzODA1Igxubx8Mgm2rQcplt%2Foq3AMozdUqQCbRHXMfBRYQ%2B9nRbqUKOft8w9%2BtvfFqbesqb6N9A81hAmBalhPB3QclD6q0b5IITwMYm2es6SOn5GPoa8Vwy6%2BFV%2FVt3iogy8%2Fj1WABPV72i82TNJLuBCOIYp4fqvBHXe%2FYBtq5AtGIj%2FEWH6GzG3XTAV4LEOENwu4%2Bv3zAXLQRl%2FYOu4ovwBPAfiIs60UVMW9gol4cdBYKSYJYsSrv3BGHrW%2B%2Fn1Ivj5KmFrXpRmTm3GeKsvPso8JbChIu%2B9qFMx3KLYUmq0nt41%2BIXv4d5D%2Bb0rrCUwWS2FmNJqqAkBjyALrr4ospqWcGLbWL4%2BhES90VENkGHQhl3mKe3uStHw6BBZ7vFJvmcrNeHGg5d2ymGWKJOA1XuNDR48KOAKASO8vXrCUkJ63BtPwHN29%2BJVNhl4LQ3dxCvZyPRSZOBa0LMtJ3fgpaIwKArjXdLq461sHDjgV%2Fr3LqGBG1DCn04%2BmM542NhDQuV8SKUda4xcx3DxDAaNaWXCzEB5C7qwykaPziO%2FQJNtd%2Fxq0MCBnPLXAEgQPbleH%2FCWvv3XoYU8ZXn%2Bv4GTfcmoHKryeImiMyTEX9svDS70jtFiIub1QI2zyEbmY1sI%2FaYCFbbKOSr9wA26iy6BUSUTDBvIi9BjqkARxU7JkAe41DSDBtjiutJsMjqzVHhRp37um3et5rooXbWZYOI8NsQR56wZTYH8X801lK0xJwiWRzo3BMPoj7AHdenkDW2q3VEFj8F6k5tDIlF%2BMYM%2BYOq%2BN0PitBv2qXmX4nhZp9n6ucIHCC4beWQqfEKaY4zBiUp7DP47ZabMvp%2FUvVXllMTi9SNiSVLHFSzJIPZPaUX0W1h0OpqaEdljChr%2BJg&X-Amz-Signature=a1b4dc686d3ac5d02407cd0791649884a640b37573fc062d11d5cee8de935649&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23a79b9d-2356-49a9-8fd9-65c6b0ab2cc5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SIXTCY26%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T141401Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBYaCXVzLXdlc3QtMiJGMEQCIE1QVBPLhOJCMMQdzB4kbQYYcx19t%2B5llXrOmwplkaHpAiA10Jo3IOYPxw%2BulXy83cceVmPXusSO67SlVNMCnwpXCSr%2FAwgvEAAaDDYzNzQyMzE4MzgwNSIMHhhJFcI%2BAja55FrSKtwD4MyyK5ucjJUQc4l6q%2FF2Ot%2F69DwGkoRM8pbnaNV%2FRVGhDnZd42Gdmy0Ssiejim9Api%2BoeVkUj0pCK4BATaC9Ez2Mabmb1D6LNJJQ0k%2BKn%2Bnf1JW6dFVh%2FdBtRK05jArNAYggHwNub6d%2Fgjy7OlFDwcFzFO9zA5AdPN7nfS6zD5Us4woPDjCEzQIL6r%2BR425zMIOWyxSwV01534rl7IuaGk3xeUBCpDvS%2Fd7JC8i%2BkWKicQVDFc%2FTIjnXTuM6h8s6Fn%2BJyegm56ftwA6cupLrc%2FC2OdGMAK5iFSTINujN926S0%2BX8z6uM8Wq%2Bo7pVp7wnML%2BI8zfLuGP%2FcepjqKK1%2BSaUhsoKXXtUxFpplUtcuBPA%2FU%2F2%2BL6%2BF09RRaAEvLk%2BVRyC762W1CBr21NaFu0PKkeW6zvd6gHmmezcuwZarpTAOXL1cD86mbtpbknCF346DdsHGTF%2FB6KiYMIyhUjdy5%2FoAiNhM29frA3GZ6hP9lKZZ6W0OytdxD%2BQxwKqtanEnQ0AmzpgdvJVUTYc6G5n6NQOYGvFGqnNhYRmDSFaybgpJKk5ZA8EUG3cCBLTDLrlAmMmh6g3WTQyCnEQ0%2B7TDCfGAocZ8LdoPlBVM7%2F3QGeBebXJzMxH1%2B%2F4oD0w67yIvQY6pgHK%2BbxOHtINjsCwiEZMRpu5aXQOUDqfFXm0k06J8Fps3njOzdzRimCPxkX6mqnhs3%2Fh5jy1mwpH1%2F8CEYLbXJ0mM%2B9ZAINuXJFtNFgfkEmXKiPwqCjBTBv%2BQUVLe8cPwzlY12G4jZ1fnaoj%2BKsQUtjemg7KwS40knXm4aEcV3JP4y5FcHEaMVrcUKQltrShhZu8PsD9SYixtiFwzg0OsVo4qcjsi75i&X-Amz-Signature=5c85d02f878263de69bdf0ca12153b2905ad86474b0ed9ca4bfe4a08333e35f5&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 4. KDE Plot
A Kernel Density Estimate (KDE) plot is a graph that creates a probability distribution curve for the data based upon its likelihood of occurrence on a specific value. This is created for a single vector of information.
**Syntax:**
```python
sns.kdeplot(X) || sns.kdeplot(df['age'])
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0d571213-2a2f-4921-a50b-880847aa05ee/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SIXTCY26%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T141401Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBYaCXVzLXdlc3QtMiJGMEQCIE1QVBPLhOJCMMQdzB4kbQYYcx19t%2B5llXrOmwplkaHpAiA10Jo3IOYPxw%2BulXy83cceVmPXusSO67SlVNMCnwpXCSr%2FAwgvEAAaDDYzNzQyMzE4MzgwNSIMHhhJFcI%2BAja55FrSKtwD4MyyK5ucjJUQc4l6q%2FF2Ot%2F69DwGkoRM8pbnaNV%2FRVGhDnZd42Gdmy0Ssiejim9Api%2BoeVkUj0pCK4BATaC9Ez2Mabmb1D6LNJJQ0k%2BKn%2Bnf1JW6dFVh%2FdBtRK05jArNAYggHwNub6d%2Fgjy7OlFDwcFzFO9zA5AdPN7nfS6zD5Us4woPDjCEzQIL6r%2BR425zMIOWyxSwV01534rl7IuaGk3xeUBCpDvS%2Fd7JC8i%2BkWKicQVDFc%2FTIjnXTuM6h8s6Fn%2BJyegm56ftwA6cupLrc%2FC2OdGMAK5iFSTINujN926S0%2BX8z6uM8Wq%2Bo7pVp7wnML%2BI8zfLuGP%2FcepjqKK1%2BSaUhsoKXXtUxFpplUtcuBPA%2FU%2F2%2BL6%2BF09RRaAEvLk%2BVRyC762W1CBr21NaFu0PKkeW6zvd6gHmmezcuwZarpTAOXL1cD86mbtpbknCF346DdsHGTF%2FB6KiYMIyhUjdy5%2FoAiNhM29frA3GZ6hP9lKZZ6W0OytdxD%2BQxwKqtanEnQ0AmzpgdvJVUTYc6G5n6NQOYGvFGqnNhYRmDSFaybgpJKk5ZA8EUG3cCBLTDLrlAmMmh6g3WTQyCnEQ0%2B7TDCfGAocZ8LdoPlBVM7%2F3QGeBebXJzMxH1%2B%2F4oD0w67yIvQY6pgHK%2BbxOHtINjsCwiEZMRpu5aXQOUDqfFXm0k06J8Fps3njOzdzRimCPxkX6mqnhs3%2Fh5jy1mwpH1%2F8CEYLbXJ0mM%2B9ZAINuXJFtNFgfkEmXKiPwqCjBTBv%2BQUVLe8cPwzlY12G4jZ1fnaoj%2BKsQUtjemg7KwS40knXm4aEcV3JP4y5FcHEaMVrcUKQltrShhZu8PsD9SYixtiFwzg0OsVo4qcjsi75i&X-Amz-Signature=3dea36b949cb5701a8da62b4fc8bd3f02c6e6a2dd4fd6f23434507db94c1ee86&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/53752550-ef82-4ca9-a01a-09921f0282d0/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SIXTCY26%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T141401Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBYaCXVzLXdlc3QtMiJGMEQCIE1QVBPLhOJCMMQdzB4kbQYYcx19t%2B5llXrOmwplkaHpAiA10Jo3IOYPxw%2BulXy83cceVmPXusSO67SlVNMCnwpXCSr%2FAwgvEAAaDDYzNzQyMzE4MzgwNSIMHhhJFcI%2BAja55FrSKtwD4MyyK5ucjJUQc4l6q%2FF2Ot%2F69DwGkoRM8pbnaNV%2FRVGhDnZd42Gdmy0Ssiejim9Api%2BoeVkUj0pCK4BATaC9Ez2Mabmb1D6LNJJQ0k%2BKn%2Bnf1JW6dFVh%2FdBtRK05jArNAYggHwNub6d%2Fgjy7OlFDwcFzFO9zA5AdPN7nfS6zD5Us4woPDjCEzQIL6r%2BR425zMIOWyxSwV01534rl7IuaGk3xeUBCpDvS%2Fd7JC8i%2BkWKicQVDFc%2FTIjnXTuM6h8s6Fn%2BJyegm56ftwA6cupLrc%2FC2OdGMAK5iFSTINujN926S0%2BX8z6uM8Wq%2Bo7pVp7wnML%2BI8zfLuGP%2FcepjqKK1%2BSaUhsoKXXtUxFpplUtcuBPA%2FU%2F2%2BL6%2BF09RRaAEvLk%2BVRyC762W1CBr21NaFu0PKkeW6zvd6gHmmezcuwZarpTAOXL1cD86mbtpbknCF346DdsHGTF%2FB6KiYMIyhUjdy5%2FoAiNhM29frA3GZ6hP9lKZZ6W0OytdxD%2BQxwKqtanEnQ0AmzpgdvJVUTYc6G5n6NQOYGvFGqnNhYRmDSFaybgpJKk5ZA8EUG3cCBLTDLrlAmMmh6g3WTQyCnEQ0%2B7TDCfGAocZ8LdoPlBVM7%2F3QGeBebXJzMxH1%2B%2F4oD0w67yIvQY6pgHK%2BbxOHtINjsCwiEZMRpu5aXQOUDqfFXm0k06J8Fps3njOzdzRimCPxkX6mqnhs3%2Fh5jy1mwpH1%2F8CEYLbXJ0mM%2B9ZAINuXJFtNFgfkEmXKiPwqCjBTBv%2BQUVLe8cPwzlY12G4jZ1fnaoj%2BKsQUtjemg7KwS40knXm4aEcV3JP4y5FcHEaMVrcUKQltrShhZu8PsD9SYixtiFwzg0OsVo4qcjsi75i&X-Amz-Signature=ee7913a3c17773f4a4a5e36b7cf005826df8c775f1c9799914f0a55fd60ebfa2&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
## 4. Correlation Between Variables
Correlation is a statistical measure of the extent to which different variables are interdependent. It indicates how changes in one variable are associated with changes in another variable over time.
### Positive Correlation
Positive correlation indicates that as one variable increases, the other variable also tends to increase.
**Example: Engine Size and Price**
- **Positive Correlation:** Engine size increases, price also increases.
- **Visualization:** Scatter plot with a steep positive slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c7ea9b0-3ef3-4357-a9c3-554fc71b6b15/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T5ORQMLP%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T141404Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBYaCXVzLXdlc3QtMiJGMEQCIAf%2B%2B6aLV2%2B10PqO6fNQO8xgkcsrX%2BwCXqKcx7fZq1uuAiAzZEzNMBza0OZpdX%2FefhkM48gm7WsZ0WA0%2FV4Dq5dWxyr%2FAwgvEAAaDDYzNzQyMzE4MzgwNSIM1U50ruOLUIqeLijMKtwDxDnhtkNPbnt7xI8FuWFaE3Tf8ivcLZOdoJ9maZIhAAvtQEFTRRfrDEnZMO3T4Ur%2FHgMjL1NuUPTMstRoxgtSRHIo9%2BHQSfV0gj4psgoaIxwFr9N1fSUrOfmitnnWm4rQAi9R0AtcRkY%2B8vhAeiUSMU%2F4OcUk%2Bd9gjW%2B12wr%2FLemXz55LBCknbb%2BczAWZ3OA5%2BBU43mZw0JKcRz7gVMPsMl1mQK5r1qqf9yPDN0LIour%2F5Hekejr5%2Fzk1SjZtdPNzz9Ge%2BJgWhvnCI55cnOwzJuyIcWoCPdsfZWPcwxLQu4gxfJ74DLcfm0%2BDh8bqViDni0F%2BwU2hM6SEiaH%2Bcur1vHV1b3%2FDKX3W3dKLgSmDdqj9Zv%2B7iukgXBxKg67RJ%2B0uUzcDW1VCLOmwHnMGMX1r5kgBIgWxQ5WmZFjsSHZIuIx%2BKIiaYzpM5mppOY3MVbZQZDTLn9RCus5%2BpkCMbVGRLMZ1vFi%2Ft2QJM8x0qEbbtZUS9c9pN%2BSroAHnUlRO4BaAQAXPSSwPJ%2BG7qgTRg0BA6UoNB6HOU5kxaf6jF0u7sh3mw5LhN6ZPU6ToWgdZN9adq2tcWiRk%2B5nc7ia0ivnMC5Am2yyfVDzxpLzBnOGzCOXo%2FhakgPpf2rClAE4wir2IvQY6pgFOj2kxLw3%2F86INtsvDQEiIYM3iTDQhHRif3vpJL43P00VIjTsvrBsve%2BCSN1q90YAWQ5BGnH1wT9O%2BoWbfSYZzuyJEt5c6ywUqYHAo%2B%2Fwpej%2FQS34TsA9e4pIq5YlREXoIFBPQnBkqWz8v2OGyH2yZLvXlly2klL6sQjg4mCkmpiADxJkzq9gPL66UwIHJz7aBLnqK46jFkydCmy4O27PE3WNtp%2Bu5&X-Amz-Signature=f197929f2cc80cae74f46fbe7cc4e4d04a3d9b5f19543c043c041a963a2d52ed&X-Amz-SignedHeaders=host&x-id=GetObject)
**Explanation:** When engine size increases, there is a corresponding increase in the price of the vehicle. This positive correlation suggests that larger engines tend to be associated with higher prices in the market.
___
### Negative Correlation
Negative correlation indicates that as one variable increases, the other variable tends to decrease.
**Example: Highway Miles per Gallon and Price**
- **Negative Correlation:** As highway miles per gallon increases, price decreases.
- **Visualization:** Scatter plot with a steep negative slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/10f1f798-9cc4-4df2-a9c1-5a339f554a0b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WTNZY3FH%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T141404Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBYaCXVzLXdlc3QtMiJIMEYCIQDYGzLzUKlwZxP%2Fw2590VlAn7FMytFYo8V7GUwrHd10hgIhAIqo3Lz41sQeY%2FVCuVqmIcfADcmSb1Qjv8dx5rGaFiJSKv8DCC8QABoMNjM3NDIzMTgzODA1IgwcCk4g1hmzZeXN6C0q3ANiiymNGsdTthdjicZU2eqd4MJsY7CtGQ7j9ZYjxi7jVuqKu%2FWct7y3bONY47Djj62qzRDi5l7euKbsTHezuECCC9kMBgg6%2BG3aTAd55tFzowHEGmHU77HVMj94IRm%2B%2FrXUK0VI4xfXgUcYu6yJVNgSPEDAzFyQx5OnLusadCIF94nPmUTPIkxu2iAeowpjsGq00bVJw%2F2L%2BMYzLQIgtJE%2BG2BzuePp8VN8vxNiSF1vlsHrM8xruEnOHx5zcDZ7LtH1oEiYnUthCGbNADO9%2BnHvb92OU9DIqSrq6h8WsXfq74oUanMigewba8ijtQhm4V3U5QVMSUmqGQuMo1bkKfKO0zC9%2FtJcV6CjhW1aGAG4luzD52cbVpVWmLYOtfkR0fUQaM0UCG%2FJfRNP0YEVljjZf2tHrXYLl%2BH8Iy7uLFCjQPYJLXvuAuxez9J0L3kSWe%2B9GPwYrKrWGGZZXii8fkhcOVQ9NqSCsNW1FeRftrzRpcxq1P0hzptNW8hUCUr1RQqBbuAe84lGRdybkYIdEXVqV2PxtUNtXUB2l1HdukZdEniePYQbubNR6tsY2c0YyjAokyj8Zj%2By1RimWIOUe%2Fk31lDGXg6VoorzZ4Mw%2B0CAcb41evIP1ji%2FsR8i2DCOvYi9BjqkAUBHDzvxDFHjSk3wxlkzyNCZfkvT53BswHjnD6lK5fTnhMlNGxttPy2EweiR%2B0Q%2F5AS1ppKhiUuwhEELNhfTuTNDgBmh2HSDsHXW7jBmbyDcOy1V9GCXrE29oIF4Zr1efi2NzuU0o3p8LQOXwn7%2B1b4fCCkaenp5DluSMKBuSsgMA5IfzMVvovvzsNdmGR8wVmc8%2BoyAybUfyfSswYhp4w2JrC%2BU&X-Amz-Signature=68a2e848b98b47109030583b0d9bfcf972f815f30b7ae339d2ee934ce77cae87&X-Amz-SignedHeaders=host&x-id=GetObject)
**Explanation:** When highway miles per gallon increases, the price of the vehicle tends to decrease. This negative correlation suggests that cars with higher fuel efficiency (more miles per gallon) are generally priced lower in the market.
___
### Weak Correlation
Weak correlation indicates a lack of strong relationship between the variables.
**Example: RPM and Price**
- **Weak Correlation:** Low and high RPM values show varied prices, indicating no strong predictive relationship.
- **Visualization:** Scatter plot with no clear trend or slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9f914514-8914-4bf4-ac84-d9e3077f6eb1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Z5U57C4J%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T141403Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBYaCXVzLXdlc3QtMiJGMEQCICq4d8D%2FJiw2X%2BuHSWnZ1OxFnS00CMqgOgVS85yIMyS%2FAiBmqfBpmpl9xs2xfxtAxFF7XldwE2ad28MOgu0ot1aO7ir%2FAwgvEAAaDDYzNzQyMzE4MzgwNSIMdQT8NaqumYGdJxGXKtwDlIYy4buheqpiNLUeqX8DaoCubmq6WP4PUHdov4uOHLfppr%2B3n3OQNh1CKaZ0m6ohw%2FMAEA9MZMG8KXzsgkM%2FD4hhmSXEfHf3ESvQAgmqIBXSjyYsFol9ZaY4RVXGg%2Bu2kLTEWzXBKMObWUMAWqZ1hVpPf%2FgHAOM9pNuIFUG8WBxfkFuROnCQnhkTXZgCHx2i1%2FwYtJ0OlgnqnItBf13uYgffby3oe5m9qmA4OLQZ1xQCj52xgLqqTYJ4fkLDsn%2B5vF3RiZufVV99t%2FmiUUbotQbeAiFDBEe7UGeIQkBW7YdZMvedOLwwmCimuGjLmYDL3uJUWqHRa9QU4hC4OjUMQY5Tk%2BqIdN5JQOhLFUXhUmaA31ewKxhbbX2rGRthb%2FfksEhovYDfxEQb2nJIbJZmAK87ZeHUE3bknSluC9UubkbSDoiOfPSo66j0fiwBozRGeD0HoNM7qwU24XM0wWE%2FjFFYJG0%2B3K0%2B5%2BwbV6hBxstE4N9GOd5STBoOyEJoWwIxu1g5vWzLrrHm0FDzX%2FvX1zFhhQ8lWDORtAlggPDyuLkAIEgnxFFjxg03vc9Ol9zPWFOzpfqdTHIPTWAnHjj1XPsBKTDYOO5cXOUznQi%2BdJsxymtJ7E4zI1Y6%2Bmkwjr2IvQY6pgF0XiKCbKb9sGO8U0TkitRg6NNH0C8GPbKxvSual7Ayjx%2BdKYgAM5jq3eaJtEvER27PTjYNNVrhsnT04EeVgv3yAcktOfEIjxO5yly77ADhgMG09%2FbEFHAvssDc6xE6L4OsuSN0198NxXJjHP1jBYFfpjovy9b5YNBDlBg%2BvRd4dOlw7qGzcVnXyuP1KEjYkl%2BvVfA2ce6wWPTE6N5CyTkdxCldpHXP&X-Amz-Signature=ea7157be311dada112783e368922251b4bf4e6b87df589930fc811516b4be57e&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f18086e5-5b04-4fbf-8309-8944ab20d213/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VZSWL2NI%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T141403Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBYaCXVzLXdlc3QtMiJIMEYCIQCHk2YyLICTrBh%2F%2BUR5nvixo6%2FJ1%2B3%2Bxz1i91JbxrsKyQIhAIykDChCspfmTeqFxWGp7GgON43GtYMRCuVrAqzV53U7Kv8DCC8QABoMNjM3NDIzMTgzODA1IgzoqKOT7Gex26OIyXYq3ANib%2FB8I4H2kY3caxyNpQaLo9RK8gcQOj8ghJ94uw6gShUzAE8ToNsASmHe77j2MjwlxwE96CrRBFjNh9mmzmOIg9e5TfjVKPJrdNm%2BescuTA6kQpNeNqvd0bzY4cWh%2BNaofG40IFUZ5fP%2BZYOp2mm6v6LyO5qS98E4wKn3I8kHe3Hyub7D4YYNatoItinuQZICJCh%2FMzChp7QVtUoJrIN7X5ygIwTicYNIClMqZc5E%2BcuGI5eIQn53Ori6taz4pJxO5A6upnkdD0CS4EALpTZkzST%2BK5DRe%2BY8wlpJ03wQCu2j6eVTGgY5M68ReRX6jY42QsVBqtMUpQffOC4pWrxURzpnLfW%2BL%2B3hxDjT748J5580LatsAAVU09VYpUmDzd27gY0Dtj4cXc3xjv4jazsBfZ8YowVsNVSXdNhmbLrLeZUtjlGjuRuqW8Ezthca7r%2BtKDkNakrQhTm1hxBB5BP0w7kXFGLuNtS54Ow3t%2FGAu07bSvMDeueqoFsCQC0pGPHo%2FPQcEf%2FsQ5KupkJ0PYf264kgUWva3bKcItqTOIr%2FLdVcR4kd4RgB6QJ%2FO2nGJBMLiKdkXptXdilNoyMgxol5Ewqm62vNFjFzbZAjocd806vlClwwWpGXwWfZzDCEvYi9BjqkAeunbowUftF%2Fru04VxOAgkiMhBhI93J1RsHpReVCIhl154MpM88XuZ8AumC4zuMyON9t6s7wtk7vr4AQl%2BvLTjpVpsh79YS15dkO3hoDAqDtQ7K8nJP9qDpfoZyapkVfZKjAly6Y1TMdE2lCjI7Er6lDmL7%2FljOaRBJprvJjPusm%2BMznTfhdKCZu49K7cqe5lNW7JJS0igaegvnmudSP1WNwF6v1&X-Amz-Signature=657a3ddccbf55a9ad406d434cf4a911492ccf4f5fe4b9de22d08a41b43e07f0a&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Correlation Plot
Heatmap visualizes correlations among variables. Color scheme indicates Pearson correlation coefficients. Dark red diagonal line shows perfect correlation (value of 1) between variables and themselves.
This heatmap offers overview of variable relationships and their link with price.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cd3b341e-cc1a-45f7-8aec-cdc00436d270/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VZSWL2NI%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T141403Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBYaCXVzLXdlc3QtMiJIMEYCIQCHk2YyLICTrBh%2F%2BUR5nvixo6%2FJ1%2B3%2Bxz1i91JbxrsKyQIhAIykDChCspfmTeqFxWGp7GgON43GtYMRCuVrAqzV53U7Kv8DCC8QABoMNjM3NDIzMTgzODA1IgzoqKOT7Gex26OIyXYq3ANib%2FB8I4H2kY3caxyNpQaLo9RK8gcQOj8ghJ94uw6gShUzAE8ToNsASmHe77j2MjwlxwE96CrRBFjNh9mmzmOIg9e5TfjVKPJrdNm%2BescuTA6kQpNeNqvd0bzY4cWh%2BNaofG40IFUZ5fP%2BZYOp2mm6v6LyO5qS98E4wKn3I8kHe3Hyub7D4YYNatoItinuQZICJCh%2FMzChp7QVtUoJrIN7X5ygIwTicYNIClMqZc5E%2BcuGI5eIQn53Ori6taz4pJxO5A6upnkdD0CS4EALpTZkzST%2BK5DRe%2BY8wlpJ03wQCu2j6eVTGgY5M68ReRX6jY42QsVBqtMUpQffOC4pWrxURzpnLfW%2BL%2B3hxDjT748J5580LatsAAVU09VYpUmDzd27gY0Dtj4cXc3xjv4jazsBfZ8YowVsNVSXdNhmbLrLeZUtjlGjuRuqW8Ezthca7r%2BtKDkNakrQhTm1hxBB5BP0w7kXFGLuNtS54Ow3t%2FGAu07bSvMDeueqoFsCQC0pGPHo%2FPQcEf%2FsQ5KupkJ0PYf264kgUWva3bKcItqTOIr%2FLdVcR4kd4RgB6QJ%2FO2nGJBMLiKdkXptXdilNoyMgxol5Ewqm62vNFjFzbZAjocd806vlClwwWpGXwWfZzDCEvYi9BjqkAeunbowUftF%2Fru04VxOAgkiMhBhI93J1RsHpReVCIhl154MpM88XuZ8AumC4zuMyON9t6s7wtk7vr4AQl%2BvLTjpVpsh79YS15dkO3hoDAqDtQ7K8nJP9qDpfoZyapkVfZKjAly6Y1TMdE2lCjI7Er6lDmL7%2FljOaRBJprvJjPusm%2BMznTfhdKCZu49K7cqe5lNW7JJS0igaegvnmudSP1WNwF6v1&X-Amz-Signature=88196c608ed5353d5aa0f18f7e8834ace3e804d6d9882a5c7dbcca3c7e99db51&X-Amz-SignedHeaders=host&x-id=GetObject)

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
