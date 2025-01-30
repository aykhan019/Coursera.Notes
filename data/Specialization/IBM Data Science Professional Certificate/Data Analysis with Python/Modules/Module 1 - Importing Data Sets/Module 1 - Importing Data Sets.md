

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

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/997ac361-58a8-4f04-bb0f-79fea4baa761/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UEVJFIUO%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T051520Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAdw6lZOOvJAh6PLar%2BOYpjKa6WEIMm03SnU%2BPC%2B0%2BjlAiEAl%2B1C4G88LGLcYRp7qejC36AJSQp%2F102WtqYRjKKBqUIqiAQInv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDCFz1rgEqAWW%2FMhTRircA%2B7lqS1%2FE%2B9DXVFbMvMoLIDRxHwwCGdIXUx4Wxge%2BSs1qou5fBpXBPvUVhrqSsVxRPCD6hjAda0J14pic8xuXdJmIVJ0qC%2BM5bUXaFBWdzoRrq%2BN20dSCP5cTZz52DVrel%2BhfaQPuTI%2BfhQQggND2ySVcR3x2fOd%2FmHMtyXzlujmCbZYl9yEBRQ7crGIFLdFlq4XDx4NHPMtgOMyBBrpriOnkixfTznM0buT%2B%2FU%2B2UwO3lGaq4v4rjMkXRN7sNKdXUnF60tAKGfKNmzh7qCZICy2mthdu4YgkNd1FKQzm5ywd2lUUc1XWDaD1JhFA0AKh3KKHvDPSdUZMvsWsZAbdTQz2poaWnXXKTN0c5kPFiRlIM5GG8xvKMsrBnqarz5rlDjOYNBq%2Fy5N5UtH2%2FV5Bz1aRxFaq0OiT0xwTCjIelfBaR0n1dZa6VdAWNXc1jcrUwAJV5ewrsaVOzToKxFn6Vn3N3Ne4bbkc%2BZGwbtv9xaqhFww45S97AtXYl0hSkhs%2F6ivXWlE0WcK%2BMPO17tQ8ii5QaBOkNEU5gOg33GkfEsKQWbZYkK4dyZcsPaigJZlLUNXjkEZKoalB3B1%2BdaKmBnpB%2FT9ncKVwOItH9EmeVhDPWpEyJko3%2Bio5v6DMOaG7LwGOqUBR2mhTwzEstVMwsGcLO1Fxhx3BxYwj3aC9LmJk1fKPB1SuGHVuRBSiLP4XEnsIeVhgLi%2F3Jyz2CfgKoO6o9Ws1WC3799DAtT5zwWZKrqxLyaz6jli9ltXtER%2Ff2cJ0bmLne29i1UP0KeOT8NVw89%2FRN%2B6Vb3fPgR7IhBltDesZ6nbg5Q3q8IQBwFtgRngC6SdPPm246udl7wcqBXX882Uax2S5SfD&X-Amz-Signature=54ca946447648fad235c32c1c63d90285a977c7c7e95795f82b7b2ed38c21815&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Data Visualization Libraries
#### 1. **Matplotlib**
- **Description:** The most well-known library for data visualization.
- **Features:** Great for making highly customizable graphs and plots.
#### 2. **Seaborn**
- **Description:** A high-level visualization library based on Matplotlib.
- **Features:** Easy to generate various plots like heat maps, time series, and violin plots.

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/733d1e42-5a53-4fd8-90c1-3d85254369a6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Z7BACOF6%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T051519Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICpyzBuRjpbANd09J5v7trFKpwAbyFdDVUGGmiTNacWFAiBvB1tG6D14HjlabtNMLh1jI9bT5z8%2BjzyBiHwZVvNiDyqIBAie%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMbNjpf2cttbsfPALDKtwDT3H1Aa3il7L2wvNoHbsG91QCJcARJZHLHmXbOkqFmWQrjioXyQFlgD5uU%2B%2BX%2FqK95r7eUfxWJANAuR5QvWRr9Vmi%2BFNUPatKKbUNn3ywMNl7hWhuQQa0O8J%2BDLox%2FmfdsumLs6S%2B4UxqhFtkWbZsr2P0KQZetiMJRD%2FaHCXBWV8DCBAu6exbAsdHVrnfKz4zQEXyBAY39qFmABXgqrWp8MlMfaj7y%2FlVO6UvB0O%2FU74DFMaHxLaLf6iNYakQpYZz%2BY2kbBTJcXGLwMbBzxRBJyt%2FBl06%2BcGve5QDFHdoc1FFOGAMbiWrgS%2B%2FITPABlmsjVsjE5az7%2FoUuJ1c4UmcK%2B9O38qJRReCQclPt2hajA5vfcR58RY8IamE4WAfn8ZpcFeq81uVao%2BgEEbklTLxgoXcmAPTODz0vh4F%2BJ5GjX9OwRMLN7%2BagyFxIQBK3M1y83dwkEpZTwQnp8lsCc9Q0rnnoK%2FESHrkWrsfe0Ck7eNWBEIOdAMs89UGS10PB6cloEcgiBblnHEefUWVNN9xUk0n1N%2BooxbqymNzMqnW8zX9T3iEwnmBSfRJLM4K%2Br4uDVth2yBMYmKop5dqGYNtOzMkHRrTtRAZJuqpRXUh%2FNywc5peK2SLQx4FfH4w0obsvAY6pgGKVf9mZJuJJRmhHlsqVYfQIb9B%2B2zXvLaD5SxhQcgcKjAUaHqx9n1iQzc8mHt%2FM%2BI9saMSqp5C08xXkLGTvt8i45W5fwCIqHKPBKnlmR0eGj6FIIJBha%2BkPPCRBC4EHEoDumL1i%2BfZ6foY8LCmiKhJPMI4Xteaapc7OtwvNufFRn4X%2Fccipudt%2FNdU%2FVNyZ0VkcvhqOUkAlFlxvGyYDyX09K1TuKjI&X-Amz-Signature=0bde5bf86875424d3ed72a2295b9ac83bdea820cabd817fbe07979db47a76fe2&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Algorithmic Libraries
#### 1. **Scikit-learn**
- **Description:** Contains tools for statistical modeling, including regression, classification, clustering, etc.
- **Built on:** NumPy, SciPy, and Matplotlib.
#### 2. **Statsmodels**
- **Description:** A module for exploring data, estimating statistical models, and performing statistical tests.

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c62885f5-417d-4179-834f-d68f8f2bdf39/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Z7BACOF6%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T051519Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICpyzBuRjpbANd09J5v7trFKpwAbyFdDVUGGmiTNacWFAiBvB1tG6D14HjlabtNMLh1jI9bT5z8%2BjzyBiHwZVvNiDyqIBAie%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMbNjpf2cttbsfPALDKtwDT3H1Aa3il7L2wvNoHbsG91QCJcARJZHLHmXbOkqFmWQrjioXyQFlgD5uU%2B%2BX%2FqK95r7eUfxWJANAuR5QvWRr9Vmi%2BFNUPatKKbUNn3ywMNl7hWhuQQa0O8J%2BDLox%2FmfdsumLs6S%2B4UxqhFtkWbZsr2P0KQZetiMJRD%2FaHCXBWV8DCBAu6exbAsdHVrnfKz4zQEXyBAY39qFmABXgqrWp8MlMfaj7y%2FlVO6UvB0O%2FU74DFMaHxLaLf6iNYakQpYZz%2BY2kbBTJcXGLwMbBzxRBJyt%2FBl06%2BcGve5QDFHdoc1FFOGAMbiWrgS%2B%2FITPABlmsjVsjE5az7%2FoUuJ1c4UmcK%2B9O38qJRReCQclPt2hajA5vfcR58RY8IamE4WAfn8ZpcFeq81uVao%2BgEEbklTLxgoXcmAPTODz0vh4F%2BJ5GjX9OwRMLN7%2BagyFxIQBK3M1y83dwkEpZTwQnp8lsCc9Q0rnnoK%2FESHrkWrsfe0Ck7eNWBEIOdAMs89UGS10PB6cloEcgiBblnHEefUWVNN9xUk0n1N%2BooxbqymNzMqnW8zX9T3iEwnmBSfRJLM4K%2Br4uDVth2yBMYmKop5dqGYNtOzMkHRrTtRAZJuqpRXUh%2FNywc5peK2SLQx4FfH4w0obsvAY6pgGKVf9mZJuJJRmhHlsqVYfQIb9B%2B2zXvLaD5SxhQcgcKjAUaHqx9n1iQzc8mHt%2FM%2BI9saMSqp5C08xXkLGTvt8i45W5fwCIqHKPBKnlmR0eGj6FIIJBha%2BkPPCRBC4EHEoDumL1i%2BfZ6foY8LCmiKhJPMI4Xteaapc7OtwvNufFRn4X%2Fccipudt%2FNdU%2FVNyZ0VkcvhqOUkAlFlxvGyYDyX09K1TuKjI&X-Amz-Signature=5831b114f1f18b1e250ea0c40664f6e2521df0995707e2082949918c9ed346e0&X-Amz-SignedHeaders=host&x-id=GetObject)
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
