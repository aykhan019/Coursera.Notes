

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

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/997ac361-58a8-4f04-bb0f-79fea4baa761/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YNEAP24J%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T011147Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGpR5TxzllB%2Fp1k%2BfN1tpwvL5J31TH036sEC1i51hKzRAiAK7B2WYVWch4tLhzfjgXG6By2ZlYpnZQW%2BmBgBY727cCqIBAjh%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMrL0Rtu7NJ1uHk%2FLFKtwDDgwELVIDs4pNeB7YpgxKvwcmDJJKTPMGERDdfwhj5KRLsdQwaurHsaKPJAqfuwvV4BPkwOrIg9xZkVcrBmeuWZpmDMx%2BZtJkOsJJ4lnBrHGA7C8MBkHtEgei70daLJOaa%2BoixefsrYZCONpblXWsLJiZC8ffPje9ryaxoFUmPOWXVEBXOOroU4YNuhnIPGGv3F4tXDFezGSSTL7O9YYFSCz055%2FuZDoqPuvNWuJQH5yC9jbLQ3tB3jUbMpQ00FFqNiT%2B6%2BWG7Tf1taHAjPD03z5J%2Bp6wFwSSO6Th1BNeM3tQIUiHTCOOIFNeuaFYANjZJUrszWPEGpKvtyhOSmWR2TF%2FYc%2Fgr%2BeHcuSLLtAOq9QDC6z0wh3v7x34IRzR4QVd8wKDQmtAmEQrcuIlIef6vOo8J%2B38zjJ5lhkSwH0iPq1%2FalFA2Xs4zVBu0g90b2NjkR0YX1SDEjjDJt6G5iRjFemREczQoU5CD3B9nrbAezHfK9M6WHW3%2BBXwSekZoidOIrb%2Bgq08eTdDsEuff4z8MrFNJyBhtuM%2BoVd7wP6hkvdWpWX5XErNtFla6RqPMGlVD4wRvJ3jME644IuS4QV22Vyo9PgNMTa8BkuwDGlmHyq05qm8WoeA1eajxHUwz%2FH6vAY6pgHTqCWBRKM6zd%2BRvwbh23RGgrBJAKr8kvB7F09wYD6RpOqiHKRLnwUl%2FBv4Vn4E14Jolp5hUiSYgnaSa0jm6HtOWqm%2BQt%2BMk9NmV7YmaD5psJA9UATuHxODzsYg1lfNFmwPLqW%2BGiypybIadak%2FrEgXFBy%2F13uGxUzk2PJcAi5M%2FBAR27iRUPjMVVd4Iq1lgRfKqzXzIPwrJco4sD7%2BOe6WCRwtIyq6&X-Amz-Signature=2165ef76c1c528888e55272e38c64be5b57f4096cbea5a1db6b14cb1a783de01&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Data Visualization Libraries
#### 1. **Matplotlib**
- **Description:** The most well-known library for data visualization.
- **Features:** Great for making highly customizable graphs and plots.
#### 2. **Seaborn**
- **Description:** A high-level visualization library based on Matplotlib.
- **Features:** Easy to generate various plots like heat maps, time series, and violin plots.

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/733d1e42-5a53-4fd8-90c1-3d85254369a6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UFCDFDPL%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T011147Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIALf0V6eKBppY%2BnLZ5VKXTFYrRDEJitQoqRludV90OsMAiEA5h6yn%2B%2Fofo9raX8y4RNTvWbuwq8ZzcQJEz5rgejg1mMqiAQI4f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLy0xCOZFkejwc4V1ircA7bNRb2xi7CTdndVtOKUgxbSR7vJo1DzwMHIq5bZg6UYsW3GGjEjqbf1WkWtglXckB%2FWGkyk8ZZ%2BxOFf9c%2F8kgZeuBr6kKXQi8Uu3tqB2TArkJf7HvHJa5CfZD5HfIJ5lIKBaI4t%2Flv37VAbPX%2FCjMtgTxIqiEYuimv%2BgzQ%2Bp158OmNrEnk%2BiZnAoY%2BDsgBxnVbu69Q2WnfgFtdhy0ef6zZi8b1mEvjqHjUoOt8gYUEFtCebzC1rREA4G%2Fugkv%2Fp%2Fc%2FcRxm5ANsaICa5XmeDknY7xh5PuFImGXP%2BjhT37dVmFULspjfRftyK83ebOWEjAFZAoQMa2I%2Fdz%2FByAcFMtPYplZMsgXr0fe7Y3v1fCQ16Zqo6NOBW2yuiq0qPZqc0zaEGBKHV5wis81Tu9zJ%2FHXoXrbVjFG15Qzey5Yu2vtfyoiqt9oBQAz%2F6rdkyfg4fjv2HGRmvKEQjFGG1PRX8HWk4dDdJDr2rp6Cr8di9ZzYbkniSm3XAnNzb1r8xUApEtMltQBTJyk8lGifjngdEENxw%2B537lemvfoUU224dt0bS3RT3kOok16IG4oQgZSwyhMyTKfFpPmE2dAbZWIcW6lWspCDBw8aPS1afKjvxFsmEEL%2FWHb0nVD2b3FMZMPjx%2BrwGOqUB6TWpsgMa1uN0KokyPaRrRHz8YCXmKIkG6oe97z1Aq%2BuINtXLWbCdC1GoxeMTEFPgIIS7NuG0Z22qRewEfTRu%2Bx3%2BUVe1Oq6DPDgKwGr2lt4%2BrtrWY0NvQUJtdMxAjQrL0yckOmyIeVz%2Bk2yCt6rcdru83nMSMDJvBUqnvPADQvstMzjv8lfEuh6txHRAVPijQm87b6LZUE39kn2BCXMG5zkKnayA&X-Amz-Signature=135ba5c3a096ae8d5b01d1385ded4a65063fe020e0ed11cca2cd4304d9c571c7&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Algorithmic Libraries
#### 1. **Scikit-learn**
- **Description:** Contains tools for statistical modeling, including regression, classification, clustering, etc.
- **Built on:** NumPy, SciPy, and Matplotlib.
#### 2. **Statsmodels**
- **Description:** A module for exploring data, estimating statistical models, and performing statistical tests.

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c62885f5-417d-4179-834f-d68f8f2bdf39/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UFCDFDPL%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T011147Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIALf0V6eKBppY%2BnLZ5VKXTFYrRDEJitQoqRludV90OsMAiEA5h6yn%2B%2Fofo9raX8y4RNTvWbuwq8ZzcQJEz5rgejg1mMqiAQI4f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLy0xCOZFkejwc4V1ircA7bNRb2xi7CTdndVtOKUgxbSR7vJo1DzwMHIq5bZg6UYsW3GGjEjqbf1WkWtglXckB%2FWGkyk8ZZ%2BxOFf9c%2F8kgZeuBr6kKXQi8Uu3tqB2TArkJf7HvHJa5CfZD5HfIJ5lIKBaI4t%2Flv37VAbPX%2FCjMtgTxIqiEYuimv%2BgzQ%2Bp158OmNrEnk%2BiZnAoY%2BDsgBxnVbu69Q2WnfgFtdhy0ef6zZi8b1mEvjqHjUoOt8gYUEFtCebzC1rREA4G%2Fugkv%2Fp%2Fc%2FcRxm5ANsaICa5XmeDknY7xh5PuFImGXP%2BjhT37dVmFULspjfRftyK83ebOWEjAFZAoQMa2I%2Fdz%2FByAcFMtPYplZMsgXr0fe7Y3v1fCQ16Zqo6NOBW2yuiq0qPZqc0zaEGBKHV5wis81Tu9zJ%2FHXoXrbVjFG15Qzey5Yu2vtfyoiqt9oBQAz%2F6rdkyfg4fjv2HGRmvKEQjFGG1PRX8HWk4dDdJDr2rp6Cr8di9ZzYbkniSm3XAnNzb1r8xUApEtMltQBTJyk8lGifjngdEENxw%2B537lemvfoUU224dt0bS3RT3kOok16IG4oQgZSwyhMyTKfFpPmE2dAbZWIcW6lWspCDBw8aPS1afKjvxFsmEEL%2FWHb0nVD2b3FMZMPjx%2BrwGOqUB6TWpsgMa1uN0KokyPaRrRHz8YCXmKIkG6oe97z1Aq%2BuINtXLWbCdC1GoxeMTEFPgIIS7NuG0Z22qRewEfTRu%2Bx3%2BUVe1Oq6DPDgKwGr2lt4%2BrtrWY0NvQUJtdMxAjQrL0yckOmyIeVz%2Bk2yCt6rcdru83nMSMDJvBUqnvPADQvstMzjv8lfEuh6txHRAVPijQm87b6LZUE39kn2BCXMG5zkKnayA&X-Amz-Signature=e367a4e591bdaabc067e0e68ae26cfdbc9839579937934334af6917ae46fcb37&X-Amz-SignedHeaders=host&x-id=GetObject)
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
