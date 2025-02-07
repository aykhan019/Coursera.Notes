

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

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/997ac361-58a8-4f04-bb0f-79fea4baa761/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663OFNKDCD%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T141341Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF0aCXVzLXdlc3QtMiJHMEUCIFJzIT82L4V8w0SySDoyBn%2F7XeYnmepiejZ3pipTf3q2AiEA3NbhjV7WY%2FR4tAfNQ6SNHbbh3A%2FG%2Floe5Twi6OMMdrYq%2FwMIdhAAGgw2Mzc0MjMxODM4MDUiDIbOe1v%2F5WL%2FCANIwyrcA1V8O1BeUQ98xTjd6lgC4c%2FZI3q64Jp8fu9vOEoOgirk1m79iWTIpoHn7DnV%2B1cKXIkNx5JfljicCsSrS%2Bexp4%2Bn1XbhKUvuHcWdfQFdkjl3mj%2BoOxrbBVjutoyoJU%2F8KnnYRYECZO9ZUb6GSgg6NVEOsQgKkCDYly%2BO%2BholdT6Og%2BAewuJKmfayFrHVRXcy%2FSRPjmANh7nBMpOwI3GZozLcAUMW2Ta3ZM8HeVyEM4BjFxMRCd3vvujH0TkOlDbQhaals0mKLoO5i2PgeGOqKy0FGnBl2m90TfiFjoJyktWn4ohMURKfhRG79gle54pZlGVm4TGVlXA4HH5G%2FddQNSY8aJhnb6Utz8V6EmZIvDMubJ5VFKdfV01WJKz8cLAhqbBtAdlOChpsS9hn2J5CuZwfAXLaBzg1Y4c9shrA6EU2ShhzcrsDKB7nEJHvuCTEMAUi5iQbS9xKkNCefZYEjm4DPxeQOzwokwhvEdpQOjBRGl4GJ4bWO3kr7uelzzlu3FO0bZ19LXtvZvQ66Th%2F6r%2Fi1F4PUktG4TsYwAsNZ6wxOg%2FMrIcaaXO44KbAEqJuvxvgH%2FMVm9ZJEJkiL%2B5RNfiGpFmcRfVIAhd6HUDy1cCw27htviW56gBT8nbZMIeLmL0GOqUBsSPocG1SonWS959HIH9hUaOrCG5tKqaLaa%2Bny%2Bf1vBVoApwJWFqYXhoQ4aM%2FQh4j2fPiGSLtBU0McgrfzB0qylt5Hdp7fWT%2FlM2lPH8YmrVA%2BfTWo1FpgL9UxopcQsjp4FJoQ%2B4kHQkeuYvk%2BqbB6g4cfVntDJmgecrT7APLESroGOJ1ngHUkeA5o%2BVYo8ZEXK8Hbu3z7iB%2FA%2FjWK%2BIi1HYO27x7&X-Amz-Signature=3d5faf62c501c7641301bb18d698ef9ac143e84d081f079dfcd55ff979e338e4&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Data Visualization Libraries
#### 1. **Matplotlib**
- **Description:** The most well-known library for data visualization.
- **Features:** Great for making highly customizable graphs and plots.
#### 2. **Seaborn**
- **Description:** A high-level visualization library based on Matplotlib.
- **Features:** Easy to generate various plots like heat maps, time series, and violin plots.

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/733d1e42-5a53-4fd8-90c1-3d85254369a6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RQXF2W3G%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T141340Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF0aCXVzLXdlc3QtMiJHMEUCIQCt%2Bnw6PK29JQkUFwAheLi8j227g5b5NPt8aWYF9jgXfAIgQ4P8qXa1yhdsLp1smbb55t3c5axtNx8OM8XiQr0%2FQ%2BQq%2FwMIdhAAGgw2Mzc0MjMxODM4MDUiDH%2BABvcwlHKVzX4gdCrcAxZlxwxexlsQfgV8vEOpt%2B56W7OUsRv7azq5Q0BTlielx7dd0oDX%2BYWVpVVKZaFWAmyie3lN5oVAGe1mCXF4xrMD%2Bq39H1GT4WjS%2Bw%2BSgBtpj5c70LAP%2FE1bMaes%2FPKaCij7H3LfMN67b%2Bsdjp2sMBuQy%2BUwj9MuR2lclJZ3m0KG6OHaTQkzqkV%2FBwA%2BVJvx6x2fdQNfV0lWWVqNJ0THp2P1CbwbaXzQm7ErksFWVkWq2uGogmRqfb5myUR49ij9UriW37ltN3gf6%2FaenIMKNBAbZs4RyCnT5QMBc914ElCrPgegKWnZGZTzlp60C8y76dBArYWfs4aBkoWpRJJLEwpw1GaZbgzg%2F9ePBQPLrQIlEu12MYXOajd%2FMFvAnTYS74IkWjnBPoz2s%2F5w74vz2uBzd%2F%2BbKSA9E0qMz3PgCEqDFVZK5JfuS7Px08klUGgaPu7ZHyI%2B2ImE%2FrtPfLGD2SqZ4TbUFZS13oBQCrUFPRD4SFGhmFLe9vRndViW8Hurgjqtqv8xZTJU4dhVZQsBoF%2Fjdn3IntXchTxeOze59lAEIW2drumnGS0sfBsqxN1gu96NoftH45u2EOgM7GAhpXWqJAnIGPTrxRkwe4v74dV%2BhpZbPruFmSa57u1DMLOLmL0GOqUBh1dGjChaCRO9bwKLkSXrfnjGdyfhc8AaoDJTehiNe8hvJxAdsaPmynanlsDw%2FnUBtsHlAQt7IOvF%2BkGRq2NAByYzea3sC9ZDvqTOIYHVLIPJud1kxTdTnYfdq%2FTy5VJd5XfkYhR9Sn00D3tollDnoBiRBpSp2PX5DJ4jh9gHitu4h%2F4PXi39wXOLx4KHq7%2BRuG%2BAymNmi8PNtLbehsOzb3sxWRYB&X-Amz-Signature=d184a5e770f9ac2ccb8961f06074d5eea3ad6726fa69e9d537dd11ecbba4e9fb&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Algorithmic Libraries
#### 1. **Scikit-learn**
- **Description:** Contains tools for statistical modeling, including regression, classification, clustering, etc.
- **Built on:** NumPy, SciPy, and Matplotlib.
#### 2. **Statsmodels**
- **Description:** A module for exploring data, estimating statistical models, and performing statistical tests.

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c62885f5-417d-4179-834f-d68f8f2bdf39/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RQXF2W3G%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T141340Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF0aCXVzLXdlc3QtMiJHMEUCIQCt%2Bnw6PK29JQkUFwAheLi8j227g5b5NPt8aWYF9jgXfAIgQ4P8qXa1yhdsLp1smbb55t3c5axtNx8OM8XiQr0%2FQ%2BQq%2FwMIdhAAGgw2Mzc0MjMxODM4MDUiDH%2BABvcwlHKVzX4gdCrcAxZlxwxexlsQfgV8vEOpt%2B56W7OUsRv7azq5Q0BTlielx7dd0oDX%2BYWVpVVKZaFWAmyie3lN5oVAGe1mCXF4xrMD%2Bq39H1GT4WjS%2Bw%2BSgBtpj5c70LAP%2FE1bMaes%2FPKaCij7H3LfMN67b%2Bsdjp2sMBuQy%2BUwj9MuR2lclJZ3m0KG6OHaTQkzqkV%2FBwA%2BVJvx6x2fdQNfV0lWWVqNJ0THp2P1CbwbaXzQm7ErksFWVkWq2uGogmRqfb5myUR49ij9UriW37ltN3gf6%2FaenIMKNBAbZs4RyCnT5QMBc914ElCrPgegKWnZGZTzlp60C8y76dBArYWfs4aBkoWpRJJLEwpw1GaZbgzg%2F9ePBQPLrQIlEu12MYXOajd%2FMFvAnTYS74IkWjnBPoz2s%2F5w74vz2uBzd%2F%2BbKSA9E0qMz3PgCEqDFVZK5JfuS7Px08klUGgaPu7ZHyI%2B2ImE%2FrtPfLGD2SqZ4TbUFZS13oBQCrUFPRD4SFGhmFLe9vRndViW8Hurgjqtqv8xZTJU4dhVZQsBoF%2Fjdn3IntXchTxeOze59lAEIW2drumnGS0sfBsqxN1gu96NoftH45u2EOgM7GAhpXWqJAnIGPTrxRkwe4v74dV%2BhpZbPruFmSa57u1DMLOLmL0GOqUBh1dGjChaCRO9bwKLkSXrfnjGdyfhc8AaoDJTehiNe8hvJxAdsaPmynanlsDw%2FnUBtsHlAQt7IOvF%2BkGRq2NAByYzea3sC9ZDvqTOIYHVLIPJud1kxTdTnYfdq%2FTy5VJd5XfkYhR9Sn00D3tollDnoBiRBpSp2PX5DJ4jh9gHitu4h%2F4PXi39wXOLx4KHq7%2BRuG%2BAymNmi8PNtLbehsOzb3sxWRYB&X-Amz-Signature=216c30b22108f1af76a1d72be0af0c8c560629e4e9c797b86b8cc9e0f1eb6312&X-Amz-SignedHeaders=host&x-id=GetObject)
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
