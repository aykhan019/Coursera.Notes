

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

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/997ac361-58a8-4f04-bb0f-79fea4baa761/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WIBPAT3Q%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T181956Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGIaCXVzLXdlc3QtMiJHMEUCIQDct6agPomTecXgonzeG2ZQ897u6UCfss0nbVA%2BaGnJJAIgHB1yrcxf84ovZrJQedGva%2FWw6vYxBucsPg6WT%2BxbqnUq%2FwMIexAAGgw2Mzc0MjMxODM4MDUiDFkX3HwrX8nSR1IjdircAw75HsPlOI95nyNCVP4lDmemESFbBhVJsuyeKngNxFWPsSF3RwyitocdRiQ32008QlgbD5bxCKDAvWPKT1ML11EmsO1tE8RMCWPaZB6OaZtrvzuoZiE1cMnArIVuGgAqJkctyhlqqOgZwL0sIHitdP68hHtwJwBtBGKOnZzLrnZIyFTX3VZRfOuiPMHBNLraO8QYQm6LCSk8Jq%2BEnE0lnoZjR2c%2BdwSGpKdcuVlz4bo1FKlwi%2BK%2FOX7tnBYxFKMyHzO8rZxdFMgLTeMPnVu3Wa%2BsURUSrP8r3h7sqGJSNYL4gaCTP9hJWh86UNIwr28WpUPdfXV3tnDmK5LIdy4mq2Ssc14doqTogRl4oO070gFU2CepAhKPCxSa7G7q1GA%2Bj2NnMQvWId4leEJMCn%2FNHfx%2BicoRL%2FGhkm9o4426DHNVoYLCzn6cHU3hgjsVVPGdzW7bdj2UqTXPmVydDv8O9AsAYYIFTSKHrlHEuYWPLvgSssB04pz6fyYj4C7jgCKatDDV3IUYLZX1BoxhOEjLCLtQYLdB7fxt3Rnf4dnZWjN8p0WZqACkZWoTbGSZOs%2FrUV64Pi4Fev0SsNq1hJ5qwhXnWj7najWfJ8THNhid6AWyjhCloSL9%2Fdy%2BFYnAMKGZmb0GOqUB9aUzF6pm9NRemEtMhkd0mV4%2B9d9GVO3yZScyoRjNAwBZPe%2F9bAKNNBGtiarBZHnoWtIINEU4f2PpvryH1Z9OAEpw7Izb2QXcv6gI43lSuuhKcBTCLL6TynLxn6TH2bzLgTs3h3lx6VdisLTx1Kdw8jPeA%2BWTEsm4x%2FavncM%2BEUMTiA9jVu%2FpDaBv5W5D8dEZCnC0WRDvDaAHlIQODQ0gNg68HE%2FL&X-Amz-Signature=32eb442720b68d4a9e91002085fa3c52389b3c72b14647e1a4fb7bc0bfef4e07&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Data Visualization Libraries
#### 1. **Matplotlib**
- **Description:** The most well-known library for data visualization.
- **Features:** Great for making highly customizable graphs and plots.
#### 2. **Seaborn**
- **Description:** A high-level visualization library based on Matplotlib.
- **Features:** Easy to generate various plots like heat maps, time series, and violin plots.

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/733d1e42-5a53-4fd8-90c1-3d85254369a6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667JORI3YD%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T181955Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGIaCXVzLXdlc3QtMiJIMEYCIQC9EqBiJSxrY3H2Od4hMEHaj8vbWF%2BEPkt75wBPcX9LdwIhAOHOXNAFyjzdOnGajJxHy3knYehac7BobVd2RMvhW8ZdKv8DCHsQABoMNjM3NDIzMTgzODA1Igwz3%2B4W43bOK0%2BKwzMq3AO%2Flc1kRxkwYOXxi0%2FglkaNdL4AGMfQ%2BL9D5GSk7lJRpsycd1cZeICiv7V1IByFs%2FMTk9rUqswWhkygQBpG8Ah%2BMX6txIX%2BGtYgyLXxshuYRdYrkG2KyyRTxQWxS1AUB%2BCA478zYYRfv2gLh75mt7e48IhD5bBgaDQUb9lBt%2BfnAoVboWEJFiTW2VXmP7GfoffPcCSiSzYsUm1qVb8MrXe23beixXBXC0oE%2F%2Be0WWsbOxOXVJAhL8eo5c7tuuAjInr6lGgmbx%2B33X4mUazP8i8jP%2BfLzHcVZ0AhYDWn7tyk6j4%2FpWPHmHvl35%2BmswMW4MT6PkUGeGbMiS4jrxr%2Fs%2BygfANTtWcebcIRnYDz8qJg3bT6lqKmmjXALkHiN0hgPX6N61N2MloSVWlCABQ%2BUStfyUV0rbNiYPLTiQEexbLxrZPkHzo1IZEE1NjK%2Fqqn3nVq25UTpP8XDnoOeNBbgPNp563f0ZXrYDxodmRYtMtH6xpiaSPMJFoptDHwNsJ2KLi4Cd32rOzlnVlo3zFJEMic%2BcUNPsWAdStr9aNo71QacD6fVwUlJZ8kEEzmY5aeULMm3c6c16awqsj3Jb1Hg6LIljZ2vMqoJSNOe%2FY8Z71rsepUzvEtugGgBc25qjC4mZm9BjqkAWlhymHNpCTWxUVxV9weLcTAQXzt65p54p8%2Fi5LIr1N7iVAEHb0PTGuiZiXQmdS72SCzeuk3cETdKClnFcVYyQ3KR9bQwiV2j48yDty8lW9LDVxlHns6sqTElG6%2BY%2FuwP5uNVtfTpxEgGTPtCNh%2FnTV5ebcdn4B1guFFWymq1G9DCUEZtTiURIUryrnzR%2FdTXsXjoPBwrk5GE0QVoPRZ47H1X27Z&X-Amz-Signature=61e44adc9038e216935af6281b332f98848e402129f47523546175b934c4c29c&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Algorithmic Libraries
#### 1. **Scikit-learn**
- **Description:** Contains tools for statistical modeling, including regression, classification, clustering, etc.
- **Built on:** NumPy, SciPy, and Matplotlib.
#### 2. **Statsmodels**
- **Description:** A module for exploring data, estimating statistical models, and performing statistical tests.

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c62885f5-417d-4179-834f-d68f8f2bdf39/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667JORI3YD%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T181955Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGIaCXVzLXdlc3QtMiJIMEYCIQC9EqBiJSxrY3H2Od4hMEHaj8vbWF%2BEPkt75wBPcX9LdwIhAOHOXNAFyjzdOnGajJxHy3knYehac7BobVd2RMvhW8ZdKv8DCHsQABoMNjM3NDIzMTgzODA1Igwz3%2B4W43bOK0%2BKwzMq3AO%2Flc1kRxkwYOXxi0%2FglkaNdL4AGMfQ%2BL9D5GSk7lJRpsycd1cZeICiv7V1IByFs%2FMTk9rUqswWhkygQBpG8Ah%2BMX6txIX%2BGtYgyLXxshuYRdYrkG2KyyRTxQWxS1AUB%2BCA478zYYRfv2gLh75mt7e48IhD5bBgaDQUb9lBt%2BfnAoVboWEJFiTW2VXmP7GfoffPcCSiSzYsUm1qVb8MrXe23beixXBXC0oE%2F%2Be0WWsbOxOXVJAhL8eo5c7tuuAjInr6lGgmbx%2B33X4mUazP8i8jP%2BfLzHcVZ0AhYDWn7tyk6j4%2FpWPHmHvl35%2BmswMW4MT6PkUGeGbMiS4jrxr%2Fs%2BygfANTtWcebcIRnYDz8qJg3bT6lqKmmjXALkHiN0hgPX6N61N2MloSVWlCABQ%2BUStfyUV0rbNiYPLTiQEexbLxrZPkHzo1IZEE1NjK%2Fqqn3nVq25UTpP8XDnoOeNBbgPNp563f0ZXrYDxodmRYtMtH6xpiaSPMJFoptDHwNsJ2KLi4Cd32rOzlnVlo3zFJEMic%2BcUNPsWAdStr9aNo71QacD6fVwUlJZ8kEEzmY5aeULMm3c6c16awqsj3Jb1Hg6LIljZ2vMqoJSNOe%2FY8Z71rsepUzvEtugGgBc25qjC4mZm9BjqkAWlhymHNpCTWxUVxV9weLcTAQXzt65p54p8%2Fi5LIr1N7iVAEHb0PTGuiZiXQmdS72SCzeuk3cETdKClnFcVYyQ3KR9bQwiV2j48yDty8lW9LDVxlHns6sqTElG6%2BY%2FuwP5uNVtfTpxEgGTPtCNh%2FnTV5ebcdn4B1guFFWymq1G9DCUEZtTiURIUryrnzR%2FdTXsXjoPBwrk5GE0QVoPRZ47H1X27Z&X-Amz-Signature=bb0700348177ee26249b41a54af370fc5f2eae40c2a7ff9d6da6f003609d393b&X-Amz-SignedHeaders=host&x-id=GetObject)
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
