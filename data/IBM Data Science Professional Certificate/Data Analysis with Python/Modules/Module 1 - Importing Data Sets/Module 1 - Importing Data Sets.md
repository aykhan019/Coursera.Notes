

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

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/997ac361-58a8-4f04-bb0f-79fea4baa761/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QN3DGNKP%2F20250330%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250330T004513Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBcaCXVzLXdlc3QtMiJHMEUCIAEUXBXC76WWVmF7YorjCDNydeSo6l3hLJUz7uYMYq2vAiEA7mNIO4NuJe5JpaTmFimqkcaKD3uPezOfpWBgPEjBRb0qiAQIgP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJEB4chEyMqws7fYOSrcA3pCPqmzBTu0B5DB63y7CBT5wBYx%2BwARDUtId83nMuQT5DezkPXrIgnI3j5%2B8HPE3ddyo2Ate15uEcbCUlH6uOdubI2aCoD%2F1B5%2FaHhzRxEoJ6tOJ3H1suowsFdtdlqP8NDu8PaSYqLE2ubYI1urn00s7twUKXXYu64mQCeinbZ%2BS65F%2Fo%2Fl2NXLBN3pWS9kJYnUHNiDTQOpVH0%2BCxzmuRYqljc%2FrnPfWnRhwEcNAmyuxGNd9i7jn49Kef9UBuepUmhkf6TVw6O3nU53RuSNP6%2B8OM535inkqN5GMb82MEOeuuOdGoEWU4rPPAgKHI7wvee95WQTMht35UORhHJNDAN4vclT8rjspVO6UxLh%2FzQEAksqJaDJq%2FIdhLTw13Y3rTyqFQT9LX5Yh%2F1IkMtjDMTAXs9AYeLkGduNaOkIPwg4bD%2FB3QFJ%2Bd0RdQKs6bMX1V5vVEfYQ0Fui3NhhXHGa%2FfjMD1zGHZTSSJW3AO%2BIK6IpnLEKEkLMryHMwyafWnW7tDM6fYRt%2BC%2F3zEtuyT4FDXWkGPsWfikNWxuiSfYO6bdYulns9bIPidrQTBZoN5DwT6DM7ceEZ8Cu9lidzkivuFYyOIywFofErJeqvR9cAhf79yUQmKgqMU3s2bYMNH8ob8GOqUBNEq7BLax%2BE9qus6EkeQFGZUr1h9V32cYED8i0qVbjEqeO%2B4bfc0bes8Z%2BGA5pA1x6X%2B3nrJrT5GfpibHn7k9WMDkKSbEelqMhV2LJbvAejRNGP7i0sFq%2BTrjfjKjATSfnywk2%2BwEDX7i0hiPLNoAKPI2ibJnCAklZo6t4JjMjog4kkHUMSoXZ3IjvYdBp0v%2FeuqiOJfMdskd0%2BYs23qPPX3eUxRB&X-Amz-Signature=8e7ae9dfc32080930c460938e5768ba7df64279599b1d63601c277138cae169b&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Data Visualization Libraries
#### 1. **Matplotlib**
- **Description:** The most well-known library for data visualization.
- **Features:** Great for making highly customizable graphs and plots.
#### 2. **Seaborn**
- **Description:** A high-level visualization library based on Matplotlib.
- **Features:** Easy to generate various plots like heat maps, time series, and violin plots.

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/733d1e42-5a53-4fd8-90c1-3d85254369a6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QT33LXE4%2F20250330%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250330T004511Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBgaCXVzLXdlc3QtMiJGMEQCIDmwXsii2YKtGbrIzBBPHyn%2FHA0ryDWe5lYj8izMeqP5AiAJKViuAv0IqJDxctwpaCGq%2BU%2BSMYJyG9czIpEvUAfIoCqIBAiB%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMJWLxSrB7yqaKTAT%2FKtwDK%2BQ7Ev6y7Hiy2hW3a3IndkS9tkMMh%2F0LEqrdImgKtkwJrFoh1Wj0FJ5rsY1rggc7GqnPy%2BubnLobE1dSkiRKmEXm64fG9pNNEO4QcRUkMH4%2BfehdQT9aGxuuv4F%2FnBc6s4clxwoDJTIDGA%2FdODNlU%2B9ULFj%2F3kbhME5nTSaP1RUj7WDkx%2B25oHB9f9rAbIGCf8xFk6zR0zYmPMKP7kW3UyqfLnbydkjaFik36zdsb2b%2Bl153M2nXcZvUYOKreyG5T1TJ6IHe6aoqlHlY68AJmE12v7ekTWPlZo0JL5NISIcAhkz70o63c%2FTF5V3LUYHe2HQbY1GwmlF2%2BdAyGL5%2B1z2dNnVWOOaqENH9bhguJIxhYcmH%2BNmQT8U%2B7QgyVe61OIvObtqNByZ2Zg6sr0N9jOXSBzkqNGt8seUQBwdAc8QuTNhGBcxLy5Ra8N1W7sXLH10ljXg5SpBp2Kgb3nCyRw6g6sW0B57F%2FpqMmtmavxK269aJTFutupXwzmXbAptkXpZOl7j6ykKaZBmP0V%2BdDYhLqca5SLH1IsI5%2BeP7sy%2BRlfW1yXHllECM%2BmoegDB4rJthjUI5pgjvcCa5%2FyTN1awM39rWIAWNAgCCFtlBLKDBHrNp%2FxPAL%2BRAsV4wk5WivwY6pgHA1kkc12PyexyA5AnmXyhXAyTrZ2%2Fe4YM1DUsRoAdxjX60VaYe2soEXBIEZ%2B5J%2BGTg3Z1FXVB3Gi%2BxL7jK48X%2BzFiyTGdr8Ju2HJ9nEFszcUmGb7zitghcPkDSgzB660KYMBzg0nV%2B4O5itxki9lfAjTaDeweDZOGQnIyhMjw7HafRATRuRa0KYYdORzkuy4KEzGME0kRBK19QSBSru%2FkoqujdKY8L&X-Amz-Signature=1bfe55b17a648fdee3c2b77184e5a57ea03ca628a8a45cc494b8aefe16a9b1f4&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Algorithmic Libraries
#### 1. **Scikit-learn**
- **Description:** Contains tools for statistical modeling, including regression, classification, clustering, etc.
- **Built on:** NumPy, SciPy, and Matplotlib.
#### 2. **Statsmodels**
- **Description:** A module for exploring data, estimating statistical models, and performing statistical tests.

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c62885f5-417d-4179-834f-d68f8f2bdf39/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QT33LXE4%2F20250330%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250330T004511Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBgaCXVzLXdlc3QtMiJGMEQCIDmwXsii2YKtGbrIzBBPHyn%2FHA0ryDWe5lYj8izMeqP5AiAJKViuAv0IqJDxctwpaCGq%2BU%2BSMYJyG9czIpEvUAfIoCqIBAiB%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMJWLxSrB7yqaKTAT%2FKtwDK%2BQ7Ev6y7Hiy2hW3a3IndkS9tkMMh%2F0LEqrdImgKtkwJrFoh1Wj0FJ5rsY1rggc7GqnPy%2BubnLobE1dSkiRKmEXm64fG9pNNEO4QcRUkMH4%2BfehdQT9aGxuuv4F%2FnBc6s4clxwoDJTIDGA%2FdODNlU%2B9ULFj%2F3kbhME5nTSaP1RUj7WDkx%2B25oHB9f9rAbIGCf8xFk6zR0zYmPMKP7kW3UyqfLnbydkjaFik36zdsb2b%2Bl153M2nXcZvUYOKreyG5T1TJ6IHe6aoqlHlY68AJmE12v7ekTWPlZo0JL5NISIcAhkz70o63c%2FTF5V3LUYHe2HQbY1GwmlF2%2BdAyGL5%2B1z2dNnVWOOaqENH9bhguJIxhYcmH%2BNmQT8U%2B7QgyVe61OIvObtqNByZ2Zg6sr0N9jOXSBzkqNGt8seUQBwdAc8QuTNhGBcxLy5Ra8N1W7sXLH10ljXg5SpBp2Kgb3nCyRw6g6sW0B57F%2FpqMmtmavxK269aJTFutupXwzmXbAptkXpZOl7j6ykKaZBmP0V%2BdDYhLqca5SLH1IsI5%2BeP7sy%2BRlfW1yXHllECM%2BmoegDB4rJthjUI5pgjvcCa5%2FyTN1awM39rWIAWNAgCCFtlBLKDBHrNp%2FxPAL%2BRAsV4wk5WivwY6pgHA1kkc12PyexyA5AnmXyhXAyTrZ2%2Fe4YM1DUsRoAdxjX60VaYe2soEXBIEZ%2B5J%2BGTg3Z1FXVB3Gi%2BxL7jK48X%2BzFiyTGdr8Ju2HJ9nEFszcUmGb7zitghcPkDSgzB660KYMBzg0nV%2B4O5itxki9lfAjTaDeweDZOGQnIyhMjw7HafRATRuRa0KYYdORzkuy4KEzGME0kRBK19QSBSru%2FkoqujdKY8L&X-Amz-Signature=ce3e223e53e10643e6ebe79f74141a43caae2ef056b6848918d593659b771ea6&X-Amz-SignedHeaders=host&x-id=GetObject)
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
