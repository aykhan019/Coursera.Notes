

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

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/997ac361-58a8-4f04-bb0f-79fea4baa761/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZMQWLIJ6%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T062128Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFYaCXVzLXdlc3QtMiJGMEQCIEfpEMF9cB04i3rJ87creAq1sj0vQoI1aQOn4OVcfdgpAiBS7vbwsJRKxfUyPshNcSqeFUX5kfDSx7WUkvV7evqFjir%2FAwhvEAAaDDYzNzQyMzE4MzgwNSIMQ3PYWrMweC%2Fe9vCKKtwDYIDWr%2BZpI54lpPbiHlFiYK5SKsBKzSgQZhu7xc%2FShl8Ri6i3c2im3ZxtEoOFzeIDs4wTIsAtadCXQVgMxt2yAJeagdUMkqBdToZWVvMBx8SslMNhHwlqnANTBtE11%2FKwQk4dxge5MhOnni1XccBnBi3Zp%2BHChcSIaIHj5WzLE%2FKu2Kv1y04Qhod%2BzGX3cEDM2Gu8n9IJgBb56%2BSNYiJMnWGmnizUL8aKJTzlsfSIIMZj3rVFBoFDv4N8c58aKLaMWvHZrV6Glv1sHFU%2B6w7VEjM6WlShdtK0nVjhFPHhPRfTNhHmROvLmQ3Pw7ckdFe8pHK%2FKIzbiTReSwjgjLNbthjhQAp4yHUrgauJcftYYajC5jJhBYYsE%2BC%2FK4ZNY7udn1CTL0a0lha88Li2lQOJ8lGHggkvJJs7Rl4H9JSLMH%2FB0vbTcoiy3OEENIZlBEW5L7zI9FpqGjuTuQ7KjhPAwbaJAxENA4dOklL4VFvu%2Fo%2FRi%2B6HBsXlSi%2Bjp9TMCegO4HeQO4608uMph4eD3DXdaYNOwirGT5v8rfyUkcm3pMLQhrClDQ6mxIbonrZlASpZhTomS0k86MLDFCSFyCqg5%2FVMR1lxl%2FacTR%2BuHG8gWf1cSc5rflS%2FK90YEoswor%2BWvQY6pgFgX2GWvhDoQsntJpkNmWGSbglALXtP8ao4bLCfAYTIbFAT742JTTxzrdS8Xl72IO77p6JBjyEy0dE8rtwrq8tGuyeYR3S%2FSgRv5zLAfRBguc1oc%2Bs3TbeuUFZpqAhRsIZWKyVdjWBuX3kRB763P%2FarX7ScXlO9JCrkYDWTZ99rLKb%2FVyGkQBYG8wDlP9DXQgeZuZx31rA78Umhxe04Iv8Y1ANZ%2FuMX&X-Amz-Signature=6e03894beb8132694e054c63f895736b598bc722dd3ca6dff6aa9f7cdf96a072&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Data Visualization Libraries
#### 1. **Matplotlib**
- **Description:** The most well-known library for data visualization.
- **Features:** Great for making highly customizable graphs and plots.
#### 2. **Seaborn**
- **Description:** A high-level visualization library based on Matplotlib.
- **Features:** Easy to generate various plots like heat maps, time series, and violin plots.

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/733d1e42-5a53-4fd8-90c1-3d85254369a6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZVS33QJQ%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T062128Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFYaCXVzLXdlc3QtMiJGMEQCIBx2AO3%2B0nCUZsZuIM5DF5a%2Fc48bGLNzHDZqmoGAAI8xAiA42QyIspQEkGygdZ%2BzYRHQC%2Fz9ACoW2KB5c6xUdSPKZir%2FAwhvEAAaDDYzNzQyMzE4MzgwNSIMmdYzYgBhPPVS%2FA%2BYKtwDvz4MBKoY7EaaHb%2F5De3DFWtU8XOqISyREmoPJ77c0YyR0oX3QtvrcFOqEC6ZNev3yqG8CtV9d4Fdo5gicZiQ%2F32ehpGVh3a8wzAPavHjnNf79%2BVQQydQxwSsOsV4YJkvpJQvYFcTxPg%2Bwek%2Bu68aVeGKvn4IJMOVEAtqX8GnAjdCZvjAbPQ2GdYRJ80L1IS138Rm8Rjw4TNrH%2FZcX%2Ba6%2FA19EYw5%2F7sqFIKSXyCEsnaOC9GRk%2FqFtquRWlyBYGOgds%2BTrUIujuGHfqiUMUGHmjahks1qhtOUCwu3r7ui0P%2Ffgo7lEpplPEbSe9C1OjegHXebSxKzesUWuekNrATnVyYfFE3T8SQXEEgBk19IQofRL8s%2B2n2Dbs%2Bh0IlCwv7IeQAJsAB%2FyAaVnpOaG9ZK9B%2By9dTnuVrGChFxwxXgmqyfYtxnK4zSWXYBgE3tCcw9a1bUobIAb4pxDe4aec6beO8Pw0mPon2IzNkrOR%2FPCMbmt2f%2BtDAoujHs7NxrLyydh9Egbm6w3RAmlhh4UoOxP%2FH6e27TT66hxC1tODD5j20am1cjyi1ZeGBb8GLiKZOjXh9MnA%2FAcDJ0KAP78gCvQaX%2FAk2GFpG6O7ZIBTDAVHjv8mkabsRqHQaJdyswrL%2BWvQY6pgHBKHoGHX83fZnh2avbom%2FNiyJUDDOzUff3pudVWAfpNvlao6ZSrbGvRcM%2BBnEGKBmZKb03zREyswkjGwCofx63yrJVD%2F0A3phF0gbfCurk70J8hyQ3qZ7z9bd7bdzgn5kgmPupWe1SDRjBZefKfjUOeDlf5OnN7aicBKD7QiDol9azkSrvHebMCVV%2F2AJ7DMlCe3gbO0Q4KsgUdAT0rTuX1Z7rd0F0&X-Amz-Signature=92126c21a05dde756914b78141110fc42648bfb598f2764a1f2ac2e5e31cdcb7&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Algorithmic Libraries
#### 1. **Scikit-learn**
- **Description:** Contains tools for statistical modeling, including regression, classification, clustering, etc.
- **Built on:** NumPy, SciPy, and Matplotlib.
#### 2. **Statsmodels**
- **Description:** A module for exploring data, estimating statistical models, and performing statistical tests.

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c62885f5-417d-4179-834f-d68f8f2bdf39/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZVS33QJQ%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T062128Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEFYaCXVzLXdlc3QtMiJGMEQCIBx2AO3%2B0nCUZsZuIM5DF5a%2Fc48bGLNzHDZqmoGAAI8xAiA42QyIspQEkGygdZ%2BzYRHQC%2Fz9ACoW2KB5c6xUdSPKZir%2FAwhvEAAaDDYzNzQyMzE4MzgwNSIMmdYzYgBhPPVS%2FA%2BYKtwDvz4MBKoY7EaaHb%2F5De3DFWtU8XOqISyREmoPJ77c0YyR0oX3QtvrcFOqEC6ZNev3yqG8CtV9d4Fdo5gicZiQ%2F32ehpGVh3a8wzAPavHjnNf79%2BVQQydQxwSsOsV4YJkvpJQvYFcTxPg%2Bwek%2Bu68aVeGKvn4IJMOVEAtqX8GnAjdCZvjAbPQ2GdYRJ80L1IS138Rm8Rjw4TNrH%2FZcX%2Ba6%2FA19EYw5%2F7sqFIKSXyCEsnaOC9GRk%2FqFtquRWlyBYGOgds%2BTrUIujuGHfqiUMUGHmjahks1qhtOUCwu3r7ui0P%2Ffgo7lEpplPEbSe9C1OjegHXebSxKzesUWuekNrATnVyYfFE3T8SQXEEgBk19IQofRL8s%2B2n2Dbs%2Bh0IlCwv7IeQAJsAB%2FyAaVnpOaG9ZK9B%2By9dTnuVrGChFxwxXgmqyfYtxnK4zSWXYBgE3tCcw9a1bUobIAb4pxDe4aec6beO8Pw0mPon2IzNkrOR%2FPCMbmt2f%2BtDAoujHs7NxrLyydh9Egbm6w3RAmlhh4UoOxP%2FH6e27TT66hxC1tODD5j20am1cjyi1ZeGBb8GLiKZOjXh9MnA%2FAcDJ0KAP78gCvQaX%2FAk2GFpG6O7ZIBTDAVHjv8mkabsRqHQaJdyswrL%2BWvQY6pgHBKHoGHX83fZnh2avbom%2FNiyJUDDOzUff3pudVWAfpNvlao6ZSrbGvRcM%2BBnEGKBmZKb03zREyswkjGwCofx63yrJVD%2F0A3phF0gbfCurk70J8hyQ3qZ7z9bd7bdzgn5kgmPupWe1SDRjBZefKfjUOeDlf5OnN7aicBKD7QiDol9azkSrvHebMCVV%2F2AJ7DMlCe3gbO0Q4KsgUdAT0rTuX1Z7rd0F0&X-Amz-Signature=33ac5a8b2f7b6b576cd6e0f5d8b768c81639351be1ea93c04f97fa2680eb2ed1&X-Amz-SignedHeaders=host&x-id=GetObject)
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
