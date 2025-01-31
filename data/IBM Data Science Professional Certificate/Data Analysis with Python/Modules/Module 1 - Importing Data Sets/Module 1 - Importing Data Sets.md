

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

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/997ac361-58a8-4f04-bb0f-79fea4baa761/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WSKFHDWF%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T191134Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIG1pZ6DgHfd6ttDBVLN47c2UbjYNeEUiX93MdBPXT9pHAiAeVa3wJxpHJqs%2Blg8Wz7hHvJOa9NxMIb4CkgDohoOG5CqIBAjE%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMSWz12tYmvg2wASqzKtwD0b91CET%2Fcb1LnKWTvAbJpzYuhU%2FXKSQO0YOyhrJcQrE2zCljluI12LBbUtQ8%2F0ttSuBLFCZj%2Bu34m5oQlZb7Bw1dWG51lJ9GL8cPqZIqBV%2F8PZMNfdNwJ%2FJxKO1H8blU4xFdQWlz0%2FMgKnqJkfmBjTIy4cCJUjtFnFPoJe7JvWFEMXfhbMhDH%2B2tehp3VQNuA0F8EMz2d3tfRwHAuZYn8xNwn%2BBnHAsejghVC%2Bii4QKX9Cz6u6bzyvWbYdtJiOoeLJX6Dyza9tAZnO1oz7gChr3OdhpVyOkkAE5hPzgO8Me52LM21W8QPndvV9jVVWk7sbCD3Lb5w4ujW%2BqXPzQXL1y61x%2F6BSAkQthGBtthjS8q1XIpY5X3LJCQ3eA8x%2Fi7iwl94SRpZDsMmOPebrcYvdrcVmsbnAXpRmezWYyeAt0xk0kaSYwkBMYgjJQoZsM0EyjySznu%2BKtWILx7kFlIY2eVxSKtu%2BcoD3gPETREMcq%2BZtsfYGgjtafH1TAj42u6ng9W3VzdxeOq%2FAKvE6sOHhWzHgIFQPUW%2F5q2eeygOk%2F23yrWz%2B67RXGcWlU2GvCVs7oVBpi%2F8IqQE2cKimLZBIfC6ZxwftybZyxSjy3ZBPhIIpxggDuT5wsZWN0wpMD0vAY6pgEy6EzB2i%2BPKb0Tnho08avwfAPO86BhbI5M0USGuhKTxu0QyA1loDS9lcsCIH7xjah5yrr0EisSSKx9VKRsClQyu7TNRLj7Iefo9bG72FHCEuidF5KLQoslCzXKA%2BlGZrFu9bs8pS9uh%2BB3O5QwCrOZEvR6nxOuIdtqXBiUHZB4%2B7HJvqDsbX%2BGeJmdT5x6nwXzskE9YDboZZzc8iMq2PWpVLwzWpiD&X-Amz-Signature=a8936471a8db1c1beed06c3d265933b560f4c752c12209a0b8462c1d14bb66db&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Data Visualization Libraries
#### 1. **Matplotlib**
- **Description:** The most well-known library for data visualization.
- **Features:** Great for making highly customizable graphs and plots.
#### 2. **Seaborn**
- **Description:** A high-level visualization library based on Matplotlib.
- **Features:** Easy to generate various plots like heat maps, time series, and violin plots.

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/733d1e42-5a53-4fd8-90c1-3d85254369a6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663SKUC3SJ%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T191133Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD05vSVPC9G%2BU%2F7m3aa5cF%2FSULJyGYKTyNAepj6CdmBkgIgNxaiXAbkFUNCc1T1ZwIP%2BUdip3WewrPC6Sv%2FauZsmUIqiAQIw%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGw1sGdajXOBzIBKCircA43FnY3KwMzkGLW8kjnYYA%2BZqSf5t3s174VO2iMSNr5%2Fz2mbK8gFhPUrteqQDBxbmtBeZ83E79qEm7rXT%2FXkXmW5d28LWRkkK77QRHiZ1I7T1yJbCo8H1ktwAiOyn5z03uxPW9B%2FWL240F3c64hjCjMlr0Jom7bJete%2BKQz2MNOVt8U42z%2FG%2BZ4TMCBIN3tnbGKJVkEbLTnfm5u5PJDbAun%2BbnaVRaHnZG5wCH2IjxmASq26GIntgt0aT%2BEYROSiZmVkO3OFPo88GmtJW0C8FD%2BRW4Pw54MMwuSHEJSz5W05cF4pJ%2BnnB93S8Jwkf%2FL7dwpW%2FTT8lIuhkXX%2BaQ4R%2FXsFT%2FNa%2BhxuTfCRAgbaIEX3kySd3MjEGVNzpP1TOLyXwkM890YJGQOurMgrPiwzZWwK%2BU5Q0YMSQ2HTsgf1LVh5nOl%2BhDAomvZhYTJ%2Fx4VCcWY1PgYUtwMMRV8jzPU1qpqQlfeUSZNIuDN1zFe7zSVtNCQP6ALSyumShOdj%2FwvNyWM2PRjpoIASwLjPsSTxCUUKxHZ8fshh2yRHqeDe959GIj7S%2BehFYaxhT0jPArb4z8mIT%2FcNp3A9gHY7AIf4Oeg%2BIpi5QGKneXL0tmfUz1AA0RuJBuIxC7cpBW%2BMMPKj9LwGOqUBPWfD5ntUe3mBwHArEuhRUgKTPBztX9u9mfpD3KaNq4g4GLgDD%2BI2S%2FWO1u%2B04sww8sGq7UfkUBJC38ye625yc6W0U7LDngE22N3a4s0kD1KUdOPxgMEajchKerCxU0kIKdsJ%2FtoLubnTzHhE9%2FtrdJE6KwTzgy5L8dB7NHDiQlqywWHNY%2BgWf8XSFRrzSiLxaQ9JqyT9dTLz1lvqrnrbh%2BRgGd0Z&X-Amz-Signature=4aa8233bcb866ac665c836860ee44037571fc7eab53ef7b53aad1014203d1b76&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Algorithmic Libraries
#### 1. **Scikit-learn**
- **Description:** Contains tools for statistical modeling, including regression, classification, clustering, etc.
- **Built on:** NumPy, SciPy, and Matplotlib.
#### 2. **Statsmodels**
- **Description:** A module for exploring data, estimating statistical models, and performing statistical tests.

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c62885f5-417d-4179-834f-d68f8f2bdf39/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663SKUC3SJ%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T191133Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD05vSVPC9G%2BU%2F7m3aa5cF%2FSULJyGYKTyNAepj6CdmBkgIgNxaiXAbkFUNCc1T1ZwIP%2BUdip3WewrPC6Sv%2FauZsmUIqiAQIw%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGw1sGdajXOBzIBKCircA43FnY3KwMzkGLW8kjnYYA%2BZqSf5t3s174VO2iMSNr5%2Fz2mbK8gFhPUrteqQDBxbmtBeZ83E79qEm7rXT%2FXkXmW5d28LWRkkK77QRHiZ1I7T1yJbCo8H1ktwAiOyn5z03uxPW9B%2FWL240F3c64hjCjMlr0Jom7bJete%2BKQz2MNOVt8U42z%2FG%2BZ4TMCBIN3tnbGKJVkEbLTnfm5u5PJDbAun%2BbnaVRaHnZG5wCH2IjxmASq26GIntgt0aT%2BEYROSiZmVkO3OFPo88GmtJW0C8FD%2BRW4Pw54MMwuSHEJSz5W05cF4pJ%2BnnB93S8Jwkf%2FL7dwpW%2FTT8lIuhkXX%2BaQ4R%2FXsFT%2FNa%2BhxuTfCRAgbaIEX3kySd3MjEGVNzpP1TOLyXwkM890YJGQOurMgrPiwzZWwK%2BU5Q0YMSQ2HTsgf1LVh5nOl%2BhDAomvZhYTJ%2Fx4VCcWY1PgYUtwMMRV8jzPU1qpqQlfeUSZNIuDN1zFe7zSVtNCQP6ALSyumShOdj%2FwvNyWM2PRjpoIASwLjPsSTxCUUKxHZ8fshh2yRHqeDe959GIj7S%2BehFYaxhT0jPArb4z8mIT%2FcNp3A9gHY7AIf4Oeg%2BIpi5QGKneXL0tmfUz1AA0RuJBuIxC7cpBW%2BMMPKj9LwGOqUBPWfD5ntUe3mBwHArEuhRUgKTPBztX9u9mfpD3KaNq4g4GLgDD%2BI2S%2FWO1u%2B04sww8sGq7UfkUBJC38ye625yc6W0U7LDngE22N3a4s0kD1KUdOPxgMEajchKerCxU0kIKdsJ%2FtoLubnTzHhE9%2FtrdJE6KwTzgy5L8dB7NHDiQlqywWHNY%2BgWf8XSFRrzSiLxaQ9JqyT9dTLz1lvqrnrbh%2BRgGd0Z&X-Amz-Signature=3add27fe4a63837935637914031337f920049e240265baba52008fb466bcba2c&X-Amz-SignedHeaders=host&x-id=GetObject)
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
