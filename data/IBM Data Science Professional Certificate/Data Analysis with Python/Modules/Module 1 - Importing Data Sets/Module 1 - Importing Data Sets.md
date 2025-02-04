

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

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/997ac361-58a8-4f04-bb0f-79fea4baa761/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WKQHP75R%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T111220Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBMaCXVzLXdlc3QtMiJHMEUCIQCVbBha%2FTeT89EJQ03XsszD9P2BLvSXxbqqnUILYh1W7gIgFvmDzFXaVpKArvi1HgOEpHYcBISI%2F62gYF0Yxbd%2BYt8q%2FwMILBAAGgw2Mzc0MjMxODM4MDUiDNjw9ifGZsCruckovircA57wD3OVtiNK38gHyzEYK2%2BzpxVVYwlasbOyLLK3e%2FkT6r3PXWtPjMMSexpo107h8fPIWisHW4MomaoboF09rjr%2FHk9%2FZ5qSU%2FVG0XKDeliSuqJMzX1oaPUhSaMO5OJz7b3l%2FrWW0I8K58Z4WB1b%2FwcP4qaDcuFOEAE%2Fj2PR%2BAsYSCi7cwhoUAx%2B8eNtZkoNOl4qBM%2FS%2Bwd6WRbM5kyp%2F71rWX4S3wSBxQ0fcGnZ6KlInShN7%2Bmc75gLKlwieRKxCjHsEmuwM2R4wBr7%2FtQeq6WrkK5eIccb6cQoM4d9d4%2BjPEzkq6VGWCZY2kHCdADnnB%2FdVvyrJtiUBZmmL%2BzCdHU6gYa%2FtaL8e6xmjaAFIyRB59DSfXtnp4RC3zCyeMSKyWccW%2FlJRnggy19F5N2loEqenuuDDQk2EQ0v8RJNCx8juB9SWSGSG3Ms1QAgeiu2yASRMaGV4TAT%2Bc9Tp0NA6G9dpcDMheJGJY%2F6VRNbFD8W1vHgiLRN4tiFCfao5xgfPhtMZFMsWyGZN%2BnSRAD0vrQHvn3ZrB%2F%2FIQfVJLhnu1fKNOP7sH4v%2BpdeJ2yYpOb6PVOEC23z%2Bu5crwsIhCGncAtoZ7GoENUZ1R5wNdcRfAYshAg6DRSzeH5GM21mML7lh70GOqUBDLgFDFLzc5Rn%2FTR0cmLHNgD1Gri5Rso%2Fiz02khN8FzsV4g05ZslCcBgAd5llaa0We%2Ff1yvWJRaEwymAnEuWoXPnogt0GxvyhtTOZ8zvftqt9zqY%2F1%2FpXlrJVD5Ok96d8xu507cUTi%2BvkuiD51aL6xJ7y65hwF7aCUN%2FYjQ1oXxMTCRAcIp1bySewauSbBlf0pTwD9bFg4AoO20tjGBfj55dWoiI5&X-Amz-Signature=e483ac26446efe2e1206f09e5ddc43e3c2979aa34355be48baa29a6f18a022f3&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Data Visualization Libraries
#### 1. **Matplotlib**
- **Description:** The most well-known library for data visualization.
- **Features:** Great for making highly customizable graphs and plots.
#### 2. **Seaborn**
- **Description:** A high-level visualization library based on Matplotlib.
- **Features:** Easy to generate various plots like heat maps, time series, and violin plots.

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/733d1e42-5a53-4fd8-90c1-3d85254369a6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665KLQRUYI%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T111219Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBMaCXVzLXdlc3QtMiJHMEUCIB3LoqR5uBTdBw7Wn1MtcX3oC%2F6BgOeqR18rgJA1Kr6dAiEAvwWn6pTDvRkf3aXNPNHouePpZgdLVMl%2FCn%2BUiqGHNS8q%2FwMILBAAGgw2Mzc0MjMxODM4MDUiDIoXLloGBs0r5iq%2FMyrcAwHX8iAz%2FuL%2BxhDtwS8JfW4YSUirwbpgOhINxwAIyE3ReUhxhUKRx1lQGenzs0IZT9tw3m6RKQhl8y4rPHKXc2ZOANC95Z9S4wUGKb%2BYKZEmVhMek4I1o%2BpZvR94ETaAofeSKcwTRO8IbaoJVb6eoAB75VruEIg700xvaxcgFkkAAcAIsJ2v4PNqGZL2o4qDPWg31xpC%2B5NnZQptfUjZ6BSOQ4IUvnifJfCMYM8hyhWGM0ZH7W1fCKNK25nT7PzBY1167nE55FadQe7zPSN8kfp%2FOw0ivaECEWxVsR39lrY%2FXKbVUAyXh%2FjDJBWKenKeDN1POeMhgvnzlVTdckPEbECG59AgkQRdJ4vk7QyFr%2Bxc5w60kvsTe3RFknKsfp3b2ny6ooRa1oG6i7b%2FgCs2hoapQbfloYfutq5JiHTuzMbOmmntkWpTUjexYvW77rvkbTOOS7%2FJ4cdq6EhBwg1pV03vuGFLAI1kWwAvkiGW5EB1w%2BE2Rv3fFdDzbfpvKFNpI3xIsSNFWbyuHXnbLkahemjNBuyw6icakPiFY7LOtyCbMp%2BqDYO8WQjdvNix7bnF0GxBoJ5rNw3h4LLWYu4qheIb58OjNd9IDkNj5Oe1tNxxSPtkOinsi9RabrDOMNHlh70GOqUB5wIQLl9SOpBCvgT0sV6clS0HoCvfgQa2vGGT3zG5L3L%2Fk9QVgW%2BTjpS5Wws3KxTpSfYDJ9wp4RnYqE0U6tRtQOr41JwhM9%2F88iJzlVv6AVaXj1idDdG29dWDZdLl1aY0jvpcV3mnPpVvTS%2BkkYQXbKtEHBXzumEAbcJJuKj10m7eaNNJSk%2Bodb4hDjNsmzEAKW1lfnHYJsI6zfsdsbXxyWKNoXcx&X-Amz-Signature=83266b5acec2a6a5fefe12cc8aeba916772eb3c886c92b4bcc20bc3bd3ef89ef&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Algorithmic Libraries
#### 1. **Scikit-learn**
- **Description:** Contains tools for statistical modeling, including regression, classification, clustering, etc.
- **Built on:** NumPy, SciPy, and Matplotlib.
#### 2. **Statsmodels**
- **Description:** A module for exploring data, estimating statistical models, and performing statistical tests.

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c62885f5-417d-4179-834f-d68f8f2bdf39/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665KLQRUYI%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T111219Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBMaCXVzLXdlc3QtMiJHMEUCIB3LoqR5uBTdBw7Wn1MtcX3oC%2F6BgOeqR18rgJA1Kr6dAiEAvwWn6pTDvRkf3aXNPNHouePpZgdLVMl%2FCn%2BUiqGHNS8q%2FwMILBAAGgw2Mzc0MjMxODM4MDUiDIoXLloGBs0r5iq%2FMyrcAwHX8iAz%2FuL%2BxhDtwS8JfW4YSUirwbpgOhINxwAIyE3ReUhxhUKRx1lQGenzs0IZT9tw3m6RKQhl8y4rPHKXc2ZOANC95Z9S4wUGKb%2BYKZEmVhMek4I1o%2BpZvR94ETaAofeSKcwTRO8IbaoJVb6eoAB75VruEIg700xvaxcgFkkAAcAIsJ2v4PNqGZL2o4qDPWg31xpC%2B5NnZQptfUjZ6BSOQ4IUvnifJfCMYM8hyhWGM0ZH7W1fCKNK25nT7PzBY1167nE55FadQe7zPSN8kfp%2FOw0ivaECEWxVsR39lrY%2FXKbVUAyXh%2FjDJBWKenKeDN1POeMhgvnzlVTdckPEbECG59AgkQRdJ4vk7QyFr%2Bxc5w60kvsTe3RFknKsfp3b2ny6ooRa1oG6i7b%2FgCs2hoapQbfloYfutq5JiHTuzMbOmmntkWpTUjexYvW77rvkbTOOS7%2FJ4cdq6EhBwg1pV03vuGFLAI1kWwAvkiGW5EB1w%2BE2Rv3fFdDzbfpvKFNpI3xIsSNFWbyuHXnbLkahemjNBuyw6icakPiFY7LOtyCbMp%2BqDYO8WQjdvNix7bnF0GxBoJ5rNw3h4LLWYu4qheIb58OjNd9IDkNj5Oe1tNxxSPtkOinsi9RabrDOMNHlh70GOqUB5wIQLl9SOpBCvgT0sV6clS0HoCvfgQa2vGGT3zG5L3L%2Fk9QVgW%2BTjpS5Wws3KxTpSfYDJ9wp4RnYqE0U6tRtQOr41JwhM9%2F88iJzlVv6AVaXj1idDdG29dWDZdLl1aY0jvpcV3mnPpVvTS%2BkkYQXbKtEHBXzumEAbcJJuKj10m7eaNNJSk%2Bodb4hDjNsmzEAKW1lfnHYJsI6zfsdsbXxyWKNoXcx&X-Amz-Signature=1d460da1ec15592c5579a98ee0e6967fae20e5917f0860a1db779e9b20bb52d7&X-Amz-SignedHeaders=host&x-id=GetObject)
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
