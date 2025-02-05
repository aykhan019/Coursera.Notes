

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

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/997ac361-58a8-4f04-bb0f-79fea4baa761/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SJF3Q7PI%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T161847Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDAaCXVzLXdlc3QtMiJIMEYCIQCoOmhohlaXXhgdxGlljNj6fLzUS0PWQS8z9yVe5q0q5gIhAOA2urETLNo3IImkmOfUoBjvbD6rbmbpSysAHXlDyyvqKv8DCEkQABoMNjM3NDIzMTgzODA1IgwyhAv3N4fXzjqzwxQq3AOqj1GZ%2BjE6icAnsl3E6k%2F3rKJqYYVRvZyO05PY1QdmgaPo%2FiHT0nsPHAwNgfQRnJbrBz0S2MfYfikwE3hsMzUUSEPyV%2B%2F4pc8ZaSQ5Ls2YdR5JEOsya%2FPWi8s5iBfoeo%2Fo823nKZeFYkzl4Igy23BcuErYkfKhXURguAu6r2K5W59JeMgmFSqMS9ECZerQCqiH2p%2FCNiUvO2OssUdLyeA4RWMIRwNMcYw6VIQbqWIpHeJElgawqu0PwQZ%2FX%2FD%2Bf8BByGsS4mLBwdSgwB1xYU5zhwPgyHkF%2BgHNqSJaEXiitD5XjyZ9ZMBRYhApUlXRKV5sVmt0RRuynziu%2BuikWp7Pqz5dw9mE%2BuLwYF1z4q3l%2FGtavT0RfQIILdkorcKfH8D09w%2BE7ZUdm6V%2FfQUup3QvszLwlRQb9bp68ZzxN1%2FMFZUIS%2FD71cV2p%2BO9YVuJ0eKFWqvvg1j6ZBSN4wHmsp%2BIvelZS3qlqulXd6KldM%2FbSPQsg%2FfMOWv%2Fmb57CqR5NlW2SWa70Jeaxcwa4VvgaGmLan6CcU5beNx539%2BKqv%2BoBRswLOcqVUQkx8iKbDh6lEL12ihyfIem58KsidGoeZQ349AXYAtwOkUY3PjnMzJiAVxscWBJ%2BJyV7faw9jCvnY69BjqkASnKFsdh19YSUbGmyQ0oo2%2FvUPGO2HQc0DCyHg5DUVPR7KtTvgypUP67isOGZj30xOg0GbVXxbTXa36HZWnv2r0R4YsVWgQrVGEuu8e6pOD7%2F7rNteZSR4v7nu3%2FAPGa9yohKCBny5THmkX9tgmLxw1UW3E9jU6AQGgeiGkGzpDEHcFDGKdbIBFWTn42bErwQROQTaGj072z4hVOzVrkadFKj%2Bbt&X-Amz-Signature=fa305029a5b7c7556d2be3f6c503bd0514d361e53697351e8267e521ba360ba6&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Data Visualization Libraries
#### 1. **Matplotlib**
- **Description:** The most well-known library for data visualization.
- **Features:** Great for making highly customizable graphs and plots.
#### 2. **Seaborn**
- **Description:** A high-level visualization library based on Matplotlib.
- **Features:** Easy to generate various plots like heat maps, time series, and violin plots.

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/733d1e42-5a53-4fd8-90c1-3d85254369a6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TKB4UG5Q%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T161846Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDAaCXVzLXdlc3QtMiJIMEYCIQCSn3N4MKJU2NRSTyAvWV4K%2BsFUgQ5eYXJuQzprq8bTOQIhAIpiALVYk8lnymlhyP3hx66AamG7w7NMfadxqdNkRhHvKv8DCEkQABoMNjM3NDIzMTgzODA1IgwCAwKHiX%2FCDNJdWGkq3ANrc47AtkcpzHVo6rLCylBsSlb1ZKgrzlf8wniV2SqHoQ4%2FrHJE1MrM6m7yB5EpILHL1BqEO%2Bgf3Hvura6u8V1rBztzrMxP6yRcPtkKMjSJAFYn8X2f5qHHKxct9LG2%2BD9TduEwKYVSHvkDBLbn84S3Qkl3AFTp1wmVWDLj1lKZnCFrl8rf3i47IgJbrJVy7oIoJjk9NjeavM5IpzvWnRByKa2HJoW3kDkru6bDoykx0muH0XfIuZDfk9kjrqnlmXWmWdpFLvul94ncmB8D35Zn8gdlz1PsIZ%2FPqFkdJ2pGa7h2IOstq0sfTioLkzAA1BQ8zpnFCLcgmCYlF6rhWDfCoIlrFNe3s4VB1%2F99ZmPmTSB2dfe%2FOFKD%2B9fMjljG0hSTZRMOltefNyj7VSs4qFMNOfESll071kS5XC4LWjKI17NUnH7I0zc%2BEH5NK%2FxXzJ0DIwF4ZK3XCYJP8yzOcW3pdjqdNM1Zq7K0M5TRTl%2BtZ2uMahCs7cTASfavvGbxd6AvGqYTp3m1iIwa1z%2BEznUGCcEtWxtn34vb4AhNw33xxC9l%2BVSOczGrBuCqU2mNYP4a0OqPvmxJhJHpwljsHv9i58OW0e6uq3gOCKdzNk6NfPBD%2BQfZ7Cip6SCtpjDhnY69BjqkAf58VBsMh0vhYh%2FJCH5%2FCoAisg6ZRu0zBfaT1xdaIpLUurZ3oqhYOCygx5Xey6dTCHb57aQ62CIyjMvpsgu4%2BKXtyge1ktK0ANj%2FK%2BoaaUVS2UEBrlAtSSUoH1YbrL1%2FOx%2BHFVQxcsgWS6rtj%2F1jQGGsT8fen3IMMUHW8scq5Dd3f53Il04NdhL0E%2Frw3A3%2F7a%2BRQnbUL9ngLyxeKbhFQk2bl3%2Ba&X-Amz-Signature=6df5ce075020be5235d207a52853dd117f49d6b29a1cdbb0b4db768ba10e583c&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Algorithmic Libraries
#### 1. **Scikit-learn**
- **Description:** Contains tools for statistical modeling, including regression, classification, clustering, etc.
- **Built on:** NumPy, SciPy, and Matplotlib.
#### 2. **Statsmodels**
- **Description:** A module for exploring data, estimating statistical models, and performing statistical tests.

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c62885f5-417d-4179-834f-d68f8f2bdf39/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TKB4UG5Q%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T161846Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDAaCXVzLXdlc3QtMiJIMEYCIQCSn3N4MKJU2NRSTyAvWV4K%2BsFUgQ5eYXJuQzprq8bTOQIhAIpiALVYk8lnymlhyP3hx66AamG7w7NMfadxqdNkRhHvKv8DCEkQABoMNjM3NDIzMTgzODA1IgwCAwKHiX%2FCDNJdWGkq3ANrc47AtkcpzHVo6rLCylBsSlb1ZKgrzlf8wniV2SqHoQ4%2FrHJE1MrM6m7yB5EpILHL1BqEO%2Bgf3Hvura6u8V1rBztzrMxP6yRcPtkKMjSJAFYn8X2f5qHHKxct9LG2%2BD9TduEwKYVSHvkDBLbn84S3Qkl3AFTp1wmVWDLj1lKZnCFrl8rf3i47IgJbrJVy7oIoJjk9NjeavM5IpzvWnRByKa2HJoW3kDkru6bDoykx0muH0XfIuZDfk9kjrqnlmXWmWdpFLvul94ncmB8D35Zn8gdlz1PsIZ%2FPqFkdJ2pGa7h2IOstq0sfTioLkzAA1BQ8zpnFCLcgmCYlF6rhWDfCoIlrFNe3s4VB1%2F99ZmPmTSB2dfe%2FOFKD%2B9fMjljG0hSTZRMOltefNyj7VSs4qFMNOfESll071kS5XC4LWjKI17NUnH7I0zc%2BEH5NK%2FxXzJ0DIwF4ZK3XCYJP8yzOcW3pdjqdNM1Zq7K0M5TRTl%2BtZ2uMahCs7cTASfavvGbxd6AvGqYTp3m1iIwa1z%2BEznUGCcEtWxtn34vb4AhNw33xxC9l%2BVSOczGrBuCqU2mNYP4a0OqPvmxJhJHpwljsHv9i58OW0e6uq3gOCKdzNk6NfPBD%2BQfZ7Cip6SCtpjDhnY69BjqkAf58VBsMh0vhYh%2FJCH5%2FCoAisg6ZRu0zBfaT1xdaIpLUurZ3oqhYOCygx5Xey6dTCHb57aQ62CIyjMvpsgu4%2BKXtyge1ktK0ANj%2FK%2BoaaUVS2UEBrlAtSSUoH1YbrL1%2FOx%2BHFVQxcsgWS6rtj%2F1jQGGsT8fen3IMMUHW8scq5Dd3f53Il04NdhL0E%2Frw3A3%2F7a%2BRQnbUL9ngLyxeKbhFQk2bl3%2Ba&X-Amz-Signature=378f427593548c21b209b50ad36484d244464cf77359e8b61bd393c2eaae48a5&X-Amz-SignedHeaders=host&x-id=GetObject)
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
