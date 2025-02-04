

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

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/997ac361-58a8-4f04-bb0f-79fea4baa761/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665EZTQOQQ%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T171248Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBkaCXVzLXdlc3QtMiJIMEYCIQCorptqEDSx3dYq9MUja40p73kSzv3HLxlll9VYx2O2pAIhAIrKzVNGZawJlt0lzmomNbJzD4fv7FpnkLbiI%2FjGlvBrKv8DCDIQABoMNjM3NDIzMTgzODA1IgwvidjM93R8Y%2B5Nf%2Foq3AP%2Fi%2Fb7coDyLnWvqwl0ZHnHTMr83dWiE6T2lljr%2BX827OoEFFuVN7niiS88uZoThSL09uro2metM73B4lJmlrxxcIL4rQ%2BEUiMLH61j24j6WddHKQ8nV5c%2BRjtrurIXI%2FIvyufy0yp1LWqA9nlDzQDwyna%2FHCzl7hp1qol60lapZenWm9PCxX6ix4Y5Xg3tGpNfCzTZ0muWNALwjOwogaaB7tYekjBW1h%2FoOzKHcwQbxdscbkh3g42EmM%2Fm%2FyTncc0O8n3ksv5tLzjMjpqezuknF5UGPmTEXJvpQ9l9ua2OREs4APoqckj%2FYp4OAl6rkfYoOv7n%2FcKELBPNbSX4CkL8a8%2F2XwynqbtO6VzuBRKN86wXhEBY2VYpNUcp5Y8yKmhME6EIfGaSHA5o5JIE1DFuKm8fvmvBxM9Ts33Jn%2Fe2thYL0Eroq9wpsKPaFgJVqyU0JfBxR1m024tfymPANLENthWDN%2Fb4TkDqv4gnzJeZNkwoDIsEb74zl97rk5IcjZNtfwXJHk%2FLN2ZlGZ2rGX9mJaqLiPAfaYfRcgxBeLJaYskbLIBmGDJ0OrCCHRE5%2Fb31dlbS7U8ehgMIFRI3516FRFwW1R%2FArd71YylLS0Hw%2Biykv8O5kNs1z3vEKjD%2Fg4m9BjqkAaJhsLu4hEkMKeZfbUs1QQ83EIkJ9VvANfxobNg6OKWOvDx0cU391NJko%2BjDVw1JADXqezxczvLd1ahJ8k8nWFe76xGKK0NdKhwIsN0Jw4N9NDjTxz6n06xJPmvk475RHo6RLZLF2%2FYESGryXAV6OIWJ9XRsDSJVyOcawRbgPcVfocVfoWpzDBbn56Eerv2b3OuwEx7oTFoIMTn5%2BktgjkfMiFv4&X-Amz-Signature=1028e9409674f849cf73cf61f230eca11f17cee4d01813136869dbe04e22b7f4&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Data Visualization Libraries
#### 1. **Matplotlib**
- **Description:** The most well-known library for data visualization.
- **Features:** Great for making highly customizable graphs and plots.
#### 2. **Seaborn**
- **Description:** A high-level visualization library based on Matplotlib.
- **Features:** Easy to generate various plots like heat maps, time series, and violin plots.

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/733d1e42-5a53-4fd8-90c1-3d85254369a6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SLWAYE55%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T171247Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBkaCXVzLXdlc3QtMiJIMEYCIQCKPgd3guseo8YhkdK6yPtah2wj%2F7eAec9tpKUMAEGmmQIhANdjPlpb5d5VL7ROS0jbFhJS5AdmfU%2BO%2FoYTkNLd%2BDXKKv8DCDIQABoMNjM3NDIzMTgzODA1IgyLv4K1bJUKH7H9b9Iq3APi3hPQaugp%2B5beXS8MeO4RS8c87ityJyTM%2B3nesffxjlRMGLD0MXvXPGz6s1X%2B3qvG1kAEJ%2F71OHowc%2B4zactWu4obCp%2F8hUAsS%2FyB1nEnaMX%2B%2BHgWQEfrdECcgOQzH1icWKiW5M1bJi15k4pDNhhpILmLENLbb3RUVUHvGgeXYV2%2BHWgdadj3SfnQgYZYWslOs5rnW%2BzibJxHX3vIaxyMzTo3CF6SJ%2F9XUIhU9sba9%2FXY3iWniY%2F4uWlKyUI%2BNgNyDwpB0Z1zavDvor5DC41pS%2F3LRJ530MyED2o4Ch9nsgeU6GNF%2Bfn8sEzqVo4eZOCs5P5pPh%2Bos%2BHiOeLLnMUalEjcAo29%2FAtZfHdxmH%2BsYPDEK7g22Hx29sXX6KkVGEhAxPGiOnri%2F0JQs26sL29GBnY%2B%2B4ZeEFenrr6hsU9rg3ZlbP7Ac2r4KN%2FoJDCnfcsGSOTGdgWAQ14lyrwLuI2lcCODe5DOLPa%2FVjKbzrbSzZS2Yg5ppKe%2BtO%2FhupCLs7sShXCDz7XEqg2ky4vjbM2wcvlNoSf91IAC5RwhizTtkV%2BCRH5c4tuIBqR4%2F57%2BNnhJI%2FApLIVc5%2BbWQWxO4QVzRJvg8LQ3qaHkAFnN0Wvk8yT834cf4%2FiL85JL4DC9hIm9BjqkAYZ1xpCUQau7h4RjACQFr4y3ddUxVQqNIQoJ1aAmj%2Bm454QfXMljP%2BCsWvDw4ITUNl9HT1yxoFG%2FhIq7HsQukFc9ZhKju0GDaEVhYBkYQ550OjlIQ4qEGrWX2sPaAOEDR5LsrJ9jYY7JMTTiuHAopgjgR1I209tKqphpzHJv%2BS0ZNa5CUtQhkUPFgm0h3TLad5e5%2Fk9sTwg3Kt3FDFgP6h9jyNhp&X-Amz-Signature=bd8954ddd4016aa1c5f480280168ea6894ab00403f5f8e06d2c0ed06dc307196&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Algorithmic Libraries
#### 1. **Scikit-learn**
- **Description:** Contains tools for statistical modeling, including regression, classification, clustering, etc.
- **Built on:** NumPy, SciPy, and Matplotlib.
#### 2. **Statsmodels**
- **Description:** A module for exploring data, estimating statistical models, and performing statistical tests.

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c62885f5-417d-4179-834f-d68f8f2bdf39/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SLWAYE55%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T171247Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBkaCXVzLXdlc3QtMiJIMEYCIQCKPgd3guseo8YhkdK6yPtah2wj%2F7eAec9tpKUMAEGmmQIhANdjPlpb5d5VL7ROS0jbFhJS5AdmfU%2BO%2FoYTkNLd%2BDXKKv8DCDIQABoMNjM3NDIzMTgzODA1IgyLv4K1bJUKH7H9b9Iq3APi3hPQaugp%2B5beXS8MeO4RS8c87ityJyTM%2B3nesffxjlRMGLD0MXvXPGz6s1X%2B3qvG1kAEJ%2F71OHowc%2B4zactWu4obCp%2F8hUAsS%2FyB1nEnaMX%2B%2BHgWQEfrdECcgOQzH1icWKiW5M1bJi15k4pDNhhpILmLENLbb3RUVUHvGgeXYV2%2BHWgdadj3SfnQgYZYWslOs5rnW%2BzibJxHX3vIaxyMzTo3CF6SJ%2F9XUIhU9sba9%2FXY3iWniY%2F4uWlKyUI%2BNgNyDwpB0Z1zavDvor5DC41pS%2F3LRJ530MyED2o4Ch9nsgeU6GNF%2Bfn8sEzqVo4eZOCs5P5pPh%2Bos%2BHiOeLLnMUalEjcAo29%2FAtZfHdxmH%2BsYPDEK7g22Hx29sXX6KkVGEhAxPGiOnri%2F0JQs26sL29GBnY%2B%2B4ZeEFenrr6hsU9rg3ZlbP7Ac2r4KN%2FoJDCnfcsGSOTGdgWAQ14lyrwLuI2lcCODe5DOLPa%2FVjKbzrbSzZS2Yg5ppKe%2BtO%2FhupCLs7sShXCDz7XEqg2ky4vjbM2wcvlNoSf91IAC5RwhizTtkV%2BCRH5c4tuIBqR4%2F57%2BNnhJI%2FApLIVc5%2BbWQWxO4QVzRJvg8LQ3qaHkAFnN0Wvk8yT834cf4%2FiL85JL4DC9hIm9BjqkAYZ1xpCUQau7h4RjACQFr4y3ddUxVQqNIQoJ1aAmj%2Bm454QfXMljP%2BCsWvDw4ITUNl9HT1yxoFG%2FhIq7HsQukFc9ZhKju0GDaEVhYBkYQ550OjlIQ4qEGrWX2sPaAOEDR5LsrJ9jYY7JMTTiuHAopgjgR1I209tKqphpzHJv%2BS0ZNa5CUtQhkUPFgm0h3TLad5e5%2Fk9sTwg3Kt3FDFgP6h9jyNhp&X-Amz-Signature=83991046ab43a89166de7c6f7be27ff3733962e8077591ef575b83efabc0f677&X-Amz-SignedHeaders=host&x-id=GetObject)
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
