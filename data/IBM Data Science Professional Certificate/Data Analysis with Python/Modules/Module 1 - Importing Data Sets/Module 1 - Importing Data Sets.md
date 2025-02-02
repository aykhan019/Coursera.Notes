

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

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/997ac361-58a8-4f04-bb0f-79fea4baa761/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Z3S7APWY%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T131501Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDwznv7kAdeH92A%2BPXdg3o%2Bx5sGc6cl80cSpk3SpmL1lQIhAMcj4rdePfUE%2BNjBWZj8vPQ1lhKpCNHOTpXqnKmLc0WUKogECO3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwFnug3vzhtkyZ7NLQq3APuT370NmuesCsW%2BTPEUQl123qNRQOtTjilvPbKwBXTfSiaptjTo%2B%2FI%2FiNgdqMGALUqlUVxgBQKPZTKkNCpRe6QpROpncPyhsrKySe4aVsSmSEHzxT%2FLliWbg3bRc9Mr02jbOug5sh9eXl4gVY5m%2Brpxl0Xssyquw%2FyTsrI20lTN1m662CTKjcJMgXSf2j9rUXbVjJfVeYk3zH8Glhs6v1ptmJvpFIzA9hGqm%2BFSMYntAlrxuw4nlsGUG7uqCflaoghPV%2FjoaBvXbJm5gsIftZmSQhZXu%2FrRF78nU%2FRiY7IDQBRFODD89xsIWbLnXhL4QnufkP8596rfNUFfhoT299dpTApim%2B7MWri%2BFfdcHMgtSOxKh7frtJjRm6bmcdeW8amJ5nRk6Dl6pi7xHxqmvYVSY4uxUSlTVzGFqd2VEgjF%2FwK3kk3hf%2F1FcgLykYCr0oT1f6ixT3mA%2FsWLbZaD5X5gE7OovG%2BwCo1dqNfDWV5RXKXLKcCRFk%2BLLD3wvHkAWfCxpiZforjDHaCqlZdVCsYeEPFdKpJuUHw9TB6%2Bk40Tu1UyhMzn7IqUsZDleQ0Gr7SVmbkohxODbLiM4dscbZU5ZdYkpEASG%2Bn8XX3CwxC%2Fs%2B0fIGfNf7YXikaeDD2vP28BjqkAVa%2FqRIEJZ3Hx%2F1uKwvsuCmc3jb7k%2B%2BOvdVKkkf4T07ycuYzaSDMxdtCZ7XUJmZj99cEEUk7EQOQoTx4cM30%2BipjDKPEOo%2BV1YgYCofLpODism22AQ%2F8RLPTuZpmOlXRVOFtTsEgQp66vesG5hMCXEsjJteBpxEeA3sVtNpZNlP2ov3wtke5ZMfo0G2cVtAq9%2BUujT6Ob%2FgG%2Bm5Q9iEnpTt0fFMw&X-Amz-Signature=489e1ea1faec81c6c42999c7231b03bcd13e164ee5ba4f6b14a47ac5d7157308&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Data Visualization Libraries
#### 1. **Matplotlib**
- **Description:** The most well-known library for data visualization.
- **Features:** Great for making highly customizable graphs and plots.
#### 2. **Seaborn**
- **Description:** A high-level visualization library based on Matplotlib.
- **Features:** Easy to generate various plots like heat maps, time series, and violin plots.

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/733d1e42-5a53-4fd8-90c1-3d85254369a6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QLH3Q4ZL%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T131500Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDuEsZhXXe7ZZVzxIBEqQbHlM68dRBaI9Q%2FRAR8iTqnRAiEA83PSEVj%2FBvdLvzfraVs2ViJrQK0GcJm7Iiy7wN%2FJ0I8qiAQI7f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNzhFzOdI1BFnPN4nircA9UxR4RR7NAwc8dxo2UjtvKSsWuRGfuS8ccmeyIvplmz8B8HhHDfrPWkej2poroLSGd%2FXy380hv9snXS19J%2F%2FjyRRgI8EhnFAFFEaKZ3EjqdYhVjs1nwZ%2FMHBltjjVTvPS3AJqgeSak4LpezZrvCz1rvAYmHD%2ByY0InE1pdoYVUurHgPuW5Hw7I6dgTSCAA2XgRWObqCfuPvqs3XAYNASLrKVQPrDCNsRKvHJrFsLwunpkfVOc4euYwk0SLIDVopaMGqBDsMFTcK%2FTK2xsk09Q12TwGy32SGyCR1Rj0386lEBSHMy%2FYbzWSpj404tptZBClFf4rRTdJ%2Bj2hKi5Za71nXBfSvwmeUSIfiwzIBRL6SeyFQwmi9SPjKBMGGM6TI64iunLbStr%2BphYiTxZzP%2BhpSNs7BV9EVhiQTwZybu7HADeIYItoWXWMtnk6HQGsPeDNv7QMdY%2BhzznRsfnnZDuil4zccNuGdPyzm5EDSpBs%2Fq0kzCyUSRznDhMKMvDaEIkgxuuxyq9%2BLbdhpNdj9B9%2BI22ekn%2FTJnkugRe8VWk9TK1UEnQNRLDIiPmcPLLvKn5j7GHj1pg2ulbfYLPkGmCIdJoJcwYJEFE3LUrj1E6J8g0uHzEMES7pUw1VmMJq5%2FbwGOqUBRB1KxIurlu9yVgIjy85zcSVzpjTJ5oPx5geFvBrhr8dvagrx75XJC93W3gAA1%2Fy9TXc2CMXFoVnewa9DRRV56r6zHN%2FyK7NqhPN6wn8a0YpaqoFis%2F5df10yjarPfFFhzpCl90eQK8%2Bd%2BMv48Wz8RNauSByJmfQTWSXrN6cT4ptzERK7kLFnFSdycgef%2FIap7x5ubI5tqIoSXdXnc7qWflL1jrGc&X-Amz-Signature=6b8aa390b20198efc128f08318e69b06d82074d9c5c2524116977fc91407fee8&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Algorithmic Libraries
#### 1. **Scikit-learn**
- **Description:** Contains tools for statistical modeling, including regression, classification, clustering, etc.
- **Built on:** NumPy, SciPy, and Matplotlib.
#### 2. **Statsmodels**
- **Description:** A module for exploring data, estimating statistical models, and performing statistical tests.

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c62885f5-417d-4179-834f-d68f8f2bdf39/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QLH3Q4ZL%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T131500Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDuEsZhXXe7ZZVzxIBEqQbHlM68dRBaI9Q%2FRAR8iTqnRAiEA83PSEVj%2FBvdLvzfraVs2ViJrQK0GcJm7Iiy7wN%2FJ0I8qiAQI7f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNzhFzOdI1BFnPN4nircA9UxR4RR7NAwc8dxo2UjtvKSsWuRGfuS8ccmeyIvplmz8B8HhHDfrPWkej2poroLSGd%2FXy380hv9snXS19J%2F%2FjyRRgI8EhnFAFFEaKZ3EjqdYhVjs1nwZ%2FMHBltjjVTvPS3AJqgeSak4LpezZrvCz1rvAYmHD%2ByY0InE1pdoYVUurHgPuW5Hw7I6dgTSCAA2XgRWObqCfuPvqs3XAYNASLrKVQPrDCNsRKvHJrFsLwunpkfVOc4euYwk0SLIDVopaMGqBDsMFTcK%2FTK2xsk09Q12TwGy32SGyCR1Rj0386lEBSHMy%2FYbzWSpj404tptZBClFf4rRTdJ%2Bj2hKi5Za71nXBfSvwmeUSIfiwzIBRL6SeyFQwmi9SPjKBMGGM6TI64iunLbStr%2BphYiTxZzP%2BhpSNs7BV9EVhiQTwZybu7HADeIYItoWXWMtnk6HQGsPeDNv7QMdY%2BhzznRsfnnZDuil4zccNuGdPyzm5EDSpBs%2Fq0kzCyUSRznDhMKMvDaEIkgxuuxyq9%2BLbdhpNdj9B9%2BI22ekn%2FTJnkugRe8VWk9TK1UEnQNRLDIiPmcPLLvKn5j7GHj1pg2ulbfYLPkGmCIdJoJcwYJEFE3LUrj1E6J8g0uHzEMES7pUw1VmMJq5%2FbwGOqUBRB1KxIurlu9yVgIjy85zcSVzpjTJ5oPx5geFvBrhr8dvagrx75XJC93W3gAA1%2Fy9TXc2CMXFoVnewa9DRRV56r6zHN%2FyK7NqhPN6wn8a0YpaqoFis%2F5df10yjarPfFFhzpCl90eQK8%2Bd%2BMv48Wz8RNauSByJmfQTWSXrN6cT4ptzERK7kLFnFSdycgef%2FIap7x5ubI5tqIoSXdXnc7qWflL1jrGc&X-Amz-Signature=8eb30d21e9db9015b74f966c92e4cc65bcb99081beab0de5bd55a8bc688aa0b4&X-Amz-SignedHeaders=host&x-id=GetObject)
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
