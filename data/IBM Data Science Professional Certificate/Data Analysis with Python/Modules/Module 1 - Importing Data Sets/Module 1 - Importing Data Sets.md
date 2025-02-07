

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

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/997ac361-58a8-4f04-bb0f-79fea4baa761/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662VIMJS5N%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T122856Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFwaCXVzLXdlc3QtMiJGMEQCIBqRLyhFQcsmZgrwG6mtqSfoWJckfRAjcRMXmoPWIsrwAiAMYqj%2BY0JcDf0zxYnC5dBT9ciLamynW4FWWbPh6NBxnSr%2FAwh1EAAaDDYzNzQyMzE4MzgwNSIM0Rr4eOA9OjcXQAkaKtwDA%2FNPTfySuMIsqC5z6v38%2BymOzunOASEJFNuJM5iPSRBfS%2BLazSxWoaHHJ6MjLX18XFbYXK7GcvbwHvbgT77HwHTYcfiIDcY%2FElkF6R4IoSw1RbubFlHwEYAy3NvHhnJ2eWASS87CZItj%2Bf8rViCq0boe9%2F%2FSGYVmxKkMBHmE6kkE6SdBIJfL%2Btw8IeEW0Benfarpk%2B1NEk70J2BI4b6CyPTjriwplXEuRbGZI%2BlTf9hFK3vov4frzipVMAUj42soshn6%2BKMU%2FiXdAtc1CJl9lTaVPyHiqQN1EibmM10tVMFJ7dROcPnsdKoC5BicXwAEVO%2FeOkTuRHb25LbiX0yZR7kGpayqRpwtu%2B7X0Lb8ko0G6Qz2yn7kUadU%2FevtE0HsNjd%2FQWT0DbDgjvo780sfHgVw9YQIiS6HyeE0p%2FdwPscz0hSLwGIsg3d1iG7GIQ1PJFM1Kn7tHQ9XDHYbF6irRgY%2FTtgwxJBz9yfeQYbbvfgALQ1i3816BUcGeyqY7bdazK%2FI7ReXwpyM5Bt8ETLn9oaHSBszBNvLjxgf2ggmJAdsNj6Ce7n5g7xiumoRmR66c6kt%2BDSVOnrT%2Fa1egEgFwtd2cIJOL8FVZPH8k%2Bkr68zN7UjIBpq2huCUOXkwge%2BXvQY6pgGR8UySlsbQ8667mpAENpbhwwvLcwCEnJQNZbOn1Me4AabhxINr2BiBHuqBMp2eDHPazgKEkUFEbY8jser1OCftG7%2B7f792%2FFunaaas%2B9aAadtkOAd11DexvZ82r0YWFk%2F3yoWv3Iyja6eBTivR06oW8%2BRgo6uedyE5uNDklb%2Fa0W%2FPz3Sju2D6f%2F88Zjjz2K%2FFb8bmpOYhv0XhiY%2BWo30hCJTEfDlc&X-Amz-Signature=aff329160067a63c17df0298216d2714eeb9fabdc83b40ff03a19f0bd05583f8&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Data Visualization Libraries
#### 1. **Matplotlib**
- **Description:** The most well-known library for data visualization.
- **Features:** Great for making highly customizable graphs and plots.
#### 2. **Seaborn**
- **Description:** A high-level visualization library based on Matplotlib.
- **Features:** Easy to generate various plots like heat maps, time series, and violin plots.

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/733d1e42-5a53-4fd8-90c1-3d85254369a6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466346HWXLL%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T122855Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFwaCXVzLXdlc3QtMiJHMEUCIQDDAUhQToMkWtANP7Y6hx4DcXzfM9%2BvOcbRh1NSs6SjJwIgeY4SI6tSkYUjgxvZ6OcjGrsS%2BYoWw%2By%2BDYKdbGXUo8sq%2FwMIdRAAGgw2Mzc0MjMxODM4MDUiDDU4TASfPr7ZqmIS7yrcA3mL5T0nPbqPRC3okc3%2FUPUxOu9AghNNPahKyMBbb5o4fiZBntfA7pBJ7eRl2E1SfpMT2zA64t2RjfQWeq4sxTGUPK9steUTpvYt3RmX7WT8m%2FH6wJR50yEDzdOeLxWPMI6WaZLiO2e7fBW%2BXKrU6TSqEg2s4jVfMH1oqXAwb5mn0FCcZAAQ2lx15q9BvKe0ewIdh%2F8ZRwrh8qNN%2Bu%2BtV1Z80vXwmgIim5JZLkfoYsaXb%2F6GhAS3%2FgBuF7iELPahrUhA0L6%2BBaGq2ZM5xwDJBdj0Rw%2BWd6M48YgZMuo%2BGEUkpHens1Ayz3Zex8cWuPIFgtDZBhyaN1poia%2Bl65EulUmC2qrttBlwl2xna16w0FVL4SLDWNOiM9xA1EpC96lMh9Pr7gQpukuoH6NWZDjrSsvXymqBW6jNky8BteMlMz2BBduVD7HbhkFIN2Miosb%2F5NCDBh%2FjBdaZG71p39EwbNkEr4jP7993cswPM9A%2BRSOKJdj6%2FDzlnGDXE3OdhY1SjM347Kag9%2BVRtN89CBncg54uTgcRJgqC0tMokduvrh9sKJE7rEKYqn%2BotnjacFQBejihlg6ZFYZs2D90ZDd4nNRIeTXR5RQk9WMBL3sV1FP8TJTk7jhyEMqsIIM%2BMK7vl70GOqUBPu6O6jj2dM5ik%2FD0pOv1akFD90LqXNn%2FCqdYHwx5J7upAjF0eyT5kP1HE5k8%2BdNdMuevFLoivU6CAj7FScXMFmmsYEYuQ0IF7%2BWdlMeDSiDq295GXMw6QGH6eEytunaMCT%2BRP8v5JnncOYoLLANzD35rKNxpXRaP4Y7mmUXR%2BvAaH%2Fc5aQrIBfnATAJPaK8MIOIfl%2BVCkVouHOCgH4zpAQfpQaEd&X-Amz-Signature=f2f136289331fbcac6ada0b633eb97c19b2a764ea8d5fb4c4005b52e97fd27fd&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Algorithmic Libraries
#### 1. **Scikit-learn**
- **Description:** Contains tools for statistical modeling, including regression, classification, clustering, etc.
- **Built on:** NumPy, SciPy, and Matplotlib.
#### 2. **Statsmodels**
- **Description:** A module for exploring data, estimating statistical models, and performing statistical tests.

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c62885f5-417d-4179-834f-d68f8f2bdf39/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466346HWXLL%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T122855Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFwaCXVzLXdlc3QtMiJHMEUCIQDDAUhQToMkWtANP7Y6hx4DcXzfM9%2BvOcbRh1NSs6SjJwIgeY4SI6tSkYUjgxvZ6OcjGrsS%2BYoWw%2By%2BDYKdbGXUo8sq%2FwMIdRAAGgw2Mzc0MjMxODM4MDUiDDU4TASfPr7ZqmIS7yrcA3mL5T0nPbqPRC3okc3%2FUPUxOu9AghNNPahKyMBbb5o4fiZBntfA7pBJ7eRl2E1SfpMT2zA64t2RjfQWeq4sxTGUPK9steUTpvYt3RmX7WT8m%2FH6wJR50yEDzdOeLxWPMI6WaZLiO2e7fBW%2BXKrU6TSqEg2s4jVfMH1oqXAwb5mn0FCcZAAQ2lx15q9BvKe0ewIdh%2F8ZRwrh8qNN%2Bu%2BtV1Z80vXwmgIim5JZLkfoYsaXb%2F6GhAS3%2FgBuF7iELPahrUhA0L6%2BBaGq2ZM5xwDJBdj0Rw%2BWd6M48YgZMuo%2BGEUkpHens1Ayz3Zex8cWuPIFgtDZBhyaN1poia%2Bl65EulUmC2qrttBlwl2xna16w0FVL4SLDWNOiM9xA1EpC96lMh9Pr7gQpukuoH6NWZDjrSsvXymqBW6jNky8BteMlMz2BBduVD7HbhkFIN2Miosb%2F5NCDBh%2FjBdaZG71p39EwbNkEr4jP7993cswPM9A%2BRSOKJdj6%2FDzlnGDXE3OdhY1SjM347Kag9%2BVRtN89CBncg54uTgcRJgqC0tMokduvrh9sKJE7rEKYqn%2BotnjacFQBejihlg6ZFYZs2D90ZDd4nNRIeTXR5RQk9WMBL3sV1FP8TJTk7jhyEMqsIIM%2BMK7vl70GOqUBPu6O6jj2dM5ik%2FD0pOv1akFD90LqXNn%2FCqdYHwx5J7upAjF0eyT5kP1HE5k8%2BdNdMuevFLoivU6CAj7FScXMFmmsYEYuQ0IF7%2BWdlMeDSiDq295GXMw6QGH6eEytunaMCT%2BRP8v5JnncOYoLLANzD35rKNxpXRaP4Y7mmUXR%2BvAaH%2Fc5aQrIBfnATAJPaK8MIOIfl%2BVCkVouHOCgH4zpAQfpQaEd&X-Amz-Signature=ce1223e6e1bfb2afdfc0d77250979569fbc364e00a920127ff986442ea4a5f17&X-Amz-SignedHeaders=host&x-id=GetObject)
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
