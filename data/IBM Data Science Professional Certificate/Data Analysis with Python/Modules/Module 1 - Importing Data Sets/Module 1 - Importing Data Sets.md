

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

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/997ac361-58a8-4f04-bb0f-79fea4baa761/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46662GQGLLN%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T024509Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFAaCXVzLXdlc3QtMiJIMEYCIQD1XAFxCX7UYYBEF4gZ1FzkiGxQursrcb1dBGkGxA8ZuwIhAL4vfzAj8naq2M9w76gtLPqWAR3AZ8djbFSIQVQ1ehzOKv8DCGkQABoMNjM3NDIzMTgzODA1IgxWQ4SIi%2BLbrejhd3sq3AMsfj4JGT60dNMoiQ4IHxMryzbKtARRkJDSEX2n4K1854ubT0r9OoQSld7nNRSXxKJmZaPK35X6KVDUm6mx%2F1HEFwdYi%2BLx0UFbbyBpve7J0jv%2FrPiW%2F%2BNAv%2BZGjyuabzhDTKAbgLH0R6KtcUo%2FTDkeRPj1eOx0RQMCUd0GqkVsgt5wMA2c9p1KgC4wfQ%2BE2Cq7bZ2KmJJbpyxXEncxL4SIU1yGo%2F9vbeBtpIxINm%2FNbwDifIygu5brJn4x4%2Bma1CkjRLFiIsIjrmahUEAcarcxcOKHtvJPEn6eg1IqCIGnc6IMrYvyjX1oCTC9pa7fcerrR%2FT58sU34DzPBxV5QnVuvKvohxQL6CgBjrI0xrfjkpzDRaM%2FkSu7G6kDgwsCVseRyc6acMXvHv20RbFpr8jOOGnwfJ1IXb4KSfwZnMb%2BwTuYJA2fktkHlIJWPpGHZl3KGkdA%2Fx3J%2FiJ%2BMdcxTmonjS%2FKOOm0jUi0ZLGA7bIXg57EIoHbndPmuV9lq3rpbiwKwTqMNRR9Gv3pMlxQKZkLbo0cAd9FwV1F41hvaXgPWbncyJAQbeP4rRUeUCXRi7dM%2B5TLrM8Apg1Y6w1KCOMIFrhO%2FNqdRS5Mb6%2BiQKahmmWUBPGjR7f7CAsGbTCmmpW9BjqkAVYoDSLyxgNmCH5%2FmY4NQ7FceV6jpXIDvlE0bgMGNHvVzfaj%2FGhZ79iVZj0o03Std%2BaQehbSY%2BYM3WHZIZJP%2Bqazbqin35BHURREzc%2BRfFW0ceDVWYcTFv%2FijlVO%2FMQYenFUmEyJL3ZOk9mpicVyJvu6txzlVTY6wDGWlEDjVKuZpcXINeHx9yRkBaSI29EBQMp5f%2FNEOyY4opwwvMv3iz%2BBF%2B3E&X-Amz-Signature=43fa84fc4038104ddc89db7210634c89d04c1d3548aa25d664bb6035906a5572&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Data Visualization Libraries
#### 1. **Matplotlib**
- **Description:** The most well-known library for data visualization.
- **Features:** Great for making highly customizable graphs and plots.
#### 2. **Seaborn**
- **Description:** A high-level visualization library based on Matplotlib.
- **Features:** Easy to generate various plots like heat maps, time series, and violin plots.

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/733d1e42-5a53-4fd8-90c1-3d85254369a6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ROH6OVS4%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T024508Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFAaCXVzLXdlc3QtMiJGMEQCIBjpzbXzKZJaY0m8Fft1itXtqpeWN%2BEOWjzux%2FO4RRtBAiAI1r610t5CddxCQeWEwDL3nQJyAXX94EqJincqa3w%2FFSr%2FAwhpEAAaDDYzNzQyMzE4MzgwNSIM%2F9y1l19HFMzQcilAKtwDm6gd7rvmh7wVtVgAHfolGyhfbZkXKpWb9xUcUj4C96usNSn9B42V7yWAliXWMSwtKde2tLF%2FBhfaaRZKISBbHqFwE3mwwDXnH1hSynGBJ60ccPwWXa%2BbZSZewMlU4Vy%2FqNdpAHdQ3kD%2FU80s8GJHLfFwbm3gD6eAO%2FN1IsFcBP6isvrjgVyxTlT9yHA7%2F0DUyfX4FiDq%2BbSfGi5L8CI4wL4RPA%2BovnKjb70EwK%2FvlkGfqZRRZqKHSKU6q3tyUAeD9Ucga6TMYtzDtWnAvjQU3LGsp05fXAi%2BBEDhIOAekIOtXhL81KLS0eivenJohWiE203wCe%2BbOBROsjajY2XA5Cx4ZerDvERsp3%2FqEyv8bsLxS%2BYCWrfH%2BAH7ilOfHmEqcr6N9MbfwhAPGFGvCNJUdpo1W1qSEU0essZYQnohnhKk0gTCNvnIOjv1jTd0mZZ2EzZMlq7DdptZidUTmxvoGilxZiOSns0JV8C62NzZeizTq%2F3oI3DtHwhajlZO0NZKViytHvU3mnisq%2FpIUnYZhcA2Y7LO0J9AG%2FqeClXfHc80iZ4ypIPAnuq5MmR8rihKKdcd4MLcgtlfxayPxchLNL%2FyU3sJ8TjyyR6xl8qSxQOc%2Fl48mwfUynWj3aMw7ZmVvQY6pgFGDqgJMv1g5n72T9tPdyNrAJYOw6JYQteutFT7thI%2F5yQKiUCecXHa7XXwUf2WiofKSp2QaxE0KFG6eGEZAFRVxTXxK1nKMmY%2Fss%2FnFp2x9%2F4eq8%2BUU3BmEZGEwNDYyKSXi%2Fx9DPxlVeE0lj9i%2BxfmW5k2jK6IPPR1qD7KQ%2B%2B2dDeKTNuQq25IDCkPBJfsqWfTM3PLbT1kvbazLvoeDTZuJjDhxrTw&X-Amz-Signature=70d547a1bcb4ffe4aeadf296fb9ef085683b0e40af0752b25105cf75d97ae86c&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Algorithmic Libraries
#### 1. **Scikit-learn**
- **Description:** Contains tools for statistical modeling, including regression, classification, clustering, etc.
- **Built on:** NumPy, SciPy, and Matplotlib.
#### 2. **Statsmodels**
- **Description:** A module for exploring data, estimating statistical models, and performing statistical tests.

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c62885f5-417d-4179-834f-d68f8f2bdf39/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ROH6OVS4%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T024508Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFAaCXVzLXdlc3QtMiJGMEQCIBjpzbXzKZJaY0m8Fft1itXtqpeWN%2BEOWjzux%2FO4RRtBAiAI1r610t5CddxCQeWEwDL3nQJyAXX94EqJincqa3w%2FFSr%2FAwhpEAAaDDYzNzQyMzE4MzgwNSIM%2F9y1l19HFMzQcilAKtwDm6gd7rvmh7wVtVgAHfolGyhfbZkXKpWb9xUcUj4C96usNSn9B42V7yWAliXWMSwtKde2tLF%2FBhfaaRZKISBbHqFwE3mwwDXnH1hSynGBJ60ccPwWXa%2BbZSZewMlU4Vy%2FqNdpAHdQ3kD%2FU80s8GJHLfFwbm3gD6eAO%2FN1IsFcBP6isvrjgVyxTlT9yHA7%2F0DUyfX4FiDq%2BbSfGi5L8CI4wL4RPA%2BovnKjb70EwK%2FvlkGfqZRRZqKHSKU6q3tyUAeD9Ucga6TMYtzDtWnAvjQU3LGsp05fXAi%2BBEDhIOAekIOtXhL81KLS0eivenJohWiE203wCe%2BbOBROsjajY2XA5Cx4ZerDvERsp3%2FqEyv8bsLxS%2BYCWrfH%2BAH7ilOfHmEqcr6N9MbfwhAPGFGvCNJUdpo1W1qSEU0essZYQnohnhKk0gTCNvnIOjv1jTd0mZZ2EzZMlq7DdptZidUTmxvoGilxZiOSns0JV8C62NzZeizTq%2F3oI3DtHwhajlZO0NZKViytHvU3mnisq%2FpIUnYZhcA2Y7LO0J9AG%2FqeClXfHc80iZ4ypIPAnuq5MmR8rihKKdcd4MLcgtlfxayPxchLNL%2FyU3sJ8TjyyR6xl8qSxQOc%2Fl48mwfUynWj3aMw7ZmVvQY6pgFGDqgJMv1g5n72T9tPdyNrAJYOw6JYQteutFT7thI%2F5yQKiUCecXHa7XXwUf2WiofKSp2QaxE0KFG6eGEZAFRVxTXxK1nKMmY%2Fss%2FnFp2x9%2F4eq8%2BUU3BmEZGEwNDYyKSXi%2Fx9DPxlVeE0lj9i%2BxfmW5k2jK6IPPR1qD7KQ%2B%2B2dDeKTNuQq25IDCkPBJfsqWfTM3PLbT1kvbazLvoeDTZuJjDhxrTw&X-Amz-Signature=0de3ae8454b2e897d34b41b48e4aa46a4e41442c0fc188b10c60888f5e4b9d06&X-Amz-SignedHeaders=host&x-id=GetObject)
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
