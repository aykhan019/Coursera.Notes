

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

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/997ac361-58a8-4f04-bb0f-79fea4baa761/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466USGLGDB4%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T191126Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDMTK%2BgWv96OLEwy7SJzwOE2gs92h8pgVr854xTjPc3OAiEAvWyMMT2Nx1YBCsw2PWsL3XdCFJDCS%2BsQIX35fZ3t5%2F8qiAQIrP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLDusUCJvSElu4hvNyrcA8rt0GYp0lvScTzgbJd8NsTXyoRx9sj9LoQIQeGhUMQ8bj1urulPJSE%2FpOp%2B8zkSJ844u14%2B3rPebrVZiDgvNv0qAx6PiQYiMDCRkCIIoNr7h4PuK0CxCQKcy7hKnND07W8Oj5Yh%2BUyglXvEkvBvmpPHdYMM%2FMuTy87Oteprr5E%2FFCVJYbMwLOuFDqB2qzmVHKr649hRKfvN3R3lCMmmuQPX13%2Fr%2BBmpQwU10yG7SgriC%2BIQjSRu7vKAQDccyIWUm3BGbuoweBnulrEc8F%2F9%2FwVQzwIGjc9W778vLrTKNsxa%2Fc8UM2yEmkdvLD%2F0vW01uxzUSQaqS2yj2Hzs%2FrZCEi%2FtaeOGkQffsO0aTHKK5RrJSzM14qOTq38xAUhKJZRTOiiNv05YMR7yvyE2aCdkEbCbkPTHW7%2BpbAntBv%2FHmtLj1l13INQMPlfCKiQUVzLPv1eJqYWkhnvsFKy58ldHM1ckswgunSlBfZZK%2B%2FF6C9Cw9SPd1OtpLoEfb2V%2FthtHxlEfriCxQ%2FyN8IAhA8uDKCujEeJEoqSTNfihiXcbjMHO0FJ5atMOUzvlQLYdYTUMrKg3hsFJIyra4%2B9HKh7tB4clgApE9%2BLb%2FeO%2Bw%2FTqdnQnQNxLe%2BEKuYBjIu9yMIGO77wGOqUBSCw%2FuxgbjEFJB%2FkCZKNxRsK11rabPj82qP7PSseuQ5Br46R3UVt9qJxPDawWVc3fdWILOzQ5Jijhb82E%2FvbIIE4KpAW%2BbrY45vm5Z9K%2Bj8x%2BEBtpj6AOg4hy2o%2BSs54Jz7bN8mpOX9l%2BvS2n9UjM1BFC8AOjfdwgzJvaiEP0Mk%2BsFPK86lHt6yuS54EOvhzDs3eCUm55zLUe4RfzdyMXjjSM3fGe&X-Amz-Signature=fb67297c8e9ab47f01c7260fb5304298576db2de218f706c698b0a8b8845833b&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Data Visualization Libraries
#### 1. **Matplotlib**
- **Description:** The most well-known library for data visualization.
- **Features:** Great for making highly customizable graphs and plots.
#### 2. **Seaborn**
- **Description:** A high-level visualization library based on Matplotlib.
- **Features:** Easy to generate various plots like heat maps, time series, and violin plots.

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/733d1e42-5a53-4fd8-90c1-3d85254369a6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666IXCLZ5C%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T191125Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDUaNs09O1Eg3HB8RNrQ7irD6KMKYpw%2BXfN9M%2BPcABMTQIgJ8AbuS6DOtTQRTeThpSJMQ9Ux38AmwlPdqNh45aXhQEqiAQIrP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDA5oxjCaYJ8YJ5EgcCrcA%2FV7R5cT0QBMohunrXaACQRVKv3MFnq37P5fHO%2FA%2Fql9y9ChyRbdkv09ynvBpiTPprxRFkfB%2BSgdLG3sezTETqds5A%2BksmC7n9EYx6f1mjmGSQmnU%2F08B%2Fut%2BzXdAPiO6hgowFpDTeV7xAOayTdyuC2aXdwdo5VTGQTvpEFDU1kvuBYfyVACC84nz6WjE7GOkPaQm9hzyIUlE35bEdKyEWJsOyQymThPPqO0bRH62WNdnuoKfSPYGgXbhMq6DD%2BWaLJ9V7xlagnMMQgjeLHNzg7bl8TfNFuxGyOfCg%2BI3GMr42UP0BJfIop92iARuMf5XT8%2FUB1Bl3D3DxFQbyYx5EbfKhINRv64TcGQSSHmRXTvhUfW%2Fd%2FdR4mua9mSzB2etkzRwp9OmSRPIZNzpqmF6EXMCzW9jBPYCWru2aDfaAXzOeRmyZqO8ISE9PX5ogyDd5iD3c8Sk%2FI9aNvpVmw6jcWNeDrwwlDzXjCS7JF%2B%2FF7W6%2BmD4wT85QEy2%2Bkkqur1QtbAYxZKMu3CqZcEeXYuQ%2Br8zhro7kass2%2BTMeRnKQD1Uy7QWLPSknFoqHVq6o8xTUst8b4gsx%2Bb07rKlpmSJuMFon6tgEltqsqE1ia0nm%2BmMvb5yLi8GmOiPiQdMJ2O77wGOqUBCUHpQmsIEgXHI%2BGIYEeVfEoYY98c0qt84f4PgQ5mthn%2BzemO%2Bka3K3gtI9K6R44JY2AMu0T0YbqkSdqiLVDK8zuZMA%2BATkTtAbY%2F9d8mC9QPxFv1XJwgYChzikvNpPqa3iHTJqdNwFBxNMsCPyNtcCh7sQMO0cYwZBue5FoaiCNJmMVlBykm6s6IB27R%2B7AJ2%2BcI%2B1vL6A4ylDnrjVO5PveyQhzC&X-Amz-Signature=40723af34870723c29c46c5b694e5eae085bad21c037a71db3397706a04f8d7f&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Algorithmic Libraries
#### 1. **Scikit-learn**
- **Description:** Contains tools for statistical modeling, including regression, classification, clustering, etc.
- **Built on:** NumPy, SciPy, and Matplotlib.
#### 2. **Statsmodels**
- **Description:** A module for exploring data, estimating statistical models, and performing statistical tests.

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c62885f5-417d-4179-834f-d68f8f2bdf39/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666IXCLZ5C%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T191125Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDUaNs09O1Eg3HB8RNrQ7irD6KMKYpw%2BXfN9M%2BPcABMTQIgJ8AbuS6DOtTQRTeThpSJMQ9Ux38AmwlPdqNh45aXhQEqiAQIrP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDA5oxjCaYJ8YJ5EgcCrcA%2FV7R5cT0QBMohunrXaACQRVKv3MFnq37P5fHO%2FA%2Fql9y9ChyRbdkv09ynvBpiTPprxRFkfB%2BSgdLG3sezTETqds5A%2BksmC7n9EYx6f1mjmGSQmnU%2F08B%2Fut%2BzXdAPiO6hgowFpDTeV7xAOayTdyuC2aXdwdo5VTGQTvpEFDU1kvuBYfyVACC84nz6WjE7GOkPaQm9hzyIUlE35bEdKyEWJsOyQymThPPqO0bRH62WNdnuoKfSPYGgXbhMq6DD%2BWaLJ9V7xlagnMMQgjeLHNzg7bl8TfNFuxGyOfCg%2BI3GMr42UP0BJfIop92iARuMf5XT8%2FUB1Bl3D3DxFQbyYx5EbfKhINRv64TcGQSSHmRXTvhUfW%2Fd%2FdR4mua9mSzB2etkzRwp9OmSRPIZNzpqmF6EXMCzW9jBPYCWru2aDfaAXzOeRmyZqO8ISE9PX5ogyDd5iD3c8Sk%2FI9aNvpVmw6jcWNeDrwwlDzXjCS7JF%2B%2FF7W6%2BmD4wT85QEy2%2Bkkqur1QtbAYxZKMu3CqZcEeXYuQ%2Br8zhro7kass2%2BTMeRnKQD1Uy7QWLPSknFoqHVq6o8xTUst8b4gsx%2Bb07rKlpmSJuMFon6tgEltqsqE1ia0nm%2BmMvb5yLi8GmOiPiQdMJ2O77wGOqUBCUHpQmsIEgXHI%2BGIYEeVfEoYY98c0qt84f4PgQ5mthn%2BzemO%2Bka3K3gtI9K6R44JY2AMu0T0YbqkSdqiLVDK8zuZMA%2BATkTtAbY%2F9d8mC9QPxFv1XJwgYChzikvNpPqa3iHTJqdNwFBxNMsCPyNtcCh7sQMO0cYwZBue5FoaiCNJmMVlBykm6s6IB27R%2B7AJ2%2BcI%2B1vL6A4ylDnrjVO5PveyQhzC&X-Amz-Signature=82cf1ea1856c206b43bfc8b5f34e6483fa8f6988bf70c9b9c11403231b5d73d7&X-Amz-SignedHeaders=host&x-id=GetObject)
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
