

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

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/997ac361-58a8-4f04-bb0f-79fea4baa761/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VT3SDSGW%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T201608Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGQaCXVzLXdlc3QtMiJHMEUCIQD50f2cVV4NDhic1Zm9trhj05%2FTjXp4i92JY4b86IGOBQIgQehCHDV6g3d1RlikTAbTureo%2FIgi7%2BLale%2B%2B6STkMAMq%2FwMIfRAAGgw2Mzc0MjMxODM4MDUiDHAjTa4wBL55wAlCXircA4jF%2FVjdJwNRnUtJhqcO9cpI41dsRkZHHqgBSxi37ccljeX4SsUqvC8STHo37iobnPbbpHss%2B1hWaCYnWSSZER1%2B9nJgfZlys7VA8PjaYwowBWb0CnNjrvGaj7Zea5y%2BzWl9Ci3NHsUmKs%2BBLXPUA59%2B8at%2Buv7ldOk35C6%2FgjJHF1HqOJyXCiKqEAzM3k44lYdjF%2B8Qb%2FPTtsrHUM81wYDSi%2BLuFILfO7PRebKcbwz7tQlsB3fEmu4H5jA5aVDNYXJUlqAAAA%2FsjUmHD7NUANGH0WdyZeCmZJEXWlKcE%2Bm08IRUYq4tylRDoXj6XEdeE1BEBVcflqUkLm%2F%2FDpvohOPOQ9vyhemjY3moIedlNsvKDkuEFYPw%2FwZoK6iWTGkYMRt%2B89hqGhb6gUC%2BHNXQjQFXiBu0FgI4LDnexBdDxiLQD7kQcGvArmSTnfvHZyoXaGOya4mGb1u6r3Z69QFg21DCgtsuhgSnGMhRbebSHzRS3ytCpx2cdBWloTdXKYCUx%2BNpmLZEPM3Uwo%2FTv79ZYzgVPYO5XvuifxzID7TUr8IhYJw%2BputYtXDqadHMLiWMEvYEwUCWd57HgjDb87AZU8JrNuYsXyKQzGV9IXVnVdKeAOZIcFHwS2Sq13IxMN3Smb0GOqUBcXZufgnbDIJucdxZAMnEupjYiMBg%2FUj2b9pVk8tqKBa8X3ovlFOmYJCZ2Od4H%2BkkOBCW9vAj38Wn37%2F5UAPy6CfWqRFyua1nEEXeDvW4STvQ2%2Boot4Cj72jR5i6AMdZrafdZEDmNGJEwzaqKbisRzpVXEeZJdqt5DfycMLMIxJMaQiPxdaMDV%2FRVoR32I4v1dqlZsC1cMATj4cS2ep6wDdvIG4gb&X-Amz-Signature=53f8c148f593a21f82107317cea1478489c0e107bff764fcf3af2793d39b1f95&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Data Visualization Libraries
#### 1. **Matplotlib**
- **Description:** The most well-known library for data visualization.
- **Features:** Great for making highly customizable graphs and plots.
#### 2. **Seaborn**
- **Description:** A high-level visualization library based on Matplotlib.
- **Features:** Easy to generate various plots like heat maps, time series, and violin plots.

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/733d1e42-5a53-4fd8-90c1-3d85254369a6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T3YXGIZ5%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T201607Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGQaCXVzLXdlc3QtMiJIMEYCIQC0AHSwdJnRfNe%2FpZdNKlmJyykmAyDsg%2FyYGvEuYSnsJgIhAJo8goCOMUWd3DJhBXQs7jWMBHwz33Pwk1AedNRIFxCrKv8DCH0QABoMNjM3NDIzMTgzODA1Igw4plSljUpM1A3QcZoq3AONTy9b5dXe16ONPVcGdt6nZKr%2F6yBKexdySVeqta0W129lkhfxwppCOBZid0SOB%2B0Vcyg9H0fh1sdGa7a%2FVMVW65AcSd%2B0ocQ1ShQtENnY3yTzhc9NI4mOomoFHJXLjfNGq%2Fogz7nNPp92q3R7BMGjHEZF%2FgK5FHllEKPZ1jzCR3x7Mj7lNowfDA9HhamReQ%2F2DENfsLr67AA0b4DMqS1p9yrj9F8RAv7dwt0pVjSACEk5f7e60GImA%2BRT%2BtmAidOWQtwQMgeGg%2FRxusNVaOWnHjWnlzqml8IZB5QInR0xDThx6DWVzoIHo5pAFuyUEijPl2k49ouAf%2B7KMgKemVMAEvY%2BjxGAwhaqpl9%2BGlMFDkQYASm367c738ZLd8uVj0i%2BkXCc2NbmJC%2BTYQ%2BaCZZLy%2Bt%2F%2BQFm81FnbxaivURIEwoPNi6OyEt6Gl1YsQUA%2F3hgKTlNYwPeCRS3Sws5dtMEmo1k5SBpjzP5S7QdTjGWQfYf1c2qcod38oV7v4Ht85YB07x9Us4zuKRUS9SsSaNKWF%2BwAcZcAvhnyjd7EY7By2U3ORBbMjHZ6J6MxwGykEyTWtusomjan%2F3JUMdec%2BCz2%2F0v6HjfTXHkdC0WmUdm7xZXCf4zqGmg%2FsiFczD40pm9BjqkAbbEBo%2B7v9uCfm4mSTfCJ61OHaY8%2BBH8Fry8U7t4QeN%2FUyv3TPUgiJ5IYeteI6q6Y3tWWrokNkDr6EPaoBR0W4a9G4cSEy26JQ6c4zHlK4EkUQPLqnwjd6Pi1OzE%2F6ia9iCvsg3hUZFV5muDf43pEZ0516BeFo%2Fcx7Rwx8sbnhh39FogcI9lm%2BAhQ9pyRxHmDc2jSKCpTrzdioFDtfki2TyERACl&X-Amz-Signature=cb882a0a63cfb17688f2debebd6ddd0f72d0be5162336723616c2ce3082ebe92&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Algorithmic Libraries
#### 1. **Scikit-learn**
- **Description:** Contains tools for statistical modeling, including regression, classification, clustering, etc.
- **Built on:** NumPy, SciPy, and Matplotlib.
#### 2. **Statsmodels**
- **Description:** A module for exploring data, estimating statistical models, and performing statistical tests.

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c62885f5-417d-4179-834f-d68f8f2bdf39/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T3YXGIZ5%2F20250207%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250207T201607Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGQaCXVzLXdlc3QtMiJIMEYCIQC0AHSwdJnRfNe%2FpZdNKlmJyykmAyDsg%2FyYGvEuYSnsJgIhAJo8goCOMUWd3DJhBXQs7jWMBHwz33Pwk1AedNRIFxCrKv8DCH0QABoMNjM3NDIzMTgzODA1Igw4plSljUpM1A3QcZoq3AONTy9b5dXe16ONPVcGdt6nZKr%2F6yBKexdySVeqta0W129lkhfxwppCOBZid0SOB%2B0Vcyg9H0fh1sdGa7a%2FVMVW65AcSd%2B0ocQ1ShQtENnY3yTzhc9NI4mOomoFHJXLjfNGq%2Fogz7nNPp92q3R7BMGjHEZF%2FgK5FHllEKPZ1jzCR3x7Mj7lNowfDA9HhamReQ%2F2DENfsLr67AA0b4DMqS1p9yrj9F8RAv7dwt0pVjSACEk5f7e60GImA%2BRT%2BtmAidOWQtwQMgeGg%2FRxusNVaOWnHjWnlzqml8IZB5QInR0xDThx6DWVzoIHo5pAFuyUEijPl2k49ouAf%2B7KMgKemVMAEvY%2BjxGAwhaqpl9%2BGlMFDkQYASm367c738ZLd8uVj0i%2BkXCc2NbmJC%2BTYQ%2BaCZZLy%2Bt%2F%2BQFm81FnbxaivURIEwoPNi6OyEt6Gl1YsQUA%2F3hgKTlNYwPeCRS3Sws5dtMEmo1k5SBpjzP5S7QdTjGWQfYf1c2qcod38oV7v4Ht85YB07x9Us4zuKRUS9SsSaNKWF%2BwAcZcAvhnyjd7EY7By2U3ORBbMjHZ6J6MxwGykEyTWtusomjan%2F3JUMdec%2BCz2%2F0v6HjfTXHkdC0WmUdm7xZXCf4zqGmg%2FsiFczD40pm9BjqkAbbEBo%2B7v9uCfm4mSTfCJ61OHaY8%2BBH8Fry8U7t4QeN%2FUyv3TPUgiJ5IYeteI6q6Y3tWWrokNkDr6EPaoBR0W4a9G4cSEy26JQ6c4zHlK4EkUQPLqnwjd6Pi1OzE%2F6ia9iCvsg3hUZFV5muDf43pEZ0516BeFo%2Fcx7Rwx8sbnhh39FogcI9lm%2BAhQ9pyRxHmDc2jSKCpTrzdioFDtfki2TyERACl&X-Amz-Signature=4a0b435bbae0c001fd64c595e174cf2e85b5ef9474e526a3f37c8916c94f02fc&X-Amz-SignedHeaders=host&x-id=GetObject)
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
