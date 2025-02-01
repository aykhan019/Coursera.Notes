

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

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/997ac361-58a8-4f04-bb0f-79fea4baa761/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46665DANU34%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T031900Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEML%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIBcwriJ2WOPJBDeGxL3etKG%2B6tRv7QK6FbB9LUJqACd0AiEAv76tUzyqKSgfbV928WlyUT6FMYaPuJ%2FycaT9jnGFGGUqiAQIyv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKVc9kH58xENDBzZzCrcAyT8UCDpCNNoq9inDTANOHg2LG5c9y0TQjIKQRvUMn38NNZ1btL8JhZJLg8oNMQomA0HeatNHV71VFn2B06mfBNjwtE6JS2HycEV3qMYFmx9%2BzdghxAMCbS6fj%2BTSuQjOsAPu0U5EEpUQZcVjCoNzuChGLm7g076nNDLxxjRxipLJYPh%2FW5mo8D71i6D5kbvpaEE5hqFCTj8xAqMIVAQ5smWaEJqbRJlxWX0wgQqYXWp2qHwdXVsLOIA98XmAGZT3P3MTT0Qb5t1sEMQnryUz3%2FIdJ9bmz2S2%2B%2FlNFHdUh23QEysb%2FPXLrNyiUP6EyZX0KuwHCzeRrPTTvMXhS%2FMsR1GcLmtsG7yAS%2FRU4qmGnsO6T7GLMv3DnfloidtsB6BP%2FlZBadbQcH6YTGYpWhI2GbN78PrJzZAAJ4guz0hOGBBOp07sMxe5zTw3mp1qYadzNQcufaK2Db5uvFt0j9gnOGNcM4hhYWnSGj6GgsS2E7OFLEUPTcAgjdd1hLwhvWyP0rTDjH5R7YVLdrN7zV%2FY8NKQuKVPDjUnkUKguoBn65IsPZXiRmudjuYFxVsp1sNT%2BwdjI6deTIPVE7gG4jiZGGFjquOMz0DLVFlfJ1a1HhfEBPFGBcsvF5Qxu7iMMPs9bwGOqUBFGRyzykL8komjIoDeru8hxFaK80IPjITfnA%2FTh5Sh0zUEulY3DRB%2BjuqUPjgZQXR%2BSGesm7RYICFmlCeT%2FN5vof9u58zlwCkXDDwz39pHdizZrZaWSnHQ8CcRjWY1L8CYEs7TkAO18VKaJlwOIGtI9cT6UthmKTm09iLkhTTjjAQqE9YyiIeEZOnSxSy8D1qqA5XgmIxFOz6%2BAT5z%2BTnvrRn3GL7&X-Amz-Signature=d1ce56f2b59a84ee5275b08be801a6c03a191024bdc129b6bec7d72a891e5099&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Data Visualization Libraries
#### 1. **Matplotlib**
- **Description:** The most well-known library for data visualization.
- **Features:** Great for making highly customizable graphs and plots.
#### 2. **Seaborn**
- **Description:** A high-level visualization library based on Matplotlib.
- **Features:** Easy to generate various plots like heat maps, time series, and violin plots.

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/733d1e42-5a53-4fd8-90c1-3d85254369a6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QRA2QQMO%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T031859Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFSQiYrxDngd27dMcBJzdS8I6MebY%2BdGzgyiGpmXXfssAiEAwaLPS5GZKlFBqkjlG4x%2FXcC0QL8BXAKbv5H4Nr6EPOQqiAQIyv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDWF%2BhEyXzDoHtRLMircA8A6yWch1HuImRC%2FwKWz24f5tuYgSVhTKICNuYHRNyXU3f71mecqTfgqk46a5tvQe4%2Fhgx8FisrKb4uro8U5oZWoABKu6WXslPxazhJH2fmMSsftms4cyRvLjvcjsTsr1aRUFHQHtFYvBj5RDzq9jjYTKtD6O%2BOvLMJAUmjMiuY4oGcJclUFLCQFnMG%2Fokij3FkRXvaBfshHni9bniNRh6Ij0Qm2gWDnB6jujcwRsayQhYUNkre%2FcXmIKn0SzrW4JfB82yiuh2caXw3680%2B2lQ25naGVD0W9vHCaFYdX1uvqVL2PP1iqXB08WFzRoT6YW9tqUwQCEC2llO2WowfFIRDJBSwFa2DmnSJanK%2B3rjeGuFBjnZpgqaIdXGprrhDcgVixvRjjuhRi7kMwra23uCAyILh1hlmckYNO3PJMaN8J2hGRyGEicoqKYFgvzTmPFaPqjfk6RDJK%2Ft%2BMD2n%2B7snm0PEjdPCBU7dBwS2AaovxsyAtLS6mkmS3%2FmI4XPZyASDHnYEx1o72qRVutlP5B2l%2BVEX76jA4KCBjfwJASP%2FFwAv8%2FvLz7T%2ByU8q1d0yUUajiQGh%2BU2VtYLofzO%2BGBQV4Zavtu0EVqdlsq9tMkdMnejkryorDa5xyTIZvMLfs9bwGOqUBGW6VcP2WjBsVE9FQYP2jJ8QQQFeDCizGEOk7nKVZz5w9cEIU%2FyWHAwAINR03t9B5ZVRN8o%2F%2BTtCdj9cmkqsV9%2FlIcSNyeWm8ElTnnUF0GCTdatm%2F2fMwjG1%2BqJ%2B8pIVKV1J%2F8Don9yd1eJ2x4zM82kwfyEd6w1ZGmg%2FzmoSunQfKb4NZAc%2Bvli1K3RBgp0OuqyDq33or3dBEXhJ7t0cof5Duf%2Bjq&X-Amz-Signature=ef3b182ebf1e67636993965035f19a37f1cbe701055cb3eb5047e159e2537db5&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Algorithmic Libraries
#### 1. **Scikit-learn**
- **Description:** Contains tools for statistical modeling, including regression, classification, clustering, etc.
- **Built on:** NumPy, SciPy, and Matplotlib.
#### 2. **Statsmodels**
- **Description:** A module for exploring data, estimating statistical models, and performing statistical tests.

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c62885f5-417d-4179-834f-d68f8f2bdf39/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QRA2QQMO%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T031859Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFSQiYrxDngd27dMcBJzdS8I6MebY%2BdGzgyiGpmXXfssAiEAwaLPS5GZKlFBqkjlG4x%2FXcC0QL8BXAKbv5H4Nr6EPOQqiAQIyv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDWF%2BhEyXzDoHtRLMircA8A6yWch1HuImRC%2FwKWz24f5tuYgSVhTKICNuYHRNyXU3f71mecqTfgqk46a5tvQe4%2Fhgx8FisrKb4uro8U5oZWoABKu6WXslPxazhJH2fmMSsftms4cyRvLjvcjsTsr1aRUFHQHtFYvBj5RDzq9jjYTKtD6O%2BOvLMJAUmjMiuY4oGcJclUFLCQFnMG%2Fokij3FkRXvaBfshHni9bniNRh6Ij0Qm2gWDnB6jujcwRsayQhYUNkre%2FcXmIKn0SzrW4JfB82yiuh2caXw3680%2B2lQ25naGVD0W9vHCaFYdX1uvqVL2PP1iqXB08WFzRoT6YW9tqUwQCEC2llO2WowfFIRDJBSwFa2DmnSJanK%2B3rjeGuFBjnZpgqaIdXGprrhDcgVixvRjjuhRi7kMwra23uCAyILh1hlmckYNO3PJMaN8J2hGRyGEicoqKYFgvzTmPFaPqjfk6RDJK%2Ft%2BMD2n%2B7snm0PEjdPCBU7dBwS2AaovxsyAtLS6mkmS3%2FmI4XPZyASDHnYEx1o72qRVutlP5B2l%2BVEX76jA4KCBjfwJASP%2FFwAv8%2FvLz7T%2ByU8q1d0yUUajiQGh%2BU2VtYLofzO%2BGBQV4Zavtu0EVqdlsq9tMkdMnejkryorDa5xyTIZvMLfs9bwGOqUBGW6VcP2WjBsVE9FQYP2jJ8QQQFeDCizGEOk7nKVZz5w9cEIU%2FyWHAwAINR03t9B5ZVRN8o%2F%2BTtCdj9cmkqsV9%2FlIcSNyeWm8ElTnnUF0GCTdatm%2F2fMwjG1%2BqJ%2B8pIVKV1J%2F8Don9yd1eJ2x4zM82kwfyEd6w1ZGmg%2FzmoSunQfKb4NZAc%2Bvli1K3RBgp0OuqyDq33or3dBEXhJ7t0cof5Duf%2Bjq&X-Amz-Signature=b0c3cbfcf65576d0f954f8454a2e2e73a96e0776b0dd9f19ca9806b6d3b37eef&X-Amz-SignedHeaders=host&x-id=GetObject)
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
