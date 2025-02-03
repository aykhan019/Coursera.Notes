

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7e6d594d-952e-44b6-97ea-31225882aea6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664PFQW6MF%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T132020Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDobKr7oLzT%2B6ur%2BnhffmSV7xAPpMUM%2BZw6oqbss%2BGtwAIhAOauXin84mexC37cZzue14b0hAIg8pFKneSKPLyhhebWKv8DCBYQABoMNjM3NDIzMTgzODA1IgxMme0P2vnCLPdKME4q3AM5xjpJSK8pDKqPym7KZvDhkbtcci7EDV4EfYJ8nXpdMy3L2YrPY4dmHUHZL81tCQXadJHqhMz57ZJEXuL3dfAVhiLGHNSAp0z9YsinD%2B%2B%2BLzKEf4uKKMtN%2FxY9spWLJAML9y2zHAdF%2FYbZFLDUfng2HLUuSSfttK2jEh4LKCEs%2BguHJYhZ0Lo5CEKS4iD3PO78kSC78R47s%2BS1vcqi%2BrEWURWtYRvNPvFkuY2NwiCP2KnINdoDOSzaGA8NjzIdWJq2FqKbQ%2FMejuqaN09TnpdATzb9E06RsgtZzVdqU04FUzOBecAKe1%2FE9tQCYCrr3YWRw42c7za7q4Uf0CkU8wlHVMU9299ZZL5xYWNh4IlZuW6jMIt1DWpFV7pDvcvsCMm%2ByziMwmx1UNhXcgJif%2BiI2xIQuvFZc2uuSkoG%2F71W3DHlU%2B1Wz%2B4J0NpVGJdP6DM5wwPdTVJwUR9IG1dEEKrkmXAuQ1pxbfPV27PUbSQ5FIr6sK2XzEUi8GwxbdModXgE4ayBWca6MtDqm1fTyMGTS1gQsZ7z0cq818fiDAq25ofcycvQ9I7EWU88ESO9FbuUt2i9bYLT3mX684B44O%2Bcr2Z73R9W0BfO4blBx%2B2dN1yVR54xrnkfOeFJ7zCM8YK9BjqkAanDqGKrIR8Eoourxtl%2FChQ5gNQB%2BazA%2BAMv%2F%2BRPTVoDlR1lcr5Ky%2BHjL93ETLNM9kmTn90j%2Bnff5P6KgNAlY1JaQyI1IBA3mAHG4J7jFrLtRtLHI33og97qxCztcP7W9o3Xai7m8Rfn2%2Bd01VwihsVgGgI%2Bi2E%2FiYfmYw4%2BoHHhNUu%2BqLiAU0xEKbhfEp2oliN9JwoADzbG8hGlbWFyxhakWpji&X-Amz-Signature=710095325fb675fedf0f314e43136a60eec016285d106a2b340ab402f06a05c2&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cbfaed9e-b398-4902-8936-dea058b21def/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664PFQW6MF%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T132020Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDobKr7oLzT%2B6ur%2BnhffmSV7xAPpMUM%2BZw6oqbss%2BGtwAIhAOauXin84mexC37cZzue14b0hAIg8pFKneSKPLyhhebWKv8DCBYQABoMNjM3NDIzMTgzODA1IgxMme0P2vnCLPdKME4q3AM5xjpJSK8pDKqPym7KZvDhkbtcci7EDV4EfYJ8nXpdMy3L2YrPY4dmHUHZL81tCQXadJHqhMz57ZJEXuL3dfAVhiLGHNSAp0z9YsinD%2B%2B%2BLzKEf4uKKMtN%2FxY9spWLJAML9y2zHAdF%2FYbZFLDUfng2HLUuSSfttK2jEh4LKCEs%2BguHJYhZ0Lo5CEKS4iD3PO78kSC78R47s%2BS1vcqi%2BrEWURWtYRvNPvFkuY2NwiCP2KnINdoDOSzaGA8NjzIdWJq2FqKbQ%2FMejuqaN09TnpdATzb9E06RsgtZzVdqU04FUzOBecAKe1%2FE9tQCYCrr3YWRw42c7za7q4Uf0CkU8wlHVMU9299ZZL5xYWNh4IlZuW6jMIt1DWpFV7pDvcvsCMm%2ByziMwmx1UNhXcgJif%2BiI2xIQuvFZc2uuSkoG%2F71W3DHlU%2B1Wz%2B4J0NpVGJdP6DM5wwPdTVJwUR9IG1dEEKrkmXAuQ1pxbfPV27PUbSQ5FIr6sK2XzEUi8GwxbdModXgE4ayBWca6MtDqm1fTyMGTS1gQsZ7z0cq818fiDAq25ofcycvQ9I7EWU88ESO9FbuUt2i9bYLT3mX684B44O%2Bcr2Z73R9W0BfO4blBx%2B2dN1yVR54xrnkfOeFJ7zCM8YK9BjqkAanDqGKrIR8Eoourxtl%2FChQ5gNQB%2BazA%2BAMv%2F%2BRPTVoDlR1lcr5Ky%2BHjL93ETLNM9kmTn90j%2Bnff5P6KgNAlY1JaQyI1IBA3mAHG4J7jFrLtRtLHI33og97qxCztcP7W9o3Xai7m8Rfn2%2Bd01VwihsVgGgI%2Bi2E%2FiYfmYw4%2BoHHhNUu%2BqLiAU0xEKbhfEp2oliN9JwoADzbG8hGlbWFyxhakWpji&X-Amz-Signature=27af5fe59e1896e3b2bfc1116617859d7449134eeaf33189d4ca81e4e6321771&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/91181646-b1e0-4433-9711-6259a96a9247/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664PFQW6MF%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T132020Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDobKr7oLzT%2B6ur%2BnhffmSV7xAPpMUM%2BZw6oqbss%2BGtwAIhAOauXin84mexC37cZzue14b0hAIg8pFKneSKPLyhhebWKv8DCBYQABoMNjM3NDIzMTgzODA1IgxMme0P2vnCLPdKME4q3AM5xjpJSK8pDKqPym7KZvDhkbtcci7EDV4EfYJ8nXpdMy3L2YrPY4dmHUHZL81tCQXadJHqhMz57ZJEXuL3dfAVhiLGHNSAp0z9YsinD%2B%2B%2BLzKEf4uKKMtN%2FxY9spWLJAML9y2zHAdF%2FYbZFLDUfng2HLUuSSfttK2jEh4LKCEs%2BguHJYhZ0Lo5CEKS4iD3PO78kSC78R47s%2BS1vcqi%2BrEWURWtYRvNPvFkuY2NwiCP2KnINdoDOSzaGA8NjzIdWJq2FqKbQ%2FMejuqaN09TnpdATzb9E06RsgtZzVdqU04FUzOBecAKe1%2FE9tQCYCrr3YWRw42c7za7q4Uf0CkU8wlHVMU9299ZZL5xYWNh4IlZuW6jMIt1DWpFV7pDvcvsCMm%2ByziMwmx1UNhXcgJif%2BiI2xIQuvFZc2uuSkoG%2F71W3DHlU%2B1Wz%2B4J0NpVGJdP6DM5wwPdTVJwUR9IG1dEEKrkmXAuQ1pxbfPV27PUbSQ5FIr6sK2XzEUi8GwxbdModXgE4ayBWca6MtDqm1fTyMGTS1gQsZ7z0cq818fiDAq25ofcycvQ9I7EWU88ESO9FbuUt2i9bYLT3mX684B44O%2Bcr2Z73R9W0BfO4blBx%2B2dN1yVR54xrnkfOeFJ7zCM8YK9BjqkAanDqGKrIR8Eoourxtl%2FChQ5gNQB%2BazA%2BAMv%2F%2BRPTVoDlR1lcr5Ky%2BHjL93ETLNM9kmTn90j%2Bnff5P6KgNAlY1JaQyI1IBA3mAHG4J7jFrLtRtLHI33og97qxCztcP7W9o3Xai7m8Rfn2%2Bd01VwihsVgGgI%2Bi2E%2FiYfmYw4%2BoHHhNUu%2BqLiAU0xEKbhfEp2oliN9JwoADzbG8hGlbWFyxhakWpji&X-Amz-Signature=322863be6a099cecb896dc2fc776ce7e908e54fd3ef7b92eba7381876b795686&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/09aba1c0-0d55-41dd-852a-a04c5b8a3fac/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YGYI5UQ3%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T132020Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCKIAnx0KRinCRf0Kx%2FSKDnABYFj43hFvcghJWNj7e%2FsAIhANdULHRKeVqhlb1W4JxmkuyvA4l4gPPiL4KoxZedmlYAKv8DCBYQABoMNjM3NDIzMTgzODA1IgwcTI4z8A%2Fpt1DWcrUq3APQTAzmOZbsW2GcMlJ%2FI9bnRzVZ%2FR%2Fb8z90S9WfYIAAjI6LazBMGHTa%2FxXVNb2IkfqHHNXAR2Cjh9FPzbXAbuTyuPDB477QmiJWAXomAQpoW0PKvpF1ltpf%2BNR%2FXNiu5qh51I5gZc3UNJC09b%2FyMjV%2Bhd6Xlk74YNQogfjpX3gCzwu9%2BRMHYttYZZU%2Bb4%2BaAMzFzzExT9pqAIvw5QEn7XVFlBT5knc6dVZY4eI2RcKZLOtmtC6M4%2BFWOG9s8WiXUccjTdFFp6mkUfyJp4CruwRxXQTlYCnZEdXKxJkMUlGTT5775mdJw%2BQSlNRQVHWcmgrG6eUDDQwjW9VPwbSQHTeuIEmCPpgSq0YOYPtEoQWWL11fq1xSwLv61hPJ%2FFvehYS9e15qaBGSW1%2B7egIplTLlVuL%2F690Okpy8RXC4DLpFtVYYsELyY%2BNCAVrIFkliseIv3BxbpJnLUaGYFoBXaQIU6NXelTzmEKJQe2xy0dkNJUDkaK1kvqFe0aOp5%2F1sPLK5u%2BMev%2Fwm2IPRwBkrgZ6%2FE0DVF2IMUp9Qtz7GlDSAfghouiVHBQp7BENFUT44Jz4rNcfnRuIjs0n6kHlqeS9utDeYxXpj%2Byw4gIrx3mfBffSU93svrjymEJ07lTCM8YK9BjqkAclmbrDp3AOBsoZ8FvwrMwcZTlNBBCMf%2FxjzqBX86%2FpqQD1%2FEHhWiJtKBeKmgAtoTFP%2FEdvdXI4y3Z8JMR6PewLuRAEeIQ%2F8UxoQPt7hiW6W0%2F384UDmBMsfMU3miu%2BybCqDeVH0uGR127xmNWpCO8k3hKkXXYEOXql4wpX12JzdgZAso13hoXt7KWP5GDoTexMlaMAA%2F3QXEn0WvhGZlBR7Aoxr&X-Amz-Signature=c1106feaf635e7fef175a76d8e61bc5654b9cc6f7bd98b4ebe5b96fd5cee7e02&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 2. Scatter Plot
Scatter plots present the relationship between two variables in a dataset. It represents data points on a two-dimensional plane. The independent variable or attribute is plotted on the X-axis, while the dependent variable is plotted on the Y-axis.
**Syntax:**
```python
plt.scatter(x, y)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23708af9-659f-4f23-b626-1a4292d7842c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YGYI5UQ3%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T132020Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCKIAnx0KRinCRf0Kx%2FSKDnABYFj43hFvcghJWNj7e%2FsAIhANdULHRKeVqhlb1W4JxmkuyvA4l4gPPiL4KoxZedmlYAKv8DCBYQABoMNjM3NDIzMTgzODA1IgwcTI4z8A%2Fpt1DWcrUq3APQTAzmOZbsW2GcMlJ%2FI9bnRzVZ%2FR%2Fb8z90S9WfYIAAjI6LazBMGHTa%2FxXVNb2IkfqHHNXAR2Cjh9FPzbXAbuTyuPDB477QmiJWAXomAQpoW0PKvpF1ltpf%2BNR%2FXNiu5qh51I5gZc3UNJC09b%2FyMjV%2Bhd6Xlk74YNQogfjpX3gCzwu9%2BRMHYttYZZU%2Bb4%2BaAMzFzzExT9pqAIvw5QEn7XVFlBT5knc6dVZY4eI2RcKZLOtmtC6M4%2BFWOG9s8WiXUccjTdFFp6mkUfyJp4CruwRxXQTlYCnZEdXKxJkMUlGTT5775mdJw%2BQSlNRQVHWcmgrG6eUDDQwjW9VPwbSQHTeuIEmCPpgSq0YOYPtEoQWWL11fq1xSwLv61hPJ%2FFvehYS9e15qaBGSW1%2B7egIplTLlVuL%2F690Okpy8RXC4DLpFtVYYsELyY%2BNCAVrIFkliseIv3BxbpJnLUaGYFoBXaQIU6NXelTzmEKJQe2xy0dkNJUDkaK1kvqFe0aOp5%2F1sPLK5u%2BMev%2Fwm2IPRwBkrgZ6%2FE0DVF2IMUp9Qtz7GlDSAfghouiVHBQp7BENFUT44Jz4rNcfnRuIjs0n6kHlqeS9utDeYxXpj%2Byw4gIrx3mfBffSU93svrjymEJ07lTCM8YK9BjqkAclmbrDp3AOBsoZ8FvwrMwcZTlNBBCMf%2FxjzqBX86%2FpqQD1%2FEHhWiJtKBeKmgAtoTFP%2FEdvdXI4y3Z8JMR6PewLuRAEeIQ%2F8UxoQPt7hiW6W0%2F384UDmBMsfMU3miu%2BybCqDeVH0uGR127xmNWpCO8k3hKkXXYEOXql4wpX12JzdgZAso13hoXt7KWP5GDoTexMlaMAA%2F3QXEn0WvhGZlBR7Aoxr&X-Amz-Signature=b7ca274c5261a3156baec2a875aa1a8496b5486095835415fcd920400ad23037&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 3. Histogram
A histogram is an important visual representation of data in categorical form. To view the data in a "Binned" form, use the histogram plot with a number of bins required or with the data points that mark the bin edges. The x-axis represents the data bins, and the y-axis represents the number of elements in each bin.
**Syntax:**
```python
plt.hist(x, bins)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/24e4424a-df87-40a1-b63b-195cbdc2e0ab/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YGYI5UQ3%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T132020Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCKIAnx0KRinCRf0Kx%2FSKDnABYFj43hFvcghJWNj7e%2FsAIhANdULHRKeVqhlb1W4JxmkuyvA4l4gPPiL4KoxZedmlYAKv8DCBYQABoMNjM3NDIzMTgzODA1IgwcTI4z8A%2Fpt1DWcrUq3APQTAzmOZbsW2GcMlJ%2FI9bnRzVZ%2FR%2Fb8z90S9WfYIAAjI6LazBMGHTa%2FxXVNb2IkfqHHNXAR2Cjh9FPzbXAbuTyuPDB477QmiJWAXomAQpoW0PKvpF1ltpf%2BNR%2FXNiu5qh51I5gZc3UNJC09b%2FyMjV%2Bhd6Xlk74YNQogfjpX3gCzwu9%2BRMHYttYZZU%2Bb4%2BaAMzFzzExT9pqAIvw5QEn7XVFlBT5knc6dVZY4eI2RcKZLOtmtC6M4%2BFWOG9s8WiXUccjTdFFp6mkUfyJp4CruwRxXQTlYCnZEdXKxJkMUlGTT5775mdJw%2BQSlNRQVHWcmgrG6eUDDQwjW9VPwbSQHTeuIEmCPpgSq0YOYPtEoQWWL11fq1xSwLv61hPJ%2FFvehYS9e15qaBGSW1%2B7egIplTLlVuL%2F690Okpy8RXC4DLpFtVYYsELyY%2BNCAVrIFkliseIv3BxbpJnLUaGYFoBXaQIU6NXelTzmEKJQe2xy0dkNJUDkaK1kvqFe0aOp5%2F1sPLK5u%2BMev%2Fwm2IPRwBkrgZ6%2FE0DVF2IMUp9Qtz7GlDSAfghouiVHBQp7BENFUT44Jz4rNcfnRuIjs0n6kHlqeS9utDeYxXpj%2Byw4gIrx3mfBffSU93svrjymEJ07lTCM8YK9BjqkAclmbrDp3AOBsoZ8FvwrMwcZTlNBBCMf%2FxjzqBX86%2FpqQD1%2FEHhWiJtKBeKmgAtoTFP%2FEdvdXI4y3Z8JMR6PewLuRAEeIQ%2F8UxoQPt7hiW6W0%2F384UDmBMsfMU3miu%2BybCqDeVH0uGR127xmNWpCO8k3hKkXXYEOXql4wpX12JzdgZAso13hoXt7KWP5GDoTexMlaMAA%2F3QXEn0WvhGZlBR7Aoxr&X-Amz-Signature=5a988be34fb80aa4f512d0472efc1ffd6dd0f3898d15750b275791e804a7e3cd&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ab5a6dfe-51f5-43ee-bcb3-33dae4a1c7ad/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YGYI5UQ3%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T132020Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCKIAnx0KRinCRf0Kx%2FSKDnABYFj43hFvcghJWNj7e%2FsAIhANdULHRKeVqhlb1W4JxmkuyvA4l4gPPiL4KoxZedmlYAKv8DCBYQABoMNjM3NDIzMTgzODA1IgwcTI4z8A%2Fpt1DWcrUq3APQTAzmOZbsW2GcMlJ%2FI9bnRzVZ%2FR%2Fb8z90S9WfYIAAjI6LazBMGHTa%2FxXVNb2IkfqHHNXAR2Cjh9FPzbXAbuTyuPDB477QmiJWAXomAQpoW0PKvpF1ltpf%2BNR%2FXNiu5qh51I5gZc3UNJC09b%2FyMjV%2Bhd6Xlk74YNQogfjpX3gCzwu9%2BRMHYttYZZU%2Bb4%2BaAMzFzzExT9pqAIvw5QEn7XVFlBT5knc6dVZY4eI2RcKZLOtmtC6M4%2BFWOG9s8WiXUccjTdFFp6mkUfyJp4CruwRxXQTlYCnZEdXKxJkMUlGTT5775mdJw%2BQSlNRQVHWcmgrG6eUDDQwjW9VPwbSQHTeuIEmCPpgSq0YOYPtEoQWWL11fq1xSwLv61hPJ%2FFvehYS9e15qaBGSW1%2B7egIplTLlVuL%2F690Okpy8RXC4DLpFtVYYsELyY%2BNCAVrIFkliseIv3BxbpJnLUaGYFoBXaQIU6NXelTzmEKJQe2xy0dkNJUDkaK1kvqFe0aOp5%2F1sPLK5u%2BMev%2Fwm2IPRwBkrgZ6%2FE0DVF2IMUp9Qtz7GlDSAfghouiVHBQp7BENFUT44Jz4rNcfnRuIjs0n6kHlqeS9utDeYxXpj%2Byw4gIrx3mfBffSU93svrjymEJ07lTCM8YK9BjqkAclmbrDp3AOBsoZ8FvwrMwcZTlNBBCMf%2FxjzqBX86%2FpqQD1%2FEHhWiJtKBeKmgAtoTFP%2FEdvdXI4y3Z8JMR6PewLuRAEeIQ%2F8UxoQPt7hiW6W0%2F384UDmBMsfMU3miu%2BybCqDeVH0uGR127xmNWpCO8k3hKkXXYEOXql4wpX12JzdgZAso13hoXt7KWP5GDoTexMlaMAA%2F3QXEn0WvhGZlBR7Aoxr&X-Amz-Signature=938c859cf266c0329f70dd6fcccb0a12885c4b8ee6c59dced9bf6c5b914c8cf0&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8f1b1d60-cf1b-42b3-9faa-f634c89c3f84/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YGYI5UQ3%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T132020Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCKIAnx0KRinCRf0Kx%2FSKDnABYFj43hFvcghJWNj7e%2FsAIhANdULHRKeVqhlb1W4JxmkuyvA4l4gPPiL4KoxZedmlYAKv8DCBYQABoMNjM3NDIzMTgzODA1IgwcTI4z8A%2Fpt1DWcrUq3APQTAzmOZbsW2GcMlJ%2FI9bnRzVZ%2FR%2Fb8z90S9WfYIAAjI6LazBMGHTa%2FxXVNb2IkfqHHNXAR2Cjh9FPzbXAbuTyuPDB477QmiJWAXomAQpoW0PKvpF1ltpf%2BNR%2FXNiu5qh51I5gZc3UNJC09b%2FyMjV%2Bhd6Xlk74YNQogfjpX3gCzwu9%2BRMHYttYZZU%2Bb4%2BaAMzFzzExT9pqAIvw5QEn7XVFlBT5knc6dVZY4eI2RcKZLOtmtC6M4%2BFWOG9s8WiXUccjTdFFp6mkUfyJp4CruwRxXQTlYCnZEdXKxJkMUlGTT5775mdJw%2BQSlNRQVHWcmgrG6eUDDQwjW9VPwbSQHTeuIEmCPpgSq0YOYPtEoQWWL11fq1xSwLv61hPJ%2FFvehYS9e15qaBGSW1%2B7egIplTLlVuL%2F690Okpy8RXC4DLpFtVYYsELyY%2BNCAVrIFkliseIv3BxbpJnLUaGYFoBXaQIU6NXelTzmEKJQe2xy0dkNJUDkaK1kvqFe0aOp5%2F1sPLK5u%2BMev%2Fwm2IPRwBkrgZ6%2FE0DVF2IMUp9Qtz7GlDSAfghouiVHBQp7BENFUT44Jz4rNcfnRuIjs0n6kHlqeS9utDeYxXpj%2Byw4gIrx3mfBffSU93svrjymEJ07lTCM8YK9BjqkAclmbrDp3AOBsoZ8FvwrMwcZTlNBBCMf%2FxjzqBX86%2FpqQD1%2FEHhWiJtKBeKmgAtoTFP%2FEdvdXI4y3Z8JMR6PewLuRAEeIQ%2F8UxoQPt7hiW6W0%2F384UDmBMsfMU3miu%2BybCqDeVH0uGR127xmNWpCO8k3hKkXXYEOXql4wpX12JzdgZAso13hoXt7KWP5GDoTexMlaMAA%2F3QXEn0WvhGZlBR7Aoxr&X-Amz-Signature=8a6b9c1b9904a38e3376147db91d9608a7cab0401757f94f92692f650b287a04&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/13ad0497-05fe-4eaa-984e-707b33e14761/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YGYI5UQ3%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T132020Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCKIAnx0KRinCRf0Kx%2FSKDnABYFj43hFvcghJWNj7e%2FsAIhANdULHRKeVqhlb1W4JxmkuyvA4l4gPPiL4KoxZedmlYAKv8DCBYQABoMNjM3NDIzMTgzODA1IgwcTI4z8A%2Fpt1DWcrUq3APQTAzmOZbsW2GcMlJ%2FI9bnRzVZ%2FR%2Fb8z90S9WfYIAAjI6LazBMGHTa%2FxXVNb2IkfqHHNXAR2Cjh9FPzbXAbuTyuPDB477QmiJWAXomAQpoW0PKvpF1ltpf%2BNR%2FXNiu5qh51I5gZc3UNJC09b%2FyMjV%2Bhd6Xlk74YNQogfjpX3gCzwu9%2BRMHYttYZZU%2Bb4%2BaAMzFzzExT9pqAIvw5QEn7XVFlBT5knc6dVZY4eI2RcKZLOtmtC6M4%2BFWOG9s8WiXUccjTdFFp6mkUfyJp4CruwRxXQTlYCnZEdXKxJkMUlGTT5775mdJw%2BQSlNRQVHWcmgrG6eUDDQwjW9VPwbSQHTeuIEmCPpgSq0YOYPtEoQWWL11fq1xSwLv61hPJ%2FFvehYS9e15qaBGSW1%2B7egIplTLlVuL%2F690Okpy8RXC4DLpFtVYYsELyY%2BNCAVrIFkliseIv3BxbpJnLUaGYFoBXaQIU6NXelTzmEKJQe2xy0dkNJUDkaK1kvqFe0aOp5%2F1sPLK5u%2BMev%2Fwm2IPRwBkrgZ6%2FE0DVF2IMUp9Qtz7GlDSAfghouiVHBQp7BENFUT44Jz4rNcfnRuIjs0n6kHlqeS9utDeYxXpj%2Byw4gIrx3mfBffSU93svrjymEJ07lTCM8YK9BjqkAclmbrDp3AOBsoZ8FvwrMwcZTlNBBCMf%2FxjzqBX86%2FpqQD1%2FEHhWiJtKBeKmgAtoTFP%2FEdvdXI4y3Z8JMR6PewLuRAEeIQ%2F8UxoQPt7hiW6W0%2F384UDmBMsfMU3miu%2BybCqDeVH0uGR127xmNWpCO8k3hKkXXYEOXql4wpX12JzdgZAso13hoXt7KWP5GDoTexMlaMAA%2F3QXEn0WvhGZlBR7Aoxr&X-Amz-Signature=69d3ff39c6337c8fc92d1e3e10cc4e103869a9ac315d5f1d8987b7b6a0c3d391&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 2. Box and Whisker Plot
A box plot shows the distribution of quantitative data in a way that facilitates comparisons between variables or across levels of a categorical variable. The box shows the quartiles of the dataset while the whiskers extend to show the rest of the distribution, except for points that are determined to be "outliers".
**Syntax:**
```python
sns.boxplot(x='header_1', y='header_2', data=df)
```
**Example Output:**


