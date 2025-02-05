

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

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/997ac361-58a8-4f04-bb0f-79fea4baa761/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TMVFQFXG%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T091612Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECkaCXVzLXdlc3QtMiJHMEUCIQDlKN0irED615Ldcbw1v7uHOanse4zZtk5Ev0jLz5bK%2BAIgYvgE%2Bd0sOsqu4nqRaspKSQxaD5mCRUemsRVq9gBoDZ0q%2FwMIQhAAGgw2Mzc0MjMxODM4MDUiDEVFwYDtqfAXMpmDECrcA7WDs3Uuq6bKwgSI4lwgh7s9Ucl%2BDUTXSA%2BlErapyyPRAyjxnQYGYi8oFZZ3VRKFr6V0GLTycmPd6cI%2F1gDHkdX%2Frg4AD4ZKRHRjbPPamG5kBE5MVX51T7H3eOXH5uxX0ONmAogFVUj60h27KcjCWBrK7GzEQSNsnRgEw1ANRebOC%2BJeOZ2J8SA1FS6KHtPKjmCEpbCduTnBXEW8LJBG9V5aKsue1hcBJhIxLsg%2Bw9usUCTh%2F8dEhnUVA%2F%2Frb3yZBOtM6rucHByZWdBvFW7ZXGeZ1dh2FBnly0jHfKTg8qm2OLTxGuAsgXKHOE9DAXKadnjaUrm%2FfruML33xo8dRWxcYsdHTy55b7bR2jTAGXzr6SYH2WliZZ4FUCIN5av5vqXcRJDvV%2B%2FI3iGIkyf10%2FGWBnrUYbr2LlRLy8%2Bm%2FK9a1xV1Ok2bLG5IXiYglIRbgJbaUVZv6NIT6u365KpDY1br9NSE8ryY%2BA4qO10iuFNWB7RFGcPLM8JWJkblgcHsG3BfeE9wABQmSkEd8trSZXAp766Df00a0VUhUoa%2FWBTki5fYhJLZ0H6gra37m2xvgBNHuBY9srh9%2Fei5uaXMl8tTmtUyQ4F%2BRBJsPYyo%2FRKURA%2FzQGGfLpmZF1924MMXPjL0GOqUB0vHh4ha8vYoe9K3jkU5EyXDoijj8H9v1Q7JodBtILHZlwpSHrwzMXgjIvBatfOACvcDrkFlnT5gSSowJMN8LQ70y5n%2BhtsAEo7GfaaE4nmP1ojfzhLPki%2FJinCOge%2BuiZ44c3gej2v9WvX%2B%2BfOf3LYLo358z%2F9e9m%2BILJ8ge%2BJ2F5Zd3ahxDVWaobAZWXy3g%2FNORr2gps%2F%2BpizVDnw3jc2N6iUTE&X-Amz-Signature=c547fd834d7517a3d3129171762d235f5b6b889516e907cac560f556bedc7fbd&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Data Visualization Libraries
#### 1. **Matplotlib**
- **Description:** The most well-known library for data visualization.
- **Features:** Great for making highly customizable graphs and plots.
#### 2. **Seaborn**
- **Description:** A high-level visualization library based on Matplotlib.
- **Features:** Easy to generate various plots like heat maps, time series, and violin plots.

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/733d1e42-5a53-4fd8-90c1-3d85254369a6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YQHFKS4B%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T091610Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECkaCXVzLXdlc3QtMiJGMEQCIFnQVhJcnDANc2SYz0CV798VGb8WkfiRGPuPSTSV%2BzwyAiAnYDip1vXC1xOjOYeHrpqPTiJX0YSc3As7ht3NG4aEjSr%2FAwhCEAAaDDYzNzQyMzE4MzgwNSIMqWf3Nb5q6aIzUpNMKtwDGcSeTNfRU4RYQnnhaejqdmK3FUIrysTsTsJ88BkAE2XtvA4zAWRcZRwCIno6xGVsSn%2F0U3y8ViVwB%2B0QGhNPScli%2BlUlj1PB%2FzBrT4TtEn%2Fkc8flNW5K%2BSodTnLd%2B97m6UOPVZmS%2FCbmIy7RoInV5zr6A7yr9XeGK4FklmXhfmzOuhM1tFPNm1d%2F%2F9EFBfHd3i%2FASnHf%2BM5vtSDYC4DjOZVkEkcYFvXFwKU6MRUPhiWCFlmdB4uY9JWkBXO%2BY1uA1m%2B1BJGSDNbO9e9pzb7PXrQJwhc0IZLLPtYVjPRAqsbCU4B37RstdzYTOvbyulUfi62adeRbhuGwm8y3KSBQExCxExAoLa0uFDzdIWwBhz56Jg5FduYe1YUclvNCR97RB9hTpMm6CNu7UX3y0wvJhL3%2FSckoxG06B5qcbRW6xjburoNmczRX4JcUpvp%2B9FuaES7xmQJ5n78W3wAqbi6WBkoZo4oQwUXPF5Da13JVCM4TuHixST%2BKM0T9ZRuX76ViucxMcayVxLlvYlh6HzY0eqbCvR9D3p9f3lkvnwl3iB%2FnER%2BF%2FkS3JB1K%2FuGde6qGkt1Fkp5LwqPFk%2FR8c%2B8i5VwkucN722v8ieaU4%2FHdZ9EUJw1O8rL9kfiOtfswhNCMvQY6pgEsJSVat6f5qJ0%2FM8rOkImOlABBizY5cAwX%2B5AHG6%2BNHTeDmrJnOkYlPH%2Fz85fq%2BgLXncCePo1HPZxoP9Can4Dlb36I6UtnhsIZ9a30zedUnvEnBbh2cmhtxl%2Fm4W6MoosCmAQUqR6BC8xnhFL2gt8heO3LDEcvfRz6ern9aRWrqXC8Jklz6A8irFZ1AzXDkf48SlzyjGXD3Pa98mjuvITGJcF9nxvO&X-Amz-Signature=434ad843109e03949e386d3b03770b783567f0c3c9b5bf6f3bc1e212cd7fbcd1&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Algorithmic Libraries
#### 1. **Scikit-learn**
- **Description:** Contains tools for statistical modeling, including regression, classification, clustering, etc.
- **Built on:** NumPy, SciPy, and Matplotlib.
#### 2. **Statsmodels**
- **Description:** A module for exploring data, estimating statistical models, and performing statistical tests.

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c62885f5-417d-4179-834f-d68f8f2bdf39/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YQHFKS4B%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T091610Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECkaCXVzLXdlc3QtMiJGMEQCIFnQVhJcnDANc2SYz0CV798VGb8WkfiRGPuPSTSV%2BzwyAiAnYDip1vXC1xOjOYeHrpqPTiJX0YSc3As7ht3NG4aEjSr%2FAwhCEAAaDDYzNzQyMzE4MzgwNSIMqWf3Nb5q6aIzUpNMKtwDGcSeTNfRU4RYQnnhaejqdmK3FUIrysTsTsJ88BkAE2XtvA4zAWRcZRwCIno6xGVsSn%2F0U3y8ViVwB%2B0QGhNPScli%2BlUlj1PB%2FzBrT4TtEn%2Fkc8flNW5K%2BSodTnLd%2B97m6UOPVZmS%2FCbmIy7RoInV5zr6A7yr9XeGK4FklmXhfmzOuhM1tFPNm1d%2F%2F9EFBfHd3i%2FASnHf%2BM5vtSDYC4DjOZVkEkcYFvXFwKU6MRUPhiWCFlmdB4uY9JWkBXO%2BY1uA1m%2B1BJGSDNbO9e9pzb7PXrQJwhc0IZLLPtYVjPRAqsbCU4B37RstdzYTOvbyulUfi62adeRbhuGwm8y3KSBQExCxExAoLa0uFDzdIWwBhz56Jg5FduYe1YUclvNCR97RB9hTpMm6CNu7UX3y0wvJhL3%2FSckoxG06B5qcbRW6xjburoNmczRX4JcUpvp%2B9FuaES7xmQJ5n78W3wAqbi6WBkoZo4oQwUXPF5Da13JVCM4TuHixST%2BKM0T9ZRuX76ViucxMcayVxLlvYlh6HzY0eqbCvR9D3p9f3lkvnwl3iB%2FnER%2BF%2FkS3JB1K%2FuGde6qGkt1Fkp5LwqPFk%2FR8c%2B8i5VwkucN722v8ieaU4%2FHdZ9EUJw1O8rL9kfiOtfswhNCMvQY6pgEsJSVat6f5qJ0%2FM8rOkImOlABBizY5cAwX%2B5AHG6%2BNHTeDmrJnOkYlPH%2Fz85fq%2BgLXncCePo1HPZxoP9Can4Dlb36I6UtnhsIZ9a30zedUnvEnBbh2cmhtxl%2Fm4W6MoosCmAQUqR6BC8xnhFL2gt8heO3LDEcvfRz6ern9aRWrqXC8Jklz6A8irFZ1AzXDkf48SlzyjGXD3Pa98mjuvITGJcF9nxvO&X-Amz-Signature=5de6410326fc31179452b6a8df6aadf178ddb8e59d5af960fd8fb2f406c26292&X-Amz-SignedHeaders=host&x-id=GetObject)
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
