

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

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/997ac361-58a8-4f04-bb0f-79fea4baa761/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46637VYKCXP%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T010943Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEO%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICbGsof%2BstuMoZLk2DXRQ8mZOpMzaNZ2%2Bc6SdT47tJTWAiAmamBM9gIqlsxdde7uqMagw4YxnnkEWCjtNZDTqeA5iiqIBAj4%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM5D1u9uvdPQTYIwv1KtwD17IzXt5KiS9ob0sZZNCWrbiR3nNWwo31tWT2xHr16tMtbuk4YEI11HVjaswVwTljV6Uf1xrrU3nVXlVeYN0lrkC1Ej7bdqZNmX%2Bx3cBbNLz2TzBmtIAyklIha07BliXnBTqXwRyyw06oo6npIUnJ3dHXBv9Te%2FLPZQ87Fq0bNshMT5%2FSNPzXXyBJe5v8P8XcKbYk2znth7Q94EOQ3kv6J8DmqWQZtaob5HcMQ5iHatAqsxWdLA1FV04Td2PDOS3EUUTNW0BEIEuWoZXlMhj4P16v5HuwuvSC9%2F1AfoUi2t6lFCMOwOoYR416R7BZtQfxn%2BH4iJQ3Ayth3cTmAHn%2FvQlh6AiVzy4woTKYih6eGO%2Fr4BvLV8uc49PpPAtoQQc9%2BiaDhBo03ETjU4sALY1hGeeVjOCxWeoP3tgPzhptsLtTAWBK%2BHlbJrSvyfq68oXbPWvhZ4ZpSLLRbGfWbe6dL%2BynxziHjnA4oB1RgUCLSiXx3wgE4vamU86yPL9YiDNEi%2F8ne1V9jop%2FvJUZMQTMp%2BdrW2xZZ2yOgbwbD%2B5pPBKFtLFEo%2BWdwAFdrKeuLhgKesG9GseP7gV9o7Faox2kbCuDMlrG6RP%2BcrDMqh%2Bs5XM9Zw62mNuDlCRW5Bwws%2BX%2FvAY6pgHEQEfAXznrD8YJ3zJXEK8Tts%2F0Ep3o%2FTzLGkWxBsTY6gPZblEJtfiayqBhSwFN7LngubX%2BPBUsK%2FLUmVGTWTICkeKFsVrRzfq0iBcBQ87ECFuI6SHJdWsLbYFzPaVrV6VNoI1ADr9CM0CtLrmvS4q9p%2BDceKkgqvJEhORlvkaUBTlT2hHBm4SqPmAXF4sHM47X3obW%2FFJlkUkr5HM9btOY1wfaMC4B&X-Amz-Signature=7b94a13d5c6eb7ac8de33090292f8929c6d436abaef724c6f2823417623b001b&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Data Visualization Libraries
#### 1. **Matplotlib**
- **Description:** The most well-known library for data visualization.
- **Features:** Great for making highly customizable graphs and plots.
#### 2. **Seaborn**
- **Description:** A high-level visualization library based on Matplotlib.
- **Features:** Easy to generate various plots like heat maps, time series, and violin plots.

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/733d1e42-5a53-4fd8-90c1-3d85254369a6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662HOFVG55%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T010941Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEO%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIAsqjxWLJK3TAwy17RKDXD19UX3bGEvjNzLggeeJdJI0AiB9LVF7StR5Di4xLxlEi5BcwxQnq7QNkyAnUCew0geb7iqIBAj4%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMwP0X%2F1GjGBfNCzs9KtwD%2BNlhgmvJqNiZrCiGYpj1BUzUC7wVrr8s%2FuCI0dWWx1Oeb5XF6ur17aOMtlT%2BUgBOK3nDFMWNDHSdM6Iqf1tUk6%2FUvY8Yu%2F18KeqXeEh98rrU%2Bb1qt8Y7VqfyWZW9kgHNvCla13v9GzEyohIvUG0AbNEcR8yv93fIEk8iZVFIa%2BQCTtQTdKzcVSVgCGEK4HxI902kUiyG7VVHFsQiqxqj83bO5zGIkv0AD95DzPJDc2bOJQDlz8DzXFfnXSUvo%2FJQKxU7qyt3Uh4j0IxfcSbMReUAbeJgbagk9M%2FMHtqNIOedt0KGSSjdNBB3j2zI028obwY2aGX4bEnREUIXZIP%2FNJ4aJDg1%2FwMkmGVV8QGofPUSLGKvO7soC7ebqqPrXrPsd3Q%2BAmLZ4YlOg4EfsfT%2FXmvKqmddr4OjnRScdoBKKW1Berqv5PQ1IFFHyaya%2BnCLiPUVSTo7oY7oXGDjuW8itd0bSACAf1nFBDKA1dJHQAsZjjtKdexB9ZWIHOT8fQCfzjx7qNRAw5wavUchvCtuV4FEkADZErauzWCpYPx%2F%2F1AQWbe9ayhHWzuo49YBKiOc%2FpifbDYSOqqAm8UEBmdpVdDFhqo5ttaqUChP0%2FD4Rc7%2BZvfUWFvqeL8lZBUwzeT%2FvAY6pgGcn%2BqQ0HigUG20ZnqtfgPokVs6EXjrGwomsHXom0jh4DApl6j1mSwIZd5LdMlyHpI4fe79amCBgCqG%2FIb1zBuYQitjo%2FPpmc%2FfkCVG1BLfLxR8JgEOCfNPCi9VKqNIxoOybkcJZ6K7lIAwHNsRoxOSW5G9tS6vreI9UbVHpldmBvy9SdIsrRIhfyx%2F5eWTMwqlXnCpy7p7aPClIXBtjh5sg70hMdZj&X-Amz-Signature=87f80658eff7067bda61e0554e65d52c27a7876d5766a0c2f782df683cc98565&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Algorithmic Libraries
#### 1. **Scikit-learn**
- **Description:** Contains tools for statistical modeling, including regression, classification, clustering, etc.
- **Built on:** NumPy, SciPy, and Matplotlib.
#### 2. **Statsmodels**
- **Description:** A module for exploring data, estimating statistical models, and performing statistical tests.

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c62885f5-417d-4179-834f-d68f8f2bdf39/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662HOFVG55%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T010941Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEO%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIAsqjxWLJK3TAwy17RKDXD19UX3bGEvjNzLggeeJdJI0AiB9LVF7StR5Di4xLxlEi5BcwxQnq7QNkyAnUCew0geb7iqIBAj4%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMwP0X%2F1GjGBfNCzs9KtwD%2BNlhgmvJqNiZrCiGYpj1BUzUC7wVrr8s%2FuCI0dWWx1Oeb5XF6ur17aOMtlT%2BUgBOK3nDFMWNDHSdM6Iqf1tUk6%2FUvY8Yu%2F18KeqXeEh98rrU%2Bb1qt8Y7VqfyWZW9kgHNvCla13v9GzEyohIvUG0AbNEcR8yv93fIEk8iZVFIa%2BQCTtQTdKzcVSVgCGEK4HxI902kUiyG7VVHFsQiqxqj83bO5zGIkv0AD95DzPJDc2bOJQDlz8DzXFfnXSUvo%2FJQKxU7qyt3Uh4j0IxfcSbMReUAbeJgbagk9M%2FMHtqNIOedt0KGSSjdNBB3j2zI028obwY2aGX4bEnREUIXZIP%2FNJ4aJDg1%2FwMkmGVV8QGofPUSLGKvO7soC7ebqqPrXrPsd3Q%2BAmLZ4YlOg4EfsfT%2FXmvKqmddr4OjnRScdoBKKW1Berqv5PQ1IFFHyaya%2BnCLiPUVSTo7oY7oXGDjuW8itd0bSACAf1nFBDKA1dJHQAsZjjtKdexB9ZWIHOT8fQCfzjx7qNRAw5wavUchvCtuV4FEkADZErauzWCpYPx%2F%2F1AQWbe9ayhHWzuo49YBKiOc%2FpifbDYSOqqAm8UEBmdpVdDFhqo5ttaqUChP0%2FD4Rc7%2BZvfUWFvqeL8lZBUwzeT%2FvAY6pgGcn%2BqQ0HigUG20ZnqtfgPokVs6EXjrGwomsHXom0jh4DApl6j1mSwIZd5LdMlyHpI4fe79amCBgCqG%2FIb1zBuYQitjo%2FPpmc%2FfkCVG1BLfLxR8JgEOCfNPCi9VKqNIxoOybkcJZ6K7lIAwHNsRoxOSW5G9tS6vreI9UbVHpldmBvy9SdIsrRIhfyx%2F5eWTMwqlXnCpy7p7aPClIXBtjh5sg70hMdZj&X-Amz-Signature=f932d89af016b2031c389573d9d22c1d0f87fe58114112ab8ef278b2802cabd5&X-Amz-SignedHeaders=host&x-id=GetObject)
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
