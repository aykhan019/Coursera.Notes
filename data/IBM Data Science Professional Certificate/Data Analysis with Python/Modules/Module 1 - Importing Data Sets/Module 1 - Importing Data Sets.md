

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

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/997ac361-58a8-4f04-bb0f-79fea4baa761/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SYLFIBHR%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T151605Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEC4aCXVzLXdlc3QtMiJIMEYCIQCfCptzhMx4HkyHfhyJSOOVnj6PYCODnHjsW58OJJZltgIhAPIFaP1eK%2B7KWpwq8pkk1pQ4f1jpH9b%2Fq7dAKraEJs2NKv8DCEcQABoMNjM3NDIzMTgzODA1IgwQFEtIjHHAtBVq2HIq3AOgdvo%2B6tpbhoNk7hhmoHdWn6o9Yk%2FizR6tMQEUK2woVusMDjoQk%2FJ7hQpQ2z0Y%2FBanMmMAj8s%2BhnPgG9U6E2kro907nhPW5rjPH%2F3RPNknqlqzHA7sR8nfA3MoVlaqJu3JcoEQN8%2BhJZWfyzEuqusy%2Bx0IiJZhYRO5UuFruLpOe3kTV5PJZ7dK2yVP7fLLyI09K1oY3E3WX%2BSVhxhCFEXIUWHxC%2Bf2VoRVi3iDPgSoLW9mZ9zydCK9stYbDhaUeE8wQJlGSHOalhUJV5Kmyi9BogwMAEhkhY4qylLw3x5%2FTf5lzCjRJGKsPyZrPiHlqLrLdzC%2BfmfXFmHZpkHzwBiVf1hE3rYEqiljtvWrw7zVAEXdLA1d9Y%2BtGUlzy0u3yO0PE%2F86ZZpfZA%2FfadrauJAFRN1jNVhXsofXDGssrNndZH1%2BIOMRWTRi%2BOeoDsDLR6sbTlITbKSGDOwdGza1E3XX0ZPIJUDAp9%2BA0oE0p6pvmkQIbfLqAo%2Bn7%2FhNtD1R464gvWUfoAx3j7MblXtvK3XrksvV%2FUCv%2Fh7Br3ts9fehZw0LHckdqAHmbsX2pphTrunQ2215O8Q2gLcp1albpBagwtgTqbp7bTrk7OndG8mTgSmC4zyconwYAgj6NzDw4429BjqkAQJ0Y2l8SGHA50tDLRsFvP1qpfU7pxzA3KIWBrXHv8EnNMpjeYemeJqcWEyhihLpT1RfexA25C3cv6p%2BcUiVgDUexh3%2Fe4Zkh85efdhn5aJQeMSPTeG8SoiQaFybu5KwHHxsLvGxG0VkFRmXHdXbti2G5CugmpS%2B8LplHpND8h%2FOL5N%2Fp412WJNVyI2EbjUywMK1LI8KUgzT6bg9DspfMCzoF5tj&X-Amz-Signature=bbd656834fde59c068cbd8793794f6ebe67ca39050cdc57f0242eb4f55057b97&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Data Visualization Libraries
#### 1. **Matplotlib**
- **Description:** The most well-known library for data visualization.
- **Features:** Great for making highly customizable graphs and plots.
#### 2. **Seaborn**
- **Description:** A high-level visualization library based on Matplotlib.
- **Features:** Easy to generate various plots like heat maps, time series, and violin plots.

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/733d1e42-5a53-4fd8-90c1-3d85254369a6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WI75MHLN%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T151559Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEC4aCXVzLXdlc3QtMiJGMEQCIA18XJvhtMRzLeEv%2BzSneo2ob%2FbauWsQ0k9tFg5paP2hAiBqUDBPiVKGErceiFVU270xKlzdnxjThaDF7rQthqIlCyr%2FAwhHEAAaDDYzNzQyMzE4MzgwNSIMHM2t%2FKiUZFNGAmhgKtwDe%2FJf7%2BTq1bkV2HpdPL4Jhk31TfUcRFK2raWOv3MbDJbaToDT2nlehmGP2h9GDiHx%2F1z2bQiYWs%2B6S8iERE02WLnE5rb0stcuLiFX5BIqluVfsE49WBay6dlXr625NpsqPGRemWgs30hU7Mur5eO7%2FQ5UoRYSGEn%2BTEE76jKi2vu5q5ZSasQXTNlP8VqgYeIi%2BHVkoxQW96ZHLwlCu4otInt5bprc1W1PzS%2F5nW9cgMOtfpyUgS1c3CRky%2BbisY%2FowIJARg7Olx26qptCaggwgoI6r0OwsbB1fC4PYvMb7FZyXH6TX6TommagE462JGJKTAyEpsP1q34HRf%2BLpCu6cbUGUO4wD58R5%2BTPwA%2B84gjGWUCH5f1UJFbpcfdE7cwXNlEH1%2FOe3HJ5SClYmbgGwRWLw8r4ToynS0FjFWiiRR0x9HZ7RCFA36VMArtCg4LL6KOCcrMq1IoViWycm1sxMANwsSCbcJPt63YvPQuzf9mdWXWNcj7kohy9jYGgHf%2BUohnKqowDWM3lQ80W54Ck9fUOwNzg88Fa0YXcOLQ3NtKvOPCvuxs5TA6KG23Pp%2FFbvPMKlfRivAFvcdTjikDcAHvcvh6pjbm7D98RQeikmrr%2F%2F3d3qV5e9p9MqMUwkOWNvQY6pgE8zqg8F7h%2Bh3sHmxttrgVi%2BwufM8qvT0IVRJvcZwhjtFnyNprbEjErRlYrcvC7LNy%2F6vyn%2Bfw%2Fibc9XbbrTORqd%2Fl8ABwhgrJTTU6PZFgDvfSDfK2XhKJQekV3j7aq8JmoC2oHVw1IRcC5Hc1uyBykaniIoWE6%2FxMJRs1UwFI%2BnxMm4dh4I35YIt35aVhcH7mokCe%2Bu80RHx0IaAmvfhnQjOAkd53O&X-Amz-Signature=7c9b1ca7a246a5c523f5954880288a97f047a90b1aee32ee153f9f6f36688931&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Algorithmic Libraries
#### 1. **Scikit-learn**
- **Description:** Contains tools for statistical modeling, including regression, classification, clustering, etc.
- **Built on:** NumPy, SciPy, and Matplotlib.
#### 2. **Statsmodels**
- **Description:** A module for exploring data, estimating statistical models, and performing statistical tests.

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c62885f5-417d-4179-834f-d68f8f2bdf39/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WI75MHLN%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T151559Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEC4aCXVzLXdlc3QtMiJGMEQCIA18XJvhtMRzLeEv%2BzSneo2ob%2FbauWsQ0k9tFg5paP2hAiBqUDBPiVKGErceiFVU270xKlzdnxjThaDF7rQthqIlCyr%2FAwhHEAAaDDYzNzQyMzE4MzgwNSIMHM2t%2FKiUZFNGAmhgKtwDe%2FJf7%2BTq1bkV2HpdPL4Jhk31TfUcRFK2raWOv3MbDJbaToDT2nlehmGP2h9GDiHx%2F1z2bQiYWs%2B6S8iERE02WLnE5rb0stcuLiFX5BIqluVfsE49WBay6dlXr625NpsqPGRemWgs30hU7Mur5eO7%2FQ5UoRYSGEn%2BTEE76jKi2vu5q5ZSasQXTNlP8VqgYeIi%2BHVkoxQW96ZHLwlCu4otInt5bprc1W1PzS%2F5nW9cgMOtfpyUgS1c3CRky%2BbisY%2FowIJARg7Olx26qptCaggwgoI6r0OwsbB1fC4PYvMb7FZyXH6TX6TommagE462JGJKTAyEpsP1q34HRf%2BLpCu6cbUGUO4wD58R5%2BTPwA%2B84gjGWUCH5f1UJFbpcfdE7cwXNlEH1%2FOe3HJ5SClYmbgGwRWLw8r4ToynS0FjFWiiRR0x9HZ7RCFA36VMArtCg4LL6KOCcrMq1IoViWycm1sxMANwsSCbcJPt63YvPQuzf9mdWXWNcj7kohy9jYGgHf%2BUohnKqowDWM3lQ80W54Ck9fUOwNzg88Fa0YXcOLQ3NtKvOPCvuxs5TA6KG23Pp%2FFbvPMKlfRivAFvcdTjikDcAHvcvh6pjbm7D98RQeikmrr%2F%2F3d3qV5e9p9MqMUwkOWNvQY6pgE8zqg8F7h%2Bh3sHmxttrgVi%2BwufM8qvT0IVRJvcZwhjtFnyNprbEjErRlYrcvC7LNy%2F6vyn%2Bfw%2Fibc9XbbrTORqd%2Fl8ABwhgrJTTU6PZFgDvfSDfK2XhKJQekV3j7aq8JmoC2oHVw1IRcC5Hc1uyBykaniIoWE6%2FxMJRs1UwFI%2BnxMm4dh4I35YIt35aVhcH7mokCe%2Bu80RHx0IaAmvfhnQjOAkd53O&X-Amz-Signature=4e0f93b4548569f33b77a3f701d3ac86c1dbe6ff489913afe30a23433542d754&X-Amz-SignedHeaders=host&x-id=GetObject)
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
