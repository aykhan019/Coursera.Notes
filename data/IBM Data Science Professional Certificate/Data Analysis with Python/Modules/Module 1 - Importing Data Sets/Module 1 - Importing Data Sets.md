

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

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/997ac361-58a8-4f04-bb0f-79fea4baa761/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665VS2LRKY%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T010938Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDgaCXVzLXdlc3QtMiJIMEYCIQDr8fD4swskztg91Gb6jSJU1FTwJChOc0vaSarPXW5KYwIhAJgY9VMkklRwBUE8G1MTF8xao7pywSTlGV0QRRMao8eRKv8DCFEQABoMNjM3NDIzMTgzODA1IgzNvoDTgqlf%2BBt4PEoq3APVDjrZHxuDdSaLfIdXsdSa9HLK9ElqgpBXFCbafmaoPsr%2F8ik%2FJlHiyZDd4pod8LFyP4TphRPPzidjVGUKAie2xNfjz5gQIK1OuJUnVrjwYL%2B8opBMJB5M3%2BMiX%2BwQvh%2F3XQD%2BAPWJAY66OvivLwVmGSI9z582g9tyjwpjQPFosBbLQpTckgRlE8FaPDpOmCfpqkN%2FLvO0%2FZz4qyVOZu14IurHVj46HuHSHmjMR6PpVmbKMi3TQOjuH51vxk7bAOrK%2B40uuiEyJHHlbNaKspCftpTa4K79ouLnfBtPmxKVT2GemQ5h2BrS2zGQ2HX3ZRZ72cjBg%2FoCH8qm4yFeeGukG3hhgiGS1ThprUJTT8yLv2Jx0MuvyOINnk9crVC8HeAFnJN4kYgJNfiL65Giy7H3KyUTTQtpY0hk3RYhgGtmRcrxiVJHKa7v2%2B7gjTy10bEun3ljCiRhEh8yiQ7ZEygeEcxzARMlLk3A%2FxMDsyrAsIbUsBit1q1valCCnwGQNCh%2BcIB6X0Ni6IwCoPxVgKkzbml4zkDa1Qb0DnOepMyHmNPusUrt9pWCMudmF2U0T9xmSke3ub0ZSikS6x1yLSik%2FAQG7hN1NIQW1g1Pya5Q%2B%2FN0KqATzGWaRdnDdzD66o%2B9BjqkASGklM4daJSdlgArYZcr3kYJAs%2FVf4IX3es9vBZ7W%2BB5JPs6tjN5mu6%2FDc33REPNZcyg1ob500Vj80Rl3I3Xsg46Tzc9F81DrxonY2dsS1Kp%2FjM%2B7jHWS4YKl5D9AxyIAx%2Fx%2Bl8IzcUSSI0bTdem%2Bmr2pg4HOkP6w874kSW05Hf0fkQQJtJRtYLjMDqeOrRyyGQtMBBJIF8oKfB2I6jh6Kr8hjDp&X-Amz-Signature=56f862f7cd22ec446f1b51ab2f62d8bcb18d9a9d22cbd43d180760bd554de22e&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Data Visualization Libraries
#### 1. **Matplotlib**
- **Description:** The most well-known library for data visualization.
- **Features:** Great for making highly customizable graphs and plots.
#### 2. **Seaborn**
- **Description:** A high-level visualization library based on Matplotlib.
- **Features:** Easy to generate various plots like heat maps, time series, and violin plots.

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/733d1e42-5a53-4fd8-90c1-3d85254369a6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666HBC33MN%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T010937Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDgaCXVzLXdlc3QtMiJGMEQCIBtkqMKWZ4g01fLuF1eX3shlBU0vxE5%2FLg05cVBAcZUtAiAb3YUsHjhf5jtDbxaGJPmIn%2FrTW%2BpEtGCJpB3udsytIir%2FAwhREAAaDDYzNzQyMzE4MzgwNSIMM%2F61VG2g8c%2BlsVniKtwDNDxtmJz%2FWWMe5FdKFHyfWajlKubQEhIon%2FFaekI87tYaw0f1S7I%2F9Gsceg8sIrwfORLxxB1wCnKRlbC%2BXtwPgGyyXIha9OSkFkg%2Fc%2Bbel82QvwuXZqz0OYDKpp%2FN4BiWa5kAsbp2zZYMeAaJplpHexaylUNKzgULri%2Bko9icjL3bGhytLWY8tF7JLkKIo%2F8eOYYuOvVk9WC3c7kTTUNvHcmDU5ZtnyOusyq9Ry20MpP8UJVH2q6jaPX7awfp%2FrnZxWyCMGghnQffl1KzGYEg7%2BgeefTrQ0R%2Fhgyk57WhkaQKyS%2FBnWFSHb6hYvrsxANsM8rrn2%2BXV78y4cOS3Y8jWd%2FZ4WGxFT8zfAQ1SWyM5oFuTCTSAzS0zLx1o93Pd0yEjX7Y8nAf3hglMez7pcqiBzQOA31CfdK59Jwh5ROsAtJgbTIF84Umd4FxToMgMbH4DnzOkzq4jXH2JomIPMzFMlw1vQ96TUfpJkp7ZauVUVd6ZfMcKaLQKfZpFrQ4e0PAtRhFkKJf8vPMaztCYrXs8PKEu7LxpsXhP5xcGcDYF4clB4rI32nsSZS6QIbla%2BTUnL8%2BMMm99tHmEOaASiSr9Vg7Z%2F6IYlrLYCnJG0Pc4QoSW%2F8dZPXj5Gxe4icw1OuPvQY6pgGPEI6oI1SiBaf3Pr4jtGRICPHkO2d%2BUsaVNsyY%2Btm%2FkTAlRVa1kx58HqNT0kSOHaGFWJap1Tnok54PkGtnG4ZOmWc5fL2NFrsjdldcLrRS6IhZCcfTRPEaACo6L6p%2FKCWbmK%2B3qvFze7YE5IOjWo%2FRs%2BRbJiq3RSoUA4RLxloVahDTh1ygbsZBqmxZWLdbBtc8%2Bt4ytRKeBuhTtBj1eLUpCrcHimeF&X-Amz-Signature=8d575f4a584bd80b398bf91d6584f13d6e88e2a85d1e309f15048055d2398701&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Algorithmic Libraries
#### 1. **Scikit-learn**
- **Description:** Contains tools for statistical modeling, including regression, classification, clustering, etc.
- **Built on:** NumPy, SciPy, and Matplotlib.
#### 2. **Statsmodels**
- **Description:** A module for exploring data, estimating statistical models, and performing statistical tests.

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c62885f5-417d-4179-834f-d68f8f2bdf39/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666HBC33MN%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T010937Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDgaCXVzLXdlc3QtMiJGMEQCIBtkqMKWZ4g01fLuF1eX3shlBU0vxE5%2FLg05cVBAcZUtAiAb3YUsHjhf5jtDbxaGJPmIn%2FrTW%2BpEtGCJpB3udsytIir%2FAwhREAAaDDYzNzQyMzE4MzgwNSIMM%2F61VG2g8c%2BlsVniKtwDNDxtmJz%2FWWMe5FdKFHyfWajlKubQEhIon%2FFaekI87tYaw0f1S7I%2F9Gsceg8sIrwfORLxxB1wCnKRlbC%2BXtwPgGyyXIha9OSkFkg%2Fc%2Bbel82QvwuXZqz0OYDKpp%2FN4BiWa5kAsbp2zZYMeAaJplpHexaylUNKzgULri%2Bko9icjL3bGhytLWY8tF7JLkKIo%2F8eOYYuOvVk9WC3c7kTTUNvHcmDU5ZtnyOusyq9Ry20MpP8UJVH2q6jaPX7awfp%2FrnZxWyCMGghnQffl1KzGYEg7%2BgeefTrQ0R%2Fhgyk57WhkaQKyS%2FBnWFSHb6hYvrsxANsM8rrn2%2BXV78y4cOS3Y8jWd%2FZ4WGxFT8zfAQ1SWyM5oFuTCTSAzS0zLx1o93Pd0yEjX7Y8nAf3hglMez7pcqiBzQOA31CfdK59Jwh5ROsAtJgbTIF84Umd4FxToMgMbH4DnzOkzq4jXH2JomIPMzFMlw1vQ96TUfpJkp7ZauVUVd6ZfMcKaLQKfZpFrQ4e0PAtRhFkKJf8vPMaztCYrXs8PKEu7LxpsXhP5xcGcDYF4clB4rI32nsSZS6QIbla%2BTUnL8%2BMMm99tHmEOaASiSr9Vg7Z%2F6IYlrLYCnJG0Pc4QoSW%2F8dZPXj5Gxe4icw1OuPvQY6pgGPEI6oI1SiBaf3Pr4jtGRICPHkO2d%2BUsaVNsyY%2Btm%2FkTAlRVa1kx58HqNT0kSOHaGFWJap1Tnok54PkGtnG4ZOmWc5fL2NFrsjdldcLrRS6IhZCcfTRPEaACo6L6p%2FKCWbmK%2B3qvFze7YE5IOjWo%2FRs%2BRbJiq3RSoUA4RLxloVahDTh1ygbsZBqmxZWLdbBtc8%2Bt4ytRKeBuhTtBj1eLUpCrcHimeF&X-Amz-Signature=1f5944918d2627ceedf1900601377f33dce5d389786b03fa0aecd3bba5c3bdba&X-Amz-SignedHeaders=host&x-id=GetObject)
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
