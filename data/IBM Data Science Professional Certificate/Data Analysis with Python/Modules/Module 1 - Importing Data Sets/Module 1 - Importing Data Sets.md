

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

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/997ac361-58a8-4f04-bb0f-79fea4baa761/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VE6LXML4%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T041756Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECAaCXVzLXdlc3QtMiJHMEUCIAvKD8BvSWLtri9cgbHPsPTrv3u6usvidmxsXiZcr%2FDnAiEAnl%2Bn5hQnb0YvT6IWrdBKojzO%2F9NJ9f0sAbWkCZqZEz8q%2FwMIORAAGgw2Mzc0MjMxODM4MDUiDMY91qHLnISnic4T2CrcAzpuoI2Ig%2BskjO0p51xCra2j9aAM3zJw1wxTj4ona3fXSyEb6Qnz5Hl8SazTPp7F8wJFhBRGJuGIF7hznR56tKL0rvWEUATT%2BbEuhA1h7%2BuF1q18GPsKTHx4fGL83eINxM19HMOslGz8OBgJnUXTNrY2wNU%2FqHTJuQub1HxVWBB0SxZLD2v0gzDoM8WBFJdWsszv29viFOqnRZVOiaSgV9X2NXxzl3jBX7j1K1HM0XGUUPhlxrj37phX6WMAyljgaEOcRX1adccH1xYbn2qu4XqD9HI%2FmWMrMbyJgh%2BXt63bpfFmgeQWRI9LiMQI4tGqPDHlxRgceQDDusSiEisPL7iO1tsidI42v59HKCQEb9OYVrnlEgI%2FzKq6phegV%2F22EYagNEMmBGzC7Qp%2B6ozzjwkDq3N0vLu2HjjZqQAOj2Y8ATUGbmGn3ubYahhLpg6QSoKsFABx4i%2BDhlCnq%2BknDIcw9AtF%2BOWH2YQJ9MyK3PcBrz72Ze0dacVJ1sbxnmcb7Hhrjaf1rBpvH6vE9mvrF9m16TcLLwqjcPs3cUX7KpZ849ix7DTNV%2FmQH2uEEvQTdH0HClbCpOy2cfdW5DpK9fKtlwNdaNErDB2Esxz9UVRm9Wv99B%2FikRCao27yMNbNir0GOqUBth86oPYLM3l0ktOgWe7W%2FkAkoLD5Uwee2cOX3CCIPBg1AFTy2yB2SQYrIYDKwPRkuV4VSXzhtLowWtGsb84dI6PKg9WHPeBEKlbU2p%2FGIXnaZJuHOc3wpj86JC1eFnoXFSgAbMgd8IAe020gUyeRAKb0X2PL52dE9z5MhiG54YBerk8DPv6q6xtdeNFBMjZKn8bfYraV5lFk1K%2BHoz7nRQaxYhrc&X-Amz-Signature=2753e9fc2b7d3bd7331c95150a5c920417e2e3d03c38557c228fb0d34b2e3721&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Data Visualization Libraries
#### 1. **Matplotlib**
- **Description:** The most well-known library for data visualization.
- **Features:** Great for making highly customizable graphs and plots.
#### 2. **Seaborn**
- **Description:** A high-level visualization library based on Matplotlib.
- **Features:** Easy to generate various plots like heat maps, time series, and violin plots.

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/733d1e42-5a53-4fd8-90c1-3d85254369a6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VT6OFBSI%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T041753Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECAaCXVzLXdlc3QtMiJGMEQCIHmpjb26MXhV4iLrRHPTqMmJ1a7KE2sTGRAyODC1hl%2FrAiB1bRaj92FIVM6wmNsDBpCzpfoHF5o2x1hAbbdRrwmiSir%2FAwg5EAAaDDYzNzQyMzE4MzgwNSIMwpGgBiRzw9MCAfrXKtwDkDOOKdWukenxxlzg8dDAso0d7RBURVMXRWZO6%2BQ9tp8omfjgDmFyz7tS7k0hUzqXmlLgYIVZZAJf2sYB%2FUdgYxgocs7Yf8kZnvE0kgiyilAXsrUYx%2BlU8lmAJks%2BTUlUVY8IML0em3asIsNMrxu1lMwCweLWonH1dbX%2FOEz7pJ%2FqTrsNcxCPLtlni3nv0bInkLGGHZV6BcAse1%2BLAQ9VpsfCs79q7ZcPXdLkrUMvSCOyP8k2kXC9ddhjB5ThsxD6Z5JjnovX%2B5LSenRLHB%2B1vP%2BrgAdteh1YhESax1SjBrkV1qmH2LWrILd13GS63iJRqOvmsKbRUI428SSNbqjkegBiuWRzNt574Vt%2BGc%2F5OLQI9cW9Rct4rivR93VrHonMMpMonqEa9uEe4i6Li39LpvuqMqbx8M2Dpx6OMVqMkRvUiljNRkDZ74zLi%2FtFh8RobGHpH8UrLvHQvHw1Pe11l7dfnqGoQG1j8kG3F5eFxYK0npQIIHaTHwQJ%2BVp208xUi3vPxEVmsr03KKuwDESaX8n8TY0P8Pt2EypBmfPzvmbVBt5Pt5FZJRxj7WPluf3J2O1g2m3d9D1Haez7Xve7xovIAJ%2BcomysRGT%2Bo3INROwgwiXRsc3C3eyZSc4w8syKvQY6pgHz8D3lId0uscxlIE97AaryFHuZQeuxYVgsIcSPz%2FzhEDvpCnvKGiVGZUDk5aiMfyEcaI7gjnqyVCCqEOQl%2BQzZy0vYyLatbvlccazqqnBRAgtzXksZdQ3V1NJXnaXvCWrcuDDfK69mLX%2FFkF7gDZoY8Qg5yC0Bj%2B95wGF0ZOhh%2F5yckXsN1DuMmZZHAUaVcBX%2Fsy4pNthGjSOCSgW%2Fk3fmqztN%2F4p3&X-Amz-Signature=6af2ecf25fa610612c4d5907646dd04fd061ff984cbeb98fc82928680873c661&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Algorithmic Libraries
#### 1. **Scikit-learn**
- **Description:** Contains tools for statistical modeling, including regression, classification, clustering, etc.
- **Built on:** NumPy, SciPy, and Matplotlib.
#### 2. **Statsmodels**
- **Description:** A module for exploring data, estimating statistical models, and performing statistical tests.

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c62885f5-417d-4179-834f-d68f8f2bdf39/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VT6OFBSI%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T041752Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECAaCXVzLXdlc3QtMiJGMEQCIHmpjb26MXhV4iLrRHPTqMmJ1a7KE2sTGRAyODC1hl%2FrAiB1bRaj92FIVM6wmNsDBpCzpfoHF5o2x1hAbbdRrwmiSir%2FAwg5EAAaDDYzNzQyMzE4MzgwNSIMwpGgBiRzw9MCAfrXKtwDkDOOKdWukenxxlzg8dDAso0d7RBURVMXRWZO6%2BQ9tp8omfjgDmFyz7tS7k0hUzqXmlLgYIVZZAJf2sYB%2FUdgYxgocs7Yf8kZnvE0kgiyilAXsrUYx%2BlU8lmAJks%2BTUlUVY8IML0em3asIsNMrxu1lMwCweLWonH1dbX%2FOEz7pJ%2FqTrsNcxCPLtlni3nv0bInkLGGHZV6BcAse1%2BLAQ9VpsfCs79q7ZcPXdLkrUMvSCOyP8k2kXC9ddhjB5ThsxD6Z5JjnovX%2B5LSenRLHB%2B1vP%2BrgAdteh1YhESax1SjBrkV1qmH2LWrILd13GS63iJRqOvmsKbRUI428SSNbqjkegBiuWRzNt574Vt%2BGc%2F5OLQI9cW9Rct4rivR93VrHonMMpMonqEa9uEe4i6Li39LpvuqMqbx8M2Dpx6OMVqMkRvUiljNRkDZ74zLi%2FtFh8RobGHpH8UrLvHQvHw1Pe11l7dfnqGoQG1j8kG3F5eFxYK0npQIIHaTHwQJ%2BVp208xUi3vPxEVmsr03KKuwDESaX8n8TY0P8Pt2EypBmfPzvmbVBt5Pt5FZJRxj7WPluf3J2O1g2m3d9D1Haez7Xve7xovIAJ%2BcomysRGT%2Bo3INROwgwiXRsc3C3eyZSc4w8syKvQY6pgHz8D3lId0uscxlIE97AaryFHuZQeuxYVgsIcSPz%2FzhEDvpCnvKGiVGZUDk5aiMfyEcaI7gjnqyVCCqEOQl%2BQzZy0vYyLatbvlccazqqnBRAgtzXksZdQ3V1NJXnaXvCWrcuDDfK69mLX%2FFkF7gDZoY8Qg5yC0Bj%2B95wGF0ZOhh%2F5yckXsN1DuMmZZHAUaVcBX%2Fsy4pNthGjSOCSgW%2Fk3fmqztN%2F4p3&X-Amz-Signature=b5a247ebb19e9d38022996a45946843423db0451f8d12ab4e076222343915888&X-Amz-SignedHeaders=host&x-id=GetObject)
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
