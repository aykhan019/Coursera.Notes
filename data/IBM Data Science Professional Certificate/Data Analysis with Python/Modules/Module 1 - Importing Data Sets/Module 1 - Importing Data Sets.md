

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

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/997ac361-58a8-4f04-bb0f-79fea4baa761/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666WF467Y3%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T221403Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDIaCXVzLXdlc3QtMiJHMEUCIBcNS7nMsTM6J7H4bm%2BpwAF4pd4reL0TPMBHJIlN6q7gAiEAmjtke%2FgVjLorRrfNmzRUS2EsdmWChnzoYPds2jdaSuoq%2FwMIShAAGgw2Mzc0MjMxODM4MDUiDAD8NitBwDx%2BSYkiCSrcA0675UVKvsn6PJQXdIlnSsvSlgETQX%2FgyQFtTT0NJ0RABBEUxPhCPOTKUofx6bsOITp%2FsxqZL9Lee6muyZXJv1jP4RoPxixtJeGFtcp3nOINMincAEU%2BSmsQNzZ1EODq7n66dxHwytNl7506P3oNZBYT%2BwHb8iexVzuM2QzuuxtiS7OmelPfif9GlduVMJNhjLupPuSAJEKT7gEDF%2BmxgEWHM6F%2F%2Bxq4oyRYjHovv5I2DSZg103HlOBa0VhUrccxVyVdM0sveDvVmwVGWd2peKIV6t1%2F0eSRRcv9x2xBOQW2%2Fiye%2BB0XqcU8kyQgSd%2FWx1qQGYVJUSlgeKlZnHrmTvzH%2BA0MlAKNpwUhzwsB74Ka3RgGrmHbBxw9qSh4QLrXLqxax8QPo15xB62xWzd2t%2BurfmgK1New9wfSqT%2FkeWxmNNcwnFSoGNubpeduhx8CGVSkLhu5Vx7ju16uNiqWcVnOoLHJtk%2BBOKK6lhekAWLS96kwHlc6a7DxknKqzdSqTF2cMJPJ87nrYmEWfX8QDSqR4BhBMsnKoe4foRm1MmdsxkiwgBTazztggwGjknjMEZkr4MBO03GrHN%2BCgwAtkMlCYzMspEhqyghyeBim%2FXWTzT091sGUOknxJj6aMOe6jr0GOqUB9n8HHbRWvMg8L09zOud3H%2FzHIT6FclLd9Tmt5BswPLczjh%2BUu2CFDCCa7m4K8W%2BcTOofc5GbeKNQTuo64%2Bc7I7k3qc8zO3jM%2F97p4OhpmMR%2BVBIUzO172cyddrSuGHrp3QMM06i4dsIoTZvOkNOQO7Trj3Nw6r2ykQ%2FBPBvg2v3Ox%2BzwLDqQ249nYt2yppcevKs2yUzfnbDGioiWBGP5lt6W4Ulk&X-Amz-Signature=3852417fafced1b88d1bdf0bf1baad703507cec2c04f28d12c3d51e54d01de36&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Data Visualization Libraries
#### 1. **Matplotlib**
- **Description:** The most well-known library for data visualization.
- **Features:** Great for making highly customizable graphs and plots.
#### 2. **Seaborn**
- **Description:** A high-level visualization library based on Matplotlib.
- **Features:** Easy to generate various plots like heat maps, time series, and violin plots.

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/733d1e42-5a53-4fd8-90c1-3d85254369a6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664HYLPLJ6%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T221402Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDEaCXVzLXdlc3QtMiJHMEUCIQDcSoLstEVNL7TdFGnKv6MYtW11UfYcQMRsav1Frs%2F3BwIgOD7xCkjO32zTTOz%2F%2B5fSV%2FbspNYBdcGGbXWUUdkYGk8q%2FwMIShAAGgw2Mzc0MjMxODM4MDUiDAVXVvi9400RbpI4RyrcAyfrZmtsAjttv4qcCd50iVrNB%2F1bHDIVWBAk0Et1%2BhRURQVlBQ1y70lhHPtc2KgL8v24DEMYDXB2Q71peibXZVyV5IUoM4fXBWRl9lvxO7yuhYLWM1Ypd%2FTlRq0jeXPnzLkv265DqQ2SMlzs7hSLQOkRmStZTAGknHYXKAqbqgCjqyaFtTF%2BiR8LJO2hj17zBPrnrLgOR6leXVQpNqt8LfD3vCHTe%2BD2TCqlmPhT0X9xKS9KJhpi%2FNEtIUSHz5YjA032ST%2FUE4bnB6%2FaM2ylesHjYEJt3Ow7sK0B79ScnDe9QgDd68B3OJUpGhlXOrBwiMaQ2DQnngWm4DYQksnGRUpjGMQ7LHByluo%2FE%2FRnO%2FL40AGfqHkOFP%2B1uhUr67Z2Lxu51ThF3WDuiP3%2B%2Fi1spQ9R4OuyC%2BlbBNSjjLORKsL9U5YHB4zX3cv3%2B6xi7gFUC9PGXX%2FQgq%2BMMQsBn79%2Fhobfh8sRwbMoC5nRTkeBMSR3MGS50vyYkYSMUXXeL7hpO9bL4AkF%2FfnK4jz8QkS7FM6WLfer4eDrrE7tWAptonXPWSgPBN8nXLNswJzHb9t08gNz%2FvE4koasdOgLn57tv%2Bjef%2BJbebJR%2Fsm6cjmEZbXT1tDuqF3V1h5YlNO5MK%2B6jr0GOqUBoHtU49Wfez%2F8D4vk109qCtKxk6fCD6cI6HiHYKMU%2Bf1lc3eZgoRXqR6UMgZ1aKJ3Opzvm9cvYYN6%2FA3d5bsHmBAq31hzqnzjSU38gDvFDC6revZqOa6wuMLPR9ibs7GwjDk4TIog485Qxru2lzewsbrZfw1oqauuuaTmGL85IFcC1BqfJcy7jH84%2B8rvhaBDkIf6JJgAsz1af%2FMpz91pr7mx%2FT4%2F&X-Amz-Signature=36a053416db680cefe5cf8b622d615ca782003bc12b9f6c7298c86871f9c7693&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Algorithmic Libraries
#### 1. **Scikit-learn**
- **Description:** Contains tools for statistical modeling, including regression, classification, clustering, etc.
- **Built on:** NumPy, SciPy, and Matplotlib.
#### 2. **Statsmodels**
- **Description:** A module for exploring data, estimating statistical models, and performing statistical tests.

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c62885f5-417d-4179-834f-d68f8f2bdf39/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664HYLPLJ6%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T221402Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDEaCXVzLXdlc3QtMiJHMEUCIQDcSoLstEVNL7TdFGnKv6MYtW11UfYcQMRsav1Frs%2F3BwIgOD7xCkjO32zTTOz%2F%2B5fSV%2FbspNYBdcGGbXWUUdkYGk8q%2FwMIShAAGgw2Mzc0MjMxODM4MDUiDAVXVvi9400RbpI4RyrcAyfrZmtsAjttv4qcCd50iVrNB%2F1bHDIVWBAk0Et1%2BhRURQVlBQ1y70lhHPtc2KgL8v24DEMYDXB2Q71peibXZVyV5IUoM4fXBWRl9lvxO7yuhYLWM1Ypd%2FTlRq0jeXPnzLkv265DqQ2SMlzs7hSLQOkRmStZTAGknHYXKAqbqgCjqyaFtTF%2BiR8LJO2hj17zBPrnrLgOR6leXVQpNqt8LfD3vCHTe%2BD2TCqlmPhT0X9xKS9KJhpi%2FNEtIUSHz5YjA032ST%2FUE4bnB6%2FaM2ylesHjYEJt3Ow7sK0B79ScnDe9QgDd68B3OJUpGhlXOrBwiMaQ2DQnngWm4DYQksnGRUpjGMQ7LHByluo%2FE%2FRnO%2FL40AGfqHkOFP%2B1uhUr67Z2Lxu51ThF3WDuiP3%2B%2Fi1spQ9R4OuyC%2BlbBNSjjLORKsL9U5YHB4zX3cv3%2B6xi7gFUC9PGXX%2FQgq%2BMMQsBn79%2Fhobfh8sRwbMoC5nRTkeBMSR3MGS50vyYkYSMUXXeL7hpO9bL4AkF%2FfnK4jz8QkS7FM6WLfer4eDrrE7tWAptonXPWSgPBN8nXLNswJzHb9t08gNz%2FvE4koasdOgLn57tv%2Bjef%2BJbebJR%2Fsm6cjmEZbXT1tDuqF3V1h5YlNO5MK%2B6jr0GOqUBoHtU49Wfez%2F8D4vk109qCtKxk6fCD6cI6HiHYKMU%2Bf1lc3eZgoRXqR6UMgZ1aKJ3Opzvm9cvYYN6%2FA3d5bsHmBAq31hzqnzjSU38gDvFDC6revZqOa6wuMLPR9ibs7GwjDk4TIog485Qxru2lzewsbrZfw1oqauuuaTmGL85IFcC1BqfJcy7jH84%2B8rvhaBDkIf6JJgAsz1af%2FMpz91pr7mx%2FT4%2F&X-Amz-Signature=28657cdfa76ac56eb44c125e472526afb008c7a603ffaae6435123372c7e7b08&X-Amz-SignedHeaders=host&x-id=GetObject)
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
