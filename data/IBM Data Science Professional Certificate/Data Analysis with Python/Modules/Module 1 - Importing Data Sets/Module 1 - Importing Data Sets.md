

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

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/997ac361-58a8-4f04-bb0f-79fea4baa761/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466V6ZU237K%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T161818Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGAaCXVzLXdlc3QtMiJIMEYCIQDrK0AmcZjZvETWhVybEXebZrtyC4X3rlp8Y9Jd%2FzIeSAIhANLWCgPEDnohANChOiwADWeTdBtu1bZwzcrUE7tiXOdRKv8DCHkQABoMNjM3NDIzMTgzODA1Igx01uRh9HIRtoAXw2oq3APtiKIAVsP5755vGt0yU9IIiN1VNE3quCzLKlkV9ETo2B6WLNoJv06H6C6HktWBEUaEsyje63%2FlTH285h9tx5kDWjg3qa729TBDaHec0nI1uq6kuZo2k19GK9EewG58iTR1GKj9CZ3UwdqdIgmBwx0qKHvwx0O7sccAdYcK8hV3vrZlvuq%2FONmLMr4YtqgD6EKLLekSocruJ38RI3kMO4HdPKhAJ1JgL1nkZL1BMqjv6z2eiEF7dWHCFSeejGA17Wm%2Br7cWZZN0WaC3zJdKyBkohti%2Bf7XXh9p85HpjP9%2FUsO6AF4sGm4Cqo3vrNOpQULxUSduR%2BoeECbqShm4YwjRJRGHDmtg%2BZl5b703l91QLiHnbpxzcygbxYwbLPe5mCj3vNWO%2BQh9cgPk3RnzH%2Bpb7v2YbF%2BResNMhUbLVNJ9nvWRQHhjcoLR3jHRrEWwr84H%2Fbt3RzdV%2FoZBhGQWftrdplqhQiexkSxwgmhyukG1SfR%2B6hMx9wtH8RsiR6QXkm6lZuYdpRun2znwcl%2FZqXLfd54TxQ54wrafoKXb%2BvMZ03K1DaXsAgtfEVgPe4rY7McB82L1J5GO2acEzPMihZRl3P1a0r3QXLvjsyiyYsWYXN8486C0X6focouwymzC%2B4Ji9BjqkAUL77uR%2BHg750RyjvJEsSIGonaGLK0d7EX2QkaIGSVs%2FROJISlbaybz3VwKUCHGVU22ovkp0whAMi3y3okxp%2BYBC%2FbuZ7APEYLeWw6nPRIQTPWVmaX9fyO2wB3HqgNeZk6%2BJzFMK6LyO%2FzU2eM5UxhL6zv0pJrsis4fyYvyOSYD0%2F0zkJgfgILvW0r3QxuwejYpS6ijC%2BY7urioHNnGth7iqqzcc&X-Amz-Signature=ae35f350bb94604a061e5d4464d6f70838fe11bf20ac58be3b691719d7ff9aa6&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Data Visualization Libraries
#### 1. **Matplotlib**
- **Description:** The most well-known library for data visualization.
- **Features:** Great for making highly customizable graphs and plots.
#### 2. **Seaborn**
- **Description:** A high-level visualization library based on Matplotlib.
- **Features:** Easy to generate various plots like heat maps, time series, and violin plots.

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/733d1e42-5a53-4fd8-90c1-3d85254369a6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665J62EKO4%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T161817Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGAaCXVzLXdlc3QtMiJHMEUCIQDqjdM5psS06kctSCJAy%2F%2FazTQnvrir2Fo%2FM6ZoQTDDKwIgacHPgiIRzPzpNU%2F1ypkJRTpH0uW7q6uKfo1oMb6lRc8q%2FwMIeRAAGgw2Mzc0MjMxODM4MDUiDLKe0r9qh6ptLlV1%2BircAyEzgv16ySnwyHKmNL8twx2ltm0TKcv1lrTthqIU%2F0d5OYWrI0S7HmLtBIWZoOjU9KSiyb2fWf%2F9jwqfJVl088RgLKXWGfrB1RqWEwxtTnXFQJq9Zfbdc899BMrts2jhWeF0s1%2F75F68QV66%2BN2Aj8qIN3UPeCRajRJS0nGlkNmLfGWrZkLt113Y0vE0SQ2PDq5G1J%2FGH1VMBIU%2FSRVfqxRgODvkoxYuqRqrxgWh0QZYTg1rFj1LjHL9XPKfOXMJ1erehPBTunJe0esWvI3NZ5dhfvnTJ9dFcmplbAD6pyi7HwzkWwDZd9o%2BHtEoosjstrI%2FaTgOWQ8Dg%2B3omx%2FSfvOK8qYZPix0sE2rnVj%2BZX3tnhbqEO1JRWl%2BWedk7bE5n57I%2BU92V8QJLsrO9XTmfAaCrQCtInnsxq51L2tixAN9T5scnJYTxWd0ms5d5QXHKYkSUrewze7UEx8CX2QCGnlTqOrG4YIy3z8f1ZrWpvYm3a4milStPe%2FitW7JGFjmyGQQbhIp6nyPtbH0VaIvwCSb7DBgtdcdy%2BtAdl5SgqAtu82MUqciYl%2B4lXbwxvjLelWg%2B72yjWHsNKalyliqL4fQEC7tY%2B9izenI9Vaxqs8fzeiwWmrLwR6SkDBRMJLgmL0GOqUB2MK%2BLQbtQZR0zFOrN0EZckIQ8tZdQhCo%2FRO%2FREEkjmMxk%2Bplr9g1QpwAmyKwaUruMHbljybNMg6hyWfmXinkstF7QMpXlKwAPTC98YAgTDmV%2B1ckcbAMWVRqCj4Mfkyrc1Yyg0gxJUpG9gP8CcESpAklgraYKD5T0sjgadzLEUQzafLQ1eWU3zq2OjSmnWNOXPM5QK5y9jYjW7ikNnTOomygSN7J&X-Amz-Signature=dcd2c6ab4bbaff53532246b5eed9c926b5848f57bbcebb0b3995aed473efab23&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Algorithmic Libraries
#### 1. **Scikit-learn**
- **Description:** Contains tools for statistical modeling, including regression, classification, clustering, etc.
- **Built on:** NumPy, SciPy, and Matplotlib.
#### 2. **Statsmodels**
- **Description:** A module for exploring data, estimating statistical models, and performing statistical tests.

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c62885f5-417d-4179-834f-d68f8f2bdf39/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665J62EKO4%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T161817Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGAaCXVzLXdlc3QtMiJHMEUCIQDqjdM5psS06kctSCJAy%2F%2FazTQnvrir2Fo%2FM6ZoQTDDKwIgacHPgiIRzPzpNU%2F1ypkJRTpH0uW7q6uKfo1oMb6lRc8q%2FwMIeRAAGgw2Mzc0MjMxODM4MDUiDLKe0r9qh6ptLlV1%2BircAyEzgv16ySnwyHKmNL8twx2ltm0TKcv1lrTthqIU%2F0d5OYWrI0S7HmLtBIWZoOjU9KSiyb2fWf%2F9jwqfJVl088RgLKXWGfrB1RqWEwxtTnXFQJq9Zfbdc899BMrts2jhWeF0s1%2F75F68QV66%2BN2Aj8qIN3UPeCRajRJS0nGlkNmLfGWrZkLt113Y0vE0SQ2PDq5G1J%2FGH1VMBIU%2FSRVfqxRgODvkoxYuqRqrxgWh0QZYTg1rFj1LjHL9XPKfOXMJ1erehPBTunJe0esWvI3NZ5dhfvnTJ9dFcmplbAD6pyi7HwzkWwDZd9o%2BHtEoosjstrI%2FaTgOWQ8Dg%2B3omx%2FSfvOK8qYZPix0sE2rnVj%2BZX3tnhbqEO1JRWl%2BWedk7bE5n57I%2BU92V8QJLsrO9XTmfAaCrQCtInnsxq51L2tixAN9T5scnJYTxWd0ms5d5QXHKYkSUrewze7UEx8CX2QCGnlTqOrG4YIy3z8f1ZrWpvYm3a4milStPe%2FitW7JGFjmyGQQbhIp6nyPtbH0VaIvwCSb7DBgtdcdy%2BtAdl5SgqAtu82MUqciYl%2B4lXbwxvjLelWg%2B72yjWHsNKalyliqL4fQEC7tY%2B9izenI9Vaxqs8fzeiwWmrLwR6SkDBRMJLgmL0GOqUB2MK%2BLQbtQZR0zFOrN0EZckIQ8tZdQhCo%2FRO%2FREEkjmMxk%2Bplr9g1QpwAmyKwaUruMHbljybNMg6hyWfmXinkstF7QMpXlKwAPTC98YAgTDmV%2B1ckcbAMWVRqCj4Mfkyrc1Yyg0gxJUpG9gP8CcESpAklgraYKD5T0sjgadzLEUQzafLQ1eWU3zq2OjSmnWNOXPM5QK5y9jYjW7ikNnTOomygSN7J&X-Amz-Signature=75b7d3182808921bee18470101819f69fe216f6630a74380d27de48873b9fdcd&X-Amz-SignedHeaders=host&x-id=GetObject)
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
