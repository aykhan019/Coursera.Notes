

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

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/997ac361-58a8-4f04-bb0f-79fea4baa761/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WW3XKTEA%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T081810Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECgaCXVzLXdlc3QtMiJHMEUCIES1xR3Mz%2Fdwu9ZhvZU1i01rmFBKJpaYrHhVr%2B%2BC70QYAiEAkZxjMx%2BHLXUID2XjjS%2B4rpIRkn3VA%2FrG73l1ZyO1dmAq%2FwMIQRAAGgw2Mzc0MjMxODM4MDUiDKS105CmNP%2BI7uRk8ircA6s1fOBoZvQ%2FarhQawekgmqOnDcN29MfqLxIOchi8Yn2IP7lzFJCNLx4lpNj2pnctUE6Uo4ZDa9uYypkn1ZVv7zuwbv7Y1fz5Fj1gK2aXiHDWWS9G5utaiBNgUq5suE9cbAciNk2kLEVHRYTVloIcsGprXLIWxCVH4UWYmatzt19zcQAcoij7NKf%2BWOfqyds3jCm1Lqx7J32P963NeyTorPeYmK74%2Byv7rCu%2FxKhbcKhNwJL8zW1S8yquZzNqZ3agoACpUG33kBjMbrymUohLToIUDVPi33Lv80E8g2HRb4huvsM5ABAsudYaga3uEJVL95IfJF3q2kvw1QcNVh5AaaAtGFLA%2FgjakkfiqMQU5hDgOWqpMT7fYVOR7locFdu9LZanAPB%2BNqdL4%2BX1u2PekwdwM5YbzKPo05Q5REi6WEs8dJlv5h9IQnPraQkqEiHt%2BdVRxOUk44zkvZX5rACiwfXRcDMN%2F8cQPOHVxI%2BqjWsQiDaREiY3qNhk%2B0cCCv%2BU46hzx%2BnIJiZ%2F6VGD8tEfn5g2nAiEIOj5uN0Kg3EKZp3TM%2BZVS1Y1rSf33N88wse7okAjhqFh66KWP66RXtohTILRo0Y4wt%2FXccAAX9aEWBKqDb0D1GC1ImAyZlCMOKzjL0GOqUBRRoTQ8MCaZIfzH0mw9zu41MYd6Bt%2BurRyR6gkWArDZOZNicZUOXpYQ7SzoHwo3DycmHfM03e3NKreqtghZPZjxgAguYfCOxyACtuLGb3mBqY%2FFphSfWfUIAtaAvD%2BcVQt4S40Eil%2FyC15Wxn%2FgzhhV4mJWsEm9Ha2ypDT%2F6HculMcyc7rEkcDCxaNWkYGUl0M1gsYvMMfwDACJXS4BHFmyZYS%2FSo&X-Amz-Signature=c57cd95b08cedf35712a237957440a6f54af401d2158acde1766ddcb0615488c&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Data Visualization Libraries
#### 1. **Matplotlib**
- **Description:** The most well-known library for data visualization.
- **Features:** Great for making highly customizable graphs and plots.
#### 2. **Seaborn**
- **Description:** A high-level visualization library based on Matplotlib.
- **Features:** Easy to generate various plots like heat maps, time series, and violin plots.

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/733d1e42-5a53-4fd8-90c1-3d85254369a6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YPQ5VI2I%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T081809Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECgaCXVzLXdlc3QtMiJHMEUCIF1M%2BEjdtfuhgrUK1mplPxkLwsmQmaqbA5RZFqPPkb5DAiEAmidQKUVo%2FBINSRMDcHPPltPUv4p7RMFbn%2Bx%2FDgjrl2Mq%2FwMIQRAAGgw2Mzc0MjMxODM4MDUiDIKVYzuV%2FlFKK%2Fy5%2FircA7EMR2M%2Bo%2FCoPstIf6Hr1bOEPnaCG3WOwBheP3LMT2KdxsJ5XOBRgOg9xS5Hb1rh9LlWtM6bqcSlbq0ElqygOmT%2B2Fvr4p8oyzabt3SJyIvPVRaMeGfKTKc3mYgBBktdEzXKqS1w%2FwIB30MVlxNBSCaajFo18ZbyGU3BLoSjpgZjUZuR7CTwz425vrG3cut4fNVYPHV4QsLr688F%2Fa0jln7%2B1%2BXM0OkNu9e5h%2BV6gdi%2FuIln2Fu2oXgdaFJ0QWE06HxXo8GHaxnwgp0K%2Bl6ilrX93DySTYihlL8dxIdm77UbpYpCQsIdDXqxffJ2fSb4auf7ZFF3skfz2b%2FwEQeIgzI1dA2R%2BTyO5C6aDGWsLOjFO2NG5vVaT5Z4Lybks%2BG3n8XAlkx8Xab10KfKmpjAhXceyZKYeYV4fSrYZkg4rax1At75HjmI3w%2B4J3Vbc9hQtse5RWET1UkclrMAJVcs55lRJ1WIOT25XZflrHYTl8Ld8KlBq8MyMWRy90Pd%2BYO3gxKnQ2ly40LEh2beo8S2diF2ffhlRyMAviQyP4U0GiyZ7JAsE%2F2Rt1Zu70azYu0fz%2FbAcWb90gn7tKTfV%2FTDpmV0XC1huXALRmYhWNCV7UAyTUKMBeBnomDEagWAMIS0jL0GOqUB9seO3UMHIe5bu1uNjSj3MlN0W7bd30ekdLx%2BKwOTZ99uL0NtaTNKLs1d87613%2BxVvzcB3XAiT7IJVqzbIOdGgAD5DeGMHpZDdVstPMDhQdkV8Niu7ZJ2r2%2FGuzhVYffWagmh3mvMYZUOKXG%2BxbYOpJVKr0mv3h7eX33Xvjj7DvlRUsL2%2FHSbu6IcU7Re4X0dtJ8HF0KTqLh3Agqfx7G6fbVD7bs3&X-Amz-Signature=32b75cc1451e9d988e5c150ffaa88b748cb49713c37f9499745181249d7afa50&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Algorithmic Libraries
#### 1. **Scikit-learn**
- **Description:** Contains tools for statistical modeling, including regression, classification, clustering, etc.
- **Built on:** NumPy, SciPy, and Matplotlib.
#### 2. **Statsmodels**
- **Description:** A module for exploring data, estimating statistical models, and performing statistical tests.

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c62885f5-417d-4179-834f-d68f8f2bdf39/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YPQ5VI2I%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T081809Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECgaCXVzLXdlc3QtMiJHMEUCIF1M%2BEjdtfuhgrUK1mplPxkLwsmQmaqbA5RZFqPPkb5DAiEAmidQKUVo%2FBINSRMDcHPPltPUv4p7RMFbn%2Bx%2FDgjrl2Mq%2FwMIQRAAGgw2Mzc0MjMxODM4MDUiDIKVYzuV%2FlFKK%2Fy5%2FircA7EMR2M%2Bo%2FCoPstIf6Hr1bOEPnaCG3WOwBheP3LMT2KdxsJ5XOBRgOg9xS5Hb1rh9LlWtM6bqcSlbq0ElqygOmT%2B2Fvr4p8oyzabt3SJyIvPVRaMeGfKTKc3mYgBBktdEzXKqS1w%2FwIB30MVlxNBSCaajFo18ZbyGU3BLoSjpgZjUZuR7CTwz425vrG3cut4fNVYPHV4QsLr688F%2Fa0jln7%2B1%2BXM0OkNu9e5h%2BV6gdi%2FuIln2Fu2oXgdaFJ0QWE06HxXo8GHaxnwgp0K%2Bl6ilrX93DySTYihlL8dxIdm77UbpYpCQsIdDXqxffJ2fSb4auf7ZFF3skfz2b%2FwEQeIgzI1dA2R%2BTyO5C6aDGWsLOjFO2NG5vVaT5Z4Lybks%2BG3n8XAlkx8Xab10KfKmpjAhXceyZKYeYV4fSrYZkg4rax1At75HjmI3w%2B4J3Vbc9hQtse5RWET1UkclrMAJVcs55lRJ1WIOT25XZflrHYTl8Ld8KlBq8MyMWRy90Pd%2BYO3gxKnQ2ly40LEh2beo8S2diF2ffhlRyMAviQyP4U0GiyZ7JAsE%2F2Rt1Zu70azYu0fz%2FbAcWb90gn7tKTfV%2FTDpmV0XC1huXALRmYhWNCV7UAyTUKMBeBnomDEagWAMIS0jL0GOqUB9seO3UMHIe5bu1uNjSj3MlN0W7bd30ekdLx%2BKwOTZ99uL0NtaTNKLs1d87613%2BxVvzcB3XAiT7IJVqzbIOdGgAD5DeGMHpZDdVstPMDhQdkV8Niu7ZJ2r2%2FGuzhVYffWagmh3mvMYZUOKXG%2BxbYOpJVKr0mv3h7eX33Xvjj7DvlRUsL2%2FHSbu6IcU7Re4X0dtJ8HF0KTqLh3Agqfx7G6fbVD7bs3&X-Amz-Signature=35ef22433efb07607205f990dcf62805b405b803051d536792f81c4ad51a0e9c&X-Amz-SignedHeaders=host&x-id=GetObject)
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
