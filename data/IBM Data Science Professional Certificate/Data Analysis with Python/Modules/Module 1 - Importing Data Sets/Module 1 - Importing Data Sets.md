

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

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/997ac361-58a8-4f04-bb0f-79fea4baa761/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Q4WO7O7G%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T201430Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCE1dDtOy%2B%2BKeiVz7hJwCjvaHW%2Fw6ACpvtHKkz9RfJvpgIhAO0VaWGHVNb8ekhY53v0DKuxPA6RIZu1ptFVz%2Fs1q7EIKogECPP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwX%2Bv39camNEmqRy4Qq3AO2EO%2B%2BN45Iqen%2B2S113urKbdEvynIkWU5yZs2rGvoz8eVEu5znIy8pAnhsiVXWwjmcOXna7qUaKcihLh7NsV%2BIM757%2BVLqg0vn4E8INY0wv5264GKh%2Fon09NQw63eO9VzoKahXTtHEuTlwvicbqbM7jWZqTODakPL%2Bj7lCAUu5xf0sS7TpIJ2kxnCtF3Kr17HAW%2F9O2altIgXdXWJVJvcooPgTgcT9tXWJGvDIjUgewjanjcFhtwEJGVJzyE1uTCpIXf96hlgaZk583uzVLfGCup3NcZhB2jxH%2FdXGucKKNuyKNag13dXcaXxOc7YI%2BukGJpgcVPwNuhrBQBUn1IK27s%2FGj%2B%2BhP3Fjd3PYTbusVmuHK%2BhSniI6lfMTGoo0eVVwQYQ6FZm7QH14gBcXR9VqsOMAwB9TnfW%2BsnRIItXtgxWXHPLcW7ooKoqYSMxTTby%2FarDOzx6ZOl%2B5vgV8jY67bi1wuVNwUs45kXUqhsl9OH5YwwZ4%2BF6t44xtZh%2BL4DPC2swk6SmHmSvuoEe33osWbmLcl0ErzLhzhe%2Btx%2BkRiJBNMXOs7UEeO9rf8NBdqwm48pa%2BsqMOnEhJGLU5ETdcczykilfYNEu1W9bMOR0paKiOSaW6x%2FkLxA1zfDDQ3f68BjqkAYQgRsX5hGEOJe2orSoKyh3PTzsdKnmuclJzFCO7x7fpY1%2Bg4yvn1MJ3%2B6%2Fa%2Bgu%2BqRsJ%2BL46K2QbhyZqCOTXYrnAPCF9Vsy2FrXT9dbRznF0vvb7oEiNlOWF%2BXzyc%2Fa%2BM8dHFZyIs0g08PqI69LzwrSDwWSPnyjSGfrVVd8fuiLCE0sb0d2z7LdClD6OJ4LWSSPHlET8F4cvGEJP6E2LPyeQ0Lk6&X-Amz-Signature=a3c71b450b78d83f8b452dafca4505bf955be7a3434256a64c7143e4dc77883b&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Data Visualization Libraries
#### 1. **Matplotlib**
- **Description:** The most well-known library for data visualization.
- **Features:** Great for making highly customizable graphs and plots.
#### 2. **Seaborn**
- **Description:** A high-level visualization library based on Matplotlib.
- **Features:** Easy to generate various plots like heat maps, time series, and violin plots.

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/733d1e42-5a53-4fd8-90c1-3d85254369a6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UTPLBXK7%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T201429Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCICwL6Udbh%2BJXvbrayL1ks5m2U4nylEb8R8xO2r%2BPVLuCAiEA6UZPk4JKgnFLj8BtsZi93KV50LK2fN9e4IVLecP37TsqiAQI8%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKTtDfS%2BF%2FHHOMG%2BISrcA9sYIKkgD%2BuOY0mUaF1ewKxXziKise9hxDyTW7dlrimzQRAkfOAlZop9ncq8OUO872FYlvngBRMHBnBs%2BCGEhaf25nxg4goE%2Fuagm0g5nN1gtbohqDMpEv7wgy0FMXovv9OVzv8ULQ1MTZRCSWbko4jB4d2uaOAQG4Oit8AtnDeUOgmCxe81joMv3MbIE5y6GRgMyYOkY4NY20CCNDptBkJ0LrPXUv%2BU5ROUk4G3K%2FapPkRCffWIfQe0Vt0JDjPDQ28gkwNCvYW5c%2FOQQYYW8NqDyynYq97uvwBras2qG5dTQ7uMwtpVnIYBcWCTtL5GAUtsG%2FwarXMzQw6rvrdUCHkeIoJHnj04uWvf7GWc0dlYzW7KCuO%2FfWChAShDYoFDsKfCs5DT9DzNGr5kWBFr6kFJS497tBNG0M6ivnFg8MQjh5vuIT9J3I7Xm9w5HzZYuRfbiNordF78KOcyhbmG6vsPHFSWNQIEyWCBrklLHN%2F0xzFu%2FsT5UyjaIc6dIE5gHE9UkuKAS1l6o5S8wAOGqOC60wX4qFEct3c6W%2Bkg1kIJIVN0LW9SKjklNXtmxuJTsRoRy0B%2FdKsA%2Fw%2ByVDCuwyhkF5AUJ7H%2BrQfczjYNAG0scmC1Y%2B9xFA3GS8jXMOHd%2FrwGOqUBHu26LVC8%2Bi9ffEV7JiG%2FpfFSfxdQf7gRVwS%2BTK3i56Xck3xZggXw2JGKSGwdXuDQq3DMSdn2hAojXpjlcSO3FgmavXxxFjV7KnC5PGr5iOZnrZrP5O6VYMOb5RlPc405PHpePYEc1HigOizqb%2BYr1j2F1MOaBxYc6mSgGaLRG%2Bv5cW4SUWukMqSpD%2F5Jstyqm1CqPsXwQmdYNubMxEgMESLr5mjY&X-Amz-Signature=49830c1dc3f3370dd5571e7acf9283b91b6044619b5d55b21223e4364dfb071c&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Algorithmic Libraries
#### 1. **Scikit-learn**
- **Description:** Contains tools for statistical modeling, including regression, classification, clustering, etc.
- **Built on:** NumPy, SciPy, and Matplotlib.
#### 2. **Statsmodels**
- **Description:** A module for exploring data, estimating statistical models, and performing statistical tests.

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c62885f5-417d-4179-834f-d68f8f2bdf39/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UTPLBXK7%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T201429Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCICwL6Udbh%2BJXvbrayL1ks5m2U4nylEb8R8xO2r%2BPVLuCAiEA6UZPk4JKgnFLj8BtsZi93KV50LK2fN9e4IVLecP37TsqiAQI8%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKTtDfS%2BF%2FHHOMG%2BISrcA9sYIKkgD%2BuOY0mUaF1ewKxXziKise9hxDyTW7dlrimzQRAkfOAlZop9ncq8OUO872FYlvngBRMHBnBs%2BCGEhaf25nxg4goE%2Fuagm0g5nN1gtbohqDMpEv7wgy0FMXovv9OVzv8ULQ1MTZRCSWbko4jB4d2uaOAQG4Oit8AtnDeUOgmCxe81joMv3MbIE5y6GRgMyYOkY4NY20CCNDptBkJ0LrPXUv%2BU5ROUk4G3K%2FapPkRCffWIfQe0Vt0JDjPDQ28gkwNCvYW5c%2FOQQYYW8NqDyynYq97uvwBras2qG5dTQ7uMwtpVnIYBcWCTtL5GAUtsG%2FwarXMzQw6rvrdUCHkeIoJHnj04uWvf7GWc0dlYzW7KCuO%2FfWChAShDYoFDsKfCs5DT9DzNGr5kWBFr6kFJS497tBNG0M6ivnFg8MQjh5vuIT9J3I7Xm9w5HzZYuRfbiNordF78KOcyhbmG6vsPHFSWNQIEyWCBrklLHN%2F0xzFu%2FsT5UyjaIc6dIE5gHE9UkuKAS1l6o5S8wAOGqOC60wX4qFEct3c6W%2Bkg1kIJIVN0LW9SKjklNXtmxuJTsRoRy0B%2FdKsA%2Fw%2ByVDCuwyhkF5AUJ7H%2BrQfczjYNAG0scmC1Y%2B9xFA3GS8jXMOHd%2FrwGOqUBHu26LVC8%2Bi9ffEV7JiG%2FpfFSfxdQf7gRVwS%2BTK3i56Xck3xZggXw2JGKSGwdXuDQq3DMSdn2hAojXpjlcSO3FgmavXxxFjV7KnC5PGr5iOZnrZrP5O6VYMOb5RlPc405PHpePYEc1HigOizqb%2BYr1j2F1MOaBxYc6mSgGaLRG%2Bv5cW4SUWukMqSpD%2F5Jstyqm1CqPsXwQmdYNubMxEgMESLr5mjY&X-Amz-Signature=92168f22d7d3ecad89a417a9c76ff0bd64051a2b328611d51478401b3ab34825&X-Amz-SignedHeaders=host&x-id=GetObject)
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
