

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

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/997ac361-58a8-4f04-bb0f-79fea4baa761/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UUFCPGYG%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T191127Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBsaCXVzLXdlc3QtMiJHMEUCIBNba4tmxceeGrLDk6J3TWqvlB%2BnJHF0uUyofjWcU5pgAiEAwLHz7R7UaLG4qHg1RENLNyfcMWVdI1MUNbinpjvp%2BeQq%2FwMINBAAGgw2Mzc0MjMxODM4MDUiDJrWtKlF73ddtyEUeCrcA2C6d9fDL5C71XqshHfbYeAdgYd23XB%2BN8Eu7Nln9kQNcTOfgkSVhHwhSHQYu79WmbcNf%2BqejAVhETAXE9NUYl7QuzCYhlZSBfkZOqLYSsVGDHLrTZapDSNADnuYMrrm1JnYvTAbEZU7CCY7boVYXqWHSlCZMQZsZrUC%2BaLkBxwChuCs64hIf2%2FOtYbuQ10ckjgGaPtolUXh5A4SzrTtLC48qt%2B900RmlcPfy9FsAe93aFmCunq0I92BTHC611Vz7VuUyD0XyE5%2Bfyduxtk1GnxurPhCyWHBf5j0FBjqHk%2FVcrY0iCpylrHIbzXuhO%2F%2F65ct1AHLwtDgU1o25q0md48JOmHtfvx1h9xfoHoVjnldpoYZOpQvrUpN4CVFWBDADdcjLJVJYYlNPw1lQHX8iq7HstoijOgK8zpxBaoCSbgQseydvz0RsdpxIWm4e0OyMxC2JTl2pYaCc4OXXYmqzB6429l5n4T4bqZyAbxq%2BIGsX0SgcgYPIvSMDHTdT3NqjTPq%2FOLVibTWFu2G6iLwmSkk50Ra3Wahpg5rJrU0wUNkdrsTfnc8ioLE%2FdGOzflnDIOifBkPQldhZv7sJ5FxvgASJ7pSNaw8uDhvtBmoRr8L9AqHJZtdgaPRcUr2MP28ib0GOqUBRy5CoN1K5gWfAdCE7zcj0xdHBnIUJdqzkXL22KeO1%2BvwGjfcBqTmclJjuywTlH31KqEktwBtYfY4pi2eO2%2BzTDvnR5zqa%2BG6Uqa%2BoL0Kz1BD5VuUBcXLpdCW2bUmx3s82Hq1G56RpAHDJ3BGus8%2B0xB%2Fgdqg0IYkzyWORvzM0HHAjMcQF6Wf4GXcuFPmAgBYAE8b8dnWtD1kSwsA4UsihUbn7SmF&X-Amz-Signature=ed5afa40c823152cd6d4c0f8a00c7f2e142352b41255ec46f448e596193975e8&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Data Visualization Libraries
#### 1. **Matplotlib**
- **Description:** The most well-known library for data visualization.
- **Features:** Great for making highly customizable graphs and plots.
#### 2. **Seaborn**
- **Description:** A high-level visualization library based on Matplotlib.
- **Features:** Easy to generate various plots like heat maps, time series, and violin plots.

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/733d1e42-5a53-4fd8-90c1-3d85254369a6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TAPUL3UB%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T191126Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBsaCXVzLXdlc3QtMiJHMEUCIQDYdM0k%2FMbQRqQTxDE5uNj4wNCxmTAPYuxpKOcTEhedaAIgMnGE2on2U0wP3FQB072wg%2FQ8KjjZCiH1p6qqKdp%2BwXoq%2FwMINBAAGgw2Mzc0MjMxODM4MDUiDLa7uKCCym0wmnSRZSrcAwL9WPKpopn0CR8re1kLbQ4uLS8WnXzEVB6nJq99yvY6u5PMXsVymGgSNcEQDyxp3tQgcTV2jmVl9nkhd2TxbHFJuT0Y1V%2BJxtNsabg0L5Cwuc23bB2UiuDJLGbwqUkz0T33GjOdDh8jSr3xx7mLWhpH4eZVUkC7hbKSjEmx6JDmdOvARpE10ihXpxoowZ5B6H1PHst3aKiwDpa%2FEoJYry%2FU3oUb7RirFdJSb43xLBQdhIKLHmK6dPvoQStLjiO4ieKtWi2Aqp7Av8qqWOaUKU34k0Gzooj2YBs9fM9RUDcFoB9THowc%2BY1Ig1M5Nv9C7KdvpDs3MCa8%2BuBRwDsrQhk3N9WbOZQvuNr%2Fro50CiomSx0rYrPtYM16%2F49XxHWrLvtR2jW%2FBkAzR6ki3Vwl%2BF9uNaFPWaj1PBzzBo5NccKcM1%2Fc0j0ZSQvaNXVl67SRCJNugZ95%2BaKD2nUX1Pg%2FiiJyvGVtJT9F4%2F2xH452snGIilnMjaOUiemhdAYoD0ZBmphINyxM6UL8Rzg%2BQ4zho7Bc4rfg6iKT1MZH75n5ClkCV1iNsjdP18nUZqN88vgcLpL0stI9Ft6iI4s0jSeDXfsP%2FipizDwECwb7Zgec%2FO2MWu3CGB7AL4gVnfAQMJm9ib0GOqUBUpgNHvyrALMixQkzafpHOOdm9aBkI%2BKn4rKlO%2B2X1argciEBRH%2FXYBv7hcetRm2rYFRc7g5QRTbiau%2BbGzj2CB9PRLVH8ZftqX50UNz06uBsyClVDAq1EAJ9BdqlPl0x%2FhKgR2p2lAu%2BRcghsmyck7FVJOY3W7RyN%2FE1a3II2JxVveeLapKFbPnwGKHSF5BAvx4gg9WW9lzOXkY8ICBKF7eYPXSd&X-Amz-Signature=28d91a4211c63922b4bd584aa77641e0d328a48d6a2f591b253776a2e7fa370b&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Algorithmic Libraries
#### 1. **Scikit-learn**
- **Description:** Contains tools for statistical modeling, including regression, classification, clustering, etc.
- **Built on:** NumPy, SciPy, and Matplotlib.
#### 2. **Statsmodels**
- **Description:** A module for exploring data, estimating statistical models, and performing statistical tests.

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c62885f5-417d-4179-834f-d68f8f2bdf39/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TAPUL3UB%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T191126Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBsaCXVzLXdlc3QtMiJHMEUCIQDYdM0k%2FMbQRqQTxDE5uNj4wNCxmTAPYuxpKOcTEhedaAIgMnGE2on2U0wP3FQB072wg%2FQ8KjjZCiH1p6qqKdp%2BwXoq%2FwMINBAAGgw2Mzc0MjMxODM4MDUiDLa7uKCCym0wmnSRZSrcAwL9WPKpopn0CR8re1kLbQ4uLS8WnXzEVB6nJq99yvY6u5PMXsVymGgSNcEQDyxp3tQgcTV2jmVl9nkhd2TxbHFJuT0Y1V%2BJxtNsabg0L5Cwuc23bB2UiuDJLGbwqUkz0T33GjOdDh8jSr3xx7mLWhpH4eZVUkC7hbKSjEmx6JDmdOvARpE10ihXpxoowZ5B6H1PHst3aKiwDpa%2FEoJYry%2FU3oUb7RirFdJSb43xLBQdhIKLHmK6dPvoQStLjiO4ieKtWi2Aqp7Av8qqWOaUKU34k0Gzooj2YBs9fM9RUDcFoB9THowc%2BY1Ig1M5Nv9C7KdvpDs3MCa8%2BuBRwDsrQhk3N9WbOZQvuNr%2Fro50CiomSx0rYrPtYM16%2F49XxHWrLvtR2jW%2FBkAzR6ki3Vwl%2BF9uNaFPWaj1PBzzBo5NccKcM1%2Fc0j0ZSQvaNXVl67SRCJNugZ95%2BaKD2nUX1Pg%2FiiJyvGVtJT9F4%2F2xH452snGIilnMjaOUiemhdAYoD0ZBmphINyxM6UL8Rzg%2BQ4zho7Bc4rfg6iKT1MZH75n5ClkCV1iNsjdP18nUZqN88vgcLpL0stI9Ft6iI4s0jSeDXfsP%2FipizDwECwb7Zgec%2FO2MWu3CGB7AL4gVnfAQMJm9ib0GOqUBUpgNHvyrALMixQkzafpHOOdm9aBkI%2BKn4rKlO%2B2X1argciEBRH%2FXYBv7hcetRm2rYFRc7g5QRTbiau%2BbGzj2CB9PRLVH8ZftqX50UNz06uBsyClVDAq1EAJ9BdqlPl0x%2FhKgR2p2lAu%2BRcghsmyck7FVJOY3W7RyN%2FE1a3II2JxVveeLapKFbPnwGKHSF5BAvx4gg9WW9lzOXkY8ICBKF7eYPXSd&X-Amz-Signature=47f2977b5c840ddf40d5ea29c4fcfdce4dc3fcf5f4149d9f92f915f2e09fb757&X-Amz-SignedHeaders=host&x-id=GetObject)
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
