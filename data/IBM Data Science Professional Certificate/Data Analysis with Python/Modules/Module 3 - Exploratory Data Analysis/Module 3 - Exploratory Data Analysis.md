

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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/7e6d594d-952e-44b6-97ea-31225882aea6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WTE636HU%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T231407Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDcaCXVzLXdlc3QtMiJIMEYCIQCORhH0SRHN50TodJ1gUB9lqIoubvye3OfEG%2FoTIYCSqwIhAI0xImVJneirDErYhgPTOLVLCs%2FJaCEUMpyjdc3GE4kqKv8DCFAQABoMNjM3NDIzMTgzODA1IgwjeLTketqwOtlLpcAq3ANfmY5syRpWPixqeqiY5K6FlQCebQ9vTdMCoRYlwq23ElInawdboJIOCb42kO9X27JNkVzLaIrfGcbwPVqRtGtS10D8sDyUjITrEKDZ8ERi2DU%2BWtKSfI1XztfiT3akbm5xNt2QGnaiLKOGNpx5S3DatO1KR5T9UisPV%2FQkyKQfsqnlJZghUk5ODhYjIFsWKbXX619SwfB9a3yF6zHRmcs10p9ZK98lxT3wXftLgLzQLGDNB3Yf0BAuHjvbe680QOGFWbXVJE%2B5QmcQNGPdCaNnkm0VS1m5qW%2F%2FCrw41DmNQCb3n1DZ5K2Pw1EuPhgJId3xnbU6UwXIFL3oYMvXKzhEa8TXnAlkUl%2BEcd8atSI6Uwl1ikLWR1ofWzNd8ROwubBhqyzoS8Rh2tYCtFEMd62%2B6yv%2FpCi%2BYgPApmu0I1%2FKGmHf5UdCjfLBTaUatq5cHXQgH9EIzidK1yB%2B%2FjP%2F%2BfPNXDD5VuRmap0DJoA0FeYRukvFjf5w3Um4KiY5%2FIky9OyT4IuZoMUn1yZVJ7R%2FGC7xkugWNph1bpHROG2%2Bwg%2BGqi%2BE6f8BUQdC2H%2BiKgtJfFgRzLfZT6i0HFrOMh2zfHec48pbwIJhyYpdAFDOjCEcyIM6YcYdelbsFDOhwDDG2I%2B9BjqkATl4Re7nm%2F9JASdS9Ki2LvAefvQ7xvuP2%2Fo%2B9%2B8otJSxpWG%2FrP68CUkFY1MwPc0BbzXvYoyRGNQkt6qFKv6YwQgcVpHNKtpfcceLu%2BJhXHAFQlm2H7inihsL7BbE%2BCl1gqFGqVyqqhkUMeqyepSlndR2%2F1Fdbom120dCe0dyFe7wBE2N3Amj9lcfnjwR2aovFuHEZeIbBRwtGFMuL8c5WApspHkF&X-Amz-Signature=8dc5af12068fc5406e35eb7a3357d0f7ab4d93b5a8aaa2dacb070945413179de&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cbfaed9e-b398-4902-8936-dea058b21def/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WTE636HU%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T231407Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDcaCXVzLXdlc3QtMiJIMEYCIQCORhH0SRHN50TodJ1gUB9lqIoubvye3OfEG%2FoTIYCSqwIhAI0xImVJneirDErYhgPTOLVLCs%2FJaCEUMpyjdc3GE4kqKv8DCFAQABoMNjM3NDIzMTgzODA1IgwjeLTketqwOtlLpcAq3ANfmY5syRpWPixqeqiY5K6FlQCebQ9vTdMCoRYlwq23ElInawdboJIOCb42kO9X27JNkVzLaIrfGcbwPVqRtGtS10D8sDyUjITrEKDZ8ERi2DU%2BWtKSfI1XztfiT3akbm5xNt2QGnaiLKOGNpx5S3DatO1KR5T9UisPV%2FQkyKQfsqnlJZghUk5ODhYjIFsWKbXX619SwfB9a3yF6zHRmcs10p9ZK98lxT3wXftLgLzQLGDNB3Yf0BAuHjvbe680QOGFWbXVJE%2B5QmcQNGPdCaNnkm0VS1m5qW%2F%2FCrw41DmNQCb3n1DZ5K2Pw1EuPhgJId3xnbU6UwXIFL3oYMvXKzhEa8TXnAlkUl%2BEcd8atSI6Uwl1ikLWR1ofWzNd8ROwubBhqyzoS8Rh2tYCtFEMd62%2B6yv%2FpCi%2BYgPApmu0I1%2FKGmHf5UdCjfLBTaUatq5cHXQgH9EIzidK1yB%2B%2FjP%2F%2BfPNXDD5VuRmap0DJoA0FeYRukvFjf5w3Um4KiY5%2FIky9OyT4IuZoMUn1yZVJ7R%2FGC7xkugWNph1bpHROG2%2Bwg%2BGqi%2BE6f8BUQdC2H%2BiKgtJfFgRzLfZT6i0HFrOMh2zfHec48pbwIJhyYpdAFDOjCEcyIM6YcYdelbsFDOhwDDG2I%2B9BjqkATl4Re7nm%2F9JASdS9Ki2LvAefvQ7xvuP2%2Fo%2B9%2B8otJSxpWG%2FrP68CUkFY1MwPc0BbzXvYoyRGNQkt6qFKv6YwQgcVpHNKtpfcceLu%2BJhXHAFQlm2H7inihsL7BbE%2BCl1gqFGqVyqqhkUMeqyepSlndR2%2F1Fdbom120dCe0dyFe7wBE2N3Amj9lcfnjwR2aovFuHEZeIbBRwtGFMuL8c5WApspHkF&X-Amz-Signature=eedd58473c641ef6302357ca920641a2f2d32cd7fcedcc84dd52bfe9160323b5&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/91181646-b1e0-4433-9711-6259a96a9247/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WTE636HU%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T231407Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDcaCXVzLXdlc3QtMiJIMEYCIQCORhH0SRHN50TodJ1gUB9lqIoubvye3OfEG%2FoTIYCSqwIhAI0xImVJneirDErYhgPTOLVLCs%2FJaCEUMpyjdc3GE4kqKv8DCFAQABoMNjM3NDIzMTgzODA1IgwjeLTketqwOtlLpcAq3ANfmY5syRpWPixqeqiY5K6FlQCebQ9vTdMCoRYlwq23ElInawdboJIOCb42kO9X27JNkVzLaIrfGcbwPVqRtGtS10D8sDyUjITrEKDZ8ERi2DU%2BWtKSfI1XztfiT3akbm5xNt2QGnaiLKOGNpx5S3DatO1KR5T9UisPV%2FQkyKQfsqnlJZghUk5ODhYjIFsWKbXX619SwfB9a3yF6zHRmcs10p9ZK98lxT3wXftLgLzQLGDNB3Yf0BAuHjvbe680QOGFWbXVJE%2B5QmcQNGPdCaNnkm0VS1m5qW%2F%2FCrw41DmNQCb3n1DZ5K2Pw1EuPhgJId3xnbU6UwXIFL3oYMvXKzhEa8TXnAlkUl%2BEcd8atSI6Uwl1ikLWR1ofWzNd8ROwubBhqyzoS8Rh2tYCtFEMd62%2B6yv%2FpCi%2BYgPApmu0I1%2FKGmHf5UdCjfLBTaUatq5cHXQgH9EIzidK1yB%2B%2FjP%2F%2BfPNXDD5VuRmap0DJoA0FeYRukvFjf5w3Um4KiY5%2FIky9OyT4IuZoMUn1yZVJ7R%2FGC7xkugWNph1bpHROG2%2Bwg%2BGqi%2BE6f8BUQdC2H%2BiKgtJfFgRzLfZT6i0HFrOMh2zfHec48pbwIJhyYpdAFDOjCEcyIM6YcYdelbsFDOhwDDG2I%2B9BjqkATl4Re7nm%2F9JASdS9Ki2LvAefvQ7xvuP2%2Fo%2B9%2B8otJSxpWG%2FrP68CUkFY1MwPc0BbzXvYoyRGNQkt6qFKv6YwQgcVpHNKtpfcceLu%2BJhXHAFQlm2H7inihsL7BbE%2BCl1gqFGqVyqqhkUMeqyepSlndR2%2F1Fdbom120dCe0dyFe7wBE2N3Amj9lcfnjwR2aovFuHEZeIbBRwtGFMuL8c5WApspHkF&X-Amz-Signature=dd50be26db5951dacc368df08bc0371844b7db61dfb70b65711f22d2a78171b8&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/09aba1c0-0d55-41dd-852a-a04c5b8a3fac/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XAS2NGLL%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T231408Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDcaCXVzLXdlc3QtMiJHMEUCIDlZaPOHgih8gFUaymzBPPQcya9qiOs5wL6L53oe8uv3AiEAqR4ni8POuQqE%2BlefMIIq6c%2FtWaHfLek9RwsoUw2oK9Iq%2FwMIUBAAGgw2Mzc0MjMxODM4MDUiDBKp52N7t1lLT%2FTEDCrcA1lFJCSTbc9b2bwg5R7UNgRuMlKc%2Fkoewvn0fpwF2zRzL6n1sPWYZ8SEjSLl6r2UOCR%2BkZURuzpw8XYL6OWPau2qF1KDXW5veDP5hDi48oFxNeL6qyr5eLcZitp%2B8ZTaGHvvpkEZET87C5cVfnZvK%2BEOo2y%2B6i6NrZflTvxiVP7Oe8xnirgzaCqJRUeoTrC7CqDXsnqbCzb6Tdonfp4YKIWVs4z07%2Bw8FJKs62K07IdpimqZtCtaIlP9sdHXNzm2p1J9EBEEYXkonVIae6Qrv4VGPfEWaHNoAKi4isNxb16g8hhV3Tw2MHmnDOAKYttr%2BLIh%2F9wuO1YHGh1fdnTFlGapiOBuQmbRiHiup%2FX4XzrgVW0gGaIKNlTv9p7aYzR0nsZyfreprw7je%2B661asHOEsJXigd0Yf0KY7dTF%2B9bg1cPFpPX9W7GcqtZmeKu08o2%2B4LfpAv0vRgw%2FPQt571VkBktGCfRtB%2FdzMmZHM3nvUqC8qbzkWr4q6Lm8hf7ggrY%2B3Qn4fKFSmoSRyXjvgTdE1Y%2FEJ%2F9QsPqlBgm9DtW9%2F72w5MH83eja3K9zwk0swHopniUHN9gw8%2F49sIytTyFgtT0Yr0sQ0MwzdWyltT7HIXgzZOu7qYpVM9cEQaMJnaj70GOqUBAZMuLz4VFWoxgmy73%2Bxziplbgu7Pt5LDmJqsAzQ5mtfkE6KqTrFRJnvxnmNjwhHS8jn26yiNhHyfM8dhwVvgCGUGCLX3jFM6R8Ay77hvN7m%2B4YpdxcUruZjONkqxiJy%2FQODRsv1T3z36BNht8uHdCjxOTiLis9jpW92zdNszNt2xh8tkERsDQp5xnPsHpWtp1ScIszNw75AtBDFP5%2FXAbZeyQd6C&X-Amz-Signature=da567715fbb39f2b0a848de17ea49fdb361c237df16384b91da28e189aabb33a&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 2. Scatter Plot
Scatter plots present the relationship between two variables in a dataset. It represents data points on a two-dimensional plane. The independent variable or attribute is plotted on the X-axis, while the dependent variable is plotted on the Y-axis.
**Syntax:**
```python
plt.scatter(x, y)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23708af9-659f-4f23-b626-1a4292d7842c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XAS2NGLL%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T231408Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDcaCXVzLXdlc3QtMiJHMEUCIDlZaPOHgih8gFUaymzBPPQcya9qiOs5wL6L53oe8uv3AiEAqR4ni8POuQqE%2BlefMIIq6c%2FtWaHfLek9RwsoUw2oK9Iq%2FwMIUBAAGgw2Mzc0MjMxODM4MDUiDBKp52N7t1lLT%2FTEDCrcA1lFJCSTbc9b2bwg5R7UNgRuMlKc%2Fkoewvn0fpwF2zRzL6n1sPWYZ8SEjSLl6r2UOCR%2BkZURuzpw8XYL6OWPau2qF1KDXW5veDP5hDi48oFxNeL6qyr5eLcZitp%2B8ZTaGHvvpkEZET87C5cVfnZvK%2BEOo2y%2B6i6NrZflTvxiVP7Oe8xnirgzaCqJRUeoTrC7CqDXsnqbCzb6Tdonfp4YKIWVs4z07%2Bw8FJKs62K07IdpimqZtCtaIlP9sdHXNzm2p1J9EBEEYXkonVIae6Qrv4VGPfEWaHNoAKi4isNxb16g8hhV3Tw2MHmnDOAKYttr%2BLIh%2F9wuO1YHGh1fdnTFlGapiOBuQmbRiHiup%2FX4XzrgVW0gGaIKNlTv9p7aYzR0nsZyfreprw7je%2B661asHOEsJXigd0Yf0KY7dTF%2B9bg1cPFpPX9W7GcqtZmeKu08o2%2B4LfpAv0vRgw%2FPQt571VkBktGCfRtB%2FdzMmZHM3nvUqC8qbzkWr4q6Lm8hf7ggrY%2B3Qn4fKFSmoSRyXjvgTdE1Y%2FEJ%2F9QsPqlBgm9DtW9%2F72w5MH83eja3K9zwk0swHopniUHN9gw8%2F49sIytTyFgtT0Yr0sQ0MwzdWyltT7HIXgzZOu7qYpVM9cEQaMJnaj70GOqUBAZMuLz4VFWoxgmy73%2Bxziplbgu7Pt5LDmJqsAzQ5mtfkE6KqTrFRJnvxnmNjwhHS8jn26yiNhHyfM8dhwVvgCGUGCLX3jFM6R8Ay77hvN7m%2B4YpdxcUruZjONkqxiJy%2FQODRsv1T3z36BNht8uHdCjxOTiLis9jpW92zdNszNt2xh8tkERsDQp5xnPsHpWtp1ScIszNw75AtBDFP5%2FXAbZeyQd6C&X-Amz-Signature=6c9586408d218e22a31667e56a3c202f695ad9a103d3786a61d3217f3a21ec36&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 3. Histogram
A histogram is an important visual representation of data in categorical form. To view the data in a "Binned" form, use the histogram plot with a number of bins required or with the data points that mark the bin edges. The x-axis represents the data bins, and the y-axis represents the number of elements in each bin.
**Syntax:**
```python
plt.hist(x, bins)
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/24e4424a-df87-40a1-b63b-195cbdc2e0ab/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XAS2NGLL%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T231408Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDcaCXVzLXdlc3QtMiJHMEUCIDlZaPOHgih8gFUaymzBPPQcya9qiOs5wL6L53oe8uv3AiEAqR4ni8POuQqE%2BlefMIIq6c%2FtWaHfLek9RwsoUw2oK9Iq%2FwMIUBAAGgw2Mzc0MjMxODM4MDUiDBKp52N7t1lLT%2FTEDCrcA1lFJCSTbc9b2bwg5R7UNgRuMlKc%2Fkoewvn0fpwF2zRzL6n1sPWYZ8SEjSLl6r2UOCR%2BkZURuzpw8XYL6OWPau2qF1KDXW5veDP5hDi48oFxNeL6qyr5eLcZitp%2B8ZTaGHvvpkEZET87C5cVfnZvK%2BEOo2y%2B6i6NrZflTvxiVP7Oe8xnirgzaCqJRUeoTrC7CqDXsnqbCzb6Tdonfp4YKIWVs4z07%2Bw8FJKs62K07IdpimqZtCtaIlP9sdHXNzm2p1J9EBEEYXkonVIae6Qrv4VGPfEWaHNoAKi4isNxb16g8hhV3Tw2MHmnDOAKYttr%2BLIh%2F9wuO1YHGh1fdnTFlGapiOBuQmbRiHiup%2FX4XzrgVW0gGaIKNlTv9p7aYzR0nsZyfreprw7je%2B661asHOEsJXigd0Yf0KY7dTF%2B9bg1cPFpPX9W7GcqtZmeKu08o2%2B4LfpAv0vRgw%2FPQt571VkBktGCfRtB%2FdzMmZHM3nvUqC8qbzkWr4q6Lm8hf7ggrY%2B3Qn4fKFSmoSRyXjvgTdE1Y%2FEJ%2F9QsPqlBgm9DtW9%2F72w5MH83eja3K9zwk0swHopniUHN9gw8%2F49sIytTyFgtT0Yr0sQ0MwzdWyltT7HIXgzZOu7qYpVM9cEQaMJnaj70GOqUBAZMuLz4VFWoxgmy73%2Bxziplbgu7Pt5LDmJqsAzQ5mtfkE6KqTrFRJnvxnmNjwhHS8jn26yiNhHyfM8dhwVvgCGUGCLX3jFM6R8Ay77hvN7m%2B4YpdxcUruZjONkqxiJy%2FQODRsv1T3z36BNht8uHdCjxOTiLis9jpW92zdNszNt2xh8tkERsDQp5xnPsHpWtp1ScIszNw75AtBDFP5%2FXAbZeyQd6C&X-Amz-Signature=226b25267d080702d05673a14fb2151c095ebf35811062ee27e64b56b1064e44&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/ab5a6dfe-51f5-43ee-bcb3-33dae4a1c7ad/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XAS2NGLL%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T231408Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDcaCXVzLXdlc3QtMiJHMEUCIDlZaPOHgih8gFUaymzBPPQcya9qiOs5wL6L53oe8uv3AiEAqR4ni8POuQqE%2BlefMIIq6c%2FtWaHfLek9RwsoUw2oK9Iq%2FwMIUBAAGgw2Mzc0MjMxODM4MDUiDBKp52N7t1lLT%2FTEDCrcA1lFJCSTbc9b2bwg5R7UNgRuMlKc%2Fkoewvn0fpwF2zRzL6n1sPWYZ8SEjSLl6r2UOCR%2BkZURuzpw8XYL6OWPau2qF1KDXW5veDP5hDi48oFxNeL6qyr5eLcZitp%2B8ZTaGHvvpkEZET87C5cVfnZvK%2BEOo2y%2B6i6NrZflTvxiVP7Oe8xnirgzaCqJRUeoTrC7CqDXsnqbCzb6Tdonfp4YKIWVs4z07%2Bw8FJKs62K07IdpimqZtCtaIlP9sdHXNzm2p1J9EBEEYXkonVIae6Qrv4VGPfEWaHNoAKi4isNxb16g8hhV3Tw2MHmnDOAKYttr%2BLIh%2F9wuO1YHGh1fdnTFlGapiOBuQmbRiHiup%2FX4XzrgVW0gGaIKNlTv9p7aYzR0nsZyfreprw7je%2B661asHOEsJXigd0Yf0KY7dTF%2B9bg1cPFpPX9W7GcqtZmeKu08o2%2B4LfpAv0vRgw%2FPQt571VkBktGCfRtB%2FdzMmZHM3nvUqC8qbzkWr4q6Lm8hf7ggrY%2B3Qn4fKFSmoSRyXjvgTdE1Y%2FEJ%2F9QsPqlBgm9DtW9%2F72w5MH83eja3K9zwk0swHopniUHN9gw8%2F49sIytTyFgtT0Yr0sQ0MwzdWyltT7HIXgzZOu7qYpVM9cEQaMJnaj70GOqUBAZMuLz4VFWoxgmy73%2Bxziplbgu7Pt5LDmJqsAzQ5mtfkE6KqTrFRJnvxnmNjwhHS8jn26yiNhHyfM8dhwVvgCGUGCLX3jFM6R8Ay77hvN7m%2B4YpdxcUruZjONkqxiJy%2FQODRsv1T3z36BNht8uHdCjxOTiLis9jpW92zdNszNt2xh8tkERsDQp5xnPsHpWtp1ScIszNw75AtBDFP5%2FXAbZeyQd6C&X-Amz-Signature=05ed5af2224fe965db4a7b5f61ac91a84ef72f6198fff73f0f5ef939e6634d08&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/8f1b1d60-cf1b-42b3-9faa-f634c89c3f84/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XAS2NGLL%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T231408Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDcaCXVzLXdlc3QtMiJHMEUCIDlZaPOHgih8gFUaymzBPPQcya9qiOs5wL6L53oe8uv3AiEAqR4ni8POuQqE%2BlefMIIq6c%2FtWaHfLek9RwsoUw2oK9Iq%2FwMIUBAAGgw2Mzc0MjMxODM4MDUiDBKp52N7t1lLT%2FTEDCrcA1lFJCSTbc9b2bwg5R7UNgRuMlKc%2Fkoewvn0fpwF2zRzL6n1sPWYZ8SEjSLl6r2UOCR%2BkZURuzpw8XYL6OWPau2qF1KDXW5veDP5hDi48oFxNeL6qyr5eLcZitp%2B8ZTaGHvvpkEZET87C5cVfnZvK%2BEOo2y%2B6i6NrZflTvxiVP7Oe8xnirgzaCqJRUeoTrC7CqDXsnqbCzb6Tdonfp4YKIWVs4z07%2Bw8FJKs62K07IdpimqZtCtaIlP9sdHXNzm2p1J9EBEEYXkonVIae6Qrv4VGPfEWaHNoAKi4isNxb16g8hhV3Tw2MHmnDOAKYttr%2BLIh%2F9wuO1YHGh1fdnTFlGapiOBuQmbRiHiup%2FX4XzrgVW0gGaIKNlTv9p7aYzR0nsZyfreprw7je%2B661asHOEsJXigd0Yf0KY7dTF%2B9bg1cPFpPX9W7GcqtZmeKu08o2%2B4LfpAv0vRgw%2FPQt571VkBktGCfRtB%2FdzMmZHM3nvUqC8qbzkWr4q6Lm8hf7ggrY%2B3Qn4fKFSmoSRyXjvgTdE1Y%2FEJ%2F9QsPqlBgm9DtW9%2F72w5MH83eja3K9zwk0swHopniUHN9gw8%2F49sIytTyFgtT0Yr0sQ0MwzdWyltT7HIXgzZOu7qYpVM9cEQaMJnaj70GOqUBAZMuLz4VFWoxgmy73%2Bxziplbgu7Pt5LDmJqsAzQ5mtfkE6KqTrFRJnvxnmNjwhHS8jn26yiNhHyfM8dhwVvgCGUGCLX3jFM6R8Ay77hvN7m%2B4YpdxcUruZjONkqxiJy%2FQODRsv1T3z36BNht8uHdCjxOTiLis9jpW92zdNszNt2xh8tkERsDQp5xnPsHpWtp1ScIszNw75AtBDFP5%2FXAbZeyQd6C&X-Amz-Signature=63f1f70181a64f7609a82cfbc10ec2aea7cf006572e02488dcaa8ecb5eb63bf2&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/13ad0497-05fe-4eaa-984e-707b33e14761/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XAS2NGLL%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T231408Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDcaCXVzLXdlc3QtMiJHMEUCIDlZaPOHgih8gFUaymzBPPQcya9qiOs5wL6L53oe8uv3AiEAqR4ni8POuQqE%2BlefMIIq6c%2FtWaHfLek9RwsoUw2oK9Iq%2FwMIUBAAGgw2Mzc0MjMxODM4MDUiDBKp52N7t1lLT%2FTEDCrcA1lFJCSTbc9b2bwg5R7UNgRuMlKc%2Fkoewvn0fpwF2zRzL6n1sPWYZ8SEjSLl6r2UOCR%2BkZURuzpw8XYL6OWPau2qF1KDXW5veDP5hDi48oFxNeL6qyr5eLcZitp%2B8ZTaGHvvpkEZET87C5cVfnZvK%2BEOo2y%2B6i6NrZflTvxiVP7Oe8xnirgzaCqJRUeoTrC7CqDXsnqbCzb6Tdonfp4YKIWVs4z07%2Bw8FJKs62K07IdpimqZtCtaIlP9sdHXNzm2p1J9EBEEYXkonVIae6Qrv4VGPfEWaHNoAKi4isNxb16g8hhV3Tw2MHmnDOAKYttr%2BLIh%2F9wuO1YHGh1fdnTFlGapiOBuQmbRiHiup%2FX4XzrgVW0gGaIKNlTv9p7aYzR0nsZyfreprw7je%2B661asHOEsJXigd0Yf0KY7dTF%2B9bg1cPFpPX9W7GcqtZmeKu08o2%2B4LfpAv0vRgw%2FPQt571VkBktGCfRtB%2FdzMmZHM3nvUqC8qbzkWr4q6Lm8hf7ggrY%2B3Qn4fKFSmoSRyXjvgTdE1Y%2FEJ%2F9QsPqlBgm9DtW9%2F72w5MH83eja3K9zwk0swHopniUHN9gw8%2F49sIytTyFgtT0Yr0sQ0MwzdWyltT7HIXgzZOu7qYpVM9cEQaMJnaj70GOqUBAZMuLz4VFWoxgmy73%2Bxziplbgu7Pt5LDmJqsAzQ5mtfkE6KqTrFRJnvxnmNjwhHS8jn26yiNhHyfM8dhwVvgCGUGCLX3jFM6R8Ay77hvN7m%2B4YpdxcUruZjONkqxiJy%2FQODRsv1T3z36BNht8uHdCjxOTiLis9jpW92zdNszNt2xh8tkERsDQp5xnPsHpWtp1ScIszNw75AtBDFP5%2FXAbZeyQd6C&X-Amz-Signature=e1f8d1021369736092707018995f25ed1a0a937a29973c888151ac0fd28e7ace&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 2. Box and Whisker Plot
A box plot shows the distribution of quantitative data in a way that facilitates comparisons between variables or across levels of a categorical variable. The box shows the quartiles of the dataset while the whiskers extend to show the rest of the distribution, except for points that are determined to be "outliers".
**Syntax:**
```python
sns.boxplot(x='header_1', y='header_2', data=df)
```
**Example Output:**


