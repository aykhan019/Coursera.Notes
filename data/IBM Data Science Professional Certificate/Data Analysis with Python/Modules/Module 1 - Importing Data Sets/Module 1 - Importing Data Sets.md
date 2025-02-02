

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

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/997ac361-58a8-4f04-bb0f-79fea4baa761/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TYYLXVVJ%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T041620Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCID2L6Ci9ve55%2B3yv3fUMiAUZf9aXJqqEamibVrGn76kRAiBmY4woOu9chnfgBonRD7gpLfP9ENfZgQ%2BYmgE%2Fzv6gxyqIBAjl%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMGpJ%2Fc7xqtHgpyxIMKtwDZBtMW5QPAkq%2BPqBw8PfJ5rZKlvqZJrvgFtc0VQg%2F40L5arta4DMEQ3EebvXyXwm2DYArTI2MN4iM90g3yFQvZSqgOYlsmxaVZTXcpdTUolUo%2F0YE9rHmxZ4GMnjHIjPoEVxbHqFrmQLk3T%2BnuqJSBNJ7ybn85Y1jOolC2kG4FulEOnA3HPVzqS6Su%2FBW5Ug2CkgUgXuddCp3c3nUUTkCN8sM1spWQyZrYhNsE%2F5MZuzPkjRvVKXAMQjag%2FOzPdamoWFAJeCGBBS564RaPHmEGQgZicBfUDq3QXQDLSe5t7EMy6bbsoeN%2FVzdIinqp7ibe3BvphjamhQZNrVrrZ%2Bkl3s5IMJyKdXOzlYgMriJ%2FjL48Zb8H58a5WxGPv2MaNQM04UOZ1Jxyk%2BMwBtT%2FsGPeUvLYdWELWUsv4IjOrRt0d1cvkiYIHsLdW%2FbDL%2FKt9%2Fk%2FN3nHKS%2BnAWJIlCHJCjAkW2sP8%2FDum7TImDZuu9cWemCkF67jnb2c2SxHZAjxVsq9yBoyc%2BPi%2BD%2BYjvaQofKsfckGSVAfJvRNbZ7ZypBwebbct6wDunbCax2%2FHY4STKCV24sttxIliGlFDZlK3u%2B07NbED1649rqpXIE0mRThdHTJj%2BGrWBh9NydAlswnuH7vAY6pgE6JuRA2OGNBDtFyiRh%2Fh4Fk%2F0RXY9Fp1y67yYfJdQTcKYsbs57UyWvbft48tXnrbQRvLCOlTxW1aJ7NhfPsEPSDNNCabfnh9pp95JJNkBABhZ88ZgT9NJhXiyXylRojZ6HlHiQGkciUa7ByyEcpVaSrAuFRn%2BiaycpmwE4KzyUwWgfAPF2%2FHql4D7vNfuRklhxGJvgSKDVi7XlGjaOcnyYVtkmTsdk&X-Amz-Signature=ba9374864c17d1313ba470e742ad6c20af6bb946aff0050206027d947473209a&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Data Visualization Libraries
#### 1. **Matplotlib**
- **Description:** The most well-known library for data visualization.
- **Features:** Great for making highly customizable graphs and plots.
#### 2. **Seaborn**
- **Description:** A high-level visualization library based on Matplotlib.
- **Features:** Easy to generate various plots like heat maps, time series, and violin plots.

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/733d1e42-5a53-4fd8-90c1-3d85254369a6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R2DIVUAV%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T041619Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEuYkKByiS86Eull1rQz2s19OOmQ089xox%2BRAxNU%2BGvRAiBYIA7yYU7aGx%2B5Nx1%2Be8AX6tzkARTyasMVYTAjPqe5aCqIBAjl%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMmxHFN7aq51kbcAJIKtwDFUy0by7EmUb67Ij9CTn1GDj7enNDYWv7YMCQ%2BkG1GxzweRNKcblqFWG6FSF8kuQsAV%2FKmlY8HbH1q%2BndW3ZxTd0y9Xe5QAXxEDOWSs0hdgW%2Bl8pJFlKInsxtNwELN0yWHaHYYoye3CpPbaWZlCn%2B22Vtuo5gGoSqWKnsE4P9nk72ETtpNSo6KxjycJ4nrJLJ3yzEjBz8sQq2ESpkmOFdvDf4wyGuZs0jpay35Ay%2B2YBM%2BsMORPzP2MmFJkxEHrMHVf0Bx0PsYOuIfCvLzwGkEyXEad78TVkBw13UiEeq%2FVFzQeQrvddmS3s9OrI0pVNxAcQP4Ll6TGq19y8rmPzdpVCwRAPthmXeiKwi4Hmh4B1cTowbsIRbHaSgmYodYyMHZQT6o%2B8zTElFcXv%2FzEfzP7CZk3TtdH%2BTZDt6WO2k%2FgOhhzDdyixzVi2cdMzKBEYU8PcN82i0NRKRXOVFTbODZ1nv7xdyy0DE98M6jehxuMm32PrG7T2B68ZK6OOSf6pu4myBrUvPMEK9ZBN%2B25PT7yiQ7WZ%2BA24oHguayAC%2Fzbm5OOfa5t%2FKZ9aVJiNw609W5cyK3odoasu%2FV4TGsICpWyIMLgO3K5bjzkzEPdI38%2BhvcKiqJArcctF9RPMwteH7vAY6pgEqoeA1vwCBGj938hqg0QFTJol8NVHrNKA5p2W1eyZxFa9G2mU4M75EiMaDFncCHRQgMeYnLunt4BfJxWEtOKNXQNYHgO03abcyf9t0lnuXDIDjcDX%2BgxfhiPuDX%2FfteMIX%2Bq3WPddjsf%2Bh3Bx6FtIX7xWJn3nML2lVoEh%2BKct26hA0FF%2FOYe3Tsb4HBI2uew5eCLGTUiFCjKysCW4I6BgEKRUTRw3w&X-Amz-Signature=3ea0492809b2bafe4dceaaa6184817a6cc610b274df51d6b1082d4861c14db40&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Algorithmic Libraries
#### 1. **Scikit-learn**
- **Description:** Contains tools for statistical modeling, including regression, classification, clustering, etc.
- **Built on:** NumPy, SciPy, and Matplotlib.
#### 2. **Statsmodels**
- **Description:** A module for exploring data, estimating statistical models, and performing statistical tests.

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c62885f5-417d-4179-834f-d68f8f2bdf39/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R2DIVUAV%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T041619Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEuYkKByiS86Eull1rQz2s19OOmQ089xox%2BRAxNU%2BGvRAiBYIA7yYU7aGx%2B5Nx1%2Be8AX6tzkARTyasMVYTAjPqe5aCqIBAjl%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMmxHFN7aq51kbcAJIKtwDFUy0by7EmUb67Ij9CTn1GDj7enNDYWv7YMCQ%2BkG1GxzweRNKcblqFWG6FSF8kuQsAV%2FKmlY8HbH1q%2BndW3ZxTd0y9Xe5QAXxEDOWSs0hdgW%2Bl8pJFlKInsxtNwELN0yWHaHYYoye3CpPbaWZlCn%2B22Vtuo5gGoSqWKnsE4P9nk72ETtpNSo6KxjycJ4nrJLJ3yzEjBz8sQq2ESpkmOFdvDf4wyGuZs0jpay35Ay%2B2YBM%2BsMORPzP2MmFJkxEHrMHVf0Bx0PsYOuIfCvLzwGkEyXEad78TVkBw13UiEeq%2FVFzQeQrvddmS3s9OrI0pVNxAcQP4Ll6TGq19y8rmPzdpVCwRAPthmXeiKwi4Hmh4B1cTowbsIRbHaSgmYodYyMHZQT6o%2B8zTElFcXv%2FzEfzP7CZk3TtdH%2BTZDt6WO2k%2FgOhhzDdyixzVi2cdMzKBEYU8PcN82i0NRKRXOVFTbODZ1nv7xdyy0DE98M6jehxuMm32PrG7T2B68ZK6OOSf6pu4myBrUvPMEK9ZBN%2B25PT7yiQ7WZ%2BA24oHguayAC%2Fzbm5OOfa5t%2FKZ9aVJiNw609W5cyK3odoasu%2FV4TGsICpWyIMLgO3K5bjzkzEPdI38%2BhvcKiqJArcctF9RPMwteH7vAY6pgEqoeA1vwCBGj938hqg0QFTJol8NVHrNKA5p2W1eyZxFa9G2mU4M75EiMaDFncCHRQgMeYnLunt4BfJxWEtOKNXQNYHgO03abcyf9t0lnuXDIDjcDX%2BgxfhiPuDX%2FfteMIX%2Bq3WPddjsf%2Bh3Bx6FtIX7xWJn3nML2lVoEh%2BKct26hA0FF%2FOYe3Tsb4HBI2uew5eCLGTUiFCjKysCW4I6BgEKRUTRw3w&X-Amz-Signature=21ebb93ccea2b8c18cc65649c71bca88abf3bf91d8118d849af97e68efc5eb85&X-Amz-SignedHeaders=host&x-id=GetObject)
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
