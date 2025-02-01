

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

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/997ac361-58a8-4f04-bb0f-79fea4baa761/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UCCMR6YV%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T122556Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDuE10rkBc%2F%2B9MnwmI1LMziY6rW5U7m1sUBPAQ%2BlniFaAIgMW0QItLqqKhBPF4qLjedpczlJpnra70s0s5Dq1%2B%2BfAkqiAQI0f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDA6kCUHahX%2BDLBYtHircAxcFBo1497B9YI0v%2B4w4D1t0ms9JYlsR3pUTw0DKz%2Fhq2w3odiL7%2Bbh7bdtXfrGAU2QonX0xvGem6KoyQhSzwh4n4U3z5CNGuu7TBoUVsB09mwi01ckIjj40%2Fb6n11YpreK7pKjlblDAE6FCbBQ0wEo4SO9uL9DiAISD3%2BWZVps07HhFAnMV3hWmd2hbibTW5ZgOoewIhUHPTsa%2BF86KHE7VN6gxGUkngN%2B%2BuwO6l%2Bzg0ZMsoxdBoyXG57EM5FkisnLqP0%2BTuqXlkH9km32TNTLHT5bwkYxeMZGD6i721548XMK68GEv7KKvMm%2Fje4Grim3bdy3QFLN1ciH4sURIrisudr8fPWD4AJOu2HG6rvNIJ7%2FAdMTi8YvCTqgHXTuJajTycNqA07x2ybTfILmgpZkbwnrjrqEA0vsjD6qlJtzKkMb%2FenzQy4j8gYyoISbCRl6fMfltPaBePV5fVnHVNTbJq7S1a6cKdr5wbYWIo5VPKeJTbPmGsQs4CoQ0GmqpIiudYElUihg9cyrLz5XLh%2F6WFQHaFHC1Tny%2BIB4Xb9TWEqf%2BnKZ%2B%2FzJYj0lMtN9kV8kHbWIANJ%2BqtCGPUlthRs2aUvBacyWScUJqXdej3D0QkGNxcBJkscjN3KO4MOik97wGOqUBblowxoBTESptGKVHMdYiA2U86SVOZirlXVOJp54vChqN6U7RK0N%2FpdNfRxj7%2BSXKrK24arPg1Tk6wZQzyibEXMgX4Zx6ajJ8RNUsVdgNyxod7PmPMunHlnwJfEJ6KzJ3q042MzBw2PoqSe6jipgENlsq6RkE%2FInk3cHY1fXZw85X7fSSHsqkurx6stqiABarlfaGqSHVDXtd%2FquDJHWhpWy9J7rl&X-Amz-Signature=718d9af2d103331304cc768a43aa0df16a2242100e24cf907f9b24a6b1ce49db&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Data Visualization Libraries
#### 1. **Matplotlib**
- **Description:** The most well-known library for data visualization.
- **Features:** Great for making highly customizable graphs and plots.
#### 2. **Seaborn**
- **Description:** A high-level visualization library based on Matplotlib.
- **Features:** Easy to generate various plots like heat maps, time series, and violin plots.

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/733d1e42-5a53-4fd8-90c1-3d85254369a6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TU7ICYSC%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T122555Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCUFHID9m9DkkVNZ0Z%2FHOFHSuzLaz71egEOTElX3SQItQIgLGxtNWyKUcyVRtw2KbwIEdlBalqf7AxEyRpV%2Bz3ZJuAqiAQI0f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLVXhUs%2BjFv1ghSruyrcA5I73MhIgtH1d09aWqXjIFS0g2tnmzaEhBDbeS6VkaXHNMv%2BfoRVw%2BnppH5QEfRbAxx0IwzspkOFdgqULtmFC3nD9zQkByLB%2BehqVqv446HhS1gs3M5yWmJT%2BtNK9DOOQ0vlkwIJblo%2FY%2F5uZpp%2BEsiqpRzZSYs6ai0%2Bfk1Mq40xt5%2BseA5CRn6nQTLYsQy%2FYAf9fMUGyUbrnFhC02WYTP9CuNk0t7bdr3XSMjRcFx8fwgstXpqIWk6UrBhwL4wHfXQeJp%2BK%2F6jSGfDbtZOgvqBA3NwEEsxtdmQy4Hf0mkEb4qGXS6V7YBH7PaRn8vsWYVeGrih2Zk6XwnteClMz30qqgIY9yOMitEcNzTpqk44t1dRwMiXxp%2BSEeZoIpHp8cDmmZFL4SV9UPKdoQMeUmu3mdISA6bNwDSW2JUT5H60veHdFhMp6kl66zQoZfqRziW1W28lA95c7fed%2Fi1GFlaPe8vFx9cNSn9cAgqY%2BQ3sBwL%2B67Dn1pZMfGlDw%2FnEx5evtozMCc68CBVlyfjzNecXFKAXI0C6Huvt1%2B2WuaJSf6iYuXAMBFohjt5ylE0KbP65Eh4%2B5htDlSjeyC70zeRCef77pRU%2BV1Ezf0X%2FouDyy0qIeGrgSKDkaXOMIMMik97wGOqUBUeQHSNmlYfy%2FrTt1erq529xnqHZzR219H%2FjfS8XxOzRCg6cdyS%2F8NvAzWrvSOvkSm%2FsRX2XYggrYpvmsHTGY2nAM2z%2BBh4gRMVgplw1nRkZQBLrICpHwmWvy0jaPZJaEIeCYuQY90miGfTMJ6LasOgzLJ3P%2FjgsWGSan7%2F0kL6trZtk%2FPbaRyqD3wgLv8oKP0HTxOuSl4ED3Xim7tpeJgxkA9btP&X-Amz-Signature=bdad5d92c20afd8c7e90aa5852f3ef8e5a34858788970d1c62004a37c7dbaa5c&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Algorithmic Libraries
#### 1. **Scikit-learn**
- **Description:** Contains tools for statistical modeling, including regression, classification, clustering, etc.
- **Built on:** NumPy, SciPy, and Matplotlib.
#### 2. **Statsmodels**
- **Description:** A module for exploring data, estimating statistical models, and performing statistical tests.

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c62885f5-417d-4179-834f-d68f8f2bdf39/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TU7ICYSC%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T122555Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCUFHID9m9DkkVNZ0Z%2FHOFHSuzLaz71egEOTElX3SQItQIgLGxtNWyKUcyVRtw2KbwIEdlBalqf7AxEyRpV%2Bz3ZJuAqiAQI0f%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLVXhUs%2BjFv1ghSruyrcA5I73MhIgtH1d09aWqXjIFS0g2tnmzaEhBDbeS6VkaXHNMv%2BfoRVw%2BnppH5QEfRbAxx0IwzspkOFdgqULtmFC3nD9zQkByLB%2BehqVqv446HhS1gs3M5yWmJT%2BtNK9DOOQ0vlkwIJblo%2FY%2F5uZpp%2BEsiqpRzZSYs6ai0%2Bfk1Mq40xt5%2BseA5CRn6nQTLYsQy%2FYAf9fMUGyUbrnFhC02WYTP9CuNk0t7bdr3XSMjRcFx8fwgstXpqIWk6UrBhwL4wHfXQeJp%2BK%2F6jSGfDbtZOgvqBA3NwEEsxtdmQy4Hf0mkEb4qGXS6V7YBH7PaRn8vsWYVeGrih2Zk6XwnteClMz30qqgIY9yOMitEcNzTpqk44t1dRwMiXxp%2BSEeZoIpHp8cDmmZFL4SV9UPKdoQMeUmu3mdISA6bNwDSW2JUT5H60veHdFhMp6kl66zQoZfqRziW1W28lA95c7fed%2Fi1GFlaPe8vFx9cNSn9cAgqY%2BQ3sBwL%2B67Dn1pZMfGlDw%2FnEx5evtozMCc68CBVlyfjzNecXFKAXI0C6Huvt1%2B2WuaJSf6iYuXAMBFohjt5ylE0KbP65Eh4%2B5htDlSjeyC70zeRCef77pRU%2BV1Ezf0X%2FouDyy0qIeGrgSKDkaXOMIMMik97wGOqUBUeQHSNmlYfy%2FrTt1erq529xnqHZzR219H%2FjfS8XxOzRCg6cdyS%2F8NvAzWrvSOvkSm%2FsRX2XYggrYpvmsHTGY2nAM2z%2BBh4gRMVgplw1nRkZQBLrICpHwmWvy0jaPZJaEIeCYuQY90miGfTMJ6LasOgzLJ3P%2FjgsWGSan7%2F0kL6trZtk%2FPbaRyqD3wgLv8oKP0HTxOuSl4ED3Xim7tpeJgxkA9btP&X-Amz-Signature=b5d9959e3f4c46d71793842918a6ced0911f379eac7b475f9714b78f327484f7&X-Amz-SignedHeaders=host&x-id=GetObject)
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
