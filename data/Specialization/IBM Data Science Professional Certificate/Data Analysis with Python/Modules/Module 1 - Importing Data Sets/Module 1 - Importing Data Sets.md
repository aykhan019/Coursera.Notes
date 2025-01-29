

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

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/997ac361-58a8-4f04-bb0f-79fea4baa761/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZXAXOFG6%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T211330Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEI3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFPBLfHHZogsGXnCi6pZS34jTHTiTyXfjvSOhqK%2BqPu1AiEA0wBVUPhad%2FvuMirX1GWXNQ%2BnUoc23AxgNAZnHmzmXGUqiAQIlv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFb59NtQ5RmIIwiY%2BircA6tYH9%2Bs1y9oE3QFi44ILA%2F9FDzHJbjSUFCDczwANR1U%2BXxgWaHEtrVFscI%2F8mk2guvMeUve7%2FKkexAiFxJ0jqAPlxB5iPtg19tLPTa5p1R2f434BeUIrAhEvbJzl3%2Fr%2FIDIsk47JF2dSrTI4Iw7qiaJ5pTER%2FSklKT%2F3AffmubdQwWRtokT3VjbWEuI4KGPvYcSaIMBMdkpFZ6rApGTZwqKff6crcQu2cFSQnnizG4L5qxYM42ua59cC12nitmOYlf5VhVj8HzRJ714yEb%2Bie%2BGsGUhutFrj0MwMI1lTEbfiUiEZhBZSbGLCGeuHpNPXUmt4v%2B4ldPMxWqnLMx7%2BROzhe%2BYL6PIYgVS4KjxkY0NrOV4Vt7HdvU0hA1mlewQ%2FbTe1mgtg4g9gLc8nmFnIyEOaMah5VgphnDLRpe%2F%2BPHtP3ezfyAXztVZ%2FdtEeG7f76ei1cr6HyvaJMTItjDqso7vVyGmmBEJxvSLdORO0YQ0EOA3R9NzilL%2FlIopmGVQm3kFtStHS%2FWkog64zz%2BzTYObVgFMOb7qPX4%2FDcdlCrduCpb6P5%2Bs6LsTPsk8dqnJ31%2FmS125%2Bj6fYFf2HB6QMEsNxziwEpwDRks6Ebk4kPgej9vSMeP45gydFF5ZMP6o6rwGOqUBRIcDrxDPsQZ2WsH0qjvgTinIvD9sBnMdXsDpkemQEqGGIsPlLOqFv8yduL3EbkatxjJ8hLoaMtvRBSFS4zWIQSv90NckVQ9Dn5gXuSaJxi5ZjkMjac6nAzicW4Fiq50bFfx6lIm2cqb9W8zyW%2BrIm%2FjFI16sRp6xmcN2r1i5aOOxUs9IoyQwKWIpMNDd7RNjK2F8Ml378HMuegMXqAqTIOHjD88e&X-Amz-Signature=cbe0f061af54c0bdb2356a2285da232fca72177a2a4977e5bf97efc908a86fe8&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Data Visualization Libraries
#### 1. **Matplotlib**
- **Description:** The most well-known library for data visualization.
- **Features:** Great for making highly customizable graphs and plots.
#### 2. **Seaborn**
- **Description:** A high-level visualization library based on Matplotlib.
- **Features:** Easy to generate various plots like heat maps, time series, and violin plots.

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/733d1e42-5a53-4fd8-90c1-3d85254369a6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XPZVDCF2%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T211329Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEI3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEsx4K9fOgYLOD6VtctFTEM0%2BWeDKlRv9scB04ZMgYNsAiAM4tkDFGKbMGJ2VWHNzCkEf8kjv%2FfO64cxhx4nHyTOQSqIBAiW%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMZs4mIx44fOg%2B%2BjBcKtwDifsKJXgSiSfLRp6GIZit7Y48WAgFrFpnaLkYPDikgCeHBhi4goWb2Gkg2OrsmsIcRXdl04FA5ReHTzw8%2B7gtrV%2BRcoYBtVJSR3Q8uIg7RbTRQiF5BxuwBiKGDnavHXvqg9WhCsohlBotzRQm4Dt%2ByA2k52bFH2CwsgDp8B%2FKiRz0sp2Q9BLOiq5xtYc294s3EKF8LVBLBOk6%2F0pyu9gomQdNsU42gupUesdJA%2FzM1rJJUiDtQeKy1r2dINiLcc8VV1wNGKHbAD26f9ybgkobGT98QAL1K1sa7L9wOJVUiaZKdN2b5imQl1YRO2Lc8b1bjCm2%2FFZ3znr%2Bf1qVcWG2C33E2bs%2BbO8vWzUW%2BQC2MmkHLzzl6uoWmpkl3TuzsjX%2FAZGnHLHmxSnNPK68dA4DgVd4uLeR0FA9Qy6YpfFpQ7I2C0DO%2F73xMTW4PS9IbGEhI0zjLhR%2B7Nej7XZ9RhWE9nKse5g4H5vwM9kUmnRHJJ4fWML0e7evKT%2BeKgDiFwDZH%2BuHNB2e8pBnYe8ERrk6EBXksWLGaQM73PoUDvr7oN%2BkkCXcoPd6dAo%2FchTTTv%2FFrZ5%2BHIo594C56jS05gMp8BrDlhtZGAtj4YdMdIZ5gVbuyscFr4bufZ9YBH8w06jqvAY6pgHcd31FYoaq%2FojqpH3dbVPES2vu7z9BCdFcnmNmOtrpmMKS%2Bl5%2FC%2BBUfSdQvaS5zts8IA9QjpkjI6oCfMxYj6y%2F2Vx3A0gRYAbYQHTQXLDgWeT5RzPproldFodJHUdlptVIZ7oeGC8Da580apow8Nf89OmC9X1mLwq1duiLxEEm0mTdGOBdaPkwjpTRTM8EPX%2F%2Bgt9nYEMiFTOBxVT1xW0knP91TAU%2B&X-Amz-Signature=fbce9f4edfd2a8c895c518c08f9e9d9e55b8f7ec3c17b34d3f7a00e4f320b346&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Algorithmic Libraries
#### 1. **Scikit-learn**
- **Description:** Contains tools for statistical modeling, including regression, classification, clustering, etc.
- **Built on:** NumPy, SciPy, and Matplotlib.
#### 2. **Statsmodels**
- **Description:** A module for exploring data, estimating statistical models, and performing statistical tests.

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c62885f5-417d-4179-834f-d68f8f2bdf39/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XPZVDCF2%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T211329Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEI3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEsx4K9fOgYLOD6VtctFTEM0%2BWeDKlRv9scB04ZMgYNsAiAM4tkDFGKbMGJ2VWHNzCkEf8kjv%2FfO64cxhx4nHyTOQSqIBAiW%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMZs4mIx44fOg%2B%2BjBcKtwDifsKJXgSiSfLRp6GIZit7Y48WAgFrFpnaLkYPDikgCeHBhi4goWb2Gkg2OrsmsIcRXdl04FA5ReHTzw8%2B7gtrV%2BRcoYBtVJSR3Q8uIg7RbTRQiF5BxuwBiKGDnavHXvqg9WhCsohlBotzRQm4Dt%2ByA2k52bFH2CwsgDp8B%2FKiRz0sp2Q9BLOiq5xtYc294s3EKF8LVBLBOk6%2F0pyu9gomQdNsU42gupUesdJA%2FzM1rJJUiDtQeKy1r2dINiLcc8VV1wNGKHbAD26f9ybgkobGT98QAL1K1sa7L9wOJVUiaZKdN2b5imQl1YRO2Lc8b1bjCm2%2FFZ3znr%2Bf1qVcWG2C33E2bs%2BbO8vWzUW%2BQC2MmkHLzzl6uoWmpkl3TuzsjX%2FAZGnHLHmxSnNPK68dA4DgVd4uLeR0FA9Qy6YpfFpQ7I2C0DO%2F73xMTW4PS9IbGEhI0zjLhR%2B7Nej7XZ9RhWE9nKse5g4H5vwM9kUmnRHJJ4fWML0e7evKT%2BeKgDiFwDZH%2BuHNB2e8pBnYe8ERrk6EBXksWLGaQM73PoUDvr7oN%2BkkCXcoPd6dAo%2FchTTTv%2FFrZ5%2BHIo594C56jS05gMp8BrDlhtZGAtj4YdMdIZ5gVbuyscFr4bufZ9YBH8w06jqvAY6pgHcd31FYoaq%2FojqpH3dbVPES2vu7z9BCdFcnmNmOtrpmMKS%2Bl5%2FC%2BBUfSdQvaS5zts8IA9QjpkjI6oCfMxYj6y%2F2Vx3A0gRYAbYQHTQXLDgWeT5RzPproldFodJHUdlptVIZ7oeGC8Da580apow8Nf89OmC9X1mLwq1duiLxEEm0mTdGOBdaPkwjpTRTM8EPX%2F%2Bgt9nYEMiFTOBxVT1xW0knP91TAU%2B&X-Amz-Signature=930bb19dbdcbc74f7e99f2826c9ecfddfe8f57e8c5da1d4788e28d926dc64cd5&X-Amz-SignedHeaders=host&x-id=GetObject)
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
