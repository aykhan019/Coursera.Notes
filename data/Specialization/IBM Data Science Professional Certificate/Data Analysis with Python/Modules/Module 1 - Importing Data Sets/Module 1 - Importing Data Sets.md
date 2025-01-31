

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

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/997ac361-58a8-4f04-bb0f-79fea4baa761/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QAPBUSC2%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T031552Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAXbTa7mDWbam8lz70MC6%2BkOywPZKlbQPjxT9Loc7vhSAiEAknE6dWOxM94Rj3nHQhUrOt9UiQueYw2XY8VtuVJe20gqiAQIs%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDCaW1oeLjtmrccwjnCrcA%2B0F5ML1mOBjUN93td8ulXgKfhHE6tSwa77CD%2BI411ORskNUUXq6T8naXgtMn5zn8wAyh0GKOiwl83zcye%2FsfInKWLrmXSr%2FX16QX14AeKY%2BkUCf5kkx6bGwauu7ORdvmUS%2BxXDfzcmM8tTaq63moan0jjHlhpE%2Fx%2BAUsBMxSql9hOU74ZKzS4fSJzqXVn302C5GV0gV%2BF7MgCIGGpj6wssbZKIens20q%2FcWk8WvwjjYz5cRL5z1hiGkOgJ1bwoVW4MTz3BgzlYxB7TL9UyebkxOvOh74NY%2F%2BVcbJxHYJbHwzs2x81QSVt81U7Ru5GpwpyVPWYqGTLurWTm6KhtVYAGv2Ihuvw2zTj%2Fqww3UVOwiu8XoeOTaTclDhYEq2Dwvv6sm87s7VWWYgPe6kGrdIKdu7Yb7pEQQ1m08RaD4sDurVse%2BuTvydum78gSXJUVT%2BSRYrSht%2BP1C0wxi7pXRYDwjV%2FEMLFBoGxPt0Aln59fM9e%2BAa7OPC7hXpolRhND%2Fti1rKH9gCUN2uGL20bJ%2F3xsCpBTLTmhx7lIQlK%2BGPfE9w%2B3qdGK%2BTr0TaAREo2ApTEJy0rdFTnnEAuYHaq7%2FVCLzJ0I2g8AzQIYdgvMGOfx56JNAChBgLuTsk3MtMMXQ8LwGOqUBZW%2B2lRGJTP2%2BuhowbQ4mqKTxc5ZgjxxTxeyZKrHxPzALkCpnAz%2BCa4Kqkw7nNpMrTFN1UTgE4V3AiiZF9%2Fqzmi0SXE4QI7XTQoSb7kyAmGS1em52XBCyaR8Gsh8trg4hwvyINUim89v2kbLKr9%2Fs3Og9Qz8BHCXh7r7TguZfQYerG4GKgf1q0NhvTyeEynG%2Fy5BFqowOdlfkzzI%2BBUc98C791V6K&X-Amz-Signature=c348518340de2ad1c072d24769ef59f044604f3a8d50c010bab9e4c7457cc6f9&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Data Visualization Libraries
#### 1. **Matplotlib**
- **Description:** The most well-known library for data visualization.
- **Features:** Great for making highly customizable graphs and plots.
#### 2. **Seaborn**
- **Description:** A high-level visualization library based on Matplotlib.
- **Features:** Easy to generate various plots like heat maps, time series, and violin plots.

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/733d1e42-5a53-4fd8-90c1-3d85254369a6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZD4GCQZX%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T031551Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFo4ef6JERPbx37gOMXW%2FbUDt72sRNofVZlP3aNgXS2EAiAe0QqkIjwUz3Miyqu30%2FTt%2FPMk%2FWxsb%2FEZbwc4%2B%2B66XSqIBAiz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMs%2FeMUHDj8eZjEF8vKtwDw8QRgZ5M%2B65gmQNF%2FQzT5R%2BEvLdvcKMn4XaQx0pjcB0QVZqNEPBBxUSn8Nk2843a4kd4ZZqcU5eamEKSzGFcXBpmSkXGDO6nxCViZeCc8OVEvVdXy6bfYEW2Fj99xy49cCRAjXIRzI81vRlcH1DHhEmR0VYMnmYbP9RARgE7LKeBrl15NqYjUuhVn9hTOwNUFKKtUvJlzWkKDWvJxNSF9JU3dbVzRnP4OJDy5fWONMGca5Ez3k1camnINHdPkY9kH0QBTJWgxxl4H9wuNSLxP8G9Azgo2yysFtkj2LsxdDbf4VS%2FokpcFcGpnPVI55ekCrbJjdnrtw82s9xfmbg5ReKom0NnWsZtR8C0rDyiR9CHguwLpNkyORK4BlxrykkVZk0ojaMk%2FmXcFkyn66eOmmNtleF5WPpcXUEXh7zbKdfKErDRf7X9o7Zyn%2FLVtXJgv%2B4lVjELRrLM1rTXLRYEGb8%2FhDMgNQgxGkvriv4RbUSP%2Fw3K%2BqUELaOyPDbJMUOeYSI4491K9xURpwVEZKcPszRldcPQX6qiyh%2BqqWIdXHd4qlmrv1GrVhmOQRl6N4VySeKyziDAXedi87s0taXlk%2B0ntSWMXaNv%2FkTNJMZUR2rMc3tUqeSxhlqJXa4wiNDwvAY6pgGdXjxuvlBjhDP8TYiUVYMJ9HDDj8k6a9sJv%2B9n0PrOK2xLJHB80lemm3Q18YsBvty674iILuGWTHoLg93JyjKynJkb0rHLTecVix%2B%2BE%2BqQCQ5RMnArYbh5scI786LsaUyto%2BZztgxUsQD9MVjm5PEBvyF4DTcA9KXJnlXelsr%2BR5CBRYfmPOvBQxfxrYGCfcWwzucuIKByro0nkWVz2L%2Bj5EQo2Xap&X-Amz-Signature=962a36c9ee77b7018618794d3f87fcdf8e3365383ecd2f093f21e3970d3f30bf&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Algorithmic Libraries
#### 1. **Scikit-learn**
- **Description:** Contains tools for statistical modeling, including regression, classification, clustering, etc.
- **Built on:** NumPy, SciPy, and Matplotlib.
#### 2. **Statsmodels**
- **Description:** A module for exploring data, estimating statistical models, and performing statistical tests.

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c62885f5-417d-4179-834f-d68f8f2bdf39/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZD4GCQZX%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T031551Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFo4ef6JERPbx37gOMXW%2FbUDt72sRNofVZlP3aNgXS2EAiAe0QqkIjwUz3Miyqu30%2FTt%2FPMk%2FWxsb%2FEZbwc4%2B%2B66XSqIBAiz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMs%2FeMUHDj8eZjEF8vKtwDw8QRgZ5M%2B65gmQNF%2FQzT5R%2BEvLdvcKMn4XaQx0pjcB0QVZqNEPBBxUSn8Nk2843a4kd4ZZqcU5eamEKSzGFcXBpmSkXGDO6nxCViZeCc8OVEvVdXy6bfYEW2Fj99xy49cCRAjXIRzI81vRlcH1DHhEmR0VYMnmYbP9RARgE7LKeBrl15NqYjUuhVn9hTOwNUFKKtUvJlzWkKDWvJxNSF9JU3dbVzRnP4OJDy5fWONMGca5Ez3k1camnINHdPkY9kH0QBTJWgxxl4H9wuNSLxP8G9Azgo2yysFtkj2LsxdDbf4VS%2FokpcFcGpnPVI55ekCrbJjdnrtw82s9xfmbg5ReKom0NnWsZtR8C0rDyiR9CHguwLpNkyORK4BlxrykkVZk0ojaMk%2FmXcFkyn66eOmmNtleF5WPpcXUEXh7zbKdfKErDRf7X9o7Zyn%2FLVtXJgv%2B4lVjELRrLM1rTXLRYEGb8%2FhDMgNQgxGkvriv4RbUSP%2Fw3K%2BqUELaOyPDbJMUOeYSI4491K9xURpwVEZKcPszRldcPQX6qiyh%2BqqWIdXHd4qlmrv1GrVhmOQRl6N4VySeKyziDAXedi87s0taXlk%2B0ntSWMXaNv%2FkTNJMZUR2rMc3tUqeSxhlqJXa4wiNDwvAY6pgGdXjxuvlBjhDP8TYiUVYMJ9HDDj8k6a9sJv%2B9n0PrOK2xLJHB80lemm3Q18YsBvty674iILuGWTHoLg93JyjKynJkb0rHLTecVix%2B%2BE%2BqQCQ5RMnArYbh5scI786LsaUyto%2BZztgxUsQD9MVjm5PEBvyF4DTcA9KXJnlXelsr%2BR5CBRYfmPOvBQxfxrYGCfcWwzucuIKByro0nkWVz2L%2Bj5EQo2Xap&X-Amz-Signature=c9c32f74cb2b1829d2a67db56161fd48ea76be8d7a0996dc11d6dad5201f9e5b&X-Amz-SignedHeaders=host&x-id=GetObject)
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
