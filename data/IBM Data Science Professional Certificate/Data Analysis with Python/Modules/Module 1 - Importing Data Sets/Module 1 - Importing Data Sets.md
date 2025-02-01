

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

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/997ac361-58a8-4f04-bb0f-79fea4baa761/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466X24AB2FG%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T231249Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQC%2FnwsTvuoXeoaQ4X6vUVJVUiPDNfd2giiTcOjVBjhy1wIgWHHalACHHn5psOX%2FDWovGVRB%2FE5L6ET%2FNnxoeCthnEoqiAQI3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJn7K3gjLimVUoCqDSrcAzQevnJWHhfBA%2BxKJ41iNX9Qj6N0QFRpX456H4AtegNd4ZHvb295bbo0aWZfS6%2BeZ6PBPbG1yB5us2SN5q90Lg9M1qZThzv0%2FQQBPnpqe1cfRZ3NqN58IJFHtU8v0CdL5Ldb889HqBCf%2Bz4rdX8F9kCVjancs0NUKIgKLEr1jwwkiaQLOPjjXb9p2qL0aIQI35eoJq75USUvkbb6x%2FOX4I4h9QXs17t1%2BTwJKW7rChk8gWgEyIx6pKiEaumAvhzGe%2BONRvkJKDBK8HnjKY4mhXbr%2B%2BKuNg%2FwoqQuZi7GSUDpWFznuupRDd0OsFv4TE1Eq5CRVp3O0LX9CkzMeejXNkTEiugJqKosWQUwvwgXHIrrY93jDI9OtL9WIp71Kh1SyCJdIShxWBbuqwsVKiokqZoHmQWsigt45Qgs9iGjhXtXx%2BUYLHKQnRjm4og9e%2FIXNWKP34kr0%2BrMOYWyiNLyYlNsgwomWRMvcy%2FTmhFhrdyyPY7HJj8f6LtB9ad5I0AywOHego0cQkjkCe%2BWVUBr%2BPk3LEoJzvMitCbdc6C%2BcL7aT4a2ys%2FWjw%2FzSPI8%2Fviwgpmnw%2BTrdFb%2FOFbm6I%2B3VyNIO%2FjfYQOTNv4DpNyXFq%2BGCMqcykkoZcXMBiD1MNq0%2BrwGOqUBVCkncTMh5oxEs5Swd9BEPOTGBF9TWLqIc2N%2FOxYZ69Gni%2FNj98dj7jzeCvsVqm6KHlCjBLCuKVE8SsCueKZcEUNyZzMKG6CCCwT1%2BRCKMrWdRvhEamQtgu4ZLJTHAUtrYIcpDIbNkCB6sbjye3vD2zBb7w7sj6bP76ex3ZO7QxRcmc6S2wSBoQHZ20RzKacSVAcpUnlMyTETRs7ohY3WaxXhNOB8&X-Amz-Signature=0aa06e1a677a635a015babfcc6f7c83bb324984c22ca8c1fce6dba38cd7f766c&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Data Visualization Libraries
#### 1. **Matplotlib**
- **Description:** The most well-known library for data visualization.
- **Features:** Great for making highly customizable graphs and plots.
#### 2. **Seaborn**
- **Description:** A high-level visualization library based on Matplotlib.
- **Features:** Easy to generate various plots like heat maps, time series, and violin plots.

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/733d1e42-5a53-4fd8-90c1-3d85254369a6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662WPNPWG6%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T231248Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHGSfs1fBkI0xf3snbr3cUQi5cZlE106xs6P23hfbhLQAiEAqNMa7PzRx0k0%2BxPwAqSeoTKXT4zN5B4ulbcHciUzBFwqiAQI3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDIV%2F%2BULJwlvjC%2BC9gircA2%2BbRddJWcxd6IGcqHgPrTvM7xbl7WhTipA9hpuBQ1HTZ7RVzgpxOd45DsydTilJn1ZnPvxULwkmqrmiVPpQIsCL74yjAhSIYhKNHeOuccNORznhhullvhUP%2BeQCiCc5AM4tpeHwhdQqQm%2FdhhgSkimPX8bSwQ9blS62z4IGbeuAUVWotZB2g2ouKXDO6GDs0uGA9s1Ghr4bPvN7UK%2B2USlYGYiNhJakxQF0VmP1Xnn9DbnfbKDLcu3ueoMWKaCWiCbL%2BHA%2FMitP2xZLnctpQRu0cCshbAFQ3X%2Biw%2Fle9Vj%2B35zbv8i8vr8aTjmSJKk9Wg3djYs8cxPxi9PL%2FY6WTpTQey0RGZmMcIpj4cl0FKHceZT8N6FM90%2Bd9Ewnqt3Ig5c4ueO6jomPaQ8sGNywVAggwCXdLgocyVtR3Yv8EaP8MaogURy1muzuJpi6phHslpMDq6neRPEl93AqeYZdx%2FOTJlNwMInpny6GVry05fNf8Yd4gF9W4kXWJbrJeNNtAjXcsWWK5z5ic%2FPl2aAXX%2BdipV8nRn%2Fqd%2BlQ5oYzx0eCf9QCMrzS8oIcDRwV0BqxtaXr9%2FUcig4gIFR%2Fy80UhnpYGSRuaksj%2BnxShf7k4GQMtduxWq3BByvafH%2FtMMSx%2BrwGOqUBoUGUW7tgiDbJGPg0l%2BpMd5v1U1stGsqLFXb5uqwZHi2Puzsg%2FOzdV2MJSpBk4cncN7AWebjItxgfJFDOw7HPBQgjSPlOdiW8pw%2Ffk5Qmet%2BqS%2Fvni5DEdcnrGBcj36pAA0jY3bXs3a55EkDL9yrdT%2BLtgLz5dw7N%2FBQ%2BG7T81ucnH38QSC6oFq0YLnWDNxschH1S1h2CnSkI2Kr1ICxMzUzNxYp6&X-Amz-Signature=301eed918378ec750d89078d49911ebd6f8f877a3c81be74b5efa1ca9de25a05&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Algorithmic Libraries
#### 1. **Scikit-learn**
- **Description:** Contains tools for statistical modeling, including regression, classification, clustering, etc.
- **Built on:** NumPy, SciPy, and Matplotlib.
#### 2. **Statsmodels**
- **Description:** A module for exploring data, estimating statistical models, and performing statistical tests.

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c62885f5-417d-4179-834f-d68f8f2bdf39/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662WPNPWG6%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T231248Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHGSfs1fBkI0xf3snbr3cUQi5cZlE106xs6P23hfbhLQAiEAqNMa7PzRx0k0%2BxPwAqSeoTKXT4zN5B4ulbcHciUzBFwqiAQI3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDIV%2F%2BULJwlvjC%2BC9gircA2%2BbRddJWcxd6IGcqHgPrTvM7xbl7WhTipA9hpuBQ1HTZ7RVzgpxOd45DsydTilJn1ZnPvxULwkmqrmiVPpQIsCL74yjAhSIYhKNHeOuccNORznhhullvhUP%2BeQCiCc5AM4tpeHwhdQqQm%2FdhhgSkimPX8bSwQ9blS62z4IGbeuAUVWotZB2g2ouKXDO6GDs0uGA9s1Ghr4bPvN7UK%2B2USlYGYiNhJakxQF0VmP1Xnn9DbnfbKDLcu3ueoMWKaCWiCbL%2BHA%2FMitP2xZLnctpQRu0cCshbAFQ3X%2Biw%2Fle9Vj%2B35zbv8i8vr8aTjmSJKk9Wg3djYs8cxPxi9PL%2FY6WTpTQey0RGZmMcIpj4cl0FKHceZT8N6FM90%2Bd9Ewnqt3Ig5c4ueO6jomPaQ8sGNywVAggwCXdLgocyVtR3Yv8EaP8MaogURy1muzuJpi6phHslpMDq6neRPEl93AqeYZdx%2FOTJlNwMInpny6GVry05fNf8Yd4gF9W4kXWJbrJeNNtAjXcsWWK5z5ic%2FPl2aAXX%2BdipV8nRn%2Fqd%2BlQ5oYzx0eCf9QCMrzS8oIcDRwV0BqxtaXr9%2FUcig4gIFR%2Fy80UhnpYGSRuaksj%2BnxShf7k4GQMtduxWq3BByvafH%2FtMMSx%2BrwGOqUBoUGUW7tgiDbJGPg0l%2BpMd5v1U1stGsqLFXb5uqwZHi2Puzsg%2FOzdV2MJSpBk4cncN7AWebjItxgfJFDOw7HPBQgjSPlOdiW8pw%2Ffk5Qmet%2BqS%2Fvni5DEdcnrGBcj36pAA0jY3bXs3a55EkDL9yrdT%2BLtgLz5dw7N%2FBQ%2BG7T81ucnH38QSC6oFq0YLnWDNxschH1S1h2CnSkI2Kr1ICxMzUzNxYp6&X-Amz-Signature=241491c5314cc9770aeedd9e5c637a80252d89d66458837fe695854b28a8a467&X-Amz-SignedHeaders=host&x-id=GetObject)
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
