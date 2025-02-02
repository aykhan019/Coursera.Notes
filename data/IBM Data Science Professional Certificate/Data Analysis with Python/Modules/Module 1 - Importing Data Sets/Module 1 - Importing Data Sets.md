

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

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/997ac361-58a8-4f04-bb0f-79fea4baa761/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WQXVDZD4%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T024320Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIF7KLbHyxYWDnRZkLAyMzzxVfnuFA1YAvD0hT%2FAxk4XJAiEA6afC9FYrf9oKn6cG6eBnRWwyQt9Dn5I51TEtTY4viXYqiAQI4%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDC7AO3CzeXffc6uOACrcA4235sFv7WH2yI3RCuLri6QJCNU%2BEmuHB78bX1EBSQsy1lORnwEnfAMp%2Bl3zetjbJWuiL7%2BgaC4a0vUdx4bv694jBwbdo6gEQa0j0IZLldtkVOy9jD5z73vu3DpIPgJWAyEbEZtMlCEXxfpc9QajcOhxvNwiSrpFlEjNpKJAnqKgfuEFEL2h80Z8XjgsoJzQnDm%2Fnl8DxykqEtapTcJzxKfW9akUD6TQQkrkMb2XZ0wZm1b6pAa4BXOvfJaK%2Bf2T7oHs7gXjcP2Jjr%2BkkUzVgQgPk1b05YA%2F7LjayINr6Z2ZGarLdQmO%2BydlA3%2BUQYAUyGSby6walwVDFGgXo%2BOZqZUc6daKiVP8tQ0zI57K6enAqxwFSi4ZrdSw4oFvKGnPHNK2frDM8oXeVlGmPxDTRbKvqqea2JB6cNn7RGf%2FHf%2FTJnkF3%2B7WaJ4FkMMVzoo6vXKbXnMyZI8UdKY1adpB0cQ6hInopWufRGAsOdUolxILvBLuxY%2BEGErScKSW0l%2FUwGp3%2BSKd6i5BiDJs4IERwKNeLHnm3FWaGNH9ra0%2FoGcLY2Qxhpi9VSQ6qbtvrP8vIeQRipKSPA4ejhrrBqmEht%2F%2Fgmx2CxlCHRCnOUdiRABY1i7Cl5Rgzd1a3qVcMPKe%2B7wGOqUBuA6whXN%2B6CAKljOrIutGYGPgXElmtd%2BRpZBY%2FJ2NjwBnvqV2id7ccdSh9EdKPvG7d1N5%2FEGKQNhMW8ulWWDipEE3NB1UBgx7TN8DtGzfgqceEvQe6W6bP7F3PaNlfjvhjJo2Hj31Kxfk7gJqGOpHy42Rg05L2kotmKyA2pHSM9uj5Yk2MsCX7QhpOeDV5or8ah%2Br9N99oZVGZGcXirEWfXEoM31O&X-Amz-Signature=30ca3bf0166ac6e19cc7436855b0439e3a3a2f5cbede2edb07e1765046489ff3&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Data Visualization Libraries
#### 1. **Matplotlib**
- **Description:** The most well-known library for data visualization.
- **Features:** Great for making highly customizable graphs and plots.
#### 2. **Seaborn**
- **Description:** A high-level visualization library based on Matplotlib.
- **Features:** Easy to generate various plots like heat maps, time series, and violin plots.

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/733d1e42-5a53-4fd8-90c1-3d85254369a6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UPUWNNVR%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T024318Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDIhF8HD2rX80zK6sxG2SjOhlJlcDGVfXcauX9mx6BNTgIhAPiSvur51Igagn6dwZh8pizO4J9jh%2FwhHedOwcQNlzDkKogECOP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwF6ebeYsFVvYoHAksq3AMVwrl3y%2FIKZOoykbylwYTS9UD4rM90aFYjD6pYw5avYrMeX8ovHI085ON4sTX4qdF66Y%2FnESUXD5TlqbeuRPGg%2BXb56SIR3y2rMkFUxPrML2ZQ54bbIEFiZAtDZFa6PQAVfeyuaEec3sEmDWqK3ZYvRgj9oBnNSKcKuRAMOH1c5IHoQmDz82TlaPIwpR6d6Qm4wWvDU7nK7%2B1qvekcP841G4Cm0OMfPRNS23DQLXGF2nb%2FgzCS%2Fy14w2fSRnhq84v%2FrZdrTc37w89hdE%2FC8gvcabNgvl5Ton2ja7aqdIMqcY0sYfW%2FnNx5dJHENoQ3dV3u25lgu%2FgwmYpfR1HZ1cFRdiARJPtDqz6Inw8ufPdGz3%2FZWNyt6BTEE9VYfZTJQUD3twHi0dSDhbYHz1b8EXD3C2Xo6dnhgOTwzdYHWDCPL73w%2F6kZnclPm6rad1bpbowhgf8LRMFdV4j%2F2iFRjOg9RZ8tg6Jkixexb3VEhHtRmUbnLTFYuE8COKiSRDcC2VuV8BiZJfDHABUXAQix8Fdnq3U8xCJBCdcI8fNiTwvJ8NU40F2NAqrxsZW3mGCNrtP6%2BuvqP8LMOuHy5E3LriBGIbORZRPpY8%2FyiRrFOonpKWGnQES7W2usW%2Fjw%2BTCQn%2Fu8BjqkAdDd8QBxObQRsxFpb85y0xuJux13Cqm0tW6fAtiByJvpN0ecFbqQrvUE9%2BgjJqvKOT%2BjIjkemzWXX16XTZqNNaiWINQAxV0Dz%2FTy1g0PWmznlU%2FVQYJji5jawbzrvqcaEHoxRl%2B%2Ftm9Ie%2FAH01Wol93oytkCkm3C93UeLneyX71J8scM7dD%2BL6r4KozkvfaTQVzcNfJT6qrN1c%2Ba%2FwPw8M7Tz5GI&X-Amz-Signature=c6b41d55958b5b73c933ef95c751cad3c80cb1d642d62bf55182fb429a2ebaeb&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Algorithmic Libraries
#### 1. **Scikit-learn**
- **Description:** Contains tools for statistical modeling, including regression, classification, clustering, etc.
- **Built on:** NumPy, SciPy, and Matplotlib.
#### 2. **Statsmodels**
- **Description:** A module for exploring data, estimating statistical models, and performing statistical tests.

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c62885f5-417d-4179-834f-d68f8f2bdf39/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UPUWNNVR%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T024318Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDIhF8HD2rX80zK6sxG2SjOhlJlcDGVfXcauX9mx6BNTgIhAPiSvur51Igagn6dwZh8pizO4J9jh%2FwhHedOwcQNlzDkKogECOP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwF6ebeYsFVvYoHAksq3AMVwrl3y%2FIKZOoykbylwYTS9UD4rM90aFYjD6pYw5avYrMeX8ovHI085ON4sTX4qdF66Y%2FnESUXD5TlqbeuRPGg%2BXb56SIR3y2rMkFUxPrML2ZQ54bbIEFiZAtDZFa6PQAVfeyuaEec3sEmDWqK3ZYvRgj9oBnNSKcKuRAMOH1c5IHoQmDz82TlaPIwpR6d6Qm4wWvDU7nK7%2B1qvekcP841G4Cm0OMfPRNS23DQLXGF2nb%2FgzCS%2Fy14w2fSRnhq84v%2FrZdrTc37w89hdE%2FC8gvcabNgvl5Ton2ja7aqdIMqcY0sYfW%2FnNx5dJHENoQ3dV3u25lgu%2FgwmYpfR1HZ1cFRdiARJPtDqz6Inw8ufPdGz3%2FZWNyt6BTEE9VYfZTJQUD3twHi0dSDhbYHz1b8EXD3C2Xo6dnhgOTwzdYHWDCPL73w%2F6kZnclPm6rad1bpbowhgf8LRMFdV4j%2F2iFRjOg9RZ8tg6Jkixexb3VEhHtRmUbnLTFYuE8COKiSRDcC2VuV8BiZJfDHABUXAQix8Fdnq3U8xCJBCdcI8fNiTwvJ8NU40F2NAqrxsZW3mGCNrtP6%2BuvqP8LMOuHy5E3LriBGIbORZRPpY8%2FyiRrFOonpKWGnQES7W2usW%2Fjw%2BTCQn%2Fu8BjqkAdDd8QBxObQRsxFpb85y0xuJux13Cqm0tW6fAtiByJvpN0ecFbqQrvUE9%2BgjJqvKOT%2BjIjkemzWXX16XTZqNNaiWINQAxV0Dz%2FTy1g0PWmznlU%2FVQYJji5jawbzrvqcaEHoxRl%2B%2Ftm9Ie%2FAH01Wol93oytkCkm3C93UeLneyX71J8scM7dD%2BL6r4KozkvfaTQVzcNfJT6qrN1c%2Ba%2FwPw8M7Tz5GI&X-Amz-Signature=7fe9342f1a411125b711e741dbaef5023d3811193978a0a19614402cc0ba27c7&X-Amz-SignedHeaders=host&x-id=GetObject)
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
