

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

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/997ac361-58a8-4f04-bb0f-79fea4baa761/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664MANP56X%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T061855Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCeIviU9%2FsqagB5XS0pCdDGss5Lt9e01P9ih5mIB4xE%2BAIgSicKnscTWNogb7gQ9CB%2FQLdMsOC3BJ66vqZCnVl7jX0qiAQI5f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHbLm5BJn%2B8h8GNwyyrcA%2F%2FvsuVXkQueyS0XC%2FCTnyC8oSWjubzHe9JirL7B4MvYn6SZWVzJB4%2BMdZYi%2Bw0XsYVnnXYCBtezcUDlZvJQMyOZTx2QVNdyGa7OKoMgl657tQYjFvSygu3GVq5%2FKXvEhq0kDjuTM%2Bz2vgNBaaDnP2xnUSQUXQc6q3bKUG%2FQtDCj5eWxG2Qj7JKvKol%2FRLt1llozdrnD5poLx%2BncGUvY1GOP9BTwWEqI%2BWsrYS%2F3kPMr9wCo9U%2BXwkuarfvdcASydDp8ekBzMQlrJpJ9TXrVfmLrfz2f%2FpnLt9ZtueCHd1AUf95JvlmSuYiniH%2FraQSijDkKqzl15BsyJmGL2CG1wV%2BbkO%2B6JCLgEWGm67uqQLyKzTTOSHJX0bRWk7dhjcGCTBSa9y1eNp7B%2FXHX8vN9GIeNshx4EjYRfGAXWgDI6cmpNUUALX5xxZfR%2FVvUbyHRakQmtqkeHwbyBCWXNaeETX2zoDqYFt18b69WaJYXbGGbAmfK2G2BXuLPqLWdj9UNqRHcHp%2F%2F6ziALHFNjDJ3qk4W%2FyEw9fiXVVtrItUGc9N%2FyHrpIOLoxWrZm1wJbDR8ChzElDFWyDaOsrRPxYjni8a%2FccMJSrp%2BztTvvAzn0qyi650dqjN7ASWpwa%2FDMMzh%2B7wGOqUBcl67jxZjyE5zZRPGI9uJX3y4BcDt3xAcuBramg3m%2F6SIqK3ssPBMs5UnTvtyRg%2Fz4nxaylZFJXLMONJ6IdImdg6PfUt%2BZe%2F1%2FCF5Ahn3XQa041d2J0YK5KG72%2FvuKNfR5MgOljHbpcCKGgMhlA9OOjxJHDH5Jv90A0bBdqwtoZ4Osjvsn%2Bn3meaACxHpKrIxbqnY8n0lB6EKei2KC0nUbliHD9qn&X-Amz-Signature=e78fc50806730dfe1bda30d2cd5a753ed8aba062349c0bcd912a6a6405358fbd&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Data Visualization Libraries
#### 1. **Matplotlib**
- **Description:** The most well-known library for data visualization.
- **Features:** Great for making highly customizable graphs and plots.
#### 2. **Seaborn**
- **Description:** A high-level visualization library based on Matplotlib.
- **Features:** Easy to generate various plots like heat maps, time series, and violin plots.

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/733d1e42-5a53-4fd8-90c1-3d85254369a6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Q5F7OCII%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T061854Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIAwzxA%2FntIdIMHaHZSN0qlU99b1jKrB0A61qsUEKx43uAiAvUPbxGMfCR3TtKytr5DicMwFkLkloTx8Its06c6pSLiqIBAjl%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM1RdwqBU5qrs7OhNjKtwDVftNphYC2moNe9q0fpl%2BXxk5qn20CiqyFVd%2BZQ2gF0MeZ4N4Vz2D7vWRfu7Fte8eYVZA%2FUMYQVldC72SkiE5PlB7gqpue7x9XJX%2BKqJ3YXWPfASPaycUb227TcbrBa22NxWjKMwmHh4Li7O38Lf%2B7202cTUqc6uwTwJujxG0%2F7hv3D%2BoVpFMPSTFMKJLecVyGbmyYEg6d%2BOr7hVE%2BKL%2Fl7094vuwKLdbeuIJ8b7O2YsvCXekH3SWI7s3X2GudFTyYfK4AaM%2F%2FQYcklytOhL7xc0tGQ4yJr9TOLAUoGQ4WSt71KIKZs5GncDaiJqyzkb6GE9Jeof2h8kBPHenR%2F38R8IGk4oA7bvpHwcAxl0vmibi%2Bbvt6gIs%2F9Rie9ZRN52E0bYRv4ql%2FFSVTvN8ggQKyTyd2r0x5t9OhWgcF2Ce1%2F3ZTAvo1US2m%2BcvvYmrau7Pl9oXRLSmYuV0C9atJHM6AXyPbJ%2B%2BjP%2FGz7kUggFNsk%2B32ktoCWPgMgLpCNTLOmbXqL%2B7HuiJFUQjBB6nPMOv8DQz%2BLyPqgASv%2BJrLvbo0qQQQVplVzhrMcePpLl1ozDfa7Ns5%2FniuaFqri%2BzuLHXgoWOJDMefmiI00Kl824hJm5SDlGEiecDZn3nGkAwt%2BH7vAY6pgGXa9p1aSpRRqqTeNqMUAclqAZlbiuz4EPCsrIlfLwi6vvz5sWKaswAP3iI3vcxhI%2B67wa3GD6mqTrMDBD9%2Bpw94y6EVccfy%2BfZ5tthUvd60D5R5FTaEGiQO4pqGmtGJjZdpP7Wo%2FvwZ0zxRjIx4i7FzpmBuceUhHoo%2F9mDjOhytOkSo%2BLq9NZoVHxGp%2BgLUTFO15LRVKaywkEz%2BgCsPIlqAlODmwc5&X-Amz-Signature=fec7868eee530a4cb50f3b02a7c919f38c7413b36ef10851ea8507cc3f382ee8&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Algorithmic Libraries
#### 1. **Scikit-learn**
- **Description:** Contains tools for statistical modeling, including regression, classification, clustering, etc.
- **Built on:** NumPy, SciPy, and Matplotlib.
#### 2. **Statsmodels**
- **Description:** A module for exploring data, estimating statistical models, and performing statistical tests.

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c62885f5-417d-4179-834f-d68f8f2bdf39/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Q5F7OCII%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T061854Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIAwzxA%2FntIdIMHaHZSN0qlU99b1jKrB0A61qsUEKx43uAiAvUPbxGMfCR3TtKytr5DicMwFkLkloTx8Its06c6pSLiqIBAjl%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM1RdwqBU5qrs7OhNjKtwDVftNphYC2moNe9q0fpl%2BXxk5qn20CiqyFVd%2BZQ2gF0MeZ4N4Vz2D7vWRfu7Fte8eYVZA%2FUMYQVldC72SkiE5PlB7gqpue7x9XJX%2BKqJ3YXWPfASPaycUb227TcbrBa22NxWjKMwmHh4Li7O38Lf%2B7202cTUqc6uwTwJujxG0%2F7hv3D%2BoVpFMPSTFMKJLecVyGbmyYEg6d%2BOr7hVE%2BKL%2Fl7094vuwKLdbeuIJ8b7O2YsvCXekH3SWI7s3X2GudFTyYfK4AaM%2F%2FQYcklytOhL7xc0tGQ4yJr9TOLAUoGQ4WSt71KIKZs5GncDaiJqyzkb6GE9Jeof2h8kBPHenR%2F38R8IGk4oA7bvpHwcAxl0vmibi%2Bbvt6gIs%2F9Rie9ZRN52E0bYRv4ql%2FFSVTvN8ggQKyTyd2r0x5t9OhWgcF2Ce1%2F3ZTAvo1US2m%2BcvvYmrau7Pl9oXRLSmYuV0C9atJHM6AXyPbJ%2B%2BjP%2FGz7kUggFNsk%2B32ktoCWPgMgLpCNTLOmbXqL%2B7HuiJFUQjBB6nPMOv8DQz%2BLyPqgASv%2BJrLvbo0qQQQVplVzhrMcePpLl1ozDfa7Ns5%2FniuaFqri%2BzuLHXgoWOJDMefmiI00Kl824hJm5SDlGEiecDZn3nGkAwt%2BH7vAY6pgGXa9p1aSpRRqqTeNqMUAclqAZlbiuz4EPCsrIlfLwi6vvz5sWKaswAP3iI3vcxhI%2B67wa3GD6mqTrMDBD9%2Bpw94y6EVccfy%2BfZ5tthUvd60D5R5FTaEGiQO4pqGmtGJjZdpP7Wo%2FvwZ0zxRjIx4i7FzpmBuceUhHoo%2F9mDjOhytOkSo%2BLq9NZoVHxGp%2BgLUTFO15LRVKaywkEz%2BgCsPIlqAlODmwc5&X-Amz-Signature=2010c6a741411bd759d9f33d1e3c49d3945995cbc1e77556e3063207fabfda0b&X-Amz-SignedHeaders=host&x-id=GetObject)
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
