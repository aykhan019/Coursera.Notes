

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

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/997ac361-58a8-4f04-bb0f-79fea4baa761/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663NJJVYCK%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T191208Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAMaCXVzLXdlc3QtMiJHMEUCIGKy7NwAW1qKNcz8bVFib%2FOVEc0VLyyarLsRbpLqxpyLAiEA34nNdB3A38%2B0JIXY0kxU84GwzZHmFnvDFvm6RbQzHLAq%2FwMIHBAAGgw2Mzc0MjMxODM4MDUiDBBwfdMaLtCkIayOgyrcAzZwQs2q8H6c9k0ho%2BGol%2BbM3ag5sKzv%2FNJD55kjPxqoA2dr7w4RtjLJNLgiH%2FEcAY2aQdzM1k995zRq6EMJXPGAaFTfMnqduNJu9v9i%2F9uaLDjPutKYVeQ66CD1vDy%2BWIruiV5uTJDeCZz%2FMBsP%2BLmUlS6KQSv%2BdZ7Zv7IVUF%2BvsmqrbsDUWgnPam0pVvgpDHZbBzWjA3LjMY2P63Q1LIx3FxVq0NUPh1DzTeevibhKI0QKlAU4C37liIQDkjzGnjX7jwGzBfc6hYiwMb0S4Ye3zS6pO6wI%2FXugH3pQExbT6R2AU0u8Bw%2FMtnNvwUbL2KeYz0s2XlwXe9QmiMUEJnTefG9Ccpe5Gviz7RfPSTz%2FgnC5wmcH3i5dH3s78p2a%2F8OZWMW39LkUrVF1QHVzttBYUnCt9TnGmAqJt0vQ7a%2ByRMxCDfLh5IGJvP%2BgvUP%2FVWxueE0i98WnTzdhpLvWNaaTa%2BfaXCySzHoBun%2Frq2WQ%2FtMLDcJBauJmFUOQNzoIszXZFRMiNCqt%2BLZ7RZItQ7pZYvklV1Kz%2FjChGQ4IT9aLczMFf%2BmCq46MBcRnT5tfwWcZn%2FU7ixAEcnwF7%2BzHi1CdLE%2Bif%2BEcPoDpIVvT5Trl2TehCBX0d30k1TaFMNGghL0GOqUBsObqJB4aRNfmaU7Fn1VR%2BKocKBIGolOwuMgdnhEA%2FMZ6pHDQFqh76a3Q6uaKcPxw%2FMEdYe8GN%2BgEUPLIKPCX2soAHl17%2Fs9i2XX5H%2F%2BmP9qXNP02GhQZMb1dFtW77GbSnTLTymMfajaMU2AJiKteE3xPX9J593YBBioFhXYiGmIOBVRoiUOy0Fo%2B9UpLc0DQgA43y43mEBBF%2B%2Bp%2FMg7l34h2Y993&X-Amz-Signature=5a7701e4f52da13ad2cd935de2c678ec910f49294e66437fd4f3dc3ff30cddbf&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Data Visualization Libraries
#### 1. **Matplotlib**
- **Description:** The most well-known library for data visualization.
- **Features:** Great for making highly customizable graphs and plots.
#### 2. **Seaborn**
- **Description:** A high-level visualization library based on Matplotlib.
- **Features:** Easy to generate various plots like heat maps, time series, and violin plots.

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/733d1e42-5a53-4fd8-90c1-3d85254369a6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466X4KM6ZSS%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T191207Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAMaCXVzLXdlc3QtMiJHMEUCIQCRSCjvDhJ4zHp0o9dKz0%2FuCpOoGvxFoVF6cWyrmVJJjwIgGVg6W%2BTPa89jai9Uo%2FJPk8Dyzilj4mh0u3rYOKOcWv0q%2FwMIHBAAGgw2Mzc0MjMxODM4MDUiDLyyCVeylULyQGXp8CrcA7k4DiLjsfd8m47M1cP1qmw9rErk1L%2BmT0Dkx2AznnL%2FG6ViJtb1YLKfgoCZCdmnyH2fOwyiqguhRJ8iHNBesL2pUT9rDufTKCDYfCGUsN5NE1R2cbtmDpgNrThVImlrsDDl8br0mUVIt3CccCfI0YE84hugPphjZDOycZhlzxFCa1fxeF3HqVbat1rwp5h7GHdVuKiXqwmPP%2FPxLTE5CCDIHKO3q6X%2FlBTYFXsJXSHynlG8XB4B0xnSiY1MAiYZmuvYUpGd5VP%2Fu7aInJb51CtY48pD%2BmR42FfBYeuWhnIz0zDEsLBj8iD1LLDIrik9R8bfv%2BG%2FFSFWDTYVRffusvDIM%2FzwTwrEzy%2FU0aYiloS40YiXWtU52mySYnZ7e7rMcLEtCvphyITItwFp%2BmXeyREK3slz5LTEjj967KLkL%2FN2Gnu6U9e%2B1RsE9zT6tPn%2Btkm7p78x4sRPOrHeWHxf7VUEDEyljkvgBbntzwirIp632qA8%2BQL28bER7cmKh%2FQJTJiKJ5xkR9qRaCRdu%2B9%2BdIIdFMsW%2Byn07psEfjzjYuGNRqFE0yk1sMBv3RZOsNNjqnsUGM4b9i0bX%2Fzb5EWeIdnBs36BrDPhXw333lgNOVxT1OcGPbg6b%2BQO0EcRMNighL0GOqUB0uZw6S4CNdKN%2F5Z8am0gKl6aGp6uxykw%2BIxQR6rIR%2BFxpqRuTEkGkxYWa7bQ07tXpuHblg%2Bpw%2BACFLo0sTSvV%2FYnf7YwH7gffVzcdyjQ88ET8eLEIAIjLr5RveBeuQHn70ZAhKPsIPZX9p8bPbjh4ykrS2JaUvvY0ghorq99j3mYGryRFuY1cvLueTkA%2BuH2HsIbpdodPcjEQIbfV4MayRcV%2FAMK&X-Amz-Signature=826a45d3616a87a403822bea2bf856b20ebe8af919ef8d0805bb76e74de6c5b6&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Algorithmic Libraries
#### 1. **Scikit-learn**
- **Description:** Contains tools for statistical modeling, including regression, classification, clustering, etc.
- **Built on:** NumPy, SciPy, and Matplotlib.
#### 2. **Statsmodels**
- **Description:** A module for exploring data, estimating statistical models, and performing statistical tests.

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c62885f5-417d-4179-834f-d68f8f2bdf39/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466X4KM6ZSS%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T191207Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAMaCXVzLXdlc3QtMiJHMEUCIQCRSCjvDhJ4zHp0o9dKz0%2FuCpOoGvxFoVF6cWyrmVJJjwIgGVg6W%2BTPa89jai9Uo%2FJPk8Dyzilj4mh0u3rYOKOcWv0q%2FwMIHBAAGgw2Mzc0MjMxODM4MDUiDLyyCVeylULyQGXp8CrcA7k4DiLjsfd8m47M1cP1qmw9rErk1L%2BmT0Dkx2AznnL%2FG6ViJtb1YLKfgoCZCdmnyH2fOwyiqguhRJ8iHNBesL2pUT9rDufTKCDYfCGUsN5NE1R2cbtmDpgNrThVImlrsDDl8br0mUVIt3CccCfI0YE84hugPphjZDOycZhlzxFCa1fxeF3HqVbat1rwp5h7GHdVuKiXqwmPP%2FPxLTE5CCDIHKO3q6X%2FlBTYFXsJXSHynlG8XB4B0xnSiY1MAiYZmuvYUpGd5VP%2Fu7aInJb51CtY48pD%2BmR42FfBYeuWhnIz0zDEsLBj8iD1LLDIrik9R8bfv%2BG%2FFSFWDTYVRffusvDIM%2FzwTwrEzy%2FU0aYiloS40YiXWtU52mySYnZ7e7rMcLEtCvphyITItwFp%2BmXeyREK3slz5LTEjj967KLkL%2FN2Gnu6U9e%2B1RsE9zT6tPn%2Btkm7p78x4sRPOrHeWHxf7VUEDEyljkvgBbntzwirIp632qA8%2BQL28bER7cmKh%2FQJTJiKJ5xkR9qRaCRdu%2B9%2BdIIdFMsW%2Byn07psEfjzjYuGNRqFE0yk1sMBv3RZOsNNjqnsUGM4b9i0bX%2Fzb5EWeIdnBs36BrDPhXw333lgNOVxT1OcGPbg6b%2BQO0EcRMNighL0GOqUB0uZw6S4CNdKN%2F5Z8am0gKl6aGp6uxykw%2BIxQR6rIR%2BFxpqRuTEkGkxYWa7bQ07tXpuHblg%2Bpw%2BACFLo0sTSvV%2FYnf7YwH7gffVzcdyjQ88ET8eLEIAIjLr5RveBeuQHn70ZAhKPsIPZX9p8bPbjh4ykrS2JaUvvY0ghorq99j3mYGryRFuY1cvLueTkA%2BuH2HsIbpdodPcjEQIbfV4MayRcV%2FAMK&X-Amz-Signature=55fad326b187429c31bdcb5896f39955f92ffc06014790ad753daa57b66b5060&X-Amz-SignedHeaders=host&x-id=GetObject)
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
