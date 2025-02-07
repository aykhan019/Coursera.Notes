

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

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/997ac361-58a8-4f04-bb0f-79fea4baa761/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667Q52RQN7%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T191117Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGIaCXVzLXdlc3QtMiJGMEQCIGiBpKcq4uDxl1gSKVuvBG8xkguqnSONzmQZ%2FUU1fupEAiAlZ1fPw1WUqdx6GcHxJgo6Wbgktz7k5CYykqOzWKkRWSr%2FAwh7EAAaDDYzNzQyMzE4MzgwNSIMLT2ezMHLauyAiDzlKtwDL7tt2sekTyXE%2BdL2hfBho70lB9TlnmZ8T69gYMQl%2FujFl59i6MwCKoPXt0h3cnudOvT9SQkUhf6MVmcLidpCrW3vACc5FSY3qVCsSMokHc5u68KLGRxTaFe3tqqSXi0jedcAkU9pvkummjrqxJddx0usEVdB8KdneSFaSYToej3FwNgpbQfs6tycCZf3S0wk8lJONZPEbIG23H6zwY4jNQi7wVseLnBx%2F3eE%2B4Oco1vIENj%2Bt9hWuVO9YNcemWK%2BiqlO2YPc77%2F3gRE1N%2Fry%2FmqftjrGvqtXQWFKvVI63sBn32kKCiCxi0dGBM%2Fqp%2BTSTrZt5n7iFQu60Og%2B9wqTkfrz%2FDJqXN3l4Vf%2FWshKEV%2BiCuVMGC4L%2BvH7o89Kn8Ywx206YQY3EFhWNSEzngYa4ckLbtsig1i9R%2FfMcNlAxBvcJ1PCRJvjBpchtViTviwjQWr7Yiecv7Iv2So%2FhWvRTYBv1H7%2FLGWKql4t53OJ%2F3U3APU8LRP6qpghvHJc6CEUnm%2FyTtZ%2Bi8sXyO4PEG2P4jgo10cVlNYTicskEixr39EpsdA3MHCarBcF72Hd6CY6RvbHQeyIzcnre72qSXvtS4saYIGEWB%2B0wJqRDXBatTTYeUHFGIwnO2xWLOwwpJqZvQY6pgFF8F0svqb%2FdhLeCz%2BCLmm4U%2FUFwvnJpCQENm7PaU21nEEeLjk5GFtGpZyF4CWLLTE%2Be%2FvMWn8KGAgRjBWVmf%2FGbpSZJw9KEf8CND2hwmfQcadnWfjnm6BQ73hTKIDSZIVjEQzEsKs8vpi9Uo7xHeTSF8EkyMh6Ffxl92lhRWaHSn68UBP7Ha89FD%2B8SSzwW12A5sc5jbLJTaYRatBWy4mYmNK%2BXnOT&X-Amz-Signature=bb9b2513e05d60f6051df6957f529f1e2602b023320cc15a4736c45de565e10b&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Data Visualization Libraries
#### 1. **Matplotlib**
- **Description:** The most well-known library for data visualization.
- **Features:** Great for making highly customizable graphs and plots.
#### 2. **Seaborn**
- **Description:** A high-level visualization library based on Matplotlib.
- **Features:** Easy to generate various plots like heat maps, time series, and violin plots.

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/733d1e42-5a53-4fd8-90c1-3d85254369a6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QI563Y7R%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T191116Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGIaCXVzLXdlc3QtMiJGMEQCIH%2B6b%2FTdnnj9GERuMbI27icXrbboMm32zEd3kDItanjqAiAKZGGChDUFXeGXz3dirA2pw1uUJMGYYDsHF6WxRYTiBSr%2FAwh7EAAaDDYzNzQyMzE4MzgwNSIMQJJ7DNz4VyZW0hQzKtwDGWg68wSBAxL4ySkEjgpo1UHbdzYa%2FoxCt1zJqVQDDf7002e1NiqxiBXHMxEFceGaU%2B0S4Yzw%2FtyrUEZJTWkfib90Ar9z4l4wimfpRaDy3cIMSVd8j6Cvj4j8vSzc%2ByrSZ%2BM%2FPnyL1IQruywrA2dEx715Yv5wNpiW50po2QGRYgcApZcHXxZSxiPstmEuK5j60S4PLu2vn9ttovaGW8liOUixk%2FP65%2BLxeheXBSpUrn1Sb7tgWHPf7d5r%2BRxg%2Fpa85I5JAjPh9oEdW%2FOGbbmarfCPfMcadRib%2FaiqUh%2FRC80bietYy2QwWX6tLg84bsPHJHMqdyw6%2FF2jafNgW9%2BeG3aOOlJ%2FsGKReexyWRHF5SXs%2Fz7LX1EDjnfIPGaE7VcamlM2%2B1CqdRABJUQJB4F84En3aQdL3veObXYsSA%2BmMjsadOklFLogvO4yieacyVL7N%2FjW0zS6IIbwbu27lHeN%2Fheoo%2FTo1SVDjpya%2B6k45Nej8TwZpCO7hCvKdwB%2F2K6iTU0viPaCOSYAb%2F7kjq%2Fk8KLPVlfn2BPvh1LbKAs19YtV41utWT1dS0cq%2FFaRF%2F%2BQws%2FhBw52HM28Os0jKxjQzpHWKnXDHantPUKQwM5uk1LW%2F2pdvIo3541gFMcwwJmZvQY6pgGeenDHe6IPD%2BWu7K11KZA6YkCbQ4pRoog8AErp3kMgMedKWNd51%2BOoUEGHk5eCFog%2FbiWLagyF1GpnUcGLHHQO5He3KPX8Qix093Jbq8HZ%2Fiv1kQ8OHhcPkz0o3IEoYqtx72fFN5Rff808WvnuusWpSlpCNIlBH1USGbJxux%2B4LaFBUUHQ0JKqHuydvEt6WG%2F0wGo8XrxKcMvYohFdddUz7T%2FXQ4ht&X-Amz-Signature=cde759aa77169f99f2dbcbe37c74972e1ad4236edd72eb0e785cd0e2acaf407f&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Algorithmic Libraries
#### 1. **Scikit-learn**
- **Description:** Contains tools for statistical modeling, including regression, classification, clustering, etc.
- **Built on:** NumPy, SciPy, and Matplotlib.
#### 2. **Statsmodels**
- **Description:** A module for exploring data, estimating statistical models, and performing statistical tests.

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c62885f5-417d-4179-834f-d68f8f2bdf39/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QI563Y7R%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T191116Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGIaCXVzLXdlc3QtMiJGMEQCIH%2B6b%2FTdnnj9GERuMbI27icXrbboMm32zEd3kDItanjqAiAKZGGChDUFXeGXz3dirA2pw1uUJMGYYDsHF6WxRYTiBSr%2FAwh7EAAaDDYzNzQyMzE4MzgwNSIMQJJ7DNz4VyZW0hQzKtwDGWg68wSBAxL4ySkEjgpo1UHbdzYa%2FoxCt1zJqVQDDf7002e1NiqxiBXHMxEFceGaU%2B0S4Yzw%2FtyrUEZJTWkfib90Ar9z4l4wimfpRaDy3cIMSVd8j6Cvj4j8vSzc%2ByrSZ%2BM%2FPnyL1IQruywrA2dEx715Yv5wNpiW50po2QGRYgcApZcHXxZSxiPstmEuK5j60S4PLu2vn9ttovaGW8liOUixk%2FP65%2BLxeheXBSpUrn1Sb7tgWHPf7d5r%2BRxg%2Fpa85I5JAjPh9oEdW%2FOGbbmarfCPfMcadRib%2FaiqUh%2FRC80bietYy2QwWX6tLg84bsPHJHMqdyw6%2FF2jafNgW9%2BeG3aOOlJ%2FsGKReexyWRHF5SXs%2Fz7LX1EDjnfIPGaE7VcamlM2%2B1CqdRABJUQJB4F84En3aQdL3veObXYsSA%2BmMjsadOklFLogvO4yieacyVL7N%2FjW0zS6IIbwbu27lHeN%2Fheoo%2FTo1SVDjpya%2B6k45Nej8TwZpCO7hCvKdwB%2F2K6iTU0viPaCOSYAb%2F7kjq%2Fk8KLPVlfn2BPvh1LbKAs19YtV41utWT1dS0cq%2FFaRF%2F%2BQws%2FhBw52HM28Os0jKxjQzpHWKnXDHantPUKQwM5uk1LW%2F2pdvIo3541gFMcwwJmZvQY6pgGeenDHe6IPD%2BWu7K11KZA6YkCbQ4pRoog8AErp3kMgMedKWNd51%2BOoUEGHk5eCFog%2FbiWLagyF1GpnUcGLHHQO5He3KPX8Qix093Jbq8HZ%2Fiv1kQ8OHhcPkz0o3IEoYqtx72fFN5Rff808WvnuusWpSlpCNIlBH1USGbJxux%2B4LaFBUUHQ0JKqHuydvEt6WG%2F0wGo8XrxKcMvYohFdddUz7T%2FXQ4ht&X-Amz-Signature=1cdd0120e171fd20774768098d066ff7b72dd7fdbd16761e1612004d0f78d352&X-Amz-SignedHeaders=host&x-id=GetObject)
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
