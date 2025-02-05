

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

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/997ac361-58a8-4f04-bb0f-79fea4baa761/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ULC23TDB%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T141338Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEC4aCXVzLXdlc3QtMiJIMEYCIQCz6LtmmmFD3%2Fe8j%2FahgcvOlrRL8H6YgO4U2P6OrVkDUwIhAJP26ziRAPzaQ%2Bc%2B5EvEXrotUX9Zf5oA6H1%2Bu6BfVuPgKv8DCEcQABoMNjM3NDIzMTgzODA1IgwkGtaGnJ3VTJU%2FleAq3AOXXpP%2BT0o%2BB5A%2Fy8Fy%2BYL2uRNibLeYhbI9q4VLQncTITuM8wUWw4hHoxX%2BvsGlhb%2BxEFtCX39jFZIPxAD5gy01r9Abd9TaH12X0aAVfNDb2lqi90eXAPsa5X4kWoMwVWVqvpE0Si4Kr3C9M2UgDLkcCp%2Fr7HKhk5pSH0S6E2asYh7s3ZZ86cYyBnYFKcng2rAysqCy%2FWUqvZ2NfjmxN03wDwVnZznaEFpxPJMoOL5wq1yrP%2BD5GLo8ESYs78ZGNuOxMzlBwf36zJwqKGfTVNPf7qTb5KxhkTdkGHMWfz8gK9HsttUKsCDHR104BKOaSynRf4rIPwHj8KUtH%2FoRpAirrpFTRpv7Ci0eA4XGMm34ogehD3raF3ynNvCZxXVo5zsYInEmDvVPKVASQZNeWgQgJEYSwrziLoQCpxDE2aXE9GX7V%2Ft1P1En6wHihAY4HEhls%2BtBeFd%2BbtFuH2VbtITEa4ioALApjrnAUZ97auaFdocjvFDM%2FiNEs3dsjymozRyQx4WnHAA1hgEPd6Q3WIxWl9E2lKTB%2BBXu5Bhu9%2Ffq%2B0X5jOKpoDTMEtc8MMrktIiEJYdnNd7%2BRjFyiJoykGoMwXz%2FFL8KpI645L1PnjUmZzmUbm22BcPSCG9fHzC34429BjqkAaNBNonWysr%2FV8U5eCymJP8jdLHmFx1A8e9Yfr404I0tQ6UDz8%2Bc6Ce6HfrATit%2BS6JWRhXSDa%2FUlbmuv8K8B%2F7IvnFQ2Bh7vAaGcDJEwHHt59kCCSggwJIZ%2BCRus3i4Ive%2BwkpxiFn8rNme6bwz36KUmKsJMj3XhGzCeGCbCKsfMOAvUm8HK4goUVvfUSUTdjyw39rTE8jdJ7J7mbTVlYxTOrbK&X-Amz-Signature=fdd1be9f018cf9bec36cb27e7aba265047f4584cda3d608d0d5db04ee77c5ced&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Data Visualization Libraries
#### 1. **Matplotlib**
- **Description:** The most well-known library for data visualization.
- **Features:** Great for making highly customizable graphs and plots.
#### 2. **Seaborn**
- **Description:** A high-level visualization library based on Matplotlib.
- **Features:** Easy to generate various plots like heat maps, time series, and violin plots.

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/733d1e42-5a53-4fd8-90c1-3d85254369a6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZAGXBBSE%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T141336Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECsaCXVzLXdlc3QtMiJIMEYCIQDIn0oFDdBbr%2Bsg1U0XMugnoDeUrMsuABkIZP8X%2FcWb8wIhAMaHlNBNj1Ciuk5nHqnoMbPh%2FJSfZ%2BINLBDKy0VNddN8Kv8DCEQQABoMNjM3NDIzMTgzODA1IgzgNfRSvHUd3BhQkMQq3ANOawMLHFaVhu3Si%2B5mJQgdp1TDs%2BgIGwVXdN1qmCnzYMH3GIO%2BWG%2BqngpAWU1qWW125v5ywUr129unBKL08qgQY7M%2FrKO1UtY7hhrKsLrhbEkU4ikgTALXyOdcyPLwECH9g%2BWOuG%2BZYSuK2yTpQVXyi9MlpJXz85gzWK8xG4pJjFOiNFsVBvl9yjQ%2BbUInl5BpWYws49%2FLUf35DDySzHotZK3mbw7SWGc2cif3KzlIDkHkidsGR2H%2BssFp6JDIH702c2dgS1Tp8gWYQd5PQUX0RMbFjAUM5QeJDGU20DiybEg9fVkCfSMWbhd6ku2EnVnNAReF7ZRaBfCLiM8BQeadK98S8NnHSC1YHFnEmEUtuTu669wadJWB2NQxaDEIVzaO8AH0E9UdpQG9c75Y%2F2%2BlinU89TuKJQ7vg1N6vc5Z%2FyLLcEmuru6%2FmG%2FDuV5rlOIY2FVD2%2F5O8ylDGW%2FUIs8rewSEUiNuXOfyoVxzOm3e8NNyNk2jXxN6B%2F5YNLkFP0T9TKk62eGGg%2FW5SmP5aNjZTUNKGl2z1uF2OoBzXgH%2F8o7j%2BdqHAvY395HCcmYZLvhvS529cfZWPorqznD5QtoQ8du2KYkStbNKzjLGXFrK71Q2e7Qv28YAz%2BAKHTDmio29BjqkAU5tOc7OVVKisx403SOEZwG3McGRcSQ8%2BF6BoixnwP0Gn5JR7fIkwm9FMN9%2FsERqM11bQws4nIBrr63K6bTl8QPzeyKQngivVavxzwcXG%2FBNriDhM0W%2F1iUgI37Irg5I0QYbuJrnMUvY6anzol2lOYFo9whrELfLl%2Fynk5xATOF2O8S8u7cOjAUAi2gX2OHQLvo9kJFwa8jbvnekA%2BQt8B05Yn06&X-Amz-Signature=58534bdce1b972bc534215b2c44b9d2b0d65a9465d3587df542e35ec697268ee&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Algorithmic Libraries
#### 1. **Scikit-learn**
- **Description:** Contains tools for statistical modeling, including regression, classification, clustering, etc.
- **Built on:** NumPy, SciPy, and Matplotlib.
#### 2. **Statsmodels**
- **Description:** A module for exploring data, estimating statistical models, and performing statistical tests.

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c62885f5-417d-4179-834f-d68f8f2bdf39/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZAGXBBSE%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T141336Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECsaCXVzLXdlc3QtMiJIMEYCIQDIn0oFDdBbr%2Bsg1U0XMugnoDeUrMsuABkIZP8X%2FcWb8wIhAMaHlNBNj1Ciuk5nHqnoMbPh%2FJSfZ%2BINLBDKy0VNddN8Kv8DCEQQABoMNjM3NDIzMTgzODA1IgzgNfRSvHUd3BhQkMQq3ANOawMLHFaVhu3Si%2B5mJQgdp1TDs%2BgIGwVXdN1qmCnzYMH3GIO%2BWG%2BqngpAWU1qWW125v5ywUr129unBKL08qgQY7M%2FrKO1UtY7hhrKsLrhbEkU4ikgTALXyOdcyPLwECH9g%2BWOuG%2BZYSuK2yTpQVXyi9MlpJXz85gzWK8xG4pJjFOiNFsVBvl9yjQ%2BbUInl5BpWYws49%2FLUf35DDySzHotZK3mbw7SWGc2cif3KzlIDkHkidsGR2H%2BssFp6JDIH702c2dgS1Tp8gWYQd5PQUX0RMbFjAUM5QeJDGU20DiybEg9fVkCfSMWbhd6ku2EnVnNAReF7ZRaBfCLiM8BQeadK98S8NnHSC1YHFnEmEUtuTu669wadJWB2NQxaDEIVzaO8AH0E9UdpQG9c75Y%2F2%2BlinU89TuKJQ7vg1N6vc5Z%2FyLLcEmuru6%2FmG%2FDuV5rlOIY2FVD2%2F5O8ylDGW%2FUIs8rewSEUiNuXOfyoVxzOm3e8NNyNk2jXxN6B%2F5YNLkFP0T9TKk62eGGg%2FW5SmP5aNjZTUNKGl2z1uF2OoBzXgH%2F8o7j%2BdqHAvY395HCcmYZLvhvS529cfZWPorqznD5QtoQ8du2KYkStbNKzjLGXFrK71Q2e7Qv28YAz%2BAKHTDmio29BjqkAU5tOc7OVVKisx403SOEZwG3McGRcSQ8%2BF6BoixnwP0Gn5JR7fIkwm9FMN9%2FsERqM11bQws4nIBrr63K6bTl8QPzeyKQngivVavxzwcXG%2FBNriDhM0W%2F1iUgI37Irg5I0QYbuJrnMUvY6anzol2lOYFo9whrELfLl%2Fynk5xATOF2O8S8u7cOjAUAi2gX2OHQLvo9kJFwa8jbvnekA%2BQt8B05Yn06&X-Amz-Signature=c7c63837a5eb23a7fa3c93331d55be64c993e5366cbc9e1e1c6ffb10ce59a3ab&X-Amz-SignedHeaders=host&x-id=GetObject)
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
