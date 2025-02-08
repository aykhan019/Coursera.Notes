

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

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/997ac361-58a8-4f04-bb0f-79fea4baa761/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466V4JNEIBQ%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T041704Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGwaCXVzLXdlc3QtMiJHMEUCIQC7D8Fh5DUjSjO4Jj%2FIXY4O38ECGn8UOgaUNHRAcGJKsQIgAOoYKEFqZTg2Al2iun2RrlIuTnMBpvQwp3nczEwBR5YqiAQIhf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDM180Czd7zux%2BpldByrcA%2BB96kUFYB3qvESDlYVnTW%2BR5WDqCGpmmxguI%2F%2FAaZ5t%2Far%2F4xVuo93A66ElYmDy3%2BYCargXIuJj3%2BehMmU20xHB2MHrT3gt%2BFve3FuGxHEHc7NjGnPcj92FZQ7niXBCqFIhk43Dexs8L6qQOTuBRpFknvPaL%2Fr2xpJRFH3C40t5X4Jy7iyqRM8aIU%2BSyCnawhfthzDJXKtfBGn70nioBvK6iqR8B327AvrvK7tpCXn5DpsX0xjxxnmV2L4QAN4G%2FSKkfC%2BV5nxZc3dl6zvJMDpL6WRKQxjEYME6OQGZwHp%2BHcmaj1mPeqDsF1bT7oL01X%2Bfz9YHD%2FYcBlIJySyvaXa5VYzCgdw%2Flx3LbyTv68ZcCTJZZOZuo7eSo7AnKJA6%2FDI4NC1cq6gojlC%2BPZqz9yYYtlo0LuTLFDCWxMEMQsToXQCQqgEnmMradEap%2Bk2vtg9I0iYVGF9rCmcJFISM5c5VprQR8Fgf2zR9H6%2FzGMJZZP3kHT4I1ZRp3axgvTiCYD0PJv7pPtAVKApYl%2BOOILPCmmdtlnmU%2BYMDaaTZ9jat4o%2Fs6P0pwRZ2rO9VRfKIYuVeZpzHxNs34ysBZ84D68%2F7n9PRpCjPrKn1QhJKNA%2BwEvLB1oCEnIBWCgDqMLGym70GOqUBs%2FImu1Gw4mhtnK0RPcMnJHhqqqyHEW7eyt2yIhlhL%2FP%2FpWZiO8i9GZ3WPCnZQcMiAh00w%2BPuOoh9%2Fs3CmLYEgnCi4ynHCBd7G%2FY4pl7HTVdZVDFvYM%2BycpfR8GfLNSa%2Bsi43U8BoLmzt4PALXGA7kjV3IiGMrHWTV709S4K1x3EBk2Rn3Too9a%2BQm4I4QuYWIOwJNcEoCQ4xl9hhmyDNE%2FpoMQUK&X-Amz-Signature=5bf4f7df745375452b5007e2946f334bf47cadb445a787cbad05011657f7fb14&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Data Visualization Libraries
#### 1. **Matplotlib**
- **Description:** The most well-known library for data visualization.
- **Features:** Great for making highly customizable graphs and plots.
#### 2. **Seaborn**
- **Description:** A high-level visualization library based on Matplotlib.
- **Features:** Easy to generate various plots like heat maps, time series, and violin plots.

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/733d1e42-5a53-4fd8-90c1-3d85254369a6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662QKEL4CS%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T041703Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGwaCXVzLXdlc3QtMiJGMEQCIEQ0wSOvZSb4lg13RVEGgjS%2FyAaVbeUAidA%2BTcGmeJvCAiAfz308K2ZUdB5g3g6eVRhZ6VYkF9dYv3yDoigGKfyTlyqIBAiF%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMXpteh2H6LnTFGfeFKtwDLc9WlZmMQSwlKwrPiLOIvNQLIpEYlKJi%2B0SPI9z5iqK%2F7y%2BQ9StRX4O7awp76Ld5RMzLWgBkFGzlMyjf%2F8Z3JijinSybMpRS744r6C%2FuRs%2F2yU1tPopprssWccKBfqw3gN2XO5P509aQI1kDzRxBBLh0dBU6P03JrD9pO7T9i%2BiSePNgOJ9czVabM02ToFVLhAVXOm3vnzaBptEqNoBQLBhxytgpnEJUuMyPrv9fJAVd8nda76UYcMXGblmwq16zkyKsl3F%2FA2fyvkq%2F7AgoNt8Jk4eTyfsnIFEwNgqYJInhAWT5I8aszI0NHvyOoT9aVQRWOUd2gR%2F%2FNCSd%2BZOxFBkz1rpO0%2BOZXwo4xkDmssCohJQtQJBN7%2BtaKmLcKFudlNIKkJ2oQitJH1MtiO3BPM205FVv5lFXD53yRI9xuBvpmPs3L0ofohH2pcTMVrdN4rB1gePU%2BgWdANTmODxqNsix7Y12LXRmsmtAYutGnU4hGAKgHbxRqEBwGxcPcM6SSI1sxaSRlrdEnJooAG6bWCuCAQG9unIepRAeIDqmAFowpeHc9eJ8ZJaFtiOP9lGv3bSR3WsMxWvadY%2F44wM%2F4G7nB%2BiulYaOX%2BezDosvEvwVD3lyO5K2YG%2FD83gw37KbvQY6pgEMjcvdWzX2mRL14Y7Gjw3zmg7%2Bh%2F6hjsM06L%2BKfTuoXDrTtWIXHDe7rNnfn9Nmnokm0DkjfFpDcB%2FU7wPAzPzXVTHVGHgrGp65%2BwpotLIu8YN2yFt75H1Nh5bwOYjmP77pD67ZS%2F901467ZkWXbMAARf13%2FC8fogpX2EtOQMVOnkHnRd1PlYqg3w9F%2Ff%2FMgf5O6j66NjIajHNS%2Bi41r6m3a6JvpQhq&X-Amz-Signature=b4199686838717a60bce17a31e099b694619cd14d0223c78e294bbd9fdbe1815&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Algorithmic Libraries
#### 1. **Scikit-learn**
- **Description:** Contains tools for statistical modeling, including regression, classification, clustering, etc.
- **Built on:** NumPy, SciPy, and Matplotlib.
#### 2. **Statsmodels**
- **Description:** A module for exploring data, estimating statistical models, and performing statistical tests.

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c62885f5-417d-4179-834f-d68f8f2bdf39/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662QKEL4CS%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T041703Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGwaCXVzLXdlc3QtMiJGMEQCIEQ0wSOvZSb4lg13RVEGgjS%2FyAaVbeUAidA%2BTcGmeJvCAiAfz308K2ZUdB5g3g6eVRhZ6VYkF9dYv3yDoigGKfyTlyqIBAiF%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMXpteh2H6LnTFGfeFKtwDLc9WlZmMQSwlKwrPiLOIvNQLIpEYlKJi%2B0SPI9z5iqK%2F7y%2BQ9StRX4O7awp76Ld5RMzLWgBkFGzlMyjf%2F8Z3JijinSybMpRS744r6C%2FuRs%2F2yU1tPopprssWccKBfqw3gN2XO5P509aQI1kDzRxBBLh0dBU6P03JrD9pO7T9i%2BiSePNgOJ9czVabM02ToFVLhAVXOm3vnzaBptEqNoBQLBhxytgpnEJUuMyPrv9fJAVd8nda76UYcMXGblmwq16zkyKsl3F%2FA2fyvkq%2F7AgoNt8Jk4eTyfsnIFEwNgqYJInhAWT5I8aszI0NHvyOoT9aVQRWOUd2gR%2F%2FNCSd%2BZOxFBkz1rpO0%2BOZXwo4xkDmssCohJQtQJBN7%2BtaKmLcKFudlNIKkJ2oQitJH1MtiO3BPM205FVv5lFXD53yRI9xuBvpmPs3L0ofohH2pcTMVrdN4rB1gePU%2BgWdANTmODxqNsix7Y12LXRmsmtAYutGnU4hGAKgHbxRqEBwGxcPcM6SSI1sxaSRlrdEnJooAG6bWCuCAQG9unIepRAeIDqmAFowpeHc9eJ8ZJaFtiOP9lGv3bSR3WsMxWvadY%2F44wM%2F4G7nB%2BiulYaOX%2BezDosvEvwVD3lyO5K2YG%2FD83gw37KbvQY6pgEMjcvdWzX2mRL14Y7Gjw3zmg7%2Bh%2F6hjsM06L%2BKfTuoXDrTtWIXHDe7rNnfn9Nmnokm0DkjfFpDcB%2FU7wPAzPzXVTHVGHgrGp65%2BwpotLIu8YN2yFt75H1Nh5bwOYjmP77pD67ZS%2F901467ZkWXbMAARf13%2FC8fogpX2EtOQMVOnkHnRd1PlYqg3w9F%2Ff%2FMgf5O6j66NjIajHNS%2Bi41r6m3a6JvpQhq&X-Amz-Signature=11c728ab539cba8b798a3aa9b5a78ae6a66896c1783627b2d2a43a48c800a612&X-Amz-SignedHeaders=host&x-id=GetObject)
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
