

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

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/997ac361-58a8-4f04-bb0f-79fea4baa761/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TEPPOHZF%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T132042Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGDFWCgAC3yCyUNUMQ5%2BnJ78FTo8C2DztbvG1O9ScZelAiEA%2FEVij4VCxOoWE22ve2MmaiGInYANIma8Vay0k%2BaO6WoqiAQIjv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDA9DYV7ZywLHEDh%2FlyrcAyI3Au8VoXQXrtNoiztxSF8hQqsdqlw70i0NlEPkiRxYYAXZPh5Jm34ihze8IU%2FPvk6%2F2RwdVSymNAlkHkEEHv9j%2Fm1BKC1BoOi1GMAEErzz7VF6bV6JSPiU%2B5h3Yr1zwSZ7eiZNcSrAk5n02vnCUud7bBoX7n1gWhvPtWW9Uml%2Fu1v0aem%2Fgeds47Dz1MsTyDgtfyQwttOjvk%2BSV3oDj0vkRh90uUSEQfp9i4JgDPK4576xXtuD5wni0XUus544b03lORgVYdXTspaKLvyzbb3gcDwHefD6JJeWIaQ0cvIxr1gzIcdV59x1OvPpJzVmb5SNdakmk2KewRjbJuDe75H1XYTVwTt2L5e7pJNIYOlSrusg3fcEo5FgX6cxyOxb58tqKCcQZuCE7yyqJ9UHz2nqg%2B7aBRprhVL%2F0cHRulNBEtcMJRGSu0sbr786OFIVS0lIX%2BUZMrs6sXar2coH%2BQBHP7g1LHkaXAb5o9GHS4aqsOl5rE89WToLxBcBQ%2B%2F4VmwVIHDkrpdYcasznSBVn7WFVcdfyRBRIhZE4d6Jj9vCpqp8zs%2F9O%2FKjqhsWE96re1ggwSKx%2BNss49Yq5UlXqCxTg6LjvvhTfSKAmkPCwqXhHnNUkieAvXsjz3XgMLnL6LwGOqUBkI2CC6VpcF5NG3NRwiz0BPUW7qvCB6OvtI65lfk2nm7rXDR%2FkLQmK%2BIwg1qiMKTzaPc3F%2FNETJTFkn1Z%2BHj6w6UpwKhvx%2F3maqImbwjGCXNnvIsAJl9MGBwk9oiFfeDg4yweKK3HQ7HSIfojPo1kU%2F2DexeMByKaPkWE3OGxeb6EvbPSw00uShyJiFgM4X14%2B0LZ2UBl%2FBvgq0bAYXEUdMNKun3t&X-Amz-Signature=23c1fbc294de3598e6e0a05d4df6e7bfd84238202486dbf17c462f2011e7e8ed&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Data Visualization Libraries
#### 1. **Matplotlib**
- **Description:** The most well-known library for data visualization.
- **Features:** Great for making highly customizable graphs and plots.
#### 2. **Seaborn**
- **Description:** A high-level visualization library based on Matplotlib.
- **Features:** Easy to generate various plots like heat maps, time series, and violin plots.

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/733d1e42-5a53-4fd8-90c1-3d85254369a6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466S44UW25Z%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T132041Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDIOhA55EjiNicj%2FCy7%2BaMd%2BSu1DIkRLkHo3aAjzYnINgIgbZyqfxmdiFWGNO3bkOHYxJOhgMEv7j3o9wXgwfeGGsYqiAQIjv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKP1IrqO5plza3mqjircA02Atqsd2AmWg6DUvDju1ExtsxtvnWe8n546y2aUqM3uOSsuDFncLd09KwjL6EFOImsaNVsIUWUAgzpfUEGHayLH8dpNPuNcG92KR%2FBuiuUuz9xTNZrvCpLHO5cftkABL5wrrMDcciy7Bne2%2FTXVl9qSu4997%2F5CSXFxnVWddcrdLaBnpHNhxdzR2%2FlC9orPV8H2MuZCrit1r205eVMtihaOkA0B0U3%2FxSQdA7GcP2b1DC2Umvgt7C5ReI80x3JYcSLLkX20kYFik1HA%2B2xqTu7%2Bja3yWZtdXZjCQV%2B%2F7eQYKv7VAZsPGUkwRMekZvpcG385nqDNNlnqVIZlDtg5OofxIUNIuCjKcQIPELNgRdoYcWPVSbZTi9iXCAM2vtxhl7R0hLNYmD14gj%2FzGHkgspnA3UePrktN%2FB1TiK6MlnQwcywWNSc2n0PRXo9rZ6cx%2FmIqzNZL7LwUhHsfKwqznSXHnp8qnuWjFdaZZMlufArPu%2B7xSBW1QAeckwYk4ymubPoh4F1ZdISYv%2BFj6wDyncxiAIn2XdVqePtba2xLy0hgp5Hx84kykZW508VrCInWniYhU4FziQoY53%2FJ5SveZq4qE4Ml6BW0IlruhWWfkVXuItu0yFtJABJwUK62MNHL6LwGOqUBHr18f%2F1LipR38M6V%2FKTZ36RxhqJakVS8fxXLPz1%2FNaUx7DY7mKdSWG6%2Bk096%2FqbHo1yKIA8Gu8duFadNhtd1edQMvFzxHhaFStWcMdLiZvLME0FTDT3N5ccBpiM4i3PLMUHFiYLO%2BxOhgDSp%2B1G%2BSsjRv0zqSr%2F7PZ8%2Fz%2FQyBezN6ETPzZQ03BgCEDalfV2nTY3CQV%2FiG1YGCnHN6Z%2BTWRwukEJQ&X-Amz-Signature=fea2be615aa7d68b90af932fd6c4849f41a5d7763ea0636866592d0403d84de0&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Algorithmic Libraries
#### 1. **Scikit-learn**
- **Description:** Contains tools for statistical modeling, including regression, classification, clustering, etc.
- **Built on:** NumPy, SciPy, and Matplotlib.
#### 2. **Statsmodels**
- **Description:** A module for exploring data, estimating statistical models, and performing statistical tests.

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c62885f5-417d-4179-834f-d68f8f2bdf39/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466S44UW25Z%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T132041Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDIOhA55EjiNicj%2FCy7%2BaMd%2BSu1DIkRLkHo3aAjzYnINgIgbZyqfxmdiFWGNO3bkOHYxJOhgMEv7j3o9wXgwfeGGsYqiAQIjv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKP1IrqO5plza3mqjircA02Atqsd2AmWg6DUvDju1ExtsxtvnWe8n546y2aUqM3uOSsuDFncLd09KwjL6EFOImsaNVsIUWUAgzpfUEGHayLH8dpNPuNcG92KR%2FBuiuUuz9xTNZrvCpLHO5cftkABL5wrrMDcciy7Bne2%2FTXVl9qSu4997%2F5CSXFxnVWddcrdLaBnpHNhxdzR2%2FlC9orPV8H2MuZCrit1r205eVMtihaOkA0B0U3%2FxSQdA7GcP2b1DC2Umvgt7C5ReI80x3JYcSLLkX20kYFik1HA%2B2xqTu7%2Bja3yWZtdXZjCQV%2B%2F7eQYKv7VAZsPGUkwRMekZvpcG385nqDNNlnqVIZlDtg5OofxIUNIuCjKcQIPELNgRdoYcWPVSbZTi9iXCAM2vtxhl7R0hLNYmD14gj%2FzGHkgspnA3UePrktN%2FB1TiK6MlnQwcywWNSc2n0PRXo9rZ6cx%2FmIqzNZL7LwUhHsfKwqznSXHnp8qnuWjFdaZZMlufArPu%2B7xSBW1QAeckwYk4ymubPoh4F1ZdISYv%2BFj6wDyncxiAIn2XdVqePtba2xLy0hgp5Hx84kykZW508VrCInWniYhU4FziQoY53%2FJ5SveZq4qE4Ml6BW0IlruhWWfkVXuItu0yFtJABJwUK62MNHL6LwGOqUBHr18f%2F1LipR38M6V%2FKTZ36RxhqJakVS8fxXLPz1%2FNaUx7DY7mKdSWG6%2Bk096%2FqbHo1yKIA8Gu8duFadNhtd1edQMvFzxHhaFStWcMdLiZvLME0FTDT3N5ccBpiM4i3PLMUHFiYLO%2BxOhgDSp%2B1G%2BSsjRv0zqSr%2F7PZ8%2Fz%2FQyBezN6ETPzZQ03BgCEDalfV2nTY3CQV%2FiG1YGCnHN6Z%2BTWRwukEJQ&X-Amz-Signature=81a75626b4c81529300a95514dfacd963d20c57975d197082452f8300a76cf16&X-Amz-SignedHeaders=host&x-id=GetObject)
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
