

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

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/997ac361-58a8-4f04-bb0f-79fea4baa761/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664LNSZ2ZF%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T171253Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCTVAPpUJOcFvxtwbL%2BtOd2xpCjueQzEeI%2BNKdiSalZ6gIhAMRuzT%2Bi%2BXk4fGi5Z9fUIRGzHoSdPXlV4BX8dUz9OXdvKogECKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igz4B9mDdk4wyA0YK0Iq3AOJwhTHR310apl4QlR97OD5WcljbVkFgl2zsQ9ava8wNmmbt5AmzIUyKSJGoB18XNQ0LJMLf4JV%2Fj3d6mv%2BsQKNbJij7zkZd1mHJkFfSjx6fzf6xUkBQgfL30nmTN3%2Fy04J6wGwgGIF2PXTHB875LJk3SeuBDIZJGV5aYhYJnl5PA4jkLQdqeOrycF12wkEssGjyqcCjbVFTUPl4lrgUhtoqUjWko3i%2ByqUKs%2FBdjykiIYBTyh8SLMj8AjEp0WTwxl3%2FH5yDk8W%2B%2FrwtfjxUcMTotsAKb2G%2FDd2FrATWzytj4BIcxy%2FmupXQEYjWQLXBjO1RPAnsH0AVoNBUjID%2BghYXKtj7PPlRLBy5C9SbD%2F7OH%2B9BL3AXCqhy6e61a7kgknROvkbqPK8hNdfIACvkOo9IRvfwhBtB2XECqmOnltM2Jfj27wiKAGXAIUcUAB2KDiEYRRJ5Zpt61byido5RbrXHQKqReaQdRejF509tXamM3DNF0roxsty%2BDTHnE7Y7W65auGc87GH63QgW71eylUkxsGslbnNqfisCocq40XkGcL0Dhb6h%2BgS5%2FRv2QR7O2n0jSlzHM3IVfdscztOWbaYNNmqin5J7p3wZ%2BCDheZlmVPQHDp2taklnaIbVjDd1u68BjqkAcY%2BQWbtaNJAeclHXfseFq5IVIJDAr99hg1DcMSwHUfyHGT%2F%2FmqJ1qAlKT2l4i6K%2BITsRmnJ0BPrQ6WyYrx5zENCvojdFGXtYCpAa%2Bi0r0MTzpEVaw%2Blr%2F7i%2Fa%2F5ziJE8E0c8Ku1Dl68OlPy2w8BhUHA78NOGHPbytVKD450cMpPmsTqMmolPxndYnz%2BZOB5GWufbAx9Zs2WcFhbX7WoE51LF2M0&X-Amz-Signature=40dbbd0d4b85e4b23f6c12323bf2f9fbae5e487b46d248080ba777cd5a9a9f07&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Data Visualization Libraries
#### 1. **Matplotlib**
- **Description:** The most well-known library for data visualization.
- **Features:** Great for making highly customizable graphs and plots.
#### 2. **Seaborn**
- **Description:** A high-level visualization library based on Matplotlib.
- **Features:** Easy to generate various plots like heat maps, time series, and violin plots.

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/733d1e42-5a53-4fd8-90c1-3d85254369a6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466S5CDU56S%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T171252Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICyLGWWPosC6oCH1SX4r%2BJAez87zXGOkwD38ohJ6cTXQAiAojPGQ3FpnqfaJDt3EgTJbN9MKT2fV20w7KohcBEwrGiqIBAiq%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMriAx8zizbAHAcpudKtwDClzijvFnKt%2F84e8on1MyA6dsIWm1g9KODPx3MxIPb4sXjREdSP1JDcWiznVd2jjreGSfxaU7cpsvYgQvMhltoDM5OU63al%2BEEuVi7mm1vNcVzlDYI%2BZXSGcrbIETCIXaeDAQHlD1ZzXuYorwMQxYIrNj31ITPFFvYpgpydJJXqJcI2CPAWKJRJhrmYKUiGUisHnG2LdjIVRsY%2BuxFpQei67pDXAKJ62UKaAFKEY2Tl9dRZFTgoSau5hB67UV9TpcNCuQiat3JglBmee8NwC%2B0olflFmLzn%2BMmViw78aiHx3dxLOhg1cWtQHzQ0SKtjMqrOq4fkQNZOMC%2F7bRnFktEe9Xh9oo%2B1fNpgwKZvfUAf%2B3H7qRV7v%2BlhmjjWPotr1DjvSIvQP2zOgG5ksTXjSDBodQNHVg9MaklsUuKmUklW28dVhSIQhWTzYXuK2biAgbUcbPi6rZh33e0QZUbZOrvToXnlEAJf0sgPDbyleOgVCCXBwTzq5OIkSt0dMXe4cT1hgveNw%2Bvo1WgxN2kgXXl4T6dH3KGPPCdSk2Ln7heznV6OOab4BLQ3MRy%2FSm0NFCetQbkBlb4PWH6AJjsf7tnVGyo1j1aaohal%2BCdZ7e5eI8uu3fIWID7Dj4IpEw0NbuvAY6pgEFjHIq%2FBQezgIQfF5angLIKejfuStYhHE%2FmRi4OLYr2T6i5cd86AzdDXBa0ZNL4CWoAOfzG01sd80cxpDP72S5KeO8gSHme9R%2F%2BR9mvFiUQb1BnHC24fBhoIo6x9uth47Nk7dh%2FhkRW2jxYE%2BLvC1rbEXFuVJBvOC1ajaZmAL4Om9gCT5i3gzTr8Cp9HPYE4rnR5C5i2JiCWKjBgC2sM9lCGy7oUHt&X-Amz-Signature=207469766e6eda4aa63d6bca72eac0a47a54c6930b342149f5efd86902f89157&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Algorithmic Libraries
#### 1. **Scikit-learn**
- **Description:** Contains tools for statistical modeling, including regression, classification, clustering, etc.
- **Built on:** NumPy, SciPy, and Matplotlib.
#### 2. **Statsmodels**
- **Description:** A module for exploring data, estimating statistical models, and performing statistical tests.

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c62885f5-417d-4179-834f-d68f8f2bdf39/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466S5CDU56S%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T171252Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICyLGWWPosC6oCH1SX4r%2BJAez87zXGOkwD38ohJ6cTXQAiAojPGQ3FpnqfaJDt3EgTJbN9MKT2fV20w7KohcBEwrGiqIBAiq%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMriAx8zizbAHAcpudKtwDClzijvFnKt%2F84e8on1MyA6dsIWm1g9KODPx3MxIPb4sXjREdSP1JDcWiznVd2jjreGSfxaU7cpsvYgQvMhltoDM5OU63al%2BEEuVi7mm1vNcVzlDYI%2BZXSGcrbIETCIXaeDAQHlD1ZzXuYorwMQxYIrNj31ITPFFvYpgpydJJXqJcI2CPAWKJRJhrmYKUiGUisHnG2LdjIVRsY%2BuxFpQei67pDXAKJ62UKaAFKEY2Tl9dRZFTgoSau5hB67UV9TpcNCuQiat3JglBmee8NwC%2B0olflFmLzn%2BMmViw78aiHx3dxLOhg1cWtQHzQ0SKtjMqrOq4fkQNZOMC%2F7bRnFktEe9Xh9oo%2B1fNpgwKZvfUAf%2B3H7qRV7v%2BlhmjjWPotr1DjvSIvQP2zOgG5ksTXjSDBodQNHVg9MaklsUuKmUklW28dVhSIQhWTzYXuK2biAgbUcbPi6rZh33e0QZUbZOrvToXnlEAJf0sgPDbyleOgVCCXBwTzq5OIkSt0dMXe4cT1hgveNw%2Bvo1WgxN2kgXXl4T6dH3KGPPCdSk2Ln7heznV6OOab4BLQ3MRy%2FSm0NFCetQbkBlb4PWH6AJjsf7tnVGyo1j1aaohal%2BCdZ7e5eI8uu3fIWID7Dj4IpEw0NbuvAY6pgEFjHIq%2FBQezgIQfF5angLIKejfuStYhHE%2FmRi4OLYr2T6i5cd86AzdDXBa0ZNL4CWoAOfzG01sd80cxpDP72S5KeO8gSHme9R%2F%2BR9mvFiUQb1BnHC24fBhoIo6x9uth47Nk7dh%2FhkRW2jxYE%2BLvC1rbEXFuVJBvOC1ajaZmAL4Om9gCT5i3gzTr8Cp9HPYE4rnR5C5i2JiCWKjBgC2sM9lCGy7oUHt&X-Amz-Signature=56e166cd4c9aba370d9a26e996998b40715a804ce93358a00e6457c3d6ee453d&X-Amz-SignedHeaders=host&x-id=GetObject)
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
