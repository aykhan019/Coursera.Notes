

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

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/997ac361-58a8-4f04-bb0f-79fea4baa761/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Q6VYNQRR%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T141214Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCimI8cg%2BoSzxzXS3bbdWQYdLH9Q9IZSJ2G4ensmQxmSwIhAJkCpgHUXO9%2FuaTOdjiAxQ7%2BPTLiYHY6flDf7VdJVF5RKogECO3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igz6SJUxr%2Fle8pmb4uEq3AOMJjoQqtxrkQwdodRmmvNkvY1IqNI%2FNTxOprVwqKOn6GjRl6FEPbRIms2pOxDInwf9pPR%2B5l42Q6OYtuxr6MDhI%2F6pr8ygvrXe2xsZw8bsmo%2B1EDIs2Q3ZZuK2tHKFl%2FLTmbtmPvnws8%2F7Jdq%2BRPSv7Hx6ZsFGLiFPEATfvv%2FNaj889PzERW8%2FXcb65BV6ygrnr3uBn%2BqC%2BFB8GlnfAFb78uD%2FOVZKg5jHFzVHgf4vz%2BUDq9uvQdhOLjsTFAofChU12mpzPSZ71muhKL%2Bc9aiamJpDn70aRVNfEy8Xrf6x8NBQjfQAUJAr6G1cUIgXc%2FsrJS6XfCnR1lEP0FdvQKbleWkrN7UlakH8Dizx1xTXtcJTVgPnW8n%2FyADZAT4NHGsZiJN%2Bg%2BUxaJUq%2FRcsruexleas3606y26r%2Fj0uh9AniBZ5j32CPVR9fpEQwcTXByLUQFUQy6Uq5%2BbaCCDSaUeLCNOOtcN5olt7zT5Fg%2F39mjbxa0iqt6RbsXxx2YW9sHGHv%2BeNvdELGcIV2yhJ%2BXegPeXMOQddekpAYnGkCTCiRTNeWUZhUIj8uXWLJrXBU2pffojJVIqQIOzytp0ASBEe9MOFo6hOJlgkPIAX31qV72Iaj8p3WXHbaCVVXjCvvP28BjqkASkvCnbOiAz8zgxTKhcHqawgsLZJVM3PGtFmcTdt0cLHluk6kERLVb6gPJbvAdkuRaONqJ%2FU%2BQZkFgxEtJH4SU0Lj1QFq0XdiYIw3aHvv4bnw7kDg%2Bk04tIeccCgjPmgAm2bSzOgt%2FM0Ke1wBKlVeZHATApKwRSQN0wj36i%2Br661iEaAcFZ6%2FKG2IidXr%2F8GTxh8n6wYkOop7O9%2BiUu6zCXZLmO6&X-Amz-Signature=80f80d8479b8778a211d44ec1d923d894e739960b41b5b5ad325ed3ab9eb1c4a&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Data Visualization Libraries
#### 1. **Matplotlib**
- **Description:** The most well-known library for data visualization.
- **Features:** Great for making highly customizable graphs and plots.
#### 2. **Seaborn**
- **Description:** A high-level visualization library based on Matplotlib.
- **Features:** Easy to generate various plots like heat maps, time series, and violin plots.

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/733d1e42-5a53-4fd8-90c1-3d85254369a6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666B435UGE%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T141213Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCRIeMm9bV31ekU2%2FFKD%2FiJzzreh%2F69q%2BB%2B1LKoo6rmtgIhAMZfXK8MVG4VC53tWUudYcOkthDNcFHlhPBAkWBy%2BHuZKogECO3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxWj2X0ezu1ePsGJ3Aq3ANgdTfpwjc5KoKFmEU%2FwOO%2F%2BobUONirXIHsZG0L954BR8rkZmgXXmmrUGe5uU%2FD2EpypTOWwJwygxTKWuIYxhae%2B2LkeVNnLO%2FzQB3WQOmJe%2BBycOuFVuJECKwYxp5kY0LlcGQpzwZPew%2B4tnXo6aFDNeB4dJFcAHO81C6gzJFU25D0fd9p6%2F47JlDs7K9gjKdGLJEsF4SvvxaQyxMUHHjpFo2nKTTivaqpUgX2fSol4UgvnlbAQN77Y1QAOjPKrvfvvH9pf6BrrQdmE3lDEiY7fpAToGtr3R9Z4zkfFZT5Do0OErk8VXOfHYW86nE04iROZMf1eEV4J7DRFVyPcplMkSj0sDnaoRz%2FRgyxdKxYIclFtUuetOzBQUWvn2zXpqvsy%2B1NDeITsO7Lv43Jj3bGJo2rOTHyopUSdU0dmOIKrCcAC7C10EXg8hLwE5javUtpiUrVFNXnxJ00kcJYzFU9W%2B6pNNXegiOyP3wWw5oG8jYTM7WVlNv6wp0foeNwgnkJ58MrSdfOytMh0isH92gbpaQKzDZSysirYKn9HB7PgGoBwczYwP4jKNgKClwQgGieHy7hV9wHO%2FoKn59KdsN3ub1zEDHGTGunyYEbUp4fe6%2Bk2sU3IWqATRimDDDIv%2F28BjqkAQOQCna1TZY98akcfe9Die2D07MwtlId%2B6GdejByx%2BQVcGJNXbFB9Vy7DO81Zx15Ki%2BEB7h9Cjc8%2Bg55hoprYOyv4iWetSKew%2FLv5U5%2B9mjPNBCiGFOgSaUNeqts3a02a%2BwQW7S%2FzkOdcSvSdq7ZDlPttPwuC8LmZHpKAcjQVmdwKPKo5SgWmjFi5k21QuCHYRwsYK%2Bq9DSi%2B4K5OAavdZ2IDhJC&X-Amz-Signature=014e101423c1ce51f32959f8eea28bbb2c690d2f4b6a06e2eda118d1ebd1581a&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Algorithmic Libraries
#### 1. **Scikit-learn**
- **Description:** Contains tools for statistical modeling, including regression, classification, clustering, etc.
- **Built on:** NumPy, SciPy, and Matplotlib.
#### 2. **Statsmodels**
- **Description:** A module for exploring data, estimating statistical models, and performing statistical tests.

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c62885f5-417d-4179-834f-d68f8f2bdf39/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666B435UGE%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T141213Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCRIeMm9bV31ekU2%2FFKD%2FiJzzreh%2F69q%2BB%2B1LKoo6rmtgIhAMZfXK8MVG4VC53tWUudYcOkthDNcFHlhPBAkWBy%2BHuZKogECO3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxWj2X0ezu1ePsGJ3Aq3ANgdTfpwjc5KoKFmEU%2FwOO%2F%2BobUONirXIHsZG0L954BR8rkZmgXXmmrUGe5uU%2FD2EpypTOWwJwygxTKWuIYxhae%2B2LkeVNnLO%2FzQB3WQOmJe%2BBycOuFVuJECKwYxp5kY0LlcGQpzwZPew%2B4tnXo6aFDNeB4dJFcAHO81C6gzJFU25D0fd9p6%2F47JlDs7K9gjKdGLJEsF4SvvxaQyxMUHHjpFo2nKTTivaqpUgX2fSol4UgvnlbAQN77Y1QAOjPKrvfvvH9pf6BrrQdmE3lDEiY7fpAToGtr3R9Z4zkfFZT5Do0OErk8VXOfHYW86nE04iROZMf1eEV4J7DRFVyPcplMkSj0sDnaoRz%2FRgyxdKxYIclFtUuetOzBQUWvn2zXpqvsy%2B1NDeITsO7Lv43Jj3bGJo2rOTHyopUSdU0dmOIKrCcAC7C10EXg8hLwE5javUtpiUrVFNXnxJ00kcJYzFU9W%2B6pNNXegiOyP3wWw5oG8jYTM7WVlNv6wp0foeNwgnkJ58MrSdfOytMh0isH92gbpaQKzDZSysirYKn9HB7PgGoBwczYwP4jKNgKClwQgGieHy7hV9wHO%2FoKn59KdsN3ub1zEDHGTGunyYEbUp4fe6%2Bk2sU3IWqATRimDDDIv%2F28BjqkAQOQCna1TZY98akcfe9Die2D07MwtlId%2B6GdejByx%2BQVcGJNXbFB9Vy7DO81Zx15Ki%2BEB7h9Cjc8%2Bg55hoprYOyv4iWetSKew%2FLv5U5%2B9mjPNBCiGFOgSaUNeqts3a02a%2BwQW7S%2FzkOdcSvSdq7ZDlPttPwuC8LmZHpKAcjQVmdwKPKo5SgWmjFi5k21QuCHYRwsYK%2Bq9DSi%2B4K5OAavdZ2IDhJC&X-Amz-Signature=34bd006e99a641c9c08fbb49fe872c40e660051f16a94da82b72aad752a29216&X-Amz-SignedHeaders=host&x-id=GetObject)
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
