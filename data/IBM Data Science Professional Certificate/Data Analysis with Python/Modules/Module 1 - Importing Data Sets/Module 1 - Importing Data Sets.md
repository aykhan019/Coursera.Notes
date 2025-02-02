

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

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/997ac361-58a8-4f04-bb0f-79fea4baa761/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SS44AFNC%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T161640Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDyMhY7I9Dw8TD4MN28v1ZPZ%2Bt8%2FmrQtTLbKseMr1h6GQIgBGqw%2BRxU0EYg904MVxhPCtEOPmwIyliIpHRLxecV7VwqiAQI7f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFg1V5LpiLE77zV%2BCircAxf1N7M60gOBpPd6EXNzaSmJnjoRf8vBGUbykqnIT%2BarMMqX5%2FIsvUDXmW87yJX023a0uFCfRrdp%2FAStBCzTzwApuEQ5poNgargJCB8APPjnQBLM0CuefN8%2BXGFCaUJWADCmXbbU1j0uNOSxLcIFWKzA%2BlG%2FqEyHQ6DAtEMjvyfF%2BCnEl5UPJEveymtGGyoCRa5aL1lNVT2kEeynX%2B8j9tUGz%2FgfZW89Zwu7%2BulXoXGiXklAa9KoLb2rL46uor68QuB2XcchLXzOaBsZGVTrYxaNISwV699aCwefqV7rgGlHb6uHm2xSEBhwLVtYF2bsFU79OH7qXmEGcnOy8ZPwpiiBnWam5Ql5mfi6xluy7ggyeAji09KeEwivcweSUoqcm1u6z34AKW4%2BzgpEAi7bBmGkyLGiTImvjwoMamauWV7oRqiLnjUKDKErNZUVKxCCflou5HsC7esUz24eW7yzjMV31xOXdo%2BRKElZJ4x0P9HXdtJO1XTDT3BzVOL184Hxtwx76gkbUAs8nmPB%2BVPhGH2Skl9o41JkNHBZOCIHLHWFOZzO2W7nj6qmbEvMGGb7smpA98LdTf0EExh0vdPpKtwgBhnlp0fSSC2QpzTLuRsH0MqPeX5W8HXX9xDsMJPB%2FbwGOqUBFKMRK86oI%2Ba%2F9IbRWi5GDtzVWYA70MMXKWEBEk0kd6ALD5wsqlYElJohxDvXjzSNI1V5Ie3KT7fp0uPW%2FZ0qc%2BTLn5W38cDZ8nf9arrRJo26%2BPP8gN74Btr6s2robShx32JSVZIHKQknyH%2BR3aQgrpMNvEEYdLGt61E8zE4ALC59oKFMZCMgYd1v2Vs9gryur7neJsAb0EB2ghbX8PlBKCFmj4N2&X-Amz-Signature=7d9e51c0d0854769e9f7ef3f7072a5c0b359f5024bfd47944cabc22d332e9234&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Data Visualization Libraries
#### 1. **Matplotlib**
- **Description:** The most well-known library for data visualization.
- **Features:** Great for making highly customizable graphs and plots.
#### 2. **Seaborn**
- **Description:** A high-level visualization library based on Matplotlib.
- **Features:** Easy to generate various plots like heat maps, time series, and violin plots.

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/733d1e42-5a53-4fd8-90c1-3d85254369a6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466X4CPWJZ4%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T161639Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIA%2F4aIwso96zJ4IYB3MkQCkUxIMdQC7PYdkKz1Tr4L0VAiBSkwGLRvLxcOdrISNnbkG9rZXa5aYZr%2FteAuA7qGUKTSqIBAjt%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMsHzfFFDjswSuAz88KtwDIiyQbSH4Xo2s4neayo%2FbxK%2Fyf%2BRdWNYpL9oMgKBxb6XhbJ3KdYzgR1nlKK4F3ygkEydUTWduYqjzi4o%2BQpsNec3Hbp0h7ki%2Bb7YgsxjIy9mu3LfatOWlhBDd6M1aJEChRTd5GG4Ik8UyK2wua%2BBBHU%2FwUkx5CTBzyAv%2BHFEMXV1CI5P%2FovfHxXJW6W6hAcEKif9JBwB9spSoQfU3etCVLTaPj%2BSp7Dm%2BqcaJlxxyg5Mb8wGumrHkd8ONSRQTjSkuKmGsBwDS%2FghN3Rrfbjm7l7eHXGETGdEXrmZg%2F7HVjJtOQDq4SYF4FvxMEpXb0t750Ut20JMk2lxzPMA6XKQxf9aWziOSAKDk8EAjK8MAiCnqN1DOiS5smeVUinD4iOofyPe9GU8ZMCsxIfwDhQ2BFdnxhBvQT2cPpPYRYoB%2BlVyWD1zySc81M7NBfEw%2FNQo1BEXAQLgHzVOz45rtouYGnNGlFFvPcP4YSSZNOCtF2Dk1JtmNsplHoGXuznLYJEpdLcWFvWSmqDtwUofHIh8Wde0fLze061HajXhp2OUMcpWNTGf%2BV4fippyT3h0SONlpaGlkT78fZVqeTeqN0OJdkpsPVfqgtDMMeaQtm7ON3qPj%2Bqi2xbWnzPkcBcww87r9vAY6pgGqMviZQmzyQaoyKOK%2Fl%2FkJ41xnpv0HbJQbNDnID6IIYyz1Odnt%2Fg5wV5FsuiVuuZZ25ild%2FHg3YukmXTuqlK8D2d%2FdeFegnM1%2B1UGLf2EbYNOKaS7LdsnC17U0XngDOMtmjRtFMDjL49jpKBrDLE3nsoHQ%2F%2FmsntaCEfsN7WEY%2Fig8jMZxvwTnseCFaBjiAJpQQhSnjOveg80d9b0DGKEFoM7Cde1w&X-Amz-Signature=7656b1153247f4a4e1a48f79900da4f5487cca5227dc6ae067cc5a6f22062483&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Algorithmic Libraries
#### 1. **Scikit-learn**
- **Description:** Contains tools for statistical modeling, including regression, classification, clustering, etc.
- **Built on:** NumPy, SciPy, and Matplotlib.
#### 2. **Statsmodels**
- **Description:** A module for exploring data, estimating statistical models, and performing statistical tests.

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c62885f5-417d-4179-834f-d68f8f2bdf39/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466X4CPWJZ4%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T161639Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIA%2F4aIwso96zJ4IYB3MkQCkUxIMdQC7PYdkKz1Tr4L0VAiBSkwGLRvLxcOdrISNnbkG9rZXa5aYZr%2FteAuA7qGUKTSqIBAjt%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMsHzfFFDjswSuAz88KtwDIiyQbSH4Xo2s4neayo%2FbxK%2Fyf%2BRdWNYpL9oMgKBxb6XhbJ3KdYzgR1nlKK4F3ygkEydUTWduYqjzi4o%2BQpsNec3Hbp0h7ki%2Bb7YgsxjIy9mu3LfatOWlhBDd6M1aJEChRTd5GG4Ik8UyK2wua%2BBBHU%2FwUkx5CTBzyAv%2BHFEMXV1CI5P%2FovfHxXJW6W6hAcEKif9JBwB9spSoQfU3etCVLTaPj%2BSp7Dm%2BqcaJlxxyg5Mb8wGumrHkd8ONSRQTjSkuKmGsBwDS%2FghN3Rrfbjm7l7eHXGETGdEXrmZg%2F7HVjJtOQDq4SYF4FvxMEpXb0t750Ut20JMk2lxzPMA6XKQxf9aWziOSAKDk8EAjK8MAiCnqN1DOiS5smeVUinD4iOofyPe9GU8ZMCsxIfwDhQ2BFdnxhBvQT2cPpPYRYoB%2BlVyWD1zySc81M7NBfEw%2FNQo1BEXAQLgHzVOz45rtouYGnNGlFFvPcP4YSSZNOCtF2Dk1JtmNsplHoGXuznLYJEpdLcWFvWSmqDtwUofHIh8Wde0fLze061HajXhp2OUMcpWNTGf%2BV4fippyT3h0SONlpaGlkT78fZVqeTeqN0OJdkpsPVfqgtDMMeaQtm7ON3qPj%2Bqi2xbWnzPkcBcww87r9vAY6pgGqMviZQmzyQaoyKOK%2Fl%2FkJ41xnpv0HbJQbNDnID6IIYyz1Odnt%2Fg5wV5FsuiVuuZZ25ild%2FHg3YukmXTuqlK8D2d%2FdeFegnM1%2B1UGLf2EbYNOKaS7LdsnC17U0XngDOMtmjRtFMDjL49jpKBrDLE3nsoHQ%2F%2FmsntaCEfsN7WEY%2Fig8jMZxvwTnseCFaBjiAJpQQhSnjOveg80d9b0DGKEFoM7Cde1w&X-Amz-Signature=7e01999d5aa00de65c3635dce574bfc4374b790daedd189997a033b326fa3236&X-Amz-SignedHeaders=host&x-id=GetObject)
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
