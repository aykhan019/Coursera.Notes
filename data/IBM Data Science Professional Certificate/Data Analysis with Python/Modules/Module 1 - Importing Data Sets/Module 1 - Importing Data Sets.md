

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

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/997ac361-58a8-4f04-bb0f-79fea4baa761/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YP5WN7QV%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T041721Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAwaCXVzLXdlc3QtMiJGMEQCIGAA%2FM%2Bke3O3cAIgAVZrPW%2FH%2BL3PE0CiZSt%2BNXtKvjY%2FAiBtmUy39V5jaPzAQcW5AEytwJaXoH8242z%2FWSS84SYLmSr%2FAwglEAAaDDYzNzQyMzE4MzgwNSIMOojWzqCYoD4sDodkKtwDdLhjP81GrKfYs4RVJU%2FZuvUetLA6wESb8KBFAQVx5c8Bv7Xq6KezlN%2Fl2IAvE6QtD8LXz6SVUyLh0ww%2FhSsJF%2BU9n67%2FwXHQeIFRMkk%2F5UcGj0%2Fjw7WRABvdNKhbLtigyS0TT1I0QFf0uxFL92kjdRGlHN6CO3lZyvDCmdMYx3ISe8z489fgEy2ScaMr91pvCqGihA0eAl3HfIq%2FJs%2BmzItoz6bSYBFU8exnDY7K7YyTBW51fBOYQJc8k6uCLL5F0Wijh6dV0mfwuTeX40M47jREVI0a9erT9JNlOeFz3fqWxdFoecYtCAg%2Fz9kz53ISVtcFKmoxEPLNesex%2BX5Ugv83TaJ64cK%2FUUCu0P9NqpoabcDIzhgjJOHGryEUxARkX%2B%2Fnz4C3vWd%2BSaAlnlHSw2N6HUvufRT4prwQMLqmiRyUKcl79kJ25BOiJnpBxQh3%2Bj5pHYc1b2t91Ftei4geM9mHfKKXHmXKcJFBBfPbkx2AST66HnYVf5G8fh8m7hkHYqKX3bPW8I4i6sZOduKs5Zxv06ItgIMUto4dBtx0nu5eTaMdgSZU27tuXa3HxHOsMFnriPO%2FJQFYKOExAXlG3kqpxhJBTb8XpHoB1KpHInqhuTF9Jb1LczZ%2BgVYw56GGvQY6pgFHvoJ4d3Ku5WgqbaHsUUrdFkGG6hg7%2BTQ3fBbKOruvLgsFDd35FSQKoTewQP3rN9vCobp9mvvZ3FJ7RYJd8M9GYoC8AHHEfT4eJ84m1SwIqxNuAWEj1L3%2F3AgDV83tx0bLZqFakmWY%2BBGQqXGOxkPxuoGxawNWe1BF2CXPEXL6bN6eGFvvAqtaSxwE%2Fo2w3zLtJJkGA%2BZ8rWxKMHOKnj7tdfQ%2FH3tH&X-Amz-Signature=080629e3e5a9a7a56d982aa7cb7b7c9c6b3c3586faa244274f67f3732dae7c93&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Data Visualization Libraries
#### 1. **Matplotlib**
- **Description:** The most well-known library for data visualization.
- **Features:** Great for making highly customizable graphs and plots.
#### 2. **Seaborn**
- **Description:** A high-level visualization library based on Matplotlib.
- **Features:** Easy to generate various plots like heat maps, time series, and violin plots.

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/733d1e42-5a53-4fd8-90c1-3d85254369a6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TJN5E27C%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T041720Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAwaCXVzLXdlc3QtMiJHMEUCIQCfwK%2BvsDcICYRbSCzJ95HcdIwwpgVEaxFA%2BARFn2jH2AIgPHoe1wmxa5BC0aAy5ooMQIMqoEVTlxxS5kLTt%2FSUxVUq%2FwMIJRAAGgw2Mzc0MjMxODM4MDUiDGZ9K9Cy1dcUbipAOSrcA5kc0geTAc%2BmDvMWtB2pMv%2FcNY01EuAtxGazkPCjFoMif8mFWOD%2BjCEGmpMyOeF1PFf8ghlItuQLEj%2BXm2UprU7CskaCA%2Ft7fByMFSY3NKmwY5hX0rDV6At9TkyMlT8xqCE6zXTL%2Fab%2FIQWDyAkaJDWo5xrSvSOIjKJsSSCD%2BW8O0qehQ0emmxdH%2BTF8sXIFxrmT27uR6s5skOXGGqBOhTgtQ2Goc5D18jN1x2RlGiAab0BmODW%2FxgHdCTQDbeiyAlHYKknyy8I46lIRIgFTlr7osRd11Pm6RMcR%2BHB26vMpikxaZyn2w0yBtMgizRlrmi%2FGac62nG9JqNdxTrJqBVCWOno0zq8QkEKqFL%2FmXG%2Bf0cLmuRlBKaYMmMce008%2BR5g9miTeiKmxxqj40v4fkFPUeCP%2F40y1FYTr8uhju%2BCq8kBhtRImYEC93UmW%2BTWz%2FybkqqZ2jB1le7iPtNZbUi5HYgb1QudG0FZTbqNZ8DKZ0YivyjjVA8bYt99MNjsad6ZiREOts8RS6kM2nw0XrXnJeXjHKgCARGokJfcBQlzKM2qJSNLxWVxiu7im668qdBnXBkubPqFsLz74hLIxZARJ1ZtXivmhjPXuYmHDvCrAyOy1gLeiPDq5KFc5MMqhhr0GOqUB980rw1EZkKr735fgkuzVWp%2FGug4hESJUY9c%2BdZvHh5t1KaZTYttUHoQf73c5JK%2BEjkcsV4VPTO7vXD5nDRh9SznkFx%2BbNmwGS6kosHB3%2BV9hV8Y%2B53AoMwigc8qgWra1xUckAHJC4Un4sEYoXx72JD%2FH0%2BAuOZi5%2BwNMgQKrad2BfjGbwisvrJa5GQoW3rh02GuQB3BwGOPXhJ7X1i0qUgTKg5id&X-Amz-Signature=950c4fe0a63c993db710a983ac84ae6991fe769d8e1937d993abff85dfaab101&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Algorithmic Libraries
#### 1. **Scikit-learn**
- **Description:** Contains tools for statistical modeling, including regression, classification, clustering, etc.
- **Built on:** NumPy, SciPy, and Matplotlib.
#### 2. **Statsmodels**
- **Description:** A module for exploring data, estimating statistical models, and performing statistical tests.

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c62885f5-417d-4179-834f-d68f8f2bdf39/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TJN5E27C%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T041720Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAwaCXVzLXdlc3QtMiJHMEUCIQCfwK%2BvsDcICYRbSCzJ95HcdIwwpgVEaxFA%2BARFn2jH2AIgPHoe1wmxa5BC0aAy5ooMQIMqoEVTlxxS5kLTt%2FSUxVUq%2FwMIJRAAGgw2Mzc0MjMxODM4MDUiDGZ9K9Cy1dcUbipAOSrcA5kc0geTAc%2BmDvMWtB2pMv%2FcNY01EuAtxGazkPCjFoMif8mFWOD%2BjCEGmpMyOeF1PFf8ghlItuQLEj%2BXm2UprU7CskaCA%2Ft7fByMFSY3NKmwY5hX0rDV6At9TkyMlT8xqCE6zXTL%2Fab%2FIQWDyAkaJDWo5xrSvSOIjKJsSSCD%2BW8O0qehQ0emmxdH%2BTF8sXIFxrmT27uR6s5skOXGGqBOhTgtQ2Goc5D18jN1x2RlGiAab0BmODW%2FxgHdCTQDbeiyAlHYKknyy8I46lIRIgFTlr7osRd11Pm6RMcR%2BHB26vMpikxaZyn2w0yBtMgizRlrmi%2FGac62nG9JqNdxTrJqBVCWOno0zq8QkEKqFL%2FmXG%2Bf0cLmuRlBKaYMmMce008%2BR5g9miTeiKmxxqj40v4fkFPUeCP%2F40y1FYTr8uhju%2BCq8kBhtRImYEC93UmW%2BTWz%2FybkqqZ2jB1le7iPtNZbUi5HYgb1QudG0FZTbqNZ8DKZ0YivyjjVA8bYt99MNjsad6ZiREOts8RS6kM2nw0XrXnJeXjHKgCARGokJfcBQlzKM2qJSNLxWVxiu7im668qdBnXBkubPqFsLz74hLIxZARJ1ZtXivmhjPXuYmHDvCrAyOy1gLeiPDq5KFc5MMqhhr0GOqUB980rw1EZkKr735fgkuzVWp%2FGug4hESJUY9c%2BdZvHh5t1KaZTYttUHoQf73c5JK%2BEjkcsV4VPTO7vXD5nDRh9SznkFx%2BbNmwGS6kosHB3%2BV9hV8Y%2B53AoMwigc8qgWra1xUckAHJC4Un4sEYoXx72JD%2FH0%2BAuOZi5%2BwNMgQKrad2BfjGbwisvrJa5GQoW3rh02GuQB3BwGOPXhJ7X1i0qUgTKg5id&X-Amz-Signature=d7a4e62d35956a85e3bc46834127291f702b08f1fc223cadca66bf66e3101cdb&X-Amz-SignedHeaders=host&x-id=GetObject)
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
