

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

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/997ac361-58a8-4f04-bb0f-79fea4baa761/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T6Q4TO3O%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T231338Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAcaCXVzLXdlc3QtMiJGMEQCIAZIT21IM9WkdQa24Q%2FOOdrHpz7EkVpuuRI3mS29IZAXAiAcNmErotzCp2IMuyKW6KTTazUMW5YaSdL3hxuUt3zXJir%2FAwggEAAaDDYzNzQyMzE4MzgwNSIMD0v138cMRr8pmfFnKtwDL3aG0TJwNU4AmScFmGi267jjc0h%2F%2BTM46oITW0aGndldZEM%2FI54kqnJPpX3XRVgmYWvJP3KndMr8jzWnfVFnxVBsaDDsGofwqFsDnj8ml8iEmqqyUD4tmGSwe8vxOw77S%2Ff6NOztHv2DXYD0ltk4NsIw0IS4WkngpZUSE%2BsxpuEC%2BD1ksiBekYdYBcSX%2FymCtrLwwz%2FnQA5gCnpWjmeU2AaK5yyLUJyy4jO0Ni01uaapqsKsLoVqTMoAdR27H8VISLztwHibuuavmgYMDavw3kfPm8AdFqzySbyoox6OkZpijBVI1BrUnidNeo%2BYlrOC4oKcFYk9o%2ByoLiCLDBWX15LUMgC91cx9Z4ih%2BqMnCJ6Z76aN%2BkzwJ9LNWharGd%2BNZizI1ztnEwU4DN7aOYr%2Fb%2BoxXka%2FJ1%2FEHDrJIoMH670DCfzjDf2wFn9gFhPpDbUU1dc4q9u5andXI4bFdvIWrm9u1DPNWlEGktUcH03jrUPJEJugbg4MoNgtWkuMX5rsuYrdrD8RlDYedd0A632G3N79B35bUm46cDdVCldEnpUO4dMiEw3nZUquLfFMnqCV4MJcLHt1xkPSpxpFPi0SO5QKdapVZya7n4yFMFIoL3HeZmIt7EfUABiDOZMw2pOFvQY6pgED9r5AZ5w2VQ6WeiI%2FUhju4gKPP4F%2FN3Bv%2B37mEowBbxt4mStfCDXJnj54jglBjmafnW0MZH2L4QWhuL1k7hydr%2BYuKRtSKwDtmpPRDPaUnw4qo3U7Jz8deesGqUz8k0bQyoUr%2BMVx7Ewfb314TfIMwFQ5bUZPUXKDz%2FlzhSa7aZO%2BSwBKhN%2BrSCGTo2EO5Cst7vQx%2Bc7mZASVKl1azP%2Bxf4%2FS6GI0&X-Amz-Signature=6df5f7a3f8b56ef5451c878d560dd03a47a3866a36dcc223a4cd47ee0b02e55b&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Data Visualization Libraries
#### 1. **Matplotlib**
- **Description:** The most well-known library for data visualization.
- **Features:** Great for making highly customizable graphs and plots.
#### 2. **Seaborn**
- **Description:** A high-level visualization library based on Matplotlib.
- **Features:** Easy to generate various plots like heat maps, time series, and violin plots.

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/733d1e42-5a53-4fd8-90c1-3d85254369a6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46663SAXJIM%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T231336Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAcaCXVzLXdlc3QtMiJIMEYCIQDV%2B55%2Bb7n7FUTi2wHr77RAjxDXX%2F%2FG2ezlZtaKrZN4cQIhAMu9z86VJT910NPOwWuaiTM%2Flrle0oSAHH%2B%2BTnwEu7cDKv8DCCAQABoMNjM3NDIzMTgzODA1Igxfk0rQyV%2BiuJwCZAEq3ANmcUelPFWY0UO9%2BS59OCxzFaGbWArfPU3lzkTdcbkPFR%2BQEp05zVMnp4IfeT8HxI%2FF1qtuISj7X6krZtnpvgSHZYkN8Wd1aXCog56mHS8HI8C7d6dkUTRPqMMcRTR2La7UVEMrU36CHhzNzoLFixSSWCFZHEUAXZREBYJlalrcrpfStlFCGVcAd8WsmqBJVLfpHgn7%2F8MaZZVHt6G1Asbza4rbfHdbgKjRRQeqswtd8ncZwKd4PRn2FZsF9r6F2QKza%2BYszu80kMcXA1Vg3zvGc%2B8VMIepjefN63Puv3pSJZxdIy780jV4RlL7sP4rCnIg%2BljqOpvALYMe%2BUDXRrRq0XHisMTW7xixEud9iDgLGsgP715ar1vquMLhM6qCXSPws3TtBLKJneGRCUq6YtuNxtb4Tw12c1P6pXLA3zj6NL7Ssz%2BVkn8eFSs6jKREYKW0cJfGzlsWlH7PQ7WXfY4LwZyskkRGs%2FptJ24A5fJCMhxNopB5G0ghwh77hbhJZWV%2BQLDM1D9iRbgdyw1BdqhdduIa%2Bh4BpG71blb5%2F%2BZVLhdgcPzZ4cgsZRHPPjjuXcJo5L6h%2FAQXBth6pe4TjvJc9UHoZom7a8i5jkP5vY5OyYkfJAMr%2B6QT27U7hDColIW9BjqkAfhVVhC8iYW1Lc%2FVkU5gMxudrZxXbJCg78osAjEWSKSFrEja%2Byk3JHlSRlw8dD7cIrKwSpDl2eeyVmryKczTG%2Br3AsEwwd%2FSLYki95jt4uMABo9AV0QmD%2Bh2p%2BIauCOtJjlxEYy4en1CaYyiz3B3PJxW%2FioSCd3oAooz64k%2FtcJHGb7%2BuhxGYerKgiLso8QgYAcgFyCoIyUClnIWyKjxjm73hlD%2F&X-Amz-Signature=05be4d8bb050a189efbd656cae8b8f6fc12a003e5c30d8089e15b42021d99355&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Algorithmic Libraries
#### 1. **Scikit-learn**
- **Description:** Contains tools for statistical modeling, including regression, classification, clustering, etc.
- **Built on:** NumPy, SciPy, and Matplotlib.
#### 2. **Statsmodels**
- **Description:** A module for exploring data, estimating statistical models, and performing statistical tests.

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c62885f5-417d-4179-834f-d68f8f2bdf39/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46663SAXJIM%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T231336Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAcaCXVzLXdlc3QtMiJIMEYCIQDV%2B55%2Bb7n7FUTi2wHr77RAjxDXX%2F%2FG2ezlZtaKrZN4cQIhAMu9z86VJT910NPOwWuaiTM%2Flrle0oSAHH%2B%2BTnwEu7cDKv8DCCAQABoMNjM3NDIzMTgzODA1Igxfk0rQyV%2BiuJwCZAEq3ANmcUelPFWY0UO9%2BS59OCxzFaGbWArfPU3lzkTdcbkPFR%2BQEp05zVMnp4IfeT8HxI%2FF1qtuISj7X6krZtnpvgSHZYkN8Wd1aXCog56mHS8HI8C7d6dkUTRPqMMcRTR2La7UVEMrU36CHhzNzoLFixSSWCFZHEUAXZREBYJlalrcrpfStlFCGVcAd8WsmqBJVLfpHgn7%2F8MaZZVHt6G1Asbza4rbfHdbgKjRRQeqswtd8ncZwKd4PRn2FZsF9r6F2QKza%2BYszu80kMcXA1Vg3zvGc%2B8VMIepjefN63Puv3pSJZxdIy780jV4RlL7sP4rCnIg%2BljqOpvALYMe%2BUDXRrRq0XHisMTW7xixEud9iDgLGsgP715ar1vquMLhM6qCXSPws3TtBLKJneGRCUq6YtuNxtb4Tw12c1P6pXLA3zj6NL7Ssz%2BVkn8eFSs6jKREYKW0cJfGzlsWlH7PQ7WXfY4LwZyskkRGs%2FptJ24A5fJCMhxNopB5G0ghwh77hbhJZWV%2BQLDM1D9iRbgdyw1BdqhdduIa%2Bh4BpG71blb5%2F%2BZVLhdgcPzZ4cgsZRHPPjjuXcJo5L6h%2FAQXBth6pe4TjvJc9UHoZom7a8i5jkP5vY5OyYkfJAMr%2B6QT27U7hDColIW9BjqkAfhVVhC8iYW1Lc%2FVkU5gMxudrZxXbJCg78osAjEWSKSFrEja%2Byk3JHlSRlw8dD7cIrKwSpDl2eeyVmryKczTG%2Br3AsEwwd%2FSLYki95jt4uMABo9AV0QmD%2Bh2p%2BIauCOtJjlxEYy4en1CaYyiz3B3PJxW%2FioSCd3oAooz64k%2FtcJHGb7%2BuhxGYerKgiLso8QgYAcgFyCoIyUClnIWyKjxjm73hlD%2F&X-Amz-Signature=a6819a8c108134549e029718e50622445cc0642ccebf96b1f6a3f4142ef3df3e&X-Amz-SignedHeaders=host&x-id=GetObject)
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
