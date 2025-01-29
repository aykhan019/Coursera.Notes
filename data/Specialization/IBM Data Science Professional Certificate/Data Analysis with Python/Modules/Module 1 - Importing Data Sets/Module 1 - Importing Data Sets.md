

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

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/997ac361-58a8-4f04-bb0f-79fea4baa761/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46643APLHV7%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T071339Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEH8aCXVzLXdlc3QtMiJHMEUCIDxeYQVwbEKvXF5dTl%2BkgaNE%2FD1hzp1WqN4qzJJNepHXAiEAsscVCt7SV%2BHqgMYBs0dAL8kkBvCUeCB6R0RqQP83phgqiAQIh%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHcmK9e7pdegjoL4rSrcA2sq2NCI9%2BtSXVd2Tj%2Fj2du20GLcsBl8%2BvfD0nUELt9KzFhtK1sHp50IaVWj2R5icqm5rioN1dMsky8cWWYvFpulSLl36ydfH%2BNSZn7UmjE8Rl8mhQm0%2F%2FZhYISDGBwSwbTnCXLubHPFtc7Es7w2iFoy%2BCH9zh81QCcejJ6MOQs9GduVcmWShllFZnjfQlvgYlOfHzmmaWampntbow4Ef3npxT5HL0uaYeIw7diKsGHPM8NugTRqXCfQC%2FVEB5meRKX04BAH1EGIB3bUUgBBevgTy5jXL2qCjDMfZeVo8dRsF4uBUPgnCklatom3j1k1pHim2%2BHdxSD2fEsSY1c5zTVdVFMlNn8iT7RPPRf9ENf0RlEOi86ADSMn8LuTXzJX6Zk1t5t1amIqtzIAClJDThMhZf8zWKGqHJgEpfCDPna80Y158DUaifAVv0FTEr5jDsVVW4Dj8Ut1WY4esnb%2FRkaBt5Z5j%2F3FDyuI1QYwrfjamgb33%2Bp6qwsNOZ%2FdzIL4uZAOBtRUZ3G1GJ832HrPkHg1ELccVNfwDTeom1xda4A1GS9sfwI0oTHjiuKb92aZwX4QYvfDXha7qzzS6dhzA%2BAmIs8nj0Yxs2hys09sL1EZE1cqlPyzdUajgF0VMNGQ57wGOqUB554hErTmdHo5MPJVB31ogq8K5lnYf1O%2F6RjImtj5rlI7pjzMIgja5udxniiD17o7dwSmquQPF7YHYSXNtz0OzGZ%2F4ZReu7h2kLutKVTlvVyxggt54UnBrIyCBSeWLh9P%2FNiIZQLFSSXg7FP8y%2B4oTU5023ESaziyGIA%2F6XrOwp2RxyD%2FFbGO3lHeh%2F36c1WTqXiQuBDUflMG7W%2BBYBA%2BVDCKN5LL&X-Amz-Signature=fe34640363bb8b2283dc742f73e65ed0e518f688df4554d865d4938f4db38861&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Data Visualization Libraries
#### 1. **Matplotlib**
- **Description:** The most well-known library for data visualization.
- **Features:** Great for making highly customizable graphs and plots.
#### 2. **Seaborn**
- **Description:** A high-level visualization library based on Matplotlib.
- **Features:** Easy to generate various plots like heat maps, time series, and violin plots.

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/733d1e42-5a53-4fd8-90c1-3d85254369a6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WAE7Q5PR%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T071336Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEH8aCXVzLXdlc3QtMiJHMEUCIQDnMu5UoWFiNZ1vtH9HGinl0gQJH7sGiIQPYoycPw8A%2FQIgVaEOK86wJmDWIoC6q9QMV60oqIkvCsPIKyN%2BwIsjTToqiAQIh%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFuv0yRZtmJuM5B3iyrcA4JxopYmFKrWGnI4kbivIvO%2Fhf07zBdBeso%2FCMWKxQ6YEUNfR8ZS0RuIGFXypoFX2r8CGtIxE8xXiWowlqFN5ywOr8Uo9VVp7omYPCiq3iMPtjYSMnDgss2dL1owEa7Y8QDIUwN3d56x2yu80iC7%2Fg0O41CI5fBjeksAyBr7naKYflV4rmWDLHg92%2BtAqUvps%2B4hdpLqXcRD3lZ3iro7qSXexyHGwfhqrNWyhIxymIzchuODQEZVDzW2pV2q1DmI8zU7%2F753whk1VcKySrYzMl4EZYh4i0pgkN7xxyVsI1Sy2XOmeo7dOHHRQZcL5Cm2aGu7U%2F8tEFt%2FYPQKgD4sUYtXULWXRh1hyWxLtfXxbo03R%2FwqLmx0I4oxnPuiCImTNwku8XJ5nUu2nnCRplCCrKLH2savQYeSKTxGQFWAEDjTBr0eVk5LBePN%2BWlCgXZxH3GAWJs01lDOFYazV4CBVMTulvwfb8ITHn066RlgxFIrnABCale8miFPRrDzwVP3BvuCxAMidH6LOzdpwGKaf%2B5bXf3YOgdMDZ4roBskfGD5Gccbvlgs04WuwdFYAKjIYJsBN5%2FySEWGd7RwRZnkJAAtV5hRWK8MA5Eo1leJa8NMDf5VKqVQXPcnicZqMNmQ57wGOqUBuW9Lx5dtR%2FxDkNT3jbxrCaGM8DGMKW2237EseVN0TLTxCevPnrLtg3LfRfbkZpFwBzixOsHkEi1CvGIRDOkIecGhzhoY0fYDp7PRksChgDNAxXBhdeRo16kLh84x3Q5rxj8y9UYQsabN1IwSrO5lBcz1frKQs6zFgy%2FWciO8C3tI4II5vjdugJ3Ht6czX8PyNWp1gQqVthJyzo%2B%2B8%2BfYMoPlQLgo&X-Amz-Signature=eaf448e81f482e4b5254cfb906ecfca360667c36917c90b31d3cdc6b69408ba4&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Algorithmic Libraries
#### 1. **Scikit-learn**
- **Description:** Contains tools for statistical modeling, including regression, classification, clustering, etc.
- **Built on:** NumPy, SciPy, and Matplotlib.
#### 2. **Statsmodels**
- **Description:** A module for exploring data, estimating statistical models, and performing statistical tests.

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c62885f5-417d-4179-834f-d68f8f2bdf39/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WAE7Q5PR%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T071336Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEH8aCXVzLXdlc3QtMiJHMEUCIQDnMu5UoWFiNZ1vtH9HGinl0gQJH7sGiIQPYoycPw8A%2FQIgVaEOK86wJmDWIoC6q9QMV60oqIkvCsPIKyN%2BwIsjTToqiAQIh%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFuv0yRZtmJuM5B3iyrcA4JxopYmFKrWGnI4kbivIvO%2Fhf07zBdBeso%2FCMWKxQ6YEUNfR8ZS0RuIGFXypoFX2r8CGtIxE8xXiWowlqFN5ywOr8Uo9VVp7omYPCiq3iMPtjYSMnDgss2dL1owEa7Y8QDIUwN3d56x2yu80iC7%2Fg0O41CI5fBjeksAyBr7naKYflV4rmWDLHg92%2BtAqUvps%2B4hdpLqXcRD3lZ3iro7qSXexyHGwfhqrNWyhIxymIzchuODQEZVDzW2pV2q1DmI8zU7%2F753whk1VcKySrYzMl4EZYh4i0pgkN7xxyVsI1Sy2XOmeo7dOHHRQZcL5Cm2aGu7U%2F8tEFt%2FYPQKgD4sUYtXULWXRh1hyWxLtfXxbo03R%2FwqLmx0I4oxnPuiCImTNwku8XJ5nUu2nnCRplCCrKLH2savQYeSKTxGQFWAEDjTBr0eVk5LBePN%2BWlCgXZxH3GAWJs01lDOFYazV4CBVMTulvwfb8ITHn066RlgxFIrnABCale8miFPRrDzwVP3BvuCxAMidH6LOzdpwGKaf%2B5bXf3YOgdMDZ4roBskfGD5Gccbvlgs04WuwdFYAKjIYJsBN5%2FySEWGd7RwRZnkJAAtV5hRWK8MA5Eo1leJa8NMDf5VKqVQXPcnicZqMNmQ57wGOqUBuW9Lx5dtR%2FxDkNT3jbxrCaGM8DGMKW2237EseVN0TLTxCevPnrLtg3LfRfbkZpFwBzixOsHkEi1CvGIRDOkIecGhzhoY0fYDp7PRksChgDNAxXBhdeRo16kLh84x3Q5rxj8y9UYQsabN1IwSrO5lBcz1frKQs6zFgy%2FWciO8C3tI4II5vjdugJ3Ht6czX8PyNWp1gQqVthJyzo%2B%2B8%2BfYMoPlQLgo&X-Amz-Signature=56fe47de390a888e8e4695ac98d699fdaeb74c10709e6ae91fba585e02166713&X-Amz-SignedHeaders=host&x-id=GetObject)
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
