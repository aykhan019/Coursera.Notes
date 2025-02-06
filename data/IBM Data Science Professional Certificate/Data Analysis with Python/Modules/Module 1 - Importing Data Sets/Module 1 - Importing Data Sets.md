

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

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/997ac361-58a8-4f04-bb0f-79fea4baa761/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UUC6REDJ%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T141354Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEYaCXVzLXdlc3QtMiJHMEUCIQD%2BlzwGyvD32E6nblZXlRnhV2mIt8z%2BSQvmzYgYhzbTYwIgGZJ2R5cKoecRAX7O6LokCPQxNygfbJ1%2BMfny9%2FTz5Vwq%2FwMIXxAAGgw2Mzc0MjMxODM4MDUiDIA%2FeAMnBDINESBenyrcAzLmjr7cbVVMSr20pRVq9pDTXex%2FxN%2BZQ%2F%2FveJxwHDKfgzNk6nMOvCWiwHRz9BTH2k8fHRs2ddPue%2BlZvlJHKRrTQfspi61tw%2BRMVCkan7n2N516ZUxas4Itf0nJqGKpwDGkbkI4ZQi6hc12NjLKbFGwmUTRItwXTpqVQfC5dg9vgPh2W6ADMJmENQIQytKyWBm7mTmCIbX4IHq6KXJ2kFhRABnURUwP%2BHcKsaDXuTTz8jCH6GWWPr8t%2B9k20M5K8Yut6gY%2FuhjJgwr%2BOoAOBoB8lTcompaKF%2BA1egpOEy0nXXrvRHbXAUK6F41%2FEqyYULYJV6n51yemGhEZQEi%2FiYEQvvisflXP4FWq9nIZ3exMJGoM9Bs%2FYX1WF9eWfM41TOtr9chqr2REWKEMPDTEfvTSMvN1br%2BmF1g3I6LN5r7x7lUXrUvB46DwbTCg00BHDMNxklGja1qv1pFQPfCT6%2BplaH4aFxdKKFKkXUDh3SbrErwZL%2BqmkVztWLR2bVLtqMF2Sug5EF5KxLIz6%2BzcdQMLaQKtF0hvWLpvjn41o5XxnyPLnuhTXtxru1AlnXJYOeHpy70YFrItLpIZbTplUG4yLyhrynxxXQN4nl%2BdG9XxPtgcbpXDONN%2FedoZMMv5kr0GOqUBAHowDYHlSZdP7zlCbjsf5DIl0nIVG6u6JrQAafqsuPGu6fcAYM%2FmRyVfrAWBcvRZPbKhbD1Wk1MB8UY9kMhP4c0KALB2FOJSe14vtI3AxhV2b1qywJCFiR2xHS8jIM9s8Jt4CAjydACVlYNdgmz1I3V8NCjLVBxb2mkeB1a%2FXip3ehJVaZx616%2FFVHAQKlrvSnvRuZ1Nh7hn969kbVIpJepI%2FKko&X-Amz-Signature=e7ad99f0306bf491c0883461c1c987d780430ce824674b2467f8c5626084a077&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Data Visualization Libraries
#### 1. **Matplotlib**
- **Description:** The most well-known library for data visualization.
- **Features:** Great for making highly customizable graphs and plots.
#### 2. **Seaborn**
- **Description:** A high-level visualization library based on Matplotlib.
- **Features:** Easy to generate various plots like heat maps, time series, and violin plots.

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/733d1e42-5a53-4fd8-90c1-3d85254369a6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZTW7MMKJ%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T141353Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEYaCXVzLXdlc3QtMiJIMEYCIQDtYl7JqMo6tx6WB0VF04XP2u%2Fd%2F8opf1rKjB3OhJP41gIhALs3SlEJVuPb8zoschkPI4ray5dpprSAaARf%2BaBwr8iTKv8DCF8QABoMNjM3NDIzMTgzODA1IgyUintWNb7cD%2FNOc6Iq3ANfFzDnNPgRPTPz%2FtE%2B8I%2BEKQUnXn2%2B%2BhlDr%2BzH2f4%2BNyPx%2F%2FCcThIPsFs7xNVzLmIZ5y5XJQZpdymnaH%2BDd7LqCAMT4sC2vIU7rbJvRvIprd4f5402OYCv9jdOTbjd%2F5HXRK2SWo3sOrF8LUkL81xI7qg6LaD%2Bf6OvGfTnDd06tpmClj5GNfJvceoPtwD12Y9cKS08WpFbbOWFa4ihRj59hPcidddqWCKzxTjD0sn0vW6RDiL%2FIhuD8EEQjwBK2WDaWqWQ0ZBN%2B%2FOLfdhwL9wxZwenO1fi6FvT0u3Oa6%2FbygUZHgbehnrUF37Si%2BLrSgXQgwI5n69QNGDwjqQcdEUJyAHevuLs%2FAMJMubAS826CF8wjlkmKZv9Try8isXEsHxfQuHsJAoltugmr%2Flsb65kkEALOdZ%2FpgTpE6S%2BvCJLN%2BIqXnHvL3SxRX9r3Z3APnA1z7g4wo3ZSM%2BKsru3zr36BdhSAgfArD6iOfu4vLULsTlHWGdKPRKgCMXTvQnlWLniTtfKrr271L9T7%2Bh%2FihoiuEa2HHdxtBAOX2nmoaA%2By0vIQRTDJ435AxTE6Kd%2FN7LeAqw6n%2BHD459eZ%2BpJruco4HzjhRbVFr0MHyBY2Vhhz5hqSkSLn1w9PQ30TjD4%2BJK9BjqkAdLEzu5rrnk1JxFOkpifmOQIifC3YbkRIdPHViVPrk8Y3%2BioFoa5ShGrZW0MMf0jW2ffFdSzgLLxaVmmOCcsdyEyBsxET%2BPXHEjywQ3Qj3MwnduitzPGKAzCx8PnTpDI2HrSk7kHjWkHt6%2FwlNfDCeBIdihdm3%2BEe9OLFyltj9JLRmx5airdN9zTPnB1b9lTmPcdkem6F8CiXbNEc5K2KWXZeRLk&X-Amz-Signature=dff93233424997b61d1b124662fd2cc669e8eb0bd43a7b5090658e9bd4fc86ba&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Algorithmic Libraries
#### 1. **Scikit-learn**
- **Description:** Contains tools for statistical modeling, including regression, classification, clustering, etc.
- **Built on:** NumPy, SciPy, and Matplotlib.
#### 2. **Statsmodels**
- **Description:** A module for exploring data, estimating statistical models, and performing statistical tests.

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c62885f5-417d-4179-834f-d68f8f2bdf39/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZTW7MMKJ%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T141353Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEYaCXVzLXdlc3QtMiJIMEYCIQDtYl7JqMo6tx6WB0VF04XP2u%2Fd%2F8opf1rKjB3OhJP41gIhALs3SlEJVuPb8zoschkPI4ray5dpprSAaARf%2BaBwr8iTKv8DCF8QABoMNjM3NDIzMTgzODA1IgyUintWNb7cD%2FNOc6Iq3ANfFzDnNPgRPTPz%2FtE%2B8I%2BEKQUnXn2%2B%2BhlDr%2BzH2f4%2BNyPx%2F%2FCcThIPsFs7xNVzLmIZ5y5XJQZpdymnaH%2BDd7LqCAMT4sC2vIU7rbJvRvIprd4f5402OYCv9jdOTbjd%2F5HXRK2SWo3sOrF8LUkL81xI7qg6LaD%2Bf6OvGfTnDd06tpmClj5GNfJvceoPtwD12Y9cKS08WpFbbOWFa4ihRj59hPcidddqWCKzxTjD0sn0vW6RDiL%2FIhuD8EEQjwBK2WDaWqWQ0ZBN%2B%2FOLfdhwL9wxZwenO1fi6FvT0u3Oa6%2FbygUZHgbehnrUF37Si%2BLrSgXQgwI5n69QNGDwjqQcdEUJyAHevuLs%2FAMJMubAS826CF8wjlkmKZv9Try8isXEsHxfQuHsJAoltugmr%2Flsb65kkEALOdZ%2FpgTpE6S%2BvCJLN%2BIqXnHvL3SxRX9r3Z3APnA1z7g4wo3ZSM%2BKsru3zr36BdhSAgfArD6iOfu4vLULsTlHWGdKPRKgCMXTvQnlWLniTtfKrr271L9T7%2Bh%2FihoiuEa2HHdxtBAOX2nmoaA%2By0vIQRTDJ435AxTE6Kd%2FN7LeAqw6n%2BHD459eZ%2BpJruco4HzjhRbVFr0MHyBY2Vhhz5hqSkSLn1w9PQ30TjD4%2BJK9BjqkAdLEzu5rrnk1JxFOkpifmOQIifC3YbkRIdPHViVPrk8Y3%2BioFoa5ShGrZW0MMf0jW2ffFdSzgLLxaVmmOCcsdyEyBsxET%2BPXHEjywQ3Qj3MwnduitzPGKAzCx8PnTpDI2HrSk7kHjWkHt6%2FwlNfDCeBIdihdm3%2BEe9OLFyltj9JLRmx5airdN9zTPnB1b9lTmPcdkem6F8CiXbNEc5K2KWXZeRLk&X-Amz-Signature=f9ade84717b4a4e04599e45249dbf0adfef3cf062dd6b4a3de2222cc244625cf&X-Amz-SignedHeaders=host&x-id=GetObject)
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
