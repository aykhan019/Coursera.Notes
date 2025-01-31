

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

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/997ac361-58a8-4f04-bb0f-79fea4baa761/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YODO2SHQ%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T010835Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBXJEBe8Cozn%2FmWNeaoZM%2Bj0P%2FWT5zHVVBznujQ1zVFgAiAb22yRSkl7ijEvKB7MfUGWAs12v1mvoqUnCtEju16D0SqIBAiy%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMlO5i5cukL7kX%2F47uKtwDaRJsv%2BtSr0Y3VjGlLKlrKLGU7boLQYUNsH4CYBj5xdNU54rip6awLNv3ZnfMn2giz%2FzQzqV0CYkS6LcV8bSrDJoi7K2zfZGx1LKF1Zb4wsSaqQhRUB2F5BCdh72jsubBoytdQZ3nyn5ZeN4VW0AsrUNm0%2Fxj%2BZY0I3%2BaVVEcawzaFZvW6dXTOMXB4hzHi264%2FRiafe%2B5idchl1QhW0HEOMBucrexmx0uWQ0LzzkIBdgj8O09BWZYHzbAVagemvqSJo5dFJPUV9G6Z3D2Z930YogAG%2BLrm7GzIZ1HPOFcoCA3WkAFlCy6YVUz0cpMsUt73gcDMcJSaj845%2B0tBVkCtA2WMVD%2FKcwMTQjC1aFYX41cCpT0aE%2Bf7QeX7hKwNGKozB6c95X8F1CCAre2rHJNmDLCgML6vPTIfTXDwzOMsGqwSokPVozBPsrzZRL9K9l38tSZBVFhK7jJ9Tf7A3kbOlobSoLtLPT79%2FMxddUYkxTcjVNpI%2FxV%2F98dB9zqOpgLG9ptysG90Eb0EQaVQG6apccT1yUKYbjHhb4W06CiwsZe4zN9lDAIMdM89JTCZvQo1zAKwPdc9%2BaBLkZtMY5UdeHKA6FAozEQyfPuFdCP%2BzDNR10o2uBs6n9Jh1Yw37TwvAY6pgFVglUCDyk%2BgTr2LzykDIcuXRFPkwRI1mc50z%2BcmyDk%2BLv8iq21pTQPbzbWVktTEQCRAZwLRz5uHhutvZaI8Xc9cAnaoe7%2FGGDmC5na8Kv4RBidGDMlHcUhr1d2CF8MtaivrGJuSgoh5fbeV6NhPHrFzzy%2B8b4TEbPIFYy0rHOlCvtpMY2ca4C7lQf0kkX2%2BNrrsamwm1HcpQ9mSLZLgwriI0JBeay0&X-Amz-Signature=1d7fce3f976285da8cbd8e3eb16e38dfc8142c9034e248ed34b06109f8fd2950&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Data Visualization Libraries
#### 1. **Matplotlib**
- **Description:** The most well-known library for data visualization.
- **Features:** Great for making highly customizable graphs and plots.
#### 2. **Seaborn**
- **Description:** A high-level visualization library based on Matplotlib.
- **Features:** Easy to generate various plots like heat maps, time series, and violin plots.

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/733d1e42-5a53-4fd8-90c1-3d85254369a6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46627FHKGNX%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T010834Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBcMs4bcIK0Lwhv7zMfGhMXpit2e10rfyFlS9HW59IHyAiAizL6HI6rrdK1LstU5n4CmAOGtvUfinZQ7w7hgND0UUCqIBAiy%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMqYulwjYI2bNEgmVnKtwD5y6n%2FLz6iJEj8BQMEu1z8iwNzA9fmNQ6uQdo73mbETmEsiG2SB73Np%2BCUQ20BbSa9NkSFYM4B%2FvNOPkZ8QQfFMBn9wGSbGgispQ3Eyg8f%2FCjPGMBMBrL51FPwbb6NFBr1ATNrskc7ewHMLICsCskZTzOegqxNHp8K6vmVG%2FSoPT5ANVlnzqU2hV%2FX0Abvvk59GxW8RR4LDV8OwYlB4dQtYEPizCb%2FOwa%2BDFlJajcBXaNP9UECOQZJF4xjP8wAoYcj2V6dpW57Q7RadR3sGXUoIWLB04T%2F4fSDy7VQKVl3AOQh%2F5Hpv8gYy9NsmcShGXBQP62lYj%2B8SI3ianGoEVCwQR87OJa9e%2FUTZKePjjPAkv%2ByBKYMYGtyIURMnPoXbc2CroBiH%2FNwwF7J23n2fem%2BdKPN67SkcVQ%2F0faBBncwzNfgCPzD%2BSNj0jZKBM46Ke7RgrcCSF4%2FvWk6QLjzXM2146JS6JYO1idLA4hhYf8IRbXdZXR4aPnsp3W1kGv%2F7Bt5uYMVotTccMbtrHkmX42STEQQxcg0hqjnPPn41hhhAkKy6KLvjyNFkAIA8MQFWiPRBRPjRJguX3fkWFXT4pOl%2BJUQb6zisGVmzeLoIZQ3RIsFExpxtGhnhn1iKcw47TwvAY6pgFKW2SUTh%2BLvrwVGMJmHKezTGkYfoIeiZnvAUgdgvVIUT3k1f7GIOwyN7iz2bUPZ9gPPkr%2B%2FldNhkoCai6x9LPjjw0iV6W%2F0eBulqB%2BNFp%2BRqfaFzvxSbnUEZ%2F2MOxmLCBCE2t%2BJmsEG4SxCruVKCw5EOjhmVmjp3UQezSm7adtoIN5YQp0UV8w4Zj781phjxvtnUcK4JYBKUL%2F%2FoR4tWKVckU6zWUT&X-Amz-Signature=d811b16db7fa54c6fb2a5377aeb9414e1598434abd92a37305b56958737576c8&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Algorithmic Libraries
#### 1. **Scikit-learn**
- **Description:** Contains tools for statistical modeling, including regression, classification, clustering, etc.
- **Built on:** NumPy, SciPy, and Matplotlib.
#### 2. **Statsmodels**
- **Description:** A module for exploring data, estimating statistical models, and performing statistical tests.

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c62885f5-417d-4179-834f-d68f8f2bdf39/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46627FHKGNX%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T010834Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBcMs4bcIK0Lwhv7zMfGhMXpit2e10rfyFlS9HW59IHyAiAizL6HI6rrdK1LstU5n4CmAOGtvUfinZQ7w7hgND0UUCqIBAiy%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMqYulwjYI2bNEgmVnKtwD5y6n%2FLz6iJEj8BQMEu1z8iwNzA9fmNQ6uQdo73mbETmEsiG2SB73Np%2BCUQ20BbSa9NkSFYM4B%2FvNOPkZ8QQfFMBn9wGSbGgispQ3Eyg8f%2FCjPGMBMBrL51FPwbb6NFBr1ATNrskc7ewHMLICsCskZTzOegqxNHp8K6vmVG%2FSoPT5ANVlnzqU2hV%2FX0Abvvk59GxW8RR4LDV8OwYlB4dQtYEPizCb%2FOwa%2BDFlJajcBXaNP9UECOQZJF4xjP8wAoYcj2V6dpW57Q7RadR3sGXUoIWLB04T%2F4fSDy7VQKVl3AOQh%2F5Hpv8gYy9NsmcShGXBQP62lYj%2B8SI3ianGoEVCwQR87OJa9e%2FUTZKePjjPAkv%2ByBKYMYGtyIURMnPoXbc2CroBiH%2FNwwF7J23n2fem%2BdKPN67SkcVQ%2F0faBBncwzNfgCPzD%2BSNj0jZKBM46Ke7RgrcCSF4%2FvWk6QLjzXM2146JS6JYO1idLA4hhYf8IRbXdZXR4aPnsp3W1kGv%2F7Bt5uYMVotTccMbtrHkmX42STEQQxcg0hqjnPPn41hhhAkKy6KLvjyNFkAIA8MQFWiPRBRPjRJguX3fkWFXT4pOl%2BJUQb6zisGVmzeLoIZQ3RIsFExpxtGhnhn1iKcw47TwvAY6pgFKW2SUTh%2BLvrwVGMJmHKezTGkYfoIeiZnvAUgdgvVIUT3k1f7GIOwyN7iz2bUPZ9gPPkr%2B%2FldNhkoCai6x9LPjjw0iV6W%2F0eBulqB%2BNFp%2BRqfaFzvxSbnUEZ%2F2MOxmLCBCE2t%2BJmsEG4SxCruVKCw5EOjhmVmjp3UQezSm7adtoIN5YQp0UV8w4Zj781phjxvtnUcK4JYBKUL%2F%2FoR4tWKVckU6zWUT&X-Amz-Signature=18acd04d8c7be68a16e2bc11645f80a3fe357e508579980dbd5662449bbd11c2&X-Amz-SignedHeaders=host&x-id=GetObject)
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
