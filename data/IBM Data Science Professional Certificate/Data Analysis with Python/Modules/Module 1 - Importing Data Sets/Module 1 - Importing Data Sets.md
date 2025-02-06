

# Module 1: Importing Data Sets
## Data Science with Python - Key Libraries
Python libraries are collections of functions and methods that allow performing various actions without writing extensive code. They offer built-in modules for different functionalities, providing a broad range of facilities.
#### Categories of Python Data Analysis Libraries:
1. **Scientific Computing Libraries**
2. **Data Visualization Libraries**
3. **Algorithmic Libraries**

___
### Scientific Computing Libraries
#### 1. **Pandas**
- **Description:** Offers data structures and tools for effective data manipulation and analysis.
- **Primary Instrument:** DataFrame (a two-dimensional table with column and row labels).
- **Features:** Fast access to structured data, easy indexing functionality.
#### 2. **NumPy**
- **Description:** Uses arrays for inputs and outputs, can be extended to objects for matrices.
- **Features:** Fast array processing with minor coding changes.
#### 3. **SciPy**
- **Description:** Includes functions for advanced math problems and data visualization.
- **Features:** Solves complex mathematical problems.

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/997ac361-58a8-4f04-bb0f-79fea4baa761/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WLP5HD3V%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T051551Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjED0aCXVzLXdlc3QtMiJGMEQCICizxMxaC%2BvG2CfE4hW1LXDdGvElCo0OCXmYCtChdtvkAiBI5alVDHJl6UBC%2F7jPoQUIdV1WWSNW1gzJnkiYJGwYUCr%2FAwhWEAAaDDYzNzQyMzE4MzgwNSIMyF3nuiA4EwD%2FcWBXKtwDC6BZcPYSctLR8ce%2FA%2BBTOPiG6L5U0VhY5ywL7cJDZERbRxSjAZUF%2FpnVUHBMjcOR35mt50HyctpX1G8OZLHLl%2Ftfucf%2FXAn4OOvp41Q2kDUfNEDdui%2BaOJ%2Frd1qA5kzikHBpfasJQzw6IKvc%2F%2Bvt17hKVVy0b6pu7PJLDyOJG%2BvmIG3PrFCF84ssMg4DBIM%2Fi1qtCeUouhmpMYR7qEe5yjG32m7BCIHn34pY3iwhzfMigFB8FdNY4fYOuyIHdQGPigditVWyB01stYsdGtHOdqRQMPTTvc7adjpc5NSpLnuGcvTz9AMtLZqeTYF80VtdBL63cRYtzdTr42bSmkOWDYjnIApvLMktEUIg0XixCZXf6xj5Aj9KdhPuXy2yhegc8Ftt%2FB63v2AAt2IsNA1mzkTz3gT9Lj4dSy8Jj%2Bmen%2BaH14E9dTN4zVM5pFrqQj0AL06gU4aAVDiVXUnmhSMB95I7kzavKvSGlXxrNErkva7a96jszvZQfBvukGL7VuMF5D9IYaLfcU2sRJBG8vmh78EW0Fs4T7y8QpZwlDFyta5h7YCPpZLcoFgM481KQBbaZf%2BV%2Fkz0mOe3%2BLtTr2ibVI0n2z4%2F4xbHGUAeFf923q%2BQ0TY%2FI%2FK8OWwbgMgw0%2FuQvQY6pgElsvTrnpwDJadDm7F%2BJ3QelYMYk%2FH0QkHqs9jKMnE0Wyg8czXCw3yhauALZGQ6ppn4JHD7A2MQUD7W4DzL35yrDLyDsGRvWfTtxxj%2FitVeBBv18dO7DNCT0Jm8G9zPVrjjvjO3GCQm8AUHUIxPwJUixCrrJKMWKdK0EJwCL8r9Vq7UAOgolBbc%2BDGSCxD8Az6nc8TQS%2FQQZFJXxwJ5wjiVA3Q4bPTA&X-Amz-Signature=a57562f5f044b8e4f824aa20e199d90cfdf3ab376dfbcfcb85eaf677976151bd&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Data Visualization Libraries
#### 1. **Matplotlib**
- **Description:** The most well-known library for data visualization.
- **Features:** Great for making highly customizable graphs and plots.
#### 2. **Seaborn**
- **Description:** A high-level visualization library based on Matplotlib.
- **Features:** Easy to generate various plots like heat maps, time series, and violin plots.

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/733d1e42-5a53-4fd8-90c1-3d85254369a6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666WEB5Q65%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T051551Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjED0aCXVzLXdlc3QtMiJHMEUCIQDjaBzriAY4mJcja3cBci61PfDAGrtRoL8KvIFWp2u3%2FgIgaMaExXb%2Fynq%2F69VeEiWxk5Z%2FQbIBcqP7yjkA8mmBpQ8q%2FwMIVhAAGgw2Mzc0MjMxODM4MDUiDOmQP8MT29HJbyrLYircA0JOXNgAj2QCrWfCPeyvQ0M55JYiBDKb82swxa8k4IHRvZK%2BJPXaDheySqQ%2FbztVrnfyl0uvewSl%2FrVWbuHb4Z%2B6zEpVorLlss858knCs5DUnKTc5EGeZ0UxCNLfLISAQc7pEC4aR8Q%2FkDMVbB4s6YCev3lG64yQ1Zdf2AphmkHZVu30k4o4qnFLclmdrGC9dw9tBFOswWp1Xe8MILjR93hmQrShxNR3xMkmtSlHHTwtHqUkIuOE37XYhYwsRphl9paJAw0e7FqQYx3xnvoC%2BrVd7EAd1x94WEr7jXbUyijI9Jer0TljvB2y7ls65pWwTvQsjhUA0cAQYfNFwFKrupjQVgb%2FY%2F4cJWKZ%2Fazwa7dyOMe7m%2BbnOwikyarlb4aijv7mtQfAPU%2FwoBKu9gOb9N%2B8ErmTmg1PlOW2Chi2g1fGb6uNFWILpwGN82afMiQhW86orUnbLsazWkZTwIpy4eOuF4SNanz6D5S26Tr497BG18VK6MIJZo024fWhnaKhuKKAdZVwKLh%2B5CfPxcSAlhycGPt4JElfX2yTwm8hZeS07TOMgp%2Fg%2BVX%2B%2FOttlBZQfOI66FFJI52EmeaZMvE0dppoX3vLnvA52b4XkBR9X9J2%2F2fiUKgPH0OmQ1FpMIb8kL0GOqUBT4kwF5c%2BrgiiJAx0dclHy1Rv%2BqkHtr2UahyxnNi675qLw8%2FpJLa9Od4ZRXMrq6VGib9GGh3m7%2FXK2%2B%2FWE4xRBtv1yaasG5L5WrjTTw%2BcBfdQN8dmeym5V4Kvl18hsrNaZXANF6trkfgHbrZSP4owXhTCSlOSH4ahQSxr8zXpmBrWEPTz0ryQuSnhHBWbRzU0YVAbmbLDggiW0LrAhPYFuXchfTR7&X-Amz-Signature=eda7d2012230ee5232e2c86f820f0f3d859df4fde3fafaa0e0a72f101c786f59&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Algorithmic Libraries
#### 1. **Scikit-learn**
- **Description:** Contains tools for statistical modeling, including regression, classification, clustering, etc.
- **Built on:** NumPy, SciPy, and Matplotlib.
#### 2. **Statsmodels**
- **Description:** A module for exploring data, estimating statistical models, and performing statistical tests.

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c62885f5-417d-4179-834f-d68f8f2bdf39/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666WEB5Q65%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T051551Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjED0aCXVzLXdlc3QtMiJHMEUCIQDjaBzriAY4mJcja3cBci61PfDAGrtRoL8KvIFWp2u3%2FgIgaMaExXb%2Fynq%2F69VeEiWxk5Z%2FQbIBcqP7yjkA8mmBpQ8q%2FwMIVhAAGgw2Mzc0MjMxODM4MDUiDOmQP8MT29HJbyrLYircA0JOXNgAj2QCrWfCPeyvQ0M55JYiBDKb82swxa8k4IHRvZK%2BJPXaDheySqQ%2FbztVrnfyl0uvewSl%2FrVWbuHb4Z%2B6zEpVorLlss858knCs5DUnKTc5EGeZ0UxCNLfLISAQc7pEC4aR8Q%2FkDMVbB4s6YCev3lG64yQ1Zdf2AphmkHZVu30k4o4qnFLclmdrGC9dw9tBFOswWp1Xe8MILjR93hmQrShxNR3xMkmtSlHHTwtHqUkIuOE37XYhYwsRphl9paJAw0e7FqQYx3xnvoC%2BrVd7EAd1x94WEr7jXbUyijI9Jer0TljvB2y7ls65pWwTvQsjhUA0cAQYfNFwFKrupjQVgb%2FY%2F4cJWKZ%2Fazwa7dyOMe7m%2BbnOwikyarlb4aijv7mtQfAPU%2FwoBKu9gOb9N%2B8ErmTmg1PlOW2Chi2g1fGb6uNFWILpwGN82afMiQhW86orUnbLsazWkZTwIpy4eOuF4SNanz6D5S26Tr497BG18VK6MIJZo024fWhnaKhuKKAdZVwKLh%2B5CfPxcSAlhycGPt4JElfX2yTwm8hZeS07TOMgp%2Fg%2BVX%2B%2FOttlBZQfOI66FFJI52EmeaZMvE0dppoX3vLnvA52b4XkBR9X9J2%2F2fiUKgPH0OmQ1FpMIb8kL0GOqUBT4kwF5c%2BrgiiJAx0dclHy1Rv%2BqkHtr2UahyxnNi675qLw8%2FpJLa9Od4ZRXMrq6VGib9GGh3m7%2FXK2%2B%2FWE4xRBtv1yaasG5L5WrjTTw%2BcBfdQN8dmeym5V4Kvl18hsrNaZXANF6trkfgHbrZSP4owXhTCSlOSH4ahQSxr8zXpmBrWEPTz0ryQuSnhHBWbRzU0YVAbmbLDggiW0LrAhPYFuXchfTR7&X-Amz-Signature=23591450c5a183a5a0e3b507ff1fa326499224ca76f843542c15afe90c0fca08&X-Amz-SignedHeaders=host&x-id=GetObject)
___
## Reading Data with Pandas
Data acquisition is the process of loading and reading data into a notebook from various sources. Using Python’s Pandas package, we can efficiently read and manipulate data.
#### Key Factors:
4. **Format:** The way data is encoded (e.g., CSV, JSON, XLSX, HDF).
5. **File Path:** The location of the data, either on the local computer or online.
### Steps to Read Data with Pandas
#### 1. **Import Pandas**
```python
import pandas as pd
```
#### 2. **Define File Path**
Specify the location of the data file.
```python
file_path = 'path_to_your_file.csv'
```
#### 3. **Read CSV File**
Use the `read_csv` method to load data into a DataFrame.
```python
df = pd.read_csv(file_path)
```
#### Special Case: No Headers in CSV
If the data file does not contain headers, set `header` to `None`.
```python
df = pd.read_csv(file_path, header=None)
```
#### 4. **Inspect the DataFrame**
Use `df.head()` to view the first few rows of the DataFrame.
```python
print(df.head())
```
Use `df.tail()` to view the last few rows.
```python
print(df.tail())
```
#### 5. **Assign Column Names**
If the column names are available separately, assign them to the DataFrame.
Verify by using `df.head()` again.
```python
print(df.head())
```
#### 6. **Export DataFrame to CSV**
To save the DataFrame as a new CSV file, use the `to_csv` method.
```python
df.to_csv('output_file.csv', index=False)
```
### Additional Formats
Pandas supports importing and exporting of various data formats. The syntax for reading and saving different data formats is similar to `read_csv` and `to_csv`.
___
## Exploring and Understanding Data with Pandas
Exploring a dataset is crucial for data scientists to understand its structure, data types, and statistical distributions. Pandas provides several methods for these tasks.
#### Data Types in Pandas
Pandas stores data in various types:
- **object**: String or mixed types
- **float**: Numeric with decimals
- **int**: Numeric without decimals
- **datetime**: Date and time
#### Checking Data Types
Use `dtypes` to view data types of each column:
```python
print(df.dtypes)
```
#### Statistical Summary
Use `describe` to get statistical summary:
```python
print(df.describe())
```
- **Count**: Number of non-null values
- **Mean**: Average value
- **std**: Standard deviation
- **min/max**: Minimum and maximum values
- **25%/50%/75%**: Quartiles
**Output Example:**
```plain text
              0            1            2            3
count  205.000000  205.000000  205.000000  205.000000
mean    13.071707   25.317073  198.313659    3.256098
std      6.153123   26.021249   90.145293    1.125947
min      5.000000    4.000000   68.000000    2.000000
25%      9.000000    8.000000  113.000000    2.000000
50%     12.000000   19.000000  151.000000    3.000000
75%     16.000000   37.000000  248.000000    4.000000
max     35.000000  148.000000  540.000000    8.000000
```
To include all columns:
```python
print(df.describe(include='all'))
```
**Output Example:**
```r
              0           1          2          3       ...      25       26       27
count   205.000000  205.000000  205.000000  205.000000  ...     205      205      205
unique        NaN         NaN         NaN         NaN   ...     25       25       25
top           NaN         NaN         NaN         NaN   ...     value    value    value
freq          NaN         NaN         NaN         NaN   ...     10       10       10
mean     13.071707   25.317073  198.313659    3.256098  ...     NaN      NaN      NaN
std       6.153123   26.021249   90.145293    1.125947  ...     NaN      NaN      NaN
min       5.000000    4.000000   68.000000    2.000000  ...     NaN      NaN      NaN
25%       9.000000    8.000000  113.000000    2.000000  ...     NaN      NaN      NaN
50%      12.000000   19.000000  151.000000    3.000000  ...     NaN      NaN      NaN
75%      16.000000   37.000000  248.000000    4.000000  ...     NaN      NaN      NaN
max      35.000000  148.000000  540.000000    8.000000  ...     NaN      NaN      NaN
```
For object columns, it shows additional statistics like the number of unique values, the most frequent value (top), and its frequency (freq).
#### DataFrame Info
Use `info` for a concise summary:
```python
df.info()
```
- Shows index, data types, non-null counts, and memory usage.
**Output Example:**
```less
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 205 entries, 0 to 204
Data columns (total 11 columns):
 #   Column  Non-Null Count  Dtype
