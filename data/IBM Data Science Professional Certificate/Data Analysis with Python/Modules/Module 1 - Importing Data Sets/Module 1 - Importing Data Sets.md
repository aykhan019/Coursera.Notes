

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

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/997ac361-58a8-4f04-bb0f-79fea4baa761/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TPWNKDKN%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T062049Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA0aCXVzLXdlc3QtMiJGMEQCIB3HdADn%2BFjYkViwXpLFssCNetrI5r%2BnIxe2jgJN3S%2ByAiAwP6MxkqvKOA%2BS7i3FiKXxKxhkaC7nO57wiF3%2FoeTJiCr%2FAwgmEAAaDDYzNzQyMzE4MzgwNSIMMEL7uoFO1IB%2FHrx3KtwDceqFHf5kS9kyNzDN3vHaTMUqHpSVBzPJvD8IUa%2BE2N%2Br5WucYWTae9UAFj%2FhqfN4m4Euj4r816dh23act%2B7CCUpI7tYs7NBp3IptpWQDS%2BZqd1g6pUs7aAV61PJtjbHdQbLz9WI%2BXLt9soTBTm%2FWRBgnLiAb7yRZ1mv6kcg70p4s2fnJhVNjCjlGMDnVX2QhgSNrdjp0hk3k0RndmUkApOURpBjq2WC0CE3ID1DAuYFX6Tan5gTgZ54odhnzHdhowhf0fqlC82TNenhJEwK6ePPtUVenwm8Y%2Flycl4lYAJTunOjBaayRyOx9xHeJSUJ243NqY0N%2BtPXj6w9rSIdQ4eIJDSbuSCDbWkJJVyvBDR6lXnj1IqlN5iGhHVgcSPL%2BB%2FjRvWfZfukqx3VujjW7H5dEnvRrEtpwbsYmAjUskXxT2uob3iw4yXB1iUA3im7Jy5DvYAegsu36AbhNVtwfcOzocXTf57yg%2Fu%2B9%2BE8QxYyVuNSPJeu8OBpRxJYzZ%2BcvNKe4S6W4sXHWIUefZn4WPO4rURrxzERA%2BA20jqm0tqEHmw3jFhiZKd45YYQ8aboyp6S4hM69XUt3Ep4%2BMtQHXB18s2tWopnqsaP%2BNc24kgGJOJgSQrygcKuIru0w3L6GvQY6pgFqoo4FUsRQS0eyr3d%2Bn9gex5YgHsuK1JL04lZXeyxWZ98%2BHq5OcxsI7e1YnQMXmogFdBBwzLqnFmSetTt63XU48hvhv9oRI4JUiy8cfaPSlU8wXcfcvHlgLdpFyRjHkxoISub4V2iycFAl7kG90eWSTGdylHjxn6xWtuUWJcMUx7OjgTKQ5wbM6xGDvkvZzYj5qj5TF7sPs5h6bK%2BmGLnmRjEj2QID&X-Amz-Signature=ed358a049e87ef2d70c3806089426a8d7c3a9e65cd05c72df666b186ab7c183b&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Data Visualization Libraries
#### 1. **Matplotlib**
- **Description:** The most well-known library for data visualization.
- **Features:** Great for making highly customizable graphs and plots.
#### 2. **Seaborn**
- **Description:** A high-level visualization library based on Matplotlib.
- **Features:** Easy to generate various plots like heat maps, time series, and violin plots.

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/733d1e42-5a53-4fd8-90c1-3d85254369a6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RMK4KVMN%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T062048Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA0aCXVzLXdlc3QtMiJHMEUCICv6k0%2F4Rt322Ewo06Fj3UNx%2BTrJMAVd8xZkzf8N3%2BsQAiEA1%2FJhaszxPplj7gxGq8Y4QPjS7T5K7q3%2FtfKxG09m%2Bo8q%2FwMIJhAAGgw2Mzc0MjMxODM4MDUiDLrVRuHvmbP%2BUhRdKSrcA0LoHp%2B8Wdn%2FJObcUjJkZk4XsooJq%2Fyddj9MMzPO73KqkjTFaouY5EqoAVOUDnIRMJiab4%2Flrpr2cSNeNIRKbxdaxjBete1gY8KB9NU4%2BePaMEQCwGvpiEmnRdjWPa3XhjZs%2FYp942wt%2FYfYHDCZydWGZtFSqtwh8mv4PPTU1pfcsWe31SmsJxq6V%2BNQbYIowgS%2BpgCZQl%2BLWAFiw%2F6uX0QR36EmwEossvlnRSVTXKOXKW45ZouIAIThe2Hgqp1HABNYkSpqf7TgXRZVj%2FCp6XhuaSsV4VPj6mDOSAwWx%2BlzamtpmbOBRmVWJsfzWmW7ZRYLqd1TtukuHwH%2BBUwR8e%2FAQhhBGxwGTFj%2BrCLWlqZMLVlOlb32jLXc2nOjJPdq1ZC6k4J7wdmX7lmbWuhD79hXkmUaL2uZ0Y%2BXNwzldwI7qK0NlBQzPpVArrOfjydPKIr01SvdrQ2GP2eAhzqO8gfD22IQCpubh%2BLdRXGvVskXdd2XDMVvNfOg%2FO93gqWj2nq7EVE3NW2Wml4ssbAWTA%2FYl3U4fssfQFejU9%2BZO69%2FDwZ1y8D5FqtNCf%2Fmi3TX%2BJEcIc9m577mGXY0jOZxj8dk7bOqcgyFuLZdkjB9NfSQ1SJ2RhnkCQtPk%2BrPMPC%2Bhr0GOqUBLwXEBZdhx6r0xOF3T88w%2FcpWhiZcCOvtpsEQxn6PuJpYmZq5f%2FX5N2a5q%2F3HhpmpPPgESNPaoHwfJBSS%2F0WkfDWJnjY0HnFxru5zCSLM%2F%2BAzOFRebS%2BPDXp2x8Tuxi9HqjYmQCxdbZ08RNmjJZxHIp74IHVDxWBaa04PfamPa8UBngAl%2BJEK3h1v58lkDXO3UhGuvQsnQLrPxJqJden71gX%2BGif3&X-Amz-Signature=5b37d9e87527e0fe5b3a6136a3aae0e541fd5a5d90ac57b2c5e4ef145f62144c&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Algorithmic Libraries
#### 1. **Scikit-learn**
- **Description:** Contains tools for statistical modeling, including regression, classification, clustering, etc.
- **Built on:** NumPy, SciPy, and Matplotlib.
#### 2. **Statsmodels**
- **Description:** A module for exploring data, estimating statistical models, and performing statistical tests.

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c62885f5-417d-4179-834f-d68f8f2bdf39/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RMK4KVMN%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T062048Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA0aCXVzLXdlc3QtMiJHMEUCICv6k0%2F4Rt322Ewo06Fj3UNx%2BTrJMAVd8xZkzf8N3%2BsQAiEA1%2FJhaszxPplj7gxGq8Y4QPjS7T5K7q3%2FtfKxG09m%2Bo8q%2FwMIJhAAGgw2Mzc0MjMxODM4MDUiDLrVRuHvmbP%2BUhRdKSrcA0LoHp%2B8Wdn%2FJObcUjJkZk4XsooJq%2Fyddj9MMzPO73KqkjTFaouY5EqoAVOUDnIRMJiab4%2Flrpr2cSNeNIRKbxdaxjBete1gY8KB9NU4%2BePaMEQCwGvpiEmnRdjWPa3XhjZs%2FYp942wt%2FYfYHDCZydWGZtFSqtwh8mv4PPTU1pfcsWe31SmsJxq6V%2BNQbYIowgS%2BpgCZQl%2BLWAFiw%2F6uX0QR36EmwEossvlnRSVTXKOXKW45ZouIAIThe2Hgqp1HABNYkSpqf7TgXRZVj%2FCp6XhuaSsV4VPj6mDOSAwWx%2BlzamtpmbOBRmVWJsfzWmW7ZRYLqd1TtukuHwH%2BBUwR8e%2FAQhhBGxwGTFj%2BrCLWlqZMLVlOlb32jLXc2nOjJPdq1ZC6k4J7wdmX7lmbWuhD79hXkmUaL2uZ0Y%2BXNwzldwI7qK0NlBQzPpVArrOfjydPKIr01SvdrQ2GP2eAhzqO8gfD22IQCpubh%2BLdRXGvVskXdd2XDMVvNfOg%2FO93gqWj2nq7EVE3NW2Wml4ssbAWTA%2FYl3U4fssfQFejU9%2BZO69%2FDwZ1y8D5FqtNCf%2Fmi3TX%2BJEcIc9m577mGXY0jOZxj8dk7bOqcgyFuLZdkjB9NfSQ1SJ2RhnkCQtPk%2BrPMPC%2Bhr0GOqUBLwXEBZdhx6r0xOF3T88w%2FcpWhiZcCOvtpsEQxn6PuJpYmZq5f%2FX5N2a5q%2F3HhpmpPPgESNPaoHwfJBSS%2F0WkfDWJnjY0HnFxru5zCSLM%2F%2BAzOFRebS%2BPDXp2x8Tuxi9HqjYmQCxdbZ08RNmjJZxHIp74IHVDxWBaa04PfamPa8UBngAl%2BJEK3h1v58lkDXO3UhGuvQsnQLrPxJqJden71gX%2BGif3&X-Amz-Signature=dfcb3b1eecdefdad2fc719e7086efd34c52ee988b98cd8effe97b30fea67c6b3&X-Amz-SignedHeaders=host&x-id=GetObject)
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
