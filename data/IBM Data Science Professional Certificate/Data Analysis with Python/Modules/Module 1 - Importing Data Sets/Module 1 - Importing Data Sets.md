

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

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/997ac361-58a8-4f04-bb0f-79fea4baa761/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TSP6CBUC%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T010833Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAkaCXVzLXdlc3QtMiJIMEYCIQDnWevVPnM1ghyZb3dFfTz5oPhhD27K%2BDcs11NZ5KoRKAIhAJQdrtAC6c%2FqwPO2yGDJUTaKlPOfz4zaYoQE6aEt7xYbKv8DCCIQABoMNjM3NDIzMTgzODA1IgzX0ToF%2BLDVbmKiuSwq3AMvFL9qs9NLvKRCT3BUvzMVH8HXAt%2BtF28SHrr67B%2FtvSeVZLW7tu0QvXbAXclik1BGAUM%2FtT6f7AqP4x2t3Xgk7sWj1KzjlS5DLacW50or51CJW2xVClG6zNLvmlT%2BI7ehq8SeEUSi%2FqOCWc1IUQP4qB91IyD2I2CEKnt1%2FW17FegtMHd%2F8iBrb%2FxUeEGflB6jvur64gVs7rxuxQH59MgtjVROUkPB3PimGMbQYbMFrnn899C53G%2Bv48rh501DBxa3WJw%2B6NJo3wwbyg6iSWfS4HMTZHUEEnZmnKLyQseIKyaQLrwRN64K59UqOwi9RA3RGyqKrr8qD53RQfp2eSsfRJBkl0bH82e7sc8M9azEayHZk%2FhiWgOK20VBDcf3oJsavG1qvfJ40ZH1P4DlEXknuJGaVcZ20hQd0KplXU%2BD4jFRFmaEL04cZOnL7azrMJ%2FvcjFqHJbJzCrf5LTpCpWu%2FpoInnfM0gNqh6K79ZQ8ZPaYVDBphnEgvAYl3FfiyB5Vl1%2BY1ADt%2BwclMp0ToehEWeRLTyLGEPV6afUHQacoS5fx%2BmABhqyjyb82QoTh2UEBUvyF8br%2F9a8AHGL%2B%2F0IJDEkT%2F7jsymfmjd3auF0VVKQZ6pALctGnV0HT6TD5zIW9BjqkAXZKCwf7X9RiSZIuwvNO%2BkSvGemTB5KRz8Hd%2FnmuN1uH4MXNi7dETJJ36tcBJJBm97jQ0cT1O2Q7ixJVcNRtKsgXUgkMvv2bI2TqeDdgCpZe0YD%2F0THgZTIrQs%2Bv50Tkv5%2B7XzeaXWIy%2FQQ4po5Ie2RszQKbfLL9T%2FPfAi%2FtqDf7r6w%2FaGinRrO%2BfF3VD8moF2wOY1wTNc5z%2BNSMOTkqC2%2FSCW1P&X-Amz-Signature=d9ad7cfc8b82f783536085dfb07fac241ccad242601096cce81b6986c7943f9b&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Data Visualization Libraries
#### 1. **Matplotlib**
- **Description:** The most well-known library for data visualization.
- **Features:** Great for making highly customizable graphs and plots.
#### 2. **Seaborn**
- **Description:** A high-level visualization library based on Matplotlib.
- **Features:** Easy to generate various plots like heat maps, time series, and violin plots.

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/733d1e42-5a53-4fd8-90c1-3d85254369a6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667LQVIXP5%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T010832Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAkaCXVzLXdlc3QtMiJHMEUCIF4ar1TS4o0YMQ1iWjdLrCQzi5CXUIWV7VVHiIkzu5EKAiEA%2B4G4Z%2FqXDvaQMCANU7NO2IBiEZV7igF2Ev3RnPBoinsq%2FwMIIhAAGgw2Mzc0MjMxODM4MDUiDBBRADtOOYK%2BF83hTyrcA1Gt6GFO2o93n6FiNf%2B4ESFgch0xOkQhe9zZBcDPwgVtJbNzvRcBhHMmoCussu2nGIGfWzPjF95o9susQgp4wMEr4owcNnhi%2BS%2Fk1y8tSf82y1rIsLulWSltJ%2Bsz8cMOsLSej9bj05YntTCQ5%2B1EX7TgwbTfBq9vyQZfB%2But8l7wE8rLMY0DdZD0TM2la07Xses9fpbKiqZc3qAqI47UEQHWQ1pAcoqZqn1U2uz0Uo%2ByF%2BDlaTRG%2BxjVkAHDnJlDneXmYyJAoKjLooReJTpnKI%2F2LDxB9jXBg9teB2fCr9uBvry8pN9dvjrHUg0a1YCGn6kicWSmtK1vM%2F7VTA00fatbGG123zJ3WWa4%2BFnH2QzPgs5iL97Im6CtdYnPprP%2FwU1Gx9Y%2F7iGrcjvSGYDOlBLKl1lLJfnhf8LVUgLcRokHCKIzwG2kpgSfVtmPwcPnN%2FiMGCX9Zcx7abgELbo7nD6Wikwuzfn%2B4PK%2BPDVEzPxJX4yOLrB3hccUHirezZhOTJG5Rn4zZo%2FNVjMIVJKTKzla8KAIWYS5tRPxKYFH6jNqtpLJMSbjnP8u4nMDQ%2B3DWKtjrEhpyFJBgipIVx1c5pn7UCCXOK6fe%2FxNQUCmhX9XSO7URWsQg1S9bir8MM3Mhb0GOqUBHnjREPdhnu1Dq%2BZbnIQzAkKDUQQAIpslOkkriPzETbgfQoismeB7woJqGNK%2Bf8j4PHQTrdDtZzRV2yoM7TcKgL9Gq0kjTWevP%2FFu0l1Dd3ktE2RqPi%2Bj0m0oMQ3IQ3syYECRANJ7yCMTWNEpVhzhzZ3IikeUKNJIIqV6clqXbrUOX4BeWxhI9%2FGSRVCw6yboRoRbHFom4ytB1cFCQDZK6ElJtME9&X-Amz-Signature=ee6b1c4cc98907299c4b9fdf320894fd43467097a239f87371c6928d33843ea6&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Algorithmic Libraries
#### 1. **Scikit-learn**
- **Description:** Contains tools for statistical modeling, including regression, classification, clustering, etc.
- **Built on:** NumPy, SciPy, and Matplotlib.
#### 2. **Statsmodels**
- **Description:** A module for exploring data, estimating statistical models, and performing statistical tests.

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c62885f5-417d-4179-834f-d68f8f2bdf39/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667LQVIXP5%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T010832Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAkaCXVzLXdlc3QtMiJHMEUCIF4ar1TS4o0YMQ1iWjdLrCQzi5CXUIWV7VVHiIkzu5EKAiEA%2B4G4Z%2FqXDvaQMCANU7NO2IBiEZV7igF2Ev3RnPBoinsq%2FwMIIhAAGgw2Mzc0MjMxODM4MDUiDBBRADtOOYK%2BF83hTyrcA1Gt6GFO2o93n6FiNf%2B4ESFgch0xOkQhe9zZBcDPwgVtJbNzvRcBhHMmoCussu2nGIGfWzPjF95o9susQgp4wMEr4owcNnhi%2BS%2Fk1y8tSf82y1rIsLulWSltJ%2Bsz8cMOsLSej9bj05YntTCQ5%2B1EX7TgwbTfBq9vyQZfB%2But8l7wE8rLMY0DdZD0TM2la07Xses9fpbKiqZc3qAqI47UEQHWQ1pAcoqZqn1U2uz0Uo%2ByF%2BDlaTRG%2BxjVkAHDnJlDneXmYyJAoKjLooReJTpnKI%2F2LDxB9jXBg9teB2fCr9uBvry8pN9dvjrHUg0a1YCGn6kicWSmtK1vM%2F7VTA00fatbGG123zJ3WWa4%2BFnH2QzPgs5iL97Im6CtdYnPprP%2FwU1Gx9Y%2F7iGrcjvSGYDOlBLKl1lLJfnhf8LVUgLcRokHCKIzwG2kpgSfVtmPwcPnN%2FiMGCX9Zcx7abgELbo7nD6Wikwuzfn%2B4PK%2BPDVEzPxJX4yOLrB3hccUHirezZhOTJG5Rn4zZo%2FNVjMIVJKTKzla8KAIWYS5tRPxKYFH6jNqtpLJMSbjnP8u4nMDQ%2B3DWKtjrEhpyFJBgipIVx1c5pn7UCCXOK6fe%2FxNQUCmhX9XSO7URWsQg1S9bir8MM3Mhb0GOqUBHnjREPdhnu1Dq%2BZbnIQzAkKDUQQAIpslOkkriPzETbgfQoismeB7woJqGNK%2Bf8j4PHQTrdDtZzRV2yoM7TcKgL9Gq0kjTWevP%2FFu0l1Dd3ktE2RqPi%2Bj0m0oMQ3IQ3syYECRANJ7yCMTWNEpVhzhzZ3IikeUKNJIIqV6clqXbrUOX4BeWxhI9%2FGSRVCw6yboRoRbHFom4ytB1cFCQDZK6ElJtME9&X-Amz-Signature=07d79a654dadee20de7c4e470ea679689741a78cb22453a2f27c93ac29a5ce4f&X-Amz-SignedHeaders=host&x-id=GetObject)
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
