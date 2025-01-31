

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

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/997ac361-58a8-4f04-bb0f-79fea4baa761/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VPFYVM76%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T131907Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDR4zyGGDI1ohn5RMg%2B54uqZeuOBmzQtHZLeJ3cmSqfJgIgVMw%2F9n7u0OkXlZmEfssqO4iOag6lQ%2Bckikw%2F%2FPO2AoAqiAQIvv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGCGH710ok9%2Bv2IwvSrcAycBERH7TYjvnVpjZEaO%2F%2B6by0xQaMRxuhJl9U8oLv92C%2Bnoq3sy3Do1oYOXyc6ZzmdqcgU8o96CiVa1rK%2FfVHJn0qq4b6xocotoacKEE1a0DHSfbhyU4tYwBr%2BJWVK3OmPTWwOZwXCUYwxWPf9K%2FkMhsNER5FNPd5z%2FUMS58XKtkjDPQ4GTHh8JybeN4C5Q5nhe0PE0TLHRBqL0drY5Jz8YXp78vcPCUZ5ff3dBwkZwPZ6Z%2B8bHGkjWm1zEGZyV5AQmuQTxjMUSWFv77OYJ9Tm61R6XYtel22gp5qvWSp1%2BP9AboZRWXxEhcmP%2BegsoGVeKjwjjdXOiceXJMfA4iQWVLk%2FG2LBJlaOHNW8C8r1iCXX3aYVH0FTwrbK7ahgcqwtd09oc8AOzSuEG68%2FupRnnpKAvEgJP%2BiGtfVdQ5eDcwLnYbXP3XwwLgboFOQpf9%2Fllz3Hqy4Fe4D7Rej%2BcrdxLq5IRSdxCGCuaWFIGULy%2B2%2BrQgGqMnG%2BEPL%2BDklyPHjdmjk%2Bve6YByLP4OBp%2FwfIgaiK1dvI4gHQ0CQQL%2FgtIFKug0183bHRekCaBvkdyuNqC%2F7rMsCWEWJRpgQEQI%2BAXukggofUva9pR9ByucGAMPBp1Qbm%2Bqe%2FWIqvcMNCP87wGOqUBloeKr62oOpUO2KRqvQqQqK%2F2nq7zwk%2FmbY8kxsgFqZrxY8QUgddq813cW0YsUmALxO2%2FiA%2Fu0UWCrcVQOxnMpab5fowHmy0IcrBa7v1mLyUFP%2BY%2BYx5dGcXhlMlKnsHLzMlCtkj%2Fam1NdYfGVb%2FPVZbXb5yfgqLJeWmnlUic7qpcx4TO6tZdoVIZi72Lnd%2FrjnyJTmfvu83nwE4%2Fv8FvwAlIgELV&X-Amz-Signature=8c58e0620e2ec5d24996a1352ec0cb9f286eed987a92315706e868e8def08165&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Data Visualization Libraries
#### 1. **Matplotlib**
- **Description:** The most well-known library for data visualization.
- **Features:** Great for making highly customizable graphs and plots.
#### 2. **Seaborn**
- **Description:** A high-level visualization library based on Matplotlib.
- **Features:** Easy to generate various plots like heat maps, time series, and violin plots.

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/733d1e42-5a53-4fd8-90c1-3d85254369a6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VX3LGCUM%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T131906Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGDH0fAkn0JCi4Nwa%2BNUSjWnqKdekN7rkTiOOavCIHIlAiAy8VeBpgDhZ5th0%2B5r5f0TzznDUJni9dMU58f3fORL3CqIBAi%2B%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMAV6JqMoME7DV3amKKtwDP7sdtuff0rBQa1LDl1G6vuGr%2BGtQseihJQqD6FvspjTrUv%2B1DiLdgnKpib1XYNmUZaFpx78hdQjEfyovqF72xB3AM9L%2BotXkF6fjlR6wWLLCHXcgEAUD0UbBWVBKmJZQURbKQYf1QFXqa4Vx9aP%2FTFZCFw%2Bu6JnVMisUazmTrfmUQACDdgTgoNplUSdPEct7zNihFid28%2FfcRqvQhDqch5KptD4%2FjsOpHmH6IcP4efnpURuyNjlJoohBrRAzoWt4OV7ecZShBRMMBGnv1PMzAaD17uAppMvGSFoMGVbUmPHal7fr0XoZDboxBPJCRlHvaZI97L8iUnKuP6oQVyFaXXQN2%2FtZ2wnI4JXqkpVmD7H6gBuCeDCcFN56yHXX%2FQpdgOdugzHTSY5ZNOc%2FVRs%2BjlRF76I41iDfqMSnLJO8iWT2iYBEyXEXe6dr2LtUgsmg9yJUwVlbgLfY8Ke5%2Fs4VIg8mTKUVX2yzQPvTaKESHKg7YKvYR5gYukMLuRFNGz4lYAaHKQi50cfSALGLNVQcTv%2FGFP1bSEofwngkp5EO3ua3xvy%2Baz5wq8RPCG0pM8xQGX4VOzyIthNPsjc3v6A%2B5zceo%2BUpuj1As4%2Br%2BSe8KtzMTaulq7woOasQQQkw84%2FzvAY6pgEy4%2FtirMBFJkQrwpmtgwOoddEZvzCJVaIivgWlW9qbaQ6B%2FdTUVPOmBanVM%2BF0qf2mRXD4HXd6veZRJzmB6V1pWMIwxxiBpcoJ4Z9E8RRM6WJCxLSCvkY1FEUMNpZEraAtU%2FuXsz92SUxMmlJLVcrOmAy62lwnID974Kl5fgX6IYfSaYogm4HO%2FPxchABDjFYYII9A9TcXuHymgeJYQKQcKbTEPWH0&X-Amz-Signature=a6b52f9fc20c545461a18280354273f296a3fe295ec527f6133831d52180dc1a&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Algorithmic Libraries
#### 1. **Scikit-learn**
- **Description:** Contains tools for statistical modeling, including regression, classification, clustering, etc.
- **Built on:** NumPy, SciPy, and Matplotlib.
#### 2. **Statsmodels**
- **Description:** A module for exploring data, estimating statistical models, and performing statistical tests.

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c62885f5-417d-4179-834f-d68f8f2bdf39/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VX3LGCUM%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T131906Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGDH0fAkn0JCi4Nwa%2BNUSjWnqKdekN7rkTiOOavCIHIlAiAy8VeBpgDhZ5th0%2B5r5f0TzznDUJni9dMU58f3fORL3CqIBAi%2B%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMAV6JqMoME7DV3amKKtwDP7sdtuff0rBQa1LDl1G6vuGr%2BGtQseihJQqD6FvspjTrUv%2B1DiLdgnKpib1XYNmUZaFpx78hdQjEfyovqF72xB3AM9L%2BotXkF6fjlR6wWLLCHXcgEAUD0UbBWVBKmJZQURbKQYf1QFXqa4Vx9aP%2FTFZCFw%2Bu6JnVMisUazmTrfmUQACDdgTgoNplUSdPEct7zNihFid28%2FfcRqvQhDqch5KptD4%2FjsOpHmH6IcP4efnpURuyNjlJoohBrRAzoWt4OV7ecZShBRMMBGnv1PMzAaD17uAppMvGSFoMGVbUmPHal7fr0XoZDboxBPJCRlHvaZI97L8iUnKuP6oQVyFaXXQN2%2FtZ2wnI4JXqkpVmD7H6gBuCeDCcFN56yHXX%2FQpdgOdugzHTSY5ZNOc%2FVRs%2BjlRF76I41iDfqMSnLJO8iWT2iYBEyXEXe6dr2LtUgsmg9yJUwVlbgLfY8Ke5%2Fs4VIg8mTKUVX2yzQPvTaKESHKg7YKvYR5gYukMLuRFNGz4lYAaHKQi50cfSALGLNVQcTv%2FGFP1bSEofwngkp5EO3ua3xvy%2Baz5wq8RPCG0pM8xQGX4VOzyIthNPsjc3v6A%2B5zceo%2BUpuj1As4%2Br%2BSe8KtzMTaulq7woOasQQQkw84%2FzvAY6pgEy4%2FtirMBFJkQrwpmtgwOoddEZvzCJVaIivgWlW9qbaQ6B%2FdTUVPOmBanVM%2BF0qf2mRXD4HXd6veZRJzmB6V1pWMIwxxiBpcoJ4Z9E8RRM6WJCxLSCvkY1FEUMNpZEraAtU%2FuXsz92SUxMmlJLVcrOmAy62lwnID974Kl5fgX6IYfSaYogm4HO%2FPxchABDjFYYII9A9TcXuHymgeJYQKQcKbTEPWH0&X-Amz-Signature=889ec7c833d5937f673acaa0a5282e3da172df7f4fc7d7d942deced58b7c7677&X-Amz-SignedHeaders=host&x-id=GetObject)
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
