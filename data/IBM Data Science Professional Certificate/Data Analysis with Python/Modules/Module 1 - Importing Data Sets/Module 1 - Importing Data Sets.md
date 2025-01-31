

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

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/997ac361-58a8-4f04-bb0f-79fea4baa761/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XJSNYPGW%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T151404Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCsa0nSyUzJzz9WX78wIibyfHp9E5WD1i3If70AwCQdxAIgI%2BIqNvv0XwpxbMBYcec5zm2gtQOhiFUF4lv8%2B6qvZ24qiAQIwP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPpWbNqY1qADV%2B2ODircAzlVvZpOnVSkfh5KUJNlDwJhI5S8XSuigc8exID6GIm5%2Fc98CI7zFjYtfr9axPVPg40vBbeSqqCI3VM7HmiP3xK0Psmk%2BO2%2BUIUJohiyon%2FbTB5CwNg2z5x7qPhTzKQERDUni4EFKYbCFAXsh0x91x3BCwaepC67kyZeZ%2FZtPe5l9j7cncdHTVAhyzIErFXnbpcHGjBHZRnJ7gi9uIjwHGD54h%2FOmiG9d5A02NwWHK5dBl60quqyaUvCv565OvcrUIDbbqxLmp7Z7mtMTv6BWDN03CLtdOMeSKKbxP%2BJkk09r0JWQu9DYeNXJEZHyGwvLRmc8i0IjCo%2FqBp3he2l0K3Y3uXdoHhCvqLG2LQQZMjT9N7wBbgtWCcDqk97XmBk0SzfeQOSlRRuMKFLcvj6aK%2B7blKOKDksQJj1yZW8vlXgMbAegEXc4AvbVprvdnQ0m1qgHOi7wTsiPamlMXnL9FwumCEUgy2hJrqdejyggNz7g0q%2BV%2BOBiHdAtES9gkrdCw3OOKjjK7q5XUGPSY3fJUrfl3aQT1wIZrGe6u3rkhlEZ0YcgYh30XMVoZaq%2FEcGbjhbi%2FxNcfqhHMbmfNpBXLq%2BQr6LV75a546NU1fBxhHRc9apSKiCplRjAtkvMMrI87wGOqUBNTVaZqwMTQTgyxKN4TKYqMOyDybUy5g%2FW88EztU8bXBerZcoy%2F6qxIGVgO%2Bb933q4HP9t25XusbPMHYPUKk8AUMRghGhWroMh4xifbqMPKirGrpBGbjB8xihfet4w3qNghdVE0c2VFtwJaFHqn%2FKBgaKFosh%2BJDYfGiAVHI4QrDIz2%2BTt32dosTq%2FcdiNAamwxOUv7cT348uavuEIBe%2BhtoaCtxc&X-Amz-Signature=e051b3a0b263de53ff6a62441979199951ec53c438c152b25edacddc32ef065e&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Data Visualization Libraries
#### 1. **Matplotlib**
- **Description:** The most well-known library for data visualization.
- **Features:** Great for making highly customizable graphs and plots.
#### 2. **Seaborn**
- **Description:** A high-level visualization library based on Matplotlib.
- **Features:** Easy to generate various plots like heat maps, time series, and violin plots.

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/733d1e42-5a53-4fd8-90c1-3d85254369a6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WFN3XXKI%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T151403Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBL1YxpxSTaMmAH86acQ161Tfc3Y50kG4enUlqk2Kh%2FBAiAxeqiQ1faDyGRwCSSxmuFVteBxDNvwUE67x68X%2FHvG6SqIBAjA%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMGcbDk8hjg8cuJDxAKtwDHMkbZmDpLGRcGxSEU%2FcLAZ%2FYC5jkxsjWTsSGHmsES1TCF84URY2wD9pKPsxqyCFEI6D0eGheJsKjj3VAK%2Fl9A2Xg69kak1z7KKUU%2Bg%2Bro5k4Yf9cVi8ALe%2FihSFzt4TJwLcA1ifxy%2BAWH094v7uiGhMJreCsFYDX%2BbUFHmRdbxLHNHrtnwhQp5D7TZeYf9H7rEf5PRENFYky2izprjmUyn96WagV7zNHT8M8oCTdo8By3YZCqNds3QMQHY9CH8j9SYhT4vSFE3zt64OOgo3n%2FhYd%2B%2Fl1CK%2FFT3LLWzyjvICHb24sFEH7nRxcRMoYcZ8DAq6xR%2BjLVTu4lRImxUaiNvdpOklcbC106%2F7F%2FSwXkfHL%2FxLVQHjDlZkJNsiv41ip7zB3oZxqY5yJzABuYf7N0ooHbwzdE6%2FyqQlMPHP72v1GcVLyf558Lkzg54%2BTEBWtW4jELWOL9nzA5%2Bptp0P5XU3Y4ZIZaKo3Hf1k3VfGMOPLfeQ0k8W%2BmXz6is315%2F0%2BPD0cOumysn2O7nZfEcL35TubwUxk5JGiuBjFnunLuKobfqbTN8zRgShDmxlb861StDYdfyWiZGDCwFfW9dx8lYnTlsyZfCz0CMC7VwZfnS9R5%2Fk1yD6DAtJqyrswzMjzvAY6pgFSXr%2FLgkAVAz8nP3xa3Vj8MfR2Mn2lVT9IqMcGdixhwWKwl4kfY4CYsskgI31b8jziJ0tass4x9jWEq%2BqbcfyYU1%2FsyraKGMDxkI0wpamJyKBek3o5kllO8devqnBs7l113VA1IakjCKiegg6%2Fo%2Fq4kjIi%2FoWqps4zZLXgJmlwrhWsuv5oKoreGV%2FkyAU4NzEaCsMmHYa59cmnCEIYGaAEzA%2FZeKyo&X-Amz-Signature=2428c5f5d8fad09e7dccd7c14190f2360e5fdccda9201c7627d3229e51458df5&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Algorithmic Libraries
#### 1. **Scikit-learn**
- **Description:** Contains tools for statistical modeling, including regression, classification, clustering, etc.
- **Built on:** NumPy, SciPy, and Matplotlib.
#### 2. **Statsmodels**
- **Description:** A module for exploring data, estimating statistical models, and performing statistical tests.

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c62885f5-417d-4179-834f-d68f8f2bdf39/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WFN3XXKI%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T151403Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBL1YxpxSTaMmAH86acQ161Tfc3Y50kG4enUlqk2Kh%2FBAiAxeqiQ1faDyGRwCSSxmuFVteBxDNvwUE67x68X%2FHvG6SqIBAjA%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMGcbDk8hjg8cuJDxAKtwDHMkbZmDpLGRcGxSEU%2FcLAZ%2FYC5jkxsjWTsSGHmsES1TCF84URY2wD9pKPsxqyCFEI6D0eGheJsKjj3VAK%2Fl9A2Xg69kak1z7KKUU%2Bg%2Bro5k4Yf9cVi8ALe%2FihSFzt4TJwLcA1ifxy%2BAWH094v7uiGhMJreCsFYDX%2BbUFHmRdbxLHNHrtnwhQp5D7TZeYf9H7rEf5PRENFYky2izprjmUyn96WagV7zNHT8M8oCTdo8By3YZCqNds3QMQHY9CH8j9SYhT4vSFE3zt64OOgo3n%2FhYd%2B%2Fl1CK%2FFT3LLWzyjvICHb24sFEH7nRxcRMoYcZ8DAq6xR%2BjLVTu4lRImxUaiNvdpOklcbC106%2F7F%2FSwXkfHL%2FxLVQHjDlZkJNsiv41ip7zB3oZxqY5yJzABuYf7N0ooHbwzdE6%2FyqQlMPHP72v1GcVLyf558Lkzg54%2BTEBWtW4jELWOL9nzA5%2Bptp0P5XU3Y4ZIZaKo3Hf1k3VfGMOPLfeQ0k8W%2BmXz6is315%2F0%2BPD0cOumysn2O7nZfEcL35TubwUxk5JGiuBjFnunLuKobfqbTN8zRgShDmxlb861StDYdfyWiZGDCwFfW9dx8lYnTlsyZfCz0CMC7VwZfnS9R5%2Fk1yD6DAtJqyrswzMjzvAY6pgFSXr%2FLgkAVAz8nP3xa3Vj8MfR2Mn2lVT9IqMcGdixhwWKwl4kfY4CYsskgI31b8jziJ0tass4x9jWEq%2BqbcfyYU1%2FsyraKGMDxkI0wpamJyKBek3o5kllO8devqnBs7l113VA1IakjCKiegg6%2Fo%2Fq4kjIi%2FoWqps4zZLXgJmlwrhWsuv5oKoreGV%2FkyAU4NzEaCsMmHYa59cmnCEIYGaAEzA%2FZeKyo&X-Amz-Signature=8122c066f905936282c21a2a6524e7c555f7ce4ed7434d46188be0a836df714e&X-Amz-SignedHeaders=host&x-id=GetObject)
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
