

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

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/997ac361-58a8-4f04-bb0f-79fea4baa761/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R43Q6URM%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T171257Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAEaCXVzLXdlc3QtMiJHMEUCIBXnTk6QdCj2%2F9V6RnQXztWX%2F0OU2tOZZbKWNMT720ccAiEAlN9dHP7UvRsxhK5vJpDiQJXXSfCZ8WSoOhO%2F9VPMAxsq%2FwMIGhAAGgw2Mzc0MjMxODM4MDUiDITFQW38LMDLFA4FUCrcA5tYUWTSoxz%2Fzpe8prgUD%2FSO8e3jatvqKa9rrcRyXkeFM3jnM%2Bn7BXq8QBK119u0Ne6ngmxvykL6EvFrX3M3ZXUI%2BZ1ISc6HeREVwQmUj6T6ay2hMuxMrCoJenB6i4jZ3btGjPLEg4lddfdCSOHch1UF%2FnCbpCC37%2Ba%2F6VZDOiU%2FsBYcFjEIQb%2F5vwIKnQGcbLILPJhrw12%2FE1epqqOZ%2Ftuq5ztDpAOX1iqhL9ca1P3C2wSQEVT2ah8cMctwUPH45STJw2ijV8RDJBbdgYEGg6QM7VT0KktSHN0w30Fwt3uCXE0izI4d4xo44m80A0S%2BFda3At%2BxYNLIGZMS57NtOxuCQBa5rS1LELi7Np1MlwVjstH74lVS3eE37r%2BjppxgRGkYsksNQ7YmxCdYR%2BMJK17VNF0EnsKiX%2BOqRw%2F7zVJ4JXFNmn%2BF2n7AmDbokE5FptNdaB7fpxZ8kqzcTh0AexvADa5C6%2F64qYF3u%2B4s6i6ITJ1fYBu41TyZLFN2WDvh9YZ5OpYK2JM%2F7hUwGbBMxtlJCD%2B%2FXCln9nJwtWQYMrCKPtvtjHtexbY7zSt04IbgQODBhZ0szG93csq4hLacNE5T%2BnHUia80X2kKbdDNPOwlb3c27orqs%2Boy%2BMrBMIvmg70GOqUBVoLzBErUHNC8IEqWMqConf2q8ln5wffZunHMFeLF2QNr%2Fbc0EPYPtzUpRfFfXcEt9kSxKM8u19461rthqXytauHB%2FTb5u%2Ftez%2F4kcm%2Bf44mtrKIIEBCv74N0BYn6ySl50M6Q0DbzRAj14ZCCeB5TF7PNZUhnwkJ7URcQJpD%2F7tvxuZTrwTfFi0kEQgDsQi%2BWO9jqF96NZ3NRhQmGf89xru4Wwy0j&X-Amz-Signature=b5d75b266e44e375596b8b23bf90bf4a81534b3a93e615dabac1924038cd7022&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Data Visualization Libraries
#### 1. **Matplotlib**
- **Description:** The most well-known library for data visualization.
- **Features:** Great for making highly customizable graphs and plots.
#### 2. **Seaborn**
- **Description:** A high-level visualization library based on Matplotlib.
- **Features:** Easy to generate various plots like heat maps, time series, and violin plots.

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/733d1e42-5a53-4fd8-90c1-3d85254369a6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664ATTSRPU%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T171256Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAEaCXVzLXdlc3QtMiJIMEYCIQCcFFiQDV8Pzi6BTxPdryAHc8eejxEgBHNW6f253BTpKwIhAO0Su4cr57LzI6i7yDn77IZBb6DNAJR%2FUUleP0z5qcs7Kv8DCBoQABoMNjM3NDIzMTgzODA1Igxp1%2FK68GqlRZy2knsq3AOzw5RJVJumwExbbyLWApV3FduAHO36y1MZplhW5SIVF5R8Sha%2BR1wdG%2Bx%2BcJcOccbT4rujgz8CE7%2F7qIZY79ZkcBKoDhPRR02FHH9hipTkO4K6W7zKCd7rIRNDrhxFjgRSQykJaBRB%2BtPWIebc3PUFjfipn6GlgsOPn5fvuXhlzZtMPhd3UmKqLnU2fwThs7gm5AVRrO4YjNuigqY8l%2F2jT4Kww29am70cB9IYyPiGT5%2FuDqTqvGMFHC%2F2uVKDhY%2FPWDUZNfvpxHXrbez7D7MaHOH6Oc37yQr7%2BsUEMzBo6ku%2FzFfBpNcRlTENa1R05R13cM2419wyC%2FuNHMPPgFW755bnO960%2F8F8vG2YIbNxpEZDg14%2BNG5Df4pweee18KMlXN%2FwB07kxeBrpcXSpgn1MjGtg3jUyOEBInakq%2BrG2qsWi5MqiIcx6WT7L4HxB2TEl4d%2BMOZ95MNKuiot6V5dKFjrVB7gz%2FqzBonEl%2FOclS%2FAwfRvXZa8fTMj6558rtqtrculyMb6C%2FPVI4djp4wyqsgrK4QWdCtJCowwJk%2F8LM8WxIt0Ci0JcAIgBS76OD7K0FV20YpgaTxrCA2QCD5frEoHYDqWxN0%2BckpmR7w03JtAwtZOblkRVMOoBzDW54O9BjqkATbcQVcd0xUgV%2FMO2wBROlKnfxHSXmPj%2FwEmFzRurErSoDUEf3Fwjh338VHVPIjGm0KW6WiPlycTguR2wHEatR4IM2tWJJ7%2BTxV5DNEdBhwjLKQhnRrMlOjmWdLdyeJd49NFtV97g3opVeRg6a4pDNJpT6uN6qrflLawf7E9m5sm%2BuHAMmVmGLTDJIXNN6xoFZvMqqQE25g2JChNufnysVw5qaYn&X-Amz-Signature=017bddba2b5b35480e90382696b7d3ba25e448f55e645f07d915dac55e1e7901&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Algorithmic Libraries
#### 1. **Scikit-learn**
- **Description:** Contains tools for statistical modeling, including regression, classification, clustering, etc.
- **Built on:** NumPy, SciPy, and Matplotlib.
#### 2. **Statsmodels**
- **Description:** A module for exploring data, estimating statistical models, and performing statistical tests.

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c62885f5-417d-4179-834f-d68f8f2bdf39/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664ATTSRPU%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T171256Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAEaCXVzLXdlc3QtMiJIMEYCIQCcFFiQDV8Pzi6BTxPdryAHc8eejxEgBHNW6f253BTpKwIhAO0Su4cr57LzI6i7yDn77IZBb6DNAJR%2FUUleP0z5qcs7Kv8DCBoQABoMNjM3NDIzMTgzODA1Igxp1%2FK68GqlRZy2knsq3AOzw5RJVJumwExbbyLWApV3FduAHO36y1MZplhW5SIVF5R8Sha%2BR1wdG%2Bx%2BcJcOccbT4rujgz8CE7%2F7qIZY79ZkcBKoDhPRR02FHH9hipTkO4K6W7zKCd7rIRNDrhxFjgRSQykJaBRB%2BtPWIebc3PUFjfipn6GlgsOPn5fvuXhlzZtMPhd3UmKqLnU2fwThs7gm5AVRrO4YjNuigqY8l%2F2jT4Kww29am70cB9IYyPiGT5%2FuDqTqvGMFHC%2F2uVKDhY%2FPWDUZNfvpxHXrbez7D7MaHOH6Oc37yQr7%2BsUEMzBo6ku%2FzFfBpNcRlTENa1R05R13cM2419wyC%2FuNHMPPgFW755bnO960%2F8F8vG2YIbNxpEZDg14%2BNG5Df4pweee18KMlXN%2FwB07kxeBrpcXSpgn1MjGtg3jUyOEBInakq%2BrG2qsWi5MqiIcx6WT7L4HxB2TEl4d%2BMOZ95MNKuiot6V5dKFjrVB7gz%2FqzBonEl%2FOclS%2FAwfRvXZa8fTMj6558rtqtrculyMb6C%2FPVI4djp4wyqsgrK4QWdCtJCowwJk%2F8LM8WxIt0Ci0JcAIgBS76OD7K0FV20YpgaTxrCA2QCD5frEoHYDqWxN0%2BckpmR7w03JtAwtZOblkRVMOoBzDW54O9BjqkATbcQVcd0xUgV%2FMO2wBROlKnfxHSXmPj%2FwEmFzRurErSoDUEf3Fwjh338VHVPIjGm0KW6WiPlycTguR2wHEatR4IM2tWJJ7%2BTxV5DNEdBhwjLKQhnRrMlOjmWdLdyeJd49NFtV97g3opVeRg6a4pDNJpT6uN6qrflLawf7E9m5sm%2BuHAMmVmGLTDJIXNN6xoFZvMqqQE25g2JChNufnysVw5qaYn&X-Amz-Signature=c1f1c024f2e98c542a4dac84626998ec59ec72c41cdb5c433415efa47b77b8e3&X-Amz-SignedHeaders=host&x-id=GetObject)
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
