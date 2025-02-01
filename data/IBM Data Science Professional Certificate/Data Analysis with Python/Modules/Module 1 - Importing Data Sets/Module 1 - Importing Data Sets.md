

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

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/997ac361-58a8-4f04-bb0f-79fea4baa761/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WB7QSAX3%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T051324Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDFVoAOxoAGHvF6UkgUJahmUHAuXOvVGmgWSPQ4nemucAIhAL78XomtC6dbDuhpBEITnCMddmvw48Q58aaE8nIMk%2ByuKogECM3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwZWdEeWocyeTR5o%2Fsq3AMmqQJQ7T13y3DxiDsRtuP26a%2FBf3NiDx00yadUIVhZAX1HsPQ1o6Dt7QskCxI4IxM67YmEKpcU71y%2Byw7VcNx5uLDRb6kNCfWl0C6ucwxwzsD%2F9sy2Jc%2FUNUejVrnpqkUVDEMBn21Jl4VxrJmSsjCyG4oRyYijZWSbK1ESwkXDa%2F2kZudOOP8BHYS85sC2U3E4zapjLqkSkbk%2B%2B1u3iCSEb8bl%2Fq2AI0m2ri62ftckSdbAXtSY3B7eO1yX9%2Bu41UIittqN%2FnJVzgJoUVcUwLc0SVfsyfZozjG5jN7XK0UKOmwBVoALKtaxRPuLd65f47FbEzWPiK%2BFASb%2FqzQ59MUNs05jPEQMPX7i%2BfmJBj%2F30dCj7fUsWGt%2BZHI3cidP7OtCbIKWpvdYLKqEYhSnlC6dq2mf4wqzIrHRqUIPH%2BE%2F3TonR8O02qXjQugkbf%2BIMxpo5Y95lafl4SYCi8gZYH92AsdL06CaakUuyZ4W27xK4rNmNSfUriaE0H4%2FQNX0xXMiG0qFE0vAldlUmfbqn938a3r6%2FiUSvJAEZXrOqm0kC4nA%2BYp8PAdMl%2BktD2vPOayOrFyjsX6pykqBNzcDVcrbEgCv9vZp3279ey7jHD%2Fn8DK7m43UNgveZQBWODC1wfa8BjqkATxvcdvXvwGxkCDRZmTZf4NlPwC7BIOPxd6nt%2F%2F52%2FiHdt%2BLJhzLfra%2FdEhInzJHzhgXoEZOlfZTkrunjDPFWoVW9Wl4iaqQeWn8USPBgUra5MmtGi2SZWef3siFrkmdtThx3tnwRODiUNuXlrBDgf1bmbnHB48idBmAx%2B5NSAGzejlvwBcHUITO%2F4QW2IjItjQkl3GnkoHxNoYVdKxT005wnB3A&X-Amz-Signature=c7e607b7ab4f13445e6b496aa7c48e99017b98caf9a5bbead8004c03fcba17be&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Data Visualization Libraries
#### 1. **Matplotlib**
- **Description:** The most well-known library for data visualization.
- **Features:** Great for making highly customizable graphs and plots.
#### 2. **Seaborn**
- **Description:** A high-level visualization library based on Matplotlib.
- **Features:** Easy to generate various plots like heat maps, time series, and violin plots.

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/733d1e42-5a53-4fd8-90c1-3d85254369a6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46627TOFMEB%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T051322Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIBQxukR%2FzxDPz7vaJ2FZUNQF65FokWD6KTPRsBTHegwSAiEA8BJxH%2FapZakOB2c2ZI2ji90QYcAL9ZXBqF49KNHRBqAqiAQIzf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMrgAdIcsPq5jZSuLircA06ncXQ63VLE1PIzPVAerc%2FWGfxxhk%2B5wp0TW2n0TSe0JRI0JYUsFONyG1XoGlR5KYPeDdmv4zzTPnEmlGHGeNx%2BOiTN5jMjYDlg2rSkYRXhUmb5%2BeRLXg9soNI0dshG5X7Gpa5cGdE0TxpvUUJe646TxFMGnD8Fbj4niaNucY%2Fyq0VOmPTZcfxwaJ7hcITesqeRe6YaraYhHvjbHMLLu5ly60z0i6McK7U%2BXrdqw8YcKAyL96PlOxmOmrrm2OS4SqxEx9m%2B1X4ro%2B6DLkxL3p1dA5xreXAf7Ehz5OBd9MwT7U2cgRvp21aif4GPAMVm%2BmgqRNPVp8tvXAZfR8v2qemZegtPP6tIoDviMCGt925%2FH%2BkS8b2xi6SCRb%2FEY6UfVNh%2BCH5POdEJ41nw7%2FGh8xg1cJkXU8ZyPz7Y%2BGbCzWR8OSG0egW3bIBC6VIEnjRsiYbtYwnitgn56EuqwBFnVHQAR6DeQ4OPK%2F5a3l6dMr3KM76thyMXSGFmNmpm91FpjeynCPo7Ux9OYRjZBGk23UMURd67CLzuXc207rkD1ggv%2BEXvkk40ZepFdVqad4DyACuW6e4m4snXXD3mywWacIO6JNXEfqt%2B2YDYTdPUyQlsjWou7T7M7UqNcNXNMOfB9rwGOqUBJGkVFEV4meAH6GEOPZFBCOJmvYLW8u%2BDufgqIBgt7U%2Fg4D2ZcTW807dCJm8hw6IPBpsthF9Jfnph%2BHHK3RnuJ041NgfnUUkH5jqrPObTWbQlsymlF7iBZ40Zcex%2B0%2Bbls3FfnB%2BDpqzLLe39YYvIhW%2B%2FqLn1VpDEfxPxmJDSwu%2BvC5QV0LR3uoh7ylfWWN%2BbXwy4sJAs%2FZj5ZiPeCBzu2oLChBCc&X-Amz-Signature=d81d661b4dd053184c8fd4c9aab5433badd5c0b763c3807c67eae788400e38e1&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Algorithmic Libraries
#### 1. **Scikit-learn**
- **Description:** Contains tools for statistical modeling, including regression, classification, clustering, etc.
- **Built on:** NumPy, SciPy, and Matplotlib.
#### 2. **Statsmodels**
- **Description:** A module for exploring data, estimating statistical models, and performing statistical tests.

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c62885f5-417d-4179-834f-d68f8f2bdf39/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46627TOFMEB%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T051322Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIBQxukR%2FzxDPz7vaJ2FZUNQF65FokWD6KTPRsBTHegwSAiEA8BJxH%2FapZakOB2c2ZI2ji90QYcAL9ZXBqF49KNHRBqAqiAQIzf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMrgAdIcsPq5jZSuLircA06ncXQ63VLE1PIzPVAerc%2FWGfxxhk%2B5wp0TW2n0TSe0JRI0JYUsFONyG1XoGlR5KYPeDdmv4zzTPnEmlGHGeNx%2BOiTN5jMjYDlg2rSkYRXhUmb5%2BeRLXg9soNI0dshG5X7Gpa5cGdE0TxpvUUJe646TxFMGnD8Fbj4niaNucY%2Fyq0VOmPTZcfxwaJ7hcITesqeRe6YaraYhHvjbHMLLu5ly60z0i6McK7U%2BXrdqw8YcKAyL96PlOxmOmrrm2OS4SqxEx9m%2B1X4ro%2B6DLkxL3p1dA5xreXAf7Ehz5OBd9MwT7U2cgRvp21aif4GPAMVm%2BmgqRNPVp8tvXAZfR8v2qemZegtPP6tIoDviMCGt925%2FH%2BkS8b2xi6SCRb%2FEY6UfVNh%2BCH5POdEJ41nw7%2FGh8xg1cJkXU8ZyPz7Y%2BGbCzWR8OSG0egW3bIBC6VIEnjRsiYbtYwnitgn56EuqwBFnVHQAR6DeQ4OPK%2F5a3l6dMr3KM76thyMXSGFmNmpm91FpjeynCPo7Ux9OYRjZBGk23UMURd67CLzuXc207rkD1ggv%2BEXvkk40ZepFdVqad4DyACuW6e4m4snXXD3mywWacIO6JNXEfqt%2B2YDYTdPUyQlsjWou7T7M7UqNcNXNMOfB9rwGOqUBJGkVFEV4meAH6GEOPZFBCOJmvYLW8u%2BDufgqIBgt7U%2Fg4D2ZcTW807dCJm8hw6IPBpsthF9Jfnph%2BHHK3RnuJ041NgfnUUkH5jqrPObTWbQlsymlF7iBZ40Zcex%2B0%2Bbls3FfnB%2BDpqzLLe39YYvIhW%2B%2FqLn1VpDEfxPxmJDSwu%2BvC5QV0LR3uoh7ylfWWN%2BbXwy4sJAs%2FZj5ZiPeCBzu2oLChBCc&X-Amz-Signature=cd652772f8df2c864a508021bbe792a376be6af01fa41aaad3cf37096cdad682&X-Amz-SignedHeaders=host&x-id=GetObject)
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
