

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

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/997ac361-58a8-4f04-bb0f-79fea4baa761/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XMNDQ4KG%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T081717Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHSZONbPArL3%2Fq%2Byv82jU%2FHqsseANKMly0nJCFdx6Wd6AiBgI7poLQl%2FwN7Aeox1%2B9RqF4Xh1QRxZPAhegq72U5elCqIBAjR%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMsGhY7wS7qnoEIzJXKtwDCe7Gi2WyUC33U99gHYTCenZiFpWG%2BtbAXc7syhgvb%2FHrR8cI04AclWaHq%2BNkFWBtQg3YzByctTM6QKrILlGCkXabYK%2Bfxj8hyjb3%2FPc806J3gTxbmvczcrHzT0PKsX8v4MOS31BUOyPLvEeW3%2FaEBhawgp6UQ5Mg5EoUgLbSSy89CGSXg4TRc7Okcn2spvSSUx1AyynFr6DImtZ%2B18iRIBbPXdVROcvAjw3BIiv4bE2FjIkQZ1pKZeCKkuPrDdU7okPw2dJrI%2Ft44E5lixyb7aq971s7GNkv6dWAKUrHlOxOtPgSaeI7DDbpFRQDHQ3sgrg%2BPwrgBEjwcKXWF0%2F5QdidfTtxUSopoA%2Bu3UG3AQBySEPSsJvQaO0puGzmaQ3XH87i0Vcil61BOewsyviOugJNnCHVJUuIcW1HBP96WwaFKbNjbCzDFM4Uv1FWJtaWKXZXvt1b2i9SVKSfaFK5niFDYKg8kj8uFl7OWdXIq4YLBllQ8Z1Ok8aUtJrXZ8rh0gbIkcMTkGyJrXuBIOo169cuH7L4O8mTCxmLy4ITGI90HsxZ9tjYpiC0gxXFyJdyF%2Bglfcr2uqozISjM%2FD7b%2BxJxQrss59Eztd8Qq7XawpXVPjpIOP0TmF2gtlMwvqT3vAY6pgF8bFAbwzLJOnipa8RoSQidCT0PxuRDZpnA64MZZapBHjrvHnBUAMIbuPdj06X5Jc5eNu3HXd5E2gdX8imOMUnQhKHJ9qAGp70kBGj3k85WAGsTeFxkTLQ9jQaW9qm4hc2oE5nqgUs8HKObs%2BUY5ffphy5nBOgP8UnICLwYlVFTEEWYoq0FE0fkAe7CJVoCEPsWJF0ONIMiGaVsmautOkSwciHPvYMe&X-Amz-Signature=3f9b5873ea6b1fbbfcf142b34e4509c7d58501cd4300f02a77b1fe5ca7024014&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Data Visualization Libraries
#### 1. **Matplotlib**
- **Description:** The most well-known library for data visualization.
- **Features:** Great for making highly customizable graphs and plots.
#### 2. **Seaborn**
- **Description:** A high-level visualization library based on Matplotlib.
- **Features:** Easy to generate various plots like heat maps, time series, and violin plots.

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/733d1e42-5a53-4fd8-90c1-3d85254369a6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46663DLKTG6%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T081716Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQD3Kj4DL5Ix7SMIF%2BI0sSuyMIw%2B019NeuPVJF%2BQOjj7oQIhAIfGvGms1WFPXRx7uvfyfV2EfKwOC%2BuZL33eKlxJ3rvdKogECNH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzUBiaDGwdgoFjCgKUq3ANmCLHoZcEp0ZtLwg4nAGYOoZGgYB9Jn3EBZlt4IiQsX0ybSFxctFfN%2BClIgYUfkeQVXCohqlPYkJ%2B2l0owCHHVHxjVEvwpfcHKSEM9v6zuYru6eVWMfv%2BOrNcTrAA0oWvaFMiPr0OnpZuEqmRBglLSuwmKAWcjQ6zVMySSoHDokDOgm7m0jRkIyRpTlffJMScmR76lYHMm0k21dpCgxPy%2BYFC4IChqewqoWbSYHqD9xlFghZgfOiQIqlShESeZKwRm%2F8QVZweWk%2Bqu2xzv2s2faQaqVpya7sqXDpQpvcmB0InNyVkLJRDPfDKmP2DLyJy66v3fWB%2BR2FwilWKtBqtJvk4QOrIbKYB%2BeeM%2B5S2L21Qa7ifgDEGdaQ9E9MfrD2DCw%2BpV7DDjzQS%2BfNWB7waRktLPGEoDINUceYz%2FdSH2EHaCraFrE9zHEnUQuWJXwnlYTaPkEkJj2O3II0JoqYq9yHLSTuFhvvuJVy68Wi38auQzIXc0rVZG83p8m21PZV51kqu36uNlwvJm3VIF6f9rbVuKqKixSoxv2JoVy7fIfmqJPdjgkjCSpOuvicO9E1jIAHtZaLnAYTtL5t2PMcCHhwbsgKcrr7PQqLV515GgTmwbbipBdQQ4RGHW%2FDDSpPe8BjqkAbZ9PBkagsJHLuVcqLkFEx4wMMXtVN5OQdnd7DqOJuMsTXHMqXgbP1XSYomj1OOSDC3hrUcOnYxuJNbxfSdiNTgswhyE7vgaQ1Ed3USi3AUT4I8S8ut7Qm6vfQEjecUhSyYtcIw6RbOHidZ4tRUJP5DN%2FGk8bacNScfMOSLxRB5YYHUMmuMnQdKr49EOVh5pTnEFQxfB%2BBPvEJWzrCbTtreBirTX&X-Amz-Signature=f256b59ceb737e9bde56bda9241496543c09d1597ef12427e667626187b4d7a9&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Algorithmic Libraries
#### 1. **Scikit-learn**
- **Description:** Contains tools for statistical modeling, including regression, classification, clustering, etc.
- **Built on:** NumPy, SciPy, and Matplotlib.
#### 2. **Statsmodels**
- **Description:** A module for exploring data, estimating statistical models, and performing statistical tests.

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c62885f5-417d-4179-834f-d68f8f2bdf39/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46663DLKTG6%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T081716Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQD3Kj4DL5Ix7SMIF%2BI0sSuyMIw%2B019NeuPVJF%2BQOjj7oQIhAIfGvGms1WFPXRx7uvfyfV2EfKwOC%2BuZL33eKlxJ3rvdKogECNH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzUBiaDGwdgoFjCgKUq3ANmCLHoZcEp0ZtLwg4nAGYOoZGgYB9Jn3EBZlt4IiQsX0ybSFxctFfN%2BClIgYUfkeQVXCohqlPYkJ%2B2l0owCHHVHxjVEvwpfcHKSEM9v6zuYru6eVWMfv%2BOrNcTrAA0oWvaFMiPr0OnpZuEqmRBglLSuwmKAWcjQ6zVMySSoHDokDOgm7m0jRkIyRpTlffJMScmR76lYHMm0k21dpCgxPy%2BYFC4IChqewqoWbSYHqD9xlFghZgfOiQIqlShESeZKwRm%2F8QVZweWk%2Bqu2xzv2s2faQaqVpya7sqXDpQpvcmB0InNyVkLJRDPfDKmP2DLyJy66v3fWB%2BR2FwilWKtBqtJvk4QOrIbKYB%2BeeM%2B5S2L21Qa7ifgDEGdaQ9E9MfrD2DCw%2BpV7DDjzQS%2BfNWB7waRktLPGEoDINUceYz%2FdSH2EHaCraFrE9zHEnUQuWJXwnlYTaPkEkJj2O3II0JoqYq9yHLSTuFhvvuJVy68Wi38auQzIXc0rVZG83p8m21PZV51kqu36uNlwvJm3VIF6f9rbVuKqKixSoxv2JoVy7fIfmqJPdjgkjCSpOuvicO9E1jIAHtZaLnAYTtL5t2PMcCHhwbsgKcrr7PQqLV515GgTmwbbipBdQQ4RGHW%2FDDSpPe8BjqkAbZ9PBkagsJHLuVcqLkFEx4wMMXtVN5OQdnd7DqOJuMsTXHMqXgbP1XSYomj1OOSDC3hrUcOnYxuJNbxfSdiNTgswhyE7vgaQ1Ed3USi3AUT4I8S8ut7Qm6vfQEjecUhSyYtcIw6RbOHidZ4tRUJP5DN%2FGk8bacNScfMOSLxRB5YYHUMmuMnQdKr49EOVh5pTnEFQxfB%2BBPvEJWzrCbTtreBirTX&X-Amz-Signature=f2502ba65a9f81e20b97116934d85397472aa719987b039e1f3ea21119b7dce6&X-Amz-SignedHeaders=host&x-id=GetObject)
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
