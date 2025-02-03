

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

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/997ac361-58a8-4f04-bb0f-79fea4baa761/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SM4I7XJP%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T132021Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDDj%2BhlpUgLiCObe6DMsrImMx1J0Nc2pqJKRRJcAPUM7QIhAO6xAtLaLodqY2%2FqiKLNwvg9eIhX%2BO2Tb6vfMJRV0luxKv8DCBYQABoMNjM3NDIzMTgzODA1IgyqZngxrJb9W6wggI8q3AOzfVovziqVu4Dy0TppvINkFiKlSryUyDGkJAnMrw9s0oCvO5r4D9V09Fe9bxft9LjcVzZOV5H5aij10IeYesXM1JYvJ3Z50432d%2Fx0VlftHE3mVCWQqcK3ub5DHBSCWgFvfrCPy%2BzCPhscRcGYa6qz2NYZLcbW4l%2BOAdWHIv5KgDH7soIHpsU%2FrJ%2Bgp0sxIVG5NtofotgIDWI3CuzhjqlZwsQwT49Je2zQXWpitCVEhr%2FNJJZnTN%2BDfUCOmWgQU%2FvVnlRXV0tgMNpr1ul%2FrH%2BMqwK%2BQGpJW6qZBzVS8Z%2FRNrGUW6eBCcx8rBTUepL8RXAmuDhtuUPlxQusUYBcqgjXck0htAsl3jLwtveOZLqSlAAJ79nHYoeAoGWSwPCDnpLViGy4kTpkcpCZJ71daF28ZVNoXXbDfcaWsQvr%2BKV%2B64WKQTzmw3G430LPKulEcTw6y%2BKIzQBEUwYpzY5S5lU9iKmmQSqTBYzNGm33njLtDkQmD6LWriM%2FzsRbhZAbFFgzUGvP31t%2B4lflpjxlCyRV1EFrPujpwqP5EHEIv28O2jO8qbF5X9amDs3YutL%2BSAvxXm1YpRaXMNj437RXQ7jUkeGorPoPYF%2Fob%2B%2Be9PJAWGTXQJ9UPmergCLp%2FDD48IK9BjqkAQIA9MREtBNKWg2IdnCxft8sQNVvTsjQ4yQZyYpWCLmsgHm2tQmkvV1d57APUpUUTg9ZxxKJFtmyM9JFFGXQj6wuGltMG%2FtA2z8Q%2FN%2BLvOSyeJ3uNNxOTVl9DO0nmuRp0armqtC0HxPoIxrfaOTNBTI25P%2BeK0o7EpLiDg59sA%2BvCdXvpR7vCOLtVPh10kTxBkzBroxu9pNBPzgWv3ADYHk2WV%2F0&X-Amz-Signature=afa3aa3d7701b81957a565733e4dd603d61e876ba1d9e8ebfa88aa5ba3492646&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Data Visualization Libraries
#### 1. **Matplotlib**
- **Description:** The most well-known library for data visualization.
- **Features:** Great for making highly customizable graphs and plots.
#### 2. **Seaborn**
- **Description:** A high-level visualization library based on Matplotlib.
- **Features:** Easy to generate various plots like heat maps, time series, and violin plots.

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/733d1e42-5a53-4fd8-90c1-3d85254369a6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QMMY2DHV%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T132020Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIBOlWVfO6voRNzEAoGhirkDk1h6JJjPwm9xIaWxRcb7kAiEAm1pftytgTOhpbdwDw4mf7WMXw6fEurulpTldxTZS%2F98q%2FwMIFhAAGgw2Mzc0MjMxODM4MDUiDEbJabDSNYljS70a8CrcA8Lh07UPFByHbDB9QxLiwrqyuL29jkaApC05AUlr2ne27tEQ4D0gL5OFEwIKlN8vUPUDZhZg1lWAm%2BzGeSceu09L1em5VLt6Ru%2FIvLVh%2FU9r34Ldb7VAs7XZAJ9MsRD%2BkeMiH%2FrziPpR4pdLDMG88B6KQ7Yuuf4ZzDZNhxRysmRyGCBB%2BrYjvrwEqCZDE4o9QjiLGb%2FFs6wLwbPiFqHCk86e%2FLkcDO537ZhGfbVeIEwgS3HJh33SaBHURxctdgXtZwTvYFBOQ58o6HaUhZQO4bO0bFKXHjaNjqzt0eKKFj40cuQX9ld%2FHtbcms5zPLDQWQRkdqVFYukLBq%2BqnzapOh1icu0lH1Utu3d4dID%2Fg6bpTURDqMn6yLyoi0KT0D%2Bdk6%2BBz3yuQSnyERFN7%2BYDoN6qEEVYskGRU4vNaeoZPrOo92P4ShjASJOHClyXayMWvvzpP7i%2FzN0f3snxZDmVtTdSjv5fG0eVOxTePDDgFWro8PEzFsJj6w8Dg%2FwLoxuE3hpX5ti%2FGEl%2F7GR458Dd%2B9LYRGI3kkmlZCD%2BOB6X99OJSJR9SCYVDPqFzqrcNy8zKXIlGNDd1Jx6MB19l6hI6rBR5adJCHZYzUwqXMHY1h98NxWIMHY3Hw1Ta%2B7jMObxgr0GOqUBeUNqvIc1nvJe49Blasgxd9zFvv2qy3z%2FFdCLuyqKssKNQay0Oe6n2ejZ1FESxEW2eJ1ZPjtbilNsYyj7SotF2FHRq6jLKIIBYYMrFrf%2Ben8SemfA1fn%2BV%2BIGUGNv3C6oHVsFWTlpMgPKruLqIprgjpd5Eo8Ym7a226yICe6MZ9bHVuhfy44q55gBNXx312KmJL9abc5fBKapdHygUuY%2Bw2%2F%2FlzuP&X-Amz-Signature=92f4a27c6781c8d497e390bc67015c5466865ac574861d9b55492e7c3d3174ba&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Algorithmic Libraries
#### 1. **Scikit-learn**
- **Description:** Contains tools for statistical modeling, including regression, classification, clustering, etc.
- **Built on:** NumPy, SciPy, and Matplotlib.
#### 2. **Statsmodels**
- **Description:** A module for exploring data, estimating statistical models, and performing statistical tests.

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c62885f5-417d-4179-834f-d68f8f2bdf39/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QMMY2DHV%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T132020Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIBOlWVfO6voRNzEAoGhirkDk1h6JJjPwm9xIaWxRcb7kAiEAm1pftytgTOhpbdwDw4mf7WMXw6fEurulpTldxTZS%2F98q%2FwMIFhAAGgw2Mzc0MjMxODM4MDUiDEbJabDSNYljS70a8CrcA8Lh07UPFByHbDB9QxLiwrqyuL29jkaApC05AUlr2ne27tEQ4D0gL5OFEwIKlN8vUPUDZhZg1lWAm%2BzGeSceu09L1em5VLt6Ru%2FIvLVh%2FU9r34Ldb7VAs7XZAJ9MsRD%2BkeMiH%2FrziPpR4pdLDMG88B6KQ7Yuuf4ZzDZNhxRysmRyGCBB%2BrYjvrwEqCZDE4o9QjiLGb%2FFs6wLwbPiFqHCk86e%2FLkcDO537ZhGfbVeIEwgS3HJh33SaBHURxctdgXtZwTvYFBOQ58o6HaUhZQO4bO0bFKXHjaNjqzt0eKKFj40cuQX9ld%2FHtbcms5zPLDQWQRkdqVFYukLBq%2BqnzapOh1icu0lH1Utu3d4dID%2Fg6bpTURDqMn6yLyoi0KT0D%2Bdk6%2BBz3yuQSnyERFN7%2BYDoN6qEEVYskGRU4vNaeoZPrOo92P4ShjASJOHClyXayMWvvzpP7i%2FzN0f3snxZDmVtTdSjv5fG0eVOxTePDDgFWro8PEzFsJj6w8Dg%2FwLoxuE3hpX5ti%2FGEl%2F7GR458Dd%2B9LYRGI3kkmlZCD%2BOB6X99OJSJR9SCYVDPqFzqrcNy8zKXIlGNDd1Jx6MB19l6hI6rBR5adJCHZYzUwqXMHY1h98NxWIMHY3Hw1Ta%2B7jMObxgr0GOqUBeUNqvIc1nvJe49Blasgxd9zFvv2qy3z%2FFdCLuyqKssKNQay0Oe6n2ejZ1FESxEW2eJ1ZPjtbilNsYyj7SotF2FHRq6jLKIIBYYMrFrf%2Ben8SemfA1fn%2BV%2BIGUGNv3C6oHVsFWTlpMgPKruLqIprgjpd5Eo8Ym7a226yICe6MZ9bHVuhfy44q55gBNXx312KmJL9abc5fBKapdHygUuY%2Bw2%2F%2FlzuP&X-Amz-Signature=3c3faa91ae00b40a6b49bbfec2ebdc41d9d631c2fbb7ced35632c3d0937a89d6&X-Amz-SignedHeaders=host&x-id=GetObject)
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
