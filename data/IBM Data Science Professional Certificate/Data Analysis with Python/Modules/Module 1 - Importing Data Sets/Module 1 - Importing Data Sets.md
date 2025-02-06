

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

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/997ac361-58a8-4f04-bb0f-79fea4baa761/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TW6OYTZV%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T161700Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEcaCXVzLXdlc3QtMiJIMEYCIQC6kUxLYyUuDVp5P25%2FmJ8aSx1fh19kpzhhCmTBdA8SGQIhAJ7Eb8w3Vs02Le4z9XEbJqSqf3BPGyW0TLf8QWtxoMn5Kv8DCGAQABoMNjM3NDIzMTgzODA1IgwhNYyYJ3hgwfSlZoYq3AMuWnC4Xt9hxlUKTlZFMI6gKfe63hyPtaMuxuptka339To22aCRZV26aZAoZZoeAXuaBhAmH3nFN8IVy1Ysbnp10fm1mSz1DyBbJv6mFl8ercWIJJIhv7xm006N0U4jhNxbfQE5PeJU0djGZbs1O%2Fysp9ShVNvsTZTiW%2BGG7AlevoOJyEiVnXTuc8ilcGRyqSh0%2BZzzx%2FiRTQftZIZ4wfEUegkOq0fCr5KdlVBY7mWAg%2FaeDjzaypWadj8XI4GIOBa7hUeHu0mc9b4X22Kc7cWcpj8hSZOhOj%2BKtCbNEow719eDqMsq9L3B93ZAMiukcrqRiTLaTEPsYEIdU8q%2FVwXRiSZlvwvylCwYbEk26DvpSd%2BkLnFm%2BPvCtvTBGOq57QaUshIzFaLluuv6yle%2BOIA8dl8k6E35XLYdNKCx172jdwQCrifze2BIQspwnprdDyASsvcINfcJPUeXMsRBTEnifQ1EZ155qAZfHvbA7w9GQv2C3Gf6JG4ATw7yHUoKzpujMjdGTlkThlPPnP0WwKNPPHaQJZkHMUEr4ef4DzqLH6sDq%2BV%2BanH2hkmPexU7%2F1L9AI6dBlYx33YSfDO5ovHsfCMjkBG2Ccvodr6a0%2FAE0YepyCh%2Bk5NGEH%2FZTzCOnJO9BjqkASesZUjOld0fMmm7kJjEwuxPpeTZaVF0ALH3W%2BSYn8hQ0Ch%2FRXiWrpOiph6BxDTjYfUJX0oyxFJBvGP7na1O9KBlZ7%2FSti0xszlxR0QELlG23VpMgqYpoFo4BB4QblWmo75tEL3cLwHAwugYukg6KYIbbuFbi3ODk5SjRfox%2F7XbcaSLh6jzePTqGWbDG8ZySkYZvk8esyE8noQP4%2BNELuWsWwQm&X-Amz-Signature=70c7930c4317ba6db4506fa6537e0a6fde86adc806b7febc8e287d9adf77b771&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Data Visualization Libraries
#### 1. **Matplotlib**
- **Description:** The most well-known library for data visualization.
- **Features:** Great for making highly customizable graphs and plots.
#### 2. **Seaborn**
- **Description:** A high-level visualization library based on Matplotlib.
- **Features:** Easy to generate various plots like heat maps, time series, and violin plots.

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/733d1e42-5a53-4fd8-90c1-3d85254369a6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667NBFR33I%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T161659Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEcaCXVzLXdlc3QtMiJIMEYCIQD6UbTRYgps5gvtkkp3hbnogHAPExeIfqJkOTW3IyELkAIhAKzD3q4vFQdDLpS5YELUcMGKCJo75ne%2FMBaZ9M6Mnd44Kv8DCGAQABoMNjM3NDIzMTgzODA1IgwuiMHtvRF789unwIgq3APiGmNqccL6bEiZy7c21sHnoMBurq28RnKfhAyCzGiF%2FuTab1XHKlNb7hW51Vu5bQR8%2BuLsLY4MnH2%2BHRt%2FlvkliS42oTMsvQ2t5j3estJLNqu9kx9FI4%2Flyq4LRclWlXcsYUcnSV5uXQHbW3Cu8RJsL94S2snQ98qxn17Lexzgh90vgWhww23xKgcRwnsi%2BVyrsyQ5ynV7KByxmE4mYB2k50GUgBFPtTKyz4RwAdIase59m8Vk9oWzGkFGQwuJJjFAYqNDDMAfHlwQL80tJQEMaO4%2BkGfAm5rh2DAU9RBhc3FEOFan5I0E1HwUn655BL%2BzsjG7n5sQyO6hU%2F%2FPu1uIjeLkQ%2BDPcbr86H2r%2BeyTyWGMNpQVuHiJBVwfvj9vgEjM66Odp2EtNHIdspmn9s8Tndfo41zMnNhNJIFJy9qM2YiotcVuvZQ70CfyUnp046OxDQTxO22C3JQT%2BbVfZfgSV0mvJtKayxr%2BKvarplpMdE4Us0SRhU2TKDkRP%2BYrEjaA4I5HoofKshbfcPrJARRpXUmN9qJc23wiC2yM8%2BFtS8dBMupk1zg6OJTmqiUvGlFsAYSBDoEA0DGaLRlE75QMY3jmqTqJdUSj8NP%2Bn6aTPLOuhCv290buDp%2FO7zD5m5O9BjqkAR3hY4jCaEwLFNPrA5IJfkxVxLV8PLHs7MIy%2FyiT6Ziqhb34Fyj0t4cwTa9laIrsLSsbATzVtYMepkGr5XLoLCTCilmcQtva6Rp0IS9TYULdXmDH0AzKu85OzB3shaWcjwzICcKTox2yRoY%2F9%2BKPg6OrEGFP46aloYvjQxQjE%2F%2Fn4SUPiConf%2BFEHfCv%2F7m1dgp%2FdwjEUOaUU20qHkas6bfRJH0L&X-Amz-Signature=eac28cbed45cd350f409eee80a4f91a00a4f8a189311c769e0605fc3c57f93ce&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Algorithmic Libraries
#### 1. **Scikit-learn**
- **Description:** Contains tools for statistical modeling, including regression, classification, clustering, etc.
- **Built on:** NumPy, SciPy, and Matplotlib.
#### 2. **Statsmodels**
- **Description:** A module for exploring data, estimating statistical models, and performing statistical tests.

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c62885f5-417d-4179-834f-d68f8f2bdf39/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667NBFR33I%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T161659Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEcaCXVzLXdlc3QtMiJIMEYCIQD6UbTRYgps5gvtkkp3hbnogHAPExeIfqJkOTW3IyELkAIhAKzD3q4vFQdDLpS5YELUcMGKCJo75ne%2FMBaZ9M6Mnd44Kv8DCGAQABoMNjM3NDIzMTgzODA1IgwuiMHtvRF789unwIgq3APiGmNqccL6bEiZy7c21sHnoMBurq28RnKfhAyCzGiF%2FuTab1XHKlNb7hW51Vu5bQR8%2BuLsLY4MnH2%2BHRt%2FlvkliS42oTMsvQ2t5j3estJLNqu9kx9FI4%2Flyq4LRclWlXcsYUcnSV5uXQHbW3Cu8RJsL94S2snQ98qxn17Lexzgh90vgWhww23xKgcRwnsi%2BVyrsyQ5ynV7KByxmE4mYB2k50GUgBFPtTKyz4RwAdIase59m8Vk9oWzGkFGQwuJJjFAYqNDDMAfHlwQL80tJQEMaO4%2BkGfAm5rh2DAU9RBhc3FEOFan5I0E1HwUn655BL%2BzsjG7n5sQyO6hU%2F%2FPu1uIjeLkQ%2BDPcbr86H2r%2BeyTyWGMNpQVuHiJBVwfvj9vgEjM66Odp2EtNHIdspmn9s8Tndfo41zMnNhNJIFJy9qM2YiotcVuvZQ70CfyUnp046OxDQTxO22C3JQT%2BbVfZfgSV0mvJtKayxr%2BKvarplpMdE4Us0SRhU2TKDkRP%2BYrEjaA4I5HoofKshbfcPrJARRpXUmN9qJc23wiC2yM8%2BFtS8dBMupk1zg6OJTmqiUvGlFsAYSBDoEA0DGaLRlE75QMY3jmqTqJdUSj8NP%2Bn6aTPLOuhCv290buDp%2FO7zD5m5O9BjqkAR3hY4jCaEwLFNPrA5IJfkxVxLV8PLHs7MIy%2FyiT6Ziqhb34Fyj0t4cwTa9laIrsLSsbATzVtYMepkGr5XLoLCTCilmcQtva6Rp0IS9TYULdXmDH0AzKu85OzB3shaWcjwzICcKTox2yRoY%2F9%2BKPg6OrEGFP46aloYvjQxQjE%2F%2Fn4SUPiConf%2BFEHfCv%2F7m1dgp%2FdwjEUOaUU20qHkas6bfRJH0L&X-Amz-Signature=9e167b078f2bf127fd5b35440dcd115c7727ea3ed6b42509a07f37158ce14a23&X-Amz-SignedHeaders=host&x-id=GetObject)
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
