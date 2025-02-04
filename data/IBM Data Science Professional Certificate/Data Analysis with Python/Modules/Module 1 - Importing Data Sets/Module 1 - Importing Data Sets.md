

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

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/997ac361-58a8-4f04-bb0f-79fea4baa761/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46657HTSMCY%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T211342Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEB0aCXVzLXdlc3QtMiJIMEYCIQD508BuO8V8kcTQCOvz%2Fq2TngztBU3jCKZP8ADQVdqm3wIhAJK7Hga3TOJWOa4FLfmoZbo3fJx64ff%2FtgQb9TE52bItKv8DCDYQABoMNjM3NDIzMTgzODA1IgyPq%2B3BTt%2F9%2BHaXmd8q3AML8psOYtJdE8wBRlr11k5Osiw5E1VP3nT5delC4BmOPTOuww0ZXI6AojNLZpIdjb2onf0l8nWnnJ8YTvo0gh1nxhjOjeKenBsGl8jJkE5J334vMlsfRZvWNqd5vSwhjkEsY8Qg9Tb5FURXXhwn3X%2Fh5pOq%2FwGofPZzsC%2FhzqekMaGEbW1yUJz7XDwq3pKYhQ%2FusHf9dPPxvRgTYTYZdNXh9Z6oXiq47NQL1cTJBw2%2Fnu99%2F%2B7Pk50kJ2p8Audun9GJNEIP%2FGGKJTctE7%2Bf5DuO5Xo5Qu117xDRm3xuO%2FXV%2FmoQ7r5UCfAqWJoRpWKNalH%2BBdJQWJa4umVo3t5lt0sbHGwzs%2BcdUe891sTTqicpjvjTXeJ0t96SqElCer8Jz7PA%2FTGjZEOkidM8NKFp%2BEucf6NnW7u9FUGDV6ctKc%2F5jZCMY2%2BzYsYbtp5%2FX1e%2B6Fyyr7YEE%2BxFcGUJonJIvh4hZ2877Y7QwUg9r0tOOnkoZbOigr6Q3JC%2FGE02aNKiMI0w%2BQHiC7jQMNg4ZbIt5KZ99VifapOJEIxs%2BXQ7SIMvNzhgEao0WqV%2FH7uKAa%2FsXaJmQ7sUgkFow39f5qlyu5SLTwtt96u0i2dNck77Iaq4fEIN0pZ%2FxMNAyZmFNzDh%2FIm9BjqkAaskTpTNGkfo%2F0qKrbMgtkQSBzUAP3U03y9EPByhLwFetyEXxmPAoviFNWZdrYhNQyYg1YymbSApyDS0gNbvAsmF2Jtxw5VrpwnzeynaokLBNYSU3Smf9JjS7lFRW%2BE%2FtyaVtWYVRrpRXSTUsDvERbwoLEZk5Iv8TVnnAa8vzCXzu55kXXUomPti%2FcoQznVGQEZ%2BhVs9Ia2xTRv8t0Vl1LodtUnE&X-Amz-Signature=2523c91dbadc80d881e8954718472d089088e7821d84bbea24ef1f9f32879f40&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Data Visualization Libraries
#### 1. **Matplotlib**
- **Description:** The most well-known library for data visualization.
- **Features:** Great for making highly customizable graphs and plots.
#### 2. **Seaborn**
- **Description:** A high-level visualization library based on Matplotlib.
- **Features:** Easy to generate various plots like heat maps, time series, and violin plots.

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/733d1e42-5a53-4fd8-90c1-3d85254369a6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XCUSNYTQ%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T211341Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEB0aCXVzLXdlc3QtMiJHMEUCIQC6wVIwj%2BhePpgZ5h90QC19PU4fmDaWAdr%2BgSonHRrnUQIgU2ocVFlhwIvoU5equkE2AS5phmZQSk4gxwzzD%2F5oL0sq%2FwMINhAAGgw2Mzc0MjMxODM4MDUiDNQsTCgsPZYgdHeumCrcA0ufNfNrrvv2HP8imJVK6G2QpcGsrEu67PnPEyk4Z%2FVIxt5D6EerPxJu0R6oczsGPvJ8%2BKe0km2hNsNO3npBiT8S9iSJIuELmBHwTlj2h6Iv1%2F4ePDSV7IhQgDF8qPk0xO3hYPb7KVP4Lhns1TZOEs2um5SYaKxvvrVIHM%2Fhy1StUClqw4mQv6v7svxSBRhCT%2FEZvSzotnWW%2FK%2FHOCS6nCAdWtfSLCSmjeeQoxjt69Lm1Qq08xCtBL0Exsnv97o%2FLVU2AJyWJ7Ck%2FeLUFAW8ytT1XZhyxMTwiA7SwjKKn48lCTIzU%2FKzEQmMnUW0VO7Caqo2XsIIQdJjGuUWggyEeh419%2Fk6EmdhS9FQZq5HJ6mU%2Fbgk%2BDKSe7COEDjM1mSqam%2BSfYrr%2F%2FSPrHZnrnly4QiXp9ckWyhAtl9jwueuvjIEAOFTE4m4sbMZt5K9EmRsvTHkx7gNP6S%2F2Y%2FMxb8cOB%2BVYyGnbG6SnzE3ZaLCR0kg5ljzjPwJXwWE%2BugMmlpvK3J5SPmiEOERrrzPQJ16OwrxcD2Y6cCfhS221o3y7s9wFHzynWNvIDWCwEPm6%2F1eMrViwE4EEmZEPTTXg2%2FqaViKqdXWnyY40jJqM3fCxy98E0n8JbGRCIdQ%2FtcaMKn9ib0GOqUBCxEZH49quNzvrAQ7ZN%2BuopkVBxCP4m2a1hRus2K8vZYOO7iQQ1CmwRmVXAUV4r2ErJjtgG%2BDz4cvq7WVFRLnI1FSVgHM9pXXY%2F%2FGfFr4xJKMrdVYkr4ygLeaZ6jTdhDklJFusnF%2BDdTTSsgPA7uedjgFDxwlncb9zn6NZAPFvbEWtYwhxwPeJ5fCUlf9m4DGYaIBXVLXKVu9r4QHcnkvCzdVy5Yu&X-Amz-Signature=f7321c6192830a4502aabd89629c5f5986b162b992f81990b35a4f997ca381c6&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Algorithmic Libraries
#### 1. **Scikit-learn**
- **Description:** Contains tools for statistical modeling, including regression, classification, clustering, etc.
- **Built on:** NumPy, SciPy, and Matplotlib.
#### 2. **Statsmodels**
- **Description:** A module for exploring data, estimating statistical models, and performing statistical tests.

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c62885f5-417d-4179-834f-d68f8f2bdf39/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XCUSNYTQ%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T211341Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEB0aCXVzLXdlc3QtMiJHMEUCIQC6wVIwj%2BhePpgZ5h90QC19PU4fmDaWAdr%2BgSonHRrnUQIgU2ocVFlhwIvoU5equkE2AS5phmZQSk4gxwzzD%2F5oL0sq%2FwMINhAAGgw2Mzc0MjMxODM4MDUiDNQsTCgsPZYgdHeumCrcA0ufNfNrrvv2HP8imJVK6G2QpcGsrEu67PnPEyk4Z%2FVIxt5D6EerPxJu0R6oczsGPvJ8%2BKe0km2hNsNO3npBiT8S9iSJIuELmBHwTlj2h6Iv1%2F4ePDSV7IhQgDF8qPk0xO3hYPb7KVP4Lhns1TZOEs2um5SYaKxvvrVIHM%2Fhy1StUClqw4mQv6v7svxSBRhCT%2FEZvSzotnWW%2FK%2FHOCS6nCAdWtfSLCSmjeeQoxjt69Lm1Qq08xCtBL0Exsnv97o%2FLVU2AJyWJ7Ck%2FeLUFAW8ytT1XZhyxMTwiA7SwjKKn48lCTIzU%2FKzEQmMnUW0VO7Caqo2XsIIQdJjGuUWggyEeh419%2Fk6EmdhS9FQZq5HJ6mU%2Fbgk%2BDKSe7COEDjM1mSqam%2BSfYrr%2F%2FSPrHZnrnly4QiXp9ckWyhAtl9jwueuvjIEAOFTE4m4sbMZt5K9EmRsvTHkx7gNP6S%2F2Y%2FMxb8cOB%2BVYyGnbG6SnzE3ZaLCR0kg5ljzjPwJXwWE%2BugMmlpvK3J5SPmiEOERrrzPQJ16OwrxcD2Y6cCfhS221o3y7s9wFHzynWNvIDWCwEPm6%2F1eMrViwE4EEmZEPTTXg2%2FqaViKqdXWnyY40jJqM3fCxy98E0n8JbGRCIdQ%2FtcaMKn9ib0GOqUBCxEZH49quNzvrAQ7ZN%2BuopkVBxCP4m2a1hRus2K8vZYOO7iQQ1CmwRmVXAUV4r2ErJjtgG%2BDz4cvq7WVFRLnI1FSVgHM9pXXY%2F%2FGfFr4xJKMrdVYkr4ygLeaZ6jTdhDklJFusnF%2BDdTTSsgPA7uedjgFDxwlncb9zn6NZAPFvbEWtYwhxwPeJ5fCUlf9m4DGYaIBXVLXKVu9r4QHcnkvCzdVy5Yu&X-Amz-Signature=68f560d1509749987d27fb88408a531109c4b4ad7062f66acd6e41a75905bc52&X-Amz-SignedHeaders=host&x-id=GetObject)
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
