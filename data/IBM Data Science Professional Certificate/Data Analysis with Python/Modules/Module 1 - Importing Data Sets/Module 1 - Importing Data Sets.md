

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

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/997ac361-58a8-4f04-bb0f-79fea4baa761/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QUOPXRUM%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T221259Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCwvXYTccWFS96PCDIR5JhVBt7YU9YAPgEEOnBs3baqzAIgU5IHNt5er2BCX3ERII9lTk5KerWAaRfITacz6sNcI%2F8qiAQI8%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDCaD7FywJxgPtqubEircA0Uqg9d3ZLgRhdQojtQ4o3GGjBLIBQRE%2BOmIiMCn%2FFHMeFono8pb4qhKvIOusXEjryLypYlnC4TMjEgswyA%2B75KpCpxs0sIYXB2YDzuzMuPLSsU4DX14T6wmVC37z3ymfX7%2Fg8YFkaGR6KPhTsbh9iXhe4EpFC%2BIsBHquxTF%2FvsruKAK0WEhpveC8%2Bd3FTH23wwIcPLjGRhEt2LsNPb%2BgcCFXBbFSR3tV9WvJDebOatkc6DZQJJ1dDFS6%2FjaJ5xP8%2FWoDFh%2F8GwwjnD9lSogUvDcD57PLOmpWP%2BqkHfGHvjQhrnDWEtLOMmxL0K2TOqyYqflQNhXzO%2BX%2FTxJ60igmOtIeGeKVsmRwqU%2BGljJnCjaTVFc321873yf%2FskgZBK5VuDz3LN7yJR50lE5ZwiO5YJF49enYd45RwlyAWKE4mhawWbladzQQ6jZbp030hsmxDNGIrs8RtGiZBnHGyFlpeiuhaXpNsQM%2BWREmotkfkb%2B5W3KcjDJ6jZkLYJW4x10Pw%2FhFkrhaBOW3%2FZLUJN03VFpn6kkZkrAYqsYDMKdkPBE7Y9rPT0YkJhQ5v6FLMaDMkt0VHMLSQSHfrZhpyil2A6HF8p8ygW9xbLmx0OusifmJ8tfE2SOjR4ZcS6%2BMJ3h%2FrwGOqUBMFo4xBs8FoiLjhbldIT5rgIXPv2lvKP2F2UAxFmCV8jhZv47FlIXvzD0D1nXwI5sEy9cQ%2FQ2Y73QyMVTkNAupJi3vA%2BbFa%2BYOfEY0PvsmRaqW2q%2FVy3Uf%2BnTsCv42u8HTj%2Ft90MwWf3guwtIMIN9OGPyNsir0IBzljfF7dLxgncE%2BBXGths4ThgqMgW2CYRWUpVU9%2Fw%2FOYCCKMJLi5%2FgPI%2B0a6Lm&X-Amz-Signature=1e63b0d17231a9319170231548ee0cd51b0349bbadeee0a0f9f2e6fac75eaf0a&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Data Visualization Libraries
#### 1. **Matplotlib**
- **Description:** The most well-known library for data visualization.
- **Features:** Great for making highly customizable graphs and plots.
#### 2. **Seaborn**
- **Description:** A high-level visualization library based on Matplotlib.
- **Features:** Easy to generate various plots like heat maps, time series, and violin plots.

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/733d1e42-5a53-4fd8-90c1-3d85254369a6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WKGOKNVA%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T221257Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHq%2BBiYDKgHqkgqBtYTMCXDhD1Ql1IcBgA6hipRcFTZ1AiBmn8SMdUGKSL1yezq8ccZO9%2FZ9AscC6t85tweHc18OTiqIBAjz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMKKM61LCevyRmejs7KtwDQH0MCKqQ4Ytt4Ag%2FIsd3OBl%2FdX%2B42BFV7dQunLbHejZ5p2aP8NmBlDFYkvVi8bZQ1FLm2o2IbiSYCU%2FXN8cOJeNqqRF1xd9896UnNkHzW%2FE78WiWGQjbbyWBRreIQigOEoFYh4%2BdoM0ht8Xq%2F4RgoGVyojbz1ESBBAIojXRkwDSwHz7xZAMhAxmjrjbtaYm9HlIf4v9ko1nhwnAGq1G1dc9B%2Fc0xLjBgf75KzeLeulf3zAYguLpDiV67n2pY2vb28VTNhWWBraaYXh6Chz0Idn4vlco%2FOFeM%2BFH5YMZ9RvHeZxYHb%2BW4uATz4jdVRpotv%2F1SPd7IA%2FD3JY1fKw6khXrAPKjbS8CtIIMZct65rWyGgWFVqfvrvFVK3axKO3iDUT0Er8eotl7qJodue0KEi6avh1oFHoJJVg%2BqKIRwkja%2BLgVMaLYXy90cN6jemwZSU7wkWJqXK7XaZ6sEQF2I2c4l7X7SCaEw4Ek5Lkcjx7d0YfeLLnD6ze1R0m%2BWRZfOSUgF7YUyKh564Gm5UNFng1vponIq5SacZY0FEF4x9AUIsvifyW8xcDkuqYj6uTl6WRsfRpZyzPQLZrkxWsX%2FQbYB5%2BqxDuHZEPn1MG6EOdIRhjDDVAeP5G7mOQ4w6eP%2BvAY6pgHlQ%2F69%2BBNzkmiwAd8KJAbhq61m4xoqdyrNIYb18116DFpyr6NhOeBnwenqhaaz4%2BacTckjKAOsEtlx%2Bp1uD0z2Ure2fPsipZMD7HeMkA7ZgpeSc9Ji7pEAQ8JB9peyanvirUDw57ru%2FW6T%2B%2BbdEpD2vSjZVFymvIUzJMwekWWSsotOzcgyxhpEHPWYk0l41zHO9IqXaukGK7vsfXF74wvm3I40txFQ&X-Amz-Signature=d5ee1bc5b0e21f5ca3ad585319a66720db48e84e95de3f46ada8c740ad0ac59d&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Algorithmic Libraries
#### 1. **Scikit-learn**
- **Description:** Contains tools for statistical modeling, including regression, classification, clustering, etc.
- **Built on:** NumPy, SciPy, and Matplotlib.
#### 2. **Statsmodels**
- **Description:** A module for exploring data, estimating statistical models, and performing statistical tests.

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c62885f5-417d-4179-834f-d68f8f2bdf39/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WKGOKNVA%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T221257Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHq%2BBiYDKgHqkgqBtYTMCXDhD1Ql1IcBgA6hipRcFTZ1AiBmn8SMdUGKSL1yezq8ccZO9%2FZ9AscC6t85tweHc18OTiqIBAjz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMKKM61LCevyRmejs7KtwDQH0MCKqQ4Ytt4Ag%2FIsd3OBl%2FdX%2B42BFV7dQunLbHejZ5p2aP8NmBlDFYkvVi8bZQ1FLm2o2IbiSYCU%2FXN8cOJeNqqRF1xd9896UnNkHzW%2FE78WiWGQjbbyWBRreIQigOEoFYh4%2BdoM0ht8Xq%2F4RgoGVyojbz1ESBBAIojXRkwDSwHz7xZAMhAxmjrjbtaYm9HlIf4v9ko1nhwnAGq1G1dc9B%2Fc0xLjBgf75KzeLeulf3zAYguLpDiV67n2pY2vb28VTNhWWBraaYXh6Chz0Idn4vlco%2FOFeM%2BFH5YMZ9RvHeZxYHb%2BW4uATz4jdVRpotv%2F1SPd7IA%2FD3JY1fKw6khXrAPKjbS8CtIIMZct65rWyGgWFVqfvrvFVK3axKO3iDUT0Er8eotl7qJodue0KEi6avh1oFHoJJVg%2BqKIRwkja%2BLgVMaLYXy90cN6jemwZSU7wkWJqXK7XaZ6sEQF2I2c4l7X7SCaEw4Ek5Lkcjx7d0YfeLLnD6ze1R0m%2BWRZfOSUgF7YUyKh564Gm5UNFng1vponIq5SacZY0FEF4x9AUIsvifyW8xcDkuqYj6uTl6WRsfRpZyzPQLZrkxWsX%2FQbYB5%2BqxDuHZEPn1MG6EOdIRhjDDVAeP5G7mOQ4w6eP%2BvAY6pgHlQ%2F69%2BBNzkmiwAd8KJAbhq61m4xoqdyrNIYb18116DFpyr6NhOeBnwenqhaaz4%2BacTckjKAOsEtlx%2Bp1uD0z2Ure2fPsipZMD7HeMkA7ZgpeSc9Ji7pEAQ8JB9peyanvirUDw57ru%2FW6T%2B%2BbdEpD2vSjZVFymvIUzJMwekWWSsotOzcgyxhpEHPWYk0l41zHO9IqXaukGK7vsfXF74wvm3I40txFQ&X-Amz-Signature=37b712c5102f4d7e077be7b45c8654fb52aaad0f271b760da1e116101ea70d58&X-Amz-SignedHeaders=host&x-id=GetObject)
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
