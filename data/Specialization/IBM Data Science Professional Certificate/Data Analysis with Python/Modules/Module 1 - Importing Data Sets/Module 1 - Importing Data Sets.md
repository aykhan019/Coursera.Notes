

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

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/997ac361-58a8-4f04-bb0f-79fea4baa761/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662NGOTUSM%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T181948Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGg5D2IJhNh1iYMJavyw0HfpLHebNe4GQevSlP1RDlpQAiEAxnWiUfni%2FsItOW6c%2FTXmZ3EwjT3qFa5%2FDgC8E8v6mI4qiAQIq%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDM24m0G84mrCb07XbCrcA3rnFUvYPicSeC1Y9QVusXQU7yEHNl1WZsEICJNefJozcfMU9sk0BUo0YOiEo8wYDuutNm0UGvnLvTN3MwALBjfG0fPz6bRcrvK67OYO%2BoBvik%2B1wj8CsWZQKWyLIjNaz5yliMpi%2BG9MrZ4M8aoNX%2FFAL6Q4zCgHYUm4BANVcjXoT%2BxyQ0mxSGiSmzV2eEC2VyOASnA9yEwctfflJNs0EMi94bEqF00iGSE9Q2zgHObRvHT5aD6xgJG%2FWupXWJcnKism%2Bx6EkE6dJdMjqRa5G0J3MXya9XR8fhqUB6iRjBOsCPTJgEmfHWQNn12vlwMAvCBlb7T8ZqVrK4mGeDWExWfow7PFE8Eqb4ndtNYX9e1KNTxFGtKuAV%2BYW3cQHvo3obEarinodvVSubHqJvUx25Laxz818xEpFVI7LnljJIzXgzD772htjPgN8o%2BKltmq9KMp0T%2FEf%2F%2BAtpDbiQzNfFQrLc9VlAqUDl9fRFEMloT4tlii6K5mlRMQLz4xjSegd6i%2F5Goh443%2FYRpFEPURr6IFcbE3kyUPBeGeZvikGI%2BFfFd0fRU6V%2FFKZSyYQu8vDmFAZrHfgFYNH26OyuVPNwTgyRtIYX%2Fp2I%2FTLkcJT293ER0r1L1nkWv5RawzMJjy7rwGOqUBe%2FEFXNxCiGmDrOo%2BiSMkw5ENkyqx9NI9IxZBe4GNtjp58IxMSK%2B8oaXIeKpGJpMcqO4H19RzXiHdG3yWIiF1UbDsjF8oeI3aDxw7B6eN2rvk0wmAJAAGnlgxC%2FYZkEkZPygFEZMLwXeZPsOWA55Oc0hqB37HPKrz0t79BiD2%2FpqYAdWs92k8Dvc1e9DfzrOIE06L10o2WEN%2BiWWHWedOgZTQYUzo&X-Amz-Signature=625fbf7a388744e3aaa5a894391ee770a11cfb0f2ac80f7b5ff60daba902ae66&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Data Visualization Libraries
#### 1. **Matplotlib**
- **Description:** The most well-known library for data visualization.
- **Features:** Great for making highly customizable graphs and plots.
#### 2. **Seaborn**
- **Description:** A high-level visualization library based on Matplotlib.
- **Features:** Easy to generate various plots like heat maps, time series, and violin plots.

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/733d1e42-5a53-4fd8-90c1-3d85254369a6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YED6TGY2%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T181947Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCTGk2XSSSK3DhVRrhUEPOUQTdPaSaeYf2F2RFtB3SDiAIgFpkz0KG8sFVr%2Fb%2Blqem1tQC8T7oCoDOn8jYcPL58NnsqiAQIq%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKI4IqwcHKouMGHPaircAwgiB%2FoUxJE5cRJnVlx%2Frae8Lv%2FYf%2BNBwP1qODf0IWk1MELIKQquJak0kHWA8mIpHoGQ0gZqLezwdUDwnM6V5crXskhjiY1pNZxnj4ngKd%2FG%2FYf2kgH7gcvBSBWic%2BFd4iF1%2FyJlIE9mb0n89E0q8mZRxs2U334BBWDPtNZ%2FTqFrXRK9OyyDsq9vsCFtOFa5%2FlaZDD6uh4IdBsqyBvrF11%2FWHGsi%2FvUn3YshvYE1THw8tr0%2F4ixxJlYdae9kI5zyYQucEcYhi%2FfaTtx%2F4mybZV9%2BCEufyVvhAblcw6M5yIMUzGrKTgWn7b7J%2Fg5DKKDhn5lpv6nHrL5LGBhCaWzymObeegBmHsLlBW0%2BJfl8NC8T8fERSFTILedEUC7nYUGrW4p04ICbI6%2Bd9V30%2Ff7mdnsW%2F9dLpxGHbX4GnSJWuWXnSBUfsvG%2FxEmbMWZd13ziRuorAEeUfE8Xp0m7WiufEOwHyMIm3QNtUee8ZgNYY8ebypwSBW2FjeGfP36U3QXReHu08tUG9iYfBqj7roLN85aT7h5Pa%2B0XktEZyNtR8cfbWn244hJAKo3wqyShao%2FII6JfV2Z8jAhwNDHaNe5F1M4X5YC2yz1jF6Pi0JL%2FMcuqaVZh2us1XgtOvKqGMIvz7rwGOqUBZWuAK8RZ3f1sKVxI5G3f4k8I1xxx%2BiMDdg1JufyuFvqbyiYXbkKp8EQ%2F2%2BuiOy0iSY1rJcOAt%2Bc9w4OxZThYlOYx0qLFbM1nP4BacagdeJ05nsFO9BaYnoXBY7XTh%2BDd9cJcqNgpTrztBLbagZh6fOdQnoD8UglVIEgai7ImtbYzT2tgzu8XyHwF4p%2BTuwy2Wd8NOVMaoC0GD1rjTUDoB2HkhorN&X-Amz-Signature=d7f673d8a412348a29b3af874b0012421e73ce7aa8e5ca779e3a6d7a7c4fc937&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Algorithmic Libraries
#### 1. **Scikit-learn**
- **Description:** Contains tools for statistical modeling, including regression, classification, clustering, etc.
- **Built on:** NumPy, SciPy, and Matplotlib.
#### 2. **Statsmodels**
- **Description:** A module for exploring data, estimating statistical models, and performing statistical tests.

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c62885f5-417d-4179-834f-d68f8f2bdf39/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YED6TGY2%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T181947Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCTGk2XSSSK3DhVRrhUEPOUQTdPaSaeYf2F2RFtB3SDiAIgFpkz0KG8sFVr%2Fb%2Blqem1tQC8T7oCoDOn8jYcPL58NnsqiAQIq%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKI4IqwcHKouMGHPaircAwgiB%2FoUxJE5cRJnVlx%2Frae8Lv%2FYf%2BNBwP1qODf0IWk1MELIKQquJak0kHWA8mIpHoGQ0gZqLezwdUDwnM6V5crXskhjiY1pNZxnj4ngKd%2FG%2FYf2kgH7gcvBSBWic%2BFd4iF1%2FyJlIE9mb0n89E0q8mZRxs2U334BBWDPtNZ%2FTqFrXRK9OyyDsq9vsCFtOFa5%2FlaZDD6uh4IdBsqyBvrF11%2FWHGsi%2FvUn3YshvYE1THw8tr0%2F4ixxJlYdae9kI5zyYQucEcYhi%2FfaTtx%2F4mybZV9%2BCEufyVvhAblcw6M5yIMUzGrKTgWn7b7J%2Fg5DKKDhn5lpv6nHrL5LGBhCaWzymObeegBmHsLlBW0%2BJfl8NC8T8fERSFTILedEUC7nYUGrW4p04ICbI6%2Bd9V30%2Ff7mdnsW%2F9dLpxGHbX4GnSJWuWXnSBUfsvG%2FxEmbMWZd13ziRuorAEeUfE8Xp0m7WiufEOwHyMIm3QNtUee8ZgNYY8ebypwSBW2FjeGfP36U3QXReHu08tUG9iYfBqj7roLN85aT7h5Pa%2B0XktEZyNtR8cfbWn244hJAKo3wqyShao%2FII6JfV2Z8jAhwNDHaNe5F1M4X5YC2yz1jF6Pi0JL%2FMcuqaVZh2us1XgtOvKqGMIvz7rwGOqUBZWuAK8RZ3f1sKVxI5G3f4k8I1xxx%2BiMDdg1JufyuFvqbyiYXbkKp8EQ%2F2%2BuiOy0iSY1rJcOAt%2Bc9w4OxZThYlOYx0qLFbM1nP4BacagdeJ05nsFO9BaYnoXBY7XTh%2BDd9cJcqNgpTrztBLbagZh6fOdQnoD8UglVIEgai7ImtbYzT2tgzu8XyHwF4p%2BTuwy2Wd8NOVMaoC0GD1rjTUDoB2HkhorN&X-Amz-Signature=17ed76d3bb7ae91a53bd519e3b057b83366a6f11462e571d52e66b1b6043c663&X-Amz-SignedHeaders=host&x-id=GetObject)
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
