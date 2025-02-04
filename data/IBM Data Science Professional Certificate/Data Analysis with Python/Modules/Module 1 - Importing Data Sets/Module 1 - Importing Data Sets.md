

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

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/997ac361-58a8-4f04-bb0f-79fea4baa761/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663SX5UQMU%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T051418Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA0aCXVzLXdlc3QtMiJGMEQCID%2BgPZ%2Bse%2BsclO9uMgCKoJyCuaQBMYbb%2FuMIkthmo%2FWIAiBtGzKLFd76nIvUQBuzH01neUF7XEe4EIzMKDXoelwqNyr%2FAwgmEAAaDDYzNzQyMzE4MzgwNSIMZ5%2BDLi0Ur%2F9Ya7fHKtwD40BhoJ%2FTG8O3oNThLDygWvkqThxNQ%2BKWAQOjAEm1qY9ImOXju5MWDVpbS%2BIt2jMymMZJc2Uxz8FI0HXqSV5A3A%2F7ArXFHm43UEtFjChtaa0cOKfxiUX6V1QpuzaQ3K9L4EQaogs6fy70mRZdrlzwq06YmvXKL412%2FStOrkSa4tayFHnwATMvrBGdH2f2NnYUPxlI1XCyBN%2BXH%2BMUJCqnB0hM6DpUJ68d%2BZN%2BwK44mKkukzrzq4pNclJhXUdwaEGdS8s%2BBcF%2FIX85pF6JxUrr%2Bc3rxFb%2BEVV0Cgj66a4y8sHOcRr6O%2Ba01TdFNfC%2F0AMOyiFwMe8W40qdXFSjFfrIJ3fZ9MJitnLhGXuQ%2FvdJBGzc79g1FyOq4Q0RmS4BEajfR9pDdyZUKto5LQlRg4wSqA5jSjjzUc4%2BAoi5mhITHgN5%2Btm4PAl%2FWbG4YBYpIL9W3dRmuCeMWG7wIrp8zVUEVdS6kxc5s2tF3LPBmOSt06Nt%2Bcn9Xhx8pT9EM9CCMJ10D3RU4pG72rM9pLYwVjWk6iznZKQH7H0tku0YYVcm7G5rvJad0D8jNs32pdZ9uUK%2FkBgb8KOwvWOZvgFgcxm5x%2B4IW2SX1uafE6x2I0RLhX7Pbb4V2fRN8hXGpw4w276GvQY6pgG%2FxKo8vF8XzLhtyEdVWj5WkRfMCWs%2FsrQevNB1A%2FZt%2FY2dDVP2%2F2%2BQ7Bn8Kqsp8rZb%2BkAMH0FgH8hr1ZrL%2B3Ch5lrSZ72JGIUlt3I2zjkrw4tbOWVsCi1V1oUki6MgaG9nwS6R15TVUz8tiBXFqFP8ni6VrStM6c9S8yXN49waAADTZlq0rDB9dmwodT5rZe1n4gH5gs25%2FXuyNldkeHCd%2B5bgMF67&X-Amz-Signature=c07f130c20459edd6abf3daf14c727edbc80b5785e5725c18049699037f00e09&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Data Visualization Libraries
#### 1. **Matplotlib**
- **Description:** The most well-known library for data visualization.
- **Features:** Great for making highly customizable graphs and plots.
#### 2. **Seaborn**
- **Description:** A high-level visualization library based on Matplotlib.
- **Features:** Easy to generate various plots like heat maps, time series, and violin plots.

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/733d1e42-5a53-4fd8-90c1-3d85254369a6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RKRNS3UQ%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T051417Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA0aCXVzLXdlc3QtMiJIMEYCIQCjzhAMBIXDN3Tu1ZiMwwhFLUc1PEliartBr9AaOi4wAgIhALN76erczXtM777GQU4t%2FLXdw5%2FTqYYISpWx5IDv6kHaKv8DCCYQABoMNjM3NDIzMTgzODA1IgyKZ9DXky95RBHTHZ4q3AOWlGjSwz8WDRiJZ7gN%2FlddrrpDdyojih3X7ZjoTtddXZyhRVGQ%2BikckASubTXlxBJ1n94vaFmKGTk%2FnR5ajeXpHNfc4GxZAkNqe4dCBLaYltxsbzN%2FJN%2FZ3O3HInUz8Kg3%2FRMMeeM91Yu03yFtCtvJI%2BlzG5hR484SpdVYLb7eRzi1Qp%2BJZdO8oO%2FT%2Fg5Nya%2F9s3YbeCoKqVdJeCYUEgLaOFY8ZDy0QGrzJje3iBPVhgJa81YnVJEvkd%2BlAEL3AQGmW88R4qRDO9g%2B9xfbSHOa7c0e71QlZkOsF49Hq%2BL82KB%2Fp1XRpGo%2FQ7185cXXi5comD1w%2BPISlE9lu0zOF251TR3kUE3Lr1VdtUa4ezU8Lpg5MpI4Ah0dlWGHYkmDhOMj%2BJE7SiE7t5YftzaZm8J664nrJf9DFdIp67X8mvToS4yH%2FXtSJngnQQPVjjOmEpM9V3lkaflEHGEP4OMI%2BRZN%2F26aCLt%2B9L0Vn0GJE%2FcHIYN0mU0LGZf3vpT4YETOpZtUzLVIjYM%2BlfoP9imz127YVay5AXPZqTH%2BvDPeEp9pzXu2mF6BvxCr%2B3u1wnTzNd7h7HOEFK%2B%2F0R4zqNOIA0cYWQbnQ1YQzzG44TuB21%2B7Gkn%2FLCQwM9fC4olUejDovoa9BjqkAYgLldpZuOvsO0cqT8Ufji1aZWs9KAM3bfDHMpIjgzEovOEpXHV1M%2Bi34l7LJkhMiJbxYBDnrX03XdlerTmNu6DzW%2BxlvWYuzrqrmojfEOJXyDauPE1R24tkmFpz0fxFXD6BGmW3eOkf7qpv8WDowWRt8CosA9n5%2B%2FRN4ND%2FC%2FJB%2Fb4zaTMXwUFVLr2dt93DYzwHuP1TH%2B%2FhM8UrOPTP3ivuTeI%2F&X-Amz-Signature=9ffec2843d8375f12060dd8e57b99aead501406884a46ae2ec1490e169e1416c&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Algorithmic Libraries
#### 1. **Scikit-learn**
- **Description:** Contains tools for statistical modeling, including regression, classification, clustering, etc.
- **Built on:** NumPy, SciPy, and Matplotlib.
#### 2. **Statsmodels**
- **Description:** A module for exploring data, estimating statistical models, and performing statistical tests.

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c62885f5-417d-4179-834f-d68f8f2bdf39/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RKRNS3UQ%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T051417Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA0aCXVzLXdlc3QtMiJIMEYCIQCjzhAMBIXDN3Tu1ZiMwwhFLUc1PEliartBr9AaOi4wAgIhALN76erczXtM777GQU4t%2FLXdw5%2FTqYYISpWx5IDv6kHaKv8DCCYQABoMNjM3NDIzMTgzODA1IgyKZ9DXky95RBHTHZ4q3AOWlGjSwz8WDRiJZ7gN%2FlddrrpDdyojih3X7ZjoTtddXZyhRVGQ%2BikckASubTXlxBJ1n94vaFmKGTk%2FnR5ajeXpHNfc4GxZAkNqe4dCBLaYltxsbzN%2FJN%2FZ3O3HInUz8Kg3%2FRMMeeM91Yu03yFtCtvJI%2BlzG5hR484SpdVYLb7eRzi1Qp%2BJZdO8oO%2FT%2Fg5Nya%2F9s3YbeCoKqVdJeCYUEgLaOFY8ZDy0QGrzJje3iBPVhgJa81YnVJEvkd%2BlAEL3AQGmW88R4qRDO9g%2B9xfbSHOa7c0e71QlZkOsF49Hq%2BL82KB%2Fp1XRpGo%2FQ7185cXXi5comD1w%2BPISlE9lu0zOF251TR3kUE3Lr1VdtUa4ezU8Lpg5MpI4Ah0dlWGHYkmDhOMj%2BJE7SiE7t5YftzaZm8J664nrJf9DFdIp67X8mvToS4yH%2FXtSJngnQQPVjjOmEpM9V3lkaflEHGEP4OMI%2BRZN%2F26aCLt%2B9L0Vn0GJE%2FcHIYN0mU0LGZf3vpT4YETOpZtUzLVIjYM%2BlfoP9imz127YVay5AXPZqTH%2BvDPeEp9pzXu2mF6BvxCr%2B3u1wnTzNd7h7HOEFK%2B%2F0R4zqNOIA0cYWQbnQ1YQzzG44TuB21%2B7Gkn%2FLCQwM9fC4olUejDovoa9BjqkAYgLldpZuOvsO0cqT8Ufji1aZWs9KAM3bfDHMpIjgzEovOEpXHV1M%2Bi34l7LJkhMiJbxYBDnrX03XdlerTmNu6DzW%2BxlvWYuzrqrmojfEOJXyDauPE1R24tkmFpz0fxFXD6BGmW3eOkf7qpv8WDowWRt8CosA9n5%2B%2FRN4ND%2FC%2FJB%2Fb4zaTMXwUFVLr2dt93DYzwHuP1TH%2B%2FhM8UrOPTP3ivuTeI%2F&X-Amz-Signature=c5a375224f65f5373fdd1aec1810c4abdfb3fe2c17503f5ff3d8aad7c2235218&X-Amz-SignedHeaders=host&x-id=GetObject)
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
