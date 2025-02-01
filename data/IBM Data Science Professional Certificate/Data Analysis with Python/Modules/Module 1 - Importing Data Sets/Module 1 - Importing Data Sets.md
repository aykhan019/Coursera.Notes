

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

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/997ac361-58a8-4f04-bb0f-79fea4baa761/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466256NQ4NL%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T111058Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFhl%2F6pFOS%2BvqonJLvUkCjvW6M2VldfZof6sWYgDSYQHAiEAoS9T8nEbFJYfPJbq4pLcauCG25iATTnUNd5WAnnPrDwqiAQI0f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDIHz%2Fe9UEbapOgTqgCrcA1afl48Jlb3Jr4Kxg7lrkpnzbvER1xlWjez6ZXR1pUJeDGwBlsJt0SGYJbsndTM3%2FdHMjySUHpKpyFjFDqSEQ2UEZwMOb%2FkVylGl3BF240bsxVAsDknu4J4NzsdD9HqItbzP4arAT7gDR0FiwE1PFI12TbXujbTBGHEE1SGICG8ujuo%2BSWc%2FIuttuCGkqciAVRkqKbg04lmnktEQBRjrXGs1AAjH5serNd8OxnV055Z1jQQL5V5CxmV6Wc8SKxSa4qZjjz6PHMqsjS%2FUs%2FxUBswvhhyxyaQlpAQSaZG51tCaAtk2kVdP9rxl5QaGr5qpV6m4W3NgXUCTWB2k4VBglWsl4eolZY04Hl8Quegcrf%2B6nB8jzBv68fxHXBeDLFdPMZalwRqQmRVZJo9g8iad2XWsSF573hfEsQ9wW5f%2F10sHtzDSEwqqRr9wJfdA0JeMsiyIv8YyWLygiSH3H8k0VtvjNsCG%2BdRksf0SlVS2ea0D59BFP1JLdLyW4yP%2F%2FErkG5V7xkqVL1CVT7%2FES0tkQyi9cI57Ao%2Bi0gsDMqg1Chn0sQ6WWWpBSESIO0iXtLswKntpYw58GsBNDmm3rbxerB%2FsUfH%2F6agUvPg9NjXsY5NCMf1y9f6Q30kgMJfsMJqk97wGOqUBgmEsYFgG%2B6k%2FqCSYoB27wLzGRxQrxzq61MM71ioG07xKa1zABRAIHpXlYg2d6EslsLTqiKhj2LbEWy097f5TfrCYaA31ENjno5yJMfOSlu%2BdzARJKkU4wGWrI%2FsCGYMMb3u8GuLoulhVACw%2BKYTZwimvylgcixT5O5tK4HJn3IGxQDzrQPXSVtZHA8YxrUz%2Be2u8hz0HMdZNx2XdcbQeD5cMoVQB&X-Amz-Signature=9864635e7221a8ea5925e4d6cf0802637daace39e53e34c53e8578755aab93e9&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Data Visualization Libraries
#### 1. **Matplotlib**
- **Description:** The most well-known library for data visualization.
- **Features:** Great for making highly customizable graphs and plots.
#### 2. **Seaborn**
- **Description:** A high-level visualization library based on Matplotlib.
- **Features:** Easy to generate various plots like heat maps, time series, and violin plots.

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/733d1e42-5a53-4fd8-90c1-3d85254369a6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XJQY7IER%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T111057Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEPJq%2F65Dv1JkAXYdbPMLKWrcKz%2FlmBrCK%2BXKXWfgR9FAiANLL7ULAtqXQA4NHQnaibdtZhACvXFBpiLAiNVWuyGoiqIBAjR%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM2bnq6BiwyDt8BfAuKtwDTZxeBi9h2es9DyjoRiCRfKcJg81Hj1Yzq4ZK9k1fPkdgbXuG1LSLGUbAuVp%2Ff0wa5AecFQaTLjcojwP0jeWlOrKo3yS0cVfd8uzcfW7bh73X5mqeR%2BFcVw5NfYh6tn10botTtAmSxqdihitlPZsS81WpcP65VPwEV1CMNX2BXSMeUXFQnz6CzbYoToiCbdvRkJii%2BMD6fxrvErTILgDAqMJHTVm%2BF%2FqsP34KAvIc0ZlO3iLZq4%2FB6LwfpYfcnRQ3VBU2JFkAwJv%2Fj%2F4Iso9XB0xkDTZ1BXm%2B%2FyXslyu0pE51%2FejBvbKoCP4fVzer2mIbE1NPlYO9QqoU0sRD8Gx7OtoehgXBGQ%2BXDZDYk1%2BoaPN3rV2iLu2jTi4WRz3UejuyhM8%2F80gJ6gER5SI03YoAtaDAAJ7LRh7Kv0wTeH%2BYzsT991eK5eidbULN4nFLM4nnnet6%2BwCx2Tm6cu%2Fwq0GD3XnKcEjl9VcHYkGQ0YrPv7Jvqj9nNlUbOIgt5fWhl%2F%2BDXt1XjfC3xNiuu8hsZk1ayKwK7eLZcYkKT2S9SripEBLftK4Vamj0MM%2FdHqWnRgCpvrxUUPC5KSjF07S3y9MWk8%2BWDhAZTK0wQGXNTlKbPb1FzxdhIZwAeimaRBAwyKT3vAY6pgGeHPd2588Nsr32b9lsloSHNeyxBm70H8sFtKaB2NvEKOk1KL4p1M0cAhk5nVmKX83iRNRxYgjRwJMWL9F7VdxoYLmtrhNTJ0Mx9oPyjt80Uf2cc2tnjgFlJ%2BEVfHpYeJPUNIXHZNS8DwfBbOqmthUUsdNKCBHTDmdJIdKBKkQkqmvx1BjyaVxPAKRmaaNXa1WI6ufaeHn%2FL8GFQw0H7Kj4Yk8sX6eE&X-Amz-Signature=4a622d8d27d7c9d802dc11ad480ab5cb8794319d0d0e4e381eb29f613d2c38b2&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Algorithmic Libraries
#### 1. **Scikit-learn**
- **Description:** Contains tools for statistical modeling, including regression, classification, clustering, etc.
- **Built on:** NumPy, SciPy, and Matplotlib.
#### 2. **Statsmodels**
- **Description:** A module for exploring data, estimating statistical models, and performing statistical tests.

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c62885f5-417d-4179-834f-d68f8f2bdf39/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XJQY7IER%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T111057Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEPJq%2F65Dv1JkAXYdbPMLKWrcKz%2FlmBrCK%2BXKXWfgR9FAiANLL7ULAtqXQA4NHQnaibdtZhACvXFBpiLAiNVWuyGoiqIBAjR%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM2bnq6BiwyDt8BfAuKtwDTZxeBi9h2es9DyjoRiCRfKcJg81Hj1Yzq4ZK9k1fPkdgbXuG1LSLGUbAuVp%2Ff0wa5AecFQaTLjcojwP0jeWlOrKo3yS0cVfd8uzcfW7bh73X5mqeR%2BFcVw5NfYh6tn10botTtAmSxqdihitlPZsS81WpcP65VPwEV1CMNX2BXSMeUXFQnz6CzbYoToiCbdvRkJii%2BMD6fxrvErTILgDAqMJHTVm%2BF%2FqsP34KAvIc0ZlO3iLZq4%2FB6LwfpYfcnRQ3VBU2JFkAwJv%2Fj%2F4Iso9XB0xkDTZ1BXm%2B%2FyXslyu0pE51%2FejBvbKoCP4fVzer2mIbE1NPlYO9QqoU0sRD8Gx7OtoehgXBGQ%2BXDZDYk1%2BoaPN3rV2iLu2jTi4WRz3UejuyhM8%2F80gJ6gER5SI03YoAtaDAAJ7LRh7Kv0wTeH%2BYzsT991eK5eidbULN4nFLM4nnnet6%2BwCx2Tm6cu%2Fwq0GD3XnKcEjl9VcHYkGQ0YrPv7Jvqj9nNlUbOIgt5fWhl%2F%2BDXt1XjfC3xNiuu8hsZk1ayKwK7eLZcYkKT2S9SripEBLftK4Vamj0MM%2FdHqWnRgCpvrxUUPC5KSjF07S3y9MWk8%2BWDhAZTK0wQGXNTlKbPb1FzxdhIZwAeimaRBAwyKT3vAY6pgGeHPd2588Nsr32b9lsloSHNeyxBm70H8sFtKaB2NvEKOk1KL4p1M0cAhk5nVmKX83iRNRxYgjRwJMWL9F7VdxoYLmtrhNTJ0Mx9oPyjt80Uf2cc2tnjgFlJ%2BEVfHpYeJPUNIXHZNS8DwfBbOqmthUUsdNKCBHTDmdJIdKBKkQkqmvx1BjyaVxPAKRmaaNXa1WI6ufaeHn%2FL8GFQw0H7Kj4Yk8sX6eE&X-Amz-Signature=fca515b1186a5bb30d3af377741be78c3e997681901ee87066002d582bce9d32&X-Amz-SignedHeaders=host&x-id=GetObject)
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