![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d207ae92-0a7c-4e2f-aa65-0ee5a2c33bf7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666ARLO2IB%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T132022Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDLSdnGReyqp8dC%2BcG8j746V0kPvuWimw1JM%2By9AL16owIgW6Dm3EQ5JHvckQO%2BHR%2F84CmpnIoBRSieUgBPQVoShpgq%2FwMIFhAAGgw2Mzc0MjMxODM4MDUiDE9Ln1KeKREL%2FBmaNyrcAwh49bUayo3TdT9E2B224Pt4cIUY3gw9kebIgU02bEMibcpj2OQ8qMylhlGUPQfSsUBITprPIomecht%2B2Uw89R8iEza%2Btw6qNnLez4kxZsOHrLVVvxvJHuM16M3NMTsGjewDaonQXEPdhCwqr9hIce7e7gcT8Xv9ofxU9Vngob8A%2Ff4l08JwE80Imhpm90lJ5RW5SNEI7IkWC8y5lrgZ%2FJZnuy0Gpw6ubQzt5C7FxXsRrj7SnUtI%2BGU77H5zkKa9qlUY9cQA%2B04%2FoM9S2j0LE60ue35uk3sJyW59INsyCZobaXPa0ZEuwIVYpENFhtH5%2B4BtviEssbE%2B0pVW3ZJa%2BD%2FgpQSdTHqYXeFI5zHpAXkY2ZI9qxfQl0oU7CYi%2BUVfXDiqK%2F8zM9SIkKQGL1bd8slR7odcq61CJnUw7OVnd66YrsDHppXm5BCGUkm%2B5i9whJM%2BmTnnwsdJSHFfBtQ0Rnag8GgZgDTO1RMvTjxnpV126sc9bIJtvEnnYo%2F%2BR7zzDZG5eCn%2FWqc0wfIfexYmXMebI4nqhUKXLzSG6aHYXqOiXzFzbWaI4KOxmuomV00mLGWqTEALVUKLHCam1xayReZXAbmrQpSZcxpdpdvYeCFffdaaSLVdz20vuhtCMLfxgr0GOqUBgwQJ8YTt8ATIE%2FVJrfVX209KNgktz7Cye3lr3fg0QQ7K%2B%2B15XiQB479ap6UvVgNdljwoyXgIkV3lxUjnPE3X1M%2Bou6c7NcQuoaxdPiiwcn%2Fl6ZCl9bHQ0zJkSVJYtCDaER342IrHDR%2Fc4%2FKvuC5H50uGrHRbg6Vu2E0%2Bvyxbe2NXuVPuepJeM0t31uxZTNKFcX%2BA7Q69dsbEwVx6egidq7x8ZuaB&X-Amz-Signature=9241a3a53dca25748a85cb842a6d762e43cd90ee720b8d8b9785ae9430f28284&X-Amz-SignedHeaders=host&x-id=GetObject)

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0e516edc-7551-4792-ab18-0494db3c4c0c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TMYC2WXC%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T132024Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCRKEdQDRoNxYoHcncVzJooANLVGJgrMsM7ihIAVw4hOAIgT5kG0ZBcvLJySDR3Ayp2js%2FoYN1z1kOCPUUvbzfjVnoq%2FwMIFhAAGgw2Mzc0MjMxODM4MDUiDFmIp23Hh8Far0rUsyrcAxp%2F0%2F0IkXe%2FarZVvpfEKrCpvzwBMAjyPQ2bd8UezNvvuK0YrwcsGTj7hh9VUxEFfCGtU47Xq9CKFsVMIw%2FDIcpjV8gE36B8%2Fvg1B2wtl5KJvol590sdm3QxXad%2BYLxS1YC1iwnkBXkAPjZd1Plaeng1ZEzINgqYgnOG3yKldH5mVykwDXecMqbzLTVR%2Fmj9UER%2BF%2F76UKLAGQbMXpOEQL9pKV22lhgfe4GNVYfunyfr9PNj%2FS7bwphSV6wZnS2VyZyHPmGf%2F%2FezVIwn%2FgdUXA4wj%2FA%2FgSsqQIVK9BkbGQbfHho2bIUERotU9qprxytL5Bto17vdFZEogtLp514yitNGpFkJFEn73ev%2BpqfvZTQ87qsVJ9i2JuP4fIDvYwTROIN1YWvXe5tMfLqxK5an%2BiGW5YuM8q5LJj33ZOqCYqPj%2FiSgGbIUoF1hp88jPPd%2BEaAJxih2PiJU8yplXMOYbPKRuKim56CV90fpgFMJvJ8XOCaHMrQWahp0Qt1sBCE%2BEFspfS5KOkk6J8CBCorUSJ61BgK6jzYaISy4iWxh8Uws53FLR4W0nmd3LAUJgxUazETo2u6dbu7IIs%2FC81imOUnThV6YQlG7jysg7BxKvqH5hjYz10WTKfeiRKf5MKvxgr0GOqUBKHxFUC9Gnu6NBi7EGQSeWUszw2WlvHYQyc4gyG9xQ07UiFzshNaeB3WVHiEe7mdX0pp6%2F9t5U9Hy4EN0NH3mWSg9OjL%2BvfqC7a4ZKk%2FkPJG0Ys%2FFnhHatk1OQiUPs7XsmTgcpXeUiJ%2Bz2oic%2Fr7YwH%2BJuCXp3%2FUV0Vq%2FYhYtkpVqq33NH13t3EanE6uZai5desVMe5b1Xy%2F7JRsOaoHAZmNRYYoK&X-Amz-Signature=1ca9ff5d618c2f0216720cfb3c175c80829fefc745530d1a8181db9ed7b54c1b&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23a79b9d-2356-49a9-8fd9-65c6b0ab2cc5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YGYI5UQ3%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T132020Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCKIAnx0KRinCRf0Kx%2FSKDnABYFj43hFvcghJWNj7e%2FsAIhANdULHRKeVqhlb1W4JxmkuyvA4l4gPPiL4KoxZedmlYAKv8DCBYQABoMNjM3NDIzMTgzODA1IgwcTI4z8A%2Fpt1DWcrUq3APQTAzmOZbsW2GcMlJ%2FI9bnRzVZ%2FR%2Fb8z90S9WfYIAAjI6LazBMGHTa%2FxXVNb2IkfqHHNXAR2Cjh9FPzbXAbuTyuPDB477QmiJWAXomAQpoW0PKvpF1ltpf%2BNR%2FXNiu5qh51I5gZc3UNJC09b%2FyMjV%2Bhd6Xlk74YNQogfjpX3gCzwu9%2BRMHYttYZZU%2Bb4%2BaAMzFzzExT9pqAIvw5QEn7XVFlBT5knc6dVZY4eI2RcKZLOtmtC6M4%2BFWOG9s8WiXUccjTdFFp6mkUfyJp4CruwRxXQTlYCnZEdXKxJkMUlGTT5775mdJw%2BQSlNRQVHWcmgrG6eUDDQwjW9VPwbSQHTeuIEmCPpgSq0YOYPtEoQWWL11fq1xSwLv61hPJ%2FFvehYS9e15qaBGSW1%2B7egIplTLlVuL%2F690Okpy8RXC4DLpFtVYYsELyY%2BNCAVrIFkliseIv3BxbpJnLUaGYFoBXaQIU6NXelTzmEKJQe2xy0dkNJUDkaK1kvqFe0aOp5%2F1sPLK5u%2BMev%2Fwm2IPRwBkrgZ6%2FE0DVF2IMUp9Qtz7GlDSAfghouiVHBQp7BENFUT44Jz4rNcfnRuIjs0n6kHlqeS9utDeYxXpj%2Byw4gIrx3mfBffSU93svrjymEJ07lTCM8YK9BjqkAclmbrDp3AOBsoZ8FvwrMwcZTlNBBCMf%2FxjzqBX86%2FpqQD1%2FEHhWiJtKBeKmgAtoTFP%2FEdvdXI4y3Z8JMR6PewLuRAEeIQ%2F8UxoQPt7hiW6W0%2F384UDmBMsfMU3miu%2BybCqDeVH0uGR127xmNWpCO8k3hKkXXYEOXql4wpX12JzdgZAso13hoXt7KWP5GDoTexMlaMAA%2F3QXEn0WvhGZlBR7Aoxr&X-Amz-Signature=7c398e0390c078840c14fa631ddd1d7e2b5ba2b50d5f9ebfdc7f96aca7bf39f2&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 4. KDE Plot
A Kernel Density Estimate (KDE) plot is a graph that creates a probability distribution curve for the data based upon its likelihood of occurrence on a specific value. This is created for a single vector of information.
**Syntax:**
```python
sns.kdeplot(X) || sns.kdeplot(df['age'])
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0d571213-2a2f-4921-a50b-880847aa05ee/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YGYI5UQ3%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T132020Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCKIAnx0KRinCRf0Kx%2FSKDnABYFj43hFvcghJWNj7e%2FsAIhANdULHRKeVqhlb1W4JxmkuyvA4l4gPPiL4KoxZedmlYAKv8DCBYQABoMNjM3NDIzMTgzODA1IgwcTI4z8A%2Fpt1DWcrUq3APQTAzmOZbsW2GcMlJ%2FI9bnRzVZ%2FR%2Fb8z90S9WfYIAAjI6LazBMGHTa%2FxXVNb2IkfqHHNXAR2Cjh9FPzbXAbuTyuPDB477QmiJWAXomAQpoW0PKvpF1ltpf%2BNR%2FXNiu5qh51I5gZc3UNJC09b%2FyMjV%2Bhd6Xlk74YNQogfjpX3gCzwu9%2BRMHYttYZZU%2Bb4%2BaAMzFzzExT9pqAIvw5QEn7XVFlBT5knc6dVZY4eI2RcKZLOtmtC6M4%2BFWOG9s8WiXUccjTdFFp6mkUfyJp4CruwRxXQTlYCnZEdXKxJkMUlGTT5775mdJw%2BQSlNRQVHWcmgrG6eUDDQwjW9VPwbSQHTeuIEmCPpgSq0YOYPtEoQWWL11fq1xSwLv61hPJ%2FFvehYS9e15qaBGSW1%2B7egIplTLlVuL%2F690Okpy8RXC4DLpFtVYYsELyY%2BNCAVrIFkliseIv3BxbpJnLUaGYFoBXaQIU6NXelTzmEKJQe2xy0dkNJUDkaK1kvqFe0aOp5%2F1sPLK5u%2BMev%2Fwm2IPRwBkrgZ6%2FE0DVF2IMUp9Qtz7GlDSAfghouiVHBQp7BENFUT44Jz4rNcfnRuIjs0n6kHlqeS9utDeYxXpj%2Byw4gIrx3mfBffSU93svrjymEJ07lTCM8YK9BjqkAclmbrDp3AOBsoZ8FvwrMwcZTlNBBCMf%2FxjzqBX86%2FpqQD1%2FEHhWiJtKBeKmgAtoTFP%2FEdvdXI4y3Z8JMR6PewLuRAEeIQ%2F8UxoQPt7hiW6W0%2F384UDmBMsfMU3miu%2BybCqDeVH0uGR127xmNWpCO8k3hKkXXYEOXql4wpX12JzdgZAso13hoXt7KWP5GDoTexMlaMAA%2F3QXEn0WvhGZlBR7Aoxr&X-Amz-Signature=a3a3ec8bd05ee54cdb5042bf55488be379d54b1d7154ff2091b9df63e90fb250&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/53752550-ef82-4ca9-a01a-09921f0282d0/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YGYI5UQ3%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T132020Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCKIAnx0KRinCRf0Kx%2FSKDnABYFj43hFvcghJWNj7e%2FsAIhANdULHRKeVqhlb1W4JxmkuyvA4l4gPPiL4KoxZedmlYAKv8DCBYQABoMNjM3NDIzMTgzODA1IgwcTI4z8A%2Fpt1DWcrUq3APQTAzmOZbsW2GcMlJ%2FI9bnRzVZ%2FR%2Fb8z90S9WfYIAAjI6LazBMGHTa%2FxXVNb2IkfqHHNXAR2Cjh9FPzbXAbuTyuPDB477QmiJWAXomAQpoW0PKvpF1ltpf%2BNR%2FXNiu5qh51I5gZc3UNJC09b%2FyMjV%2Bhd6Xlk74YNQogfjpX3gCzwu9%2BRMHYttYZZU%2Bb4%2BaAMzFzzExT9pqAIvw5QEn7XVFlBT5knc6dVZY4eI2RcKZLOtmtC6M4%2BFWOG9s8WiXUccjTdFFp6mkUfyJp4CruwRxXQTlYCnZEdXKxJkMUlGTT5775mdJw%2BQSlNRQVHWcmgrG6eUDDQwjW9VPwbSQHTeuIEmCPpgSq0YOYPtEoQWWL11fq1xSwLv61hPJ%2FFvehYS9e15qaBGSW1%2B7egIplTLlVuL%2F690Okpy8RXC4DLpFtVYYsELyY%2BNCAVrIFkliseIv3BxbpJnLUaGYFoBXaQIU6NXelTzmEKJQe2xy0dkNJUDkaK1kvqFe0aOp5%2F1sPLK5u%2BMev%2Fwm2IPRwBkrgZ6%2FE0DVF2IMUp9Qtz7GlDSAfghouiVHBQp7BENFUT44Jz4rNcfnRuIjs0n6kHlqeS9utDeYxXpj%2Byw4gIrx3mfBffSU93svrjymEJ07lTCM8YK9BjqkAclmbrDp3AOBsoZ8FvwrMwcZTlNBBCMf%2FxjzqBX86%2FpqQD1%2FEHhWiJtKBeKmgAtoTFP%2FEdvdXI4y3Z8JMR6PewLuRAEeIQ%2F8UxoQPt7hiW6W0%2F384UDmBMsfMU3miu%2BybCqDeVH0uGR127xmNWpCO8k3hKkXXYEOXql4wpX12JzdgZAso13hoXt7KWP5GDoTexMlaMAA%2F3QXEn0WvhGZlBR7Aoxr&X-Amz-Signature=84a63947366533e81f402caf6ac13380e100ee9d923c88740d8d51b8a7098f15&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
## 4. Correlation Between Variables
Correlation is a statistical measure of the extent to which different variables are interdependent. It indicates how changes in one variable are associated with changes in another variable over time.
### Positive Correlation
Positive correlation indicates that as one variable increases, the other variable also tends to increase.
**Example: Engine Size and Price**
- **Positive Correlation:** Engine size increases, price also increases.
- **Visualization:** Scatter plot with a steep positive slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c7ea9b0-3ef3-4357-a9c3-554fc71b6b15/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QEPZAYTQ%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T132022Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD0TkDT5CZBcoZTiaB3aGQQOMr1cHEq7u1ScQguq86gYAIgBp%2Bcr%2BvWWTjPvo%2BNWyigMdFP8ZhYtEpQf7JJzXnsxVgq%2FwMIFhAAGgw2Mzc0MjMxODM4MDUiDE5HeaQ7j2F3IVmtXCrcA7UFq16J9rWIR9aL5nwWAjSvU9w0nrrGbet3nFuh8oyCLKZOrVWtiQFsjL3pnHx9%2F9cW2RwHIcnEg6h3fSfPQPyQpn3uEgDEZLm%2FygFwAvMHfTjGglJIotPDSjGOQspQgODbVcN5X%2BtlxcE8R81M%2BUUcExC180mM54G8UcM4kYn%2FJJRpWZWiInSdzE9S3WFvK378orLdTy8IYsgLBCJnP7FR5poR7tHuMI5BsadO%2FrVvtHFdMY5y5wXYpgeqpJu%2Fm1uCjCfco2DrAH2RZoen4bo4JxzQTbhxNqBZcpJLRmryg2xXmmmQnFxm%2B6VYOW01VS2BG3iOJiUEiJI2cUioip%2FRKMdE2nAo4dDi2fEjzUIDr18ZxrbOOxsqRNPt0nOTEluJPzPco9sBUtOb8LrOHj%2B7h%2BSvrgPMsBiCopTaEHvGEOuiR4HxOTBw7R0PCnxpJSeEaQlBT4QzhJEJDdge2U2SL2nXnyuruaKKbGljbz4mT54ZAC8GohPcYmWk9fNjHy8FO0DWc%2FVSjRTdAAZVzB58Dce7KJsHE7%2F69CaYJJBtZ3X4lqDvqkaRs6OohquaNvUt4PHaRMaWGVab%2Bq6KdXINPd62WisfA3g82CEzLrDaf3N9KWt00YV3FIT3MIvxgr0GOqUBodflXwneNsymKHWRtZdxGxOR6NVPozRt8oKcb%2BJayjeHVZU07qGF1g64OOS5wfTIVqPWAhKkGB8VrX28%2Fe1vTgH78QqYhgVrS8ic%2BVV%2BlfGsZdjQFa%2FItAanVGcSyj2Ydr2jwwZrEyx8Wx5e7LLakMnrJ0pTXiF05cB4eqI98%2Fw%2FIafTkFGNsbmUqLQYeYeZ%2B0rfJ5XT2HyYPEZOrYIsCyNeuOxw&X-Amz-Signature=3124739485d249a1ff933e0e3ce1cfe628bef2b8da2a704bfb297ad2a4cfff4a&X-Amz-SignedHeaders=host&x-id=GetObject)
**Explanation:** When engine size increases, there is a corresponding increase in the price of the vehicle. This positive correlation suggests that larger engines tend to be associated with higher prices in the market.
___
### Negative Correlation
Negative correlation indicates that as one variable increases, the other variable tends to decrease.
**Example: Highway Miles per Gallon and Price**
- **Negative Correlation:** As highway miles per gallon increases, price decreases.
- **Visualization:** Scatter plot with a steep negative slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/10f1f798-9cc4-4df2-a9c1-5a339f554a0b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VL4KRBYQ%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T132022Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQC1zgsNT0uxvdOqLaQHzUqGp3uomtvr2eGioSq8D9bhTAIgYbaHM1ifykHa0CViYmq%2FKkencOjUOL966gsLJnXH%2Fssq%2FwMIFhAAGgw2Mzc0MjMxODM4MDUiDH2JqmiQ%2Frzek5xyxircA5vLujA1a6LTAs3G2b9%2FYD5zQiycPS%2FZHbkZgO%2BP0lUz%2FaFmT3dkihY2KJxyFwH1eZY5NcZRR9j1JuTIWY%2BtgFP%2FwdX95KgN56d23k57WQtgQSnoT%2BxdUXBGJbh5jcIE8lHF30V7CsP8luNoInPTwPH3%2BhYUJ04jmt2RH%2Bb9gMeTneOLsaiyRPL4gsfDfZepA7wB2lZUntzGrlqKnvKmuW7VHFojZ5NN4MGRFYLNYmVr3c8hdrkIa0PPciX%2BZKZbQFTjUM%2FZtZpRLOU3mj9I%2BYsdCxkv%2FTx8fMhlerHr3Ns4BR9DEKcjHgKnUJuD6%2BTjFWQP%2BMEbeh%2FEmKJoxIWDFGbBjJ%2BGFAANXMW5EDpGPYq5IEIYLtetVvtBoEIph2yV1V3qgra4zcCQmFnFFH9ModH9p%2FAGiteIiG4MkKfO3ZDGCcGtGAWQjQHa4e5uyHPlb5ABM88dMAHJ32NIzThkOhAestz8aovDi7%2F8N4kdgYghbZo7b2jLCxyqFA1QCrYTL7eVT2ywzRpxqTKY2c%2Fcj%2B3qGYXvz6E1Ikyxx%2B8zgc9srDRKJLZ93VM6w63EY%2F0CPeQnhbVJvl2rMf6LJeYXOviwzrJ6pAXGxASzbv%2FDSEgaDH1s6yDWfa4l7p%2BUMIDxgr0GOqUBOh5X2hrWl2eWb0LJo6lwgCni3fRyNVHcdDQ2xyn2o1j3jaVYYE9tOiDlOc5HGkIKFvSd6df25N0wJallinslxM47iXe5cJFkpIEVAF7LkX1AhMBXCxYWc1j85OAUB6XdOe9NL4Hi229D6uPWK9obSDrR8OxK57dN7OBk4HbuQGKHC0xQs0T4ecZ3DK2HJvOeNS%2B6TUTOoNZLCUaCjt9BHFhax8l%2F&X-Amz-Signature=6df2e179b08021e18133f8ebb477c484c2818605f955518a152d11514de8cabd&X-Amz-SignedHeaders=host&x-id=GetObject)
**Explanation:** When highway miles per gallon increases, the price of the vehicle tends to decrease. This negative correlation suggests that cars with higher fuel efficiency (more miles per gallon) are generally priced lower in the market.
___
### Weak Correlation
Weak correlation indicates a lack of strong relationship between the variables.
**Example: RPM and Price**
- **Weak Correlation:** Low and high RPM values show varied prices, indicating no strong predictive relationship.
- **Visualization:** Scatter plot with no clear trend or slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9f914514-8914-4bf4-ac84-d9e3077f6eb1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RLCLRTIG%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T132022Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDNrX3BW1j7AW8sWMvsdMspdJBsjavjn7f6rH06w%2BBe8AIhAKcTVJCZJihwX1zS8YPIiByMebeybVc6BqhNZY9%2B9jH0Kv8DCBYQABoMNjM3NDIzMTgzODA1Igy4pnmEuqvqGrH2hrsq3APe1m7Ekpil6TWClV727oUf4Gb7jEbrjXKskRuIO%2Fxkj5YzS1MLyJJgH6VL0jNgkevAD%2BVkP0m5dmftbP%2FHHjcyp3h0mOO6eWOdDTH1neZSxxGcfi4wQ9q%2BZ%2FF11lYvc4hAmt6eEWaNBx70RpMoTT8W81%2FD9LLmqE4h9aXkGgpz%2BEjLv8Zw0EmZailLzzWkrV6IxBrWy%2BXiS58WMQktyIRbjif4nEuXoMPLiV%2BFUhe304ZCyOzso%2BHxMVMhWGscPZuci5m229efxP%2BqJJD8dP9c0rds6KfM5POT%2Bbg7iP6sylgu0xYdGHH7ww1hK57ZvhMDqWJkcQEph19qFoAt9%2FBlGxVHxPE%2BGVSQO9LOcd7rzueSFNAwWf1Sam2KvZZ3ucTfzwVboo%2BBl3AxueuAivLsxI8SUTNB0WBqIMwEJLrDlM9HFv9ScJDEviRwXuCyCfkSvE5qJYyNfPnZwHfPdfwvym%2FmvZ8DUZj5%2Bv7WqxECSGC7tccpHH2ZypZJLefaP2sqQafB0X0Zm5MiFhUqUVFo8JWW73OIPSGcZu0Cme2LzpcZEzq5xpR%2BPB8%2FiM5B2bTnH2GiVfxJAUPVR66OepSdQ5AZJRYkJugkan%2FNZZxWaHzBs1UnyClhKlAAzjCU8oK9BjqkAcckudCnqY7S0TkT2%2Fju0QYT2pa6jf8bKVamDHvTmkHQB%2FlHQ9qkLCB%2BmMsYxWU%2FpxeI8TeaCeHBIUx0vem28CrxQUM9RhMyqQ5bOuZqd7GEtFnAcg0pBrH0sA%2BYpDztiMNp%2FCAD1LOkaUqrn3Px55EY4fFf7AS49f9UAG8NWKSqU%2F4FTlHr2IhS0F5WdinjiN9p%2B%2F9DnckqHNqq2A3n6HL%2FCQaD&X-Amz-Signature=175f67ea93c78655482f8a90b678644b6e6d64e2bd672d2ee005545936586360&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f18086e5-5b04-4fbf-8309-8944ab20d213/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TPIBPYOB%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T132022Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGNI9xCZkk5JeLgSCJqPFCIB7GEEvD5Rf9CIe03hLijbAiBw6br%2BERENb%2BXk5OR3rff6wo6rHhHCu5zy9JFAK9qIpSr%2FAwgWEAAaDDYzNzQyMzE4MzgwNSIMZysFoX%2FPOZvOFyutKtwDpRPNWsKwY%2FGjPcXnIZwmWLqrzlwL7%2F7ZPBcpu%2Fl%2FQEFjxN%2FjlRRD%2FxDFn3hlIEVT49pm0wzfVYvbtJCRdUIMqJ7ha%2Fijyrry1%2BKiII4Xt1BKQdoeG2bei7KslB6RfX%2Bu6bmQBN1x17ol1nOk7PmjcaxbaDkw3f%2FwYKCJgf0G%2FduYtFvB99FhDTY5qOOG0je%2B4K4YC0FvsogstHap7YZnLK1kfUnzR7CjwWg8QaLFC7Mq1jITA%2FyM7GDNMJ556i5rsJIgWDNwL2jYUKkGF3FYuRZc0ykxH5qKS8yXRMSKajUod1aC1vTn23sTg69XG9U%2FWJWWBuwVxJmrVAgkmW%2FeFUResC6dSSGftWalCzrZstuRvat5esaoinloYqnVOM4ArI3zqrJw%2BBP8LaPpuEPRPq9v5Vg4kDdH%2F1Ck5vjUdJo58%2FQscqXdyrF6SKCSYhs6cthjLcw6f%2FmGhJJYWxXr1E%2BQVG4WVYT%2ByCXJ4oXIU%2FLl9to2ySiQr3mpUhs8VhZJjdArsWoggFWyrxZNeIpg%2BZUR0aGRcOA2dw8C8O8p4UEy0OdPS0PNoZHmI0soFEgvb3t8W1iNpufkGSs6hK3Odx7gij%2F%2B0bUtCTvp8CSUw64SJsgLaFmdDPy1uHww9vCCvQY6pgH3IxhLg16ExoGYIo8KEyB5tYhlKn%2B4GS6a7fw3eANml%2BaiPmrBpRRK6QBEdd0FDuoUtiZGfzLXGzShCSKTmlBihFY%2FQ8QxGV7Sgx3FIbqYgaoBUvXl1LYH4HDggkWJN8fHiFuKxFahLGFXgiE%2F00XeOZeTEp8aZgGMczNbdJMNoQAEUr8pl%2B%2BtVA5DuR9NzO%2BcUbRDsOb%2BkzPbaUBxrdDeWdhJ9WEt&X-Amz-Signature=bf646d1637de463aab4ace106f56f1b894c3130d6cfee175e23ce5b89238f27d&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Correlation Plot
Heatmap visualizes correlations among variables. Color scheme indicates Pearson correlation coefficients. Dark red diagonal line shows perfect correlation (value of 1) between variables and themselves.
This heatmap offers overview of variable relationships and their link with price.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cd3b341e-cc1a-45f7-8aec-cdc00436d270/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TPIBPYOB%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T132022Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGNI9xCZkk5JeLgSCJqPFCIB7GEEvD5Rf9CIe03hLijbAiBw6br%2BERENb%2BXk5OR3rff6wo6rHhHCu5zy9JFAK9qIpSr%2FAwgWEAAaDDYzNzQyMzE4MzgwNSIMZysFoX%2FPOZvOFyutKtwDpRPNWsKwY%2FGjPcXnIZwmWLqrzlwL7%2F7ZPBcpu%2Fl%2FQEFjxN%2FjlRRD%2FxDFn3hlIEVT49pm0wzfVYvbtJCRdUIMqJ7ha%2Fijyrry1%2BKiII4Xt1BKQdoeG2bei7KslB6RfX%2Bu6bmQBN1x17ol1nOk7PmjcaxbaDkw3f%2FwYKCJgf0G%2FduYtFvB99FhDTY5qOOG0je%2B4K4YC0FvsogstHap7YZnLK1kfUnzR7CjwWg8QaLFC7Mq1jITA%2FyM7GDNMJ556i5rsJIgWDNwL2jYUKkGF3FYuRZc0ykxH5qKS8yXRMSKajUod1aC1vTn23sTg69XG9U%2FWJWWBuwVxJmrVAgkmW%2FeFUResC6dSSGftWalCzrZstuRvat5esaoinloYqnVOM4ArI3zqrJw%2BBP8LaPpuEPRPq9v5Vg4kDdH%2F1Ck5vjUdJo58%2FQscqXdyrF6SKCSYhs6cthjLcw6f%2FmGhJJYWxXr1E%2BQVG4WVYT%2ByCXJ4oXIU%2FLl9to2ySiQr3mpUhs8VhZJjdArsWoggFWyrxZNeIpg%2BZUR0aGRcOA2dw8C8O8p4UEy0OdPS0PNoZHmI0soFEgvb3t8W1iNpufkGSs6hK3Odx7gij%2F%2B0bUtCTvp8CSUw64SJsgLaFmdDPy1uHww9vCCvQY6pgH3IxhLg16ExoGYIo8KEyB5tYhlKn%2B4GS6a7fw3eANml%2BaiPmrBpRRK6QBEdd0FDuoUtiZGfzLXGzShCSKTmlBihFY%2FQ8QxGV7Sgx3FIbqYgaoBUvXl1LYH4HDggkWJN8fHiFuKxFahLGFXgiE%2F00XeOZeTEp8aZgGMczNbdJMNoQAEUr8pl%2B%2BtVA5DuR9NzO%2BcUbRDsOb%2BkzPbaUBxrdDeWdhJ9WEt&X-Amz-Signature=cd3725a2d9c2e499f7b528f497d1f4a3914fb92e7ab8cdac37468e76589e6b06&X-Amz-SignedHeaders=host&x-id=GetObject)

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
