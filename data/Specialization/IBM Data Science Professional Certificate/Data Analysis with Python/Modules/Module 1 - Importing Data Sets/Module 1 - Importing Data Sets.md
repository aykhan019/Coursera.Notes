

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

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/997ac361-58a8-4f04-bb0f-79fea4baa761/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665OERKWIL%2F20250128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250128T201548Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHQaCXVzLXdlc3QtMiJGMEQCIA3B%2B4RJgZr%2Bf1Fq15y8uFm3IMthuH13%2Bb0TDIFi8GhwAiBc0pbI7SAI6ivkOxkG1evydFH%2B96%2Bt65seG5qGG73%2Bkir%2FAwh9EAAaDDYzNzQyMzE4MzgwNSIMWqVPwsvaNXbm2XhYKtwDbLaojgruFw4ZsFEkEjS%2BLnCntZiBnK%2BjySo7i10zL3UCPwXcP%2BX1tDOg2TLcZFPRv%2FGPb2PCUN%2F8uIImvhjfnBK3sug3hiZNzBoyy5Z62oFo6pj%2BfP22UpifwH9pORy2Yr9x8ZbHiiFBXuYI0FFYTrEGmwDUNiDC92eK00V25g%2B2MdaUNrJ7iyVt%2BcX9XbB6XK%2FIvqZ9PpVjZHjMAmlLFAVkZt%2FMQHMTCUSgOt%2FYF918En%2FZ64W5PSLDM7D%2BvGgXJzm5GR3tg6StagVrgT2BSiEoj%2FgfdnYr3vTk%2BFLvSme5u6yJyU0Jb9l05mQuKmSIygL0BZzVTbgYGujh8Jr%2FhP3Lel4irT978udL%2BWPNbgYDTIFWTtWyVp%2FH%2BSIOYDCZytXHdhEzD0EocHGCicX%2FZXEmAT6aSHWNMK7JoCq3CB2dah5CJS4OrnlkpqJYBCgAza6nuGF3w9EwTQ6gHiJIboIZza3xTJolxw7azhExLIJ%2FhhPCuUUgK9138134AbS6ADSggGohRRcjta9rr9LF4Gp8XSWkzeQWpbLj8VpOa8zhQqHYaXpkL3k8oGG44%2BwXh3LGY8h2DXj9RtpHThu6H%2B%2BGWO8JlBbbN3w%2BeOcNFT4Gd4UyeIMthrew1vQwr%2BrkvAY6pgG%2BYYm4CWHlBpD02BVfsxFnTbwi92HUZ%2F2RQT7mNCa%2BQufH6r5N6lPKJpi7Ap%2Bx1s4OSDDvl42CFFWd41X%2Ffuc8X%2B0pqodarCgLhCx827KE1MIcZbI8oDr66zEgPLS5D3luI5lnno2aquS7PuwD27iPZF5bBc5Fz7XJ%2BRT9jykH21wXXM%2Fv%2FVnUwWeMKMC0ItKyjV4DILrGNqypHcPprpHFJ5kYaANT&X-Amz-Signature=337f504ec5ef60507fa2f8d46f460904d36bf0a57230f241f54ef1c8513e80ac&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Data Visualization Libraries
#### 1. **Matplotlib**
- **Description:** The most well-known library for data visualization.
- **Features:** Great for making highly customizable graphs and plots.
#### 2. **Seaborn**
- **Description:** A high-level visualization library based on Matplotlib.
- **Features:** Easy to generate various plots like heat maps, time series, and violin plots.

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/733d1e42-5a53-4fd8-90c1-3d85254369a6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VPGTJA7L%2F20250128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250128T201547Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHQaCXVzLXdlc3QtMiJHMEUCIEJG%2B%2BGN8lpz0SVhbA0NhxpeARXoWAExSOB9BGSXfCaNAiEAvUJVu%2FbkyvVfOzn7aSofSlxjYl0jfwjO57gXy%2BtmnyUq%2FwMIfRAAGgw2Mzc0MjMxODM4MDUiDI%2FYKq60kUZmfOTh1SrcA%2BJM5seyI%2FCG6JIIkvGpTxq3V92%2BWHM9qburQLy0Mj7MIjoeEV5FUc4XfB6VDjvGHKvXzYuHfsH30IqrhMleAzBYGRQWfv0NQ301fiYadb195hlEnv4t1NFWZz1nVpuCa5MQi8gctgWvtLuRHGvXQixSKQ2twT7%2Fq9m6JXjDVDIA%2F4osz25LRHBuV0jZvW3NuR1R%2F9qF2SXRFD7japlxVdZtu2Tgl4bqC6QjCCfn4YmcyorT6XNqF5akwBs9a63SUGsYB3U56Gt56DkIL4rhhzK6JMSMoYnVLUX6Pca1BRQLacOzOmWgre%2FKZbQEB%2Bneh3fd%2BbcPXTtCHWvl%2BrTATWd2zDebMTDdeD3XLchtrbUX6dB2TlsROu7DL4T9b5KHKCleGj71VGGMNsLfK0BVVjbsN3xSzRHpAqzIw5xX%2FHIxVwXbWdr6d3juDnDrtMkinNog6sxFPSmlf0pkKRRKzfCUo49E%2Bl9ffp2PYosKB20NG2XszQisHZsUiwVSJ4GKHnKa1U5d3WNagQeNFQccV%2BPK6tv4TJtCqarxTSfxhI2p4928k%2BbFqaaghXosDbGtptPPhRY0Li%2F8ty9%2FiFTWEQUO%2FL3xlcnlJNvcqAlbdNC3dvdw%2FmUzlrjc2rWaMIvq5LwGOqUBwSXe3rPwRKG%2FncRISVvuvxWldoHl35UPMDxgjhxEf05gstNe6u2y5OlDwr%2BDVDCLlcar0TEQC7UVV5jhuLt%2BEQNBiOpMRxO2p0ru4SJPzXY3cda4pRC%2FqHyWd9kqSzvScC%2FYPgClZ5a%2BRxQhWaqMG6qHHXaGuVAH2mK%2FMdfalZcfp4umwQigpfUoO%2Fpe9pC8HiynYX73ju66GZQNwxCxDBQR6iUu&X-Amz-Signature=68da90099d6aad1e17f8f109e3143ca7b7d3da423b1a0c44c97bcded28582131&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Algorithmic Libraries
#### 1. **Scikit-learn**
- **Description:** Contains tools for statistical modeling, including regression, classification, clustering, etc.
- **Built on:** NumPy, SciPy, and Matplotlib.
#### 2. **Statsmodels**
- **Description:** A module for exploring data, estimating statistical models, and performing statistical tests.

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c62885f5-417d-4179-834f-d68f8f2bdf39/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VPGTJA7L%2F20250128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250128T201547Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHQaCXVzLXdlc3QtMiJHMEUCIEJG%2B%2BGN8lpz0SVhbA0NhxpeARXoWAExSOB9BGSXfCaNAiEAvUJVu%2FbkyvVfOzn7aSofSlxjYl0jfwjO57gXy%2BtmnyUq%2FwMIfRAAGgw2Mzc0MjMxODM4MDUiDI%2FYKq60kUZmfOTh1SrcA%2BJM5seyI%2FCG6JIIkvGpTxq3V92%2BWHM9qburQLy0Mj7MIjoeEV5FUc4XfB6VDjvGHKvXzYuHfsH30IqrhMleAzBYGRQWfv0NQ301fiYadb195hlEnv4t1NFWZz1nVpuCa5MQi8gctgWvtLuRHGvXQixSKQ2twT7%2Fq9m6JXjDVDIA%2F4osz25LRHBuV0jZvW3NuR1R%2F9qF2SXRFD7japlxVdZtu2Tgl4bqC6QjCCfn4YmcyorT6XNqF5akwBs9a63SUGsYB3U56Gt56DkIL4rhhzK6JMSMoYnVLUX6Pca1BRQLacOzOmWgre%2FKZbQEB%2Bneh3fd%2BbcPXTtCHWvl%2BrTATWd2zDebMTDdeD3XLchtrbUX6dB2TlsROu7DL4T9b5KHKCleGj71VGGMNsLfK0BVVjbsN3xSzRHpAqzIw5xX%2FHIxVwXbWdr6d3juDnDrtMkinNog6sxFPSmlf0pkKRRKzfCUo49E%2Bl9ffp2PYosKB20NG2XszQisHZsUiwVSJ4GKHnKa1U5d3WNagQeNFQccV%2BPK6tv4TJtCqarxTSfxhI2p4928k%2BbFqaaghXosDbGtptPPhRY0Li%2F8ty9%2FiFTWEQUO%2FL3xlcnlJNvcqAlbdNC3dvdw%2FmUzlrjc2rWaMIvq5LwGOqUBwSXe3rPwRKG%2FncRISVvuvxWldoHl35UPMDxgjhxEf05gstNe6u2y5OlDwr%2BDVDCLlcar0TEQC7UVV5jhuLt%2BEQNBiOpMRxO2p0ru4SJPzXY3cda4pRC%2FqHyWd9kqSzvScC%2FYPgClZ5a%2BRxQhWaqMG6qHHXaGuVAH2mK%2FMdfalZcfp4umwQigpfUoO%2Fpe9pC8HiynYX73ju66GZQNwxCxDBQR6iUu&X-Amz-Signature=576d81f2a1a0b68d50127fa204baf32f2c7f0de368be01f0eb85caa4db9726dc&X-Amz-SignedHeaders=host&x-id=GetObject)
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
