

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

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/997ac361-58a8-4f04-bb0f-79fea4baa761/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ROX6PKC2%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T151554Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDgQnb7m3ylG3LgDf4sZurppJLP0NsHiUiIrrwPZQnPJAiEAhx19jzMbIZjaeflGxpsgfc3NDET1vNSOg4r1ztOcGs0q%2FwMIFxAAGgw2Mzc0MjMxODM4MDUiDJyXlo5Jb69WpS9bfyrcA56P4iZo8m4E3H%2F6HAKlxq1ZC2RSwd0DtqXjXV9NRCsPPf8kLPiECAw35HBTWowxqka0L1s1mti%2Foy%2BIPBhyeRwxv7CV5aAWZ0XCWcWYrkvqkZv8rTwpdK%2BiwkbtJGH2dqcN5JK1zKYm4M1Y8YQYLP2lzsSFuFDB2UIzCuPUvaM6FSjsKKOCsxODXoJK2q2Wo3PoYt3GsxYOueEIDuAOr5rqzSDJ%2B2kPgHnzxOX0dAf7usaB5%2F9Wau0WabkRIewGxN6%2FiGJbYptz9AubDXWSvR%2BecF8hK%2FTMIh711aKvFJBsg7n2og41YaJryw8%2FazC%2BHzonEb0G0bxNYrQ7IosKMAO3IOBd1BDUEDVS%2Fi5lweTl4LEHr3UGsR3oEO0G0y%2BaCLVD1QQZqGp0CYTQgfch76w9bLEbXoe6rhe1hww0RjfcVPM%2FDDCfkqTMaW7GYGqD7taNpYqdr98rn85PGy2zzTRMhq1LfBCbVQ%2BMAWcFTkeOony4rfgPXURYHo3yZsfWJub%2BMTlFzpMYwHmP%2FcBUfCWabN6zKpOMLeBquAQjuDB318aS7OAvsiJbQiRPMGuPoJBqVqIxx8%2FhmTEwRd3yHkBnxaAcQORLkUR0Ho8aDzcDzdmpIAp1MAbTbOLAMKCNg70GOqUBK%2FMYlumOxP%2FD6ND8YdxDULbpQy2MBnZwEdG8MAYDkQvH%2F9I24Ey5iuYrs%2B2ZnpITDE2MciLbWkxTwgY8yixjVbzh9jTzGu0hbtNx%2BZxhQn7NySiiC3TeW6cGAyRgM1XkL2aKCpFOsW0Udrzgi9Vqh9DXHIwoHks69UZl1F%2FbW%2BU%2Bx78MKSsGYQW0LaZGvpvMpjc%2FbI658Szf3fWIppqPkMX%2BEdWV&X-Amz-Signature=2702a9a27d589c5bba4dd692d1f9552286de90ac35d29aa0f86a6f8fa0a1aa31&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Data Visualization Libraries
#### 1. **Matplotlib**
- **Description:** The most well-known library for data visualization.
- **Features:** Great for making highly customizable graphs and plots.
#### 2. **Seaborn**
- **Description:** A high-level visualization library based on Matplotlib.
- **Features:** Easy to generate various plots like heat maps, time series, and violin plots.

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/733d1e42-5a53-4fd8-90c1-3d85254369a6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XNFVPWEJ%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T151553Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCOCzCBQ7EwYlJgHo3K3tLTbzQHLoW0DS3gTB2JhZWTDgIgDNv8jf%2BCOsdmySJ%2BDaHHa2xrAF%2BJCCRHvFuk600Itm4q%2FwMIFxAAGgw2Mzc0MjMxODM4MDUiDJpk8OgEoHHNiORd1yrcA2rkzyyqxJbJY9u10dO2NyqkA4s4PRzUOankIS6dyf56iIZKvxYwpzRkmtrUvMICj9OcbEWP6cfQxqQZIq2x0mpkkLO%2FKqe6PuXkil6m2AjZ67wngqQ9XjZY7vfVQ%2FWtNWyBxkmizJEUuPkBT%2BP%2BAj3lfwlX%2BwB4OS4KsE4L%2BjsLUY5E%2BuM4tLA1scLa88jdjl3GvdTEexNXJPRxRd%2BwM%2BUy3uDMgPnBiT2c7roXJbeji%2BHUj7naYkm39jNhRapxn1kwgQRxAhbch8uxQLiirkMki0B%2BkLlzWSFU%2B73Kd1aMZXmbqhEQQvlvwrK1DB0gRocdc3EM%2BGGRIJMYkfMHfSSQuYAkM6qhoPGhpJF8Lm%2FpCUo4SXPgqf55Bb1DFsXrmGLnzieBthQKjS%2Bf6NwI4y%2BM9eAC7EBHvlv8nPhbTnEtn4s8nFjxPfpxqSWqHRtCTPxw7wdOq%2B36hb10RHeMoayVcNebF8PKDmMhJAAMEyvpEmKftI3qY%2FS7ZtHxnYLAHkluvsPjn3kzAKXd53wmCD3XSLg%2BWQAhdMh1HoluwsN5KlC0B8f2DM2SBYNmdk3qA9krYZ2TuLUXXFKG%2BJcedr9uYetyvBC2LsikZRhmKpWqtCAQ9GehOXt7hcTVMLiNg70GOqUBhe4b3brCt00jdnio%2BUvdxK%2Fdt%2FUHs%2FEdEULlZWAavfxVlMpPmnljfoQr9EaPuGNWmqwZEzAMzn0Pb1bSIH5gErXGHPZLZeVRXehGA%2BQJh6g%2FJ2lobLh%2FTQY%2FXfDIHKvOgKL6HkiwHFbfZiTkhY910XgrxM20mcg%2BlRgWYt3KfiwYb0zp5L1fiJ1PRKZR%2FXKUJZIAxZVZkdSslUJvy1ps%2F%2FQrsqL6&X-Amz-Signature=3e649011fd659bba8000b893e70ed33f4fafcf899ede5c3f3cb25ace63e225b5&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Algorithmic Libraries
#### 1. **Scikit-learn**
- **Description:** Contains tools for statistical modeling, including regression, classification, clustering, etc.
- **Built on:** NumPy, SciPy, and Matplotlib.
#### 2. **Statsmodels**
- **Description:** A module for exploring data, estimating statistical models, and performing statistical tests.

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c62885f5-417d-4179-834f-d68f8f2bdf39/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XNFVPWEJ%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T151553Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCOCzCBQ7EwYlJgHo3K3tLTbzQHLoW0DS3gTB2JhZWTDgIgDNv8jf%2BCOsdmySJ%2BDaHHa2xrAF%2BJCCRHvFuk600Itm4q%2FwMIFxAAGgw2Mzc0MjMxODM4MDUiDJpk8OgEoHHNiORd1yrcA2rkzyyqxJbJY9u10dO2NyqkA4s4PRzUOankIS6dyf56iIZKvxYwpzRkmtrUvMICj9OcbEWP6cfQxqQZIq2x0mpkkLO%2FKqe6PuXkil6m2AjZ67wngqQ9XjZY7vfVQ%2FWtNWyBxkmizJEUuPkBT%2BP%2BAj3lfwlX%2BwB4OS4KsE4L%2BjsLUY5E%2BuM4tLA1scLa88jdjl3GvdTEexNXJPRxRd%2BwM%2BUy3uDMgPnBiT2c7roXJbeji%2BHUj7naYkm39jNhRapxn1kwgQRxAhbch8uxQLiirkMki0B%2BkLlzWSFU%2B73Kd1aMZXmbqhEQQvlvwrK1DB0gRocdc3EM%2BGGRIJMYkfMHfSSQuYAkM6qhoPGhpJF8Lm%2FpCUo4SXPgqf55Bb1DFsXrmGLnzieBthQKjS%2Bf6NwI4y%2BM9eAC7EBHvlv8nPhbTnEtn4s8nFjxPfpxqSWqHRtCTPxw7wdOq%2B36hb10RHeMoayVcNebF8PKDmMhJAAMEyvpEmKftI3qY%2FS7ZtHxnYLAHkluvsPjn3kzAKXd53wmCD3XSLg%2BWQAhdMh1HoluwsN5KlC0B8f2DM2SBYNmdk3qA9krYZ2TuLUXXFKG%2BJcedr9uYetyvBC2LsikZRhmKpWqtCAQ9GehOXt7hcTVMLiNg70GOqUBhe4b3brCt00jdnio%2BUvdxK%2Fdt%2FUHs%2FEdEULlZWAavfxVlMpPmnljfoQr9EaPuGNWmqwZEzAMzn0Pb1bSIH5gErXGHPZLZeVRXehGA%2BQJh6g%2FJ2lobLh%2FTQY%2FXfDIHKvOgKL6HkiwHFbfZiTkhY910XgrxM20mcg%2BlRgWYt3KfiwYb0zp5L1fiJ1PRKZR%2FXKUJZIAxZVZkdSslUJvy1ps%2F%2FQrsqL6&X-Amz-Signature=48ae265a656618d0b00136587586de8e5ae4f267f2245b67d82f1a38c6220052&X-Amz-SignedHeaders=host&x-id=GetObject)
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
