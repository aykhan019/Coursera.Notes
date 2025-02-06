

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

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/997ac361-58a8-4f04-bb0f-79fea4baa761/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UXZCB6YT%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T231613Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEE8aCXVzLXdlc3QtMiJGMEQCIDh4ADlPJEcvHo777HLuYobA%2BzZfUHaP0YkWcsJHhMhIAiBMTdcgDlCJu0Y5llY1Ytdey6jebmUu7b6xQ4qy9ElJjSr%2FAwhoEAAaDDYzNzQyMzE4MzgwNSIMfylC5gNGKk7dEuJSKtwDoHLXckhcpMtidASX%2B8IqycAeDg1naRRHpl9e0%2F0%2BMSIdBG%2BHGa3A%2Bpbro8uHBleogmRbEX8MVsNo6qHgNISu5MiNY%2BXMtD9zKI%2Bs8g0byvr9JkNCCyNUPhO0rQdHIsxVpeiAXnADrqQ4A28zJdlBhFstdWaLnfmR%2FRJxk%2FfTQllOEn0VAh8SG%2BhfdzRzx8M80jcoAkqV4Upw8ZLMiCd27vTPbqiRjhGViZ4J06HzIxoktNdZNtYXKzV%2FnTJTMFju2dcNA9HaPgFHm059wI3pVCx5c%2FgkP8dSC4a9ppWxgffx%2BApT3daIxwrYcKJ8kX%2FFjkJz6UTj4a7qhbHF%2BVWhDbIYPlESBRPS%2FnURWvdnqZiiTjMYdu3jG%2BgHnRFt1%2BwT2Rz1y2N%2Fd%2B6DAgLS80r7iRgS5TK0heoa8qEiuJR8eb15oUCFknoKRhHZKZfr4uy5WEK07cQ6nk2Ce9lR6zw2Bs6MX6MzwYzkI8Jm67KNIz8rLEGv%2FwREgNbohEpjn5%2BqxbD5OVwErj4aES6ZN6Na5S5ZOS7gqpEx%2BC7HByLQkTb9iSBGLSKjMKI4QcFcRRg3twL20Mrj7q%2F9wece5qw1eVsrQPRsQZw7J%2F8YOEMyR9keI%2FLG0OjhXiwgb0cw3%2F2UvQY6pgEi1fnPzY8ZsNfjhIhy5WwEml93wyIwqoH5q%2FQVN1xo2lkmn1r0gRwhrk1CkxEmc3tJy%2BpMH4QyHUiHuFQXA22xGf5Twxar98y2AwfqbhhRYyDOWRA274wAYexucFDbgAKhIdWHWKNZtRaMIr%2B%2F0x%2F4DheN2OH7M%2Fe1Z9wZBzNvQ4Ddwuow9Dw2X02YRZc9T%2F2INphPYdLizi8CS%2B1daJUYiZH8vmvZ&X-Amz-Signature=3554a16cafb1521a9b4339fb32121d13fb50e0ea04089dd3988827942f1ae8a7&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Data Visualization Libraries
#### 1. **Matplotlib**
- **Description:** The most well-known library for data visualization.
- **Features:** Great for making highly customizable graphs and plots.
#### 2. **Seaborn**
- **Description:** A high-level visualization library based on Matplotlib.
- **Features:** Easy to generate various plots like heat maps, time series, and violin plots.

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/733d1e42-5a53-4fd8-90c1-3d85254369a6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665E25HJQ3%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T231608Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEE8aCXVzLXdlc3QtMiJHMEUCIC2RseCqYu%2BJKeU3Z96aOsqGHQSdhSIztgAhJcDIzdTjAiEA6qp8QjJndONfpXZ6MHgu4D2D%2FlNb8JV2dJpnQ2eOsWsq%2FwMIaBAAGgw2Mzc0MjMxODM4MDUiDA%2FqvEM9kNCJRCp2UircA6i4SVBRNf%2FZE%2BzmIBgys5Ocfvy2R3tKkYJrNcW1WyUGoZEB92plRU4yIz6CM1hgKQQ%2FRp3wDoo4uym12HnxTGr1l4koORR0xTJnBJFTaoEurol2XPk2GA0emlFaITC8JfmDci440lgIdbrTnz3wcBLAoqI8rh7cvBnhvnDUF1P607t%2B9vnPKxNBm94ISZQcFg3RD46MinAOh9dvTAE2PXOihMMs7KWJgQfKTlyeFflzYXcvn2FQjy3u2pI7lcwCMpv%2Fno4ZYumV%2FdMROzyX%2Fx%2F4lTRi4XyYDZrQUfQzPjhdrOWzg3O8Kp7vMw3wWR8CwfXY1cxoRjIH3Iapb1NcOyjtXaUiV4AGIwzLtWpFwGi81aqilczwJGpm3B0AaIOuXg5bMxDrL0K2azghNBxzY9Sq8LgT8oViXzHP%2F%2BXlEaYTaoJhuNSk3JZ84D5OwMqZZCWBKGqlK7HpX%2Btl26nQ647XtjM1zhyr7asrXUrR0zQkDi5vj1sXVCT2zME9PC2DN7tLLNZjf%2Fa%2FfYacurJa7vaCt6fmAZJaczWo9xjIGYwBJBU90i0fQxjUfIUR0NFUldcgTVHz3VkJpgoe07X25FVw98Pc0rQqvsceIIBTJ1JbBOoUX6HFYH0DYYWOMKT9lL0GOqUBMV6F2tAkpGu7hFZ5c7tUkzca3PzMNKDtPUeVaTXd%2F3t7Ye9y87V8AECtn914sh6VRQQ1zBQSfFt3wYVyRmTpD4uJZ29C0jo5v2LKpeXKEzLRKYOrM%2BwFIHSCzDmohfg1p9DbzVw8Cy7GqBLSmi0cyWfr1zJbMwl1QUjLKQ3fCvUDjxvvf8ECTKm%2Bq7UhF9hF%2Bcow4o8W6R6EGEeCqXHuZpjOGzU%2F&X-Amz-Signature=b831bed0a5132e0ce7b05c73e758b983dff41fcff452afb62709e5efc697c6c3&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Algorithmic Libraries
#### 1. **Scikit-learn**
- **Description:** Contains tools for statistical modeling, including regression, classification, clustering, etc.
- **Built on:** NumPy, SciPy, and Matplotlib.
#### 2. **Statsmodels**
- **Description:** A module for exploring data, estimating statistical models, and performing statistical tests.

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c62885f5-417d-4179-834f-d68f8f2bdf39/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665E25HJQ3%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T231608Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEE8aCXVzLXdlc3QtMiJHMEUCIC2RseCqYu%2BJKeU3Z96aOsqGHQSdhSIztgAhJcDIzdTjAiEA6qp8QjJndONfpXZ6MHgu4D2D%2FlNb8JV2dJpnQ2eOsWsq%2FwMIaBAAGgw2Mzc0MjMxODM4MDUiDA%2FqvEM9kNCJRCp2UircA6i4SVBRNf%2FZE%2BzmIBgys5Ocfvy2R3tKkYJrNcW1WyUGoZEB92plRU4yIz6CM1hgKQQ%2FRp3wDoo4uym12HnxTGr1l4koORR0xTJnBJFTaoEurol2XPk2GA0emlFaITC8JfmDci440lgIdbrTnz3wcBLAoqI8rh7cvBnhvnDUF1P607t%2B9vnPKxNBm94ISZQcFg3RD46MinAOh9dvTAE2PXOihMMs7KWJgQfKTlyeFflzYXcvn2FQjy3u2pI7lcwCMpv%2Fno4ZYumV%2FdMROzyX%2Fx%2F4lTRi4XyYDZrQUfQzPjhdrOWzg3O8Kp7vMw3wWR8CwfXY1cxoRjIH3Iapb1NcOyjtXaUiV4AGIwzLtWpFwGi81aqilczwJGpm3B0AaIOuXg5bMxDrL0K2azghNBxzY9Sq8LgT8oViXzHP%2F%2BXlEaYTaoJhuNSk3JZ84D5OwMqZZCWBKGqlK7HpX%2Btl26nQ647XtjM1zhyr7asrXUrR0zQkDi5vj1sXVCT2zME9PC2DN7tLLNZjf%2Fa%2FfYacurJa7vaCt6fmAZJaczWo9xjIGYwBJBU90i0fQxjUfIUR0NFUldcgTVHz3VkJpgoe07X25FVw98Pc0rQqvsceIIBTJ1JbBOoUX6HFYH0DYYWOMKT9lL0GOqUBMV6F2tAkpGu7hFZ5c7tUkzca3PzMNKDtPUeVaTXd%2F3t7Ye9y87V8AECtn914sh6VRQQ1zBQSfFt3wYVyRmTpD4uJZ29C0jo5v2LKpeXKEzLRKYOrM%2BwFIHSCzDmohfg1p9DbzVw8Cy7GqBLSmi0cyWfr1zJbMwl1QUjLKQ3fCvUDjxvvf8ECTKm%2Bq7UhF9hF%2Bcow4o8W6R6EGEeCqXHuZpjOGzU%2F&X-Amz-Signature=4b5528c84cc886875041d7148f259768b28caaac9689b2b131029594575e8a01&X-Amz-SignedHeaders=host&x-id=GetObject)
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
