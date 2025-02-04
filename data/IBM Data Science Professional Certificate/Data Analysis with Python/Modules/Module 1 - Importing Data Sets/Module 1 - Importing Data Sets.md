

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

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/997ac361-58a8-4f04-bb0f-79fea4baa761/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663TLO7FRT%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T091531Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBEaCXVzLXdlc3QtMiJGMEQCIGD%2Bw91aM6xG3d6GSyOkAHXnUUhStPdqY6au1C7v0jPWAiBAIw0lTJ6xjdPB7rf27xjGFlvohjPzvuEAaEhEQ%2FjjQir%2FAwgqEAAaDDYzNzQyMzE4MzgwNSIMf4552C6qJ42%2Fpox5KtwDgTRea0uZIVtbfdDNsK95qsqBQ83NKCE2ufh%2BwVfCUZ1pjId%2BJ9VXch4bUAgFZEjttZGvFtHqrMhguz7nm7j%2Fiil4sUDk4kIdtlJ%2F%2F12yHQHztpx%2BU7HvuEOQENsPL4SUkC21okrLbq27QesP9NCttCFgByHnJmsvfCcjzLLLS5D%2BfSIEjPQvoY9skfqeSEBPgcWe0DXSCT%2B%2Bm2XiuwmJGcQARDo9Gj8JBtvi24TOtEanS0XBpCOZ4qVC25VsocnbANyJ923z3exEb42ktpcJwb2l1lxJvzd8X%2B4FXcBEbl%2FZJ6xsgjDpmz5tiHUYy0erfevNPvlRcAe%2FPjWepNC00ConF%2F1EtwfIzIiZqwj2J3E%2FswVMZNVtHXCzm9ssu55TF2BHENlZaiw59w07vi68bhJD1lNZKKVztqXp9WUm6I0Inbhg3uol%2FU5%2BauHwqv8LwL4jdvvlxGY8GrP2MS%2FUylr2C3gqPYYmfiaT2a1nRPhCw80Os8OtnYkf%2FQLBr%2BtvYxEGBRKjhAtshk0%2FFMEARB0NRb8OzpdYcx%2FWJ8D%2FuRhep%2BTiKyeca0QlzDs%2B4dRIvYb1pG3ZxQoYcMAx58poGXIGnEkty3v2mQkNtn6NoZI%2B7t95zCprgfnl2UUwt66HvQY6pgEH8%2BzjS%2FVMsaNpXIrgVQY%2FoyrLNFN8KwPgdh34H0yKrjEdnvpT9oslwkwVPJDOMT61vXSmsr6EpcI4oFGunrwuUE5z31DsQA43VIxQ8b%2BoCgVZ%2FFjgcPXatnSaaMd1tUqyQit7hxk6qWaplWnVEWTjT8cX2g8zME0Gh2nnDv3ra2BjBcs%2B0gwirpC6DXIg5M1RE0IOehYn0UgieA4U%2FiziNe%2FWNanD&X-Amz-Signature=29a2eb9adb2af8b772939111f0ff314523beab95f6795d7389d9928743b4aa46&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Data Visualization Libraries
#### 1. **Matplotlib**
- **Description:** The most well-known library for data visualization.
- **Features:** Great for making highly customizable graphs and plots.
#### 2. **Seaborn**
- **Description:** A high-level visualization library based on Matplotlib.
- **Features:** Easy to generate various plots like heat maps, time series, and violin plots.

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/733d1e42-5a53-4fd8-90c1-3d85254369a6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XSW3CF2U%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T091530Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBEaCXVzLXdlc3QtMiJHMEUCIQCAJDSYnmZD39cQD1nXlTrFO5LixXgJFRjCo0eSy2YKOQIgM5OFkq4GU6awuFqEcIxIQT8SJrFDpg4YwJ1FYxiz%2BPMq%2FwMIKhAAGgw2Mzc0MjMxODM4MDUiDM%2FxaLtwnpVkiE9uRSrcA0oQnQNbCBuXMrGl%2BBICY4hYViEzbSNX%2FkzKKXR%2B9Aq7cyHlMuHxx0G%2BV9TPpDUCvd5KHvSivWidDlcjJbauEj7cTZxScW0LfUSX1BNgooYLBFgYOoFq3LcMXK0YNE3ko%2FnGL43yG3colky%2BX74xJS6G%2BB%2BQxnXBWqB2vHSAF%2F392VuTnfrwWe7B9F%2BgFaRa6ofa9djj5FwQW2ldxOaOI%2BSZ%2Feu%2BuJRpb3%2BAZTUFsQldLXd5kMuQXRspSdGUEPaY5WSyMxdldK5Lqw35%2F2U9wKGeDYt8c1fE7vVk6DWRKxbnmDDA4pGbMpgBqcigxzTy9OZpMb1Qi5pn%2BSKLiG5umuvqEZqmPVlzuNWudz5Bvq0jMEhWrBkwa2JdckqwF1oJ66o3fPtHDQiT2IdJmp6FRpj%2BrLqft%2BsfpuuBuaHQh9zWACw%2BaSnlzslrAxuVJ9SmNgJhhJqLp8MYiSAoNKHysQ%2Br91XhK0aSzsOHwh855KSIBrJvdLbNd6aH3%2F4enCIaf5JL3PzaMwP91L9NPADRsRc8waBDHCzFJnaHpKqx8jVX95KusAL3b9vmVQOQ6xyEVUcY5rOim03uPPOvFGS2P%2Fq6SPKa9vxaPb2pShRq%2FeKQtdS0VX8KVLelwGrCMMquh70GOqUBDxLmKD1CWImUlWhli1E6jJ4ljvgysI3Zy4bfVvsjp5glBZNE%2FrfI0QjR1%2FyDjj72iCHgsKdr8eWRqLgUoTcdSUJsEnE1sL1y7mfyemon%2BnntWn3d%2BbQlKHinDgUMBVMO6S1rEqa3kLZZs%2BD%2F7B7k0d9A%2FLjefDO4VpASruD3KX3Ey2MbOmAsSmxGhwM5yXDisWxRTQmDFc5U9Vo6z%2BK1EatyH9T1&X-Amz-Signature=0e2533356861a8106e9304364835ec7a4b87e4e51ea5793ac67f0f3033da517b&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Algorithmic Libraries
#### 1. **Scikit-learn**
- **Description:** Contains tools for statistical modeling, including regression, classification, clustering, etc.
- **Built on:** NumPy, SciPy, and Matplotlib.
#### 2. **Statsmodels**
- **Description:** A module for exploring data, estimating statistical models, and performing statistical tests.

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c62885f5-417d-4179-834f-d68f8f2bdf39/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XSW3CF2U%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T091530Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBEaCXVzLXdlc3QtMiJHMEUCIQCAJDSYnmZD39cQD1nXlTrFO5LixXgJFRjCo0eSy2YKOQIgM5OFkq4GU6awuFqEcIxIQT8SJrFDpg4YwJ1FYxiz%2BPMq%2FwMIKhAAGgw2Mzc0MjMxODM4MDUiDM%2FxaLtwnpVkiE9uRSrcA0oQnQNbCBuXMrGl%2BBICY4hYViEzbSNX%2FkzKKXR%2B9Aq7cyHlMuHxx0G%2BV9TPpDUCvd5KHvSivWidDlcjJbauEj7cTZxScW0LfUSX1BNgooYLBFgYOoFq3LcMXK0YNE3ko%2FnGL43yG3colky%2BX74xJS6G%2BB%2BQxnXBWqB2vHSAF%2F392VuTnfrwWe7B9F%2BgFaRa6ofa9djj5FwQW2ldxOaOI%2BSZ%2Feu%2BuJRpb3%2BAZTUFsQldLXd5kMuQXRspSdGUEPaY5WSyMxdldK5Lqw35%2F2U9wKGeDYt8c1fE7vVk6DWRKxbnmDDA4pGbMpgBqcigxzTy9OZpMb1Qi5pn%2BSKLiG5umuvqEZqmPVlzuNWudz5Bvq0jMEhWrBkwa2JdckqwF1oJ66o3fPtHDQiT2IdJmp6FRpj%2BrLqft%2BsfpuuBuaHQh9zWACw%2BaSnlzslrAxuVJ9SmNgJhhJqLp8MYiSAoNKHysQ%2Br91XhK0aSzsOHwh855KSIBrJvdLbNd6aH3%2F4enCIaf5JL3PzaMwP91L9NPADRsRc8waBDHCzFJnaHpKqx8jVX95KusAL3b9vmVQOQ6xyEVUcY5rOim03uPPOvFGS2P%2Fq6SPKa9vxaPb2pShRq%2FeKQtdS0VX8KVLelwGrCMMquh70GOqUBDxLmKD1CWImUlWhli1E6jJ4ljvgysI3Zy4bfVvsjp5glBZNE%2FrfI0QjR1%2FyDjj72iCHgsKdr8eWRqLgUoTcdSUJsEnE1sL1y7mfyemon%2BnntWn3d%2BbQlKHinDgUMBVMO6S1rEqa3kLZZs%2BD%2F7B7k0d9A%2FLjefDO4VpASruD3KX3Ey2MbOmAsSmxGhwM5yXDisWxRTQmDFc5U9Vo6z%2BK1EatyH9T1&X-Amz-Signature=1ea587a822a0a2f984f26bf799a7bbaaa9c7b1ee6a2eb47c9351e3666d201f25&X-Amz-SignedHeaders=host&x-id=GetObject)
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
