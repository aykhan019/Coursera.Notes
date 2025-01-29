

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

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/997ac361-58a8-4f04-bb0f-79fea4baa761/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667DERB3RM%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T151511Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC53gaiwhTmjOVDcqlIZvgaGMj7H1bExJbePg2bR7MwQwIhAJJp9ix4CZMpJEKaoNgdhKUHK8zj0LVQaI2Y1%2FyIb0e5KogECJD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyWO%2BA3L%2Bvy9RVdcTEq3AP%2BFpCQQM%2BAZcSbXIYVvdxgGQMumzkpRyA13HhT1KveS22QO0UIMkLknOMaQhnteke4nrRa%2FB%2BoUlspU4nppftpdBiDZOt%2Fm1NkGdNHvIoSxTw2eN0yABGhyYEXJG0EnhcNPHyxJ9%2B5cJiCUm2%2FJnlcN0vhm5iOrmPm9Fqg6yeMjUmgumdzwEl1E7e0%2FfEOBFeDAanbOssTq%2F0KK0UDNJmHVNFAjkq0c3rzGy5HsccO%2BmHf7E7cgSSPD563kstW7Rcw7lKrWQiPyYfhSW%2B5WbCTD4BaHNLsHO2ZvsQNoohxKYaLUF3Qg9n333OU%2FN4B8g4%2FRMilfqDHONPzeWdeWvnK0W8V%2Fl0qg045uMQhsroQ2keN7HN94ELnlLnKcAq3ZsNQt5ONHHvEuiG%2FLJBQsQvGR%2BcodJ4H7CWU%2BkPzgXZM4Nz1sOPpfOsl9pEY8eMJqhh6K4hJgDf9rIeXO%2FWAdCFCnxl4wawHnDlLWi00EwDhdPZFs2Yh4TCA8eo3Rums7WCjrB%2Fj6qNOt%2BGbPWU1d8uSHUQnaWlGYqwmCVSth3Xv2RkRt%2BvUp2%2FTlddQqtd5mvub6iQx1bZGCdicAzZ4whwcz9HNWtFJmXJKQ0W7zKID97y%2FSzRHTJaE0wVR5jD3g%2Bm8BjqkAUsCFY0LSSLowQnd1NxWn6w20hNDFgK%2FQl2sCyAo95Zmu9L2q7MLIeYHrHsKr3OhneVFerCuDnmXw6lMB5%2BhNIV9BeqYtFnP7%2BHzK7IO7qveEPjCIOmIoCd4wzvSDx2zWNaWdR3Oo8Iez%2BahwMGEyIBRgEJLLQsoIuG8VHOewABZgbCXEF4K9moT747EtibTdKiOgtE7VjYTOyqrZ8V0XYDNj5dQ&X-Amz-Signature=012833a395c19add10d4a813e5358db8c66a15a8c5df4a7acea7563f2ef431d8&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Data Visualization Libraries
#### 1. **Matplotlib**
- **Description:** The most well-known library for data visualization.
- **Features:** Great for making highly customizable graphs and plots.
#### 2. **Seaborn**
- **Description:** A high-level visualization library based on Matplotlib.
- **Features:** Easy to generate various plots like heat maps, time series, and violin plots.

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/733d1e42-5a53-4fd8-90c1-3d85254369a6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46675KBRZIO%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T151510Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDABaa2J1AvdI2wkwvSRhoqgrc9oRgnZ2VuLcmtVzYE9wIhAIs%2FpSodM2zkdYNm0rcYAduyCLiNV9gIm0%2FGMwC6m3BwKogECJD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igx9hNfKZ4lTuL5KTmcq3APnbeidmk3HMGK5waZ0qJCz30Py%2BARJuzz50ZFjRYGlzmBH1GnZ%2FiSfrO5rAu1aUZOIgXWwd1ERXtBL8sAfsjp3iSo7wDK04NGPStQ4IhBq27Pl7BDjfXTphYW23ccKlYtJuUuQ2I%2BQI8UDsxp9ftwJL6jnipzb%2Fv6Hkj1sbrMVvywpEMSu3oKlydvBzpO0A%2FHWqeG%2FqLfzGCj%2B6QYsFFQRVRAyuaFf%2BsscqfFkmhNL7%2B2ZkhIW09wFC%2B6MLzRthaDVW4pJX6tXrDzP2IuMMds5mDdOJWP8wIxdYEobgcQNXzPBKRvc%2Buu%2BXcLrYJK0Sy%2Ff%2FP5XW2JTyX62aIL%2F1EEQX5m3MzSyI0fyD4ED5uTjpIBbFzuC0tP3NlKLjgJ7MLkdf2l3KiqiNC80AmAnUWmQph6sR1XKLBSuqXzeX%2FOtC9bTbizL9qgvEebu7OhuafXMxXZDxZ4jaAnYkW1QnyJM5A%2BNF6l0Rry7843%2BXIeaO1dbiK8ACa4BXAO28AvhoE9jGCrv6zjWGM0J6saiGe3fcUSUl9r4NPINcaCxNR0Nw2s7zMe%2BldZmjdjqm6nItK7vWzbwZh%2BDcOiasq9W8XasvREpVzCHwwlhmXEhBYnKFnnkrC2c7tW5z5yFXTC4g%2Bm8BjqkAb%2Fekf7lL44YsB0rdNI%2F9x4iX2OvCWvcb4mDwQzkuammLfMmTAWz1uYNhE6gbC7tL%2FdENxnufK%2F%2Bq%2Frwqq7oqeM6V4Ugjt1EN%2Bl9gDXa0M4hybwKvhhcWTSTAydY7swbM24NuK36tCsAV%2BYkzpYb5mvaADEaphNwEx0A4721C3Z216MTSZaX6FhODmc2XaxfqqTz%2BUOS7CVPkQ1t42X4nXEtAPrg&X-Amz-Signature=400bb20928bc61c85a581dec27e95a7f8bdb37ecc72b92d00af616875aec4376&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Algorithmic Libraries
#### 1. **Scikit-learn**
- **Description:** Contains tools for statistical modeling, including regression, classification, clustering, etc.
- **Built on:** NumPy, SciPy, and Matplotlib.
#### 2. **Statsmodels**
- **Description:** A module for exploring data, estimating statistical models, and performing statistical tests.

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c62885f5-417d-4179-834f-d68f8f2bdf39/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46675KBRZIO%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T151510Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDABaa2J1AvdI2wkwvSRhoqgrc9oRgnZ2VuLcmtVzYE9wIhAIs%2FpSodM2zkdYNm0rcYAduyCLiNV9gIm0%2FGMwC6m3BwKogECJD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igx9hNfKZ4lTuL5KTmcq3APnbeidmk3HMGK5waZ0qJCz30Py%2BARJuzz50ZFjRYGlzmBH1GnZ%2FiSfrO5rAu1aUZOIgXWwd1ERXtBL8sAfsjp3iSo7wDK04NGPStQ4IhBq27Pl7BDjfXTphYW23ccKlYtJuUuQ2I%2BQI8UDsxp9ftwJL6jnipzb%2Fv6Hkj1sbrMVvywpEMSu3oKlydvBzpO0A%2FHWqeG%2FqLfzGCj%2B6QYsFFQRVRAyuaFf%2BsscqfFkmhNL7%2B2ZkhIW09wFC%2B6MLzRthaDVW4pJX6tXrDzP2IuMMds5mDdOJWP8wIxdYEobgcQNXzPBKRvc%2Buu%2BXcLrYJK0Sy%2Ff%2FP5XW2JTyX62aIL%2F1EEQX5m3MzSyI0fyD4ED5uTjpIBbFzuC0tP3NlKLjgJ7MLkdf2l3KiqiNC80AmAnUWmQph6sR1XKLBSuqXzeX%2FOtC9bTbizL9qgvEebu7OhuafXMxXZDxZ4jaAnYkW1QnyJM5A%2BNF6l0Rry7843%2BXIeaO1dbiK8ACa4BXAO28AvhoE9jGCrv6zjWGM0J6saiGe3fcUSUl9r4NPINcaCxNR0Nw2s7zMe%2BldZmjdjqm6nItK7vWzbwZh%2BDcOiasq9W8XasvREpVzCHwwlhmXEhBYnKFnnkrC2c7tW5z5yFXTC4g%2Bm8BjqkAb%2Fekf7lL44YsB0rdNI%2F9x4iX2OvCWvcb4mDwQzkuammLfMmTAWz1uYNhE6gbC7tL%2FdENxnufK%2F%2Bq%2Frwqq7oqeM6V4Ugjt1EN%2Bl9gDXa0M4hybwKvhhcWTSTAydY7swbM24NuK36tCsAV%2BYkzpYb5mvaADEaphNwEx0A4721C3Z216MTSZaX6FhODmc2XaxfqqTz%2BUOS7CVPkQ1t42X4nXEtAPrg&X-Amz-Signature=503a13acd3e150bad1343a3d43b745aa2a243c29049d8559ecf8be2f89b76277&X-Amz-SignedHeaders=host&x-id=GetObject)
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
