

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

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/997ac361-58a8-4f04-bb0f-79fea4baa761/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VSCADCCD%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T041748Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDwaCXVzLXdlc3QtMiJHMEUCIQD5TMSLtDI2Vf0L7wLm7GzdUUdNbLg2bn8DpnD9HDNEegIgO%2FRGkbZ1Y4dek0hpVR6kzCMWubMLfiYezX5X5QenGnUq%2FwMIVRAAGgw2Mzc0MjMxODM4MDUiDFfcCfgH64KuVYRjEyrcA9ewzRg27bbkMFxmYBWn8XW%2Bkqykx4FvA9a%2FpEDmnYn87iBBZ%2BYlrDO5lFIvxTnyNISi9ljgwlzi6bxl1VKiP%2FhKfd%2FhEfvHYktM2OrSWo4SJUAbRe4G7V7VqM%2BAr71hDPxGrvS3py9UR6gXSJy4CL3ZH35gBqAvOWr1keAFobrfSOnD3hphfaGE3f6RMWAZIxB1ZIzs0%2B2KpfB7LKFqjf7RlyJAd7Wj0hwIOyQ0IOq2B%2BuwjyM7jnPbPRHRIZSnOKbqkzhDoKcYeLiLqh9iz5Rjygp2vfK753qZmQtOriGBwCi63%2FEg5SctyLMFXGIU00ZXdR4%2BuO86fcn%2FhTGReCaUQm%2FyLVQSgOGg85papELng0z3QeRe5SSAZJN1s5bE%2FQgb5Aut9kz8uNvZ%2F3KCi%2FOVbniC22kjjXi6UsdDSnP9q%2FJv7SGUPKOdJlji8sVlQaooAC9ky9Y3rwpXhLcM8esstIh23Ev%2FmRIyfvGnQ%2BlVxpjoWmMCxtilgGT1aiTZtdCYzqPoBUhQvswldrv3UZJOo7u8TLwtQVoWlMPnwoPNk%2BNRELkO3WhTbTEb8WAJ8uC1me37dUMpj0BwA3qmMzMjn6H94eCINHZVqcrp0FcTH5AQpntLaVDimyaGMMnfkL0GOqUBqNVL7uLtqSIgpQGNib4HV37Dt2xoo%2FAcXAXOQlfcqd6iat91gVKb4EBtCltK9vabqbkXlPtic%2FlTjHhorEg0cWPNOS0RsfKVmwrMJCUwg3J6dXk55VBUNVFhqmd3fFaEHJqBZp9W6myqjVY49Y%2Bbn8xbofuVdkruKNqk2jjpb%2BcUFlWgxBNRDVX8tMRqGxS3K0eSgtIAKGMD2AlsrRjZfGBs8JkS&X-Amz-Signature=f13fd85f89de8931bea357e46e49673bf58684ca06fc7adbfd42e88ac7bed41c&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Data Visualization Libraries
#### 1. **Matplotlib**
- **Description:** The most well-known library for data visualization.
- **Features:** Great for making highly customizable graphs and plots.
#### 2. **Seaborn**
- **Description:** A high-level visualization library based on Matplotlib.
- **Features:** Easy to generate various plots like heat maps, time series, and violin plots.

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/733d1e42-5a53-4fd8-90c1-3d85254369a6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466S7SMP35K%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T041747Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDwaCXVzLXdlc3QtMiJGMEQCIGVr2l1Fv3QZZ0xutE1VpAdkqxQj%2BvJ%2FPNl%2F0txJd6UlAiBCF2q0Oba7dcU92fKRbhVgz3uDt8oRAePtCVz6JwnAdSr%2FAwhVEAAaDDYzNzQyMzE4MzgwNSIMW02kHYYPSp5y56cTKtwDe0mRXSsSP9Ar7DGmxSor6Xza%2FFia0XmfjcP%2F9efeg5etovpSGUF1CelX0O%2BumKUPzfwlxZ83M4QpJ%2BBJ5zIVgMUQGtRknivEUdnH3JyhnMQdDLHF3QXoDNcMSW0UK8W8nYSXoHbWSSRE9%2BPcKDj2Pn5XIEtYT%2FE8LIKKyphtTBXsMeV1ptp2txUv%2B7kmzFzI4U%2FQPOf7Tz7%2B9SIc%2B8%2BzXOt9ieeIp2IkhPfP7P6B9E5NXtuHemMBzMO%2BrZcmv78TEFooX%2FX6a9ScZotNzKdhOBaeJqtlaA%2F25%2FycWqgTZWZs%2FT7lGBunKBuS4sGUB0rlWAcEIExz1LLQGpYdCapMkKotwSPeujAieoEdW7cu0GjQkNhcRwhlSbP8fduQtlInDsPQNnXDPOCL36pYFVkIHLq8bxpef4OJNJTsAKWmxDL7ipHCo6V59OQ%2Bx0HXcs9HXi2tcs8E790%2FrqOLZ0gKUU5HG%2FOyur7croH742moISCaW%2FjBW%2Ba7hXjtc1%2F8BZVmWlWa1cx6cc%2Bgtpeox1Up591wAFt7eaZ1lQsiA7EevsHyFJLtVkhFlvvPRQYjiSO4QaNdCUWbJgW%2FnFUiuNPId0MXwEa4cX5RXU%2FfKlHjYzrM0BwHH1AbqXXfXWww09%2BQvQY6pgFbivrrwJ282eMfSuPNSxXGxfvZ47US%2F2VVF2kMeGWsoNPLRYV8mh9OigeRO0Y5HcBA4rtZIJk6QBEtw3y7ZTsZRvK%2Bu3eiRDlU0kBFt%2FPY9bPB4h%2B9aKuwDn1w1ppLZqO0yzsSvGkT2rUhneZwI%2FdR%2Fa0WFOSPvvQfcO31M7DAT7Q7WtItWc1z4WN4z%2F%2Bv5iAwPFE9Q35IBOiEPU3tGzvr2%2BdbGo7Z&X-Amz-Signature=84d46200d3a97890d3ddb9292ca1a1eac0a58bf1b28594b9b42ed9bfda1dd1fc&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Algorithmic Libraries
#### 1. **Scikit-learn**
- **Description:** Contains tools for statistical modeling, including regression, classification, clustering, etc.
- **Built on:** NumPy, SciPy, and Matplotlib.
#### 2. **Statsmodels**
- **Description:** A module for exploring data, estimating statistical models, and performing statistical tests.

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c62885f5-417d-4179-834f-d68f8f2bdf39/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466S7SMP35K%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T041747Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDwaCXVzLXdlc3QtMiJGMEQCIGVr2l1Fv3QZZ0xutE1VpAdkqxQj%2BvJ%2FPNl%2F0txJd6UlAiBCF2q0Oba7dcU92fKRbhVgz3uDt8oRAePtCVz6JwnAdSr%2FAwhVEAAaDDYzNzQyMzE4MzgwNSIMW02kHYYPSp5y56cTKtwDe0mRXSsSP9Ar7DGmxSor6Xza%2FFia0XmfjcP%2F9efeg5etovpSGUF1CelX0O%2BumKUPzfwlxZ83M4QpJ%2BBJ5zIVgMUQGtRknivEUdnH3JyhnMQdDLHF3QXoDNcMSW0UK8W8nYSXoHbWSSRE9%2BPcKDj2Pn5XIEtYT%2FE8LIKKyphtTBXsMeV1ptp2txUv%2B7kmzFzI4U%2FQPOf7Tz7%2B9SIc%2B8%2BzXOt9ieeIp2IkhPfP7P6B9E5NXtuHemMBzMO%2BrZcmv78TEFooX%2FX6a9ScZotNzKdhOBaeJqtlaA%2F25%2FycWqgTZWZs%2FT7lGBunKBuS4sGUB0rlWAcEIExz1LLQGpYdCapMkKotwSPeujAieoEdW7cu0GjQkNhcRwhlSbP8fduQtlInDsPQNnXDPOCL36pYFVkIHLq8bxpef4OJNJTsAKWmxDL7ipHCo6V59OQ%2Bx0HXcs9HXi2tcs8E790%2FrqOLZ0gKUU5HG%2FOyur7croH742moISCaW%2FjBW%2Ba7hXjtc1%2F8BZVmWlWa1cx6cc%2Bgtpeox1Up591wAFt7eaZ1lQsiA7EevsHyFJLtVkhFlvvPRQYjiSO4QaNdCUWbJgW%2FnFUiuNPId0MXwEa4cX5RXU%2FfKlHjYzrM0BwHH1AbqXXfXWww09%2BQvQY6pgFbivrrwJ282eMfSuPNSxXGxfvZ47US%2F2VVF2kMeGWsoNPLRYV8mh9OigeRO0Y5HcBA4rtZIJk6QBEtw3y7ZTsZRvK%2Bu3eiRDlU0kBFt%2FPY9bPB4h%2B9aKuwDn1w1ppLZqO0yzsSvGkT2rUhneZwI%2FdR%2Fa0WFOSPvvQfcO31M7DAT7Q7WtItWc1z4WN4z%2F%2Bv5iAwPFE9Q35IBOiEPU3tGzvr2%2BdbGo7Z&X-Amz-Signature=d408ffffeeacc5e1fda616a77439001c6b844a8bcb6a36ac83872a5c814fb7e9&X-Amz-SignedHeaders=host&x-id=GetObject)
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
