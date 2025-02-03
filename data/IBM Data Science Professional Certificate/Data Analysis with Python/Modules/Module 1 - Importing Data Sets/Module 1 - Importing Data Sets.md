

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

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/997ac361-58a8-4f04-bb0f-79fea4baa761/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SFK7HZCW%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T051441Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHbfT3HTGhKQm1I5%2BqsmkfX%2FUCUyLjIh%2BkBa1VsMDIyOAiB6RCJkiztKNfQt7mCXhvI8HbhsYSiKezbvmWEkU6CTPSqIBAj7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMWqjPF9jPk6Ty3mPVKtwDlH8QYChjiw1zTNpd6mnFGBi%2BiXiD%2BwiRZcNgS%2BrhYsLyvNzQA7HLaAQiZdrb7U%2BGDJqly50cl5dMNuON5LEHE4WUJ0FVaThPoShG%2FAj0jCY%2BbGT8zR3cv1P0CKfvuro2Gw4aVrJDDZ2N6pFChQ6V6Hk%2FaCpsm7N9Ejj5L94qCVlI7HMTigoiGhTkmPFp9GvTgwXB%2FKCDhTl%2BW4ZUFAlJ%2B0NJgoOd775t8VGJap3RTUlwGNB8CBI6%2FpcOvTw%2BGsMYJu6AeW5563w5iYQidl8rosl2Ign55dE0YS64EhPxm6IBIQV3iP74E%2Bvb2CEIpFVplM3HBwEYsR1PF58mUdPfDsEyLBFIiiDKntllB8X2zJpB2xtfOf9hYa0m6GUaImlV7m0WOiH%2FkRZvjndvi%2F6X8QrryukMFm%2BUp6VDC8X1nPg51cJuVGaK%2Bko14efcmLMaaqGY9FEZWVwGS4%2Bu2u66GPCMwelXKaR0gqRJCkqm1%2F4pcYzr%2Fmnx0XiBEsR6%2BhUP9kc1XwzF18dxNlxun1anFRK4cmV602%2FDrChJZ2LxOQ0K%2FBkTd60cG7%2Fa8RAXYqSC0C452I1%2BRE6CODuCglMIDf4favQ5np0X7GoXSd6PD98RVwvr58Q%2Fm%2FskXvQwrb%2BAvQY6pgGlDWCS%2FPLzgBJ6zJp8yB3LrgyB3U6Ip0a4WmmfLNthXQlKF8YF8pDVS8CODB1S4J4q%2F2K6%2BDhBC5vGtEA6TiuQxjpIGKHX33vLNQd2lnuIjs38upyBTTA0qh8irgBUebdUiTvIkRw%2Bm6zD1aN5afdJ6%2BFDJuOOIN4vD3305noDR9L1vdaRmcvEC%2FOcQz4YbVqQ%2BJHWENngo7TsO5ZP4wW2bplYns0C&X-Amz-Signature=7f044e00fbd8a18718473d120f94aed160de2b289a90f12bf12ad15d7369e24d&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Data Visualization Libraries
#### 1. **Matplotlib**
- **Description:** The most well-known library for data visualization.
- **Features:** Great for making highly customizable graphs and plots.
#### 2. **Seaborn**
- **Description:** A high-level visualization library based on Matplotlib.
- **Features:** Easy to generate various plots like heat maps, time series, and violin plots.

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/733d1e42-5a53-4fd8-90c1-3d85254369a6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T4LFAZ7S%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T051440Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFqa%2Bgh%2BkdpCy1BfbQxPzfYhGI9uyqPccJGE2wwu7k3VAiBoSWcM%2Fyzr6xkllM79iMR%2Ftgbc9SjlOn5IHhiNBLX7EyqIBAj7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM2UdAWalbmGB7%2BqBKKtwDCW8uiR5YzZW3jT2eeeQWAfkhG05nFiWKZg73duzSbuvYTEJdYjYrCDkRlDlB8G8LDRnt2wliklgMKcej7X7yQjTAPYt0G9RN%2BAgw9CTZdFenemyWleNgxbf3R5sH06CAB5xSiVLtV87vIDS6T%2FcRNYEtZm1uoemMjKeujL89XE8o4mkHLL5FdqUMeHF%2BrvkFpV5sCqgMv9DNpWyU8dXkXl3ETO3ysebMSBQs6RXOtc0Ma%2FNlzVGEi%2BUYYkvwFjHxnwY9f4xMGFueg%2BbXWEXSHixIDCSSPgwqbsGqqaF5efRW2Xs%2FpiQzQpMgNd%2FsUcjWTC%2F3zPgLEPs%2BCzxp%2B0ODW6I2TyN%2FFDGE0e96BRZqh5Bfr1E5JvbY5Vw%2BuVtjknOeMZjGkTek69BLsORTpAUQdBd6CdTHB%2BaLuqr0ukU97iF7rgOUZOGCxdlabjWJ%2Fh%2BBXFhTc4SNOVJyH%2FNo0wZG9ivxSswlRtx1T0Tt6Ps81pCPuF65m%2FYbPKHMUwozrWu7418pO2Tt2KNh5e1BiL%2FERgRacGYP7gnUSZNiz5Kccki4Qnty7INu92hgt2sW7OHOqqANngoEUXhyfK2CTlLQ9KQvkByDOiqlgUJsSKNAAGONVjdL4bM4V2fth4owi7%2BAvQY6pgHDGozWxmkiXEGMDfMZ1q9TA8LS19OVvSBxUA0Ogabifxl96WYoovMmWdA81ZlIGPDTyWWnHy%2F5m8dukIf7ZsofpbpcKS%2BGn7A%2BnJUAZhv%2BSQhsTr8znmSTVhTgtfcyaWyOgcH%2BkGUeLk30X3CkyzHVSMnLmI4ibIZ0HeBppNIrnDHVR8buR%2BGySvd%2BHO%2BmIuWoQ00Czn9v%2F4d8PXh6cAusAgC4UWnU&X-Amz-Signature=886b293492b4d62854704952bf4fd0965aad990a3902c7b9674d14856dbfe25f&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Algorithmic Libraries
#### 1. **Scikit-learn**
- **Description:** Contains tools for statistical modeling, including regression, classification, clustering, etc.
- **Built on:** NumPy, SciPy, and Matplotlib.
#### 2. **Statsmodels**
- **Description:** A module for exploring data, estimating statistical models, and performing statistical tests.

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c62885f5-417d-4179-834f-d68f8f2bdf39/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T4LFAZ7S%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T051440Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFqa%2Bgh%2BkdpCy1BfbQxPzfYhGI9uyqPccJGE2wwu7k3VAiBoSWcM%2Fyzr6xkllM79iMR%2Ftgbc9SjlOn5IHhiNBLX7EyqIBAj7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM2UdAWalbmGB7%2BqBKKtwDCW8uiR5YzZW3jT2eeeQWAfkhG05nFiWKZg73duzSbuvYTEJdYjYrCDkRlDlB8G8LDRnt2wliklgMKcej7X7yQjTAPYt0G9RN%2BAgw9CTZdFenemyWleNgxbf3R5sH06CAB5xSiVLtV87vIDS6T%2FcRNYEtZm1uoemMjKeujL89XE8o4mkHLL5FdqUMeHF%2BrvkFpV5sCqgMv9DNpWyU8dXkXl3ETO3ysebMSBQs6RXOtc0Ma%2FNlzVGEi%2BUYYkvwFjHxnwY9f4xMGFueg%2BbXWEXSHixIDCSSPgwqbsGqqaF5efRW2Xs%2FpiQzQpMgNd%2FsUcjWTC%2F3zPgLEPs%2BCzxp%2B0ODW6I2TyN%2FFDGE0e96BRZqh5Bfr1E5JvbY5Vw%2BuVtjknOeMZjGkTek69BLsORTpAUQdBd6CdTHB%2BaLuqr0ukU97iF7rgOUZOGCxdlabjWJ%2Fh%2BBXFhTc4SNOVJyH%2FNo0wZG9ivxSswlRtx1T0Tt6Ps81pCPuF65m%2FYbPKHMUwozrWu7418pO2Tt2KNh5e1BiL%2FERgRacGYP7gnUSZNiz5Kccki4Qnty7INu92hgt2sW7OHOqqANngoEUXhyfK2CTlLQ9KQvkByDOiqlgUJsSKNAAGONVjdL4bM4V2fth4owi7%2BAvQY6pgHDGozWxmkiXEGMDfMZ1q9TA8LS19OVvSBxUA0Ogabifxl96WYoovMmWdA81ZlIGPDTyWWnHy%2F5m8dukIf7ZsofpbpcKS%2BGn7A%2BnJUAZhv%2BSQhsTr8znmSTVhTgtfcyaWyOgcH%2BkGUeLk30X3CkyzHVSMnLmI4ibIZ0HeBppNIrnDHVR8buR%2BGySvd%2BHO%2BmIuWoQ00Czn9v%2F4d8PXh6cAusAgC4UWnU&X-Amz-Signature=c39140a62daa520d83e07dfc55672de5da9fa7e87bf195e937dbb62a1a0e2cbb&X-Amz-SignedHeaders=host&x-id=GetObject)
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
