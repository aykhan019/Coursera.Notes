

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

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/997ac361-58a8-4f04-bb0f-79fea4baa761/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665A2EGK5U%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T081822Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCmK1jEEw94XIDLqFWd2HQmNG%2Fc1fFQMPSAyjSG0%2BImmQIgRpxepyWTB8F2Az%2Fkr83xxDNVGHBBqOzdmPHSf%2B1S4SYqiAQIof%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDE4Ajpy0tbe5Q1ewkircAxwEgl7YbWgSroz8xgHRoFBrK5ilP5R4i9%2F%2FG09Tz6MbC20cQqO0EOQXM8ObITm%2FqpzOPxkrMG4XxB8S3Vb%2BGHMkE529SYqFQYjbBsP6MxP8ZiUHdBiJsKB%2F6AtIqeLwHuMu8nmsMb04xh%2FBJS7thchfcltgboAEZXuT65pbY4PeHmwUXDfkGCOiMTzNHZarn719uYx9OUVEIFtgsqW3cvPgd5eRUrc449hvyoYQza8OplukOLo3O1i1N%2FbKTP42pukQEHmo9bs1JhJ1GTrc0MhvgKZso37UbR4WN1bXsDpTOUDDtdOCYt%2FS9ahi4Y7GwgWvvtKab4VIjMfwfOYUhi%2B19ztN0G1ZtVm9129nhjTVHQnpT%2FcFVQuq%2B5o%2Fj%2B9UuGUoX8tS8MrGeYHDTluKYkEhhGNN2CJHhR21HSMGpGfZleBp8VVVy%2FgqyA%2Baya7MzbQBRlHXAHgOvD8vxIciIcX1PcdyEzBoIOFRbOojUB1fzeaZ4%2B1wlp6Ldykqlv956pO488LfZwZuAMSF1rtT82SfzKbbI7tiB0qZzCwGPlPaU5Mr9ZTcjEKY4DVcSjQHuOcittHLlT2EZBjgCRonPBSvsXw4Wk1xKY6uxVeaGQPrzEH25q9GQJAviYjSMJXr7LwGOqUBfUhQVQ9PO1afq%2B78n730oACScNIQoQrWEie4If0j%2BeHkyb5O2wNw%2FBP%2BeCdLo9NpXH%2Bg7k4zusoUZ48kEY9P7D5fZpvPPHLm%2F6P%2BYOIpbhinZK4KwGAsSxOhzrGR%2F%2FNCdnlcq1z141ZGs8dV8XZz9vdL7hUooGp%2BdLozOeVI2qQF948vskWCZEaRNMEVtDI%2Bq0B1VtbgqbtktE3F68hcHSKeQr7n&X-Amz-Signature=9660dc52482ec70bc385bdc473dea2e59fad538258e0156513cff1fe1344ec92&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Data Visualization Libraries
#### 1. **Matplotlib**
- **Description:** The most well-known library for data visualization.
- **Features:** Great for making highly customizable graphs and plots.
#### 2. **Seaborn**
- **Description:** A high-level visualization library based on Matplotlib.
- **Features:** Easy to generate various plots like heat maps, time series, and violin plots.

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/733d1e42-5a53-4fd8-90c1-3d85254369a6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667HGV4GTB%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T081821Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCuzaH5QvMH%2BZce2Xg%2FH5fyv3bRhQwpdsHG%2BjlhqQJ0VQIhAIczwokD%2Fni%2FddsK9ZBwHno3M5D0EBShenBR5JAYr7rMKogECKH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igwi9Hrq3dWECd6Ppwcq3APADmzVOeuYHPOBnVGTTE2o50JWOX1o3waApPNlUEcRavEkcx%2BSU9FSPu45J5V%2FZTQ9MT8fWHnt7M7VOwe4fCxZLcsPlaTa1ANVR8F8zfhiWS9M0N6pvt%2B0eZwfC3hkC6vFGAeJDc4nXF81m5fnPUHMGE9PM0xWIFV6HGDwacUSMXtxQFfV2jk95waU7oppg9NBU9dLz2aK9oNM4qzzBOQL3Qy8Ra9rz4xIACW88pIZ87%2BRDvlnyRGsUJ%2FqTygfVnfQRWiRcDhZRsxEyjK1ewCemNhp7284xYya%2Bn4BlIpW5jpZbcFO7YrhZMlAKMaAnSukSQxSViF73EkLKIeb%2BIKJ7CLXQmwUxf3Ax6sApeNmoZzxVD%2FWqM6QRyR6q7daHyFvZDyMVT6upX1JKuWVoz5Sd481vTCfbHYPbECkBHr5%2Fy7WOzFF3FByMZa1S7cvdQQOICLrDI5K9HtWn0qEO%2BDkb%2Fdsqw3xG%2BxzmIEGtlJ0ygBa%2B%2B88%2B5K371JPSA%2ByNosH%2BUMnKLq7ETxk4tzPVru1%2FTYs2wrwtFKL8GB%2Fd9zQVElA6IpUreSgLSTz1YARP5Y%2FByBbHcPKN0iFrdatYbSXau4XwUYaXZa7GfVwN5e%2FdqEU0GTG%2FETzUnnNEDCP6%2By8BjqkAYgtVLcEg%2FgMkbYpMHU8SJtot6ph%2FwtQtVDrAza1%2BQOHHHEcsRh02RKmK3wXXurGfnoWk6UvcX4TZnx2PIu95T%2F3%2BmTdvSP8By%2FdWVDrCnFBk3HJJ5f58xynWpR4e%2BaqJxpenSrBv%2B2BoAiVgLo8agBUQognm4uPKykpMCVj09EHHmuTgrFiSol6rl5p4YZEr0akJJ1GJWq2b4EjMD6bXCBOnCnH&X-Amz-Signature=0bffb7764bf4f85946b9ca6efd19cfde538e1dba9a2c141eb5859c4f0b1e1464&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Algorithmic Libraries
#### 1. **Scikit-learn**
- **Description:** Contains tools for statistical modeling, including regression, classification, clustering, etc.
- **Built on:** NumPy, SciPy, and Matplotlib.
#### 2. **Statsmodels**
- **Description:** A module for exploring data, estimating statistical models, and performing statistical tests.

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c62885f5-417d-4179-834f-d68f8f2bdf39/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667HGV4GTB%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T081821Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCuzaH5QvMH%2BZce2Xg%2FH5fyv3bRhQwpdsHG%2BjlhqQJ0VQIhAIczwokD%2Fni%2FddsK9ZBwHno3M5D0EBShenBR5JAYr7rMKogECKH%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igwi9Hrq3dWECd6Ppwcq3APADmzVOeuYHPOBnVGTTE2o50JWOX1o3waApPNlUEcRavEkcx%2BSU9FSPu45J5V%2FZTQ9MT8fWHnt7M7VOwe4fCxZLcsPlaTa1ANVR8F8zfhiWS9M0N6pvt%2B0eZwfC3hkC6vFGAeJDc4nXF81m5fnPUHMGE9PM0xWIFV6HGDwacUSMXtxQFfV2jk95waU7oppg9NBU9dLz2aK9oNM4qzzBOQL3Qy8Ra9rz4xIACW88pIZ87%2BRDvlnyRGsUJ%2FqTygfVnfQRWiRcDhZRsxEyjK1ewCemNhp7284xYya%2Bn4BlIpW5jpZbcFO7YrhZMlAKMaAnSukSQxSViF73EkLKIeb%2BIKJ7CLXQmwUxf3Ax6sApeNmoZzxVD%2FWqM6QRyR6q7daHyFvZDyMVT6upX1JKuWVoz5Sd481vTCfbHYPbECkBHr5%2Fy7WOzFF3FByMZa1S7cvdQQOICLrDI5K9HtWn0qEO%2BDkb%2Fdsqw3xG%2BxzmIEGtlJ0ygBa%2B%2B88%2B5K371JPSA%2ByNosH%2BUMnKLq7ETxk4tzPVru1%2FTYs2wrwtFKL8GB%2Fd9zQVElA6IpUreSgLSTz1YARP5Y%2FByBbHcPKN0iFrdatYbSXau4XwUYaXZa7GfVwN5e%2FdqEU0GTG%2FETzUnnNEDCP6%2By8BjqkAYgtVLcEg%2FgMkbYpMHU8SJtot6ph%2FwtQtVDrAza1%2BQOHHHEcsRh02RKmK3wXXurGfnoWk6UvcX4TZnx2PIu95T%2F3%2BmTdvSP8By%2FdWVDrCnFBk3HJJ5f58xynWpR4e%2BaqJxpenSrBv%2B2BoAiVgLo8agBUQognm4uPKykpMCVj09EHHmuTgrFiSol6rl5p4YZEr0akJJ1GJWq2b4EjMD6bXCBOnCnH&X-Amz-Signature=9d72b916baa07aaf569ace934dfdedc9bb3ee232ca4822fd59fe80d809880cf9&X-Amz-SignedHeaders=host&x-id=GetObject)
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
