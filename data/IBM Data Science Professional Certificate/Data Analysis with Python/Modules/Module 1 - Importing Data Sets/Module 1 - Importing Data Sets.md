

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

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/997ac361-58a8-4f04-bb0f-79fea4baa761/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664LPYQWDJ%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T122532Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCeqtz1lAuBGsFLOHNmEBglIgr%2B9SgUuk6IJAj2HdO6BQIgJgJOdeapAt5N4fLVTzgk0%2F5mkk%2FYvRPU0vNOEqBUmGYqiAQI7f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPgia54Kqp1vnSBHrCrcAx%2FQLPrja00x6XfaOXpRWQmGYG6o9XtHSb8uvBW1GrUC9Rkjyew9aeC5NfDR0EGnqpaij7xbdkoZPMzlxnaKB7gDyxdVkC1XprdA9MG3j22vPFdZuW%2BBwmqBc6kRAdtozom6lEIWuy6iDpl%2BmeA4%2BbsGsTYGxFESmebaBvZm5x%2BMLk1WlGkfCAL5SbMR230Qfwzu3VSdReZPOs94zSaYFYpdBUQG%2BUjIefQlMnLzraUJlDwoZFRooUFphHCWmXomy4Jb8ZPzxdvcSs76IKBlUyCkfEjtuMbp%2F5%2B0tXMpj%2BozXRtZBYmvLCDoBOmDka0IBjkSWZbfeeihvXwYE%2FtL1YZ09n7FkpcFWGfz5cOoI1rgCRya2k1wJKSD4gfBuQcfD72H95nEhLncE%2F%2Bt9g0xfol9FBK9Oy7X2Evdb5rDPww2JK5n61YeGq6gQMsbJiL4DOzU7BL6oGBPcJZ3f57oAMZxvGtCim%2Fj2CSb3vWNVc1xkchYSjZwlOh6FNsaea6qIEmsfpq5YcQFUbY0cVxyLGd4U9eU10WAhysJKPQe0uiTM3FiwFidp7XWVgEZCmUjkGkgR1T2qCPBlcnwbHZaXp9n8IVOL3aWFvPbHxvIahU120pUh8aaAvagoV0VML%2FB%2FbwGOqUBxuEfqw4R9ReoK4ga8K9F0QrtLTsePGBhbsNzDQUF%2Fqs%2FP7ps%2FttMFrbXIO4tn3M7F8rW4W%2FijBbnTLNdTlSkAstgvQsZMejAwpOGUd0O%2F76eVp5VOBGrWg8J9rQSyhHqmwyuxSdBtnp8sYkYiH6b2RclPe75Ddizf%2BDy8cBiRrcDWy6GCj4tlLU5tbzpI%2FSWJIPAhH4GKvIUnmKFOQ0pmGnBgEap&X-Amz-Signature=d8a45220ff8d3f97ea0cab37bc7cf4b673f91c4c2e9638924a613af17ea94ce9&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Data Visualization Libraries
#### 1. **Matplotlib**
- **Description:** The most well-known library for data visualization.
- **Features:** Great for making highly customizable graphs and plots.
#### 2. **Seaborn**
- **Description:** A high-level visualization library based on Matplotlib.
- **Features:** Easy to generate various plots like heat maps, time series, and violin plots.

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/733d1e42-5a53-4fd8-90c1-3d85254369a6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666E5YOJYI%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T122531Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFQrBaHobLllvz7lCJzXxO2mjPF2huzJXU7tFAXcvaXUAiBmWnjmFtiGPBNaVn3oT4dMWhSBBtNAIZUgfNI7mSCAjSqIBAjt%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMUGGFbg0%2Bj2MT59tTKtwD4MZdRjlE3J1mPXC7vU14pownWK0IfzN%2FXFy7tar8CzGTphJhFKJeyDRblOsyPdGRDS7renTzdEfdSAt8vhgMyh5KagUxhbZ%2FkfGIWMe0HmcNky8S4w%2FLZqGdGPALg7uhpisSmcvgx9HnMVc5pkPvA4HtdDojhM%2Fvz3%2F6TeEwkZVbt8O8azABVFZxOgOgLM5%2Bd3EXdX80T2%2FWY0BbvGosqdBYxLeZrgPeHq81%2FfG3wMLLYOwBeSV%2Bidbp6BPugg8z%2FV8p8NTQ%2FzbcLGTXjNcFBxf%2FpRTT61w%2BoFgm74tS1R8v%2BWomOgVBoPcEvQBRVqRWkljqj7uTZOQyR7ydemUJhyV44zUAe2CDC9pcfMEW3l%2BjZReoorak3zxK1iuItrxo4wZmqxd26opEFwpnrGXEYdG6P6J92nrVunWIQzgWb%2BlC%2FZyhzZOz4n8l1zQRItaIj90wDiEzJRiaS3w3ZvsL%2FKUsPUIDWpr4amHZ6nRld%2Bvr%2BWgpzoRxiQF5aK96r%2Bl8aidpL3vXG1xfRh8VUOJ1dxb4lB9kyZeqyWjHe0VKkH5l6gl8R9NziueAAaN0wac%2FQpjDvh4mUXwhZwWwP6eOGu0YsIyBORpQI9Zp0gxKwEYq3pebC9OnG3EaHiYw6bj9vAY6pgF2MNY2qqgHJpmHH9jR2EUP38Lz6nv3%2BlsW%2Fql2Tk8eD8J27RWpKNCtxfm78zDPF%2FzOyee7MErP4l1ZJh9BdR2SyP2wCuA877X6ykjTmO1XppiWhMfG0t6zXUJPyljni3E7Acil98ykZN2ZOTk8aKpA%2FSGBZhEoVuywE%2BA9LUyjFtcJHS9Yw%2F7EU0LVcJe0AP3FjIKXmZdxqIwaPes0nOIYPzt5G5OZ&X-Amz-Signature=de3a01c0f4743ac12d6a4969512d82504570ad216305cdfa0cf74872f645f43f&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Algorithmic Libraries
#### 1. **Scikit-learn**
- **Description:** Contains tools for statistical modeling, including regression, classification, clustering, etc.
- **Built on:** NumPy, SciPy, and Matplotlib.
#### 2. **Statsmodels**
- **Description:** A module for exploring data, estimating statistical models, and performing statistical tests.

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c62885f5-417d-4179-834f-d68f8f2bdf39/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666E5YOJYI%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T122531Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFQrBaHobLllvz7lCJzXxO2mjPF2huzJXU7tFAXcvaXUAiBmWnjmFtiGPBNaVn3oT4dMWhSBBtNAIZUgfNI7mSCAjSqIBAjt%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMUGGFbg0%2Bj2MT59tTKtwD4MZdRjlE3J1mPXC7vU14pownWK0IfzN%2FXFy7tar8CzGTphJhFKJeyDRblOsyPdGRDS7renTzdEfdSAt8vhgMyh5KagUxhbZ%2FkfGIWMe0HmcNky8S4w%2FLZqGdGPALg7uhpisSmcvgx9HnMVc5pkPvA4HtdDojhM%2Fvz3%2F6TeEwkZVbt8O8azABVFZxOgOgLM5%2Bd3EXdX80T2%2FWY0BbvGosqdBYxLeZrgPeHq81%2FfG3wMLLYOwBeSV%2Bidbp6BPugg8z%2FV8p8NTQ%2FzbcLGTXjNcFBxf%2FpRTT61w%2BoFgm74tS1R8v%2BWomOgVBoPcEvQBRVqRWkljqj7uTZOQyR7ydemUJhyV44zUAe2CDC9pcfMEW3l%2BjZReoorak3zxK1iuItrxo4wZmqxd26opEFwpnrGXEYdG6P6J92nrVunWIQzgWb%2BlC%2FZyhzZOz4n8l1zQRItaIj90wDiEzJRiaS3w3ZvsL%2FKUsPUIDWpr4amHZ6nRld%2Bvr%2BWgpzoRxiQF5aK96r%2Bl8aidpL3vXG1xfRh8VUOJ1dxb4lB9kyZeqyWjHe0VKkH5l6gl8R9NziueAAaN0wac%2FQpjDvh4mUXwhZwWwP6eOGu0YsIyBORpQI9Zp0gxKwEYq3pebC9OnG3EaHiYw6bj9vAY6pgF2MNY2qqgHJpmHH9jR2EUP38Lz6nv3%2BlsW%2Fql2Tk8eD8J27RWpKNCtxfm78zDPF%2FzOyee7MErP4l1ZJh9BdR2SyP2wCuA877X6ykjTmO1XppiWhMfG0t6zXUJPyljni3E7Acil98ykZN2ZOTk8aKpA%2FSGBZhEoVuywE%2BA9LUyjFtcJHS9Yw%2F7EU0LVcJe0AP3FjIKXmZdxqIwaPes0nOIYPzt5G5OZ&X-Amz-Signature=6f0ccf251ccd5a784024b859e2e2ca69df5c84b9f8b7c263315aef1a239c5529&X-Amz-SignedHeaders=host&x-id=GetObject)
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
