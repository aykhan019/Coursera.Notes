

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

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/997ac361-58a8-4f04-bb0f-79fea4baa761/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663XK6UPHE%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T111104Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHAaCXVzLXdlc3QtMiJIMEYCIQDL2AZKu41VdC%2B1Uxfmiql4QjSBSwe%2FT1oSQ9Cw07i2pQIhAKrcil5nHJvDUaQkTd15FqRmv5%2Fa3f%2FMaS%2BLypFBHXeMKogECIn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igx1sR63QHCYQu%2F4QJkq3AMmxvrbZlG3QxasBkV4pjdAfTc82If%2Fs3cRSg29a2CjLuHdS80C6JV%2FzBrGZi%2BqTQTRNEPB5eie7i%2BAiruBzj3GXj5pOi%2Fk7d41W4c2OI9s6NWbJIDkwn1ztDHaouEG1UtAfBF2qfyre6s7Vn0KYXZGaaGOd%2FwJvYhLCwzc0WBlrOgxQ2Ul5UVa0MBV%2BNGNaoXsx1mZTlabURlFlgoipa3C70rFYgjN7VWi0MkacijzHBB58CnJJJT1zRV5bcDuYXIORr11avpQmaCkcMNgkl9jNR701xeUGfF3DC4fJSalBVb2dR%2BTpRpF5I3r55HQM5Cx0Wp0l3%2FX2%2FZsdayuAVDtRGJX6A79YWZO9jcDtSFA8k8%2FUaXfJyBqi682rtOD2EV0dTrfh0Qc4IYv%2Fszc19tN%2Ff32Z9led%2BHma9P5DZz4c5oPuhCTu2aXg2jAfplP8vqaJkICu3OKWwI2DdLCUUbc32izYipfM7AdHQMew2ZzQ3I7cppRp4MCQHJ7Wq5PPmu6myq1NWoMIwwO3GeseTV36WBreRkOGeSyXIdLyi77%2FXtmgjZvHq7gXxMLhAcErtD10MSYwliYhPDR6DQOrcpDadPmju6w%2FR6npdzcZDk2SmsAmZobH61PIrQJ6zDQjpy9BjqkAfmzN0ALTR4F4A9DH3DSUerRQdCDM12RaqQVUEnP13wA9VyVh9uuSrZcJl0LQERkr4HAHrO6Mrictms5V2o6D7horSR%2F4x%2BDM6mdgHZtS7HWEIjGaGojKQKNkQOtX88qC6pqRN%2FYzGWf0TRzlBmc3wHqfWpw86%2FjrnI62rDxqvE%2Fev%2FWGIUtnoypixlq1OZKSh8%2BIbCZRe1jKfJYLe5Z0lbeFfHi&X-Amz-Signature=8bd6758590a19fa5cafb54ba3567ba57f21f5e973ed6b0614201e19dada0fbb9&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Data Visualization Libraries
#### 1. **Matplotlib**
- **Description:** The most well-known library for data visualization.
- **Features:** Great for making highly customizable graphs and plots.
#### 2. **Seaborn**
- **Description:** A high-level visualization library based on Matplotlib.
- **Features:** Easy to generate various plots like heat maps, time series, and violin plots.

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/733d1e42-5a53-4fd8-90c1-3d85254369a6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UE2CYSGM%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T111103Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHAaCXVzLXdlc3QtMiJHMEUCIQDw4py%2F%2Bfvb0bScpHAYL7l3LOxoZg1fDpfIAmTr4Gvz0AIgEjiFROavpAir9KQGtYa4rx31ev5lQJOqIMWxcTPVDasqiAQIif%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDCAzi%2BQsRDgUJYyxWCrcA%2FHNbYa%2FZx1qx39%2F97vmrM9brrz909L6UfQnxptFLyk3tGiRB%2FXgYC4GUJi9i7Hg8gKjQ%2F2ZniuAwCRm%2B%2F9MGrxaWgwL1KZXZ2PtzbwUXjQJa5p0U8kcAvZBWkRtOWaKLjELCN9bQGoifceChbmUo2wdKVgoDZBNufQPT2E2XpOnL1RuughzE2ywXxuMh3Ph6s3ltouJUtwUd5hkdW%2Bl9%2BBg1KqGOPgDQW3AqnVPXZaa7kR9D3S62Umh37dcmPLMi7lGTzDw7ytqtfAuPBAOui0MUdrwBF%2BcpuEZ%2BTjmPFMQvvil%2BvEhJGQinhmrKkIsEaBnaRwMBWY9jb4J96EchwFpP6k9bjHlzZGC8NPNrXPE7h2xwU3KeLH6RzGECz%2BMdr%2Fx61D2hdJur7cqn4kC8HvBuGI8ZXPddmBryUrZpvm3Kk1Fo%2Bi%2BTtVXRafZq2I18HkJEiDjNI9BCZRn4AO0aCAMAuKLqMjcJVW81iImRL49D96GJVSQvwnCsTHGpcyIJPQ4sVDMmBjyaj5zlUDn2wt9qB1WDQmY0HLJ5mHuVHKS4kogY661Zvns17ihQKto%2FqzjpRi4Qi4NKliZCW2eV5cMh1HIINTz8OTaSGIhuf9xgOGU7S6hxR7IGxVZMJGOnL0GOqUBtCGm40%2BPqhb6ZzzvEhBKc%2F8vl6Dn8H%2BbCezUFkU4WHSteXU5gq81keQVVFCWcoSvDrxZN2Nlsrip2SD7%2BePcbC2WWylyyC1oOSI00JlCWTiFUICi6%2FMwg%2FS5kuI5Yf1gcSAI2Xz2xbNAqZ9LwGd4YTIvr0uuGu7RxS7q9ya7AveR2qMQMQrjl4y5sDt%2BxXH24P%2F1%2B19c4skUkDRRNhtIM4SN83CN&X-Amz-Signature=22600857cb21235dd817da67bf67ae415832a34cb6c99c47c03a86d64e416eb5&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Algorithmic Libraries
#### 1. **Scikit-learn**
- **Description:** Contains tools for statistical modeling, including regression, classification, clustering, etc.
- **Built on:** NumPy, SciPy, and Matplotlib.
#### 2. **Statsmodels**
- **Description:** A module for exploring data, estimating statistical models, and performing statistical tests.

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c62885f5-417d-4179-834f-d68f8f2bdf39/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UE2CYSGM%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T111103Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHAaCXVzLXdlc3QtMiJHMEUCIQDw4py%2F%2Bfvb0bScpHAYL7l3LOxoZg1fDpfIAmTr4Gvz0AIgEjiFROavpAir9KQGtYa4rx31ev5lQJOqIMWxcTPVDasqiAQIif%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDCAzi%2BQsRDgUJYyxWCrcA%2FHNbYa%2FZx1qx39%2F97vmrM9brrz909L6UfQnxptFLyk3tGiRB%2FXgYC4GUJi9i7Hg8gKjQ%2F2ZniuAwCRm%2B%2F9MGrxaWgwL1KZXZ2PtzbwUXjQJa5p0U8kcAvZBWkRtOWaKLjELCN9bQGoifceChbmUo2wdKVgoDZBNufQPT2E2XpOnL1RuughzE2ywXxuMh3Ph6s3ltouJUtwUd5hkdW%2Bl9%2BBg1KqGOPgDQW3AqnVPXZaa7kR9D3S62Umh37dcmPLMi7lGTzDw7ytqtfAuPBAOui0MUdrwBF%2BcpuEZ%2BTjmPFMQvvil%2BvEhJGQinhmrKkIsEaBnaRwMBWY9jb4J96EchwFpP6k9bjHlzZGC8NPNrXPE7h2xwU3KeLH6RzGECz%2BMdr%2Fx61D2hdJur7cqn4kC8HvBuGI8ZXPddmBryUrZpvm3Kk1Fo%2Bi%2BTtVXRafZq2I18HkJEiDjNI9BCZRn4AO0aCAMAuKLqMjcJVW81iImRL49D96GJVSQvwnCsTHGpcyIJPQ4sVDMmBjyaj5zlUDn2wt9qB1WDQmY0HLJ5mHuVHKS4kogY661Zvns17ihQKto%2FqzjpRi4Qi4NKliZCW2eV5cMh1HIINTz8OTaSGIhuf9xgOGU7S6hxR7IGxVZMJGOnL0GOqUBtCGm40%2BPqhb6ZzzvEhBKc%2F8vl6Dn8H%2BbCezUFkU4WHSteXU5gq81keQVVFCWcoSvDrxZN2Nlsrip2SD7%2BePcbC2WWylyyC1oOSI00JlCWTiFUICi6%2FMwg%2FS5kuI5Yf1gcSAI2Xz2xbNAqZ9LwGd4YTIvr0uuGu7RxS7q9ya7AveR2qMQMQrjl4y5sDt%2BxXH24P%2F1%2B19c4skUkDRRNhtIM4SN83CN&X-Amz-Signature=52738d9c2bb4c8ec2282aece4369ce717893901e0548eab3a6276ba1a5f5e44a&X-Amz-SignedHeaders=host&x-id=GetObject)
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
