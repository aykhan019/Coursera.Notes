

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7e6d594d-952e-44b6-97ea-31225882aea6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46672RCMLT4%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T010924Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECAaCXVzLXdlc3QtMiJIMEYCIQDcCTmt9qcedF1VV5yL3SB3bIpmtdW9J01LqazoB83lIQIhAMG3Yjj%2FkUW7xI8vLJp0uFSY9NkZeI6%2FIdP7aiZL6j0QKv8DCDkQABoMNjM3NDIzMTgzODA1Igwb8KNDlsJ4Xc4Nposq3AOdIgRao2AG33fOsU92TElMjyBXt%2FgTP%2FKJe%2FI%2FA%2FcqdtzAm8dV%2BRM29XEYoYztmbk2WVJI82oXCac7NDyHsCvFp8zIXOGX8tg7ve3OqMe4jeT6lUB%2Fif0uGcwbPTbRzlniq%2B%2BkPVrmokjTywIFG1wBly2C2cdiIyMA7WGLWkqqXHchpnYsdFNJuYwZ75TRnyYDNTjprMQp3DdWkhUKbVfbk20pFHxcosHghvkS%2BxuJAjnTlP0DDP3SRT8o8ZSCd9tV6DI9N725kr2bQzIXe3YodeEtqqMidi2ch90K33Xlwftturz4jlaawkOFpDNlFIc7%2FG4oj4%2F6wLc9o1JLv%2FcfiTK%2BQSe5HJal6gI4LMXjxH4ZId2Ia2x1KqPrd4KTU3Etm9Wux%2B615gEShzJ0AyMXOvH7i3qKoA%2BrgAt0LQ6gFBi5vzdnwSlAEvX3qh5c%2Bo6yqqmKDPtyYfL%2F1IhYRFHd4WVzujr6b5z3rppqCTfskdmiRnyUIAT7SAI2tAL1aQaKvZHe7YZSxwUr7qRhrxG52ulCGEmbc8U347hLCp7hwZ%2Fxdzu5y9E%2BAFc2weiBRNTRiP4KjTdd3RAb7fbbIDM6KmHsU8AAoAVhaSuZr7IW1AbiRBZGvRDzuz43ijCizYq9BjqkAQXrQUv9YAGRJR5LU1ZPEEb2OTzhBa7I%2FETClxj50N14wHa%2FRnMlaMYMbFkzSgOLbBVajWsml3f7hcQMveUW0kQc8hX4OphjuaDNHVoHSc2MkhmPGvyTgyHwK9eTcx%2FR5kY162aCFraYICZrbeg8lZexWy7fp0yj9wP5lYbBmZKhDHrtCDapoFTsW%2BYCTgnSkBIjp2oofkVunmtebaCEHmDVH%2BFi&X-Amz-Signature=afc2404214e32a8132aa92a8fb661fa04e5b68be973f605096bb83dd4b08a5c6&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cbfaed9e-b398-4902-8936-dea058b21def/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46672RCMLT4%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T010924Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECAaCXVzLXdlc3QtMiJIMEYCIQDcCTmt9qcedF1VV5yL3SB3bIpmtdW9J01LqazoB83lIQIhAMG3Yjj%2FkUW7xI8vLJp0uFSY9NkZeI6%2FIdP7aiZL6j0QKv8DCDkQABoMNjM3NDIzMTgzODA1Igwb8KNDlsJ4Xc4Nposq3AOdIgRao2AG33fOsU92TElMjyBXt%2FgTP%2FKJe%2FI%2FA%2FcqdtzAm8dV%2BRM29XEYoYztmbk2WVJI82oXCac7NDyHsCvFp8zIXOGX8tg7ve3OqMe4jeT6lUB%2Fif0uGcwbPTbRzlniq%2B%2BkPVrmokjTywIFG1wBly2C2cdiIyMA7WGLWkqqXHchpnYsdFNJuYwZ75TRnyYDNTjprMQp3DdWkhUKbVfbk20pFHxcosHghvkS%2BxuJAjnTlP0DDP3SRT8o8ZSCd9tV6DI9N725kr2bQzIXe3YodeEtqqMidi2ch90K33Xlwftturz4jlaawkOFpDNlFIc7%2FG4oj4%2F6wLc9o1JLv%2FcfiTK%2BQSe5HJal6gI4LMXjxH4ZId2Ia2x1KqPrd4KTU3Etm9Wux%2B615gEShzJ0AyMXOvH7i3qKoA%2BrgAt0LQ6gFBi5vzdnwSlAEvX3qh5c%2Bo6yqqmKDPtyYfL%2F1IhYRFHd4WVzujr6b5z3rppqCTfskdmiRnyUIAT7SAI2tAL1aQaKvZHe7YZSxwUr7qRhrxG52ulCGEmbc8U347hLCp7hwZ%2Fxdzu5y9E%2BAFc2weiBRNTRiP4KjTdd3RAb7fbbIDM6KmHsU8AAoAVhaSuZr7IW1AbiRBZGvRDzuz43ijCizYq9BjqkAQXrQUv9YAGRJR5LU1ZPEEb2OTzhBa7I%2FETClxj50N14wHa%2FRnMlaMYMbFkzSgOLbBVajWsml3f7hcQMveUW0kQc8hX4OphjuaDNHVoHSc2MkhmPGvyTgyHwK9eTcx%2FR5kY162aCFraYICZrbeg8lZexWy7fp0yj9wP5lYbBmZKhDHrtCDapoFTsW%2BYCTgnSkBIjp2oofkVunmtebaCEHmDVH%2BFi&X-Amz-Signature=90b7feb58c02942a8d26acb0a9ce2bc85cf887ad733a532ad7883e0113b213e0&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/91181646-b1e0-4433-9711-6259a96a9247/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46672RCMLT4%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T010925Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECAaCXVzLXdlc3QtMiJIMEYCIQDcCTmt9qcedF1VV5yL3SB3bIpmtdW9J01LqazoB83lIQIhAMG3Yjj%2FkUW7xI8vLJp0uFSY9NkZeI6%2FIdP7aiZL6j0QKv8DCDkQABoMNjM3NDIzMTgzODA1Igwb8KNDlsJ4Xc4Nposq3AOdIgRao2AG33fOsU92TElMjyBXt%2FgTP%2FKJe%2FI%2FA%2FcqdtzAm8dV%2BRM29XEYoYztmbk2WVJI82oXCac7NDyHsCvFp8zIXOGX8tg7ve3OqMe4jeT6lUB%2Fif0uGcwbPTbRzlniq%2B%2BkPVrmokjTywIFG1wBly2C2cdiIyMA7WGLWkqqXHchpnYsdFNJuYwZ75TRnyYDNTjprMQp3DdWkhUKbVfbk20pFHxcosHghvkS%2BxuJAjnTlP0DDP3SRT8o8ZSCd9tV6DI9N725kr2bQzIXe3YodeEtqqMidi2ch90K33Xlwftturz4jlaawkOFpDNlFIc7%2FG4oj4%2F6wLc9o1JLv%2FcfiTK%2BQSe5HJal6gI4LMXjxH4ZId2Ia2x1KqPrd4KTU3Etm9Wux%2B615gEShzJ0AyMXOvH7i3qKoA%2BrgAt0LQ6gFBi5vzdnwSlAEvX3qh5c%2Bo6yqqmKDPtyYfL%2F1IhYRFHd4WVzujr6b5z3rppqCTfskdmiRnyUIAT7SAI2tAL1aQaKvZHe7YZSxwUr7qRhrxG52ulCGEmbc8U347hLCp7hwZ%2Fxdzu5y9E%2BAFc2weiBRNTRiP4KjTdd3RAb7fbbIDM6KmHsU8AAoAVhaSuZr7IW1AbiRBZGvRDzuz43ijCizYq9BjqkAQXrQUv9YAGRJR5LU1ZPEEb2OTzhBa7I%2FETClxj50N14wHa%2FRnMlaMYMbFkzSgOLbBVajWsml3f7hcQMveUW0kQc8hX4OphjuaDNHVoHSc2MkhmPGvyTgyHwK9eTcx%2FR5kY162aCFraYICZrbeg8lZexWy7fp0yj9wP5lYbBmZKhDHrtCDapoFTsW%2BYCTgnSkBIjp2oofkVunmtebaCEHmDVH%2BFi&X-Amz-Signature=3112377bfdb3808deac45c6792d7a18d3313f411b47e2c16e2c3c52c075c4007&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/09aba1c0-0d55-41dd-852a-a04c5b8a3fac/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46635QBE6NT%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T010925Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECAaCXVzLXdlc3QtMiJIMEYCIQCSSfHIGmFG0eCk8iL9XTgN0tTGv0JrmryWpqvpggcIsQIhAPrQPFf3%2BoU%2BeJXbzhIefVLVBYwFO9XGs64RDPvtiI4HKv8DCDkQABoMNjM3NDIzMTgzODA1Igy%2BiqfAmEc4gTQ0wakq3AM2LGtrblKUYs0ieaDHBGkhGbB9Z7u3LTlI2Vp6ym9vRZqyGqYjnVBxjSho%2BJGp6IvLxxRYgwZk3W0TXpwm6UtasjugcWp6ilCFB%2Bx1m%2Fa6RQzW6d3tuns1rm2Bg5Py0PlnxZaYe6sRum7E0V%2BWvsgwEkhJxett9u7m5opGA%2BrgtY%2FsK3BI8MQv9WU9xACQ%2FBR9Mbh1X8HJHt5%2FQku5faJMw%2F4Lb7wijEYBIUowm9c%2B%2FQivpIjV1CoEtR1ChnkWv1889UOiS9X8UZwetMA0SKWKovMyDet7Fd8Fecgt5p1XeoEHaCnv7Gz18jo2pQkHuFKra%2F9mIOC5AYl6DXg%2BV%2Fq1HUiY7iczozeNSwqkuSs6gceKLC5z1C3siLn9CP7BlUB7QCnw9bMVPDuuHkQIavdUq0HLTVjw%2FMWSt%2BxQzVSstlzXXMX%2FeWdu7sqazIR426GcxCICPhRAijqgZKGyok2wZ4P07bcNLluja7i65%2B%2FLeGKXMLPJaBnL7Avb%2F3fzE9TfN5%2F08OAZhnDdD7qv3ox3FQy3f0%2FXAP6hdDTlKW7X1JLsk52jTnffMcjfVDK4WZzZc5mAKQrdt%2F1U%2BHdg0nsWQhgTcycEZ05xE8uEmorQjebaqiHFpIx6A9aOMzDSzYq9BjqkATv%2BognP8qnndmej02R2N%2FMylaEv0ktIOMhuu%2FegxhnmW6zemK04oOfqUDr%2FAbk%2BS6mjCaAToRAH%2BVhEOGhB%2BGHYbu4n%2B5NfxsvfxvLnHZDkbiNe8H1TDbJO7zK3aHUIAIRJcIljInVf8YUMOXO328jpx9OGzkwWd0sJyO55unDwZBHDklrdvlZl5hk4hIHtnFCILr3f7mMaWtVnfrrWCC65wFqR&X-Amz-Signature=5fb83ef57c4f0e0212642cf280d5634d30799d85e25f00b3ef208bc460e9852e&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 2. Scatter Plot
Scatter plots present the relationship between two variables in a dataset. It represents data points on a two-dimensional plane. The independent variable or attribute is plotted on the X-axis, while the dependent variable is plotted on the Y-axis.
**Syntax:**
```python
plt.scatter(x, y)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23708af9-659f-4f23-b626-1a4292d7842c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46635QBE6NT%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T010925Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECAaCXVzLXdlc3QtMiJIMEYCIQCSSfHIGmFG0eCk8iL9XTgN0tTGv0JrmryWpqvpggcIsQIhAPrQPFf3%2BoU%2BeJXbzhIefVLVBYwFO9XGs64RDPvtiI4HKv8DCDkQABoMNjM3NDIzMTgzODA1Igy%2BiqfAmEc4gTQ0wakq3AM2LGtrblKUYs0ieaDHBGkhGbB9Z7u3LTlI2Vp6ym9vRZqyGqYjnVBxjSho%2BJGp6IvLxxRYgwZk3W0TXpwm6UtasjugcWp6ilCFB%2Bx1m%2Fa6RQzW6d3tuns1rm2Bg5Py0PlnxZaYe6sRum7E0V%2BWvsgwEkhJxett9u7m5opGA%2BrgtY%2FsK3BI8MQv9WU9xACQ%2FBR9Mbh1X8HJHt5%2FQku5faJMw%2F4Lb7wijEYBIUowm9c%2B%2FQivpIjV1CoEtR1ChnkWv1889UOiS9X8UZwetMA0SKWKovMyDet7Fd8Fecgt5p1XeoEHaCnv7Gz18jo2pQkHuFKra%2F9mIOC5AYl6DXg%2BV%2Fq1HUiY7iczozeNSwqkuSs6gceKLC5z1C3siLn9CP7BlUB7QCnw9bMVPDuuHkQIavdUq0HLTVjw%2FMWSt%2BxQzVSstlzXXMX%2FeWdu7sqazIR426GcxCICPhRAijqgZKGyok2wZ4P07bcNLluja7i65%2B%2FLeGKXMLPJaBnL7Avb%2F3fzE9TfN5%2F08OAZhnDdD7qv3ox3FQy3f0%2FXAP6hdDTlKW7X1JLsk52jTnffMcjfVDK4WZzZc5mAKQrdt%2F1U%2BHdg0nsWQhgTcycEZ05xE8uEmorQjebaqiHFpIx6A9aOMzDSzYq9BjqkATv%2BognP8qnndmej02R2N%2FMylaEv0ktIOMhuu%2FegxhnmW6zemK04oOfqUDr%2FAbk%2BS6mjCaAToRAH%2BVhEOGhB%2BGHYbu4n%2B5NfxsvfxvLnHZDkbiNe8H1TDbJO7zK3aHUIAIRJcIljInVf8YUMOXO328jpx9OGzkwWd0sJyO55unDwZBHDklrdvlZl5hk4hIHtnFCILr3f7mMaWtVnfrrWCC65wFqR&X-Amz-Signature=74ffb7e4b5d3e514ae495e83b635e535c004014065744f0eb16de32875d59e71&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 3. Histogram
A histogram is an important visual representation of data in categorical form. To view the data in a "Binned" form, use the histogram plot with a number of bins required or with the data points that mark the bin edges. The x-axis represents the data bins, and the y-axis represents the number of elements in each bin.
**Syntax:**
```python
plt.hist(x, bins)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/24e4424a-df87-40a1-b63b-195cbdc2e0ab/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46635QBE6NT%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T010925Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECAaCXVzLXdlc3QtMiJIMEYCIQCSSfHIGmFG0eCk8iL9XTgN0tTGv0JrmryWpqvpggcIsQIhAPrQPFf3%2BoU%2BeJXbzhIefVLVBYwFO9XGs64RDPvtiI4HKv8DCDkQABoMNjM3NDIzMTgzODA1Igy%2BiqfAmEc4gTQ0wakq3AM2LGtrblKUYs0ieaDHBGkhGbB9Z7u3LTlI2Vp6ym9vRZqyGqYjnVBxjSho%2BJGp6IvLxxRYgwZk3W0TXpwm6UtasjugcWp6ilCFB%2Bx1m%2Fa6RQzW6d3tuns1rm2Bg5Py0PlnxZaYe6sRum7E0V%2BWvsgwEkhJxett9u7m5opGA%2BrgtY%2FsK3BI8MQv9WU9xACQ%2FBR9Mbh1X8HJHt5%2FQku5faJMw%2F4Lb7wijEYBIUowm9c%2B%2FQivpIjV1CoEtR1ChnkWv1889UOiS9X8UZwetMA0SKWKovMyDet7Fd8Fecgt5p1XeoEHaCnv7Gz18jo2pQkHuFKra%2F9mIOC5AYl6DXg%2BV%2Fq1HUiY7iczozeNSwqkuSs6gceKLC5z1C3siLn9CP7BlUB7QCnw9bMVPDuuHkQIavdUq0HLTVjw%2FMWSt%2BxQzVSstlzXXMX%2FeWdu7sqazIR426GcxCICPhRAijqgZKGyok2wZ4P07bcNLluja7i65%2B%2FLeGKXMLPJaBnL7Avb%2F3fzE9TfN5%2F08OAZhnDdD7qv3ox3FQy3f0%2FXAP6hdDTlKW7X1JLsk52jTnffMcjfVDK4WZzZc5mAKQrdt%2F1U%2BHdg0nsWQhgTcycEZ05xE8uEmorQjebaqiHFpIx6A9aOMzDSzYq9BjqkATv%2BognP8qnndmej02R2N%2FMylaEv0ktIOMhuu%2FegxhnmW6zemK04oOfqUDr%2FAbk%2BS6mjCaAToRAH%2BVhEOGhB%2BGHYbu4n%2B5NfxsvfxvLnHZDkbiNe8H1TDbJO7zK3aHUIAIRJcIljInVf8YUMOXO328jpx9OGzkwWd0sJyO55unDwZBHDklrdvlZl5hk4hIHtnFCILr3f7mMaWtVnfrrWCC65wFqR&X-Amz-Signature=ae784e736695f49cd838074b6acb03688f1ebb2f7826b83d9654be2ad6e3803b&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ab5a6dfe-51f5-43ee-bcb3-33dae4a1c7ad/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46635QBE6NT%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T010925Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECAaCXVzLXdlc3QtMiJIMEYCIQCSSfHIGmFG0eCk8iL9XTgN0tTGv0JrmryWpqvpggcIsQIhAPrQPFf3%2BoU%2BeJXbzhIefVLVBYwFO9XGs64RDPvtiI4HKv8DCDkQABoMNjM3NDIzMTgzODA1Igy%2BiqfAmEc4gTQ0wakq3AM2LGtrblKUYs0ieaDHBGkhGbB9Z7u3LTlI2Vp6ym9vRZqyGqYjnVBxjSho%2BJGp6IvLxxRYgwZk3W0TXpwm6UtasjugcWp6ilCFB%2Bx1m%2Fa6RQzW6d3tuns1rm2Bg5Py0PlnxZaYe6sRum7E0V%2BWvsgwEkhJxett9u7m5opGA%2BrgtY%2FsK3BI8MQv9WU9xACQ%2FBR9Mbh1X8HJHt5%2FQku5faJMw%2F4Lb7wijEYBIUowm9c%2B%2FQivpIjV1CoEtR1ChnkWv1889UOiS9X8UZwetMA0SKWKovMyDet7Fd8Fecgt5p1XeoEHaCnv7Gz18jo2pQkHuFKra%2F9mIOC5AYl6DXg%2BV%2Fq1HUiY7iczozeNSwqkuSs6gceKLC5z1C3siLn9CP7BlUB7QCnw9bMVPDuuHkQIavdUq0HLTVjw%2FMWSt%2BxQzVSstlzXXMX%2FeWdu7sqazIR426GcxCICPhRAijqgZKGyok2wZ4P07bcNLluja7i65%2B%2FLeGKXMLPJaBnL7Avb%2F3fzE9TfN5%2F08OAZhnDdD7qv3ox3FQy3f0%2FXAP6hdDTlKW7X1JLsk52jTnffMcjfVDK4WZzZc5mAKQrdt%2F1U%2BHdg0nsWQhgTcycEZ05xE8uEmorQjebaqiHFpIx6A9aOMzDSzYq9BjqkATv%2BognP8qnndmej02R2N%2FMylaEv0ktIOMhuu%2FegxhnmW6zemK04oOfqUDr%2FAbk%2BS6mjCaAToRAH%2BVhEOGhB%2BGHYbu4n%2B5NfxsvfxvLnHZDkbiNe8H1TDbJO7zK3aHUIAIRJcIljInVf8YUMOXO328jpx9OGzkwWd0sJyO55unDwZBHDklrdvlZl5hk4hIHtnFCILr3f7mMaWtVnfrrWCC65wFqR&X-Amz-Signature=40c18e003461739e533faca08e344d17f30e0d42f6834b8408234e2888ed9eff&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8f1b1d60-cf1b-42b3-9faa-f634c89c3f84/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46635QBE6NT%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T010925Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECAaCXVzLXdlc3QtMiJIMEYCIQCSSfHIGmFG0eCk8iL9XTgN0tTGv0JrmryWpqvpggcIsQIhAPrQPFf3%2BoU%2BeJXbzhIefVLVBYwFO9XGs64RDPvtiI4HKv8DCDkQABoMNjM3NDIzMTgzODA1Igy%2BiqfAmEc4gTQ0wakq3AM2LGtrblKUYs0ieaDHBGkhGbB9Z7u3LTlI2Vp6ym9vRZqyGqYjnVBxjSho%2BJGp6IvLxxRYgwZk3W0TXpwm6UtasjugcWp6ilCFB%2Bx1m%2Fa6RQzW6d3tuns1rm2Bg5Py0PlnxZaYe6sRum7E0V%2BWvsgwEkhJxett9u7m5opGA%2BrgtY%2FsK3BI8MQv9WU9xACQ%2FBR9Mbh1X8HJHt5%2FQku5faJMw%2F4Lb7wijEYBIUowm9c%2B%2FQivpIjV1CoEtR1ChnkWv1889UOiS9X8UZwetMA0SKWKovMyDet7Fd8Fecgt5p1XeoEHaCnv7Gz18jo2pQkHuFKra%2F9mIOC5AYl6DXg%2BV%2Fq1HUiY7iczozeNSwqkuSs6gceKLC5z1C3siLn9CP7BlUB7QCnw9bMVPDuuHkQIavdUq0HLTVjw%2FMWSt%2BxQzVSstlzXXMX%2FeWdu7sqazIR426GcxCICPhRAijqgZKGyok2wZ4P07bcNLluja7i65%2B%2FLeGKXMLPJaBnL7Avb%2F3fzE9TfN5%2F08OAZhnDdD7qv3ox3FQy3f0%2FXAP6hdDTlKW7X1JLsk52jTnffMcjfVDK4WZzZc5mAKQrdt%2F1U%2BHdg0nsWQhgTcycEZ05xE8uEmorQjebaqiHFpIx6A9aOMzDSzYq9BjqkATv%2BognP8qnndmej02R2N%2FMylaEv0ktIOMhuu%2FegxhnmW6zemK04oOfqUDr%2FAbk%2BS6mjCaAToRAH%2BVhEOGhB%2BGHYbu4n%2B5NfxsvfxvLnHZDkbiNe8H1TDbJO7zK3aHUIAIRJcIljInVf8YUMOXO328jpx9OGzkwWd0sJyO55unDwZBHDklrdvlZl5hk4hIHtnFCILr3f7mMaWtVnfrrWCC65wFqR&X-Amz-Signature=32c84460f978d57e56e854f7342cbd5e73ca1bd07673fcc39f3756ea2da05730&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/13ad0497-05fe-4eaa-984e-707b33e14761/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46635QBE6NT%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T010926Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECAaCXVzLXdlc3QtMiJIMEYCIQCSSfHIGmFG0eCk8iL9XTgN0tTGv0JrmryWpqvpggcIsQIhAPrQPFf3%2BoU%2BeJXbzhIefVLVBYwFO9XGs64RDPvtiI4HKv8DCDkQABoMNjM3NDIzMTgzODA1Igy%2BiqfAmEc4gTQ0wakq3AM2LGtrblKUYs0ieaDHBGkhGbB9Z7u3LTlI2Vp6ym9vRZqyGqYjnVBxjSho%2BJGp6IvLxxRYgwZk3W0TXpwm6UtasjugcWp6ilCFB%2Bx1m%2Fa6RQzW6d3tuns1rm2Bg5Py0PlnxZaYe6sRum7E0V%2BWvsgwEkhJxett9u7m5opGA%2BrgtY%2FsK3BI8MQv9WU9xACQ%2FBR9Mbh1X8HJHt5%2FQku5faJMw%2F4Lb7wijEYBIUowm9c%2B%2FQivpIjV1CoEtR1ChnkWv1889UOiS9X8UZwetMA0SKWKovMyDet7Fd8Fecgt5p1XeoEHaCnv7Gz18jo2pQkHuFKra%2F9mIOC5AYl6DXg%2BV%2Fq1HUiY7iczozeNSwqkuSs6gceKLC5z1C3siLn9CP7BlUB7QCnw9bMVPDuuHkQIavdUq0HLTVjw%2FMWSt%2BxQzVSstlzXXMX%2FeWdu7sqazIR426GcxCICPhRAijqgZKGyok2wZ4P07bcNLluja7i65%2B%2FLeGKXMLPJaBnL7Avb%2F3fzE9TfN5%2F08OAZhnDdD7qv3ox3FQy3f0%2FXAP6hdDTlKW7X1JLsk52jTnffMcjfVDK4WZzZc5mAKQrdt%2F1U%2BHdg0nsWQhgTcycEZ05xE8uEmorQjebaqiHFpIx6A9aOMzDSzYq9BjqkATv%2BognP8qnndmej02R2N%2FMylaEv0ktIOMhuu%2FegxhnmW6zemK04oOfqUDr%2FAbk%2BS6mjCaAToRAH%2BVhEOGhB%2BGHYbu4n%2B5NfxsvfxvLnHZDkbiNe8H1TDbJO7zK3aHUIAIRJcIljInVf8YUMOXO328jpx9OGzkwWd0sJyO55unDwZBHDklrdvlZl5hk4hIHtnFCILr3f7mMaWtVnfrrWCC65wFqR&X-Amz-Signature=4c3260b4df6301115ed461dd0a20d113aec5a99be7c17b76d261abcb62da31ac&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 2. Box and Whisker Plot
A box plot shows the distribution of quantitative data in a way that facilitates comparisons between variables or across levels of a categorical variable. The box shows the quartiles of the dataset while the whiskers extend to show the rest of the distribution, except for points that are determined to be "outliers".
**Syntax:**
```python
sns.boxplot(x='header_1', y='header_2', data=df)
```
**Example Output:**


