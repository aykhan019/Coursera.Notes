

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

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/997ac361-58a8-4f04-bb0f-79fea4baa761/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466X5LN4DXF%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T101541Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEEaCXVzLXdlc3QtMiJIMEYCIQDXFE6aVbsQKanBiBuJJTb9h5KOEh0aVBHkOLuugPqKiQIhAID61dcBMhdBsiJS5gWlSfb5a8XK2SoTMp6ikGLzTmYjKv8DCFoQABoMNjM3NDIzMTgzODA1IgzJpQcKqNhLDFjIcB8q3ANJYfdcDKNl2CyRP2hmRhAiKKQRj9SYyBfH%2FEMKbOyP9sgql2hVzQEqEdweZeTq0PrkvtB3HIjfhr4NephiXNPyAh4L0eOJhrNJb36LDey48RRhQXRuDFHQ7tO2uRKAGA2ZRynZmcHttIGM96cizJm53QlXKHGhEDfklAdxaSOB%2BB5%2FsrjvNK1M60IYSZmWG8pZASXEzMB%2FiwEIVDZbsTqbBJnDZi%2Bz6ZiOD%2FtmSpeh7iM2UnyGXxY1BRHgdk9Bg4ibRdTjD5kwH0vc7y7Rq3TNxLXmMPMAA2ITTi5ztj1qgcI4RBnNtFyRII9nofFdWfXLyzlYUy%2BINkANH38kHqQOWCecEsplc5naYddw73FvdQAPWLKIAmaX5gje6kC%2F%2FkwmVy9XP0ZYd5NH%2BdfXtGblbufI%2F8%2FXTiRsr8QE08zN%2F4s4Ut8J%2FJBy7Z%2FyV1ApOrIe1XynFqm03DG2i2vlBLuaehR1MQWQucIg0107kmesd3UtXAGak8K31CwAFyTK3riCwer1pL8fD2toButkl2ttgNOjpJP2yoyy8tJKjMkyTZ9l%2FZaOXJBalFI6K0KXWzYx4YtzP41606TUT7qSsWpUdLIkedoT%2FnlbK8od6stjv%2B4Oz9n3%2FRTtgxZgMjDf65G9BjqkASni1PJTbwlLoIzTaHkdszDysQYzs9EruVkFoaW8HAO5d8j8nirEEVakwFkXuzRFwK1N6lEHfQnzM2UpGfjdQ9OnChplHEblHEL1%2BwBPESA1dW0vXWYpEI9hcFMQmbOBBTwzSpaF2btIFmBLmMv7RVNQOOLZbY1FKsTzOgZ%2FtkGLHlvDJxycAVtjyqhOr2v6mJ7TOYxvPFKAOZPr9MsShmVSEEhK&X-Amz-Signature=75e7ee7d378abfca55ef53b583e81edf62ef7814db1c8e20ea18ac2b5a2f2180&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Data Visualization Libraries
#### 1. **Matplotlib**
- **Description:** The most well-known library for data visualization.
- **Features:** Great for making highly customizable graphs and plots.
#### 2. **Seaborn**
- **Description:** A high-level visualization library based on Matplotlib.
- **Features:** Easy to generate various plots like heat maps, time series, and violin plots.

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/733d1e42-5a53-4fd8-90c1-3d85254369a6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Y7WG45LK%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T101540Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEEaCXVzLXdlc3QtMiJHMEUCIQCvPgYPsHuyDBs9pLxLgwy5DDUm1iosw9JSFG3ReE%2FiZwIgW75IptilaXuJ8SHjWWbTDkV6QmADqFYDEkGYtn%2BFA7cq%2FwMIWhAAGgw2Mzc0MjMxODM4MDUiDBtfhy%2FTy1aUZ%2FwxKircA%2FJOXo3rxxSRBgShmTLkM6qVTixv1ZEsL%2BKI5ogXUuomkFTjgtIxFW197iw%2BxuL9c%2BDK9GZyPCjFf1bz3yuuntAjcM5qVoR7HJ8LKjlHKRw0LARCH5T025sqOsxXMz%2B9EvpUISwauNzO0DV2hXunzzy0uneD8W%2FLHE327JlxCDr6nvsIACdOZ5F19%2BD5y1kOhp3wwPLkEvZhBLluBmJ2tqA5p4WUwWSKdKXYcZlyQFSjnWe%2FP9PxLApgR7DkYurSYi%2FZtihZa%2F4i0cfrPDv2uVx%2FRhIjm5itA04hN10YehE%2FrVYiyDR0uEA4imLE5jfGkgeV9Lr8N0zAWRtOzVtfxZ6bMOWF6lGroA40diTwnlhmQC6L7CZq3Cdsf9DkVzaMHA%2B7%2B%2B6EUR6L8QMFfKIhFtqBN%2B3%2FPH2Tv8RIIWtQz%2BUFhftTBTdOkht9umLOH1mV2rnGA8c%2BiLEUpYyDh8qEq2Sfz6KHX%2FEMrM9Pa6ukdWGFiYaS9oOy3FgviioSO5UDV9F%2FvIuerNwoyok%2BK00%2BvLLq7Zzw9xH%2FYh3RyXjkm9yIWfq3Z9t2qVB91MC4KF9b5EpI5aluJlzEbBe99x%2Bix0yQqSs2%2FZ90zHCJ%2BpF%2Bi8XiWrmWyLynpB2iwVnIMKrskb0GOqUBat85H%2Fb8IrAyT050XqBzwVykPDPm2ekXYE7azQqw9CTM2%2B%2FPCOCFspWwXiSv%2BvJovwFtggD6CbLxmmFZD5MOr6HZN2S4wckzIt4no3teXxI%2FKIoL%2BWLEcxq8B7J7GIimHoJwhrWv01uifAr9VIcPMq%2BueY3a1CYd8m0m1qgxQN0tIWF5HLXXqnVTqLPU8y5kil2Z295A9cUCaHHU0DbSPwuDhV6%2F&X-Amz-Signature=84fccb7d4bbb8d70e234a0743d5370ffb25ee3a723404d70cceae119460f3803&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Algorithmic Libraries
#### 1. **Scikit-learn**
- **Description:** Contains tools for statistical modeling, including regression, classification, clustering, etc.
- **Built on:** NumPy, SciPy, and Matplotlib.
#### 2. **Statsmodels**
- **Description:** A module for exploring data, estimating statistical models, and performing statistical tests.

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c62885f5-417d-4179-834f-d68f8f2bdf39/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Y7WG45LK%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T101540Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEEaCXVzLXdlc3QtMiJHMEUCIQCvPgYPsHuyDBs9pLxLgwy5DDUm1iosw9JSFG3ReE%2FiZwIgW75IptilaXuJ8SHjWWbTDkV6QmADqFYDEkGYtn%2BFA7cq%2FwMIWhAAGgw2Mzc0MjMxODM4MDUiDBtfhy%2FTy1aUZ%2FwxKircA%2FJOXo3rxxSRBgShmTLkM6qVTixv1ZEsL%2BKI5ogXUuomkFTjgtIxFW197iw%2BxuL9c%2BDK9GZyPCjFf1bz3yuuntAjcM5qVoR7HJ8LKjlHKRw0LARCH5T025sqOsxXMz%2B9EvpUISwauNzO0DV2hXunzzy0uneD8W%2FLHE327JlxCDr6nvsIACdOZ5F19%2BD5y1kOhp3wwPLkEvZhBLluBmJ2tqA5p4WUwWSKdKXYcZlyQFSjnWe%2FP9PxLApgR7DkYurSYi%2FZtihZa%2F4i0cfrPDv2uVx%2FRhIjm5itA04hN10YehE%2FrVYiyDR0uEA4imLE5jfGkgeV9Lr8N0zAWRtOzVtfxZ6bMOWF6lGroA40diTwnlhmQC6L7CZq3Cdsf9DkVzaMHA%2B7%2B%2B6EUR6L8QMFfKIhFtqBN%2B3%2FPH2Tv8RIIWtQz%2BUFhftTBTdOkht9umLOH1mV2rnGA8c%2BiLEUpYyDh8qEq2Sfz6KHX%2FEMrM9Pa6ukdWGFiYaS9oOy3FgviioSO5UDV9F%2FvIuerNwoyok%2BK00%2BvLLq7Zzw9xH%2FYh3RyXjkm9yIWfq3Z9t2qVB91MC4KF9b5EpI5aluJlzEbBe99x%2Bix0yQqSs2%2FZ90zHCJ%2BpF%2Bi8XiWrmWyLynpB2iwVnIMKrskb0GOqUBat85H%2Fb8IrAyT050XqBzwVykPDPm2ekXYE7azQqw9CTM2%2B%2FPCOCFspWwXiSv%2BvJovwFtggD6CbLxmmFZD5MOr6HZN2S4wckzIt4no3teXxI%2FKIoL%2BWLEcxq8B7J7GIimHoJwhrWv01uifAr9VIcPMq%2BueY3a1CYd8m0m1qgxQN0tIWF5HLXXqnVTqLPU8y5kil2Z295A9cUCaHHU0DbSPwuDhV6%2F&X-Amz-Signature=a7936177db2308a42c5847dad702e8aafaa6fcdef0264f72bd9977e1178f7ede&X-Amz-SignedHeaders=host&x-id=GetObject)
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
