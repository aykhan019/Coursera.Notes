

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

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/997ac361-58a8-4f04-bb0f-79fea4baa761/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662IH2NXJQ%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T201547Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCHyfS0ugl%2FqU74IY2vxOvBZW9DTaDejfHgnyUJTC3D9kCIQCJpT75o2YDmxt%2BSOvWlPTHG50qEuKCgRSMT4i%2B%2BxdXBiqIBAiU%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM885SS5Soum5n%2FcnLKtwDSTgjpmJznxEXIK4MQaBjOJ0%2BXEN80Slbpc5lHrb1lw00VdvzICLmVm%2BRoVC1qWX2dgTImwIcd8nDD4ak%2Bb9yA0tb%2BwSTNyJTB8bnb%2F2bjIIp9PHv%2F4epkICMv9ObpsVvghOuTb2yQXZlbBN6lSVJPyZ%2Fueo3ylg4fKfXaRVJKn2%2BhIyJ%2F3uqC8z0VcSOd4ZsQuwtW8jdxWbLRse16C%2FBIt7UOZdP3d9x4bYhVWBFCzvE2H0YmIT42mxG1GUCLtIzpRt84heMow3Xuje9HQD6Rv6V4nTCDVymmYTcnFIViW5Ix%2B3%2BzCvZagKIux1rjqC7zLkQn0dwsmigqL0ogaQCm%2FxV34544a6B0Ej4rQMBC9R%2BPiZfo9sz7eNoJUJf35A9bOfeMJUTdwdUXo32JentRvNGgZx78lbBLYc43xONUGHX%2BtnQrnosrghPIgs1chfkUsK8BkCOzebSDKomCssmXyMyQCVlO%2BX7mm9SsOBbaKHiAA%2FzjSr%2FEL1eFBUxy5nNy0nclqDP%2B9BNLXKO9UeMPcNfy5j8%2Bo79dlCss7lDb9YNAqFtz7smSDa3Q0Nejx05gtlluqBQZNixpz%2B%2F2eoNktzuw7P61sCWkw07%2BabvGToGW30xq7MaruNacfowy%2FTpvAY6pgFre5Ld11A2FH627WsbZrCI%2BNJpeQNncICKDAmbq%2Faw1M97lklVAum9SR8S0pIBwSbYk4M4V3394QtMji7KGSwIXmsFCMaMdHmYw8uycJho8MDhC5LN%2BKlB8Ko2LkRY7ZqyTCRlKKvFqOmcdb6L0bk48oXvba1cFcqoZecuS0%2FweIRwn%2FpWfsQmT39HVP6StOyjXhvSxnncMKD2Ix4ur0SsPVTF57fj&X-Amz-Signature=df14278216ee42d60d43122bd0ff0b1e829d3db03254bc606df1e204ed363a62&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Data Visualization Libraries
#### 1. **Matplotlib**
- **Description:** The most well-known library for data visualization.
- **Features:** Great for making highly customizable graphs and plots.
#### 2. **Seaborn**
- **Description:** A high-level visualization library based on Matplotlib.
- **Features:** Easy to generate various plots like heat maps, time series, and violin plots.

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/733d1e42-5a53-4fd8-90c1-3d85254369a6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UOFUAQ5L%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T201547Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQC%2BnNJSYL64GSHZTyMcILrWHo436xd0ediA0s%2B5Qo2YKQIgFaPyETyQqGHBMiN5QXfS1Bg3W4Heg%2Bjn5m10R9mYNsQqiAQIlP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJo7r%2F6XNLvjrBlBwircA4k%2BN7GjMmPDCNtzIAZ4x%2BxLvWsfSoPLGd%2BcRF%2Beil%2B4zb7f7jihF1I1OSnAP4jOKitsS3hKAFkt%2FV2xuRjkST5WdEyq4dxnG6qQxxNNGQhm7O77FsMZFl41UT7MyM1QPqFTxbeFvKxdq%2FFE6FZFYUmkyszTZX03FlEeijHwwMdj03Ltu1J2Th83LsD7Toeem3BLso3wMY9ZnolsMbdZvTCKR3gvYTnoZCtSo3PRXfnv2abcs7xZdH0Bfe%2FHe0fENyEMDuLoFIASv2KdJ6Douq5eXcF7kXR68M4wiFA0rlgiNUK2dX3o3I%2F7P%2Fjc09SXfi5ZGadML9CSuSMqNsNdIsFtWrN3VBxnIsgVFH7gTpchgRexGh6F%2FENJIhPwTPiX3FYykve6YppUxg5Fx%2FWWtxsQjRZWf12LATCax2nUaIsL9wCR4nGRhebg9DWpPSVewzjw3TuRWlGXCp1baQjw2r6NrbmltWqqDcJtKhxSv%2Fad82JzReZx1gJ0jh4mTZgXrYEgH8aMcR8jyDoL7gEtypKSnyIchkLhPBaUpqPeMjbahMUKZB%2FpWCfWZuD5qHLfXFxbGV5u3AC2TqNyzvnqdcX0UNOdDp18trAWzKb2uCAOvg6tipXjKz%2FH%2FFjbMJj16bwGOqUB%2Br%2BBqLCnpqJ7YCSLeW4XZ2Ku44naR0vdNfmiMidIoDj1jpifXkicwEo15BzdddTfqI2PEKcH7JDAkL13SNaN4%2B5xqMQOSp1JriKtvdFH%2B5vg3mCoXQgtZl7o%2B61x2XQf6%2F56cankfaJTLJYGbuIh8Y1%2BedJ936yvfCkl5%2BN%2F9tCvCSSD49fmf9KGGKR7XGpG3%2BmsL7TRjxOT%2FyquIUn9fnTF5ypv&X-Amz-Signature=b559dbe722610236d286a6b2ca18f01d551f684666bb76f6447d8186e5e50a63&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Algorithmic Libraries
#### 1. **Scikit-learn**
- **Description:** Contains tools for statistical modeling, including regression, classification, clustering, etc.
- **Built on:** NumPy, SciPy, and Matplotlib.
#### 2. **Statsmodels**
- **Description:** A module for exploring data, estimating statistical models, and performing statistical tests.

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c62885f5-417d-4179-834f-d68f8f2bdf39/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UOFUAQ5L%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T201547Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQC%2BnNJSYL64GSHZTyMcILrWHo436xd0ediA0s%2B5Qo2YKQIgFaPyETyQqGHBMiN5QXfS1Bg3W4Heg%2Bjn5m10R9mYNsQqiAQIlP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJo7r%2F6XNLvjrBlBwircA4k%2BN7GjMmPDCNtzIAZ4x%2BxLvWsfSoPLGd%2BcRF%2Beil%2B4zb7f7jihF1I1OSnAP4jOKitsS3hKAFkt%2FV2xuRjkST5WdEyq4dxnG6qQxxNNGQhm7O77FsMZFl41UT7MyM1QPqFTxbeFvKxdq%2FFE6FZFYUmkyszTZX03FlEeijHwwMdj03Ltu1J2Th83LsD7Toeem3BLso3wMY9ZnolsMbdZvTCKR3gvYTnoZCtSo3PRXfnv2abcs7xZdH0Bfe%2FHe0fENyEMDuLoFIASv2KdJ6Douq5eXcF7kXR68M4wiFA0rlgiNUK2dX3o3I%2F7P%2Fjc09SXfi5ZGadML9CSuSMqNsNdIsFtWrN3VBxnIsgVFH7gTpchgRexGh6F%2FENJIhPwTPiX3FYykve6YppUxg5Fx%2FWWtxsQjRZWf12LATCax2nUaIsL9wCR4nGRhebg9DWpPSVewzjw3TuRWlGXCp1baQjw2r6NrbmltWqqDcJtKhxSv%2Fad82JzReZx1gJ0jh4mTZgXrYEgH8aMcR8jyDoL7gEtypKSnyIchkLhPBaUpqPeMjbahMUKZB%2FpWCfWZuD5qHLfXFxbGV5u3AC2TqNyzvnqdcX0UNOdDp18trAWzKb2uCAOvg6tipXjKz%2FH%2FFjbMJj16bwGOqUB%2Br%2BBqLCnpqJ7YCSLeW4XZ2Ku44naR0vdNfmiMidIoDj1jpifXkicwEo15BzdddTfqI2PEKcH7JDAkL13SNaN4%2B5xqMQOSp1JriKtvdFH%2B5vg3mCoXQgtZl7o%2B61x2XQf6%2F56cankfaJTLJYGbuIh8Y1%2BedJ936yvfCkl5%2BN%2F9tCvCSSD49fmf9KGGKR7XGpG3%2BmsL7TRjxOT%2FyquIUn9fnTF5ypv&X-Amz-Signature=bfa422a39efcb4895f829e09413fc0a26f770b7b65b45cfed0b86bf5aebfae0d&X-Amz-SignedHeaders=host&x-id=GetObject)
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
