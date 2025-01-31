

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

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/997ac361-58a8-4f04-bb0f-79fea4baa761/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YLFAIMXP%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T062101Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIB87An1OPYBjTm3IFlQAg6YoUnmYzFXhPORTLdlt04DfAiBEROJD%2BcSiKKWEs1QaI%2Bx56nLmryPsqwYOWa4oib6bfyqIBAiz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMsTTvg3QYyatQ01YfKtwDELAQ8cNAWu3KFugKE3rEvoSiXwYgeQIYG%2BA%2BzIEaYu%2FM1YaPtDGpvSKmBLaY9jrnHYvYJo323jfPomZiHiCdLn6wK%2F9loErU7obKJr6aWqbKQn9vY48xI%2FkagZMRAx2rGKh3ekiy8MIl0%2FOWKi4dgZ22PRWxgn%2BcFt%2F9XEh366GKynRcxzRyi56%2F9%2B82HYWS3BRNGuNVwfYL6JY6GQo4ZHEFi42vDPlcH7h5KBM%2BW5KgQlcVEc4ajk1%2F%2BUrpIUQcrTbNzzfBeDtava4APb1igRwmAL4s8GLE%2Fi2O%2FHxy%2FL9MLpJOFB6r1Q4B8SMzbxMaeN9IoGEskrc684OkGdiKDgXt0JRV%2BhUAfCFcp0T7c5AxY7q7PHlglpA%2BoFZ36%2B2Cig1Ra9afM3LYESqshZB8zyQTDTfjirmvwotAhG%2BFBbgPpZjep6s7JNSEBpTBXvBE5bKVsG%2Bob62IuQG%2F1E8QW15EaEeDiSdYUhmGJDMdVXHHkvMMGHzVTtfcMxuYeHDj8EdTjoRqVTbXUAqdZQQ3yBF8MRjjTp4AAfIjKy55CEeV5tOL%2Ff%2FURdd7Ouj%2B4LQ1fGMbZpuaQQA9ZzxUfPteRMLsxibZ7y2kOir9%2BfRUoHB%2FAvlyDpuwzEGupRkwvNDwvAY6pgEUzlNoo0bXc8mkpyA%2BgG8v0JcC1wKAenh065I48fRcY5WF%2FIBtqp4kHBxUBt5cM2dnH6BSLgrEEf4sLaHYv5GmL0%2BvbdiH%2FPUUtYcRcjBZiIgC%2BR0DS106DwGABI7MD2JARyKgiqv6x3X0j4ol7y0fPZ6H0%2FvTjgvCZ%2BP7ixWb5tZGLDG%2Fur0PpKyEXI9HiT%2BW%2BZN0%2F4COLT34iYPMmGQpiqrH39pT&X-Amz-Signature=49d58dd986ce75b4caeb7f530dec9cad36af0fbf37de3e3103a13e2055e0e1b6&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Data Visualization Libraries
#### 1. **Matplotlib**
- **Description:** The most well-known library for data visualization.
- **Features:** Great for making highly customizable graphs and plots.
#### 2. **Seaborn**
- **Description:** A high-level visualization library based on Matplotlib.
- **Features:** Easy to generate various plots like heat maps, time series, and violin plots.

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/733d1e42-5a53-4fd8-90c1-3d85254369a6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665G7MEF3M%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T062059Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIDnEtv2cse1x04L342LuUDNulRz3Z%2BD%2Fz608qD8vORxRAiBe4taqltW5oMtOVfvc499KN43cSaw2DerEAFUwqCBOnyqIBAiz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM1POJQ1h%2FaeKNKWIiKtwD7%2FI4kCN3XvTtRUJE36YPcu8UCs83QEY8F%2FJJHIovci0DTCXC0EbgXT3108wQZOW9vD%2FF9%2BjPFOkZWJwgNdH9jsmf9z%2F9caZsF6EqkVP6IjTPC9Ov9MW1Xdqg0K4CSWd1TOPtetSIyXQroYL%2BKWSRd857VsaPENfue%2BW2jdGih0VaM6M6%2BdnnH2LeMjrHE%2FNoU9r8FYmHe2HD%2FQrtVE2%2BEArMdqiV7IN%2BNw4UBp3g57u3Y9TNpvIHPjr3ee7t1A9RAVPthjjJU71KtTeuWrSsgKJuuqaD5FCL%2FGkZgNewu%2FVSE0aWjZALGFXgwY5BaXbevknL9ZVxKtSc54CvPGYXgCMSImEurQRTWbKx3zHFtkAvicDXlB%2FYvRvHNgvi3GOTh3rOohBoMQg8uq1C%2FvaXeuQoFW8XfGhKpD3YsJz4zCZIdg9smfOBp0moGd5x%2B3PpAxcplKTIwLzq6h9pmRcG6P7fZFBGqkO%2B6dR55T9vDsnIiiHcKs8lFdAnFr%2BGQThJ4Nt1%2FgApwOJFBMD0ZoYNEb85ti%2FpGHM8C0VP5xp1M6NF2A8T%2Fc%2Bs6pc%2FXc0hUOHnnXueQWr7pfL%2BqRveeJZ%2BSNm7m6OMcBS0zpC6wIEWEYUddap6M%2FT6HmuG95IwhdDwvAY6pgEEPsmSx4uFFdA8jbo3moUpISUEzeIg88QGEqc3d6NF3LqeKl1F%2BpDj40uM49ATlMKVjuYjssL%2F41VVHWyAF2CVkmgnikEkd0JXlMsX8T55h%2FMwLNFqU8tPgozuzMqdYCtmkEHMSXbE%2FSiYl5uet6bM0bjpfsmnAo2Lux3n6cA2j5llJg%2BmLJWdCu0Ol5PRJYv2fu6cXWz%2F1gaGp9RTYLbRPTXwcZ2P&X-Amz-Signature=c684e11a673972d73a956ba538ecf4e57a438fbd8edea221985de1c44887ebaf&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Algorithmic Libraries
#### 1. **Scikit-learn**
- **Description:** Contains tools for statistical modeling, including regression, classification, clustering, etc.
- **Built on:** NumPy, SciPy, and Matplotlib.
#### 2. **Statsmodels**
- **Description:** A module for exploring data, estimating statistical models, and performing statistical tests.

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c62885f5-417d-4179-834f-d68f8f2bdf39/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665G7MEF3M%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T062059Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIDnEtv2cse1x04L342LuUDNulRz3Z%2BD%2Fz608qD8vORxRAiBe4taqltW5oMtOVfvc499KN43cSaw2DerEAFUwqCBOnyqIBAiz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM1POJQ1h%2FaeKNKWIiKtwD7%2FI4kCN3XvTtRUJE36YPcu8UCs83QEY8F%2FJJHIovci0DTCXC0EbgXT3108wQZOW9vD%2FF9%2BjPFOkZWJwgNdH9jsmf9z%2F9caZsF6EqkVP6IjTPC9Ov9MW1Xdqg0K4CSWd1TOPtetSIyXQroYL%2BKWSRd857VsaPENfue%2BW2jdGih0VaM6M6%2BdnnH2LeMjrHE%2FNoU9r8FYmHe2HD%2FQrtVE2%2BEArMdqiV7IN%2BNw4UBp3g57u3Y9TNpvIHPjr3ee7t1A9RAVPthjjJU71KtTeuWrSsgKJuuqaD5FCL%2FGkZgNewu%2FVSE0aWjZALGFXgwY5BaXbevknL9ZVxKtSc54CvPGYXgCMSImEurQRTWbKx3zHFtkAvicDXlB%2FYvRvHNgvi3GOTh3rOohBoMQg8uq1C%2FvaXeuQoFW8XfGhKpD3YsJz4zCZIdg9smfOBp0moGd5x%2B3PpAxcplKTIwLzq6h9pmRcG6P7fZFBGqkO%2B6dR55T9vDsnIiiHcKs8lFdAnFr%2BGQThJ4Nt1%2FgApwOJFBMD0ZoYNEb85ti%2FpGHM8C0VP5xp1M6NF2A8T%2Fc%2Bs6pc%2FXc0hUOHnnXueQWr7pfL%2BqRveeJZ%2BSNm7m6OMcBS0zpC6wIEWEYUddap6M%2FT6HmuG95IwhdDwvAY6pgEEPsmSx4uFFdA8jbo3moUpISUEzeIg88QGEqc3d6NF3LqeKl1F%2BpDj40uM49ATlMKVjuYjssL%2F41VVHWyAF2CVkmgnikEkd0JXlMsX8T55h%2FMwLNFqU8tPgozuzMqdYCtmkEHMSXbE%2FSiYl5uet6bM0bjpfsmnAo2Lux3n6cA2j5llJg%2BmLJWdCu0Ol5PRJYv2fu6cXWz%2F1gaGp9RTYLbRPTXwcZ2P&X-Amz-Signature=4bd79872b247d4222fbbdb0ddeee3f66d1fc9b4bbcb3a1feeccd3eab15134a06&X-Amz-SignedHeaders=host&x-id=GetObject)
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
