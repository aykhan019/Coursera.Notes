

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

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/997ac361-58a8-4f04-bb0f-79fea4baa761/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666YKDTB4Z%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T062014Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHsaCXVzLXdlc3QtMiJIMEYCIQCwceqegs0FTLYrKFbaL8f5nC8sRSCTaOqvsP75EzzpVgIhAM%2Fw5gcxjCybK0O4Elaaknm4UBaeYG0ZkPE484U8vrN2KogECIT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzaEQdrAAeqztKCr7Mq3ANmYETc6yOgFkwHb9uEfFyPWZp5lAvF6nKYIhHQDrHhSwBQltiqpY2IjQ%2ByUQl7ZC%2FdFi2cLNZJEdHrUMFgr5697Nuvvove3Fgsqy9JqlSB%2BhkkCoJozaxbDziPVCSBtFmAdsCqtpszwDK6e7vTTg7KFlt3XhKa4m2c%2B5epQaUDcel1Q6IdIrkiBListGfKM4q%2BFhK9dNqG5p8M0cdjCpQjH0Zs4dOyAFIl%2BnyuhSzIx3WiWowurjbTsyviAKFiZZ0SjrqbVxxX6WnotodUEcgCsr55%2BHFPGvhImbtoOi2CsXHLf87jEPdRTq4c61pL%2FB0h43Am7IvXuhLnj8oaW%2F1C4QxtuzJBdEoxGXRV3w9cZXiiHoA%2BXyVNIIIFplKSSfSsWXavzFzJIQBUpS4kBdPqJPdYgyHok7t7r1CJUNbbzKmuhBW979BG6XiKa%2BRiYzqBiVqXfaIr4lW%2F5TbU4uD63VfXP52nzFrjbb3tV7ePgeiwUDb4tGsSOxTSu5y3CnKQcKcxZMYyE6ewzDBeU7jwRAXIa4JNT71ADdip8l5%2FgmmtsLFnVtR%2BivBZYjOBVpRL%2F7FvRk3qIxRowlrNH95NAclnj3rm%2BewrHCayN3Go7pdbVgWrO9Sj%2F3Q%2BTDCYu%2Ba8BjqkAd%2FvkOmYl%2BY%2FMDbOe2dKNqkECt2UdY6anyZ6Fg9J0XGyEQ%2Bi0OJbAQzX%2BptU%2FTnWLP6cIFpWW9OusIz7cYHek%2BargACt965%2B07kn9ZbibZuHSRRwG5J9ysie5%2F4XNYfwhxHqf3mXr82oI9TUWBn4xRx0sPcciU%2Br2P059FvnUE6qkwTK9pA9XMW66UENoF1z6AbZ4wpEUJ1SDQ8FKKqdC0ul4OvP&X-Amz-Signature=677517b613e5406136d4579b94da9c14843ea1a9851ea07c006232966ea1a8c2&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Data Visualization Libraries
#### 1. **Matplotlib**
- **Description:** The most well-known library for data visualization.
- **Features:** Great for making highly customizable graphs and plots.
#### 2. **Seaborn**
- **Description:** A high-level visualization library based on Matplotlib.
- **Features:** Easy to generate various plots like heat maps, time series, and violin plots.

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/733d1e42-5a53-4fd8-90c1-3d85254369a6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UFDLYRU2%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T062011Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEH4aCXVzLXdlc3QtMiJHMEUCIEyIRffebPhPG5%2BBTeF06tdbLBZlFd8l256UoQK%2B2sVfAiEA17gP%2FivLP9K%2FKS7yObGeNynRFBGan3c2Ep8vClj3C38qiAQIh%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDIO9IGW9eVr423ezNCrcAxwb95xHuqUPu0yzET0odOdgOEcBFrwMy64lDvjo8wif6KXmeJws2FSC1cXga2Vw6e%2BMEMe5Tgc0pIV%2FfllFRa9tkG3LGuPlFmf16K4TYr1SwlO%2B%2FI2lpwGALdliA1eH8S7rpWTdYu6p9EqLbFiUWTTlkPrbZV%2BS86PjOS5obsiaThxE5CQYjAqWz3g9J8wXdnpzxhPxDqYJ9egrPUW7GXVZeLHAbeskiiqFpY4MIWxdjhsyHChYbibrIqyoxL%2F46szvGvJ%2B%2F%2B0t3GK%2FWMvpPg7pjlxHmUAFL9a71u%2Bm4ZIFR28q%2BnooO5KTqbL0t0w8IgsbI9A9huSxVo%2F9yk3DjZ83L0%2Fd0BD7ElzPqMsbyaHOHiOcuEOsYYPZAvsH0ZCy61kB1sha4y2WS2osWnWOp5QjMpQDVkX42g4Pi5Yu6Z6MAtRBG9kuQk5Ao5TFaAuNUEbZaUavbQYFHTv959%2F8tXVjRZTRjHBoj7qnF7qMoeHhHcYG4Oq4X0Owvmfmr2iT05pcV7lWWhV15c1YTXVAP%2BbN0uF%2BDS4NWfo%2BmQOzTxM3DnAE%2FC%2BQHcwEji4Jqn012AJgttYhJDOXOnlhrCYiMWFk7rqEc0tkd63IAwuYEfytfM5MXedV7stD7WXEMISQ57wGOqUBxxBWJMWAngQ2mTk78LM53myWznSDM0hpLB0tyxmEINNdZioXik7XxsIOenPYVXZGtnDcQyhf9EWm%2F0fskXLcNub2jkT76aSK0RRqW9aeNUYmqBzJNqN73M62Y8K5ZecDJ6zOiK%2B8XgPGKX1TT9S%2BLqXnFHkSEVs%2BnrS4u3GF1bVOX10X3iiaA7OonOa6cgO7Kz82LpjCveggzNPkArxjsmtcYpQL&X-Amz-Signature=2c129ea30dd8fe2e4b963ed89ea8645329114c0b93b16cfa205b9d30bc81cffc&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Algorithmic Libraries
#### 1. **Scikit-learn**
- **Description:** Contains tools for statistical modeling, including regression, classification, clustering, etc.
- **Built on:** NumPy, SciPy, and Matplotlib.
#### 2. **Statsmodels**
- **Description:** A module for exploring data, estimating statistical models, and performing statistical tests.

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c62885f5-417d-4179-834f-d68f8f2bdf39/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UFDLYRU2%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T062011Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEH4aCXVzLXdlc3QtMiJHMEUCIEyIRffebPhPG5%2BBTeF06tdbLBZlFd8l256UoQK%2B2sVfAiEA17gP%2FivLP9K%2FKS7yObGeNynRFBGan3c2Ep8vClj3C38qiAQIh%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDIO9IGW9eVr423ezNCrcAxwb95xHuqUPu0yzET0odOdgOEcBFrwMy64lDvjo8wif6KXmeJws2FSC1cXga2Vw6e%2BMEMe5Tgc0pIV%2FfllFRa9tkG3LGuPlFmf16K4TYr1SwlO%2B%2FI2lpwGALdliA1eH8S7rpWTdYu6p9EqLbFiUWTTlkPrbZV%2BS86PjOS5obsiaThxE5CQYjAqWz3g9J8wXdnpzxhPxDqYJ9egrPUW7GXVZeLHAbeskiiqFpY4MIWxdjhsyHChYbibrIqyoxL%2F46szvGvJ%2B%2F%2B0t3GK%2FWMvpPg7pjlxHmUAFL9a71u%2Bm4ZIFR28q%2BnooO5KTqbL0t0w8IgsbI9A9huSxVo%2F9yk3DjZ83L0%2Fd0BD7ElzPqMsbyaHOHiOcuEOsYYPZAvsH0ZCy61kB1sha4y2WS2osWnWOp5QjMpQDVkX42g4Pi5Yu6Z6MAtRBG9kuQk5Ao5TFaAuNUEbZaUavbQYFHTv959%2F8tXVjRZTRjHBoj7qnF7qMoeHhHcYG4Oq4X0Owvmfmr2iT05pcV7lWWhV15c1YTXVAP%2BbN0uF%2BDS4NWfo%2BmQOzTxM3DnAE%2FC%2BQHcwEji4Jqn012AJgttYhJDOXOnlhrCYiMWFk7rqEc0tkd63IAwuYEfytfM5MXedV7stD7WXEMISQ57wGOqUBxxBWJMWAngQ2mTk78LM53myWznSDM0hpLB0tyxmEINNdZioXik7XxsIOenPYVXZGtnDcQyhf9EWm%2F0fskXLcNub2jkT76aSK0RRqW9aeNUYmqBzJNqN73M62Y8K5ZecDJ6zOiK%2B8XgPGKX1TT9S%2BLqXnFHkSEVs%2BnrS4u3GF1bVOX10X3iiaA7OonOa6cgO7Kz82LpjCveggzNPkArxjsmtcYpQL&X-Amz-Signature=c3cd2449549f45b6303ca601024f754f2ff01a4efb1585f2d74579acf4715167&X-Amz-SignedHeaders=host&x-id=GetObject)
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
