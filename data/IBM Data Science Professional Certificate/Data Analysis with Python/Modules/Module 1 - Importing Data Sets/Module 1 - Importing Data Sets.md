

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

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/997ac361-58a8-4f04-bb0f-79fea4baa761/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RN3LILQU%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T071418Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA0aCXVzLXdlc3QtMiJGMEQCIHDworyucNPNJkKngrNrGtIzPEc%2B6Fcu1kBwrFGXWSTNAiBZrUW9pY1Iz%2FTo2OH6cd6bV3DUhFGfNQWLb4MfL%2BxzMSr%2FAwgmEAAaDDYzNzQyMzE4MzgwNSIMdBoy8gPXi%2F2K574AKtwD2%2F1vhqO3OY%2F2%2F%2BgnL%2BiAtKnxVL7ZRmQzl347b1UNe%2FpAwiJfbhOx3s4nz0vvZC7puY%2B0hEzu3y1obaCJ%2FmhVFzs7M0lvaz6LZu8eY016JpkV3QmK5lFwyXoRw5ucLaa2sWw%2FgcbpoTWm9Irnc%2Fm0rdoWmLNW%2BL5wUWUnHk0gqJSE1uTK6fmlnUmWNCznBP4pKjAnOnyqRuWvQ1sbZO0Y4gPhG38XuhCdMLskPownkjUmcricJp0femUbUhDR0M1FSM7RLtKNJnPopD4TEH5Tm06sTCDeQxPdPRW3DUDPhBdYQBhqu6qpwkY7YP9xHhbD1hnIyqY3j%2B7P8jlBMJuyjzmc0d4VtNiIjZInbGZvfgnnDiBHBKxnBgZQBaEHYfbX7cHIDpkgN4tX6lpGN2o%2BxUeAbjXoaURdNAR0TUXtOaRgugqLm78p2vlgTrR7AqTxqwl2D0SUH0JNkMS3J5YL0FUJ9DuJGpFPbqDeYc2bUgOxrrxAP75JQOTpuuNLK30Gfnqp1jhrNbFsMaD3EJMRvp4r7rNnCM1OfaBnEwRSuHcxk3273594FcOxRvIEK7WFShpeabKbZqmBg2asAvROz6ShT%2FWdgunIBc%2BVMNK4XuntiEJgUPe4I4kiJ0AwxL6GvQY6pgH7r28rA0cg0LbcAVlmeF%2F7lTEg0RTpIGpb28x5%2FEZ2ONi%2FMowsdQ6b1gCz8bPBeanfDt0I%2BTnxAPS7g5%2BMcFl74idm6LeNb0eDzHms9g95%2FtRFGS9%2BJ0TtYmUj%2FDPf1aE5o4jNuDSB3QsHqQ0u8LUMVjDmkNR4E1CwuhQ%2FcfIA41FUl30Cg9D0FsS9uSnVt%2B5JI3Ha4cj5uAEEsqDbgh0F0dfFVBVw&X-Amz-Signature=8a2d7483e693e45d44f61c4a886950851ea35b3acfe61891ad364c618e998407&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Data Visualization Libraries
#### 1. **Matplotlib**
- **Description:** The most well-known library for data visualization.
- **Features:** Great for making highly customizable graphs and plots.
#### 2. **Seaborn**
- **Description:** A high-level visualization library based on Matplotlib.
- **Features:** Easy to generate various plots like heat maps, time series, and violin plots.

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/733d1e42-5a53-4fd8-90c1-3d85254369a6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XVEAMGKN%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T071418Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA0aCXVzLXdlc3QtMiJHMEUCIQCaYqDqlfkCsrN19%2BV7f%2Fow9agM7dNWUiqudp8NyZ%2BX9gIgaR%2FhN8xP9%2FUkwrEwBq%2FsNwu9YxsBvfkWfdoX7oIAyLQq%2FwMIJhAAGgw2Mzc0MjMxODM4MDUiDJ9osPc2jSCGIuPBrCrcAzXJu%2FhSzCM3b3HMLnViNP9tkpGwSxrbbHEZNe0zJXEgof4sCmjm7zd%2BYD0EF7IpUtV9XEf4SETq%2FpIicEIvQm7Qhl9nxgH6WRo8R7vFQyJ4Bw%2BMAoW2Pc4CqFfxEPxj2h8DTL8RRlXcgsHnkJZ%2FK3Rl6tDmrS3K9kduTOJB8iWL%2BbRCCG48KALErGlXHZVj0EpwCUakyhQipsdQXILimqdSSappSEo30JFIeQnC9aC9VuKfVH2RgkWMmTKyZPmClbNFpCDxKMDhN2hCieSyb4Od8qbWCqm8EEe8ds6qyS15O2rbwRxYz6HGqC4ps%2FkCymFq41u5xZcIFuLT%2BpphNseoU%2Bdzrms8%2BarjCc2rjhtBLq%2BdStM%2BGSEC4C0BsLo7qTNJwSExEcZ4rEj7W855FGBqtesfcAMpHDfuZosxSjEJ1b7G3c29RCVkuc7t2fOo%2B2%2BVmD9p3kwRqMbLZI6ep6FaUYPoic5hJ4cQYa%2FYuu7VrpRgLqEhCGPIWh82k1gtkEaxKIonFgD3gY9tmpvkmQTFqRCxfw5zfoXaebu3jTIgLXJ9yfE1eRme6foV9GfJyvUL8iUDyrQ6aDedBF6A0Od2Zl%2FmtL9OAuhuSgZcbku6eFGHDXLMTyTHxz1PMLO%2Bhr0GOqUBiLFXN3bce0QD5ibdl%2FTgcFifR2SOwRyRWgd69qyaUXWPhQdhTAOu9LXl%2BlEFoVWiz8a%2FWOsc9smS%2BzCsLdZwvybCXjiJ%2B2oaqCkxytLH9yozQILws06J3WLA71dF98TJxaqixMtCjDtH7j2Wi88TwuBDPNyotqR85c23gaaZTmSVy7JjUOkuwjcKQ3K7tKJoOSN5mT562rQ0DPdEMnYCFx7IcV8s&X-Amz-Signature=2e2c2c95cf39e599c6e293ccd429dcd612945a8fded1cdf81ee2277d4f5cf58a&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Algorithmic Libraries
#### 1. **Scikit-learn**
- **Description:** Contains tools for statistical modeling, including regression, classification, clustering, etc.
- **Built on:** NumPy, SciPy, and Matplotlib.
#### 2. **Statsmodels**
- **Description:** A module for exploring data, estimating statistical models, and performing statistical tests.

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c62885f5-417d-4179-834f-d68f8f2bdf39/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XVEAMGKN%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T071418Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEA0aCXVzLXdlc3QtMiJHMEUCIQCaYqDqlfkCsrN19%2BV7f%2Fow9agM7dNWUiqudp8NyZ%2BX9gIgaR%2FhN8xP9%2FUkwrEwBq%2FsNwu9YxsBvfkWfdoX7oIAyLQq%2FwMIJhAAGgw2Mzc0MjMxODM4MDUiDJ9osPc2jSCGIuPBrCrcAzXJu%2FhSzCM3b3HMLnViNP9tkpGwSxrbbHEZNe0zJXEgof4sCmjm7zd%2BYD0EF7IpUtV9XEf4SETq%2FpIicEIvQm7Qhl9nxgH6WRo8R7vFQyJ4Bw%2BMAoW2Pc4CqFfxEPxj2h8DTL8RRlXcgsHnkJZ%2FK3Rl6tDmrS3K9kduTOJB8iWL%2BbRCCG48KALErGlXHZVj0EpwCUakyhQipsdQXILimqdSSappSEo30JFIeQnC9aC9VuKfVH2RgkWMmTKyZPmClbNFpCDxKMDhN2hCieSyb4Od8qbWCqm8EEe8ds6qyS15O2rbwRxYz6HGqC4ps%2FkCymFq41u5xZcIFuLT%2BpphNseoU%2Bdzrms8%2BarjCc2rjhtBLq%2BdStM%2BGSEC4C0BsLo7qTNJwSExEcZ4rEj7W855FGBqtesfcAMpHDfuZosxSjEJ1b7G3c29RCVkuc7t2fOo%2B2%2BVmD9p3kwRqMbLZI6ep6FaUYPoic5hJ4cQYa%2FYuu7VrpRgLqEhCGPIWh82k1gtkEaxKIonFgD3gY9tmpvkmQTFqRCxfw5zfoXaebu3jTIgLXJ9yfE1eRme6foV9GfJyvUL8iUDyrQ6aDedBF6A0Od2Zl%2FmtL9OAuhuSgZcbku6eFGHDXLMTyTHxz1PMLO%2Bhr0GOqUBiLFXN3bce0QD5ibdl%2FTgcFifR2SOwRyRWgd69qyaUXWPhQdhTAOu9LXl%2BlEFoVWiz8a%2FWOsc9smS%2BzCsLdZwvybCXjiJ%2B2oaqCkxytLH9yozQILws06J3WLA71dF98TJxaqixMtCjDtH7j2Wi88TwuBDPNyotqR85c23gaaZTmSVy7JjUOkuwjcKQ3K7tKJoOSN5mT562rQ0DPdEMnYCFx7IcV8s&X-Amz-Signature=4ee2823c7d8448ad97f5d019372a0f29dc7c7f35eaffe07bb998792eaa027855&X-Amz-SignedHeaders=host&x-id=GetObject)
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
