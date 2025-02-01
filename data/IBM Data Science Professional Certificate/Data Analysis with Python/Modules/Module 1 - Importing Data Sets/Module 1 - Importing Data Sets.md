

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

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/997ac361-58a8-4f04-bb0f-79fea4baa761/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UIVQBL4I%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T011218Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCID3gi3O2DNwHdlVUjmwSUlZN%2BAiZ42ggMmTncZnE7nrUAiAxygAbdH5BmW8eBaJfYmiQmMCrzMe7d7jDSWNeFEMwoyqIBAjJ%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMUX2uGEOjiFlXs%2B5mKtwDoWc%2BvRA01HQ%2BIYhL7%2Bda31RNpgS8MtqJ1WxKA%2FmF136fqjDLYHePfRH39m4AId2kZSuR2n4FMJDDLMLzZATt4LukOXr4x%2FMdNZVzF%2FSRY78leiygRddjtPfD5ayxv30GsmQFkSYqNMlv1Ccu5CATzZgVqhKXgKnBiR9PMw%2Fu%2BJBv%2BcpLYH1ZNyM07LVY2CCCJCaFS6pwQ8gn3I8GtMLh8ffX2fX%2FvNoCJ8HPJWldLK9YX9hRZITf6uE5sqM104B0%2F51%2BfUDRfaHLdiQW4sbaK62Rque%2F9ySdI2yfpw7INnyMT%2BcWINOe6KlgNzldD2%2Bq0l9AI8%2BCZu0bN0c9%2BVBCYkwMxk5Te7Wa6hNGB220WdoDntSyfSx%2B5WfQbndTb45yAXnvAyVnxdEY5790n3QivlCXT8zNtVpQ2AnXx7N%2B%2BWx5D%2FF4li3dsl8AOf6%2BZtpnqMduddGmY2PWVaBnNnDSq%2BaQIcv1vAHlG%2BWAk7vSdXjmjtOWICUlg%2FQ%2BuGJqEAAdB2Pltz8npnzrcXfASOr3sEawUbuO4xleJ194KaDFL78av8AQ129TAzzL%2FsfhsnWIbOq7ZJ1I3i80B4nsebl%2FP9qauJ9zb2f1ERfzFhlxQKe2VDRn2kU3OYkaF78w0cz1vAY6pgGtlGO9LuyQm5nLAstOC9XLg1xPKqsqnoA6YCkRdZXbSTHcee1U%2F5keGQoSeCEBB01Icu4mnY5H3p4VCIv7jh8puyl4XT1ptJoNuZ%2BkFFrTFIWoCnGnhgebQezf3LKnBmFD2%2FkV0FB9zqpxcYTKt6u5HPiogkdnDUuRBNphwHV16tLMG6E5e%2BVWOukxQ511I3vaFJvDMOgVZ3ZcMvChhn0LIeiLRgiV&X-Amz-Signature=ffc7fe835eb98f5787746ea767e78600b89750611fe3096205bf05256d9af4c2&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Data Visualization Libraries
#### 1. **Matplotlib**
- **Description:** The most well-known library for data visualization.
- **Features:** Great for making highly customizable graphs and plots.
#### 2. **Seaborn**
- **Description:** A high-level visualization library based on Matplotlib.
- **Features:** Easy to generate various plots like heat maps, time series, and violin plots.

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/733d1e42-5a53-4fd8-90c1-3d85254369a6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SK5GJXNK%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T011216Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQD3j%2Fryk0e35G8V2BvCMTv5uO2P3tVhJgJrBW5t60enogIhAMRzB4X1g8oJBW8Q7ilLvT5RPMK7wysD7dh2EoiqUFqqKogECMn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igzk9XjJW%2Fu%2Blqno6wcq3ANLOg3HiLt0epoiTWsp%2BJadn2zDEZ2wMD9U3yVM9rBr6l603%2B5j6QX28m7FPPElbSh4aEYr9FSqxg%2FjJ51f%2FT%2BLXmSnr7C3qf3VFRr1WDdanHHdjsgTXmTRIQXqoMoLheSw30BtdB8HN%2Fd20CXx%2FxThdXrC8E4SeI%2BNPgoxFtzvsf9Ws1l1xf3I3edRzlL6v8xcigUQbAHKxDJbkz%2BARwGWMCK7UcZ5pkx%2FgtQ43sXRrHuMlYI2hHPDfmClcf3GhZd2n8EGgFqu7ceJlVDkUVqPkg1Dra42ThgyzVye88%2BYmKly2LZ2FOmheI7ZzsXh7X7sly%2BPKOd6hDb%2BE3bZJ%2FNCSeccCINHZqpJs4DIq4KoFBa5racWJ%2FNKj3AWh2u7dUqcHHn%2FQXYecKMD0Rp6Rc08DYWCFdRKH0mUexcqwx%2F0ChiqlBRz816fWlYWXLOpJYFuy%2F8nkPC0gAwMVKDEfPHJoCPRHW5ZK8CBXg2w%2FPBlRPi20vOWO5oVtgZekruz81OoLJZa%2FZ3kqPmZVKWn6M2DuMzp0dkqJoi6Kk5WCTwPKaQf4yDlGWw14U3pwEhxdZAsM%2Fw1D3iQZWO2VRT0kJBShjZIS4n9pqvx3QAQz2odO2hPlIVOdt8b7lBEXTDmzPW8BjqkARnSQPCptKvB5qMZ5T9g0Sq8ktr8hgf%2BU4cNzyxY7iD42WQp6Gv0%2BvvovzJKwqyqFOUNX9NsSVAYTW%2BIgEX57FRya1kcAGf1CaOi4QzBxwy35HnqW1Xu6rHmLekUjhOmI5as5cqZVvbJh8NVgx%2Fvs7lLOhFtqCAnewoygZFH3eGaqvHEWo9yLMOGnTfyMS4ohvTNa0wFnkOQJxaifC%2BRRjdCLtRT&X-Amz-Signature=18aa257b2ad3e73c6f454f027565e454f336d83a7fdc9d7913711c2101b32488&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Algorithmic Libraries
#### 1. **Scikit-learn**
- **Description:** Contains tools for statistical modeling, including regression, classification, clustering, etc.
- **Built on:** NumPy, SciPy, and Matplotlib.
#### 2. **Statsmodels**
- **Description:** A module for exploring data, estimating statistical models, and performing statistical tests.

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c62885f5-417d-4179-834f-d68f8f2bdf39/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SK5GJXNK%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T011216Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMD%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQD3j%2Fryk0e35G8V2BvCMTv5uO2P3tVhJgJrBW5t60enogIhAMRzB4X1g8oJBW8Q7ilLvT5RPMK7wysD7dh2EoiqUFqqKogECMn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igzk9XjJW%2Fu%2Blqno6wcq3ANLOg3HiLt0epoiTWsp%2BJadn2zDEZ2wMD9U3yVM9rBr6l603%2B5j6QX28m7FPPElbSh4aEYr9FSqxg%2FjJ51f%2FT%2BLXmSnr7C3qf3VFRr1WDdanHHdjsgTXmTRIQXqoMoLheSw30BtdB8HN%2Fd20CXx%2FxThdXrC8E4SeI%2BNPgoxFtzvsf9Ws1l1xf3I3edRzlL6v8xcigUQbAHKxDJbkz%2BARwGWMCK7UcZ5pkx%2FgtQ43sXRrHuMlYI2hHPDfmClcf3GhZd2n8EGgFqu7ceJlVDkUVqPkg1Dra42ThgyzVye88%2BYmKly2LZ2FOmheI7ZzsXh7X7sly%2BPKOd6hDb%2BE3bZJ%2FNCSeccCINHZqpJs4DIq4KoFBa5racWJ%2FNKj3AWh2u7dUqcHHn%2FQXYecKMD0Rp6Rc08DYWCFdRKH0mUexcqwx%2F0ChiqlBRz816fWlYWXLOpJYFuy%2F8nkPC0gAwMVKDEfPHJoCPRHW5ZK8CBXg2w%2FPBlRPi20vOWO5oVtgZekruz81OoLJZa%2FZ3kqPmZVKWn6M2DuMzp0dkqJoi6Kk5WCTwPKaQf4yDlGWw14U3pwEhxdZAsM%2Fw1D3iQZWO2VRT0kJBShjZIS4n9pqvx3QAQz2odO2hPlIVOdt8b7lBEXTDmzPW8BjqkARnSQPCptKvB5qMZ5T9g0Sq8ktr8hgf%2BU4cNzyxY7iD42WQp6Gv0%2BvvovzJKwqyqFOUNX9NsSVAYTW%2BIgEX57FRya1kcAGf1CaOi4QzBxwy35HnqW1Xu6rHmLekUjhOmI5as5cqZVvbJh8NVgx%2Fvs7lLOhFtqCAnewoygZFH3eGaqvHEWo9yLMOGnTfyMS4ohvTNa0wFnkOQJxaifC%2BRRjdCLtRT&X-Amz-Signature=c899dea66cb4924d7ed355375058803cde4cdc61122d1107726b33d67a40290b&X-Amz-SignedHeaders=host&x-id=GetObject)
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
