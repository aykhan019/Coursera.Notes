

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

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/997ac361-58a8-4f04-bb0f-79fea4baa761/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WKBCP3I5%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T231358Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEB4aCXVzLXdlc3QtMiJHMEUCIHPr2R2f2HIeHMP39lSpxG0xklZ6RlPqU1k5LTPxHe4XAiEAxji%2BrQDZzTQhLTxtx4b2X7WzHkA1AWAQVhGJA6vSHusq%2FwMINxAAGgw2Mzc0MjMxODM4MDUiDNQa6fiqiIZKvDtCNSrcA3JGXCvzVncB8MPmIqIT8fFDzE4oCfyDY%2BAcG9Lv26DZ%2FA2W2wo32JZDPElbAshtsYe2i3KjFb6ndBO3iPUBRWsOSVAr%2BbMpwaGzwOKjwWX8R8v0EqksN8ObcWqnWYj896i9KKp%2BqUZjoeXPjV8YCvezr6guGRIEj2%2B0wQwvHhs8VruxEtYK8fNhqby3rHGlCfjZ35CS0mDNvsWytihJX%2B9E5DXTlEZjH7wFv5cba5fUTm7J1AllmODyIg5TkFBoqjpnuURr6%2BwKSo%2FxkE%2Fp8dKq9QRPI3l%2BOakyfYYxgToc1q1UuiURZfeQe8y9H%2FcSXQtSeiA6IOaJogFDCQWlkaipW9zD3eVJ6mjnJYapUPmtKbz4Bdug1c8%2BZxEKsSoZWOkndNRLF9qjQcgCJVVtZR6BNq7bU5bqTu7RGRkom%2BG%2BRUzhzFyA7gfPzJJuY8OhVYCeJdxwWDVSUZp9%2BHlgGhGG3sQdq9a59q%2FQKnzX3GLEe%2FKriOmGNE2C%2FHAS%2FKKTp4OvizdqH8Vwt086DBpiaDJFlkiHpxXpNveFX4P%2FLOzZ2TeGY6ZKscXm2gDmjQcjFHIb3jyPR3r17Ay2JTmgjnX1PMuYo69fzwWgEBM7%2FAQL4WAVsKjQ9F2aXnQpMKiUir0GOqUBY53YqojhzhAyVEE7%2BIoP1zWH57XIqTmy%2BwMKijY%2FwSe10%2FaDbDgGu%2B7819do9pLvnMVtVD7bm78WmCg729kNpTxBQdS0FlZHtufdEveOzyaMK%2FkDLqLSrqIM9Rxbd184QeryfcvyazAfnj%2FZKqK%2BY10eT7dqUvodIiZaUeXl0lt%2Bdzt1wDyJHYoxmLxVgDZNFRM6Yf%2BS6r807xn6LghFYLElxMLB&X-Amz-Signature=5e3009b70b98ae80ae22ce3ec07d389b90b97e9e46d6e398b430d052a129faf4&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Data Visualization Libraries
#### 1. **Matplotlib**
- **Description:** The most well-known library for data visualization.
- **Features:** Great for making highly customizable graphs and plots.
#### 2. **Seaborn**
- **Description:** A high-level visualization library based on Matplotlib.
- **Features:** Easy to generate various plots like heat maps, time series, and violin plots.

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/733d1e42-5a53-4fd8-90c1-3d85254369a6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YM5HKIGP%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T231357Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEB4aCXVzLXdlc3QtMiJHMEUCIGkf%2BX2GsAeus%2Bid8vYdasfzLCZdlGlrzCATqpsPuqhUAiEAk66gib686N7dTKHK5deWo4ugffJ8l83ZO%2BrOds5mJLoq%2FwMINxAAGgw2Mzc0MjMxODM4MDUiDLZthjK0wjxlMfN0OSrcA8rT5mo48Jdm2d2iE7dK8eV1w5nkNJxrHQWY%2FNq7d0pUowBJavoo2kTwAPCW7702oR2mYYZ%2FE5swO7Crxz9vzdPUefteO37e4mQrvatNIfR%2BFjK1YtJC6VRmVrxnGeZ%2BcZQPK%2FdNHA5q2C3kCrlT4cXflEqu8IMlSLExjYO8qkUNym4j1sslExbZNIJjs8BWNx%2BsCZTU7g%2FGOghb8p9KEz3pPRZp9rkS2J6OnNhfZf6Zo8HP5figSxByab2RgH0eFN4wA6fCkaNIFvB8btcePOEB7jdppejSoDierxeuICZDJDskpj9Qf4uJoqL4LqzbZ1pDZO3%2BvJnphpgv8t2hrLwtz7c1AT2UAgRFsRm568UyFDNT0IzbZsZOh28eskLUCU8KLGS%2FU1tZ2jrorgWot3To5eVQH4IUa8RtydDw23wYtZAiJIXO57t6gMjP5Kep5akC8RSvjFDqqvbw2TNW2YTuE%2BADe7yOrTliwZaG58mPOtcDHD6arEtFdPCOvLKFyF8a65yfGlelQayXynVlfobXJzbp9JVIBgMq4x5s%2BJYZCfS%2FygoC5%2FnT2%2FbMJO5FXb4QnpnM3fa6dg3hF1CHmFWFH%2Bv88Mbr9%2F52qHPt%2FooJ6WfdCi%2FQdYabG%2FdBMLiUir0GOqUBWotuIXX4kcr8%2FtONAc4jcOHGkSSWpyDCgUa3MqCYh5gZrIyABedUnSPOFL1GXLdfCWV1yn06xZhqquK0GCgGBncZpn9GdHgZerYchc7rsSYm0l%2BFUzVcoDbfN5NL4TVItvlUHs9aUTsvCehFSSnNAfPAU%2B57NWo2zsMq4wATHuRtayzk3nSTWQ%2FHxOsYibSBvsvWjJAxyJ6jTwJZm%2FW5j2yTmhLj&X-Amz-Signature=6c705fd862b6710f245f9b85be321b068cd0dd707ca682ccde3a86fb9460e663&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Algorithmic Libraries
#### 1. **Scikit-learn**
- **Description:** Contains tools for statistical modeling, including regression, classification, clustering, etc.
- **Built on:** NumPy, SciPy, and Matplotlib.
#### 2. **Statsmodels**
- **Description:** A module for exploring data, estimating statistical models, and performing statistical tests.

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c62885f5-417d-4179-834f-d68f8f2bdf39/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YM5HKIGP%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T231357Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEB4aCXVzLXdlc3QtMiJHMEUCIGkf%2BX2GsAeus%2Bid8vYdasfzLCZdlGlrzCATqpsPuqhUAiEAk66gib686N7dTKHK5deWo4ugffJ8l83ZO%2BrOds5mJLoq%2FwMINxAAGgw2Mzc0MjMxODM4MDUiDLZthjK0wjxlMfN0OSrcA8rT5mo48Jdm2d2iE7dK8eV1w5nkNJxrHQWY%2FNq7d0pUowBJavoo2kTwAPCW7702oR2mYYZ%2FE5swO7Crxz9vzdPUefteO37e4mQrvatNIfR%2BFjK1YtJC6VRmVrxnGeZ%2BcZQPK%2FdNHA5q2C3kCrlT4cXflEqu8IMlSLExjYO8qkUNym4j1sslExbZNIJjs8BWNx%2BsCZTU7g%2FGOghb8p9KEz3pPRZp9rkS2J6OnNhfZf6Zo8HP5figSxByab2RgH0eFN4wA6fCkaNIFvB8btcePOEB7jdppejSoDierxeuICZDJDskpj9Qf4uJoqL4LqzbZ1pDZO3%2BvJnphpgv8t2hrLwtz7c1AT2UAgRFsRm568UyFDNT0IzbZsZOh28eskLUCU8KLGS%2FU1tZ2jrorgWot3To5eVQH4IUa8RtydDw23wYtZAiJIXO57t6gMjP5Kep5akC8RSvjFDqqvbw2TNW2YTuE%2BADe7yOrTliwZaG58mPOtcDHD6arEtFdPCOvLKFyF8a65yfGlelQayXynVlfobXJzbp9JVIBgMq4x5s%2BJYZCfS%2FygoC5%2FnT2%2FbMJO5FXb4QnpnM3fa6dg3hF1CHmFWFH%2Bv88Mbr9%2F52qHPt%2FooJ6WfdCi%2FQdYabG%2FdBMLiUir0GOqUBWotuIXX4kcr8%2FtONAc4jcOHGkSSWpyDCgUa3MqCYh5gZrIyABedUnSPOFL1GXLdfCWV1yn06xZhqquK0GCgGBncZpn9GdHgZerYchc7rsSYm0l%2BFUzVcoDbfN5NL4TVItvlUHs9aUTsvCehFSSnNAfPAU%2B57NWo2zsMq4wATHuRtayzk3nSTWQ%2FHxOsYibSBvsvWjJAxyJ6jTwJZm%2FW5j2yTmhLj&X-Amz-Signature=8945a97ff690a46b247646ded1c2b806a59f7740498ed6cb889c34c1cdb34bf5&X-Amz-SignedHeaders=host&x-id=GetObject)
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
