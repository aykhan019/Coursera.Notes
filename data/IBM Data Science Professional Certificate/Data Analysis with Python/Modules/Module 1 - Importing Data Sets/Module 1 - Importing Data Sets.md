

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

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/997ac361-58a8-4f04-bb0f-79fea4baa761/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662FY3BKZF%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T132104Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEQaCXVzLXdlc3QtMiJIMEYCIQDPKa7kqCpDxAS0tFuybMVKX%2FCFhCTeQU6p0ETY9VDLMAIhANiUF47RtIS%2Frf3SzkbqVPHwqXbT4wIsb84vqw5rniJ4Kv8DCF0QABoMNjM3NDIzMTgzODA1Igwm6MrknqvWTDqoJ0kq3AOMAtUKLLdRrubHE6CK8wccbWNV8UERGVe4mw7R3mNEePMNd5A4YPZ61VLsYMXohxAliVBbRD6KDvBAd3hpGaLlwTmcPQaDPBbaQLy1bewyY3YtFfDnDR8TUtZU2aFk9k3QwDc0EatqVklKsuUehy4tvkhRhRHmPSiW6utNgLxA2dOjkoEbzXUPD7Fmrr33qj4ncAhAP5aKjEF6A%2FHKEva7CwWUGl8QVQC6krSWWowHPvyhs8OxFQlKqmi5ssmCrcK9leWH144PGHq%2FL0JLkRko7M1MZNByzAkifByRIc%2Bf%2F4S3UEzHfIQrwL%2BjKZAL%2BiqhjWjZFWWfTmGdXYiUu9KJmzQy1yO2CqZoA3jBhk6vBEQiwOj52yzeUYKDg3LSt9qOnkS7ns6J8hdIH37uUna9n01js0zpZR4lEdnPUML8QaUrB0RmzYEZ5NbWrkMtistNoJN%2BVHGFkpPdzPHZ%2BPsnAXmyVsfEdTZ4m9fPWj0ajfQYU2L7rVPn1YvbIOjIbLLdoJc5hJXBvCFbRcjXBUDIKsRxKk6eApoCuKUnh8gWXiuXSTejt70U2MTbRcseAu0sxLE%2Bij2IHHqwhfTiDXwSsWtrP0N4NZD8OTD9iN2WStNL0tL3xIHX3RCg5TCrxJK9BjqkAYtVksP1fl%2FerqsVQ9qR2zSzfB2Z7Tcb2QYHsN9JZdLbVmLRU2EjZEMAxyeaSKWFJYkyVlgCcVDbvXNpx1wC2wNtU%2BvAB%2BzSy7evFx6rPNucRD7Dn%2Be51DfVaBTFOLGpB53IpqELOkmGTnlXebTNNyBh1cmjiq9elhTXpyz7kcNDdEXZQmEHlyqnKo%2BEAosRfT0vmrk%2FKNxdADnRAXO8UEJZS71Z&X-Amz-Signature=f52ddf4bc9e4f83d80a5c5c44993e80821927e3940c592ccb212a44df8fbc195&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Data Visualization Libraries
#### 1. **Matplotlib**
- **Description:** The most well-known library for data visualization.
- **Features:** Great for making highly customizable graphs and plots.
#### 2. **Seaborn**
- **Description:** A high-level visualization library based on Matplotlib.
- **Features:** Easy to generate various plots like heat maps, time series, and violin plots.

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/733d1e42-5a53-4fd8-90c1-3d85254369a6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZCYDUNUQ%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T132103Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEQaCXVzLXdlc3QtMiJHMEUCICzrPOs%2BDvRgb6MlPPY%2F%2Fegp1eCGzAUK8CWQqkPWq%2B3qAiEAzvMg4e%2BpQPl%2F1Ks8qhAxNirIHILUczI7oaCR%2F2Lrt8Eq%2FwMIXRAAGgw2Mzc0MjMxODM4MDUiDHySY7J4K4SDJeH4tyrcA2eAiU%2BYFNbBc37et2BedF2Tce2I9v2%2BL4MnMcFc3Aoc8Ic0JvuTbBHqTKWpc1vCudrfGtQrh%2FbNWpWIp8XC2JZZYqtHVCbi%2BUHC9PHEMvxt16ecX8g6VMbjAM%2B3Pv9IE%2F3CsYQ%2BqTPRdIZlHeKL4DNdtKITVGQrxhNAyEYdD8bulU0X%2FmjP50bF7DN5LIZSaDvoDL9U36MJuld32kCdqz3zOZpcismR4mBTvFG3kPm6dXPZFgPsePVBxl9b8ssZsUAFlkxwwkCh0DpznLURhr7vNbErQ12WROL5aU7MrotI0Tgs5uo1zlICweE3lTQnoCE10X4pw4JxEjNIAOjB8aCyYk1BSFLwh6ByqAYfWDYkczrj4MiE9QXlXYiHx6c2EvfJVIbLQWgST6dR27bMCkFimfSlyTF6kYr%2FQ1LWAN1Bbw8TdZsAynp4F2wOnjnxKtIjGjwyU37EUydozhjmSGoRB0ENkb2rVJb6fuMmm2jEu2HFrXhzXRJHK3jPa1VYpy6MhbMZbhyfVJr8Tgmy23waK9vD%2BML7LYK2dABnEkCxrpoNc5xJ89ftxTR9s2QDDPeHaneT09p6myCVQpkZpLyNpZ8HplzyevVSpt2Gq30GQf62en1rvMNmzowtMPnDkr0GOqUBmvuRdO5ZeKnNkR2mqp39ZZspr%2BOwW2L2JSFEhN%2BBoM7c%2Fo%2Bn%2BQ7xIzQjEjv0cKdgHD%2FBfMRKaQW%2FiTiwA%2BRVhr0IPnKHghNF9KLft6%2BXOkLHzpm3uO0tKuvkcGeIPZfEtOQFczSZhSPV%2BSI5R4Vv91QFSDOM%2BXXWGLCodkIcnx0qGyeWuhWyqeRZuPJRwLSzJPdw4q6jFTBCljZqHHY%2BkU8upoRr&X-Amz-Signature=f08dc5c1e14509fcec023c43f38ec9c3a99eefc87941061c88e92e8ae05d1672&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Algorithmic Libraries
#### 1. **Scikit-learn**
- **Description:** Contains tools for statistical modeling, including regression, classification, clustering, etc.
- **Built on:** NumPy, SciPy, and Matplotlib.
#### 2. **Statsmodels**
- **Description:** A module for exploring data, estimating statistical models, and performing statistical tests.

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c62885f5-417d-4179-834f-d68f8f2bdf39/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZCYDUNUQ%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T132103Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEQaCXVzLXdlc3QtMiJHMEUCICzrPOs%2BDvRgb6MlPPY%2F%2Fegp1eCGzAUK8CWQqkPWq%2B3qAiEAzvMg4e%2BpQPl%2F1Ks8qhAxNirIHILUczI7oaCR%2F2Lrt8Eq%2FwMIXRAAGgw2Mzc0MjMxODM4MDUiDHySY7J4K4SDJeH4tyrcA2eAiU%2BYFNbBc37et2BedF2Tce2I9v2%2BL4MnMcFc3Aoc8Ic0JvuTbBHqTKWpc1vCudrfGtQrh%2FbNWpWIp8XC2JZZYqtHVCbi%2BUHC9PHEMvxt16ecX8g6VMbjAM%2B3Pv9IE%2F3CsYQ%2BqTPRdIZlHeKL4DNdtKITVGQrxhNAyEYdD8bulU0X%2FmjP50bF7DN5LIZSaDvoDL9U36MJuld32kCdqz3zOZpcismR4mBTvFG3kPm6dXPZFgPsePVBxl9b8ssZsUAFlkxwwkCh0DpznLURhr7vNbErQ12WROL5aU7MrotI0Tgs5uo1zlICweE3lTQnoCE10X4pw4JxEjNIAOjB8aCyYk1BSFLwh6ByqAYfWDYkczrj4MiE9QXlXYiHx6c2EvfJVIbLQWgST6dR27bMCkFimfSlyTF6kYr%2FQ1LWAN1Bbw8TdZsAynp4F2wOnjnxKtIjGjwyU37EUydozhjmSGoRB0ENkb2rVJb6fuMmm2jEu2HFrXhzXRJHK3jPa1VYpy6MhbMZbhyfVJr8Tgmy23waK9vD%2BML7LYK2dABnEkCxrpoNc5xJ89ftxTR9s2QDDPeHaneT09p6myCVQpkZpLyNpZ8HplzyevVSpt2Gq30GQf62en1rvMNmzowtMPnDkr0GOqUBmvuRdO5ZeKnNkR2mqp39ZZspr%2BOwW2L2JSFEhN%2BBoM7c%2Fo%2Bn%2BQ7xIzQjEjv0cKdgHD%2FBfMRKaQW%2FiTiwA%2BRVhr0IPnKHghNF9KLft6%2BXOkLHzpm3uO0tKuvkcGeIPZfEtOQFczSZhSPV%2BSI5R4Vv91QFSDOM%2BXXWGLCodkIcnx0qGyeWuhWyqeRZuPJRwLSzJPdw4q6jFTBCljZqHHY%2BkU8upoRr&X-Amz-Signature=be156ead30449cb378eba62b1ca24dfeb26c22c4f7c9d77596da7d9e59f8d756&X-Amz-SignedHeaders=host&x-id=GetObject)
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
