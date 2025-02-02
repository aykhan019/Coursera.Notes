

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

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/997ac361-58a8-4f04-bb0f-79fea4baa761/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZQEEVNGY%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T181845Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDqrcz7VYbUDQLQkLEF3vpDO64jLMuLHrbPlLg36if2iQIgf3PKYnc9gN6tYPITxixAlYrCwmiEzIQBDL%2BCYZvymsUqiAQI8%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDIJCWkE9i5aOEXVNdCrcAwhV5RrOe0nzLnea3sgb0xHE1jn7grllClQFkRp6PfZNKb63gxWoaHGdOyKzR55MIHvYVv%2Fi6wWuWW%2FAizFrTkpY5tGi4lKUf%2FCcgG9NRe7dCKR5uLi8w%2BjybBSeNPkBaIWs7QTy%2FHJ%2BJdXpgjFcXGTTmmQWcjgnLjvFHyDd0EuGpiRGQttoZh5myaOk9I6Tc3TFUN7Ez9vvyyrt2lm3rkP5WwarJSqIIIyvE3HmHPxc41Bqd%2F8U64hfbMYv9BTIfMCq1ih6HkYBk3atKMLLZt4Ei8xKd3LWyHiEZHzpqjfARtIe0eOkdesmA%2BnPniXk2rBWjxUfGA7jL7twEJxPQhzU6Z30WnxrwMbxnr73gBTp3mwMviyq9kRQXyDAJk506PHyGlCi8eNV0zmY4MykjTr7xTKr%2FSwrNwX0FrSiu5hn499fSQwtjT4vdrfh9HW%2FR9t37LijY0Jw18cSzY%2B5%2BU8UzlAtL12hOtJywBJo3lEco%2BWdKMlFOvI1OtfiRfGhLjFhhTXOwPtbCZqfLYttrEUsh7oXgvrBcdb3%2BOuVomQHOmh39bcK56a5Go%2FS2X4WP1y88Oc5uxWwR0yCv5RnOu0MNJFE%2Buh3fMgX%2F8cJKW5AgOyfNHQjXodvH8waMOnj%2FrwGOqUBKZ%2FfeOlIGdGDDEdtkxUQ1COOKho1hOjA%2FuEkqc1q23wwddaEvniMSDzc9vkxBpknk%2F3ojz1yFgxK51dduVTr0q0qDIc9kdqfk9fd0t021J8BbSSO9MHmTjPj6925O838%2BPKTEhfdItEtR0ZdmKZ2U9PXlN2Lu7zuhQHR16nDPly7CUXrg7PXCHwnN7b7vzslQJGAOLhTv7KEVajPWoKetwQylFxg&X-Amz-Signature=eac706607f7d73615ce99c4b0ef0413a725969e381b20fc91287bba8caf79507&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Data Visualization Libraries
#### 1. **Matplotlib**
- **Description:** The most well-known library for data visualization.
- **Features:** Great for making highly customizable graphs and plots.
#### 2. **Seaborn**
- **Description:** A high-level visualization library based on Matplotlib.
- **Features:** Easy to generate various plots like heat maps, time series, and violin plots.

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/733d1e42-5a53-4fd8-90c1-3d85254369a6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RX4GOJAK%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T181844Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC6nunrJiameFmAxcfQdnkDty1g4wDxIH%2FGL07xykVpzwIhAJEIdGIV9Oo6Ow5C18pAPv3DynprbcHc0B8gOFOBOgtxKogECPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwyhBL1rQvyVVf%2FVuEq3AOW%2BdOO34YWFye00dJSBXjQQPx%2F%2BSCjQD7I2hsN2KJ595oitHIwazQqRvh2rZR8COn8w9ifNFc3ege3XQyWvvJKHyCA%2BtusQ5wpnVCgrfA%2FQvBDWG9ZAEvlDU1qTJ8oUgpwEds2S6LzLrGbxB6v77oAE5ZCU73%2FvSl0%2F3kjnBa2vdOordF%2BUpjGF0cuMlcRo2vtdEbGAEu0%2BhhShtpfS%2BgpInLQQDfXj%2B3bV7TGewTthQ9dY8q17oo8yoso44RIVO4k2GIa6DJirhg9aSNlo40MVpDE3NhCmQceefJdcmhKQv0pUSC3WDbCgVkKiiVADapTlWLKTnl%2BqtdhK718Tex%2Bt%2FEctQhMMpZqlNgGF88OqzNohVaOaWvpjq0S4H%2BLHGO%2Bd6IIxhEoj5MSAlRM26YJ3rWlpEFRd%2BCwyWN0495X%2FpKm5dRIJHa5NXMZFVnJS9tXXLqFTuFrtA8AhWA3gkqqRElqnTdknTVTyTlZ3QtlzrC0lZwgYG0maQ51G77qcLahbx1sX5HlbaIRDQZmZ2pxd0gX40TpKJZ1eyZF%2Fpqigg8%2FI374nlKBNAUVNLZDkd2jo%2F5c5fsGKp%2BfDf9BPVcWHq7dkibb3OELIkQ6YcTrqVwU7lb6HGK4H6fPvjCb1f68BjqkAYdYerwJ97pq3q61wssI9mCijJyZ5h8%2BSMauYrckKscCFweUBGIQi0LZyD6Vs6lWGKa3gPKTR4byskVSNG9D6qk3K5uNlfqWxmVnQGTD8fkfIE6PIDDyqdWb2S4rh1X2ZTxrJ9bvQB51cgK5ARp8Z6%2FS8O0v%2Bv1qHHWozc37tjg%2FnOEHzT%2FPAyVGgWSos%2Fye6fMyIZihINZEBbVC%2BSZBYEn70lYP&X-Amz-Signature=06520ae1ea1b1c8ad16be8aa0cc903fc156d1e2f7625005d59cf4b5271bc318a&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Algorithmic Libraries
#### 1. **Scikit-learn**
- **Description:** Contains tools for statistical modeling, including regression, classification, clustering, etc.
- **Built on:** NumPy, SciPy, and Matplotlib.
#### 2. **Statsmodels**
- **Description:** A module for exploring data, estimating statistical models, and performing statistical tests.

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c62885f5-417d-4179-834f-d68f8f2bdf39/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RX4GOJAK%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T181844Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC6nunrJiameFmAxcfQdnkDty1g4wDxIH%2FGL07xykVpzwIhAJEIdGIV9Oo6Ow5C18pAPv3DynprbcHc0B8gOFOBOgtxKogECPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwyhBL1rQvyVVf%2FVuEq3AOW%2BdOO34YWFye00dJSBXjQQPx%2F%2BSCjQD7I2hsN2KJ595oitHIwazQqRvh2rZR8COn8w9ifNFc3ege3XQyWvvJKHyCA%2BtusQ5wpnVCgrfA%2FQvBDWG9ZAEvlDU1qTJ8oUgpwEds2S6LzLrGbxB6v77oAE5ZCU73%2FvSl0%2F3kjnBa2vdOordF%2BUpjGF0cuMlcRo2vtdEbGAEu0%2BhhShtpfS%2BgpInLQQDfXj%2B3bV7TGewTthQ9dY8q17oo8yoso44RIVO4k2GIa6DJirhg9aSNlo40MVpDE3NhCmQceefJdcmhKQv0pUSC3WDbCgVkKiiVADapTlWLKTnl%2BqtdhK718Tex%2Bt%2FEctQhMMpZqlNgGF88OqzNohVaOaWvpjq0S4H%2BLHGO%2Bd6IIxhEoj5MSAlRM26YJ3rWlpEFRd%2BCwyWN0495X%2FpKm5dRIJHa5NXMZFVnJS9tXXLqFTuFrtA8AhWA3gkqqRElqnTdknTVTyTlZ3QtlzrC0lZwgYG0maQ51G77qcLahbx1sX5HlbaIRDQZmZ2pxd0gX40TpKJZ1eyZF%2Fpqigg8%2FI374nlKBNAUVNLZDkd2jo%2F5c5fsGKp%2BfDf9BPVcWHq7dkibb3OELIkQ6YcTrqVwU7lb6HGK4H6fPvjCb1f68BjqkAYdYerwJ97pq3q61wssI9mCijJyZ5h8%2BSMauYrckKscCFweUBGIQi0LZyD6Vs6lWGKa3gPKTR4byskVSNG9D6qk3K5uNlfqWxmVnQGTD8fkfIE6PIDDyqdWb2S4rh1X2ZTxrJ9bvQB51cgK5ARp8Z6%2FS8O0v%2Bv1qHHWozc37tjg%2FnOEHzT%2FPAyVGgWSos%2Fye6fMyIZihINZEBbVC%2BSZBYEn70lYP&X-Amz-Signature=1614fcd0ad90dfe3bb95f79ffbb8fd4fd4bde240c830efec469fb136e9f1cfa0&X-Amz-SignedHeaders=host&x-id=GetObject)
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
