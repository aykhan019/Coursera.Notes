

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

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/997ac361-58a8-4f04-bb0f-79fea4baa761/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46625ZADVZ6%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T231340Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGYaCXVzLXdlc3QtMiJHMEUCICmHW%2F8G%2FTbJMHFgwDg7o1ZvG3VAMHqI4v9LtoHnZLMwAiEAlPX%2FqIGySwdc0%2FAabMeZwDCfKGlUAI9n7MlNWsiVxQkq%2FwMIfxAAGgw2Mzc0MjMxODM4MDUiDBcMb24IIq%2FHGv9SzircAzxEKGrH%2FJeHlpDcF%2BdFDJ712FQAVkTCj8QxtKfcZtjItIBr%2FZ%2F%2FE3U8hU%2BccDJ9SP4lctRMj5n8nom%2BWTDxamZvWqvrkjSP1NUiANaeyZZ278lnBHRgl%2BFep0pee1iOjvJO9%2FsQDAuWnWABUjJ6hXYrs5BDbk2%2BnruYy2L4Jl0D1ixgRgIOGARa7in4fQumnfX7M9zXhNdTmKwSGqTZId0VWD0tbq8h6Us0w20kFZtgud5teHuPGR9N9r1J9ld9ro8WxrAZIi3EVL7ERQkVIlm3yI2fwnSppIYq5a5LNu2xi%2FZpFkRf%2BtaQk85Q1cpMiVAmD61aZRL%2BPKRrDP0IdYwqnJEfrt6oFy6ZwQZt1OHCbfydeCjqhpVOQbG0n6sj4DPy0MqvcRchu7i9zleQJjXAC00ott9H0pnMMeNbVXGO%2FKHfHjVF5hNqXRgy%2FBzBVxK1iw9qw0zMXrZeDi4a02S3bs3OHS9sDxD5fBNUc6nzMRJ7e8Lak0mEbSbAFIQbqfY5WkizzeAgxEFiuZG%2FYxGE69wVoeqfE0lJYiqC6GcYeLVolk%2BR1ldsTv13KrM15%2FQG%2BLhdAZcPh%2Bc%2FR4SOUZ9gfQt4TktyqF32LoZfuXx6rZGrqXBjNU6O4j8PMJj%2Bmb0GOqUB5CChgtBoYPRECpScF2eNv5rwCfhGGmNEKAC%2BqsVowfCOWafHurL6EKltu5IQP%2FGQzcoPj15kz171N5udLpWioaUPZdhMgiOpG%2FHFSVFQGouwFkL38CtIQJrzFBk0sF%2BwLWcQgEm7VcL1CyDrEiOo95gqoA6cNbBsq7IusqYe%2BwzTtg8Jd5nSe7nM%2FLgJOG%2FVnlLLI%2Bhc0SahG%2FjWrh%2FpbpSSsG3x&X-Amz-Signature=74c1c805e4424411a536dbf020713371502a710bcba30e31e9db57a2db1253a4&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Data Visualization Libraries
#### 1. **Matplotlib**
- **Description:** The most well-known library for data visualization.
- **Features:** Great for making highly customizable graphs and plots.
#### 2. **Seaborn**
- **Description:** A high-level visualization library based on Matplotlib.
- **Features:** Easy to generate various plots like heat maps, time series, and violin plots.

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/733d1e42-5a53-4fd8-90c1-3d85254369a6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SVICYKFV%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T231339Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGYaCXVzLXdlc3QtMiJGMEQCIDVim%2FBg923oYYUxX4hv%2B%2B6Zxws%2FtyN1%2Bg2puFGGDF7aAiBM4bDl36TjaHfyxyQuo3ewT2n0L0iDVNKp45p5EihY7ir%2FAwh%2FEAAaDDYzNzQyMzE4MzgwNSIMM04LLAUCfjueqhoRKtwD47R6aDz0TT1GJr%2F2iUOO1PA4GBm6hJIYCTWDV5dlgXJ0s25EYLIr94U13y6msJW5oSv3aGuEmmlycbKF8AbjmmdtoXy81PUNsPCrFk8JqT%2F%2FVXzzfuFBhTCGInor0kHwUnhkmeA1vxyAm8798uxR9vIyPaw5TQGkzTPm4BQDaaWrEbBjWwlJB0vGiNDMOCrxRRLCozl8U3iwYQZmcPTAkYxKluIA2mEnxVa270frxLHs33bw5%2F0ehY8qqDxtN8K2PtyNgOUK5AveKNk9obWEf%2FzdROqaUzKL%2Fo0tlCoGvYBcVT0%2F4vBCd%2BmCaZNkXvnLwpQdFTjA%2FBBCnVg5RP%2F4qD5xFEuMw749qjgU7xe0HioJwGVXkEoPx1P%2FhEZmHHzDgrclzR233QFaU1Xw6yMMszeAAbK90uH739HDWSnxs3Hm0OmU3opSv5wHHoDnRF%2Bp%2BYqzriIifo2ZU1B8icHp6iy%2BlKsfx44mCgoOv8kg1V5kAVLTeWpjRmC%2F5USiiMcsSlGWdB%2Fx9I6MvMTT8BOqHFiZVbqt1uIDs%2Bnuvnbq40uMxd1jHkp%2Fjm0YoPyMQVF8GKjdj3DaJGlkDcjVnc6DDpdM9YLLLDrSzdfR8ObCUGLoHvCV2BagiGqDLOcwqP6ZvQY6pgECGsCETqI3D0TkhVyIT%2BTLGSEAvJJ0i%2FbXIhEMvmADJ42cb4UQc7yOTzU%2BRTT1f3rnk91egWzO6%2FB9EpRIoRUYmLMPd5WNQyb1bmPZKty6l7YZkg%2B7xb8%2BKiaMNqONR0CGb5mSbjsjVuCpqiJ2mw5EcYsPRem696iJ7jWUzaI%2BYfXQ8uEq2cPeYZ5U%2BCr6ShS7lHZda2BeqgWHH8EBhK1TeQkTKSlj&X-Amz-Signature=a6923a4d121a1df829213f76bb0e6b097b58d19d4066299a940179ca3d566116&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Algorithmic Libraries
#### 1. **Scikit-learn**
- **Description:** Contains tools for statistical modeling, including regression, classification, clustering, etc.
- **Built on:** NumPy, SciPy, and Matplotlib.
#### 2. **Statsmodels**
- **Description:** A module for exploring data, estimating statistical models, and performing statistical tests.

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c62885f5-417d-4179-834f-d68f8f2bdf39/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SVICYKFV%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T231339Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGYaCXVzLXdlc3QtMiJGMEQCIDVim%2FBg923oYYUxX4hv%2B%2B6Zxws%2FtyN1%2Bg2puFGGDF7aAiBM4bDl36TjaHfyxyQuo3ewT2n0L0iDVNKp45p5EihY7ir%2FAwh%2FEAAaDDYzNzQyMzE4MzgwNSIMM04LLAUCfjueqhoRKtwD47R6aDz0TT1GJr%2F2iUOO1PA4GBm6hJIYCTWDV5dlgXJ0s25EYLIr94U13y6msJW5oSv3aGuEmmlycbKF8AbjmmdtoXy81PUNsPCrFk8JqT%2F%2FVXzzfuFBhTCGInor0kHwUnhkmeA1vxyAm8798uxR9vIyPaw5TQGkzTPm4BQDaaWrEbBjWwlJB0vGiNDMOCrxRRLCozl8U3iwYQZmcPTAkYxKluIA2mEnxVa270frxLHs33bw5%2F0ehY8qqDxtN8K2PtyNgOUK5AveKNk9obWEf%2FzdROqaUzKL%2Fo0tlCoGvYBcVT0%2F4vBCd%2BmCaZNkXvnLwpQdFTjA%2FBBCnVg5RP%2F4qD5xFEuMw749qjgU7xe0HioJwGVXkEoPx1P%2FhEZmHHzDgrclzR233QFaU1Xw6yMMszeAAbK90uH739HDWSnxs3Hm0OmU3opSv5wHHoDnRF%2Bp%2BYqzriIifo2ZU1B8icHp6iy%2BlKsfx44mCgoOv8kg1V5kAVLTeWpjRmC%2F5USiiMcsSlGWdB%2Fx9I6MvMTT8BOqHFiZVbqt1uIDs%2Bnuvnbq40uMxd1jHkp%2Fjm0YoPyMQVF8GKjdj3DaJGlkDcjVnc6DDpdM9YLLLDrSzdfR8ObCUGLoHvCV2BagiGqDLOcwqP6ZvQY6pgECGsCETqI3D0TkhVyIT%2BTLGSEAvJJ0i%2FbXIhEMvmADJ42cb4UQc7yOTzU%2BRTT1f3rnk91egWzO6%2FB9EpRIoRUYmLMPd5WNQyb1bmPZKty6l7YZkg%2B7xb8%2BKiaMNqONR0CGb5mSbjsjVuCpqiJ2mw5EcYsPRem696iJ7jWUzaI%2BYfXQ8uEq2cPeYZ5U%2BCr6ShS7lHZda2BeqgWHH8EBhK1TeQkTKSlj&X-Amz-Signature=9f973c5ea816f945a3344a16ac0ec5f85c2c909a8a7eeb062d5ba255b448eb10&X-Amz-SignedHeaders=host&x-id=GetObject)
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
