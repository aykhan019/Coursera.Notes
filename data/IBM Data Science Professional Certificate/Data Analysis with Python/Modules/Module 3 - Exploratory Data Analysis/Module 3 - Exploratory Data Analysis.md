

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7e6d594d-952e-44b6-97ea-31225882aea6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663RVLFT2I%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T161554Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIEgBMb7mQmz4qD7YEsdp78A9w1WCroC6EoKro76tXJ6zAiEA4btLYeY%2Bemg2BxHo%2Brz2ht%2BrC0RedP72TRBTnwrUuyYqiAQI1%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFOmCpkOab1wlwWe0CrcAyfEQ5YIfn0ojPsi2jAmiRhJ8GLyNbbtLRMFgIYyIiYiFd4D3Hmtx4oDK%2B8QEIfCTOS%2Fr4f51ns3jXn%2FXeWAroVrzOmLbrOd3AsXxzVrNL59vnsagGaWNdb%2BSKKYJ6XFbtbwQzZo5ZszMRpZlhKdJeBUdL3vut1c5kAcGZLQqNcyn%2BZqRxbYGpZGgSjzoVcPifo4x1pG4F3SEjE50gZaiLuRK%2F2lKCjy08cw7kBneXgpDqHyD6MLChHtAHwyjo7jXkovJTt6YHMMm6bpqwKRkHMHsMI9zLzdIy5LcyQOe5JnsNYqQklawu97B8AFB765tDc7ysRqrhUmc0qrMCuByaBX5xRL%2BhvvDlWC%2FHg%2FlxqC23BOU6lWRmBO9U3zkJ15WUAnTSBFplud%2Foc6dIQ0KmbPS83QlfK2N6MX%2BzSLQqkgb%2BD549ExrY1TFj%2BpokHY8xSxv81GYrRKsq5eKvKFwS2FzQTTFGBfKnuvCBI2ae5RAEzDBgWLmtcHRNur6%2Fe8y7fRDku%2BjBLN043%2BKKcB3RevYwfmu94iEeGy18ZnBiG%2FIMjSVb04dzOcsLRea18Iihsg7jEoYhOcWM%2FbL9NVQ9ilBr4M3h15UdUWNFCULVBJFRHQ%2FImHSpP5Cl4MMKvE%2BLwGOqUBxL7KC78K7kCQdIlI7rboIbJ7ZfJaknWvHel9ne3RVs7J%2BvpAAuOeY2PEPB0yxD4Pbhu2Y3o9SqoiIfUGJMquGavFuKP7C2Hfm6ucgUDP%2B%2BO6eWRG8f4Xw%2FTdhMY5tkG2JEViFVqaA2eZRcLbkqMb9OpuDwjsktcR5zsS0Ol%2FPLr8DpLStUo6VPNNudIgdu85gv6ac4gyuSLEBAtZXJ5cUEHDVLTA&X-Amz-Signature=8ee86f9214dbce02562c8727dd87ef320ea73d00ecc351ac7a9357d473c09f62&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cbfaed9e-b398-4902-8936-dea058b21def/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663RVLFT2I%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T161554Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIEgBMb7mQmz4qD7YEsdp78A9w1WCroC6EoKro76tXJ6zAiEA4btLYeY%2Bemg2BxHo%2Brz2ht%2BrC0RedP72TRBTnwrUuyYqiAQI1%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFOmCpkOab1wlwWe0CrcAyfEQ5YIfn0ojPsi2jAmiRhJ8GLyNbbtLRMFgIYyIiYiFd4D3Hmtx4oDK%2B8QEIfCTOS%2Fr4f51ns3jXn%2FXeWAroVrzOmLbrOd3AsXxzVrNL59vnsagGaWNdb%2BSKKYJ6XFbtbwQzZo5ZszMRpZlhKdJeBUdL3vut1c5kAcGZLQqNcyn%2BZqRxbYGpZGgSjzoVcPifo4x1pG4F3SEjE50gZaiLuRK%2F2lKCjy08cw7kBneXgpDqHyD6MLChHtAHwyjo7jXkovJTt6YHMMm6bpqwKRkHMHsMI9zLzdIy5LcyQOe5JnsNYqQklawu97B8AFB765tDc7ysRqrhUmc0qrMCuByaBX5xRL%2BhvvDlWC%2FHg%2FlxqC23BOU6lWRmBO9U3zkJ15WUAnTSBFplud%2Foc6dIQ0KmbPS83QlfK2N6MX%2BzSLQqkgb%2BD549ExrY1TFj%2BpokHY8xSxv81GYrRKsq5eKvKFwS2FzQTTFGBfKnuvCBI2ae5RAEzDBgWLmtcHRNur6%2Fe8y7fRDku%2BjBLN043%2BKKcB3RevYwfmu94iEeGy18ZnBiG%2FIMjSVb04dzOcsLRea18Iihsg7jEoYhOcWM%2FbL9NVQ9ilBr4M3h15UdUWNFCULVBJFRHQ%2FImHSpP5Cl4MMKvE%2BLwGOqUBxL7KC78K7kCQdIlI7rboIbJ7ZfJaknWvHel9ne3RVs7J%2BvpAAuOeY2PEPB0yxD4Pbhu2Y3o9SqoiIfUGJMquGavFuKP7C2Hfm6ucgUDP%2B%2BO6eWRG8f4Xw%2FTdhMY5tkG2JEViFVqaA2eZRcLbkqMb9OpuDwjsktcR5zsS0Ol%2FPLr8DpLStUo6VPNNudIgdu85gv6ac4gyuSLEBAtZXJ5cUEHDVLTA&X-Amz-Signature=0ecc2da76015ce44fb9180bf0fc15e2ba0bbf53452203ad7036e44de792efc5b&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/91181646-b1e0-4433-9711-6259a96a9247/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663RVLFT2I%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T161554Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIEgBMb7mQmz4qD7YEsdp78A9w1WCroC6EoKro76tXJ6zAiEA4btLYeY%2Bemg2BxHo%2Brz2ht%2BrC0RedP72TRBTnwrUuyYqiAQI1%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFOmCpkOab1wlwWe0CrcAyfEQ5YIfn0ojPsi2jAmiRhJ8GLyNbbtLRMFgIYyIiYiFd4D3Hmtx4oDK%2B8QEIfCTOS%2Fr4f51ns3jXn%2FXeWAroVrzOmLbrOd3AsXxzVrNL59vnsagGaWNdb%2BSKKYJ6XFbtbwQzZo5ZszMRpZlhKdJeBUdL3vut1c5kAcGZLQqNcyn%2BZqRxbYGpZGgSjzoVcPifo4x1pG4F3SEjE50gZaiLuRK%2F2lKCjy08cw7kBneXgpDqHyD6MLChHtAHwyjo7jXkovJTt6YHMMm6bpqwKRkHMHsMI9zLzdIy5LcyQOe5JnsNYqQklawu97B8AFB765tDc7ysRqrhUmc0qrMCuByaBX5xRL%2BhvvDlWC%2FHg%2FlxqC23BOU6lWRmBO9U3zkJ15WUAnTSBFplud%2Foc6dIQ0KmbPS83QlfK2N6MX%2BzSLQqkgb%2BD549ExrY1TFj%2BpokHY8xSxv81GYrRKsq5eKvKFwS2FzQTTFGBfKnuvCBI2ae5RAEzDBgWLmtcHRNur6%2Fe8y7fRDku%2BjBLN043%2BKKcB3RevYwfmu94iEeGy18ZnBiG%2FIMjSVb04dzOcsLRea18Iihsg7jEoYhOcWM%2FbL9NVQ9ilBr4M3h15UdUWNFCULVBJFRHQ%2FImHSpP5Cl4MMKvE%2BLwGOqUBxL7KC78K7kCQdIlI7rboIbJ7ZfJaknWvHel9ne3RVs7J%2BvpAAuOeY2PEPB0yxD4Pbhu2Y3o9SqoiIfUGJMquGavFuKP7C2Hfm6ucgUDP%2B%2BO6eWRG8f4Xw%2FTdhMY5tkG2JEViFVqaA2eZRcLbkqMb9OpuDwjsktcR5zsS0Ol%2FPLr8DpLStUo6VPNNudIgdu85gv6ac4gyuSLEBAtZXJ5cUEHDVLTA&X-Amz-Signature=7128314c7ef542e68384ae92fddeaf356e60ef2216a58a17be841337facd1ad0&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/09aba1c0-0d55-41dd-852a-a04c5b8a3fac/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46665NKZ6IV%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T161555Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGF94CUXcUTAMJHDuuv2KSUaLM0orEQOZRrAV4ALR2muAiBE%2FaifUxe6ijR6K8JVbRhHjo%2BoC9wrJYmBtUFJRQ%2FLMCqIBAjX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMHB5O5ahcHe9tHlk%2FKtwDigl%2ByBOxL1EXS3ml92tWxVGVK7WF9XKIHsz6lgaJhyEBJqXYEONgrBoEM%2B6a5vi%2FeAKGib8QuKFv0B49cmW7vUPYik7nZM%2FMSSbHgFLWgLQJPUtSxXTP6k11MqwIFKTs8dioPqigBIDPdZjFJymeCYuE57A9Cakh19tctpA8fGrUvm9d3FyhRTIn89E7woxn%2BpnItHOx4KdPcQPXtRp7vlt3Rn0DayGGfr%2Bc9NNhuB53vb1eZWPAZa0Gcu5n%2FrkaTI6%2Fv%2FwaO19OA9IwHdXKxwwC9KCevjahT58BeKqqsYx%2FEzoqUgNHzemqaF%2BM%2FQT1wiLN8SSsLcGhokBb7aVt10lvGGr1SX%2Fs1tckWtAM1DmkoHrIgd18%2FF74AdLCHZ%2FOn1D9BfXul%2FYAfTtxqz67JJ6AA3zC4k6%2BcTiEYe3JSpfjQP0SFwRt%2BPwCBbV0bG4kUcUqDdTcOEecvNMcVUWHDONtasFoWk%2F5O5q5rfE1yLaaOJhGjZs7e5EnZiHhIX6dILmn7iYnNNck60LFWS3KD71gZqpexBsSsZ6av9i7tebYfDs9nKdxCzZhy82oPjIoW4x4lnf40dPB8Q4Oxn%2BJ%2FRVFYijR2ltvSdh0WxGEWNYjMiL8TmVUCmR%2BFw8w%2Bcr4vAY6pgEHy%2BwwOHtjahLK%2FImOK8%2FVbgMmj0OMFfetfy0pVlSVdEo9WLufQ1kQrtuXQd7KHA5%2BedqhA4kBKUSxgEo4onYBwFm%2BRI5TWkrz4N9IaI6eJmdXbVY8yiHNKty3ERvSGdTckD%2FkjD1gcq3BhdJsRCs1YN22X2gffU4u%2BysAhBHL8HHJEtlLcd1MLm0Y1eYPQxoMh2FN2fPUE8Q66fjJ7TVgQv3eASeX&X-Amz-Signature=3c401afa5099ecd972b9f7594d8d6de836cdcdae38a95a60316e0647832a8ed6&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 2. Scatter Plot
Scatter plots present the relationship between two variables in a dataset. It represents data points on a two-dimensional plane. The independent variable or attribute is plotted on the X-axis, while the dependent variable is plotted on the Y-axis.
**Syntax:**
```python
plt.scatter(x, y)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23708af9-659f-4f23-b626-1a4292d7842c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46665NKZ6IV%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T161555Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGF94CUXcUTAMJHDuuv2KSUaLM0orEQOZRrAV4ALR2muAiBE%2FaifUxe6ijR6K8JVbRhHjo%2BoC9wrJYmBtUFJRQ%2FLMCqIBAjX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMHB5O5ahcHe9tHlk%2FKtwDigl%2ByBOxL1EXS3ml92tWxVGVK7WF9XKIHsz6lgaJhyEBJqXYEONgrBoEM%2B6a5vi%2FeAKGib8QuKFv0B49cmW7vUPYik7nZM%2FMSSbHgFLWgLQJPUtSxXTP6k11MqwIFKTs8dioPqigBIDPdZjFJymeCYuE57A9Cakh19tctpA8fGrUvm9d3FyhRTIn89E7woxn%2BpnItHOx4KdPcQPXtRp7vlt3Rn0DayGGfr%2Bc9NNhuB53vb1eZWPAZa0Gcu5n%2FrkaTI6%2Fv%2FwaO19OA9IwHdXKxwwC9KCevjahT58BeKqqsYx%2FEzoqUgNHzemqaF%2BM%2FQT1wiLN8SSsLcGhokBb7aVt10lvGGr1SX%2Fs1tckWtAM1DmkoHrIgd18%2FF74AdLCHZ%2FOn1D9BfXul%2FYAfTtxqz67JJ6AA3zC4k6%2BcTiEYe3JSpfjQP0SFwRt%2BPwCBbV0bG4kUcUqDdTcOEecvNMcVUWHDONtasFoWk%2F5O5q5rfE1yLaaOJhGjZs7e5EnZiHhIX6dILmn7iYnNNck60LFWS3KD71gZqpexBsSsZ6av9i7tebYfDs9nKdxCzZhy82oPjIoW4x4lnf40dPB8Q4Oxn%2BJ%2FRVFYijR2ltvSdh0WxGEWNYjMiL8TmVUCmR%2BFw8w%2Bcr4vAY6pgEHy%2BwwOHtjahLK%2FImOK8%2FVbgMmj0OMFfetfy0pVlSVdEo9WLufQ1kQrtuXQd7KHA5%2BedqhA4kBKUSxgEo4onYBwFm%2BRI5TWkrz4N9IaI6eJmdXbVY8yiHNKty3ERvSGdTckD%2FkjD1gcq3BhdJsRCs1YN22X2gffU4u%2BysAhBHL8HHJEtlLcd1MLm0Y1eYPQxoMh2FN2fPUE8Q66fjJ7TVgQv3eASeX&X-Amz-Signature=acadee195ed4c1b23cb4a0e8a13824d16ff482147051d114dba59d7f678cbf4f&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 3. Histogram
A histogram is an important visual representation of data in categorical form. To view the data in a "Binned" form, use the histogram plot with a number of bins required or with the data points that mark the bin edges. The x-axis represents the data bins, and the y-axis represents the number of elements in each bin.
**Syntax:**
```python
plt.hist(x, bins)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/24e4424a-df87-40a1-b63b-195cbdc2e0ab/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46665NKZ6IV%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T161555Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGF94CUXcUTAMJHDuuv2KSUaLM0orEQOZRrAV4ALR2muAiBE%2FaifUxe6ijR6K8JVbRhHjo%2BoC9wrJYmBtUFJRQ%2FLMCqIBAjX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMHB5O5ahcHe9tHlk%2FKtwDigl%2ByBOxL1EXS3ml92tWxVGVK7WF9XKIHsz6lgaJhyEBJqXYEONgrBoEM%2B6a5vi%2FeAKGib8QuKFv0B49cmW7vUPYik7nZM%2FMSSbHgFLWgLQJPUtSxXTP6k11MqwIFKTs8dioPqigBIDPdZjFJymeCYuE57A9Cakh19tctpA8fGrUvm9d3FyhRTIn89E7woxn%2BpnItHOx4KdPcQPXtRp7vlt3Rn0DayGGfr%2Bc9NNhuB53vb1eZWPAZa0Gcu5n%2FrkaTI6%2Fv%2FwaO19OA9IwHdXKxwwC9KCevjahT58BeKqqsYx%2FEzoqUgNHzemqaF%2BM%2FQT1wiLN8SSsLcGhokBb7aVt10lvGGr1SX%2Fs1tckWtAM1DmkoHrIgd18%2FF74AdLCHZ%2FOn1D9BfXul%2FYAfTtxqz67JJ6AA3zC4k6%2BcTiEYe3JSpfjQP0SFwRt%2BPwCBbV0bG4kUcUqDdTcOEecvNMcVUWHDONtasFoWk%2F5O5q5rfE1yLaaOJhGjZs7e5EnZiHhIX6dILmn7iYnNNck60LFWS3KD71gZqpexBsSsZ6av9i7tebYfDs9nKdxCzZhy82oPjIoW4x4lnf40dPB8Q4Oxn%2BJ%2FRVFYijR2ltvSdh0WxGEWNYjMiL8TmVUCmR%2BFw8w%2Bcr4vAY6pgEHy%2BwwOHtjahLK%2FImOK8%2FVbgMmj0OMFfetfy0pVlSVdEo9WLufQ1kQrtuXQd7KHA5%2BedqhA4kBKUSxgEo4onYBwFm%2BRI5TWkrz4N9IaI6eJmdXbVY8yiHNKty3ERvSGdTckD%2FkjD1gcq3BhdJsRCs1YN22X2gffU4u%2BysAhBHL8HHJEtlLcd1MLm0Y1eYPQxoMh2FN2fPUE8Q66fjJ7TVgQv3eASeX&X-Amz-Signature=dd0e5a87ac1bec4c2dc0dd33880282315fe9ed6026b89dc68292bb4f4a624403&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ab5a6dfe-51f5-43ee-bcb3-33dae4a1c7ad/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46665NKZ6IV%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T161555Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGF94CUXcUTAMJHDuuv2KSUaLM0orEQOZRrAV4ALR2muAiBE%2FaifUxe6ijR6K8JVbRhHjo%2BoC9wrJYmBtUFJRQ%2FLMCqIBAjX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMHB5O5ahcHe9tHlk%2FKtwDigl%2ByBOxL1EXS3ml92tWxVGVK7WF9XKIHsz6lgaJhyEBJqXYEONgrBoEM%2B6a5vi%2FeAKGib8QuKFv0B49cmW7vUPYik7nZM%2FMSSbHgFLWgLQJPUtSxXTP6k11MqwIFKTs8dioPqigBIDPdZjFJymeCYuE57A9Cakh19tctpA8fGrUvm9d3FyhRTIn89E7woxn%2BpnItHOx4KdPcQPXtRp7vlt3Rn0DayGGfr%2Bc9NNhuB53vb1eZWPAZa0Gcu5n%2FrkaTI6%2Fv%2FwaO19OA9IwHdXKxwwC9KCevjahT58BeKqqsYx%2FEzoqUgNHzemqaF%2BM%2FQT1wiLN8SSsLcGhokBb7aVt10lvGGr1SX%2Fs1tckWtAM1DmkoHrIgd18%2FF74AdLCHZ%2FOn1D9BfXul%2FYAfTtxqz67JJ6AA3zC4k6%2BcTiEYe3JSpfjQP0SFwRt%2BPwCBbV0bG4kUcUqDdTcOEecvNMcVUWHDONtasFoWk%2F5O5q5rfE1yLaaOJhGjZs7e5EnZiHhIX6dILmn7iYnNNck60LFWS3KD71gZqpexBsSsZ6av9i7tebYfDs9nKdxCzZhy82oPjIoW4x4lnf40dPB8Q4Oxn%2BJ%2FRVFYijR2ltvSdh0WxGEWNYjMiL8TmVUCmR%2BFw8w%2Bcr4vAY6pgEHy%2BwwOHtjahLK%2FImOK8%2FVbgMmj0OMFfetfy0pVlSVdEo9WLufQ1kQrtuXQd7KHA5%2BedqhA4kBKUSxgEo4onYBwFm%2BRI5TWkrz4N9IaI6eJmdXbVY8yiHNKty3ERvSGdTckD%2FkjD1gcq3BhdJsRCs1YN22X2gffU4u%2BysAhBHL8HHJEtlLcd1MLm0Y1eYPQxoMh2FN2fPUE8Q66fjJ7TVgQv3eASeX&X-Amz-Signature=7ead46353038b465c38571dc57ae9e45e21a33cd3a8d5cdb0059f0b52550e765&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8f1b1d60-cf1b-42b3-9faa-f634c89c3f84/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46665NKZ6IV%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T161555Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGF94CUXcUTAMJHDuuv2KSUaLM0orEQOZRrAV4ALR2muAiBE%2FaifUxe6ijR6K8JVbRhHjo%2BoC9wrJYmBtUFJRQ%2FLMCqIBAjX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMHB5O5ahcHe9tHlk%2FKtwDigl%2ByBOxL1EXS3ml92tWxVGVK7WF9XKIHsz6lgaJhyEBJqXYEONgrBoEM%2B6a5vi%2FeAKGib8QuKFv0B49cmW7vUPYik7nZM%2FMSSbHgFLWgLQJPUtSxXTP6k11MqwIFKTs8dioPqigBIDPdZjFJymeCYuE57A9Cakh19tctpA8fGrUvm9d3FyhRTIn89E7woxn%2BpnItHOx4KdPcQPXtRp7vlt3Rn0DayGGfr%2Bc9NNhuB53vb1eZWPAZa0Gcu5n%2FrkaTI6%2Fv%2FwaO19OA9IwHdXKxwwC9KCevjahT58BeKqqsYx%2FEzoqUgNHzemqaF%2BM%2FQT1wiLN8SSsLcGhokBb7aVt10lvGGr1SX%2Fs1tckWtAM1DmkoHrIgd18%2FF74AdLCHZ%2FOn1D9BfXul%2FYAfTtxqz67JJ6AA3zC4k6%2BcTiEYe3JSpfjQP0SFwRt%2BPwCBbV0bG4kUcUqDdTcOEecvNMcVUWHDONtasFoWk%2F5O5q5rfE1yLaaOJhGjZs7e5EnZiHhIX6dILmn7iYnNNck60LFWS3KD71gZqpexBsSsZ6av9i7tebYfDs9nKdxCzZhy82oPjIoW4x4lnf40dPB8Q4Oxn%2BJ%2FRVFYijR2ltvSdh0WxGEWNYjMiL8TmVUCmR%2BFw8w%2Bcr4vAY6pgEHy%2BwwOHtjahLK%2FImOK8%2FVbgMmj0OMFfetfy0pVlSVdEo9WLufQ1kQrtuXQd7KHA5%2BedqhA4kBKUSxgEo4onYBwFm%2BRI5TWkrz4N9IaI6eJmdXbVY8yiHNKty3ERvSGdTckD%2FkjD1gcq3BhdJsRCs1YN22X2gffU4u%2BysAhBHL8HHJEtlLcd1MLm0Y1eYPQxoMh2FN2fPUE8Q66fjJ7TVgQv3eASeX&X-Amz-Signature=146581dc924e84efe5ece1a20d57e2f4b72e8f5a68ae0832b3e628183267c6cb&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/13ad0497-05fe-4eaa-984e-707b33e14761/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46665NKZ6IV%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T161555Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGF94CUXcUTAMJHDuuv2KSUaLM0orEQOZRrAV4ALR2muAiBE%2FaifUxe6ijR6K8JVbRhHjo%2BoC9wrJYmBtUFJRQ%2FLMCqIBAjX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMHB5O5ahcHe9tHlk%2FKtwDigl%2ByBOxL1EXS3ml92tWxVGVK7WF9XKIHsz6lgaJhyEBJqXYEONgrBoEM%2B6a5vi%2FeAKGib8QuKFv0B49cmW7vUPYik7nZM%2FMSSbHgFLWgLQJPUtSxXTP6k11MqwIFKTs8dioPqigBIDPdZjFJymeCYuE57A9Cakh19tctpA8fGrUvm9d3FyhRTIn89E7woxn%2BpnItHOx4KdPcQPXtRp7vlt3Rn0DayGGfr%2Bc9NNhuB53vb1eZWPAZa0Gcu5n%2FrkaTI6%2Fv%2FwaO19OA9IwHdXKxwwC9KCevjahT58BeKqqsYx%2FEzoqUgNHzemqaF%2BM%2FQT1wiLN8SSsLcGhokBb7aVt10lvGGr1SX%2Fs1tckWtAM1DmkoHrIgd18%2FF74AdLCHZ%2FOn1D9BfXul%2FYAfTtxqz67JJ6AA3zC4k6%2BcTiEYe3JSpfjQP0SFwRt%2BPwCBbV0bG4kUcUqDdTcOEecvNMcVUWHDONtasFoWk%2F5O5q5rfE1yLaaOJhGjZs7e5EnZiHhIX6dILmn7iYnNNck60LFWS3KD71gZqpexBsSsZ6av9i7tebYfDs9nKdxCzZhy82oPjIoW4x4lnf40dPB8Q4Oxn%2BJ%2FRVFYijR2ltvSdh0WxGEWNYjMiL8TmVUCmR%2BFw8w%2Bcr4vAY6pgEHy%2BwwOHtjahLK%2FImOK8%2FVbgMmj0OMFfetfy0pVlSVdEo9WLufQ1kQrtuXQd7KHA5%2BedqhA4kBKUSxgEo4onYBwFm%2BRI5TWkrz4N9IaI6eJmdXbVY8yiHNKty3ERvSGdTckD%2FkjD1gcq3BhdJsRCs1YN22X2gffU4u%2BysAhBHL8HHJEtlLcd1MLm0Y1eYPQxoMh2FN2fPUE8Q66fjJ7TVgQv3eASeX&X-Amz-Signature=bc7e64fd2b6868a7591b490f1d22e61f859b29803419df2d196752438c3d9b55&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 2. Box and Whisker Plot
A box plot shows the distribution of quantitative data in a way that facilitates comparisons between variables or across levels of a categorical variable. The box shows the quartiles of the dataset while the whiskers extend to show the rest of the distribution, except for points that are determined to be "outliers".
**Syntax:**
```python
sns.boxplot(x='header_1', y='header_2', data=df)
```
**Example Output:**


