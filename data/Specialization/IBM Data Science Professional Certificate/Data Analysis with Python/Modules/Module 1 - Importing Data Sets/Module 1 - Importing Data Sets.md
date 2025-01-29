

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

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/997ac361-58a8-4f04-bb0f-79fea4baa761/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662QPD6HU7%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T091516Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEID%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICFa6pFQmkmXyNTMkV9ugnBMZURqShI3G0XLDqa893RtAiAhHPeLIWWelCNcEVjus1%2BlBZyRCWyy1gI06zcmcszRkyqIBAiJ%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMiiDL6uwaV8%2F0fJudKtwDFyHbHRhUnRnruMawAhiZstukw%2F7H4uuq0sbZVABPXL1HBRbQT9kS6IS3SO9MHb%2FWod%2BZKkiWg57dTBRu30LnLec%2BzcwGhD%2Bj%2BeXDdI4XNog4famHrcyCsqA9oNMw1cxxvukY6lrRLCoBk0h65TKAYDdv%2BXnkUfLJcWerBAmp4Jeutmzx6wRi2Pv%2Fyw7M2v9Jf6%2B%2BiZUq61%2FXLNOryL1CzpEfFnARQehFxXl5Z91aFsbHi6piXm3yHYN1eg1z%2FT4GbMsAqsj3ehkRNsGZ9AxqD5F1Euo2YgfBsHjVWeKIRaF5c8ARIhpSb2kaI1pnFAHBGBexo39caqfY%2BeAAXZaT3dFLli2sL%2FWogoxgZoyjltQR2XZH19GU61BQoIhrcsi9LtrwhTcPcFXizMRO%2Fav63igy0aBIRUBmfoWrg%2BdEWIVEZJ1CP6Vz%2BZpMXul%2BzTMxdx%2BuSbhf6D0ZMVWf1XB%2B%2FgYKICAHreVslg5R4fI7wD3LuMhszYux%2BrTAqLjKwSr0%2B8PjAWFFobgkd%2Fyrla91w0HBmKJWb2da%2BRew3AXyJQ3rA5vp0IOfGbDAed6DB4ca0SbZDn0SuXHUN16rl6%2FwSBcxPu75sv0LylIENq2RanUXqeOU9tMAiGFFYYYwucfnvAY6pgF0QxgqxPOTQurI47T%2FTwoYhmvynjvxArU6MEHAT4AD5Z0HSl%2BKEM0M6w2NSkCF8YXEd%2FdTn9TpnWAEg3mF3fgycL841gayhshLUdQMvGCKZoMnGXVP4s%2FDYg0vLeawj5lX99tI%2BFHP69T4d3Fx6zFGbrcWtVhM1TshZRBosBZ7pcD00PAxf%2FxcIgacW5wA8dm2vZH3DXk0Gxth1tHpP%2F1kvqldYBEU&X-Amz-Signature=c98b974f449bb0ac169aa653c32c10986efb7bcf93ad55f02dd7af592f3d73f5&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Data Visualization Libraries
#### 1. **Matplotlib**
- **Description:** The most well-known library for data visualization.
- **Features:** Great for making highly customizable graphs and plots.
#### 2. **Seaborn**
- **Description:** A high-level visualization library based on Matplotlib.
- **Features:** Easy to generate various plots like heat maps, time series, and violin plots.

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/733d1e42-5a53-4fd8-90c1-3d85254369a6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663C2H5CE3%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T091514Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDIOWWCDC9Zhgb%2BPVNayR4MI2XMwtyRZkg4TofhzdMUNwIgAzQRrdptfpZEHwOd%2FTdNO0q6i6vifDYBz%2FnDNNV6L%2BEqiAQIif%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKknLBrvPce98EXuiSrcAwZ%2BH39xJNurs5HDlboKb2wRw%2B1NL2U05R3yFjNlnQZuMGkMuPcJc8IjIfvzWat3ToSoZ4LlV6H5k7eKsugonDCbJJsz77rNZ35sIbeN5BFVpHkWHg4z1g%2BaQLJjZcDvfeQ%2FaljE7yhKHv9Pg0nEiuVBc31jATsg8lY5mIgy9JH5jJ8qDAsyb%2Fp3UgWoB1HTS7quVtTe7OvXpXuq4AdNrKUekf1vAf2ONYzcvwNhIuuO%2FboHs0l3pIRycvnwvjhQObhsZntYsMeF99Oy%2FpBZd69J4pkOJfRrKZQqFyhGziR9DOOr0L0ThbajZZqXt1VS5yW3zcQk%2BsaxL64iLlTUIvLc3%2BvV%2BXorl5iijXFxx%2F9dJtY0vE%2BkJqPZTfADaWitfO%2BFs6tJpx7nS%2FodFACBl9Ff%2FTLDs8G26BxUuyzXZHvypDBdrgwTLruP240HCpzvntekB9DXSZONohF8ppTX1ABa2XOK9ei9nVNgRf805A83cVWqcSe1lnqInbEd4nVcDTxdMbp1UYLmOdHg6DCA04HGkVd7%2FSV0Fe5QiJQVnuPxdRPMen3JUkyLmANwZTrZYfEzuyDKgeE%2B%2BZDxvpiDzMvpnaRkawiyR14CgOD%2FOKerruDpL%2FkdchGqmBC6MMHI57wGOqUB4AOBnVMFIpnfFYMfuTe792Z7myBFBS%2FSneCLiJ00w4XDrtHv5uHrIyucg0vGGk2MxaosO6v8RISzUx%2BMHXiaDRTtFRjc8E%2B99s4nHc1OkDwcKGooJF%2F1O4OwsQ6W%2FWo1ms9Ub%2Fa69zPwjlNpCBX8ilLwKXHVbM30Clha4fcA45P2WDI5ZcxVI%2FzUlEhari5FukVEwrd1ZGsqYcwDSvwKuE8fwjVt&X-Amz-Signature=d01e39dec45d898527d5728daaea0989275794f2e6f05c98428a645d3ae844ee&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Algorithmic Libraries
#### 1. **Scikit-learn**
- **Description:** Contains tools for statistical modeling, including regression, classification, clustering, etc.
- **Built on:** NumPy, SciPy, and Matplotlib.
#### 2. **Statsmodels**
- **Description:** A module for exploring data, estimating statistical models, and performing statistical tests.

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c62885f5-417d-4179-834f-d68f8f2bdf39/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663C2H5CE3%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T091514Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDIOWWCDC9Zhgb%2BPVNayR4MI2XMwtyRZkg4TofhzdMUNwIgAzQRrdptfpZEHwOd%2FTdNO0q6i6vifDYBz%2FnDNNV6L%2BEqiAQIif%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKknLBrvPce98EXuiSrcAwZ%2BH39xJNurs5HDlboKb2wRw%2B1NL2U05R3yFjNlnQZuMGkMuPcJc8IjIfvzWat3ToSoZ4LlV6H5k7eKsugonDCbJJsz77rNZ35sIbeN5BFVpHkWHg4z1g%2BaQLJjZcDvfeQ%2FaljE7yhKHv9Pg0nEiuVBc31jATsg8lY5mIgy9JH5jJ8qDAsyb%2Fp3UgWoB1HTS7quVtTe7OvXpXuq4AdNrKUekf1vAf2ONYzcvwNhIuuO%2FboHs0l3pIRycvnwvjhQObhsZntYsMeF99Oy%2FpBZd69J4pkOJfRrKZQqFyhGziR9DOOr0L0ThbajZZqXt1VS5yW3zcQk%2BsaxL64iLlTUIvLc3%2BvV%2BXorl5iijXFxx%2F9dJtY0vE%2BkJqPZTfADaWitfO%2BFs6tJpx7nS%2FodFACBl9Ff%2FTLDs8G26BxUuyzXZHvypDBdrgwTLruP240HCpzvntekB9DXSZONohF8ppTX1ABa2XOK9ei9nVNgRf805A83cVWqcSe1lnqInbEd4nVcDTxdMbp1UYLmOdHg6DCA04HGkVd7%2FSV0Fe5QiJQVnuPxdRPMen3JUkyLmANwZTrZYfEzuyDKgeE%2B%2BZDxvpiDzMvpnaRkawiyR14CgOD%2FOKerruDpL%2FkdchGqmBC6MMHI57wGOqUB4AOBnVMFIpnfFYMfuTe792Z7myBFBS%2FSneCLiJ00w4XDrtHv5uHrIyucg0vGGk2MxaosO6v8RISzUx%2BMHXiaDRTtFRjc8E%2B99s4nHc1OkDwcKGooJF%2F1O4OwsQ6W%2FWo1ms9Ub%2Fa69zPwjlNpCBX8ilLwKXHVbM30Clha4fcA45P2WDI5ZcxVI%2FzUlEhari5FukVEwrd1ZGsqYcwDSvwKuE8fwjVt&X-Amz-Signature=347f0d281f56677d7e264e1323ee60d8ed07689531ba4d06855ea1f82f810c32&X-Amz-SignedHeaders=host&x-id=GetObject)
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
