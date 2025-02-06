

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

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/997ac361-58a8-4f04-bb0f-79fea4baa761/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YM7NA5EF%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T122954Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEQaCXVzLXdlc3QtMiJHMEUCIQCEkYU6wTxAq80zi%2F0cAZZBLfXbRU2vdb04vkD2CLWLsgIgTuZIJBYz%2BATzXCllhNjUoexRQAbnlJE7WgxA%2BbxkjOYq%2FwMIXRAAGgw2Mzc0MjMxODM4MDUiDH7S6SCeYl8i3pesrCrcA68rKgg6VveOtNfY1%2FbII6zINu6F8Q4O7Es0Tj3nvbBuwP5VIQAiiByr8ZXxKQebsSIvtausMGsI3Y5S%2FhL8Db35Eo6h7zGQZlTvRxzRWP3ggTL1Hc5bA1pHF4Bi%2B3NqMQ4%2B7Sr0ZnvUytKeaupJAX2j0ME1yuQyo0p70v06rKso4aypVjYa042o9soVhhtXhwnHUHqDARk0k5aJs%2FkqQFLSkHDAZE2S9QB8GlbONaTO4OT1uClMarhr6Zng%2F7eCTV4e0bg%2FIubuiHQEr9hQoAH2SpfFL%2FPu48fRzKB7hzFCJg2t81lOjx3woGJ0G7lPamVWlqtmwwInfX02cIXsJZSw7E6n6%2BBuGLas977s0r3DzvBcdgucyb7r0L0wgQ44eApbY3MmJH%2FCJkFoTe2UTsQ6wr6hSVFlT%2BTrcVYzef3fFnt2pBA1k3M7noEHapQRogRAruDjEMfUiPwUyki1laC9yq4jFFGgoOUwFULFxRgmIUOptF3CJ%2Bw65up4ETXVW4ytS5RneYm4FBSTw9Rnl6URPVs2ohxKFxkNacyftmWn5CEcByc40C3wjwjDykh%2BFy3etZqqeR%2Bu91hUw2ELHSBdD7Fgl%2BKfvmKGJBmtWFw%2BeaGvvrZezCxFRj6sMLnDkr0GOqUBnIAcLJTODXNjjibgGSSjNKv34q6Zyhb6lyi627fZoG47%2Ft3r3jSFECFgaW2%2FDAsBjfcRT1G1HY3JEXTJqZsMmwMRtufxFp%2Ba%2F1JaOLgPpX3H2EtFIPANwc4So9s8I1f123Z1yQdU6nWwq%2BefFyqHgRqwrrgM9W8FCDi3YvTbRrB2UCdTQd7cupqwVw1C3JitdadOYQiZB%2FS5HWt12%2BNA%2BUFuTX9M&X-Amz-Signature=317680134cb5c480c660a7b939e1d79b2b539ee3f9e6f6b4d4122d76b851a13d&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Data Visualization Libraries
#### 1. **Matplotlib**
- **Description:** The most well-known library for data visualization.
- **Features:** Great for making highly customizable graphs and plots.
#### 2. **Seaborn**
- **Description:** A high-level visualization library based on Matplotlib.
- **Features:** Easy to generate various plots like heat maps, time series, and violin plots.

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/733d1e42-5a53-4fd8-90c1-3d85254369a6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VG7XXFO5%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T122953Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEQaCXVzLXdlc3QtMiJHMEUCIQDFNwKZRlelhTrIwNpbSCh5eImhAwYSTNOUg0E4G3X9dgIgND87%2BywEje%2FPEjIOS2ouANbGrvugZK2rQPDVE2KTkwgq%2FwMIXRAAGgw2Mzc0MjMxODM4MDUiDPTYnlCSvrWtpJ%2BxWSrcA2PsAFhmmijogoDIZX2FmFEbfC6ozYGmGfqeMnGzQpgFIkbzG3%2B6912yaNBZ5vgQScH38mfxicI17bVBLmU3P6chG5p9dN1K8JpZ%2FUeljqq9FSI7VhYG7sfCTIopw%2FKeou5JGHeEdo6NNKq5Z3CHPC1hS3LOKAxnWD1nWmmdph0wrp5O4cpFOU4CpCiLW%2BCsABvFdnntIIJAloy%2FcT66ocLpq%2Fu3y6TumkILWakPW1KzdhRCpl9kbIEENouUQPgue3h5UZTyMAUyHJ%2BjxLcIhk0IvsJesB1vpXfjH1w2n8CAfacQUnmh9b%2BvwsR8bw2TlQWjOaCNQbJ8pDfVMjBDZNxwbD%2FLRyJX122UXK8AY3GmxWID%2FeIREz78CecHbqoqPz50tX%2FsPh5bhfSjW0JxYx7s%2B5Mb0Tp5S1P29SLRWwzrrk1IltvDMwTdTNoQ5H3IZwr7LmFwjGBy0%2BJkiyPV8Tn3zeumU6Ozbedg%2FktiyPFmTsLYsQkjycMrrs8GPeFTDwgLjNkLdKwabk8qo4uq3XLbLy%2Fg%2FM%2BdbI7nubVy6vfaea180qjvHkp1JxyAjRmhTh9h827a2Sewlt%2ByzKuVoqIHZKyJz1TgVMNHnlvXFTiMLE3Rv%2BtmEH69bQ%2BKMPjDkr0GOqUBPIfpxjVCpw3ZrVGt1Q81BoO0tLEC5ld%2B4gFYwuVgvnm1dIJm6UZht%2FOf6pGu2UAVY827pTQnQFZbLz%2F5zExDl5w0fMKp9EJn%2FFCpnVvQVS%2BrCZrxoGrI%2BWGU7bolwrONhZlkUXnm%2FGzAIKySGHwOr557M8DL3YR7t%2FkZMBllZtowWN%2BxBdz5szIu8XBZOTVRBOldh%2FghuLGC3QnjBntBH%2FtDTWep&X-Amz-Signature=0f872851b4337569c9f03f541309a0d665a13d0e4abde886667e71c77a73d24a&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Algorithmic Libraries
#### 1. **Scikit-learn**
- **Description:** Contains tools for statistical modeling, including regression, classification, clustering, etc.
- **Built on:** NumPy, SciPy, and Matplotlib.
#### 2. **Statsmodels**
- **Description:** A module for exploring data, estimating statistical models, and performing statistical tests.

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c62885f5-417d-4179-834f-d68f8f2bdf39/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VG7XXFO5%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T122953Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEQaCXVzLXdlc3QtMiJHMEUCIQDFNwKZRlelhTrIwNpbSCh5eImhAwYSTNOUg0E4G3X9dgIgND87%2BywEje%2FPEjIOS2ouANbGrvugZK2rQPDVE2KTkwgq%2FwMIXRAAGgw2Mzc0MjMxODM4MDUiDPTYnlCSvrWtpJ%2BxWSrcA2PsAFhmmijogoDIZX2FmFEbfC6ozYGmGfqeMnGzQpgFIkbzG3%2B6912yaNBZ5vgQScH38mfxicI17bVBLmU3P6chG5p9dN1K8JpZ%2FUeljqq9FSI7VhYG7sfCTIopw%2FKeou5JGHeEdo6NNKq5Z3CHPC1hS3LOKAxnWD1nWmmdph0wrp5O4cpFOU4CpCiLW%2BCsABvFdnntIIJAloy%2FcT66ocLpq%2Fu3y6TumkILWakPW1KzdhRCpl9kbIEENouUQPgue3h5UZTyMAUyHJ%2BjxLcIhk0IvsJesB1vpXfjH1w2n8CAfacQUnmh9b%2BvwsR8bw2TlQWjOaCNQbJ8pDfVMjBDZNxwbD%2FLRyJX122UXK8AY3GmxWID%2FeIREz78CecHbqoqPz50tX%2FsPh5bhfSjW0JxYx7s%2B5Mb0Tp5S1P29SLRWwzrrk1IltvDMwTdTNoQ5H3IZwr7LmFwjGBy0%2BJkiyPV8Tn3zeumU6Ozbedg%2FktiyPFmTsLYsQkjycMrrs8GPeFTDwgLjNkLdKwabk8qo4uq3XLbLy%2Fg%2FM%2BdbI7nubVy6vfaea180qjvHkp1JxyAjRmhTh9h827a2Sewlt%2ByzKuVoqIHZKyJz1TgVMNHnlvXFTiMLE3Rv%2BtmEH69bQ%2BKMPjDkr0GOqUBPIfpxjVCpw3ZrVGt1Q81BoO0tLEC5ld%2B4gFYwuVgvnm1dIJm6UZht%2FOf6pGu2UAVY827pTQnQFZbLz%2F5zExDl5w0fMKp9EJn%2FFCpnVvQVS%2BrCZrxoGrI%2BWGU7bolwrONhZlkUXnm%2FGzAIKySGHwOr557M8DL3YR7t%2FkZMBllZtowWN%2BxBdz5szIu8XBZOTVRBOldh%2FghuLGC3QnjBntBH%2FtDTWep&X-Amz-Signature=fa305bc7b0190c2c1ab464dc133d0a540c9591c86d7c4e14c15d8e9d20c92e96&X-Amz-SignedHeaders=host&x-id=GetObject)
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
