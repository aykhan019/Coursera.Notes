

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

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/997ac361-58a8-4f04-bb0f-79fea4baa761/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YAAXPS32%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T101602Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECoaCXVzLXdlc3QtMiJHMEUCIQDtZD3aVlEMF54%2Be88BprRf8OSU%2F%2BgZmnLeXMBB717gXgIgDNMNhvOpjdqT8YA%2BEQCzPamRupurKeW0cMiCPXLpegAq%2FwMIQxAAGgw2Mzc0MjMxODM4MDUiDGvTJ6TVKX0JnKzNJSrcAxdxz%2BwmrcTzjWR2wwiyEis2KJm42xJf9jY%2FckI%2BziRMJLMbWStHgWx0gk6xgCnnq9dazQiWDFZ5wSPnsi3G3wV41vu3lxzeQvn7MjM0ZcdE11%2FwsPb%2Bh99FX6mdcx%2FlD9XNmUJQHe%2FoA%2B5Rf4WT9US6o%2BUOcsXaa5vkHeuJgD4t63zkMzmc9%2BkiQBnS3g8%2Bxy3gfbFxh8hOzgzj4CHbm0fN9pJ2fdnp1T6zGUuYAm7ZVnsEvPtsz5Z5SVgxuUbS5IZC%2F3wlv9odUZIo8LiDpbhkIAsfCDN030yS7u1gq%2FTvBd2qJv0tCustFgHuqYM%2FLdGwC1mSBCLPVBrS%2B8m3BfK4RV4UZ8%2BYw6uIu8vMt4fr98XmDMcfchK9PWgLA8KE434ZbekwkEtXACijkMLV80ep7%2F8WZi73Zdd4HnaZcvehwYmlTEOc%2BnF8i9BqnJZz1hq%2BMfjvqGwvOnE1dij2uew7KsFdBWvq3Y30HHWmiI3XE6J3nqQUYZ1suW8aEAM2wnkoDu642DYs9IEESKkblCeluLEUoUpjkAvIxXw6n5ek%2FGqmEJ40evEgTq52Uwo%2BGI78S547QB04p8gdtRBylerE3Ne%2BpictD1Mo9oUja5MnVCQQAQ%2B72ctVYvHnMI3vjL0GOqUBorwrQFMmzsjVYmemnYYyldkXKs%2F1OjaUlNbM1sZNhqcsJMEu%2BpPgDhckPKJ7liZ9oc2Wa2zqpHDYO%2FtnZG74VMjZBxRgn1zuuwxVstgS0fcq2jYFFQhlCe6vXcI%2BuHFoXPfOBNLffXYudZSsxhRXcy0uVPiqWjHzgZiqj6bGCzXbF5WFFO7QPPmR0Gg9pVqILNA5gZ9LWUZCOdwZ1VbTq%2BUqVAgJ&X-Amz-Signature=31d2061d3ee679722ccbae60909224ddf818a8706c6ae20323dedf6504f12ae4&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Data Visualization Libraries
#### 1. **Matplotlib**
- **Description:** The most well-known library for data visualization.
- **Features:** Great for making highly customizable graphs and plots.
#### 2. **Seaborn**
- **Description:** A high-level visualization library based on Matplotlib.
- **Features:** Easy to generate various plots like heat maps, time series, and violin plots.

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/733d1e42-5a53-4fd8-90c1-3d85254369a6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46625B35V5P%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T101601Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECoaCXVzLXdlc3QtMiJHMEUCIH1F6ikhgvEDi9C3mTOFk5jf1FYIzkKLZYuPSC2SvnzUAiEA6il8OE2zIbNV9MZG78%2BqYmr0wl3IFwdXZTwfny8YKSUq%2FwMIQxAAGgw2Mzc0MjMxODM4MDUiDJIJV35tBhDHdVQXPSrcAxJH8UDrF9CQRTqPklA5W3b2A7qblzg17Z02Lac90XN0MvGnArEAN7b3fzgAbAi5MrvBwvHREprfaeL04ZU1jCsBsZPJ%2FORmawsIylWVjwvLzmekubg1O%2FvtCsm%2FPKnTLB2NFnylj8CKbyVPraiEHmNC3lWHNpBIJZBLyKTS63RTh1n%2BajqMKsWv8AVkwRbZLhdbjLLLpKXim3a1Ix82m%2FJIEopvlaDI0HikDEh3ErdJ1KnnsTaUnnm2qsY%2FMhu9%2FBaM8db%2BEPAlA4CW6i5YFTgLps1ZFLS7BQet0qyy25Yd4QhQ097fOPaiXIZVT%2FE%2FnZHMs8ms%2FjxZSgmlrMHJonK%2FZhcGUa%2FOg1gFKhB0L6oZMTluK7f2YuyQ3wby%2FkTnzdkjq6GQNHeIXow9wnYomR7PuVz0uW%2BJ1soE0m8jsdvjR5Bzueq6xroIPzbUtMlYcxtZooE07mDsy%2FYGYGVdVAGB4DtHVTxQnwZjOE5BPDFYzSQUkVBl0ou%2ByDq8bWTjtKzOJn5Zv8jaDEA%2FUd48GGF3CoEZbipqwpIboVxjLqO%2B%2BuRAk5ptFn00IM2jLXpITrSQnZ8mAT83N5JcR%2BEYhMS1mwDgpNrfaJJWAQOOHbAPPBGE51XOlrGrcocEMKPvjL0GOqUBPrbmlZnlxyk7i7Kp46ZBLsixglL3xfPnNYYGm8GQYYDd5tFR5bXxM8KDrV80%2Bux2w68vNkWFF5Xap5a2vf5yE3bY254DERGYyVL422N5Qyls1ld%2BPI1AVxO7xTxSZXQ8784lEZ%2Bd9F3SwbEYmvZVmzoOdQ%2BxJw10DYrwwN3kNXnI7mw4twRMC0qNagJYSCL2U4VZNSwkHIsFp0UiyPB0phICV9Fe&X-Amz-Signature=327a623e3e08a1944b0546803585dbc208471fee57cd9b3299461d1100d91777&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Algorithmic Libraries
#### 1. **Scikit-learn**
- **Description:** Contains tools for statistical modeling, including regression, classification, clustering, etc.
- **Built on:** NumPy, SciPy, and Matplotlib.
#### 2. **Statsmodels**
- **Description:** A module for exploring data, estimating statistical models, and performing statistical tests.

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c62885f5-417d-4179-834f-d68f8f2bdf39/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46625B35V5P%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T101601Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECoaCXVzLXdlc3QtMiJHMEUCIH1F6ikhgvEDi9C3mTOFk5jf1FYIzkKLZYuPSC2SvnzUAiEA6il8OE2zIbNV9MZG78%2BqYmr0wl3IFwdXZTwfny8YKSUq%2FwMIQxAAGgw2Mzc0MjMxODM4MDUiDJIJV35tBhDHdVQXPSrcAxJH8UDrF9CQRTqPklA5W3b2A7qblzg17Z02Lac90XN0MvGnArEAN7b3fzgAbAi5MrvBwvHREprfaeL04ZU1jCsBsZPJ%2FORmawsIylWVjwvLzmekubg1O%2FvtCsm%2FPKnTLB2NFnylj8CKbyVPraiEHmNC3lWHNpBIJZBLyKTS63RTh1n%2BajqMKsWv8AVkwRbZLhdbjLLLpKXim3a1Ix82m%2FJIEopvlaDI0HikDEh3ErdJ1KnnsTaUnnm2qsY%2FMhu9%2FBaM8db%2BEPAlA4CW6i5YFTgLps1ZFLS7BQet0qyy25Yd4QhQ097fOPaiXIZVT%2FE%2FnZHMs8ms%2FjxZSgmlrMHJonK%2FZhcGUa%2FOg1gFKhB0L6oZMTluK7f2YuyQ3wby%2FkTnzdkjq6GQNHeIXow9wnYomR7PuVz0uW%2BJ1soE0m8jsdvjR5Bzueq6xroIPzbUtMlYcxtZooE07mDsy%2FYGYGVdVAGB4DtHVTxQnwZjOE5BPDFYzSQUkVBl0ou%2ByDq8bWTjtKzOJn5Zv8jaDEA%2FUd48GGF3CoEZbipqwpIboVxjLqO%2B%2BuRAk5ptFn00IM2jLXpITrSQnZ8mAT83N5JcR%2BEYhMS1mwDgpNrfaJJWAQOOHbAPPBGE51XOlrGrcocEMKPvjL0GOqUBPrbmlZnlxyk7i7Kp46ZBLsixglL3xfPnNYYGm8GQYYDd5tFR5bXxM8KDrV80%2Bux2w68vNkWFF5Xap5a2vf5yE3bY254DERGYyVL422N5Qyls1ld%2BPI1AVxO7xTxSZXQ8784lEZ%2Bd9F3SwbEYmvZVmzoOdQ%2BxJw10DYrwwN3kNXnI7mw4twRMC0qNagJYSCL2U4VZNSwkHIsFp0UiyPB0phICV9Fe&X-Amz-Signature=e2832e09ae928ec6c061af1fbe540b5cd2846712a71b6d1dc2525a4fc8de9b17&X-Amz-SignedHeaders=host&x-id=GetObject)
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
