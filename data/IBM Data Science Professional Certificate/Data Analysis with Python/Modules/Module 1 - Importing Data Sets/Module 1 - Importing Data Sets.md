

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

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/997ac361-58a8-4f04-bb0f-79fea4baa761/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46623LRYOK7%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T171242Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGwUQERwocddI3i8mUEwjn953HC13l3r3Qu7pQBbRcImAiBh41G4eAppZbFq9dOSt2r1p8zxLx5rT2qAF2F0HaPTKCqIBAjt%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMZivourU3vprIRH75KtwDIRT1rNVvaMguikMoS%2BT%2BGLD0oXM%2BQ1LHXL4jH9%2FvdvSB%2FEh98df5YdHktAKBOcr3703ENnULudXrf%2F%2BZmdQsIHkengw71qLBkJUE5svzYsIpWvpNvm6c9UQq4HUt%2B7DnPFXuwnCzrMPxTCJEXJv%2B%2BJq%2Bxnl9HpbWWU%2F%2BZz%2BiL0z8wMx%2F%2FWWgUSuP8gyTVV4TF5%2FIvtrTFAh8wCweAGkH7WcO4hsEG6IFdk10l7VurQ6S8tJrPf26VSccl2ERKHwZWY49T1O7lO0nc%2Fct%2FI6%2FueL71%2FZNAiyfJAHUP3jnh4kTJNqF%2Bjiuabb%2FLSBVdtNrL1ZHgKS0ON%2FWmQ9vWtw0qaV4Kxt7Ba1Wsktc%2FMr2KLYs6iJ9DJm%2Furip25OrOFzVDxhf145GO%2BlARXxkw1SukKCh%2FgnOdFtr1dEMMpRLztI3tRjIqeiQXxd1rX%2BoYvkAydiCniEav4%2BPulpw%2BK8zn%2BY%2FF0QT9F4T1y8REW%2F0CeN%2FJTqyGp7QlYMvu4XWRZWQXIvOYi2jLZd1CuKfrG1P8GJdoAbMs22LZ85sxSyHyHrw7WE4gv5NVLpx8OVYdd5b446eJo73ngfn74gNGwpxCM23j%2B9J9%2FeVURnqJeT7iROm%2FhnwVk3UZGcjFmEwnrj9vAY6pgHM%2Bm5gFqDz0mOrYI4tg7jqt5sk78NfG4G0KR%2Bl4IsScVz2ksWXFCM4JHCcxPlinU8tMujSUsWrqinoa8im%2BPLrScFK7HkjM0Fl296pPrb6EUjcAB8LEEp91A9Ko8T4QSEtu0VqVBQ81zl4seDc83mmDqEk6GRFYB7PL0PrN7OW96FprpqAVsVa2j4WQKJcSIwl2tD65ZbIc9wU%2Bo2rV5PHp78vUMFu&X-Amz-Signature=603e873abc6b383af2d61d01f34ce664c1d8713d866ebb9a1c791f94435b88b3&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Data Visualization Libraries
#### 1. **Matplotlib**
- **Description:** The most well-known library for data visualization.
- **Features:** Great for making highly customizable graphs and plots.
#### 2. **Seaborn**
- **Description:** A high-level visualization library based on Matplotlib.
- **Features:** Easy to generate various plots like heat maps, time series, and violin plots.

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/733d1e42-5a53-4fd8-90c1-3d85254369a6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SQH5D33A%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T171241Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIAdhOfz0mlQnc3WYULceuL2JmZ09%2Bh5XBCi9oCNQ%2FjZWAiA2rNOJb6bYSJ5rNmfa%2BG4m2vOZzLJ0bO5u%2B%2FOEIowsPCqIBAjt%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMad5lFD7zQGtXxCziKtwD%2FV6f0oDiD7YCee%2Bz5F9pqCWHu73l36D%2FG%2BgJHyTvI7uD4I18qUz4wou8yUzyyZCM5kaVy5dVOKY6ddp6v71KPpQksAY59OyYWS9ny8De89EmyCckSICpR60yuoqkjZ1R8dMfHHVdPn5qFK3wVduR3F3xLTKUj83LLTw9cEu87omIQzEh1XYGfPQA3TgmFr4uAGnKwOpauIhAssJAc0JM3U3iH5eQiVsNZfMbMxTs3G%2BHdvNLX%2Fg1D0%2FiFFB5ZJm6LvzcQLFQ9NRGrDI0XDzfCt9HW%2FjvHh8%2BQ%2FGBgmboTQfSxQ%2BvTZgkxTvNRAgw4vnELyShEoapHAly3JgCXly8SAHdHd9XK666Y7xWxY6%2BpM%2BdRW%2FWc47hXAuv%2Fu%2FyUOByVYbPDW4NyxuCGkuNmgJAKH%2BvITHT665MXW4kA6U0gv3jMnWU1lh5YPKnYL4fW2roOdk1ZYcpXTBz3vf9OguSpIYIQQWQpO3j06uAmydQR0Dx3eXGl9V1Ky%2Bdd5VjNFIRYhYC05OXq9H6t9A7ZsZ1Qdas7kMWlXEKHyteeI29MPfHYJnqpFKiq0T45CBw%2FnXQE7H9hBCJy90VQBB8JGmvLqUqJCjJjpbUXM4kWzqwKWIsoo7fm3V8Y39prCAw2L%2F9vAY6pgGhfXQDPv4Lob8m6NvEjP2SCgIVOTQxGrE75fQ3QqrmAQUK1EXI097w%2Fb2PQy4r2EvcskEE0qEHejWv2OtK1SFv%2FLp37oGY%2FxsEldD1SYHY5PA7vv%2FKmSoyyg%2BCuIs%2FK76gzw2jos9BA6Xs3rSwlYBK0GdbXAEmuhUiBuvWiMOoZUE5njdNJ9D2DaGaeyLxELu4%2Biv0w5WrfyeH1cYdmM3CWcWtF8h3&X-Amz-Signature=7b75208e373b04a81c5c21bc1a35a5c5714e56007b4e6b6a7097e1e725b36c96&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Algorithmic Libraries
#### 1. **Scikit-learn**
- **Description:** Contains tools for statistical modeling, including regression, classification, clustering, etc.
- **Built on:** NumPy, SciPy, and Matplotlib.
#### 2. **Statsmodels**
- **Description:** A module for exploring data, estimating statistical models, and performing statistical tests.

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c62885f5-417d-4179-834f-d68f8f2bdf39/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SQH5D33A%2F20250202%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250202T171241Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEOT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIAdhOfz0mlQnc3WYULceuL2JmZ09%2Bh5XBCi9oCNQ%2FjZWAiA2rNOJb6bYSJ5rNmfa%2BG4m2vOZzLJ0bO5u%2B%2FOEIowsPCqIBAjt%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMad5lFD7zQGtXxCziKtwD%2FV6f0oDiD7YCee%2Bz5F9pqCWHu73l36D%2FG%2BgJHyTvI7uD4I18qUz4wou8yUzyyZCM5kaVy5dVOKY6ddp6v71KPpQksAY59OyYWS9ny8De89EmyCckSICpR60yuoqkjZ1R8dMfHHVdPn5qFK3wVduR3F3xLTKUj83LLTw9cEu87omIQzEh1XYGfPQA3TgmFr4uAGnKwOpauIhAssJAc0JM3U3iH5eQiVsNZfMbMxTs3G%2BHdvNLX%2Fg1D0%2FiFFB5ZJm6LvzcQLFQ9NRGrDI0XDzfCt9HW%2FjvHh8%2BQ%2FGBgmboTQfSxQ%2BvTZgkxTvNRAgw4vnELyShEoapHAly3JgCXly8SAHdHd9XK666Y7xWxY6%2BpM%2BdRW%2FWc47hXAuv%2Fu%2FyUOByVYbPDW4NyxuCGkuNmgJAKH%2BvITHT665MXW4kA6U0gv3jMnWU1lh5YPKnYL4fW2roOdk1ZYcpXTBz3vf9OguSpIYIQQWQpO3j06uAmydQR0Dx3eXGl9V1Ky%2Bdd5VjNFIRYhYC05OXq9H6t9A7ZsZ1Qdas7kMWlXEKHyteeI29MPfHYJnqpFKiq0T45CBw%2FnXQE7H9hBCJy90VQBB8JGmvLqUqJCjJjpbUXM4kWzqwKWIsoo7fm3V8Y39prCAw2L%2F9vAY6pgGhfXQDPv4Lob8m6NvEjP2SCgIVOTQxGrE75fQ3QqrmAQUK1EXI097w%2Fb2PQy4r2EvcskEE0qEHejWv2OtK1SFv%2FLp37oGY%2FxsEldD1SYHY5PA7vv%2FKmSoyyg%2BCuIs%2FK76gzw2jos9BA6Xs3rSwlYBK0GdbXAEmuhUiBuvWiMOoZUE5njdNJ9D2DaGaeyLxELu4%2Biv0w5WrfyeH1cYdmM3CWcWtF8h3&X-Amz-Signature=7bd5edfb9321b63562d0ea3dfe6837001a17a09fdd7c4d1f14387b98d844d66b&X-Amz-SignedHeaders=host&x-id=GetObject)
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
