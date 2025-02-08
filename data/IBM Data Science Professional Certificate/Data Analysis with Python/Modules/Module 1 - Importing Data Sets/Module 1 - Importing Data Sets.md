

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

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/997ac361-58a8-4f04-bb0f-79fea4baa761/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XZZ5VXZS%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T051318Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGwaCXVzLXdlc3QtMiJGMEQCIBJj2gY0GNcGgY6OVklKR4cas9eW7StF4yRJl98ytPriAiATHX8sauZEPcUCoqeny4wo2C4H%2BbGkaBtPTigHiX6jkCqIBAiF%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMvfpfyGQYwDfI5kngKtwD46F5tmR1JmzAeyLDqz3p11DczqVGHlLhLLCcFZq2u8rWA3JTYHE6GMihcBuzWRK5RMQ9rdWaDOltjnLCJsxq5nfFjq7EmQkf0muHMA2QmgTaLLipk86sE8zE4fqWiYNjRWcuujPiZlPnqm%2Bn4cw6MPMzK%2FlpS9nml6J9CZjyl%2BURPESKc4NE3g%2BwxhW5pU0xVq7ZOvVcAy1FeWO7EysNZVBNei2JiGsdZXXUPMbkHQDhA7D5jQtTUe8H7saIcO6lUazx7y54wjQ7uZ0v9o%2FgERMzFmwvtmWNVtnIdpzlGOqRHJPOL0gANLU3H3FFQx1tiqxZ6VXYrlYR6M70BUrbS34W6SAZgcpDil7OGuue9AnAFxzMaq9AIaG3nFFlKDxWJBWyjvdKuph6CEdNvuNOHIfwc3CWY6Vf%2B01sTF5oewVU26UjXv%2FNmSmoQ9Q%2FknekwXd8BzwVJ8R2a6WB4ddVWcvMJKW2%2BVFoY2r8if0209BUU7Z9dkU8CfBxaT%2FZcIg2EOBiamSzxP3bOk1rJHOsAN6C9wkobo2ipPuKAXv5i1nGcc%2BVvwR33WpvEL1XusRxPs40mdNZtuLXnKzjTcdHQ3dEM5GWJDxErrG5ibDgRFDXyv5Bg8H1qOhsaqcwjbObvQY6pgHDdP54zR17VqB4up8cgD%2FYocj%2Fz2INZePzPjihbaheth4LXl4QZRECSg7TvEsCVF1DrrL4NMWc1%2FJzdA5QOPXSHY3Q2u1fpzWMMSbHec2v2mmuKPG%2FOnMLRuGDAJJuTtwGqsR%2F1TcGJrOliSd5aQVxs%2FLPjL975L%2Fb%2BgX3RSnTRyAPXzVyTEnfycOZ64NGpdO%2F62HjsrUw3iyPRJ03XiOvC%2FRf0Ee4&X-Amz-Signature=58a22686e16f1ab0f9ff4dc32474d7c10347c23131f727430b63896cbd87f687&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Data Visualization Libraries
#### 1. **Matplotlib**
- **Description:** The most well-known library for data visualization.
- **Features:** Great for making highly customizable graphs and plots.
#### 2. **Seaborn**
- **Description:** A high-level visualization library based on Matplotlib.
- **Features:** Easy to generate various plots like heat maps, time series, and violin plots.

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/733d1e42-5a53-4fd8-90c1-3d85254369a6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667BTAI22O%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T051317Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGwaCXVzLXdlc3QtMiJHMEUCIQCnP9%2FGyvt5lmD%2BQpa4lcOh%2BUFxFCV9gdCJAEyXSnAAHgIgJJIDh6ilL%2F8tdnonXMUuay9i7NnSIvNwUPCZ%2Fy%2B0hzoqiAQIhf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDIJFbmgwGYaiHfVGOircA2I4mONyGKs6iQHCoF8gofEif0WjsIXzGTaCY4BI1MiZCeN71g8Gve5hirmQULwq296ON6NHxxA5NsHzA1%2BHoKSIpouuUFqQHK1Mkdbiv2TmAPhMbNL6UBHz0G0j1bWk9zqJCHEfS6BFBAYr08AC4x5FiNjM5%2BqdL0qHt6VcELqF4OfSttgT25c3KMidWifrSE30OU4eMl6bR1SYcAy07%2B81fS1QDGNKjh50zCH3UKtZCsotu%2BjQ5G%2FnNJHPmUjJpa0DCkCifzw8k4xZ1bwSIWCdNB2t2Yvx2sKl20o%2FtsaHDvcBcb3wYfZtY8AlABkJrUYRTQD%2BgoDH8dvhscg4OkJSvZgu0ndsYOX%2BB%2FJ2FiiKxWJB4%2BaxIhXII1mu5l4aPrVXrV3t%2Fx3KX9pqViDYlNew%2Fu4HIzzHEhRp8l15Zk3wYa2A5V88APwfG25Mza%2Bd%2F%2F%2BM%2Bvd1fBmOBW4itLMnFiHaulNaNpze5kJivoDHdAZI6oae4WYKEKehB4Koe4eNA77EVJE9y9y4bTEbpzFaG8scT3NnVOMX8Ds4VwcOr%2FxtqbCMAF1YVvsBeDv6qfWJDFUcDo0IaPhroDELK9StssqnEqpPh6k7tvenbaw65exQ%2BCsEA0MSvEPgUMnKMPGym70GOqUB9Uivm3uUgGd9A7PVS%2BKxkbpYsWrJDa2SlvBVdo1vm7oD%2F3XpUbFJ26YlLYcGJ%2BTtEYbz2bMXxodCmbWPlIHJCdMoXue4M7PFG0Put3IURUtxCzdZbfKmR5VLYMwzjqR44uqeRiWu%2BAKAXAzRNEpJOt28J%2FzgBUlcqStNb8F%2Bbryvnv0zbQsj6ZF5C3lIVOFCzAYBweWPvHQe5ND%2F%2FxnWXUwqUeVi&X-Amz-Signature=d955120f9179963fdb94d197a2bf43da6bb3b2ecd193268e2157b2cdf73b2387&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Algorithmic Libraries
#### 1. **Scikit-learn**
- **Description:** Contains tools for statistical modeling, including regression, classification, clustering, etc.
- **Built on:** NumPy, SciPy, and Matplotlib.
#### 2. **Statsmodels**
- **Description:** A module for exploring data, estimating statistical models, and performing statistical tests.

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c62885f5-417d-4179-834f-d68f8f2bdf39/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667BTAI22O%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T051317Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGwaCXVzLXdlc3QtMiJHMEUCIQCnP9%2FGyvt5lmD%2BQpa4lcOh%2BUFxFCV9gdCJAEyXSnAAHgIgJJIDh6ilL%2F8tdnonXMUuay9i7NnSIvNwUPCZ%2Fy%2B0hzoqiAQIhf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDIJFbmgwGYaiHfVGOircA2I4mONyGKs6iQHCoF8gofEif0WjsIXzGTaCY4BI1MiZCeN71g8Gve5hirmQULwq296ON6NHxxA5NsHzA1%2BHoKSIpouuUFqQHK1Mkdbiv2TmAPhMbNL6UBHz0G0j1bWk9zqJCHEfS6BFBAYr08AC4x5FiNjM5%2BqdL0qHt6VcELqF4OfSttgT25c3KMidWifrSE30OU4eMl6bR1SYcAy07%2B81fS1QDGNKjh50zCH3UKtZCsotu%2BjQ5G%2FnNJHPmUjJpa0DCkCifzw8k4xZ1bwSIWCdNB2t2Yvx2sKl20o%2FtsaHDvcBcb3wYfZtY8AlABkJrUYRTQD%2BgoDH8dvhscg4OkJSvZgu0ndsYOX%2BB%2FJ2FiiKxWJB4%2BaxIhXII1mu5l4aPrVXrV3t%2Fx3KX9pqViDYlNew%2Fu4HIzzHEhRp8l15Zk3wYa2A5V88APwfG25Mza%2Bd%2F%2F%2BM%2Bvd1fBmOBW4itLMnFiHaulNaNpze5kJivoDHdAZI6oae4WYKEKehB4Koe4eNA77EVJE9y9y4bTEbpzFaG8scT3NnVOMX8Ds4VwcOr%2FxtqbCMAF1YVvsBeDv6qfWJDFUcDo0IaPhroDELK9StssqnEqpPh6k7tvenbaw65exQ%2BCsEA0MSvEPgUMnKMPGym70GOqUB9Uivm3uUgGd9A7PVS%2BKxkbpYsWrJDa2SlvBVdo1vm7oD%2F3XpUbFJ26YlLYcGJ%2BTtEYbz2bMXxodCmbWPlIHJCdMoXue4M7PFG0Put3IURUtxCzdZbfKmR5VLYMwzjqR44uqeRiWu%2BAKAXAzRNEpJOt28J%2FzgBUlcqStNb8F%2Bbryvnv0zbQsj6ZF5C3lIVOFCzAYBweWPvHQe5ND%2F%2FxnWXUwqUeVi&X-Amz-Signature=6a838801891205696dab6ddd1510bc612f024cc2683435c570aad47809070254&X-Amz-SignedHeaders=host&x-id=GetObject)
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
