

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

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/997ac361-58a8-4f04-bb0f-79fea4baa761/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662555IVCO%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T051407Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDG3aSSfvc%2FeQ%2BEuGRatZf8NWPxlQZR3QmhNEFP48ygmgIhAMkXieFyAtkYoFDdKy2tyW%2B99%2BvE5VKjiMJvIB9w1V6GKogECOX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igw%2Bhzdt9%2B%2B%2BXPzNfAMq3AOx6%2FrFzCVTGj6IRyVYa%2F3mgYqtDWoTKgqhu7J1EEgga%2Bns2u4yVrKNJAYaKg%2Fw2h%2FwaJBiooMQkA9WVywY1bbs7Vzdkaw4HKOmiO7ZmGeKVJqaK2yAiTJ1M2tXD4Q2hfoI7UkUO8nRGiZD2hUXOtD4npc%2FAhbZsExYyCYq6JJ5FzpDSqnILZQzakavS%2FxDMfP5wp8HmKGZ9M8GzKJBMMP2dL9IdkbHYG1dsI5lxqLQz0DPt8px6qEsVINCUkJ%2B4ElgqitJ3H2GehESGvuaDUsHLg4MLHiTcjmY6Df9x5xlS6d%2FUQ%2F0Hq3ipZY6rFv%2Fzsp8%2BV50EN9f%2FH%2FrC07aj2%2FkHUNzLHdrDIMDpoOK5q%2BOXHNtMldpflPt34dFy1blkUhTS8voUiCd5jAJWWRjrNkXcTNjr3eemrS1ioptT9PQCLROKeP8uryJ3D6t2FLKRHeOx%2BTp2wSEWwgAxOUeCkRaJG21P9MZxm939a7ILmHA7kF6GkdWEhbyF%2FNszDMhhpgjXq%2ByTsmHjI79Zy6uMbILXu39jsCw5jNKPoD8PfRG5mWyB04PxHNieE6ZWiAyBykSMscBfDtzvq459H8aKxCFvK8OzhxObBpbi309UFgoCgUjraP2FprYWE15PzCC4fu8BjqkAUsL2Z3VhN13at5ao4wdesgIoLWygiUDAChzL%2Bq0p%2F98NdGcYBaNervgNNmxmvKrvye8OaO145qrfpJTM1lO0dv9e31EXZ61j9OBy9yGeaRDTMJIcn3Z4RNT%2FtCfkvOLq62vNOQtprzqy0%2BlGwcg2jA44WZxsHDOMxV7nrTqv%2FaVusxwFp4MxjoAx32%2FspD0phXQjUroi0TZCyNyTURfyLVgsF5a&X-Amz-Signature=443ddf423a04ebdbf640db2155324bc9f9209e637968ebdc103ba4f3866a177a&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Data Visualization Libraries
#### 1. **Matplotlib**
- **Description:** The most well-known library for data visualization.
- **Features:** Great for making highly customizable graphs and plots.
#### 2. **Seaborn**
- **Description:** A high-level visualization library based on Matplotlib.
- **Features:** Easy to generate various plots like heat maps, time series, and violin plots.

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/733d1e42-5a53-4fd8-90c1-3d85254369a6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UW73NOP7%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T051406Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEqYE0dU6StNgTb5HKv4EUhJmCru1IP4PTxf4LtTO%2B0cAiBO4T5lX0F2P6oOfynS7ltE9Je2KL1ktnA%2BkSFL%2BjNkYCqIBAjl%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMKe35U5I6iPZ6omXxKtwDhD6X2bJYk5%2BAihks2EIQDiyP%2B0yMK0XC1PmO%2BMEK0p0A0VBeHLnePptwrr9WMICMK10j3rB2347dEoUvIINrt6em5HFmiPLY0mwCgG4%2FgOxA%2FIHrgiN3mv7%2BtEx4gB2N44h3EY8VteEm91olWRDjmc1ddh6uumOaxXnXDUi55ANpDkQIsT7glxHzEj4pv8pNvVeMDmBQrYQ0%2Fd6XGAVfpd7AfzXvtlpzkNn5BAg%2F%2FJbdneRS8qEgzZQ0cvj8TG%2F0sQYUAbwlWLR609ao3DNekbSyVK9R5yyQFlif8lZ%2Fh6BcgiPFgnC4qwzNnWha%2Bm6IDT5uacKyXvzbu3TbdptkgTrITIMF25pkfSCfnmORAR8negatDI2YUKY0RZGg3y25rx9tH7T6jxfrYE4mSbY52St1EuPv%2BlQ9EJ7jgLaKhYB4jeDUgRZEgpjbtLMfmlD4%2FHbXHTZ2WugB2tLC1Egyt7pv7oC909%2F1LfelwzUkU65osWXwKneKcvj0tC0fmL6amnJwCSHhvbg%2F5gTSoXc1VydEg54GZptp6YU6vsBj17F2SxGMBL%2FW0OvRzX%2FB7qvgqD77QU5h%2B36nl3emiRdnD%2BifMR%2Fz55R%2F1laM58hRkIYycbXH4nrnVJ%2F7ofMwjeH7vAY6pgF5dVumBIJhC1gqcw0T3JOaht7JsZcivYr%2Btdba4tHmySFq3e8DIycE5besLjWHHSIA1C8%2B9gNQqojQaFRi0Pw8lzkBKfknMYE11cPsqizxF8MNDKLcfGJ15MwR%2Bb5TyNMK%2BErVRj%2B54S9reBYI7eL%2F5VLLzn27NOHEpzzrAH%2BILrfh36V1slmihRXxNSQ2vBG%2BsUpxIDdALpHZXV2uqB%2Fdo27vj%2BiO&X-Amz-Signature=137ee449dacf9e66d2271706937d13299f294711515e11c9d0a80f0e4e989720&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Algorithmic Libraries
#### 1. **Scikit-learn**
- **Description:** Contains tools for statistical modeling, including regression, classification, clustering, etc.
- **Built on:** NumPy, SciPy, and Matplotlib.
#### 2. **Statsmodels**
- **Description:** A module for exploring data, estimating statistical models, and performing statistical tests.

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c62885f5-417d-4179-834f-d68f8f2bdf39/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UW73NOP7%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T051406Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEqYE0dU6StNgTb5HKv4EUhJmCru1IP4PTxf4LtTO%2B0cAiBO4T5lX0F2P6oOfynS7ltE9Je2KL1ktnA%2BkSFL%2BjNkYCqIBAjl%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMKe35U5I6iPZ6omXxKtwDhD6X2bJYk5%2BAihks2EIQDiyP%2B0yMK0XC1PmO%2BMEK0p0A0VBeHLnePptwrr9WMICMK10j3rB2347dEoUvIINrt6em5HFmiPLY0mwCgG4%2FgOxA%2FIHrgiN3mv7%2BtEx4gB2N44h3EY8VteEm91olWRDjmc1ddh6uumOaxXnXDUi55ANpDkQIsT7glxHzEj4pv8pNvVeMDmBQrYQ0%2Fd6XGAVfpd7AfzXvtlpzkNn5BAg%2F%2FJbdneRS8qEgzZQ0cvj8TG%2F0sQYUAbwlWLR609ao3DNekbSyVK9R5yyQFlif8lZ%2Fh6BcgiPFgnC4qwzNnWha%2Bm6IDT5uacKyXvzbu3TbdptkgTrITIMF25pkfSCfnmORAR8negatDI2YUKY0RZGg3y25rx9tH7T6jxfrYE4mSbY52St1EuPv%2BlQ9EJ7jgLaKhYB4jeDUgRZEgpjbtLMfmlD4%2FHbXHTZ2WugB2tLC1Egyt7pv7oC909%2F1LfelwzUkU65osWXwKneKcvj0tC0fmL6amnJwCSHhvbg%2F5gTSoXc1VydEg54GZptp6YU6vsBj17F2SxGMBL%2FW0OvRzX%2FB7qvgqD77QU5h%2B36nl3emiRdnD%2BifMR%2Fz55R%2F1laM58hRkIYycbXH4nrnVJ%2F7ofMwjeH7vAY6pgF5dVumBIJhC1gqcw0T3JOaht7JsZcivYr%2Btdba4tHmySFq3e8DIycE5besLjWHHSIA1C8%2B9gNQqojQaFRi0Pw8lzkBKfknMYE11cPsqizxF8MNDKLcfGJ15MwR%2Bb5TyNMK%2BErVRj%2B54S9reBYI7eL%2F5VLLzn27NOHEpzzrAH%2BILrfh36V1slmihRXxNSQ2vBG%2BsUpxIDdALpHZXV2uqB%2Fdo27vj%2BiO&X-Amz-Signature=e2ac0831dccf2ff19c95bd176f32f84e20ed7c167bcc0990844db8d36d0d9fe1&X-Amz-SignedHeaders=host&x-id=GetObject)
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
