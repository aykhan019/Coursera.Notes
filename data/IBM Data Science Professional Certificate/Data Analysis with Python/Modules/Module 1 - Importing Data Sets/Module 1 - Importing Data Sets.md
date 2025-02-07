

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

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/997ac361-58a8-4f04-bb0f-79fea4baa761/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665B7ZNPW2%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T111208Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFgaCXVzLXdlc3QtMiJHMEUCIGd6F5wd4uRc9LlJrDGZE2LqVD3nXt1KfQ2cIukM0JeYAiEAsohUXDClDvZjThu2Md%2FsFJen2BWpl5E3Gi%2B7GCAzCmQq%2FwMIcRAAGgw2Mzc0MjMxODM4MDUiDCaxbrziRC1DQrBdmSrcA%2BdqpYEVD8y%2BfUMkGITL2RGk9EjQRmndH5HAmyBKky5oJrADCgDzKC4uk2JM1DFEZPAimXfrumTpW%2FflAJ3BlTH4Bdcz4UVqrq7lfHB9obkGE4WuYkIfu525lLIWCAvbUjCHiNJ%2BW%2Bdxfw5NwWuTC952gIRvW%2F4%2Bdf947lvLdKYysAmnPiJL%2FOqH3ftzYol%2FsZ0xJjh9OwvZIo%2Fp9%2FJN0izd%2F5fWQTDdDOJZ4gYoOyVTmX0u%2BKF%2FH57irseIsvlfHNaDPYqMCq8I98UgyR1s5RIK1XTY%2FtYKeckrB2pi7QcK41H2K2huS6Bo2H1EzRjwkr6yPLznFGJp7iWzVuxUR5%2FghSAfPCLrZ4Nf005eE%2FzVrtEUfiKNeUufS2tZvH28woSVzZ21lCd21lvu8cB%2Fc2jvOKC1DB24kDxtuXLQz6Qol2%2FudZ8KKutSsUxLwfQ9wfSgIH6rhO5LRwIGn72kefntU%2FnWtx%2Bd0MCjlgBt1KDs9GUMfO3HU0jXsvqaESLQBdQI9wksw9A55Q3sSdQB7ZEy0%2BxXst7OS2v60jcGJSxG7uHGnoGjVBRgJL8R%2FgiSIjvePZhNXUst%2BPB7EE5TD1xz9R3%2BKBOWpIAYeQId4480ykAaT9TT7TolmMhMMML5lr0GOqUByPRuLGkdTs6RYfG7vMmSOifXZiIKXMiixs8K3acSjCFUJd%2Fan5s22nyFgukfwG%2BPlDZYy7TVVRtf53wY8TeZqU3aNz26cLfmDh3xxV732%2Bdojclt0J%2FiRq3eloY2ESo8%2FiKHSyz%2Fz8FT%2FYRyjRqrYblQpvOwOatw1o%2Bn3Lbduvl2WVQxv4Ox5lvi19EB4bMdFvSEE7nVyF36tiICOuMc5olqAcrM&X-Amz-Signature=35f122873f2dbbebc9eda5e26e9cbf5392e4eab223b6eb33a26d1889ab30d539&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Data Visualization Libraries
#### 1. **Matplotlib**
- **Description:** The most well-known library for data visualization.
- **Features:** Great for making highly customizable graphs and plots.
#### 2. **Seaborn**
- **Description:** A high-level visualization library based on Matplotlib.
- **Features:** Easy to generate various plots like heat maps, time series, and violin plots.

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/733d1e42-5a53-4fd8-90c1-3d85254369a6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663YSFXEAI%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T111207Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFgaCXVzLXdlc3QtMiJHMEUCIAPDyyQ%2BAjl1g%2FYWTxLLCRoy88SUxy095UPdkyv%2BFoxxAiEAx0bwGZae1pmiQ5pXuC%2B9yqSxx5wt0Irv9U8YJsuNfWoq%2FwMIcRAAGgw2Mzc0MjMxODM4MDUiDHQQHgVFXXyXCrNahSrcA6QHdFgvDxP%2FHnio1UhHu6W25AFqkbk%2Br%2FDxANaXbDRy0Ef0or2bneZAjPKPchGFFQumLdPGaR0OkPA8bH%2FJDcVn3jqyZ%2FmLzSOfvlCW9GQW434UnMwmu0YMaeoftsT%2BR87bECGfPLqfsaHTGYsWYejWqdm4E4RvTwuOAb4caJkDolcAjGZKUPAa0du14TSyCAkmMbvWSgsyNpiSmew6EaZCBEM%2BJ60WM0h2ZhMI3DT%2BL9LmQfb0KcdioefJgAoeb3cjkSsN%2B0dQc6gozsf4x6cgF7i44KRMHCSZ%2FL8Rz%2Fd%2BrZlP7mNJkMdC3xGjdNg3gxngOmQISJryAQgZ%2Bq49CzeN72Vz4heho9LkI3MVs16eRshzYtWkNxZ9EYud6h9EYdibZzONpFn5Nm5Ve4yTvcW7CP3mKr4WnLRBe1inxUTb4RJZ1cYJZmBeCteDfQ8M%2BiwvAf7x0%2BgrW36lBGlhASIx9LrV%2F%2BCUdBbGzo%2BYb9qjC6FO4DvSE4itDrIm1zRnxAJVkCXxZRYBCHvNfn%2By99ufDQaz1JKYlq6tjWImkgdN6F5YGqq9INMEBnx9wyRXCUUeEdauzOHuuaHlq%2BrQRsN5WODAasvkYnBIjTluAFjRHTML8ogyUNnZCpPpMML5lr0GOqUBDLmG1sUhhyrY59Yw3FNpia3a16s3tVjhDIBqn8pSeOSO0gkX%2FQ8o5wXChRp14MisNRXJ6yAe6nDHgEgc5YNVJB4H3dQ%2Belr7s5uYL2LcUnR2wUZeTh2JRZUuIhd6Goawm2QItY0DO%2F%2B8qzryRXrEZI94rBESjZ4sBF0TRNhsNHmYaMCQ4SWalxjSAZ2JC8rCvoB55aS5DQ9Trpn6g4G3OsNt6Jxv&X-Amz-Signature=2baa0ed18bc7f845a4771138d61f0133fdde70a8b70929abcbc6ead289d71f67&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Algorithmic Libraries
#### 1. **Scikit-learn**
- **Description:** Contains tools for statistical modeling, including regression, classification, clustering, etc.
- **Built on:** NumPy, SciPy, and Matplotlib.
#### 2. **Statsmodels**
- **Description:** A module for exploring data, estimating statistical models, and performing statistical tests.

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c62885f5-417d-4179-834f-d68f8f2bdf39/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663YSFXEAI%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T111207Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFgaCXVzLXdlc3QtMiJHMEUCIAPDyyQ%2BAjl1g%2FYWTxLLCRoy88SUxy095UPdkyv%2BFoxxAiEAx0bwGZae1pmiQ5pXuC%2B9yqSxx5wt0Irv9U8YJsuNfWoq%2FwMIcRAAGgw2Mzc0MjMxODM4MDUiDHQQHgVFXXyXCrNahSrcA6QHdFgvDxP%2FHnio1UhHu6W25AFqkbk%2Br%2FDxANaXbDRy0Ef0or2bneZAjPKPchGFFQumLdPGaR0OkPA8bH%2FJDcVn3jqyZ%2FmLzSOfvlCW9GQW434UnMwmu0YMaeoftsT%2BR87bECGfPLqfsaHTGYsWYejWqdm4E4RvTwuOAb4caJkDolcAjGZKUPAa0du14TSyCAkmMbvWSgsyNpiSmew6EaZCBEM%2BJ60WM0h2ZhMI3DT%2BL9LmQfb0KcdioefJgAoeb3cjkSsN%2B0dQc6gozsf4x6cgF7i44KRMHCSZ%2FL8Rz%2Fd%2BrZlP7mNJkMdC3xGjdNg3gxngOmQISJryAQgZ%2Bq49CzeN72Vz4heho9LkI3MVs16eRshzYtWkNxZ9EYud6h9EYdibZzONpFn5Nm5Ve4yTvcW7CP3mKr4WnLRBe1inxUTb4RJZ1cYJZmBeCteDfQ8M%2BiwvAf7x0%2BgrW36lBGlhASIx9LrV%2F%2BCUdBbGzo%2BYb9qjC6FO4DvSE4itDrIm1zRnxAJVkCXxZRYBCHvNfn%2By99ufDQaz1JKYlq6tjWImkgdN6F5YGqq9INMEBnx9wyRXCUUeEdauzOHuuaHlq%2BrQRsN5WODAasvkYnBIjTluAFjRHTML8ogyUNnZCpPpMML5lr0GOqUBDLmG1sUhhyrY59Yw3FNpia3a16s3tVjhDIBqn8pSeOSO0gkX%2FQ8o5wXChRp14MisNRXJ6yAe6nDHgEgc5YNVJB4H3dQ%2Belr7s5uYL2LcUnR2wUZeTh2JRZUuIhd6Goawm2QItY0DO%2F%2B8qzryRXrEZI94rBESjZ4sBF0TRNhsNHmYaMCQ4SWalxjSAZ2JC8rCvoB55aS5DQ9Trpn6g4G3OsNt6Jxv&X-Amz-Signature=d8663453d416b790ca1bd0a2b200c5989e00cca605e2e1db5646ea40141f53d7&X-Amz-SignedHeaders=host&x-id=GetObject)
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
