

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

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/997ac361-58a8-4f04-bb0f-79fea4baa761/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665XOQ7C5Q%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T141425Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDJev2K2%2F1YdXbC8LffJfjBVX9DSHXrqlU5sdUAYHavvAIgM9aJwjTbsB4tQK8cD4mKMEEriQ5hAPIlHXBRZkXCBmUq%2FwMIFxAAGgw2Mzc0MjMxODM4MDUiDB%2B1UfgRwWHHJUqtdircA5%2BQhAp8MSDhnyjaaB2dStOLHJ3KA75c21LkEe6%2BmyYce%2BpuSmEobFGMkpsFurUOEm9BgUEogAmYfKZi7cw46fBrwuQXJBMOrOdvdSk9wZyJc6QwZoxpkdqGTR8u8Du0zlqmkV9m8z%2FGRCSsoc8m3oG6Rx%2FGksHLtfquMs4ACcJA2JbWkwDfn2%2F7QAZdJbO4%2FCI5Rbs2zeDEyWif%2FqAjTwBLxdJobP7LMGe9wyaP%2Bw95cAJKzmVu5EW7FRLkrpwSaXl9orJJpCGKW1HO3PeXgFRya4ukPGq9nbK13JhpYJlIypNMQfZQxOgi8aDbDIxddehBkV77G%2FyVEtzHZ8sCvx2ZlzJuB5MRGXil5UsODCc31dinJI9mBqiAu%2FTv%2F92pcP6OJtsgUiV6pp2%2BeoBharymXVEVB6N2nukVaMhL7WPTx99R37UYsbu1WjuuhhWcAQWtvX0hV1zM5pJQDiaYEdL8DjZRC%2BXPsUzhMlgCTqV6pcw2vU%2B4sAdJrXBm9LZUPHcIIR0zhgNFWS1JeoFtLr8uUasaMe25mAaKAfJd%2FYtDpZ6yL5i%2FzRKZdpQcgd0CXvka2RL2KN6xsHX2Q1fCRWpH1NUJuF%2F3tUtbeP6g0s5Zm%2FGOIB%2FKLNFQegLVMOqOg70GOqUBce%2BvxDLAf%2BOnXc%2BDnDqlySlaK7W41CemUS6fmjwqLxBWvSUV8PSmy2D0SzoYPdcLE6EEsKY63Ugcb2ppvwRWs5SVQPMLusuX47o1NCZ%2ByUo8fKJ4grBZJW9JhEkzTAoI4hyR8w5N4j7pky5u4INYw4QQKno6Uh%2Bi8XRISWBprQdBiKpN1cE123VjZO3cgYYn%2FOqC%2BsopLfNyLLsKrmIr2nYT9Jms&X-Amz-Signature=afbd6177f20ab751acee5d02cdaac89b217123e7cd40a9c3e0458dc103b3b355&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Data Visualization Libraries
#### 1. **Matplotlib**
- **Description:** The most well-known library for data visualization.
- **Features:** Great for making highly customizable graphs and plots.
#### 2. **Seaborn**
- **Description:** A high-level visualization library based on Matplotlib.
- **Features:** Easy to generate various plots like heat maps, time series, and violin plots.

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/733d1e42-5a53-4fd8-90c1-3d85254369a6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZZE3XOT2%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T141424Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGWX8DgjVjn%2BP0PzUEWgeHEGZPJbn89YCLO1wiKOX9iTAiBvirpAPxlZU9gTbKuZbCFMZoMEaOeay2MMv9AQ5pSGXir%2FAwgXEAAaDDYzNzQyMzE4MzgwNSIMsX3TyoeGauC2np%2B8KtwD2Ne7drw6HC%2Bp89E3JOpO9dRbG8hhos0noAgclMWeY7U83RcnbeQXjgPOIoneO%2F1TRMqWV50%2FFupW6SLbkRM9Dh3cnhFxkRDafUwYWGAwP45HyVpg%2FqiwOWVtohqdBTss1ZIP9cmutA6e39kIuYMbWK7ByhxymICQ1s0QKjo3qcg1NGatt%2FR11de4rh%2BQmGs4kgJdoedSKI4YNO4BY1rl7fnne0ip88uvWZueNXY49RAPzDTy4NBSSkCi%2FVJjGmRMH5zF3fWxJ4DAUJM2xZZzfvpoy4mDEzOCEmUYhS5kecUm%2BLKkJD9xB7tNEpf%2FhGxD%2FgWVjXlBTE%2BiC1GKYwoi%2FX35k%2BukCvVgKcLHynmDyQ0v2jOYmGEpDnGov5LZW9cXzvJLV3slEZ2v%2FXkmbfP1ZEH9tkHyYMKOo2bnr42bAeRugpa7zQ5YJpKJaNkvpKkuU9boa9EfEOyUvbgtWqeQDWf%2BOTII6vTjuMDi8YxMwD4MNRjPmtWWDjaWfOUKtW6oXcwUhh9pLwaBCSKnjtD2rSVfDbq7nH%2ForROP%2FCjglg8cys5QJ42evGq9wII7Ap2Zt%2BG69wIpfYTSRpoQiHsZ60GCma5WaLCpsBCY9qL6RG7Mgrr6BxW7ytKW0tMw%2BI2DvQY6pgGYE0yUnNXp7X0GjqDoHCNQMBn3MsU8MjUwZbP2YT9gMM5Sjq8Y%2FIo1rp38oqJnt%2FskbxD37QH57f6CKCMYJC6VnfeaIxfOQaJqQaT%2FK%2F9DrKN%2B8%2BGDB87uKoWKuXKLVBJM4KTmrP8DQpUyAsODpBrvYQjOn4vTmz87eh80MgSfastm%2FTROJpy9%2BlvChqJHtvatsLJdho0FvKMSONSaA%2FiJwldecPhA&X-Amz-Signature=a3e0abf483f11f4a3219285a3e6648d13f0825d74f00bb537cd2cf7355214724&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Algorithmic Libraries
#### 1. **Scikit-learn**
- **Description:** Contains tools for statistical modeling, including regression, classification, clustering, etc.
- **Built on:** NumPy, SciPy, and Matplotlib.
#### 2. **Statsmodels**
- **Description:** A module for exploring data, estimating statistical models, and performing statistical tests.

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c62885f5-417d-4179-834f-d68f8f2bdf39/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZZE3XOT2%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T141424Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGWX8DgjVjn%2BP0PzUEWgeHEGZPJbn89YCLO1wiKOX9iTAiBvirpAPxlZU9gTbKuZbCFMZoMEaOeay2MMv9AQ5pSGXir%2FAwgXEAAaDDYzNzQyMzE4MzgwNSIMsX3TyoeGauC2np%2B8KtwD2Ne7drw6HC%2Bp89E3JOpO9dRbG8hhos0noAgclMWeY7U83RcnbeQXjgPOIoneO%2F1TRMqWV50%2FFupW6SLbkRM9Dh3cnhFxkRDafUwYWGAwP45HyVpg%2FqiwOWVtohqdBTss1ZIP9cmutA6e39kIuYMbWK7ByhxymICQ1s0QKjo3qcg1NGatt%2FR11de4rh%2BQmGs4kgJdoedSKI4YNO4BY1rl7fnne0ip88uvWZueNXY49RAPzDTy4NBSSkCi%2FVJjGmRMH5zF3fWxJ4DAUJM2xZZzfvpoy4mDEzOCEmUYhS5kecUm%2BLKkJD9xB7tNEpf%2FhGxD%2FgWVjXlBTE%2BiC1GKYwoi%2FX35k%2BukCvVgKcLHynmDyQ0v2jOYmGEpDnGov5LZW9cXzvJLV3slEZ2v%2FXkmbfP1ZEH9tkHyYMKOo2bnr42bAeRugpa7zQ5YJpKJaNkvpKkuU9boa9EfEOyUvbgtWqeQDWf%2BOTII6vTjuMDi8YxMwD4MNRjPmtWWDjaWfOUKtW6oXcwUhh9pLwaBCSKnjtD2rSVfDbq7nH%2ForROP%2FCjglg8cys5QJ42evGq9wII7Ap2Zt%2BG69wIpfYTSRpoQiHsZ60GCma5WaLCpsBCY9qL6RG7Mgrr6BxW7ytKW0tMw%2BI2DvQY6pgGYE0yUnNXp7X0GjqDoHCNQMBn3MsU8MjUwZbP2YT9gMM5Sjq8Y%2FIo1rp38oqJnt%2FskbxD37QH57f6CKCMYJC6VnfeaIxfOQaJqQaT%2FK%2F9DrKN%2B8%2BGDB87uKoWKuXKLVBJM4KTmrP8DQpUyAsODpBrvYQjOn4vTmz87eh80MgSfastm%2FTROJpy9%2BlvChqJHtvatsLJdho0FvKMSONSaA%2FiJwldecPhA&X-Amz-Signature=4947b1f5906658b3b70d147a2390041510275d0dc8a675a49a9a844d6729ef86&X-Amz-SignedHeaders=host&x-id=GetObject)
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
