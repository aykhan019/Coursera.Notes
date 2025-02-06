

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

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/997ac361-58a8-4f04-bb0f-79fea4baa761/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666GMW2VKC%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T201555Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEsaCXVzLXdlc3QtMiJFMEMCHw03y%2BUAlgzV6uWGRGcds4P6HHJ7i%2BKpm1PSST%2BWfHoCIGUzlxWDWlTRgXzgjLocsXyYZE8iPjb%2FS90g6X7PMN2AKv8DCGMQABoMNjM3NDIzMTgzODA1IgxUwQ3GZspHHOjcsqsq3ANsRdlQ6ZGp6g2IERsDgQuniWDF28sEWM2y5TJ%2FKr3H2v2Lg3gBRDtEIT%2FDCzmuvodqiueLlnVRFsxuxrEtzup7ba3QseqXuBeKUVEa5TMyMdgDVgowVPNDRkb8JIGw76nsolSTniZjEz4%2F23sK%2FD1fdTTLjRFYgbxCSy34hZMpkVG0h8oB0T%2B90dr%2FY%2BrnazVk9%2BsI96tC2WC5jI1%2FthsN4cGNJ%2FxGuM13n19PVJGlBf4%2Ft%2FQLhq%2FWQYrHSq%2BwlCfqfAy5q%2F%2BZmnSbZ3Ph5%2FWftdzBOd%2FDFpxM57wRlyhoob7nxKaedruGXR2ie8bEAop3PwXSpku8lNvM2KguEEpGkH5EGgA2rj%2FOITkIU5IT90Rwyx3F7%2BuXO3WUrQomHgqopUMTpkTj7aVRFeurQjaN1ip29gDta%2BYQtREXtaQbSSPhwlT1EQdcQBVWkxGjvzu7AQlf1ODtd5PgagOARF9Oww%2FYYkd1GF2OOHxZMM6hNk4Fris3p1GOZrVva0RS%2FJztYP8yHMQDP%2BL35MIOCHvJqKCIeDt4DGvU5Q%2FfrTJY1Qy4nWnkQsjVm1siRM81wpyyLU1bUOIV%2BTGsuGcsP6oWjSAeevfMrHMEfIMkkgczGF%2BvjaoDfolFdAdHRzDD%2B5O9BjqnASfRJoABQQQbu7PO0LGusLdPQlYhSxCGwrGwvQVXdGltZfZDQtge7KpLPV%2BnCHqxKOfziXPp5ZSeMrGiRHCeGHVpMeaXUwmmeE4F0JCbHHzvhKIOYicLr5FvBwse%2BgnwXbxQe5xoL%2Fb%2BxF%2Fi952FfF1dkTfJZP6rZwEo96%2FZCUjW8sLB6lXUAwvxI0Td0Te6pSLOC62ctrCJ8XdaZBLAX9hXt%2F%2F1A2F0&X-Amz-Signature=b6ea7e122769b70d4f258dcf9a4dd35eab7c9914a673b13f1c708b833cec42c2&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Data Visualization Libraries
#### 1. **Matplotlib**
- **Description:** The most well-known library for data visualization.
- **Features:** Great for making highly customizable graphs and plots.
#### 2. **Seaborn**
- **Description:** A high-level visualization library based on Matplotlib.
- **Features:** Easy to generate various plots like heat maps, time series, and violin plots.

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/733d1e42-5a53-4fd8-90c1-3d85254369a6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665S45FF23%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T201554Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEsaCXVzLXdlc3QtMiJGMEQCIBe%2BmWjuJb0k49JinRSE0gBiahJYV4WIMlCuxGbQse%2FYAiBQm17YBDGBKt3U9h54jnosHsIeJEAVKuoW3RO%2FM4jKcSr%2FAwhjEAAaDDYzNzQyMzE4MzgwNSIMso49i1inhxZf7DBAKtwDEitR7K2udJwsDXuVV9fum9bHTgu9qTeC3BAyY3pomUqli8W3iTeojxpB8e4%2FwFnuoUCVpfk9J%2BkNlUmFfCTR6vOOtL9N8C2fmqP1OqNfBm7Bw0HOC%2BOFuFzB1WCF4LLP25%2FNn%2Fhn9i6ufC3pQ39zHWWRwo3CiPRSz1ZMXiNBZYx6DixS6CRSsul6aK89KYEEpERqNK2U5JKDO%2FlMifj8UczUV3rS7lIUIazxrXTySEwQ6LyIYmfNMnK%2FjtIVzN5pgmPkbr7paUs4ubYkrRNPWpmM8d70wI4UibJjMafamSPW0TJ33pa%2FRwtozcEkfhOYDUR0PR%2Bw0FF20AZbMr6QWHHsjpt74U8PPTMdfzLkpsZPlf0LxjTeK0Y3au9NT%2B0WAP%2B%2FCVypRR7EyP28z3qrF15gRcBeIO1K5kppkCDoSfaa4i6ma%2F8J%2B9pBRWrkC6QFs%2BwE5e6oywv3jhJ4HLhbNmkM0R3rY6OagaaLmwySQgXELmKTkC8vdvilHyvVk8QGE7Es3c%2B5Zo%2BFZxQLwclVlcEfMaTiALaVID5cHZGdKc%2F%2F59KQVsxkaUl%2FzBILvcXi6zaqnXhv5LBiR7j%2F8rXXkG5hQhQPHuozz%2B1FEvt1rpIZ9amQIleSTdDSLY4w2%2FuTvQY6pgG3yniOFZqhXQF56uDi35FMRTkrt52%2B%2F1dNvvBtA0bdX7H92oFJ4gOU7xsHJoWjyY8mCYGtvTdgWtPXD%2FfJx1Gz2s235%2FWimCIW%2Fhu4SHqB%2F6jHj2T6x%2BDknK8GWqxC3WYg3ivCxVVrPQlQyfRFR2GrFPSIrn0J2ZALyzOtDYAX3EJ1J7onx78O52X8U6WrOHZwfYnx1xMnsPQeDKMO4onyrwTMU%2B3X&X-Amz-Signature=3aacc058a44fa8773c3409f815b6051ae0a6349e4c3291832df58c0c635855b2&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Algorithmic Libraries
#### 1. **Scikit-learn**
- **Description:** Contains tools for statistical modeling, including regression, classification, clustering, etc.
- **Built on:** NumPy, SciPy, and Matplotlib.
#### 2. **Statsmodels**
- **Description:** A module for exploring data, estimating statistical models, and performing statistical tests.

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c62885f5-417d-4179-834f-d68f8f2bdf39/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665S45FF23%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T201554Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEsaCXVzLXdlc3QtMiJGMEQCIBe%2BmWjuJb0k49JinRSE0gBiahJYV4WIMlCuxGbQse%2FYAiBQm17YBDGBKt3U9h54jnosHsIeJEAVKuoW3RO%2FM4jKcSr%2FAwhjEAAaDDYzNzQyMzE4MzgwNSIMso49i1inhxZf7DBAKtwDEitR7K2udJwsDXuVV9fum9bHTgu9qTeC3BAyY3pomUqli8W3iTeojxpB8e4%2FwFnuoUCVpfk9J%2BkNlUmFfCTR6vOOtL9N8C2fmqP1OqNfBm7Bw0HOC%2BOFuFzB1WCF4LLP25%2FNn%2Fhn9i6ufC3pQ39zHWWRwo3CiPRSz1ZMXiNBZYx6DixS6CRSsul6aK89KYEEpERqNK2U5JKDO%2FlMifj8UczUV3rS7lIUIazxrXTySEwQ6LyIYmfNMnK%2FjtIVzN5pgmPkbr7paUs4ubYkrRNPWpmM8d70wI4UibJjMafamSPW0TJ33pa%2FRwtozcEkfhOYDUR0PR%2Bw0FF20AZbMr6QWHHsjpt74U8PPTMdfzLkpsZPlf0LxjTeK0Y3au9NT%2B0WAP%2B%2FCVypRR7EyP28z3qrF15gRcBeIO1K5kppkCDoSfaa4i6ma%2F8J%2B9pBRWrkC6QFs%2BwE5e6oywv3jhJ4HLhbNmkM0R3rY6OagaaLmwySQgXELmKTkC8vdvilHyvVk8QGE7Es3c%2B5Zo%2BFZxQLwclVlcEfMaTiALaVID5cHZGdKc%2F%2F59KQVsxkaUl%2FzBILvcXi6zaqnXhv5LBiR7j%2F8rXXkG5hQhQPHuozz%2B1FEvt1rpIZ9amQIleSTdDSLY4w2%2FuTvQY6pgG3yniOFZqhXQF56uDi35FMRTkrt52%2B%2F1dNvvBtA0bdX7H92oFJ4gOU7xsHJoWjyY8mCYGtvTdgWtPXD%2FfJx1Gz2s235%2FWimCIW%2Fhu4SHqB%2F6jHj2T6x%2BDknK8GWqxC3WYg3ivCxVVrPQlQyfRFR2GrFPSIrn0J2ZALyzOtDYAX3EJ1J7onx78O52X8U6WrOHZwfYnx1xMnsPQeDKMO4onyrwTMU%2B3X&X-Amz-Signature=353de7ff826d968a1cda278067c72969b5966ddee5d13338b5f505fe3d70b480&X-Amz-SignedHeaders=host&x-id=GetObject)
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
