

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

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/997ac361-58a8-4f04-bb0f-79fea4baa761/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SW5JKFNP%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T101549Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBIaCXVzLXdlc3QtMiJHMEUCIF0ykw6CF2MljfOsWl0jWV0owaM3UNKfob%2FrT77nZmqPAiEA6pJ7RqDT1poSp9TedRNRGk4wlaDODeHCswRuTJtNGi4q%2FwMIKxAAGgw2Mzc0MjMxODM4MDUiDPRz8lnBoKYpHNVEfSrcA9ynPYd2u1DelGGwB3KvK8e5QGlE4wxAFaJL%2B%2B9zATOAdxNvEpSKQn0%2FHltGx7vvL0xVh3Nn2%2BSnaxHcSCB6MJClz1QEWKPi8kdNDTNP75ohhRpl7eoRZxjHEiJOAsVEIBmoBWsnBdUY%2BPnPv8bwPkRkGejtmxF1dM1i5srDCZ77K4K%2FGkvcgcxZ4uMcdeOHwQL15JJICceV1IGDAXqGXm1UAaKh6SAeCh5qGBQSM%2BCrePQgfn%2FWNuePGp7iFZxKpbHuB4UUqiPq7Tosq7bT324PgvGeraab0zj7AQA%2BnZnJD8Rm%2FyUE1yJOZ%2FVBCsuubSzQgB7NB6QLUFj%2FnzfvSzxQLXRfQI8UYcqpDw91aI2MZIa4fcJK0blxReRjEpSf0RqU81nCxWCsrybBZHohMEwp%2F%2FdO2glJd8d8HrDh5temfV9uIzxuLIU6K6RvczcMZO%2B34Mo8COchIT6GmSsSdI8C8rx48dJj68Qm5g7DS%2BM3knb8woaqIXL9%2BRzTckp9UT0IPyN%2FiBOC3mvrbitCb8%2FCo10cIsAb0WAEY1aG0XjI3gFTrr3FL%2BtdLHZyyiy7GKChYb78tLFvpWjlU7cjn%2Bu6lbc0PMdaJUZ18XNzW7HkC%2BTBk3Q6aHI%2FfUsXMMnKh70GOqUB8a6tHHNfmo3LRo8TzWita4OCKyie%2FMmGugHcJYUKxTGkWpaS7tRC8XUwVaI4Q08C7DKMKMU1iZz1GdJNWD%2Fdf0WAgkWanO0R%2BnPljQ5c2X8TgnslwXLHNUyh%2BT20eLvp7%2FAqteeKRuhV3UF6bSEPIxNgtb5SYG4Xt96hP6T4CaFFMNJAzs%2FmjDpsGge8YH4B7np%2BL3VBTnbvdxz7P95uyOmjyppU&X-Amz-Signature=a2a6b083bb5723e14c91aad9323cfa8ba1e2b240d525bdc24e18ad3839665eba&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Data Visualization Libraries
#### 1. **Matplotlib**
- **Description:** The most well-known library for data visualization.
- **Features:** Great for making highly customizable graphs and plots.
#### 2. **Seaborn**
- **Description:** A high-level visualization library based on Matplotlib.
- **Features:** Easy to generate various plots like heat maps, time series, and violin plots.

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/733d1e42-5a53-4fd8-90c1-3d85254369a6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WXWBV3DD%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T101548Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBIaCXVzLXdlc3QtMiJHMEUCIQDVCVpMAPYLdzPTmJu2%2FLMKtFtIA9ailiLTJ3HyQgFkuwIgCpeCFRGLNijq3q6sNH6TQX4ExSL13OFCPmHC75ehTVQq%2FwMIKxAAGgw2Mzc0MjMxODM4MDUiDN%2FqErHDuJIQ4%2B9p4CrcA6E7KG8zM%2B32r9VEgPRotAp%2BRU%2B2FuzR%2FJjPz9VZuwZQjoLgFGvsRUiI6f4f8gjn16G5CKnbkpzDHsZCeL0OlhiquGzrxWndLCu6OB6wFCBs50ZTRFVdKo4%2FexmVhh7P2Qp%2BDbZH4nlL4XdKph0PUFI6ZPRuNdeaBGjSgSHdnzYpbTcG4xUClQyB0s2obbWnDBKSjpx1H9HPu%2Bbm5VTbl7RCi8UvR5CFX9qtrKGvmNoYUXT9KpWOK2i45%2B%2FQaVdnTDsBYBObhY0WxI4128Rk6TEpmHqjEGksILVwPVrGYwoz2n%2FUzrWD9%2BoUk9l%2FTSkbPfhZcoDWyA9rCkFwZZgtrVeHuwMcTf51Nwz5UZ5jkZhVvFLLK025VAftK1SScL7iOSy2iSn7ftVhPbLTSPCez3aTGU1jDJkfl5d2EMQfWwRITQqK%2BGIxiiQJM3eM%2BS4x%2BmJyZzNwHesf3v1COqcfbskHd94%2BCodGhCuN3n1jkB%2BCnaZDqxYQSqMWYKv22KXYRXaXV5%2BDKPZi7qsatNc1xM5VYT3sYc5Q93TD%2B0m7hmCkpl88581lVtzMY5eJN%2FkJtaRDbS3kFhRAGdkQ8PT2BoQhRce%2F7FYE2xz1jVjV8U3qcGXVTgP9ubajBNpJMNrKh70GOqUBr%2Bo%2Fc48QvamASeWuRjkYgYkipyMUDyFIm88OOqsFKYCIqdEhrGgC%2FrLi9K0qmEhpEXLSlPX5wG%2FneJ%2BcKHICE14orkCrOnMP0m5YMWdfP0mCEHO5wJJ%2FZ3FtkfxSpBn7tMHJ6FXW%2BWis7%2B5XN128Xt%2B%2BgyQEIPHyyLEYXEZ5nsZ1yJ%2BNWfOt6KTox%2B4g4IRiWa0eZVa1NhMPl9Mn9YY6mT0C9nco&X-Amz-Signature=36af65e5ffb1901cf81342997436ffc296198b750cc2ad76960cbef7a027becc&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Algorithmic Libraries
#### 1. **Scikit-learn**
- **Description:** Contains tools for statistical modeling, including regression, classification, clustering, etc.
- **Built on:** NumPy, SciPy, and Matplotlib.
#### 2. **Statsmodels**
- **Description:** A module for exploring data, estimating statistical models, and performing statistical tests.

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c62885f5-417d-4179-834f-d68f8f2bdf39/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WXWBV3DD%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T101548Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBIaCXVzLXdlc3QtMiJHMEUCIQDVCVpMAPYLdzPTmJu2%2FLMKtFtIA9ailiLTJ3HyQgFkuwIgCpeCFRGLNijq3q6sNH6TQX4ExSL13OFCPmHC75ehTVQq%2FwMIKxAAGgw2Mzc0MjMxODM4MDUiDN%2FqErHDuJIQ4%2B9p4CrcA6E7KG8zM%2B32r9VEgPRotAp%2BRU%2B2FuzR%2FJjPz9VZuwZQjoLgFGvsRUiI6f4f8gjn16G5CKnbkpzDHsZCeL0OlhiquGzrxWndLCu6OB6wFCBs50ZTRFVdKo4%2FexmVhh7P2Qp%2BDbZH4nlL4XdKph0PUFI6ZPRuNdeaBGjSgSHdnzYpbTcG4xUClQyB0s2obbWnDBKSjpx1H9HPu%2Bbm5VTbl7RCi8UvR5CFX9qtrKGvmNoYUXT9KpWOK2i45%2B%2FQaVdnTDsBYBObhY0WxI4128Rk6TEpmHqjEGksILVwPVrGYwoz2n%2FUzrWD9%2BoUk9l%2FTSkbPfhZcoDWyA9rCkFwZZgtrVeHuwMcTf51Nwz5UZ5jkZhVvFLLK025VAftK1SScL7iOSy2iSn7ftVhPbLTSPCez3aTGU1jDJkfl5d2EMQfWwRITQqK%2BGIxiiQJM3eM%2BS4x%2BmJyZzNwHesf3v1COqcfbskHd94%2BCodGhCuN3n1jkB%2BCnaZDqxYQSqMWYKv22KXYRXaXV5%2BDKPZi7qsatNc1xM5VYT3sYc5Q93TD%2B0m7hmCkpl88581lVtzMY5eJN%2FkJtaRDbS3kFhRAGdkQ8PT2BoQhRce%2F7FYE2xz1jVjV8U3qcGXVTgP9ubajBNpJMNrKh70GOqUBr%2Bo%2Fc48QvamASeWuRjkYgYkipyMUDyFIm88OOqsFKYCIqdEhrGgC%2FrLi9K0qmEhpEXLSlPX5wG%2FneJ%2BcKHICE14orkCrOnMP0m5YMWdfP0mCEHO5wJJ%2FZ3FtkfxSpBn7tMHJ6FXW%2BWis7%2B5XN128Xt%2B%2BgyQEIPHyyLEYXEZ5nsZ1yJ%2BNWfOt6KTox%2B4g4IRiWa0eZVa1NhMPl9Mn9YY6mT0C9nco&X-Amz-Signature=eb9711a5529c584f65964bada36a6b00cdfc018c7be4500daebc7e345a5ece86&X-Amz-SignedHeaders=host&x-id=GetObject)
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
