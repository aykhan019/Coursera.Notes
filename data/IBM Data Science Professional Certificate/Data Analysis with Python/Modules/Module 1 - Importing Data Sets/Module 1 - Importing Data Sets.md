

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

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/997ac361-58a8-4f04-bb0f-79fea4baa761/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WNUQFA2C%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T122941Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBQaCXVzLXdlc3QtMiJHMEUCIDV3boDYw%2FIkpykpmN2988RU%2BGRjVe9hoITt40rgBU%2FUAiEAqk06zG7gTVUGO7qbDA5ugu1NMJThP4HBqD7eDQco8%2BIq%2FwMILRAAGgw2Mzc0MjMxODM4MDUiDME3mjC8zJJQmXu%2BTSrcA23nb5gM6qWUJda4RKZrgOYxzCMe9UZZE8jxetQbm52K9zf%2B6FRkzHhaq2l9AGZ7zNaSVb4ykFW%2BeVeN5LQQffpytmJXtRsIo1p3t2r5RSwl5bEw9yiyp7Kd%2F3S53UkMxdlpHMZoFb31okrUVPlCINn3%2B6T%2BGmVbjUg5FF2U3ZCFeuaAXGTYAYIqGppbzeuYR7mDrkIyR2D67EFCmdw5M5FQrDBk48Zqhuk2CJCgzp3hXZNHZhQjalquwPQPaNFD1hrFNh%2FsxPCFCU9r4wxSIXOjtrpqwAWgwMpb7muSo1ZHWkA6lGleXAREdX%2B5g4dAjXnJgjkSN5QOkqxGK%2FDviV%2BQOMC%2FoA2%2FiSte2az9ZucRRguszLvO0aC4I0VXlp5vmnCi2j%2BR99hnY%2F8L5zJE8UeuiPPv4K38Bjz91hx3EuzT0EHsLbYSqKX732lXAfNi%2BDGMnJLpZ%2F7rYcjbSVLvHQgDT7s6z9TFV%2Bm54%2BVh1G6aCPrdOL8PFaW5LdYPm%2F4vdV85t1PNkseSgDLJLUdedD9d%2F14okTbT5r6uYpMqnAFDK5HTazceDhtNz3GuPtkS8wiFrhawvK9UF75VfEfAd5mTDGnSIGNoNffr%2Be%2FMoAOBkbilINhmepI3JLOqMPyBiL0GOqUBLbZvYmts8StliaI8TBK3nH%2FZpeXAcBl1ft5wmeDhaB93X56xc%2Bwo9ogkt5YcEvZyQIB%2BWFTtIgZSsCVZuXO86yp0g08CSijyf3ZZ%2FtQ%2Bqot6vNAHFKWfLRHNPhd%2FOFWaVbRhY%2B0zjv4HDZLGUWJ4E8gt8Vs5wYtHmsrpNSiqmK4zw3TCNuPcfmNH9UsrcVIUnmYZJyaARbWSy5hDhO3cFfw4P8VQ&X-Amz-Signature=f16f4be5c47a87800d32aec60ad958c1012a0b8d3ee82d0348e2b5470552e10d&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Data Visualization Libraries
#### 1. **Matplotlib**
- **Description:** The most well-known library for data visualization.
- **Features:** Great for making highly customizable graphs and plots.
#### 2. **Seaborn**
- **Description:** A high-level visualization library based on Matplotlib.
- **Features:** Easy to generate various plots like heat maps, time series, and violin plots.

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/733d1e42-5a53-4fd8-90c1-3d85254369a6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SVHLKQKZ%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T122940Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBQaCXVzLXdlc3QtMiJGMEQCIE4XrvH41%2BC7kkItiIPP75kVVrAzPqb%2BoYGV3QG0Xl4CAiBS%2BgEaGt2a%2BJ92xjCoXRnbJMQTcCq1GbfO8KzqYC3byyr%2FAwgtEAAaDDYzNzQyMzE4MzgwNSIMMZn2nUnJAlvJ7UBzKtwDDlWJAxU6DmRjDP6%2FP1jyfREwhzamdQm%2Bqgu74sB0irABT45uTVpKAUAZOM0k2XWW2uJbHNNba89Wh2NxGzX4jK0zTjwaRR%2Fjeaqe9oFUhOnz6aGjEyQvgE7d7hTxM6GrHBe2Z%2BK5coXMrxe8SRXQTliInM9fQTlFL%2F6n8OpVSPZQCzwjxHQJXo6Ep7V205k5mslfQe0vUhZC8y1ZpmIBeYcRofCLJNAoEFVGLh3m87oBUUkltrcdRN8l3wdoM52WXtAILVAUcXZ8TD%2FE6liH%2F9scE7Rk6UxSEyy5cq9Bmb7HCNmaUcMY4p%2FlrUGN8QJUGdO6ebqnC2vRdoPpiyAybsSwP%2FBiNkm4IBpFAns0161JgiTSVtgMu3A1JiUelO7ViGPy1N0ZDH05kBJmL3XBChP%2Fh5sLkleOe8l5JJivzvtW%2BY%2F523lwzW1ytuDab%2Fax2S9XmYcTXNU8XSmuFqXnhQeN3MRYiiwim%2FBFHSoZiFlxcGiIqWK9oAZ4qVLLWDX8%2FHlhrr5BKNXi6wq6CLVvxn%2FH7lEPZsEoh0AwCY7uOS2sfrHwE26KQ2Zw6J9WmL3c9sXdZYEPWu%2FM1gqalTseiB0gixBVMglZQ8tifE2QziVsSAtDZHYxgueC574w%2BoGIvQY6pgHb47ArwFjEgymaWIsrKmblFxSUIoR6W24mZ6%2FtY4UAvxttiY%2B9RiR9NSJ%2F4fVWudPl4ghsgQZDzUNCNG7XJaPy4lJBq%2Bk0VpyVPqLS4Lvq8UBcMoCbvUhFtg5WiyURPFhtKQS7LTNDH5XLbS1g3SGWJPurnPCazBT2ouJgia%2FHBtm6Ey2MZhYnopCgncUrOwU4vNqGBqQ7Mb3EIWiznjwqtUJi%2Bm7Q&X-Amz-Signature=34aa4f7061dc09f906538ba43964b5f738c67c35e8292f4ff6fe45bcd2b567d0&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Algorithmic Libraries
#### 1. **Scikit-learn**
- **Description:** Contains tools for statistical modeling, including regression, classification, clustering, etc.
- **Built on:** NumPy, SciPy, and Matplotlib.
#### 2. **Statsmodels**
- **Description:** A module for exploring data, estimating statistical models, and performing statistical tests.

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c62885f5-417d-4179-834f-d68f8f2bdf39/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SVHLKQKZ%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T122940Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBQaCXVzLXdlc3QtMiJGMEQCIE4XrvH41%2BC7kkItiIPP75kVVrAzPqb%2BoYGV3QG0Xl4CAiBS%2BgEaGt2a%2BJ92xjCoXRnbJMQTcCq1GbfO8KzqYC3byyr%2FAwgtEAAaDDYzNzQyMzE4MzgwNSIMMZn2nUnJAlvJ7UBzKtwDDlWJAxU6DmRjDP6%2FP1jyfREwhzamdQm%2Bqgu74sB0irABT45uTVpKAUAZOM0k2XWW2uJbHNNba89Wh2NxGzX4jK0zTjwaRR%2Fjeaqe9oFUhOnz6aGjEyQvgE7d7hTxM6GrHBe2Z%2BK5coXMrxe8SRXQTliInM9fQTlFL%2F6n8OpVSPZQCzwjxHQJXo6Ep7V205k5mslfQe0vUhZC8y1ZpmIBeYcRofCLJNAoEFVGLh3m87oBUUkltrcdRN8l3wdoM52WXtAILVAUcXZ8TD%2FE6liH%2F9scE7Rk6UxSEyy5cq9Bmb7HCNmaUcMY4p%2FlrUGN8QJUGdO6ebqnC2vRdoPpiyAybsSwP%2FBiNkm4IBpFAns0161JgiTSVtgMu3A1JiUelO7ViGPy1N0ZDH05kBJmL3XBChP%2Fh5sLkleOe8l5JJivzvtW%2BY%2F523lwzW1ytuDab%2Fax2S9XmYcTXNU8XSmuFqXnhQeN3MRYiiwim%2FBFHSoZiFlxcGiIqWK9oAZ4qVLLWDX8%2FHlhrr5BKNXi6wq6CLVvxn%2FH7lEPZsEoh0AwCY7uOS2sfrHwE26KQ2Zw6J9WmL3c9sXdZYEPWu%2FM1gqalTseiB0gixBVMglZQ8tifE2QziVsSAtDZHYxgueC574w%2BoGIvQY6pgHb47ArwFjEgymaWIsrKmblFxSUIoR6W24mZ6%2FtY4UAvxttiY%2B9RiR9NSJ%2F4fVWudPl4ghsgQZDzUNCNG7XJaPy4lJBq%2Bk0VpyVPqLS4Lvq8UBcMoCbvUhFtg5WiyURPFhtKQS7LTNDH5XLbS1g3SGWJPurnPCazBT2ouJgia%2FHBtm6Ey2MZhYnopCgncUrOwU4vNqGBqQ7Mb3EIWiznjwqtUJi%2Bm7Q&X-Amz-Signature=9722db87ccf006e84a7d295e566c90c3b5bc469510b00c977f3f05db48c2558a&X-Amz-SignedHeaders=host&x-id=GetObject)
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
