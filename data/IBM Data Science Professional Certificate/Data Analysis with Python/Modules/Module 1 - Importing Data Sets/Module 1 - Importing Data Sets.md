

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

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/997ac361-58a8-4f04-bb0f-79fea4baa761/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QNPVIU4U%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T151552Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBYaCXVzLXdlc3QtMiJGMEQCIHUTyZWyZ4y0NSRU1k1Nc7joHOPwbahKj9nSIwHeRtvPAiALzYVcMpfYx6JADz2WPbZIYAV%2FbONNspQpfLwqJSOGZCr%2FAwgvEAAaDDYzNzQyMzE4MzgwNSIMCO7pB8xs1YmBZJ0pKtwD8Fy8IXXF9m0no9PWGSqQgn%2BDnV51lUm29W7IEzpizZ7PyMH9DPrazPUD79rUs5H4ioUe2hwycyxoYNfhocX4qJS9T%2B30IDkjt1XLi1mb6fjJlg%2Frb1Zq20JMYW4P6CRdNk6bKd7d78xkqfzH5MUfsGuK2EH%2BJ%2BaAoIUaX%2B%2Fw17WtLbA0IC14cETcFAsMiQbBhLdTQU%2BaBPX2p1TCI5XinOUflyzgKbauX1whKkgj4YktLcx19TUPJX5jxUINrMjb7NPQD9PKcOBcmdYbDahx6bsn7ZF8mHYd749X1QBe%2Bl4l2YNuOaMO8RI%2FnKnh3akKInfEPTsA1i8FSg6iiyDflE6CWTeV6D0xcKysqMsn2xkDoDbBcd6aRSU8vKACcuwBeXLoEBjsNlmWw6Wm7Kk7f1EcL%2FdsDWQDsJMkLGtb9CJX%2Fn97c3KASdb7UB70dzchDMrop%2B6VZDeQQVQGZHjeEAuPUf6YNjkoSnYgrSbt5MN7DcB%2BtbiNLnADpPtwhwRBkSoInGZt8UhnYkQBeE%2FWfHZ4Qk6vaj74ikRg1MUEzrOsE5Ls0iYS%2B2NujBZmuI%2FQZ61jdjq3yfxdVNNxk28RTACUyEUrMu%2BvP7tYXhZfcDzohXFlbFc0huv2Vn4wv7yIvQY6pgHTBJn0%2F7WwGb6K9TOHi8EWbHn7iNFYB1taw3h2l7khDrx%2FWmPncMcIgI0tu4psBD97qs18g1cP3D8Sm4L%2Bld6Oelo7myLA9O8HddMipjaTSD6wXr58QybxLutpajGFE4g6PKg0Dsm%2FGIPihc%2FPv%2B9Uxzu4FSpE58ZoLGDuW%2BCm7G9gTaYLstXpP5IJ6aIdupUBHW2B%2B84fE4WG7LyhZLV6UP2qIxGh&X-Amz-Signature=15ebca9f0e65b4604ffb518b5ae83877a6ecb36cb2e6b28806f84f84b968812b&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Data Visualization Libraries
#### 1. **Matplotlib**
- **Description:** The most well-known library for data visualization.
- **Features:** Great for making highly customizable graphs and plots.
#### 2. **Seaborn**
- **Description:** A high-level visualization library based on Matplotlib.
- **Features:** Easy to generate various plots like heat maps, time series, and violin plots.

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/733d1e42-5a53-4fd8-90c1-3d85254369a6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZQCPAT7R%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T151551Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBYaCXVzLXdlc3QtMiJGMEQCIGBitiqe8UQ%2FALOg6QzUscRy%2Bgiwhawm95KMTWgDe2AfAiBt0%2BucvTNVHsPj0Zqqbf6PKW%2BvAF%2BIvBg1Sr4IdWOeeyr%2FAwgvEAAaDDYzNzQyMzE4MzgwNSIMnMrTte6iNCLHAgvCKtwDuPFdDW2KfrHgLLcpWz8KG7HJgE%2BklmIsFmrUwDrwKs05yPlp3tJW%2BMXxfAbM%2BcftRiJ8v4bUZyqPsaCoVAL%2F4YMRq5%2Bd80gRFw3MUfhGWZsEh0VNJyrpphxGWrqW5g3pDgxP3D2lEFLczfkrMmtXKyaEG1OB4PIwVL9s33mJi6yxibSDzDNXOpq%2BkxaYWI0QD7TU3Iz5TnSQ1xwniYFVxmxzps2zDz38j2xrKplhS0qqfVZSBasbUaQbuPtIwgY2iMkg4NmC1YAVWR%2BCIkK7VsfG7L3%2BVTe9obs11Uk1u9s9TZ58C%2FlZE5aPw3b1O8DCSaa5UuR5m%2BZ5To45LjxZSSCZxNocdEa3TX4THuRDMXhU9qd4FEk0Fks5TOX2K9y6N4e9bBMYWtnkdI%2Br%2FrdDoCjllZxUGb%2BuLra2vWztRxTjzOzXFl1%2FTVX6p417YyJ%2F0HPQirjRjKxfnDhrPTmPlt7PAO4WifLIyleBWmOb2643sylQ7wD3jAx841D%2F2Hgb0%2BomjEE5GhUOM1rwg0doXhXhAqKoI8knhXOyH19pu5xRrAmkdbagYIBKoOTWftpC%2Fs%2FYk2wQIWxHHCbC%2FgZDZZpdleHJusvDfOYK1zytDOZ7Dhoq%2ByBuPPHf6oIwo72IvQY6pgGntkOe36%2Bv1RogRyua4VJTh%2FbFrM7NcOYihuPyRYZw9r7GY7SaU%2F3zLDeuSB4INmfa5BA3s1pSEXX15QRiUic1KUPzkp72sbqlpItUyfp55mEyFKdRTWvJdNmxmVBFHqwjJJHXlhKdPEW163ImKsKoTGQvKTa2TFCkslRJQUhVrg5KsL2AZ5zqjOPfqQ2ABPb3REDltafd0smo7M8KiHZ%2BUYT6f3VJ&X-Amz-Signature=ae2a305cf090cdc5caced25106ab0a32fe43afa7debfb117d2f10e8f0937d88a&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Algorithmic Libraries
#### 1. **Scikit-learn**
- **Description:** Contains tools for statistical modeling, including regression, classification, clustering, etc.
- **Built on:** NumPy, SciPy, and Matplotlib.
#### 2. **Statsmodels**
- **Description:** A module for exploring data, estimating statistical models, and performing statistical tests.

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c62885f5-417d-4179-834f-d68f8f2bdf39/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZQCPAT7R%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T151551Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBYaCXVzLXdlc3QtMiJGMEQCIGBitiqe8UQ%2FALOg6QzUscRy%2Bgiwhawm95KMTWgDe2AfAiBt0%2BucvTNVHsPj0Zqqbf6PKW%2BvAF%2BIvBg1Sr4IdWOeeyr%2FAwgvEAAaDDYzNzQyMzE4MzgwNSIMnMrTte6iNCLHAgvCKtwDuPFdDW2KfrHgLLcpWz8KG7HJgE%2BklmIsFmrUwDrwKs05yPlp3tJW%2BMXxfAbM%2BcftRiJ8v4bUZyqPsaCoVAL%2F4YMRq5%2Bd80gRFw3MUfhGWZsEh0VNJyrpphxGWrqW5g3pDgxP3D2lEFLczfkrMmtXKyaEG1OB4PIwVL9s33mJi6yxibSDzDNXOpq%2BkxaYWI0QD7TU3Iz5TnSQ1xwniYFVxmxzps2zDz38j2xrKplhS0qqfVZSBasbUaQbuPtIwgY2iMkg4NmC1YAVWR%2BCIkK7VsfG7L3%2BVTe9obs11Uk1u9s9TZ58C%2FlZE5aPw3b1O8DCSaa5UuR5m%2BZ5To45LjxZSSCZxNocdEa3TX4THuRDMXhU9qd4FEk0Fks5TOX2K9y6N4e9bBMYWtnkdI%2Br%2FrdDoCjllZxUGb%2BuLra2vWztRxTjzOzXFl1%2FTVX6p417YyJ%2F0HPQirjRjKxfnDhrPTmPlt7PAO4WifLIyleBWmOb2643sylQ7wD3jAx841D%2F2Hgb0%2BomjEE5GhUOM1rwg0doXhXhAqKoI8knhXOyH19pu5xRrAmkdbagYIBKoOTWftpC%2Fs%2FYk2wQIWxHHCbC%2FgZDZZpdleHJusvDfOYK1zytDOZ7Dhoq%2ByBuPPHf6oIwo72IvQY6pgGntkOe36%2Bv1RogRyua4VJTh%2FbFrM7NcOYihuPyRYZw9r7GY7SaU%2F3zLDeuSB4INmfa5BA3s1pSEXX15QRiUic1KUPzkp72sbqlpItUyfp55mEyFKdRTWvJdNmxmVBFHqwjJJHXlhKdPEW163ImKsKoTGQvKTa2TFCkslRJQUhVrg5KsL2AZ5zqjOPfqQ2ABPb3REDltafd0smo7M8KiHZ%2BUYT6f3VJ&X-Amz-Signature=9f51b2d5cf229d3ccee8f17d4b375c59582893c3080c90cd8b6d2e3e24784f96&X-Amz-SignedHeaders=host&x-id=GetObject)
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
