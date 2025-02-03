

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

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/997ac361-58a8-4f04-bb0f-79fea4baa761/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46676JFKJ4R%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T122915Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQD%2BQ5z1OG2Atyam1W05F39dc120u66PEq3cu7HJruMLAwIhAIEwL41a9iyt%2BDhAmEHHQGV9qk7LjmjEBtwSzHsXMOi%2FKv8DCBUQABoMNjM3NDIzMTgzODA1IgywpINkKEwJLWEr7ekq3AMdztulEa02UHM12L3Shp12lsUeJOKHXZ7pEJ6MTNoEn6J2xh%2B9C2jbHYgdGOiXvvPfLtaJ1xcFrcl9cLuRx1lDVZ%2B6v7c9ZFITgh6JyYF1ZR%2BM7fadVTqFq8BmPUjQp%2BOF0DPk3Y6gItPM%2B%2BnmgZFYep8ANPRqkegIxubtHGK%2BJ%2FlWY%2BAPo2%2BGOhYno3hVjan8S%2FmJUh5qP1CizePTNXFoNb8%2FHwGwfhFsQcPzzGKNsmLA4dEKeLMVtgs9ooC9V9wxhHxWXcDjtgfx%2BDW7TiPQkilAtpVXNUbohwwRSluq1WnbN35zcbIz3nRjKXhtYyUlg4FijYLQL8Vl3cFxZASqgZyuXJFxQ%2FTnqGy58qAkW%2FDF5g49dVZwySBQAdpCd%2FA%2BWE8SOQGOxMc3MvTB0LkJOj699h5QgsxOJX3OIxEoRjp8E0xfLXt3jfYVqoZape5RbQUbfB0XsnWmH1C1hRl5HmDPQg6gn7ga5gfGh0eV5GW1f7DDkRPx6GeUOcebvcknYTTNjBzXnX6WvNHihsPQYHEEzXTYmUpOKo56BPjO2cg%2Bl79LB8FHpAnqeX5XtU0SIdDs%2BBN%2BTgwze9wLdRPw43yjmHoTa6tBvKtWJJmggDFEqMB%2FGJ%2FNkJYn0DDc0oK9BjqkAUeEmUfSlPJob6olDUX9S65TMYWVDlLW%2B0HkwsnHGqUUrwOpSR6bCyiFsp73re9oc3t8wtovdfF0junn6aBJvq1ghhivYBfYG6wXC24873PTZX4EzhIGMceTChyrYbCNULCaCzhggkmo81bRDiUmDPi%2FfLUrE%2Fr2yngncZvdEzpWR7K0lHt7Xt9sVZiXSSnrmJefV5B2cA1rwKNCPHdeJXTN%2FGvs&X-Amz-Signature=af2651801ccaa4ff3abe27d6c76c131b9c83bb8b9e4b910cf93fbfd1ff5195bb&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Data Visualization Libraries
#### 1. **Matplotlib**
- **Description:** The most well-known library for data visualization.
- **Features:** Great for making highly customizable graphs and plots.
#### 2. **Seaborn**
- **Description:** A high-level visualization library based on Matplotlib.
- **Features:** Easy to generate various plots like heat maps, time series, and violin plots.

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/733d1e42-5a53-4fd8-90c1-3d85254369a6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TMID762F%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T122913Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIEBEyP6K3PibXSHsl4sJkFZInB2ri%2BlSyFjQk7K12cLIAiEA%2BeY8b31QG0HHXI7317ZkK9wyOiG2Nu04KSUCxsjYqhYq%2FwMIFRAAGgw2Mzc0MjMxODM4MDUiDFE5LSx1Kf89alv4cyrcA4ik3j1xnnFwQ7f8otAKYfHQu3Q%2FZXRuM3o4pXc2y8zpvAirWTvzmTUMvE9QHi84yDPJzNJ7qFxMZYHvIxNnsFdLH1Hx6BnWhzcl2N8QQV4nnv8pwan9vcrjVJaEShvX5we%2Be89hZqRdKE7c4mU8IHtIMYQPLfQV1kR6x5bH46fgBdnNOGqJJWAo2p%2FKHoQzqE8%2FTdFX0wgcmXyJNtgXXpIRTGnuXhdYYMifC3HtUT4tkrkMJDSCkIkdyK0HlnQj3rz8Nhk5okTMd1lauN0BkJOinnd9yD3AcdtylSTCuLxB3%2FsqBohyV5YVXaNIKgfBebtVcNMvpwYhYYGecpi%2BR0wS5vHSAmdxFTN7CQQRMYk%2B1%2BzchzDT7jy86jihqxCcyVriloXHrGtHFOxFkvBruEiNWfqmtwpeTQXZ19RCzRBBY2LB3Ja8xf1KwtxNCIN7pGEUCjHFfF23l37kl5c7Mc72hHnqh3N%2F1Sds0yNqRinI10zqoR7JEwnn5EGfjidTdqkrqaZmPxzZCWdGW7cA1CE%2FHYmkk4VTapWHSkS7TymY1bWa5QD1jKYQo2SFZd49GFtfRunKOSdTpg6q9hWhWN8qz0%2B08TNVHqCPBvEqqaBlmQW%2FUBOIkqh4yXuNMO%2FSgr0GOqUBSfz1fnlvSfsqplyi2ZiRWH07KFTbbJEQFOjYUKOUful9HuAQQ5qlM46AWI6DpwrYGtRNQ74reQTQfIHbA8cBEeGrnTEhxHMZSZwL9wLHh0dlbnDq28qeRn3EJF4D456ihZeAtkzUaM7unANLOkuc69%2FR4rynWyy%2FBDDx09s0PUhPj%2B4xC3FIAU6pjrtguOwaRjdHZiyDZ65tHCEvFgWJtLtY8zvd&X-Amz-Signature=e0ddbb594f4f0004ad0f1531f6a6b4656954204526d63eac2b68e412334f166d&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Algorithmic Libraries
#### 1. **Scikit-learn**
- **Description:** Contains tools for statistical modeling, including regression, classification, clustering, etc.
- **Built on:** NumPy, SciPy, and Matplotlib.
#### 2. **Statsmodels**
- **Description:** A module for exploring data, estimating statistical models, and performing statistical tests.

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c62885f5-417d-4179-834f-d68f8f2bdf39/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TMID762F%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T122913Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIEBEyP6K3PibXSHsl4sJkFZInB2ri%2BlSyFjQk7K12cLIAiEA%2BeY8b31QG0HHXI7317ZkK9wyOiG2Nu04KSUCxsjYqhYq%2FwMIFRAAGgw2Mzc0MjMxODM4MDUiDFE5LSx1Kf89alv4cyrcA4ik3j1xnnFwQ7f8otAKYfHQu3Q%2FZXRuM3o4pXc2y8zpvAirWTvzmTUMvE9QHi84yDPJzNJ7qFxMZYHvIxNnsFdLH1Hx6BnWhzcl2N8QQV4nnv8pwan9vcrjVJaEShvX5we%2Be89hZqRdKE7c4mU8IHtIMYQPLfQV1kR6x5bH46fgBdnNOGqJJWAo2p%2FKHoQzqE8%2FTdFX0wgcmXyJNtgXXpIRTGnuXhdYYMifC3HtUT4tkrkMJDSCkIkdyK0HlnQj3rz8Nhk5okTMd1lauN0BkJOinnd9yD3AcdtylSTCuLxB3%2FsqBohyV5YVXaNIKgfBebtVcNMvpwYhYYGecpi%2BR0wS5vHSAmdxFTN7CQQRMYk%2B1%2BzchzDT7jy86jihqxCcyVriloXHrGtHFOxFkvBruEiNWfqmtwpeTQXZ19RCzRBBY2LB3Ja8xf1KwtxNCIN7pGEUCjHFfF23l37kl5c7Mc72hHnqh3N%2F1Sds0yNqRinI10zqoR7JEwnn5EGfjidTdqkrqaZmPxzZCWdGW7cA1CE%2FHYmkk4VTapWHSkS7TymY1bWa5QD1jKYQo2SFZd49GFtfRunKOSdTpg6q9hWhWN8qz0%2B08TNVHqCPBvEqqaBlmQW%2FUBOIkqh4yXuNMO%2FSgr0GOqUBSfz1fnlvSfsqplyi2ZiRWH07KFTbbJEQFOjYUKOUful9HuAQQ5qlM46AWI6DpwrYGtRNQ74reQTQfIHbA8cBEeGrnTEhxHMZSZwL9wLHh0dlbnDq28qeRn3EJF4D456ihZeAtkzUaM7unANLOkuc69%2FR4rynWyy%2FBDDx09s0PUhPj%2B4xC3FIAU6pjrtguOwaRjdHZiyDZ65tHCEvFgWJtLtY8zvd&X-Amz-Signature=a2be427cf63aa7217f9d3b6fe43406a0448f423d232ac9faf33f1f2a3f535ba0&X-Amz-SignedHeaders=host&x-id=GetObject)
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
