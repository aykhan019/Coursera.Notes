

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

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/997ac361-58a8-4f04-bb0f-79fea4baa761/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SLTA2T6E%2F20250323%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250323T004418Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGwaCXVzLXdlc3QtMiJGMEQCIA51Q%2F0wS3dQ6JYVVNbO7KgHmZnUA7%2BJp7JAPCYmub8XAiAIUtFqGOUQFz4kp3LlLWQ7F9RM2j%2F4ex5jUw%2B8U%2BF1IiqIBAjF%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMw5clxkp5DrPSqlNaKtwD08lbKdTIIqg4i01tBCK7xkz8iHwojp5UQsCYk1nTKzLeOSLPopV82%2BPNwKdys0dqQpDkTVp8ewY5Yu1mhmCtBfzCGhAzxuk0Z8rX7oMDwWtyqGoBAkA34xkar6HUOeYkzGvI7FWp3bq9ZswSVDgzZvWr%2Fc%2BXIsdxKg8Hs0dGn2eHmwX%2Bah8kXwObFeV8%2BzrleJzxs9J6yQ9q9yQR2yampY0La%2Br%2B2vKAKayGAJDX%2FDt5PeS5gEDoaFyXH6RHDzC5tREp3WADic4SWcw6zAheH2sew6aZkEIiG93V5X8qk%2FMbKF%2Fxhs0oaNS4Lcy%2FF%2FKwGfiu3%2FoBPmj%2BqYr%2FezPGh05UtxQ2SBqZuXq0ZqiHY55IBDFMMzeXOuTiJ4gvrWtN7Mw3N7fseYXtXeohAN8cifJ%2FbB%2BmuTF86YZGRrxn5vt8Bh7K56yLOjMvTr4axaXpjrFZ1O4E7li9GoxYM2jLFtLAjjr3oLRrUOby%2BZxYfdRvM8RqIjk%2BCDtibPa2u9Y10b%2Bhe0jIBAhBAoNgjIba5gQcTzrcnbfwQtJ9NxfkylgV4sPVw4z9H2PZygy%2B%2B%2BIWHaSJxL1WlyZfrDp9ktIXpdb7gBqyQz1dkq49i4J%2BJuLTY3DJTSH3ojixlgow3LX8vgY6pgGQoH1g4oyZBK2NguQC6n4ViXqrP4rvak5eH8fe3jwfK%2FWR7QUU0boPsYC6wrRXPRWaRoo2GUHclWMBSXofH6ejCEOgPgsVzdzOX4BGpXOLyYGnLRh6WKVTVmg5hc8hb9lAkUD2LED%2B4hAkKPqR1ueTwHZmcLeEGQ404VT4E14bctjWPZQQwPD%2FjmBr0mpQ3i3JVj%2FSzF5hk26efZmOqxCOxEjJP%2ByW&X-Amz-Signature=40a3b9afaffbec711b706bd6844c03de7062c1b6b96e4d52b110253e529c3972&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Data Visualization Libraries
#### 1. **Matplotlib**
- **Description:** The most well-known library for data visualization.
- **Features:** Great for making highly customizable graphs and plots.
#### 2. **Seaborn**
- **Description:** A high-level visualization library based on Matplotlib.
- **Features:** Easy to generate various plots like heat maps, time series, and violin plots.

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/733d1e42-5a53-4fd8-90c1-3d85254369a6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666UXOZB6A%2F20250323%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250323T004416Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGwaCXVzLXdlc3QtMiJHMEUCIGMNGHGa%2F8kpZOp4E1GUEr1BVvJpe5%2FLscMm00dOppBtAiEA08y0tI10Bo8XZCWDZ0h5%2Bj4omRPH%2FfooZhMjSj7rvXgqiAQIxf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOr9%2FIFknbvyNjPCxircA0%2FGdwt8m5BnCYlSMEe5UtuNmFOOPL18fshaP7usHL1NRSaVeSWOZGuIcGgiA2h%2B%2FNiuv0nW6h3vwIYYtSjps6XZ4tvIIZHmKimp2cxdRSbRn0mJhuBU2egOHwilJlAwQDj0CrWsrq5Zexeib21curctQ2VDijype5NMO5tk0opZqL9itgx1pS6rAWPenjIy8WxPqSqmxyYeoxV0i9O8h91iS5ILryjtA%2FTXnF652iCpepRFoAo%2FmpRbJ6hWCgoJVAbkFcBCaM6wsvoZb2Llkx0m2CtsIhmKcdY4lC5xyNcixdqcCFYrsmrCShTerls8jEu9hVtkLgmGviO%2BufU3T9KwZ70qzx0A0I%2Fu3%2BStTiPxcrqzIfAO5mKdEqr9bZAndYWfNxYEBPThoVYBCpH%2BsSZ0jRuOSpWm6bevix8Fu4OcB7f%2FD3nLPZ7ZT5IpCMCT%2F2PHelxs4TDSKb9Em4PHlBS4vrodkTLGNcdt0nZylp4wCsOjbzfTO320PYjETXnkL3WP35QtlRg9dkg2dqCHWklvEM5NTCE69bp5fctR9TXpDOrkUflnJWDOhHIsLPm5sY2pKAMiEvf6LBG09m7TqZMIjon0pOchZb3VCe4GFV41T5ACfyVnNwGKjG5aMIa1%2FL4GOqUBsJWstzA1luZdd62l%2FE09MsqpiMCEHpaaWe1b8E%2B2Msb6ulfNgSzTdgIOCufclu1BqAcyVa0a7SqJFqIW4amV7P4JWiRzv5oPTsJ3mok5gumr4PCUENOldj1oea38jzt0MOKnMy1fwytZfDuT0BsQnIoiQOujLuNh6s5fARD6SB5UM%2F4N9GJablzzK5Ixgg7GxqOiKM5N4hIjJfbMlHuTPd3vOzL9&X-Amz-Signature=6220ff6f33c715727a4e94d432f516cbd00df6629dd8e427798a0bdb1a709643&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Algorithmic Libraries
#### 1. **Scikit-learn**
- **Description:** Contains tools for statistical modeling, including regression, classification, clustering, etc.
- **Built on:** NumPy, SciPy, and Matplotlib.
#### 2. **Statsmodels**
- **Description:** A module for exploring data, estimating statistical models, and performing statistical tests.

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c62885f5-417d-4179-834f-d68f8f2bdf39/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666UXOZB6A%2F20250323%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250323T004416Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGwaCXVzLXdlc3QtMiJHMEUCIGMNGHGa%2F8kpZOp4E1GUEr1BVvJpe5%2FLscMm00dOppBtAiEA08y0tI10Bo8XZCWDZ0h5%2Bj4omRPH%2FfooZhMjSj7rvXgqiAQIxf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOr9%2FIFknbvyNjPCxircA0%2FGdwt8m5BnCYlSMEe5UtuNmFOOPL18fshaP7usHL1NRSaVeSWOZGuIcGgiA2h%2B%2FNiuv0nW6h3vwIYYtSjps6XZ4tvIIZHmKimp2cxdRSbRn0mJhuBU2egOHwilJlAwQDj0CrWsrq5Zexeib21curctQ2VDijype5NMO5tk0opZqL9itgx1pS6rAWPenjIy8WxPqSqmxyYeoxV0i9O8h91iS5ILryjtA%2FTXnF652iCpepRFoAo%2FmpRbJ6hWCgoJVAbkFcBCaM6wsvoZb2Llkx0m2CtsIhmKcdY4lC5xyNcixdqcCFYrsmrCShTerls8jEu9hVtkLgmGviO%2BufU3T9KwZ70qzx0A0I%2Fu3%2BStTiPxcrqzIfAO5mKdEqr9bZAndYWfNxYEBPThoVYBCpH%2BsSZ0jRuOSpWm6bevix8Fu4OcB7f%2FD3nLPZ7ZT5IpCMCT%2F2PHelxs4TDSKb9Em4PHlBS4vrodkTLGNcdt0nZylp4wCsOjbzfTO320PYjETXnkL3WP35QtlRg9dkg2dqCHWklvEM5NTCE69bp5fctR9TXpDOrkUflnJWDOhHIsLPm5sY2pKAMiEvf6LBG09m7TqZMIjon0pOchZb3VCe4GFV41T5ACfyVnNwGKjG5aMIa1%2FL4GOqUBsJWstzA1luZdd62l%2FE09MsqpiMCEHpaaWe1b8E%2B2Msb6ulfNgSzTdgIOCufclu1BqAcyVa0a7SqJFqIW4amV7P4JWiRzv5oPTsJ3mok5gumr4PCUENOldj1oea38jzt0MOKnMy1fwytZfDuT0BsQnIoiQOujLuNh6s5fARD6SB5UM%2F4N9GJablzzK5Ixgg7GxqOiKM5N4hIjJfbMlHuTPd3vOzL9&X-Amz-Signature=72575af0c37262a1c3e76451f8ee24455b68ba503fb848cb3d4ab0925d02c3f6&X-Amz-SignedHeaders=host&x-id=GetObject)
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
