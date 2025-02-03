

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

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/997ac361-58a8-4f04-bb0f-79fea4baa761/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46633NTQ6DY%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T031920Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCUIgQrmxpyx4D9S0BtzWTS2lxKo49hRHIqdcH76Q4uygIhAJSkvG9H4SkzOyATMRJhD8m5rKq%2FLV5aprfP%2FgGlQS2JKogECPv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxjQXptkBbwtluvtfgq3AO28slNnoizkzyeRuUlhgNahOkGM8fq9bF6rYZMBcxhNYTDANYzOLMfCLzVDUL6%2F9ijlKdt3UFxQ3HmolCaWKFfY1ydMX5TZdQEo4GYb5z%2FR8eT%2Bc%2F%2FFt3Sw5IlNRY5rZdyiPgeKww1jvXLkYdeOVT1JXBohYWZ5qqGJFcEMBj85IFkfW4RTjTvp3bxwUch1ChW5iJdRZi2FfTER37PEwpOcSthsP4VU4zGWGNZqvv2QkBJNmjSR1LgPGxba8oY29cEaOKT3ZD3s3%2BDVB4qWvdzA0QZEdzH1aExWgdKZ1NTm4KrS1qz7u4SBEqj2UAArrX21bNuASusB41oOyKNnCGhx6YRJYDj1CplnoIPNpxRBFf4mZUbSAllYA2tAoo9qqzOk48aB3KJ6ib%2BrrCEoTsaerEB0PYGQ%2BQS6PckUFiCuetsz8lLKujJKgLKez%2BqZqj%2F98uDcbf%2Blj%2FD0s5xkBC0rxU0fiPu4b9ry8CjRauzjjcUwb6NPswZfe8LHjk8voNaxypVAdB2ophgzffN42Te2iOM1c7L%2BQxtoI2m5idRxkUIqN27qxhouzLeMN%2F0QZbqPCbVLU3VOuxHl42Gxv6zWtMX%2B8eopLPZ0YXXiZxg0ihx0z4smDekkp%2FV5TDMv4C9BjqkASe39E%2BgOsU6P3fAcaBH5WAHhD54%2BOZTmqO1zhfhx8g2vM1wa6GZlDCDTUpLFv4P8whfno7pI5qRPaUHfYi6IGv1C9HKgskylAquqrMf6qGZ3ovgBnlDc6v%2FVT8hmQg%2F%2Ft08B1wf34K4W%2Bk1XEtfwLD87wXH6soUJ2fHr2qlaKSysNYFazmFjpYI2g4pQbHqMh2KJk7NeyIMRZT4md2EgrjzGtlw&X-Amz-Signature=e8809300337d677f8bab2b8e3c1dba8c52a2f327edc0946d32188c4230eb2ed7&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Data Visualization Libraries
#### 1. **Matplotlib**
- **Description:** The most well-known library for data visualization.
- **Features:** Great for making highly customizable graphs and plots.
#### 2. **Seaborn**
- **Description:** A high-level visualization library based on Matplotlib.
- **Features:** Easy to generate various plots like heat maps, time series, and violin plots.

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/733d1e42-5a53-4fd8-90c1-3d85254369a6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665TEU7E5Q%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T031918Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCD48Wv68dgnk12sWjYScf0cnGg7b2SzJ8usZ6z%2BOTmMAIhAOyOcFsu9WB5o1CQUcMDjERe4PmE3MhH2fkO8VJhEeBNKogECPv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igx0kkIWCa9ZBOzc6VAq3AOgRUWzj0t6mNIWn%2BzkeBajLyZ%2FlbSH7OhPlrf6TsPOxYW195cWuPlsuhpMSPvg%2BM91RWJLCUykGru6Gp7PjaUluZloDuSeQoeVHwdSipI9MzfWpIpa6fjjV%2FZhssSqTmPQYmaUd1QjJjRUahymB2kIHUzg0R9Gj5jAJSuRXW3UsfdYFWk5zXaI10RcQMZllt%2B8zSAheHfL%2B7HhnVpdI9pcEiatYuuGby%2BHwXTOJe6mbOmGnBTeg8FbhwdXeupIxS6lhzvsh1%2Bvfw0o4QEHF43jW2oTXySVXWoAKMx11zJE8wvDdaRqjvXHSp%2FN8RG0JTxPOBQETVNzoCDcb8kQO0R1%2BzZ9lLKPKlGJVJD6QwcbvQ0aqZWi%2FobbVJ%2BisVCqFGIQbIOIgp0LmKHmFWozmBP00%2FPCk2zYfkkFODewioCemc5bDbt6qKgfao7IaABkrSBHh0oQZMHrgT%2Fa6JRD3jSPg6xGyMr%2BMdjIPwHh6FhMOfHE3JcUUZMZkrYaAyT4qwQPXh5T9cuO72veIw4XzVgZvWf2Ot5HlHoiCKVlCZhEhvLDwCJ%2B2llEwYtPBLl4H5Btl6h%2BKMiUzF9ySZSIr2eOQC2TgX9xhi%2FfYxsiR2E4PnmISLnH6gpzjD2pyTCRv4C9BjqkARZO94WCfkREnDpXYTXUoeEwgHeK2HgcppFd2u1V8CdCrt2aAUDirnSimgTx1P3%2BKOMepGVkQQbJqGYd5UGGy1PlCg%2BTP7ArKWbMU%2Bd29tDCbNueP1ePCa3Dp5p0PRqPF9N4LClmbjdB%2FoYzCRNW%2B4MfYEWGvoB5cSxukOeZxpXm0PccZ3gSHHpiB8QzTmOLSzQwHE2gwReCMmmM5sX3pgiqydPd&X-Amz-Signature=77b8ed26535d95ace1705e10cbcf77e6849518d4951392481e7046325b17dbed&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Algorithmic Libraries
#### 1. **Scikit-learn**
- **Description:** Contains tools for statistical modeling, including regression, classification, clustering, etc.
- **Built on:** NumPy, SciPy, and Matplotlib.
#### 2. **Statsmodels**
- **Description:** A module for exploring data, estimating statistical models, and performing statistical tests.

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c62885f5-417d-4179-834f-d68f8f2bdf39/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665TEU7E5Q%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T031918Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCD48Wv68dgnk12sWjYScf0cnGg7b2SzJ8usZ6z%2BOTmMAIhAOyOcFsu9WB5o1CQUcMDjERe4PmE3MhH2fkO8VJhEeBNKogECPv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igx0kkIWCa9ZBOzc6VAq3AOgRUWzj0t6mNIWn%2BzkeBajLyZ%2FlbSH7OhPlrf6TsPOxYW195cWuPlsuhpMSPvg%2BM91RWJLCUykGru6Gp7PjaUluZloDuSeQoeVHwdSipI9MzfWpIpa6fjjV%2FZhssSqTmPQYmaUd1QjJjRUahymB2kIHUzg0R9Gj5jAJSuRXW3UsfdYFWk5zXaI10RcQMZllt%2B8zSAheHfL%2B7HhnVpdI9pcEiatYuuGby%2BHwXTOJe6mbOmGnBTeg8FbhwdXeupIxS6lhzvsh1%2Bvfw0o4QEHF43jW2oTXySVXWoAKMx11zJE8wvDdaRqjvXHSp%2FN8RG0JTxPOBQETVNzoCDcb8kQO0R1%2BzZ9lLKPKlGJVJD6QwcbvQ0aqZWi%2FobbVJ%2BisVCqFGIQbIOIgp0LmKHmFWozmBP00%2FPCk2zYfkkFODewioCemc5bDbt6qKgfao7IaABkrSBHh0oQZMHrgT%2Fa6JRD3jSPg6xGyMr%2BMdjIPwHh6FhMOfHE3JcUUZMZkrYaAyT4qwQPXh5T9cuO72veIw4XzVgZvWf2Ot5HlHoiCKVlCZhEhvLDwCJ%2B2llEwYtPBLl4H5Btl6h%2BKMiUzF9ySZSIr2eOQC2TgX9xhi%2FfYxsiR2E4PnmISLnH6gpzjD2pyTCRv4C9BjqkARZO94WCfkREnDpXYTXUoeEwgHeK2HgcppFd2u1V8CdCrt2aAUDirnSimgTx1P3%2BKOMepGVkQQbJqGYd5UGGy1PlCg%2BTP7ArKWbMU%2Bd29tDCbNueP1ePCa3Dp5p0PRqPF9N4LClmbjdB%2FoYzCRNW%2B4MfYEWGvoB5cSxukOeZxpXm0PccZ3gSHHpiB8QzTmOLSzQwHE2gwReCMmmM5sX3pgiqydPd&X-Amz-Signature=95163f6f36354468954e1cc8935d031b1d7d7d1f157c746f01ae3a8eff67a53b&X-Amz-SignedHeaders=host&x-id=GetObject)
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
