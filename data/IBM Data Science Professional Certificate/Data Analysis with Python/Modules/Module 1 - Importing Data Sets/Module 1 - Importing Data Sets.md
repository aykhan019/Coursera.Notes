

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

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/997ac361-58a8-4f04-bb0f-79fea4baa761/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662VVUFXNM%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T041713Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFJ3YFVQoIdQp5%2Fpwp05AzNkl6%2BQpX1KaGV4JJgg0RHwAiEAoQ5%2Fgh5b%2BYLJkcX2k428pf8OoCvZr1HECvwAlLHkJD0qiAQIzP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDM0UjmSdZAA7f7BOoircA8hFOonrjHsh96Suflyw6P8uU%2BXqFbdaIrahXMPQyOHO8E57Ipn3jv5q4ANWrlh7JQUkUcv6rbgbqPskOL64WSfnidI7JKNBg2Pf9U3lR6T9i2ZObwhDsmaj9fVcjLU8lwsImor%2BS9bGVkFv8YogO2GSvMo%2F0pLAPT5xoZle27HJaSb0gycr41H7g%2FcYeH9pVScJEo5BAUogXB311LB2IEaIdGBUuwz7wXyIUOJSKL9qID9U8l56vjn6Zi0tloISES8y4LgOqsd1jlaGMo7Snb9yIzuoywwdCdYnPABmcuqag3Qal9jgUlUD2PAKaA5TBKd7ktVjjFAiWlYxPbWxf%2BSKGrFGIBZLOYk8nLyT4EEMOksronk3umECB%2FAEbtgii5LWmkBT4qwoikusFwPgJjyQy51YB0fVTGgNGnUHSYWD2c5QENvdupq8qfkfETlGqKVhV0BZuCku41iJW8MolDT5z%2FAihYNbiRoE5nn7E8AkTeeYKn4LPKcyhPh%2FKL%2BL%2BMrOsUzTWvp%2FtedhN4tjDDRU5Md5JoiJUx7s54JQlmKv1EgVbynPJkK66n8iKRu1X%2Bh0TgAiCgNtWscaoGG8HjTwgjzJt8eDHUXrlAFnwN6s2spbKLs80djZsoRpML2m9rwGOqUBlNSvpO%2BZ19j6c9yyUwrsnI5V%2FCcE10fcgRZhbs%2FqlneAlbYsj2Ucr1E2IrXp1%2B7LVoS8Fy0xPFysbbamEeq65rhd4J15wCBlOMVq1jZpMZV%2FXPUxrwwcEM5uXQ0Nw8m%2BBqN1zAn2KzUbBMUZj5lnpWt9m5r78XE0gQYVyO8WW1rMV7py%2BwiDjZnKBz3DQwaAIJomsxH7vD4NyzfQZL7Y6YswBN7N&X-Amz-Signature=413814fe26426d75b80b9eb0998373862decdfa2d25e35176707f9dd19d165f1&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Data Visualization Libraries
#### 1. **Matplotlib**
- **Description:** The most well-known library for data visualization.
- **Features:** Great for making highly customizable graphs and plots.
#### 2. **Seaborn**
- **Description:** A high-level visualization library based on Matplotlib.
- **Features:** Easy to generate various plots like heat maps, time series, and violin plots.

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/733d1e42-5a53-4fd8-90c1-3d85254369a6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZAQLAOTZ%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T041713Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICRCvLca8ARWEwtQ0PAJ3NVsz9AFqxTWLiyCnBb5lHHwAiBvorifP6xHcScinzRsyqyenuTBzb%2BSsLiKXrPLIk4KYCqIBAjM%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMubfDhnj0sOpSgpKyKtwDRut6h3dnIAa8XY%2BpWFOM3Nbx2%2BWRQcbqIiPDKRi5GauhYpZDZBwi%2BtDq6dEwdW%2FJ5zgQzwvhuM4oY8F7H%2FvyWFWlJsCgmvMMHTVcgPIoK9vgUKhkBHjXVoMn%2B%2FUVivVTmIpELNSDWaKE9qBrT3nOKc5XDPlm1a01p8b0QvAKE1IW7W3A0VX75c8lfgRpXct4uu%2FEHO6I6IF%2FeHLGA4l7v6AxVV4T3hduc5oPnz4ZyhRPDGXop2Hn2pyvnG98xl06NzaJHzAtCK8wjsdVyozam2GHW6WsClFG3O7dKHe%2BhymsP9s6R1%2FmTI5dJQFNET95UJCkXnPEmJ9VdAtoALykiPD1xXEjPk2ZZpNJhvc1grpgRBYbdEwvfBtNZKx%2F0YbNhKxt4%2B3cTpa%2B8y1o3v9D4UXiplQJBApwBxFV9SW77YyIR0MdDtH%2BZ9DHVQCjruG%2BsVbgeLy2v%2Bl6bA%2Bbuqcd3IG6YCmMugfhe4lxp%2BBwtm0Lz86WU5dLLyW66eBZv%2F9V0wVCiJeZ%2FC2B2P%2FfX0dkkJ5tj%2Fiv61XH%2FK6e2CPMq8HvulpymdRNVL5Z1sFUG4h5fmaik1PIXKqkxEU0ULCG6EAI8RuawEl4HKOQpnUOO2lw3uXZBGEk1FtTZacwyaX2vAY6pgFqpiZ12fNNua%2BGP72I4%2FZVBMWbpdJc%2FNG9K4odvTJekiVmO7IauKEyFQJUzKqbdrstgJF0YaE4Qg8%2B61b7aIoS8T9baK5SI%2F6k5D9e81xCvYlmd1XWaA4k8DFEe38qQKtek7Hvdq1y9xDtHvXoE4Z1qValLUq2wP1fjrNdviKm6kk3u8l1GJyD0DsaMdafOwKynAG3tUIUtdjCy8TWR%2FbW8ti11ijw&X-Amz-Signature=3ad26b7581d88d903b578d462a82e55217e3b14af08017b00e1f8baeec1bde98&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Algorithmic Libraries
#### 1. **Scikit-learn**
- **Description:** Contains tools for statistical modeling, including regression, classification, clustering, etc.
- **Built on:** NumPy, SciPy, and Matplotlib.
#### 2. **Statsmodels**
- **Description:** A module for exploring data, estimating statistical models, and performing statistical tests.

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c62885f5-417d-4179-834f-d68f8f2bdf39/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZAQLAOTZ%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T041713Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMT%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICRCvLca8ARWEwtQ0PAJ3NVsz9AFqxTWLiyCnBb5lHHwAiBvorifP6xHcScinzRsyqyenuTBzb%2BSsLiKXrPLIk4KYCqIBAjM%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMubfDhnj0sOpSgpKyKtwDRut6h3dnIAa8XY%2BpWFOM3Nbx2%2BWRQcbqIiPDKRi5GauhYpZDZBwi%2BtDq6dEwdW%2FJ5zgQzwvhuM4oY8F7H%2FvyWFWlJsCgmvMMHTVcgPIoK9vgUKhkBHjXVoMn%2B%2FUVivVTmIpELNSDWaKE9qBrT3nOKc5XDPlm1a01p8b0QvAKE1IW7W3A0VX75c8lfgRpXct4uu%2FEHO6I6IF%2FeHLGA4l7v6AxVV4T3hduc5oPnz4ZyhRPDGXop2Hn2pyvnG98xl06NzaJHzAtCK8wjsdVyozam2GHW6WsClFG3O7dKHe%2BhymsP9s6R1%2FmTI5dJQFNET95UJCkXnPEmJ9VdAtoALykiPD1xXEjPk2ZZpNJhvc1grpgRBYbdEwvfBtNZKx%2F0YbNhKxt4%2B3cTpa%2B8y1o3v9D4UXiplQJBApwBxFV9SW77YyIR0MdDtH%2BZ9DHVQCjruG%2BsVbgeLy2v%2Bl6bA%2Bbuqcd3IG6YCmMugfhe4lxp%2BBwtm0Lz86WU5dLLyW66eBZv%2F9V0wVCiJeZ%2FC2B2P%2FfX0dkkJ5tj%2Fiv61XH%2FK6e2CPMq8HvulpymdRNVL5Z1sFUG4h5fmaik1PIXKqkxEU0ULCG6EAI8RuawEl4HKOQpnUOO2lw3uXZBGEk1FtTZacwyaX2vAY6pgFqpiZ12fNNua%2BGP72I4%2FZVBMWbpdJc%2FNG9K4odvTJekiVmO7IauKEyFQJUzKqbdrstgJF0YaE4Qg8%2B61b7aIoS8T9baK5SI%2F6k5D9e81xCvYlmd1XWaA4k8DFEe38qQKtek7Hvdq1y9xDtHvXoE4Z1qValLUq2wP1fjrNdviKm6kk3u8l1GJyD0DsaMdafOwKynAG3tUIUtdjCy8TWR%2FbW8ti11ijw&X-Amz-Signature=b05400698d0c99b431555cfb9e407f583951aebf31f96778e5025e782f613edf&X-Amz-SignedHeaders=host&x-id=GetObject)
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
