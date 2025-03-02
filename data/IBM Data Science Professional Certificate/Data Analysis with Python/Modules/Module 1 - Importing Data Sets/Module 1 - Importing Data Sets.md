

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

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/997ac361-58a8-4f04-bb0f-79fea4baa761/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46625MGKTF5%2F20250302%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250302T004224Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHgaCXVzLXdlc3QtMiJIMEYCIQC4QIl%2FGYHTwM5CG%2BDz2OSRSjC1oXUFtaqmPpQSLocK9wIhAJc72hoBpX8%2FzJRIKvzhXG7ZkHi6fHb8J6hH%2F1a1gK6cKogECLH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxLdy53yxhGk%2B6w7Akq3AMHOsvgPnGN3L6TX4qBTmuHuBQbQ%2BOgzRu2%2FJCqRcT5hHbCMdlXyqhmENnQT4wakfWouFP7KdnS89rUwtb7X5XE5wS4VO%2BojF9Wy%2FVO2pkGiEtGZWNsJF8ndEAiugA83EeO16rXfJbKoq4gBrUA06uO29Vn2QAyrA8D4pp271WCjQC4g8rnhIW9oXOMgYxM80lTPPOGLtdWgBD%2FWGhHPakBYc%2Bn2qhQPL6YKJQ0bEO8V5N6wFAoNC884hZwGT%2BDLyy4YHXynzfRvDQ6LXuJidKBhT4mtJlB4J8z%2BMV67ff5xB9kGVS3m2MeIPPw8qzP51a7vb2H8pK6FA0%2FfOY9VYib0zjkrW7xfJ8QcJjqrnP0SHPN6bT1Ik45%2B7Zahh6ZvgJVPvmu7Pd58N1KwY4YNw7W%2Fr1l9sfeHUK1PBSWgULM58fncvO6YK8bMnEIjx%2BS2KmSFoNSEkPKXyPmTFeyWmnCeWaRa4Xn1Wvd%2FoYfiVywyJApZQq9gQ06Q1SY8aF84%2BVvJM0mUtiDNi41spxgyiKsywbKbL7IqMPNrRBZS0iL0JMmmTYSMKlj3a0LSX9qitjR3U5UH3Wfss4%2FaqlES0SyaDNpIPugPzaqWOW5QH%2FwCtHdpqVamQfQXUrz%2BzDnt46%2BBjqkAbNZCTtY2tKTwXOoGry0nVRJLxgU818B9%2F0sCp5h0CKgvB7UTRT%2BanwjrRuad9ziP9q9ArmCq%2Ftv5%2BIkWeMLgoDlmouybUhSRszdVog71YMeT4Sp21iJScfVFKmpl314fQCOPlq4%2BQUpL1WScG3B9QfUuhyR8iwzuQZWWlEIkvDhnTBC5Xve4e3ummOqnR2ysv%2BgPzXJswIsF8%2FV8ZLqValoDcr%2F&X-Amz-Signature=bf48a40ecdcb6e5d690a00ad11e204fe71c7a5d913c8102060433d876ea886f9&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Data Visualization Libraries
#### 1. **Matplotlib**
- **Description:** The most well-known library for data visualization.
- **Features:** Great for making highly customizable graphs and plots.
#### 2. **Seaborn**
- **Description:** A high-level visualization library based on Matplotlib.
- **Features:** Easy to generate various plots like heat maps, time series, and violin plots.

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/733d1e42-5a53-4fd8-90c1-3d85254369a6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665W2RDUWF%2F20250302%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250302T004223Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHgaCXVzLXdlc3QtMiJGMEQCIEYX%2BKy3IY9NacE625%2FdCjRm6VHzWFNKXUiOT1RswwG8AiA5xoDk7N3IgkOeJJwPoQnWdrNAchm%2Bx2zMsGO7wZALyCqIBAix%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMjQLy0mbkZPLn%2FOTcKtwDSh%2Fo5HBsw6XgNBDHt0Hp29HuBDjBA1OU7mpZaZnbO5I3YXuRkm9QuP4nW%2FrABQeMwao2EWr5p%2BhcQhtbYy%2BUQRwL4fNhe2TklAX6I%2FrfCCmK%2F0OKDisApIUD3bpS1O0x%2FIhC%2FKe8aoHaGRB5YtI2IDv4N5nmIaX4RvbEQn%2BRLp3UEd68bC65tGlXmA2C894AV5MrvytjfSV9Po9tqB%2BDG%2FdoizDBbJ5qSBs7GGw%2FmeBYfugEuFg6b0XWQOvZqkLmhii2p45MvRPuFqRG%2FzHmQlK06U%2BhXf7BKOpE%2B6vEOhdN9bEXEjpiSR0RIx1R96FDh3SSIaOHZig%2FwkQttmqu43felvIMY%2BzeXH1ZRuXrD%2FrzvJIMhNOs1nb9nq7FSYEo%2FKu7KxBQFNghTN7ugatzQSIX7iLejvOjxguy3xzOrytpHgEz%2FFHgM0tIR0xkrrTNhYdYcSr8gu0se2YUnDAZxVL%2Bv5NCLAYejWBZMuYOAGPm6Aw26utS5yIVpDjN%2FOqbDJj9QsDcq3dZJ%2BybGGIUusT5tgOgLVe7eVQZUlmeyhKjaGgzojTZFP4%2BB80eZw4jrGOyj9LcB%2Bir1sU49Bk4WdWrUr5SO4Vs88x4DCyX4YBVKttJuG90hJ2GsNQw77eOvgY6pgG2giNHLLfsKFHgGa%2BM66e1fOEckmRCGE%2BxkA8cVy5YRxdFGEmOMucNuoHTlwM%2Bfw4uY0zOE8MOQ19dwemNFXwzhKJJMtitWR9k9ohkxKx%2F7RHDOGQfC8XY3sZvC2GG65J0vnJHWHlazr81X19Se452ETiYR0GB%2BhhMTVXfpb%2FS14vFiH1LO2CgpdY1qw0CgouxwqAOuqf2g2RLBJyyrt6qRt0JNaqV&X-Amz-Signature=130d7945007aaefca54c11de4c975ec838daa65a057045331c46bc3798ab3520&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Algorithmic Libraries
#### 1. **Scikit-learn**
- **Description:** Contains tools for statistical modeling, including regression, classification, clustering, etc.
- **Built on:** NumPy, SciPy, and Matplotlib.
#### 2. **Statsmodels**
- **Description:** A module for exploring data, estimating statistical models, and performing statistical tests.

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c62885f5-417d-4179-834f-d68f8f2bdf39/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665W2RDUWF%2F20250302%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250302T004223Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHgaCXVzLXdlc3QtMiJGMEQCIEYX%2BKy3IY9NacE625%2FdCjRm6VHzWFNKXUiOT1RswwG8AiA5xoDk7N3IgkOeJJwPoQnWdrNAchm%2Bx2zMsGO7wZALyCqIBAix%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMjQLy0mbkZPLn%2FOTcKtwDSh%2Fo5HBsw6XgNBDHt0Hp29HuBDjBA1OU7mpZaZnbO5I3YXuRkm9QuP4nW%2FrABQeMwao2EWr5p%2BhcQhtbYy%2BUQRwL4fNhe2TklAX6I%2FrfCCmK%2F0OKDisApIUD3bpS1O0x%2FIhC%2FKe8aoHaGRB5YtI2IDv4N5nmIaX4RvbEQn%2BRLp3UEd68bC65tGlXmA2C894AV5MrvytjfSV9Po9tqB%2BDG%2FdoizDBbJ5qSBs7GGw%2FmeBYfugEuFg6b0XWQOvZqkLmhii2p45MvRPuFqRG%2FzHmQlK06U%2BhXf7BKOpE%2B6vEOhdN9bEXEjpiSR0RIx1R96FDh3SSIaOHZig%2FwkQttmqu43felvIMY%2BzeXH1ZRuXrD%2FrzvJIMhNOs1nb9nq7FSYEo%2FKu7KxBQFNghTN7ugatzQSIX7iLejvOjxguy3xzOrytpHgEz%2FFHgM0tIR0xkrrTNhYdYcSr8gu0se2YUnDAZxVL%2Bv5NCLAYejWBZMuYOAGPm6Aw26utS5yIVpDjN%2FOqbDJj9QsDcq3dZJ%2BybGGIUusT5tgOgLVe7eVQZUlmeyhKjaGgzojTZFP4%2BB80eZw4jrGOyj9LcB%2Bir1sU49Bk4WdWrUr5SO4Vs88x4DCyX4YBVKttJuG90hJ2GsNQw77eOvgY6pgG2giNHLLfsKFHgGa%2BM66e1fOEckmRCGE%2BxkA8cVy5YRxdFGEmOMucNuoHTlwM%2Bfw4uY0zOE8MOQ19dwemNFXwzhKJJMtitWR9k9ohkxKx%2F7RHDOGQfC8XY3sZvC2GG65J0vnJHWHlazr81X19Se452ETiYR0GB%2BhhMTVXfpb%2FS14vFiH1LO2CgpdY1qw0CgouxwqAOuqf2g2RLBJyyrt6qRt0JNaqV&X-Amz-Signature=d31793a89621c0307cb49353b96e4efc6cf54826115668ec2edd6b2fc5aa39b4&X-Amz-SignedHeaders=host&x-id=GetObject)
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
