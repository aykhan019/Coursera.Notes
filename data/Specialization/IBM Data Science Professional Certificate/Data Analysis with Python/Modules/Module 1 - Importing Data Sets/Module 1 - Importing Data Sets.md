

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

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/997ac361-58a8-4f04-bb0f-79fea4baa761/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663QCHYBTM%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T221402Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEI7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCID8%2FfF7m9%2Bz3sgzwh4urulhvMeeQ%2BIRam0iJLQSCQR4qAiEA6FdDspjNgcKegTKgEl51KN3lzj9pZkmt8Y%2FIXX5uXs0qiAQIl%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMMJk8NpSzl0w%2BaJoSrcAwAzCN05wcJmTAxyXy72I8n7VQlp%2FCIOLNYnxNoKrGlQGVlIIRdYqbi%2BIeFDCaNfQw9ntYw4Gq3ihSMy4SK%2BIzSLJXLiz4mE9OqSprAw8H3tbKZnWf%2BQiy40Ow172IhKGUlU6XYd9TUlprPmMQGCOqXhcqOeaxGBirS3CcPr8PYH21MmGWtp5HIDMMxModM59T%2BA56kG7Mv463Pfy0exXa6TeRfWkmL7KCIDeDzfv5aJQWh1CEXZ05%2BPZqmVe7vzG6FtetsKcSI%2FXpbTjEAinpe4txlYgwhhOUMFdQeOj4Fx5FTyS7Ug4tOwuo0KMGsvk%2F49EOV3ekcUbcjuBcAa30tv0MA6HxutNy8WNOQ3n6kqBTPsIZx96FotLVauKcofwIWJC7D5sq%2BdZxekHGWWZRy7uEurra6%2Foija2NBMrMr7zG7pWGccait469B00BJ5%2B7JvVUG41fMqT1UMNeTIl%2BCtmsgycbpEYUoVlDlth9isg48y75WBzTVUdn%2FOUID2wjxnHeyH5Sn4QU2Wiq6R1uI53HCFu8l%2BUH4frT8wlVlBYP1xTqZvDY7oQ7HL1SjbSs3nmW0adfGeTIX1Mm%2BaUjyJajhy19WxqwNaJWefWj%2FZu2fVSmao2WevA3yiMNLF6rwGOqUBdpQZEOnJJZCrqPqm%2Fnn60DaLdFmbDa1yXom0F4KKzmNK%2BAwYpoGNnEFQonTinDbV5iihQFXLXp5kEbqWCwDGpOuE6Usy7cfJLIUdMQ%2BE8Dz4bb7%2F9WGdh5GWNBLTXE5JOFbjzuc2josrl7QGXHN0sg4EceMDOP4v8XGDuDXZO1HKlwepmuaXME5oDHX1zyyDA4Q8DDpKwLt6e%2B1u5Iapkk0Ru8uC&X-Amz-Signature=e871a9a8b9b3abc29083b707bbe1d62937e867e6583cd5170369136fa80fff7c&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Data Visualization Libraries
#### 1. **Matplotlib**
- **Description:** The most well-known library for data visualization.
- **Features:** Great for making highly customizable graphs and plots.
#### 2. **Seaborn**
- **Description:** A high-level visualization library based on Matplotlib.
- **Features:** Easy to generate various plots like heat maps, time series, and violin plots.

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/733d1e42-5a53-4fd8-90c1-3d85254369a6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667H34HZUB%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T221401Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEI7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAbxw2nexdp23RpQhjfvM%2FAoejG%2FsVm%2BgMOXsku%2B%2FibwAiEA527U1MuvT9M9BrC0KHB9KyihsD%2BJtVlWkB7Iv9zLADIqiAQIl%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHIXnLEVAj0URRNAPSrcA%2B1%2FYK6VTNbFoose%2BOmDasEZG98JPXYqYvjcE0JCSJMT0T%2B4xQ2JEYjOrb5PLXzpWbqY4SEoIC4SlY16OqRv4EOjP7SSMUsb2RNITbnOqRB%2FfsEH%2BmoppcT3v7InMYe0j75CWkOJTohGfnUXfa7%2BqOT5SN1FJ6j9vBPx58g5oUlAulgvrUeMcHwBbu6MbDQ1xqS%2FB25RMALQHhhZPWKTxjl%2BEOOX50T35OBLea2MyS%2FKAoJ7AarMrnWSMj4MaPibGyKJOeOqtYTWDNlDF%2BWENPDdSOcC0MT%2Bq363lZerM9L3bITbADIKEBLeZrdmLXt%2BdP4MeVHEh6xc1j8TZt4AYwchu5C1vOs9PaJtETwMRcjcfbr5kWdpqooCIlVKUMaaygEdkVTN1L5Lw0cHBUxO9Hd%2BR6PQV21stOKFNPEDjbSnxu0GKsInXjuICSDR8BEiaGYXx1nVSpSRoxpeQi%2F58IXTIOvhPnXr6MDnHIlf2sBYHQ%2B0x%2B61xuAJIEb1JkHRgp2hGoMbOe4zVbvCOpJK7edbxfnCzFAlK%2B%2FIhaE9NMHIZUX7dhC9cx%2BpfMnmonZyguJt4KFCvClqhHxC9yWf%2Bl%2BXBYlX00KOGlyjPpFPI47baqS4X5Iw6jKPcRnFMPHF6rwGOqUBYvde4hmGdNbDfX76vG%2B858NE%2FetjiiM5vOO%2B%2FMDCXPNWRRR9vWz8l8EeC6okD0vO3F29v%2BGugeEbuqCsZYvJfpVtuzToQ1h5wI8rTLDdl1HwvLi7GJRRf%2F%2FL2D1SoLfxz%2B6tve6joDTwlv31kXAAPN2Eoi2b%2BOUQl87gjvEj62BpFel%2FyVJRHFNwbBPolEcpJxLA6Qq3clT2MkJFuDgMRI2Iljst&X-Amz-Signature=fc9f13860d261070d93dd7dc7e92218ee4178cb90bdb7b353438407c4a1701d8&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Algorithmic Libraries
#### 1. **Scikit-learn**
- **Description:** Contains tools for statistical modeling, including regression, classification, clustering, etc.
- **Built on:** NumPy, SciPy, and Matplotlib.
#### 2. **Statsmodels**
- **Description:** A module for exploring data, estimating statistical models, and performing statistical tests.

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c62885f5-417d-4179-834f-d68f8f2bdf39/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667H34HZUB%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T221401Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEI7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAbxw2nexdp23RpQhjfvM%2FAoejG%2FsVm%2BgMOXsku%2B%2FibwAiEA527U1MuvT9M9BrC0KHB9KyihsD%2BJtVlWkB7Iv9zLADIqiAQIl%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHIXnLEVAj0URRNAPSrcA%2B1%2FYK6VTNbFoose%2BOmDasEZG98JPXYqYvjcE0JCSJMT0T%2B4xQ2JEYjOrb5PLXzpWbqY4SEoIC4SlY16OqRv4EOjP7SSMUsb2RNITbnOqRB%2FfsEH%2BmoppcT3v7InMYe0j75CWkOJTohGfnUXfa7%2BqOT5SN1FJ6j9vBPx58g5oUlAulgvrUeMcHwBbu6MbDQ1xqS%2FB25RMALQHhhZPWKTxjl%2BEOOX50T35OBLea2MyS%2FKAoJ7AarMrnWSMj4MaPibGyKJOeOqtYTWDNlDF%2BWENPDdSOcC0MT%2Bq363lZerM9L3bITbADIKEBLeZrdmLXt%2BdP4MeVHEh6xc1j8TZt4AYwchu5C1vOs9PaJtETwMRcjcfbr5kWdpqooCIlVKUMaaygEdkVTN1L5Lw0cHBUxO9Hd%2BR6PQV21stOKFNPEDjbSnxu0GKsInXjuICSDR8BEiaGYXx1nVSpSRoxpeQi%2F58IXTIOvhPnXr6MDnHIlf2sBYHQ%2B0x%2B61xuAJIEb1JkHRgp2hGoMbOe4zVbvCOpJK7edbxfnCzFAlK%2B%2FIhaE9NMHIZUX7dhC9cx%2BpfMnmonZyguJt4KFCvClqhHxC9yWf%2Bl%2BXBYlX00KOGlyjPpFPI47baqS4X5Iw6jKPcRnFMPHF6rwGOqUBYvde4hmGdNbDfX76vG%2B858NE%2FetjiiM5vOO%2B%2FMDCXPNWRRR9vWz8l8EeC6okD0vO3F29v%2BGugeEbuqCsZYvJfpVtuzToQ1h5wI8rTLDdl1HwvLi7GJRRf%2F%2FL2D1SoLfxz%2B6tve6joDTwlv31kXAAPN2Eoi2b%2BOUQl87gjvEj62BpFel%2FyVJRHFNwbBPolEcpJxLA6Qq3clT2MkJFuDgMRI2Iljst&X-Amz-Signature=57f761fb6be3a16d46305a45fec522dba0d4b19f235d29d4bba2441ed2fbc4a5&X-Amz-SignedHeaders=host&x-id=GetObject)
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
