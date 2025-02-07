

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

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/997ac361-58a8-4f04-bb0f-79fea4baa761/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664IJRJJKA%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T171249Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGEaCXVzLXdlc3QtMiJGMEQCIAUYgLBx2MrgsD%2Br4YalmfXidXopEV2EloXtWX%2FiwP%2FKAiBHPEnPIXF%2FLBwRcrQDpD9iZPTj8eIXjOsdtJWK%2FcmB%2BCr%2FAwh6EAAaDDYzNzQyMzE4MzgwNSIMjsZE7ntn6T9R4lQ6KtwDRUmSPGgy7TQvvz7IasFAtwcvFOzuGyAZHF10alGLNv%2FRGXQD6r4trkvZiSf9C8o7vx126R7RwiEWR6caypWZAbswg7sP6rXD4ritWj7OwabV%2FhcRo8k13YCCVJ0B6m7DrxC8AHoZiiF5Z4cQUQoKAoccJeOq4N2x4LiExRh2DAHlxvGGt0%2FIa%2B85I8orqIxMd06xDApYny1hciICUxPqpD%2BFRp2yDgXdZrLyfFhBzPx3fx06QMLzGfC72dgcLvjECH%2BN%2Bl3NCWoeNSj5qaMw7Lf1BPGHIOrKQgjLzE8AGD3Op%2B7rpTIjmiqQu28VW9ZCy5gmfOXhyrC5HSp3Sj9KKuVi%2FhQa%2F43V17Nsp1tl4FqITFb%2FLEFD%2FFoOEvxL9fMBLdU6ZjY9sakjto%2BQVG5VutD1Xv2%2BomgaKIg3iNHF3SimIqnCYYSUoDw9MiUw0e7QOuPjvQa2FQipzFJD%2Bg8C1g69TS6tSd3G%2Bmho6%2B5Lq5aCCb8vty%2Ft%2BM3LbDxoZfEOkUHYHyrXlmFYxoaWiQRC%2BK2FUI%2FkIRCyf%2FzFVRv401RF8ytt%2FNWkDFy%2FqC2FM0i60jlSx4KoLsr1ROP8RMeCP7DQIX7OZ6OuMEBDXYAdkx%2BQkhNJQlZXqhejhsQwr%2FyYvQY6pgG05zhMlDP6LTxEPFiipEd32EtQp%2BlGSUM6yKQ01shG0xTXBP36A6cZpXDNqeuBP7MWL9jcUcemZbPL%2BYOXRxMQ%2FQvhGSax88WhXrOq2UVcIgupweZAwg0X9zYwDZT8SjAlGl1MJLPtsBKhfTn3Yyo2efptmSbCJqAT1%2B9JkJtfr7poms5cimEc1lI0%2B1eLigZqYwyynopq9TJtTR9aH%2BcxF2mnIsly&X-Amz-Signature=53e840e8f1e29fee0847b723abba0fd9309079e196841df732281fdcd6f17d05&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Data Visualization Libraries
#### 1. **Matplotlib**
- **Description:** The most well-known library for data visualization.
- **Features:** Great for making highly customizable graphs and plots.
#### 2. **Seaborn**
- **Description:** A high-level visualization library based on Matplotlib.
- **Features:** Easy to generate various plots like heat maps, time series, and violin plots.

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/733d1e42-5a53-4fd8-90c1-3d85254369a6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QEBJNS2F%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T171248Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGEaCXVzLXdlc3QtMiJHMEUCIAOrUkqW%2FuGBrJSJLXOoYpX5wCSwMhktBe6uL1BlpS1sAiEAhSab31%2BmjwJwb%2F%2FyKxTPvietpi6iTPVallTQCEpKa4Iq%2FwMIehAAGgw2Mzc0MjMxODM4MDUiDEKkRfHQbruLNmGCQircA9VKGF%2ByihXEcw32HsXSpSU8tVsTiPLxbUpk36e0sDCalmLlnyb191%2B%2Bz71bKK1Z4OY2b4FGUfBk88aEVVOi7XfeqpHitSKQEJ6tZ2SGQQcHzPay9aWSgF6YkTRfgQ07wWbE48OzSQvG76bK3BUJFgRPqmIhCa9KwDyW7dTdwzvnB%2BlDXh1Ut%2BOlrITtTe7ymMkLIBkEURjA5bnWEyxAA1QBZ9okSvbMmeRHOF%2BxfZnlMu6tAE4UR7Vv7MeaV5bd2BpyWff02TvRaoaK8mJfFDMapKCVCc%2FlISYF5fERA35XL%2BTxKGlXPN7WkVWzEfR8hPD7asMhY6dGy0FC3xorN7vKt5BeNx7SR5HgYgQggDl9XfcTdcrwz7OyWdgYfQjt0%2Ffa2xBwMHXg7Je3%2Bzl8JJpI6yU%2FxfBUfyzf0OiPaNb5PJ6VWfqJWyxG3ls9boEuCrrT2cI2I12HwlEyJZavQ7Md7eN4EcBl7srHqYB2RlOa5HlokQW5OhX0WvX1nzzlyJ4rJmBS%2BkclBKIpc9tY8c1jTar2E%2BZdC%2FS0zUwSUewBG2i5qPMAONZ7nIfvSrkpjQ2nSXLlKp2B2eRYiaRBe141olZLcgdEWqSURjOoV3jSvVL0%2BmAbZsY4unCbMKT8mL0GOqUBYxrsSTw28eYBT0ClrVIUfC8ugeLEDZKrAB7jgy5UMfCwbv%2BtOcQTlNSlGq96YrC1KYCqX%2BeA8NADYczLwMi7TFDzrZVK9E6TWae6NXfkaLrFeuty2cjkLfc8BevmQEAKY6eCfx%2FvBN4ECiJJkB1EPy%2Bq2sG0X0%2F%2BkM0IYh0sCcApTwmmYIAoes29BORWUSnQFqoxya%2FT5yDXNsITmLxuEsOVfzWh&X-Amz-Signature=c86a020261c080a44781e7973df77b7f821b289188de6f13058a090001b00e79&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Algorithmic Libraries
#### 1. **Scikit-learn**
- **Description:** Contains tools for statistical modeling, including regression, classification, clustering, etc.
- **Built on:** NumPy, SciPy, and Matplotlib.
#### 2. **Statsmodels**
- **Description:** A module for exploring data, estimating statistical models, and performing statistical tests.

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c62885f5-417d-4179-834f-d68f8f2bdf39/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QEBJNS2F%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T171248Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGEaCXVzLXdlc3QtMiJHMEUCIAOrUkqW%2FuGBrJSJLXOoYpX5wCSwMhktBe6uL1BlpS1sAiEAhSab31%2BmjwJwb%2F%2FyKxTPvietpi6iTPVallTQCEpKa4Iq%2FwMIehAAGgw2Mzc0MjMxODM4MDUiDEKkRfHQbruLNmGCQircA9VKGF%2ByihXEcw32HsXSpSU8tVsTiPLxbUpk36e0sDCalmLlnyb191%2B%2Bz71bKK1Z4OY2b4FGUfBk88aEVVOi7XfeqpHitSKQEJ6tZ2SGQQcHzPay9aWSgF6YkTRfgQ07wWbE48OzSQvG76bK3BUJFgRPqmIhCa9KwDyW7dTdwzvnB%2BlDXh1Ut%2BOlrITtTe7ymMkLIBkEURjA5bnWEyxAA1QBZ9okSvbMmeRHOF%2BxfZnlMu6tAE4UR7Vv7MeaV5bd2BpyWff02TvRaoaK8mJfFDMapKCVCc%2FlISYF5fERA35XL%2BTxKGlXPN7WkVWzEfR8hPD7asMhY6dGy0FC3xorN7vKt5BeNx7SR5HgYgQggDl9XfcTdcrwz7OyWdgYfQjt0%2Ffa2xBwMHXg7Je3%2Bzl8JJpI6yU%2FxfBUfyzf0OiPaNb5PJ6VWfqJWyxG3ls9boEuCrrT2cI2I12HwlEyJZavQ7Md7eN4EcBl7srHqYB2RlOa5HlokQW5OhX0WvX1nzzlyJ4rJmBS%2BkclBKIpc9tY8c1jTar2E%2BZdC%2FS0zUwSUewBG2i5qPMAONZ7nIfvSrkpjQ2nSXLlKp2B2eRYiaRBe141olZLcgdEWqSURjOoV3jSvVL0%2BmAbZsY4unCbMKT8mL0GOqUBYxrsSTw28eYBT0ClrVIUfC8ugeLEDZKrAB7jgy5UMfCwbv%2BtOcQTlNSlGq96YrC1KYCqX%2BeA8NADYczLwMi7TFDzrZVK9E6TWae6NXfkaLrFeuty2cjkLfc8BevmQEAKY6eCfx%2FvBN4ECiJJkB1EPy%2Bq2sG0X0%2F%2BkM0IYh0sCcApTwmmYIAoes29BORWUSnQFqoxya%2FT5yDXNsITmLxuEsOVfzWh&X-Amz-Signature=0e89dba6e51647688284169e91e974561d44edd3e2123852ce51cdfd5f043a92&X-Amz-SignedHeaders=host&x-id=GetObject)
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
