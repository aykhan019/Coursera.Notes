

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

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/997ac361-58a8-4f04-bb0f-79fea4baa761/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664Z24GRL5%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T141406Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFNOWgJhVqZq4Fr9E8inOw3tuSPAkm8elnESmke1aDGBAiAit9MlyJOV3IOxfheAvI%2FrkO4q0hxkAbZ9TJA745%2FlhiqIBAin%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMzvNPGPUIgtF1hpGnKtwDNAET86oqzibBRqu7254jpPPfc%2BhoGxHLxQFr1vNzPhWtvcAP9oWqblCsOMJuK2PPT5WOnWUge85CvTUnCR1l7XDRibB%2FsKmU8hsMcwPVn4XcoaZb6r%2Fa49l63TlP8hHi3RAxKsaeFOnS%2BWiTxKS0dX1iJzPfomZyZfI586kOtHYr9JxhslqyR8QVVkcMUpOsR1v4y%2BPNK7rDpaaf7KS4lQ85OWT79DZVL73dS9DSLWd4WHzx6vgpJjvkRDRr6SkchUYyx97XYAteK6%2BuhYXxEp9tPNTcQkExDpDCGM31M7WgexJ8jH%2FX%2Bcba2F4Gs2Z27g3DoZGVFXRQk3jn6vLd4TtC2S3AqmaJHwBZZtRtS4ejFFGiVatimrvj5wfH7KzkraMGTwt%2BNfjIG1msZA1nTLaikp9WPl9esx1CCpdvkzMklb1LkgZUslYQfyLFw%2F541JzuMaUpVb9k1BbVDqvwhIlfYpqYZoEeUUtQazQm1sLlDjeKkgvFKea9m7x6Cc28O%2FRN22LZdpwEI1q74ynpXcb%2BDO9dGZylD6gDLQn4i1BnEbjL0tA%2BClPA7xAVnH1KVkGvWQNi4%2F80La%2BRNYVfBimcPcdyWMd2rVvTR2mf3aEl3s7AsZT5B1Cy0U0w7PrtvAY6pgG7bdYkLG6V9wA9nzhgYxwrLKlH%2FUiOHomQGjzCt0XWSPrIJeqMirHiCaRPDGmqFYX2SufybM9JipHBwhBDMyCmADRSsYdvlG7GQ%2FsoZ0u%2FalAuDNKCRsc8x2%2Fkwiu9vckVJNwwHJUVseZTe5%2FotJUV0cB7F%2FYqFYSuF%2FzCKIQwqIjKemvdlPLnI4Lgv5UdW99e1yx3WFN8%2F8Pt36d9RwWPt%2BKHdOV8&X-Amz-Signature=a7bbc01767b5df45d4cf45150fd1040e269f0ef6104e7fdac422709a02604284&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Data Visualization Libraries
#### 1. **Matplotlib**
- **Description:** The most well-known library for data visualization.
- **Features:** Great for making highly customizable graphs and plots.
#### 2. **Seaborn**
- **Description:** A high-level visualization library based on Matplotlib.
- **Features:** Easy to generate various plots like heat maps, time series, and violin plots.

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/733d1e42-5a53-4fd8-90c1-3d85254369a6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666SJDNACJ%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T141405Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCyYVMiGi44V2eMTH6yOk1oPPQLrcKHqPBniusjLACdxgIgKRO0Ma3VUCxkP2gVWuGOlbVhu2Qmh%2BYiQPRqI12yo3kqiAQIp%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFWVQgsq9ifvlBblSircAwbExG%2FaDalLhUnC9PMwvHMEbv%2Fa2iSVRjEhZGcgAiZRLOOdNEfcnX%2B%2FZxMxBzacbKb%2FnMqs4RXGBCV9z1bR6nTZZmVrMEgBxtCXQbcBMr9vpmyAiBdUEeEiJeLRQhe1LeMJUrN62ErqmniWKETbo87QMTYcP8F8mL3%2FeMp7jzgL%2FABhuGgw0aw4wu1ti2TiIt9F7SLExO0zcBxrwwpm3UbpH4CcHt3t%2FeTjIDMFosOmxk4UjqWQKuoadtbJEd0h7lYglW6tc3XsBvUVmPb9GIhs4yn38qXwTZ7sNbIYgVXXKZCZJcziQ%2FUkRjG6ZIb%2B47qsTTnSpSqLu%2BDRFM9h2lsXGzdmwKizUjLWJbK4OI%2BG%2Fr4pQuMcxVrdZvSKMxIa0J5L08g6LwCUiT3EOX8p%2BM3Snl%2BEy2efidnRJzJ%2F1b3g5VlxiqekeG%2F9Tgin06Bw2IbLc%2FyaMjY%2BID8anzrWqbyRLAvX25FRfrFehTA9K%2BtzxpfpkUOXZMiiVRDGBxKZstf4JN4z06DBP9s9k4eScAGTkoecoRzUyfh22bnEq473tfdDdgC1cM1YU1ImNd8af9%2BYaKLB43JomsKE1qFMFWuAO9aacImpz%2FjzueYaaXNaCX52Loyooouyj9OrMOr67bwGOqUBDSK3G5BhOyAfGEruhOEaJ4llia%2BWSp2j4GzBOTBVcWvxlEggB%2BAn8Sk2oEm2CRMQPqoJ%2ByaFi0cHvoDngVAsjdwLOOyHH5Vt7uu9Rq43pzMe65vi0Ucf0eyLqc9gEoO3KAwKjwqCBdIAN4SdoHYY87i8hiW0gmdbn86rEEgHHeoyyK6S1E7E5fgGoVq0NvA0BDrgBOmMJut%2BdS0tsUPhB5XNcWDR&X-Amz-Signature=67c48ffe8aecc41ff53645926a83b2563811ca6bca1e160499b8f3e409973f42&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Algorithmic Libraries
#### 1. **Scikit-learn**
- **Description:** Contains tools for statistical modeling, including regression, classification, clustering, etc.
- **Built on:** NumPy, SciPy, and Matplotlib.
#### 2. **Statsmodels**
- **Description:** A module for exploring data, estimating statistical models, and performing statistical tests.

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c62885f5-417d-4179-834f-d68f8f2bdf39/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666SJDNACJ%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T141405Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCyYVMiGi44V2eMTH6yOk1oPPQLrcKHqPBniusjLACdxgIgKRO0Ma3VUCxkP2gVWuGOlbVhu2Qmh%2BYiQPRqI12yo3kqiAQIp%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFWVQgsq9ifvlBblSircAwbExG%2FaDalLhUnC9PMwvHMEbv%2Fa2iSVRjEhZGcgAiZRLOOdNEfcnX%2B%2FZxMxBzacbKb%2FnMqs4RXGBCV9z1bR6nTZZmVrMEgBxtCXQbcBMr9vpmyAiBdUEeEiJeLRQhe1LeMJUrN62ErqmniWKETbo87QMTYcP8F8mL3%2FeMp7jzgL%2FABhuGgw0aw4wu1ti2TiIt9F7SLExO0zcBxrwwpm3UbpH4CcHt3t%2FeTjIDMFosOmxk4UjqWQKuoadtbJEd0h7lYglW6tc3XsBvUVmPb9GIhs4yn38qXwTZ7sNbIYgVXXKZCZJcziQ%2FUkRjG6ZIb%2B47qsTTnSpSqLu%2BDRFM9h2lsXGzdmwKizUjLWJbK4OI%2BG%2Fr4pQuMcxVrdZvSKMxIa0J5L08g6LwCUiT3EOX8p%2BM3Snl%2BEy2efidnRJzJ%2F1b3g5VlxiqekeG%2F9Tgin06Bw2IbLc%2FyaMjY%2BID8anzrWqbyRLAvX25FRfrFehTA9K%2BtzxpfpkUOXZMiiVRDGBxKZstf4JN4z06DBP9s9k4eScAGTkoecoRzUyfh22bnEq473tfdDdgC1cM1YU1ImNd8af9%2BYaKLB43JomsKE1qFMFWuAO9aacImpz%2FjzueYaaXNaCX52Loyooouyj9OrMOr67bwGOqUBDSK3G5BhOyAfGEruhOEaJ4llia%2BWSp2j4GzBOTBVcWvxlEggB%2BAn8Sk2oEm2CRMQPqoJ%2ByaFi0cHvoDngVAsjdwLOOyHH5Vt7uu9Rq43pzMe65vi0Ucf0eyLqc9gEoO3KAwKjwqCBdIAN4SdoHYY87i8hiW0gmdbn86rEEgHHeoyyK6S1E7E5fgGoVq0NvA0BDrgBOmMJut%2BdS0tsUPhB5XNcWDR&X-Amz-Signature=5f9712faa80cf0b50a224e9ca9a4bbf878c61e46bdd1a8b12dbc038abf27fb3c&X-Amz-SignedHeaders=host&x-id=GetObject)
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
