

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

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/997ac361-58a8-4f04-bb0f-79fea4baa761/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663MFUAUET%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T101544Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFgaCXVzLXdlc3QtMiJHMEUCIAO42iRJZtd0A98V081PgLIYdM2DXvg3g0o%2FAP93qvP5AiEA%2F4BfXH%2BXpr%2BTwy5YmIlCcsNpvhQc531vtDFnJXOu7Bgq%2FwMIcRAAGgw2Mzc0MjMxODM4MDUiDMh7YTV94nbIu2LvbSrcA1Am3FsBkTIMhQX5CyMppvuUzDr%2FNjJAFxFOnfK4TfeBFcxz7b1%2BLWLegvXEZmpqBgsodrtBSdsSvwlzUgge9XZLa0UrumlbNf%2FJesWQ1c4w1UYXjAp%2B8SjUx8JzGYvcxXV3wkz6XIxIztA026Qk00FNhhZYyeX9TdVi0q6oLjTkqrPzI3oFE6aP87B9gSMBo8x42QXrthopTW%2F5PRXadIW1q7USIhAmm4Ct4tIGMVc3Zrw5V3WpDeaJEhY2Ol%2FXm2Z8Jmf%2BifFCR%2FfCpPz7QHfNaliZpQU9nBEUdixTSnSgRTFYr0yJtAVDSriUa3z4eoXYQWkW9M6rWh%2FeZkmQXqRpWS1efHykuQcQLuCe%2BrvhfhyPuFalzHMgCCcBh%2FcUG1N4RWNcNMx3ik82MMMYmAvAgCeFehNSz%2B5Jeg5LPc%2BgFOe5Oske2UU3Iez%2BckJT4IJfi4jsZYuMmL%2BJEyGgl%2BnKABhe4hImtdrrwXj69IaGIjSIqmwqrFWwl02tM34opph9wFtuIwdg2VbGEhxltB5GuifFx7z3j7jd30HAimxyLRK%2FiQav9TEhAxkOpKwIMODX1YajV58RFuQmw5a5KPzrvxDlbR%2FjamELgixI0JU%2BDgulTKw8Uz8x3MtyMIP6lr0GOqUBTUCwANtDX0XBW3w6ypXn5xVQXMjUbOdh0rn9vnXffB5t8uDFtiVnWjH%2FXIIh4jU7mhF%2Bx0FF%2BDPo3XrtYeQ4oekNVlQnvM7B%2FtqF4XrBdtujfIAoqrxRvJUQpu8Nn%2FY1JK6uSYaduinP80dh9m3djiUuuUrNphMscfwjyFNjJXUm3tuM0P8rPaWBtXjPy5SOx6GKLgfjkDaQAhgiCFb71ukwuJzw&X-Amz-Signature=9cdd596e1e32a3119eab73585d2f1d71c354e1d3979d93d76ac549881433bf18&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Data Visualization Libraries
#### 1. **Matplotlib**
- **Description:** The most well-known library for data visualization.
- **Features:** Great for making highly customizable graphs and plots.
#### 2. **Seaborn**
- **Description:** A high-level visualization library based on Matplotlib.
- **Features:** Easy to generate various plots like heat maps, time series, and violin plots.

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/733d1e42-5a53-4fd8-90c1-3d85254369a6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665FY5DLTM%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T101543Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFgaCXVzLXdlc3QtMiJHMEUCIG%2Bozru3zrayWZeC6OJV6EU2UmJlj47mSqaIaRm4R35OAiEA%2FbaojR%2B3AAO4dJUNwqrBLNhnEIZEIpdlimwMFDT9lBAq%2FwMIcRAAGgw2Mzc0MjMxODM4MDUiDG%2FbMAaDaN8CkGXSyyrcA0hudrWH5W%2BaDZIAnG0mpfGvDq1gK4Dtfq9YNOcXXVPcv6aOcQXnxAH8UuPDbZHIBDImi3oB3QVJiOxUsCAEmRVFMh86x2Dl6N9Gj%2FqvQfj6Dumx9B0UlnI1RD0xpJ3fUrEUl9ck2mq9O92uRCmDf7MkgkERa9R4yfKRSW9Gbap6fCKpQE%2FHj77vI1xvm41FjyB%2FUaK7wLBhJYyD0gdjp7aEehmKlreZpfg9HHTrP63PpJan53J5zmDXWj52mqTYLCJ7osXiLYGelJ7IsalDN1dOkc7p0wtk5uvhlF1BHFzjkah2B3OIqftEzbveVWioRYOVu33YRewoEZFPQ6ToYqI26avGqTzou%2BVKDP6EzM9fXt9QJ5IIwBLbEDzdE6Y8pAy7zT5rILhuy3pD8qgBCRCcoXF%2F9%2B5TIyPuwDYArhBc59dj7xh6rHFeKRJ3cRUkRKRL1HA9XV7qDb3jxT0Q7sH1V2zNKnpLqd0etMdwVw3Wv0zLLssQeapI8AaGEGunam9KUKlfAdP3%2F%2F2xIL1sROaXsouvJGZEA6nXD5mCLlcflVRvPoW%2BppEJvJkBC%2Bhql87P%2BM%2BOyHTdNk9l%2B1bGu4DnTA0klzpS8izMZapYFASi%2Bf2O2L1iqNA%2BfHE0MMD6lr0GOqUBprKJJtYKSRhdyXAagzLmOI6IOCJEzdHMAhvuLlMZcScHTOyAGtmEWWP39ctDYHGPY6qDsuIbzWefOaUp%2FB%2F6h6LS0465ijtuZrLWuSRaAJvVJsuGWkCL3uolBRfMFBVEfxFPwWt%2FujSTXq5UZjU1%2Fgo9zb3n4yA5hjnyKSUEBtJzx9S5%2FJb%2FOqyYKrTVO4ibBKO4R9C0UU13I5lqXDhnhkYd2PHw&X-Amz-Signature=7f16823c6b047748716494311efe44b4f4791fa39f17f01dba3520d083fa6e36&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Algorithmic Libraries
#### 1. **Scikit-learn**
- **Description:** Contains tools for statistical modeling, including regression, classification, clustering, etc.
- **Built on:** NumPy, SciPy, and Matplotlib.
#### 2. **Statsmodels**
- **Description:** A module for exploring data, estimating statistical models, and performing statistical tests.

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c62885f5-417d-4179-834f-d68f8f2bdf39/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665FY5DLTM%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T101543Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFgaCXVzLXdlc3QtMiJHMEUCIG%2Bozru3zrayWZeC6OJV6EU2UmJlj47mSqaIaRm4R35OAiEA%2FbaojR%2B3AAO4dJUNwqrBLNhnEIZEIpdlimwMFDT9lBAq%2FwMIcRAAGgw2Mzc0MjMxODM4MDUiDG%2FbMAaDaN8CkGXSyyrcA0hudrWH5W%2BaDZIAnG0mpfGvDq1gK4Dtfq9YNOcXXVPcv6aOcQXnxAH8UuPDbZHIBDImi3oB3QVJiOxUsCAEmRVFMh86x2Dl6N9Gj%2FqvQfj6Dumx9B0UlnI1RD0xpJ3fUrEUl9ck2mq9O92uRCmDf7MkgkERa9R4yfKRSW9Gbap6fCKpQE%2FHj77vI1xvm41FjyB%2FUaK7wLBhJYyD0gdjp7aEehmKlreZpfg9HHTrP63PpJan53J5zmDXWj52mqTYLCJ7osXiLYGelJ7IsalDN1dOkc7p0wtk5uvhlF1BHFzjkah2B3OIqftEzbveVWioRYOVu33YRewoEZFPQ6ToYqI26avGqTzou%2BVKDP6EzM9fXt9QJ5IIwBLbEDzdE6Y8pAy7zT5rILhuy3pD8qgBCRCcoXF%2F9%2B5TIyPuwDYArhBc59dj7xh6rHFeKRJ3cRUkRKRL1HA9XV7qDb3jxT0Q7sH1V2zNKnpLqd0etMdwVw3Wv0zLLssQeapI8AaGEGunam9KUKlfAdP3%2F%2F2xIL1sROaXsouvJGZEA6nXD5mCLlcflVRvPoW%2BppEJvJkBC%2Bhql87P%2BM%2BOyHTdNk9l%2B1bGu4DnTA0klzpS8izMZapYFASi%2Bf2O2L1iqNA%2BfHE0MMD6lr0GOqUBprKJJtYKSRhdyXAagzLmOI6IOCJEzdHMAhvuLlMZcScHTOyAGtmEWWP39ctDYHGPY6qDsuIbzWefOaUp%2FB%2F6h6LS0465ijtuZrLWuSRaAJvVJsuGWkCL3uolBRfMFBVEfxFPwWt%2FujSTXq5UZjU1%2Fgo9zb3n4yA5hjnyKSUEBtJzx9S5%2FJb%2FOqyYKrTVO4ibBKO4R9C0UU13I5lqXDhnhkYd2PHw&X-Amz-Signature=1ae4a3f99bd96f7cfc0e0455dee222e3929f0939cf3e61efa2c33af736311d74&X-Amz-SignedHeaders=host&x-id=GetObject)
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
