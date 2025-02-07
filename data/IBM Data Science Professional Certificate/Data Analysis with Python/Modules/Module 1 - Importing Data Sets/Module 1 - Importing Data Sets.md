

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

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/997ac361-58a8-4f04-bb0f-79fea4baa761/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46662BSK3Q6%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T211311Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGQaCXVzLXdlc3QtMiJHMEUCIDOMB0qpav3jOq59sZwVJqtpPaC7yfWF51JUuFEmErf%2FAiEA41dyu%2FlrnUzImpDgZFWF1wTDcbN2frtUtQ%2FIW1aPjF4q%2FwMIfRAAGgw2Mzc0MjMxODM4MDUiDG4CDxvJPFG4LuSeKCrcA%2Flq9ElgaU1k2qh5kC2xG1sCR18uonmsEkuzMF4WgtHwN7INN2fOW5VW%2F8NML4PI89amu9q2D%2Fts2pazojBMPriHpxZcVoo26YBuIbMIWkDltsLp8SL4Jyy%2BEHu5K4OvAiJOKkH9TYjvSefwwe3RKrVhFK%2FZunFi3DWO3i2OPQbkHZJ%2FEf5uEOqxMmshGuVpBHGxNHgpSAfJfwhNswDazxJ9ju6aRVUEMzCaGwIwbR6Q6uhb9iMtEYrGnYE90nihcCH18%2BXHYoVJqhAnBAY2X3wRHtE6BLyfPhRmUDaPj221F0O9MNtoifKurn24MuUnw4SwsSAhBS9jUGkzJRysy%2FoIVDuvAJc6CBriTQKKCR56hUrdMm1d2iqmhyVA%2Bxmbr8scw3RBgd9Cne39laeKDno4COp0oKIS89I7tfxiC3MgwKbkgvISGhLZpPn5efaQ34BE511qjaB3rw5D5v2G2EYRIU1w1wuq%2FHY9ZhupAGR5eWenz3v511xjaA4Eb2zyOsHzSK9hkamEh6Wt9L4UvH7P6uulx0Zj%2BT8xPAIenmYhvDOKbRi0%2F96mnDGwDqJXxtU0%2FVJVf7tId1%2FLjg%2FRdHCiQUHBQmLl3JwL6qNrG79a6RSTj93hN2QCs0JCMOfSmb0GOqUBTIbCPs7futntf6%2Fins7SIQtUE5S5MoHt8Rh%2BsTIYMWdpfFXNL81w%2BTSKUV2H8QjKmz2yrt2yclLaxrzIlQJ%2FehBryGjURvCL1cceqx%2BQavcIhaju2l5rbyLwHytOFOs79kBimPijPzoB6S134n0V%2F3Y2PvokFr34ydSXMDy9g14jFpf2PygCDzzGAdzxRyU5nm7mElTSj1gUd3zfBZKOgyiepvNv&X-Amz-Signature=23f6a619c11fa90a63f8f76a5333e59bc046008a76ba34a714a8c3ad6a6ae61e&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Data Visualization Libraries
#### 1. **Matplotlib**
- **Description:** The most well-known library for data visualization.
- **Features:** Great for making highly customizable graphs and plots.
#### 2. **Seaborn**
- **Description:** A high-level visualization library based on Matplotlib.
- **Features:** Easy to generate various plots like heat maps, time series, and violin plots.

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/733d1e42-5a53-4fd8-90c1-3d85254369a6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SJ5BBRWG%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T211310Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGQaCXVzLXdlc3QtMiJGMEQCICj3oqwY5f9OTdilTEU1U51GL4iz7s3IZ%2F%2FI2x86bKaGAiAEcEjY8pss8WpzuD8KnQ7e9OA4nZQq6lvGltFmzFJILSr%2FAwh9EAAaDDYzNzQyMzE4MzgwNSIMQI9RugJl8YyPy0bFKtwDxfgxD%2FPSqEeKcXdE5zMHuShFFyNRiHQAJEuJTsBq9PVi%2BHtgFa1GMgCGExd%2B1nBAvF1Na4gpjkdnLArO2lz8U%2FvsnFpd35mglSHdI0eduFMJHPO1KUAB7lyDpnq3qxTs2Uei%2FOT1SRqc3GJi%2BmSylY9IpuXSXurU5RQIFh1LDkTk7XaQe3pVKw3WaF3qJtZSCFS1BCCAWiEBPdtPY%2Fws%2BpvmnOZthmXQ504%2FIXy%2Bpks1qqLUCkVe314AKC7zUJMJY9GR1khoqD8xiFdutV%2FKBIAayXTduhIEBE7teZY5k5UsEU583EGenyLdOArJ2Ce0qx9ivOV8hk%2FdRyVaHufTCX1%2BRYGxnA2dpPPhOPjLJvWBnrOGJYaAlunrPUcAELXrSwJj1htI8IpKIlhN%2BAE1oLJeAJYUMwVy9%2BwwxTD0Kk4%2FSVT6Wsvu6cxycjQO3fg9VHhbPbrMjKGUz1eaBvX6zxGT9au47CinrGF%2BBd6XvaJf8CE5g4XMNUeZ3hf5dEnLIqZmYXMfNCORbwKimgZWPnJ7P3pi2a5qnlhYGHsj%2F6UVa%2FZY1u%2FpsyuyhoeRsYVkr6nrHbVCH%2BZWfFGRI%2ButyWUdjDQVIkHoZ3fA6OyoYy%2FcD%2FjpzMI%2B6Sk9XRcw09KZvQY6pgFyWSMgFZ7QSwaWUUzH83LtI1a86ICJS39HsUzcMs1vljcsr6uyAzxK06Xan7JAerwvWFBvqUo5pBn6K7gPduWNhBj45b4%2FPT%2BJdZvYlF26hnqX3eMpg1zN0a%2FUTof%2B5BJ2JvJ%2BI%2BEanexVeHtzujg1uPVy3TrZGc5B9gUPubY7KbaxYnkGtFsU9dt30Q%2BlTSCxS5uF3c%2Byz1maw9QiuskJeJlYCstd&X-Amz-Signature=4d535a128633d022d0494b909dd463d8a77b01cf3c60ac3ac2b1b2ec436f5ad4&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Algorithmic Libraries
#### 1. **Scikit-learn**
- **Description:** Contains tools for statistical modeling, including regression, classification, clustering, etc.
- **Built on:** NumPy, SciPy, and Matplotlib.
#### 2. **Statsmodels**
- **Description:** A module for exploring data, estimating statistical models, and performing statistical tests.

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c62885f5-417d-4179-834f-d68f8f2bdf39/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SJ5BBRWG%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T211310Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGQaCXVzLXdlc3QtMiJGMEQCICj3oqwY5f9OTdilTEU1U51GL4iz7s3IZ%2F%2FI2x86bKaGAiAEcEjY8pss8WpzuD8KnQ7e9OA4nZQq6lvGltFmzFJILSr%2FAwh9EAAaDDYzNzQyMzE4MzgwNSIMQI9RugJl8YyPy0bFKtwDxfgxD%2FPSqEeKcXdE5zMHuShFFyNRiHQAJEuJTsBq9PVi%2BHtgFa1GMgCGExd%2B1nBAvF1Na4gpjkdnLArO2lz8U%2FvsnFpd35mglSHdI0eduFMJHPO1KUAB7lyDpnq3qxTs2Uei%2FOT1SRqc3GJi%2BmSylY9IpuXSXurU5RQIFh1LDkTk7XaQe3pVKw3WaF3qJtZSCFS1BCCAWiEBPdtPY%2Fws%2BpvmnOZthmXQ504%2FIXy%2Bpks1qqLUCkVe314AKC7zUJMJY9GR1khoqD8xiFdutV%2FKBIAayXTduhIEBE7teZY5k5UsEU583EGenyLdOArJ2Ce0qx9ivOV8hk%2FdRyVaHufTCX1%2BRYGxnA2dpPPhOPjLJvWBnrOGJYaAlunrPUcAELXrSwJj1htI8IpKIlhN%2BAE1oLJeAJYUMwVy9%2BwwxTD0Kk4%2FSVT6Wsvu6cxycjQO3fg9VHhbPbrMjKGUz1eaBvX6zxGT9au47CinrGF%2BBd6XvaJf8CE5g4XMNUeZ3hf5dEnLIqZmYXMfNCORbwKimgZWPnJ7P3pi2a5qnlhYGHsj%2F6UVa%2FZY1u%2FpsyuyhoeRsYVkr6nrHbVCH%2BZWfFGRI%2ButyWUdjDQVIkHoZ3fA6OyoYy%2FcD%2FjpzMI%2B6Sk9XRcw09KZvQY6pgFyWSMgFZ7QSwaWUUzH83LtI1a86ICJS39HsUzcMs1vljcsr6uyAzxK06Xan7JAerwvWFBvqUo5pBn6K7gPduWNhBj45b4%2FPT%2BJdZvYlF26hnqX3eMpg1zN0a%2FUTof%2B5BJ2JvJ%2BI%2BEanexVeHtzujg1uPVy3TrZGc5B9gUPubY7KbaxYnkGtFsU9dt30Q%2BlTSCxS5uF3c%2Byz1maw9QiuskJeJlYCstd&X-Amz-Signature=1f155deb0ed0c4e04424ca5eb2722612d92ea89b3faee1c51b0103a3366257c9&X-Amz-SignedHeaders=host&x-id=GetObject)
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
