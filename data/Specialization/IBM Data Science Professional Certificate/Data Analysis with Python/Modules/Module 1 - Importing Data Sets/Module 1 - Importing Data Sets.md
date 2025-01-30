

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

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/997ac361-58a8-4f04-bb0f-79fea4baa761/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZE464S43%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T010716Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBc0C9MogwvZSvvzcH4YCjk%2Bsjh%2FjYglg1dZGwNQsJUOAiAQffirUVi1zopoMsK1Mf0504PSmiwoInkLst7gVIm%2BrCqIBAia%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMzgHl%2FaQr7yNIzoVFKtwDkJNe3fKJAwK8m1Cs5VK3gsvo2C1Z93lcpIYkOV2qur%2FwaWow5aIThFSvk6olrP9R28UU6Ow%2BvUTRsZUs65nk51tarKfbpC2KmCdpADpyrh8QuIrcns1NCMQ7I%2BPSPVpCxVHOgofbYP91AJvWu9Ms1lxuGM%2BJNhVXkYffOza8fG3jZo%2FYovfW6TVeDU%2BVgVm65rWyY7ILgvHxQPiAngihMgmfsUQNHB1Zufd8pQWp8j7xqUC%2FWB7ZF%2F0jCxmoFEJOCRYmDqNsHAP%2FYdxH8GBJb%2BnasRcREkllnFUVvMHbL23E1hY4Pf2D7Zy8p1Np28FnTWBCbdu2hv5SjGcNjLle4F6NDX1tSBKQGET4k9lK2DzyUs66%2BVuRRiWLbYlwll2cPeBQYtB220AjKXTWBNFPUmU66qFK1Mp5CY7Q9BDL4isBroiYYqdj9kFE4%2Bkcoo%2BJi%2Fe2Piy8onhsebUfKG2GBqui6VOeKXY3%2FHYoRRGTMMxzDNWzuZ55clvI%2Fgh3sOKWCPOzECQ5o%2FSWTsbG2pRd6uVF9mDHGaPZ6q6x8vsfWDKPdAHZ8wf9zqAyg0Ep9QFWVvkaaL%2Be9D4f3mRycBw6irMU82maHZKE1LYpTc77myXfMcsIlUC4eZ5KyBEw%2F5brvAY6pgGVwvpcGyob197NonYDvtCZr%2FeWHnEbYXMA3BgbclkIK2PuCqqRhFwU0K9sYWCJURLKAbE4lN9DLMwJvH0ZtBR3UvwwWWHFGyhuIMDceDTkVJa%2FHhWxVCgkCKEejmrSp5vDeYfr4uJSRxaPP71a%2Fg%2BOTzKQOxihj5HXugezlA2qnyduzUPe5dvEXa77D9FjbW4u4eqiGC80USCsj4NCz81sOHocvg1P&X-Amz-Signature=9e9de65e8c9004de8a2cc172442db9a4917ddc80d4823d10da749e385d25ca94&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Data Visualization Libraries
#### 1. **Matplotlib**
- **Description:** The most well-known library for data visualization.
- **Features:** Great for making highly customizable graphs and plots.
#### 2. **Seaborn**
- **Description:** A high-level visualization library based on Matplotlib.
- **Features:** Easy to generate various plots like heat maps, time series, and violin plots.

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/733d1e42-5a53-4fd8-90c1-3d85254369a6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VT6BVSDM%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T010714Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDLZkRjAn2xyb0pLvtqvUgUfEb9S7FJhjbKIHD%2BuhbgNgIgOeFtbZ3oiEvp1nQvu09acXCUzUUpg3PyDW%2BCLG3nuIoqiAQImv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHJRCIdwIoJR992d%2FircAwF7NEVnBX%2FbeF0Bm18WYsJZSJddkouQQT0kncpjlhbTaH%2FtTijyhgBhzPQEyNDgRR3m%2BRe5tQuZE%2BOf9JACkldRXyhSP9MyOYMlTajhdo8qHBKVJLqiof92VbYQJ7UZZnlHXjWkRxoFyLh1HKwOK5ZKI0SdS14He17Vzusd1q9Pj1Pr1UcjX%2F0RbtnkJVNmpVjfpDMf3TOQZH%2FW%2FRaCTNiXM6m2MZho9CgW2XzZi3CEO2UWh7KJ6QE%2BG%2BaBEmT2%2F5uDqYMnC7VJ%2BDbDIHYBbGNIehGD%2BKV9vH9YK%2Fz2gms3hhVvHNyfZzVXpuog9HHQ4r%2Bk%2FR4%2FHzQeaxUtR6SZ%2Bf41YGy4QMcbfHUKMI%2FdWHxaHsDNO0S4zLq4FTtTXU%2FAHep5P%2F1JY%2BKLt8PGoantLRn82KTXIzTel%2FxQZOFPMR21QhKNnUs15K1voO3tsypVtOHYl5O1rXPOHkPP5ZaLj74qhWSriVzl1En4X2eG3HVIYUzlGBaY3JMCFdXK3mDxBNAa7mkZ%2FGtq36W7YHVAVC9YLrWU3j0YpExdpLNsm8ANRTAS1Cj7ZyLQoU5gl6u5duISsHWAqaWhl72lKNtfAC9OkFtNUvu%2FGGMaBkCxHasHdkKdgICLnRegfv%2B5MKqX67wGOqUBtuAVYksQ24BZlRtEa7%2FCzCGyCsb9cDFZXlCer2%2Ba83gKRP2toCouQz5ZCpV6Jh%2FuOhFAkPAcsIlYvrIFy%2BsJ2eS0zeLaeyKS2%2FOtUlTHfRmzJ3fNJay2LFnsgAKv3o6zaMk%2Fr8kgczxKr90XQmxC9dVlypS%2FDpfBgvNT5pX5NFodbrW2IYkqnNl%2BOA7f7vCInWUG0oI66ZlhDAvCXc%2BEzvhCvUhn&X-Amz-Signature=cc08d2a98b16f4b57e12b7680bbaf71ffd64c8886bae5e446203ed970280a0b0&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Algorithmic Libraries
#### 1. **Scikit-learn**
- **Description:** Contains tools for statistical modeling, including regression, classification, clustering, etc.
- **Built on:** NumPy, SciPy, and Matplotlib.
#### 2. **Statsmodels**
- **Description:** A module for exploring data, estimating statistical models, and performing statistical tests.

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c62885f5-417d-4179-834f-d68f8f2bdf39/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VT6BVSDM%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T010714Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDLZkRjAn2xyb0pLvtqvUgUfEb9S7FJhjbKIHD%2BuhbgNgIgOeFtbZ3oiEvp1nQvu09acXCUzUUpg3PyDW%2BCLG3nuIoqiAQImv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHJRCIdwIoJR992d%2FircAwF7NEVnBX%2FbeF0Bm18WYsJZSJddkouQQT0kncpjlhbTaH%2FtTijyhgBhzPQEyNDgRR3m%2BRe5tQuZE%2BOf9JACkldRXyhSP9MyOYMlTajhdo8qHBKVJLqiof92VbYQJ7UZZnlHXjWkRxoFyLh1HKwOK5ZKI0SdS14He17Vzusd1q9Pj1Pr1UcjX%2F0RbtnkJVNmpVjfpDMf3TOQZH%2FW%2FRaCTNiXM6m2MZho9CgW2XzZi3CEO2UWh7KJ6QE%2BG%2BaBEmT2%2F5uDqYMnC7VJ%2BDbDIHYBbGNIehGD%2BKV9vH9YK%2Fz2gms3hhVvHNyfZzVXpuog9HHQ4r%2Bk%2FR4%2FHzQeaxUtR6SZ%2Bf41YGy4QMcbfHUKMI%2FdWHxaHsDNO0S4zLq4FTtTXU%2FAHep5P%2F1JY%2BKLt8PGoantLRn82KTXIzTel%2FxQZOFPMR21QhKNnUs15K1voO3tsypVtOHYl5O1rXPOHkPP5ZaLj74qhWSriVzl1En4X2eG3HVIYUzlGBaY3JMCFdXK3mDxBNAa7mkZ%2FGtq36W7YHVAVC9YLrWU3j0YpExdpLNsm8ANRTAS1Cj7ZyLQoU5gl6u5duISsHWAqaWhl72lKNtfAC9OkFtNUvu%2FGGMaBkCxHasHdkKdgICLnRegfv%2B5MKqX67wGOqUBtuAVYksQ24BZlRtEa7%2FCzCGyCsb9cDFZXlCer2%2Ba83gKRP2toCouQz5ZCpV6Jh%2FuOhFAkPAcsIlYvrIFy%2BsJ2eS0zeLaeyKS2%2FOtUlTHfRmzJ3fNJay2LFnsgAKv3o6zaMk%2Fr8kgczxKr90XQmxC9dVlypS%2FDpfBgvNT5pX5NFodbrW2IYkqnNl%2BOA7f7vCInWUG0oI66ZlhDAvCXc%2BEzvhCvUhn&X-Amz-Signature=4677243357ed257b916fe383fad26cd155f82b2ce5509472bc7659b54d4de221&X-Amz-SignedHeaders=host&x-id=GetObject)
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