![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/d207ae92-0a7c-4e2f-aa65-0ee5a2c33bf7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663TLYNWYT%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T231409Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDcaCXVzLXdlc3QtMiJGMEQCIDv02%2FS927raZgjdurt6YrXBBKtebewkr8JE0VFv0RiWAiA12QbJDGfLEqJJxC3wZZqACYM66gG5KjYSFZoIoDBWTCr%2FAwhQEAAaDDYzNzQyMzE4MzgwNSIMEqR0XqLtqwIY4IL4KtwDyKaIRBcT3MlK9mpvK8PIS47DjKEIYUAa7wZS%2FubaeSFyW3JVlusVadR%2FYP9NbxKbUmyy9BUrjHHB97OnFMeQFrMLQpxhvYvYmnJCCnghlx4lGf1%2BR24jAjWmhW1uk%2Bqjmq5VCUsxu0BRjGXM6doLrKTqZ%2BRrA4QraZIGbQ7IwkxER6ZZHInxgGpjH3qQdnRcbMIVlj7dWiLjQruBZwXvN18BPb3LaonJEqMT6Yw0XDxapfoHOrDdk6SAmTTQRNPsi33SMC%2Fy3szGKpizBqLKv88kWTEKcTdft5gn5zTzmpeEfSNvgRxC7WpCXcHwcFopMtolzOlnQaU2wu9qZ1%2FOQBzGtyBt0KJuqZgDeYaPtxx2Fqjnt95Unv%2FyO%2B3SceDNAaokTq6Y1a727Wd%2FlVDFGdFU%2FSgArPlZJIFBkmECJQrpJwoIYBLIUkk8mqGYyo3u4eVHgkXEbE3KomzkHXrQl0hz%2BZR7SY6rgan4BtDETVIccSN4gmvE5YAiyfCaE4It0l%2BguE%2FS14gmKNBy9eWX16pRJfbqn2kTA891uoXYbbd6JJqQZG56p2A9koKEgZriJPd6Zfh7LbNYmk628%2FJ8ieCM5%2BlLZKWepQQ54F6r0uQCNUaA7lyA39%2FFtlIwoOCPvQY6pgHVJH3SKUubZMLnIjRVLRHYOkIsm0OvWCZxYF7TGbuaw6aC2fp8h5cwYclEaAMOSLWDvp48sKvl%2FjwRvBbvGjxY4WIt%2F5Us6tcflb1sOP1tZAeQ%2FOcxoBRWFPdXeSesciA7Augk%2BC8hds6vEeblHNKk7G4MKc%2BaMdfsGN4dDURyx%2FGF61odaJuBtVye6k%2BmAWGNsulT60jQEd8eXHg6lF4j4OUUeC3K&X-Amz-Signature=180b36d13e639b322fa3e3d54210736ccc9c9740b22c0fb655e51eeea669af3b&X-Amz-SignedHeaders=host&x-id=GetObject)

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0e516edc-7551-4792-ab18-0494db3c4c0c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TBDD4OTT%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T231409Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDcaCXVzLXdlc3QtMiJGMEQCIAxdS82e4u3sVZvHLtpi5xnuZwINEzOqD7K86ofPfpDdAiBm4SFzsIUt27BJhTRO7N5o4eOr5PEJp2gj8cU%2F6TYcBir%2FAwhQEAAaDDYzNzQyMzE4MzgwNSIM%2Fjhl2eyy%2BGvc0ifGKtwDXR98d5gM2brawZi4ZnQ3aGqF%2Bq2r9a4%2BDhhMHuZMT7SXfk%2BEMq4I4EI7Vvraggx3kbSCXjUxy8QTIzlPpWk2vDD7UGeZGunug%2BRBfTc3t%2FzVmeLftXkBgSs6kC%2FxExAO4NLcfUvvwZszmNcqUrnrC245%2FMu%2BSy8NgLtt3ewOkp3PEl5wDfXeHYasXvQGXdPo38r26g1nkyU6S32spnR%2B6T1px6kxGRnFwRIXYTP9b%2FHk4RyH0Ta1p8mOBBBDnxofm57%2BnnO5gefMFWuiESutpBx%2FTMNtXR4Hen79AQSHHrLbXlaB5N85K1m3IGm2ziBMaJFH%2B7VQXgXd5tMFekqM7IvpKpAP801GPc74bx%2Fgd8SbF5SBrEGmxdkkEXDftwN3IPij6rKQR1Ijh7o4eHR%2B5B073LNlFj7uprY%2FRUUCBQs2AgOTt%2F7uy1wzPyMn2ecsaSCpvkc%2BRPTUAcRHGIW667h470WxVHWj%2Fus0B3OXXh5JIVg21xxL0uHT08F8R6ZBwIE0ZvPKkemNSgC9IP%2Fx0c1%2B%2BIk4reRRwWnAEIcXlGkBiKd55zP02Z5YztwBo2BwC6fuBigiw03G7o5%2Fe%2FerKUTL0BOwqfjqTgcCurSZjrHU66v0x%2Fzt%2Fniap2kwntuPvQY6pgE7hjH8bNdPl5whGg%2B9yvo%2BLOmsgehtJPU4%2B1Vp5Fl2n3hNXNOLeyOlljjbQdBhrt0Dt8Zr4nBG2OS15rzdFNrcD34wFZiW3nvPYiYKXtdHnfTH2Me2GQdNff2x%2FnXSARtzPusQnVOtFdZnP844dpz208EjY7l7DW96HOM6DAiuAy6dUiXvk6pNrTHOBRFGRHaeHhPt0kkizogvVwUFjhFRDXax4Bxz&X-Amz-Signature=791e55648c4735730ce5511fe7f5c2a5296ba422b3d2c4f6d0611d6025d56ea4&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/23a79b9d-2356-49a9-8fd9-65c6b0ab2cc5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XAS2NGLL%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T231408Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDcaCXVzLXdlc3QtMiJHMEUCIDlZaPOHgih8gFUaymzBPPQcya9qiOs5wL6L53oe8uv3AiEAqR4ni8POuQqE%2BlefMIIq6c%2FtWaHfLek9RwsoUw2oK9Iq%2FwMIUBAAGgw2Mzc0MjMxODM4MDUiDBKp52N7t1lLT%2FTEDCrcA1lFJCSTbc9b2bwg5R7UNgRuMlKc%2Fkoewvn0fpwF2zRzL6n1sPWYZ8SEjSLl6r2UOCR%2BkZURuzpw8XYL6OWPau2qF1KDXW5veDP5hDi48oFxNeL6qyr5eLcZitp%2B8ZTaGHvvpkEZET87C5cVfnZvK%2BEOo2y%2B6i6NrZflTvxiVP7Oe8xnirgzaCqJRUeoTrC7CqDXsnqbCzb6Tdonfp4YKIWVs4z07%2Bw8FJKs62K07IdpimqZtCtaIlP9sdHXNzm2p1J9EBEEYXkonVIae6Qrv4VGPfEWaHNoAKi4isNxb16g8hhV3Tw2MHmnDOAKYttr%2BLIh%2F9wuO1YHGh1fdnTFlGapiOBuQmbRiHiup%2FX4XzrgVW0gGaIKNlTv9p7aYzR0nsZyfreprw7je%2B661asHOEsJXigd0Yf0KY7dTF%2B9bg1cPFpPX9W7GcqtZmeKu08o2%2B4LfpAv0vRgw%2FPQt571VkBktGCfRtB%2FdzMmZHM3nvUqC8qbzkWr4q6Lm8hf7ggrY%2B3Qn4fKFSmoSRyXjvgTdE1Y%2FEJ%2F9QsPqlBgm9DtW9%2F72w5MH83eja3K9zwk0swHopniUHN9gw8%2F49sIytTyFgtT0Yr0sQ0MwzdWyltT7HIXgzZOu7qYpVM9cEQaMJnaj70GOqUBAZMuLz4VFWoxgmy73%2Bxziplbgu7Pt5LDmJqsAzQ5mtfkE6KqTrFRJnvxnmNjwhHS8jn26yiNhHyfM8dhwVvgCGUGCLX3jFM6R8Ay77hvN7m%2B4YpdxcUruZjONkqxiJy%2FQODRsv1T3z36BNht8uHdCjxOTiLis9jpW92zdNszNt2xh8tkERsDQp5xnPsHpWtp1ScIszNw75AtBDFP5%2FXAbZeyQd6C&X-Amz-Signature=9453c1a93390ba4dcc96092895b1ed951e1169ddad635d119547015b16533c0c&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
#### 4. KDE Plot
A Kernel Density Estimate (KDE) plot is a graph that creates a probability distribution curve for the data based upon its likelihood of occurrence on a specific value. This is created for a single vector of information.
**Syntax:**
```python
sns.kdeplot(X) || sns.kdeplot(df['age'])
```
**Example Output:**
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0d571213-2a2f-4921-a50b-880847aa05ee/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XAS2NGLL%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T231408Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDcaCXVzLXdlc3QtMiJHMEUCIDlZaPOHgih8gFUaymzBPPQcya9qiOs5wL6L53oe8uv3AiEAqR4ni8POuQqE%2BlefMIIq6c%2FtWaHfLek9RwsoUw2oK9Iq%2FwMIUBAAGgw2Mzc0MjMxODM4MDUiDBKp52N7t1lLT%2FTEDCrcA1lFJCSTbc9b2bwg5R7UNgRuMlKc%2Fkoewvn0fpwF2zRzL6n1sPWYZ8SEjSLl6r2UOCR%2BkZURuzpw8XYL6OWPau2qF1KDXW5veDP5hDi48oFxNeL6qyr5eLcZitp%2B8ZTaGHvvpkEZET87C5cVfnZvK%2BEOo2y%2B6i6NrZflTvxiVP7Oe8xnirgzaCqJRUeoTrC7CqDXsnqbCzb6Tdonfp4YKIWVs4z07%2Bw8FJKs62K07IdpimqZtCtaIlP9sdHXNzm2p1J9EBEEYXkonVIae6Qrv4VGPfEWaHNoAKi4isNxb16g8hhV3Tw2MHmnDOAKYttr%2BLIh%2F9wuO1YHGh1fdnTFlGapiOBuQmbRiHiup%2FX4XzrgVW0gGaIKNlTv9p7aYzR0nsZyfreprw7je%2B661asHOEsJXigd0Yf0KY7dTF%2B9bg1cPFpPX9W7GcqtZmeKu08o2%2B4LfpAv0vRgw%2FPQt571VkBktGCfRtB%2FdzMmZHM3nvUqC8qbzkWr4q6Lm8hf7ggrY%2B3Qn4fKFSmoSRyXjvgTdE1Y%2FEJ%2F9QsPqlBgm9DtW9%2F72w5MH83eja3K9zwk0swHopniUHN9gw8%2F49sIytTyFgtT0Yr0sQ0MwzdWyltT7HIXgzZOu7qYpVM9cEQaMJnaj70GOqUBAZMuLz4VFWoxgmy73%2Bxziplbgu7Pt5LDmJqsAzQ5mtfkE6KqTrFRJnvxnmNjwhHS8jn26yiNhHyfM8dhwVvgCGUGCLX3jFM6R8Ay77hvN7m%2B4YpdxcUruZjONkqxiJy%2FQODRsv1T3z36BNht8uHdCjxOTiLis9jpW92zdNszNt2xh8tkERsDQp5xnPsHpWtp1ScIszNw75AtBDFP5%2FXAbZeyQd6C&X-Amz-Signature=a69639367a61d6851f2c2fb2f0fa86aba5874c490c2a5ba904cbca5fb32fa7e9&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/53752550-ef82-4ca9-a01a-09921f0282d0/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XAS2NGLL%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T231408Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDcaCXVzLXdlc3QtMiJHMEUCIDlZaPOHgih8gFUaymzBPPQcya9qiOs5wL6L53oe8uv3AiEAqR4ni8POuQqE%2BlefMIIq6c%2FtWaHfLek9RwsoUw2oK9Iq%2FwMIUBAAGgw2Mzc0MjMxODM4MDUiDBKp52N7t1lLT%2FTEDCrcA1lFJCSTbc9b2bwg5R7UNgRuMlKc%2Fkoewvn0fpwF2zRzL6n1sPWYZ8SEjSLl6r2UOCR%2BkZURuzpw8XYL6OWPau2qF1KDXW5veDP5hDi48oFxNeL6qyr5eLcZitp%2B8ZTaGHvvpkEZET87C5cVfnZvK%2BEOo2y%2B6i6NrZflTvxiVP7Oe8xnirgzaCqJRUeoTrC7CqDXsnqbCzb6Tdonfp4YKIWVs4z07%2Bw8FJKs62K07IdpimqZtCtaIlP9sdHXNzm2p1J9EBEEYXkonVIae6Qrv4VGPfEWaHNoAKi4isNxb16g8hhV3Tw2MHmnDOAKYttr%2BLIh%2F9wuO1YHGh1fdnTFlGapiOBuQmbRiHiup%2FX4XzrgVW0gGaIKNlTv9p7aYzR0nsZyfreprw7je%2B661asHOEsJXigd0Yf0KY7dTF%2B9bg1cPFpPX9W7GcqtZmeKu08o2%2B4LfpAv0vRgw%2FPQt571VkBktGCfRtB%2FdzMmZHM3nvUqC8qbzkWr4q6Lm8hf7ggrY%2B3Qn4fKFSmoSRyXjvgTdE1Y%2FEJ%2F9QsPqlBgm9DtW9%2F72w5MH83eja3K9zwk0swHopniUHN9gw8%2F49sIytTyFgtT0Yr0sQ0MwzdWyltT7HIXgzZOu7qYpVM9cEQaMJnaj70GOqUBAZMuLz4VFWoxgmy73%2Bxziplbgu7Pt5LDmJqsAzQ5mtfkE6KqTrFRJnvxnmNjwhHS8jn26yiNhHyfM8dhwVvgCGUGCLX3jFM6R8Ay77hvN7m%2B4YpdxcUruZjONkqxiJy%2FQODRsv1T3z36BNht8uHdCjxOTiLis9jpW92zdNszNt2xh8tkERsDQp5xnPsHpWtp1ScIszNw75AtBDFP5%2FXAbZeyQd6C&X-Amz-Signature=4b5fc431c1ee6cb0a06cb233ea5d521330212d64a6ac17d9224876f0f8977d31&X-Amz-SignedHeaders=host&x-id=GetObject)
![](#)
___
## 4. Correlation Between Variables
Correlation is a statistical measure of the extent to which different variables are interdependent. It indicates how changes in one variable are associated with changes in another variable over time.
### Positive Correlation
Positive correlation indicates that as one variable increases, the other variable also tends to increase.
**Example: Engine Size and Price**
- **Positive Correlation:** Engine size increases, price also increases.
- **Visualization:** Scatter plot with a steep positive slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/0c7ea9b0-3ef3-4357-a9c3-554fc71b6b15/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YVN55IQO%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T231410Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDcaCXVzLXdlc3QtMiJHMEUCIQDxGtCWJuf8QBe7%2BR11y07%2BHxRulNMMvbl6iEEQ7ZOhKAIgA1jw8AGA5NaWL%2BHtEHsAw3Rl6vKSyQwcj4ph3TqpQrUq%2FwMIUBAAGgw2Mzc0MjMxODM4MDUiDJDuj1T6BCCTYICsJircA0E0IqtINEmu%2BcxYENwotYOIiPHkqhVGuWj4c1MqMpPWDEm9F7BOdGLHksUksKLG4eu4qlwkhIqOAgZIRb1GEhfQ2T5jf%2BWNfnPhJ8mGcYk%2FmI%2BV%2FP1MK4cAfFQB1aEDjQNjwvfjgcAtkp77k%2F4HCBsADgyr8%2FlsIYdI0kkNW9kbKXj%2B4B%2BjlVNjWVxYgx6DepESJoyUHUdC7uMniggmIMiYjPrPApR7OYHEZuKDIFpjHISuJpWGfSI4cNen3frb9qQ1l2s1pPpGyB2O3KNv%2Fqq5DQ%2B5vHjxV8FUlE1Ydik0e0K1hjM%2FxIr4QcQPyd7ID2U5j1tsmTHuL6i%2FxcrfvzqBtljxUJ16zFJuTmjIP%2Buoq%2Bf2lfkBpVgYQf7s5BL6oUgbOvKTCnN0ckvCMme1Gv60lQVLgyD1u%2F8zfJCR%2FcFly2a52ZjAmZ91%2Bq3dPNoqiSB5V1aUioed5uxDeyEfXQH7rhWxmZAo1%2B8msqal50jCRo1T27n4UZ7DOoKPajzc%2F%2BflLJNnROKUvHpA0QMg5XBt1EPoXlH8YiLndbraiKX0A61fTw0NVULsL%2FYIvoiJGx%2FaMQz%2BRVmM4M67uYg7adAzXKhWQOlUhubKkv4BGJMolmdvjUdpv1za77IMMOzbj70GOqUB9IdKk3qjX8gF2qraN2hj9UWTonsAZrwVpquUC39WU3EhwSmPHrwfrGBZMc5hDQnueJEtwEYSPHZQ2KKY4i9RxqDWxxHnuJt%2BAJX9dSw8NKe4qVR5NqLvm8tDaUiTJKvNY8j0ACYSnCOuKZNIakurYVcFObrLr5MdlwkLLnBegP9NrDoM7Vt2y4%2BsbHiqQ%2FQq0OWwknUbrs%2B3RxBFgECP%2FJYzZ66A&X-Amz-Signature=a568d0799f72a629ad48fdca094015262b0118279c55228d19d102f979106f14&X-Amz-SignedHeaders=host&x-id=GetObject)
**Explanation:** When engine size increases, there is a corresponding increase in the price of the vehicle. This positive correlation suggests that larger engines tend to be associated with higher prices in the market.
___
### Negative Correlation
Negative correlation indicates that as one variable increases, the other variable tends to decrease.
**Example: Highway Miles per Gallon and Price**
- **Negative Correlation:** As highway miles per gallon increases, price decreases.
- **Visualization:** Scatter plot with a steep negative slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/10f1f798-9cc4-4df2-a9c1-5a339f554a0b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RV7UFYJI%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T231409Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDIaCXVzLXdlc3QtMiJGMEQCIHj8owwiS2TsdPnVaZolxTMFfjvYqpQjn7Ew6XNJthDfAiBI9O%2F4qYD0uG%2FzHBYr8ZR5wVdofpoSBIlkhIzFziiv3yr%2FAwhKEAAaDDYzNzQyMzE4MzgwNSIMFt5HIF5FpRwEfKFoKtwDX7ScXLfdK%2FFSxMoHPR7GmO%2BZXKbQ4VOS%2Be4GiKtfPtPGrgISLLm62CDpIOaccZZtkKxdFh%2B%2BGG5%2BNpPGLNlcpfETMWRG7O0KFfV0tapVIBcFrPtjmQqr8y%2BZvjAOJqzKx8x1JugwceXHL7gW0usk2hGYIUUF1ElSfiVHkgnWuOyTSkFO75rrH1sHmfmYLjM4BcZ4t2Fz3x0gsgqgZxcnsppEztGnQEAvVE%2FqVUT%2B%2FsB2zBYtnORQN18dfe1eQDzmf%2FylMItFuK1vspUconLFc7OI%2Bru9lefiLPb21GNzjWdVwIYThqLlwoCsAEKLdVMd1y8JQaFfYzwl7y8TTuTe6YishOq7%2F5zTHJzjt5H%2BlKHAHkMyncvToK8MNBQwhmxJkpyrFjeCErJQfdXqeEn3Iuc3Idv2%2Bx5s2uTNzOAuYGMccfQ6UYi1K0k7u8OHu1Eiod5ulQryLPqncS2MuXlrqHHXR%2FWMwe7%2BLPMp83MUNLZtQTnYj7bV9cULEOxkhlyybl4g0xBomd9Z0LFnDSaXXuWGZmznUQm4D2ZWW9Xmd%2BaCIKZpY3JElfmkztfqg1KzBO2dcNL7nA5UqA4xzg7MV%2BF%2FVkoMceoZhJoalAncnpjpgD3bM1aIBh%2Fh2lQwibyOvQY6pgE336eVSOi7DqwBeu8RlOOT0ZuaIFmEyC0bsspgzk1c2v%2BZsQvORpyUZNqUoYGJGK1YIdz%2F6cZrt6f1LdsfQx5P3%2FTklJwTUelbr8khjEU1%2F5MB52VnpusC38v2QpV7%2FsbxhJAK1PRchPprJdNdNwmFiUAqC7RIocJdOb5GUJ2dPskKtNM67tBxVg5l3oHa1AGegQFzGgDMeBtncq9pIbx31clb0E8F&X-Amz-Signature=bf69017119b4cd722ddacb7534d2477e65cfe590805cd6b020a4c95b72740e85&X-Amz-SignedHeaders=host&x-id=GetObject)
**Explanation:** When highway miles per gallon increases, the price of the vehicle tends to decrease. This negative correlation suggests that cars with higher fuel efficiency (more miles per gallon) are generally priced lower in the market.
___
### Weak Correlation
Weak correlation indicates a lack of strong relationship between the variables.
**Example: RPM and Price**
- **Weak Correlation:** Low and high RPM values show varied prices, indicating no strong predictive relationship.
- **Visualization:** Scatter plot with no clear trend or slope.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/9f914514-8914-4bf4-ac84-d9e3077f6eb1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YKQDXFCS%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T231409Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDcaCXVzLXdlc3QtMiJIMEYCIQD1iRMrZeypMG7R1i0V9FGdVfsVMuc3ySd2km76f9Vx%2BQIhAInywaMDS3JhbI5m9D4X6fYXXV1tG1Ca3dDYmTAZe2ugKv8DCFAQABoMNjM3NDIzMTgzODA1IgxInQgaf3UfkBjkA7Qq3AP7qBwC%2F3iXrU0x%2FSaSq%2BtrUM6iiB0OlvBu4mgGWhPIeV7bcBgmscpZ5iZ9SImyDedh%2FeyNzsvDcxuqADvPXlO%2FsN3O79P6bjiF5BHhM%2F%2BFSdF8E3raQUfgD7oIsI%2FvL7KaP6Itdh3q024bcimWiUhvzRAYQ6Bo5C8h7HStQs9G7mFTtugKFiAhbBHHI00f8HKuNYd14P6Hr1hQfHdGJtBlu9xkj7J4u4bxbx94JDU5I5COgj3a3GmI0jRc0m2mHKhwzbS0UnCZQlfyLk85FHA9tYK4Rahnu%2F%2BmKyAesCUID8oHDsc8Pv4kwyNi9Cc2KBTabOJRVtDPOr9DFqnVpu15U412NRxHVwAYYD0tOJGprOWm7OEzutXevL8063ReB1foCYpyhrm673Y%2FJq2z32C7Aw%2Fq%2BSNyubcZ2n81wDiNFR4PQdCLHNv6VvGBxky0zB7vy4OQ%2FTt9HSks8xWAZzgBNdL2UyDXSq3gAB88BJOylv9hc6K%2BzckhVH2RHBJW%2B5XAdlig%2BuUlBIcXk%2FkKISY%2BIcnRWW%2Bnrzq5Q3F2p%2FWwOyT5uXc9cZahdhunZoObtXYrzeMQWtplK5FZt0ZTgkln37PqmXTDuMpb6HZnFUCdGOBkPOwtN2t%2BTEtUtTDh3Y%2B9BjqkAVfWZcbxktmkJJuMDf8zikgO9DVEwwVt1OXkVjWbAR4p5yTgyWFR7kvXNQS6M1iGUn9XExphTkvdwFjjy648tYwsKhtCzYdfKgTxS4MTIuua8rUdRbA4SCPMtGkoopuDDXKC%2BwPzvnrdz51OcpfXh%2BQWWOL2Zovg31aELahY8wq7ZNChUAacl%2BCRH2sZ28TDWWaVvZOVOX%2Fmnp%2Bvy8%2FvK6H%2BOCrz&X-Amz-Signature=64afeec2feb0ef61a025412715751eec559631b6184898ed405b56939462c03f&X-Amz-SignedHeaders=host&x-id=GetObject)
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
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/f18086e5-5b04-4fbf-8309-8944ab20d213/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662VDQIGNR%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T231409Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDcaCXVzLXdlc3QtMiJHMEUCIQDXmzuSCxB1dCK3DSg9wvnTPH6RVrnt9Vrfgg4zpGzt9AIgI7LQokZAOLcfFuDa2Ut7s%2BtREG7MTRcJRfXkgISORYoq%2FwMIUBAAGgw2Mzc0MjMxODM4MDUiDMNGMBIVZ%2FT%2Fp7h3PircA25NTSNMUclM7fWPRsc7Y0Wl71oeQ6AqemPhbzqesRTCi9Jufyd2y%2F2jfKoD5OTVQ%2BzKfTv1X22AiOkw08OnrlCw08qMwxZHzVkquULo5k38mRN2iC0xxQQQE4JaDTz%2FeGqFwJhlZ7KygI%2FybbEJbR8h3m1VlFLst5RYxXJOz9gqo0fuj9GeTX%2FF3UtY1MSvzpo5seCuzM5XO%2BKKMJCB20pcONvDdQeRe8VNkkLY06dGGG5Uzl15LE56AttrXg57E8d5ZDbgHB586cxBT1FaNUm%2BoTghpS3F3dOSg3QS3uc25UpAAP03X1Lnlgz06eYJWi5gtuO3Qr5wjFwcVFcLQfCL4xB53NMvE4GE8%2Bql71QVYkxOzJynCy%2BPGxyhR%2FC5yvtfA8%2FW9ddLO2dSq36zl%2FJ5Axky0Il3xsbfnNCT7oaenKPgArrxcmCP89jPj4nImG9NhvDMuQ1eS6EHAhKke52cpHu9K%2BMTeBNtXyEcYRVBHt4NE3BEZoSRnl8D%2BOta4h0wKeVnwBrnKkVIQ%2BTrYwAQYP0TEAcyGCzATDKSrTGOrK%2FslSke0ajTlAX3BQm56HAnj4A2jhWCQp1I9WnVz7IKBlhjY2wmAwIDxES6GMX2Oa9yQHjEoSRGh6%2FrMJzZj70GOqUBjjZKn1A9%2BvYhSDZUe661vhcAgXFrPFfagDhkADcjCiORddDR5N9YMRwcqMuwcc7GNNQxN7HKQQvpPNVQjt%2FH27t0PpaSNAJ67z9FlafDYpNmWLov13uQ6xYW71wxhtNISchQ08t0n9%2FqpITUF7Nu%2BIQXuKJ9Q3ZNqAbWMmqq5RudO2t6jCIglYnPFM3Q%2BqAViAPbP99hpJy%2BmUXsa4IjaZWtHSne&X-Amz-Signature=cbb58bfbc71c906fe6337d53ffc47e73511e14615754fb52e4d80ee1ffb84442&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Correlation Plot
Heatmap visualizes correlations among variables. Color scheme indicates Pearson correlation coefficients. Dark red diagonal line shows perfect correlation (value of 1) between variables and themselves.
This heatmap offers overview of variable relationships and their link with price.
![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/cd3b341e-cc1a-45f7-8aec-cdc00436d270/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662VDQIGNR%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T231409Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDcaCXVzLXdlc3QtMiJHMEUCIQDXmzuSCxB1dCK3DSg9wvnTPH6RVrnt9Vrfgg4zpGzt9AIgI7LQokZAOLcfFuDa2Ut7s%2BtREG7MTRcJRfXkgISORYoq%2FwMIUBAAGgw2Mzc0MjMxODM4MDUiDMNGMBIVZ%2FT%2Fp7h3PircA25NTSNMUclM7fWPRsc7Y0Wl71oeQ6AqemPhbzqesRTCi9Jufyd2y%2F2jfKoD5OTVQ%2BzKfTv1X22AiOkw08OnrlCw08qMwxZHzVkquULo5k38mRN2iC0xxQQQE4JaDTz%2FeGqFwJhlZ7KygI%2FybbEJbR8h3m1VlFLst5RYxXJOz9gqo0fuj9GeTX%2FF3UtY1MSvzpo5seCuzM5XO%2BKKMJCB20pcONvDdQeRe8VNkkLY06dGGG5Uzl15LE56AttrXg57E8d5ZDbgHB586cxBT1FaNUm%2BoTghpS3F3dOSg3QS3uc25UpAAP03X1Lnlgz06eYJWi5gtuO3Qr5wjFwcVFcLQfCL4xB53NMvE4GE8%2Bql71QVYkxOzJynCy%2BPGxyhR%2FC5yvtfA8%2FW9ddLO2dSq36zl%2FJ5Axky0Il3xsbfnNCT7oaenKPgArrxcmCP89jPj4nImG9NhvDMuQ1eS6EHAhKke52cpHu9K%2BMTeBNtXyEcYRVBHt4NE3BEZoSRnl8D%2BOta4h0wKeVnwBrnKkVIQ%2BTrYwAQYP0TEAcyGCzATDKSrTGOrK%2FslSke0ajTlAX3BQm56HAnj4A2jhWCQp1I9WnVz7IKBlhjY2wmAwIDxES6GMX2Oa9yQHjEoSRGh6%2FrMJzZj70GOqUBjjZKn1A9%2BvYhSDZUe661vhcAgXFrPFfagDhkADcjCiORddDR5N9YMRwcqMuwcc7GNNQxN7HKQQvpPNVQjt%2FH27t0PpaSNAJ67z9FlafDYpNmWLov13uQ6xYW71wxhtNISchQ08t0n9%2FqpITUF7Nu%2BIQXuKJ9Q3ZNqAbWMmqq5RudO2t6jCIglYnPFM3Q%2BqAViAPbP99hpJy%2BmUXsa4IjaZWtHSne&X-Amz-Signature=c6006bf86682f040fd23cd30562722db52be38883cb5891e03105c4d786556a9&X-Amz-SignedHeaders=host&x-id=GetObject)

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
