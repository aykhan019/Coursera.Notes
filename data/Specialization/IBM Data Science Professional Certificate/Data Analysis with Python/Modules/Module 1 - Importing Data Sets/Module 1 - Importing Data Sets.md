

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

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/997ac361-58a8-4f04-bb0f-79fea4baa761/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663I64GRKW%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T171303Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQD6ut7enLWjyIBKBYX05PeMvoNBT0nQte8XvLF7yf%2FBOAIhAJExPMxENEJyzfLiwJyOPV8Czd%2BMbaGvUX9SY3HjUIvuKogECJL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igw%2B%2BXpxSd5GJjkpy8sq3AMyI5RE3isjvKONvS2P0epPMkmiy%2BKEmIqbQobDu9fvD4GZrgjPY5ZM7RHDpzmg594MJ0UU%2FVMVl%2Fkyt1olalqqadUNhbUMW3MAgbZB6rhcuUhPIy1a4tQjEYpYqnDZQ8vg7SxMhi075RiOBxCDItURX7RpI3rNp0WEAcyYrv7dDotm83HQnQi06AaYKP0ZWYBZWm2NL5L8WYq6rshRq3tx7R%2BegD3i5Bsu142OQ%2Fs3SB8RLOmME1aKdXuRLEGm98f4RusDWjxqfUvApTiEa%2FChZMhEduHNmqyulJ2RushHsWSGaIi%2BeuZq1Lvz%2FvoZU68oYI%2FYIn5Yf%2Fs%2Bg%2BljnDotkFMC%2BAUCT4poh2JDSs9FgwN3wa5G28AxywSWzOUSOA8x0csspNzRjyv2tnG87hH%2BpkQafkgrg7vrB713EgZfw04HMF7nP%2BeIdPnZJEh6GSX4y%2Bbuz%2BFmokgPfMFDvw8cXuymWEdEVhFvtopVferwQlCP532ydrN1J%2FNCeAUP0ejrZi2hTpXPwcHIsXve4qoYOWiuUjq%2F8fIQ31Zi0QwGzc1nN9XX%2BhdOOPvxujWJWiesXgt6X%2BbHedz3GOHy%2FIuGI0HUde1OOREe1hXSuRqRchQJZa3lnVZQ0aCpEzDfvem8BjqkAbx%2FA8TgPcJddN1vI1nRcNA2g1j62QYYW2LWds6aBJMuen9sblBPt0eikj%2FQqQkpmYAIL3ywKvhnfqtXPjA80Xh8wSVq0j73e5qhwEiuYQp2uqA%2B75k4%2B2fF%2B2%2BDP%2FU6128Yzq0plep9Jwr0puufKKyknoS%2BOiaJkSZthZKxY33%2Fy5lKN%2FSvFTtMx9otcKjBv2Popz7RbnpV0Bj6bZSaCiFO%2FWkx&X-Amz-Signature=7fd3b5bf6e42896c002f2fd588d3a4497414e3bfac8ede2f4352270d9547cbff&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Data Visualization Libraries
#### 1. **Matplotlib**
- **Description:** The most well-known library for data visualization.
- **Features:** Great for making highly customizable graphs and plots.
#### 2. **Seaborn**
- **Description:** A high-level visualization library based on Matplotlib.
- **Features:** Easy to generate various plots like heat maps, time series, and violin plots.

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/733d1e42-5a53-4fd8-90c1-3d85254369a6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TLT2DRD7%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T171301Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDy12FJRdNEKtuXZVUbx6y8aEWSLU8oFZY7uuG9hqb6tAiEArkZaUAWN5Q8c%2FaRNHmGhE3WI4C6iB8B8t%2FpM%2BAHxSAMqiAQIkv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDEabr5OUpIM8xVPreircA9lm6tG5cS55oRHNWlpi%2BwO4RBLVJWHAGqlAAIkGdD61O%2B7zuwrj7%2Bl3a66KfVww7RbcyT5ud52zzLbnGgSFMaC5%2FZnjOYlWWwZ45uqGQMJtShIPVEhOUMmAv8yLOvcAxcATBGv1HaHct05FQIdTxb%2B2vJA3tMl2IX1WWUxobN5FGagQHlJzHSOLawE5UaC39%2BJT67NWDkXn86dr2Ji6COHywsoeFkNvtIMQPvOEFtyN5VghVYfKrLNBzlWolK%2FGQ2IddmxCA8DZC9UxeJ98NWW2Oko%2FHdpferkFTNTZJYaTqmsDKrZkIxSqxw%2BdJpJ1IJUE3WGhqtkifyBoldtUCi771vDdRHbSAXKhN2wtv8%2FpxUgl%2BiJk1S3fi8R445XO2J52hqo09tm%2F8o%2F4awaY1VvjEveylaM0q78pcRu1%2FAZXbUeqrlxiFyc0w1DXvBKfZdNSfzNHNX5YmHHlE%2FTLS0Kl5Z5%2ByjVIEQxewBhA8gWL5ZCrRwl1HUED3n6ze%2FxybHNSCCL1QJwb6OeryPtnMmBhwlbckciay98wCzbvcdWnUcOFIoTKwgE2NirGQrUm8XSm0%2BVdYcOVkZx9cEGF1x6V1AXWaHIa9O1a9b%2FCKJ8N3wA7DaGimXOUVLnVMJu96bwGOqUBRkcqljpUvWMlgW7PS%2Fmog%2FejjcY3kKhppKUOSY7F%2BiZO8AxLOdtFBf7%2BSuzgUZtO26KyWMmgUIsY4F9O3UOELPrCbvuvduSyx5dIWfSbEOk8FHhk%2BTk5qL6DcNlVtHF47VXHEbIrdxgSrOkmDd8u9kIzqs0g1Upt7ySvhZfh4WEC6aLwGKdKejjGEP5lP8v8zwO6jMu4EIzJQOxJEO1Pl7cVJYnr&X-Amz-Signature=c9430385b3f2cb9d97ee12a1c0afc9f343f8a4431ad98d7140151541084b9fc0&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Algorithmic Libraries
#### 1. **Scikit-learn**
- **Description:** Contains tools for statistical modeling, including regression, classification, clustering, etc.
- **Built on:** NumPy, SciPy, and Matplotlib.
#### 2. **Statsmodels**
- **Description:** A module for exploring data, estimating statistical models, and performing statistical tests.

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c62885f5-417d-4179-834f-d68f8f2bdf39/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TLT2DRD7%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T171301Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDy12FJRdNEKtuXZVUbx6y8aEWSLU8oFZY7uuG9hqb6tAiEArkZaUAWN5Q8c%2FaRNHmGhE3WI4C6iB8B8t%2FpM%2BAHxSAMqiAQIkv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDEabr5OUpIM8xVPreircA9lm6tG5cS55oRHNWlpi%2BwO4RBLVJWHAGqlAAIkGdD61O%2B7zuwrj7%2Bl3a66KfVww7RbcyT5ud52zzLbnGgSFMaC5%2FZnjOYlWWwZ45uqGQMJtShIPVEhOUMmAv8yLOvcAxcATBGv1HaHct05FQIdTxb%2B2vJA3tMl2IX1WWUxobN5FGagQHlJzHSOLawE5UaC39%2BJT67NWDkXn86dr2Ji6COHywsoeFkNvtIMQPvOEFtyN5VghVYfKrLNBzlWolK%2FGQ2IddmxCA8DZC9UxeJ98NWW2Oko%2FHdpferkFTNTZJYaTqmsDKrZkIxSqxw%2BdJpJ1IJUE3WGhqtkifyBoldtUCi771vDdRHbSAXKhN2wtv8%2FpxUgl%2BiJk1S3fi8R445XO2J52hqo09tm%2F8o%2F4awaY1VvjEveylaM0q78pcRu1%2FAZXbUeqrlxiFyc0w1DXvBKfZdNSfzNHNX5YmHHlE%2FTLS0Kl5Z5%2ByjVIEQxewBhA8gWL5ZCrRwl1HUED3n6ze%2FxybHNSCCL1QJwb6OeryPtnMmBhwlbckciay98wCzbvcdWnUcOFIoTKwgE2NirGQrUm8XSm0%2BVdYcOVkZx9cEGF1x6V1AXWaHIa9O1a9b%2FCKJ8N3wA7DaGimXOUVLnVMJu96bwGOqUBRkcqljpUvWMlgW7PS%2Fmog%2FejjcY3kKhppKUOSY7F%2BiZO8AxLOdtFBf7%2BSuzgUZtO26KyWMmgUIsY4F9O3UOELPrCbvuvduSyx5dIWfSbEOk8FHhk%2BTk5qL6DcNlVtHF47VXHEbIrdxgSrOkmDd8u9kIzqs0g1Upt7ySvhZfh4WEC6aLwGKdKejjGEP5lP8v8zwO6jMu4EIzJQOxJEO1Pl7cVJYnr&X-Amz-Signature=c9457a8041698652f26f5aa3a46dd2d3dd9a29bbafff06c07335e9fffebbf04e&X-Amz-SignedHeaders=host&x-id=GetObject)
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
