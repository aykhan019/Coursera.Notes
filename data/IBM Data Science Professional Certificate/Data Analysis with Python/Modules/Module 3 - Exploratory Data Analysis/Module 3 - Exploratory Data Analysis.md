

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7e6d594d-952e-44b6-97ea-31225882aea6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XR7BQ2KT%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T201644Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDEaCXVzLXdlc3QtMiJIMEYCIQD0VeMq%2BtzxEKA%2B0vtuG8goVbeboQ98%2BAGTCWhuWha6WQIhAI0xoefZpIGD6AOLZ7NB6kTDiWbBCEP8mIT4aNWbmN68Kv8DCEoQABoMNjM3NDIzMTgzODA1IgxlPJhXhWbuoYRnV9kq3ANgQhOChiGEt5wJThXqF7JKYdic1gLW6Z0ZXfdlzLppiTAE4qmzd17Pz05nFsI1JMFFtL%2Bqm347ASff5EjoemwS9vIIhjgUbSkWHpowzkqVIKQgmhPcrrGGoUcRzCDVaaAfklJBqUh%2BV35wjvTFDw8wCIUNFUWFY7W8FWVl%2FPQ%2BEdyjDpQnlZ%2BHHh3sc7AkRC%2FaHtImlmaNnutFA0sGaFLL9gJHZO1sCITEnT0GKvpH07ymP16vVuoIey0SP44DwveIWch7T6oXp8l4%2ByvWY6jU7ZjO0%2BV3z3%2BNZlVpffbpi35gtw6Uyh1dJtuR8%2Blwf%2BMCmgAMUEG6hgERvxSAHK7emi2UxKHYxyfr7456O0E9bFY5uVAEtujJ%2BwyzD3tSH%2FtgNKettTYHT7tqMGSlHApN%2FjIy1M1aezREOkcNcZhLppcydbG240j%2BYQcosIubUk547yAQccK3iXhUKxUyr98uLJFlDdj8bBWpzqnP5%2FfufXqERGp%2B4a9yGZcY4cnPaCBOR%2BS7IlxdGzjD2w77pExVoddZPunPYtwLDC6GEi011a6E7Zg3XzV9qpHBz%2BElcEfayF4tZwxxJotblwnKJu50xQfbak0PK2k%2BN%2BytT9uZdAU5LMHIIwrNxHuZujCjuo69BjqkAVoLVhOg2v2VudAz7XWmo08las9MkYBI7OJYCotB4XBsT7okHfX2mF9eg7Z58ETlvWKU7nPQ4XT82BdzhODFy34BxHXWLl404jcsCrkNesY8sQ4%2Bv5Nl8PI06%2Fj7Dw%2B0JONAJLLM0h8Ov%2F2p8iS5g9PxDF6TH34fVHyWedkl4%2BmHOfXgyE5WzFIpqsIIh9AU0ND%2FsDGNgbEds3V8Ln2gP%2BmSQ3tD&X-Amz-Signature=fd51fa99ef55af723ab3f1df072bd0c8f5470ec2fd6f5ba6e1d41cbcd95691b3&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cbfaed9e-b398-4902-8936-dea058b21def/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XR7BQ2KT%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T201644Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDEaCXVzLXdlc3QtMiJIMEYCIQD0VeMq%2BtzxEKA%2B0vtuG8goVbeboQ98%2BAGTCWhuWha6WQIhAI0xoefZpIGD6AOLZ7NB6kTDiWbBCEP8mIT4aNWbmN68Kv8DCEoQABoMNjM3NDIzMTgzODA1IgxlPJhXhWbuoYRnV9kq3ANgQhOChiGEt5wJThXqF7JKYdic1gLW6Z0ZXfdlzLppiTAE4qmzd17Pz05nFsI1JMFFtL%2Bqm347ASff5EjoemwS9vIIhjgUbSkWHpowzkqVIKQgmhPcrrGGoUcRzCDVaaAfklJBqUh%2BV35wjvTFDw8wCIUNFUWFY7W8FWVl%2FPQ%2BEdyjDpQnlZ%2BHHh3sc7AkRC%2FaHtImlmaNnutFA0sGaFLL9gJHZO1sCITEnT0GKvpH07ymP16vVuoIey0SP44DwveIWch7T6oXp8l4%2ByvWY6jU7ZjO0%2BV3z3%2BNZlVpffbpi35gtw6Uyh1dJtuR8%2Blwf%2BMCmgAMUEG6hgERvxSAHK7emi2UxKHYxyfr7456O0E9bFY5uVAEtujJ%2BwyzD3tSH%2FtgNKettTYHT7tqMGSlHApN%2FjIy1M1aezREOkcNcZhLppcydbG240j%2BYQcosIubUk547yAQccK3iXhUKxUyr98uLJFlDdj8bBWpzqnP5%2FfufXqERGp%2B4a9yGZcY4cnPaCBOR%2BS7IlxdGzjD2w77pExVoddZPunPYtwLDC6GEi011a6E7Zg3XzV9qpHBz%2BElcEfayF4tZwxxJotblwnKJu50xQfbak0PK2k%2BN%2BytT9uZdAU5LMHIIwrNxHuZujCjuo69BjqkAVoLVhOg2v2VudAz7XWmo08las9MkYBI7OJYCotB4XBsT7okHfX2mF9eg7Z58ETlvWKU7nPQ4XT82BdzhODFy34BxHXWLl404jcsCrkNesY8sQ4%2Bv5Nl8PI06%2Fj7Dw%2B0JONAJLLM0h8Ov%2F2p8iS5g9PxDF6TH34fVHyWedkl4%2BmHOfXgyE5WzFIpqsIIh9AU0ND%2FsDGNgbEds3V8Ln2gP%2BmSQ3tD&X-Amz-Signature=676a535936a16d5c846951c46ac3114adc443ee0d0bd3e55edf5be24b1936316&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/91181646-b1e0-4433-9711-6259a96a9247/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XR7BQ2KT%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T201645Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDEaCXVzLXdlc3QtMiJIMEYCIQD0VeMq%2BtzxEKA%2B0vtuG8goVbeboQ98%2BAGTCWhuWha6WQIhAI0xoefZpIGD6AOLZ7NB6kTDiWbBCEP8mIT4aNWbmN68Kv8DCEoQABoMNjM3NDIzMTgzODA1IgxlPJhXhWbuoYRnV9kq3ANgQhOChiGEt5wJThXqF7JKYdic1gLW6Z0ZXfdlzLppiTAE4qmzd17Pz05nFsI1JMFFtL%2Bqm347ASff5EjoemwS9vIIhjgUbSkWHpowzkqVIKQgmhPcrrGGoUcRzCDVaaAfklJBqUh%2BV35wjvTFDw8wCIUNFUWFY7W8FWVl%2FPQ%2BEdyjDpQnlZ%2BHHh3sc7AkRC%2FaHtImlmaNnutFA0sGaFLL9gJHZO1sCITEnT0GKvpH07ymP16vVuoIey0SP44DwveIWch7T6oXp8l4%2ByvWY6jU7ZjO0%2BV3z3%2BNZlVpffbpi35gtw6Uyh1dJtuR8%2Blwf%2BMCmgAMUEG6hgERvxSAHK7emi2UxKHYxyfr7456O0E9bFY5uVAEtujJ%2BwyzD3tSH%2FtgNKettTYHT7tqMGSlHApN%2FjIy1M1aezREOkcNcZhLppcydbG240j%2BYQcosIubUk547yAQccK3iXhUKxUyr98uLJFlDdj8bBWpzqnP5%2FfufXqERGp%2B4a9yGZcY4cnPaCBOR%2BS7IlxdGzjD2w77pExVoddZPunPYtwLDC6GEi011a6E7Zg3XzV9qpHBz%2BElcEfayF4tZwxxJotblwnKJu50xQfbak0PK2k%2BN%2BytT9uZdAU5LMHIIwrNxHuZujCjuo69BjqkAVoLVhOg2v2VudAz7XWmo08las9MkYBI7OJYCotB4XBsT7okHfX2mF9eg7Z58ETlvWKU7nPQ4XT82BdzhODFy34BxHXWLl404jcsCrkNesY8sQ4%2Bv5Nl8PI06%2Fj7Dw%2B0JONAJLLM0h8Ov%2F2p8iS5g9PxDF6TH34fVHyWedkl4%2BmHOfXgyE5WzFIpqsIIh9AU0ND%2FsDGNgbEds3V8Ln2gP%2BmSQ3tD&X-Amz-Signature=851200d7d3309c4943aed9e80f5f66890fd3e73bfc243fd1e361d7dd301c5c87&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/09aba1c0-0d55-41dd-852a-a04c5b8a3fac/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662GFE3QZR%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T201645Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDIaCXVzLXdlc3QtMiJHMEUCIQDkxsh5WGSCKMx82N%2FCt5sQ77aFfHxz%2Bv%2BCuw%2BAIxhc6AIgZsjdHT2K1N04isamVkg3%2F%2BQGhYss3lQpYHd5x2PdTJkq%2FwMIShAAGgw2Mzc0MjMxODM4MDUiDE549ugwa8DTzvTkJSrcA5Go4RkpDmSytdVWHSAm6xN%2FCtf3FzLt2kePhrDBXLcmNMef3LIDrgf%2BSQZ0A8yax3LrBLcqblhRnxqev45nlElboeYtHr6JGGGQV%2BRW4w27FgLxU3iLu2Un7p%2FGSk2eQFEcizNvEfnGvnFJ0wi4zAa9j7TqFJ2nYYuR9LS7rgjRKRpkSeDl%2B%2BNoEFN%2BpD4Az5fR03DgMxapu%2BR03Smrc7XwJAws7gjAjtX5e52a%2FeaP7%2F4HNHSaIWgiTyhVnpthFmxwVBh%2F9xAE%2BzuK96hagOu5mK%2BL6GB%2BmMHcrrlfU61snz2UVDJVrY%2BpTeLJyoEJedQjGg78xjTwf5aRuv7vpXF%2Fzuw0BbUrvIAi33K2lOtoHigNQ4xnqIAkdjhhAk6TfseRS0MYob9tsAGTFztip%2FeKm%2BXcxl1wfLHX6Une%2FIf%2FSCIfm%2F7qoo%2By6RzZlUjectpHC7ykfiUVzBWXgAv%2FpSxVKUa7YgmxI852P7jDpXQhJ3BACggbwDyeqmwLjfozNMQdPY86PE5vL9YgVePriiVJc9nIL3RilZ0zwgbC1U6WdrodtJvZYZ6LGA7%2FuJpYfdSHYpTtwgwHB3jtOLwQXG3m7EBLIkfd78ALBv2Er%2FvGVhfuH84BntZ3EBi9MMS6jr0GOqUByQmNoGB3cY%2BQ1rF7Mdt2WVpDzJj3JDdUsSOmE%2Fumez%2B8PHr35knfd7LyZSX7B%2FVG9ktNMYuqoP8fTP114rj4hbO9ad2q5S7swcJro3uyaUKYgQKUOBAxDgTJ0pZgJ6xvhkZY6sGqjYPE%2FoeNblQVcv3QXeVxb0XtaiNNaX4gWocZOdsQ72qWrN4bMYzJ9XrrxFykNzKMLv4eoll0oz3h0o6YW%2BFB&X-Amz-Signature=9e02199419a8e58bc467228460b09fd5af4b95ba3c23a7801fccbb85a089bf0d&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 2. Scatter Plot
Scatter plots present the relationship between two variables in a dataset. It represents data points on a two-dimensional plane. The independent variable or attribute is plotted on the X-axis, while the dependent variable is plotted on the Y-axis.
**Syntax:**
```python
plt.scatter(x, y)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23708af9-659f-4f23-b626-1a4292d7842c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662GFE3QZR%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T201645Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDIaCXVzLXdlc3QtMiJHMEUCIQDkxsh5WGSCKMx82N%2FCt5sQ77aFfHxz%2Bv%2BCuw%2BAIxhc6AIgZsjdHT2K1N04isamVkg3%2F%2BQGhYss3lQpYHd5x2PdTJkq%2FwMIShAAGgw2Mzc0MjMxODM4MDUiDE549ugwa8DTzvTkJSrcA5Go4RkpDmSytdVWHSAm6xN%2FCtf3FzLt2kePhrDBXLcmNMef3LIDrgf%2BSQZ0A8yax3LrBLcqblhRnxqev45nlElboeYtHr6JGGGQV%2BRW4w27FgLxU3iLu2Un7p%2FGSk2eQFEcizNvEfnGvnFJ0wi4zAa9j7TqFJ2nYYuR9LS7rgjRKRpkSeDl%2B%2BNoEFN%2BpD4Az5fR03DgMxapu%2BR03Smrc7XwJAws7gjAjtX5e52a%2FeaP7%2F4HNHSaIWgiTyhVnpthFmxwVBh%2F9xAE%2BzuK96hagOu5mK%2BL6GB%2BmMHcrrlfU61snz2UVDJVrY%2BpTeLJyoEJedQjGg78xjTwf5aRuv7vpXF%2Fzuw0BbUrvIAi33K2lOtoHigNQ4xnqIAkdjhhAk6TfseRS0MYob9tsAGTFztip%2FeKm%2BXcxl1wfLHX6Une%2FIf%2FSCIfm%2F7qoo%2By6RzZlUjectpHC7ykfiUVzBWXgAv%2FpSxVKUa7YgmxI852P7jDpXQhJ3BACggbwDyeqmwLjfozNMQdPY86PE5vL9YgVePriiVJc9nIL3RilZ0zwgbC1U6WdrodtJvZYZ6LGA7%2FuJpYfdSHYpTtwgwHB3jtOLwQXG3m7EBLIkfd78ALBv2Er%2FvGVhfuH84BntZ3EBi9MMS6jr0GOqUByQmNoGB3cY%2BQ1rF7Mdt2WVpDzJj3JDdUsSOmE%2Fumez%2B8PHr35knfd7LyZSX7B%2FVG9ktNMYuqoP8fTP114rj4hbO9ad2q5S7swcJro3uyaUKYgQKUOBAxDgTJ0pZgJ6xvhkZY6sGqjYPE%2FoeNblQVcv3QXeVxb0XtaiNNaX4gWocZOdsQ72qWrN4bMYzJ9XrrxFykNzKMLv4eoll0oz3h0o6YW%2BFB&X-Amz-Signature=9bce0874ebf1b4fcf0ea5d2fb89343f3d70e23d6287f77b694173de25d3f8e0c&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 3. Histogram
A histogram is an important visual representation of data in categorical form. To view the data in a "Binned" form, use the histogram plot with a number of bins required or with the data points that mark the bin edges. The x-axis represents the data bins, and the y-axis represents the number of elements in each bin.
**Syntax:**
```python
plt.hist(x, bins)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/24e4424a-df87-40a1-b63b-195cbdc2e0ab/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662GFE3QZR%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T201645Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDIaCXVzLXdlc3QtMiJHMEUCIQDkxsh5WGSCKMx82N%2FCt5sQ77aFfHxz%2Bv%2BCuw%2BAIxhc6AIgZsjdHT2K1N04isamVkg3%2F%2BQGhYss3lQpYHd5x2PdTJkq%2FwMIShAAGgw2Mzc0MjMxODM4MDUiDE549ugwa8DTzvTkJSrcA5Go4RkpDmSytdVWHSAm6xN%2FCtf3FzLt2kePhrDBXLcmNMef3LIDrgf%2BSQZ0A8yax3LrBLcqblhRnxqev45nlElboeYtHr6JGGGQV%2BRW4w27FgLxU3iLu2Un7p%2FGSk2eQFEcizNvEfnGvnFJ0wi4zAa9j7TqFJ2nYYuR9LS7rgjRKRpkSeDl%2B%2BNoEFN%2BpD4Az5fR03DgMxapu%2BR03Smrc7XwJAws7gjAjtX5e52a%2FeaP7%2F4HNHSaIWgiTyhVnpthFmxwVBh%2F9xAE%2BzuK96hagOu5mK%2BL6GB%2BmMHcrrlfU61snz2UVDJVrY%2BpTeLJyoEJedQjGg78xjTwf5aRuv7vpXF%2Fzuw0BbUrvIAi33K2lOtoHigNQ4xnqIAkdjhhAk6TfseRS0MYob9tsAGTFztip%2FeKm%2BXcxl1wfLHX6Une%2FIf%2FSCIfm%2F7qoo%2By6RzZlUjectpHC7ykfiUVzBWXgAv%2FpSxVKUa7YgmxI852P7jDpXQhJ3BACggbwDyeqmwLjfozNMQdPY86PE5vL9YgVePriiVJc9nIL3RilZ0zwgbC1U6WdrodtJvZYZ6LGA7%2FuJpYfdSHYpTtwgwHB3jtOLwQXG3m7EBLIkfd78ALBv2Er%2FvGVhfuH84BntZ3EBi9MMS6jr0GOqUByQmNoGB3cY%2BQ1rF7Mdt2WVpDzJj3JDdUsSOmE%2Fumez%2B8PHr35knfd7LyZSX7B%2FVG9ktNMYuqoP8fTP114rj4hbO9ad2q5S7swcJro3uyaUKYgQKUOBAxDgTJ0pZgJ6xvhkZY6sGqjYPE%2FoeNblQVcv3QXeVxb0XtaiNNaX4gWocZOdsQ72qWrN4bMYzJ9XrrxFykNzKMLv4eoll0oz3h0o6YW%2BFB&X-Amz-Signature=e734d68ce33175900b39d541de25ab2539bc0b4489f85c4cfefa0e035c0dc599&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ab5a6dfe-51f5-43ee-bcb3-33dae4a1c7ad/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662GFE3QZR%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T201645Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDIaCXVzLXdlc3QtMiJHMEUCIQDkxsh5WGSCKMx82N%2FCt5sQ77aFfHxz%2Bv%2BCuw%2BAIxhc6AIgZsjdHT2K1N04isamVkg3%2F%2BQGhYss3lQpYHd5x2PdTJkq%2FwMIShAAGgw2Mzc0MjMxODM4MDUiDE549ugwa8DTzvTkJSrcA5Go4RkpDmSytdVWHSAm6xN%2FCtf3FzLt2kePhrDBXLcmNMef3LIDrgf%2BSQZ0A8yax3LrBLcqblhRnxqev45nlElboeYtHr6JGGGQV%2BRW4w27FgLxU3iLu2Un7p%2FGSk2eQFEcizNvEfnGvnFJ0wi4zAa9j7TqFJ2nYYuR9LS7rgjRKRpkSeDl%2B%2BNoEFN%2BpD4Az5fR03DgMxapu%2BR03Smrc7XwJAws7gjAjtX5e52a%2FeaP7%2F4HNHSaIWgiTyhVnpthFmxwVBh%2F9xAE%2BzuK96hagOu5mK%2BL6GB%2BmMHcrrlfU61snz2UVDJVrY%2BpTeLJyoEJedQjGg78xjTwf5aRuv7vpXF%2Fzuw0BbUrvIAi33K2lOtoHigNQ4xnqIAkdjhhAk6TfseRS0MYob9tsAGTFztip%2FeKm%2BXcxl1wfLHX6Une%2FIf%2FSCIfm%2F7qoo%2By6RzZlUjectpHC7ykfiUVzBWXgAv%2FpSxVKUa7YgmxI852P7jDpXQhJ3BACggbwDyeqmwLjfozNMQdPY86PE5vL9YgVePriiVJc9nIL3RilZ0zwgbC1U6WdrodtJvZYZ6LGA7%2FuJpYfdSHYpTtwgwHB3jtOLwQXG3m7EBLIkfd78ALBv2Er%2FvGVhfuH84BntZ3EBi9MMS6jr0GOqUByQmNoGB3cY%2BQ1rF7Mdt2WVpDzJj3JDdUsSOmE%2Fumez%2B8PHr35knfd7LyZSX7B%2FVG9ktNMYuqoP8fTP114rj4hbO9ad2q5S7swcJro3uyaUKYgQKUOBAxDgTJ0pZgJ6xvhkZY6sGqjYPE%2FoeNblQVcv3QXeVxb0XtaiNNaX4gWocZOdsQ72qWrN4bMYzJ9XrrxFykNzKMLv4eoll0oz3h0o6YW%2BFB&X-Amz-Signature=fe7139ecee12eee867aafadf114011c080fd3cbdb7a54d14c5551b60bfcd7cbe&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8f1b1d60-cf1b-42b3-9faa-f634c89c3f84/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662GFE3QZR%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T201645Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDIaCXVzLXdlc3QtMiJHMEUCIQDkxsh5WGSCKMx82N%2FCt5sQ77aFfHxz%2Bv%2BCuw%2BAIxhc6AIgZsjdHT2K1N04isamVkg3%2F%2BQGhYss3lQpYHd5x2PdTJkq%2FwMIShAAGgw2Mzc0MjMxODM4MDUiDE549ugwa8DTzvTkJSrcA5Go4RkpDmSytdVWHSAm6xN%2FCtf3FzLt2kePhrDBXLcmNMef3LIDrgf%2BSQZ0A8yax3LrBLcqblhRnxqev45nlElboeYtHr6JGGGQV%2BRW4w27FgLxU3iLu2Un7p%2FGSk2eQFEcizNvEfnGvnFJ0wi4zAa9j7TqFJ2nYYuR9LS7rgjRKRpkSeDl%2B%2BNoEFN%2BpD4Az5fR03DgMxapu%2BR03Smrc7XwJAws7gjAjtX5e52a%2FeaP7%2F4HNHSaIWgiTyhVnpthFmxwVBh%2F9xAE%2BzuK96hagOu5mK%2BL6GB%2BmMHcrrlfU61snz2UVDJVrY%2BpTeLJyoEJedQjGg78xjTwf5aRuv7vpXF%2Fzuw0BbUrvIAi33K2lOtoHigNQ4xnqIAkdjhhAk6TfseRS0MYob9tsAGTFztip%2FeKm%2BXcxl1wfLHX6Une%2FIf%2FSCIfm%2F7qoo%2By6RzZlUjectpHC7ykfiUVzBWXgAv%2FpSxVKUa7YgmxI852P7jDpXQhJ3BACggbwDyeqmwLjfozNMQdPY86PE5vL9YgVePriiVJc9nIL3RilZ0zwgbC1U6WdrodtJvZYZ6LGA7%2FuJpYfdSHYpTtwgwHB3jtOLwQXG3m7EBLIkfd78ALBv2Er%2FvGVhfuH84BntZ3EBi9MMS6jr0GOqUByQmNoGB3cY%2BQ1rF7Mdt2WVpDzJj3JDdUsSOmE%2Fumez%2B8PHr35knfd7LyZSX7B%2FVG9ktNMYuqoP8fTP114rj4hbO9ad2q5S7swcJro3uyaUKYgQKUOBAxDgTJ0pZgJ6xvhkZY6sGqjYPE%2FoeNblQVcv3QXeVxb0XtaiNNaX4gWocZOdsQ72qWrN4bMYzJ9XrrxFykNzKMLv4eoll0oz3h0o6YW%2BFB&X-Amz-Signature=b3c2ed8f56747c6bc31031bdbfde24cde5c03b107d3dd130b6067ae67cbb5f16&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/13ad0497-05fe-4eaa-984e-707b33e14761/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662GFE3QZR%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T201645Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDIaCXVzLXdlc3QtMiJHMEUCIQDkxsh5WGSCKMx82N%2FCt5sQ77aFfHxz%2Bv%2BCuw%2BAIxhc6AIgZsjdHT2K1N04isamVkg3%2F%2BQGhYss3lQpYHd5x2PdTJkq%2FwMIShAAGgw2Mzc0MjMxODM4MDUiDE549ugwa8DTzvTkJSrcA5Go4RkpDmSytdVWHSAm6xN%2FCtf3FzLt2kePhrDBXLcmNMef3LIDrgf%2BSQZ0A8yax3LrBLcqblhRnxqev45nlElboeYtHr6JGGGQV%2BRW4w27FgLxU3iLu2Un7p%2FGSk2eQFEcizNvEfnGvnFJ0wi4zAa9j7TqFJ2nYYuR9LS7rgjRKRpkSeDl%2B%2BNoEFN%2BpD4Az5fR03DgMxapu%2BR03Smrc7XwJAws7gjAjtX5e52a%2FeaP7%2F4HNHSaIWgiTyhVnpthFmxwVBh%2F9xAE%2BzuK96hagOu5mK%2BL6GB%2BmMHcrrlfU61snz2UVDJVrY%2BpTeLJyoEJedQjGg78xjTwf5aRuv7vpXF%2Fzuw0BbUrvIAi33K2lOtoHigNQ4xnqIAkdjhhAk6TfseRS0MYob9tsAGTFztip%2FeKm%2BXcxl1wfLHX6Une%2FIf%2FSCIfm%2F7qoo%2By6RzZlUjectpHC7ykfiUVzBWXgAv%2FpSxVKUa7YgmxI852P7jDpXQhJ3BACggbwDyeqmwLjfozNMQdPY86PE5vL9YgVePriiVJc9nIL3RilZ0zwgbC1U6WdrodtJvZYZ6LGA7%2FuJpYfdSHYpTtwgwHB3jtOLwQXG3m7EBLIkfd78ALBv2Er%2FvGVhfuH84BntZ3EBi9MMS6jr0GOqUByQmNoGB3cY%2BQ1rF7Mdt2WVpDzJj3JDdUsSOmE%2Fumez%2B8PHr35knfd7LyZSX7B%2FVG9ktNMYuqoP8fTP114rj4hbO9ad2q5S7swcJro3uyaUKYgQKUOBAxDgTJ0pZgJ6xvhkZY6sGqjYPE%2FoeNblQVcv3QXeVxb0XtaiNNaX4gWocZOdsQ72qWrN4bMYzJ9XrrxFykNzKMLv4eoll0oz3h0o6YW%2BFB&X-Amz-Signature=7519ab839b227989dbac2bb4777f124e486be9ce0b623f7feaa643d086ac1c74&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 2. Box and Whisker Plot
A box plot shows the distribution of quantitative data in a way that facilitates comparisons between variables or across levels of a categorical variable. The box shows the quartiles of the dataset while the whiskers extend to show the rest of the distribution, except for points that are determined to be "outliers".
**Syntax:**
```python
sns.boxplot(x='header_1', y='header_2', data=df)
```
**Example Output:**


