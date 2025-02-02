

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

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/997ac361-58a8-4f04-bb0f-79fea4baa761/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667FK2OG2K%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T071237Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEN7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFNmAHeDNur4HuqD%2BRmM8%2Fwy1YpOdoMHuOE9ZdUaG0UnAiAPmx%2FlRvxJLcBV5PfaImPRi%2BETM32czg%2FFvHD7oOACkyqIBAjn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMC4imzbncNNS%2FV7bAKtwDVS0CZhb4Yhuz9Ehtf%2FqH9LsuNL8JjYncbjQk9nLKeusCqCvU9ZpG0MP9wgAjrFzASRw0qW3YZI1iMBQR3TX80yWYhB53EfgcmwdqgqCP5DdC3PEovNAzV0NU375XHtSDFSLu9V3f41MLt8ISXbmG4jtFPh5Yp3ksJZ5yJr7xBraLnqMowiiMDvR17rqSCY5sveafNA4%2B7d8TkT4%2BMrqsOuxOxgoo%2BOIbVO7h%2FCVRHIwaKIxaNSRAIRep5dvf9BxLvwnh0npM8yLZuV%2FOq1hYA9gqvgR0e3PUW3XE5M416nO6aIglDXdgzDoHxFXblM7%2BbXlMaEKP8VDgOgfgBpJNblllDeaDFmitO0aXdfVfhkkRbHInd8KQdaJmf53KVMd7LKb5VHVgH0QeqY8%2BK9740AM%2Bgae1fbp0dGuTuTXpoPmAOSS%2BLYu%2BfGWhBPFC3MN6xQB%2BT9l8W1Czz1HI0h9j1amCu6w%2FsALJzkgUdjR5Q3ozB7LddPy1lUGySrU37fDTGOJ9IiTFvDz17E%2B%2BA%2F8Scl4rx%2FNH7xlXoIdsbwr8%2FW6t%2B2B7V8TP4%2BNzTzJtXa0ceYHdSzXf%2BaGjku6dKWCXZZQP7Z1uttbxkAzVmC%2BsvjdjfYR2ASRGCkle28Ew75v8vAY6pgGrP5aQqLDMmAKs3senktfiQaqk%2BSUaAwIraoBLJw%2B1xZy6SHsAP9u7ds5dLQsfhlac4bPzQ8Yh%2B4VDmAqtq7%2FtrukXfSR7yhuCXMSF2tckzGIPUVO6AJhJ2FS4R2Ajmveyo2OcVcXQO2S7iHnMK6NNIs0nST4Eibpqzwrw1ud85vDNeP84UFANVeolvB0KoI8fOGBlGxlPEUpAtXntsXzZ%2FovPStzR&X-Amz-Signature=d3c748244a9d224b857c6852e09aad973862b5b3268630a16435ba93b37be957&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Data Visualization Libraries
#### 1. **Matplotlib**
- **Description:** The most well-known library for data visualization.
- **Features:** Great for making highly customizable graphs and plots.
#### 2. **Seaborn**
- **Description:** A high-level visualization library based on Matplotlib.
- **Features:** Easy to generate various plots like heat maps, time series, and violin plots.

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/733d1e42-5a53-4fd8-90c1-3d85254369a6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YMBDZZA3%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T071235Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEN%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIAyp23yldCLQAMW5zxDzzGQBf7xe2A3yDd1dfgAtCLJzAiADagUyGw7FQITwghjWoaaaueM99Eactv38PcgTO%2FjdvyqIBAjn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMs1YbGgNLqQCf3%2F2MKtwDS2cN56%2BuOVgu%2FzBslqmKztySpuTBO1DRjzwCmDa7F9xE0gnH5EZC%2FdGn5L6KQ4JXvK44rGHaHDA4%2BbysoPLcSWkqbP9DqOiW4uLyGRMPz%2FExIijoU7P2jO4HEzkvBcIvfB3v12G1NYo7ifxjrftmiidHWfI%2FfH3wJKu3wf27LpIbydnCLGvZbNQHOZirt9WZPf8pUTpifTzw0a%2B3IH%2BHZw2vxY%2BPYZh7lGgJsvBBcHZXyG1lAijk%2BbqqcQc7gmO%2FF58MaFM4Zyiv0fI7O0x9k%2FOL1hP1Mp1H%2FKItpDybXAFP4mBq3ucA60S7MzFK50YwutgigHvG825PQeMz1yXsx9Damusa5zMvJ24tyGCUHB6%2BRTop9ZOf9QOUm92E7KPsi1lyinjLyvJcrhl60oScyan9%2FXtJ0qSL6JVE%2FP3rQ3uhvQB4%2FPuAeB5XxWrvpl8uptQBcTGATmffoB6gA9FolhOeMthh8vlr3is0z1dYJDT%2Be28MDI6ITyfw2qjJw4wepwPZGkHE44un4xBoeKxEfMR3CYNW9wsBmy2uoMpZdSk7U02rruffgf9%2Fp%2BL7Wq%2F5pnHIM90KAaKLFnCd3hHS2t2cjX8D1bccthtnnXCj%2FZf7hx4HdDiO1Rzf5Kgwy5z8vAY6pgH3iNs4Cmd1VhqOieEp%2F747vLmEA5ZPX9TTQAMi2B8bGGUJ9N2XYWqwHag0bjsaF3T7Q%2BmeaZ7ooejhaJ4y7sc0faOIQGEuonFN5awH%2Flhji%2BPvNHIZi4iXxOVQT4kB8LmoiSVbEbgs60R%2Fnz0oixayFlJbc%2BY%2FT6OBEZW0K6GjBot6WuZs5Hllj%2Frg9TWdKTZcbtmrMsNrFTd7DcucinodZ92El0TG&X-Amz-Signature=b58c34290c41c6f5a39ec79253945c5e40424f515728df39ae21d84b90afd5fa&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Algorithmic Libraries
#### 1. **Scikit-learn**
- **Description:** Contains tools for statistical modeling, including regression, classification, clustering, etc.
- **Built on:** NumPy, SciPy, and Matplotlib.
#### 2. **Statsmodels**
- **Description:** A module for exploring data, estimating statistical models, and performing statistical tests.

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c62885f5-417d-4179-834f-d68f8f2bdf39/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YMBDZZA3%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T071235Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEN%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIAyp23yldCLQAMW5zxDzzGQBf7xe2A3yDd1dfgAtCLJzAiADagUyGw7FQITwghjWoaaaueM99Eactv38PcgTO%2FjdvyqIBAjn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMs1YbGgNLqQCf3%2F2MKtwDS2cN56%2BuOVgu%2FzBslqmKztySpuTBO1DRjzwCmDa7F9xE0gnH5EZC%2FdGn5L6KQ4JXvK44rGHaHDA4%2BbysoPLcSWkqbP9DqOiW4uLyGRMPz%2FExIijoU7P2jO4HEzkvBcIvfB3v12G1NYo7ifxjrftmiidHWfI%2FfH3wJKu3wf27LpIbydnCLGvZbNQHOZirt9WZPf8pUTpifTzw0a%2B3IH%2BHZw2vxY%2BPYZh7lGgJsvBBcHZXyG1lAijk%2BbqqcQc7gmO%2FF58MaFM4Zyiv0fI7O0x9k%2FOL1hP1Mp1H%2FKItpDybXAFP4mBq3ucA60S7MzFK50YwutgigHvG825PQeMz1yXsx9Damusa5zMvJ24tyGCUHB6%2BRTop9ZOf9QOUm92E7KPsi1lyinjLyvJcrhl60oScyan9%2FXtJ0qSL6JVE%2FP3rQ3uhvQB4%2FPuAeB5XxWrvpl8uptQBcTGATmffoB6gA9FolhOeMthh8vlr3is0z1dYJDT%2Be28MDI6ITyfw2qjJw4wepwPZGkHE44un4xBoeKxEfMR3CYNW9wsBmy2uoMpZdSk7U02rruffgf9%2Fp%2BL7Wq%2F5pnHIM90KAaKLFnCd3hHS2t2cjX8D1bccthtnnXCj%2FZf7hx4HdDiO1Rzf5Kgwy5z8vAY6pgH3iNs4Cmd1VhqOieEp%2F747vLmEA5ZPX9TTQAMi2B8bGGUJ9N2XYWqwHag0bjsaF3T7Q%2BmeaZ7ooejhaJ4y7sc0faOIQGEuonFN5awH%2Flhji%2BPvNHIZi4iXxOVQT4kB8LmoiSVbEbgs60R%2Fnz0oixayFlJbc%2BY%2FT6OBEZW0K6GjBot6WuZs5Hllj%2Frg9TWdKTZcbtmrMsNrFTd7DcucinodZ92El0TG&X-Amz-Signature=fd90f9742f588b400ff78143a6eeedc54ef16ee5b2aa147188d65eb297c9db45&X-Amz-SignedHeaders=host&x-id=GetObject)
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
