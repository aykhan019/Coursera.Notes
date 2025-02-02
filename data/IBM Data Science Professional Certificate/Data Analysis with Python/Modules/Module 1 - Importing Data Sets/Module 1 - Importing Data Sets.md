

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

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/997ac361-58a8-4f04-bb0f-79fea4baa761/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VO2K6PEL%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T231258Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEO%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFXpEY1QKKfKwOK2iINs3L7D3QNCRhARvonZLe5eshGMAiEAnOxWU%2F00NiQdPtdKbNd18%2FPuzjOAc8ki2gEJu%2BnE%2F40qiAQI%2BP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDN0bZAoWv9j%2Fk%2FLZwircA0VxazVxs3ju1ATTzCPkg9L6dkQUIuwuauKCoFUtG0DJL3U1bEBTTkQ7JdDG%2B0F8pEshE5EB3osFzbrucSnWiZMiI8VKIHOoB2gx7tsq9jYW1KaNnlE8Bh5QYIafM8xP%2BoxPo0LZcm2piF31NLLENO3eVDyZk2QipFvH0vbI3RPyK6%2BWCGtK6zQAr41r9adGGjQ0ymmuP8yLDnganWDumLiBc7LcIeDxWdmjwoNuQJNOiIWRjytZlpzIZkztD2njy7CGqEkOXfbISGiZVwn78T3HgF3%2BGanAHkqmNAcs9uSSGQYRhudX%2BSy4KZuLKqEOXDGD3%2F4gsNKXkcf2XhNTWmlaBmKUsKoKCLRmb2On%2Fb0LUvAuJbS7gRxWmA1eEyHSfvEMT%2FGakGYrIRTOEShHc57mR74J3lhxz2qC8gnjNZXLf0N22gbQUd2CmD489OO8yK2hceZdeHistsqumfmmTLVnZRxaaZngcije5eafit%2B0qrx1ivNlVPLQwKs98ZS5qYgJ24BMkY2ssjk2zBrnutdXNKQzccDuZ6t5czASBKEbP3UlOe9BayZ94hkCArB%2FSmyHNMsrSFqOw6FOZNvbip0tgtPbqAtFvfkKpbb%2FRIBM2ZpLKUgU0tvzTnbJMKTk%2F7wGOqUBohYD2DEawK0JU%2B5wqelQrDaZM8%2BpxmJPshnB2nfYWVFfr9U5dIk09zLUNhFpmvBIiIYFG3XZgTS1imERspV%2BaInxYl2UeE7GWZDv0FDV1QAKO%2BMEPikkEs9WvfDY08NF0N1mCBtz1D8nNNh9jDYB0VVMNWqazqdmonDdHofnZfxNpd0Llyv87PpsPZXdNQ8ORnbf2%2FfCBHQOVu%2BpBDQIhP5%2FVSxP&X-Amz-Signature=06daf6408552f8e277e0743ca0fc0016cb112d1aea0f237a9fb265dab8fa4a20&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Data Visualization Libraries
#### 1. **Matplotlib**
- **Description:** The most well-known library for data visualization.
- **Features:** Great for making highly customizable graphs and plots.
#### 2. **Seaborn**
- **Description:** A high-level visualization library based on Matplotlib.
- **Features:** Easy to generate various plots like heat maps, time series, and violin plots.

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/733d1e42-5a53-4fd8-90c1-3d85254369a6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VGGACIOZ%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T231257Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEO%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCB7okCvzm4ThYfe%2FumhgKiCiWkYsO1d%2Fa%2F4xOJ0eQXZwIhAIdS1Cu7Sho%2B%2BvjabVKMbjYXWxbhwsxd%2B9QN86r493HyKogECPj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxeUHK5EuVPNQByaUkq3ANa8Sp2vF6QgTQD8pFvr7XlWUP9s8%2FbrNy%2BfQzcGnIwVrzmaNnMndVPdCgE9%2FTKxzc0IKCqEBUL0mdZrQfSKvCGHwfD%2FSqwR1mTY9xiXvurIHv3%2BSrhzk0%2BY1s2h%2BWHDGBR0rWIrU0x8qIcNIOOXA0DIYJ%2Bd%2BNjf%2FM4u22azcJjH6ovdyGBoQebppx1XHy8TRKoe0QHllv38l%2BoN3BlvwgxsEp72o4tORKvskfh4QFLf7opTlORCqLx%2BdLDhYje%2FuZcLgvnHx4aC84CbebCaRJm37CuV4ZezKAHk66deD4s%2FnfFurabqx6Z1fq9b0ttAtSdOhg9wmOP66ccBXnmYpW8QaMNvvHYRGlo2PhOi3HEnKOapHUHUwIpe5sheYfBBgIL%2B1NEGiaavYiKVt%2FxmuHQPjnhg0ANJomuhh4CraafsX%2B3NL%2BOmkrJ%2FFZxvUID2VakvWOsqiZoZh1l7voQCJTnFg%2F5m7MHnSflEoBGkEriF6SrD7RTWwQCb5Xsx5dgEBizwkFafXT6Z1Y%2Fyu9H%2BFxtyxMjCFkiZMP1aJKhGAmB1lLXVJt2eM3YhofGYs10BP5l%2Fw5JZxjv9Lt7%2FBWF%2BrLdoVXrV5UPZiLmQSOjSflV6LhHMHGMlJCa7UeOtTCv5P%2B8BjqkAeGT8xyuvN9h6dRgwpo6ceaSL7c8VSfaL%2BOhuscLD%2B1%2FXj2%2B6FUfQAfl1c%2BvliJ9Z2fxwkMWcXyAqd%2BSG5qXbtQcPrVCJ2%2BdC2tGzEDvBUH4XEBo5NWmZbe%2BnUCtUapaNMvLeN5FcV%2FJh2GIQeduOAOOjUF%2FnPkWq8cQnzUDo%2Fg7e%2FZq9eD%2BKtXznXGUkPO1Nal0iqm%2BDM0y%2BlnkTqcxv0M124iR&X-Amz-Signature=51ded5556812470b4a815dc2945a7b5a102a1f67dae948447c1b7098612069f7&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Algorithmic Libraries
#### 1. **Scikit-learn**
- **Description:** Contains tools for statistical modeling, including regression, classification, clustering, etc.
- **Built on:** NumPy, SciPy, and Matplotlib.
#### 2. **Statsmodels**
- **Description:** A module for exploring data, estimating statistical models, and performing statistical tests.

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c62885f5-417d-4179-834f-d68f8f2bdf39/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VGGACIOZ%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T231257Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEO%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCB7okCvzm4ThYfe%2FumhgKiCiWkYsO1d%2Fa%2F4xOJ0eQXZwIhAIdS1Cu7Sho%2B%2BvjabVKMbjYXWxbhwsxd%2B9QN86r493HyKogECPj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxeUHK5EuVPNQByaUkq3ANa8Sp2vF6QgTQD8pFvr7XlWUP9s8%2FbrNy%2BfQzcGnIwVrzmaNnMndVPdCgE9%2FTKxzc0IKCqEBUL0mdZrQfSKvCGHwfD%2FSqwR1mTY9xiXvurIHv3%2BSrhzk0%2BY1s2h%2BWHDGBR0rWIrU0x8qIcNIOOXA0DIYJ%2Bd%2BNjf%2FM4u22azcJjH6ovdyGBoQebppx1XHy8TRKoe0QHllv38l%2BoN3BlvwgxsEp72o4tORKvskfh4QFLf7opTlORCqLx%2BdLDhYje%2FuZcLgvnHx4aC84CbebCaRJm37CuV4ZezKAHk66deD4s%2FnfFurabqx6Z1fq9b0ttAtSdOhg9wmOP66ccBXnmYpW8QaMNvvHYRGlo2PhOi3HEnKOapHUHUwIpe5sheYfBBgIL%2B1NEGiaavYiKVt%2FxmuHQPjnhg0ANJomuhh4CraafsX%2B3NL%2BOmkrJ%2FFZxvUID2VakvWOsqiZoZh1l7voQCJTnFg%2F5m7MHnSflEoBGkEriF6SrD7RTWwQCb5Xsx5dgEBizwkFafXT6Z1Y%2Fyu9H%2BFxtyxMjCFkiZMP1aJKhGAmB1lLXVJt2eM3YhofGYs10BP5l%2Fw5JZxjv9Lt7%2FBWF%2BrLdoVXrV5UPZiLmQSOjSflV6LhHMHGMlJCa7UeOtTCv5P%2B8BjqkAeGT8xyuvN9h6dRgwpo6ceaSL7c8VSfaL%2BOhuscLD%2B1%2FXj2%2B6FUfQAfl1c%2BvliJ9Z2fxwkMWcXyAqd%2BSG5qXbtQcPrVCJ2%2BdC2tGzEDvBUH4XEBo5NWmZbe%2BnUCtUapaNMvLeN5FcV%2FJh2GIQeduOAOOjUF%2FnPkWq8cQnzUDo%2Fg7e%2FZq9eD%2BKtXznXGUkPO1Nal0iqm%2BDM0y%2BlnkTqcxv0M124iR&X-Amz-Signature=32f89973eef5d9a6ad99c0a023350c324d4e9fb8b67f0ce2aca7f1bc160847bb&X-Amz-SignedHeaders=host&x-id=GetObject)
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