![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d207ae92-0a7c-4e2f-aa65-0ee5a2c33bf7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VCTEAYWP%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T201647Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDEaCXVzLXdlc3QtMiJHMEUCIQD2HlYJNIHYQuftusofs9n3h7bl8egeOlr%2FIKvvYxW5uAIgR6USWOK5hwqbXUi%2Br8Zj0G8ZvgYV2a7Bn5zl6aka8jAq%2FwMIShAAGgw2Mzc0MjMxODM4MDUiDCN1e9LRyOwsJxEggircA5%2FJibjLpbxe22eqRr8FlcJq4MH0CYl2W5w3hm7O6zTDpLY5UTK1rSwwCM7HQcKvLr8abQS2GWjU9z05TVvja0lVuwMgVUeayCoVUmBMxPp0nV8NSYssUeccnzLjVTHri7mK1MsjeF1z6YIf0V45q204T1d8IY1MHg8MalbZrz9BokdkJcli74bxpeQ%2BT6rfyRX57iB2H6EW%2FowoHbCubbWKxvodhMg012IoBpZV19gYNAcVXk%2BvLBfi2BZObrjFvCMPnCViPk9y1rJnipJBJqswIlRPaSKxNxKMz0%2BbHzzhdxIRsDB2L97w7Ug7H5Q6Za8Kv8aOQZo4ph4yLBMe7KHzu9CiI1yaqQFY7vbXDvpkBtnVMkre31jxCQbAR3yyXdvr%2FfhbWA6UNwMmeCPcKWej72067vc4cDEHf6qbRC%2B%2BeuPj%2FansD5Sd4Ne88y3mnXA2Wd1DnsTrGGV%2B6F6E3NpROKff5Bnq8cYB2m9ZxLePxcdRV12HXKvbDr3VpIr9fRwD15%2FEfqnhQSU6aUnJouHKuBScUCvjrez0JPtNKrS01W6rKWRo3If1VhG47zsK9C3gfXF3wsx5JR%2FKH2fL4MgI0oUt1%2BI6OK4TfYxKC3zAB%2Fpt3Fmq1%2FcmEWT6MLi6jr0GOqUBJ%2BkljsmBGvKjQKxoGjgSVH4JanIIg9r5m91ceTDmyGUjfUL1s%2FGGYUb73xCZkO%2FetzVa1daiN6cWvZf%2FmdnTenxmmAo3%2BdGHy%2FUYiBCPumVi36O%2FSreNA1gEbagJCSs2r5KEn4bjgYC8L%2B%2B0czhaN86gmPEYCU%2Fo3LasJy1L4s3ahjnJxik5Jk9XjvM9rECL89e%2BMVTzajOVpGhvoE32mm1%2BLxL1&X-Amz-Signature=2fe9d4ea91ecb03d90edca0506f8152f8b172d030df4748993cbf52e960dd3a0&X-Amz-SignedHeaders=host&x-id=GetObject)

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0e516edc-7551-4792-ab18-0494db3c4c0c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664VRBHPJC%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T201647Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDIaCXVzLXdlc3QtMiJIMEYCIQDC80BWe1S6FyaNT6zCHElhK7U2vDB92fBv18HCAT3EHQIhANmiTN9XRsNL%2FuKj8fL2ThKUa3FEojGx4nGZE7Uhb%2BJXKv8DCEoQABoMNjM3NDIzMTgzODA1Igyk39QIaw42bjVGhtAq3AOthKs04j%2F1LmfKUZzJXxqZSBqxVnbbhvDS96DF342kgsymuDZHtiMTHvDs0RE1umxE0CjoNKjZS%2FsrY1bHuZp%2BCIIxHUGfDxmBOASUXph7ELJPjQ81Gwu%2FWyVSTP3tHJaMrFDH2Qwu2s5nZMrCtmAt0GS%2FAG1OLeczu%2FmzYqxlTjmMMJPCT7JmFOkmp4%2Bn6oYLyyb8yYf1MGvkkNTz0cgKsrV9Jd9xJDzCqgJAcuax3vyEom9DOkwo1xeYhxiR4HiWgBhX9wZ934IX2x6rOgDbkEWzF7l6hhkw1ZOW1T6ZGNcWT%2FIFPmDJE4rnLOswh0GOiR9rUHsnEUfObpBk6%2FK6XuFX8SHl3i919QZJfsEglGaEf4dXh3bm2p1TegVED1kiCVn4vcUvfIJ0QdrwmezCIfHNfltokqtSmFzMAjDYYJ617e59pCMeJ%2Fbl7j9xmGUD5AHf84NZSAWptty09E2635U1dLlViroFN2kHU21wRWpWzyfgDxb7a9UIREONAQ73I4vtR%2Bn6vusXp7dAGnisw7ejHei7kzdNMG8Kp5OlQ%2FehQLjfacAlgxWQmkoaX4JqHfPuM41sbDyhLFZ6GFjHd3BiQskd93Q9u%2FAKGPiPriiA3A5fozO9vQgbYTDauo69BjqkAb2vLAKEds9GvU%2FusLQnJWVShQwdLY6v7zhwhXCHsIaUY%2FaDbWA88IumrQNq2jgu87NIHk8hE889m7bY2nNejjpGWLX9uAMWjO9zvoM3UQLehHwwqExcqMLLFfhfVVQSxpI0jdc3DUWdOYmwOibjXYJD7P5WsKktiD4%2BK8UnyyhuqnY6dhvjO5BOEzYgy%2FbjJ5ZMtrtRagaNF9dPjg6YedpATLKm&X-Amz-Signature=e5049e762263245a111e27e7e32aeb5cea51d1c92bf79f9bc2151e91e1705708&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23a79b9d-2356-49a9-8fd9-65c6b0ab2cc5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662GFE3QZR%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T201645Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDIaCXVzLXdlc3QtMiJHMEUCIQDkxsh5WGSCKMx82N%2FCt5sQ77aFfHxz%2Bv%2BCuw%2BAIxhc6AIgZsjdHT2K1N04isamVkg3%2F%2BQGhYss3lQpYHd5x2PdTJkq%2FwMIShAAGgw2Mzc0MjMxODM4MDUiDE549ugwa8DTzvTkJSrcA5Go4RkpDmSytdVWHSAm6xN%2FCtf3FzLt2kePhrDBXLcmNMef3LIDrgf%2BSQZ0A8yax3LrBLcqblhRnxqev45nlElboeYtHr6JGGGQV%2BRW4w27FgLxU3iLu2Un7p%2FGSk2eQFEcizNvEfnGvnFJ0wi4zAa9j7TqFJ2nYYuR9LS7rgjRKRpkSeDl%2B%2BNoEFN%2BpD4Az5fR03DgMxapu%2BR03Smrc7XwJAws7gjAjtX5e52a%2FeaP7%2F4HNHSaIWgiTyhVnpthFmxwVBh%2F9xAE%2BzuK96hagOu5mK%2BL6GB%2BmMHcrrlfU61snz2UVDJVrY%2BpTeLJyoEJedQjGg78xjTwf5aRuv7vpXF%2Fzuw0BbUrvIAi33K2lOtoHigNQ4xnqIAkdjhhAk6TfseRS0MYob9tsAGTFztip%2FeKm%2BXcxl1wfLHX6Une%2FIf%2FSCIfm%2F7qoo%2By6RzZlUjectpHC7ykfiUVzBWXgAv%2FpSxVKUa7YgmxI852P7jDpXQhJ3BACggbwDyeqmwLjfozNMQdPY86PE5vL9YgVePriiVJc9nIL3RilZ0zwgbC1U6WdrodtJvZYZ6LGA7%2FuJpYfdSHYpTtwgwHB3jtOLwQXG3m7EBLIkfd78ALBv2Er%2FvGVhfuH84BntZ3EBi9MMS6jr0GOqUByQmNoGB3cY%2BQ1rF7Mdt2WVpDzJj3JDdUsSOmE%2Fumez%2B8PHr35knfd7LyZSX7B%2FVG9ktNMYuqoP8fTP114rj4hbO9ad2q5S7swcJro3uyaUKYgQKUOBAxDgTJ0pZgJ6xvhkZY6sGqjYPE%2FoeNblQVcv3QXeVxb0XtaiNNaX4gWocZOdsQ72qWrN4bMYzJ9XrrxFykNzKMLv4eoll0oz3h0o6YW%2BFB&X-Amz-Signature=fb76398527236b4919cb9b82277689d51bfdcc2febaa3fb01e15555800b3b6fe&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 4. KDE Plot
A Kernel Density Estimate (KDE) plot is a graph that creates a probability distribution curve for the data based upon its likelihood of occurrence on a specific value. This is created for a single vector of information.
**Syntax:**
```python
sns.kdeplot(X) || sns.kdeplot(df['age'])
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0d571213-2a2f-4921-a50b-880847aa05ee/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662GFE3QZR%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T201645Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDIaCXVzLXdlc3QtMiJHMEUCIQDkxsh5WGSCKMx82N%2FCt5sQ77aFfHxz%2Bv%2BCuw%2BAIxhc6AIgZsjdHT2K1N04isamVkg3%2F%2BQGhYss3lQpYHd5x2PdTJkq%2FwMIShAAGgw2Mzc0MjMxODM4MDUiDE549ugwa8DTzvTkJSrcA5Go4RkpDmSytdVWHSAm6xN%2FCtf3FzLt2kePhrDBXLcmNMef3LIDrgf%2BSQZ0A8yax3LrBLcqblhRnxqev45nlElboeYtHr6JGGGQV%2BRW4w27FgLxU3iLu2Un7p%2FGSk2eQFEcizNvEfnGvnFJ0wi4zAa9j7TqFJ2nYYuR9LS7rgjRKRpkSeDl%2B%2BNoEFN%2BpD4Az5fR03DgMxapu%2BR03Smrc7XwJAws7gjAjtX5e52a%2FeaP7%2F4HNHSaIWgiTyhVnpthFmxwVBh%2F9xAE%2BzuK96hagOu5mK%2BL6GB%2BmMHcrrlfU61snz2UVDJVrY%2BpTeLJyoEJedQjGg78xjTwf5aRuv7vpXF%2Fzuw0BbUrvIAi33K2lOtoHigNQ4xnqIAkdjhhAk6TfseRS0MYob9tsAGTFztip%2FeKm%2BXcxl1wfLHX6Une%2FIf%2FSCIfm%2F7qoo%2By6RzZlUjectpHC7ykfiUVzBWXgAv%2FpSxVKUa7YgmxI852P7jDpXQhJ3BACggbwDyeqmwLjfozNMQdPY86PE5vL9YgVePriiVJc9nIL3RilZ0zwgbC1U6WdrodtJvZYZ6LGA7%2FuJpYfdSHYpTtwgwHB3jtOLwQXG3m7EBLIkfd78ALBv2Er%2FvGVhfuH84BntZ3EBi9MMS6jr0GOqUByQmNoGB3cY%2BQ1rF7Mdt2WVpDzJj3JDdUsSOmE%2Fumez%2B8PHr35knfd7LyZSX7B%2FVG9ktNMYuqoP8fTP114rj4hbO9ad2q5S7swcJro3uyaUKYgQKUOBAxDgTJ0pZgJ6xvhkZY6sGqjYPE%2FoeNblQVcv3QXeVxb0XtaiNNaX4gWocZOdsQ72qWrN4bMYzJ9XrrxFykNzKMLv4eoll0oz3h0o6YW%2BFB&X-Amz-Signature=79895be4990561e8aa907e2b35a7dc379c7efcff01d722d587ae1fb9c1c84089&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/53752550-ef82-4ca9-a01a-09921f0282d0/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662GFE3QZR%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T201645Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDIaCXVzLXdlc3QtMiJHMEUCIQDkxsh5WGSCKMx82N%2FCt5sQ77aFfHxz%2Bv%2BCuw%2BAIxhc6AIgZsjdHT2K1N04isamVkg3%2F%2BQGhYss3lQpYHd5x2PdTJkq%2FwMIShAAGgw2Mzc0MjMxODM4MDUiDE549ugwa8DTzvTkJSrcA5Go4RkpDmSytdVWHSAm6xN%2FCtf3FzLt2kePhrDBXLcmNMef3LIDrgf%2BSQZ0A8yax3LrBLcqblhRnxqev45nlElboeYtHr6JGGGQV%2BRW4w27FgLxU3iLu2Un7p%2FGSk2eQFEcizNvEfnGvnFJ0wi4zAa9j7TqFJ2nYYuR9LS7rgjRKRpkSeDl%2B%2BNoEFN%2BpD4Az5fR03DgMxapu%2BR03Smrc7XwJAws7gjAjtX5e52a%2FeaP7%2F4HNHSaIWgiTyhVnpthFmxwVBh%2F9xAE%2BzuK96hagOu5mK%2BL6GB%2BmMHcrrlfU61snz2UVDJVrY%2BpTeLJyoEJedQjGg78xjTwf5aRuv7vpXF%2Fzuw0BbUrvIAi33K2lOtoHigNQ4xnqIAkdjhhAk6TfseRS0MYob9tsAGTFztip%2FeKm%2BXcxl1wfLHX6Une%2FIf%2FSCIfm%2F7qoo%2By6RzZlUjectpHC7ykfiUVzBWXgAv%2FpSxVKUa7YgmxI852P7jDpXQhJ3BACggbwDyeqmwLjfozNMQdPY86PE5vL9YgVePriiVJc9nIL3RilZ0zwgbC1U6WdrodtJvZYZ6LGA7%2FuJpYfdSHYpTtwgwHB3jtOLwQXG3m7EBLIkfd78ALBv2Er%2FvGVhfuH84BntZ3EBi9MMS6jr0GOqUByQmNoGB3cY%2BQ1rF7Mdt2WVpDzJj3JDdUsSOmE%2Fumez%2B8PHr35knfd7LyZSX7B%2FVG9ktNMYuqoP8fTP114rj4hbO9ad2q5S7swcJro3uyaUKYgQKUOBAxDgTJ0pZgJ6xvhkZY6sGqjYPE%2FoeNblQVcv3QXeVxb0XtaiNNaX4gWocZOdsQ72qWrN4bMYzJ9XrrxFykNzKMLv4eoll0oz3h0o6YW%2BFB&X-Amz-Signature=c9762d1f462fae032eeed1987dd1cda6ea3db49183bbe3c000bdcd975b09db62&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
## 4. Correlation Between Variables
Correlation is a statistical measure of the extent to which different variables are interdependent. It indicates how changes in one variable are associated with changes in another variable over time.
### Positive Correlation
Positive correlation indicates that as one variable increases, the other variable also tends to increase.
**Example: Engine Size and Price**
- **Positive Correlation:** Engine size increases, price also increases.
- **Visualization:** Scatter plot with a steep positive slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c7ea9b0-3ef3-4357-a9c3-554fc71b6b15/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46643O33NVB%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T201646Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDIaCXVzLXdlc3QtMiJIMEYCIQDywYPy3dRRtUxKlFobskdUr1rOwCJv6AdXrLpJqulhwAIhAID6jiUHpWt7rh1B2%2B3SLKbPmUDaaZAnQUPIypQvIMQAKv8DCEoQABoMNjM3NDIzMTgzODA1IgwoPkZBIfY1UwoB5fIq3AP2ab6vNt5lu968h5CIFynn%2FdqMJ%2Bxv2DsHpvw6Z8DO5Fnq6P%2BVGpzLGcuQaKXxcH3RhhY775AlqNdzUJBR7dLzJ%2FDAfJbhLnzq6wwn0nHMuhpkFZP2GLi9JhvY0Mdi%2Fiz%2BPKrD0GEcI5qXoTHxj%2B3G%2FH4FwEIDFHzgLUELtA61kIdeVmXPBUAVjJP51%2Boz3EfeVUo%2BceZLq2rW%2F7cFKfeGPUgoue4o9cN7XJIMh5UsVUibDl%2BogFFe%2BRq0%2BX9E8v7Op1Dz22N6MhnUnFAvYgRqf8WhKbW%2FSoXxmpjivnWHJ%2BiuX6jth1aLZ%2FqG%2FhGekLRBN0XivkkqL6t%2FB8fWKhPN0hBmPpmATlLKTnQ%2BykGHjnczIQCse7VqCqyT9fcY6y7b%2F%2FkgmpY0QHJv8RsCe36tLUlNr3TcI7mWLDXoANq5Ssm5yj%2BGsYR1tnCsw5Mc%2F7Cc1zXJi6J09jl4fMyGGekjbWL6LWlEpX%2FcIRto3zLGsOAlRvHfqeXjgwtY75IpSz7qYSXLdnhieb47sS5Kjh%2BnL1f%2BP%2B6qGGASrmwucxub0Fml7Tz9Itr6QAXffnARpJtGjJqcJm7Y3ScSoO3prG1V%2Ft%2Bf3l4nAPKAk7Hd96L2tk1n2L4XfKHHAFniujDPuo69BjqkAQ0CXfPJITGn5MPbelUGJcRVqSGAtIn5dC8w1oeh95veFvSPTij3Bh4v5ITqRBCjmh7otlc5r7mfmiiTFuakxT5k4zxlcb4ZruRzXUSPP5an6Ys26uNU%2Fc1UhoVdYLxxWrXuzIsgZbR01GJjBImvs8o%2F1oI4EOKpC6yhZTS3ekUbFIVlhh%2BKxfchLYvpCT1LBMsjiouRhDB5BhEOF8Ccf691HdaY&X-Amz-Signature=78a84a125343b11ac8f93359eb3346702987581a7fae701a401350dc8a5a8149&X-Amz-SignedHeaders=host&x-id=GetObject)
**Explanation:** When engine size increases, there is a corresponding increase in the price of the vehicle. This positive correlation suggests that larger engines tend to be associated with higher prices in the market.
___
### Negative Correlation
Negative correlation indicates that as one variable increases, the other variable tends to decrease.
**Example: Highway Miles per Gallon and Price**
- **Negative Correlation:** As highway miles per gallon increases, price decreases.
- **Visualization:** Scatter plot with a steep negative slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/10f1f798-9cc4-4df2-a9c1-5a339f554a0b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663SGA4OOO%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T201646Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDIaCXVzLXdlc3QtMiJIMEYCIQDNFy1Ne5xwtjkpMIsplbEtp3IWguinTH2WiyJs7YdJhQIhAKLt1moHJqL0tQKB5l17yhpyroyDUE2BkrKnS6S6IJK6Kv8DCEoQABoMNjM3NDIzMTgzODA1IgyWIPFhQH6X%2Bfcyr8Iq3AMEoP5M6y%2BnqDnpb6XshxQJ3Rzvnx9K919XepCGK0W0%2B4Z8bhKw%2BwwdJFL7jKiiX58tdefAc3zbbANlZOUDXpMMFJzI7VN1tzJ9MM9q9xylACVlfOHHVE4h17RCKDpbnVcRYIoplG8gMUakfL4nofIPw51DKKMLiE8K99X3u54YLuaO4OwxzP4M50PrxgOwZ%2B8F%2BBT%2B2tW0WZEE6zcXkDkVbO6iGLpi1NaSbf3fzrDv1kVfur0sz9PEINf1PCnY1KtZSP4jna2JDY%2BQTtFJNuIPXb1trozejyyr56sUNTWRWVR9ijDwQ9N6L4Hc1yKQ%2BHTFTPn6vywo4UFH48WYfEBrq15Zs1eC7qnin8YYnRMk2WolGC9ND36tDck7KoIPjNNjm7EzanKjx6GtpBzLtr0nlA3o%2BXhxi6axapBAJBBDGuyZ1v3SlBytrZpuTsdS1pb94q7arUvhdKdkqUQmC%2FkL6G%2BXUszgOiXxS2iOZXzX1q4S3HtjfFwZGAsHiXgVS5M%2BZWte7SinlNZpMx5iqq5w46WyC3CElwUvwG%2BVmF%2Fbxid6CzJUr20PMVHUejVEKNM97J4FVmIrGPwIrT%2FgmlZU4BasK1On446LbaIhvYENVK7FUz55kN2JazbKczDauo69BjqkAfWnZWxeo6t4rsOvKKAlNzrNLms6NXRoe7hiyJpquqRvhHJ9N%2FpZcB0Hv4dYgGoLM2ZRSmZwwrUytTKpKs%2FmLQ2F0foOzq%2F4piOsdSYVYibgnfJw8RVjmkHTBNEiclpB9IS7vbW3NrGab2s0q7otHKnGI6XrK6lmXTRd4YcW44jL%2B5eIUVNdz6L8wqWgEVF1dltmrZ9Cz%2FVhqKtshFfv2ZovlBv2&X-Amz-Signature=c7de3b747900d44aab4b008cacc4531efd147919f2eed460dddeaef52d04f662&X-Amz-SignedHeaders=host&x-id=GetObject)
**Explanation:** When highway miles per gallon increases, the price of the vehicle tends to decrease. This negative correlation suggests that cars with higher fuel efficiency (more miles per gallon) are generally priced lower in the market.
___
### Weak Correlation
Weak correlation indicates a lack of strong relationship between the variables.
**Example: RPM and Price**
- **Weak Correlation:** Low and high RPM values show varied prices, indicating no strong predictive relationship.
- **Visualization:** Scatter plot with no clear trend or slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9f914514-8914-4bf4-ac84-d9e3077f6eb1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46646PKW2PG%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T201646Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDIaCXVzLXdlc3QtMiJGMEQCICFbN51aFBkYbiAkFo2h84e%2Fums75k6ow6VE3%2BdH%2BmC3AiAHQsz1rm2nbo1pixu7Nkfeg8MHXN6%2F3Cocf69qwHzpZir%2FAwhKEAAaDDYzNzQyMzE4MzgwNSIMteZz%2FoDidOMWj1sFKtwDgDEUoulTwhcSDitq3vcYyrNLy%2BUiF5iR%2FMZvyLfJzo%2FvKwC62rK%2FF4W%2FVnAGY0zH00T3cDT647Q4%2FFsYgHWIxqr5oCRPuKO5iQAa0j7skBndmhbDdevN5GTxj8g0ssHpWoyZIcT8Sz0SC6nbyUsPyQpXlTRLGst30MtWHmwyshVTPsYm6z6EfQfGJbMxE1NZkLxNcnDZ97XgW%2BaCW8AMOclTaJTnKvnV1nOi%2B42t5nQidB0tn9tiYunH4wSZsIf547ot41GtNVMqAhHYd76gnl49AC0RmNS1vMfDkILIsu9mBfa98iW4S%2BMfNRjsc%2BqwkFySBrVlqXv4096jyrw49lqH9cmb5rHXnXChPnCpAGfwGBYPDivCWw3K0xiB1YvbiAc%2B3eLoEwlhP0fpCplePJ%2FyODBImtq42nefhgl4na7idkDPm3YS1EV%2BHI3fXDF8e0DcGQ0PZ8yalgb8mN5KRhjtoMzqms598GKxmwOSrfouQoKe7z9tErJ6f0pU7etYtribNAP7ZEQeR0iP3WYsfBYjO3ds9TV05JQXJZwAQpuF2rK1DnjdUVTH%2Fh5JjQh%2FmSNTAkhb4trIpgto%2Bi3UCFADIXznjefiJhuUyn63tgDU8GyddDyKV0U%2FZ9kwzbqOvQY6pgHgURQkgQVrlAaIitw2x04MqskpOvsolVaiNJISxA1%2FcFFt3rd1PnGYk%2FGlhHsTjvCGk7KmrEXFhYtM2t6pqBKTadmL4Swgq2LuGgysD8CBvCr%2FVcbOS7W0EZd5iwl7DF3z0H5XSXEFnSePtOs3X8JkZRatlGDwUyqj7nQZyZOosr82aUEPD199DMys3wfctuoNb9WZnrS50R6Tl8uPM1UQ9k7Uqk3A&X-Amz-Signature=55e5e52d136cf22e1096624d8f6debca0ef0dc2dcc1bd9d98584aff5cf2b3e2a&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f18086e5-5b04-4fbf-8309-8944ab20d213/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VP4F5TSC%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T201646Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDIaCXVzLXdlc3QtMiJGMEQCIAurj12KvFQY2exsL%2Bv9Cbwk4rqGlmESPoynJK%2FPNF4RAiAcLWNxg6SW6wc8wIaeM3V4skJU34csRNsCpKS97bVXzSr%2FAwhKEAAaDDYzNzQyMzE4MzgwNSIMnj4EUcV34p8eJn7gKtwD3yEOiiIVzfyrsJbZPRpW7zysmOK1%2BI5teQL3%2BkW7%2FlWlqRKbD%2B084pEGxpHXLtXwUMm0n0Ew5txCIS%2Fko8JUKQX7mF%2B11IwAzs25Yi4%2BQhr1MStZHBULAG7TRazktOfyT%2F6fEKae0PaCuaQww4xtRe3S1GkBShQ7lgRnFDiZiaT07etMhUvbIDN8DxFqeL9yxtLz2Twxkw0FCR8RsQZflb8%2BAEsNYtobeEzEM11zgsMtMmlFecZTKKlNWK6Fm4gDn0%2BZ2bti%2FQeIZ%2BDgLzpCysKSHBbbxsT6m7MjvRdWY8zQzIXeKFG4N04JM8Mfwge16sA8AZub0IIU8gtBmL5rFb0jYkbG30vW7BC9mHR0cw2P8BdExJVvMqMOhUxSfIVCFDpT17S8vaQWJieO4pQitkg%2B%2FbOdFRBx8f7K7herrDesO2m6Q45YDPsdSybnel0x6cofKCCAVfsRvo98150BvukNY%2BSC0DK3QgeZI14gPhtxfN62P69of%2Bwxh08gbm5k8MtLWexlHtNT9wa5ejmcnJ9FjNd7z4dEuB2ZhBnHWgWbYq9in59B1KTg9P8tU15uFROvUeone65wsbanGEeFKHiiiENgpSPcrxvTKo0SOanUhA3F9x4YPv5%2Bi1owjbyOvQY6pgGC4zss4L5%2FpUqs92%2F3khMrVFVxotRCRYdRWHAtWpqapOVPhzydbz5jOuq4wQVzQ9hIxIzTDfGY5G488n6dwugQ2pFX9PlApGPFefRpBq4uF1%2B%2BK%2BbECSWHcwZCqk6dYHEUBtks6ORw2AKN6H0nmnkp%2FgJt8LE02jHV%2BWqIvcSaEcS5yOqECxKNhn6P02D2GybmDGO8ATEXCSJbfVu7PDa8zRYd0UXS&X-Amz-Signature=601b403a99b54c9c882d8da4e4d62711484054b103bb2816a6a4359b0f8a34e4&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Correlation Plot
Heatmap visualizes correlations among variables. Color scheme indicates Pearson correlation coefficients. Dark red diagonal line shows perfect correlation (value of 1) between variables and themselves.
This heatmap offers overview of variable relationships and their link with price.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cd3b341e-cc1a-45f7-8aec-cdc00436d270/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VP4F5TSC%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T201646Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDIaCXVzLXdlc3QtMiJGMEQCIAurj12KvFQY2exsL%2Bv9Cbwk4rqGlmESPoynJK%2FPNF4RAiAcLWNxg6SW6wc8wIaeM3V4skJU34csRNsCpKS97bVXzSr%2FAwhKEAAaDDYzNzQyMzE4MzgwNSIMnj4EUcV34p8eJn7gKtwD3yEOiiIVzfyrsJbZPRpW7zysmOK1%2BI5teQL3%2BkW7%2FlWlqRKbD%2B084pEGxpHXLtXwUMm0n0Ew5txCIS%2Fko8JUKQX7mF%2B11IwAzs25Yi4%2BQhr1MStZHBULAG7TRazktOfyT%2F6fEKae0PaCuaQww4xtRe3S1GkBShQ7lgRnFDiZiaT07etMhUvbIDN8DxFqeL9yxtLz2Twxkw0FCR8RsQZflb8%2BAEsNYtobeEzEM11zgsMtMmlFecZTKKlNWK6Fm4gDn0%2BZ2bti%2FQeIZ%2BDgLzpCysKSHBbbxsT6m7MjvRdWY8zQzIXeKFG4N04JM8Mfwge16sA8AZub0IIU8gtBmL5rFb0jYkbG30vW7BC9mHR0cw2P8BdExJVvMqMOhUxSfIVCFDpT17S8vaQWJieO4pQitkg%2B%2FbOdFRBx8f7K7herrDesO2m6Q45YDPsdSybnel0x6cofKCCAVfsRvo98150BvukNY%2BSC0DK3QgeZI14gPhtxfN62P69of%2Bwxh08gbm5k8MtLWexlHtNT9wa5ejmcnJ9FjNd7z4dEuB2ZhBnHWgWbYq9in59B1KTg9P8tU15uFROvUeone65wsbanGEeFKHiiiENgpSPcrxvTKo0SOanUhA3F9x4YPv5%2Bi1owjbyOvQY6pgGC4zss4L5%2FpUqs92%2F3khMrVFVxotRCRYdRWHAtWpqapOVPhzydbz5jOuq4wQVzQ9hIxIzTDfGY5G488n6dwugQ2pFX9PlApGPFefRpBq4uF1%2B%2BK%2BbECSWHcwZCqk6dYHEUBtks6ORw2AKN6H0nmnkp%2FgJt8LE02jHV%2BWqIvcSaEcS5yOqECxKNhn6P02D2GybmDGO8ATEXCSJbfVu7PDa8zRYd0UXS&X-Amz-Signature=9c401177047caf9dc02cf8aa50d1babfac72ff94e33ce62bdcd9075067705cae&X-Amz-SignedHeaders=host&x-id=GetObject)

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
