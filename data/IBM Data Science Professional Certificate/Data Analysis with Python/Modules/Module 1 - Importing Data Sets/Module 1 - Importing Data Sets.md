

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

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/997ac361-58a8-4f04-bb0f-79fea4baa761/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YWHFIWXH%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T031631Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGsaCXVzLXdlc3QtMiJHMEUCIQCs5m9GQgJE3z7oq9sPHduNLtXD88eyS1zuLr4Thss91AIgPgRC26WqIiy4vS0xDMZj9HHBgm0AsysBphyMGraPyy4qiAQIhP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDC8uRYf75Lr3PM7poyrcA23REFBrFsLymgGI44xMVrfMWSSExwN6qQAaW6Bjk3twDi3wiZJ5leblTP1cNPohn1%2BsDkrdNE4u1Nha7qTE5hl6RKl8aiYUSNUMtRC8CCwylsUu7e31vGkc%2F3MasSyB4n25TV514Kt3DV7Lldy9caly9itGN44NERlD3G0b0EQIEueLXdPPOeoqRhyLA6YPY%2Bvj72d5sKAC%2FQGHrhsJOT80mzXcleipuL60T1cq0DRyXzGM7NwXuUD8csk%2Bfky%2FR7CxTQO3WHbfv1zb%2FOeAjGFGdFmUJ%2BeHcDM1LRZ0H3GGChCEJ4BC8lKjBt4WEfJeydcwgJ0pBBbZZKIARYI7b0bthMiw9j4h0em3%2BrzY0pzdt2STfcdwHhvwMijp%2BkZUlmdvSnyeCw8cgtAseBSuIatYRtfvi7D8O9L4h%2FIfOmgGgFMjyYjIB6oOGHe7vsms%2F4BUpbL3rcJoIAAlcM6vIqDZ%2BgzTZVIBg6B%2Fj6zNoxTBn29LrIs439XpzcTAHUM5cgrHjvqEm9n%2BAioC5wZvV0x4BacIugm7GqUCw%2FrsoweS%2B6PD%2B3ubavt5OUjOHVvPoMMBaB%2F9GMLEijV15ry3EYEG4BEux9XKb%2FxVhjDKqB5o7bTFS74wB7eeIsDyMOSVm70GOqUBaRl1xKSU%2FFbXvufHHd19Ho5t2cyav26SN7ee8sPMqtC7Kid62jJY6pyhJaMhhY2hGnpIqShss6vyvgInA%2FJrDTxx9nutMQYi1FnqVLH9Kwokn%2FzMGp%2F6vRaphik64DOfr5fHV%2BP99nj1IpMjhY6Me52u%2Bf%2BzGDKJvPVbqy%2F3KUAjHxJTjnDt9C2Zrws8AWLIoEV5q9ysXBCb3oOM9JtYQ9FnXJTZ&X-Amz-Signature=08088101efb4045821a43d5b866a32012c00a2eababb1daff679e4f694c8c59e&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Data Visualization Libraries
#### 1. **Matplotlib**
- **Description:** The most well-known library for data visualization.
- **Features:** Great for making highly customizable graphs and plots.
#### 2. **Seaborn**
- **Description:** A high-level visualization library based on Matplotlib.
- **Features:** Easy to generate various plots like heat maps, time series, and violin plots.

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/733d1e42-5a53-4fd8-90c1-3d85254369a6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XKCWCAIR%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T031629Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGsaCXVzLXdlc3QtMiJHMEUCIQCUdHeMSKxAfp36uWts0cPmuF7B4WhkSlHbvRZfcLPX%2FgIgcQjH8o1SVTvbjtVZ0N1pUOUPo1yo4D5tlC8atASa4eoqiAQIhP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJzDa0nN2461O9nLBSrcA5wsI4JxNVexs4YCMsnbYwKSCJHbT5ha3D2IkE%2BudzxaTlXhU8y74F4vE9gNBzMA%2F6gqMvCZ6vrC%2Fx3TfMxCvjvcx7khDMdFVMVfUkEzY9ZNPHafg5URkiMNjWqDWmkmuiKFPTvz55F5MR0n1i1IMRo0XijRvQF0yguUDQZobUlo%2BYWxK2rswZjT3w1MsMG46fV0OyaS7aKGl0jN%2BRPDwReiU6fn6a%2Fvn4CMsLx9YllH736KMfjGs8f0EdfUPo%2Bh69cvX5BW4LCbWsF0a1hrhEvgNzsQGRI9t3NK%2FfhBrpb5hYj%2F5GQ%2BnYMCiirHKg3oH6HTcY5WBdTuPvQeaNbvJnd%2Fy70Nx%2FGwThoC6wxa02G2y5dXmHwV8T6%2BXShpwcUIa60Dic7ZhswCj1cswzKzVavL7wsW7F553KAtT%2B165mD%2Fv1qzpmZnmhLlZu%2B%2FNkIl%2BFivDEstBXIEGGqzi0qeccbYDshLzcjz1Mx3F0Fns6RgQP5gnmY2zVK9hJmPOQLdGZT4%2BQJLzLxMjo7HanExRyWpbbH%2Fex%2FZY1l72bRnHzSq%2FtYYNBn6Hbg%2BvUWIeycgacWtdeG1q7do9u0oXP%2BtWiO%2BPGN5dgqkRCKHdX5rSfsZO%2BficPbJhBrfJ22QMKKWm70GOqUB7N0Moez92ifVcehljogg2JxQNZNxIUph7ca3dm1UeSWtGAyJbQ5ae7jSD%2B3ssABbtoM0kf4VvFy9%2BmsYUeMHA0xfFrLqyQemAAPyv8%2B59LP42wFy1QEHll3I9DAbmEDUQI%2FzVM0FXLkVovREIlX9nR4pmYKXmYYTGC4sU01UQCuEFWi7VQXGpDU6%2FhKXV6ZmFi7kyO1BcoAZYiO8SvhDLGGxNu3f&X-Amz-Signature=603c87fc9a7a23e50b9a032d906d8a1e5a85ad0a73ba5a0798ffbf54022f9f86&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Algorithmic Libraries
#### 1. **Scikit-learn**
- **Description:** Contains tools for statistical modeling, including regression, classification, clustering, etc.
- **Built on:** NumPy, SciPy, and Matplotlib.
#### 2. **Statsmodels**
- **Description:** A module for exploring data, estimating statistical models, and performing statistical tests.

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c62885f5-417d-4179-834f-d68f8f2bdf39/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XKCWCAIR%2F20250208%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250208T031629Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGsaCXVzLXdlc3QtMiJHMEUCIQCUdHeMSKxAfp36uWts0cPmuF7B4WhkSlHbvRZfcLPX%2FgIgcQjH8o1SVTvbjtVZ0N1pUOUPo1yo4D5tlC8atASa4eoqiAQIhP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJzDa0nN2461O9nLBSrcA5wsI4JxNVexs4YCMsnbYwKSCJHbT5ha3D2IkE%2BudzxaTlXhU8y74F4vE9gNBzMA%2F6gqMvCZ6vrC%2Fx3TfMxCvjvcx7khDMdFVMVfUkEzY9ZNPHafg5URkiMNjWqDWmkmuiKFPTvz55F5MR0n1i1IMRo0XijRvQF0yguUDQZobUlo%2BYWxK2rswZjT3w1MsMG46fV0OyaS7aKGl0jN%2BRPDwReiU6fn6a%2Fvn4CMsLx9YllH736KMfjGs8f0EdfUPo%2Bh69cvX5BW4LCbWsF0a1hrhEvgNzsQGRI9t3NK%2FfhBrpb5hYj%2F5GQ%2BnYMCiirHKg3oH6HTcY5WBdTuPvQeaNbvJnd%2Fy70Nx%2FGwThoC6wxa02G2y5dXmHwV8T6%2BXShpwcUIa60Dic7ZhswCj1cswzKzVavL7wsW7F553KAtT%2B165mD%2Fv1qzpmZnmhLlZu%2B%2FNkIl%2BFivDEstBXIEGGqzi0qeccbYDshLzcjz1Mx3F0Fns6RgQP5gnmY2zVK9hJmPOQLdGZT4%2BQJLzLxMjo7HanExRyWpbbH%2Fex%2FZY1l72bRnHzSq%2FtYYNBn6Hbg%2BvUWIeycgacWtdeG1q7do9u0oXP%2BtWiO%2BPGN5dgqkRCKHdX5rSfsZO%2BficPbJhBrfJ22QMKKWm70GOqUB7N0Moez92ifVcehljogg2JxQNZNxIUph7ca3dm1UeSWtGAyJbQ5ae7jSD%2B3ssABbtoM0kf4VvFy9%2BmsYUeMHA0xfFrLqyQemAAPyv8%2B59LP42wFy1QEHll3I9DAbmEDUQI%2FzVM0FXLkVovREIlX9nR4pmYKXmYYTGC4sU01UQCuEFWi7VQXGpDU6%2FhKXV6ZmFi7kyO1BcoAZYiO8SvhDLGGxNu3f&X-Amz-Signature=bd148534f434b9d744b14322d325645810e20b369e2d0942a09afc79574590d8&X-Amz-SignedHeaders=host&x-id=GetObject)
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
