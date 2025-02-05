

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

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/997ac361-58a8-4f04-bb0f-79fea4baa761/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZAXBE4KK%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T132043Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECsaCXVzLXdlc3QtMiJIMEYCIQDNV7v%2FJdbqD%2B21Ws8DifuxCCZS5B%2Be9eCX%2F5zzri5L4QIhAMvdY8fFZdBjMEQxs9ZobNpLkpFpSumhdGf92Wa9AZg%2FKv8DCEQQABoMNjM3NDIzMTgzODA1Igx7pxVHyy2zDsQB9E8q3AP8K7GXCzCJGyVrOKm4Vzze2%2Bk0jGEhlaRj2VZKVvODqzprfTi3jEhIPULgrvypI84DdOI6s%2Fl4StAw0YGa74qbVQbkDL8fDuPsk%2FXSJqxFG7Z1fgbbai8d%2B2g5SuHt7WK%2F85VGq1XJl7MKbiSYkubPBEr%2FynshvNmpZ5T1B8WBv2bYflxjehrw06colVoUzn3zydPMwqqGhTkdEC15LBeJMnJ8DFohsg1TWoGf3ZAKES%2FXbU5p5VH6MxFarBM7VBM%2FnG4Bp23B8Yug3F%2Bnu1NFHDEWiiAVT7gOXsYLsMd0fGrvuP0xDJVFE%2BkRjEAuaHh2O1yL8eNUoXAYTP0huG46sIiBcw4CR%2ByEeWq%2F%2BxjD8lLOllhF7s9VcU8BhborKuz6LrFaxPzh7gRu4dOXLN2v2oWtjMonxXOcmOp88gdbRi7MF3Cw0iCAWwUb09RINoaHLj4XR4Xc2hARsHcH7emO53F6Xa0VFMTtER%2BekVT2DXL1SO8C8aricS%2BKmF6CwHCmlxIZ1Y5TfEUnb1UOauKneoVYCbkFusPKzz8tsoIQ0RTj%2FuBe8piiS1Zull5iLYwO0Icw1qmKGf%2F%2Ffop20bE7RrzzrBBm63Rtqehe7R3MHoVSB1nTXkz5tssSDjDnio29BjqkATyxt2RpylJAv3XTcfZUkqk3L7jz5jfDHeNn0zyFWNotbmviWwuDcGwKZRrLiJbT4jOflmtHElDq%2BDLOVf8b2YnExpJKU6UVVhTN36GwfuKaPUdITfrkgNQnhSKl1y%2FE7KQ5Xs41W6sfQnl89NDBeEyblB%2Bfv8UtvzwXY3u%2BXC9a561NPnH%2F%2BXBTf5Of2AnNVtudzKfyTrDsAk2waFutH8eCvHC%2B&X-Amz-Signature=bc92c64da18ebd543fea76b9f16d33d9836ac4ad600e5170102b8e6a07579fdb&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Data Visualization Libraries
#### 1. **Matplotlib**
- **Description:** The most well-known library for data visualization.
- **Features:** Great for making highly customizable graphs and plots.
#### 2. **Seaborn**
- **Description:** A high-level visualization library based on Matplotlib.
- **Features:** Easy to generate various plots like heat maps, time series, and violin plots.

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/733d1e42-5a53-4fd8-90c1-3d85254369a6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UUXG7TUP%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T132042Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECsaCXVzLXdlc3QtMiJHMEUCIGJHjMihehaH0XGokFvPn3OpwOOW9wp%2B8eea8bhFZaabAiEA%2FdpyYNFqSa3vaTI4ldHEzuG0Cq%2Fq5NiP1%2F%2FIZ2LVh1cq%2FwMIRBAAGgw2Mzc0MjMxODM4MDUiDGCDl5Eb79CP3XPmsyrcA7Rkhw%2FDDo9zjf1jY%2FoJMv5%2BO42bweyXgrxdlsLtoxWz%2FM9LoU67KKrzEtDqXxz39AjjaxpGFO0bsmca4VQiW64fhb7Hr9GIp9hrO7hXRTldv3%2B3QxB3DPExZmwDLCQQATzPPnW%2BGZEB9yuCpTiuSzfzbPoTIXI55NxovcyVDc6CgRerzc%2F95pHEupnWbvYTEJ46KFaYjSP2XZOj4yCnoYxpSKtHB7kiSm7XT%2FAxHfSLSLAbUWwevMOYQgZ%2BR9Su7mFLeBJ9OwJovDuS%2BqbweD5%2FQpl5ZNVr%2Ff1VqTBWrmkmL4q39xIAXHwOtbV9YK0mHVCtYSJEFHJPWbDLHe8yxxHVzZCxdkL0Tpetf0ehvJ4AouAzyyhxsBEnV07ricvD6wrhO7Ic%2BlVEdq171jRxoHSsTjregpBT6KbagFD5xjocnro6gYUZNrSJyfQk9hlmtac3FZ6cgYswT%2B9GoUs2Xg2vyWaT0FZfan9ecbbbAtt0SD49jEOKota7xG6hSafB30LfWPT0yGCU8iX2Nwc8D2ZcvbfAZL2vZVOe4AA%2BzfUgf%2B9UBRaRYwX6kyuY3J9yN6Dj2b8Q3YOh0fe%2FVWhVSYr1S3Zx7LBZYRQE%2BjmTag5g%2B%2BZVK1YGKIyxaC2BMNWKjb0GOqUBqXoix8tTEQ7wHDUU57beWx7WPrTmsZf%2F0taASIrUxT8z3LZis%2F6uxBS9qZh%2BzyPY4Y%2FZMPNqL0%2F1Gct5SYo4bnowh1XI%2B%2BWK%2FKbln6UkK9m3cvBoLn4%2FR9K4nhJ0v%2FXqw7d4G758p942cuZ7q%2FmN8up7qyBgFfC2DpCWM5zj4cVktj%2F%2BNxooFh2d%2FVbBCu8S3LWZoO9dffEFwwhPmzGPyr2lSf45&X-Amz-Signature=c77ccf5b46e48ec2ab32141421c46157d86c9a6a375994433032a6bc9bb45914&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Algorithmic Libraries
#### 1. **Scikit-learn**
- **Description:** Contains tools for statistical modeling, including regression, classification, clustering, etc.
- **Built on:** NumPy, SciPy, and Matplotlib.
#### 2. **Statsmodels**
- **Description:** A module for exploring data, estimating statistical models, and performing statistical tests.

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c62885f5-417d-4179-834f-d68f8f2bdf39/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UUXG7TUP%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T132042Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECsaCXVzLXdlc3QtMiJHMEUCIGJHjMihehaH0XGokFvPn3OpwOOW9wp%2B8eea8bhFZaabAiEA%2FdpyYNFqSa3vaTI4ldHEzuG0Cq%2Fq5NiP1%2F%2FIZ2LVh1cq%2FwMIRBAAGgw2Mzc0MjMxODM4MDUiDGCDl5Eb79CP3XPmsyrcA7Rkhw%2FDDo9zjf1jY%2FoJMv5%2BO42bweyXgrxdlsLtoxWz%2FM9LoU67KKrzEtDqXxz39AjjaxpGFO0bsmca4VQiW64fhb7Hr9GIp9hrO7hXRTldv3%2B3QxB3DPExZmwDLCQQATzPPnW%2BGZEB9yuCpTiuSzfzbPoTIXI55NxovcyVDc6CgRerzc%2F95pHEupnWbvYTEJ46KFaYjSP2XZOj4yCnoYxpSKtHB7kiSm7XT%2FAxHfSLSLAbUWwevMOYQgZ%2BR9Su7mFLeBJ9OwJovDuS%2BqbweD5%2FQpl5ZNVr%2Ff1VqTBWrmkmL4q39xIAXHwOtbV9YK0mHVCtYSJEFHJPWbDLHe8yxxHVzZCxdkL0Tpetf0ehvJ4AouAzyyhxsBEnV07ricvD6wrhO7Ic%2BlVEdq171jRxoHSsTjregpBT6KbagFD5xjocnro6gYUZNrSJyfQk9hlmtac3FZ6cgYswT%2B9GoUs2Xg2vyWaT0FZfan9ecbbbAtt0SD49jEOKota7xG6hSafB30LfWPT0yGCU8iX2Nwc8D2ZcvbfAZL2vZVOe4AA%2BzfUgf%2B9UBRaRYwX6kyuY3J9yN6Dj2b8Q3YOh0fe%2FVWhVSYr1S3Zx7LBZYRQE%2BjmTag5g%2B%2BZVK1YGKIyxaC2BMNWKjb0GOqUBqXoix8tTEQ7wHDUU57beWx7WPrTmsZf%2F0taASIrUxT8z3LZis%2F6uxBS9qZh%2BzyPY4Y%2FZMPNqL0%2F1Gct5SYo4bnowh1XI%2B%2BWK%2FKbln6UkK9m3cvBoLn4%2FR9K4nhJ0v%2FXqw7d4G758p942cuZ7q%2FmN8up7qyBgFfC2DpCWM5zj4cVktj%2F%2BNxooFh2d%2FVbBCu8S3LWZoO9dffEFwwhPmzGPyr2lSf45&X-Amz-Signature=c058645dcaca589307fc99862f32d9c7ada7eac4e402f2c7034c8fa8c2a6aecb&X-Amz-SignedHeaders=host&x-id=GetObject)
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
