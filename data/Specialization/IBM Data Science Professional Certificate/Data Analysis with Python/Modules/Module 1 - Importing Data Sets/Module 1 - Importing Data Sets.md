

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

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/997ac361-58a8-4f04-bb0f-79fea4baa761/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662C62CJLA%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T062024Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDC%2FuzgO7OLv7tZv0rBHp1cH3vBUwGPGZSnaa9nDYohpwIgZe14zY5WPBLPll4aVcmIQLRBcjc%2Ff7M4CyQeRKCuaY8qiAQIn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDAeISqghX8VyVvcStyrcA5DuedOBBeV%2BTmuxWPRS8rd0fiqj5fACKKkfozdTLJuGUNABHJcR66Wn7BgSRCi%2FDQofDnWGIUElhc%2BtqkEPKQCZjmdQhPu9lCvU8IafeDR6qkCMv3PoOVzq17s6MmGgaACyfxnKgGm7Rgarll9kU8jc1huqI9HDiefu5EpK0qjD42AEo4zkBjERIt0FSi4ezG6ZOYb4MgsO1tbw8gEAwJk5Zc5opqhdVdgA8lgdBRv7UCwyQlHHJUw194F1cLbb7orKXjHJdWghQyCoESo7I5LaSEjU4khAXghA88p70ofIDO04NIdO3%2B8ocpvGhdRuAGrfT1ss3OtEy%2F6LtcEpRUX%2FnWucLawtELAYSZSZPLHB7x1YtVsAvR6LuPbgEMoGd8rRHNTPx9o40JJq6wivba87l0yvhbOBjOj%2BOSSrD9lv4p4SZGS67LTXdTNOmbQADrkXtW9I1pnzX2mE6%2BC1T56wc36Ko0Biq3puXh67n2Czfqa8ncHzMuCZlh6xZunQiwGap0kKGEKC%2F8niB4DPFAPm6m5tKYnvLHVoNZJKChl3PyK7a0m9ROmc11%2Fb%2Fa6MKYr93SE3MKfi4sn4mDKcXtGHWLvEKe3iAOgmpPJXaECZRAPS1567qKoxAEBTMOSi7LwGOqUBN6am7gWjO9o%2B8MVJvFByAqbZj6AM9dv3llYumNm4xdlcaE22%2FLnNfJtEP4St1w5XMQsXbYvq2g1tEh6KyIjEN6hbTX6PPixeQHwyF5IY3ragbE0ekg0n2UI0Y%2FdCa4y2iSTx0RQH8Ffrpyc8yA0dw3uzqIwYpaIV7Y5ULR6WftHsr%2FfQ7TmS7LMsdCBSQlkbem98JIoB0vtFEE9cAtFk9vQ%2BxndO&X-Amz-Signature=5f937b8194a5b3d815c18737f7640e05b65f7ce7a08e2eb39ca4cb53dd9c96db&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Data Visualization Libraries
#### 1. **Matplotlib**
- **Description:** The most well-known library for data visualization.
- **Features:** Great for making highly customizable graphs and plots.
#### 2. **Seaborn**
- **Description:** A high-level visualization library based on Matplotlib.
- **Features:** Easy to generate various plots like heat maps, time series, and violin plots.

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/733d1e42-5a53-4fd8-90c1-3d85254369a6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466U5YPO6PY%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T062024Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGhTLuPKhmyxjl0YMEPRBRibD59Re2JbQjlpBcdkDY%2BeAiEA7AQqz5lj9LN%2BhuygLAsIuAuVayCGxScGze4DDQfiJvsqiAQIn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDBbJLUu13tZkCCjE9SrcA1z1h%2BpNwF3OR4RQ%2FnAKsi1mY6JW9nY%2FFra1aaPXKD%2F06PePzJ4DlDOcxaaVQksJfjfP%2BWbDZ2cPQjKmw3M5ocjWD29ybQPzVGkEwfge1QJMSqzJnzg%2FRhjpiebI7MKbhqUWB%2FOqherJnczE3S%2Be4yFnFa1cRmB6S0ir1dhfPIjf0gpSu6vIZqymspyYriugK0j4I7xj4L5lTGd6qoxKC4kdfWxLMfc%2BskgdvFJVeRWuFSMzBXN%2BtvHUEKq8tyQiHjcWbtbKAaErMVLJ6RhOci4sQc0k8FckFrBXCyjfeeil5x0pl7W14n9IQeWu4hQcEtMQltpKDIGvE2NDEYOVNbcDxSYrm1MPt8xFQeIc3zaKtpt%2Bi6kipt46Q2ipP9BFIStn9C88WhU3v5HvrtmtiifNvcHFDyQ%2F4s5H2WZAp%2Fv9QwtpQFP8QztP%2FsHR2ptCBUoZHcIYPVDnVMKkgRjypxIyDy8InAmeMdw1vDvLrtNLY0LEUsbJ9xonuxfb3m4haOI3ITlY31KJZw2ANIA9V35oAn0ivX24aK7wu%2FtAXGW2d1XWhi5aHytpGxD0aHfsjwI1Ifzj1oKM0yxhva62rQa9KsZoFWtu6KwOnvx9XI2B7px%2BCWyRI9YIZUxpMPii7LwGOqUBXXfMxId6WNZkZNqKtkBjNv4WBdlw5XuzQQdhI5Fmvrw6lFtN7oxGmzowrIPB5Wi4nk%2B%2B8DOBJ5pO6xZtF1Ujkn8dMZ2DfjJ3HZZIWCTvIBRAqBdGduCbgWjjMFuZ3w9PX7vMi4rPD7liv3K7%2Bu%2FRyh5DbmnLZ0Xfw%2F1x0OA7%2BDZOFxrXLbS5DwmR5i3CBxah8Ik7M9j2JzbpPvWxk16xY5bcjnVh&X-Amz-Signature=1cd500d7def4ac0012cdfc7af1b2305e7cc1fa567a369dfcaf3bf01d0f6f0bce&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Algorithmic Libraries
#### 1. **Scikit-learn**
- **Description:** Contains tools for statistical modeling, including regression, classification, clustering, etc.
- **Built on:** NumPy, SciPy, and Matplotlib.
#### 2. **Statsmodels**
- **Description:** A module for exploring data, estimating statistical models, and performing statistical tests.

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c62885f5-417d-4179-834f-d68f8f2bdf39/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466U5YPO6PY%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T062024Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGhTLuPKhmyxjl0YMEPRBRibD59Re2JbQjlpBcdkDY%2BeAiEA7AQqz5lj9LN%2BhuygLAsIuAuVayCGxScGze4DDQfiJvsqiAQIn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDBbJLUu13tZkCCjE9SrcA1z1h%2BpNwF3OR4RQ%2FnAKsi1mY6JW9nY%2FFra1aaPXKD%2F06PePzJ4DlDOcxaaVQksJfjfP%2BWbDZ2cPQjKmw3M5ocjWD29ybQPzVGkEwfge1QJMSqzJnzg%2FRhjpiebI7MKbhqUWB%2FOqherJnczE3S%2Be4yFnFa1cRmB6S0ir1dhfPIjf0gpSu6vIZqymspyYriugK0j4I7xj4L5lTGd6qoxKC4kdfWxLMfc%2BskgdvFJVeRWuFSMzBXN%2BtvHUEKq8tyQiHjcWbtbKAaErMVLJ6RhOci4sQc0k8FckFrBXCyjfeeil5x0pl7W14n9IQeWu4hQcEtMQltpKDIGvE2NDEYOVNbcDxSYrm1MPt8xFQeIc3zaKtpt%2Bi6kipt46Q2ipP9BFIStn9C88WhU3v5HvrtmtiifNvcHFDyQ%2F4s5H2WZAp%2Fv9QwtpQFP8QztP%2FsHR2ptCBUoZHcIYPVDnVMKkgRjypxIyDy8InAmeMdw1vDvLrtNLY0LEUsbJ9xonuxfb3m4haOI3ITlY31KJZw2ANIA9V35oAn0ivX24aK7wu%2FtAXGW2d1XWhi5aHytpGxD0aHfsjwI1Ifzj1oKM0yxhva62rQa9KsZoFWtu6KwOnvx9XI2B7px%2BCWyRI9YIZUxpMPii7LwGOqUBXXfMxId6WNZkZNqKtkBjNv4WBdlw5XuzQQdhI5Fmvrw6lFtN7oxGmzowrIPB5Wi4nk%2B%2B8DOBJ5pO6xZtF1Ujkn8dMZ2DfjJ3HZZIWCTvIBRAqBdGduCbgWjjMFuZ3w9PX7vMi4rPD7liv3K7%2Bu%2FRyh5DbmnLZ0Xfw%2F1x0OA7%2BDZOFxrXLbS5DwmR5i3CBxah8Ik7M9j2JzbpPvWxk16xY5bcjnVh&X-Amz-Signature=600f2dc413c75b184b56b15f85b77d963c250298ccd22e38cb40a534147dc018&X-Amz-SignedHeaders=host&x-id=GetObject)
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
