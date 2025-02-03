

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

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/997ac361-58a8-4f04-bb0f-79fea4baa761/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665FSNBHL3%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T071440Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHfiiy9qRya7E5EzW4GDZFM3xTYxlrcI6lPEKAgz2eGsAiAzt7iRQ2xhSp%2FecZO5Xk7rZ1EZk2zp8tGzEVd3x9%2BJtSr%2FAwgQEAAaDDYzNzQyMzE4MzgwNSIMCHrBiJNhb0q2sbFBKtwDPdA9z4kV4b5FJ8AfZd2VDBrfjXmnj1lNbgPXwbfE7xQZXogLgX6ZdKkcmTKVsk5D4e31%2Fq%2FsBDA3fM1dkRcAiOKi47bqlHDhSSN3w2d9tP3IxkAPK4xBYg5mu3SX8xNlaBhYnbfiH%2FU2zzFOdD%2Bixf%2BGRVUqUr9HVNF9b2KiznUZRD3xmtb1MwDEIxfMCplhoP3N%2BH%2F7CXqw%2FGuiooMkzpTua%2FQ7SLfKNP9mg%2BhqpPCH%2BtU%2FOLhTBXkiBislJ0l54ng6ny%2BKvnRqjoEL%2FLAN1MddWx8YzXSCjgNPh0RNvmDiYjBx%2BiuAfhQtaWvZdSlbRSba1sqxtd%2BJ%2FEFdq5jPj5nZhbRw1QqoC1R9OSGlPITyA8wh%2BCPFuD6crrSNHQE27owZhVAQMkgWQv7eUxXyJw4coyRnfBhaTWlJdE33OAfIvl1Aq2h8KnzsqPH83rat7%2FLokzLmTSoRtwYIO%2FpmP%2BK2tonbrR%2BmEa4r9nkB4%2FX7ZmPeA2n6HbtSKqCbs%2FIdvRLFa2%2BtLkCva%2Bnl%2B%2F6RpSIiUIk1YuO6Dpd637YI20XP1pevHx27ROsOZH4wwPlmSdS%2Bg1cDQIVjyIw%2B0BqvRPEQ8a55OxWceUHNfSA1MKJ%2BiNHr90mxQkFJqX4wntaBvQY6pgH%2FIMQjJJFyGtUy7jDwKw3gxP8%2FdO5tFHL6dvUBC2MzuVc0bwcMKvuFaTvowt7EK95x6cWdzUhv4ZDDwP6oCbHxFogLvEmUGYNBS3KGvBPfunmSpYsGk6rq11H5qNHDY%2F0imh6fXWCwMiVDOUGdefRkKfWNq%2B%2BDcCAAy6pLFiBqwLLkB15JAU4qblQ67lgjOgAQgm8On0AVw%2BJ33%2FEcxH8PtLMAQS42&X-Amz-Signature=650386e856c79b9b2f8899b8baaefcb899b9954113fa50ea819b2924d655e6aa&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Data Visualization Libraries
#### 1. **Matplotlib**
- **Description:** The most well-known library for data visualization.
- **Features:** Great for making highly customizable graphs and plots.
#### 2. **Seaborn**
- **Description:** A high-level visualization library based on Matplotlib.
- **Features:** Easy to generate various plots like heat maps, time series, and violin plots.

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/733d1e42-5a53-4fd8-90c1-3d85254369a6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466X3G3RNWD%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T071439Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDM8RzysxcWSpSNPWL%2F%2BWqtNlBKbZbUvx3i5bi68Yp0QwIhANW%2F8%2F1xlRt4whZ5ptm6g0TBS6FN71jFCYBRwU1nAe3FKv8DCBAQABoMNjM3NDIzMTgzODA1IgyCP8eyuVRkQjDOvFIq3AP%2F891XxISSAcThj6V3EKzQ7%2B70Cjvk%2FrsZpeTY4rshVCMGd2toKe%2BpdJjGZ1dHHZjE0TqJlT8rTZc46TDZiDkdm3VQw7sRlWZduQOIggX%2FAJactx69PRM8Kde6xrvnm0pUnl8oEQ4abV6KVyEHlKZ4NhEvUHkZlzTfTwJdoXnmSzB%2Bam8uoUNK11jU43DhPmPnmcWqvsS1CNgvVeDDg90hwASJVjNX1WGAQuXSG4YxgemLxafc0kl%2BUQwagpMjUPcQ%2FuIHT8iAAEkhSI0L9l56X7O629G411J37fUNkqAUXynesvt2r%2FLHBXh9BOBcjqAsUajrUFvdPqhFoXOquSt9hVRoerUpnx2t4ENm7a6y7Pypffvih0WeksCa2ZReEiAwXeP5wTmwsBoKqCB3S0P37zf93q8Gh7L9%2FJ75YSbSLpTzF%2FjDwxI1GCEZLOXlF1vvM56BcHHH8xJk8XUgHbkst51Gw9PSH29bF1jXfyK31MjOA7TIOZwfM%2BaVDewvfRbXnoXBV7DwauXDO1Z%2BrnWu0fajNfL8W42Zc9uSrMrttLJwJdpbgMCQm6kwlNO183vr5vkkdC529XYho%2B9%2F0L6Wxtko5PBiHoKm2QZyDKpNZ5tIAeXOuihuN%2B0unzCZ1oG9BjqkAd5yLj0m47blO6bvZmLO5WhYaMDZGXWycD0gixioDfIwwOi05SZNS5us4L5mgpO534ByFddWh%2BFGQLTZZ0KBLBZnSZIFvKuMtv%2BuaB8auHLIjvQWSpmAbEFEuzJ4oy0jXo903lX7M5UjJUze76RXqDwzu5BseSuAhGZ%2BoJADbbXvw2lA1NIBaFIagFMOcpvLpdhJ6mD2WCLbxnP10ZL413rQ6mWh&X-Amz-Signature=66cbb15f385a604b88d2eabe4c84ee1ba7a9fd437f64d42a6b73422cafc9fecd&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Algorithmic Libraries
#### 1. **Scikit-learn**
- **Description:** Contains tools for statistical modeling, including regression, classification, clustering, etc.
- **Built on:** NumPy, SciPy, and Matplotlib.
#### 2. **Statsmodels**
- **Description:** A module for exploring data, estimating statistical models, and performing statistical tests.

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c62885f5-417d-4179-834f-d68f8f2bdf39/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466X3G3RNWD%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T071439Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDM8RzysxcWSpSNPWL%2F%2BWqtNlBKbZbUvx3i5bi68Yp0QwIhANW%2F8%2F1xlRt4whZ5ptm6g0TBS6FN71jFCYBRwU1nAe3FKv8DCBAQABoMNjM3NDIzMTgzODA1IgyCP8eyuVRkQjDOvFIq3AP%2F891XxISSAcThj6V3EKzQ7%2B70Cjvk%2FrsZpeTY4rshVCMGd2toKe%2BpdJjGZ1dHHZjE0TqJlT8rTZc46TDZiDkdm3VQw7sRlWZduQOIggX%2FAJactx69PRM8Kde6xrvnm0pUnl8oEQ4abV6KVyEHlKZ4NhEvUHkZlzTfTwJdoXnmSzB%2Bam8uoUNK11jU43DhPmPnmcWqvsS1CNgvVeDDg90hwASJVjNX1WGAQuXSG4YxgemLxafc0kl%2BUQwagpMjUPcQ%2FuIHT8iAAEkhSI0L9l56X7O629G411J37fUNkqAUXynesvt2r%2FLHBXh9BOBcjqAsUajrUFvdPqhFoXOquSt9hVRoerUpnx2t4ENm7a6y7Pypffvih0WeksCa2ZReEiAwXeP5wTmwsBoKqCB3S0P37zf93q8Gh7L9%2FJ75YSbSLpTzF%2FjDwxI1GCEZLOXlF1vvM56BcHHH8xJk8XUgHbkst51Gw9PSH29bF1jXfyK31MjOA7TIOZwfM%2BaVDewvfRbXnoXBV7DwauXDO1Z%2BrnWu0fajNfL8W42Zc9uSrMrttLJwJdpbgMCQm6kwlNO183vr5vkkdC529XYho%2B9%2F0L6Wxtko5PBiHoKm2QZyDKpNZ5tIAeXOuihuN%2B0unzCZ1oG9BjqkAd5yLj0m47blO6bvZmLO5WhYaMDZGXWycD0gixioDfIwwOi05SZNS5us4L5mgpO534ByFddWh%2BFGQLTZZ0KBLBZnSZIFvKuMtv%2BuaB8auHLIjvQWSpmAbEFEuzJ4oy0jXo903lX7M5UjJUze76RXqDwzu5BseSuAhGZ%2BoJADbbXvw2lA1NIBaFIagFMOcpvLpdhJ6mD2WCLbxnP10ZL413rQ6mWh&X-Amz-Signature=06767974ff2eb6608aff9f767fdd43bf1f420819d9946bec95090d5cf494f25f&X-Amz-SignedHeaders=host&x-id=GetObject)
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
