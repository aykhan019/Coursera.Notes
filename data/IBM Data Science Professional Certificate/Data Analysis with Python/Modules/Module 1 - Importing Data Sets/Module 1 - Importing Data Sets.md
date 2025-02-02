

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

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/997ac361-58a8-4f04-bb0f-79fea4baa761/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Q4IJRYQI%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T211228Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIAVIab53BQwdAUtow6xXpNJbs5JCbG7lXGm8BgIv%2BCqLAiBUvaqOS2erBd1XfSZv7zahV7QWeriv1eUoLy5fpts3DiqIBAjz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM2HPafu1J899t7TErKtwD6zW9a4x6DG%2BBSNJcTMz3T7arkd2CPTekkDeRrDFFN3bkLMmMxAvhg09zJQAHBly1jbIGTuoIJY9QJaU7AgtX0sWX8I9HzCWjtQdnJwKiBBKglBy%2FviwRWpBWRFUl0BMLc99t47f6TZk5yqPGPbar5qEH0cDtMw7Y8R4P61Ilac74izbbLVDJMZjg8A%2BdWhStq0gS7zvHpsvq7Qvzvy4SQn4wt7Q8J87Bj4T9OEk3hybLHtSU8nVrUDCuHtwc7YyW7JRmn%2BqbY3dBI04Kg6jTL24C5Tn8evC05C38pvASlYBzXIiTvLHP02je94ri3kkArjRgkYcH4j%2FGU0M0cxumLoMLlMJZaheDDzZk%2F5H6Qm4p8vgszw5ScwbkpcNFhX8xaP6TOQFAUypB1eoeoDJgO64ngzdNIkbnKkIqP8c1tl0p7BeL7lQCayCm8PWgULRGtDwV7P4hW8IlxOW4Gj0%2BIS4VOkscyHmPrxr%2B0Owbl5RIbHSfGInRaE13GPg%2FyAUhQlszLAdbzbJJBk91S9pSTyT9j46LLAX4cVZ33Hvt3llvmbpdDdUcNbUGoMBA0XDO%2FtjdcqWNFFsNkBoaw8salJ9butr8hBDlAkBZc%2BV62onqGLotU7zxo%2BndwRkwkOD%2BvAY6pgFjNipoIW39QkknJ8RrjT%2FSsqlasBVpWrR%2FmX10vIReqkhym7fX%2Ba4U71UoNhg8zRQBopOzUN8MF9YPNN4Stov3%2B29%2BAkeK%2FnRoi1pdSehTqa4v61pt3G1QGCgwGSIrq%2BWqrk1Pn1IKnKGMMwIZ5Im1r6JbSw9Sm7xUFQhrogjIWK6kAHYBAM6q80y%2BuxKhQs33OopcMbxZTLp2AgdAjs2PPU1XP5hs&X-Amz-Signature=b6f677f53721081f1cf35a519fab0d4bb175e54ab161b95b1905ad344568c0d5&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Data Visualization Libraries
#### 1. **Matplotlib**
- **Description:** The most well-known library for data visualization.
- **Features:** Great for making highly customizable graphs and plots.
#### 2. **Seaborn**
- **Description:** A high-level visualization library based on Matplotlib.
- **Features:** Easy to generate various plots like heat maps, time series, and violin plots.

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/733d1e42-5a53-4fd8-90c1-3d85254369a6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SAF7LH4G%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T211227Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIB4IR8UbxNanUxt0CSn7rdHPQrqQ7pIny53k0%2B18PKAjAiEArulxx%2B%2BTY%2FR3Xr1nPJ1yXMXtqDIV0zPWLsAcqpGZDhIqiAQI8%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDADRQ4dNmcZd%2FCGXOircA1vx0BeizM8tF2IQfdSPd1EfbH1yX4grhN1BBK94JZxYa3AwDGvGreVAcVI7dxRlc7zzeb1khe4xl1%2BEPeB4Dj6Owya6w0ABAy8W3op5PIAms9EZQU6r3KfN%2FBr2quLu2%2Fkni7r6hQ1MKf0fPjt7hCpGMzIHlt8k6ZK1lF%2BpC9HnwXjabuHGaC%2F5DaPng%2BJgPnGts%2B7vYLxJf%2FNsYsyDfId7%2FTI3EZZNdlOglSDv3cQrvstXeRHWgHF5j6cmfz31SkF%2F9MSS5GHwfnJVkP5xHqbjkC%2FKiMmqyF71o%2BVvu%2FlJ72GsTIUnILmzFNonHd8PuqEhEjo04BAZsp5h%2ByFPDLUgkQlmjQxC3GKi2hLIKa9Amwl%2BeLb5asvY13UC9NwkTLpHkMfuP1GJPW53Er6icKXpq9kVOYHklzn3rlKm0FAjlmFgZ9FTeU59IBiu6pJhTqol9Rh%2BIZUHBEOYWXYbB%2BvaFLHveBIqtVhqPTJ0C0mSw9sMvMlN3syI1H8hdVymFd%2FKprubuNQsthTBWn6sC9vetufB5sY%2BMjtrnRGF8YLkNyJlV%2BP8qaqS2n9ykT0%2BIMWM6bWCFZ08VatGTK%2B8CXp08Lugkb6TEsQRwGaPA3yWv2Zo%2FCNx%2B4tMtzt8MJrb%2FrwGOqUBgq614LPQHUwhXBFVCcpNXRIJqOc%2Bmxk%2FllqnEP2BCW3hFrwY5Dn8Dhhst3hAAKo1twgV492zsEV8k2CvdU4dFiG0lgVUlAlrHqkEcH4ELfLdsbnPCIK0%2BxEzeKGKImuZ9akf5eGx91GdFvRJkg9aIuhpJ2IlytEeKT19el0ne0V9Q92nbebQz%2FDcdr63cGbjoTC%2BoMcyJYpVtGS%2FHBmEmmIplIeM&X-Amz-Signature=0ac987497acefe71a48a2f09c6cbb4dc7a63a9b12e27828ed244340d0b64960c&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Algorithmic Libraries
#### 1. **Scikit-learn**
- **Description:** Contains tools for statistical modeling, including regression, classification, clustering, etc.
- **Built on:** NumPy, SciPy, and Matplotlib.
#### 2. **Statsmodels**
- **Description:** A module for exploring data, estimating statistical models, and performing statistical tests.

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c62885f5-417d-4179-834f-d68f8f2bdf39/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SAF7LH4G%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T211227Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIB4IR8UbxNanUxt0CSn7rdHPQrqQ7pIny53k0%2B18PKAjAiEArulxx%2B%2BTY%2FR3Xr1nPJ1yXMXtqDIV0zPWLsAcqpGZDhIqiAQI8%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDADRQ4dNmcZd%2FCGXOircA1vx0BeizM8tF2IQfdSPd1EfbH1yX4grhN1BBK94JZxYa3AwDGvGreVAcVI7dxRlc7zzeb1khe4xl1%2BEPeB4Dj6Owya6w0ABAy8W3op5PIAms9EZQU6r3KfN%2FBr2quLu2%2Fkni7r6hQ1MKf0fPjt7hCpGMzIHlt8k6ZK1lF%2BpC9HnwXjabuHGaC%2F5DaPng%2BJgPnGts%2B7vYLxJf%2FNsYsyDfId7%2FTI3EZZNdlOglSDv3cQrvstXeRHWgHF5j6cmfz31SkF%2F9MSS5GHwfnJVkP5xHqbjkC%2FKiMmqyF71o%2BVvu%2FlJ72GsTIUnILmzFNonHd8PuqEhEjo04BAZsp5h%2ByFPDLUgkQlmjQxC3GKi2hLIKa9Amwl%2BeLb5asvY13UC9NwkTLpHkMfuP1GJPW53Er6icKXpq9kVOYHklzn3rlKm0FAjlmFgZ9FTeU59IBiu6pJhTqol9Rh%2BIZUHBEOYWXYbB%2BvaFLHveBIqtVhqPTJ0C0mSw9sMvMlN3syI1H8hdVymFd%2FKprubuNQsthTBWn6sC9vetufB5sY%2BMjtrnRGF8YLkNyJlV%2BP8qaqS2n9ykT0%2BIMWM6bWCFZ08VatGTK%2B8CXp08Lugkb6TEsQRwGaPA3yWv2Zo%2FCNx%2B4tMtzt8MJrb%2FrwGOqUBgq614LPQHUwhXBFVCcpNXRIJqOc%2Bmxk%2FllqnEP2BCW3hFrwY5Dn8Dhhst3hAAKo1twgV492zsEV8k2CvdU4dFiG0lgVUlAlrHqkEcH4ELfLdsbnPCIK0%2BxEzeKGKImuZ9akf5eGx91GdFvRJkg9aIuhpJ2IlytEeKT19el0ne0V9Q92nbebQz%2FDcdr63cGbjoTC%2BoMcyJYpVtGS%2FHBmEmmIplIeM&X-Amz-Signature=92a32dd0591d2e63b8be4f26dab8df0577ecb2c308a2fe4d89fd9ac49c60a878&X-Amz-SignedHeaders=host&x-id=GetObject)
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
