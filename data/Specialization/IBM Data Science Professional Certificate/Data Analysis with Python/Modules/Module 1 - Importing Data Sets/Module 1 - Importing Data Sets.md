

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

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/997ac361-58a8-4f04-bb0f-79fea4baa761/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665XT3FBEL%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T122857Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGd0dLJQ2q0Z9Jag9N3oPBTTjdOQXYuCjtRcdw9YwuElAiEAs4xaab9shzYjOm5McWFitEA5yN3d18fnXygl9cmKV%2F0qiAQIpv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNPJJns%2F9wOI71iM8yrcAwudQFtNG0jW%2FStJCR9E6g3eoGAP7KJMYfJMmUBcBXjnsOLoieOa8ESS9vL%2BAPhgjFtkC74U53irOzHOn2z8C3y9qWILEOmdrOFNsiQbWQC9RueN1M9Oxvx%2F%2FKkEl1%2BwWRUrk%2B7WzAk6iJwlAmDeOHmMvbzdr5HCzqJC%2BFSjLGrECY7vAYARnZKxuo%2FSi%2BGdso5xfoQByBRvN0il8%2ByiTcwgeeLIePHQgWKJRycUYCdF%2B9QgvUcy0f4jhDuk7tHhWmATq5ijQ4nHuLQKciWjZQ2yesaNdCqFqVK2oypUo91nJ7ZvL0aUkepXz1cCT47KMJrUMsr7visFY6kk4Ox%2Bs4vB0j7wtXOVKbTZLo9ystQ6EhEsE%2F5ce8cbjXbxWRLEGmXZi3p34yvePYg2J3QZ6i%2Buq4ywCL7c2ex3Qz3ADqyotsQlfZK1W%2FULzdhweniMi73NW5YefEpTR0NJqkmPi2r6dlJEpg0iBijf78moU5cFzy7Xj7%2FYpb%2FjrdaBAR3xnyohONAnB9zpPwPXIz4U9GB%2F09ao61FK3BPH0KrbtFHEXOYxt4xLzW2054CEgnFJtnQVat5TSAPsglT98G4rI3ZKzDI3GrisEyWrqzgGBjZKQVT86ZpS8xqXtEIBMLze7bwGOqUBRmpm5j2KKZoyy5ldzHuTQa6yp45T8tNF8HRGBI33taysfGpeQwoiUqbcgDFRemfazQ2r2HJwM9S52BQ8WHq5gSjcnU%2BEo%2BgvAMKHCrjImfn8IuYXGnjibOQpUshp%2BWjThOebnyNw%2BNqBVpKSoFhofUVWkVpzz61Dpt1xYdXHwlaNRrEaTAHBsZxxkvgg5nrukUq0AP1ZyyUDfVh%2FuwvIjw8STzV0&X-Amz-Signature=f4272f22c1423253de8ce9895d9b7f76cb8139d081f45bf000ec9cdac77e77e7&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Data Visualization Libraries
#### 1. **Matplotlib**
- **Description:** The most well-known library for data visualization.
- **Features:** Great for making highly customizable graphs and plots.
#### 2. **Seaborn**
- **Description:** A high-level visualization library based on Matplotlib.
- **Features:** Easy to generate various plots like heat maps, time series, and violin plots.

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/733d1e42-5a53-4fd8-90c1-3d85254369a6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QK4576NQ%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T122856Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBEx9ddDcg5s2%2F%2FMXj9cNyZjxQeKDhwruW6aEy72t9qaAiAxsZebFc7ZGUipMlxw8R0iB8rLYf0I0YgBflXxuXXtSyqIBAim%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMTPrSWCaYCPTZ0FTmKtwDapKT9lPD0GUVNVNBdmwZSYhjYCd7NJrMlTaJ2C9MYBRZfkN62AyGNw4kPaGcLnKP3xyiY680E8bCqJVPBgcdDuAcmFch1VbW9VXHpnSS7LSHbEKB%2BD%2Fg4MN4DoPsOJ2BPsvVkZo9RaQqF7W%2FPf42n57eJyBQMsMXfNCJC2CyHvWU802E9oE%2BuzfjYw2dx8EwbWDv2yCDXuSIVl7hYaZMayjTAc%2BVujE1Kz2S4EyLQwjvjajkaRiDu%2FmQgSO2IritRPPYmvDwk1o9T04TDHukrMmYmH0yfj%2FcTy9e2bqeGL21HNYD2SiUzKb3tEC7VW6yP703SPEG0v67LqK7P86QDbWsNA%2BfNheK2Q7WH9g%2BwvDrEsB8o0PxqhjWvv3oYgU0fLqjYygSbDuN%2BjoCiZzxSlmsF1TK7jIFfRQe8bjrye7O7eLg0m3xb8vsZ%2B0Gd13IivnNQejvA%2BNtSlvykBUD3X6pqvKDkaZ8wFmzlO3kVnFF1KdTKE9WIPc43N4Pfa8Y8mVdvfcu3R2oKm%2Bs8nHsy9%2BNfa%2F35b6dPJO979hiJab6cVMVdbQR0Csb%2BYas4dXqfKcAma%2BLXhTNt12YRMncpYDubq%2F8W9LLphaQXNbC2AlnbK8DiUB%2FLQv%2FlZowo9%2FtvAY6pgFHs30r%2Fzk4shlrnevDbDfszey1ybksQFjqU%2FihaoCTPz%2B1LIbFE1R9A2kx4owGCaaLzhNB62gcWxoWHAN%2BK6vHHlArAFn3uDfH2A8dWE5LHA%2FO3D1YjQ44uTe3CV3lJ%2FPV7dsf6kk35l8TKQdonsdUp%2B8vVY9pP9tYCA8QzqL4bsGP3rMEHBGctNNmbNlgjzm5sXvOTc0XvW8eIX3NzBIbEpCbfl28&X-Amz-Signature=79bebfe7bcf337c179ffc3807669468b8737c4a3dd950fe5ce1fcb861c183621&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Algorithmic Libraries
#### 1. **Scikit-learn**
- **Description:** Contains tools for statistical modeling, including regression, classification, clustering, etc.
- **Built on:** NumPy, SciPy, and Matplotlib.
#### 2. **Statsmodels**
- **Description:** A module for exploring data, estimating statistical models, and performing statistical tests.

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c62885f5-417d-4179-834f-d68f8f2bdf39/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QK4576NQ%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T122856Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBEx9ddDcg5s2%2F%2FMXj9cNyZjxQeKDhwruW6aEy72t9qaAiAxsZebFc7ZGUipMlxw8R0iB8rLYf0I0YgBflXxuXXtSyqIBAim%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMTPrSWCaYCPTZ0FTmKtwDapKT9lPD0GUVNVNBdmwZSYhjYCd7NJrMlTaJ2C9MYBRZfkN62AyGNw4kPaGcLnKP3xyiY680E8bCqJVPBgcdDuAcmFch1VbW9VXHpnSS7LSHbEKB%2BD%2Fg4MN4DoPsOJ2BPsvVkZo9RaQqF7W%2FPf42n57eJyBQMsMXfNCJC2CyHvWU802E9oE%2BuzfjYw2dx8EwbWDv2yCDXuSIVl7hYaZMayjTAc%2BVujE1Kz2S4EyLQwjvjajkaRiDu%2FmQgSO2IritRPPYmvDwk1o9T04TDHukrMmYmH0yfj%2FcTy9e2bqeGL21HNYD2SiUzKb3tEC7VW6yP703SPEG0v67LqK7P86QDbWsNA%2BfNheK2Q7WH9g%2BwvDrEsB8o0PxqhjWvv3oYgU0fLqjYygSbDuN%2BjoCiZzxSlmsF1TK7jIFfRQe8bjrye7O7eLg0m3xb8vsZ%2B0Gd13IivnNQejvA%2BNtSlvykBUD3X6pqvKDkaZ8wFmzlO3kVnFF1KdTKE9WIPc43N4Pfa8Y8mVdvfcu3R2oKm%2Bs8nHsy9%2BNfa%2F35b6dPJO979hiJab6cVMVdbQR0Csb%2BYas4dXqfKcAma%2BLXhTNt12YRMncpYDubq%2F8W9LLphaQXNbC2AlnbK8DiUB%2FLQv%2FlZowo9%2FtvAY6pgFHs30r%2Fzk4shlrnevDbDfszey1ybksQFjqU%2FihaoCTPz%2B1LIbFE1R9A2kx4owGCaaLzhNB62gcWxoWHAN%2BK6vHHlArAFn3uDfH2A8dWE5LHA%2FO3D1YjQ44uTe3CV3lJ%2FPV7dsf6kk35l8TKQdonsdUp%2B8vVY9pP9tYCA8QzqL4bsGP3rMEHBGctNNmbNlgjzm5sXvOTc0XvW8eIX3NzBIbEpCbfl28&X-Amz-Signature=2eb2a9cdf5ad3b884be951aaef6d569ec1ee54abee735bfb4e21a78746ca1474&X-Amz-SignedHeaders=host&x-id=GetObject)
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
