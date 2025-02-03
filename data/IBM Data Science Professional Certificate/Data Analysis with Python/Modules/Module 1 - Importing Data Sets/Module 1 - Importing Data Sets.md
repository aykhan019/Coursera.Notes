

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

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/997ac361-58a8-4f04-bb0f-79fea4baa761/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466STZHAKAJ%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T211343Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAUaCXVzLXdlc3QtMiJGMEQCIBgWwiPODHMTOnJWkgCf%2FjSOlqqhuYqpS79CmRTnjbjJAiBYDAmyrAgdSt5q8CwLVFV3rjb4ttPQZK1BWENXh6pMnCr%2FAwgeEAAaDDYzNzQyMzE4MzgwNSIMllrpAQ7oLga%2F3ITTKtwDnVIz4%2BXPD4jAIWdURoFJKCgJkf3MfKS89Mn7avjPChbmgofElifmrXqmzQuPm%2BNgTgYUSzVlkNyIVnb7mU4Qemgtq8oaBzJ02GTq9SGBNZ4K%2FwStD3GlfhFlRhBGfhgy2T%2FoYyhFmQnna8vBHFhvtTuAuvaN%2FFUSbwE1Zoqb%2F1LOfZCj15pNDSqGo55NsWh5ZM3ch8vzTasgZCTp41LR7UaP%2FO34Aq4clxFB%2FQ4v8sS6leUmfLc3vY2xxBvLcFbJ5CRH6EqTHsnZh58sMR75rhVIgXXo%2BYXJou19Pe%2F751jmT74G3rQ%2BuTwa%2FzS9%2BGbpQO6M0nHKVIzSbPZpNGEnoj6pg0d69DeurMpIpPg52Chplxec0uDCpWL16jM8rsDwAZ%2FmEy04rgcxsmXB3%2BH%2FQ0xrYxkOwgcFwW6VHev9RhDvPGgnV%2FN6L9i%2FpDONBeV94wUicTxkQw0ILAI5UIqm5S1irPZkMbCyXBlyfrmQooWHPYqpqZUFuKGi31fhFBv3kJycldifKYh%2BN8VatfKyLsS09pYM%2FuOP7JkeU6x%2FJRRwI7%2FxWf3CPvbtipc4btR28ZeYws6x%2FynPW%2F8tsbn2Ox5durFJIOU397JFkORhF0HjRq2OfDz2cI8sN04wktqEvQY6pgFleQBXwGlNlEt6Uxop8BPzAK3LtPEK9Iuxw5Jkfaa4rec1fccW5AXWUQwY%2BSlQ5YhPHHq54Q7h4OqLKevMlZo7TN3cRgAqXW0rdh6oV9K4JsVTpgD22Hh5B2uYZEnUDl%2BTJIwZkCi6TTJTG4w1Qmw6UwuWR3pFZ51p5z7Gd8WIMvaSuHlR0%2FJFUr1pJNhc0pq69YEnbbe9yZMLYyIPfOtGLB4XISjy&X-Amz-Signature=c1cfc32311736160011d3068947a2477697e208bf84fe72f4f8a69da866f5e93&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Data Visualization Libraries
#### 1. **Matplotlib**
- **Description:** The most well-known library for data visualization.
- **Features:** Great for making highly customizable graphs and plots.
#### 2. **Seaborn**
- **Description:** A high-level visualization library based on Matplotlib.
- **Features:** Easy to generate various plots like heat maps, time series, and violin plots.

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/733d1e42-5a53-4fd8-90c1-3d85254369a6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QMYRKHDQ%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T211342Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAUaCXVzLXdlc3QtMiJGMEQCIAxYb9c0lLWmwOAeelVyOF3Gvt026S1tGoaxIVq2n5vpAiABNG5BAtxEwLq2tc1kRnCyrZe%2BdS2LzsED9X0GU79FYSr%2FAwgeEAAaDDYzNzQyMzE4MzgwNSIMfkcplco72UPFVA3yKtwDUV4kohgciyhzgg%2Fpxc0Y%2FKYrIWXM0NaeRiQWjdCnxsgAHxOoGofZivK%2FC9BnWcX9H26m8G8nYhbRpoZ4K71YcBczNrC%2B1hxw3eKbqgKQQI25JmfL7m1%2FFn741l16%2FgAmtRnOgG6wVU5Wo7il5sYNArmg%2FBHvQnLv1pj0Kk8t2p2G2sr39V6mmzgb306fMWegNZy%2FMduRFwx5zUa8JCLQcvXTEvWxzqJmz413pV0UnAPCa%2BtmDqokOyQLJ%2BLDt%2BCyr%2BnhR7PNS5yA2gfqY2tCEvgYMyh8uUSn%2FSuEbgZgdPUpEmOma6yIOw8aPBUjOMAzDPj%2B%2BbQyxAkGNcKCxovReRN21GkuAwNbOxgjnpDBBJ9z31bPzE%2BnZosAezQNpU63tEGMNyP%2BOW91Duq%2Fg3%2BmKd01lmQF3TLjLRV2202X1H1MA6e7Ipbpwpgn46d2Th%2BgOFfofJGq6ECVRhYHahMS6ddOcQMq6U56wj2e8XVkm64qCLYGMyf6auQvOEjyhkil9TaU9xaqRfMRxLSX5hNq5XxKyi7uiyHXDJPsnKQSrfDTwSS6yzNihn2fKuVfoBXZXCLGl6vYFzor5h5ZwI6uPfbTPHy3oT13dtYiZcPR537IceZck0adfwLCadMw39mEvQY6pgGolndqh6ftxDBjvyae%2FEda0zDB2EiAUTNDR92g6%2BZ2HZ5izPEv1lKNOwUzIDteXHmJZLGr%2BT4kMKVyfTHlBY%2FG5eoKkmrhI%2BZVj3QLjvR2wm3EwnYD6JAqZlHGkErDXeOWwSH1DgOwE8WaWS3h0CZGbWzFDbZmSpZhjnkXehOa4gJCbc0V4mwdU5G9rgpczEYWuMBiAupwtgFQ1ma9YmnLwzB1AcgK&X-Amz-Signature=c91e0023af034ff9c208f7e67732f96f144b0dfe46ce9cc8cb6da53d8c4fe58e&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Algorithmic Libraries
#### 1. **Scikit-learn**
- **Description:** Contains tools for statistical modeling, including regression, classification, clustering, etc.
- **Built on:** NumPy, SciPy, and Matplotlib.
#### 2. **Statsmodels**
- **Description:** A module for exploring data, estimating statistical models, and performing statistical tests.

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c62885f5-417d-4179-834f-d68f8f2bdf39/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QMYRKHDQ%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T211342Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAUaCXVzLXdlc3QtMiJGMEQCIAxYb9c0lLWmwOAeelVyOF3Gvt026S1tGoaxIVq2n5vpAiABNG5BAtxEwLq2tc1kRnCyrZe%2BdS2LzsED9X0GU79FYSr%2FAwgeEAAaDDYzNzQyMzE4MzgwNSIMfkcplco72UPFVA3yKtwDUV4kohgciyhzgg%2Fpxc0Y%2FKYrIWXM0NaeRiQWjdCnxsgAHxOoGofZivK%2FC9BnWcX9H26m8G8nYhbRpoZ4K71YcBczNrC%2B1hxw3eKbqgKQQI25JmfL7m1%2FFn741l16%2FgAmtRnOgG6wVU5Wo7il5sYNArmg%2FBHvQnLv1pj0Kk8t2p2G2sr39V6mmzgb306fMWegNZy%2FMduRFwx5zUa8JCLQcvXTEvWxzqJmz413pV0UnAPCa%2BtmDqokOyQLJ%2BLDt%2BCyr%2BnhR7PNS5yA2gfqY2tCEvgYMyh8uUSn%2FSuEbgZgdPUpEmOma6yIOw8aPBUjOMAzDPj%2B%2BbQyxAkGNcKCxovReRN21GkuAwNbOxgjnpDBBJ9z31bPzE%2BnZosAezQNpU63tEGMNyP%2BOW91Duq%2Fg3%2BmKd01lmQF3TLjLRV2202X1H1MA6e7Ipbpwpgn46d2Th%2BgOFfofJGq6ECVRhYHahMS6ddOcQMq6U56wj2e8XVkm64qCLYGMyf6auQvOEjyhkil9TaU9xaqRfMRxLSX5hNq5XxKyi7uiyHXDJPsnKQSrfDTwSS6yzNihn2fKuVfoBXZXCLGl6vYFzor5h5ZwI6uPfbTPHy3oT13dtYiZcPR537IceZck0adfwLCadMw39mEvQY6pgGolndqh6ftxDBjvyae%2FEda0zDB2EiAUTNDR92g6%2BZ2HZ5izPEv1lKNOwUzIDteXHmJZLGr%2BT4kMKVyfTHlBY%2FG5eoKkmrhI%2BZVj3QLjvR2wm3EwnYD6JAqZlHGkErDXeOWwSH1DgOwE8WaWS3h0CZGbWzFDbZmSpZhjnkXehOa4gJCbc0V4mwdU5G9rgpczEYWuMBiAupwtgFQ1ma9YmnLwzB1AcgK&X-Amz-Signature=1d19333b93ab3cffdf8ce0fb6599308a7d19c90932c135b49add44c5fb329cf1&X-Amz-SignedHeaders=host&x-id=GetObject)
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
