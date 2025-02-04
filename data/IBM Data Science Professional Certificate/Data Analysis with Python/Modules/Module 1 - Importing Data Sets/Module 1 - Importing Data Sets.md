

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

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/997ac361-58a8-4f04-bb0f-79fea4baa761/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RZYCE276%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T221352Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEB4aCXVzLXdlc3QtMiJGMEQCIDSCVGMRKVYOduFx%2FFFzXFKKgCvQgfpbUvtMQHJrDAgZAiBWsLXKO1mBtLOTlLRMdckKTm0qB%2Fmd8OCPTT%2FGQZvWCir%2FAwg3EAAaDDYzNzQyMzE4MzgwNSIMt7IiccMZu%2FuMcDckKtwDQvuP3uJqX3ABqTBZl4rqbNwU88KKmpTjf3ZfpUcHAwYQOpDjAuo9eA6ChbL%2Fm%2Bff%2FmIgjC4pP0mULn7PwCDs18U5Mr5eqzsMmCkApnHucV%2FfawhFq2jltAxgGTfoegacbmHSUT5KLU5JQCXDj12ahOyhDhbvSKswwbX2YaYOQpY4ni8UtqXguWpC81eu7NKetCbpflkPbYJ%2FDDRIlO7X5mqTZUuuVavQioOxcozN0VL%2FzmpzoXPrP%2FFIUUPno5LKt6BqIoq9Zl7B3pqhnST%2B0UTZJHDyIq0gNW2erE6iT45aCkL%2BPI3H5eUB0jpZXXAI7mzYbA%2FxXak33IK8ScnjNB%2FKb80D33be8Vzv%2F8vknYJsawnVH9uVBfrfMsPxTlECmZt%2FJAPBVpC2K9NdNTeuO4%2BNmeeld6wYU0pxiYjPX5HTzHTyaJ2vPBY78cliMN6iF3VNdHU2llkQoJPXa%2Brb%2Fa3gTnjC0KrSbAUBctTTA%2BUf2S4Y7QYGhF%2FbsIOnYyPAVA3Mcj6oFGIp7DjJqnH0JLSNfNUVNVy%2BQJqlUPnM6wNCYAJ%2F%2F2KwK37y3U0n59nUfaDiLcv0B5d278Yi8VoZrSMms%2BoomljsI2R2np6AXdPLpF6IR53vZT8Zw%2B4wk5SKvQY6pgF3SYcikDFLIuzriAWR0fO0pZGvQFxJszd%2BvDFcttK62VU8%2FQ2CiHgcgjw%2F8z9Ff4cYgpda4dLFumjEjV8E04bzevah6ukSpG5fAghpQdQTw12wc%2BNLiKFf4PMpyAyfXRz0PLnayGEdceW901dbrTPp71KfECsNOw3UYCjMtIGo1VQJ3%2BZS6w4DitvhkgB0CEprkIp1ejSjMFnL25wdoYY48wJe5HDO&X-Amz-Signature=c80e410024eb9188ffe588a5299878d5b14039a3480737dc962f752213596586&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Data Visualization Libraries
#### 1. **Matplotlib**
- **Description:** The most well-known library for data visualization.
- **Features:** Great for making highly customizable graphs and plots.
#### 2. **Seaborn**
- **Description:** A high-level visualization library based on Matplotlib.
- **Features:** Easy to generate various plots like heat maps, time series, and violin plots.

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/733d1e42-5a53-4fd8-90c1-3d85254369a6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZK2EMV6W%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T221351Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEB4aCXVzLXdlc3QtMiJIMEYCIQD0mPsL4Fw9avVPHvFq4PLu%2BBdpnNoo%2FlhcgeeBN9rPjQIhAJjAF8NH82tHIi1FtLoFJ%2FYXMbrBSw55R%2FoupC0Pcm9pKv8DCDcQABoMNjM3NDIzMTgzODA1IgzYeeRt609vHN42TQIq3AMB125iY1BldGQWi7akpY%2Bbpkylpnn92We8IXRGs%2Bsp2PT8EYmMCzyUnd8Y8OrM0Mh8QmfZuMIm501%2BqOVcHLnhug0MWYGqOjr9JaBkhUdWD5nPEhBQFGs5Owq2ZPqvnzjvW66pwH3Ki%2FlI%2BWulMYW%2FbxE61FHx%2FkPieOLXco8C2B3M3VHDFHCFpV%2BgrcZ3n9hiIO9C87GR83IIJYDD%2FwUw2P3vUdd4OsQzVF9KIS%2B8DJQFWnMY9yeyyQ2lgoadDzG69KQbCARUbhvO5E%2BymY8IDssnQFIPMJe9roUo6FFzSR5Mud2LiLgopfq%2BI9O2OwEGufStG25TyDVQRkT8GOPyNfy6r2%2BaI8KNunPIzI5rntxVwaFiDyxQIkWfhE8gFn1caaNaGTmBTj8T6m9OWHo12Ae1EN%2BJQOiGfhCYKmNRrpzHaMifx0zlqq6Bj%2BT%2FLnfmFQrSO7%2FbjgxHOhzv5%2FZqL1d26kXCVpqNCt4GSgi18mKfgo9aJJy3DWO%2B7TnWkX%2B5ryLTgh8A3acat172AcuopDoJx6gEJqv6y5iI5t9g%2F4WndWgY3sYdt9yUDtLffyh0OOmFzWgcXzJZ7hoZy92HnQchKlGFQfua%2Bm%2F%2F3b4uwbfiflb4MVK%2B7Pj1VjDflIq9BjqkAbezpQwnV3xbdX3HHPYrxFr4KIr3OYmoB0gL4s6KBfQmBxV%2B%2Bd9McUdNhTYxuYvwR5wQo73CVg4YISQxDWdmOZHgmXJJOfOmKiVBr0e9wITpz8dx%2ByhyIopkx%2BS3S5M4%2BRkzWJxvn11xGwpG0XCVvnYGS9AVsPfNr7g8%2F19x0I5FkfUYpFGQ%2FluujQTCfSqW5k6y7J4mUOiY83o7yNpSZ00E0FuF&X-Amz-Signature=5c3f1ead4c384e2527c1d482bf9ba16c2b62c2d4f63892602cf6b315de7147d9&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Algorithmic Libraries
#### 1. **Scikit-learn**
- **Description:** Contains tools for statistical modeling, including regression, classification, clustering, etc.
- **Built on:** NumPy, SciPy, and Matplotlib.
#### 2. **Statsmodels**
- **Description:** A module for exploring data, estimating statistical models, and performing statistical tests.

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c62885f5-417d-4179-834f-d68f8f2bdf39/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZK2EMV6W%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T221351Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEB4aCXVzLXdlc3QtMiJIMEYCIQD0mPsL4Fw9avVPHvFq4PLu%2BBdpnNoo%2FlhcgeeBN9rPjQIhAJjAF8NH82tHIi1FtLoFJ%2FYXMbrBSw55R%2FoupC0Pcm9pKv8DCDcQABoMNjM3NDIzMTgzODA1IgzYeeRt609vHN42TQIq3AMB125iY1BldGQWi7akpY%2Bbpkylpnn92We8IXRGs%2Bsp2PT8EYmMCzyUnd8Y8OrM0Mh8QmfZuMIm501%2BqOVcHLnhug0MWYGqOjr9JaBkhUdWD5nPEhBQFGs5Owq2ZPqvnzjvW66pwH3Ki%2FlI%2BWulMYW%2FbxE61FHx%2FkPieOLXco8C2B3M3VHDFHCFpV%2BgrcZ3n9hiIO9C87GR83IIJYDD%2FwUw2P3vUdd4OsQzVF9KIS%2B8DJQFWnMY9yeyyQ2lgoadDzG69KQbCARUbhvO5E%2BymY8IDssnQFIPMJe9roUo6FFzSR5Mud2LiLgopfq%2BI9O2OwEGufStG25TyDVQRkT8GOPyNfy6r2%2BaI8KNunPIzI5rntxVwaFiDyxQIkWfhE8gFn1caaNaGTmBTj8T6m9OWHo12Ae1EN%2BJQOiGfhCYKmNRrpzHaMifx0zlqq6Bj%2BT%2FLnfmFQrSO7%2FbjgxHOhzv5%2FZqL1d26kXCVpqNCt4GSgi18mKfgo9aJJy3DWO%2B7TnWkX%2B5ryLTgh8A3acat172AcuopDoJx6gEJqv6y5iI5t9g%2F4WndWgY3sYdt9yUDtLffyh0OOmFzWgcXzJZ7hoZy92HnQchKlGFQfua%2Bm%2F%2F3b4uwbfiflb4MVK%2B7Pj1VjDflIq9BjqkAbezpQwnV3xbdX3HHPYrxFr4KIr3OYmoB0gL4s6KBfQmBxV%2B%2Bd9McUdNhTYxuYvwR5wQo73CVg4YISQxDWdmOZHgmXJJOfOmKiVBr0e9wITpz8dx%2ByhyIopkx%2BS3S5M4%2BRkzWJxvn11xGwpG0XCVvnYGS9AVsPfNr7g8%2F19x0I5FkfUYpFGQ%2FluujQTCfSqW5k6y7J4mUOiY83o7yNpSZ00E0FuF&X-Amz-Signature=9da459a70acf9ffb17f998e5f1d66686618c37d6709cba54f688da5bbba8d5b6&X-Amz-SignedHeaders=host&x-id=GetObject)
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