![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d207ae92-0a7c-4e2f-aa65-0ee5a2c33bf7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SB4T5LZW%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T010930Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECAaCXVzLXdlc3QtMiJHMEUCIGjzU9ccHDxNEQqHfuBHWYv4%2B4D%2FWtbu9EParWlv56MdAiEAnX3%2BEC%2B%2BLOJKmI2Ka66MUdh0GABxqasqSSI1oP6cq6oq%2FwMIORAAGgw2Mzc0MjMxODM4MDUiDDwh07sdvQ7GFljlCSrcAwzhQ34JlkBz%2F1FSFAW6n%2F7514dxOwX1yDD3W5Abt1VPNnMfuPDmWOog1J2QJe%2FR%2FYMm8QwZEFP4B1pUgLvguorprI5KGvkYMkVJQbFQxyxVMwahTPuavZYK%2FkoTwf%2BsQdquKOrJXh5%2FKUP0orikbtJWhs1JuB11QEfCXl%2B52DPKw5ifmydnMt%2BIm5W%2B7DNQkoubGT1V%2F6k%2F178VHcVxI8L9xTSseSSjVvcdb%2Faeb8e1vD%2BWko8jzFUDwalfM8AmMlb7z645IoB%2Bk0PCgK%2F1n85p53oueufwmtTFC6HqyDWJi10ALuOp8q8wdoHYcwJJxSM8F948jIoqTCrdu2NyRHYsjeMtgVZOr5eByko4rPdNd3ERzz%2BLzvwWgyOaDqrIwjlMajc%2FHJwQH3buAYHYEFHntET9DsVEmAL64A8mU3bfY8Mr6jzJ65jaPsE84SM1Dn4mdYxikSUyE2KyC7vUUETV%2BpAGX6gC5Zh6hVT6yY8pRwc2tDRgwbWhsXn1d2sbb%2FNREPVd4aTKd%2B99ZcjnQs5SBHgNZmJTID0Sj0vfKh8dN89Rm%2F%2FaexOogNT0vnyey55H%2FaZBu93EgyaTglIOXHv4r5knofFLKTJlzG9%2FhPjJ9Otd4rj601ML0ikpMNXNir0GOqUBeTjYdvIrievF0PE%2BnR1YARK1BW0EsMIblBTGuhRrJqLWdovGjyYsJkw32sEULCen%2FyjUzVVzMrHVMhnsv5qUz5TSP%2BAOstXJ1zpstWGk8E1byVU3RyxsBj7IzLiVd4jZnCsbpSctwuqK0oxFwliBXS%2BEoy6qD4gitehRkv0Q8QL2zQ9as8bsr7b0ABCvTZlyuViZL7bSoDstoa%2F%2FVXioOeYKzBuY&X-Amz-Signature=c089f999b131cd1757aab939e78f9144aeb37992d00a766236789fd72b8f57cf&X-Amz-SignedHeaders=host&x-id=GetObject)

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0e516edc-7551-4792-ab18-0494db3c4c0c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WKBBFJGH%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T010930Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECAaCXVzLXdlc3QtMiJGMEQCIGpdDCrOuS2JLa0ehNYZQfT1ytfeznaH0cc1j2S8SBudAiA2SQM4HIUrBdHBc7IgBw3W%2F0FOPCT1UAWx4LK9EjQ5uyr%2FAwg5EAAaDDYzNzQyMzE4MzgwNSIMe5M%2BCryfS78xoaFCKtwDzzhQuNpz5T8bCkeggE4TioOMBydTkK2XJX87AWznz6jnmlWlCnXn0f4AjRgXx5o6ik1xqtCxVR7NOOG23myLN42FUNUxdF6zX%2BYO7USEQdw2NhJJjRkztiudXe1dqccR3xCptVp7o1iwKuJiaHSo633VS4Vj%2BcAgYxiTGLJRDAu%2F4dQ9Bc%2BQOt%2FGsGeKwOrmNuEWynTi4DXV%2FM5L%2FgGeDesS6sf4tOzFYoNKqGjZAvggWxJdbc2C57yCQTJ9UNLh5y3hnAV1zBzeePk8Pv5AHsp7JWk5MjVxhaaAJ66Wn0XrBH1IMuEoQK497P9%2FMofpKzoBWZ%2ByPHjs%2FTNuRaCMUro2o8%2B0QbKrJ9jSOITItqVzb6HsK8mXSdFfSPkhHZJmKnWwibVqWUWGE0ldtQoq1MZ25pCrJotIgZdphvA4KN3VI2NCDw6dUtDSY7ZL6msF1%2BDiwmJQmaBBwA6zwqUb%2FMmgdQyzODfpaL7PabUxovyB2yYJrSrRT778885J94Kmw%2BXPYMVdsrL8o1H4WdB8UxXGxm0IryNTd43YnmB5oUqALKq05fhDke7QzweEbr%2FY1iLR5vwRS7OjMPxD6NuyABjQxvRVcFTnz4LxbVj5juLL77BE7BnU4S10UcMw6MyKvQY6pgF7K9HqFNN3cYf1YodeTZ3joj0uFkLASsrCUU6o6eSYByOfQ9DY7Vtkhg9fCRRGVBR6g4M5Yh4PV3JFlTKzD%2F7HHG2rVefLdFw8IUmSsnG3fg7jXQXHEzKiOloXZClHITRIvqIHLDmlhj34CWKsmH1dfQMRfdPcb45N6hSz4gbv4FXlf6zJSL18U%2F6ymsolQKHrdgraqzL6UtYEeK8xlund98Dj4kJe&X-Amz-Signature=a20d07228b33f086d08b5805620a36b29d31aa10c2fcd7b45d60ac57e6928c63&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23a79b9d-2356-49a9-8fd9-65c6b0ab2cc5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46635QBE6NT%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T010926Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECAaCXVzLXdlc3QtMiJIMEYCIQCSSfHIGmFG0eCk8iL9XTgN0tTGv0JrmryWpqvpggcIsQIhAPrQPFf3%2BoU%2BeJXbzhIefVLVBYwFO9XGs64RDPvtiI4HKv8DCDkQABoMNjM3NDIzMTgzODA1Igy%2BiqfAmEc4gTQ0wakq3AM2LGtrblKUYs0ieaDHBGkhGbB9Z7u3LTlI2Vp6ym9vRZqyGqYjnVBxjSho%2BJGp6IvLxxRYgwZk3W0TXpwm6UtasjugcWp6ilCFB%2Bx1m%2Fa6RQzW6d3tuns1rm2Bg5Py0PlnxZaYe6sRum7E0V%2BWvsgwEkhJxett9u7m5opGA%2BrgtY%2FsK3BI8MQv9WU9xACQ%2FBR9Mbh1X8HJHt5%2FQku5faJMw%2F4Lb7wijEYBIUowm9c%2B%2FQivpIjV1CoEtR1ChnkWv1889UOiS9X8UZwetMA0SKWKovMyDet7Fd8Fecgt5p1XeoEHaCnv7Gz18jo2pQkHuFKra%2F9mIOC5AYl6DXg%2BV%2Fq1HUiY7iczozeNSwqkuSs6gceKLC5z1C3siLn9CP7BlUB7QCnw9bMVPDuuHkQIavdUq0HLTVjw%2FMWSt%2BxQzVSstlzXXMX%2FeWdu7sqazIR426GcxCICPhRAijqgZKGyok2wZ4P07bcNLluja7i65%2B%2FLeGKXMLPJaBnL7Avb%2F3fzE9TfN5%2F08OAZhnDdD7qv3ox3FQy3f0%2FXAP6hdDTlKW7X1JLsk52jTnffMcjfVDK4WZzZc5mAKQrdt%2F1U%2BHdg0nsWQhgTcycEZ05xE8uEmorQjebaqiHFpIx6A9aOMzDSzYq9BjqkATv%2BognP8qnndmej02R2N%2FMylaEv0ktIOMhuu%2FegxhnmW6zemK04oOfqUDr%2FAbk%2BS6mjCaAToRAH%2BVhEOGhB%2BGHYbu4n%2B5NfxsvfxvLnHZDkbiNe8H1TDbJO7zK3aHUIAIRJcIljInVf8YUMOXO328jpx9OGzkwWd0sJyO55unDwZBHDklrdvlZl5hk4hIHtnFCILr3f7mMaWtVnfrrWCC65wFqR&X-Amz-Signature=c01608fa7e5e52f84bd29dcfe32b64e946274e74e48a7d137adb8979a84ad066&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 4. KDE Plot
A Kernel Density Estimate (KDE) plot is a graph that creates a probability distribution curve for the data based upon its likelihood of occurrence on a specific value. This is created for a single vector of information.
**Syntax:**
```python
sns.kdeplot(X) || sns.kdeplot(df['age'])
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0d571213-2a2f-4921-a50b-880847aa05ee/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46635QBE6NT%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T010926Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECAaCXVzLXdlc3QtMiJIMEYCIQCSSfHIGmFG0eCk8iL9XTgN0tTGv0JrmryWpqvpggcIsQIhAPrQPFf3%2BoU%2BeJXbzhIefVLVBYwFO9XGs64RDPvtiI4HKv8DCDkQABoMNjM3NDIzMTgzODA1Igy%2BiqfAmEc4gTQ0wakq3AM2LGtrblKUYs0ieaDHBGkhGbB9Z7u3LTlI2Vp6ym9vRZqyGqYjnVBxjSho%2BJGp6IvLxxRYgwZk3W0TXpwm6UtasjugcWp6ilCFB%2Bx1m%2Fa6RQzW6d3tuns1rm2Bg5Py0PlnxZaYe6sRum7E0V%2BWvsgwEkhJxett9u7m5opGA%2BrgtY%2FsK3BI8MQv9WU9xACQ%2FBR9Mbh1X8HJHt5%2FQku5faJMw%2F4Lb7wijEYBIUowm9c%2B%2FQivpIjV1CoEtR1ChnkWv1889UOiS9X8UZwetMA0SKWKovMyDet7Fd8Fecgt5p1XeoEHaCnv7Gz18jo2pQkHuFKra%2F9mIOC5AYl6DXg%2BV%2Fq1HUiY7iczozeNSwqkuSs6gceKLC5z1C3siLn9CP7BlUB7QCnw9bMVPDuuHkQIavdUq0HLTVjw%2FMWSt%2BxQzVSstlzXXMX%2FeWdu7sqazIR426GcxCICPhRAijqgZKGyok2wZ4P07bcNLluja7i65%2B%2FLeGKXMLPJaBnL7Avb%2F3fzE9TfN5%2F08OAZhnDdD7qv3ox3FQy3f0%2FXAP6hdDTlKW7X1JLsk52jTnffMcjfVDK4WZzZc5mAKQrdt%2F1U%2BHdg0nsWQhgTcycEZ05xE8uEmorQjebaqiHFpIx6A9aOMzDSzYq9BjqkATv%2BognP8qnndmej02R2N%2FMylaEv0ktIOMhuu%2FegxhnmW6zemK04oOfqUDr%2FAbk%2BS6mjCaAToRAH%2BVhEOGhB%2BGHYbu4n%2B5NfxsvfxvLnHZDkbiNe8H1TDbJO7zK3aHUIAIRJcIljInVf8YUMOXO328jpx9OGzkwWd0sJyO55unDwZBHDklrdvlZl5hk4hIHtnFCILr3f7mMaWtVnfrrWCC65wFqR&X-Amz-Signature=9e454cef1fef7e4e6e4bd6755c6b26ab6310acd87e7d25e0faa81ecd86f954c5&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/53752550-ef82-4ca9-a01a-09921f0282d0/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46635QBE6NT%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T010926Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECAaCXVzLXdlc3QtMiJIMEYCIQCSSfHIGmFG0eCk8iL9XTgN0tTGv0JrmryWpqvpggcIsQIhAPrQPFf3%2BoU%2BeJXbzhIefVLVBYwFO9XGs64RDPvtiI4HKv8DCDkQABoMNjM3NDIzMTgzODA1Igy%2BiqfAmEc4gTQ0wakq3AM2LGtrblKUYs0ieaDHBGkhGbB9Z7u3LTlI2Vp6ym9vRZqyGqYjnVBxjSho%2BJGp6IvLxxRYgwZk3W0TXpwm6UtasjugcWp6ilCFB%2Bx1m%2Fa6RQzW6d3tuns1rm2Bg5Py0PlnxZaYe6sRum7E0V%2BWvsgwEkhJxett9u7m5opGA%2BrgtY%2FsK3BI8MQv9WU9xACQ%2FBR9Mbh1X8HJHt5%2FQku5faJMw%2F4Lb7wijEYBIUowm9c%2B%2FQivpIjV1CoEtR1ChnkWv1889UOiS9X8UZwetMA0SKWKovMyDet7Fd8Fecgt5p1XeoEHaCnv7Gz18jo2pQkHuFKra%2F9mIOC5AYl6DXg%2BV%2Fq1HUiY7iczozeNSwqkuSs6gceKLC5z1C3siLn9CP7BlUB7QCnw9bMVPDuuHkQIavdUq0HLTVjw%2FMWSt%2BxQzVSstlzXXMX%2FeWdu7sqazIR426GcxCICPhRAijqgZKGyok2wZ4P07bcNLluja7i65%2B%2FLeGKXMLPJaBnL7Avb%2F3fzE9TfN5%2F08OAZhnDdD7qv3ox3FQy3f0%2FXAP6hdDTlKW7X1JLsk52jTnffMcjfVDK4WZzZc5mAKQrdt%2F1U%2BHdg0nsWQhgTcycEZ05xE8uEmorQjebaqiHFpIx6A9aOMzDSzYq9BjqkATv%2BognP8qnndmej02R2N%2FMylaEv0ktIOMhuu%2FegxhnmW6zemK04oOfqUDr%2FAbk%2BS6mjCaAToRAH%2BVhEOGhB%2BGHYbu4n%2B5NfxsvfxvLnHZDkbiNe8H1TDbJO7zK3aHUIAIRJcIljInVf8YUMOXO328jpx9OGzkwWd0sJyO55unDwZBHDklrdvlZl5hk4hIHtnFCILr3f7mMaWtVnfrrWCC65wFqR&X-Amz-Signature=3c8aa747b6ab34cbcf1a899ebfc9dd8fc27683ce9743a183d74abda16c6b96ec&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
## 4. Correlation Between Variables
Correlation is a statistical measure of the extent to which different variables are interdependent. It indicates how changes in one variable are associated with changes in another variable over time.
### Positive Correlation
Positive correlation indicates that as one variable increases, the other variable also tends to increase.
**Example: Engine Size and Price**
- **Positive Correlation:** Engine size increases, price also increases.
- **Visualization:** Scatter plot with a steep positive slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c7ea9b0-3ef3-4357-a9c3-554fc71b6b15/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46652LOG442%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T010927Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECAaCXVzLXdlc3QtMiJGMEQCIEgDvRavx8hv0WA9FL2szJtqksLbuh%2FwXFcr13TDj7PsAiAzYa4m%2Fx6UAa20tvMDsjM%2FXMb3bRBJpCngjzMy9fGnyyr%2FAwg5EAAaDDYzNzQyMzE4MzgwNSIMTR7BUY6Uuoo%2B1GIMKtwDby%2BXKeh9w2XhG6M0BFK8u%2FPA89EaBSKItEu7LrI6GR%2B6PPAdpUW%2FPzzPdp2QGp%2BKKfD4E65N5bK4jmyZN5RSjd41WYFWdX4antE0CEz1kcvCCIFotFT4VK%2F6wDitGRMkq6okbXIDrjpB3%2BNYiidGSDMCTu%2FmETfmDguLWFUbH4YXDIB07XCrlBOd7Uz3CAK%2Fu9cP6FPk1SAroBNDCsIj3lRFWScE78TzaoFKktjJZ4w5MRQlwYK9WGPxg4TmowhCYs2jnT%2B3Ei1NWlW241EXHvet%2BEAHFSSs%2BADeGbuchwzUcrc9Qp1%2BIKC3azyqB6Pn5svT1sRglWerW5X8VFAztFan%2BeT0Ej8sLXXVz0f4NlCMdzmDustu2Lw5izzBS0en6kwg%2B1YJ9l%2BOlaJC1cTs%2Fa2Q8CpRnEIQ7KkHDk5ot96IRfbxEXbffyvu4i0yu1t6%2BzYCkLkZlgYR65NEa8cn2E00L16%2FZEGk8F7OX2HtFqm3NI%2FDEqckQros5KZ5EkoKFl2BPx%2F6NnZTyvQRagHk3viPcJfzJQr1MC9SobL2krjW0aCZT5L3Eh72xfn1AUGga9SPvnxQ3A613%2FG0nmaxovxEmyzYq%2BXpDurfd1hIzlBICgptnk1yNTuAOVkwmc2KvQY6pgGM339njgshSpgL%2BaSW5BDYq1u%2FivFrFz08jYC0reQvL8%2Fs0W9IlBqDZu1CWGXUSDZ2u%2BrOeDO5ruK9gOFG%2FmRPsjoR3GFJlZB1XK4b72aHFgExzsu8h8rBZSwL0RviFYIGwMQjBtYnrDrc8aBFRrXB5GG%2BiykS%2Bd6HwfI7cBB9pKdU4ix8OkuJC8MBw3A9kK0Va1JOk%2FIWQZCXkbZAfPxZ5pFYYFPQ&X-Amz-Signature=455bcd2b3444c7440c008750cfe869593331df22eb2ac79b6f8774e2e39b5ac4&X-Amz-SignedHeaders=host&x-id=GetObject)
**Explanation:** When engine size increases, there is a corresponding increase in the price of the vehicle. This positive correlation suggests that larger engines tend to be associated with higher prices in the market.
___
### Negative Correlation
Negative correlation indicates that as one variable increases, the other variable tends to decrease.
**Example: Highway Miles per Gallon and Price**
- **Negative Correlation:** As highway miles per gallon increases, price decreases.
- **Visualization:** Scatter plot with a steep negative slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/10f1f798-9cc4-4df2-a9c1-5a339f554a0b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VJNIWBHL%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T010927Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECAaCXVzLXdlc3QtMiJGMEQCIHq2dHLA2v579H3zAwQHpiyBvzW2LSJ6h8kcvgQ2Uxi8AiAfLA%2BNOluWu8CUZd8GtnaJ8G3iaIJqimIRs7idTqf%2FYir%2FAwg5EAAaDDYzNzQyMzE4MzgwNSIMNUQjzF7vLlQmJ2FTKtwDcV2Oj8z2FigwWqEsxYjP5T84laPur5HXtpxKiIid7p3CtgZq4y3WZafpN7hHt4uclmXlo8KfGjdLHzATvEkzPHUcZca3dU7aC0L%2BBwceP23G6gdyH4QtgGWnBuF1vJDdXHyEHcifcRQ9sUYE%2FEJJcn2Cp6AP4UALe3fMnjFeucwYOl4uq5rD5gTys9xiSvpDSfNuEa0E3zcuXZuqrxnrnJx5LhNYDzkrWJ0mcQ9HBvyrIkrBnDP824g2IqITmlVqKhYO1QjzcSOu1lFKn8hLBHq6LPQjxdn03Qa7QNVOSSoII0Q%2FtgidK9bLPOZmM%2FgzoHzkoPtmh6muwgMM0Z%2FDPsloL5yE3aUr0ZjfEuWiLXCtXdsaokDXJ7ZDK958RtSK9sn%2Bo9jrdaR9kpI8gDFo5d0Y9sddKQdmM94Jy%2FGhRZju9aAPf2lB1X77ebPC2YXlqhfzClTGVvoX23NW4sEZWETVciyFPnD0cT8RertfVTHgp4TfxuBwadOphGNeBFdwIq7%2B9pQc4besk7syH%2B%2B3CURAVy9pnlp98H1GOdN6j2FTceGEcl1EtKsUmSSgtEfoqTqGht3VtBKSYPfKDkhq9lLDCfJLOFLe%2FnrONChxDk2d5dpfJrR0hSf8Cl4wk82KvQY6pgFO5vVjYZ4w2XFIam7Btz1CGA93TaBnT9YxmPD6tNeHbiZh6Ua46OJAPCRLJp0%2BTn%2B%2FDAWa%2BLbD5ISbXFJtpYcZ19JVya1KEntbxZAx6sd3RXggzjPhxchpn65GZkSjWLYff1GjRNJ%2FdnRPuQVxWNPFgZH%2BfDPt6u5l9EVEc7ui8VQK23Ny4Ztep5KLcDUrIAw9CnKyKJoHTTTcScMrNUbtwkLb2kFk&X-Amz-Signature=b12b2f70601dbb9822b4f67f2c4c8279c7ae794b1ca5b1c8e4613674e763630a&X-Amz-SignedHeaders=host&x-id=GetObject)
**Explanation:** When highway miles per gallon increases, the price of the vehicle tends to decrease. This negative correlation suggests that cars with higher fuel efficiency (more miles per gallon) are generally priced lower in the market.
___
### Weak Correlation
Weak correlation indicates a lack of strong relationship between the variables.
**Example: RPM and Price**
- **Weak Correlation:** Low and high RPM values show varied prices, indicating no strong predictive relationship.
- **Visualization:** Scatter plot with no clear trend or slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9f914514-8914-4bf4-ac84-d9e3077f6eb1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663PSXINK6%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T010927Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECAaCXVzLXdlc3QtMiJHMEUCIQDeIRYTdbFj2Cq7G6YmsDsz2sc5nIXcgXK1KD1lmUqd%2BQIgCv05uL73djvLcm0hqTSzmtF0QRmsKWlXlx8zJLmC%2Bi0q%2FwMIORAAGgw2Mzc0MjMxODM4MDUiDBGO7Em9SOrs7IHAbircA3SbD42ckLQISEQXIqdDuljJEn%2BRzcWhisqc8T6dO1lFReTlU%2BgJ188E8VUJX8OZmsIbgl1Kw%2BEofze4%2BDbX3tnDEt13vrzL1M0smLsUcLWEng2y5juDYj7zG5looTuPtsqIKP16y6VEsdCGT%2BDOGO0nwM86GDJCHU98lbAOZVAASuQ8Sfr3SQIZS5rKIiKfyXm23PWkz%2FqdyM%2FflNf52kize6nzf9GL4FZWaMV7HBGRdusQ0VTZ38RhyrcXwvDKHxsSakWpU58%2Bh%2BHsUCAVIeimQX1cyCcjtMlRYNLWDwzMLj4kl6Vud1elFAfpj2pMeaeN95rJB74SxrIjCquRn3%2FO36%2FcSoVwufva9tqfPXzcCYIINhgdjlJqPP5D4sd6S51O0G7Uudbo2n7rElcjxyTPguKWgR4pKLFIYXjp0QP9ve6SZ5L5Ls0rZYfCAZxNELmgQqcQuclDkKZLwFDIehJ4u%2FqzjCcNnXsmVBPu1WVpAQjKWIFpUI0sZztDymsI397cN2hy59UDezROGc9oYOaZ8ZHeQVMjZN%2FV2YdV9m9%2BPP3cnI0qMHzv3DsJ7OEEzWmpSDswv%2F0%2BddupZrfiFyQ3B%2BaqcTgOgECosQxiJCaQQSvAJqx8gZdYGKVKMPnMir0GOqUBTAOsUYvevl5j9NDdJFbSGLIigGVsaCz3udGpMg8zMiET9eSPmQufTOHuG8OWQyxhNyuNBz29GAmzRG8AzEqaEMEMrDJDfHGdXMiHcY60GLeDxNKlHIFca%2FH5n96exICCQ2jwjsfLm2HvQCAKxHcJqAFlDXcswNTjs%2F02XNs8m7VEmD5l2apU72r2Vq4F4XD8fqo2pART220UXPuQaQA1uhqZ4vcl&X-Amz-Signature=1328da6b30d843439aec28b17393d866b6faef4155da65f15937c4dce571672f&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f18086e5-5b04-4fbf-8309-8944ab20d213/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466S4NZBMW4%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T010926Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECAaCXVzLXdlc3QtMiJGMEQCIC8gv5EImbE%2Bcadod2UUtIhbafEvB%2FsfySpHYKiusYgZAiA5UYbQTsU7ABvqbjfdyWJsjTsCX9VKN%2F0wIOQI6oQMmSr%2FAwg5EAAaDDYzNzQyMzE4MzgwNSIMqcsYokoReMWScCpiKtwDfkhoIi%2BltXkdvu3ByEhHoH%2BoIk4oRzyjw4GsMzTPLoa7oJ6EE9K9oP2wVfygYD4BEJk26m4WfS7YuYjeDHghcGDlxGpPG9DzOp9jENa7vD9VQ7tLliydhihpLo1OqwKqB6oEvsg%2B%2FH3RixJ%2Bd5MBm4pmsJ9S2zg0h7KO29BsRf5ZQUFP8xE2yTh8tLOpmM5F6f%2BvdaDjX80pnr1rucS21tdAIg0mOc8Ca1uvrIfBiwXcPHl7J4T4bE0TJ%2BK7Rk37m6%2FqdHXPxjXmbF26d8lQm1OSBLs5PRFbR70CL33lIEsm8cBtnwDbQXVGf8qMhDzdd69%2Fah%2FUKl2I1NZ%2B5496RCgGIMmeF8aU2J1ZmaOAr04MNR5yL9zply3OfTh9bGKgXTxpg0odh0DjtkGRZImr3xfpU7jtFet0b0UekttuffI17O5rIS5Co4ikIURyRXo5CANVMMB%2Fjvt%2FFNuitRksx8ACPnAtETpwIlX7PIsqcl3QYb%2FkuRkx2csHKmEUKnfpe2IR6rimMEwi1uuVBMqXVIHfdpH1PdZJWQjJYcluMJtTWrOW6CVNh7ga7%2FEdZT8M8pn3%2FAa5ajKKIPs20YYD%2BMZyPAziJMzDR4cckJ9VREqNciGIaEv85SK2ImYwoM2KvQY6pgHyZqSQbP3KXcYQecvtFfAw9vgx%2Bag396pHM8KhEqoxIIuEnWE862nHTAjPgtxQ%2BZcwIGzou9kjczZH2Q61vag6xndXQXsFAlsHPPVuwF0ENwZk3uMSqvyZVc8kfgf4vAIzE6SpW0b1faES9lJVekrZgPWrUwAcuJziDm2OnCVAbjfQXUK9HwcehK7k3HUA7eUMqtfSbuCmRqxLP74%2Fpf%2FeWYTzdQB%2B&X-Amz-Signature=e532964c02bf4f03efa7e6c1a0c04dbe5a2bd77b5db6bb69ee90e2d9d9131ef8&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Correlation Plot
Heatmap visualizes correlations among variables. Color scheme indicates Pearson correlation coefficients. Dark red diagonal line shows perfect correlation (value of 1) between variables and themselves.
This heatmap offers overview of variable relationships and their link with price.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cd3b341e-cc1a-45f7-8aec-cdc00436d270/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466S4NZBMW4%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T010926Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECAaCXVzLXdlc3QtMiJGMEQCIC8gv5EImbE%2Bcadod2UUtIhbafEvB%2FsfySpHYKiusYgZAiA5UYbQTsU7ABvqbjfdyWJsjTsCX9VKN%2F0wIOQI6oQMmSr%2FAwg5EAAaDDYzNzQyMzE4MzgwNSIMqcsYokoReMWScCpiKtwDfkhoIi%2BltXkdvu3ByEhHoH%2BoIk4oRzyjw4GsMzTPLoa7oJ6EE9K9oP2wVfygYD4BEJk26m4WfS7YuYjeDHghcGDlxGpPG9DzOp9jENa7vD9VQ7tLliydhihpLo1OqwKqB6oEvsg%2B%2FH3RixJ%2Bd5MBm4pmsJ9S2zg0h7KO29BsRf5ZQUFP8xE2yTh8tLOpmM5F6f%2BvdaDjX80pnr1rucS21tdAIg0mOc8Ca1uvrIfBiwXcPHl7J4T4bE0TJ%2BK7Rk37m6%2FqdHXPxjXmbF26d8lQm1OSBLs5PRFbR70CL33lIEsm8cBtnwDbQXVGf8qMhDzdd69%2Fah%2FUKl2I1NZ%2B5496RCgGIMmeF8aU2J1ZmaOAr04MNR5yL9zply3OfTh9bGKgXTxpg0odh0DjtkGRZImr3xfpU7jtFet0b0UekttuffI17O5rIS5Co4ikIURyRXo5CANVMMB%2Fjvt%2FFNuitRksx8ACPnAtETpwIlX7PIsqcl3QYb%2FkuRkx2csHKmEUKnfpe2IR6rimMEwi1uuVBMqXVIHfdpH1PdZJWQjJYcluMJtTWrOW6CVNh7ga7%2FEdZT8M8pn3%2FAa5ajKKIPs20YYD%2BMZyPAziJMzDR4cckJ9VREqNciGIaEv85SK2ImYwoM2KvQY6pgHyZqSQbP3KXcYQecvtFfAw9vgx%2Bag396pHM8KhEqoxIIuEnWE862nHTAjPgtxQ%2BZcwIGzou9kjczZH2Q61vag6xndXQXsFAlsHPPVuwF0ENwZk3uMSqvyZVc8kfgf4vAIzE6SpW0b1faES9lJVekrZgPWrUwAcuJziDm2OnCVAbjfQXUK9HwcehK7k3HUA7eUMqtfSbuCmRqxLP74%2Fpf%2FeWYTzdQB%2B&X-Amz-Signature=2285a52d665e9bb071920e011deaf80212109ecefe15b31f7331a21fc706693d&X-Amz-SignedHeaders=host&x-id=GetObject)

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
