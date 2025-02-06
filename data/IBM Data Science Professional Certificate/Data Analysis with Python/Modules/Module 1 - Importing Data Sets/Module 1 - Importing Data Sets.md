

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

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/997ac361-58a8-4f04-bb0f-79fea4baa761/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R6AIVVV2%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T221413Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEE0aCXVzLXdlc3QtMiJHMEUCIAzM1Nv4UNlNSAC%2BUWa1F%2F6ZLgJ9VxBPgX7MJ0LUZu2EAiEAgb0P6Q%2FR4q9%2BpEEH1jZPHsQ7h0RDLjcUM6TsNYH0FJYq%2FwMIZhAAGgw2Mzc0MjMxODM4MDUiDCWdtjI2D3W%2F6LoUaircA%2FP6X%2FSxupeLTApB4ckbNtESlWQ3zWRiHUq%2FLDCst5GW2D6qKAVZXQQy%2BtRw6XQUJEtjobvNOJPokfs91qzdLOxPqLglbo%2BhwTFBWPWLFHQ%2BvOto5O4md%2FFyckJSx5Gq04roho9SBcGpkNYtQUzs4Y4kf2%2Fh9WRqE0XUioELi3n3z7pUAzux5Kze7QnFRqpgpRaJIqAvS28JfvI%2FyMl0emPqMn6ciIzdVW56tSFUfviyyaorJsKiI%2FSkj4ZiedCQVq%2BBktG5x0ZsGZKLDukNq6ThKF1kIZMLSuYmaeNkzJyv5vNRU80Jr35wDkYqz1UiSc3fBb5Q0lkyDJYq1SXRZ0M9wF8LrMNvBGumqMfoX4gCZKz8oA9m7xJ1%2FireCobD1zfb8t2pvMfCiHi0CyoEmI%2B%2BC0eeAb4h5RiCmj8xE%2FC0yP6J0NcvbDutPXHiKmhb6BCwHNFE3MCakT%2FkmpRgCrxogTi75ZLzYOANVTtN8N7pknVB4i49pIxPxhRLJNQChccdTooQxpDIVT%2BGksFNnq8v3L9OfQBB9PlpEmhxhkPszdcv5Q3ZJqokeOm8rH%2BLRw0S4olWBKqAzOMWqIXtQi%2FsSnfTTGh%2Fb2G%2Frt%2BEBAOQQH6S9CgslbPj%2B%2BuBMOy3lL0GOqUBXM0Mlr03FL3hfFSaEsemok5%2FCBonSukYzk8QnMCCp%2BTkB29YA%2BPfJDk6i4Smo0VT6e05d40uuNvQAu2y7tunYoh5y%2Fk7bCD6VNLj5%2BO%2BmQqRGhr0C4FE8OiXWDW%2F5e5i6CmFDwiqvNqM%2BoAq1PXH3zGBsb6zAHJMDgnczfyUDiPveLWj1nd%2FepjoMDWVg841lUvhVk4oFmmmv2iQswOtDo%2FwSnNk&X-Amz-Signature=86c1ba3ff76e6428dd1ab09b6734a2648dad922e70c65a7a496943d0ce5faa18&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Data Visualization Libraries
#### 1. **Matplotlib**
- **Description:** The most well-known library for data visualization.
- **Features:** Great for making highly customizable graphs and plots.
#### 2. **Seaborn**
- **Description:** A high-level visualization library based on Matplotlib.
- **Features:** Easy to generate various plots like heat maps, time series, and violin plots.

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/733d1e42-5a53-4fd8-90c1-3d85254369a6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QIKUJQ4X%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T221411Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEE0aCXVzLXdlc3QtMiJHMEUCIHomAONKGYfMaH8K5%2BEmgIbwQB%2B3%2F46DoweGIEyVkX1KAiEA%2Fj61os70YKJp5ti6qLL1TF42HtpZ2EblkeArV7tbyd0q%2FwMIZhAAGgw2Mzc0MjMxODM4MDUiDGc6cRm3%2FMCrUhEsOircAw9pteJYMlJTslde14YBk6x1S3LDFd7fJbFJAkodeeBL7gXuZY1ViKcF0t9XRQIHeZ6uvJinE%2B9ARRXTvFeu%2BKgIMbfQcu4IcdqYmBUAp2KbQu%2BREcaubxZVtlKHkp9QnodCb1ai%2BzhY6dp7AwOTiLkC2vWAsdobNbSlTF9b%2B6RwGAxxMow51KJ2WvJ6KyvKvrdbnGUToWhgbE9oG5WfOUXseCD1nNbgvitOPpFXh1gYWDiuqwa0HaFJQAoO9masSOJjJQroN1iaFaE%2FbsVdlmXjlDAHd3qZkX902dVAxmc6tKoKhRG5J4Rb17NelSae1GWFPFBPlLlPSQ1lTRuxIhc0prAZ2DVd8dqSOfwAUqP%2FgnSvLCr91jLOZHamEe9mwHJaDFIKLNo7tyWm1%2Fyex524Va7AaAHcQClWiaQ9KRhDD1rED0G3tr0XbxozHRtyqVvlPx03oQ8ywq1l0VneQ%2F8ZywZQHJzPVg09BxtzRtNfGdkdVwY8kw5SofK719olZgCpeBdBASkmeaAeTnSGfQ9zKky%2BsH27lEkUWhX8WFkS1qeyQpUAltXv%2FfBTJYlsC9iKoKYvdiNLcjKFqtpg%2F2k2Z0gcaO5sBJt4KnQ4ujE4frDyBViUnV5FnJlRMKO4lL0GOqUBiLH7RFkwKNPJk%2FJ9pLfv198onnanUnMF81k0H36SjxZw%2BtYKnnZ%2FL%2F5zGJ4Hq3Gf84QxDCEVTBsy6pCm6FzRHKpA9w5J7peND5RYRGwbcmK7Jb2DD1ZtdDUg5n4HZjNxB1f8WRgChC4kPF%2BCcdgI8mOb2IMO08BTDRCArktXeuY1%2FxmVzWba9hTM1x9LkJR4pIh6NrRgbUPBeq2LxlDsu4hg00pN&X-Amz-Signature=a995770fefa78f3ec037532c83ead6674500ef3307bbbe71c43cab6b8276084a&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Algorithmic Libraries
#### 1. **Scikit-learn**
- **Description:** Contains tools for statistical modeling, including regression, classification, clustering, etc.
- **Built on:** NumPy, SciPy, and Matplotlib.
#### 2. **Statsmodels**
- **Description:** A module for exploring data, estimating statistical models, and performing statistical tests.

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c62885f5-417d-4179-834f-d68f8f2bdf39/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QIKUJQ4X%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T221411Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEE0aCXVzLXdlc3QtMiJHMEUCIHomAONKGYfMaH8K5%2BEmgIbwQB%2B3%2F46DoweGIEyVkX1KAiEA%2Fj61os70YKJp5ti6qLL1TF42HtpZ2EblkeArV7tbyd0q%2FwMIZhAAGgw2Mzc0MjMxODM4MDUiDGc6cRm3%2FMCrUhEsOircAw9pteJYMlJTslde14YBk6x1S3LDFd7fJbFJAkodeeBL7gXuZY1ViKcF0t9XRQIHeZ6uvJinE%2B9ARRXTvFeu%2BKgIMbfQcu4IcdqYmBUAp2KbQu%2BREcaubxZVtlKHkp9QnodCb1ai%2BzhY6dp7AwOTiLkC2vWAsdobNbSlTF9b%2B6RwGAxxMow51KJ2WvJ6KyvKvrdbnGUToWhgbE9oG5WfOUXseCD1nNbgvitOPpFXh1gYWDiuqwa0HaFJQAoO9masSOJjJQroN1iaFaE%2FbsVdlmXjlDAHd3qZkX902dVAxmc6tKoKhRG5J4Rb17NelSae1GWFPFBPlLlPSQ1lTRuxIhc0prAZ2DVd8dqSOfwAUqP%2FgnSvLCr91jLOZHamEe9mwHJaDFIKLNo7tyWm1%2Fyex524Va7AaAHcQClWiaQ9KRhDD1rED0G3tr0XbxozHRtyqVvlPx03oQ8ywq1l0VneQ%2F8ZywZQHJzPVg09BxtzRtNfGdkdVwY8kw5SofK719olZgCpeBdBASkmeaAeTnSGfQ9zKky%2BsH27lEkUWhX8WFkS1qeyQpUAltXv%2FfBTJYlsC9iKoKYvdiNLcjKFqtpg%2F2k2Z0gcaO5sBJt4KnQ4ujE4frDyBViUnV5FnJlRMKO4lL0GOqUBiLH7RFkwKNPJk%2FJ9pLfv198onnanUnMF81k0H36SjxZw%2BtYKnnZ%2FL%2F5zGJ4Hq3Gf84QxDCEVTBsy6pCm6FzRHKpA9w5J7peND5RYRGwbcmK7Jb2DD1ZtdDUg5n4HZjNxB1f8WRgChC4kPF%2BCcdgI8mOb2IMO08BTDRCArktXeuY1%2FxmVzWba9hTM1x9LkJR4pIh6NrRgbUPBeq2LxlDsu4hg00pN&X-Amz-Signature=547cf9b79ef85b81cfbb5dd171b90aa2c40f34a46d327829984fc52898cf026e&X-Amz-SignedHeaders=host&x-id=GetObject)
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
