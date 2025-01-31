

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

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/997ac361-58a8-4f04-bb0f-79fea4baa761/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666KOV3GED%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T201529Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCtU5mWZxYMqSV6CCR7%2FShmkfsL3QxYGkfEnGhNooVwOAIhAN%2BcLfGN8A1LOgyzVDhUKbnMXgHFlgulr%2F9cZ%2FxuW0LwKogECMX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzS%2FxYiC%2BwJXCc0lBsq3APW8DjteLctyjMou1eJ2349pVVtz8l5CDQ3V5PrJXeyWImwOnklMNn%2BSMdP7X2QuQogg2ZEELKhQielpSqvIwyADQRkT7AEt0a9zB8L%2Ft1tW8XYrJJDcI%2BHlDni1TlMDgXmCppHXgXCnLcUrQDtPK7qK6ibSnJYlf8bpVShgO8Q2pW1E3irfXIy32u5%2By58mvkYI8h9j%2BVPgZPBKhBFD3ukAGzctF3lrgSye%2FP677dlw7ey80vK34TVy%2BrpaljSEgbRF87n7dljR0ph9c7OgF7lveHqqBv9wP2vNmmopQsqlDnMVkW2L3NcUCi5ILz6Ej1FjA3Ii0O5wdcmkIS1Xv4E1RPF1r2zN85ZkCl29a3q8tej2QutMEZvwK6sPdP6RzsvYMfm1zzwUXj9E6%2BySkEOivS1LS3Bv6G7RvE0IpldXOTmDIN853XQM6zmc1Ha1Rd%2BEfy%2B%2BO0MN3sFKjljaved%2FYHel%2BCHPTHffS2Kmfldt8hiEM7ijZi0AFBGUgYXCYOYSVm8vCTJlK4ljeL%2BOLE8XfWzqLBnXQk55j9%2B%2BSWdVaL2MS4KDpD%2B%2BnHn0ZUL7iAPix0QNkAo2r5imb6WCaddrF5srmUf3rFqv7zqWUx5IIjXNM4FQ1jhi6Zw%2BTCy2%2FS8BjqkAV92R425FZBR2g%2FztL5EvlVJRtgy31d9FsFuMu6hnAOykYk5720%2FNe9dtwmf%2FYYvwutZGNIPohz7jMyq9XXphnik0oiF1dAg7wFA1LUcKZ8G5sy6HRH1goUc5pG40QMmPezWJ4k3kXbzniCirW%2BA8AraHeODj3Gkxzwbah98NilN4KZqhN7YG8ml2nnW3jrEE4Qb1%2ByHeylB84%2FS%2F96KAEbur37X&X-Amz-Signature=79780cd389f81ef45ac005898495fc7a3dfad59cc79f192e93b464d7df3ca0c3&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Data Visualization Libraries
#### 1. **Matplotlib**
- **Description:** The most well-known library for data visualization.
- **Features:** Great for making highly customizable graphs and plots.
#### 2. **Seaborn**
- **Description:** A high-level visualization library based on Matplotlib.
- **Features:** Easy to generate various plots like heat maps, time series, and violin plots.

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/733d1e42-5a53-4fd8-90c1-3d85254369a6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TUMLTD5P%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T201528Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCEnP1cnKqKuWr4BNJ4E%2BzuzHsLCTDF3PTX92gVkgtTagIhAKpfDXOIcCjCUhzDHTcv60H%2B5MJY1yFO1reHQbPc7qGVKogECMX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyFWLQ%2BAnUn65sRBcMq3AMYQgXaPZWqZIzKV2Fk8FGjK9Ii4Yvuu9DW9TIo%2F6olRoQyGWdCPQF0TDA4TLcEVy%2FZEM%2F%2FI2R6KSn6t44MsQ%2FBVtcFDafalegTtuX994fxETJIksSCZiumopGgLx42OPYpnqezU6nXNbLW%2BXZ%2Fpum2o3VScKc8P4dSFn%2BSv112QpSCgvRIowZPzD7%2B97ThUDGz9DQEtWomC2hT1Q1ADqpM1cTRB6Zr4KAg%2BhY%2Ft%2FQcPLBHP1L6yhe9L41XQClNkdLd9dkMvoexwMrQ608tYaubNyBfnUuySshuG4XJsWkOpzx3c%2FKQlfjLdySyfDU7SEK4vcUwIrhn0mlX0zL94gyB3UAzmSXHaCG9AfBmqYkf8qz8IjsGvXHWSBc1Bcy9srVCRlBxOjL%2Bkn8egwzZU6r9NJRC0vDGXU3NMjcKWlgoZeQhQYzDgErneX8Wl%2F%2BxmY7SxyAOEwUg4Dl6HrvfIPT%2BCZ3GwMh2O%2BKw8A3hbLGA7e8Aenv%2FMjT%2BkANbPuDo3lLla0xBrYO86Z7YZikcdNhBeZwMd0af2rJmHoTdeuNKqX9cVZm9bocjOlgkLiC4s1TyJcDhxRfvdLBdeHaVW9BJJm08RFhxX3wLV6lzGjWcI1GasyKW7GE08uhggzCI3PS8BjqkAUIhjuqcBo6cerQYM8yjLqD8ax0T7UuyQn58EEZT65ZMqHXDm23SvAp5O2gl7momTf1Wsj8WzojZnY24ecr1boDu2cxehyZBAIXCaybdCebJEtIh7tePlqGIQ4XMuFEyXaudpYe2uoN526k7X16APH%2BuGC2%2FptgYZDmXUxEhmxCqVVHgQ%2B8jdeWy%2B9IzdfebUuqh53TizgSftLJCAIk3T6oNjdD7&X-Amz-Signature=f8f8933018e6fd470aaa7ed2b477a2a43a75651bdde4beeb22662e04e8a34209&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Algorithmic Libraries
#### 1. **Scikit-learn**
- **Description:** Contains tools for statistical modeling, including regression, classification, clustering, etc.
- **Built on:** NumPy, SciPy, and Matplotlib.
#### 2. **Statsmodels**
- **Description:** A module for exploring data, estimating statistical models, and performing statistical tests.

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c62885f5-417d-4179-834f-d68f8f2bdf39/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TUMLTD5P%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T201528Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCEnP1cnKqKuWr4BNJ4E%2BzuzHsLCTDF3PTX92gVkgtTagIhAKpfDXOIcCjCUhzDHTcv60H%2B5MJY1yFO1reHQbPc7qGVKogECMX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyFWLQ%2BAnUn65sRBcMq3AMYQgXaPZWqZIzKV2Fk8FGjK9Ii4Yvuu9DW9TIo%2F6olRoQyGWdCPQF0TDA4TLcEVy%2FZEM%2F%2FI2R6KSn6t44MsQ%2FBVtcFDafalegTtuX994fxETJIksSCZiumopGgLx42OPYpnqezU6nXNbLW%2BXZ%2Fpum2o3VScKc8P4dSFn%2BSv112QpSCgvRIowZPzD7%2B97ThUDGz9DQEtWomC2hT1Q1ADqpM1cTRB6Zr4KAg%2BhY%2Ft%2FQcPLBHP1L6yhe9L41XQClNkdLd9dkMvoexwMrQ608tYaubNyBfnUuySshuG4XJsWkOpzx3c%2FKQlfjLdySyfDU7SEK4vcUwIrhn0mlX0zL94gyB3UAzmSXHaCG9AfBmqYkf8qz8IjsGvXHWSBc1Bcy9srVCRlBxOjL%2Bkn8egwzZU6r9NJRC0vDGXU3NMjcKWlgoZeQhQYzDgErneX8Wl%2F%2BxmY7SxyAOEwUg4Dl6HrvfIPT%2BCZ3GwMh2O%2BKw8A3hbLGA7e8Aenv%2FMjT%2BkANbPuDo3lLla0xBrYO86Z7YZikcdNhBeZwMd0af2rJmHoTdeuNKqX9cVZm9bocjOlgkLiC4s1TyJcDhxRfvdLBdeHaVW9BJJm08RFhxX3wLV6lzGjWcI1GasyKW7GE08uhggzCI3PS8BjqkAUIhjuqcBo6cerQYM8yjLqD8ax0T7UuyQn58EEZT65ZMqHXDm23SvAp5O2gl7momTf1Wsj8WzojZnY24ecr1boDu2cxehyZBAIXCaybdCebJEtIh7tePlqGIQ4XMuFEyXaudpYe2uoN526k7X16APH%2BuGC2%2FptgYZDmXUxEhmxCqVVHgQ%2B8jdeWy%2B9IzdfebUuqh53TizgSftLJCAIk3T6oNjdD7&X-Amz-Signature=4dc202b4bdb3a1281aabfe920bbb65525380899891c23b053e6c42621bdb2a21&X-Amz-SignedHeaders=host&x-id=GetObject)
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
