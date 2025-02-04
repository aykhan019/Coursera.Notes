

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

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/997ac361-58a8-4f04-bb0f-79fea4baa761/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466V5HZX4VU%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T024136Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAoaCXVzLXdlc3QtMiJGMEQCIF%2FfPtsBYY6tlSjHlH4b2yBiBcmNvB%2Fy6wSzUH0XPWnVAiBOZfCaREH5A4JjJo64Dlu56P77Gj1szeppLR28H%2FtAYir%2FAwgjEAAaDDYzNzQyMzE4MzgwNSIMbkxVDUx7G7K3%2Fr4LKtwD7pM6xQ%2FnORpezDJ2gNSbo2n%2Behe%2BVXczOZ6Kogch3V5sV2DuK2OQGW9n9rKjtI%2BXznqZepB%2BbGulr63dPasukc7xIbI0X9cCZ9KQpIm5KYLGxy9A%2FLTTqmHUzT2JEFOPufv3pWeRPZYhu4VIcAKV225hJLJEX1e0Qsmgp3fMvM031duhrGeRlaV%2FcFi35fiRzkqTEpXZHoTmUKvGJsOUMxPqzSWVkmeFa3aDImp0LQRaYX4kblWiI98pYlzUYbtvzaNZIs%2BAX6SaLOLVaMljR2ebPc03Uu0gLqy%2FAswS1qvOL3glotFXCAAJ3TSS%2FDCQMvs5F%2F%2FBBw3jI7tDDmkFr9c83ZniJMEV6vIlDOm1ea%2FK%2BWPnGPjkQAvlsjjE5OSwBwtSoA6DAQdmB%2FXLr2YvdeY6HwZpfr4UC3UdBHSWmAYVsq3bDr01hQfnDd76gORbhiZcnmL60ui2j2r49%2FwqXZAnazThDpLguH4cx7zURM1oJ2K0ZB9axIafvuoVt6QOEKv1tLBBocdx%2BkqWc%2BouwCciwuWirL9KwtdPIbe7tkaJdQWmRahKK7SFc4wqMxjG4LmtHcTpdv37F5bKm39UTj6%2BLNfq3YnWZSV1k8W%2BHw26SKNiIjhJHFf9jfIwsOmFvQY6pgFoFWA8AjQmfx3nxhtmdFUerStqQ1HaBDRc5k9%2BglXx7mXHoP0%2F2fW1sMzUVV%2FXLMvjRPQCQ0rp15W8fQvvMp1VuJYpvTbXekWOtQRGKgOxVh%2F6mWk7JqQLUSSQJpsbQKQfWRSzNdYLXT8hqYkF1sY3ZoUdYRfaY78A%2FhGlYP5DnWgkCXyzI5xBZSqX1UBPeGL09TrzQROXjgo0JsS9rvviQSn8aEKp&X-Amz-Signature=662633a6a99787a54bca49832a393c61192faef9c78b155e78eea754b2cb5336&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Data Visualization Libraries
#### 1. **Matplotlib**
- **Description:** The most well-known library for data visualization.
- **Features:** Great for making highly customizable graphs and plots.
#### 2. **Seaborn**
- **Description:** A high-level visualization library based on Matplotlib.
- **Features:** Easy to generate various plots like heat maps, time series, and violin plots.

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/733d1e42-5a53-4fd8-90c1-3d85254369a6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664CU3RMFM%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T024135Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAoaCXVzLXdlc3QtMiJHMEUCIQDOciADmWrHyYvwzgqcubm8C5oZeD8w0tvrsw65f6egpwIgJLH6j32iKZVnX1k6WVKbMiZ6IAP6uD6gRh18SW%2FT%2Fcoq%2FwMIIxAAGgw2Mzc0MjMxODM4MDUiDFjhjYUnu72pmwD2AircA9%2BdTSIlpnlJzczBsX3zwcKmRyHE%2BUXnwCOZURM9lvAMvp%2FyRc8M7nL59UsRSjpA4%2BOd2AYA6Jy7JmuW2Ioh0Lw5mH55aV7ppToA4yqVsjAXngusIqHxNhCyeRFsmsYG%2FyTjTb%2F8aNuzGCz1yeVTGvDlvULBKdZTRW%2FW6hroZsbJVcQZQQXu0V9vUhuo2RKDbttUVyK%2BaY6wcy1iNwQ0NE07ICeFHJsVTP7RByiMzVff0d40wbhJWkKdoCVSbrnFS16Xl%2BOPnXSG2wbEcBOm6xV5Ku%2B58cLC2%2BAGlsjOg2pjDcerFPlMvrnYp13FAcsdyb6HS%2Fv8%2BLK6HN%2BY6eEQVSJ%2BIfaCkpK1rNAYtwbJdZJn3VfxqF5ce9U8n3BZ8lydj7pm5hxx2QLLUFOxE7qo7xr4gzXxyODLQ%2BuD5yh6Q5BUFUMqIIptRgzr8Tb%2B1%2FLbaeaLmTdqT4U76DwJvoq1GcPeCII%2FVJ8VYs366BPNCxEPGIHCyErF5J3hWHyUEh43vsfzoJQDO%2BjqWHU6RJ6ofAWFc4pIVeKNaT0JcCSm%2BcpY3jmRr%2FaR%2FQhu%2BASdB%2Focu0pjllw9CGpqMRqti52wigXpdAF1XM78ubgMjL9r%2FyCCJfjyYFzTjplxFHGLMIrphb0GOqUBb7R3MU%2BRM2rYXZ86RXq%2Bd3OqnMNoI0YCNzVV3lr86%2FKUspbw7vcthuoom9IYMK%2FPBhUd7j5U8sNh%2FzDR4DC1b0RULEeUdKMVeVqwhrdxUvGX7akGjesKperkSz7K7GnafeVH6bJV1a5AzBv57lJnGk6wSQZm6cuCHBo06xZDpVA3Lj9hnxM4haV0URfwKMMPathPrJeNWza7uTYmk1vxLQuKpwkq&X-Amz-Signature=9c055d0a0512136969ee3486b13a89f1c6f544bcca6b6d3a7ebf27b252f304d4&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Algorithmic Libraries
#### 1. **Scikit-learn**
- **Description:** Contains tools for statistical modeling, including regression, classification, clustering, etc.
- **Built on:** NumPy, SciPy, and Matplotlib.
#### 2. **Statsmodels**
- **Description:** A module for exploring data, estimating statistical models, and performing statistical tests.

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c62885f5-417d-4179-834f-d68f8f2bdf39/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664CU3RMFM%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T024135Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAoaCXVzLXdlc3QtMiJHMEUCIQDOciADmWrHyYvwzgqcubm8C5oZeD8w0tvrsw65f6egpwIgJLH6j32iKZVnX1k6WVKbMiZ6IAP6uD6gRh18SW%2FT%2Fcoq%2FwMIIxAAGgw2Mzc0MjMxODM4MDUiDFjhjYUnu72pmwD2AircA9%2BdTSIlpnlJzczBsX3zwcKmRyHE%2BUXnwCOZURM9lvAMvp%2FyRc8M7nL59UsRSjpA4%2BOd2AYA6Jy7JmuW2Ioh0Lw5mH55aV7ppToA4yqVsjAXngusIqHxNhCyeRFsmsYG%2FyTjTb%2F8aNuzGCz1yeVTGvDlvULBKdZTRW%2FW6hroZsbJVcQZQQXu0V9vUhuo2RKDbttUVyK%2BaY6wcy1iNwQ0NE07ICeFHJsVTP7RByiMzVff0d40wbhJWkKdoCVSbrnFS16Xl%2BOPnXSG2wbEcBOm6xV5Ku%2B58cLC2%2BAGlsjOg2pjDcerFPlMvrnYp13FAcsdyb6HS%2Fv8%2BLK6HN%2BY6eEQVSJ%2BIfaCkpK1rNAYtwbJdZJn3VfxqF5ce9U8n3BZ8lydj7pm5hxx2QLLUFOxE7qo7xr4gzXxyODLQ%2BuD5yh6Q5BUFUMqIIptRgzr8Tb%2B1%2FLbaeaLmTdqT4U76DwJvoq1GcPeCII%2FVJ8VYs366BPNCxEPGIHCyErF5J3hWHyUEh43vsfzoJQDO%2BjqWHU6RJ6ofAWFc4pIVeKNaT0JcCSm%2BcpY3jmRr%2FaR%2FQhu%2BASdB%2Focu0pjllw9CGpqMRqti52wigXpdAF1XM78ubgMjL9r%2FyCCJfjyYFzTjplxFHGLMIrphb0GOqUBb7R3MU%2BRM2rYXZ86RXq%2Bd3OqnMNoI0YCNzVV3lr86%2FKUspbw7vcthuoom9IYMK%2FPBhUd7j5U8sNh%2FzDR4DC1b0RULEeUdKMVeVqwhrdxUvGX7akGjesKperkSz7K7GnafeVH6bJV1a5AzBv57lJnGk6wSQZm6cuCHBo06xZDpVA3Lj9hnxM4haV0URfwKMMPathPrJeNWza7uTYmk1vxLQuKpwkq&X-Amz-Signature=3762b94a6ab76b1272ac710d95809fc13b4b015deb66b93e86262bde57424382&X-Amz-SignedHeaders=host&x-id=GetObject)
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
