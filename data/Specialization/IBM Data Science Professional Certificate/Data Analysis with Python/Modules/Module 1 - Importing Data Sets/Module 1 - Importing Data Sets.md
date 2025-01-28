

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

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/997ac361-58a8-4f04-bb0f-79fea4baa761/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WY7ZLK3U%2F20250128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250128T231344Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHcaCXVzLXdlc3QtMiJIMEYCIQDv2AKYV9RR2S3XD%2BmsyH09AAiuP3LKWtjtBgVcG3tkRgIhALWO5mlqRh0h9UMm4rS00PzdYJQPoQF4Ao8wFLqVbcF%2FKv8DCH8QABoMNjM3NDIzMTgzODA1IgzaRX7ry%2BwTc7hu0fIq3AOhD8eOf61FYz0Zp8z13dwCOOk00a%2F3ANPESo5IefKEjO83XR57lg3Emc8Lh8KpFIbaWHLCwmdOVYw2aStvGve5UEiumO0Mrffx3PEYFb%2FBImA9FURRHWz%2BQy8tQViN1hdzosGA2HnNYEX90E5Py3opLiLujFSuhCuZFD8C9RdMhLJ19NFmnkW7rTU%2BJ8VA5zY0bGaZXc6XKiHKPf%2ByGfxZkqFabnJqFR3oPLU97Z7dx6JR%2BBX5cdNdtCy296QtXy3CHb%2BaKQLu1w2qtM6Z9t2tYt96RlUsnLaiBcx8azSsvnTxvidYiRJ0EZtOm6LKAv6j99TQsJfnBgsqqenjwkjOk3QVzrh6Cj7Y%2BHYBNxVMPjP98E7q7RJ%2Bur7s8QyyoHtq9ZlPtSwa0aK%2FeY6TbKwz2D4442v7F1LIWuartJWkPvL%2BaEWirP7HKT7uw%2FOE39PggvChsz37f%2F5P%2BS6%2BX%2BneXMJNfuf0kDaB84VdIAaHz4js7aYP3Bujn%2BWq2gIbybmBTXFsZEYScL143Wuex86RreNwf%2FMlhL3fa4TSjVF3PhU5jMFON4VIdDW6HryGbmF5bKcxGC57BkrcmOjpWeRnZ14Auxm9pBdtxRbexKoT9a6DmAUMb%2FhO6VQTcTCiseW8BjqkAaHJiL2ZvwzuQqdPLePS9vgBWOrV%2B6wf6mI6BllhHPAASedk1pqjpEUgKKX%2FNgpfk2Pq2gsDGAXFU10TJMgURxJTf15cyIawCtZXudj9vMQWEFPsmkBTmShws5BnhLdsAuJkl0fHE7lvWG%2FqIx9dlW8D%2FNF%2B6eru%2FvURTljwt2yiC1NZ25nsWyn5%2Bf9%2BTMrwph4uMT5hkvkoEYwLceWYQ2CEAbyK&X-Amz-Signature=e13973f10c7273e64017bca790b0e305d744069efe0640ecfffd78d0103692a5&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Data Visualization Libraries
#### 1. **Matplotlib**
- **Description:** The most well-known library for data visualization.
- **Features:** Great for making highly customizable graphs and plots.
#### 2. **Seaborn**
- **Description:** A high-level visualization library based on Matplotlib.
- **Features:** Easy to generate various plots like heat maps, time series, and violin plots.

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/733d1e42-5a53-4fd8-90c1-3d85254369a6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466U6U3ZJNC%2F20250128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250128T231343Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHcaCXVzLXdlc3QtMiJIMEYCIQDaoDo4wOB5oiu77rO0cG1NpnNTnhCv%2BYbmURdyIKAavwIhAIMIy%2FBIdU%2BjiVk7ldxCejAoZDAb%2F6a0LZZWw9knXVVXKv8DCH8QABoMNjM3NDIzMTgzODA1IgxcFPo1HreOQdFdBtQq3ANtaW0PO7VD5axcclDBr2mri4jrIYYnPB%2FtX2lqschXEqFYD8EATQ5BLE81PZOIsZM%2FIcxAiPGeLqshBeBge%2BXbfzl3fgpkkTWZCDwLxgcIV4JuUBhZpECAaVOPYhEp9VbhAb8grmKt25LQ8B%2BvYNK9dgnERf%2Fo5EuyfA4HanLJ7G0vUuv1GwSIw4SZIM19%2Bz7c%2FGM2YxT7%2FOvFzZVSlXTNIiK5%2BllFnhnFEwncODAxy6ofHkDGgFlpWLJ6WWij6JKkjaIMcc177OYIgkrRtZqwFPop%2BQex3qA6lndSouRAiJ1yXryKk1jHBBYNGTzIELYcFTeoUgpKbhJix2vq63cm%2BGzdBCVzcsT1Ej5GEc1GgINq%2FRI1SXNY%2FssYAbtuM5cmJkhfJYMtP0QzVQvpt8uK7elRqh%2BqTKTkW2B%2BxNsgoVaC1R05pJDkYG9%2FuA3A4NVqYf7cJaMbs%2BTQEr%2F8B49DuJzOpwONczK%2FN1scS6wTDfa2uCH8yr82BK4o8jmxbPUZSm4I9kSa%2BeR4kz6dxCYKd8enpOo5hbXCwX8REx9S9Grok5pMP08hlnS48f%2F3crQbnLja7v6qhaKjjRf9IMedAuGKDUA363CfJWJWPvGfLFzP%2FEyNa3WYx5coFjDQsOW8BjqkAbHfS8rg69%2Fa72EcXWlamyenenTAOXVrvCC4PG%2F8tbNz7FwjtioYNqCjC1XYyjZf2Ifg7hYa25Jj1M%2F8sVWI%2Bl0x%2Bw585t0lKFc%2FUrobJ87CPGmfTbQTvN53ApjQ6r6neXD1FGQ%2F23NQUJTrr58u%2Fm7cMFYI3oJA%2FTmkeX0rtKtePtEY9hpzUtrOwLyeyn%2BeCF1hfE8choOKmUEfyC%2BxvYbWitE5&X-Amz-Signature=f865c60e284f69cb0bdd953d8db9e6801898426f0b9364068af790e21990fa2a&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Algorithmic Libraries
#### 1. **Scikit-learn**
- **Description:** Contains tools for statistical modeling, including regression, classification, clustering, etc.
- **Built on:** NumPy, SciPy, and Matplotlib.
#### 2. **Statsmodels**
- **Description:** A module for exploring data, estimating statistical models, and performing statistical tests.

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c62885f5-417d-4179-834f-d68f8f2bdf39/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466U6U3ZJNC%2F20250128%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250128T231343Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHcaCXVzLXdlc3QtMiJIMEYCIQDaoDo4wOB5oiu77rO0cG1NpnNTnhCv%2BYbmURdyIKAavwIhAIMIy%2FBIdU%2BjiVk7ldxCejAoZDAb%2F6a0LZZWw9knXVVXKv8DCH8QABoMNjM3NDIzMTgzODA1IgxcFPo1HreOQdFdBtQq3ANtaW0PO7VD5axcclDBr2mri4jrIYYnPB%2FtX2lqschXEqFYD8EATQ5BLE81PZOIsZM%2FIcxAiPGeLqshBeBge%2BXbfzl3fgpkkTWZCDwLxgcIV4JuUBhZpECAaVOPYhEp9VbhAb8grmKt25LQ8B%2BvYNK9dgnERf%2Fo5EuyfA4HanLJ7G0vUuv1GwSIw4SZIM19%2Bz7c%2FGM2YxT7%2FOvFzZVSlXTNIiK5%2BllFnhnFEwncODAxy6ofHkDGgFlpWLJ6WWij6JKkjaIMcc177OYIgkrRtZqwFPop%2BQex3qA6lndSouRAiJ1yXryKk1jHBBYNGTzIELYcFTeoUgpKbhJix2vq63cm%2BGzdBCVzcsT1Ej5GEc1GgINq%2FRI1SXNY%2FssYAbtuM5cmJkhfJYMtP0QzVQvpt8uK7elRqh%2BqTKTkW2B%2BxNsgoVaC1R05pJDkYG9%2FuA3A4NVqYf7cJaMbs%2BTQEr%2F8B49DuJzOpwONczK%2FN1scS6wTDfa2uCH8yr82BK4o8jmxbPUZSm4I9kSa%2BeR4kz6dxCYKd8enpOo5hbXCwX8REx9S9Grok5pMP08hlnS48f%2F3crQbnLja7v6qhaKjjRf9IMedAuGKDUA363CfJWJWPvGfLFzP%2FEyNa3WYx5coFjDQsOW8BjqkAbHfS8rg69%2Fa72EcXWlamyenenTAOXVrvCC4PG%2F8tbNz7FwjtioYNqCjC1XYyjZf2Ifg7hYa25Jj1M%2F8sVWI%2Bl0x%2Bw585t0lKFc%2FUrobJ87CPGmfTbQTvN53ApjQ6r6neXD1FGQ%2F23NQUJTrr58u%2Fm7cMFYI3oJA%2FTmkeX0rtKtePtEY9hpzUtrOwLyeyn%2BeCF1hfE8choOKmUEfyC%2BxvYbWitE5&X-Amz-Signature=75f786d6662a1ebde26e8ebbd267978dd77335820482bcdaa21bdc62641bc41c&X-Amz-SignedHeaders=host&x-id=GetObject)
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
