

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

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/997ac361-58a8-4f04-bb0f-79fea4baa761/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664TA74IZG%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T161831Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIF7Lge80Vhi%2BOMfLYrFD%2B78ffxKNNxZN%2FMYBFlvsOIByAiEA%2FpKAIyx0Oa9mtbDqVm0mwP2Cf%2BAZ3tZsCs4dwl1gSzoqiAQIkP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJ7zuMf13yp4Z9atsircA7YLqVQg09NSLaXBn2RhsnpP%2B9vWuc3hPJv1Dc4L3CV%2FC1tVNfHbZbmDtlk5jOWU7vXyegLkgtR6d0FXyszNqVS9%2F4SevxNPw3wbIWXbbxumRy6e3Vx94bRGkSClOh5NClwMKqx7fsB3dCxgYMNL53IS6drvdPRPYKdOaXoVYrnx8j%2F5Y8brjPv%2FIdsK70BcYIEkck9dY9OADCgoh17fmzx87gcNBfEAP8KgoPEvz8OJtcXbyYAU5AREquPLHmAYuPX%2B%2BAdrTS3QKoFW%2B%2B84s3fgamnhuQ%2B4JTxNKjucwbl4q7V6GuM1QpeBz3m7YmTbEtak3gnfLDaPyP4K5LXgSUuXFlmz%2B5V%2Fvjv4ewnuuqbsiYzacDsEdh4WUhFxBo7yTd%2BSISIiWkohXygXV7%2FpLzStpfjNiP7xybX2%2FXORLsg44R4heeKodXxG6o59Vg9QklOEUkSR5fmzWNmnIjA7AEWCSPf2YB5yZHGi0buX9%2FVHh30evoewQtr47RvulxbFKuDoFDjPO4RieT9ktNBs4%2BcywpOyj31vfKXG20cEQGjnhnxrigHmWv0WBr%2FzYduN16%2FmPhXlfSownsO%2FIFJb7wQmNSJ6lPzGThhiiZNx2UijhoXNsq%2F7czCxnme5MKuD6bwGOqUBknRXa1pfm%2Bl683SSBcd5RBMyKSAf%2F62m%2FiEY8xE%2BHDV9dAcJatD97FDRTCv%2FMRRy%2BDQRVSp49wIsQD%2BZwUUkIcPdhA8TbQW4fqXT5kktUr0uQdCOKVxJNU%2BUKQGmYZcLJ%2BavsgGWfuwS6ubH9W0ePxBnY6l5eb9IXGx2mrUxethBtoqE2ln8aYJW%2BAi6xr37vvNflYKTKkWbrtBfSzVftEYSbCjk&X-Amz-Signature=00fe23310f8f171ef97572ef4ff9185ac246521e9baa633e4865b938522182ad&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Data Visualization Libraries
#### 1. **Matplotlib**
- **Description:** The most well-known library for data visualization.
- **Features:** Great for making highly customizable graphs and plots.
#### 2. **Seaborn**
- **Description:** A high-level visualization library based on Matplotlib.
- **Features:** Easy to generate various plots like heat maps, time series, and violin plots.

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/733d1e42-5a53-4fd8-90c1-3d85254369a6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46675KBRZIO%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T161830Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDABaa2J1AvdI2wkwvSRhoqgrc9oRgnZ2VuLcmtVzYE9wIhAIs%2FpSodM2zkdYNm0rcYAduyCLiNV9gIm0%2FGMwC6m3BwKogECJD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igx9hNfKZ4lTuL5KTmcq3APnbeidmk3HMGK5waZ0qJCz30Py%2BARJuzz50ZFjRYGlzmBH1GnZ%2FiSfrO5rAu1aUZOIgXWwd1ERXtBL8sAfsjp3iSo7wDK04NGPStQ4IhBq27Pl7BDjfXTphYW23ccKlYtJuUuQ2I%2BQI8UDsxp9ftwJL6jnipzb%2Fv6Hkj1sbrMVvywpEMSu3oKlydvBzpO0A%2FHWqeG%2FqLfzGCj%2B6QYsFFQRVRAyuaFf%2BsscqfFkmhNL7%2B2ZkhIW09wFC%2B6MLzRthaDVW4pJX6tXrDzP2IuMMds5mDdOJWP8wIxdYEobgcQNXzPBKRvc%2Buu%2BXcLrYJK0Sy%2Ff%2FP5XW2JTyX62aIL%2F1EEQX5m3MzSyI0fyD4ED5uTjpIBbFzuC0tP3NlKLjgJ7MLkdf2l3KiqiNC80AmAnUWmQph6sR1XKLBSuqXzeX%2FOtC9bTbizL9qgvEebu7OhuafXMxXZDxZ4jaAnYkW1QnyJM5A%2BNF6l0Rry7843%2BXIeaO1dbiK8ACa4BXAO28AvhoE9jGCrv6zjWGM0J6saiGe3fcUSUl9r4NPINcaCxNR0Nw2s7zMe%2BldZmjdjqm6nItK7vWzbwZh%2BDcOiasq9W8XasvREpVzCHwwlhmXEhBYnKFnnkrC2c7tW5z5yFXTC4g%2Bm8BjqkAb%2Fekf7lL44YsB0rdNI%2F9x4iX2OvCWvcb4mDwQzkuammLfMmTAWz1uYNhE6gbC7tL%2FdENxnufK%2F%2Bq%2Frwqq7oqeM6V4Ugjt1EN%2Bl9gDXa0M4hybwKvhhcWTSTAydY7swbM24NuK36tCsAV%2BYkzpYb5mvaADEaphNwEx0A4721C3Z216MTSZaX6FhODmc2XaxfqqTz%2BUOS7CVPkQ1t42X4nXEtAPrg&X-Amz-Signature=58b9b36a9b2229538603847038ee2b71ef722f908ff5a0b2ff4f0ff5adde11fd&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Algorithmic Libraries
#### 1. **Scikit-learn**
- **Description:** Contains tools for statistical modeling, including regression, classification, clustering, etc.
- **Built on:** NumPy, SciPy, and Matplotlib.
#### 2. **Statsmodels**
- **Description:** A module for exploring data, estimating statistical models, and performing statistical tests.

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c62885f5-417d-4179-834f-d68f8f2bdf39/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46675KBRZIO%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T161830Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDABaa2J1AvdI2wkwvSRhoqgrc9oRgnZ2VuLcmtVzYE9wIhAIs%2FpSodM2zkdYNm0rcYAduyCLiNV9gIm0%2FGMwC6m3BwKogECJD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igx9hNfKZ4lTuL5KTmcq3APnbeidmk3HMGK5waZ0qJCz30Py%2BARJuzz50ZFjRYGlzmBH1GnZ%2FiSfrO5rAu1aUZOIgXWwd1ERXtBL8sAfsjp3iSo7wDK04NGPStQ4IhBq27Pl7BDjfXTphYW23ccKlYtJuUuQ2I%2BQI8UDsxp9ftwJL6jnipzb%2Fv6Hkj1sbrMVvywpEMSu3oKlydvBzpO0A%2FHWqeG%2FqLfzGCj%2B6QYsFFQRVRAyuaFf%2BsscqfFkmhNL7%2B2ZkhIW09wFC%2B6MLzRthaDVW4pJX6tXrDzP2IuMMds5mDdOJWP8wIxdYEobgcQNXzPBKRvc%2Buu%2BXcLrYJK0Sy%2Ff%2FP5XW2JTyX62aIL%2F1EEQX5m3MzSyI0fyD4ED5uTjpIBbFzuC0tP3NlKLjgJ7MLkdf2l3KiqiNC80AmAnUWmQph6sR1XKLBSuqXzeX%2FOtC9bTbizL9qgvEebu7OhuafXMxXZDxZ4jaAnYkW1QnyJM5A%2BNF6l0Rry7843%2BXIeaO1dbiK8ACa4BXAO28AvhoE9jGCrv6zjWGM0J6saiGe3fcUSUl9r4NPINcaCxNR0Nw2s7zMe%2BldZmjdjqm6nItK7vWzbwZh%2BDcOiasq9W8XasvREpVzCHwwlhmXEhBYnKFnnkrC2c7tW5z5yFXTC4g%2Bm8BjqkAb%2Fekf7lL44YsB0rdNI%2F9x4iX2OvCWvcb4mDwQzkuammLfMmTAWz1uYNhE6gbC7tL%2FdENxnufK%2F%2Bq%2Frwqq7oqeM6V4Ugjt1EN%2Bl9gDXa0M4hybwKvhhcWTSTAydY7swbM24NuK36tCsAV%2BYkzpYb5mvaADEaphNwEx0A4721C3Z216MTSZaX6FhODmc2XaxfqqTz%2BUOS7CVPkQ1t42X4nXEtAPrg&X-Amz-Signature=a682ad4987c5632d31b3176e222b27a8a3e11f10fc5e8da5fe2a6f61cd7459cd&X-Amz-SignedHeaders=host&x-id=GetObject)
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
