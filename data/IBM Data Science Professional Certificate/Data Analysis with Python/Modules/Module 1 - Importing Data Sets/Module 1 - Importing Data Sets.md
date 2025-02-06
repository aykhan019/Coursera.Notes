

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

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/997ac361-58a8-4f04-bb0f-79fea4baa761/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ROZT4LED%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T182040Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEkaCXVzLXdlc3QtMiJIMEYCIQDaPv5SfRhM%2BJzh414RwpqKAdGrtxr%2F5EUt4EyrXAXg7gIhAN4wAhhHgBW0VNAES1cJxdYHE0skdw9p0QsQrF00A3CuKv8DCGIQABoMNjM3NDIzMTgzODA1IgyZwWLwy3EUFMYxaoEq3AOdPuYEejH8S2xY0mqDKwepDuQjwdTMT%2BP%2F%2FW5bDI5AA1OIs9kN481%2B6mgEah2Ddpbm0JvQRCBceKikCM4BQgB6noby7ZCgD3hqCaqSTlU0cjtmIQTx9mkyoFB%2Fc%2FsV6VlvwrdZl0YtDpaZOAE0kqBg79Q85VsqG%2BNCNJOChNR%2BDvgm2y%2BSBjnlmw8q3VcpJYyIF%2B7WRumyXSyaNbpADNfElRvjY5OK21vp6%2BBFv8kY6xBn1pndZAm9ZnSeqRhYqNTcSfkd6RQlcOvkk1deN8G%2FM6vjarYns%2BQGSlZ%2Fr%2FFa5v89%2B87D9zP36q7LH8hKr22zGwYWTfwNtBN8qcJlZAogsixnibMiIYhnNIlmSFb8IBXXsZQCm31kniKUPqgO6IGC9LaHYucJypJM8IzoSqWhfxdKEfGl8%2FdVCfmr4rouGDAPwFu8TSH1aUKxo0o3U95IEXo8bKhwK9NaNuIZ3LW%2F%2F7JKTrwv3sRh5HCbZTUnv0FIT9ZOyPLOAHEBFtIDKzDKLw2ayQW7dp29rszPKCCneH5Sos7ILsfvoKkqJ4SC%2FO%2FoxE18dN1u6XcEe%2FdLZ94XYTPzcV2pD9TgIcnps9xweNwtgU1prox5e8VSCRGcorieKV23wHwgXAoKADDD0pO9BjqkAZQMac26SFJmoKgnZSzUezgV6NAY9YoTJmIS%2FGomaPYwXiHdWHNd%2FFKwfAcD2LqTvODo%2B4FoT6fmtMnLzwuKUtPqa0bmtEdcxA7%2BVbn01hQz3GAKVaYErfi6OcaLWwPlS05iOQoFainAcoUwYuxbQvZ9PtvEMrNLbDmDEv%2FGHojZy%2FeDzfo4Ot%2FeDevevA0XxwEe2usy0AMPDRujQRYrqhmak1ru&X-Amz-Signature=867b5de3eccfe40a89e71f5b6e7d2ba887776e75a45c6ffdad47f45a3d863656&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Data Visualization Libraries
#### 1. **Matplotlib**
- **Description:** The most well-known library for data visualization.
- **Features:** Great for making highly customizable graphs and plots.
#### 2. **Seaborn**
- **Description:** A high-level visualization library based on Matplotlib.
- **Features:** Easy to generate various plots like heat maps, time series, and violin plots.

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/733d1e42-5a53-4fd8-90c1-3d85254369a6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666ZXPXJKF%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T182039Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEkaCXVzLXdlc3QtMiJIMEYCIQC7StJi6RRlIffowMFARgu2KxoX1drkVG6uQtD%2Bs1XYuQIhAKzYVGG76b%2BAfig4LBgLzg9946%2ByP3neXZYMW62W19f1Kv8DCGIQABoMNjM3NDIzMTgzODA1Igwvfg%2FR8yZqIGH7H1Uq3AM%2FztYbT3WYA9Mqqs1Lq7tOP5Sa3KcoXbGftuhhgczWH50Z2pnU02%2FUaLUeCCi%2Fa9jttgBS4vTbz%2FPvBkwPMk%2FnfDK9K7oyJyUWcm3NkRBoHNfYonJ5bnEUQP1%2B5LmVF7vSysOE1SLqEs10Kp5GetL5dj5KAxXMMQH0Aj2R%2FpqdSDg8U6rHpFiFyXhdkbXgzsByrIjZwh0FqxkSiyh%2FHmCTJDNqf6sH1SLKv3WfDiBD%2FC%2Fym9ekUZMWRnhzOFxFWFNK9EMgG%2BbRvcRE26VOUeQrUXWr1D%2FwsbYYnjeesfJVGfmSudLmxjVN63y42bgPEekoSaMZS4Z8kclr5PqgS92XI6xXrbjfcP3A7tJFTUYETYpedmrJOo0eRtIxSnZAPYuVTm69C6veKMv14GEBll%2FWFVMHj78JFu0EUzkyBxktl3dZ51%2BGPukR9sV94JlrrP8E%2BKJeK%2BDKdVkqprsGeXF%2FL2SVEzR6oJZQ6APb%2FOMGy82fCqrLV0Si7%2FJ9Lsgxa7xF%2F6U4nXRbnahBv2blDx7Samoo4ybQ0wMMRmClGZnxw%2FfKYQrSBFv0YnBzGsp3TvnZe%2Fcti2nZCW87PN60MvgtO29nrB7vU1KEuYPmOxoxIcMIP27SHNTjpvJ8BjDD0pO9BjqkAZXfzgVNHBE6LBg%2B1wmAQdnNvddZBybzWN7kEpXEeNYiivK9oGoOERI%2BQ%2FTVxGWb3m9a4aoRlLBoAwC4dsycCECukCqCxf3WMwl9wWTmlIAT5Ie97%2BTKYAMqc2pkUOrb90z4jj1hHBx28r7Ijn2rKGM8F08WvA8w8Fx3LNA2y2pq4qj5vqPnpNArTYxhPiT2WN2m8M1%2BDPIYwuE5MSfz2CGo4ff5&X-Amz-Signature=d82fc1921181f5115df402c3d5ea82cd6869cd049adbf870dd8ecd5c88fd7abc&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Algorithmic Libraries
#### 1. **Scikit-learn**
- **Description:** Contains tools for statistical modeling, including regression, classification, clustering, etc.
- **Built on:** NumPy, SciPy, and Matplotlib.
#### 2. **Statsmodels**
- **Description:** A module for exploring data, estimating statistical models, and performing statistical tests.

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c62885f5-417d-4179-834f-d68f8f2bdf39/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666ZXPXJKF%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T182039Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEkaCXVzLXdlc3QtMiJIMEYCIQC7StJi6RRlIffowMFARgu2KxoX1drkVG6uQtD%2Bs1XYuQIhAKzYVGG76b%2BAfig4LBgLzg9946%2ByP3neXZYMW62W19f1Kv8DCGIQABoMNjM3NDIzMTgzODA1Igwvfg%2FR8yZqIGH7H1Uq3AM%2FztYbT3WYA9Mqqs1Lq7tOP5Sa3KcoXbGftuhhgczWH50Z2pnU02%2FUaLUeCCi%2Fa9jttgBS4vTbz%2FPvBkwPMk%2FnfDK9K7oyJyUWcm3NkRBoHNfYonJ5bnEUQP1%2B5LmVF7vSysOE1SLqEs10Kp5GetL5dj5KAxXMMQH0Aj2R%2FpqdSDg8U6rHpFiFyXhdkbXgzsByrIjZwh0FqxkSiyh%2FHmCTJDNqf6sH1SLKv3WfDiBD%2FC%2Fym9ekUZMWRnhzOFxFWFNK9EMgG%2BbRvcRE26VOUeQrUXWr1D%2FwsbYYnjeesfJVGfmSudLmxjVN63y42bgPEekoSaMZS4Z8kclr5PqgS92XI6xXrbjfcP3A7tJFTUYETYpedmrJOo0eRtIxSnZAPYuVTm69C6veKMv14GEBll%2FWFVMHj78JFu0EUzkyBxktl3dZ51%2BGPukR9sV94JlrrP8E%2BKJeK%2BDKdVkqprsGeXF%2FL2SVEzR6oJZQ6APb%2FOMGy82fCqrLV0Si7%2FJ9Lsgxa7xF%2F6U4nXRbnahBv2blDx7Samoo4ybQ0wMMRmClGZnxw%2FfKYQrSBFv0YnBzGsp3TvnZe%2Fcti2nZCW87PN60MvgtO29nrB7vU1KEuYPmOxoxIcMIP27SHNTjpvJ8BjDD0pO9BjqkAZXfzgVNHBE6LBg%2B1wmAQdnNvddZBybzWN7kEpXEeNYiivK9oGoOERI%2BQ%2FTVxGWb3m9a4aoRlLBoAwC4dsycCECukCqCxf3WMwl9wWTmlIAT5Ie97%2BTKYAMqc2pkUOrb90z4jj1hHBx28r7Ijn2rKGM8F08WvA8w8Fx3LNA2y2pq4qj5vqPnpNArTYxhPiT2WN2m8M1%2BDPIYwuE5MSfz2CGo4ff5&X-Amz-Signature=3902117105980f20e0da5e074090d31c0be9564e71526eb001254388f3a9beb8&X-Amz-SignedHeaders=host&x-id=GetObject)
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
