

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

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/997ac361-58a8-4f04-bb0f-79fea4baa761/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SWRINDRU%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T141220Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHQaCXVzLXdlc3QtMiJGMEQCIHR4wJ%2BRwSSPWVFZ5Yt83cG7LcArth%2BXxKYTb8e21TLVAiBWR827m2qFUY7Yr9XllsY8s378DidhknE%2FbHbhNfKDWCqIBAiN%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMnCBrds%2FU8THDWMl5KtwDa48JSqshooDGMquxbvgRsJ3twtVggqEQe6%2Bcp0XwFIukGyMLgPUkPs0Q92mwxcvDzx0%2BxnhpF3si%2BGY1zh406Yk%2BjcVBNsGJxiWgy19fgJ%2B6wGoUz%2B%2BxWWWpndFXASReQiGwhbQhhNlaScbaQkDq4RZSXjz2v8vK%2FmC3bJkSBT0rsE63k8PV6oogRXfgLG0D90t91K91TEoRtFA5TAUPjpAx8EiHM%2BqANEAUJa85sg276YsYWKe0L8Rm8xC17fYITkj1BxI8yGQdD3WYfjgHJs%2F9i8m3GPCksxTYHoiUWVX1THw9g1VnzEiCtY088Xb%2F7%2B5AP8HJ4tnZ2aAyZhSNUX5IzqY%2FZFHsVluUkt64xgLdUYo%2F03AbATgmBdu5QFEuOMonbi6Am%2FCPbI1DBSbv6BAaOB%2Bmuuq3%2FXJo5IkSJyJfSoSLaHRNZVhVDPfhVYJ4kMBnDhbwi%2BKl4lU3KF5pM%2Bn3K7I591ufrG2vlZ5xmoNnOnstXsvaqhjv7qhxNHA4lCs0SCyt3mIb44sg7DiYwF9kzGMOS%2FegO%2BjTyNi4CgcE78%2B0RJ3ENn%2B6fuV3AVjvHLS6sW%2FFbhz8YAtqSu0Q%2FBZfS%2BHvFUU%2FdtbAystZS8bzmM3X%2FysQgS1r4icw1YWdvQY6pgFj4TsDZP3R2RV6QOvIbNblWwqc%2Bg3pbDSUxDjgNz4yUqYPT5QTWsdwXjhdxRVV2tnUPk4L4%2B0zNK9zKMu%2Br%2FEBhQN0msjeFNdXSGmnmTTJKRjJyJyo3VUQI8zrC0%2Fqff1AgjA9m2DmEclcc%2BO2yr5RsyW0iZH4rWOtq8KOfCjomnTGmsX3NJCy7iqvU6yW8WOmiP4v8jU7RGDrXmoFBaiEesjEJ4pV&X-Amz-Signature=fe607454657036de819b9e9bf9274aa0f6acb027ad800053c34189e01eb1c73c&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Data Visualization Libraries
#### 1. **Matplotlib**
- **Description:** The most well-known library for data visualization.
- **Features:** Great for making highly customizable graphs and plots.
#### 2. **Seaborn**
- **Description:** A high-level visualization library based on Matplotlib.
- **Features:** Easy to generate various plots like heat maps, time series, and violin plots.

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/733d1e42-5a53-4fd8-90c1-3d85254369a6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466S5EQLPQ4%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T141219Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHQaCXVzLXdlc3QtMiJHMEUCIQCfGiIEZr5qVk1qeNKsRmRIY0p28Ga2b5UMFLPx%2FH07PgIgDJzUupKp5qVYmkkWHKQXmdFODbRXU8fnk7nPcvaBIgwqiAQIjf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDP7lIzqcZ01YvKpLcSrcA%2Ft7JFgmfkzBVNWruCLOBmx0RBZMfx1gwwjj6haCPuiHduUdyNVz6W0fWh2KCw0zJGy2BNxX5FywpbKFqnXVeee2R0eg6sX73dso7OWYg%2FScNLlg6xAhxdA%2F2oFsTu8jm8uGSDEgWlXa0%2Bb8E1taFt2U9MNeYKRfzLahQb3St0fQpxhPP9mhsI4qEHt%2BUC2q2N%2FQgUq%2FvzduWpsaF%2BBnOGt1eSCwT%2FlKAgZ6zncLaa4QcPlOj%2Bfx65fG%2BsG2cflEl58f60N714gaMD3S9itokxpmAJtIEHYoqNkYvlwZ9HzTQWqcMyXSfGzdVvDw3GUeFkZeIEys8Y7booNQRUVW7MnvjcAOquMJLyN7wGIttZ9eIIIkXFLnMUNcItuHYc%2FtwN5HvBR%2FrMxfgR4fqXYrFNTWXi7XpEiHt2z8uT8x2TGoYcPcDWteo9U1mY3kMyT%2BSlikKk3pQ4PqKZpU8DFSvwixoEpCz9%2B4upyb7Sicdw2MgZRf4JEY%2BUZBq%2FoRG2ttEb%2Bk%2Bs7I%2F%2BBo2vhtBXshoBMm%2Fm%2BCjytYFDaRXduzkM%2F0qO%2B8NfkD03DfHdAHUoOIxgFPKTrbEiwja8cBKSGO4ZL5LZc%2FOz5V1bhpPAA2Q7ygu%2BUxQBzWQ0J1MbSfMMiFnb0GOqUBRbp2E8mSJTJFbvMJShtyvK2VM0T56hLdWWQKw583KKpAGUxlmnkPKFqvUo2u2%2FbHTqPpmN6jMAU83Ugsw%2BxIKASxtXIZ4Y1zNY9qwpQMu56nabmxVxigsOwisATtMIrkZXpQOy1aYYMDkKEa9QDLZ4SC7f1RfMzhKjFjgEp1XL1FbUJs0Y3AIYOxTqcJ%2B6b4AVcabcX5vLkQnmzCGsC0dcYXo73O&X-Amz-Signature=155c5c985838d8e19aadcf40ce29b5edbdcf0f4af00634a9211d3e92727e3c81&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Algorithmic Libraries
#### 1. **Scikit-learn**
- **Description:** Contains tools for statistical modeling, including regression, classification, clustering, etc.
- **Built on:** NumPy, SciPy, and Matplotlib.
#### 2. **Statsmodels**
- **Description:** A module for exploring data, estimating statistical models, and performing statistical tests.

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c62885f5-417d-4179-834f-d68f8f2bdf39/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466S5EQLPQ4%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T141219Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHQaCXVzLXdlc3QtMiJHMEUCIQCfGiIEZr5qVk1qeNKsRmRIY0p28Ga2b5UMFLPx%2FH07PgIgDJzUupKp5qVYmkkWHKQXmdFODbRXU8fnk7nPcvaBIgwqiAQIjf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDP7lIzqcZ01YvKpLcSrcA%2Ft7JFgmfkzBVNWruCLOBmx0RBZMfx1gwwjj6haCPuiHduUdyNVz6W0fWh2KCw0zJGy2BNxX5FywpbKFqnXVeee2R0eg6sX73dso7OWYg%2FScNLlg6xAhxdA%2F2oFsTu8jm8uGSDEgWlXa0%2Bb8E1taFt2U9MNeYKRfzLahQb3St0fQpxhPP9mhsI4qEHt%2BUC2q2N%2FQgUq%2FvzduWpsaF%2BBnOGt1eSCwT%2FlKAgZ6zncLaa4QcPlOj%2Bfx65fG%2BsG2cflEl58f60N714gaMD3S9itokxpmAJtIEHYoqNkYvlwZ9HzTQWqcMyXSfGzdVvDw3GUeFkZeIEys8Y7booNQRUVW7MnvjcAOquMJLyN7wGIttZ9eIIIkXFLnMUNcItuHYc%2FtwN5HvBR%2FrMxfgR4fqXYrFNTWXi7XpEiHt2z8uT8x2TGoYcPcDWteo9U1mY3kMyT%2BSlikKk3pQ4PqKZpU8DFSvwixoEpCz9%2B4upyb7Sicdw2MgZRf4JEY%2BUZBq%2FoRG2ttEb%2Bk%2Bs7I%2F%2BBo2vhtBXshoBMm%2Fm%2BCjytYFDaRXduzkM%2F0qO%2B8NfkD03DfHdAHUoOIxgFPKTrbEiwja8cBKSGO4ZL5LZc%2FOz5V1bhpPAA2Q7ygu%2BUxQBzWQ0J1MbSfMMiFnb0GOqUBRbp2E8mSJTJFbvMJShtyvK2VM0T56hLdWWQKw583KKpAGUxlmnkPKFqvUo2u2%2FbHTqPpmN6jMAU83Ugsw%2BxIKASxtXIZ4Y1zNY9qwpQMu56nabmxVxigsOwisATtMIrkZXpQOy1aYYMDkKEa9QDLZ4SC7f1RfMzhKjFjgEp1XL1FbUJs0Y3AIYOxTqcJ%2B6b4AVcabcX5vLkQnmzCGsC0dcYXo73O&X-Amz-Signature=5698b07c1acd265842e896eec0e600af50a0caf463408adc362a60db215eab2f&X-Amz-SignedHeaders=host&x-id=GetObject)
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
