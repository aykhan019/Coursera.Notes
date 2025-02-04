

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

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/997ac361-58a8-4f04-bb0f-79fea4baa761/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WCRM4JMX%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T141358Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBYaCXVzLXdlc3QtMiJGMEQCIF6FP4PdOQXMZHLLLMqYGmXvOlPtkVs8bd43Xv8gPCY1AiBcR9OZoxZE0g29XF3VDf1zyWoQ3fwU1hl1Fr3pjVtmbSr%2FAwgvEAAaDDYzNzQyMzE4MzgwNSIMJRkaoEL2WgNCwtMbKtwDo1ZcCzIdi0kAh0UvW1N2CzCv%2BG2ZA0yEFhNa0NVyifMAyUzwKCnY7JJN5IKQSyDOQAd7iQUL6tKMWajZPy08Qh03Ys9KAy9nT8JLHeGcfW5xWODTaS7%2Bjni6prO%2BqV76nbK9Uq3IhcTzb6MEF%2B723BcZNWxhVjJo0EO69yG1R3q6BX%2FqxAf1s2NpT94%2BmtpDp8PFQROUS6aFHJPXqlHJ64iOIgW4jm9yJc6CWItjf86P9DJZlhsnZRuKJtIhEhjTpVjD6pg2zrHpopOay6U4p2IuNNATMZp9kC23dL7f2oIHwWlq%2BLYGxHJe%2B6HJGgwQ75QQHokALaARCzauHPgt4A5J1DDdQJncPeIc7b6YiEeJMSvWx4WklQrusueSGKOx5Gug2pPW5x39FBPMkhDVKgDYpvsggu0K4fTRBjpV8JN%2BpTiKZXREBFpaPheslzpIQFxjE7T%2F7jl8LDxzpKSzrAlWdsQjvVQFA4PiNCkl%2BCiK6F3MrDhJ0xJdoSxzxdMZDI917UOzryIkpmLDKi6hOLc04C9SSkreQs2r0DoiqhsAgEuanUZ6uER8qq1j7CUvmTYM%2BI3OpfQrtGR%2Born6vyvNvZYz5eQJjZrrzefBNzdgQo%2FTOckHGUKTUZkwy7yIvQY6pgElDQVqjSI2Ede2OpKx%2F%2FbjACDhFS5iu0nymf4RTgvFi5CHtP4KIfksSRilLa2uuJ8Cu5ZEfABWuOOQfLHglPJn4qIJaCi5UTBdYozBGoJH09c1ETNPURBKdM%2BvMxwcVB0SU1P5Jno0%2FqLjHXg2QmKvsosxOqfkv2iYJ1H0pcphIw0RoxUWam6%2B0cfRvPWKIGLFEDNE%2B1kavLGncd%2FYm59jjhykoj2z&X-Amz-Signature=470e6c636c8a71898b024b886d6930a45d73ebe5afd231190b8bb05281dbe9fa&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Data Visualization Libraries
#### 1. **Matplotlib**
- **Description:** The most well-known library for data visualization.
- **Features:** Great for making highly customizable graphs and plots.
#### 2. **Seaborn**
- **Description:** A high-level visualization library based on Matplotlib.
- **Features:** Easy to generate various plots like heat maps, time series, and violin plots.

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/733d1e42-5a53-4fd8-90c1-3d85254369a6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XMJCGOLH%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T141357Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBYaCXVzLXdlc3QtMiJHMEUCIQDjqBObU%2Fc9OYj0%2FkPwvnRioMJa7UKPk9hTLaTd5ivLJgIgW2bb65r6lZNboZKOM3FPT2CKCTOMXdeibJz5wkd%2BxgEq%2FwMILxAAGgw2Mzc0MjMxODM4MDUiDKRzzfNgHdrh6HIBkCrcA7gR305a5Y0O2F7Tx6VdWkVVzuJBRUWXOI%2BFphMt0IAhEzSKJXymjDgyUKK9Q%2FKBUo6YlNWnHQv72VIxr9tzNORkgXHgDtTKmHOxyB19lIAfJx%2FSx%2Fjqz2HV%2FogJ90Z8wpPEFSaJdfoQ3kTVTQluVFVa%2FJhxZHzAXRVwXqv%2F9aznTOiIviidEc90BBuOduvqdhQQ8a3ha39emb%2F0yVT%2Fegv6o3lCAnHGGjIYHic4B%2FSNa8v3MJIXeX0eIyc1xctSZCUt7WE0EzhDB%2FDoXDX7DnMeDAPBjUFMdVtd9pWnq9RQSlmJwlaNZ5QDpECQXFbMlZ94eNkWEjg4ZEJ1CrcoHP5hH0O2JJG0HE9UDmf8oEQ9DyYxqk2jUkTN6OGvcRNuLLRv09m2oHwRHeNCfbjQ2yI7GOG%2FAGuVyik1f922aOP3ODc4bbva83VaK8prmkyn8LUcX4Bd2OkJl9atciUtsR5PCMBnp8JHexfpIqJi7bXT2fgww5Y2%2F%2FYxvYmbfSt%2FElezb4DspA23LCmMvUzxTur%2B7TAT%2B8g8O4RjMF4tgJZKZkdjAFXwmgalP8pahxnqpRZs4LJPOa%2F%2F3R2Zw2lNHgcdSwK0tRBxULAMceci%2BM1gmSM1LV6EyT7cEEBKMJC9iL0GOqUBoHIAyD9SRKkrFA1Txxs70pzmfJBqQ6f%2FkhtwnY5TEgXME05TS%2BfsxM8nhKb2xCOOOrFKjiCCFzDC7Cj16IXp2fZ8%2B4KioaBUsVD86xv9eQTJn%2B2grblLFIuqe43pW2viR8%2BL9Cah3WotMh4xkgbZ0ZQlx2km1MgURe6iUsEv7tvRuYOgthpiDRGj3aUKG%2F5yPLhzV%2FDtECAfeGQSG%2B1VhlchjXZ%2B&X-Amz-Signature=3852b271f91d766b507f774df9355c3bbca83e06dfbc09a87e8714563ee651a8&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Algorithmic Libraries
#### 1. **Scikit-learn**
- **Description:** Contains tools for statistical modeling, including regression, classification, clustering, etc.
- **Built on:** NumPy, SciPy, and Matplotlib.
#### 2. **Statsmodels**
- **Description:** A module for exploring data, estimating statistical models, and performing statistical tests.

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c62885f5-417d-4179-834f-d68f8f2bdf39/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XMJCGOLH%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T141357Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBYaCXVzLXdlc3QtMiJHMEUCIQDjqBObU%2Fc9OYj0%2FkPwvnRioMJa7UKPk9hTLaTd5ivLJgIgW2bb65r6lZNboZKOM3FPT2CKCTOMXdeibJz5wkd%2BxgEq%2FwMILxAAGgw2Mzc0MjMxODM4MDUiDKRzzfNgHdrh6HIBkCrcA7gR305a5Y0O2F7Tx6VdWkVVzuJBRUWXOI%2BFphMt0IAhEzSKJXymjDgyUKK9Q%2FKBUo6YlNWnHQv72VIxr9tzNORkgXHgDtTKmHOxyB19lIAfJx%2FSx%2Fjqz2HV%2FogJ90Z8wpPEFSaJdfoQ3kTVTQluVFVa%2FJhxZHzAXRVwXqv%2F9aznTOiIviidEc90BBuOduvqdhQQ8a3ha39emb%2F0yVT%2Fegv6o3lCAnHGGjIYHic4B%2FSNa8v3MJIXeX0eIyc1xctSZCUt7WE0EzhDB%2FDoXDX7DnMeDAPBjUFMdVtd9pWnq9RQSlmJwlaNZ5QDpECQXFbMlZ94eNkWEjg4ZEJ1CrcoHP5hH0O2JJG0HE9UDmf8oEQ9DyYxqk2jUkTN6OGvcRNuLLRv09m2oHwRHeNCfbjQ2yI7GOG%2FAGuVyik1f922aOP3ODc4bbva83VaK8prmkyn8LUcX4Bd2OkJl9atciUtsR5PCMBnp8JHexfpIqJi7bXT2fgww5Y2%2F%2FYxvYmbfSt%2FElezb4DspA23LCmMvUzxTur%2B7TAT%2B8g8O4RjMF4tgJZKZkdjAFXwmgalP8pahxnqpRZs4LJPOa%2F%2F3R2Zw2lNHgcdSwK0tRBxULAMceci%2BM1gmSM1LV6EyT7cEEBKMJC9iL0GOqUBoHIAyD9SRKkrFA1Txxs70pzmfJBqQ6f%2FkhtwnY5TEgXME05TS%2BfsxM8nhKb2xCOOOrFKjiCCFzDC7Cj16IXp2fZ8%2B4KioaBUsVD86xv9eQTJn%2B2grblLFIuqe43pW2viR8%2BL9Cah3WotMh4xkgbZ0ZQlx2km1MgURe6iUsEv7tvRuYOgthpiDRGj3aUKG%2F5yPLhzV%2FDtECAfeGQSG%2B1VhlchjXZ%2B&X-Amz-Signature=79f60cd4668e8c228ddaab38af8e679e7feaef5624cc2430b3ad427a01e7ddd9&X-Amz-SignedHeaders=host&x-id=GetObject)
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
