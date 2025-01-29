

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

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/997ac361-58a8-4f04-bb0f-79fea4baa761/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Y6AJTPLS%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T182003Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDch9MjG%2BAdxNIQlPSVeBE7vL1f386EcHV083u37JCC3AIhALI9RM5Ms3PNyDUuTt3UdrG1W%2BoqHogaL5I00vicWoZlKogECJP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igw47qRz2VUsrFkfFOoq3APTxQIe6xHdwEDc8vW0D2p1yABqt7n%2FUUKU2IE%2FovIHFoXHgxgrvMoXkT3DQ0AarjO0rkxbzByLW1xk36noOvX%2BSwwgwv1Q%2Bm9PfJ6gcOBSEvXQ2wiTbQmXMeUu4u3cklPzlmtkHPxl2czm81%2BWLyRoKuCpPiQFl9527INFjTv5nR5JHxFwRtn0qOgxkYjlA0Oa2Dd%2BSYNmUp%2FdYddUK%2FtbecIYKLHk1cofUlBY2wqAmiECi6rKwgLY0O09B5EGtoLrCaf1uUCRuzZlBOjTHKYyIfnwDlqvE9KRg%2FGNprk3uJQmaXSXYn%2FIAY3l4%2BSE22SfGO8zg25fw3rQhTbIY7L5h5DimSiOHBjV3gBSz5JoNm3OiyjFY47PpicMX4wmMV9dkXUM81ookdzvOWSoAZI4YRNIEsNG0OA5R%2FT9lspi4EcXBizF2scNwzGC19NhxjggmMbNSNzQj7OsbiAthYCyEKA96lhMzh8XiP3NarK%2B7K9%2FdSUGP4YCOuG8VZCL4eOnl%2FYHHyYam3XymGHzLx5t0ZZIcySAUZ41R0lmERXRz95b235RCbEd%2BKLtUATParSDSvbLCXuHyjTXG5jn0bTHIJcPM6xQVCOCpMCU63GbmXNuQZM8YBE7G5AhHDDn2Om8BjqkAeX4UBQhtCBrebon%2FKDjNEVwSVpaDMdcNwfhZnip4aPHpT2Ku26CuJMjf5zuhytInLqSeBCapcQzFWZQUJ0KPe1wVRMSNMJ0kW5Yn0fyMm%2FSeYdbAdMZ5once%2BXgJGEiw1m1Qm306sdwjedXqAFESeI%2BXEA9SK7SIscNNhy8WT1NcMcGauoKMLkN0Ga%2F4NkTNea5WFNxrXZfn0TPKBxZxjNCo2e%2B&X-Amz-Signature=8603dece4f6e5a44e8df4f29ee2bf597a216933a22d7adf48e73730f5ad43fb1&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Data Visualization Libraries
#### 1. **Matplotlib**
- **Description:** The most well-known library for data visualization.
- **Features:** Great for making highly customizable graphs and plots.
#### 2. **Seaborn**
- **Description:** A high-level visualization library based on Matplotlib.
- **Features:** Easy to generate various plots like heat maps, time series, and violin plots.

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/733d1e42-5a53-4fd8-90c1-3d85254369a6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VUC2OMU2%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T182002Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIEt9hp8JimGEaQIZKARHgpC891DGBR4QIPgPcuqYjIF%2FAiEA3rN%2BKginzt3QrGKecPxnjtgaJy%2BkaqDJTQDXxvMdDUQqiAQIk%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDAKFHiqUJ9CKje%2FMbyrcAwe8QKnJZjC6oRLURvz2PGo5ZC3X9H0XtP0PAgGBZpSXVamqner7bbcv7m2G3k1Tyl2fFposCcluIZD%2Fqnki1kFdYEqpi4pbU2vuvjXIV%2BdZQersPu4e1ql6iwBFm0BxzSLKrGno3rmIjeIeuGjGzfHZJWFkRSrMQTH5sg9usnBMsp00kM%2FTCjU1nr%2FY4cCyKSkdg3gUPnVkAnU7dh3qEyybCK3qqlJz2Us3C2f9cf5r3q54MGrsfW9%2BApgFM3brrHLeNqFtR%2BrJ11ghR0d2zeSQcIsZ0OpLi4MG4SwBezu7LOsETasG%2FBiRtDiD4XlkmNhp2W9Bt7xbE1SepBgv2LVHfmjpFtzJO1dqqNnDl8%2Bcq%2BFT%2BfLFTUobDNFDmkDSunl1eou1WZoJKOT4jgF%2BprFF2edHHbXn8jsg1cJUu5HZGebP%2FaF1hAQEvl9pSgSUqgciJClSBmW6kWqShkLHadnsEIO5gYPBzexNFE2FbfCFOzD9yQV%2Fy%2BuusQ9GS8hwDWUMQFCGQ4DHsqJH2OB1xeNdl3wilZaTzvyXMijhIxf9HRySC4Mokm%2B1xc5VMbGBDbutIsMz%2FlxnCF96cwMXlhDcgpozhyfOLs2B1aAjwyTvVVvvsoMz%2BOPQLE2%2FMMPY6bwGOqUBiWjzXv3%2BNlNXiECbNX0%2Bf0OJIyaWgUbhD4yAT%2FjzGJyZQB8i2q%2B4Y26dlhZ5RaO1huRD02YKAk8e1fXe3AsBclI0Z7HnSExGCOwQwNQtXTEl3yiIZ67U643mZR%2BZoA0UJCC1K6Go7Gbd5duQKRYExQYXKt3EgmI9Nd0RVSy%2FQhIFo1AFvIjB4lAcDnl8ro7Czds4CO%2Fn6uG6M2dfzmv6h09ewjng&X-Amz-Signature=754549b78d09a8b951632578051bddc3438af12f03838ce8f7d0e6780436527e&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Algorithmic Libraries
#### 1. **Scikit-learn**
- **Description:** Contains tools for statistical modeling, including regression, classification, clustering, etc.
- **Built on:** NumPy, SciPy, and Matplotlib.
#### 2. **Statsmodels**
- **Description:** A module for exploring data, estimating statistical models, and performing statistical tests.

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c62885f5-417d-4179-834f-d68f8f2bdf39/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VUC2OMU2%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T182002Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIEt9hp8JimGEaQIZKARHgpC891DGBR4QIPgPcuqYjIF%2FAiEA3rN%2BKginzt3QrGKecPxnjtgaJy%2BkaqDJTQDXxvMdDUQqiAQIk%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDAKFHiqUJ9CKje%2FMbyrcAwe8QKnJZjC6oRLURvz2PGo5ZC3X9H0XtP0PAgGBZpSXVamqner7bbcv7m2G3k1Tyl2fFposCcluIZD%2Fqnki1kFdYEqpi4pbU2vuvjXIV%2BdZQersPu4e1ql6iwBFm0BxzSLKrGno3rmIjeIeuGjGzfHZJWFkRSrMQTH5sg9usnBMsp00kM%2FTCjU1nr%2FY4cCyKSkdg3gUPnVkAnU7dh3qEyybCK3qqlJz2Us3C2f9cf5r3q54MGrsfW9%2BApgFM3brrHLeNqFtR%2BrJ11ghR0d2zeSQcIsZ0OpLi4MG4SwBezu7LOsETasG%2FBiRtDiD4XlkmNhp2W9Bt7xbE1SepBgv2LVHfmjpFtzJO1dqqNnDl8%2Bcq%2BFT%2BfLFTUobDNFDmkDSunl1eou1WZoJKOT4jgF%2BprFF2edHHbXn8jsg1cJUu5HZGebP%2FaF1hAQEvl9pSgSUqgciJClSBmW6kWqShkLHadnsEIO5gYPBzexNFE2FbfCFOzD9yQV%2Fy%2BuusQ9GS8hwDWUMQFCGQ4DHsqJH2OB1xeNdl3wilZaTzvyXMijhIxf9HRySC4Mokm%2B1xc5VMbGBDbutIsMz%2FlxnCF96cwMXlhDcgpozhyfOLs2B1aAjwyTvVVvvsoMz%2BOPQLE2%2FMMPY6bwGOqUBiWjzXv3%2BNlNXiECbNX0%2Bf0OJIyaWgUbhD4yAT%2FjzGJyZQB8i2q%2B4Y26dlhZ5RaO1huRD02YKAk8e1fXe3AsBclI0Z7HnSExGCOwQwNQtXTEl3yiIZ67U643mZR%2BZoA0UJCC1K6Go7Gbd5duQKRYExQYXKt3EgmI9Nd0RVSy%2FQhIFo1AFvIjB4lAcDnl8ro7Czds4CO%2Fn6uG6M2dfzmv6h09ewjng&X-Amz-Signature=d1caeee1bbeb4c53dcf8b8586fc99bd619dac4af902185a55f19c0528d47700c&X-Amz-SignedHeaders=host&x-id=GetObject)
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
