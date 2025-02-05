

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

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/997ac361-58a8-4f04-bb0f-79fea4baa761/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XAWXAYYC%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T171302Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDAaCXVzLXdlc3QtMiJHMEUCIQD0AEy%2BM078lAVtCcoOelQt7tm7m3%2FGi0zpxCBy%2FwBCYwIgOW7o7lGZL5zRDOA4vZFxCK6CEFSYdcLyClFp3IObDhEq%2FwMISRAAGgw2Mzc0MjMxODM4MDUiDCuod19NU2mG3%2Br%2FaCrcA3JonkHbY17%2FwzolMjZtd3LveFBEV%2FC4HcqY0RjlvTEDZZIoYAKDiYVwSoJKYTHEjDGhk2zWHi5lsdGMydtJSTekooNHQ65Hjnm0nxjopd3xT9dibgjfBNFQjoI1OnPUDzWHHU6UH2KCmn4CWt1%2BHlRKeT2ILNDWdBIeMDYKiS0rUzwsazb7HvMolIVdWPzppauAukcJz%2BZG2pB6Ea%2B9geN2wfpHPZWzFUB87mVUfdYQoDR7vkkrUfRnTyahmg47rJMYvz7BKRIBK5oHz63Q%2Fc2P8oDVe4uBC0SHj%2Fez1ru3Qo8oUQfIHsBsYgPPcLU1WKMQz50T6jVdZcjd4x1ZyrDp5nMqAsW4a4OsuWWvBiCE8T2cbf5FyAjjQU24xBuBbfJf6dP15vkPwWnPBFhDfBVjR5wEQNLsZK2uGyItK6N0RwVNnfmLhlxGgJXzGVbivMQU8v6VLZpLAhLHL01r85fx%2FJdwqF9mbNCxWtBcgouyNcyX1vHi4wLbCof9LzovSnWqWkLZgXMN%2F9UXk2ek2X%2Bu7eRy%2FjIn7hvYQLG2njgurEJbDlaaKRuzjHOekoPX2K9ei1Jftt1qIA6t430bxywB5z%2F25WBMEkTpxEN7W10ufYFV%2FXI9cFpszJVRMJ2djr0GOqUB5DGp4yz9uab3LcUedPcTSOCDOVUcGS6D9FWN%2Bdn2FbhdSjsWF0kxcV1dfRO7kndQlIG88x0FBFF2qLTiJLQHXMuXXPvNKbdVCeaVjYI%2F%2FnjE2UEyZRmiK0VJTk1HPpqBMOOX0TjBNmNhm382XYtSgwhXPgptZLJu7apec4uyP3wVSLNI4YoGhLeg9ClQLsX%2BKr4u8isRRi%2FO31XdInqKvUWbCOw%2B&X-Amz-Signature=daf336db9359a76681765d6154f61a94fec6aa9be6eecfdbe647cbc6a67ed5f9&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Data Visualization Libraries
#### 1. **Matplotlib**
- **Description:** The most well-known library for data visualization.
- **Features:** Great for making highly customizable graphs and plots.
#### 2. **Seaborn**
- **Description:** A high-level visualization library based on Matplotlib.
- **Features:** Easy to generate various plots like heat maps, time series, and violin plots.

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/733d1e42-5a53-4fd8-90c1-3d85254369a6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667UMUVGJJ%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T171301Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDAaCXVzLXdlc3QtMiJGMEQCIFZgBeYe4Drixn7ZW0lZVMLPKVxsRk7NlvSmoitFzScPAiA3JY3CORQJId%2BRgdrDjcM7gj%2B93zqoDOvd74tdaoZGDir%2FAwhJEAAaDDYzNzQyMzE4MzgwNSIMwHhtSz0wMxX%2FR09oKtwDCZR9TVCh%2FmGM7nSp1teX5%2Fi74Y9c8%2BznABI%2BfjCeczsgNt%2B%2BoJQQ7cGcu%2Fye96my2EqW3DnysL8bpr3RU5CvtjVQ1q4eDrM48v%2F7rIZ%2B2YhsI7gqq2WpQz4IoguGtq5tew5cpiiE4R%2BRte6hSOXeD0S3q6RhjqfhNsMguJwhdlbWuoS8QnghWjJylUBO8lX%2FElo7JpQ%2B6SUJLDQ6TeHw5qi5g5H5OhTLavRQJgtYAvAz5hSccog4IAYBtwMWW1HdBQibpmGqEVy5RhnpS8%2Fq%2BQhm1h0kCB5iQ9saDwBlo2TYqfQC13xZrQUCsvdguCPgfVPEl8q8yuxUExVpLwfg6g5WcPui3XpyHYK8ztqMEs6DXIuKN3bPn%2Bfx4uNVFYBVonJ5CAnmnUb9O2UbcTzgBY6A6VhTHtfz%2Bh4x7Hn2VmY3mfWXDRY8Qbq3uciHhFaV7twLjQtTyEYYg%2BuZWGJXguFHVmSrsrKU09hXxw5h%2BLz0WkkwxOBfeSS5FqyBrUWTJHcX8y2BpNR%2F%2BWO%2FH38E5BjtvjgyCnVsFBMvicPlYe5SPqlCrPKQVtRUnDIXb6blREybOsw873%2BtDSS7oVIQiOStlCSgHv%2BqAnIX%2BK9E2fa3xKoevMEEmk9Z10kwpp2OvQY6pgHYP1PUoN0uvr%2BHLz6npSF7BDAeT%2FTptBMr71mEqWt7rLbiVc4gxVmf8jgpImRYsfj%2F6lFXVEQPz9YVvdEhgGk8RTNeMXDHR%2B8fd3mG9o1eCzqmUet3m3CqzCEx8kPyo2hJSlR4dQrGwQ7KIfjnN4Ochlmeb8w7sVc75ZvAweCmnuOYRPwSivALoR1yMDplpFjzhwZjl3CRfTpR22529bkcGGwG3x5C&X-Amz-Signature=9311ffda45e4a09eaa808ca2077978941acdd9e58af4ce9c0cda3fe848b2797f&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Algorithmic Libraries
#### 1. **Scikit-learn**
- **Description:** Contains tools for statistical modeling, including regression, classification, clustering, etc.
- **Built on:** NumPy, SciPy, and Matplotlib.
#### 2. **Statsmodels**
- **Description:** A module for exploring data, estimating statistical models, and performing statistical tests.

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c62885f5-417d-4179-834f-d68f8f2bdf39/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667UMUVGJJ%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T171301Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDAaCXVzLXdlc3QtMiJGMEQCIFZgBeYe4Drixn7ZW0lZVMLPKVxsRk7NlvSmoitFzScPAiA3JY3CORQJId%2BRgdrDjcM7gj%2B93zqoDOvd74tdaoZGDir%2FAwhJEAAaDDYzNzQyMzE4MzgwNSIMwHhtSz0wMxX%2FR09oKtwDCZR9TVCh%2FmGM7nSp1teX5%2Fi74Y9c8%2BznABI%2BfjCeczsgNt%2B%2BoJQQ7cGcu%2Fye96my2EqW3DnysL8bpr3RU5CvtjVQ1q4eDrM48v%2F7rIZ%2B2YhsI7gqq2WpQz4IoguGtq5tew5cpiiE4R%2BRte6hSOXeD0S3q6RhjqfhNsMguJwhdlbWuoS8QnghWjJylUBO8lX%2FElo7JpQ%2B6SUJLDQ6TeHw5qi5g5H5OhTLavRQJgtYAvAz5hSccog4IAYBtwMWW1HdBQibpmGqEVy5RhnpS8%2Fq%2BQhm1h0kCB5iQ9saDwBlo2TYqfQC13xZrQUCsvdguCPgfVPEl8q8yuxUExVpLwfg6g5WcPui3XpyHYK8ztqMEs6DXIuKN3bPn%2Bfx4uNVFYBVonJ5CAnmnUb9O2UbcTzgBY6A6VhTHtfz%2Bh4x7Hn2VmY3mfWXDRY8Qbq3uciHhFaV7twLjQtTyEYYg%2BuZWGJXguFHVmSrsrKU09hXxw5h%2BLz0WkkwxOBfeSS5FqyBrUWTJHcX8y2BpNR%2F%2BWO%2FH38E5BjtvjgyCnVsFBMvicPlYe5SPqlCrPKQVtRUnDIXb6blREybOsw873%2BtDSS7oVIQiOStlCSgHv%2BqAnIX%2BK9E2fa3xKoevMEEmk9Z10kwpp2OvQY6pgHYP1PUoN0uvr%2BHLz6npSF7BDAeT%2FTptBMr71mEqWt7rLbiVc4gxVmf8jgpImRYsfj%2F6lFXVEQPz9YVvdEhgGk8RTNeMXDHR%2B8fd3mG9o1eCzqmUet3m3CqzCEx8kPyo2hJSlR4dQrGwQ7KIfjnN4Ochlmeb8w7sVc75ZvAweCmnuOYRPwSivALoR1yMDplpFjzhwZjl3CRfTpR22529bkcGGwG3x5C&X-Amz-Signature=8e1bafed3e34c6bcddb2456e298a9835689af63439d4380baab362b82d63f06b&X-Amz-SignedHeaders=host&x-id=GetObject)
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
