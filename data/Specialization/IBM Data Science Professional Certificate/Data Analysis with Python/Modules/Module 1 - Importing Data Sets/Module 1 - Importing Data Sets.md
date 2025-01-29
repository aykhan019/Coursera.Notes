

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

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/997ac361-58a8-4f04-bb0f-79fea4baa761/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VAHQPWP4%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T031618Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHoaCXVzLXdlc3QtMiJHMEUCIQDoiJ2QImN5HYAqvuU4ceUkli0G5M941GjPZXofCL4%2FygIgGTze79bjkHPa63HYofonCDf01npkyvKcvMtuRHHh5%2BgqiAQIg%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOsxbVSmwcKadSeysyrcA%2FSAxaTepeWeNyKWB6KbIjkuOGfF5gk1RmFhX4GXpX%2FMPk6t693lQXHvc5bM8G02cqkSl4bt1DAOW47NHuPglEV94RPyEPmy0qVzPRXuBECmKtQByEZgagvlmlLu5im1%2B7QtTAmQ%2BpZY%2FCb2s5FiqZRTnJxaY%2F1iCpAf%2BeUQrry194tZKVgpgkZlzzcralhqd48qlZc2aM8ZKMWZ8kJ8wU4EcRXgtQb3GAqVSmWWfTqv9QsxJRg%2FmWlITectCO1iT9XJM7GOXIZq06TGCDBeWtTsGMV7pAhE4PCFY7jXgY3uriGP9wHIA%2FY%2FWXnpD5wg8PctN%2FG9JXFpYARFnJYhvnmqsM%2FzYPbpBZjbvjxQRzqK1ghiqXltCLosMKGXaozK7S95zL%2Br7X4fkBt2buXfmzgoUaI2uXsOY%2Fu0Gr8m2J02tPL%2B1KrsRd%2Ftrcm7m%2BAcIoVH2KCP%2FUfaXs6l%2Bj3lIXHiaItEgrezQcVPTIFZJmD7FCyW1sVbxQ%2BwqWG2OkRnpOem%2FTjfrGRr6NAg%2B%2FK1KFZ9GLs5vMmVmW3%2B%2FVipUqx%2B35UP%2BsB%2B0OVFixZiy%2BXzYNbERmTdxgVpSY3hL9x8hoUwic5%2BhPstCjQw5JBcy3ebuuQThlM%2FtlsHh7kqMMCf5rwGOqUBLpJ5TEI5rLkueky9AgjP7T3%2FJyqc5LaqZn0IvI7GyZag3yV3scBDk1UkKFQjw6hpde04fgkNdfXe2dyAoNcDLAqEXFXKkJlz%2FX2cG8E4GTx9kLumiKasxk%2BkTkO3EHbdzi%2BNE2paM%2Fuxs%2FEC2tWDtHsOEyYVR1wV30seSQ1P%2BnZ2mmW%2Fm7L6SzNKGZVd51XDg%2BIW3rugOEtKryAH3ip%2BdI5N9Qvb&X-Amz-Signature=cc81c4eb31ef0b4970254297dd12aab0565dba06fe4657c7b9b9bdec141adbe9&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Data Visualization Libraries
#### 1. **Matplotlib**
- **Description:** The most well-known library for data visualization.
- **Features:** Great for making highly customizable graphs and plots.
#### 2. **Seaborn**
- **Description:** A high-level visualization library based on Matplotlib.
- **Features:** Easy to generate various plots like heat maps, time series, and violin plots.

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/733d1e42-5a53-4fd8-90c1-3d85254369a6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RFT5N42F%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T031617Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHsaCXVzLXdlc3QtMiJIMEYCIQCnw4ZlYipO%2B7CrWlOmgbXtq14tOBDGpySslcM58irstQIhAKzG6%2FwRBmnj0k%2FgSoxSSET1sT7vptd6JiBsTLVbSI6CKogECIP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxXKU8Mmmx3Tc3lRFsq3APixi90KLxXSD0DAl9nWb4JJFMeGJxvIA8Hqg8ybylcP%2FjtXnBQy%2B5zJOB3rzOINJhQW%2BK8RkJtgP1cY1U6SjKZmLSHNulT4XK7DayD3fVhKTubcoBmnbI3Ux838sQxOoBNtwGMulPNO7lFZU4hT6h8M0bb0WHMiyvvJ8fNx0GF3tk1i8NIINvM7TQjj1DOPUoLESGLfgeyl%2Brqr%2FILSv3H%2BBHRuWUAhHSzX%2BPny1gJ%2F0J1QiXIaV%2Bz16knM%2BjL2BJecdcHaBsvfQTErXmvrIjmEOT3o2LMvtnQvPM5GLBZEAD9jIfWXuaJEI1HQWCVmoh3cC7Q9X2lwgxKxJerrlN5NL88cn6WUwqt5oIunLF1VMiEB232xpU7lpOLWLa7dDbfVvHJ96qY4V5c3InNUIDSawSiY6srpH5k9mfwFC3hgAbx%2F2mAEZxxgFMuzn67gubdPRkg%2BNkdrpi4H%2BGNZ%2FZx3fi05QWQt274x7pduUWeBEddK%2Fm%2BEiloYf4lKiJuITEkc6p%2FbTK6afad%2F0%2FdLY%2FmDoLx2QyomiKXvFwcFf%2B%2FrJADP6UsVHt4B5tMC%2FTQTXwLz4N8cd7gA%2B6O8jWc2LoXzUdlG59T5eN9vSJ4oDH34qaoLPnlKQgGiip1ETDGoOa8BjqkAcpH9baf3NTeZ7RnRtL%2Frc0mWkqPdMkQY2fCBTyRxU4Iz7Ho2krz1a3oJOxT4CFn5IMk0a%2F8rve1Gwl%2FMbdYhR5j7GU6FkPDyO3l7ovKh0ArM%2BNva8tGsJA4LHKmGX32JDR1gLR5Vr1de4qV1PIAhwfgsayaCXwCcfaX0p7lXz8Jppj%2FuBNxo%2B8lCZ0BKxigJu0j5ps3lvX41APiZi2hcuShz9dS&X-Amz-Signature=30f369b10df2680e38a6caef58fed2fb9d389e3bd652733340011af4591451cd&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Algorithmic Libraries
#### 1. **Scikit-learn**
- **Description:** Contains tools for statistical modeling, including regression, classification, clustering, etc.
- **Built on:** NumPy, SciPy, and Matplotlib.
#### 2. **Statsmodels**
- **Description:** A module for exploring data, estimating statistical models, and performing statistical tests.

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c62885f5-417d-4179-834f-d68f8f2bdf39/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RFT5N42F%2F20250129%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250129T031617Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHsaCXVzLXdlc3QtMiJIMEYCIQCnw4ZlYipO%2B7CrWlOmgbXtq14tOBDGpySslcM58irstQIhAKzG6%2FwRBmnj0k%2FgSoxSSET1sT7vptd6JiBsTLVbSI6CKogECIP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxXKU8Mmmx3Tc3lRFsq3APixi90KLxXSD0DAl9nWb4JJFMeGJxvIA8Hqg8ybylcP%2FjtXnBQy%2B5zJOB3rzOINJhQW%2BK8RkJtgP1cY1U6SjKZmLSHNulT4XK7DayD3fVhKTubcoBmnbI3Ux838sQxOoBNtwGMulPNO7lFZU4hT6h8M0bb0WHMiyvvJ8fNx0GF3tk1i8NIINvM7TQjj1DOPUoLESGLfgeyl%2Brqr%2FILSv3H%2BBHRuWUAhHSzX%2BPny1gJ%2F0J1QiXIaV%2Bz16knM%2BjL2BJecdcHaBsvfQTErXmvrIjmEOT3o2LMvtnQvPM5GLBZEAD9jIfWXuaJEI1HQWCVmoh3cC7Q9X2lwgxKxJerrlN5NL88cn6WUwqt5oIunLF1VMiEB232xpU7lpOLWLa7dDbfVvHJ96qY4V5c3InNUIDSawSiY6srpH5k9mfwFC3hgAbx%2F2mAEZxxgFMuzn67gubdPRkg%2BNkdrpi4H%2BGNZ%2FZx3fi05QWQt274x7pduUWeBEddK%2Fm%2BEiloYf4lKiJuITEkc6p%2FbTK6afad%2F0%2FdLY%2FmDoLx2QyomiKXvFwcFf%2B%2FrJADP6UsVHt4B5tMC%2FTQTXwLz4N8cd7gA%2B6O8jWc2LoXzUdlG59T5eN9vSJ4oDH34qaoLPnlKQgGiip1ETDGoOa8BjqkAcpH9baf3NTeZ7RnRtL%2Frc0mWkqPdMkQY2fCBTyRxU4Iz7Ho2krz1a3oJOxT4CFn5IMk0a%2F8rve1Gwl%2FMbdYhR5j7GU6FkPDyO3l7ovKh0ArM%2BNva8tGsJA4LHKmGX32JDR1gLR5Vr1de4qV1PIAhwfgsayaCXwCcfaX0p7lXz8Jppj%2FuBNxo%2B8lCZ0BKxigJu0j5ps3lvX41APiZi2hcuShz9dS&X-Amz-Signature=a8ff4659ea1059c0ba093be31e208130318629c3b89a8833397ac63d0946f963&X-Amz-SignedHeaders=host&x-id=GetObject)
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
