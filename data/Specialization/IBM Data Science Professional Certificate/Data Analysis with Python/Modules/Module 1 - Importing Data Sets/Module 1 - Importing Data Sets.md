

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

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/997ac361-58a8-4f04-bb0f-79fea4baa761/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RHFVL7XK%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T231439Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFYpBi2kZWiC4pOSV2zonCHtH%2FV5ZTd6kHGWDRLiffFhAiBnGg7F73eMI0U0WlKTSu%2B2sXrJDhBfQ0TCI2JgycVcciqIBAiw%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMlhadz8QQlm4zf3ubKtwDMUlYpEzLTq6rLDVo7WncI%2Fcg5Qjzev%2F2ac%2Feo53Mv5wZtDqu5%2B8RStaPHQRbepHC3ZsJYrfkKORZXJrNMW0NYBMuVzkNRmkpiam2XVQxPKe6xVOrik1wgk20cOlU1PwGEmBBpb%2FICyF063w8zucpS9XxbtYK5%2FLxAXHi8u7acPBl8xWfa4Dmn0aZhENF8%2BV0f7OxuYBhMcXu8niC3Z1yXPBP4MeT5YJgVsljlG%2FD%2FyZTvmCTPU6idHK0ZMwS%2BqFtc1LqIfaERiNqBXKujwapVD8P9V106rz85ifX%2FL5Y1jEN2LcxG2C11uqHhEBs%2F3XlFhR1YhEKOZyC6DMuU%2FdgBAAiq7eI%2Bt17zlGQGj3pgR3uTC3EvZAl05%2FM7e1%2BZhDPNm7m1%2F2soSzploAAp5v1MUzzdECT%2BgnghuIOCHJAMi0zDRVArd65jnND3NBZL%2B7eSmUy1ETQhZJ8xXXYE5jOw4zRxOD7Q28le4hoc5c%2BHU%2FmTFxgBYDd0hSzfMZZg69%2BdHDz5XXIxsYWDFSSfwMVOpSACPf%2Fdw9djucMEfDqENVf7BBWztJ%2BETn5NljxMfpHeG2gp%2BfsnnthWqNZ27dF1FIeaA%2BEQSrD5kL6luyOiUkI3ju1kyL9RRIvQ%2F4wtP3vvAY6pgGMm42%2Bnd27ADnCLJ1l4VP7o5N1PlWGwifN9c3JUltC1Uw8DrTHJJnszfkLgGDv7EqMKW%2Fu8Mi8SgzFeJHhpjIbsxE9ItTszp%2FHIdLUoGnk6GFrOPId2lNZx0ePWn9IHqet%2F3PI16kMwDoGFjdCfV9wqs0Tv5mgQRhnwVYZ8e23xZ%2F42bOU0IfjxQlujHQFedg4O0gEcu%2BCXHFbbzU24TiA40ELB%2BCH&X-Amz-Signature=d293001ae6dcfa054d82f85dd9a244364a92022746b390e47c1cfabe26906830&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Data Visualization Libraries
#### 1. **Matplotlib**
- **Description:** The most well-known library for data visualization.
- **Features:** Great for making highly customizable graphs and plots.
#### 2. **Seaborn**
- **Description:** A high-level visualization library based on Matplotlib.
- **Features:** Easy to generate various plots like heat maps, time series, and violin plots.

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/733d1e42-5a53-4fd8-90c1-3d85254369a6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XEYS7VIX%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T231437Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICrSm88J3tXbhBtyr0frEJqzrzFFolO6JtUV3SC7PkEeAiBnGNL9EbYJdyLXVWo70wIs8d6L5vyDDMIX4ndkc8O5HyqIBAiw%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMe35eIi0eTiLYZ8FHKtwDzOkZc4mDTLtG6%2BaGAbhnmgZeau%2FCf6BSpWTXhnM9ddzfVj%2FZx41ll3OSBvxMc9Swa5DHssQnC9WBQZm%2ByIQOfubd4QiS0Bs%2B1xjp1%2FJlXhLT6GC96P73bmcYKXzC1FWGEEoiSbnwuiXrDKj8z5AT35T7lnvlxiQUCbYbykuAnRxNiSmG2sBHBZSQ3cG0aM0c3vnyN%2FcUChL2K50wmsBWCyoI3H4XoZrxiytwyLei6K4ERTmAVc55K50Pdkpn037fuiEVVtpH7BJWPj9y7zHaW7sbwlpZ%2FlHXnulzyh5BqhSGxUT%2Fi4bzMcTI40%2FgFathJ8VcEpMMjoE3RWuGu4O%2Bg5cx6unwpIougzvoMPFEpKue08VvN27AsrgGHNbwmiBhhGU%2F7sEnffL5381ASAtzcRScHgRnzq5E9a7o%2F5jpQjL80F3WVnfcPEhW8VEGke4qH%2FKzNzpjgmkGINRjUnwizKKIjQkARNaMaQZO2Ng21ZM2pCOuSfEqYZQ02kaIn4NuZzqGKChbQh2fBC%2BR63beXif09IQexb0WRYVGm05X31kC%2B9%2FwPLTzTK0g9O32Zt1vkBipA7cSUjqZw3ksKgLujUc6kBGztN6B5azzCp07g1Ud%2FFDBuV5E1rgrSjowyvzvvAY6pgG6YLCgXmEr1ZcvMXiUaKOJGRT4Sdd3hEUCImCKcsuIXXnZstGxckSwEWno6EXLCoV64rcdL5ZyL9plk4A5xQ22BYa%2Fx8f1bt5rFekn63Xo1J8n6AQOVc4qEnpIN8LsizzQ5vDUhvOieHj7tMBWzzRFboLgEkShw3GuY4DJ6Vakz0ADZmtOf9QO3s5grnQ0mvpZA8rBZdWjRpcQLi20MvSbj8ELMtwr&X-Amz-Signature=44f879d8736eddf05bf418a19e8c64e695d08708ca4f3ad4b8e05254a80a75fc&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Algorithmic Libraries
#### 1. **Scikit-learn**
- **Description:** Contains tools for statistical modeling, including regression, classification, clustering, etc.
- **Built on:** NumPy, SciPy, and Matplotlib.
#### 2. **Statsmodels**
- **Description:** A module for exploring data, estimating statistical models, and performing statistical tests.

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c62885f5-417d-4179-834f-d68f8f2bdf39/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XEYS7VIX%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T231437Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICrSm88J3tXbhBtyr0frEJqzrzFFolO6JtUV3SC7PkEeAiBnGNL9EbYJdyLXVWo70wIs8d6L5vyDDMIX4ndkc8O5HyqIBAiw%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMe35eIi0eTiLYZ8FHKtwDzOkZc4mDTLtG6%2BaGAbhnmgZeau%2FCf6BSpWTXhnM9ddzfVj%2FZx41ll3OSBvxMc9Swa5DHssQnC9WBQZm%2ByIQOfubd4QiS0Bs%2B1xjp1%2FJlXhLT6GC96P73bmcYKXzC1FWGEEoiSbnwuiXrDKj8z5AT35T7lnvlxiQUCbYbykuAnRxNiSmG2sBHBZSQ3cG0aM0c3vnyN%2FcUChL2K50wmsBWCyoI3H4XoZrxiytwyLei6K4ERTmAVc55K50Pdkpn037fuiEVVtpH7BJWPj9y7zHaW7sbwlpZ%2FlHXnulzyh5BqhSGxUT%2Fi4bzMcTI40%2FgFathJ8VcEpMMjoE3RWuGu4O%2Bg5cx6unwpIougzvoMPFEpKue08VvN27AsrgGHNbwmiBhhGU%2F7sEnffL5381ASAtzcRScHgRnzq5E9a7o%2F5jpQjL80F3WVnfcPEhW8VEGke4qH%2FKzNzpjgmkGINRjUnwizKKIjQkARNaMaQZO2Ng21ZM2pCOuSfEqYZQ02kaIn4NuZzqGKChbQh2fBC%2BR63beXif09IQexb0WRYVGm05X31kC%2B9%2FwPLTzTK0g9O32Zt1vkBipA7cSUjqZw3ksKgLujUc6kBGztN6B5azzCp07g1Ud%2FFDBuV5E1rgrSjowyvzvvAY6pgG6YLCgXmEr1ZcvMXiUaKOJGRT4Sdd3hEUCImCKcsuIXXnZstGxckSwEWno6EXLCoV64rcdL5ZyL9plk4A5xQ22BYa%2Fx8f1bt5rFekn63Xo1J8n6AQOVc4qEnpIN8LsizzQ5vDUhvOieHj7tMBWzzRFboLgEkShw3GuY4DJ6Vakz0ADZmtOf9QO3s5grnQ0mvpZA8rBZdWjRpcQLi20MvSbj8ELMtwr&X-Amz-Signature=cdf3c4c4408336b025012ebcf7f199f0f008bcfcefa72e5aeb58e36d184949ec&X-Amz-SignedHeaders=host&x-id=GetObject)
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
