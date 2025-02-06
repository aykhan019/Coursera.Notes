

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

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/997ac361-58a8-4f04-bb0f-79fea4baa761/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QR7OISNY%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T071401Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjED8aCXVzLXdlc3QtMiJGMEQCIB%2BBK8X8DQJPvmzW06CjmwBqZyBfDywLj4kveU5B4g3gAiB7KdP2NONrVr4KjNTQnd1NaSL3m8A917hpBjk7yAIubir%2FAwhYEAAaDDYzNzQyMzE4MzgwNSIMXY35DJhNcbYUJaYEKtwDoubhqQqqcUgf1I0ekZ0UzRofVIXLyierBmod3kG0KPM04Pr%2Fp0Am9u3SmCjemHVVUfV9ohmzAMiy3pw7rgRljvJ5EoKeUoN6hjKyLkNecz1PqTBRhfZZlMtuTk%2FaIRs%2FG0wf1yZUSEmjFnTstA1x7l%2B1G4grtJzBewO8thRxiVKOkr9Kja7%2B88nOXdSCuRxk%2FNE60tYLAfXYqmhvmAP5qIi2axYv%2FJnVocIJsCfBpvDtennCZQgiln7oJ2IqXDRPNRIJF4oArt4KZXguQ0yc04IAAMRUH17R6IowLvvdGavNHj1cRw6%2F%2FnTYDtk6h9XGsmcWfhf0fu0dewOZw9m024zmomgboEJ5mGFlSUNGysIJJWKrzCXCdSU1x99YBTTXSLVwsjeSuTENEKqyJKGIUYW2W9I0ELLskfZUbkKPM8MCAIUvCyUZzjxNNxX0qy5R85ovm4tR%2FCXJJstZmWaPDTZdF67Ehhy4m3Er70B%2Fjdpo81JBU1fD3XSEmsWEafgDhUOkhTZwzaUk20Av45pfC4gfgDCdmXP3Vu6UaAUJhVKRUlHqbkIc83eBsJMajGh0Q%2BGHflXV%2BsFS5PPtMdo%2FsBG6NmaZ7LYjLo3gpqmLN0ovECMoU2PjLGJJee4wsLWRvQY6pgE1w09lVlzoCCkvnpVW20fXNnHJZNo21teq%2Fxg4sbRyNmk74PpMuIis4PhasJjQnzfCbILxkg69P5ufUfU%2FEA03xVPAzF1zZnWm4ciWYVd6KF6F4Icn896jBe3A1LOWuQ3Qkufwy8t0bJ4Qhrr88ijpwI502s50EaCy8ndW5WBDx0k4p0yluFH2yGeDor3tFiEroM1%2BjryLAIt3PIReBj11AvsGU5%2Bu&X-Amz-Signature=39c012cc6c050da9c70fa33f3e184709171b2274220957be000184ff085ad5a2&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Data Visualization Libraries
#### 1. **Matplotlib**
- **Description:** The most well-known library for data visualization.
- **Features:** Great for making highly customizable graphs and plots.
#### 2. **Seaborn**
- **Description:** A high-level visualization library based on Matplotlib.
- **Features:** Easy to generate various plots like heat maps, time series, and violin plots.

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/733d1e42-5a53-4fd8-90c1-3d85254369a6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663U3EQ3NH%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T071400Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjED8aCXVzLXdlc3QtMiJHMEUCIAVj6R7z1essYYqiUXZHxg4DatLFEcSEeOsFD9ILN6E9AiEA6PK5hJS3oax%2FQy%2BVr%2F78m3d8Ht43RUH0L%2FL3Q%2F5gWNQq%2FwMIWBAAGgw2Mzc0MjMxODM4MDUiDDxbDoKoq5xwWCKjqyrcA6MnDIOlxCNCJp%2BQf%2Bb30h%2FuQ1BFd1WK5UQCMfPdHEewVMacHed2ikhxDsPjWDMTJDed7ixMIoOHfu1VLr%2FMD5HXFSnHrOfrITWTMSKqSlv%2BBtWNLs8mSLs3%2Fjc4%2F643zpyIYDs0I%2FFfnRlNtbVfGWbz5YxymUOz2Rfwct5FGv02UIL9vbxyVxUpbGSD78A2C8RKpT1mk5R0TtCp3erJXH66fHi7%2FPwvmlr4OfzhFx63TfDoRp%2FoQjvxKhFqAbzblD5DDOYWfh3fKNyp1lugOAz7HyFYJy3PLVzXt5F31LgVKbwbe3B0IYUj%2BtiPJXQwBw827EmVsmxr31xhOrmI3YVXHLQAUJQqwA8p526FVSWS8gp6zD55aAUaYwqusZSXySBhAjue4epokoQnVVqRzh5HnVLUOU%2B%2F8zeikHGPs9IgBrLn%2FuG9xdyaLdq0xv75czMX3p22i3nVtcwTYk40cFNJI2n4Qy8RFAAoPfMIyUAPcAuXpRiIKBEQnh99TzyQnvE1UUMWM28f0B%2BE3J841GhU47pOeYQ1lpY1oGKlWuNkGBGCtOaOB2VG%2BFh%2Bj0PNgDlREFoOvzaYPotsMbESRVwc5i3lK3JH4LIzIGYi3cvWC3oKwylCG%2FVX36%2FRMKq1kb0GOqUBzABkynUOPyr6TI2aTE2tM6UpIdvPzamj%2FhAFqF5iGvdqX5sgE6yeudP6pYMHVC9vv5Nrfjx1ur9fW3iXWWAp4dp91djh2pChQZalMjDf3H8WU8%2FMX%2BzRjB1nny6QuR8W9CMaZomhPgXWj%2FQMhdFbKSuW3RtKFvThn%2BABmNxb0VOzfO3IbdoaXLGb9%2F6XxN0CwRjKiiObRyobneh%2Bsiq%2FxsvwIR8V&X-Amz-Signature=bd5fdd7e6ef907ee0f20fafe8947c1ad66fd999f77d633492928b5cd67ccc894&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Algorithmic Libraries
#### 1. **Scikit-learn**
- **Description:** Contains tools for statistical modeling, including regression, classification, clustering, etc.
- **Built on:** NumPy, SciPy, and Matplotlib.
#### 2. **Statsmodels**
- **Description:** A module for exploring data, estimating statistical models, and performing statistical tests.

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c62885f5-417d-4179-834f-d68f8f2bdf39/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663U3EQ3NH%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T071400Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjED8aCXVzLXdlc3QtMiJHMEUCIAVj6R7z1essYYqiUXZHxg4DatLFEcSEeOsFD9ILN6E9AiEA6PK5hJS3oax%2FQy%2BVr%2F78m3d8Ht43RUH0L%2FL3Q%2F5gWNQq%2FwMIWBAAGgw2Mzc0MjMxODM4MDUiDDxbDoKoq5xwWCKjqyrcA6MnDIOlxCNCJp%2BQf%2Bb30h%2FuQ1BFd1WK5UQCMfPdHEewVMacHed2ikhxDsPjWDMTJDed7ixMIoOHfu1VLr%2FMD5HXFSnHrOfrITWTMSKqSlv%2BBtWNLs8mSLs3%2Fjc4%2F643zpyIYDs0I%2FFfnRlNtbVfGWbz5YxymUOz2Rfwct5FGv02UIL9vbxyVxUpbGSD78A2C8RKpT1mk5R0TtCp3erJXH66fHi7%2FPwvmlr4OfzhFx63TfDoRp%2FoQjvxKhFqAbzblD5DDOYWfh3fKNyp1lugOAz7HyFYJy3PLVzXt5F31LgVKbwbe3B0IYUj%2BtiPJXQwBw827EmVsmxr31xhOrmI3YVXHLQAUJQqwA8p526FVSWS8gp6zD55aAUaYwqusZSXySBhAjue4epokoQnVVqRzh5HnVLUOU%2B%2F8zeikHGPs9IgBrLn%2FuG9xdyaLdq0xv75czMX3p22i3nVtcwTYk40cFNJI2n4Qy8RFAAoPfMIyUAPcAuXpRiIKBEQnh99TzyQnvE1UUMWM28f0B%2BE3J841GhU47pOeYQ1lpY1oGKlWuNkGBGCtOaOB2VG%2BFh%2Bj0PNgDlREFoOvzaYPotsMbESRVwc5i3lK3JH4LIzIGYi3cvWC3oKwylCG%2FVX36%2FRMKq1kb0GOqUBzABkynUOPyr6TI2aTE2tM6UpIdvPzamj%2FhAFqF5iGvdqX5sgE6yeudP6pYMHVC9vv5Nrfjx1ur9fW3iXWWAp4dp91djh2pChQZalMjDf3H8WU8%2FMX%2BzRjB1nny6QuR8W9CMaZomhPgXWj%2FQMhdFbKSuW3RtKFvThn%2BABmNxb0VOzfO3IbdoaXLGb9%2F6XxN0CwRjKiiObRyobneh%2Bsiq%2FxsvwIR8V&X-Amz-Signature=392cf7bc651f5742f2457a2e8a48b70994f07cc5e7590b648914f35f1c3c12f5&X-Amz-SignedHeaders=host&x-id=GetObject)
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
