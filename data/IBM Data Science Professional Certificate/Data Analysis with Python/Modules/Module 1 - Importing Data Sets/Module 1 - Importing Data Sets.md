

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

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/997ac361-58a8-4f04-bb0f-79fea4baa761/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UGNOQPN4%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T191145Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEsaCXVzLXdlc3QtMiJGMEQCIFmhlw9HB26j%2FZ%2Fi5JuptAMbBZhCDDFh7XphlR6rRwhtAiB9tgc1Z4yRcWsCNr%2BxI6dOqxmdqveOf3EnvWsX%2FkU05Cr%2FAwhjEAAaDDYzNzQyMzE4MzgwNSIMLjo4Y1muu6YCdpDjKtwDI%2Bm4JyjVfMX1QMpmLYwOit6QxN1cwO2%2FRX8N%2F0u0oZj%2BJUyxhtMmeyKMRspMSqM7YY3%2FuR5eSez81WqijM5DyXih3o9z0JJKYPfszvDaupJ5uGo7Ymy%2FCanOTBnAqcO2mgZ%2BUTYcXDWVTsJDc87mihL1Lpa9Hy9O2Z3p%2FX6sD2nzkTFW1EJFrU%2FP8pkHOhCP5fcral6AOh53IwxAiYpKuR8YgDTO%2Bi%2BtqEhwpxCL9I8KS7n8hEduIJNIhlQlBFXhkxZws4PeyA7xJl563X5WEV%2Bml%2BIasBrJ9C0qWrq9HZy6XqXnfvNGDbqzjFyPQofF4GTypx98h13BJbWNq4KL2%2BW%2BPTcho%2B%2BrlOjnH1OpefGUFxuc%2Fkfbb0MGCu7wtXm58auXLNyzIZDRZ6%2FAd%2BDBqY6R83Gqn3d3TuDUtUgv45lkWT3zqVGrIWi7LnVqScRIHR3iK9hgRO879EPLXCoHBofWvLP%2Fxfni4XAKO%2BNPyG9dwF9kSWnkGwb4n9o0XqxI5lTFS7sTKxwMAKDP4T0hGeYGl3SdGbMtiDMB78P9OK7TxaR8kPC9OuNrPL9zUpi%2BbFO1ByoRPftnO7wqyv36jB8tbUQ8xi7RX873XsbUcg5bOaEBaAHjzcBOYd4w6fuTvQY6pgFI1VNq39Bst7ILdnYkcue4l0E4NWh%2BMGBMK1LjC5jnJcyljaXhJ9KK0NAzeWqB4MGX4MAi2Isx0EnAaTz2uhXSZtfx1ehGsFtyBoPArkSYKUoMxppWKrOBQEg4Wfss71gxWCnOwEHLd%2Fpu%2FMWc8OvmxLCTtKC2O2dzhjYJqa9J0%2BRSJaPv6QxfLsR3fL2v%2F1Q6iGolTQKVckItrwd9i7VPM4Zf83Ru&X-Amz-Signature=e94f73dda7e5a517b88632da7360722d735e21c663789c55a191ab5a9ec804d2&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Data Visualization Libraries
#### 1. **Matplotlib**
- **Description:** The most well-known library for data visualization.
- **Features:** Great for making highly customizable graphs and plots.
#### 2. **Seaborn**
- **Description:** A high-level visualization library based on Matplotlib.
- **Features:** Easy to generate various plots like heat maps, time series, and violin plots.

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/733d1e42-5a53-4fd8-90c1-3d85254369a6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XQYINVDF%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T191144Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEsaCXVzLXdlc3QtMiJIMEYCIQCARKSRC2UIXz4GcSwZx7fKdxQWde0aYKBWs1nlJe6ZpwIhAPtWlPhEU%2BK87DFcgkWGnozpmC7AGd%2B5vJPRHGn0WURAKv8DCGMQABoMNjM3NDIzMTgzODA1IgzqXuS0ab6Q7rFuGg8q3AOmrL16SBs9OUqKjZRXmRuRFKKDzgaDAgGWf286oX%2BXJHHStkFheLpRi5ZA2650hN%2BAVBRKKiIMtN3l8Bhae37zPZIBlO15ZH9Bhk5dviPvsoHp%2FwNUrzvbWfb98Lku0xKu0qTBOfwfgJXFSklfwwa2ogc6yLbFqOxU4uNdxbFn78leS6e7kBK%2FQ7zWjoHBQMPHjZswb1wuGKiOU185z3XmBenIFQmOLtS%2FDq334xb7x8SlqQRDwsWoFj23kYz5yVivi7rLrwWQ3PyaOaT49ysyVIiRHtjhyUoeEV05qgHxU56zqMoIn77tsWaspc65yXplAEXjIQWP%2BTD5TDMhUgKhn2Lwq%2FD6s2JEAxwqEsq%2FhxJyGo5%2F9DBlEftlcNYFVtX6lOv%2BpvPbEc5AcEXqUfws8fo7C89JLXXKSiYZ%2Btp8qgJsLqSF91p7zcRR3WchT929LBUos7pX15CMzARqn1AAc15607M1SAa8RlB7kJoCCCEufYBygJZezNUEH5HG8sP83SrJn6rT5W5Kp9AbevQPUrnV4yT3D4fx14TBiVLhi%2BdcF3ZzL8dqsERb2B%2BvR4rYSED4nIMzKL9gVrxKo5b3gX3cCzaoOBAY6itodGMNB8APOW1AQF2e5u2NgjDa%2B5O9BjqkAb6XYJNan%2B1dexyr03ln6IxxB47yXRVw%2ByZbcVDpMnuo0nTwm7GO%2F3dpGNMQyjzmiJ62T6ysV4WDwoeN9dpP1XqlkCLDwYiRav6SlbQSLpP5B3VGfLaKVKh8t8mbBGMh%2FgI6xdFI2QKrU1nYyT4vf6jYeNRha2kQUW3XKF9qlMJFHaQMp94NegF3X5e7VYyxrDLxDyD9WyrcczfMUuONxjG5mojl&X-Amz-Signature=44455aa93f5df90831792f4cc0d5e9f64c1fb5760569d7a5fb3674b0f1a2d34a&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Algorithmic Libraries
#### 1. **Scikit-learn**
- **Description:** Contains tools for statistical modeling, including regression, classification, clustering, etc.
- **Built on:** NumPy, SciPy, and Matplotlib.
#### 2. **Statsmodels**
- **Description:** A module for exploring data, estimating statistical models, and performing statistical tests.

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c62885f5-417d-4179-834f-d68f8f2bdf39/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XQYINVDF%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T191144Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEsaCXVzLXdlc3QtMiJIMEYCIQCARKSRC2UIXz4GcSwZx7fKdxQWde0aYKBWs1nlJe6ZpwIhAPtWlPhEU%2BK87DFcgkWGnozpmC7AGd%2B5vJPRHGn0WURAKv8DCGMQABoMNjM3NDIzMTgzODA1IgzqXuS0ab6Q7rFuGg8q3AOmrL16SBs9OUqKjZRXmRuRFKKDzgaDAgGWf286oX%2BXJHHStkFheLpRi5ZA2650hN%2BAVBRKKiIMtN3l8Bhae37zPZIBlO15ZH9Bhk5dviPvsoHp%2FwNUrzvbWfb98Lku0xKu0qTBOfwfgJXFSklfwwa2ogc6yLbFqOxU4uNdxbFn78leS6e7kBK%2FQ7zWjoHBQMPHjZswb1wuGKiOU185z3XmBenIFQmOLtS%2FDq334xb7x8SlqQRDwsWoFj23kYz5yVivi7rLrwWQ3PyaOaT49ysyVIiRHtjhyUoeEV05qgHxU56zqMoIn77tsWaspc65yXplAEXjIQWP%2BTD5TDMhUgKhn2Lwq%2FD6s2JEAxwqEsq%2FhxJyGo5%2F9DBlEftlcNYFVtX6lOv%2BpvPbEc5AcEXqUfws8fo7C89JLXXKSiYZ%2Btp8qgJsLqSF91p7zcRR3WchT929LBUos7pX15CMzARqn1AAc15607M1SAa8RlB7kJoCCCEufYBygJZezNUEH5HG8sP83SrJn6rT5W5Kp9AbevQPUrnV4yT3D4fx14TBiVLhi%2BdcF3ZzL8dqsERb2B%2BvR4rYSED4nIMzKL9gVrxKo5b3gX3cCzaoOBAY6itodGMNB8APOW1AQF2e5u2NgjDa%2B5O9BjqkAb6XYJNan%2B1dexyr03ln6IxxB47yXRVw%2ByZbcVDpMnuo0nTwm7GO%2F3dpGNMQyjzmiJ62T6ysV4WDwoeN9dpP1XqlkCLDwYiRav6SlbQSLpP5B3VGfLaKVKh8t8mbBGMh%2FgI6xdFI2QKrU1nYyT4vf6jYeNRha2kQUW3XKF9qlMJFHaQMp94NegF3X5e7VYyxrDLxDyD9WyrcczfMUuONxjG5mojl&X-Amz-Signature=7f5c6037f09c9e5a4c7d478de5d273a97c99bb5d7338654d0e8b0c96ddac71c9&X-Amz-SignedHeaders=host&x-id=GetObject)
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
