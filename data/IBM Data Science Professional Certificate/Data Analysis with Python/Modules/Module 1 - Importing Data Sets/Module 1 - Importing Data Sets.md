

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

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/997ac361-58a8-4f04-bb0f-79fea4baa761/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XZXIU2YZ%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T081923Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEAaCXVzLXdlc3QtMiJHMEUCIG6ldbiJAQn0Cpm9CYIJKK3YA8TU31Mc8%2Bg2s17aYhpUAiEAvYbi3dKZ8mW5WpVFAofdhboELVQ9v7ssnmoZTMWEvn4q%2FwMIWRAAGgw2Mzc0MjMxODM4MDUiDIbYT9WxzlVU%2BPoWSSrcA8KBZqDUaKmz5CHvKyIosmf3K03C23AaB%2B902ell2ybTPFZzINVGNzcNqByqsafrtrSiNG1YQiGHBtt6imAsqWp%2B05d6tfMOjg1y%2Fh4ZUFRjI6O7Y4%2FqMf4J0m6jeoCAIlNNchr6hFJLHvEQA1dJ%2Bpk%2Fv1dwp1jkkvgbnTNDVXxs%2FkPw54AMjs%2FNXncs1YvMmudidZMXauAFvjygAXgMO%2FKOeg%2BTmpxSjfwQtIR%2BdUsMXGiaSWe3K3BpNWa88rK40nAmQ8mfFhIyPWH2OtHLwsZKgP1DbGJFQwT%2BECZXeFCUfXbCH3S7aetjXBDAFm0xuCNnGRa43ykJveTRARV9gGU17%2BPf6Yp%2F3S1RDHnEoe%2FyrN5zl0ZaW%2FQRRvKTsdZzxM5hOkTVTf72AKs2jzxj47o9w6ZVbYPPx4uOZIX0rpYmqruXHpoS8Y9lvSXF%2FERmplXOtZcR%2FiL3aIawMyHcGOzHrflh2ZZH8%2FKAHZ%2FXxMN%2FPydEJmdebp5umaC8DXFxmYdPZNP3xgUMy8tn4cv6FXIbiKZhoDzHqyB0KBe1Aj4Fc1u%2B8m9WOE%2FooNZzY4mYxSV9ugCvIuXAImXVqgaaMaPKlx8pnJgUybNPK0P1hbXdh6hS7yic6unctY5wMIjRkb0GOqUB%2F2i3IIW%2Bfh%2B%2BpnCFz8YBkLhLZGcRXs%2FWJZCzHquh1XKoj9pyjlCY71KLPHyA3Rom%2BkprXJBBn22XG5G8%2BVYWuAKYaPAqCXM8qfHEBB2bwadu%2BaO1JuIYPk5GoM9iZqGbiIKIo%2BnahjSBzWWZWJ5JIsyJ%2Beg9hLolVMgOYnEF9o6usKJaj2UK1Fbt53aEB1yCHXYTz2Bdn0F8En49v9U11CaJcb4%2F&X-Amz-Signature=62929a7f5edf980192a9aaeacb98429b78d77700bc1f44e5f6d42027446d0a1c&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Data Visualization Libraries
#### 1. **Matplotlib**
- **Description:** The most well-known library for data visualization.
- **Features:** Great for making highly customizable graphs and plots.
#### 2. **Seaborn**
- **Description:** A high-level visualization library based on Matplotlib.
- **Features:** Easy to generate various plots like heat maps, time series, and violin plots.

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/733d1e42-5a53-4fd8-90c1-3d85254369a6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SRWA3TYI%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T081922Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEAaCXVzLXdlc3QtMiJGMEQCIB8xeNy7TRrrF8TaL6Ce4kd6QPR7OPz%2FbxrTXO5wvxvMAiAbI2g5Jc1W%2Fna34NPZcxC%2F71hske9CnKHZ4D83gfu8YCr%2FAwhYEAAaDDYzNzQyMzE4MzgwNSIMpac3VUDTxHLadhb4KtwDtHGOpN28XTUo5joYsn6h9iH9WbUMtytywLP3Ma3VZAs0%2BBkEdINyx9VnP9X9d5EENsUG06RLqD9VTz1pgEzbt0bxdeoZVcCtfr3KZdAcGpf5h7B%2FZSvDvzTRiiZrTEmI4EW%2FJu9xu%2Bjfk4y4kpOCzTlq%2B28Nc%2FsjPIuQqEaBAdqkO0XXO%2B2Td9UK4q25YDt0Ndy8XtBo1jbtWTn2aQb7Q5OP1t7kC6Tw6Sk75AH7Y%2BanSU91g1yYX%2BXizTj5MHCs%2BKrcICvhOu6amDF%2B2AtJaJIx4Nqq6H2ALYAwNLRxMo51CltFKRIRA1GX8g2eog5ZfchDgoKYbTzbpsOdNQdDGfthxtqD83Z8G%2B3UbLoyQvUPnhwfZo91RWggqqiVcbHqfv%2FDutmSSeDW7VZLU8a1oIIzq8oTakA5SKx%2Buec041CEtJiHyzbHJhTpazljQy8wjDzDJJx0MS8zes18JFO7UzyrhLaYUWOfFpuFVBdQ5vQhv20xGJ6pYXfI%2F5oNRU56301JSgx7RJXSoA%2F8egyefnxHiad0giDs%2Fb6uCtDhvCWaWXhC6pbsoYSZr5Y8t%2FQlC1%2FZztbAh6XolJty1aEbr8SKrqZc6DHB6lHAO46ZzG1HrAwAtjLIC1TxMyMw2NGRvQY6pgF6NPAhc8C8uCgaOeIGHzImBycujB7EQ3zhKz882t5VovJePJnpzWbXkUZnlvVwSXX6EV%2Fnn0bet%2BpVgP7Lo6P7WUMENbWVSdhh0JlDxDRpClVO3iuIl8Chwsw7%2B%2Fiw53iDgKWzovi8fzrx3J8DSZ5y2Y9GXnrEWdxX2JnAP6W7SPVNLGkAey%2BrBX%2FYzXpo8d0zSpk%2BFDbwOBmLmykmJyFtjYUxs7bQ&X-Amz-Signature=af0cb3593171ae092c656046395ae2b5f34b3167f3124b5c0085eb720721f489&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Algorithmic Libraries
#### 1. **Scikit-learn**
- **Description:** Contains tools for statistical modeling, including regression, classification, clustering, etc.
- **Built on:** NumPy, SciPy, and Matplotlib.
#### 2. **Statsmodels**
- **Description:** A module for exploring data, estimating statistical models, and performing statistical tests.

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c62885f5-417d-4179-834f-d68f8f2bdf39/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SRWA3TYI%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T081922Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEAaCXVzLXdlc3QtMiJGMEQCIB8xeNy7TRrrF8TaL6Ce4kd6QPR7OPz%2FbxrTXO5wvxvMAiAbI2g5Jc1W%2Fna34NPZcxC%2F71hske9CnKHZ4D83gfu8YCr%2FAwhYEAAaDDYzNzQyMzE4MzgwNSIMpac3VUDTxHLadhb4KtwDtHGOpN28XTUo5joYsn6h9iH9WbUMtytywLP3Ma3VZAs0%2BBkEdINyx9VnP9X9d5EENsUG06RLqD9VTz1pgEzbt0bxdeoZVcCtfr3KZdAcGpf5h7B%2FZSvDvzTRiiZrTEmI4EW%2FJu9xu%2Bjfk4y4kpOCzTlq%2B28Nc%2FsjPIuQqEaBAdqkO0XXO%2B2Td9UK4q25YDt0Ndy8XtBo1jbtWTn2aQb7Q5OP1t7kC6Tw6Sk75AH7Y%2BanSU91g1yYX%2BXizTj5MHCs%2BKrcICvhOu6amDF%2B2AtJaJIx4Nqq6H2ALYAwNLRxMo51CltFKRIRA1GX8g2eog5ZfchDgoKYbTzbpsOdNQdDGfthxtqD83Z8G%2B3UbLoyQvUPnhwfZo91RWggqqiVcbHqfv%2FDutmSSeDW7VZLU8a1oIIzq8oTakA5SKx%2Buec041CEtJiHyzbHJhTpazljQy8wjDzDJJx0MS8zes18JFO7UzyrhLaYUWOfFpuFVBdQ5vQhv20xGJ6pYXfI%2F5oNRU56301JSgx7RJXSoA%2F8egyefnxHiad0giDs%2Fb6uCtDhvCWaWXhC6pbsoYSZr5Y8t%2FQlC1%2FZztbAh6XolJty1aEbr8SKrqZc6DHB6lHAO46ZzG1HrAwAtjLIC1TxMyMw2NGRvQY6pgF6NPAhc8C8uCgaOeIGHzImBycujB7EQ3zhKz882t5VovJePJnpzWbXkUZnlvVwSXX6EV%2Fnn0bet%2BpVgP7Lo6P7WUMENbWVSdhh0JlDxDRpClVO3iuIl8Chwsw7%2B%2Fiw53iDgKWzovi8fzrx3J8DSZ5y2Y9GXnrEWdxX2JnAP6W7SPVNLGkAey%2BrBX%2FYzXpo8d0zSpk%2BFDbwOBmLmykmJyFtjYUxs7bQ&X-Amz-Signature=e238aca8b7513e8d86cfc64905205f5969807f0e93e9f188d3d930a6665c5f4a&X-Amz-SignedHeaders=host&x-id=GetObject)
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
