

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

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/997ac361-58a8-4f04-bb0f-79fea4baa761/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Z3AHXUDN%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T023935Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCDxx8Jz639qUdaVVD4VP%2BdXCglPdQ2Z0Q014mjfMIcRAIgRFg%2BPdNBRRH4lrLrKmyNaFq%2F0lTRxN9a2S9325bNd8wqiAQIm%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDBCyDEWoJllnWXGSgSrcA2rE5iFuE6e26sBTsHgg8zL%2FEmEJ0yy9RwN0twNTyk%2FAozzsX8PJAT7O5x3Gd0bgShE65i%2BmJb3gSi0dXbBcDoE5ugAzDecSm0PMbDPudIcyo1wljXS%2FdK8Uce%2Fs9avgj5DlXE2jU%2FH5DMECQ361lADVGMc4X3JOx7SrKQ7%2FLx1IEE3OkjAJnvg951LWBkMcRf6G3qojXGJxjsjJxd9dje9cvbfSEHbvjVmAtXxmCU9n6gE8vk%2BsC6Xd%2BUelLL%2F3yimQxJMwneGeoUYY8dJlfwC%2FQU%2BqIYxVFlzk4RhgQGkRcwxHOQ8tMRJngwKqSJandGXv4cSDRQk%2FWiowVh458bIXac4zlgZbja4BApWT7h4R6ubCg4nsfKdXGaDMY%2BFN92HbRgpvUcsndaIO5hH%2FDUIDSZbBxbB04XXOZQnMVDrk7i3oGTeS5vrGMBFuqUVTSqcWcaKMkRhrw5j6OfKTANeND5FmfAPGAGyONk2qmxBT6Yt9LAnQnmhzisfThXb%2B4yOV1HASX%2FIyh%2FqWhuVTqI2gow3NdRJlJ%2BNiLjby96HcNisoRk1XLPlwrp9RwxCKF499pPLqBR6DWcZftdgS1zy%2B49Mad6QeydWJpwl%2BiRsDtyXBZKqnRjXMNumNMM%2Bx67wGOqUBHvQSjG1qmS5VFLFS987uH%2FvuGcOKf7C3IN9zUhdrzB4JbG9do2AVTtKcV4lFMYdpMPhEwIuvqlHy%2Bi03km2t97%2B4CI5o%2FxhbAnu6O4n7ffPP%2BZG%2BtPpwhz7D0rRzakoO4jzigWA2VtyKLdHdCmAZQmj9mSv18eS5L4UXVQH7kinGvMZkJEgCaQYkMNYImZ01g4Q9zxaCDTUAUFc5nhKyMZ3S%2Bnx3&X-Amz-Signature=d840795c22b832cd86379126d905033c2744cf3f73a335943896cf08e7b372ce&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Data Visualization Libraries
#### 1. **Matplotlib**
- **Description:** The most well-known library for data visualization.
- **Features:** Great for making highly customizable graphs and plots.
#### 2. **Seaborn**
- **Description:** A high-level visualization library based on Matplotlib.
- **Features:** Easy to generate various plots like heat maps, time series, and violin plots.

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/733d1e42-5a53-4fd8-90c1-3d85254369a6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TG32NOHU%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T023933Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIC98XazzyebqLHSCd5MFViAz%2FPxZCKgBC0%2FUG4OqUGogAiEAppCt0Qx3MMlpvPjAPrIgLXz7r%2BpnVOEzttdUmMTMdbwqiAQIm%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDE%2FohrQ%2FnUYmdUow%2BCrcAxxHDGGmeik75oBkXPoQbI2adGcSadJ3nerJrU7DrzbH6FLZut366PcsdN6sneBaet1IsK9HK6bQedzrTWxnKKqelqBAke8hUalVcyeOK7ndgAqkEX0FCtTHRFzdY4p2lLsn8BzexQUrVWrdJAgpDYUI7u1ebw1gLN5LmKM3aXUrbOI71g2EDqMnSUeTfTj1blUDmY6F5Mjin20DAG2xylItDg3Js%2BC91hbgKL4W0mf%2FSq782Kwo3trccVqnnYfYJEsLY%2FuwWiQMm5Qv5SJs3iSFTc%2BLD9MP2i5iceBoKcH4J3E1U6J7AJNEFuoNi74T%2BbD%2FWfU9L%2FU71mGiyXH88RD3WXp%2FLyw%2BX6MdkjZ2kSYmCT3QGdiq2m683OEebP7t8PqCDvLqCTeQTOR8ejTbcGWonP%2FPAw%2FwS%2BnQ95txT3M4pz4gjcIcnT1PbBZQHKkqpAXqkh6KAPtjmY%2FbsIO8VNkn3gFSvwDjmQv5hl0reKKrP3bUQlee5ERCh45KhD54%2BAlo%2FzijDO5AmbU6XH4N8Ts5N9UxwQuv%2Bb673FxUYOYkAkQBjdulPP7gYZbIGNpxebkihR5Q0DI5XA8Sa5I9HdeDsyFoxX2%2FdrZFtw0mZ7sZT6Of7Zp%2FAHFxxHsqMIay67wGOqUB%2B0fQZbRGCUc%2BdFGtGI7pD%2B1vbnSc8yLsd%2FxkC6Vd4TKNw8M70W0iFarnncfnGCSviGdfk1mjmnq3Y7xy5lyHN%2FQanSnO7HwnXCT2iANR8BP8GobVnEDD%2FEsoG13P7rdRVnpsIIOYGW%2F5A2sPb3gXfD9yU7XMvev3%2BoBGv4yTMjG581ouQPehaYWcGa3e3y9JdyC7ZRshn1bST7v7iWrsnmkuoKLK&X-Amz-Signature=a24be87310d19ad430ba63289c5ababe26b5f3f3e37d000738ac112c532f22ba&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Algorithmic Libraries
#### 1. **Scikit-learn**
- **Description:** Contains tools for statistical modeling, including regression, classification, clustering, etc.
- **Built on:** NumPy, SciPy, and Matplotlib.
#### 2. **Statsmodels**
- **Description:** A module for exploring data, estimating statistical models, and performing statistical tests.

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c62885f5-417d-4179-834f-d68f8f2bdf39/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TG32NOHU%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T023933Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIC98XazzyebqLHSCd5MFViAz%2FPxZCKgBC0%2FUG4OqUGogAiEAppCt0Qx3MMlpvPjAPrIgLXz7r%2BpnVOEzttdUmMTMdbwqiAQIm%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDE%2FohrQ%2FnUYmdUow%2BCrcAxxHDGGmeik75oBkXPoQbI2adGcSadJ3nerJrU7DrzbH6FLZut366PcsdN6sneBaet1IsK9HK6bQedzrTWxnKKqelqBAke8hUalVcyeOK7ndgAqkEX0FCtTHRFzdY4p2lLsn8BzexQUrVWrdJAgpDYUI7u1ebw1gLN5LmKM3aXUrbOI71g2EDqMnSUeTfTj1blUDmY6F5Mjin20DAG2xylItDg3Js%2BC91hbgKL4W0mf%2FSq782Kwo3trccVqnnYfYJEsLY%2FuwWiQMm5Qv5SJs3iSFTc%2BLD9MP2i5iceBoKcH4J3E1U6J7AJNEFuoNi74T%2BbD%2FWfU9L%2FU71mGiyXH88RD3WXp%2FLyw%2BX6MdkjZ2kSYmCT3QGdiq2m683OEebP7t8PqCDvLqCTeQTOR8ejTbcGWonP%2FPAw%2FwS%2BnQ95txT3M4pz4gjcIcnT1PbBZQHKkqpAXqkh6KAPtjmY%2FbsIO8VNkn3gFSvwDjmQv5hl0reKKrP3bUQlee5ERCh45KhD54%2BAlo%2FzijDO5AmbU6XH4N8Ts5N9UxwQuv%2Bb673FxUYOYkAkQBjdulPP7gYZbIGNpxebkihR5Q0DI5XA8Sa5I9HdeDsyFoxX2%2FdrZFtw0mZ7sZT6Of7Zp%2FAHFxxHsqMIay67wGOqUB%2B0fQZbRGCUc%2BdFGtGI7pD%2B1vbnSc8yLsd%2FxkC6Vd4TKNw8M70W0iFarnncfnGCSviGdfk1mjmnq3Y7xy5lyHN%2FQanSnO7HwnXCT2iANR8BP8GobVnEDD%2FEsoG13P7rdRVnpsIIOYGW%2F5A2sPb3gXfD9yU7XMvev3%2BoBGv4yTMjG581ouQPehaYWcGa3e3y9JdyC7ZRshn1bST7v7iWrsnmkuoKLK&X-Amz-Signature=892de84ac49aaae0fc6ce3543acacc48698f3bb7c74276a3068c7370eb795876&X-Amz-SignedHeaders=host&x-id=GetObject)
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
