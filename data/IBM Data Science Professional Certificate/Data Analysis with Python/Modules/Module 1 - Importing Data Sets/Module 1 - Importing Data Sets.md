

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

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/997ac361-58a8-4f04-bb0f-79fea4baa761/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Z2BU4KDY%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T031923Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFAaCXVzLXdlc3QtMiJIMEYCIQCfSie8a6tR4z5rSZ6cnpHuUBOy8%2B2PUtEIOI%2B%2F0xn5wwIhALn5lrJ9wJIlznVaYJ9a4yFWtht6vANmaRhimUZGV%2FhyKv8DCGkQABoMNjM3NDIzMTgzODA1IgwHFCdmIwwGY2yznBcq3AOKmn1HlZ23DpfUhrx4ctlfSmUMRij7Mr18Kv8t2tfTsiDT7QzDQ9o0ntweP%2BoTmalC%2BSfwcs3K41ss8XSqUms7ag2Quw8LmUZLksS2BgcTDbXSOEhXhCMmVC8GH2XpJ6cGLmV1VUZIQBLIyV%2FMxyi97WnSwzlRmXeqdu3pTvZj7aLY2NJUxa8uIyIU6km1bA7Rcg6yqVQHq2%2BFSgZD8NFov%2FgO4V%2FOaglsGY6lVHNde2GpdklU3gpvYtJPcelVEGAJmJjzLlaURdDh7panvWuZVTkMTzq4NAhVJ46pL%2FiT%2BwiZ1N39MYHSKZwp6TUeYUTElE1aMY%2B59mHokE4jYuco2nQOAXJHLML%2F0CZqCNB0Q%2FPTubFF01poW6sSadYYIQemcYnes32nJJmjbUah2uC86YNECgE1TfMoaKVEPVMZUNlS04WdMdT%2FQH%2FEh2H3kSnEkwFx1Dw1yhi2LInjIUt%2BqliflFmBiCz%2BaRNrrx7M0TPBcsVsiZDn3oqLS6oc0PMKvDmlhpGdsbHoy3UpTvxf5rMtbKLPCKBmATgnnzfsi5OMOP0%2BjzSmH5mNghrGdCzrcr6LtvnAEAl6ujAjIeaI01x5ZDJ2F0UA1aTZSuhmNyP1oyn51tCSLgGYrTCampW9BjqkAZWL4oaBKXMC3iLRwKI9tC3UHBgAk3MLDZCA4Q9SpqkDBSAsLaF%2BRPHWtWZDNkv2V2cGELFq5Yyqq%2FXDEST9SrC%2BUNB7tZgu9JHoqsSbu%2BASGwi4IdL2nUmOkzuXC1N0tXDtaPEP3GoetIsOfgHKUTu18hReNieJplBBbs2%2BjsX6xa6EdGgpc1pYyps%2BIRq0FksW2quUBt4g%2FOUVCOYrF9zMgOKl&X-Amz-Signature=ac88d454f31b23e4ccd0ac2f81093972cdef88984b481dbaaddd2d862d86cac5&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Data Visualization Libraries
#### 1. **Matplotlib**
- **Description:** The most well-known library for data visualization.
- **Features:** Great for making highly customizable graphs and plots.
#### 2. **Seaborn**
- **Description:** A high-level visualization library based on Matplotlib.
- **Features:** Easy to generate various plots like heat maps, time series, and violin plots.

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/733d1e42-5a53-4fd8-90c1-3d85254369a6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666T6YP7PY%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T031922Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFAaCXVzLXdlc3QtMiJHMEUCIQDle%2ByvPk9MEmsW1gf4DCPFOb0j3fGTY0KUokAV3OLIjgIgOHkFHvvNss37U%2F66tdXubdhFqMzg3TadBsba0aVoLPkq%2FwMIaRAAGgw2Mzc0MjMxODM4MDUiDNCyUdIWqg9Jg%2FuHlyrcAzd0Hyz5b0zYZHwKeOavxoE24jodtRjGIn1WYYBuq1vgWwRx1mRfEPH%2F0yaerbM3P0%2FWT23Fi4%2B3NVn4DZ7rGEFt7lcqOpTJYkXQEB3EyKRpo6ZCjHzqf5uAxjiYQA8hmG30SR3vfxEw3HVGXfbGgKpcvH3JRN4pcAur46xXOiAUzAEqkCsdfqzy3SLsv33nGMeWA1HkRVdTkNmbD%2F1GZiPkUZTLkzREuj8b7XmDtJuxk3u0oPYwOy9IQSAhKm6wT8A%2B5wxP1gEflSLjN2b4Si5vRP1YIdZZtf7kJg9yqs86P%2FnKXPzfSOUhDXdRFapzFfxasc38I4BWGVQcAwmRtvGSLXYR6i34XEzImLnLoH%2BqYLp497b8GPzmR9jUGpN8btkzNFBblKg74CrNzhyautovuLvkJVfVYc3Qwzb3qD2zYKSbajplogaeH9Om%2BKkVDRRN8iJasD4m3SVkYhHBYjUxeZxJuqlpzgZZMaMgdSE1O3sDz%2Bf8Snx3YGDI5fdMmKvRl%2BMA9yctiQ2tfBE8wYuIq8i5qo%2BvPyf%2FgLpnKAwHg56l183WWsyBdXLMo8mCbI8X0%2BaLLDMw%2F0G9POLFKsj0ih8biI3601f5Shkf3YDfeCHoJ5V4%2Bv0zz5u1MOKZlb0GOqUB1MNzbG5U%2Fa0N8NRf0wCFkevNKSpKEZM9OQ3wPqYp0OUSLqWa8%2BZazKTyN1qmwD%2BI2LkTPojPBY2PQnGjZiDYp%2FVGQIYY7MIg17TMSLFtxPXoDrbgk3056%2FQ%2FxqJg0qbX35qhBrFnqxHZixgUf9bB5Xc3X3cz4OID56%2FznVQ2%2BjBIA%2BrI3kflnv%2FZPS7YK1Rd49ZZuppK6zE76bUIoWPscK260w3w&X-Amz-Signature=01b1aeddd7d30e3c57b0c677f9f041ee04b2b7d681688983b0ec790964478e2b&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Algorithmic Libraries
#### 1. **Scikit-learn**
- **Description:** Contains tools for statistical modeling, including regression, classification, clustering, etc.
- **Built on:** NumPy, SciPy, and Matplotlib.
#### 2. **Statsmodels**
- **Description:** A module for exploring data, estimating statistical models, and performing statistical tests.

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c62885f5-417d-4179-834f-d68f8f2bdf39/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666T6YP7PY%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T031922Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFAaCXVzLXdlc3QtMiJHMEUCIQDle%2ByvPk9MEmsW1gf4DCPFOb0j3fGTY0KUokAV3OLIjgIgOHkFHvvNss37U%2F66tdXubdhFqMzg3TadBsba0aVoLPkq%2FwMIaRAAGgw2Mzc0MjMxODM4MDUiDNCyUdIWqg9Jg%2FuHlyrcAzd0Hyz5b0zYZHwKeOavxoE24jodtRjGIn1WYYBuq1vgWwRx1mRfEPH%2F0yaerbM3P0%2FWT23Fi4%2B3NVn4DZ7rGEFt7lcqOpTJYkXQEB3EyKRpo6ZCjHzqf5uAxjiYQA8hmG30SR3vfxEw3HVGXfbGgKpcvH3JRN4pcAur46xXOiAUzAEqkCsdfqzy3SLsv33nGMeWA1HkRVdTkNmbD%2F1GZiPkUZTLkzREuj8b7XmDtJuxk3u0oPYwOy9IQSAhKm6wT8A%2B5wxP1gEflSLjN2b4Si5vRP1YIdZZtf7kJg9yqs86P%2FnKXPzfSOUhDXdRFapzFfxasc38I4BWGVQcAwmRtvGSLXYR6i34XEzImLnLoH%2BqYLp497b8GPzmR9jUGpN8btkzNFBblKg74CrNzhyautovuLvkJVfVYc3Qwzb3qD2zYKSbajplogaeH9Om%2BKkVDRRN8iJasD4m3SVkYhHBYjUxeZxJuqlpzgZZMaMgdSE1O3sDz%2Bf8Snx3YGDI5fdMmKvRl%2BMA9yctiQ2tfBE8wYuIq8i5qo%2BvPyf%2FgLpnKAwHg56l183WWsyBdXLMo8mCbI8X0%2BaLLDMw%2F0G9POLFKsj0ih8biI3601f5Shkf3YDfeCHoJ5V4%2Bv0zz5u1MOKZlb0GOqUB1MNzbG5U%2Fa0N8NRf0wCFkevNKSpKEZM9OQ3wPqYp0OUSLqWa8%2BZazKTyN1qmwD%2BI2LkTPojPBY2PQnGjZiDYp%2FVGQIYY7MIg17TMSLFtxPXoDrbgk3056%2FQ%2FxqJg0qbX35qhBrFnqxHZixgUf9bB5Xc3X3cz4OID56%2FznVQ2%2BjBIA%2BrI3kflnv%2FZPS7YK1Rd49ZZuppK6zE76bUIoWPscK260w3w&X-Amz-Signature=968d775029d86119e6845c6f313a9335ebd1b8ef3af73d2ecb683f57e1bc01cf&X-Amz-SignedHeaders=host&x-id=GetObject)
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
