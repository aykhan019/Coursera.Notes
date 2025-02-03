

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

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/997ac361-58a8-4f04-bb0f-79fea4baa761/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QH2RTOHM%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T201555Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAQaCXVzLXdlc3QtMiJHMEUCIQDtx9FtLxw3u5uoOVEzyxpV%2FXV5HQWw4RTUg3SbSdwZiwIgSJ18td0bHbBq3veLBtdp8qwTH1Qy0KzIz3tgosXU95gq%2FwMIHRAAGgw2Mzc0MjMxODM4MDUiDHp3F2CGXUMgjcWnsircA1lvuU4DuS7fA8YuhwzP3sxjcxFQQI0sil2qn37jm7JyNeE6r0XC0Qyr%2FCxdycIxP9Xnulkwa8Kovak%2BnjnyRy6A4XrhPg5R5w8WyIBZfcabEw0alHJ%2BwjfKWCg2NgWvD9pwCEVmtLwTC9io1pK0Zqx9qkz948qjtwpnoOI2J0Q3bJfN5dnvkW3JbmLSauM9IB4p9viYds9gY3m6mIeQWyx4MJs%2Betc%2BXwY4VAKruPfUZ0%2FXdiwzJUq%2F5bKYCs6aXfBHzTLMoj8%2FyWFJffUMD9e7JtphZz6QlC0r6pNXfqVPrCfIYq%2F%2BTACno8zwBzmcy01TRxy1sIrVV0RUwyPPRkA65Z6ze%2BHuHcnm03vUGk14HQs%2BxcQ2nZhDaRVIVUvn%2BqxSIfKCn02pfAcxCXC%2FM0ryGLKANLvZItL8NvLYJPdw92W6jbaCllKl5PDZt6Kf%2B6OK1oRYQ7IVCSbReMgxJUwMxKuIMZuRghLdLpFrbfPm8HRbCZjv3hXR9U0wD9qCfTuft1hHq9t0DSFEh2MjIP%2BehQzcInzDLC5csbOme65ggPA0qHJRvMSQFlvByGnWpA6fitUokkWISc5Fi8yTuWJCyCKJ3Sc8NzY0%2BV0WRslLE5QelXRxMmxfA%2B1tMOq8hL0GOqUBaoKLlJVP2HmhZS3uPFlt4IuvCqcUO17O%2FDrdmm0x0XIzpje9p6rC0SUHQXUflyPDcdP8XOF1J8t%2ByStHHOdvxwAUhbcrX4DzyXtdXiuFpu9b2o9pDpcunWhB0W9tNsiwYDD3BSnHsaV5lk1H2RDNJIp1pLAJGLe7PgFN0dRH%2BjXtLIlHjOlVFg5kghof9ujjecXntqzDtQeZCnLv1iD8qAt%2FXqMx&X-Amz-Signature=f69830650dcb73a7eef817f0881c5f545d2eb7ba3d50998ce3f929c5c8464e27&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Data Visualization Libraries
#### 1. **Matplotlib**
- **Description:** The most well-known library for data visualization.
- **Features:** Great for making highly customizable graphs and plots.
#### 2. **Seaborn**
- **Description:** A high-level visualization library based on Matplotlib.
- **Features:** Easy to generate various plots like heat maps, time series, and violin plots.

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/733d1e42-5a53-4fd8-90c1-3d85254369a6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UCWM4EW7%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T201554Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAQaCXVzLXdlc3QtMiJHMEUCIQCWA5Gz7suUF6YG%2F%2BZjO7mtVWsonp%2FCbvzARnEJLQsInwIgLauxADOevsgNmZol0ulmi6QYy4%2BoNCnmsqe6aLdcHH4q%2FwMIHRAAGgw2Mzc0MjMxODM4MDUiDI7HjTkIiaN%2B1z%2B2EircA49GMDMJpPnOLVb04qUA0beV9WR10pOfVOK8XFRL3U0tAxD9g%2BeVrIjDICGot9jDhir1QjrLeuYEu8WulAvrlHUhrW4LAAJKZXJUGBqA1A8s9%2F5JKAbAYEEZ4bJ6w6HUBPLexBGYheo9%2B18eSF6dEi6b3FtWzBnvsb7igf8EA1beSMJsWmr3l%2BKKsZyWR4iYdiUbOKtbZJkRuLL1HE%2FdwjaJNyZ02GoySRIt19wEVJsPRRY4P%2BHPzypt%2BnfsN8DzTFpt4FhOaOUh2Il2cdtyroWxxwak2TGYSZPQWNUn38tLxYi2ZunYrEJNuAbZGK9IbuZ0T2qdMGa5seJHPFJPE6L0lhJcKkBoauD%2Bbzp0CPXwO5Q8Vmemm51JhrLirxPEUfcvvt5HlDX2Mo%2BhIOoppSoEM3835lmgb1y41teURB08Ed76055COnU1XyhGED2%2Fn6HASTZCjQslhv6gXmkKBl7p3KkPnBsOgYeFKv%2FRUw%2FAv9YyHUWUXlOgdEQiN64SHh5TKQ3wGao1aQCC2H08UJp7XwmMycp50MdX4mrM%2FpQ%2BKekiKh%2BMXynXv3zt5S8C%2Bdq9kiQZ9obT49%2BUQzIZ1r9hwfR9zteomOkN6Oz5mf12NsGpkVUPL141e6OZMN68hL0GOqUB%2FRnYDgooljwb%2Bu1T32ve0PdKpFgmnTRbX5WsXWJUKiDXfMpYc4GlBuFknI6y4MJO%2F5aM5gdgcdaY5x8po%2FV3pl%2BzUQbZ6jp6lWZV6P%2BxF%2B3qkJktQ1VmUm2Y2XmO3%2FGE2HM6W1EJf0Lb77tb7CoMIbQh5yzsMg76MevwCNrD79G%2BqaM7HNGvi7tnYeCB%2FuUZ5HOIzIB63w%2F0xtM84VR4cxSFAXDi&X-Amz-Signature=86e4b8236da721f79652edd6b138acc3db4dbf7f53f2808081149cf0ca33d346&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Algorithmic Libraries
#### 1. **Scikit-learn**
- **Description:** Contains tools for statistical modeling, including regression, classification, clustering, etc.
- **Built on:** NumPy, SciPy, and Matplotlib.
#### 2. **Statsmodels**
- **Description:** A module for exploring data, estimating statistical models, and performing statistical tests.

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c62885f5-417d-4179-834f-d68f8f2bdf39/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UCWM4EW7%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T201554Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAQaCXVzLXdlc3QtMiJHMEUCIQCWA5Gz7suUF6YG%2F%2BZjO7mtVWsonp%2FCbvzARnEJLQsInwIgLauxADOevsgNmZol0ulmi6QYy4%2BoNCnmsqe6aLdcHH4q%2FwMIHRAAGgw2Mzc0MjMxODM4MDUiDI7HjTkIiaN%2B1z%2B2EircA49GMDMJpPnOLVb04qUA0beV9WR10pOfVOK8XFRL3U0tAxD9g%2BeVrIjDICGot9jDhir1QjrLeuYEu8WulAvrlHUhrW4LAAJKZXJUGBqA1A8s9%2F5JKAbAYEEZ4bJ6w6HUBPLexBGYheo9%2B18eSF6dEi6b3FtWzBnvsb7igf8EA1beSMJsWmr3l%2BKKsZyWR4iYdiUbOKtbZJkRuLL1HE%2FdwjaJNyZ02GoySRIt19wEVJsPRRY4P%2BHPzypt%2BnfsN8DzTFpt4FhOaOUh2Il2cdtyroWxxwak2TGYSZPQWNUn38tLxYi2ZunYrEJNuAbZGK9IbuZ0T2qdMGa5seJHPFJPE6L0lhJcKkBoauD%2Bbzp0CPXwO5Q8Vmemm51JhrLirxPEUfcvvt5HlDX2Mo%2BhIOoppSoEM3835lmgb1y41teURB08Ed76055COnU1XyhGED2%2Fn6HASTZCjQslhv6gXmkKBl7p3KkPnBsOgYeFKv%2FRUw%2FAv9YyHUWUXlOgdEQiN64SHh5TKQ3wGao1aQCC2H08UJp7XwmMycp50MdX4mrM%2FpQ%2BKekiKh%2BMXynXv3zt5S8C%2Bdq9kiQZ9obT49%2BUQzIZ1r9hwfR9zteomOkN6Oz5mf12NsGpkVUPL141e6OZMN68hL0GOqUB%2FRnYDgooljwb%2Bu1T32ve0PdKpFgmnTRbX5WsXWJUKiDXfMpYc4GlBuFknI6y4MJO%2F5aM5gdgcdaY5x8po%2FV3pl%2BzUQbZ6jp6lWZV6P%2BxF%2B3qkJktQ1VmUm2Y2XmO3%2FGE2HM6W1EJf0Lb77tb7CoMIbQh5yzsMg76MevwCNrD79G%2BqaM7HNGvi7tnYeCB%2FuUZ5HOIzIB63w%2F0xtM84VR4cxSFAXDi&X-Amz-Signature=c4c5492c53da3a9833d9673ddce360288c84e8f8e06fd087e6c9d9cc401fe1c3&X-Amz-SignedHeaders=host&x-id=GetObject)
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
