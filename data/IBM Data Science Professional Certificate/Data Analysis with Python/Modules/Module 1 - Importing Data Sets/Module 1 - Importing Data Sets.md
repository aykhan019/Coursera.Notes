

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

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/997ac361-58a8-4f04-bb0f-79fea4baa761/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZEZUZVV4%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T191232Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDEaCXVzLXdlc3QtMiJHMEUCIQCw4vpTCgeZxvDvXPcjabcf9uT5SoFXGfXu6oJuN1TBQgIgfLPiF9S8dltdN7lsDsYnek5oK4TAsTD3bXW0PxMCBVQq%2FwMIShAAGgw2Mzc0MjMxODM4MDUiDJIDeKw%2Bby%2BmTfaR3CrcAzBHiiFzpOGbTFw%2F8mrqvKvUlDiQCfaxZ9jk0SawOkrSievPvvu0LSRezJnDFe21s4Vf8VE45mhTDmQWwky5VG6r9lLDp9iyc4m2J3ao8sgEChA2nQHSkXpOhaxSXrcLQVL50Mavy8zagH1e34C%2B2UBZr%2BtNvS8F1Hh%2FrNNZU%2BuDWAPFP18kV3cxTiJ2ak4tX82SbTxtP50CHSI3y25Wdkv%2BYsTX3FlzOVgWWAfRxPLxzvqe3yKlYiAY%2F7tgMsY%2FwZw9rj8av6P4Dy16DDxsf8iT2roU2FumsK96nc5fssJhtXbl4X0Wbx3fxCBKNr3H2ECvAdVidS9NARSVclfq8JR%2FX1BFNMlfDNz4i2AbOzP8v89mds7zzHk6L5vB29Lcia3b552i0YnUf8PDoYucpjG%2Bgcj%2FkYiYkCk8ZPbQwcLvyfIpT56m6htFBCY%2F0MufEoDmN93PFQy0XB29g33UFTi%2BDXSlKZ8Cc5xZVVJYm9HA%2BgkNnoZlVFNp5%2F0NH57G66LKk2hpMcf82s7o23DdzTFa5sMe01oco4erBPt0Db3LXHSHMRiSNGmcBx3C0Ozwx5QKtsdFHVgDRLKKMGQTA8zz5ka1%2F5QODHnlfklENUb1K19CDbBddH40dtJPMJm6jr0GOqUBzzKPZDJskACwQexiwdwQrzVTVZts%2BVHMvhs8xtaSMDGst%2FtrqDmFvgdZMfpVPih9goSavCkqoMGo55V%2F6JZxiJBqr3wj1wm742WK0l93N2Rr6kV1G5kyaoCXKiK0zNhqbXNzPbEXsp5GRKsCDzSLgQQQqdjesbZe%2FDfEQN5vN3vxDnbQOqQyjM2ccYp0cZJG%2Be5IH9PFD07%2BNJG0arGnPSqbG83x&X-Amz-Signature=3210e7e87956111af64ab70e7125579bddb6be75c7ac94dfeecaa3eea5778b8c&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Data Visualization Libraries
#### 1. **Matplotlib**
- **Description:** The most well-known library for data visualization.
- **Features:** Great for making highly customizable graphs and plots.
#### 2. **Seaborn**
- **Description:** A high-level visualization library based on Matplotlib.
- **Features:** Easy to generate various plots like heat maps, time series, and violin plots.

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/733d1e42-5a53-4fd8-90c1-3d85254369a6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VVTRXMVY%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T191231Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDIaCXVzLXdlc3QtMiJHMEUCIQCE3bVJda27BkVgmVHy5IaN%2BrbQ0XaitcgkFTcbm4CJLAIgKgCBSiZ5U0Q7X4i%2BmEOY87ACMdweRkHbRnS2IyifM8kq%2FwMIShAAGgw2Mzc0MjMxODM4MDUiDLUXGVcEWzl3bgimEircA9gBUeguJkHnogP%2FgrruZ3gtvjo%2FdDeWBwxy2CC8O%2FMmQY4vlVOUP6zy7VdihyXVw3we6ADvMZJG80VpDFRAGj0k1MB3nl9XmFJjL%2FQ5FJJZiTVH1%2B85mUYhhyyhlGEK4utAHeFGPhYXLZ4cR0zzrPxCnTOzQHlvtHKzI5VxHNOTHvyHJvyiBmnr%2F6c3RxeoX%2F%2FuSnk0Ek1UMuCP2KBcdXa%2FLo4YurqbuRAy2K855Yuq8IO22IfSoubcMZvWa%2F5XDBAMNr%2F4XIjo1vL8fWqOr8IjmvoSoq25I2ALOpMcq2fJJVhxg2qKiHCV9Pg15o9OIFttmcLj4bGk5c6eirvL9Y1ecJyR%2FjHa1I3UWpImEYNX1osAAGYjiJqYdTCrrX3QskUTGsoF8Jd0swP4zAhV2sXT28UkUJnmIvUuD0vV%2FNNYV8I7FMvdoniIxhKe2ossYPfd82PooL%2BEFuPlwsdMcW1GZbRx5dsuzoFBiTqrEkYIA0wODPvy9xNid43B66sM9c2PpY9Vi0oBRYpsPD%2FeCYXz0%2BpaGqRp5VyjKGAuefM%2BadrbYLYQMHlCoTk1eryzeExzsoxr8tqO7objcDbMPG3lLarMmmJ1VsECmDEqMLOeBUPUkLx5MZ9HkMcmMMq6jr0GOqUB2j%2F84KSXSOhm9hcULKHh0rCOV%2FSOT7Vco5vUfJb0o%2BQSUfQlXQrJ37ZtoxSY5DTLd64N1ULs21xobFZL15kjKqbVE8SN2UIVdhhpdIR3%2FYR6M6V2rpNRZy3O6idfiaR7%2BhQPs0dCZo7ap4pjXW%2FkjSjs05xFrD4Kr%2FHjPAOwz4%2FIq6tF%2BXqEH3k8GIZVKldbRrd7Sg72lYBgDC1G8e4Qdz9L62vd&X-Amz-Signature=baaec3471e24744353df82b493fe47b7d2935e3275e76f5903c20767fb7538c4&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Algorithmic Libraries
#### 1. **Scikit-learn**
- **Description:** Contains tools for statistical modeling, including regression, classification, clustering, etc.
- **Built on:** NumPy, SciPy, and Matplotlib.
#### 2. **Statsmodels**
- **Description:** A module for exploring data, estimating statistical models, and performing statistical tests.

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c62885f5-417d-4179-834f-d68f8f2bdf39/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VVTRXMVY%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T191231Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDIaCXVzLXdlc3QtMiJHMEUCIQCE3bVJda27BkVgmVHy5IaN%2BrbQ0XaitcgkFTcbm4CJLAIgKgCBSiZ5U0Q7X4i%2BmEOY87ACMdweRkHbRnS2IyifM8kq%2FwMIShAAGgw2Mzc0MjMxODM4MDUiDLUXGVcEWzl3bgimEircA9gBUeguJkHnogP%2FgrruZ3gtvjo%2FdDeWBwxy2CC8O%2FMmQY4vlVOUP6zy7VdihyXVw3we6ADvMZJG80VpDFRAGj0k1MB3nl9XmFJjL%2FQ5FJJZiTVH1%2B85mUYhhyyhlGEK4utAHeFGPhYXLZ4cR0zzrPxCnTOzQHlvtHKzI5VxHNOTHvyHJvyiBmnr%2F6c3RxeoX%2F%2FuSnk0Ek1UMuCP2KBcdXa%2FLo4YurqbuRAy2K855Yuq8IO22IfSoubcMZvWa%2F5XDBAMNr%2F4XIjo1vL8fWqOr8IjmvoSoq25I2ALOpMcq2fJJVhxg2qKiHCV9Pg15o9OIFttmcLj4bGk5c6eirvL9Y1ecJyR%2FjHa1I3UWpImEYNX1osAAGYjiJqYdTCrrX3QskUTGsoF8Jd0swP4zAhV2sXT28UkUJnmIvUuD0vV%2FNNYV8I7FMvdoniIxhKe2ossYPfd82PooL%2BEFuPlwsdMcW1GZbRx5dsuzoFBiTqrEkYIA0wODPvy9xNid43B66sM9c2PpY9Vi0oBRYpsPD%2FeCYXz0%2BpaGqRp5VyjKGAuefM%2BadrbYLYQMHlCoTk1eryzeExzsoxr8tqO7objcDbMPG3lLarMmmJ1VsECmDEqMLOeBUPUkLx5MZ9HkMcmMMq6jr0GOqUB2j%2F84KSXSOhm9hcULKHh0rCOV%2FSOT7Vco5vUfJb0o%2BQSUfQlXQrJ37ZtoxSY5DTLd64N1ULs21xobFZL15kjKqbVE8SN2UIVdhhpdIR3%2FYR6M6V2rpNRZy3O6idfiaR7%2BhQPs0dCZo7ap4pjXW%2FkjSjs05xFrD4Kr%2FHjPAOwz4%2FIq6tF%2BXqEH3k8GIZVKldbRrd7Sg72lYBgDC1G8e4Qdz9L62vd&X-Amz-Signature=6fbefcfcbe6425553eb2641288d0af17905dcc7357d710368a45b0a0770e3328&X-Amz-SignedHeaders=host&x-id=GetObject)
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
