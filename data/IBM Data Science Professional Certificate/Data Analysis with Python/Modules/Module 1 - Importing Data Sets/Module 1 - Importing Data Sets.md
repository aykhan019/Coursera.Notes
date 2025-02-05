

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

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/997ac361-58a8-4f04-bb0f-79fea4baa761/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662RQTQCCP%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T182018Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDIaCXVzLXdlc3QtMiJGMEQCIHX5aQy8bHqFEDq7Lj7B4Rsx9P%2FxUbUwuJ5ka%2Fyzh3upAiAjBKrVxMWpuu1KvOw1fdER4isZQgzEtVFuxRIiVC7zKyr%2FAwhKEAAaDDYzNzQyMzE4MzgwNSIMerDV5uJ40JN6BAVEKtwD3VTvukd8ceB3eMxpoEGRKbtgfG7ZPpQYhO0FzfYfZIG5mMih%2BbnEU7K1C6O1AZ30TZXJwqJTtI1gNxW3DUh0HjVAvgu7kXlTA9ZMDqjJ%2BLNeXm04%2B%2BcrUq%2BuPRqem8nGohMLZCIS6%2BAqsdXD1z9QzS0qiPmEdiqvOthZHZfWXg%2BdqYLhDuCycVRDXUoAFiHttQ2thGXMr9hMzPDOXZzKs1PZvDzKaH%2BaM6AEo6BWc%2Bqjh%2F4kgIbgsqmNlUqgp58fYklj55cFbnEkMYuyjebOqx09RnWBFQoTUnx3wj6Qinu9XkpCZZ%2B7Cms5gl41oOTQX%2BE1ayulfHpTdaT6wrSAjNoX8OAeWAJzBaCQu1UwQ3L26PEue6u5fJzi%2Fvm7huKAceMxLtvmLuuPuaO5wlXL9L%2BdUitvrndxfnXwHSVQWuzZW3okMXTajvg9CulKe0F2XSK9n4%2BcCrr47XOcrct1KlyOEdwJ%2FPFkLEWwtxIr%2BmxEBzVqo3V1gN6FcLBa2B1HtPEAc604wNZr89D%2Bd5JOGk8I7lsnPGhKJITluC98Gmvn5fpblewWjrzq7%2FGiDPO11X5LtDHNNz%2Be18dlt1KKJICrXVsNTynIl3K7T8mC%2FFKBezycQ%2FkyDKIefcYwrryOvQY6pgGX4hCEFk6BL%2F%2BOWFhS8AQ1Ag39JVTGOj868dC3e%2B%2FvB8XIAqFnoEhonDHtbwZbEEtzTCOhK4WfhILyEaoKgRjJ70igEmF3hkXEtQ3AWlB2y0rVhc4hJ7zn%2B8iTlbp%2BXP6Kb7KGPQoPh%2BV4qtkm13oif90bZxkGPJDnL3ML5ltFXs3TWWOFaRKYZ1n6DXeZSS3At2Jn8mhL7YQpOnQY6pcMRAzi605u&X-Amz-Signature=d238a93753e257540768ee7130ee8e69c123dd89d4dce61930db9f250adeb810&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Data Visualization Libraries
#### 1. **Matplotlib**
- **Description:** The most well-known library for data visualization.
- **Features:** Great for making highly customizable graphs and plots.
#### 2. **Seaborn**
- **Description:** A high-level visualization library based on Matplotlib.
- **Features:** Easy to generate various plots like heat maps, time series, and violin plots.

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/733d1e42-5a53-4fd8-90c1-3d85254369a6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666OOXU3I4%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T182015Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDIaCXVzLXdlc3QtMiJGMEQCIFS%2FDpvQ6Cx0B5ay43ofddmikVi7Iu4K2KG3rudu49jNAiAfp0YoH6HK5kigEYpq4nbNSmy4KxQrbB0cTkFJ69zInCr%2FAwhKEAAaDDYzNzQyMzE4MzgwNSIMY%2B6AGmtyI8ud6UdVKtwDk5j0uJcIVG9NDii2UaBnn%2Fu0xmXC%2Bi%2BTdkLdZyQcTGw4jaMfXA7XmRsO45WcHFT%2BazRbnWYCgIzVbmjDYhPM5EXHgSBztkqTEQKmFoUHVpJHameMWeG7RCxovmpQp98hrPSVUeCEEbzfQ9FK2xEv2qIj4qUqJWAfSwiKLRI7uYB1hyDpLZA4%2BFeUPjDLV54EQ4ex%2B7VQJ%2B%2F2nWNe3tJB1nQlpZNakUVLHrRbUlqfPPXi7Rs7Xk57%2B%2FVzTgSGlvLE1bb%2FijcxFkQhrHqvZ36tKpUMSkxktoQjGiM3mWtie6xfMMybk5ywFJ5F51KZq3LcjaiI6bEPYetOX7YriJVDuOU6%2FSsTPoJ%2BOqHdOFZNZcCKTMS4JilwQ9lNMzuhCMVCz7Wxk5AtRwncG4bg4w8atudyx9jHZWQIAQE%2BTKCH0%2FV7syI2Z7XEnPX8yij1EI1h81wwDdZjQvKaK0Ebm5Ah6Q8mAzilK5v9Orihg8aHuHA3E6zrpZwo%2FoAkVksz9%2BG%2F8ngcSXYWYP15%2BXVzhM7XbrmyAf8qPQVucA1sWE1%2BXV%2FzShS9TIblhZ%2FLuR0Q72TLqpg3cMv3m3H7YII%2F%2Ffj9A7ybm6nQB9ZPEUFkaW%2F2JnhMC8aISd7nO7AwmC0wibyOvQY6pgHWKFG2ri7mqB7%2FA1fuO8SCxjGz6EIQg7xASv%2Fs0EgNKR15gD5nwVo5M4m1iP8Lwwb6jvDJb3kycN18bUkgxE2gFn37AO5ZTlSrAbrMa3nboTmhOMBKs4oxDniHXIWXjbme%2FFZReq13dNdyFGEM5imSD7bis8rc5N9quK1ejNVeg5m0M0X4onAZZPJs%2BzrTMU9dievpEiLhtjwbU1gPdz%2FVegl17M8%2F&X-Amz-Signature=7ed1152d1e09e8d160e8be8f63b0f7974705858f633905ab2effed049cf14a43&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Algorithmic Libraries
#### 1. **Scikit-learn**
- **Description:** Contains tools for statistical modeling, including regression, classification, clustering, etc.
- **Built on:** NumPy, SciPy, and Matplotlib.
#### 2. **Statsmodels**
- **Description:** A module for exploring data, estimating statistical models, and performing statistical tests.

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c62885f5-417d-4179-834f-d68f8f2bdf39/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666OOXU3I4%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T182015Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDIaCXVzLXdlc3QtMiJGMEQCIFS%2FDpvQ6Cx0B5ay43ofddmikVi7Iu4K2KG3rudu49jNAiAfp0YoH6HK5kigEYpq4nbNSmy4KxQrbB0cTkFJ69zInCr%2FAwhKEAAaDDYzNzQyMzE4MzgwNSIMY%2B6AGmtyI8ud6UdVKtwDk5j0uJcIVG9NDii2UaBnn%2Fu0xmXC%2Bi%2BTdkLdZyQcTGw4jaMfXA7XmRsO45WcHFT%2BazRbnWYCgIzVbmjDYhPM5EXHgSBztkqTEQKmFoUHVpJHameMWeG7RCxovmpQp98hrPSVUeCEEbzfQ9FK2xEv2qIj4qUqJWAfSwiKLRI7uYB1hyDpLZA4%2BFeUPjDLV54EQ4ex%2B7VQJ%2B%2F2nWNe3tJB1nQlpZNakUVLHrRbUlqfPPXi7Rs7Xk57%2B%2FVzTgSGlvLE1bb%2FijcxFkQhrHqvZ36tKpUMSkxktoQjGiM3mWtie6xfMMybk5ywFJ5F51KZq3LcjaiI6bEPYetOX7YriJVDuOU6%2FSsTPoJ%2BOqHdOFZNZcCKTMS4JilwQ9lNMzuhCMVCz7Wxk5AtRwncG4bg4w8atudyx9jHZWQIAQE%2BTKCH0%2FV7syI2Z7XEnPX8yij1EI1h81wwDdZjQvKaK0Ebm5Ah6Q8mAzilK5v9Orihg8aHuHA3E6zrpZwo%2FoAkVksz9%2BG%2F8ngcSXYWYP15%2BXVzhM7XbrmyAf8qPQVucA1sWE1%2BXV%2FzShS9TIblhZ%2FLuR0Q72TLqpg3cMv3m3H7YII%2F%2Ffj9A7ybm6nQB9ZPEUFkaW%2F2JnhMC8aISd7nO7AwmC0wibyOvQY6pgHWKFG2ri7mqB7%2FA1fuO8SCxjGz6EIQg7xASv%2Fs0EgNKR15gD5nwVo5M4m1iP8Lwwb6jvDJb3kycN18bUkgxE2gFn37AO5ZTlSrAbrMa3nboTmhOMBKs4oxDniHXIWXjbme%2FFZReq13dNdyFGEM5imSD7bis8rc5N9quK1ejNVeg5m0M0X4onAZZPJs%2BzrTMU9dievpEiLhtjwbU1gPdz%2FVegl17M8%2F&X-Amz-Signature=e85d9a3d10583f275938563dfd77f667dc0ac66d67e1fbfcb323bdadae0ee56e&X-Amz-SignedHeaders=host&x-id=GetObject)
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
