

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

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/997ac361-58a8-4f04-bb0f-79fea4baa761/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WLANSRJ5%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T171224Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICKurSqZD1zyS6QkHQALY%2BMNDlyEbeK2Z2vLQEcXCw02AiBt3VwYeeNc7yOdg%2BXLfxt6pZNrbcj1gITU%2BqCoxDtXzCqIBAjB%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM0YLgYgh4JnokiR3dKtwDDbP5xwTfByL49ZmUUUCFe8f71anRVea%2BD0f5NSYi7UPxIwPTxByLEna6NKYDhzdq%2BE8rtnOAPfE4dPnAZhGzSLnh6x1Mlw%2FocS4HonPB%2FB0dcG2Ezuxz57Eewqw%2BAAK7f7EWZIr9B%2BRkYbHeGJhyq1Hfp1yVXIl81tehqzmlDzD0KByRjFRkt7YWr95Z0YZJtDOemHFBG8NHylzET%2BXxgVNflntjYCuJCzce3DvjrXWGQptDeRN%2FMfmBbQ%2FqNPZDWsNRFKlD%2FO17M%2Fy%2FsQSzSMETrGNdntwoni5uI2L7%2Beg%2BslOtF%2ForfYQ6fzgqJusSlZMjkhdVh%2FMuqnosCKYgewKNeeGJA1r4LV3lYHA7xqArqMAhB2JA25BeAoqg4YNnjGZug9aHxVonBGvbG65LAgZ6c7O4XHOoZxyXJhrsqsaEUIah2us5yC8CnXaHcH8iReYxRFvaHzyAjRripwq0tQJztMH13N%2B4Mi%2FTIQJgt2J%2BTSvT3nr4Kk9oT13EHUzqipPBqRp5xENN2IzTN3NtU4fqw8DQekRAwzCt1pNGCMcnOU0MiDLgEtuk0UbAz5l%2Bbf2Jq0bzASEX5rXV7j1gXS62o3AYbqhpMGhxV5Od88crDmykjcoqFW2neREwkOvzvAY6pgE1Hra5Vuifezxzwx%2Ftovl4aQYpg4z%2FPlNEGo84WgcxCnh0r4GbC89ZKyUJa2U3SBJRnkIQlsQHueNWkInaqwqCFT8EIp%2FgDsnV1NES1Y7yEqNBOZAhFUJNOR56EKtqnWJpzrKPBCJuRDtwXKYQXg7kmCYGZPvY2Q%2BjbhIykJljh8Ocj2v3%2FQuWD8BwY3j2nzNhf92YWmm0fEzr%2FNsFtx%2FToekGIL8F&X-Amz-Signature=1e55966e587d3e52491ffa915bdec8d65fcddec1003ff87ffaf06f535d9ebba2&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Data Visualization Libraries
#### 1. **Matplotlib**
- **Description:** The most well-known library for data visualization.
- **Features:** Great for making highly customizable graphs and plots.
#### 2. **Seaborn**
- **Description:** A high-level visualization library based on Matplotlib.
- **Features:** Easy to generate various plots like heat maps, time series, and violin plots.

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/733d1e42-5a53-4fd8-90c1-3d85254369a6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TYGNXKX4%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T171223Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIB%2BoxuNviuG7Rsh41k8%2Ffj1l35WqL6PHvuRRm%2BrXigvsAiBUpDZyvBD7gzoFbWacAoP5xSLcx5oZTx4hMTQGkX23zyqIBAjC%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMMN3xiumAAhhOjU%2BXKtwDidS8V3megruiTgVd8fqD404aLCoZpAINN6Pj0Vnt1jf6ueJGO8i%2BMLu4yQ%2FglpMQCJqthjxMaE%2BQHaNIzhGwpZtoWSnweUlGTatRYMMu1J2NiqaKvcvlVo5mymE%2FgxuEoPOXURo%2FOWwKzgz5vve5yMJQpJ7AuGZay9ZWkjnwpTKod%2FsmzIYGVNdAo88shK6lMSoYlPPtA6GLxXHKJFK%2Fj7LKqs3YWeA3E5beRDASz6NdKFJEHZnJu98WQbS4www9wbWhmi313oxh3WiqI5o%2Bt5BtlJeXj7lcyeVq3rhsWu68e7F%2FyeG46cLjKmhT6Ds2yA8v08rf1SKXE8wpkjwtA2ZLUUD1awigZOpWt6L7j7PEofKP0eC%2BKUHB3oMaZiFT8yK4A4QHG9%2F6EXLYgisNjIqTXS6YBbjxl9rpRGiOai8XR%2BQaTO9tyGdt%2Bf1FZ%2BPkjcd347hyqC8aE6wntYFB%2B%2Fi61rxPLBnvpvQxybxbYT3L8zIVJniv9Y6E5f7NvydrJba0ZhtINGg4qy8i7fR94ddFpe6ZsvBb%2BERHlMVLUzaNwa9tknEy2W4zZCCx5t8Pg0vPZu8aosMMziFHZu3cgmaW748WxDbTwm0yMLRfdjSolnNcccpF2agLLuQw3Yf0vAY6pgHryjSbFLlcBPNl56gCPSJyXSV9bt%2BrzwPnnuEAS%2FIzXG26BV4TVFeSzoev6TeQUIfb9YdC9ul8CKXmMjYyafOgmkZvjKZk04NTGGU3Y1jBTBedv2QejNXpLqtGQaIpYxJMU9W%2FgZNGS%2FYkW%2BYk9HMT2QCqUN94MoYIlmSw9ESjLEbU33SlGjyOJ6Ek4di8ITXBVywEhOvw9lXyIEbF70Hj7RZ9advT&X-Amz-Signature=bc4350e49109559efd6d029756fa89c98486adabb33ba964c90097b28a86a102&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Algorithmic Libraries
#### 1. **Scikit-learn**
- **Description:** Contains tools for statistical modeling, including regression, classification, clustering, etc.
- **Built on:** NumPy, SciPy, and Matplotlib.
#### 2. **Statsmodels**
- **Description:** A module for exploring data, estimating statistical models, and performing statistical tests.

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c62885f5-417d-4179-834f-d68f8f2bdf39/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TYGNXKX4%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T171223Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIB%2BoxuNviuG7Rsh41k8%2Ffj1l35WqL6PHvuRRm%2BrXigvsAiBUpDZyvBD7gzoFbWacAoP5xSLcx5oZTx4hMTQGkX23zyqIBAjC%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMMN3xiumAAhhOjU%2BXKtwDidS8V3megruiTgVd8fqD404aLCoZpAINN6Pj0Vnt1jf6ueJGO8i%2BMLu4yQ%2FglpMQCJqthjxMaE%2BQHaNIzhGwpZtoWSnweUlGTatRYMMu1J2NiqaKvcvlVo5mymE%2FgxuEoPOXURo%2FOWwKzgz5vve5yMJQpJ7AuGZay9ZWkjnwpTKod%2FsmzIYGVNdAo88shK6lMSoYlPPtA6GLxXHKJFK%2Fj7LKqs3YWeA3E5beRDASz6NdKFJEHZnJu98WQbS4www9wbWhmi313oxh3WiqI5o%2Bt5BtlJeXj7lcyeVq3rhsWu68e7F%2FyeG46cLjKmhT6Ds2yA8v08rf1SKXE8wpkjwtA2ZLUUD1awigZOpWt6L7j7PEofKP0eC%2BKUHB3oMaZiFT8yK4A4QHG9%2F6EXLYgisNjIqTXS6YBbjxl9rpRGiOai8XR%2BQaTO9tyGdt%2Bf1FZ%2BPkjcd347hyqC8aE6wntYFB%2B%2Fi61rxPLBnvpvQxybxbYT3L8zIVJniv9Y6E5f7NvydrJba0ZhtINGg4qy8i7fR94ddFpe6ZsvBb%2BERHlMVLUzaNwa9tknEy2W4zZCCx5t8Pg0vPZu8aosMMziFHZu3cgmaW748WxDbTwm0yMLRfdjSolnNcccpF2agLLuQw3Yf0vAY6pgHryjSbFLlcBPNl56gCPSJyXSV9bt%2BrzwPnnuEAS%2FIzXG26BV4TVFeSzoev6TeQUIfb9YdC9ul8CKXmMjYyafOgmkZvjKZk04NTGGU3Y1jBTBedv2QejNXpLqtGQaIpYxJMU9W%2FgZNGS%2FYkW%2BYk9HMT2QCqUN94MoYIlmSw9ESjLEbU33SlGjyOJ6Ek4di8ITXBVywEhOvw9lXyIEbF70Hj7RZ9advT&X-Amz-Signature=6135e5ca60594c836e50941c27f332e1bae6a1cdc4293f208010eb46f6819eff&X-Amz-SignedHeaders=host&x-id=GetObject)
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
