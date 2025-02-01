

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

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/997ac361-58a8-4f04-bb0f-79fea4baa761/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RISGODFT%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T024458Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEML%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBHaL3C6YkutYwjAuN5aXIpLFygBU%2FZJ8kCHuxNHYlwsAiAEHsaM6Q%2BT10Y9lteWYGlFQfWg0sKS%2FcClvciZKltaxiqIBAjK%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMkYvhazF6zKMh9aUqKtwD2wje0u%2BoqOc7qjl%2BWzXJO8p7Hn9Kz0h8QOTS30RBYXaO%2F%2FeKmkazWVAx0Kkk5DzfwqEwzHK4kYTyZSTKDxKUsJUex0m10H6DvgDMavewz4xxfTMlUtEV76ahLEUfRmZao1Xt9A37z6f4RYFlc4L3ce9PWdaRadHKYmXF5yPBph%2Bj62gJhBhu7wgJO1ggkJN4Kxc9lwMiheCL8SlnrX0rfsRbI7Ynq9nLagQcNWWqmVPt3C359I4aYLq7vStmKzbmPCki9zjdOFSC%2FGOXFJSnQaOJV3bF9%2BSKl%2B68hfGw8FzbRKWwGhG2o6AUs7wvRlRrl6dzag2YhJ2gE5K8IgvgAPm1lCsDHcyvrR2RMqC%2FIYZ09ZGLKER7GZ4jLs%2BXrgqNNSJ%2FJr77kaJfjjPKAtm6xyEBrv3Kf51RrUUJvxygETA1gXHCgiIZHK%2BpoM1qGW%2BVasadlLFD9pPPOxocobNICxhc5ppjQ5WB4mmZiOkHK%2BkGz2BAIqEi6rk2SoNAUIaSwJ%2Fm91ss0%2BibI0El4gZRbMk7o2aG9lOsQvS0grfG%2Fdo8jZJvanuT24IUQIT4kkBUeGV9boAnXzTH5LIurpkKfMW%2F%2B%2FnyQG90%2BRda8jntAeMGLWR%2BWPaHVXqGUHEw3Oz1vAY6pgGy2cInuK13RBSgt1cAMBI4WQlJ6HQNsPDjOcOuMY%2F8%2B%2FMvcuNxUFu0sL1i9rMdHKC%2F6sRWU99%2FtE0w5FWmOB1gidpJu8vVMtx5XsXjCecYhQRNXLrveq%2FY9MxQTUKks8oHzB9kUjHYe2IALXIsXAkMIZ3GmySZuwZ1uXOgGmlbnU56ORsaJ1ap061Uf2132YQLTlzCzXthNai8kFyXSO%2FI0JDffktP&X-Amz-Signature=dc1e2a17065c40365bd0c5efafc53c9e2c78af8240e3be51bc91ea822962e9f6&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Data Visualization Libraries
#### 1. **Matplotlib**
- **Description:** The most well-known library for data visualization.
- **Features:** Great for making highly customizable graphs and plots.
#### 2. **Seaborn**
- **Description:** A high-level visualization library based on Matplotlib.
- **Features:** Easy to generate various plots like heat maps, time series, and violin plots.

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/733d1e42-5a53-4fd8-90c1-3d85254369a6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YNUX6Q5J%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T024457Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEML%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFF0IvSirAjGBzGwQ0JUdjYFwpY%2F2dlRU33JL1q2KOvRAiA0JbSjxlmHfF8XI17x1aOUHVF691vQqhPow9m%2B7gHmlCqIBAjK%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMod1Ii1EW6bu28hmvKtwDxhWMJPR5z59F6fOZ%2FlvxmDJzaAc%2F5XfcSWmTNN3NblDcBhgyL9kkV%2FPRxYp0j5ksRHxzYOMaUof3SFJZk25mhnr%2FeGTPaFN1QbNyApWhWWO3ljoLyGGFsA1G04LASzFMQItOGFIS%2FDDGg8wyhuBrexUyf7wC2STwKXgqjDR9dpcupZERpPStb2PN59OXNwt3GkY7iVmrirxffusmuIuaIuJK4occop%2FRnfEMLTFR6N2PMZtCSK1VthcOD15PTphmP2lMzHAV7nIq6NyUtZ8INZiDL7j3xTj8lIva1Ea16DN0U850eUGBcgTJVosmnjqmz7268ltF%2BDH075yhnkpFHNWdeZ2ndTi4ymk1X2ZlbhSjZDAeA0m6V4PjQa%2BhvFna%2FRyiM8hRqoJ%2FTBZXThJ0Gr5K6nk%2BKUY7zmFYToqBEFoUAuq1x0tFIDXA3fABdXjJUklQusGK2nEB09k%2BycBspbMytflzR%2FFBWK26bgfBQAufBfERcN870m9sQvEElACj%2FaBZMmKTRRzC5WFVxGlIDUCPNtHTRGpanBNeo%2FtG0xdDM1S8YrWdmrSvXGKazrg9CTiW%2FWsvf9yWwGIAGqAzM5AhTIUpfQMlJve7H7S3pzmJffLjOl6QUp%2FSf3Qwxez1vAY6pgEh3SMl1UdC83%2FpvjtX1g54DRjAUmxGoNynuZY3S%2FOwScRTn3HYh9BiRguxoMJInu%2BPB7bjoDAUkFtP1vaUQ7nChg4CCR9oZsTEBqQIIddI7tvFgAqwmtCqCI7BI0xZQxNXqgb7MNfRZVBVLGtc%2FS1E9OHTS7sO3S1733Yu3TcQKrpwjddaOYd8%2FfA6KPpE6omjoJ6jTlg1jDhernvg%2F7c5CPHqgsMd&X-Amz-Signature=e923b4e8f074e618c6ebf00f1fa47e958aa6fa84a1ec8efbbf6053bfe0b1f71c&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Algorithmic Libraries
#### 1. **Scikit-learn**
- **Description:** Contains tools for statistical modeling, including regression, classification, clustering, etc.
- **Built on:** NumPy, SciPy, and Matplotlib.
#### 2. **Statsmodels**
- **Description:** A module for exploring data, estimating statistical models, and performing statistical tests.

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c62885f5-417d-4179-834f-d68f8f2bdf39/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YNUX6Q5J%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T024457Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEML%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFF0IvSirAjGBzGwQ0JUdjYFwpY%2F2dlRU33JL1q2KOvRAiA0JbSjxlmHfF8XI17x1aOUHVF691vQqhPow9m%2B7gHmlCqIBAjK%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMod1Ii1EW6bu28hmvKtwDxhWMJPR5z59F6fOZ%2FlvxmDJzaAc%2F5XfcSWmTNN3NblDcBhgyL9kkV%2FPRxYp0j5ksRHxzYOMaUof3SFJZk25mhnr%2FeGTPaFN1QbNyApWhWWO3ljoLyGGFsA1G04LASzFMQItOGFIS%2FDDGg8wyhuBrexUyf7wC2STwKXgqjDR9dpcupZERpPStb2PN59OXNwt3GkY7iVmrirxffusmuIuaIuJK4occop%2FRnfEMLTFR6N2PMZtCSK1VthcOD15PTphmP2lMzHAV7nIq6NyUtZ8INZiDL7j3xTj8lIva1Ea16DN0U850eUGBcgTJVosmnjqmz7268ltF%2BDH075yhnkpFHNWdeZ2ndTi4ymk1X2ZlbhSjZDAeA0m6V4PjQa%2BhvFna%2FRyiM8hRqoJ%2FTBZXThJ0Gr5K6nk%2BKUY7zmFYToqBEFoUAuq1x0tFIDXA3fABdXjJUklQusGK2nEB09k%2BycBspbMytflzR%2FFBWK26bgfBQAufBfERcN870m9sQvEElACj%2FaBZMmKTRRzC5WFVxGlIDUCPNtHTRGpanBNeo%2FtG0xdDM1S8YrWdmrSvXGKazrg9CTiW%2FWsvf9yWwGIAGqAzM5AhTIUpfQMlJve7H7S3pzmJffLjOl6QUp%2FSf3Qwxez1vAY6pgEh3SMl1UdC83%2FpvjtX1g54DRjAUmxGoNynuZY3S%2FOwScRTn3HYh9BiRguxoMJInu%2BPB7bjoDAUkFtP1vaUQ7nChg4CCR9oZsTEBqQIIddI7tvFgAqwmtCqCI7BI0xZQxNXqgb7MNfRZVBVLGtc%2FS1E9OHTS7sO3S1733Yu3TcQKrpwjddaOYd8%2FfA6KPpE6omjoJ6jTlg1jDhernvg%2F7c5CPHqgsMd&X-Amz-Signature=864df77744ce51dd316cb37d67844bd4227219351ec17119f930cde115c56f5a&X-Amz-SignedHeaders=host&x-id=GetObject)
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
