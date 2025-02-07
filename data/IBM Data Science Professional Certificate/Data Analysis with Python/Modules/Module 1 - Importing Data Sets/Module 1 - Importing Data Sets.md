

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

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/997ac361-58a8-4f04-bb0f-79fea4baa761/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466X6ICQA5W%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T221336Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGYaCXVzLXdlc3QtMiJGMEQCIEAn55IxP1SX7%2BBfE3ei8J4q5Cxe1TDMj6CLsMuKZ%2BCQAiBfvnRehsbtX0tXGMAfjmyD0ckL2ApjFN7OBIaQoTH%2Fzir%2FAwh%2FEAAaDDYzNzQyMzE4MzgwNSIMOUosgIR0d%2Bt7Q5NzKtwDOmcfHqs4bEeo1y%2BZajMUJd9LeRj73Y1%2FIgW0OzahSS8dAb7Ub8wj1mxQQjJ9TeBQOS0lCzVTeqnptfpaF1ll1GzwxtW9c%2B1jckoGbDsSO%2FJ0l5jHjHUBAbDtx5MajmNXeu0P4qMX5U5pxfmij8bYj6eBJw6ahvzEgIN1dfx5QQUWXHd7U1KI%2F3M1Y13VeszQE441hr%2FKhnd5dUA%2Bqyirz2aWea5wZ4fPcDUx3h7QPkBd43sUY1iCmFORrYt1S5KYLz6WU4p1DmcskM4CrQi2tzxFCPwBQGu9fYw1t6qcFyWksFqk0FimL7X5yqfeSjRC4qSl10erQbnDXmPzf8RTA6wOaAzBKipGpG%2F58u6%2FeuoySkDPFqXfFYuQrOzRDh3U0WiY4Fd29UmYku13amLKKBHR8qPw19qh90xqnvzTpzrUBP70skmdBoLhkdLV2vQ%2BJLcO%2B77jChKKnPk2FQ56XOUjzgEzd28Ax4NxY7nMSOrSKwyofxQYdpgAI9uC37EJf3l%2BY5zbnoyNRr%2FFYdT4yPotA55e6mY%2BOP%2FDAooRO3MSWwJeRBtMCbPe8%2B%2B46npK95T93A5v%2FApbUQA6SyNBUPm9L1QMC%2BxIyQgP6qZNqM5bwnUgUVqlITsPXpMw3P6ZvQY6pgHKL2xvwi0kTN3f9eFRn%2BoWpa3L97QMf9dr2suVEOYTfog8F%2FwWMsblFe2JUsI8a0JKxL3PefigDQeDtutTxJFRFRFd5fNhOSgEIV7%2F72Khz%2FOkZTSiPuA25fsc7IyeW8K%2B%2BpfBqdD9zJlBtj%2B8fb4WpyodOebYjYJcGSjP07NxM0aYMIwXeGx55UOn3vu53%2Bk9ZMnnelsp7RKyHsEfVcyaQnU6EtRb&X-Amz-Signature=771b61ea1b5e02e56bd2f86c6370587134bf46f57d0bf14813728ad876c26d6a&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Data Visualization Libraries
#### 1. **Matplotlib**
- **Description:** The most well-known library for data visualization.
- **Features:** Great for making highly customizable graphs and plots.
#### 2. **Seaborn**
- **Description:** A high-level visualization library based on Matplotlib.
- **Features:** Easy to generate various plots like heat maps, time series, and violin plots.

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/733d1e42-5a53-4fd8-90c1-3d85254369a6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662TZBZLUN%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T221335Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGYaCXVzLXdlc3QtMiJIMEYCIQDx2U2K9kRN%2FoFgXTzjqDNVjEl%2BEEhcdJfZDJ4wTkn9eQIhAM4T9ocMJgo35SUXm0v%2FSoGibdxb3B%2FWqehDyyn2peemKv8DCH8QABoMNjM3NDIzMTgzODA1Igz9WOkh553vNrFlXJYq3AO23XpGxhoiHME7J21%2BFEZE8pjYWex3KjsXw04PAesVAnA40SuOht8%2B1QIGpHig1SMD34Yv%2B3ED%2BZrmJ0NybMnff9%2F6rXXZjCzLiVdR%2BJh2mPQx0bm8vFNFtpTI2tVOef6TqyiEwesgPHvinm2y%2FBPjap%2B8lKMuNYS3zk31QgkV9uZ5v3hgf8BPfXNkqQr72IIMf9DjfwPZNVt7nRSqrjJPkThLusuU%2FH4zVS8Js8%2BsNgd9FW1pztt%2Bcmrq4789aJZeTIxhIP3vjW%2B2hRcEP2WcgNrnt%2FsjCk8ZaxSXFaXKVaLOvRSmwUK7NRjm97Gp2xUgStCRrsZEPobj1EhhxV7nmc3j5Rrov5TwliA%2FT3TAikNlITS4igPyUXTR%2FCnMzXrjHMkwkx7s1OAmmU3yMUJ34eqRiP7GTT2gTaJlV8mPRIiNSS1sZm09kJbnC8ssnytC6hnp0dBaMmnmlORWrzRgxzcx%2BXJfOg3MxR7zDcOIqvAUkCH%2BP1iL4UoCGwaKaA4o161Aj9rXJNEitdy%2F6dAMWbc%2Bbbnn41VfOcGRw0r2377Fxls9segyMruNdM%2BB1p59uq7fT60KXM35PvZ1yT3TO2asez3ND9AUFu6W%2BilSHGV725m4lSeVVLSJSjC5%2Fpm9BjqkAaCsvsfV5n%2BhNT5oT3MFdjiGfJxtelLitkB8V8JkbWOcenHBnBMd%2F8cLHnoNCIoVd7WbPbOQFMYnhFMYeRsbQtQL9fjjQaPqXx7Xi4F6Sj7w5Z%2BeC5vDW8uswn4%2FhI6wTdQ%2Bhd6yHrLjWBuG6D%2Bg%2FlUZo3Uog4%2BtWrt0aKQkBVqjAA87sl1l3LnS%2FoMyXqr%2Fa8K%2FR7OMUnyyZVQ4lw9X7GzicrEv&X-Amz-Signature=183d0d9dd00c79291574135e5ea16a61b57b0d4354d9511dd367e404f451d579&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Algorithmic Libraries
#### 1. **Scikit-learn**
- **Description:** Contains tools for statistical modeling, including regression, classification, clustering, etc.
- **Built on:** NumPy, SciPy, and Matplotlib.
#### 2. **Statsmodels**
- **Description:** A module for exploring data, estimating statistical models, and performing statistical tests.

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c62885f5-417d-4179-834f-d68f8f2bdf39/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662TZBZLUN%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T221335Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGYaCXVzLXdlc3QtMiJIMEYCIQDx2U2K9kRN%2FoFgXTzjqDNVjEl%2BEEhcdJfZDJ4wTkn9eQIhAM4T9ocMJgo35SUXm0v%2FSoGibdxb3B%2FWqehDyyn2peemKv8DCH8QABoMNjM3NDIzMTgzODA1Igz9WOkh553vNrFlXJYq3AO23XpGxhoiHME7J21%2BFEZE8pjYWex3KjsXw04PAesVAnA40SuOht8%2B1QIGpHig1SMD34Yv%2B3ED%2BZrmJ0NybMnff9%2F6rXXZjCzLiVdR%2BJh2mPQx0bm8vFNFtpTI2tVOef6TqyiEwesgPHvinm2y%2FBPjap%2B8lKMuNYS3zk31QgkV9uZ5v3hgf8BPfXNkqQr72IIMf9DjfwPZNVt7nRSqrjJPkThLusuU%2FH4zVS8Js8%2BsNgd9FW1pztt%2Bcmrq4789aJZeTIxhIP3vjW%2B2hRcEP2WcgNrnt%2FsjCk8ZaxSXFaXKVaLOvRSmwUK7NRjm97Gp2xUgStCRrsZEPobj1EhhxV7nmc3j5Rrov5TwliA%2FT3TAikNlITS4igPyUXTR%2FCnMzXrjHMkwkx7s1OAmmU3yMUJ34eqRiP7GTT2gTaJlV8mPRIiNSS1sZm09kJbnC8ssnytC6hnp0dBaMmnmlORWrzRgxzcx%2BXJfOg3MxR7zDcOIqvAUkCH%2BP1iL4UoCGwaKaA4o161Aj9rXJNEitdy%2F6dAMWbc%2Bbbnn41VfOcGRw0r2377Fxls9segyMruNdM%2BB1p59uq7fT60KXM35PvZ1yT3TO2asez3ND9AUFu6W%2BilSHGV725m4lSeVVLSJSjC5%2Fpm9BjqkAaCsvsfV5n%2BhNT5oT3MFdjiGfJxtelLitkB8V8JkbWOcenHBnBMd%2F8cLHnoNCIoVd7WbPbOQFMYnhFMYeRsbQtQL9fjjQaPqXx7Xi4F6Sj7w5Z%2BeC5vDW8uswn4%2FhI6wTdQ%2Bhd6yHrLjWBuG6D%2Bg%2FlUZo3Uog4%2BtWrt0aKQkBVqjAA87sl1l3LnS%2FoMyXqr%2Fa8K%2FR7OMUnyyZVQ4lw9X7GzicrEv&X-Amz-Signature=61fddf682864451f78741cc06fff3bee73040f5620cb9e52ffcf04ff89ea26a2&X-Amz-SignedHeaders=host&x-id=GetObject)
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
