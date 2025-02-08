

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

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/997ac361-58a8-4f04-bb0f-79fea4baa761/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QD2XMUXZ%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T071225Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEG8aCXVzLXdlc3QtMiJIMEYCIQCU0miPOJDb2I63%2F9VLfKKob2GNhz4MwqqzCotW7cegrgIhAKo9xgCE5VQsE6jgcGKzvPo0WB7S%2BeSxov%2F1WAsorcOvKogECIf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igy%2BXyA9TISZwU4SoKEq3ANYuH9d2J%2FlwTRQ3FVAoTizKmuWox2smvfMvzLDasnRimVV2tk5iuZzIu9f3Stj0AbCqr%2BWtpKX4LQ4ZTKkMlEMkWWwvsjj7wR6SUrKWfekC9SoUaytJILjNnoXf2P6nUmP6Xm%2BIhmQtcsa0AeHDyq6s95Rjl4BQsH6cDuxMijX5Kx8xCJf38wXcJPEnjntnRrwam5p9c6L%2FBqJ9RUzx2pBzxi2QZ4nhphHHhYR7DlzeiOx3cGiCJ22%2BkQJ0nYVN%2FqI41zc0fE%2ByHthRehjHdjaaR%2BrrpFqcdohEx9WgYpZT%2FQ%2F53dff8yLZwoJu5MUgkHJRtSYsxhdNe%2B7WzqKpUNSCm1yH5w5eZWOLb6tL6B%2B%2BDoFn86IR6eG8O4S9nAxAScPxIciMT2%2B0m7Iv0rLvyxxig70NrbVDWQfDov2fRq0kC4jRy5uwBoa3nkAWdg6CfRAzxy5w%2Bk%2Bj%2FTFjP5zSQhDlclalJFK36iKK0WlurM7f1OSOVaMjBWUBexhme5uq0%2FJAL%2FXECH25XFx80NcSXSMMl77%2B7Qr6IhYkH8o5fmC2kwmpyPOdItemmPg94fYYsgXdIfo4sH7T3gCx4Q63XgGbZ2sgwCOUlZF%2FP5%2BuILqxgAKq2dY2JYI1fgwRjCk75u9BjqkAXCmgxPfeGmE%2BySlMD0PN65MFG08VVWxivug0KxVEBQ5YFag3JL0FL2arB40pfrUyerhmV%2FRpQyny417ApznvkTwPRrLIUTxy1GkrfwqWHEG9vLaPha84TtXJZmmGYf5vxDWJISZrMwzktZYHstetjp46ZxQTSi4EOJ5UDMiZTX5lIS5rSpGGvAo8xAGH%2Bjx2lVBYTkrBkL0oqQs1u9FF60%2FxSMl&X-Amz-Signature=cf7f133e8f0f357a8efeacd3e4007ab4351b85ae8320de5af9be6a61c00ad96f&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Data Visualization Libraries
#### 1. **Matplotlib**
- **Description:** The most well-known library for data visualization.
- **Features:** Great for making highly customizable graphs and plots.
#### 2. **Seaborn**
- **Description:** A high-level visualization library based on Matplotlib.
- **Features:** Easy to generate various plots like heat maps, time series, and violin plots.

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/733d1e42-5a53-4fd8-90c1-3d85254369a6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664PIBRJPX%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T071224Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEG8aCXVzLXdlc3QtMiJFMEMCH3oA9UaRE0VLBGa3v1Us97kgh8OSR5IVQikNjR4uUPICIGDZL4xo4WAjkVob3xxEplkf%2BCVQONPGXw6xzqYyaqEXKogECIf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwzifVy%2Ff4Pf9%2Fj1CUq3APO40CW54lxaDJTXJUu3ZEUjM2wIKqSYL3Usx0qGptC8JzGEPbAX%2FW4%2FqvtZAk8Rm8fJQUeuQTWXLQ5sdazIeH1gsSFDXl0GO5CMbS%2FDz5l5zEjNRnjrSNvokbzaz7HRbsLxVQR7erJAzCYAmBY03esM2bwrVSQc9g4RoEXpk6c1rFHJKbDtkJNf%2FjTtqCQYffJDIfXgaBQukeWup1du8ihqutbyTkMqEgAYGunU5%2Ba6J5CG3HeVz9%2BMtIpcZPGhqQEKqLoR4RsB6bitoBeEdpUZ72xvUtFL86bTmHCC4vmZ1hO1APZbHmxxziYQWLlSNydnAn0BL4oEWtuP5rpm%2BXoXIdOG5wteuwxfbWCfyqfjwZnt7gRuAlV76mdsoRwowyiRj1ID22bCeteoJ0OGIILFwz7C3G8r%2FqMVIHT4%2F2bPQHfNn14QgKvsmPj25BX4NgD6mY%2BOxRx2ns3Lr8ZbO9pPT8mRsKARxQ%2FYac40%2FnYpg0nGc%2FVhJ5gb4GQcsyXf58XVokXqwfzcmMZfQ7YwzVBItMHOpH8i829ONTGFHx1Issf3lp4sW9W3IuaXNrnjoYxlu6AX4hn5d4UxV%2Bnd2%2FBjzf6JFyFGKRdmw0ALdcPG0422Ew5MwnriwYANjCi75u9BjqnAWPoOb%2FInNbbedYfskMZyc3yqJS2NHwRmXkMf7OerptkpbmJE8QSvidPCsmf85qXKTvPW75PwEGoV8VbfMRHPlgODX4C4QuIIewyzIQDaSQWjjJLJUlvMBwoa1mt%2FkZHbZlQw3TXwIuxPR09qCDExFmp0KxNKh5QsZ9dhQJToQ0iHTDfsHoBbc4HCLtEueBITe%2BUd61qt4Ojieny1o2siTC1QlQmUCbu&X-Amz-Signature=4a79293ebd2751d2153bb421cb938dbe72dbea9529058494914ad8682050a2eb&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Algorithmic Libraries
#### 1. **Scikit-learn**
- **Description:** Contains tools for statistical modeling, including regression, classification, clustering, etc.
- **Built on:** NumPy, SciPy, and Matplotlib.
#### 2. **Statsmodels**
- **Description:** A module for exploring data, estimating statistical models, and performing statistical tests.

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c62885f5-417d-4179-834f-d68f8f2bdf39/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664PIBRJPX%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T071224Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEG8aCXVzLXdlc3QtMiJFMEMCH3oA9UaRE0VLBGa3v1Us97kgh8OSR5IVQikNjR4uUPICIGDZL4xo4WAjkVob3xxEplkf%2BCVQONPGXw6xzqYyaqEXKogECIf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwzifVy%2Ff4Pf9%2Fj1CUq3APO40CW54lxaDJTXJUu3ZEUjM2wIKqSYL3Usx0qGptC8JzGEPbAX%2FW4%2FqvtZAk8Rm8fJQUeuQTWXLQ5sdazIeH1gsSFDXl0GO5CMbS%2FDz5l5zEjNRnjrSNvokbzaz7HRbsLxVQR7erJAzCYAmBY03esM2bwrVSQc9g4RoEXpk6c1rFHJKbDtkJNf%2FjTtqCQYffJDIfXgaBQukeWup1du8ihqutbyTkMqEgAYGunU5%2Ba6J5CG3HeVz9%2BMtIpcZPGhqQEKqLoR4RsB6bitoBeEdpUZ72xvUtFL86bTmHCC4vmZ1hO1APZbHmxxziYQWLlSNydnAn0BL4oEWtuP5rpm%2BXoXIdOG5wteuwxfbWCfyqfjwZnt7gRuAlV76mdsoRwowyiRj1ID22bCeteoJ0OGIILFwz7C3G8r%2FqMVIHT4%2F2bPQHfNn14QgKvsmPj25BX4NgD6mY%2BOxRx2ns3Lr8ZbO9pPT8mRsKARxQ%2FYac40%2FnYpg0nGc%2FVhJ5gb4GQcsyXf58XVokXqwfzcmMZfQ7YwzVBItMHOpH8i829ONTGFHx1Issf3lp4sW9W3IuaXNrnjoYxlu6AX4hn5d4UxV%2Bnd2%2FBjzf6JFyFGKRdmw0ALdcPG0422Ew5MwnriwYANjCi75u9BjqnAWPoOb%2FInNbbedYfskMZyc3yqJS2NHwRmXkMf7OerptkpbmJE8QSvidPCsmf85qXKTvPW75PwEGoV8VbfMRHPlgODX4C4QuIIewyzIQDaSQWjjJLJUlvMBwoa1mt%2FkZHbZlQw3TXwIuxPR09qCDExFmp0KxNKh5QsZ9dhQJToQ0iHTDfsHoBbc4HCLtEueBITe%2BUd61qt4Ojieny1o2siTC1QlQmUCbu&X-Amz-Signature=82dbe09c1b2264494e87b449fed7350be0b051c61b42f3e7f05d8298887d5a7d&X-Amz-SignedHeaders=host&x-id=GetObject)
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
