

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

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/997ac361-58a8-4f04-bb0f-79fea4baa761/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466742BJUUL%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T111304Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIBzngjWqunnfz6lm4QHQdTo4SLMHaE92l%2F86bCze0gmuAiEA%2BiVMq%2FiMmnKxCX7wzrg6CwHkdALcbIgzJdkOTuPXsGkqiAQIpP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDE4XGTfgvVpB4TNNUyrcA%2BB6GKAPFbV1YYJ89qrxSU0hEiA3yik9oK5sclbs%2BwnaaHWK94nRM%2BA44DspDTkph7vYC1JcH2sm21vHbyEFelJAX1yb6pEvv%2FuG8tTr0jFqEbIHqZwrqx5q2SdY8jy2AO1akvJmHLNIbp9hwSTPWaTmGSVa%2BPerth4YAL23bZdid%2BO6IQT6T3eXdRjvbiQYXYmzWSfHZ%2FYGePdP38bGje7tozIf4JcTu6LEilD8bCUtEKjkq%2FcPpw1UBzJvBUTBQofgFU59bHGgrmsfG1g9Q3keyanWremHjo3DnNePZhQNQzgKrs9yRtmiaEhXuK0zq55qZ59XYl4uCk00Me5yzFwNF%2F3oBBLfuXGWLYIc13hqaBcwvREiGBvdVGmZEnRg3lS7i%2F5m55R5vd5c4NwJPmC3EHT9I1M0EC%2FFD8Ea7Em2CgFPUBwwCl9z1xxllUjIx9CdBdneUl3TsmcbjPSs9HZG1PgOGhSb0uz1uPyNY7BdB2NcsgUhU02bODbGznc%2FdntxnCNLS83PKe%2BfXZTADC36oNO4%2F6dtyyUZ3%2FOEWRW2458wrkMHCFn9OhqaQjnoWTnbsiB7QJBfqnb1V94otVuxAE9n2AVDZWNw0WRxijDP0Bdq3NSiVevOwiqeMJao7bwGOqUBRTN9Y3ZMYh8h%2F4y3pz2n0dx06R3gHoUOY8KBQiue2LUoGXk018Q5E0WUOjHa9J4g1VmiqI3yVWemVSOn0gDXmSv3zjfK0NpjLyd9wiqec5KWUaVodVU71NsLModGdx1P2xS0bM9PGYf%2FGS6cbab5kL%2Bhc4rFktHk3fWN5ci0NjJZMbhFzOO0o%2B2Rpu6Nvl9D%2B7YR7YwsgZtpLOWLFUx62%2FYR4riQ&X-Amz-Signature=4ff2234f16b3b755130f0aa4d2d7f481195a56a99ffa8b902b8bddb00cf2a2b4&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Data Visualization Libraries
#### 1. **Matplotlib**
- **Description:** The most well-known library for data visualization.
- **Features:** Great for making highly customizable graphs and plots.
#### 2. **Seaborn**
- **Description:** A high-level visualization library based on Matplotlib.
- **Features:** Easy to generate various plots like heat maps, time series, and violin plots.

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/733d1e42-5a53-4fd8-90c1-3d85254369a6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XAQW63SZ%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T111303Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHsV27S4DThgTmme26RsVhHhJyTztfH9CTYk4XrMU%2F6eAiBpf3ZEfhIhw%2BUUTeBwl9%2FyTnF90b4Noq4UJutPUR%2FB9yqIBAik%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMXGwI03bM92pI6I98KtwDUkSBei7ly1hPimdC1Hpf5WRkcpXdBky6AKjan4iKcganI3lplPlLX%2F6am0%2FIOoV0Rrb0m5G7WFOaVKXHIj2ItGlXxX43W1%2FTleL8Yucm9RnMlaZMJsmVwcKSwZOw%2FoTjzzULq5x3fJeICuzejytAMuUjBvBDghymj6lmn5bv5JPUpUq%2Bub%2BGKB6gvHaYsOq2CgMkI8DBUk4JNqEh40NR%2Byyr4CoIwva3gIFjJu3gnLeSweeg5T2b9ugSrhTeQi%2FiBVjKb4MT%2Be8YsbptqGIU07dtWQK3%2F3YcXFx%2FWlnO502zlP%2BnHPELdmq1vGKWvfbh9mEKu4fBGW9egEzxQmdIf9qNdSpEyoG9sqZhbsCQZeduYTmpvH2Lvfaj%2BycOuhtNjHtFoSL6JpvFHx%2FfTs6qOFqno4UPmRaBEBmdPJGvp7oGWK4ow5cjWZMuQn88sY8XM1ncuxRj1als5wvpnbGIoAt%2BnZeK49K80loOq3bwomgNU7krjQtd9EdEMISP2AcQRMOz%2F0I0QCd74yby2lsQTEifyLJnptq4qyJbCstrBIvQAXiSCytqwUCBke8nwC6uWFXqK3QqLnF1BnEgAF8YmUZWMfPBYvn2iYoGPzcIrVZmgj617s0Zjv71XW8w66jtvAY6pgGe3%2BQkW6MAXZbpScV6wCzMl1TKlLc1LOF6mnl7Bltj%2BUN05Kh%2B6fCSBBZM9dLdSrHUCnozWqJkZQNwzwhpE7XiX3Qjz7ZFO4Mmd7mdy%2BnjWW2vko4UI4k%2BZjtwH6OfIeoq8zzx5nUWJS1DCD4BoVYLFeGXDVImsCz7P69by%2BlobpdbNpDORCyAX83EtwVVTgBGKNmoc7OOZRJnKU8pnxEobWtFx9r3&X-Amz-Signature=fa1441166b1eb9fe7b10d969c1dc09b25338f38a56b9990220a160105aa4e2e1&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Algorithmic Libraries
#### 1. **Scikit-learn**
- **Description:** Contains tools for statistical modeling, including regression, classification, clustering, etc.
- **Built on:** NumPy, SciPy, and Matplotlib.
#### 2. **Statsmodels**
- **Description:** A module for exploring data, estimating statistical models, and performing statistical tests.

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c62885f5-417d-4179-834f-d68f8f2bdf39/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XAQW63SZ%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T111303Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHsV27S4DThgTmme26RsVhHhJyTztfH9CTYk4XrMU%2F6eAiBpf3ZEfhIhw%2BUUTeBwl9%2FyTnF90b4Noq4UJutPUR%2FB9yqIBAik%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMXGwI03bM92pI6I98KtwDUkSBei7ly1hPimdC1Hpf5WRkcpXdBky6AKjan4iKcganI3lplPlLX%2F6am0%2FIOoV0Rrb0m5G7WFOaVKXHIj2ItGlXxX43W1%2FTleL8Yucm9RnMlaZMJsmVwcKSwZOw%2FoTjzzULq5x3fJeICuzejytAMuUjBvBDghymj6lmn5bv5JPUpUq%2Bub%2BGKB6gvHaYsOq2CgMkI8DBUk4JNqEh40NR%2Byyr4CoIwva3gIFjJu3gnLeSweeg5T2b9ugSrhTeQi%2FiBVjKb4MT%2Be8YsbptqGIU07dtWQK3%2F3YcXFx%2FWlnO502zlP%2BnHPELdmq1vGKWvfbh9mEKu4fBGW9egEzxQmdIf9qNdSpEyoG9sqZhbsCQZeduYTmpvH2Lvfaj%2BycOuhtNjHtFoSL6JpvFHx%2FfTs6qOFqno4UPmRaBEBmdPJGvp7oGWK4ow5cjWZMuQn88sY8XM1ncuxRj1als5wvpnbGIoAt%2BnZeK49K80loOq3bwomgNU7krjQtd9EdEMISP2AcQRMOz%2F0I0QCd74yby2lsQTEifyLJnptq4qyJbCstrBIvQAXiSCytqwUCBke8nwC6uWFXqK3QqLnF1BnEgAF8YmUZWMfPBYvn2iYoGPzcIrVZmgj617s0Zjv71XW8w66jtvAY6pgGe3%2BQkW6MAXZbpScV6wCzMl1TKlLc1LOF6mnl7Bltj%2BUN05Kh%2B6fCSBBZM9dLdSrHUCnozWqJkZQNwzwhpE7XiX3Qjz7ZFO4Mmd7mdy%2BnjWW2vko4UI4k%2BZjtwH6OfIeoq8zzx5nUWJS1DCD4BoVYLFeGXDVImsCz7P69by%2BlobpdbNpDORCyAX83EtwVVTgBGKNmoc7OOZRJnKU8pnxEobWtFx9r3&X-Amz-Signature=6bb9fcac49250f425283e85c69f018b738b3426ecbdce80ac081d12c757e3886&X-Amz-SignedHeaders=host&x-id=GetObject)
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
