

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

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/997ac361-58a8-4f04-bb0f-79fea4baa761/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46675M6IXWC%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T211408Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDEaCXVzLXdlc3QtMiJIMEYCIQD5H5GndYddHE7sL5l9S1yeh4lG9y0Z45hKUWkq%2BA88ogIhANoPRFLwA1BYwndapQoPyOH%2FB4VMuhshDnfoVdS%2FeMOMKv8DCEoQABoMNjM3NDIzMTgzODA1IgwQHVrz%2FOZAk4Sy%2BPwq3ANB7sxwYkFy%2BgGOHLbmPwG4ZMDD0gxTIGYh0iKyVNIqiY%2FUMgZcvNRdWK4QUWG%2FmfV%2B8SUA3OSEfyMQTHh%2FTkiYfYsBuD0x3YvRJwYPw3leMH5qKBQBKwWd15LyJJft91bamveOBUhZdRqZheYCzS0Xq7VJ2WcaEI639R1JEPb700g4bP6FCv6IE%2FRvo%2BdemCcpn%2FgdrBBBORWaOevyfFvA2Z3kThOIWFo%2FJiSVsUuGiRqx59jXLB2OsvmuMHXcwro5fJwI%2BEwT%2BrmQ25KVOnktUtX20BA1qAKamFODwdEp%2BnClVXNUdNh6n66dtUbwwcFk8Rh%2FKQveN9AqNd%2BIa566bu5hzgQ%2FwZfWTGGcSW7gDlNDKaX0MaE1QtOKVSIiaQO9NN1COdamTJnrBF8%2FuWA2e1sAApFoO5Gvsw8bAT2mla%2BThVCumJlWIurZw9r9ts9hRj6dL4hzrwSYrubFSqpSmb%2BaHabmywxBhvbFdcWGtZUN%2FAACPDcPFQAfSGA50aJQ%2FoHHx5dXmVuIJ5RAUyiKNvU6Y%2B5f%2FQgrmdVYv4nUEU68M9dGhZMJLiMVroLm4kYuX6T7G4yaRXKOU25TubxmtgdfJK20%2BaqmqvKw4QWfMuTqPv9hQIgyDz%2BtBTCmuo69BjqkAVzaboTmwqGceBqv5BUhpEJckiKnkrbxM9kl4r9YgSHrXRUkOVmycuJ1ehoF33cJ7mayUlNXy2G4mZM5jA%2BAJ1kt9l3ZYlZCY%2FNPw0Nkx1zMjZcRGkcLY1exCWvNYhTtlGvPnj47U6BTnGfslnh74aG7IUdOajZ2L5bFqadsYRzshaCc4qVItGOSbLLtEiVIIshF%2F6OwZLC1MTOCXkAyJMZfJq5%2B&X-Amz-Signature=4fe75a1378f1d8c454d7f2e189d31f622c0b129d601d9d34d43878a9c194aa30&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Data Visualization Libraries
#### 1. **Matplotlib**
- **Description:** The most well-known library for data visualization.
- **Features:** Great for making highly customizable graphs and plots.
#### 2. **Seaborn**
- **Description:** A high-level visualization library based on Matplotlib.
- **Features:** Easy to generate various plots like heat maps, time series, and violin plots.

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/733d1e42-5a53-4fd8-90c1-3d85254369a6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R6HYU2SS%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T211407Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDIaCXVzLXdlc3QtMiJHMEUCIQCqTOBDkXYAr4L9p5mxv4MJ5FYfj%2B8GVtTFeA%2BBhDH8wQIgcicdeuB2lec0MGqmRHmF0j6GaifxuBVRFczLxrYVWqAq%2FwMIShAAGgw2Mzc0MjMxODM4MDUiDEU8U6IHWrwslY9wVyrcAwdAkRdxB6fLUNlyTT3K8wA%2FC3Nky7zRVcjDoSEz7WJWDnw%2F5xjVYRIfT9LDCa7VvQFeyZCqih88bHuCvnZu1fk8aKmWAOdv%2BngUsJ47e1RjxcStba79GfgNE6n8Njn0mgUtRW73mOZ%2F8bBFcXfIIApE6Df34EzItw%2F%2F4gmuRVVOFj9PLkWzl1S4fAtWvxsxkuH8Asfx2risT5jD2LRtd%2FQ%2FUZDAFcSYNlYdO%2BIDIu0P3pfMLMZpFw0MK8%2FsmqcEYCTQAYUPrCtGZxOyM4RdW%2FpMujC%2FSvLJD0DNZ4Dx%2FmYTWIS0cES0LgIc92OSAk0%2FUv5HyayPZKVXO1VYayrIQXYwTHrMm1fXPHV%2FaO08g4klHwwFQt8Xm4N5%2BsNBfr2%2FCPT7ccGw6TgOJbmJyRVX886YumdTIN15HZ3mHQthgm0lTnru7xbhFl7PD5O5ljwEUhaWweRyn%2BRQXK5Sa5WhyfWvAQE0cYyIlGaflfJcTpy%2ForcvgV7HvbfaPtB8XdrJ%2BAduZsW2tnn5EGIP3KVVH%2F0p34iJmSK0B0JhsAdYMmKZCz2OlChE5%2BZssLdkX3BtvKmrery5PwcmE2hHZy3rHJerLspbEbLUQZJKKZf1UxFcgP8fV7emVJgbud9uMOS6jr0GOqUByJFND1HkIxnKHY5Na5U9w%2Bzfy5Sm7RAntbxuNvoOl2fvbJe9L81Pdeh1Z82b8FtGwROps22VTgESPtP1gG6bdqMuOqGn4P8gVEfBeXySpuHdwcvLmgkoPB1oQDisEkOoy%2FFgqCYtFjQh7S6OkUr3aNa53IX2dlyf9uv20Cd0xZVsKfHviNrAmH%2BvHKBKCRT3dNqL4A4TPJLq2KTZYd4XVxlRA1eu&X-Amz-Signature=8a63f9cc3c5471af966f5c4d723e25701af11dd67db0296bfae2d3b537564dd4&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Algorithmic Libraries
#### 1. **Scikit-learn**
- **Description:** Contains tools for statistical modeling, including regression, classification, clustering, etc.
- **Built on:** NumPy, SciPy, and Matplotlib.
#### 2. **Statsmodels**
- **Description:** A module for exploring data, estimating statistical models, and performing statistical tests.

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c62885f5-417d-4179-834f-d68f8f2bdf39/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R6HYU2SS%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T211407Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDIaCXVzLXdlc3QtMiJHMEUCIQCqTOBDkXYAr4L9p5mxv4MJ5FYfj%2B8GVtTFeA%2BBhDH8wQIgcicdeuB2lec0MGqmRHmF0j6GaifxuBVRFczLxrYVWqAq%2FwMIShAAGgw2Mzc0MjMxODM4MDUiDEU8U6IHWrwslY9wVyrcAwdAkRdxB6fLUNlyTT3K8wA%2FC3Nky7zRVcjDoSEz7WJWDnw%2F5xjVYRIfT9LDCa7VvQFeyZCqih88bHuCvnZu1fk8aKmWAOdv%2BngUsJ47e1RjxcStba79GfgNE6n8Njn0mgUtRW73mOZ%2F8bBFcXfIIApE6Df34EzItw%2F%2F4gmuRVVOFj9PLkWzl1S4fAtWvxsxkuH8Asfx2risT5jD2LRtd%2FQ%2FUZDAFcSYNlYdO%2BIDIu0P3pfMLMZpFw0MK8%2FsmqcEYCTQAYUPrCtGZxOyM4RdW%2FpMujC%2FSvLJD0DNZ4Dx%2FmYTWIS0cES0LgIc92OSAk0%2FUv5HyayPZKVXO1VYayrIQXYwTHrMm1fXPHV%2FaO08g4klHwwFQt8Xm4N5%2BsNBfr2%2FCPT7ccGw6TgOJbmJyRVX886YumdTIN15HZ3mHQthgm0lTnru7xbhFl7PD5O5ljwEUhaWweRyn%2BRQXK5Sa5WhyfWvAQE0cYyIlGaflfJcTpy%2ForcvgV7HvbfaPtB8XdrJ%2BAduZsW2tnn5EGIP3KVVH%2F0p34iJmSK0B0JhsAdYMmKZCz2OlChE5%2BZssLdkX3BtvKmrery5PwcmE2hHZy3rHJerLspbEbLUQZJKKZf1UxFcgP8fV7emVJgbud9uMOS6jr0GOqUByJFND1HkIxnKHY5Na5U9w%2Bzfy5Sm7RAntbxuNvoOl2fvbJe9L81Pdeh1Z82b8FtGwROps22VTgESPtP1gG6bdqMuOqGn4P8gVEfBeXySpuHdwcvLmgkoPB1oQDisEkOoy%2FFgqCYtFjQh7S6OkUr3aNa53IX2dlyf9uv20Cd0xZVsKfHviNrAmH%2BvHKBKCRT3dNqL4A4TPJLq2KTZYd4XVxlRA1eu&X-Amz-Signature=c4e3c54b6a54417913bad09752780cc584467c6fc607ac4d489a8dafe7a5a9a5&X-Amz-SignedHeaders=host&x-id=GetObject)
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
