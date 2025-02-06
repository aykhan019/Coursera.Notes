

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

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/997ac361-58a8-4f04-bb0f-79fea4baa761/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663XN6WMFX%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T024348Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDgaCXVzLXdlc3QtMiJIMEYCIQCkz7sdlwroBF%2BffkvljGJsXfwsD%2FMZRnhu7ZSktVrxSQIhAO6SwisVr3jBrLwYl63qYUqDQLarGkLZOOtfAugcqo1WKv8DCFEQABoMNjM3NDIzMTgzODA1IgxHvLFVMou%2FqX4u7I4q3ANnjzuoTInMv%2B%2BVa%2FEKxCZ92BOXunTRGSHRkSgk6%2FrRdsRn1bHM38S0YzYGUIcE%2FFCRtBUgNozEj8j5%2FGnmSwoKOi4CYmYKaagSAnL2EDs9%2FHChdMbgcbGTSKtIbjN2P6CoGQa%2F4EFhRZcFwn4o2TrvPybq%2BwiUg3KmtHtS1nkQ7yZJOqsg91mM1Lo32eUIXalDm%2B%2FWvh5WAlkY9y%2BYvQUQ9NnRzRiVoRf2ARmAJ4C5nW7HNzZNEUbm0q57AfJ992IDDpIxZADjtOqcDRuf09VakJyf9%2Bf3b4QVbS4UnBHM0gHinhsNVG0WCYUtYyY6C6X2IDLjvwU9xp5wMsnFpkfx6xlIgGozGPAxFv6DDzzr7m0TTCsmCBVCA1afWcZZPrSkn4MHPxY9w5N4gsQa16A6k9%2BRSwIqNAd%2F8xJ0homWFQ5LuO8u4vlD2JBaKivwWobRnPuI7kUm0KPXif5yYZmzeEr2QMFnx5%2F%2FSK45IXb7RBtaY4JkRl4BlCotdbZlSAfGZC9HeNlVH281fSD9B0oC27fa9LacBi9ug0kT%2FuAVHPPsgYBnvxvIgtZV%2FaBWVyxIrfk1RoJfF2PCWSeuj9SRAdCtxDfal17QC96tMCrv10HT3de2Gc1h4adzAzDw6o%2B9BjqkAYZYAFQY3EHMEm2S%2FPf9WhpZ3ZnpkqtWaEOG7POv%2BI9e8GZpMga2rNp%2BAt9bZaCdoBmxqSryj%2FOBmhwHslG1qCu%2FG8G%2BfqPEtyD6Des3iRdFwVDnMKd6%2BZpNpek1A8idBLbs8U0SvKwn%2FyaLLUQ0OKLKI85sHZagUsmS2YEhnMJ23jSULcIBLqp23D7Ru9jmKcc0pKWmZis0sP%2BAs2g5vGC%2FuwUi&X-Amz-Signature=47f6175fe24223d11fe4425d5ec783b41e6d74b455a8c3e287bba0e8d567028d&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Data Visualization Libraries
#### 1. **Matplotlib**
- **Description:** The most well-known library for data visualization.
- **Features:** Great for making highly customizable graphs and plots.
#### 2. **Seaborn**
- **Description:** A high-level visualization library based on Matplotlib.
- **Features:** Easy to generate various plots like heat maps, time series, and violin plots.

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/733d1e42-5a53-4fd8-90c1-3d85254369a6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WJNGOCYF%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T024342Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDgaCXVzLXdlc3QtMiJGMEQCIB66ZVyNXxxz5rrKrsqKBYzXf405wOCHe62p0aJQlGm1AiBdgUBgUMt2kNXt%2FSDUBINT3xeIyfEEZobWk%2BPE8maKsir%2FAwhREAAaDDYzNzQyMzE4MzgwNSIM87kgj4dgPKXUPQ6XKtwDfCFxkktRiiulJEdiMa1YApNbcSQLcl6Rtb4nPvpg61O8qZI6mw7DTC07mruK5SN%2FL3IioTGWTG01OmHOPC41nJmzz%2BVgvLLevjApFqDAkxEAOr96O%2FO3hX%2FVXYoT%2FKq3bXsvKvxM6xKKlOyD9TJOzXz1yThWHa9HB1Xg7XnRkFQD0f9YxkTIolzsdm8xbYAxUeqjsQUueHkn5LbWrlr6FX3DJ9YreUKhmeLK%2B3l4nyfprGEuS7U1GMtaDwMR1hwvYKKKzpKFh0x77vyep0ItvSwqaHX20oABs%2FEcXHLUJrQCMB0tkjnWwnSg3EwHmQhywMmO3DvdCEEsf4raLVaDB1u1S%2FLO69sWiVxn3886Wp%2FdpZgW88nvPYMz9jNy4Fo8D9I4Z9%2Bs26WNy0arI07b2jd%2BiNBx6VJmKB82aF1hEmsPrYpXj5FgR0wdrsn1vcdEQX4I0mEtdoFQ%2FsVN%2FEV%2BtboD2JuP9d%2BwSUJyokIjM09dUq6SP3EbWD7XJLu9gXza4s%2FGSldXbqCiob2g6Rupx%2Bp34g65ftQpaCO2n0wVfEK7v3lBz%2BmvP7Xxiszs8eKegvY%2BqMDCy3%2Fs40%2BSEYENXD0pOzSQ1evrZoFzrqFQ4PPfDwUcN85UVVFFT6Aw5eqPvQY6pgG%2FQqOO9D8Y3m3%2BtUxz%2BKwKTJ0EbxkTPU1W1QJW9ZiOQw9bOSgMUCxP3BQZ7HauAUx9V7v8S02Sj6orUj7f%2FNMFPRQK3aDsUrloP1dlg63wosBrhTrILZNzBgcdUlwJL0UeTfBboh1%2F2D%2FrByYYMhyt3%2FtjCigz1JqSZcru19jW1448n4Gt49kiQCZJGNtaL3wDrPGi4pPlGWq1GEdYDk%2F4EmC303vz&X-Amz-Signature=7d6b6d4e51e4e70a79b3cecdad4013e49fd8419116c712f527d89d559a087ee3&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Algorithmic Libraries
#### 1. **Scikit-learn**
- **Description:** Contains tools for statistical modeling, including regression, classification, clustering, etc.
- **Built on:** NumPy, SciPy, and Matplotlib.
#### 2. **Statsmodels**
- **Description:** A module for exploring data, estimating statistical models, and performing statistical tests.

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c62885f5-417d-4179-834f-d68f8f2bdf39/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WJNGOCYF%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T024342Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDgaCXVzLXdlc3QtMiJGMEQCIB66ZVyNXxxz5rrKrsqKBYzXf405wOCHe62p0aJQlGm1AiBdgUBgUMt2kNXt%2FSDUBINT3xeIyfEEZobWk%2BPE8maKsir%2FAwhREAAaDDYzNzQyMzE4MzgwNSIM87kgj4dgPKXUPQ6XKtwDfCFxkktRiiulJEdiMa1YApNbcSQLcl6Rtb4nPvpg61O8qZI6mw7DTC07mruK5SN%2FL3IioTGWTG01OmHOPC41nJmzz%2BVgvLLevjApFqDAkxEAOr96O%2FO3hX%2FVXYoT%2FKq3bXsvKvxM6xKKlOyD9TJOzXz1yThWHa9HB1Xg7XnRkFQD0f9YxkTIolzsdm8xbYAxUeqjsQUueHkn5LbWrlr6FX3DJ9YreUKhmeLK%2B3l4nyfprGEuS7U1GMtaDwMR1hwvYKKKzpKFh0x77vyep0ItvSwqaHX20oABs%2FEcXHLUJrQCMB0tkjnWwnSg3EwHmQhywMmO3DvdCEEsf4raLVaDB1u1S%2FLO69sWiVxn3886Wp%2FdpZgW88nvPYMz9jNy4Fo8D9I4Z9%2Bs26WNy0arI07b2jd%2BiNBx6VJmKB82aF1hEmsPrYpXj5FgR0wdrsn1vcdEQX4I0mEtdoFQ%2FsVN%2FEV%2BtboD2JuP9d%2BwSUJyokIjM09dUq6SP3EbWD7XJLu9gXza4s%2FGSldXbqCiob2g6Rupx%2Bp34g65ftQpaCO2n0wVfEK7v3lBz%2BmvP7Xxiszs8eKegvY%2BqMDCy3%2Fs40%2BSEYENXD0pOzSQ1evrZoFzrqFQ4PPfDwUcN85UVVFFT6Aw5eqPvQY6pgG%2FQqOO9D8Y3m3%2BtUxz%2BKwKTJ0EbxkTPU1W1QJW9ZiOQw9bOSgMUCxP3BQZ7HauAUx9V7v8S02Sj6orUj7f%2FNMFPRQK3aDsUrloP1dlg63wosBrhTrILZNzBgcdUlwJL0UeTfBboh1%2F2D%2FrByYYMhyt3%2FtjCigz1JqSZcru19jW1448n4Gt49kiQCZJGNtaL3wDrPGi4pPlGWq1GEdYDk%2F4EmC303vz&X-Amz-Signature=4ae261b03931e717b8c5b9f846814dc6d4ddca8aef2054c31d7161c0dd1ed1a7&X-Amz-SignedHeaders=host&x-id=GetObject)
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
