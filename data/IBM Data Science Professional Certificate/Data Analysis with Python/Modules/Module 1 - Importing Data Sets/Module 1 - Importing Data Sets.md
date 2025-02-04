

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

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/997ac361-58a8-4f04-bb0f-79fea4baa761/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666EGAW4DX%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T201601Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBwaCXVzLXdlc3QtMiJIMEYCIQDobBwvwbc3KD5vO6AuDKdtbJL9TT%2FoTg9Pq2SsA6V8nQIhALNsionc5vR5AXovTL8GRkU92vbuXayzdX6RzSx9IwKVKv8DCDUQABoMNjM3NDIzMTgzODA1IgyJufMlWHf0mrR1FB0q3AMocROg3aj8iwllwoW2jZEuUsHx8%2F0l79wg9S9k8Fs7x%2BTyCXy3FY%2FKXPgf39RnNKkg5qwhTBRWp4MiEhk8NHN3nT5oX%2FCHirpRSi8oBIQg9BP417XIuC0wVk7fXl%2BWb0xYv2UZ8QeWRWsF49oe0vl%2FHotzqFA3JN535tSOTu8D3FMgJ65QpkAaPyvNQXE%2BbtOCwrgXssIB5LIeBA%2FWRY7a47%2FhkGrABRGV1W7IxG0FyretDM0BPpEPSfvsSrW8vNlzpPuyLf0nP2vtn82eHjIXqt4Rfrlw0btKOVMwbMGSKyMlftHl14Ce%2BP3FrLBZycNvZweJ%2Brzq7WnvW5jboYNpVTpo6XHSVmusU%2FXsjDEmSo12obrpLmqocgs5RUiciYB3%2Be38WQ0zxDnuu3ySBb3LK34y%2FfGR%2BJiMz%2Bk6cD6kVsPQpBYamfONG8Q4PHJUWDC7Zm50YKq%2BQ5zlOCIQO5dPlswhXb%2B1wfB%2FdfFzkX%2Bg1bkNW4zhpbGeU%2Fur5xybvq9oTQnsTTSLg1pEm9DDOxXxN%2B2WeXjjIckYdUu8cFgvoEvgTKDDfGiL2nsttN%2FezasH91BxcL3i27AnM2sqxwbOmE1kpvQMGZVhlECQ28g%2FhfbB0ctmIed2vdukbDDv3Im9BjqkAfqUZm1%2FqfPfgvDgrXlg8ctaFKNxpQ%2FbsK2TLJwFh5Q%2FFleDjsrihGJAsENJnIQ%2BMs%2FBnW5OPjdmELuxVeMe7hsa9NMmZK7NHfCh9BLrNeMAfWb2oUagGzDkIdJ7v8C%2Bfibzbl5Ru5ZmYOzmI0e%2FWatXS2NwB08zzVwuIQJXzBPxwhdlQrqBZG5w2cjKL1%2BvphYASDNAFEVcpBhq1F%2F0oPL9WpwQ&X-Amz-Signature=8f906e60a7916defc30ea66b7b990015f636a1fa2c19e40e0256c2df958dc64e&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Data Visualization Libraries
#### 1. **Matplotlib**
- **Description:** The most well-known library for data visualization.
- **Features:** Great for making highly customizable graphs and plots.
#### 2. **Seaborn**
- **Description:** A high-level visualization library based on Matplotlib.
- **Features:** Easy to generate various plots like heat maps, time series, and violin plots.

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/733d1e42-5a53-4fd8-90c1-3d85254369a6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WBP2YTSU%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T201600Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBwaCXVzLXdlc3QtMiJGMEQCIBv5ilJJWlFI7fBXCaNKfbABmGxHVXBZfjNPLn2BuDUvAiBo1nEk8%2FI9TuPZZgoc5eLpeghYE%2Bx%2FniPPJBL3qgRcgir%2FAwg1EAAaDDYzNzQyMzE4MzgwNSIM2PYfVNYukEDt3PUFKtwDhGH3lXCcjGWGWPZby6bZeERfSvM0W784tliJBq2N6DJ97rhDjfPwxqJpCSWEKwBNGBJpTVEN2TRySXGINrq%2ByzJRkG5sYCLVjX6scrhuv8SAfvms5tdTdbioUF5SmXnHDFBAhUCybA4JbLZRMRw%2B6AZiIybLf8XjtOlMEneHJwV1MZ06ty0FBV%2FvcNC1b9jlJynonN%2F3u0lPv0J8Vyq5o9vhiNzuGra%2B%2Bp3WrZaMhxjNyS%2BbnHyyIZ2N39MlUPj5OD1iyN%2FgFWJA0tpARIXQut5RMrDRc0PZozV3qR4J9bHZSdhCHi%2FjsVWYBcJW1hahUusjzY36YBrooxGO5hEjwwth6xohdr7wX9pqxzNWPxYTlLiy4Rm%2Fn%2FGDek2GHi1jghZsBd6q8VzPf69zzQFMXs0FoF0FXW9OOcuRaXREHmX1Yn4WrwglAnHHO6oTOIEqT3PghTNDJQo3UsDmDdAaR%2FAkGxC5ELkFVOzwOWj0l5O1QHhSu2kXOdO7vC5OwjuloLqCE82JgL1zbTN5gMTVAbIF5hwYHp4z8Z9M8mYBTRC7%2BvWAenfhNq2f8R19qf6J3nQQ5xuqyZcHMhxpo7mOXZRwtJnqU6M4%2BNLh31tEyZGCd%2Fn6Vjiy2od7oKIwht2JvQY6pgEq6EA%2B6NM%2FqsteOey6%2FUYuDObuEEUVdtEAX6GgagVBYgpj3wAvVry%2FQmnQTVMDLY1MiR%2FFYGZHQx2i4XS34AhM60UZ7pHTyeOEtuf0bIUWebh5QM3s7xqTIz64kbGbDl0Ucd8JfsOVcAxHrJEEjd%2Fmd8yhNTH1NUg7wgND4EBjaJnPqNkzT64jZRcsF9Pz2hb5x%2B60BTioGMq2%2BOFdJQ0vPVM5BqWF&X-Amz-Signature=dd92dba51d2eec2bc6cbae0bc6ceec3e7a4270008ed355865a1a52ef6969584a&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Algorithmic Libraries
#### 1. **Scikit-learn**
- **Description:** Contains tools for statistical modeling, including regression, classification, clustering, etc.
- **Built on:** NumPy, SciPy, and Matplotlib.
#### 2. **Statsmodels**
- **Description:** A module for exploring data, estimating statistical models, and performing statistical tests.

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c62885f5-417d-4179-834f-d68f8f2bdf39/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WBP2YTSU%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T201600Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBwaCXVzLXdlc3QtMiJGMEQCIBv5ilJJWlFI7fBXCaNKfbABmGxHVXBZfjNPLn2BuDUvAiBo1nEk8%2FI9TuPZZgoc5eLpeghYE%2Bx%2FniPPJBL3qgRcgir%2FAwg1EAAaDDYzNzQyMzE4MzgwNSIM2PYfVNYukEDt3PUFKtwDhGH3lXCcjGWGWPZby6bZeERfSvM0W784tliJBq2N6DJ97rhDjfPwxqJpCSWEKwBNGBJpTVEN2TRySXGINrq%2ByzJRkG5sYCLVjX6scrhuv8SAfvms5tdTdbioUF5SmXnHDFBAhUCybA4JbLZRMRw%2B6AZiIybLf8XjtOlMEneHJwV1MZ06ty0FBV%2FvcNC1b9jlJynonN%2F3u0lPv0J8Vyq5o9vhiNzuGra%2B%2Bp3WrZaMhxjNyS%2BbnHyyIZ2N39MlUPj5OD1iyN%2FgFWJA0tpARIXQut5RMrDRc0PZozV3qR4J9bHZSdhCHi%2FjsVWYBcJW1hahUusjzY36YBrooxGO5hEjwwth6xohdr7wX9pqxzNWPxYTlLiy4Rm%2Fn%2FGDek2GHi1jghZsBd6q8VzPf69zzQFMXs0FoF0FXW9OOcuRaXREHmX1Yn4WrwglAnHHO6oTOIEqT3PghTNDJQo3UsDmDdAaR%2FAkGxC5ELkFVOzwOWj0l5O1QHhSu2kXOdO7vC5OwjuloLqCE82JgL1zbTN5gMTVAbIF5hwYHp4z8Z9M8mYBTRC7%2BvWAenfhNq2f8R19qf6J3nQQ5xuqyZcHMhxpo7mOXZRwtJnqU6M4%2BNLh31tEyZGCd%2Fn6Vjiy2od7oKIwht2JvQY6pgEq6EA%2B6NM%2FqsteOey6%2FUYuDObuEEUVdtEAX6GgagVBYgpj3wAvVry%2FQmnQTVMDLY1MiR%2FFYGZHQx2i4XS34AhM60UZ7pHTyeOEtuf0bIUWebh5QM3s7xqTIz64kbGbDl0Ucd8JfsOVcAxHrJEEjd%2Fmd8yhNTH1NUg7wgND4EBjaJnPqNkzT64jZRcsF9Pz2hb5x%2B60BTioGMq2%2BOFdJQ0vPVM5BqWF&X-Amz-Signature=673d3244fbed7fbf3b1a397633c52504ae06d222ab09aa5ba348083a442560f0&X-Amz-SignedHeaders=host&x-id=GetObject)
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
