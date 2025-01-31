

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

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/997ac361-58a8-4f04-bb0f-79fea4baa761/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TRREFZ46%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T231315Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEL7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDEVgZFI3QU9dWbTWPkCyRw07Fw2BmPXLC4PRUB9dkgLQIhAKFUTghecbOjyknaTfJVhTVv1hhFdGs0Q6efI3X5J3H9KogECMf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igz8tOlr%2FEUV1uqsFNoq3ANIB4vFdr51%2FkX56FVuN7gHNhMGsHR2Ste0cfv8v15Rh3hG2eDIdOhsgVvZekwMTHNV%2BcE1Gydnrjun15VfvYnpdjD%2BWET6srThyRvtwzUPneg7DXU47JvnN5WC%2FkKLKwlAMqTeZoprytZNhvJMMdDEvotdttksAv%2ByGKAOr1JJ1EZaQ2Vy%2BhN2EZtepr7%2FGUgi32y6aXOpin1d5AY%2F0gDKHnvZuJ7SNJjqwxsyR%2FXydzZC4ldaZ18En1BeqVqyY7BI5X47lNtrOO9lCWLp4WIvNvn1%2FISeDaWv%2FoXyqf9tgf4hvFek4jmVRM2M5jdY4EfW9U7ENqBIuXOjkM2%2BCZsE9JpTKNilaASuOo9OixSZvzvEvwuLSuTa3Bf0hU1JfN6WJdH4YMu4CC5HKjSs4Ht9mFKiDK6C8Uzqk4VnAEze61RI7kCcfkM7Jjejjg19GKdHoZRTbIG0dWNloXwsVvNjDvO5mQ%2Bhm8twhFxD097QGJQ8u6eBWmoiz1%2FQ2G32wfWj7%2FqxzCEzhZrlAkvbfZE%2FxaykzspO2RQRnxkvUijKsC9Ay0KvSeEFbwUM0Y9CJTC7YduJhTJhHRiZ0yZrFLQ0ZyOHYuK7MUV8aNjh4%2F0dnJoPZ6kd3nNKfQy%2FozCDlPW8BjqkAZS5QYbGkmXatiUrRru6Mu2j0rgUF70qSGiGUt7Bv0YyOGf%2FaZiUcohuIPnTaIoqA%2ByeIdrkHC5HOXmveFLwCvFoaiLw8ZxELGegFPLuMrB5kKgFK%2Ba09YW2QiyTcfuBAqAmMpLF%2F3ywsliySHpr%2BndAI%2FRjjblJANIDDna8GfjutsrgXrk8jiqcCmtJAirfgJw24Z28eI2ppauPi%2BFVTTHhk0%2By&X-Amz-Signature=b3028b78dee0bb0a8952d65d0982dfdf624827f3e51e45897faaf09692562fe6&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Data Visualization Libraries
#### 1. **Matplotlib**
- **Description:** The most well-known library for data visualization.
- **Features:** Great for making highly customizable graphs and plots.
#### 2. **Seaborn**
- **Description:** A high-level visualization library based on Matplotlib.
- **Features:** Easy to generate various plots like heat maps, time series, and violin plots.

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/733d1e42-5a53-4fd8-90c1-3d85254369a6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665QLFHXNA%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T231314Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEL7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAHMmbFpJMLJBzsLleNY2vJHrpJBU7r7vyGJIuE%2FLdCOAiEA0chPjM1o%2FO1uIc25yh56PQCGrZv5Z2xivvt7m1DyrQIqiAQIx%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDCbag4JMEJqTyv0qpCrcA2PinUqsIFEf50sS7E2AE8AcSLrIhC30vs7jLCgKc3WrnS%2F0ZCG550f5U0bRUtXuh2hL%2BrYUQjT9b4vjOlrvP6qjwg%2F9cZyhxpgiv1XOE2fCoT%2FKOKzY4wWa2XMGOLmRvw6TRVki3KXqUmPr52v%2BFQtWrLTBfoxSDrxEcHGnaryt4pUEgNoGWURl8zyREDLWJYTVSZH2Mwu7QeBK2HqZxeApmY070e8VCEkVMXicqw0Ve1rjhU%2F4O8M38zGN2kYfx5e129cP3U1Ch4QhGpHYRsWdGqg5aB9JEUD0S1nA4GQXi6B4lZCJ5Pt6%2B%2BrSBlEbgcwHZZO1CGS3pzL4f8SPXQXLhm0YDqjo3HNDouIvF9XSBOw4%2BT2KdE0yyBklP%2FoUlesRaHvSrWtLuBF7dR0tMz3h1nJo98Uov5orGPbF88ymW7RKAACQczw8i8kblJnJ75m9aYWd37Yw%2By8NCSbIg8GBEfdQpaybOZaVzViXrPKg5LgjJQTt1REpkoDVoHDviuJt42eHd6B1wOidjXf6tKpXyWnWkl9%2BHrawHAaJIjNisbhzOX6DFpypDa%2F0GSFwK42CTHFRFTk6rpw2PYU8IWNLJoTTmjyS519n2bl5tIroEl8VMBnGRoWusrkPMNKT9bwGOqUBGG%2BYedVkmZTNk%2BqRNqX2VeizjB3hSxSTV%2BTVMC2stlFeRavLNOA%2FvQ8KeQq8EpEZo5a8e6vklBGzgtS0E6bTIY5vfRbs%2BcFgNBZemD8%2Bu1I7OK3mL5PXnc%2F5%2FxRi%2FpDrgAI4YQ1iD3fGIRlSmsldxitnTX4ugyVLv8jwxiVL9aZNK5WeQV3oc%2FZc9f9Thb25bwXUJJMe09XdxUlXWUAz8epUNmwj&X-Amz-Signature=7b25039952f2b9f079a5247e859970afb583acd5de8dde74e61b1ab7abffc3d2&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Algorithmic Libraries
#### 1. **Scikit-learn**
- **Description:** Contains tools for statistical modeling, including regression, classification, clustering, etc.
- **Built on:** NumPy, SciPy, and Matplotlib.
#### 2. **Statsmodels**
- **Description:** A module for exploring data, estimating statistical models, and performing statistical tests.

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c62885f5-417d-4179-834f-d68f8f2bdf39/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665QLFHXNA%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T231314Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEL7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAHMmbFpJMLJBzsLleNY2vJHrpJBU7r7vyGJIuE%2FLdCOAiEA0chPjM1o%2FO1uIc25yh56PQCGrZv5Z2xivvt7m1DyrQIqiAQIx%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDCbag4JMEJqTyv0qpCrcA2PinUqsIFEf50sS7E2AE8AcSLrIhC30vs7jLCgKc3WrnS%2F0ZCG550f5U0bRUtXuh2hL%2BrYUQjT9b4vjOlrvP6qjwg%2F9cZyhxpgiv1XOE2fCoT%2FKOKzY4wWa2XMGOLmRvw6TRVki3KXqUmPr52v%2BFQtWrLTBfoxSDrxEcHGnaryt4pUEgNoGWURl8zyREDLWJYTVSZH2Mwu7QeBK2HqZxeApmY070e8VCEkVMXicqw0Ve1rjhU%2F4O8M38zGN2kYfx5e129cP3U1Ch4QhGpHYRsWdGqg5aB9JEUD0S1nA4GQXi6B4lZCJ5Pt6%2B%2BrSBlEbgcwHZZO1CGS3pzL4f8SPXQXLhm0YDqjo3HNDouIvF9XSBOw4%2BT2KdE0yyBklP%2FoUlesRaHvSrWtLuBF7dR0tMz3h1nJo98Uov5orGPbF88ymW7RKAACQczw8i8kblJnJ75m9aYWd37Yw%2By8NCSbIg8GBEfdQpaybOZaVzViXrPKg5LgjJQTt1REpkoDVoHDviuJt42eHd6B1wOidjXf6tKpXyWnWkl9%2BHrawHAaJIjNisbhzOX6DFpypDa%2F0GSFwK42CTHFRFTk6rpw2PYU8IWNLJoTTmjyS519n2bl5tIroEl8VMBnGRoWusrkPMNKT9bwGOqUBGG%2BYedVkmZTNk%2BqRNqX2VeizjB3hSxSTV%2BTVMC2stlFeRavLNOA%2FvQ8KeQq8EpEZo5a8e6vklBGzgtS0E6bTIY5vfRbs%2BcFgNBZemD8%2Bu1I7OK3mL5PXnc%2F5%2FxRi%2FpDrgAI4YQ1iD3fGIRlSmsldxitnTX4ugyVLv8jwxiVL9aZNK5WeQV3oc%2FZc9f9Thb25bwXUJJMe09XdxUlXWUAz8epUNmwj&X-Amz-Signature=f10092f82273356cb044d98d660c8bf73e4f8fa5b784a3b6b8db4de9cf401f8f&X-Amz-SignedHeaders=host&x-id=GetObject)
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
