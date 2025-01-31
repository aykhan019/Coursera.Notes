

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

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/997ac361-58a8-4f04-bb0f-79fea4baa761/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VASL6MO7%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T041736Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCID%2BuyrELHMmEBG2%2Bu4nwjKILfGBmtTPjEOAjqkI0Pn3hAiEA3m0bFyk7vtje3QcD4uiNPvazTjcy3hh5eHa2gGTNw%2FIqiAQIs%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDBfqhvQiHm5vitaN%2FyrcAzVqcfyhFOomK61pKJC95TD7QFqDB3rxbF9JaRyBB%2FhGCOaTVfIDt5udmliX355x%2Ff9SWTUcAXmQY7Hd74rCvvhg9foAHZFJry%2FtpbdTYksxNoQOqE5VkhnZsH0FQDtOeuT2BDoU9WXw3Pl007d1AtdHPzE6J6A8pjdxIruI1pymYA1wDxcU2x%2BjArhJD35%2BWDVcBoOKO5%2B2fkz6Pfh8j%2Bld13bJhGX%2FUuqM8ZzLMCIDvv4SmwDV%2F2EbRUpqgmGF9migeS%2BKBDpOvHgcDS10mPO%2FM3t%2FVPVs%2BQ3972Zsl8bWLqwo7TODPBO6h5QghnbS8cK7n8CtHbmkjl799xDEgpRgHltGyq8mr2xSqVmYyri3z449EndLhzlixms9zFU2M7sJDnSjqkGXuh7%2BaFD1g6Gel8GIl%2FuartQhsF1WTff8vfKk45AVbBdAhQ3jDG7LWNGPlpoDYxUjB4Ffx96juJschi6VrrPB7aYQeSJdwvrPloZqN7kfuxsLXCDTkzDnN4UFpz1TtH2ZFT5eWp72fsQlkg7cDj7Ve2CH7LL%2FOuzHol5Y7yBAFnTGhAK%2BFM%2BQCY6NGvW63bLWDbzWRFgmXgtw699%2BUTJ%2Ftq6jkqecCcGxUVfaCWKlTu1aXFX8MKnQ8LwGOqUBvZlBvRHLmzgaJMhf3JiIA%2FeAm%2BBr3%2FDrIi6f5wzdnxep4n5YtgaXyPBTLyShTNQGuVs0RK%2FOGLJQMezFTeU1Em%2B1ZfOGkhcV0rS%2FC33nEavH%2Bwu84Vq4mjVUEdzir1NReCq9X8kbQxdzbs7LhZcDvkE9YgV31cpFNLU8EblS%2FPqULntOlas5qIDwz0SK68ihfGOEQeIV5F0AljQFY2rt6jc0dtXm&X-Amz-Signature=db57d1adcc00d8913d6a3bd0566082156c212a598d7db3975f58d448034c08d6&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Data Visualization Libraries
#### 1. **Matplotlib**
- **Description:** The most well-known library for data visualization.
- **Features:** Great for making highly customizable graphs and plots.
#### 2. **Seaborn**
- **Description:** A high-level visualization library based on Matplotlib.
- **Features:** Easy to generate various plots like heat maps, time series, and violin plots.

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/733d1e42-5a53-4fd8-90c1-3d85254369a6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667LSUCXX4%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T041735Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFZs7tIHh%2BIUhvdEBLkivYmEFoG6zOBvAP6y6GEqfIliAiARDiEwliAzGhOVVG8v%2BHu%2BzmUAolUjarKH%2Bj6xSUKRUSqIBAiz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMjCeErHE8et6bx5adKtwD3P9iAVtw6AP1KOXZ5liy0%2BCzR2EUeRwMWEp4t08CK27tEl4nKS%2BjPO476yRISpDIb88E642RCIyKO7IY6XWqlVQr3KpcLEbsq2tBj4%2Bla32LIWeLA6uuZUx5byVr2253URQrxTaeHiLEyVRKwxQv7cX%2Bc%2FeVGrz3OsAMsFnh0PKM%2BVxW2gArJ7gkR6LiyPsBOUXeo0dURMWZC%2BZijRaajs%2FxPpTLaKdD09qC8Z4l0dnxlPoxPP0DOdpwiIa5khtUgy1teGfaj4m6tMrFlS534SrQf7fJgQdWrGlMTq1v5JHS1jfwg%2Fd0%2FbcXY%2FjVhqN94%2FO%2BHD%2FRtDLC5hLSqxwxqbxatSzcyam44KRDpYcaTNfCB3pmHwWxgXBF7kf0pWnqe4oJJ80Y5iKLJYkIbHLzYamIFLDTOYkja0mi2De2pJU7sV8Is4jBSnRIHr6FGLl%2BYDIWXP%2Ft9rTv1FUTU63Tt6Y7nLMLl4pEtZHhUIzZixwJFn3Iv4FzCHwSMZHYkyTEmu76dyeYJxJVpmcZ5xeSKtFSPOJNbG%2Fl6cS2g9v0b0R76w%2BRlwpmC33MgT0AHLsTyEEHnrIZHmwk5kUu5DpZRSPAE5SUCA4cDMNV1Vj9vyhV2UF82ElD8P70IGow%2FdDwvAY6pgE06pq3lH6pmGATrkSuEXQExtHifIL7JDi%2FysDTf0KyM943r%2BRaHeXQ8ca8%2FSHANvVr52Ic%2F2YetJ89KdzlbPdJHb8CmTHMUtm1fAHCAYeXzDVbqnb5NLmXqwwzXvfW0mR3FgJ2fbygLYx0Ku%2B7J1VxQuYgFxgaJ8Gy8659o6BIDHC8ot%2FgEq0SXBfCBLmsPFVRlpLeF5eAJVGZy6z4bE%2BSaiY901kU&X-Amz-Signature=ec784d5d119dca3bfdf44f0d37ff7dc1067965abc54fd620577d8420d0c55808&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Algorithmic Libraries
#### 1. **Scikit-learn**
- **Description:** Contains tools for statistical modeling, including regression, classification, clustering, etc.
- **Built on:** NumPy, SciPy, and Matplotlib.
#### 2. **Statsmodels**
- **Description:** A module for exploring data, estimating statistical models, and performing statistical tests.

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c62885f5-417d-4179-834f-d68f8f2bdf39/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667LSUCXX4%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T041735Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFZs7tIHh%2BIUhvdEBLkivYmEFoG6zOBvAP6y6GEqfIliAiARDiEwliAzGhOVVG8v%2BHu%2BzmUAolUjarKH%2Bj6xSUKRUSqIBAiz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMjCeErHE8et6bx5adKtwD3P9iAVtw6AP1KOXZ5liy0%2BCzR2EUeRwMWEp4t08CK27tEl4nKS%2BjPO476yRISpDIb88E642RCIyKO7IY6XWqlVQr3KpcLEbsq2tBj4%2Bla32LIWeLA6uuZUx5byVr2253URQrxTaeHiLEyVRKwxQv7cX%2Bc%2FeVGrz3OsAMsFnh0PKM%2BVxW2gArJ7gkR6LiyPsBOUXeo0dURMWZC%2BZijRaajs%2FxPpTLaKdD09qC8Z4l0dnxlPoxPP0DOdpwiIa5khtUgy1teGfaj4m6tMrFlS534SrQf7fJgQdWrGlMTq1v5JHS1jfwg%2Fd0%2FbcXY%2FjVhqN94%2FO%2BHD%2FRtDLC5hLSqxwxqbxatSzcyam44KRDpYcaTNfCB3pmHwWxgXBF7kf0pWnqe4oJJ80Y5iKLJYkIbHLzYamIFLDTOYkja0mi2De2pJU7sV8Is4jBSnRIHr6FGLl%2BYDIWXP%2Ft9rTv1FUTU63Tt6Y7nLMLl4pEtZHhUIzZixwJFn3Iv4FzCHwSMZHYkyTEmu76dyeYJxJVpmcZ5xeSKtFSPOJNbG%2Fl6cS2g9v0b0R76w%2BRlwpmC33MgT0AHLsTyEEHnrIZHmwk5kUu5DpZRSPAE5SUCA4cDMNV1Vj9vyhV2UF82ElD8P70IGow%2FdDwvAY6pgE06pq3lH6pmGATrkSuEXQExtHifIL7JDi%2FysDTf0KyM943r%2BRaHeXQ8ca8%2FSHANvVr52Ic%2F2YetJ89KdzlbPdJHb8CmTHMUtm1fAHCAYeXzDVbqnb5NLmXqwwzXvfW0mR3FgJ2fbygLYx0Ku%2B7J1VxQuYgFxgaJ8Gy8659o6BIDHC8ot%2FgEq0SXBfCBLmsPFVRlpLeF5eAJVGZy6z4bE%2BSaiY901kU&X-Amz-Signature=2147b875ddda78d34e99a29508bb9991d7092975ca32c55a3e5bed44996bfbad&X-Amz-SignedHeaders=host&x-id=GetObject)
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