![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d207ae92-0a7c-4e2f-aa65-0ee5a2c33bf7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XDPVLUUZ%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T161557Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDo6Lc84PUHS4bo%2F%2BU4Gz%2BNi87f%2FcUsn85RNppmikG5YwIhAIz9kYc2AM2YCkUqkW28DuAhDPDUCinqB4fR04S4903%2FKogECNf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwmO%2BUP6aEP60XpFBUq3AMGi4L%2BeSVlHz4Kl5Nh7VKvR47a2QnT8I7rN6RcfrpjdRLoJVteCXFdlq74FuhxoEVmGrs5tArBAfoXdrkxDZ8H30Xk9ZEm1%2BwkAzJ9K%2BzxqDs3j0OAYMLuF8rteVieLWBwXzMP%2FFEJqFQpkvBKj%2FqSXol7SH0QdEe4yTEuwXRfHNnfL0xN3rxDhWqyQp87TDqf9MOUt1vQk2MkpG6zYdXebk%2FLkjEUdigqkKpdTDadi6vWs%2BqpFXF3Lm5Ekl3nwDtc8%2FRQYGDuoRhcze031PSMlhnV0ELGPhbtB2NdKVTVpXRVAhbp1hI0rDGqt%2FecLeRg9V7WG75K043xzoPifmk2EMRpudKZ6J4IzvQjkHCUeC3tl02Gz9sodt8wh6LC4z8mpmtDK0QB6yBHYa2y1M6MOyefswlUdOaN1tc4QwweSa6qk%2Fo2EkQfh2bt15AHibrA1ZpkBMttyb4TnqpZOYYQjJNyAGor9PNKVSaNB7pep4vL5zwMx%2BjqRPzATfpuzs%2Fia9%2FcRmVMvPjPwfg7T1QzXg6U%2Barh61jVWJTfIMeroHTGYEZtId%2B46kPdq2uGZiHFmfxqniBFmGotIyKYIB6s6YCn8k7MohUjo6xAErsbJ5QE2x42J2ynOxW%2FsjCrxvi8BjqkAdGlidrZt9htyZF1%2FBFQrrKk0cmlsDsAxXQF8SC40ELx6KAjrHCoYWhyjSsyJztp0Dp6KNuKNS8XmtXSKBreQWmENAAMiYOIJjNepxyN3B1X%2FYbseOflF%2FlCP46v50z4IxvxGymKn8%2BN2NncRSaSBinDjZaWtYVAxTVBy2mNo8dpQT56EFfuAz8q%2BxmWU7%2FZSqhrMaS3ZS0soljgbNyG%2BSU7ZcII&X-Amz-Signature=f211d477b8966588581ef9f08561fcbf4a3c3ee117de37417fba2bd834c6fc5d&X-Amz-SignedHeaders=host&x-id=GetObject)

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0e516edc-7551-4792-ab18-0494db3c4c0c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YDOGRH35%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T161556Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDa2O0ZvF2TBjOaAzQNjg4s4FKiTRewheN6mfpZoKOiPAiEAwg%2Fc5wbsMfL8rVQjhUnFF5jmpbF3loWvcT6Btro19mQqiAQI1%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDETiyV5uoy4QUIZkICrcA46w15BeXvfgm0GeB64sfVC89kBwcTFSiECvC0TMp7Q4THJy1jo9DIrDt96yKmwcmPxgMUpKDMP%2FqZiZpYHQxFviKw5HY4neQ%2FUQWjBnHrUsiIWJLQXaztySumItUCS9iJ%2FgJ2Hse%2FpAAsRe7EjFvTXoTFc%2BfLYsCI7%2FKQdqoARPmD4R%2BC1VTUJp%2BNBijwuQZNJa7NJdZ1jkVh8CBSAVhobm%2BqIr2Sjuf2COU3JTF3uSaMMirJNC2tykKop3xnmdZomry%2BzQUJHtaSh7WpRJkX%2BB1W8WPCxlqcYX1jPXIXC8ENgbrFHbgarhU4UyhHdn5S%2F7xpiDXcbWGBHJOKlU9uX%2Fpg%2F4tu0ehxOznM0Xza0KYWU%2B%2F1vozNJlIocK0u%2BjMgXgzhfaYegnrEdbFMeRNpOO6FSwInRw0rDKRdRcy5oLhhVbrqwSLmF%2B7o4URvqLjf6OMGjWyR55O9ylLeY95WRTZZt89ktRYLQfyOHUlBw0U6bgpBLWGktJVoqYkmX7EiOlfLcIHoVQbL1qM%2FQ2tl461olEjbWt9QopKaDxbltujnr14j6z6tauw0CZOq7xzrKZOMkQChxyBrhM77t5bOZlu8oolqeiIIab804HuMEd4FW6pWxmEqGYD4TOMNrH%2BLwGOqUBCBlEVxZLLNpIV8FHcQ%2BYvPCaSEtGNfMnVhWllf14DaQpM31w1aXEAaVzuF%2FnRuIJZ4fWHNC4kZEbQoB1JhRYHlflB8TFETSVIo77%2B44FQQ1TMAZAiSUX%2B27U9%2FbEApA5SGkTUqhLKdDaCN%2BXSFZf8uDuN4LBRvu%2BW%2FbbV7%2BPzvNOMg%2FD%2BXoHLJxaKWW%2F%2BcdRVZS1O%2BHqNujv3g0qSnhL0swxUbKY&X-Amz-Signature=ac0554b442736dcca8aa25df3d5e9e321e774ba46517e8413c7e0cd695f8b8bf&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23a79b9d-2356-49a9-8fd9-65c6b0ab2cc5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46665NKZ6IV%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T161555Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGF94CUXcUTAMJHDuuv2KSUaLM0orEQOZRrAV4ALR2muAiBE%2FaifUxe6ijR6K8JVbRhHjo%2BoC9wrJYmBtUFJRQ%2FLMCqIBAjX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMHB5O5ahcHe9tHlk%2FKtwDigl%2ByBOxL1EXS3ml92tWxVGVK7WF9XKIHsz6lgaJhyEBJqXYEONgrBoEM%2B6a5vi%2FeAKGib8QuKFv0B49cmW7vUPYik7nZM%2FMSSbHgFLWgLQJPUtSxXTP6k11MqwIFKTs8dioPqigBIDPdZjFJymeCYuE57A9Cakh19tctpA8fGrUvm9d3FyhRTIn89E7woxn%2BpnItHOx4KdPcQPXtRp7vlt3Rn0DayGGfr%2Bc9NNhuB53vb1eZWPAZa0Gcu5n%2FrkaTI6%2Fv%2FwaO19OA9IwHdXKxwwC9KCevjahT58BeKqqsYx%2FEzoqUgNHzemqaF%2BM%2FQT1wiLN8SSsLcGhokBb7aVt10lvGGr1SX%2Fs1tckWtAM1DmkoHrIgd18%2FF74AdLCHZ%2FOn1D9BfXul%2FYAfTtxqz67JJ6AA3zC4k6%2BcTiEYe3JSpfjQP0SFwRt%2BPwCBbV0bG4kUcUqDdTcOEecvNMcVUWHDONtasFoWk%2F5O5q5rfE1yLaaOJhGjZs7e5EnZiHhIX6dILmn7iYnNNck60LFWS3KD71gZqpexBsSsZ6av9i7tebYfDs9nKdxCzZhy82oPjIoW4x4lnf40dPB8Q4Oxn%2BJ%2FRVFYijR2ltvSdh0WxGEWNYjMiL8TmVUCmR%2BFw8w%2Bcr4vAY6pgEHy%2BwwOHtjahLK%2FImOK8%2FVbgMmj0OMFfetfy0pVlSVdEo9WLufQ1kQrtuXQd7KHA5%2BedqhA4kBKUSxgEo4onYBwFm%2BRI5TWkrz4N9IaI6eJmdXbVY8yiHNKty3ERvSGdTckD%2FkjD1gcq3BhdJsRCs1YN22X2gffU4u%2BysAhBHL8HHJEtlLcd1MLm0Y1eYPQxoMh2FN2fPUE8Q66fjJ7TVgQv3eASeX&X-Amz-Signature=27fa13f8e2d5db7de2a6c05f3a468440285d9674b25d93dfb27e30a8dd520154&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 4. KDE Plot
A Kernel Density Estimate (KDE) plot is a graph that creates a probability distribution curve for the data based upon its likelihood of occurrence on a specific value. This is created for a single vector of information.
**Syntax:**
```python
sns.kdeplot(X) || sns.kdeplot(df['age'])
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0d571213-2a2f-4921-a50b-880847aa05ee/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46665NKZ6IV%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T161555Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGF94CUXcUTAMJHDuuv2KSUaLM0orEQOZRrAV4ALR2muAiBE%2FaifUxe6ijR6K8JVbRhHjo%2BoC9wrJYmBtUFJRQ%2FLMCqIBAjX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMHB5O5ahcHe9tHlk%2FKtwDigl%2ByBOxL1EXS3ml92tWxVGVK7WF9XKIHsz6lgaJhyEBJqXYEONgrBoEM%2B6a5vi%2FeAKGib8QuKFv0B49cmW7vUPYik7nZM%2FMSSbHgFLWgLQJPUtSxXTP6k11MqwIFKTs8dioPqigBIDPdZjFJymeCYuE57A9Cakh19tctpA8fGrUvm9d3FyhRTIn89E7woxn%2BpnItHOx4KdPcQPXtRp7vlt3Rn0DayGGfr%2Bc9NNhuB53vb1eZWPAZa0Gcu5n%2FrkaTI6%2Fv%2FwaO19OA9IwHdXKxwwC9KCevjahT58BeKqqsYx%2FEzoqUgNHzemqaF%2BM%2FQT1wiLN8SSsLcGhokBb7aVt10lvGGr1SX%2Fs1tckWtAM1DmkoHrIgd18%2FF74AdLCHZ%2FOn1D9BfXul%2FYAfTtxqz67JJ6AA3zC4k6%2BcTiEYe3JSpfjQP0SFwRt%2BPwCBbV0bG4kUcUqDdTcOEecvNMcVUWHDONtasFoWk%2F5O5q5rfE1yLaaOJhGjZs7e5EnZiHhIX6dILmn7iYnNNck60LFWS3KD71gZqpexBsSsZ6av9i7tebYfDs9nKdxCzZhy82oPjIoW4x4lnf40dPB8Q4Oxn%2BJ%2FRVFYijR2ltvSdh0WxGEWNYjMiL8TmVUCmR%2BFw8w%2Bcr4vAY6pgEHy%2BwwOHtjahLK%2FImOK8%2FVbgMmj0OMFfetfy0pVlSVdEo9WLufQ1kQrtuXQd7KHA5%2BedqhA4kBKUSxgEo4onYBwFm%2BRI5TWkrz4N9IaI6eJmdXbVY8yiHNKty3ERvSGdTckD%2FkjD1gcq3BhdJsRCs1YN22X2gffU4u%2BysAhBHL8HHJEtlLcd1MLm0Y1eYPQxoMh2FN2fPUE8Q66fjJ7TVgQv3eASeX&X-Amz-Signature=521a16c5226110b862e248937c09b7258dddb9b3b0470c9188e9c3a8a96f30b7&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/53752550-ef82-4ca9-a01a-09921f0282d0/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46665NKZ6IV%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T161555Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGF94CUXcUTAMJHDuuv2KSUaLM0orEQOZRrAV4ALR2muAiBE%2FaifUxe6ijR6K8JVbRhHjo%2BoC9wrJYmBtUFJRQ%2FLMCqIBAjX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMHB5O5ahcHe9tHlk%2FKtwDigl%2ByBOxL1EXS3ml92tWxVGVK7WF9XKIHsz6lgaJhyEBJqXYEONgrBoEM%2B6a5vi%2FeAKGib8QuKFv0B49cmW7vUPYik7nZM%2FMSSbHgFLWgLQJPUtSxXTP6k11MqwIFKTs8dioPqigBIDPdZjFJymeCYuE57A9Cakh19tctpA8fGrUvm9d3FyhRTIn89E7woxn%2BpnItHOx4KdPcQPXtRp7vlt3Rn0DayGGfr%2Bc9NNhuB53vb1eZWPAZa0Gcu5n%2FrkaTI6%2Fv%2FwaO19OA9IwHdXKxwwC9KCevjahT58BeKqqsYx%2FEzoqUgNHzemqaF%2BM%2FQT1wiLN8SSsLcGhokBb7aVt10lvGGr1SX%2Fs1tckWtAM1DmkoHrIgd18%2FF74AdLCHZ%2FOn1D9BfXul%2FYAfTtxqz67JJ6AA3zC4k6%2BcTiEYe3JSpfjQP0SFwRt%2BPwCBbV0bG4kUcUqDdTcOEecvNMcVUWHDONtasFoWk%2F5O5q5rfE1yLaaOJhGjZs7e5EnZiHhIX6dILmn7iYnNNck60LFWS3KD71gZqpexBsSsZ6av9i7tebYfDs9nKdxCzZhy82oPjIoW4x4lnf40dPB8Q4Oxn%2BJ%2FRVFYijR2ltvSdh0WxGEWNYjMiL8TmVUCmR%2BFw8w%2Bcr4vAY6pgEHy%2BwwOHtjahLK%2FImOK8%2FVbgMmj0OMFfetfy0pVlSVdEo9WLufQ1kQrtuXQd7KHA5%2BedqhA4kBKUSxgEo4onYBwFm%2BRI5TWkrz4N9IaI6eJmdXbVY8yiHNKty3ERvSGdTckD%2FkjD1gcq3BhdJsRCs1YN22X2gffU4u%2BysAhBHL8HHJEtlLcd1MLm0Y1eYPQxoMh2FN2fPUE8Q66fjJ7TVgQv3eASeX&X-Amz-Signature=352fd4448a53f58b635d16556ea24daaab7bf15820811f020d579c2db118717b&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
## 4. Correlation Between Variables
Correlation is a statistical measure of the extent to which different variables are interdependent. It indicates how changes in one variable are associated with changes in another variable over time.
### Positive Correlation
Positive correlation indicates that as one variable increases, the other variable also tends to increase.
**Example: Engine Size and Price**
- **Positive Correlation:** Engine size increases, price also increases.
- **Visualization:** Scatter plot with a steep positive slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c7ea9b0-3ef3-4357-a9c3-554fc71b6b15/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YE5H3EO5%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T161556Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCvlj3quyicHzNoUW4e1WH9WLwtHWiSAG%2F3SX%2B%2Bjgma6wIgVEJwEsvWd6VeuNqv9hlPnkHTsLv7vzSEVmf3WsLD5ksqiAQI1%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHasDabn86jp9052KyrcA0SRExV5iNDojA1YxbAh470ewnYYQVEtUYZ7JfNqBdpBvHDGAAKgpV2%2BMsvd149zgp6Dykfl6DFY0%2BoHXsWYy21liwefFFNfpjWs35BcoJY7RkfD43c2X3CnR8NqIPjz9g4T%2FUh1GJ1CPWUyS1yaMKFIS0HwKRJQq7FuHqzB6%2FzDgOPB3xVvspH0AGB%2BHICaNfDu%2FAZZRCQdgdVGWM3W7VAo3%2BWHZOpHiCQi4huIGsKpHerPJyC%2FCORW1v1RqXX%2F4w0rT8JMOa0XErmNqUAEIALdOMnZh0xYEOK%2FGi6niteh%2BeL%2Bo7cmAZQhqMD2ZwqqyIUEN3PXxRBqNMa2N8D8UJeKjFTy1xU6r%2FQE%2FemjYnktZYHsWe2fNdPw7e1rNlzdQogY7Qz8z6koQUvltJnkJYAbjda2BOhHL7Rv1KMWu7NNQlKe7ib0V4tl0zJlPrD9p6qKNtZVMZA0PELhA7Zgn44RG8LAj%2BIImO4Ai0VAkqfFvOHj%2FuatbMPepzwW5tv3kVtB5x7HC8UABkzLJrG%2BaeM86cSIi3v0v5hW0M2dqUpE0pYRsOe2Zb73Ylxrak1q9uoYvD%2BJcSzItUr9LHuMWkAk0NeBZabWpsofEaURmTEroxsI1Le5ji2gqh7DMMPK%2BLwGOqUBF%2Bz9X4QILRaqnLEwzcIF%2Bn14ZHrUAhpLlIQjPjXSOnxZi%2FBZHb%2BT6u2fJV%2BfSwWMb2WS9EzaBObssHdROJCU1VoCDsBSPo3EXTSNAjXMtpPTOOArVMwNOafNG3oT3dyJ12pD%2FLNXlXshIuI2%2BC9iCD7fgJzI1D0TeqKthScj8%2BZV15zINuyh53Ickfust8lTDiyKgDlaYV%2FeuNBdLqSDHP209v9x&X-Amz-Signature=5c4e83393573adf77276271773fc558a172cd2c2cf69eb169db8e711b2b242f6&X-Amz-SignedHeaders=host&x-id=GetObject)
**Explanation:** When engine size increases, there is a corresponding increase in the price of the vehicle. This positive correlation suggests that larger engines tend to be associated with higher prices in the market.
___
### Negative Correlation
Negative correlation indicates that as one variable increases, the other variable tends to decrease.
**Example: Highway Miles per Gallon and Price**
- **Negative Correlation:** As highway miles per gallon increases, price decreases.
- **Visualization:** Scatter plot with a steep negative slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/10f1f798-9cc4-4df2-a9c1-5a339f554a0b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RLQM7YH6%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T161556Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCECQi7EEhW4diU5%2BZbjLPLOFgEasjijk7wARy0b5qHpgIhAIjtNp0si5E1Tb6PlcQfL4N8OF9b7XbtWCrH2uDVnobSKogECNb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyFWEmGY4RwGTRYfz4q3AOSQ9%2FlZWB3xM%2B4ilgpZOIReXYogVurPpDTO2jFlvKHKkxHmX5OXD1s3e7z0VMxO1LD1pLoHyVLpuJLID6fnIrkshAyi3jBTaaHjX2PhvYSiYb9dG2N8WhWTakoDiMmft9og1307RuU7Cvu%2F4eqpr1xRSwmnAuy9U1hzjDSS2WwkHuZbTND0Ey75nkHuAYvWYNh18fwX0IVCAbBo1OSw%2BOLVu0QlyodqPGG6mhe6wGQzxzfXCRc3KOwihjy7SGZsiOki1w070d971JHic939PtThG7XFgx6AD3KA7LvgB%2FfJCvfao5tB94JY%2Bgb%2FhVfcQUPw1N9M45WULXegyb2%2FjpPcsrGlO4OeBvKwVUDZOphtQ08nqsi32g8AaFCDspVFk0Sk1pUlHXlyE9Yb9jazj4QsDzQulV8YyIk87Px1JR7%2FCmmdZ%2BngNNIE7efadcjrlCUp982a7fuRfAgYO875U1uYeAt5m59KNTDUZrVI1nElwoAv7f2PabjE2E%2FgOd60EICdEL9KCDORhz5yTnZwUc2tRuHwQHkgVozKfDaWOaMLr%2BfX6%2F88G0tENb6C4zFdHHGAnJd08Qs1cB7vMiMfCRewHOSTlJeBMFLGu7u88cKNiDuIA7vdcd7UsgAwjDuvfi8BjqkAd5quhDuVWoXfqTrQGNKra9FQtiIn4pxijYEWRSzR7WP7g0s%2BNWNKQKt6WKWhClW9zTppnoOudxchHah%2B8WtV7R44qs3ePcKHIXyzA%2FgdsMlNOEOwy29bV3QgMTsXete%2BwHyFFE0bea28qXwSYhwxBYpmYQeGGzINAHxJvTDxdNczrGp6gMrC9rRbuvrVlZzPL4ayR84pq8%2BKL4FZJZCPzOeu8w1&X-Amz-Signature=9ede2bded757fb8d353c8d545b3fcd59e0d64be2577d49249b487eaf406393ba&X-Amz-SignedHeaders=host&x-id=GetObject)
**Explanation:** When highway miles per gallon increases, the price of the vehicle tends to decrease. This negative correlation suggests that cars with higher fuel efficiency (more miles per gallon) are generally priced lower in the market.
___
### Weak Correlation
Weak correlation indicates a lack of strong relationship between the variables.
**Example: RPM and Price**
- **Weak Correlation:** Low and high RPM values show varied prices, indicating no strong predictive relationship.
- **Visualization:** Scatter plot with no clear trend or slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9f914514-8914-4bf4-ac84-d9e3077f6eb1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663Z7RQJYZ%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T161556Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGpMqPkrDIq7y9dxquxlZ110jWowWdDyR%2BqV6XO1lstTAiB4Y9haoSCNvgSYpcWqoXKcBVJmBoMUBSRe4JNAZggipSqIBAjX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMj9Gx9n7MtQHZCs%2FKKtwDXzUwQ%2BVcFO3vvYF06SW4%2Be3%2BW%2FQKAnrw40Twvf9pq4G3%2Bu6qrSYbuI0%2Fjo6wrjCXvY0UN5DTq8H0FqxU3lsKryg5BWT5t885E2anmkVBkgP1a8sbIqshuNXvAQtdMHL9iA7TIK0pCR2DzDSyAeGLiKBpjpoSvTdoPu2b5sGDv9Gv4H5wQZSEdvaqBQEi9mwzpHX4prC41CqalB054tZairfQT6tgkPTHghYjDgBbGxLytagG1BzuwghFslru5fwa%2FwLRIKpDWRCMCQmaRLlzmwtY8h54poFmAirA0e8nHTsI4DVe%2FMWALsJ%2FlADs53uuXcs5fzSfDZ9%2FVuzJ43vMIfgaBRuuWfbQKxj3ScuMiL8NKXhAYBOW9d3lHpDeadceam2oDBE6sUbBQsUgeR1iWbPmS7yi5rt5QNITgaiu8lBm99tGbtCQ3mOv4X2727gOyoUoKPkhY63wfC5ZnfxXbHbf8UX6t0dnOkADLc7QSGnOJ9ti8%2BVMGjJ6QPlt7c6VcCHsnY4zv%2F5J03pw7w4s7rO4g%2BXUIQbaPd0eW7VfK0YxXwcq5npkapPOfLBaQF5dkQNBaIj%2B95IRKmco93YrCo7ELhX%2FdCWybgmOtgA0xKemnA6xzl%2BiztD5788w88L4vAY6pgFXs3qc1oLBevzFuB0dYJpj2G2kLPhFA%2BZQp3hcnTFK8bHF5iriOGpwOqP2VKZgEt5SRs%2F6ocFxXmSWjDes1QvWEKOTjyZ47pXah%2FfmVZ90l%2BFTMkh2OHhV26vmndY7bnwBtjAPGg%2FiLTGY%2Bgxpgjn6HumBsRKfkoAjr1fueSt1SEY7Opre6ptcenR5NA0d2ATHeXE4A1vOhkxuXa%2B7CRWrnHTKumvS&X-Amz-Signature=61aa7ff0fcd12608c9b005783906e36437dbd9edcdbe5b5d46389e138f829041&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f18086e5-5b04-4fbf-8309-8944ab20d213/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667FCHA5UW%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T161556Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICyN40ll3ayByYopjWZ1WeXePIHjoikv5rHLxEIqrdXTAiA5SQLWVTwGlhwdZjgPYxtMlV%2FSNXjN5G7VIP3ScUEv3CqIBAjW%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMM2D2LDQ4Rv0%2FetpCKtwDTzp70ghxD6dsN8JZA24rrmUd8vEbkvkGFCPNhTBL%2FkBkcNe5kfFjLgeldFIcw%2FjCq9tBC68l5kRU0ZCOtG%2BZLvKPCP8Dyj0BmpqJgbtukEvGEucMzoOtsB6GmF7Ls5metfUhoXtIGLoWdrutwMPTNC6kdIQoE5JDsoktR17f%2FErSmZUYWRwFEV6lPlZcrGIa5IY19JD%2BaNKRKM2wixbF3L5DVw2Zk70B0IK85eE6WX%2FUFCXgXVIMDRxUCbeF5Maf5CixgaHE828j4jfXFY4oBVAYBLc6LOiRnPyTW6%2BgxqzRV6%2B5OzoXQFHPIHSE6WuYqaB6x3P6lQYEXDWRmY4xHf2TZg9SIHH8HCGg1A%2B%2BIiTjHo4DTNpJwFJM2sqHcU4cRKkzkEvDvYPharGp0yqLA%2B5Ctr8LVftXGmcGBnUBC3ksoATVgHqEVMn7fl9DUnJxCZH7T85EmZcdQHbGzBPg9aHJ5gM4OqLtaz59GYXnY5XO0TfGPuLga9P1tdFs0IT%2BdOXl9fcKnGRh%2FK8RpY05aQSz%2FBZhkwa3unevAL46uoULDJlNVt5uZciV3tWQ76FjN4VIMkyPWce7FtaBoqQTTahQ19YjtW2ydfCpElm5ocTBAdINA6yFlgl2GAUw57L4vAY6pgE7ob4Twfe%2Bng9Dku5pXpmMoTpEpBnp7YOdT356uhLa18h852nzjMtUUGg64rvn1yRXwL9G7bC%2FydUMkr%2FyS84y9TMf4H6sxurJwRQk7Et72LinHgso7hQ3wzdau1ymHmbtKRzVNIxHEMoi8V%2Fw1x7CcSjOi7UHep7hYg0ZHDSVORk5yaVsYoPcyn6zBKGpltbEXAUQxzDewCchtVBsa4DS%2Ffi3Vh2B&X-Amz-Signature=cc3d58da11dd1575fac6c4bc3c705990c514fbc543cb7c33301779566c60e1c1&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Correlation Plot
Heatmap visualizes correlations among variables. Color scheme indicates Pearson correlation coefficients. Dark red diagonal line shows perfect correlation (value of 1) between variables and themselves.
This heatmap offers overview of variable relationships and their link with price.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cd3b341e-cc1a-45f7-8aec-cdc00436d270/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667FCHA5UW%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T161556Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICyN40ll3ayByYopjWZ1WeXePIHjoikv5rHLxEIqrdXTAiA5SQLWVTwGlhwdZjgPYxtMlV%2FSNXjN5G7VIP3ScUEv3CqIBAjW%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMM2D2LDQ4Rv0%2FetpCKtwDTzp70ghxD6dsN8JZA24rrmUd8vEbkvkGFCPNhTBL%2FkBkcNe5kfFjLgeldFIcw%2FjCq9tBC68l5kRU0ZCOtG%2BZLvKPCP8Dyj0BmpqJgbtukEvGEucMzoOtsB6GmF7Ls5metfUhoXtIGLoWdrutwMPTNC6kdIQoE5JDsoktR17f%2FErSmZUYWRwFEV6lPlZcrGIa5IY19JD%2BaNKRKM2wixbF3L5DVw2Zk70B0IK85eE6WX%2FUFCXgXVIMDRxUCbeF5Maf5CixgaHE828j4jfXFY4oBVAYBLc6LOiRnPyTW6%2BgxqzRV6%2B5OzoXQFHPIHSE6WuYqaB6x3P6lQYEXDWRmY4xHf2TZg9SIHH8HCGg1A%2B%2BIiTjHo4DTNpJwFJM2sqHcU4cRKkzkEvDvYPharGp0yqLA%2B5Ctr8LVftXGmcGBnUBC3ksoATVgHqEVMn7fl9DUnJxCZH7T85EmZcdQHbGzBPg9aHJ5gM4OqLtaz59GYXnY5XO0TfGPuLga9P1tdFs0IT%2BdOXl9fcKnGRh%2FK8RpY05aQSz%2FBZhkwa3unevAL46uoULDJlNVt5uZciV3tWQ76FjN4VIMkyPWce7FtaBoqQTTahQ19YjtW2ydfCpElm5ocTBAdINA6yFlgl2GAUw57L4vAY6pgE7ob4Twfe%2Bng9Dku5pXpmMoTpEpBnp7YOdT356uhLa18h852nzjMtUUGg64rvn1yRXwL9G7bC%2FydUMkr%2FyS84y9TMf4H6sxurJwRQk7Et72LinHgso7hQ3wzdau1ymHmbtKRzVNIxHEMoi8V%2Fw1x7CcSjOi7UHep7hYg0ZHDSVORk5yaVsYoPcyn6zBKGpltbEXAUQxzDewCchtVBsa4DS%2Ffi3Vh2B&X-Amz-Signature=94f276ff6463a16101d439d0cff032b8b5c097c708b6bc289686fd95b86b636d&X-Amz-SignedHeaders=host&x-id=GetObject)

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
