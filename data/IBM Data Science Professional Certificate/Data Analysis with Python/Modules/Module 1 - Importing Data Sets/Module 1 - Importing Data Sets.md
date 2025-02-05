

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

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/997ac361-58a8-4f04-bb0f-79fea4baa761/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TRP5VZGZ%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T231408Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDcaCXVzLXdlc3QtMiJIMEYCIQCHgjsakn2UWUO4FBfVyLzORv2bhRoPg6VdslK2A6vidgIhALabZ04e1fKtN9XamKILDbTkD38I3g%2Bt5iTEfzIFkxlvKv8DCFAQABoMNjM3NDIzMTgzODA1IgzviOjVyqHQZnFTkvEq3AM1n0bBt9CHoYNeHljO0P2kH9pohpLQTGPFC1YUMLw7I%2BmBNEcTtCj3StyIYt8uyDOYcMCnLqEEoKWIKlL1W%2B%2B1RqxqSVlSG1ZlWiKCqCf7tGA%2BRNGZdRXiJPFzeX5WLIaex4V3nzpG4mQPeY%2BXs6xQedhA6L10J7JNKdS%2FmVLRMGviYWqVQwQbBgl%2F6jbiB%2FOVlLjsAJ4roV16alIWc2BouUXyIF3JB8QBFuV3SUANkcjefggjKefvY%2Fz2gXtY468z6ZpGy%2BlkIzgYnk%2Fwi6uy3N3akA29BLPlkPvR4wi399wPejni%2B%2Bljg8xGbR1X1FZ4LDz5vLF0EPQhxNojXgAex%2BSYIDh45iWuhOxibcn%2B3R%2Bft%2B%2FiCkdXFnvWxA7ja5McC6gcrd7xIViGPJfeVPSbQRqEmUqSilGaAaiuFsQQbTezMK8w51awHXl5Doc2veNvjOv4Dy%2FRsoIf5ctUCsn6tXFwXMLQMqsk1fI036Ha96AhIH4ZLVZtDswxOlamUu6Inokoxn4x89HhH0y3laFGHLCTqI6%2B1hzU5nMTkye9Tup%2BkHK8rrCScOMLJVUYesqHP8oHfp7MrCr%2F7uFrfIj5l84QUcgQ%2BjvR5A%2FWcGKm6j0l%2F6l%2FzIO2yn9BxzDz2I%2B9BjqkAXfmCW%2BusCDGQLjasrMNYXxQ5QE31RcYKVBMdUt50i6%2BcU3cvAY7eHhijqToTCKsqjsaoUPVSl4VZp7%2BKBChU%2FwhTEUgWAIEcfxbpAyx5AvhR%2F1dpTSSqGGtFFJBCFyC21Ky9JCSKE9LXrlvSgaHsIcwHumWwsC0YA%2FCL0NFLxC1D12ErwsHDPVDis23uD8BTNxYcIolnIB3oM4Dzc%2BCi2%2B8rCRt&X-Amz-Signature=5647034f3f62dfd4d991a51ba7aecd0734495a59f05760144bc69f0e04f0f335&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Data Visualization Libraries
#### 1. **Matplotlib**
- **Description:** The most well-known library for data visualization.
- **Features:** Great for making highly customizable graphs and plots.
#### 2. **Seaborn**
- **Description:** A high-level visualization library based on Matplotlib.
- **Features:** Easy to generate various plots like heat maps, time series, and violin plots.

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/733d1e42-5a53-4fd8-90c1-3d85254369a6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466V7JENUI6%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T231407Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDcaCXVzLXdlc3QtMiJGMEQCIBTDKqYtb2wwdDkStwRNpXFCdT8zRxW4EWunN%2Fi19ddPAiAlbRWvlqq7nLS2%2B6dmc%2BKpRgnP9Ez4K%2F01%2Bm7%2BLbxSfyr%2FAwhQEAAaDDYzNzQyMzE4MzgwNSIM6OyLvR4XQP6r%2BQiWKtwDlTctjSj3zWyj7pbookUnY%2BjO4778u%2F%2B1GZ0%2FpOHYwcnjeJRP8R1DH7WbgPhwogwANxLidksOmwYlsCdHqTkOM2hga4vg5yVsMkfjpHxB65LmHj8rcj6WwMNM5o8bMLWTw1A%2FuZCRBRxHVGPhxknk%2F5xu%2FiU2Jfe%2BdOBqnh6TiwkL4BbnJR2%2BitfXdpWghmZiER%2FvM73IQW5DaOnWCkW09b%2BnEwPc7WwRigxSe2uVNeEh1Sm8jfYbTl3ZJHFuBp3WlZg1KnHD%2FzuJiMY4aqE94aK5oYFBQCT2IL5tRkM8MZr%2FgqsPwyKxPTsDJ3Bi9gg9wDabbzsK8aqBoRJry2Af0J48TfxiBYsMC%2BGfS2HwOyBsZ%2FAl8ZuGLRQI%2F0i3WYALjnHcbVqmuX040acWW7wrGHACmEIf7Ah01%2F6wYlj7%2BhLdwPo1F21aqS3aiBJhDCb3WOb0tFtkHDiGPxiigKKKvNUFQQWOASr3sdCrtivpLV0CfQ6ODCzOZhXRy8RTLWgmhKyf%2FaI3w6KaCJbiDs6R%2BBBCFcwz1vMteZEM3N7iR10rZD2lp80UI7S9oJqlVHnZjb7HYmqhrT9Y0qZiEKgJdhUhF7VMmvWpjijGeTakDXUP1Sxi%2FPRUdHqfe2kwlNyPvQY6pgFZ0Ecd%2FqIfoRczl2GjWr4MjKtixV%2F38%2F1rZMfHvcv2aVIPFIeaz1xMR75QYPvJCp0c3KQ3Rs5P3E3ylWNi3MGFcqKPdHBfV4GJUfqYxo31jDOqqbmbkFQ8O2ZCkaKbQr%2FVDlcIZyMJvOQ5jy8U%2BCFX%2F1vAill3VO9NANR2NyVghxkAYtranSUK5M1Vc315nr9zywdHON3Q6%2BslyCaK3QQS3tn0EFwD&X-Amz-Signature=17b9771df388574d160e3afd4120b9c1044af865ef0d258696efed59a43777fc&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Algorithmic Libraries
#### 1. **Scikit-learn**
- **Description:** Contains tools for statistical modeling, including regression, classification, clustering, etc.
- **Built on:** NumPy, SciPy, and Matplotlib.
#### 2. **Statsmodels**
- **Description:** A module for exploring data, estimating statistical models, and performing statistical tests.

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c62885f5-417d-4179-834f-d68f8f2bdf39/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466V7JENUI6%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T231407Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDcaCXVzLXdlc3QtMiJGMEQCIBTDKqYtb2wwdDkStwRNpXFCdT8zRxW4EWunN%2Fi19ddPAiAlbRWvlqq7nLS2%2B6dmc%2BKpRgnP9Ez4K%2F01%2Bm7%2BLbxSfyr%2FAwhQEAAaDDYzNzQyMzE4MzgwNSIM6OyLvR4XQP6r%2BQiWKtwDlTctjSj3zWyj7pbookUnY%2BjO4778u%2F%2B1GZ0%2FpOHYwcnjeJRP8R1DH7WbgPhwogwANxLidksOmwYlsCdHqTkOM2hga4vg5yVsMkfjpHxB65LmHj8rcj6WwMNM5o8bMLWTw1A%2FuZCRBRxHVGPhxknk%2F5xu%2FiU2Jfe%2BdOBqnh6TiwkL4BbnJR2%2BitfXdpWghmZiER%2FvM73IQW5DaOnWCkW09b%2BnEwPc7WwRigxSe2uVNeEh1Sm8jfYbTl3ZJHFuBp3WlZg1KnHD%2FzuJiMY4aqE94aK5oYFBQCT2IL5tRkM8MZr%2FgqsPwyKxPTsDJ3Bi9gg9wDabbzsK8aqBoRJry2Af0J48TfxiBYsMC%2BGfS2HwOyBsZ%2FAl8ZuGLRQI%2F0i3WYALjnHcbVqmuX040acWW7wrGHACmEIf7Ah01%2F6wYlj7%2BhLdwPo1F21aqS3aiBJhDCb3WOb0tFtkHDiGPxiigKKKvNUFQQWOASr3sdCrtivpLV0CfQ6ODCzOZhXRy8RTLWgmhKyf%2FaI3w6KaCJbiDs6R%2BBBCFcwz1vMteZEM3N7iR10rZD2lp80UI7S9oJqlVHnZjb7HYmqhrT9Y0qZiEKgJdhUhF7VMmvWpjijGeTakDXUP1Sxi%2FPRUdHqfe2kwlNyPvQY6pgFZ0Ecd%2FqIfoRczl2GjWr4MjKtixV%2F38%2F1rZMfHvcv2aVIPFIeaz1xMR75QYPvJCp0c3KQ3Rs5P3E3ylWNi3MGFcqKPdHBfV4GJUfqYxo31jDOqqbmbkFQ8O2ZCkaKbQr%2FVDlcIZyMJvOQ5jy8U%2BCFX%2F1vAill3VO9NANR2NyVghxkAYtranSUK5M1Vc315nr9zywdHON3Q6%2BslyCaK3QQS3tn0EFwD&X-Amz-Signature=f6e24bc4ace9bc746f03b214da52bd574ba45fb28646ed1a6d8ec65ca148aae7&X-Amz-SignedHeaders=host&x-id=GetObject)
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
