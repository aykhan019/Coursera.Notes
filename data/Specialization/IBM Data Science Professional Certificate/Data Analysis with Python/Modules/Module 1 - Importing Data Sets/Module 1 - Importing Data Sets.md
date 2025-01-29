

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

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/997ac361-58a8-4f04-bb0f-79fea4baa761/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QDN7ASHZ%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T111156Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIASKI0wAGFkPkrAN%2FG4lKLmGafmQ7fXdNjv9Dj4KJYNEAiEA1hXkaPTlCreRY8WdxJaA4XDkqmoZzxhvak3hauwMyI4qiAQIi%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDD2rg0k%2FSrM3IZm4zSrcA%2BanVD2mEGKcvylgrXVM%2BhGzyR1%2F4Ca5tBHCes%2BiPxPubjGY8cUhwJ0YaEY4w4QgcHcHq93OXjt37LdVaECunmKMmU1SD5z%2Be7rtcNHrrnivJO2QGox98jMRq2iLcNTXFmn48DOG6Wt2L%2B4eFYD5JGOesULED7R3pnOhxBO6D1i5s9vXzbG0UFcpKzPRinL8cWD6gl4tkmbi05K04N5gLKSEA7ebYilAF3sYk892PbjF64%2FYuQtbLEgbeRGD%2BtsLhNnhUNpOBCwHoymfAKy8B4iZnmLd2sYvSW%2BdtodFe4UzHPNfZw6szNt3%2FkEHbG5yVZ3ct5BkpJOv5TeTPAvhrBN59HMvk6UAGF5vvKBxMTCecsuOxteyFAa84EZZQf3nnRbo1%2B1sXnshQ%2FfazrXqGLgyje6xY%2FYotpaMV68LJk22mKryyv0oAPFL%2BxoLLcsJx1MSz6YPZuf3jkz19qIUQ1lrxA7XDw4yL6rzILWoHhaYrBk4vTQivf8E3yqTDLBQY1PPG0h15nY9PUhrJmQBFQwU%2F4voJP1TCt6Nf0orwJrqg7ovB3qAzg0msD6U54iSvggfiNASMk53ndlqO69hO0i1hNQMeZ%2BtRDNzswOOoHNdIM%2B21HykRaU6zD1vMO3%2B57wGOqUB7uDqVWJBfciDi1Q7dAT7WmilL57lbfFYJz9VL5egbr5UQyWvBwuIVUffjCvr3Bf7lmaeuDXUOFU11PCFrCkrgWoiL9HFk1uhTIemw0l2I8b9nHHcOvhb0fIyIxFjKa8c4FOA4UAiery1y4Z8RA2XWdeJ8swDIiacHBmUX5AYMXQrCOQCl7fH3px1idzAms92d6MJgNpPw8FmNxc%2Fo1CjEjrpeJDJ&X-Amz-Signature=41e578b961f0021345e86be97c864c6886d8f90cea6d5825afd7c82f4058a0a5&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Data Visualization Libraries
#### 1. **Matplotlib**
- **Description:** The most well-known library for data visualization.
- **Features:** Great for making highly customizable graphs and plots.
#### 2. **Seaborn**
- **Description:** A high-level visualization library based on Matplotlib.
- **Features:** Easy to generate various plots like heat maps, time series, and violin plots.

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/733d1e42-5a53-4fd8-90c1-3d85254369a6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YYBQYF5E%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T111155Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIG7GeIJ8rh3g%2FLzWYi0dIlB2t%2Fvpmh8EbYWRtDna5T3QAiEA4dyNIdhs%2FzURHvXqMO%2FrFmW4i08GZXEi5WateTEdhtYqiAQIi%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNBfvjiLs8Wjq0lyMSrcA5WFYz6TeS48WvINgRli3YUMwW2aDgI81tdSN9tFRbUP4SlQA%2BNYLqs37ADtUgFoMRRKBPd%2FlA%2BwNAgBi7so74momsTmNvA0RlEdITs%2F%2BExb%2BA6Jma573mATHIQK1%2BPPuCG01DmZD0jbfETNvWCXGoWM4EMSNzLzs6eFip8Lt%2BmTJQI8XnRR%2FV2cI%2FPriUBEp07puo2pI53nOt%2B8QnhMQnIusK8oH9fRdttl5MVWLw2Mfk6vt8QOJq5Jj8TxFYckf1xEaH1Li1Qh7yJ1iOrcozyvbM83qanM0LUXR%2FXwka8xKJpiyAAq7Z4mGuAuh38cPBMKPWqoT3mdS%2BWzNu8NNmcTLsU9FWYf9ta2W8lPivOhppBHdxpszgmJCRcquyrWY4mdocJC7tpRfkziEWMbeA%2BxW4DNV0RrK%2FgLhlbPLW3yQOm3K5N77htwdHeahcs7SxAN%2BTp3DXBwDkTtBs89jcFiPSnRWB1K3FKe%2FHPzH51TQU7R028flAsI3ek882MkJaVqEVyTe1dbhFklUHvhGE4oguyKTwP4OM4fPTJko1MF6AoXHOFt8c8yGuMd0Oe50WLvtHDUq%2BLIgRRKPuKMCBBgN2AMQlZZxhfLGRy6Ss1sZu612p0FV46zk1aKMO%2F%2B57wGOqUBvW7%2FZp2qxX6xLmQr2gUjpbrYO7GVOzoNS9eGMPqM37TsG90wI5BhnOLaJDZJKxAK%2Fn%2FUyVRcZuFyQ2lJ59suNRLSV3Mf5ebgr%2FvlFHpk%2BkEx%2FUi2uEBT%2FZ1uQvUc2MiF46mSpCROSMrBeHVTTo4Nu0b3kbSob0aQiGsKY%2FFqMTCEldm%2FGB035%2BRSfBGDxaCZUrhUFe%2FBhucs88UACEt59YERc8tN&X-Amz-Signature=8c4f755b04347f4ca633018ba07da64f412f4bdce9d7fa33544d9733695c68c9&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Algorithmic Libraries
#### 1. **Scikit-learn**
- **Description:** Contains tools for statistical modeling, including regression, classification, clustering, etc.
- **Built on:** NumPy, SciPy, and Matplotlib.
#### 2. **Statsmodels**
- **Description:** A module for exploring data, estimating statistical models, and performing statistical tests.

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c62885f5-417d-4179-834f-d68f8f2bdf39/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YYBQYF5E%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T111155Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIG7GeIJ8rh3g%2FLzWYi0dIlB2t%2Fvpmh8EbYWRtDna5T3QAiEA4dyNIdhs%2FzURHvXqMO%2FrFmW4i08GZXEi5WateTEdhtYqiAQIi%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNBfvjiLs8Wjq0lyMSrcA5WFYz6TeS48WvINgRli3YUMwW2aDgI81tdSN9tFRbUP4SlQA%2BNYLqs37ADtUgFoMRRKBPd%2FlA%2BwNAgBi7so74momsTmNvA0RlEdITs%2F%2BExb%2BA6Jma573mATHIQK1%2BPPuCG01DmZD0jbfETNvWCXGoWM4EMSNzLzs6eFip8Lt%2BmTJQI8XnRR%2FV2cI%2FPriUBEp07puo2pI53nOt%2B8QnhMQnIusK8oH9fRdttl5MVWLw2Mfk6vt8QOJq5Jj8TxFYckf1xEaH1Li1Qh7yJ1iOrcozyvbM83qanM0LUXR%2FXwka8xKJpiyAAq7Z4mGuAuh38cPBMKPWqoT3mdS%2BWzNu8NNmcTLsU9FWYf9ta2W8lPivOhppBHdxpszgmJCRcquyrWY4mdocJC7tpRfkziEWMbeA%2BxW4DNV0RrK%2FgLhlbPLW3yQOm3K5N77htwdHeahcs7SxAN%2BTp3DXBwDkTtBs89jcFiPSnRWB1K3FKe%2FHPzH51TQU7R028flAsI3ek882MkJaVqEVyTe1dbhFklUHvhGE4oguyKTwP4OM4fPTJko1MF6AoXHOFt8c8yGuMd0Oe50WLvtHDUq%2BLIgRRKPuKMCBBgN2AMQlZZxhfLGRy6Ss1sZu612p0FV46zk1aKMO%2F%2B57wGOqUBvW7%2FZp2qxX6xLmQr2gUjpbrYO7GVOzoNS9eGMPqM37TsG90wI5BhnOLaJDZJKxAK%2Fn%2FUyVRcZuFyQ2lJ59suNRLSV3Mf5ebgr%2FvlFHpk%2BkEx%2FUi2uEBT%2FZ1uQvUc2MiF46mSpCROSMrBeHVTTo4Nu0b3kbSob0aQiGsKY%2FFqMTCEldm%2FGB035%2BRSfBGDxaCZUrhUFe%2FBhucs88UACEt59YERc8tN&X-Amz-Signature=f49a272d10ff3b37637bf3f6f6d351ab7503c52476fca479ff4c90a76d40f3ec&X-Amz-SignedHeaders=host&x-id=GetObject)
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
