

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

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/997ac361-58a8-4f04-bb0f-79fea4baa761/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SIJ4DMVO%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T062044Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIBlZO9UTYwF4DIP5Shvrm9oJMQes%2FbpbO8%2BfRsolD444AiEAm4VIgccp6wesPeK22SvPy%2BEM%2Bb%2FL6yinVrCn6CVu0VoqiAQI%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDDFLf5i9YzRgioQ7yrcA1nlbYq19Bv8EY2oV3QyN23sLe67eG%2Baeerye7KXtLyFDiwWHQnYW9geqYxjGwpu6LDx4SRg99GxAA%2BGTpLP8kFiBllzsrPL90nNulQxRO8KvFkN%2BatzsWp7HTALwYfv2F1Ux%2BN7sQXzxSydR4KLSKE65hsmy3aDj06CQpehN0NeHI6%2FiVzZiWKvaG2i62CJrLknca9PN%2FQeEp3FuQRIWISJ8PzKmyG6xkLKBuzXuRSgPm%2FdbT0otRtY%2FkNA63jFdHS8QG3dktRnApe9W2SQXRmScri8psnjtX26Es8ShkPY37iKRqJeJ0Emnnmxio3sndKjTpKF%2B017imcra6zSd%2BbRVYap55yfamxCwccPau5eEkioLkUnqaOPGFXjUa0iy4FeFSuvyuRPmtpxJw4oBly%2FvPMxk8FWoTYCm%2BsAK0k8HC1dUAaIpEi%2FqeyfoHu%2BwhByMPbpD8lgRFcIeY9zl1yth0EyhIPCGpqq%2B%2B%2B8kWmd5o0Xm%2FDoSKjhmVD1JL47glZeYajda10UvVIGNW7jUhErf463RqOYVwuJzIA30DeXJFGrLgI3H9ipo45%2Fxwe5qfjRSJd0H9gbHJ%2BKDX6vqX2AItmbmWuKipccBsaxOq2EJGriPUEL7D9VLdfvMP25gb0GOqUBbxfxUsjHoI9XsBvQdlPbIMI20qVwovt%2BnXCqDy1WCqhOi%2F9wY0BJQFvRbaFbkfT%2FGF8dHBNSK%2Fei7t2muUonLxnIc3jFo11FPz%2FsSSQKL32yKztNRSTdW3UoXFdrOEsLfIG%2FdkB1tL4MPbwz5xh%2Bf%2BtpFvN%2FNpP1Zhv0lNv6x3uXyc%2FpUSKi%2BMc4cE5yDCLriJOakuOB0rSqHD%2BU0ZD2FF5HuR1D&X-Amz-Signature=cc0021888366cfccafbc1d97355c38ec318424a8f89b14021174b03b09933b30&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Data Visualization Libraries
#### 1. **Matplotlib**
- **Description:** The most well-known library for data visualization.
- **Features:** Great for making highly customizable graphs and plots.
#### 2. **Seaborn**
- **Description:** A high-level visualization library based on Matplotlib.
- **Features:** Easy to generate various plots like heat maps, time series, and violin plots.

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/733d1e42-5a53-4fd8-90c1-3d85254369a6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466USN5KF2N%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T062043Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAkyq3F%2BH7yvVkuXEXJMqMyP2LPMdmgSFxXb8PxraWLDAiEA82GPqL9ZYI8wsNYKsmGsyO5ztuQoGECcFrBqXa%2BcSLYqiAQI%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDG2fKXE2tKHUOOi7NSrcA%2FbUd9mB3fppVBon8%2BeqdOlUDWnBeVI9Jwrl%2BkOPbrEhXNUM7%2BlaMDdbACLwWpt8D1DSTIr7nIfvy9yXBCSyj9zVoA%2FwE7Upy0MWt9%2F4tGz3IxT2Hci5ZWNCvzbSK%2FFbF7PdUp4cdNbf2lEFQg7r38npUYd9cj3giXhJJOYqvQqxxNiFae2U1ehP1JNvoRLPMga7J0EP40x2o8xxCPGKZpifgMw89G%2FAJKeMtNtC8%2F8A4Aha%2F%2B0pAh8NpdfjJltWJismUjTMu6zjYPC1eql9TwN4XR8cEhhyJVzmGHnFSiCIQlqcpe%2B24gr3F9gUoAxgmD%2F5pBxmjC%2BFRA%2FXJVaxW3fkBLdN5IZUms7CHVqLvFLo2ehzJxKpU4G5m%2BOv1%2Bo3kEeKXxYDQa6ENo8E4%2BFrQEFEVttqxE3dmXYqOvOOZGcu6VjIo6HLgBzbvKIjQjsWqNkjkrxkkH9GZYWjByk5sfwhrAVI7c2%2BIL4H9fPhaQ4nQCNOpdJgV7h2juzTjXOf%2BqARz%2Fxojl6%2Fp%2FST1uoFZcAWz655Ba1BzIUKWzwflHSC%2FuIxsPlMc1UuvQ4sy3gTTz63dAf%2BUpUzQYaNpcinIMZF3%2FLvsjGP3avZeTJkMCodJpV77sH8IbhgY7D9MPm5gb0GOqUBuOjrwoyhsCDkrZQyksjJ%2BlbVD13MI0msJu1pB2t5LU%2FvlFItr36rh7ylTGBXPMCmiYjpUso2bYFgHTkZCBH%2BjT9j6mNSFjEPAjpPOEwjyGueuWUrte2RBFOlWClqJPFJlBNNYWZmKz8C0hww09sltA2BPUQ5noFwsaiMExcUa7npIGl6IbhwVTuoLqrcM5PMtGq9EYqKp%2BSZ%2B4PeR3jwHa3Z0XzR&X-Amz-Signature=0633b9d8a584b7c5cec22382604d224d7c70f27a03d2c6984c7c82bbc4285042&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Algorithmic Libraries
#### 1. **Scikit-learn**
- **Description:** Contains tools for statistical modeling, including regression, classification, clustering, etc.
- **Built on:** NumPy, SciPy, and Matplotlib.
#### 2. **Statsmodels**
- **Description:** A module for exploring data, estimating statistical models, and performing statistical tests.

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c62885f5-417d-4179-834f-d68f8f2bdf39/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466USN5KF2N%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T062043Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAkyq3F%2BH7yvVkuXEXJMqMyP2LPMdmgSFxXb8PxraWLDAiEA82GPqL9ZYI8wsNYKsmGsyO5ztuQoGECcFrBqXa%2BcSLYqiAQI%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDG2fKXE2tKHUOOi7NSrcA%2FbUd9mB3fppVBon8%2BeqdOlUDWnBeVI9Jwrl%2BkOPbrEhXNUM7%2BlaMDdbACLwWpt8D1DSTIr7nIfvy9yXBCSyj9zVoA%2FwE7Upy0MWt9%2F4tGz3IxT2Hci5ZWNCvzbSK%2FFbF7PdUp4cdNbf2lEFQg7r38npUYd9cj3giXhJJOYqvQqxxNiFae2U1ehP1JNvoRLPMga7J0EP40x2o8xxCPGKZpifgMw89G%2FAJKeMtNtC8%2F8A4Aha%2F%2B0pAh8NpdfjJltWJismUjTMu6zjYPC1eql9TwN4XR8cEhhyJVzmGHnFSiCIQlqcpe%2B24gr3F9gUoAxgmD%2F5pBxmjC%2BFRA%2FXJVaxW3fkBLdN5IZUms7CHVqLvFLo2ehzJxKpU4G5m%2BOv1%2Bo3kEeKXxYDQa6ENo8E4%2BFrQEFEVttqxE3dmXYqOvOOZGcu6VjIo6HLgBzbvKIjQjsWqNkjkrxkkH9GZYWjByk5sfwhrAVI7c2%2BIL4H9fPhaQ4nQCNOpdJgV7h2juzTjXOf%2BqARz%2Fxojl6%2Fp%2FST1uoFZcAWz655Ba1BzIUKWzwflHSC%2FuIxsPlMc1UuvQ4sy3gTTz63dAf%2BUpUzQYaNpcinIMZF3%2FLvsjGP3avZeTJkMCodJpV77sH8IbhgY7D9MPm5gb0GOqUBuOjrwoyhsCDkrZQyksjJ%2BlbVD13MI0msJu1pB2t5LU%2FvlFItr36rh7ylTGBXPMCmiYjpUso2bYFgHTkZCBH%2BjT9j6mNSFjEPAjpPOEwjyGueuWUrte2RBFOlWClqJPFJlBNNYWZmKz8C0hww09sltA2BPUQ5noFwsaiMExcUa7npIGl6IbhwVTuoLqrcM5PMtGq9EYqKp%2BSZ%2B4PeR3jwHa3Z0XzR&X-Amz-Signature=267a9db0115e023358a9fccfae45dfe147c77c0aaec195179be85816c1ccefff&X-Amz-SignedHeaders=host&x-id=GetObject)
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
