

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

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/997ac361-58a8-4f04-bb0f-79fea4baa761/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YQDH37XX%2F20250223%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250223T004152Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCB5d6AGeb33JaFCp2ga2jMARi2ZKnf2PjTLc7fylzAHQIgXfkRUyKVKQGoQrBTpnOSnL944dMTX2eSgBJsPlTQJM8qiAQI%2BP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDCeAAiW8EO84JjdTyircA0qSIJ%2BDT8ODdc2R3EU9Xlm4nlZ3WxtYn7TEypfqxvTBqk4GbTrxs8t827BYr7TBiL686tpyNwOCkIAavVn7c%2FrmsyDee7E1ZknAu82BLheWmHb%2BirJMaNdWAXSOQnikELxIyTe%2Foektd0ZN3bkwoyKK3ix4PCcKzD%2BPkVOdWp7q8g5eKTXvWRJKBn5n4dnt5SWQjpg3xsJvExms6pvhWAX7YkvwDvL6jt2fvpakIXEeNWzBj8iFSPgNmtm%2BmstN4zLlQ%2F6GxXYY0LQHFPK8qafKe1H0UTLd5HnFUlXyfiGjjIPMq9%2FYzWQXRfXNdQ5zTICHzyyfdyzvjQaj4ClPTI5tcXx%2FqWshAa8Jdvu1NvGOdHFw534G%2FVI%2Ba6GmTKNlJxW5wy%2BUyIkm5ofsCVe73jX%2BpfDxYW6Ww7wVKUi9ug2EGtK80xHO2k%2F%2B0bBC%2FYEYLxfqYJ3ZqjAfHYau36qgI30URetVoqI%2F8%2FQFea90WDWJSZBjQGtvgl4ib6kUFUFksFvEdUxZgadE8ryXXEwsV5nxC2tqY8buAXFI6jFAkc0ogrs7pHqLLvBq4JJs1Ee3E9mSzzDIIKlKO0P%2Fqmt8u5rqRNHXcF4lAmy2EJzvuuQOdwb42mFKFJQejdeGMIKs6b0GOqUBZ9kNtldn6zSDdy%2BunZSLrfc2A%2BUCFrlJvWthisHzffknpNULSraB43lRXzA200qeBS1NkbzKR7u8mreC%2Fgc9ruSeXF92cVV%2FpunEg5QoDOrUURUFJiT2l2k7i9enW6mwkBqS%2BTtgBzfvngQDR%2FIWKDDtR6E9kYyhWsyJ4AxirYsjdpo0ZzOtcM04ACKN6AFvB9S%2FZpCQn%2BwT5wQC28fGzVZsF26T&X-Amz-Signature=769b4699f3a2cbbe7ba62e84a4921767e713b38261f250098a62915384312091&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Data Visualization Libraries
#### 1. **Matplotlib**
- **Description:** The most well-known library for data visualization.
- **Features:** Great for making highly customizable graphs and plots.
#### 2. **Seaborn**
- **Description:** A high-level visualization library based on Matplotlib.
- **Features:** Easy to generate various plots like heat maps, time series, and violin plots.

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/733d1e42-5a53-4fd8-90c1-3d85254369a6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466S26ZMA2R%2F20250223%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250223T004150Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGDa5NfyX%2F4AdywW%2BvH2qvZgvv02Tku69ScajGlSZSAaAiEAnG1KeGG9e05YkyuUYpCN94SS%2F3BVStf1qmzEm70fXG0qiAQI%2BP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPvlRkhTz0h7E343ICrcA9noh9nE1FX7W5cRbuXP5QsdWkkElTmA4%2BsaaD39p9AYjy%2BuKpGED%2FbzwwVR1IQtrEZ8o%2BYqzn3FwlkbdJk2%2FdGXO4nOx0zwNExb%2FfDByEOnPpuFLYwPEoWXh%2BCcTePY0wHgD28CAHv4ttwUiy3C37fbcByfw9gP9Wcdnwut6dPlZc11ZXCRPUdwVhsbYIIJoxH7X9U2DJ1mLNE7wamoibiAlSw651Q9CrRUT51H5Y6xjkjFyGune3yEERBdPSZfxuVbDS%2FpCagR99Q4quHRebY2dM3bZCydubQGWaiw8mDOvz%2FGukVBLFQ%2F2B6vvn6YtZDy1wue4LuLQNp%2BHlvhX8PW1U3NaAsvA4ff9u1mkIhNZNz7mDM9JkDEb8XHW%2FyqXi1b6LdOVjD6VmGBiTpVJntgQEp2d%2Fu7qSvjGowljqFkV8fubzz3R6vIO75TDn1ou6OnHIJtYYQQEMWG%2FaJgzVEc7okGuMiVuqbTWyhq3CVbRtJMQQHKvr981cwuOD%2BrUKuMv6gHxB9pq9ran3W%2F15NEkIRrJz0mI%2FqKvUBqdTRdZ9fCKt8F5Wyfx2JxYpoJAAua%2BF4ZP1ccbqLGVGqXY0xyRKApuSakaHWH8%2F27470e30ftvMn9ptUcsWBBMMer6b0GOqUBhMlove223%2FCg1%2FWi7JiDhfsZTqdZyVDIorFv1aImsMipGkt52F%2B3k75FAZnuMg7XQbAo5pNinr5aYQxVwz%2B5Nq99tHpSyZ3C2qJ%2FuAKiOPkdK5WuoLxXEY2v0IWQ4gZx4W6%2BU333Ktc8frsKwDCPmszoJSElV09AQTmg%2F0kNYh083P6f9mGybEyv%2BNHA898vsu1zLlwveopuNgN1BS7mFCzUBbUd&X-Amz-Signature=2b7354a1a622e21dc8868a2e34f287c6c96fcff79d0a7a767e3fcc7b2f0e6466&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Algorithmic Libraries
#### 1. **Scikit-learn**
- **Description:** Contains tools for statistical modeling, including regression, classification, clustering, etc.
- **Built on:** NumPy, SciPy, and Matplotlib.
#### 2. **Statsmodels**
- **Description:** A module for exploring data, estimating statistical models, and performing statistical tests.

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c62885f5-417d-4179-834f-d68f8f2bdf39/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466S26ZMA2R%2F20250223%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250223T004150Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEM%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGDa5NfyX%2F4AdywW%2BvH2qvZgvv02Tku69ScajGlSZSAaAiEAnG1KeGG9e05YkyuUYpCN94SS%2F3BVStf1qmzEm70fXG0qiAQI%2BP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPvlRkhTz0h7E343ICrcA9noh9nE1FX7W5cRbuXP5QsdWkkElTmA4%2BsaaD39p9AYjy%2BuKpGED%2FbzwwVR1IQtrEZ8o%2BYqzn3FwlkbdJk2%2FdGXO4nOx0zwNExb%2FfDByEOnPpuFLYwPEoWXh%2BCcTePY0wHgD28CAHv4ttwUiy3C37fbcByfw9gP9Wcdnwut6dPlZc11ZXCRPUdwVhsbYIIJoxH7X9U2DJ1mLNE7wamoibiAlSw651Q9CrRUT51H5Y6xjkjFyGune3yEERBdPSZfxuVbDS%2FpCagR99Q4quHRebY2dM3bZCydubQGWaiw8mDOvz%2FGukVBLFQ%2F2B6vvn6YtZDy1wue4LuLQNp%2BHlvhX8PW1U3NaAsvA4ff9u1mkIhNZNz7mDM9JkDEb8XHW%2FyqXi1b6LdOVjD6VmGBiTpVJntgQEp2d%2Fu7qSvjGowljqFkV8fubzz3R6vIO75TDn1ou6OnHIJtYYQQEMWG%2FaJgzVEc7okGuMiVuqbTWyhq3CVbRtJMQQHKvr981cwuOD%2BrUKuMv6gHxB9pq9ran3W%2F15NEkIRrJz0mI%2FqKvUBqdTRdZ9fCKt8F5Wyfx2JxYpoJAAua%2BF4ZP1ccbqLGVGqXY0xyRKApuSakaHWH8%2F27470e30ftvMn9ptUcsWBBMMer6b0GOqUBhMlove223%2FCg1%2FWi7JiDhfsZTqdZyVDIorFv1aImsMipGkt52F%2B3k75FAZnuMg7XQbAo5pNinr5aYQxVwz%2B5Nq99tHpSyZ3C2qJ%2FuAKiOPkdK5WuoLxXEY2v0IWQ4gZx4W6%2BU333Ktc8frsKwDCPmszoJSElV09AQTmg%2F0kNYh083P6f9mGybEyv%2BNHA898vsu1zLlwveopuNgN1BS7mFCzUBbUd&X-Amz-Signature=6b52020fe35ff6cb3e1d01b6695a15fc7bc549d3e67d2849e944523c1968cebc&X-Amz-SignedHeaders=host&x-id=GetObject)
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
