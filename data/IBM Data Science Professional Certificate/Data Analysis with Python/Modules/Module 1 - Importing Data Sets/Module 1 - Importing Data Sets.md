

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

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/997ac361-58a8-4f04-bb0f-79fea4baa761/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663Z5A3G56%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T041735Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQD3UG%2BTT73%2FuXR%2FsnmXw5ecJmWsCFRHiGqq27ws5REd1QIhANA9RCzg2SEvNk7%2FcV1kaPMpOqBFyKXiAqM8r87sG%2B3fKogECPv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxQhqm4kSn6rvZp8boq3AMMbl9xGkXxqLU8XMF2Ox9IuO6c7m0%2BEYgjuqOtxt1xVbwt05926NGMT01R8cAGeYitkMbmtTLBE2aoO0k1wH1MtzIIZzJXxc0XHjFVKKtDjAVFp9B6tJ8nLR548hiz%2BZZwuQUqOvfqrgVe4EfBgHmseO2apUr%2F1KXlNPg6cw%2FodozfT9LFGvOTt%2FjEmQ39A0eub%2B0ZLOPGYiKQFzwGuL26awpDVNv9jxEWJvrxQyv8kginPobC7fbb82cem695E1SvHYbKl%2FCwTDUNuTzqC9ieL3qe8gHzNQ3OSFFLBesLP7GbDZ1K17zHhtTjGgbnzMBd0O%2B9MdwO3MHZj1fFxASRbuHoLwl7muNGuYsdTxWMLY2Iyi92gjdXLovhNMvlC3PIJ9m2cbT283v50XuRSXoC6Rx%2BVtP%2F2UuVhH8e9dL1KG2F9THUqkTPiyy0Rlrw19hnaLbMXUBDiJvgwosKT1tECjkt1ADVxhqrqfLDITlr9QUoDtuZsaB6aSBpdqxB4IRC%2Fhg6nFe9BIE%2FW21DJ0C3HFO64DBxQk6%2F%2BUBV5DR4vjA8BTWWE%2FM0sB4vvaHiyIiHTM7SoAC3oTtPEEPJLu%2BJa7ZEQ%2BfjnVkBldABCFO7drwqYx6QKVnan519KTDMv4C9BjqkAQQV5bf%2BpuVSEpFtd9kZ0EMjohaxgj8uHCJsmWv3XHiRzwPxr0FC2GG5A0k4AWC%2BFWVYy6aI7qFqdPb1cRwiO95Dpb5fD4hxad0Ayp0wYWkdiPGHQmMK2M6seoEqZ5mU7gk1mhOUNie5Siq2u8vzkJESTSzlwrJZKgJBmwqaTdoH5dJ%2F8Ckn%2FDP3WeNDLWoUmUfTuKQMSS7KX8l9uFmLcDVwGoxY&X-Amz-Signature=d10eecf1bb4e2348d423ca6cd60e23d6725b6f3db6e363cf2e395d3a1dc4782b&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Data Visualization Libraries
#### 1. **Matplotlib**
- **Description:** The most well-known library for data visualization.
- **Features:** Great for making highly customizable graphs and plots.
#### 2. **Seaborn**
- **Description:** A high-level visualization library based on Matplotlib.
- **Features:** Easy to generate various plots like heat maps, time series, and violin plots.

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/733d1e42-5a53-4fd8-90c1-3d85254369a6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YMCYDG44%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T041734Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDAtzlkgxFjfNSz1qV3JoLUlSxOsfSjXc5qq03Itl1v2QIhALV%2FOgjgrYG18SwNqsD%2BxqTtzPYzZ96Qm2x5Wog4nudLKogECPv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igy6%2Bd3GrHVUtbuy%2Fzgq3AO3Q0Rt8%2Bo%2FuAuLXbBHZIz%2Bbz01PO8OOgD3Xo75qnvbaRst4%2B21OrFGsjDYYE925dy6Q3MWxMIkKXFusfCKhRy%2FIhZgFMmpnmkWjkfNgbjq2JQy747V3SgQjh5zBPK95OkgzA%2BLSoZkUusLc5ePafukTn6WlqQU37z0OJThMn33cvQocZYOjt9w13ayx0tAq1pNU%2FFvThlkv%2BhUssI2Y69s3dBS3GDBc%2B4jNGZ8HozFqDtfGzmmAw%2FW3a5JaSoo1bzlENumiQCPGmzsaeE1puPdKu%2FVfXQA72olnO4bG%2Fv3dA4rjGc21SZsXRUJjLOTt70kIve7j9EfeijIW%2B2hGvtYht%2BsfXA8Jsz6ysPeAVZePG5wmzJFUYOexgpYgHxhJqoqtJgJ%2BK5aGvIpup1iPSQrs0Qzlg7VIqm%2F3Tp4CXPAuk90XXDmkNkhWWG6kVZw1MZXK%2BxcO3FKI%2Fl74YH1Tv2VHuXYrBlpT5BtV3lTNkaiEAobkXzMUNRbh3ExTZ1%2F6LN8LFD9xB8jNuGclf1KaDxckZPjG16AUMx0Zak%2BLMkTF7Bq07RzCKpv%2B1fTGHT6RTzU%2FYhBqT9k1RZpwzeZivnL7b%2FwlO4L8g%2Bh3TOhGogoN30VAzMlcKxeh12YnzC0v4C9BjqkATOSS0m3XqSILuq7vMWG9buUichLXWF31A9CoZDj1wnNKw5pvCu5GG%2Brq6rv11PKI8b2%2F7HWB7zE0aH66VLBr8LtuOmzniJneHcWIoD9wvh8ReVPMT8bKEjcCROusEDLWgoiZou8LpVol%2FafdA6dKoSFEM0kXy7XLVvVozSMreuqxlifF2lk8RekiPytn2Dd8tCOg767T90Vse7POAJ1J%2B6BbFj9&X-Amz-Signature=f63bee0097f815c520b564ef12b3a68413dce80333735f02eea3436508f97884&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Algorithmic Libraries
#### 1. **Scikit-learn**
- **Description:** Contains tools for statistical modeling, including regression, classification, clustering, etc.
- **Built on:** NumPy, SciPy, and Matplotlib.
#### 2. **Statsmodels**
- **Description:** A module for exploring data, estimating statistical models, and performing statistical tests.

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c62885f5-417d-4179-834f-d68f8f2bdf39/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YMCYDG44%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T041734Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDAtzlkgxFjfNSz1qV3JoLUlSxOsfSjXc5qq03Itl1v2QIhALV%2FOgjgrYG18SwNqsD%2BxqTtzPYzZ96Qm2x5Wog4nudLKogECPv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igy6%2Bd3GrHVUtbuy%2Fzgq3AO3Q0Rt8%2Bo%2FuAuLXbBHZIz%2Bbz01PO8OOgD3Xo75qnvbaRst4%2B21OrFGsjDYYE925dy6Q3MWxMIkKXFusfCKhRy%2FIhZgFMmpnmkWjkfNgbjq2JQy747V3SgQjh5zBPK95OkgzA%2BLSoZkUusLc5ePafukTn6WlqQU37z0OJThMn33cvQocZYOjt9w13ayx0tAq1pNU%2FFvThlkv%2BhUssI2Y69s3dBS3GDBc%2B4jNGZ8HozFqDtfGzmmAw%2FW3a5JaSoo1bzlENumiQCPGmzsaeE1puPdKu%2FVfXQA72olnO4bG%2Fv3dA4rjGc21SZsXRUJjLOTt70kIve7j9EfeijIW%2B2hGvtYht%2BsfXA8Jsz6ysPeAVZePG5wmzJFUYOexgpYgHxhJqoqtJgJ%2BK5aGvIpup1iPSQrs0Qzlg7VIqm%2F3Tp4CXPAuk90XXDmkNkhWWG6kVZw1MZXK%2BxcO3FKI%2Fl74YH1Tv2VHuXYrBlpT5BtV3lTNkaiEAobkXzMUNRbh3ExTZ1%2F6LN8LFD9xB8jNuGclf1KaDxckZPjG16AUMx0Zak%2BLMkTF7Bq07RzCKpv%2B1fTGHT6RTzU%2FYhBqT9k1RZpwzeZivnL7b%2FwlO4L8g%2Bh3TOhGogoN30VAzMlcKxeh12YnzC0v4C9BjqkATOSS0m3XqSILuq7vMWG9buUichLXWF31A9CoZDj1wnNKw5pvCu5GG%2Brq6rv11PKI8b2%2F7HWB7zE0aH66VLBr8LtuOmzniJneHcWIoD9wvh8ReVPMT8bKEjcCROusEDLWgoiZou8LpVol%2FafdA6dKoSFEM0kXy7XLVvVozSMreuqxlifF2lk8RekiPytn2Dd8tCOg767T90Vse7POAJ1J%2B6BbFj9&X-Amz-Signature=350fe376d3de90629f3b0789b34a59b95734657ddd7fd9d99d2125b848b8026d&X-Amz-SignedHeaders=host&x-id=GetObject)
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
