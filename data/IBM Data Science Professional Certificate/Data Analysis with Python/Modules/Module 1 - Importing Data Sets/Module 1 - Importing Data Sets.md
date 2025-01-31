

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

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/997ac361-58a8-4f04-bb0f-79fea4baa761/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667ZIM6OYG%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T122814Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIApzAGUMllZqp8NRHBIeMckCEGjuErqjoU4Q5bvJ8pIQAiEA47kykD4Mt0%2BgbNeojdIxorzrRQ5GRZOWkl%2BoJmsJrF8qiAQIvf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNdc34BW867NuEScpCrcA5%2BR1%2FlM7ZzYNW%2BN6b%2B9%2BhyPVoSZLDUX4VB%2BLPXKcQqnswIULnlBdoKYKVXt1Al4CfJW0VoeurIOS0awLyYUNBvey5m841oOLVJGHOfDzDSi0NKCkza3gq6DCbmMiQDUIjhdYIGKRHAUgbaPE6va4%2B9VNpY7MPUGyyV76DYlzdwUbl2kY%2FEMGEvxGTm9FqcMlbkgX7j%2BD2OMhnxl3WGdS%2BwvWfL3RnAxjPlYnsmrDxozil24NOJTzrJuo27ACWDKVI9kZHTDDpQdcrV5lHU%2F9YKeWPttic%2BvEo5z2sNw9gRNkos2972sokN8ufz94M3WqJuRxGxG5ZUq6NCQmOhkR5p39vASWsWpNvlP2PuBE%2Fd7B1vzLfaGhTPlRRsPWyDjn8pBRP6x%2FfZG59px1dvowN0FYSFrpN1FLtum9xQvNmpoag99yP5oBbpeiTmrNzMTZIGUCQInyXiN%2FNzFiUiQ8mTPWZtcNHpDMQFS02NIjk8JIyVeA%2BU1kP1BrAETj4UDb2CFEvvaTWU%2Bhu1TI%2BUI6noKFdSssUyzs%2FnuS2HfGQorLGzG7rWx2WR6ymZF4bwx94T%2F7xdN9lsatdzwEP4K76qLXMdQI96MG3SeChw6RpKz0oJ3e3pJfMzJkRKTMPrz8rwGOqUBPk0Ut7N0GLLr1iX1dXkvp24gHPUqQr0her%2FN97NIGDTaVoFGoVVn7oG9B%2FVEh9sJq%2Fjdc0unPHApJVYfF3JkFpL0I0h1Tn47xJRDF4WYa%2BlTKXqh65iOPTPWS%2BlusjQ0tKBB4b2Yh66i7TuQtWCOmH%2FmFg8SyswTdYCUWE8CXHmwr9W2IWhhRri%2F0SNnWrQNeLTzTLNEbUD%2Fmo95dTjkC3adu%2FIl&X-Amz-Signature=aa5464f6c1b25d23fe7b7ad6f2d20a880d3f51b89c6fc29bbf092e59dd0cdd5e&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Data Visualization Libraries
#### 1. **Matplotlib**
- **Description:** The most well-known library for data visualization.
- **Features:** Great for making highly customizable graphs and plots.
#### 2. **Seaborn**
- **Description:** A high-level visualization library based on Matplotlib.
- **Features:** Easy to generate various plots like heat maps, time series, and violin plots.

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/733d1e42-5a53-4fd8-90c1-3d85254369a6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466U4GIKUKK%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T122813Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGXDJj3VpHEOJwTq3I5i0LxF%2B257toSK4OnsSEv9Y9ryAiEA9zcgUGHEecr4Xx0Pe1Fl3sTAu2c1x5XJ60KiiKxVVYMqiAQIvf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJY%2FeOk6RE1RAkd6PircA8OBUiT5dadwd66eGOIOUMTmfvyaVG0G7J%2Fn7uiWztb%2Fqj8J0nYZ0ZW3klR%2FC%2BxvwBR0ChpFm3Gq22i%2BgsOYc0e6O5lAAbqJ3dTptj%2BvQh%2FFv9dPyqkCEl7qN1JiJYqmZpFB8%2Fr9yt3kFS6GHD2G6hMoRy8G6s12Gau1wmscGZUTMbLt4gTQB9xC5BRCthI79oijfHWIgb0GFm2Gof54Weyx5EA32uRdy9FJaoclwoQ%2FzCXWqtnzAR0fWIApp%2Bpgd3sh1aaRSe8ww28fv0SFyQKJk6hziaJahciYoiwvwtyWx116%2F9B5mCYsyQ5ykrOvLmWk2qsyuzAd%2FMA7Xkf7ZIlksg3%2FDjtZDHK60jhWwFcZxia6LKTX51GUtfi6%2By9Y%2BE8dnA50l429%2FXexuqH%2B9ZFXHxpFGVrq7nsOvROC80dRTk418iqzCRUB2WHXo%2FIT9M7nMEILM59ST3nOrbAY71ApuGFoBWgsAnvCHtw1ZMF7QVF5OXFafzq3U3OjLlzIIR80D%2BRuNUglA2RODx4rjyel%2FKJvgeURBb4ZtaYH%2B0t3JrQN3INFhgP1W%2Bg6ZyHQq3n7Z9AM73qDRd2ADMmAZtzvPJHyB9VGu2t726pUJGUeqJtSwZlrWXGihIk%2FMJn08rwGOqUBSFvOV5opVe7y50ERzha5Wpq1Zv1RVCQXUtWOybrxw4N9KnCMflEkNBAChN0zCx24CpKvoODTLmY9F7n%2FbCNr%2FZolWkXA6mH8wRrbFkaqEzO%2BCuosat%2BewLUMQN2XfH7AHtF6L7%2FP8IsINvKPL2B2aX8SuQoZ67qfhjduo9DOteC6dqDTeU6mHnCKG3isITiAKkw%2F6vv8xbzrnWEb%2FLJi8g8ffY0z&X-Amz-Signature=b9c79a07ddcbfee14066f9da38d5a2dd23b445dbee93e5462b78cfbf23791c13&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Algorithmic Libraries
#### 1. **Scikit-learn**
- **Description:** Contains tools for statistical modeling, including regression, classification, clustering, etc.
- **Built on:** NumPy, SciPy, and Matplotlib.
#### 2. **Statsmodels**
- **Description:** A module for exploring data, estimating statistical models, and performing statistical tests.

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c62885f5-417d-4179-834f-d68f8f2bdf39/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466U4GIKUKK%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T122813Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGXDJj3VpHEOJwTq3I5i0LxF%2B257toSK4OnsSEv9Y9ryAiEA9zcgUGHEecr4Xx0Pe1Fl3sTAu2c1x5XJ60KiiKxVVYMqiAQIvf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJY%2FeOk6RE1RAkd6PircA8OBUiT5dadwd66eGOIOUMTmfvyaVG0G7J%2Fn7uiWztb%2Fqj8J0nYZ0ZW3klR%2FC%2BxvwBR0ChpFm3Gq22i%2BgsOYc0e6O5lAAbqJ3dTptj%2BvQh%2FFv9dPyqkCEl7qN1JiJYqmZpFB8%2Fr9yt3kFS6GHD2G6hMoRy8G6s12Gau1wmscGZUTMbLt4gTQB9xC5BRCthI79oijfHWIgb0GFm2Gof54Weyx5EA32uRdy9FJaoclwoQ%2FzCXWqtnzAR0fWIApp%2Bpgd3sh1aaRSe8ww28fv0SFyQKJk6hziaJahciYoiwvwtyWx116%2F9B5mCYsyQ5ykrOvLmWk2qsyuzAd%2FMA7Xkf7ZIlksg3%2FDjtZDHK60jhWwFcZxia6LKTX51GUtfi6%2By9Y%2BE8dnA50l429%2FXexuqH%2B9ZFXHxpFGVrq7nsOvROC80dRTk418iqzCRUB2WHXo%2FIT9M7nMEILM59ST3nOrbAY71ApuGFoBWgsAnvCHtw1ZMF7QVF5OXFafzq3U3OjLlzIIR80D%2BRuNUglA2RODx4rjyel%2FKJvgeURBb4ZtaYH%2B0t3JrQN3INFhgP1W%2Bg6ZyHQq3n7Z9AM73qDRd2ADMmAZtzvPJHyB9VGu2t726pUJGUeqJtSwZlrWXGihIk%2FMJn08rwGOqUBSFvOV5opVe7y50ERzha5Wpq1Zv1RVCQXUtWOybrxw4N9KnCMflEkNBAChN0zCx24CpKvoODTLmY9F7n%2FbCNr%2FZolWkXA6mH8wRrbFkaqEzO%2BCuosat%2BewLUMQN2XfH7AHtF6L7%2FP8IsINvKPL2B2aX8SuQoZ67qfhjduo9DOteC6dqDTeU6mHnCKG3isITiAKkw%2F6vv8xbzrnWEb%2FLJi8g8ffY0z&X-Amz-Signature=cc11086d3d949f329a0e7d0118ed80b2175b30eacb149da95993183b9d34badf&X-Amz-SignedHeaders=host&x-id=GetObject)
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
