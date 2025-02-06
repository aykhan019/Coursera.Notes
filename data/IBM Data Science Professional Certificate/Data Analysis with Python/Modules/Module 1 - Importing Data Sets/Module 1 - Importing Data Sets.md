

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

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/997ac361-58a8-4f04-bb0f-79fea4baa761/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WS5DTBO4%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T151610Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEcaCXVzLXdlc3QtMiJIMEYCIQCJz9kcbHuQqt%2BBWVfXDJCMZcuFMKsQjagIkrRi2rhyWgIhAOH2OdZ1jpZFuZ2wv5Ik2vdSuZgMkffr%2B%2Bi4Kf24nUnTKv8DCGAQABoMNjM3NDIzMTgzODA1Igx1IXut3rXiYXwq26Qq3APjfUp9Ovw9ZRDLc%2F0m5GQVzM7SR%2FFT1ffliWJYKcsp8EQwB2RcRYcgnLET7OUz118uCSMZBC1Ur6nU%2BMMqBQjxNbuYY7wjAKO4DGLtAwvsuQKwuYz%2FRf5hNr7BguC%2FmUL7xz6v47zf822BRDeJy8icB322h5yFKReRWDw8ahtJJ4lEoDRRGbeLp0tkIB8MlpjDCVZFGFdhzpJNDi6o1ilG2rYykkWeY8pzCu3IKazP8IW6gFClyXUGolTSZiDRv5t1rjmSK1IBKuw0z15bBFqN%2FutdJK7GJhQ8%2FSFFgbVtUfCgmlA1%2FDbyGfTWhp%2F1wZ8XmeuNd1qw0Gvq38mFtmRhIBqozKUPT2eUbk3RnIpF3zhPKitST%2Bqdi%2FLEh47FdeM5JKKxSyeKVEXl8t1bXK07DURAABSV4r4LT2jIRqNjIv4Ow%2Fzj9pnaLr7WL5XIkCGB1KCcVNHpKrfq8ibqlPzjjByVgTOmRloIoGUWRTo7mtugt5KKMa1vkkkolY5JxhOACujNyCAmFU5qRPmkgDY7N2EsTJz%2Bzuwb6HoYLYL09qToh5zVCe%2BBUIQhCLkBXQIw%2FxmRmZbU7Wa3K6%2FNdqMCfoKQEK9fre1pLegf7Y%2BCXxCfCB6iKXrt1smdWzCunJO9BjqkAfoI5wkbL%2B2KH7d99j9Y%2FSIxzZabz1yX4GjWDO3g9i96aYFieL9qmfzuvHgHUguraZLD7IjD9l8rY%2FOuGNipbp8JYcfdfHNhh6GoHOOVTPF0n2S3SEpA1tIxhxoQ7tq4rOibPZBPzFNRX4eEAY6ULA1i%2FaSRDKrDEcyl33zNvij1icONzlcdxMICmq9wSLW%2BdMNeSoxBiAc%2BxjFUeL87kN2gvKG%2F&X-Amz-Signature=1e119523e6bb18f1a8bde71aa8956aa74db31d66b64404ea9087d39081efdd36&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Data Visualization Libraries
#### 1. **Matplotlib**
- **Description:** The most well-known library for data visualization.
- **Features:** Great for making highly customizable graphs and plots.
#### 2. **Seaborn**
- **Description:** A high-level visualization library based on Matplotlib.
- **Features:** Easy to generate various plots like heat maps, time series, and violin plots.

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/733d1e42-5a53-4fd8-90c1-3d85254369a6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WDDB6URA%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T151608Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEcaCXVzLXdlc3QtMiJHMEUCIQDaEIxJe03s5EE1mJOVVfAPGZEf8ZlPw36tdZyerXWfCQIgOGuOOiG85xc7aYk6WNs1M%2FDnMZGVSF0mEnBmefnH5EMq%2FwMIYBAAGgw2Mzc0MjMxODM4MDUiDKd%2B9K3GWjZMka90kSrcA5GCo%2FqbzMqLLiz43O2cPPvSft3w%2BfZfDnQrvnRcMry6wFT18Ug9zYeiroAO2D5Xb%2Fq1Y8g62bctJ6cehhq8XX%2FkRovBTV1NfUjeyXLwFAnUVeAE3TOh8jjJg%2F0MqPsJUImeIY1P1i6GVOHvMy17IAsr2iW%2BQvC7HDWhq9Ms%2FFvZWChZYtsdZ8T%2FwB5%2FOr0C4fk7CS7m0KkLVwqaWOtZKetDy0NEp%2Bna1MtSX54NeJyd5Fl0kP1G1h96uqL2CJ7hxnL4dMhPNqCidMz1qqbekfxiqpgHjkcDIhyyCmA4vjYd2YqMjV97PGeswC3pPBf%2BAiNRc4JkGzZgv%2BvbBa2KzC1MtMdqFrUUJijBW93WlW2oeIPLU6dt87xKoWkQ%2FRggu6SKq%2FT2KJ63fCToBzpmjFOY8gr0XgJu2xGSckVPTthpU8SoOG6g%2BxPuSzisAx%2FsOoTMmTMMVB%2FShVo5NnngD4xIdE%2BfCap%2F0HgCp%2FzJJgiCa5SzwwOxckSmXVt4coAHM7udSxty2nVT27L%2BuI7Bzc8RQnltjNLlKCU5Iu0xJhQxuZ9M3GppL4p6PgkEQZoLFOfOIwi05xH1HaUEBffNwZI8aWjRWBQUytwKEnC8nbp9G%2F3qxA8Ds7xSKMhkMO2bk70GOqUBXI68KdSjrBqHPxSZ3Mm%2Fj%2B%2F%2Fb2QK3HqshQAJxjQ9czi0ABnYzSzpYXqLKW9pQ4BvwoQ6gz5W6euREJ1qh10YKyI0%2FgfALwmoCuTzjUEYTuxnsmMA5tCykrnSpGmSQTzoKycrGxpeTsnVC6TSR%2Bq%2FP1Q4ZXRJjLx1Nzzq9ALEzl9yIGZBnvUhcgQE%2Fz2LiTUxQBM0%2FIGSMsMUpHoIzXUMTzYRmc4G&X-Amz-Signature=3563c088e59b1cb75503a0e6d211c08a612e08d7815da83484616d25ee057fa7&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Algorithmic Libraries
#### 1. **Scikit-learn**
- **Description:** Contains tools for statistical modeling, including regression, classification, clustering, etc.
- **Built on:** NumPy, SciPy, and Matplotlib.
#### 2. **Statsmodels**
- **Description:** A module for exploring data, estimating statistical models, and performing statistical tests.

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c62885f5-417d-4179-834f-d68f8f2bdf39/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WDDB6URA%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T151608Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEcaCXVzLXdlc3QtMiJHMEUCIQDaEIxJe03s5EE1mJOVVfAPGZEf8ZlPw36tdZyerXWfCQIgOGuOOiG85xc7aYk6WNs1M%2FDnMZGVSF0mEnBmefnH5EMq%2FwMIYBAAGgw2Mzc0MjMxODM4MDUiDKd%2B9K3GWjZMka90kSrcA5GCo%2FqbzMqLLiz43O2cPPvSft3w%2BfZfDnQrvnRcMry6wFT18Ug9zYeiroAO2D5Xb%2Fq1Y8g62bctJ6cehhq8XX%2FkRovBTV1NfUjeyXLwFAnUVeAE3TOh8jjJg%2F0MqPsJUImeIY1P1i6GVOHvMy17IAsr2iW%2BQvC7HDWhq9Ms%2FFvZWChZYtsdZ8T%2FwB5%2FOr0C4fk7CS7m0KkLVwqaWOtZKetDy0NEp%2Bna1MtSX54NeJyd5Fl0kP1G1h96uqL2CJ7hxnL4dMhPNqCidMz1qqbekfxiqpgHjkcDIhyyCmA4vjYd2YqMjV97PGeswC3pPBf%2BAiNRc4JkGzZgv%2BvbBa2KzC1MtMdqFrUUJijBW93WlW2oeIPLU6dt87xKoWkQ%2FRggu6SKq%2FT2KJ63fCToBzpmjFOY8gr0XgJu2xGSckVPTthpU8SoOG6g%2BxPuSzisAx%2FsOoTMmTMMVB%2FShVo5NnngD4xIdE%2BfCap%2F0HgCp%2FzJJgiCa5SzwwOxckSmXVt4coAHM7udSxty2nVT27L%2BuI7Bzc8RQnltjNLlKCU5Iu0xJhQxuZ9M3GppL4p6PgkEQZoLFOfOIwi05xH1HaUEBffNwZI8aWjRWBQUytwKEnC8nbp9G%2F3qxA8Ds7xSKMhkMO2bk70GOqUBXI68KdSjrBqHPxSZ3Mm%2Fj%2B%2F%2Fb2QK3HqshQAJxjQ9czi0ABnYzSzpYXqLKW9pQ4BvwoQ6gz5W6euREJ1qh10YKyI0%2FgfALwmoCuTzjUEYTuxnsmMA5tCykrnSpGmSQTzoKycrGxpeTsnVC6TSR%2Bq%2FP1Q4ZXRJjLx1Nzzq9ALEzl9yIGZBnvUhcgQE%2Fz2LiTUxQBM0%2FIGSMsMUpHoIzXUMTzYRmc4G&X-Amz-Signature=11398ac39b0aa7552199c4ccce4cd3458239e60ba295a71da66be185fd341d52&X-Amz-SignedHeaders=host&x-id=GetObject)
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
