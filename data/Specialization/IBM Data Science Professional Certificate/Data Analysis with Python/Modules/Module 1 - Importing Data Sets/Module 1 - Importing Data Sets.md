

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

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/997ac361-58a8-4f04-bb0f-79fea4baa761/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TIXHQKBI%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T010810Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHkaCXVzLXdlc3QtMiJHMEUCIFA3jjo%2BleOnGTkOhiJ3tG%2Fjhfz6mYTUq9g2WGsDLGJzAiEA3989wn6UneEmlU2dqGJOsbgldIYYSn8DSuOvFu00iwcqiAQIgf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJoxFktWtJTcylm%2FGCrcA5s68zgYCGXUSPQawWqoHKXewLUtU13betj0bPgvXXLQTGlr%2Bj6RyNs3G%2B2fIZjz3q8rbCjirW2c1iUFb2E5vdA5zKb2MTznoUxRCVVHLdFO%2BpJ5QKlXXRZTXL2%2Fj0xqWGQTG4VARbdDtsD6Jo8MzZYtOUw%2FPPx6bnd%2FetgE0mxU9AnKYEopTw8qoPaxvfyGWJ3qQbZgpcx2C52LM6Z06a6Pu0si97W9fSNKPjHQf6Qdgs49DIzkZMcgOM1Y%2FRSt8iTNmIMtbYUQrPpJ6G7W3%2BM6kwsGAJIg9%2FJOyXKasEGI8n1kaQw9SEpynSQ6p1tRxNZGi2L8Icdt6v3qMy4nZ2JZdaRXWUH7r6sIX50fkKOdGHewn2othpobPvU3mTtNTAEokEAajgmTPta4JY%2Bd9wVY0tQv26S3LaM4LUp0%2ByA3crxB119rdqGDsquUPUbMGsABZpXHGc2Eb6kpS2KdWyC%2F1mg7gA9lyvguatVGPyyarGPFdxuhsuWM3wHYDZNivWzncrMOnrm%2FwvpTb3NC6eJiqLylX2F2OLN1AZF%2BZyZekDZeGsYLBCc1QuFGW%2B3e52%2FPagOTHluKoCOXvg1IC5OU3xGz%2Fwq06FhJWdfpeyv%2F3hgh3r%2BYKP3%2BJAdUMJjo5bwGOqUBLDFJIjtNoIthpS%2FgrFY1W5SCaiBxODcnpVZOjjLJ1TPTWUoO%2FQvtC5WrhlzH16JxN3iBR9TQtuylieor2JtF8lGeS6BurvfZbE03yu0zUIjxpZPZnArXWnXZBFaKg%2BCiBM5SpfqNSBZsFFLI8nOI9cPH8yg7bnKlRal4J83UYNkqkmQ6lc1prImqwjBFOith%2BfspN%2BG2o2LO5pmyK84wdA9lJvtr&X-Amz-Signature=a21082da18cf09d11691dabdc1fccf86f451d2d2ac5a6a6440926659188ac4c8&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Data Visualization Libraries
#### 1. **Matplotlib**
- **Description:** The most well-known library for data visualization.
- **Features:** Great for making highly customizable graphs and plots.
#### 2. **Seaborn**
- **Description:** A high-level visualization library based on Matplotlib.
- **Features:** Easy to generate various plots like heat maps, time series, and violin plots.

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/733d1e42-5a53-4fd8-90c1-3d85254369a6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZYMUMIHK%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T010809Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHkaCXVzLXdlc3QtMiJHMEUCIERYDGPHi%2FErIhuZJ2TuTK47lK3LE0X5my%2FD9DdV6JyXAiEA7e14HzDhWVGnv1e3UnhZMYEnM9MKA1ZZaOKfldhRb90qiAQIgf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDBngyAoWAyHpupQ8QyrcAw5vIn1FUZMcQVDMY24NvbHowffLq%2FLHpaMS%2BPJ2cJM1nNu0OAC%2BDuPmDVHrLnx9GNTqKoXXP%2BT%2BSJkUglOHtXtLbjmeqC0SIhPQk%2Brt3bTl7zqu8xN3sRSDKs27i1mE7BycW7bfEUCbmKeACkHyAzOux%2FGpFt41aM7Iwp%2B%2Bp4%2FIP67wZJL0Dmu4IJ1hYnDGTDHk%2FCBI5nWdMKO2tSwHSztR%2BNNPnw7DgWipbmj%2FljLNqUntnk3NxQ%2BRq1DnHukEMW3h8xe4lFYuVMvVQGZ5p0JROzWYRh6WvrjHJnLLITDOnEzub4ak4op%2Bx%2FY1AmImtl%2FobyN8pTq%2FbHKk%2BRo3j4aKbmnWMSv%2BX27JErAf2mjDiK%2F377Td4e90TRep%2BqQ5NQhid%2BqllehprunCBUCmuDCXANKrER44TzG%2BgB%2FybsCh9S5vxtHeTdlvkj4Nf9wtLmS3Hiv63dDX1loxo8C%2BANonT%2F2FDZjg8x6C4MPUiV5q0qnTM9XB1nz%2BZtpFPF%2Bg8HffQipVfOzOrTbRLSMe5GuRk52vTvs2KQRLrCBNOjVSsXU9Hs10ROSUOuCZzKK0CYkOZSklil12sX7Yv7yBZ6uTnnLVaO5ed%2BaanIH9%2BqCNJf4uWkP87I7r5a%2FZMJro5bwGOqUBi8%2Fj%2BOKcOGJEIIst8qbczoK8AV%2FVT8fGizwBGb4Ticl76k%2FdjzRx2A9bMbBGosgrnQsc9J5kn09v4bWLNbwKrp5607YtK9UbWiWO8o5EEjXSGAdgf7jQSxWr31Xp4mDmjdHJzAXR0zL3wCqhSkDbPddcBPH0G%2B6ctDVQuN5FgdhCjb523CugKSn3Wr2ZrV7i8A6sDIc7Q7nf%2FddKT%2BUDmT8NMG8t&X-Amz-Signature=fe641c071f45c38a8402ec75db969be9835e4e0e3435b8fa1ca8713107b820fe&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Algorithmic Libraries
#### 1. **Scikit-learn**
- **Description:** Contains tools for statistical modeling, including regression, classification, clustering, etc.
- **Built on:** NumPy, SciPy, and Matplotlib.
#### 2. **Statsmodels**
- **Description:** A module for exploring data, estimating statistical models, and performing statistical tests.

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c62885f5-417d-4179-834f-d68f8f2bdf39/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZYMUMIHK%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T010809Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHkaCXVzLXdlc3QtMiJHMEUCIERYDGPHi%2FErIhuZJ2TuTK47lK3LE0X5my%2FD9DdV6JyXAiEA7e14HzDhWVGnv1e3UnhZMYEnM9MKA1ZZaOKfldhRb90qiAQIgf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDBngyAoWAyHpupQ8QyrcAw5vIn1FUZMcQVDMY24NvbHowffLq%2FLHpaMS%2BPJ2cJM1nNu0OAC%2BDuPmDVHrLnx9GNTqKoXXP%2BT%2BSJkUglOHtXtLbjmeqC0SIhPQk%2Brt3bTl7zqu8xN3sRSDKs27i1mE7BycW7bfEUCbmKeACkHyAzOux%2FGpFt41aM7Iwp%2B%2Bp4%2FIP67wZJL0Dmu4IJ1hYnDGTDHk%2FCBI5nWdMKO2tSwHSztR%2BNNPnw7DgWipbmj%2FljLNqUntnk3NxQ%2BRq1DnHukEMW3h8xe4lFYuVMvVQGZ5p0JROzWYRh6WvrjHJnLLITDOnEzub4ak4op%2Bx%2FY1AmImtl%2FobyN8pTq%2FbHKk%2BRo3j4aKbmnWMSv%2BX27JErAf2mjDiK%2F377Td4e90TRep%2BqQ5NQhid%2BqllehprunCBUCmuDCXANKrER44TzG%2BgB%2FybsCh9S5vxtHeTdlvkj4Nf9wtLmS3Hiv63dDX1loxo8C%2BANonT%2F2FDZjg8x6C4MPUiV5q0qnTM9XB1nz%2BZtpFPF%2Bg8HffQipVfOzOrTbRLSMe5GuRk52vTvs2KQRLrCBNOjVSsXU9Hs10ROSUOuCZzKK0CYkOZSklil12sX7Yv7yBZ6uTnnLVaO5ed%2BaanIH9%2BqCNJf4uWkP87I7r5a%2FZMJro5bwGOqUBi8%2Fj%2BOKcOGJEIIst8qbczoK8AV%2FVT8fGizwBGb4Ticl76k%2FdjzRx2A9bMbBGosgrnQsc9J5kn09v4bWLNbwKrp5607YtK9UbWiWO8o5EEjXSGAdgf7jQSxWr31Xp4mDmjdHJzAXR0zL3wCqhSkDbPddcBPH0G%2B6ctDVQuN5FgdhCjb523CugKSn3Wr2ZrV7i8A6sDIc7Q7nf%2FddKT%2BUDmT8NMG8t&X-Amz-Signature=4796f5ab725d3d44920326bf1c126aee60803868dba6553ce2dff73fc970d06a&X-Amz-SignedHeaders=host&x-id=GetObject)
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
