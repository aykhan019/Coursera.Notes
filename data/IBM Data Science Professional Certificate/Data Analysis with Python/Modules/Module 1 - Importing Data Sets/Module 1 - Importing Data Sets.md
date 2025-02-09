

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

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/997ac361-58a8-4f04-bb0f-79fea4baa761/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YZOAX72P%2F20250209%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250209T004056Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEID%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIBIFFIXxZaK%2FFtTXl%2FaunGdNobeSgRuV%2FpdrQZi7MqKXAiEA2NxcY9xiDs2MblouHCuqJw8eOAtjZTfY2fIQbSvW%2FzEqiAQImf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDO2LYS9jAJ%2FrTRtq3ircA0dHluNrhiztn6a5CWEQKuS7UyUniI2X3oZDXgrPN%2BLuH7zuz1YLhMiqtmBOEPXOB5adG%2FaACxjruRHhH6g56fKabQtd%2FZ2bEZvNZefXOQGRpVSKc7rB1n4Zr9mzabzzcE%2F0UqlL53agiqbJ5qh%2F18LC75ARig1EnM4i3u52m597SyW4%2FHPmYRLJOP0K85goCwDIImNrB6d19b%2FtbtW4jK%2F7PeZZffSMxYfMmYCZmdSBu26zT1LHPOGgVOR%2FZ44ZIf3rOR9bizhMAuj4Hc2gkgqiS%2FL2%2BH3WtHA3SdcqmhXhkQzDCHje3NIiA2rZSQ%2Ft2t3oGLfrYUjUI3CK4Z3y18Tg%2BzaI5PPLTWtlvxe3SCqDgWPBm3u93jVX5IsgwdQbLlJ08u5kcjyLpXD%2F2MLPqTYyRUdN6iH8O7wgHNkNyJ2spdLx3PuDdJKHC9woGv%2FE8VSLQ9%2B%2Fc2Xu8XlvfFCQ%2FJqINmcyXGsI96LMDmWcE0CUR1vhw7zW8qmF%2FoMsJW0axS1RDqQcno2wG7qOVAJabR2meoTwk86DKSBVTTYupt1IVQRjYzGs2HD7ezVlJzpFt3T%2BrPrvgduUk8lM8cZhhWNdNsLBb600bJeFT68%2BzFH8PmrYnhNLS0I9HdTLMJnXn70GOqUBd6JTkS%2BYTLyP%2Bpo2G%2FYzb1RvITTZewMUdFAqFsiX8iB4cHZXxU2s%2F%2BgEq03hIvWbzo73kh6pLte%2FUW%2BnHpmxqemqofWnsInHzDxd9%2FXDiPSin5FgPoIy3MnpzNq3ZOesYIWPhJf%2BbqlB3CTpMxv%2Fg1LkWPkald2aoFCKbZoiX5PsA9Q7BrGIJZSF1CMjqY87qzporoX8WZBAJNTl5SLVsUQJTXQP&X-Amz-Signature=b4ed3c43126e3b11ead9f974828dbcaf8b5bdee52704a4fa664638a73ad83695&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Data Visualization Libraries
#### 1. **Matplotlib**
- **Description:** The most well-known library for data visualization.
- **Features:** Great for making highly customizable graphs and plots.
#### 2. **Seaborn**
- **Description:** A high-level visualization library based on Matplotlib.
- **Features:** Easy to generate various plots like heat maps, time series, and violin plots.

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/733d1e42-5a53-4fd8-90c1-3d85254369a6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RCULEI2C%2F20250209%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250209T004055Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEID%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDYqkWjqI%2BUZcdfxaK0LN86Cbq2%2BmMHNhqoy9o0ebZ2jgIhAJ3n0C76CsnV8%2B6wKPQXJYCHo%2BdXim0XUVwJLJnwTv53KogECJn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igz5jv5ijSINuvE3Emsq3APRrRKSINFW%2FGi0YGvffThdNjTGDqfVgOOCFMazFLWdVQCrsbIYSCBv9x1wRL54gJuv9IpKmMo9AOsAtOWVBhERQHKot%2BHJKNWA4dQWmdJ3loiyMdv3RZPXg61OC9hFHnN9dYOV7jOkkH0VhSr6nRw41YyfA%2F7hCyAan7R1mhXyrhrr4pw3aQH7v%2FTh3FsKfF%2Fa8slrKGQAKAi3iK5IaXYtvqRGZSrtMNf7IKQTTo2oqYvFUMpC6Zwr37yVVOP%2BfDSnlK8VCcxBorLFTlKsVlzTl40n%2BMoeuRC2DMbMFeEXfqiZx%2Fl4jNwaHPd5RYXyMczZOshbB%2FpeceuwChseac9KTjU3MUybzCyTOvmB2j33DHB64mub%2F7IJROu5cniy338eTRUjk9%2BQ1%2FctSvTi%2BrzBD7JxuL81JVmIA%2FgU533cby54YCJMOKQz75pFt0hs6HN2fitz4sAjP42JRLIx3l%2BNjSKMTPAyxerNmRZK7Lkey8vYuIg9S%2BmOzEsvnrZjCLyEOEnvKQUTcwjMj6pAUAAQ%2BsJEjLWwINFn5Vv3bMrKuP4yc9cvomR2iwMKEho2AaubYcBpfLxQh4U8tuyRWswJTcrEbWmvcYb8%2BfYYXIYct0aToThqwKtaABuRAzCr15%2B9BjqkAXg4JMTKg7eBOlV0TY4WIiYDjRaIURdFKcSfNtWe4odDGR6052aNZeSfytEejcIJraHN48%2BFgdCYA6fi99aiyWP0pV9XetOXvBZIaAS%2FtDSPdV0t1BrJjwQL4rwrIvr8lJVaRuoXPTgSVPBJWMMkM%2BYfShk9HZPHDHfT2Hurf%2Buagtr%2FYDjLP%2BwSRriO0hzsRWP3KwYyiiUzIqJxo7P05p%2FX1lvR&X-Amz-Signature=d7fe5bd9022cba09228164368c038e4eeeed002db2f99abe2466220a050d2b7e&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Algorithmic Libraries
#### 1. **Scikit-learn**
- **Description:** Contains tools for statistical modeling, including regression, classification, clustering, etc.
- **Built on:** NumPy, SciPy, and Matplotlib.
#### 2. **Statsmodels**
- **Description:** A module for exploring data, estimating statistical models, and performing statistical tests.

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c62885f5-417d-4179-834f-d68f8f2bdf39/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RCULEI2C%2F20250209%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250209T004055Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEID%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDYqkWjqI%2BUZcdfxaK0LN86Cbq2%2BmMHNhqoy9o0ebZ2jgIhAJ3n0C76CsnV8%2B6wKPQXJYCHo%2BdXim0XUVwJLJnwTv53KogECJn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igz5jv5ijSINuvE3Emsq3APRrRKSINFW%2FGi0YGvffThdNjTGDqfVgOOCFMazFLWdVQCrsbIYSCBv9x1wRL54gJuv9IpKmMo9AOsAtOWVBhERQHKot%2BHJKNWA4dQWmdJ3loiyMdv3RZPXg61OC9hFHnN9dYOV7jOkkH0VhSr6nRw41YyfA%2F7hCyAan7R1mhXyrhrr4pw3aQH7v%2FTh3FsKfF%2Fa8slrKGQAKAi3iK5IaXYtvqRGZSrtMNf7IKQTTo2oqYvFUMpC6Zwr37yVVOP%2BfDSnlK8VCcxBorLFTlKsVlzTl40n%2BMoeuRC2DMbMFeEXfqiZx%2Fl4jNwaHPd5RYXyMczZOshbB%2FpeceuwChseac9KTjU3MUybzCyTOvmB2j33DHB64mub%2F7IJROu5cniy338eTRUjk9%2BQ1%2FctSvTi%2BrzBD7JxuL81JVmIA%2FgU533cby54YCJMOKQz75pFt0hs6HN2fitz4sAjP42JRLIx3l%2BNjSKMTPAyxerNmRZK7Lkey8vYuIg9S%2BmOzEsvnrZjCLyEOEnvKQUTcwjMj6pAUAAQ%2BsJEjLWwINFn5Vv3bMrKuP4yc9cvomR2iwMKEho2AaubYcBpfLxQh4U8tuyRWswJTcrEbWmvcYb8%2BfYYXIYct0aToThqwKtaABuRAzCr15%2B9BjqkAXg4JMTKg7eBOlV0TY4WIiYDjRaIURdFKcSfNtWe4odDGR6052aNZeSfytEejcIJraHN48%2BFgdCYA6fi99aiyWP0pV9XetOXvBZIaAS%2FtDSPdV0t1BrJjwQL4rwrIvr8lJVaRuoXPTgSVPBJWMMkM%2BYfShk9HZPHDHfT2Hurf%2Buagtr%2FYDjLP%2BwSRriO0hzsRWP3KwYyiiUzIqJxo7P05p%2FX1lvR&X-Amz-Signature=d78f827931e5abb9be83b340da133929c725cf607ef23da271d4bcc1279a4577&X-Amz-SignedHeaders=host&x-id=GetObject)
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
