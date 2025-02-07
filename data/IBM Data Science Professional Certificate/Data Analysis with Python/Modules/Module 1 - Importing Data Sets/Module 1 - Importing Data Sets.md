

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

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/997ac361-58a8-4f04-bb0f-79fea4baa761/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663U2WD6Y4%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T091526Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFgaCXVzLXdlc3QtMiJIMEYCIQCcZxXQdWqCBRfR8EBNJZryQvPQoZRXJu6wnoGdtxb6ZAIhAJv5M1PY4WPMQCldqgdBztSIqJqYPlWb1LeUhxELkZhYKv8DCHEQABoMNjM3NDIzMTgzODA1IgwjHUoemsKbuSVje%2F4q3AP5GoNJuLDvG%2BUfkjQ%2B1nNPXolEQ8yyTK4CnCAVVBeAC1W7TovN7L4ubTpl0s%2Bb1Crc9se9EiARfmiOTkybIBPvqlSkScC9%2B8Hegfhd5UWFAh258jfpTdGLgRCYCFOOBBYzYswyFyq1rrZN7su%2Bq0uFJ1qqi49KA37R0JP%2Bs4F6%2BEEShoSYMAtaPFRGMw2jHnsXZ0iG0A6aFIOuvnWbDduMkW0RLpS5IRfmg75yiIYHCw2aV3sCNMs4VcfHs3UmKbhlNwcycGZHAGmVmCVS17Cu0WKiUxYLVm3rmU7e3atnxR6eSZ5ibJ5uISco5bdnkpLtzRgJxRFkEsLK5D8N%2FgY3O5JZX5hKknYj6U9O0qrmK1yBSUCT9F34%2BKF75nbBum7F2t61X%2BK%2B4W5qQGR%2BII1ZuSUOrot14%2F%2Bx3%2Fr3S512fOYXwF8Jgle5C3SPHwsJOSXZY2BI2ZWmFtPIvvI%2F3Pv%2FZwka5eNClaczFC9JkEeG2KRYKkMBaL5GU9%2FeM2yqmdUO2wckvv8ryrinehhh8wdIrPIM8HMpgEGiTkYPDFdZ3EWb5JAHWKDX7ZzUU7IxcZwRLglytv93Amy9s7Wdc1LaU8CE%2FjeWopokhBw89YH3GLNygGHMAhw1sVWEvDCC%2Bpa9BjqkASYrKZtmDymXg0B2sdntgRCEzh5I1C4qSCl%2BGp7BnxZVp%2F3HFBSZEt3d9Z5yagO%2FocRJMrxGKmpDQ1T6feo8Y5b%2B7TclREG3ydei%2BJy7wUcck2z4CziJjydk6Jpo%2Flfynsfeh4tVCwVfYGQVG7zHhQkWbq18Qb3sFcjZuxL6KfepdNpAKFGO7kTohpoFoG40d6Uipg%2Bm7OAvRKa9ujzjI0a1xm6Y&X-Amz-Signature=41e516b2d02f36e97c898c0d99eccce14bd2e4988b53539a7f7028924f82fac1&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Data Visualization Libraries
#### 1. **Matplotlib**
- **Description:** The most well-known library for data visualization.
- **Features:** Great for making highly customizable graphs and plots.
#### 2. **Seaborn**
- **Description:** A high-level visualization library based on Matplotlib.
- **Features:** Easy to generate various plots like heat maps, time series, and violin plots.

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/733d1e42-5a53-4fd8-90c1-3d85254369a6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665MEBIWVT%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T091525Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFgaCXVzLXdlc3QtMiJHMEUCIERI1UlnnbTUDm4tRCCEt2pHXHSc4l9mQF1Yb3yyh6XWAiEA%2B%2FumEFdcmsIx2XmDUu45JZrPpngSF5XDLohCD9WwyYMq%2FwMIcRAAGgw2Mzc0MjMxODM4MDUiDJGWYQ%2Br34c%2BCHfPrCrcA5c4rjO2GWPkrPWpeAZnbdkKT1LaID%2FBuaWhZA7NT%2FZU2Xjx%2FCbktQXOH2nQZH7vYcjt9q09aAmrnt0xRNHgKDqH81SGnAXeFOqJ3RDfIaUFu0AGuae7x1P11SMD33GsBMoNBmXTQREeNpoiwO5YXJId6kcFtTGsnrS20SFS%2F7%2FBT%2FsYiDkv4B19P7EV%2Fm5p8%2Fj7LDNi7s%2FPECZW1pJ%2BKiiWqUxt8Wf%2FZSwG8kmRW4YeRdcqjGmMPIZljL59SnInSX0q55UxILHDaoHpVV40m6a24GyqIN5UZDZKuJor%2BjbOgaQQlw%2FgKnYiyPFZnabsA4LZLHsjWW54UKuXmyMAkKZrQ1QKtQLR0lPwBisDC4IZjhBpbAkUqfzetGbEhnkS%2BaShZ63VRAqd%2B6%2BhdBzHlHXltbOwn8HjMlVsLV%2BNPwDlmRvkCnL5Hqd7t0St8Uf2OJ43QXXHOQzpTxqD4Mw723jnKNQ3Q804mq9QwFOSDFaeFgtKWSZ7TS2zq2mn0xJTifv%2BA5xbKao4BtelrBdQT%2BsQw32MSSEnYAArMq4Ud7VOFcxfRqYV5MDwVH%2B7ZpvpoEs4kyrSA3L6ZjMs9WTXmUrWJdsAUM5S5j4nETrofyWMsBUtJrma%2Bj8PPv96MM%2F5lr0GOqUBb0S%2F69cX11dO8fFekliS8j8tWwoVV7Tr%2BXMv88Qbuhcpm0BM1%2B%2B99m%2FZ68hd6%2Fn1PoZC2Q95%2B2q%2F3PWZj6P5jSa1dlV2WihvY9464LJUN2ExRTGGqWMCNq6vSa%2BJb5yJ0EXULDG7628%2FAww8L5VCKMBUovBHySBlr6kY6oygt1vlVJ%2FDunA%2FupBHNwlLBfP9D1c9PdPym56kaYHaDFkeP7ZcT7kV&X-Amz-Signature=de2a97fadb85871d6c68dabb1ba201f843db970c1167281350a91ab3872ffcf6&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Algorithmic Libraries
#### 1. **Scikit-learn**
- **Description:** Contains tools for statistical modeling, including regression, classification, clustering, etc.
- **Built on:** NumPy, SciPy, and Matplotlib.
#### 2. **Statsmodels**
- **Description:** A module for exploring data, estimating statistical models, and performing statistical tests.

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c62885f5-417d-4179-834f-d68f8f2bdf39/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665MEBIWVT%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T091525Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFgaCXVzLXdlc3QtMiJHMEUCIERI1UlnnbTUDm4tRCCEt2pHXHSc4l9mQF1Yb3yyh6XWAiEA%2B%2FumEFdcmsIx2XmDUu45JZrPpngSF5XDLohCD9WwyYMq%2FwMIcRAAGgw2Mzc0MjMxODM4MDUiDJGWYQ%2Br34c%2BCHfPrCrcA5c4rjO2GWPkrPWpeAZnbdkKT1LaID%2FBuaWhZA7NT%2FZU2Xjx%2FCbktQXOH2nQZH7vYcjt9q09aAmrnt0xRNHgKDqH81SGnAXeFOqJ3RDfIaUFu0AGuae7x1P11SMD33GsBMoNBmXTQREeNpoiwO5YXJId6kcFtTGsnrS20SFS%2F7%2FBT%2FsYiDkv4B19P7EV%2Fm5p8%2Fj7LDNi7s%2FPECZW1pJ%2BKiiWqUxt8Wf%2FZSwG8kmRW4YeRdcqjGmMPIZljL59SnInSX0q55UxILHDaoHpVV40m6a24GyqIN5UZDZKuJor%2BjbOgaQQlw%2FgKnYiyPFZnabsA4LZLHsjWW54UKuXmyMAkKZrQ1QKtQLR0lPwBisDC4IZjhBpbAkUqfzetGbEhnkS%2BaShZ63VRAqd%2B6%2BhdBzHlHXltbOwn8HjMlVsLV%2BNPwDlmRvkCnL5Hqd7t0St8Uf2OJ43QXXHOQzpTxqD4Mw723jnKNQ3Q804mq9QwFOSDFaeFgtKWSZ7TS2zq2mn0xJTifv%2BA5xbKao4BtelrBdQT%2BsQw32MSSEnYAArMq4Ud7VOFcxfRqYV5MDwVH%2B7ZpvpoEs4kyrSA3L6ZjMs9WTXmUrWJdsAUM5S5j4nETrofyWMsBUtJrma%2Bj8PPv96MM%2F5lr0GOqUBb0S%2F69cX11dO8fFekliS8j8tWwoVV7Tr%2BXMv88Qbuhcpm0BM1%2B%2B99m%2FZ68hd6%2Fn1PoZC2Q95%2B2q%2F3PWZj6P5jSa1dlV2WihvY9464LJUN2ExRTGGqWMCNq6vSa%2BJb5yJ0EXULDG7628%2FAww8L5VCKMBUovBHySBlr6kY6oygt1vlVJ%2FDunA%2FupBHNwlLBfP9D1c9PdPym56kaYHaDFkeP7ZcT7kV&X-Amz-Signature=891f755b3886be0ea0080b09d22394ce78860858068e0bc7d28e0c7a590d638f&X-Amz-SignedHeaders=host&x-id=GetObject)
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
