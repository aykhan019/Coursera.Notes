

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

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/997ac361-58a8-4f04-bb0f-79fea4baa761/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667EQCBYT6%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T161832Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAAaCXVzLXdlc3QtMiJIMEYCIQD%2BkuPsKXuqId57oIuU4UjAW9Bez1SSVgkAOeRK8nPhkgIhANhpcQSluhaAbs8trHneh0h2wvyxbDrMiXYwPuusxDrQKv8DCBkQABoMNjM3NDIzMTgzODA1IgyiLFkuQR06eEGz16gq3AP8tpdz8b0%2F%2FvYrBZrjmXk7%2Fpz3NSclD1T9HdBmineqAHELQ701kY6nsZMxmtOxNWllirBQNDBaPXGO4CzHS1ODMNNabsqMWNXkpzIHQLP3IQUpSLnNC7xKBXFXC8WF6lWVXktR7PSdh5%2F9xrJ6YL7QgOQu3OqCUmMCa%2F6A3XuWuVptb1Cq%2BaAih2Y3%2Fk%2F4QqFQM1oX4M%2BKZIV2O%2Fr1brLWxU0OuYkwuuXrm%2F%2FuLdoJq8N6T4%2BXhxkrHWGcJmVlkoqjZaD7QLPkZEm7oxa7lT5YhKkxKz2Xf%2F3ioporu2FmqXeVkJ8Eup3s3NUQpmgZp32YZmJXLxMwdcwoMC%2Fyq55gHaHE6DNFuH9H7CQ32qK9%2By2ZLHuq2xHGCqWFVt%2BBn%2Fc%2BxK%2FxO8GfUGg8C6R99UNo9WOH2xPHqwEweItuwYL5uTEQaQbYEWryFgeddC%2BjAR5b%2BOwyvbFcxssp8ocOV5UfHefpGyLyo064Ylma4J9W6uqwHDPE%2BEYvpZl7GChe8lz71J1M56CdGc51bo8%2FO7o8J0O82bzmQ%2Fv88pfFI4HJBod8nS%2Bhv9CAL80bdmCuQRgA2FBaWrVnK%2BbShjxO%2BPasgoggsmh0prOKokkFOx1R5G5hvIT60B%2FojRmp9jCIyoO9BjqkAXe5OpMNskp7%2FZMymMK%2F%2FyJ%2BeEnngsKom1TCVkrZmicktcFNOvyzi1dLC1BzaY4zKR1KqyT0yDavkhI25hvQ5GlqW91J8DVZPMFiY7AgYP0UlqmtZzVV58Ukay%2B1TbtLS4JFEjEz49NjdZLYb0elU6LUFhZi7b4wqxYipn8JmKtqo5CjdFvaBdAjuc%2BV1HY6CYjG8RSEV5agcaYp8SzXtE6Huv5%2F&X-Amz-Signature=e983901db325567f7258cc9e3c49fde6785870dc8749f309c5664d220529c502&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Data Visualization Libraries
#### 1. **Matplotlib**
- **Description:** The most well-known library for data visualization.
- **Features:** Great for making highly customizable graphs and plots.
#### 2. **Seaborn**
- **Description:** A high-level visualization library based on Matplotlib.
- **Features:** Easy to generate various plots like heat maps, time series, and violin plots.

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/733d1e42-5a53-4fd8-90c1-3d85254369a6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662YSXHPI5%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T161830Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAAaCXVzLXdlc3QtMiJHMEUCIQCFbdWc3A%2FzQukV6twyxBnTHeD%2F5qdnlR66pBAsl5DJHAIgX%2FZU7siYdBAptlF7pPWgLWhdN9VboExy%2Ba%2BYlX6FQZwq%2FwMIGRAAGgw2Mzc0MjMxODM4MDUiDCZSyC5oddSqpVMapyrcAzk58WETrI9swcKFzzTiOUX%2Bp6GKlBGmypZQKewb%2FAfzlyKxsuBI6N3%2Bhkg1Vj7q1%2F1eEzQTVeqFo3bwPOhQr1T%2BPEFPBdJ44MZrJ%2BCVSEF3QRnlrOfaPHU%2Fxx1HWxusMdbQ%2BmeFbouha2aT2NuYUDg42O7Z8w4WN5Q2EzODQf2sZzBG3S9ITtdj%2BKVwa1uShmNo6Xs35aJhkksWoUSDOzua4oIjNAtF9pnTa%2BNGzegMzMURiEUdP563cK2iZHu135HyBxzJXqkhX%2FkGj5iJdrkx52kdJ0iohOThL5OWEhd9PVdLQO0UARUlMa0%2BxgJi65j6fgOgqC8k11wO364cBpf%2BT9YCGzBi%2BqRBqMAcy%2Fytaz6vNbzuA0wkkhO2uSmtuh11aVnl9i%2F23z8MfGEW7cU5Z5kgmhyViGJjpwTvxeWrdu6t4bXDU10BzMgiSkosIUhq0Ny65LhjQVmjFCCAbMN4Qo67eA5SNnfu5TS3PV9WAkkexvBXm8tT6Eo5rvpiJGi08O97fNoRFtIlVpZ5tZ70X3GXS9ELKWe9FD0dQo6nbj%2Bv5RHmmnqo5MVACQXKrcNfmF%2BPL9ztqubz8289%2F%2FFwjdqkx9hFLgnDh2d4i%2FEUNdK7IPjiZu2%2BSHuXMMvKg70GOqUBNi3qmk25w%2FOjla3yptXjN29W%2FQDIZLc%2FVpLjz8xGj9jVs0MUueHFx2mvxUJHnUhqZ1ZHS8j4p0y2DrXM7QvENuS0niQx12AFky1wjzgr4qCSjJqZAza2r7jFvs%2FM6lb34alz7JxN4Wms4Hvho%2FCRvc6a%2FQ9Z8FYQFKtP6TiZbTuB377EaLkZlqa7MNUpaBBW8l9W0sscHjHbbSuj%2Fc6C3dxjsnKl&X-Amz-Signature=535481c556d2ed182f1b6259928b55d8976cdcdd111e5d9b0d4f9b312e7c4bc8&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Algorithmic Libraries
#### 1. **Scikit-learn**
- **Description:** Contains tools for statistical modeling, including regression, classification, clustering, etc.
- **Built on:** NumPy, SciPy, and Matplotlib.
#### 2. **Statsmodels**
- **Description:** A module for exploring data, estimating statistical models, and performing statistical tests.

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c62885f5-417d-4179-834f-d68f8f2bdf39/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662YSXHPI5%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T161830Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAAaCXVzLXdlc3QtMiJHMEUCIQCFbdWc3A%2FzQukV6twyxBnTHeD%2F5qdnlR66pBAsl5DJHAIgX%2FZU7siYdBAptlF7pPWgLWhdN9VboExy%2Ba%2BYlX6FQZwq%2FwMIGRAAGgw2Mzc0MjMxODM4MDUiDCZSyC5oddSqpVMapyrcAzk58WETrI9swcKFzzTiOUX%2Bp6GKlBGmypZQKewb%2FAfzlyKxsuBI6N3%2Bhkg1Vj7q1%2F1eEzQTVeqFo3bwPOhQr1T%2BPEFPBdJ44MZrJ%2BCVSEF3QRnlrOfaPHU%2Fxx1HWxusMdbQ%2BmeFbouha2aT2NuYUDg42O7Z8w4WN5Q2EzODQf2sZzBG3S9ITtdj%2BKVwa1uShmNo6Xs35aJhkksWoUSDOzua4oIjNAtF9pnTa%2BNGzegMzMURiEUdP563cK2iZHu135HyBxzJXqkhX%2FkGj5iJdrkx52kdJ0iohOThL5OWEhd9PVdLQO0UARUlMa0%2BxgJi65j6fgOgqC8k11wO364cBpf%2BT9YCGzBi%2BqRBqMAcy%2Fytaz6vNbzuA0wkkhO2uSmtuh11aVnl9i%2F23z8MfGEW7cU5Z5kgmhyViGJjpwTvxeWrdu6t4bXDU10BzMgiSkosIUhq0Ny65LhjQVmjFCCAbMN4Qo67eA5SNnfu5TS3PV9WAkkexvBXm8tT6Eo5rvpiJGi08O97fNoRFtIlVpZ5tZ70X3GXS9ELKWe9FD0dQo6nbj%2Bv5RHmmnqo5MVACQXKrcNfmF%2BPL9ztqubz8289%2F%2FFwjdqkx9hFLgnDh2d4i%2FEUNdK7IPjiZu2%2BSHuXMMvKg70GOqUBNi3qmk25w%2FOjla3yptXjN29W%2FQDIZLc%2FVpLjz8xGj9jVs0MUueHFx2mvxUJHnUhqZ1ZHS8j4p0y2DrXM7QvENuS0niQx12AFky1wjzgr4qCSjJqZAza2r7jFvs%2FM6lb34alz7JxN4Wms4Hvho%2FCRvc6a%2FQ9Z8FYQFKtP6TiZbTuB377EaLkZlqa7MNUpaBBW8l9W0sscHjHbbSuj%2Fc6C3dxjsnKl&X-Amz-Signature=9e7d448b7da597448a6a335537bd36b437fa0a7572e6fb90edd1536cca2c8d2c&X-Amz-SignedHeaders=host&x-id=GetObject)
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
