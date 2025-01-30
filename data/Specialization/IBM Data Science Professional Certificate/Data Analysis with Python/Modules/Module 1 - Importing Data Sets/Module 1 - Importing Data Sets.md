

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

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/997ac361-58a8-4f04-bb0f-79fea4baa761/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663EOMBL4T%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T211326Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDQUPsX64YkTdCpjldMfUggTJb5zfotIzCSAVFaY%2FwkJwIgfPmAWixZEHab9%2BQ9wuMSJQh4tzSQWlJi%2FtB80K0ibbIqiAQIrv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKtghyBm47k58G2p%2FCrcA4XrGqnRqQASKH51a0bvtgwG%2Fi985W6YlhqRJ1QCJhi7q8oDpdqdYx2nBoHDHFVlpE%2BBdK0Az3VB%2Bu9SOCFmaT4AbhElfXdxPP72VNI4BDAbg5sgoPRGJRqqjDSZ0LCchLWw0h%2BR4XfQ58fdooxBsaaj0oCs%2FJ1Mlmrv%2Bp4DDryt7NEFEIaH%2FCL36kB0AsKOg%2FVkPAV4WxfUPrIEwvXTGmXixzaeeqnDp1AEzUpD3BCCNnR%2BQh9LHTS7gzcZnPov6i4jU6eNX9NZ8XplcqY5JerYP5Cu6hmPjJt85HFAbZa9EMuzsnIANhT0qq3lSAcl9BzLT06i6zUb0QEYpUydqE2eLM8dIgGH%2B5AZdWwmvVzGoUWKU%2BG5NAk9kEUruCb5GhvjcU6PYsDdCWpRXRwt64EXBH3XnhZNcQ%2BEgGF2IcyFEsUILU7vyb2nGELwlGTa4jmUF%2Bf2RgeZh4Mtplhnck82XwaHECndqZv5mQVeJ38CDNL%2BDcTkxRFWiJQtqwWMvwYkLBYU9yRvcHineOq%2Bhem%2FDPSQy8wOl3Je0fi5kG9vzM5fhSPtjxz%2BBcyNgzk%2Bd%2FyoLxhg3HIoDue3fSfgFXNUYjyUWjlgTJi6J9Tntuku%2BNSsEsRZeqQmbuZ4MMnF77wGOqUBBQElorbZ3Sw44MACCXdzqet7ImorZGY0p2xGbUV8sdXoIrfNElHVXms9m7BHODgchGwFSOm5iCPzQTpZfponcA5IdAcyn2eLZrCRe5DiO0pS80TKGO8NCtLd9LFrMjYxvIquVfoBSbYOtm%2FPbDZf1sUziKuw3%2Bad6NLcJtWMC1WUE6ymMVIct%2BGrJBhq0LaUnDEJtA%2FsMLYwHK03UanuDD8Yuufh&X-Amz-Signature=04579ddc36841f394c5e8696e7b9a25f07efca87384d3bdabc50d4a018b7ff51&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Data Visualization Libraries
#### 1. **Matplotlib**
- **Description:** The most well-known library for data visualization.
- **Features:** Great for making highly customizable graphs and plots.
#### 2. **Seaborn**
- **Description:** A high-level visualization library based on Matplotlib.
- **Features:** Easy to generate various plots like heat maps, time series, and violin plots.

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/733d1e42-5a53-4fd8-90c1-3d85254369a6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WEOKCCAM%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T211325Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIF1xseEqF8uIfNFkOhZDr5foMlJ57DOhUl6kJEkEF7wUAiA8%2BHIk%2BsQgBsXMjQ2ZCxX3qiuIISRy%2BqmfkVvI%2FbBBbCqIBAiu%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM5NFlnHn6%2BZN8NXViKtwD6pCAyfbjgqon%2BAXIG8XGpzzbuUY80OVjlQcgJZLHERFcQ8EomZp0ytQaMNB5R%2Fi06lLpYcp4JShNjfk4XzMl7TfzghWqlzjPO0fxbfVwtwM%2BW9H53J2JQGwvxpr85ndReB5gQ3mQSdwOREozuFMKLdmjxohKQ1ach54TwQ65YT0phJPNScF3fD1VFat6dhn2h3YmFT92vSH8evV4mLQuB9Pk733Zn0236K5xL4CGCwNdJmd7O4Sq6uc05an9BQrNhEByj8iZyg%2FJzLwcmjgd8aVde0zZyVvuNCYB5Hyg9V5ZBBcrm1vcDfqcyRqFaQQAO9Ga4Am4E6lVp4Uy3lGeHyMdJpKBJADJ8RK5RJiHpv%2B67dgvCeXCbH4N56o%2BRUnEDDkw%2Bz3ef0CF05PTs9IlxTxnC2piiBlTkO4ismTviPQXlTwrvDt1athg5mWVLOrULDIIYC49JsKzssIvUJGycLYtktHe0RIL2gVL07HsS0yMJMwSwXAgmxU4ZHxdbmluvBR1kaz5vqZd6gp6D2ynfvpwbbDxjK%2B2nTKaXhV%2B7IOjO3%2Ba4m%2F6MxAmik01bXCXiIbfjMjOr8AiXa3SRP%2Fll4OLXeDmV19yLRMX3M73sCHuBNtdzJMmjF8sM3gwpsXvvAY6pgF7vj3W%2B5IQekjJ6MYOq16LFXEgcMTTnkfE%2BfaACtxBViONSPJipUpZSKNJ5ijKI5Aq2qCz3XFqk1CkiN8OYFjywyL7EyKcY5c7%2BXi3smrW8UkG7by2F1MuF9MvrMtSRfTASyIQMZHU909caV0o%2BIwccByxudI5Jbi%2BeTvTHqdGqyKQHR2447bSoeLWO4x2BhJKuIvAb%2FnbiuzoM%2Bi7n0Hlls2Lq5lR&X-Amz-Signature=10b29d40d2c27a6597cefce2e9ca7962c7283481c2a9dda5809dd29c1e7e9947&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Algorithmic Libraries
#### 1. **Scikit-learn**
- **Description:** Contains tools for statistical modeling, including regression, classification, clustering, etc.
- **Built on:** NumPy, SciPy, and Matplotlib.
#### 2. **Statsmodels**
- **Description:** A module for exploring data, estimating statistical models, and performing statistical tests.

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c62885f5-417d-4179-834f-d68f8f2bdf39/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WEOKCCAM%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T211325Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIF1xseEqF8uIfNFkOhZDr5foMlJ57DOhUl6kJEkEF7wUAiA8%2BHIk%2BsQgBsXMjQ2ZCxX3qiuIISRy%2BqmfkVvI%2FbBBbCqIBAiu%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM5NFlnHn6%2BZN8NXViKtwD6pCAyfbjgqon%2BAXIG8XGpzzbuUY80OVjlQcgJZLHERFcQ8EomZp0ytQaMNB5R%2Fi06lLpYcp4JShNjfk4XzMl7TfzghWqlzjPO0fxbfVwtwM%2BW9H53J2JQGwvxpr85ndReB5gQ3mQSdwOREozuFMKLdmjxohKQ1ach54TwQ65YT0phJPNScF3fD1VFat6dhn2h3YmFT92vSH8evV4mLQuB9Pk733Zn0236K5xL4CGCwNdJmd7O4Sq6uc05an9BQrNhEByj8iZyg%2FJzLwcmjgd8aVde0zZyVvuNCYB5Hyg9V5ZBBcrm1vcDfqcyRqFaQQAO9Ga4Am4E6lVp4Uy3lGeHyMdJpKBJADJ8RK5RJiHpv%2B67dgvCeXCbH4N56o%2BRUnEDDkw%2Bz3ef0CF05PTs9IlxTxnC2piiBlTkO4ismTviPQXlTwrvDt1athg5mWVLOrULDIIYC49JsKzssIvUJGycLYtktHe0RIL2gVL07HsS0yMJMwSwXAgmxU4ZHxdbmluvBR1kaz5vqZd6gp6D2ynfvpwbbDxjK%2B2nTKaXhV%2B7IOjO3%2Ba4m%2F6MxAmik01bXCXiIbfjMjOr8AiXa3SRP%2Fll4OLXeDmV19yLRMX3M73sCHuBNtdzJMmjF8sM3gwpsXvvAY6pgF7vj3W%2B5IQekjJ6MYOq16LFXEgcMTTnkfE%2BfaACtxBViONSPJipUpZSKNJ5ijKI5Aq2qCz3XFqk1CkiN8OYFjywyL7EyKcY5c7%2BXi3smrW8UkG7by2F1MuF9MvrMtSRfTASyIQMZHU909caV0o%2BIwccByxudI5Jbi%2BeTvTHqdGqyKQHR2447bSoeLWO4x2BhJKuIvAb%2FnbiuzoM%2Bi7n0Hlls2Lq5lR&X-Amz-Signature=3456bf808da9c058ee83b46d62c3ea6f64c27863f8c9dbe8ee23c2bab191aba9&X-Amz-SignedHeaders=host&x-id=GetObject)
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
