

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

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/997ac361-58a8-4f04-bb0f-79fea4baa761/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667XMPX3NR%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T031813Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECAaCXVzLXdlc3QtMiJGMEQCIGzDgN7X4GGg3N4r7D3iTksgSrHkUG9sKWsILWprO1hHAiBmg5jkL5PLctnqL0Ot3EZvMVQDpr2z%2FdWYkzsUe%2FuYWSr%2FAwg5EAAaDDYzNzQyMzE4MzgwNSIMSVe7wZehi1XI47fFKtwD5HLzBict5nwzuy4vckH0NiVtTxTmqHGQu%2F2HNhopxbw5ZcWsQ0XPcD0MmSxZkcDPry9OSsXFDXOzzcnGPrU0rivLxoUlT20WnJ04SU3pAyUv3Xu1GrG8z6FNOmwBL4BSzICSCCgfBgad2rgkw0%2BA1CneUz%2FmxN%2BA%2FigD9fTZdCd5JfE3Q6OeA6uV%2FH8jXd3e4N3GXFFfF%2B0eRCgXK3R7jqf9pYLSxJe6xgtB%2B4hLFOxyVPM8HywA1IM%2FrI9NIQDMs4a6UR0kq0wyy0a%2FQ4PjAyJb063Wmp4DmAH4UdQe4xGz36mhcJc3XQCytUwutEPvH3WnjBRC9LkpnWT4paJ4KCmid17fZ7cTda%2FH7tgOIApkVwpOPryg6gX3auU%2Fh%2FesM4gvP3nWQ2ebFKlAYRO%2BL%2BR6fwKYx%2FSHt%2FD0kuNJxJaTgkxpmr4Yxs%2F8qmgZGVHpavJjzabDkxSXroqaF7zBTsXTMd6PuTpVnOpBGuLx6goKCqORo98xWTjtqXazPENWzkA8HWbmX%2FMrqENRF3LRHLVGGYK3vXazbT8zcZ%2F%2BA%2BO%2FYddGIzVBD383B0p8NsyoZTFP7OqdtBVF5xNgdNpD15Ex88XTfKdsSJ2XF0fTtoy3G6U0Xh5VQXFJtNww1s2KvQY6pgE592WXCCxIeHeH7cIhCW76N1H2jkUKLHx4ei4rJ3sQGmx67tRz%2F%2F8WoR2780btFu5DFo3FoZtFTA1orGRo3eeUlQivB0xYCnSJQxFSmllkXZNkGtRq0Sb85df97jzfhBtqHZtEpudm6sPxHzw3NCm%2B2uEHmY%2B8oyIsP65oSfeB7VGvKTN%2FJ87vcvjzIp%2FQC5Zg0nDhJT9IkUj%2FV4EALlz5GyKhvDOb&X-Amz-Signature=212cdd7e034d9946f3f27d4cf13d74f3110fd3cc88da4ad059f38a44c13de39d&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Data Visualization Libraries
#### 1. **Matplotlib**
- **Description:** The most well-known library for data visualization.
- **Features:** Great for making highly customizable graphs and plots.
#### 2. **Seaborn**
- **Description:** A high-level visualization library based on Matplotlib.
- **Features:** Easy to generate various plots like heat maps, time series, and violin plots.

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/733d1e42-5a53-4fd8-90c1-3d85254369a6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663T5JP5O7%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T031812Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECAaCXVzLXdlc3QtMiJHMEUCIAVFKqvu7uMrNxqg8fYetwm4ZMRGj1v0Wi%2B%2B0zbHdww0AiEAwwqpAw3WR9fmpna6nTUulFyfffrRURu7owjUhIAirscq%2FwMIORAAGgw2Mzc0MjMxODM4MDUiDJIO7MeMbRJ%2FEOoK6ircA8BEd6VqCG2aiuk7BcOPD2iQM%2BJjA0BT5p13Wkr2alp%2FSSQXD8KyfckrwHpQZBMuS%2FldWkrszOy2ijUdxeRDrk0E09%2BiK9CjSJu7pC41NMOtXZmUNRwCva5K%2Foe0mhhNn4aWPGha5FtVQDc2v%2F5t5lTQZWuH574mt5mnk%2FMR2pJk7XMDu11mYWs9er%2Bl4oqqmI5fH6O6jA4Js3bj3nrAwWzkBX6LK4Hf5taFWbvPARYLRimDKDvnqjtaqhNLWxYfS8Ur0GjBfFJevYjNh21wWBYnYx2bb1XRJbWcwzpeNsM3Vr8fOs18eVbU5HNXxwqPsHMG08iMPCi4GQZ9fjRxIhxc%2BtTkwE5glDkJjUHiFoxjBr7625i72CYv9Ekar4McOBwtU%2BHvsgdyT3jYZA2vaRqfNnPpjYEeA6IQ8GzuNLfXfRi3mE1cttG342qapHLTL6vpY%2Bvka0BBHqCbRzyjQI0EBLJnn0%2FmkmcwJLINALRTWvCCVbKcRLkR7AGySQvtaR3oz%2BFtblSUHHAYpn5FyLsj6vbAo7j23E%2F6lg%2BFRwlLaM%2FW1xuGURNmxcmHyPHUjPQKvXsGVO%2BJhniIGvhGX%2FYAp%2BUmwLvYJFKp9uNZtzHQ6PVqQ3Vxt3hKTNvpMJDNir0GOqUB%2Fw1McQH1ruUIsskn29gE2DC4oDSIJ%2BcgrY7CBS1qlOyqyvNvXjfWRi12BklSePCP3cAsW4JgeBKAMhJpE2dykZhQPuXNZzT8iqkT%2FA96lJ1Q2ANM7ktX0RPT21Ipv3KHu7WIoJQNLIJJ%2BeVxHvSVKm3VNLJAmi7UyfFMIdLSnbuKKL2SzwUa4G9jU%2FQjgPSqHw3htxW%2FELtLSyLixledyypfIS%2BY&X-Amz-Signature=1aec34c66ecb8d0fd76e52dbe2ae2078b5b0e47f247fb333303ac7dc191a6233&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Algorithmic Libraries
#### 1. **Scikit-learn**
- **Description:** Contains tools for statistical modeling, including regression, classification, clustering, etc.
- **Built on:** NumPy, SciPy, and Matplotlib.
#### 2. **Statsmodels**
- **Description:** A module for exploring data, estimating statistical models, and performing statistical tests.

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c62885f5-417d-4179-834f-d68f8f2bdf39/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663T5JP5O7%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T031812Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECAaCXVzLXdlc3QtMiJHMEUCIAVFKqvu7uMrNxqg8fYetwm4ZMRGj1v0Wi%2B%2B0zbHdww0AiEAwwqpAw3WR9fmpna6nTUulFyfffrRURu7owjUhIAirscq%2FwMIORAAGgw2Mzc0MjMxODM4MDUiDJIO7MeMbRJ%2FEOoK6ircA8BEd6VqCG2aiuk7BcOPD2iQM%2BJjA0BT5p13Wkr2alp%2FSSQXD8KyfckrwHpQZBMuS%2FldWkrszOy2ijUdxeRDrk0E09%2BiK9CjSJu7pC41NMOtXZmUNRwCva5K%2Foe0mhhNn4aWPGha5FtVQDc2v%2F5t5lTQZWuH574mt5mnk%2FMR2pJk7XMDu11mYWs9er%2Bl4oqqmI5fH6O6jA4Js3bj3nrAwWzkBX6LK4Hf5taFWbvPARYLRimDKDvnqjtaqhNLWxYfS8Ur0GjBfFJevYjNh21wWBYnYx2bb1XRJbWcwzpeNsM3Vr8fOs18eVbU5HNXxwqPsHMG08iMPCi4GQZ9fjRxIhxc%2BtTkwE5glDkJjUHiFoxjBr7625i72CYv9Ekar4McOBwtU%2BHvsgdyT3jYZA2vaRqfNnPpjYEeA6IQ8GzuNLfXfRi3mE1cttG342qapHLTL6vpY%2Bvka0BBHqCbRzyjQI0EBLJnn0%2FmkmcwJLINALRTWvCCVbKcRLkR7AGySQvtaR3oz%2BFtblSUHHAYpn5FyLsj6vbAo7j23E%2F6lg%2BFRwlLaM%2FW1xuGURNmxcmHyPHUjPQKvXsGVO%2BJhniIGvhGX%2FYAp%2BUmwLvYJFKp9uNZtzHQ6PVqQ3Vxt3hKTNvpMJDNir0GOqUB%2Fw1McQH1ruUIsskn29gE2DC4oDSIJ%2BcgrY7CBS1qlOyqyvNvXjfWRi12BklSePCP3cAsW4JgeBKAMhJpE2dykZhQPuXNZzT8iqkT%2FA96lJ1Q2ANM7ktX0RPT21Ipv3KHu7WIoJQNLIJJ%2BeVxHvSVKm3VNLJAmi7UyfFMIdLSnbuKKL2SzwUa4G9jU%2FQjgPSqHw3htxW%2FELtLSyLixledyypfIS%2BY&X-Amz-Signature=7041def05b458e4c58108727c4297ea069d15ea00235604376a9acbd2284a4a6&X-Amz-SignedHeaders=host&x-id=GetObject)
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
