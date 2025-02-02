

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

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/997ac361-58a8-4f04-bb0f-79fea4baa761/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UM5HMWG2%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T081640Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEN%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCMRCQ2JWfL3LCCx%2FZXLaKFDqOI7cHgHTapKUtFPFQNwwIhALu2HD219qnleb3iZjXg3%2BAXUdOvM3HAv%2BcFO65hEjbGKogECOf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwHFluY1hJFqR7LSfIq3ANSKgBuXzXNelRgyE2LukQLPb6B%2F2fAEamforuGIl54KkNXn4oA7cT3i%2FV7oVGib0mowuQ3aNd7f%2BMNGagqERbVqrTwdLRYkoWQ7sY9ynY6T1kL5W1mlygSK9Ou35keOfo95CnEffTnsn3UxpSLxoEd4bMltrID9WJxXtOJbGkWGF9iOp9nLCAxklWRaFbcWWqXoZHHsUEXt3jOV7A4BlDGs%2B%2FM6hKP9fDI6tRYJE4%2FxImRjLy%2FVSkxThMuoKO5rn7W6s6Ytx5%2BJSLXM3N6aLAp4qneMhletun1dMMdc0s00pcKOHUaudRnAslHwcDDj7r7434lVnZiaAsWb0Y%2FVhhdjco0XWooKGvMDlG4Iyw3pOqXHy7OTUC1rvAuSCKHYSG8ZqvLaW%2FP2GLZGdwNsc2AdJT3K0B8ticpc6cAaKt2xxZ92ycXgoEWwLOyYJIRyMJLZgFz3t24xM9BNQNhR4hJ1zmSISiu%2BgqcVIZyBBrqLHw1qdPkjngztkXEnCuXJrkuA%2BrSuZWKCxozaqvnLtObZucB46maAhm1Na9b%2FdPx7fB%2B6SuAik6aQZZG%2BxhU2QQJDre8mmG1rRz62imw6hr2JwwIv2PeROnKYcPcK08smZL9OcvcCYdgwNb0tzCmnPy8BjqkAZ3LEO2nwsJ3hHmi%2FiUxfakJRQC0VYzmwxA1MGtnJ1Bcu78l4frNvRg54JThKhwAOik2Jl1BZ81G0aXP54vFsC4W%2Bt02%2B5YwaxDHLUCBqblrRkJv2nRdZ0UuR9nXiAGi%2FxNFLhbN32gkTj%2FkL%2FCedVlsYOwNyG%2BZMVdIvIHHo737x%2BTf8U2acmsPovgkbMtV9xdEJk6mg%2Fjya0dUHuIGjZPy8Zzp&X-Amz-Signature=14a235051b436cdc3d290d475f914a0022e1cf6d652109cadd1ca981233222ba&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Data Visualization Libraries
#### 1. **Matplotlib**
- **Description:** The most well-known library for data visualization.
- **Features:** Great for making highly customizable graphs and plots.
#### 2. **Seaborn**
- **Description:** A high-level visualization library based on Matplotlib.
- **Features:** Easy to generate various plots like heat maps, time series, and violin plots.

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/733d1e42-5a53-4fd8-90c1-3d85254369a6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666UVP6LZ3%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T081639Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEN7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIApsoB9d61KQEHHhDCD5JNUR6p1NFqIrrOaiJdfs4Ad4AiAgYeJTbQO8%2FpLEx5Nh6G1mB3K0ArbGz9eSGDa3XnPc%2FCqIBAjn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMlFtcqoidv2N4%2FEGoKtwDEWRq6asFv1pjWTmCFTJ29EzQELSij%2FUT%2Fb5NWkSCjhiotCXMqInB4DPNFdHDEQa3DddaePGfaHBtvRJozU1pb4RyTsejfykbpA3upSnN3NkIIbx2trrSdMo8XBb2QwhXbADiUBDMRmJ%2FUIGYQ%2Fj%2BbIx1jv%2FQg5oU%2BA4b34xqDdho8bbN%2FPKXQqmjNWk6Wz5ApgthdHrlEyl79jSYExqJW0Bd1NO71Ty24FEazJmB6lGpWLpdBeOCCyRz42ehQTLb%2BxTH4GJXA%2FwyDh%2FyjPBMEG9iXaThSK9ebL5uUK1cf0s7Enq0wLEX0a2gkBGw2S9utCc7eEDWC5w8mRI7ok5Ii4Jrw8sBVq4XGC1p3tgZo7HcN1bA2bJX0hBDDS0bTwHTEMUgNHxOBA%2BwY%2FJtnVIRINU7d70hbX2XwudaR%2BcI2K0XRZfW2cd5oR0DQw5JauZZNY9gs9LXnUBgAhgh7l%2FyfgUd%2FghBhSe3XkmdGrQw99co4KzMzV7mag2q6GHggfudE%2BsYp8pUU0woxVx%2FsUCbbAPh5ccLGJ92eqyEdETDiP3XsMyonRUJSU%2BqZGApW14YIkDN3yTUNKiLVE%2B1NpI03LLn0hA1NnIjWZ3qDwIsvkzS96nj8pmtW8RCJ8Qwz5v8vAY6pgFk8w1llI9FWUDYi7TjvcEmOxQ2A5txHd%2Fxg1OPMWfI3uAx87qnhIHA1nvgFhWFYyS4wmtCZzg%2FV0alFDch0pEIZbx3x3hRHfsNF6121p%2BGx3RCvkv8LrfbmQmfgd0NRuj74%2FD099eZxEuIFtFIrZjd0j%2F4XkP%2FCct3WoU0gfW18fuubqEMfA4Q%2ForwkubAC%2FN0WhrQlkk6T%2BzYnSNgVnLOHUPfdHR7&X-Amz-Signature=0f4c49a91384716ef6703d15cf6161042559057c7a2fb531f86b82745855fba5&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Algorithmic Libraries
#### 1. **Scikit-learn**
- **Description:** Contains tools for statistical modeling, including regression, classification, clustering, etc.
- **Built on:** NumPy, SciPy, and Matplotlib.
#### 2. **Statsmodels**
- **Description:** A module for exploring data, estimating statistical models, and performing statistical tests.

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c62885f5-417d-4179-834f-d68f8f2bdf39/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666UVP6LZ3%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T081639Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEN7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIApsoB9d61KQEHHhDCD5JNUR6p1NFqIrrOaiJdfs4Ad4AiAgYeJTbQO8%2FpLEx5Nh6G1mB3K0ArbGz9eSGDa3XnPc%2FCqIBAjn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMlFtcqoidv2N4%2FEGoKtwDEWRq6asFv1pjWTmCFTJ29EzQELSij%2FUT%2Fb5NWkSCjhiotCXMqInB4DPNFdHDEQa3DddaePGfaHBtvRJozU1pb4RyTsejfykbpA3upSnN3NkIIbx2trrSdMo8XBb2QwhXbADiUBDMRmJ%2FUIGYQ%2Fj%2BbIx1jv%2FQg5oU%2BA4b34xqDdho8bbN%2FPKXQqmjNWk6Wz5ApgthdHrlEyl79jSYExqJW0Bd1NO71Ty24FEazJmB6lGpWLpdBeOCCyRz42ehQTLb%2BxTH4GJXA%2FwyDh%2FyjPBMEG9iXaThSK9ebL5uUK1cf0s7Enq0wLEX0a2gkBGw2S9utCc7eEDWC5w8mRI7ok5Ii4Jrw8sBVq4XGC1p3tgZo7HcN1bA2bJX0hBDDS0bTwHTEMUgNHxOBA%2BwY%2FJtnVIRINU7d70hbX2XwudaR%2BcI2K0XRZfW2cd5oR0DQw5JauZZNY9gs9LXnUBgAhgh7l%2FyfgUd%2FghBhSe3XkmdGrQw99co4KzMzV7mag2q6GHggfudE%2BsYp8pUU0woxVx%2FsUCbbAPh5ccLGJ92eqyEdETDiP3XsMyonRUJSU%2BqZGApW14YIkDN3yTUNKiLVE%2B1NpI03LLn0hA1NnIjWZ3qDwIsvkzS96nj8pmtW8RCJ8Qwz5v8vAY6pgFk8w1llI9FWUDYi7TjvcEmOxQ2A5txHd%2Fxg1OPMWfI3uAx87qnhIHA1nvgFhWFYyS4wmtCZzg%2FV0alFDch0pEIZbx3x3hRHfsNF6121p%2BGx3RCvkv8LrfbmQmfgd0NRuj74%2FD099eZxEuIFtFIrZjd0j%2F4XkP%2FCct3WoU0gfW18fuubqEMfA4Q%2ForwkubAC%2FN0WhrQlkk6T%2BzYnSNgVnLOHUPfdHR7&X-Amz-Signature=422d912d24749a929f3ee13b5e6561da9329e60e8eb33281d14728eb6b4a9fec&X-Amz-SignedHeaders=host&x-id=GetObject)
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
