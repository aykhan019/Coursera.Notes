

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

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/997ac361-58a8-4f04-bb0f-79fea4baa761/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663EETKCER%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T171310Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEkaCXVzLXdlc3QtMiJHMEUCIQD1Nvv114iKhi2Q2gXjYcd1NaHrw0GPeGjVQ8kxdwU%2BogIgG9b5aBZGVXDuKJhyEbpeZGzYjnM70OU2vTlZMR6Zz%2Foq%2FwMIYhAAGgw2Mzc0MjMxODM4MDUiDKjLcgZUD8I9cbS4%2FCrcA9mGVU9bOWQMs2qq9icWLzi9R79orb64Q5hXr8rTS4JhO5IKLf9zifP0wnnY%2B2srL6yj48wJjNX5XkXI1UMySAHRclvHDhHYd2huMv%2B2CsiUl0m5tNt4vV9K8g3dK5%2B0XOv6LU9i%2Bhe054GHQ4jFW8jYmnUF3to8rZH1GZDwtpHzBA8upMWGqYww7V3NihFNcM7wydkLu3U0d3k2K4F4Qm8BPfyUM6QJtB%2BdoCDKeQHrLIfXr8CjUZif8kQGZiQvw0zRTVULOqyYoMw2T3dv9s5nZBkhmorI8b1CUtBmf%2BER7ZTtp3Rqg2IQ9%2FzJ3ydoNRHNYfuN%2FTNpuUOg7LRoTuQwFABBfnRRIaeB8yAV4U1Qi81lcOiMGDZbsPGQ%2F0C7m0wOwAouwn%2BHpa6H6A2CqXB6WBOTACmS6tv8VdOcHGx52DiZudxDcQ4gfrdsTwvWf4kaelBR0E1030xTu8xnsKH5tIxjvkDzEnWJ0z4JntRQ9KK3xguesmGb1tdNR3BMvs31RDgL16vURwhwHJkmQrybw3vI7zE%2Fq1VwXiJQeROEG0yI4nLEcscjuj3eYB5vHOgu00nhyTm01Y%2FelU2Z1FF5qLqYWMG7ubyX5RB6JN0sbRoXI4VywKb74noMMMbRk70GOqUBqka77JcPV5WfGpNRJaXMGNrLp3kC9JSnPP7hI3v%2FsvVdudCDbyFW6zuTbO8qonKxiEffYH%2B5lGFTBFZvfQTLffhcM7o%2FefWQiwMcRCg1ADIS1OJzQYC3JwinYRSfgX0THfbSALJcs7enxnqxGnE31ixOecAQkb1Tue07rc1h2hPVg7%2FIudCSUJ49A1SEn%2BzF7E6oyCN8ZIfrKu1C2zvnBmlKo2rd&X-Amz-Signature=b65c51a64ea8b27cf08923a404aaada2f8a0fe3f0915340bf6c2f5865f6f8183&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Data Visualization Libraries
#### 1. **Matplotlib**
- **Description:** The most well-known library for data visualization.
- **Features:** Great for making highly customizable graphs and plots.
#### 2. **Seaborn**
- **Description:** A high-level visualization library based on Matplotlib.
- **Features:** Easy to generate various plots like heat maps, time series, and violin plots.

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/733d1e42-5a53-4fd8-90c1-3d85254369a6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SETGW2FH%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T171309Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEkaCXVzLXdlc3QtMiJHMEUCIQCnh6C9JP1YXv6vWNiraGwQICxnPmgELH4zX1SCKFRfygIgYohmOJj308YFJTX9hFSxlg1Tl7ofRjA8LoYPzs2a9N0q%2FwMIYhAAGgw2Mzc0MjMxODM4MDUiDDVB3t8z4BCYFbPxLCrcA603lm%2FHpbCfnys2IkXN8AXYON8MPkrLsYkz3cP28PanwWOS59IqGc2Udp3kSSTY6rzijW1kaH98pk732OL3%2FOU75DChoTSdq5Sm6CxZLWfFkLWJJl8T8lflGcijgi1kaM8mAj%2BJX%2BNFCwz4VbRvknCa930oTfpzdqZZiIomtN3d4B%2B0O52E6Jz25BLvs0Wrl9KLVYZaxM4zC5HQF7veUPfnk1AiizAlBI8SzBnvHULcA6meNAkTBX89CWIH669Bt9RRZrytCUc4YF1I%2FG7ccV8WN%2B93pWYAOziCN%2Bt%2FaB36XXn9xM3lGYzqYRKPuQl0PRHSryvwAV%2BWIXyxmcsXPbNecLDgAWXO18zfQPk2Bd20yo9JAF%2FEAzooNhwI9ETJ3%2FBxFvtBe4biDMrNarbNDxBvRCXuneu9fsX6kZEduy%2BHaaHl%2FDQLULfjjN4RquVZeYCc5Bpr%2BB3IBjK%2FfZdmtnGHNDzfAWYzb5Wy9J29N51Xd8KgZtftlZSIPA%2B12OPLRes1HFYxHYnG9kMumQsVTum1%2BAIWWVkatW0eu6CsHF0zWZKbrbmSBsmP1zSwg72SsXQFj6m6XYc9U9Uz78PAPz7n4Nlx8ZcWKgQlE02%2FgtmwLvE0nhCThOWNkIqSMKjRk70GOqUBkkbvVnLhVnvWk3dFAhy66uHJS69RYiFAYyxKFyOnQLqPDB5zOUEIjAvlW%2BF6XDEtVOcbytuJnOkrUG81dt%2Bxj0AMKoYy3jII1sUOaAC87NjJzPRxOq92wSSUueZHirxBK8I4vR%2B%2F4TCbqmDSSktDmoa%2FOLUEnw8tEeDrAT7bSYwviPpjCyuuE9bNejWqkhCOQs5iHztBFUfhwoSrJQVAUG8JGLOZ&X-Amz-Signature=7de18b897e7ed3b869dc1634b7052c3868f03778c429981050bb5c2f7da30e9d&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Algorithmic Libraries
#### 1. **Scikit-learn**
- **Description:** Contains tools for statistical modeling, including regression, classification, clustering, etc.
- **Built on:** NumPy, SciPy, and Matplotlib.
#### 2. **Statsmodels**
- **Description:** A module for exploring data, estimating statistical models, and performing statistical tests.

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c62885f5-417d-4179-834f-d68f8f2bdf39/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SETGW2FH%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T171309Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEkaCXVzLXdlc3QtMiJHMEUCIQCnh6C9JP1YXv6vWNiraGwQICxnPmgELH4zX1SCKFRfygIgYohmOJj308YFJTX9hFSxlg1Tl7ofRjA8LoYPzs2a9N0q%2FwMIYhAAGgw2Mzc0MjMxODM4MDUiDDVB3t8z4BCYFbPxLCrcA603lm%2FHpbCfnys2IkXN8AXYON8MPkrLsYkz3cP28PanwWOS59IqGc2Udp3kSSTY6rzijW1kaH98pk732OL3%2FOU75DChoTSdq5Sm6CxZLWfFkLWJJl8T8lflGcijgi1kaM8mAj%2BJX%2BNFCwz4VbRvknCa930oTfpzdqZZiIomtN3d4B%2B0O52E6Jz25BLvs0Wrl9KLVYZaxM4zC5HQF7veUPfnk1AiizAlBI8SzBnvHULcA6meNAkTBX89CWIH669Bt9RRZrytCUc4YF1I%2FG7ccV8WN%2B93pWYAOziCN%2Bt%2FaB36XXn9xM3lGYzqYRKPuQl0PRHSryvwAV%2BWIXyxmcsXPbNecLDgAWXO18zfQPk2Bd20yo9JAF%2FEAzooNhwI9ETJ3%2FBxFvtBe4biDMrNarbNDxBvRCXuneu9fsX6kZEduy%2BHaaHl%2FDQLULfjjN4RquVZeYCc5Bpr%2BB3IBjK%2FfZdmtnGHNDzfAWYzb5Wy9J29N51Xd8KgZtftlZSIPA%2B12OPLRes1HFYxHYnG9kMumQsVTum1%2BAIWWVkatW0eu6CsHF0zWZKbrbmSBsmP1zSwg72SsXQFj6m6XYc9U9Uz78PAPz7n4Nlx8ZcWKgQlE02%2FgtmwLvE0nhCThOWNkIqSMKjRk70GOqUBkkbvVnLhVnvWk3dFAhy66uHJS69RYiFAYyxKFyOnQLqPDB5zOUEIjAvlW%2BF6XDEtVOcbytuJnOkrUG81dt%2Bxj0AMKoYy3jII1sUOaAC87NjJzPRxOq92wSSUueZHirxBK8I4vR%2B%2F4TCbqmDSSktDmoa%2FOLUEnw8tEeDrAT7bSYwviPpjCyuuE9bNejWqkhCOQs5iHztBFUfhwoSrJQVAUG8JGLOZ&X-Amz-Signature=7f8c9a8fea310082debe572438c446749d5e1fa862b636da04460a18085dbf52&X-Amz-SignedHeaders=host&x-id=GetObject)
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
