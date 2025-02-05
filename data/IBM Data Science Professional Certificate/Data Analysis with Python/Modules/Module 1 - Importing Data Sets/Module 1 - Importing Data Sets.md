

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

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/997ac361-58a8-4f04-bb0f-79fea4baa761/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46622P7Z2CG%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T024315Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECAaCXVzLXdlc3QtMiJHMEUCIDTjYiJUOiXDKR8v%2FGGln92vCsUqknVgoirnKxTwadDjAiEAhVQ2kx0iA9KpBoVpn1Tyko%2B%2FaNApgdUeNgl5h%2Bi0pXcq%2FwMIORAAGgw2Mzc0MjMxODM4MDUiDMCqg1UOQlR%2Fgbvr1ircA0%2BccB0hOXE8yoUYOzMDbPYybwmE3p2gQTzVL%2BOiatjtmJWdmbZlW28FBIAwTXKLgasQ2FXvU8QjLi1sSq%2Ff2qtqD20JkfLEDLEol4V%2BHdIaPdE%2FpMG6dSo7cXedzSIO486nkMgWS7Xf1eXA9akqcq67vzae1SPreGvVNZuNCg5XV%2Bw0520fPGU4Rqkm%2Fy2FKCprR2240p5NBrRTJ3FAP0%2FYaBAsc0qLcW%2BxdfSAH7xpvpEeo7%2BZDjdUIJSm77uoH0IR9C206DWD97dj4x6syxT4GBYRjZpqVLnOqHPmiR%2FKyYq9u%2BTEtEDH1sW7SEe8Y4HLQxoAm%2BZbp9%2BDatLRbwodF8A1X3Rn0NpPtew0%2F4OnkANUuU7l%2BqTYJrKNn52JdaGcc917hhF9My0dxnA4qYeNesfUk5VRTUJFudo7lmsnXfRXoRJk6LvAMEgkhmOidbkOoXyrND7ikB2NnxLTcSZpyGM0O8z0as8Ld%2F9Zb3uH20miGDdIQ0KwAXq5dXFgr8QT4rIZ%2BdDo6vChbhii205Tf6ww3RYiI4aZbtcAdcZJGTaLTt3OHmGxYe89F%2Bh2pUk1DzfX15hhabX5pOJ6K9gx7%2Fo1YeaS%2FDvxJXCyksd10COUbN1t7E0czLaHMPDMir0GOqUBAieSTSEVz4WqOgQiMhGnho6bfparJrOshKbngQFnbRag%2FVf5s5E3E1OJMpNAoWA%2BmOcBUBIcgmYfV3j8TgULhNpZigmZ2MSrPr2HMicsFN8IcNMwW7CI3QvcrZKmPBAqfbjfOyXNwejo77vwwrRFCUauAdrxAE455AGA%2F4sEfHohrbvdKEs9miMKwdZHjD3N1ImTYi4wQQwXvh18BNTYByjVXQNl&X-Amz-Signature=64d31cd752e2cf9fedfe00b8d0da44abdcd962e781d40f219671a044137f2322&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Data Visualization Libraries
#### 1. **Matplotlib**
- **Description:** The most well-known library for data visualization.
- **Features:** Great for making highly customizable graphs and plots.
#### 2. **Seaborn**
- **Description:** A high-level visualization library based on Matplotlib.
- **Features:** Easy to generate various plots like heat maps, time series, and violin plots.

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/733d1e42-5a53-4fd8-90c1-3d85254369a6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664DBHBNYW%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T024311Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECAaCXVzLXdlc3QtMiJHMEUCIQDvhllZuj0FbneKYDHp0Mfstw3Dta0C9LAwp0gslJ%2BCVAIgKUVyJuUlUa1jtLOj9dsS1sJp84FbTnPtfRHiYhGJVqcq%2FwMIORAAGgw2Mzc0MjMxODM4MDUiDDYjexezqyAtmvVKsircA0HKZ3VaUVCEUflYT5q5AwK2XHF8cL8FFvyz6WFwEBfOPO3w7qEFWLMPkJjYu9MfluKFuQ0xso%2BzwIsToExqBVYj1z%2BxQgL2VFsLoe4Dmk2KZl7eWmldDU9FEsdLBGUbv0tR3R%2BxvzSFSUHbhYK5tBi6kEyJGn7Seiicy%2Fxq4%2B3V%2BDiPdWiKZEBvJAleNIwXpq6DJ2S4DWAI24T83hx7WxIOtTXAhycVRmxYlCtzlnkAomrpgG3hnXuLJvrQv3mv3jbmPye3wnQkJmYF1apDRuO71eLBKYMohEVn8m%2FL8V6jFVkT43tByFoCPhK40HKVclLYJtS6TDn9uIDo%2FxNgIsQkOHR%2B8NUF%2BXTnHKbNoK5GyA4vpkx7PjYmz1HFQQR9rnwlr2bU%2BS01otX4tKGNh61zuZy8fjFzR1JkkxJw2WcjWFwT600CMsFRiZzsyB0c%2FZIpJDzQ3FkFA4MkxYigxOnT%2BZyc0%2BFO9uuVNEzw%2FE3P9m0F3gpiKVjxZHHcLS3VRs8I4caOPvivzDa5f5hReZUFBm8pXhN7aTxt8O0R4f4o2JJNR2fTn0Tf9ikveML%2BFSfruUoibxhDzXuHrxLgTwglbgJIG9Xs7gnXqR46wb8t6uXcN4JC9YvdcQHCMKvNir0GOqUBKhcazII1ExcnZ3R53tAl%2FWiSOcF9%2FP%2FFc%2F4pQ8v4OSUGRpC6WW2%2FN98pHda5T14YBzhKxqO1Obbhz0kormAiliO4jigmfYidXLm0XakdPRQhK%2B2O5SVNDV0IN6uI8GaSm1ZoIVe6%2B9ag1mzgwUEi3w5NgmVEgdS2yeWI6JNfGc5J87tPR35J%2BaRNCEaAMXLShQG9lz3Qbq5Afi8Rd2CWUlqdCnNQ&X-Amz-Signature=237c649cf923dd3bcf529cadb4109762140cd99b40f958c8bc1a29a9d4af8aee&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Algorithmic Libraries
#### 1. **Scikit-learn**
- **Description:** Contains tools for statistical modeling, including regression, classification, clustering, etc.
- **Built on:** NumPy, SciPy, and Matplotlib.
#### 2. **Statsmodels**
- **Description:** A module for exploring data, estimating statistical models, and performing statistical tests.

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c62885f5-417d-4179-834f-d68f8f2bdf39/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664DBHBNYW%2F20250205%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250205T024311Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECAaCXVzLXdlc3QtMiJHMEUCIQDvhllZuj0FbneKYDHp0Mfstw3Dta0C9LAwp0gslJ%2BCVAIgKUVyJuUlUa1jtLOj9dsS1sJp84FbTnPtfRHiYhGJVqcq%2FwMIORAAGgw2Mzc0MjMxODM4MDUiDDYjexezqyAtmvVKsircA0HKZ3VaUVCEUflYT5q5AwK2XHF8cL8FFvyz6WFwEBfOPO3w7qEFWLMPkJjYu9MfluKFuQ0xso%2BzwIsToExqBVYj1z%2BxQgL2VFsLoe4Dmk2KZl7eWmldDU9FEsdLBGUbv0tR3R%2BxvzSFSUHbhYK5tBi6kEyJGn7Seiicy%2Fxq4%2B3V%2BDiPdWiKZEBvJAleNIwXpq6DJ2S4DWAI24T83hx7WxIOtTXAhycVRmxYlCtzlnkAomrpgG3hnXuLJvrQv3mv3jbmPye3wnQkJmYF1apDRuO71eLBKYMohEVn8m%2FL8V6jFVkT43tByFoCPhK40HKVclLYJtS6TDn9uIDo%2FxNgIsQkOHR%2B8NUF%2BXTnHKbNoK5GyA4vpkx7PjYmz1HFQQR9rnwlr2bU%2BS01otX4tKGNh61zuZy8fjFzR1JkkxJw2WcjWFwT600CMsFRiZzsyB0c%2FZIpJDzQ3FkFA4MkxYigxOnT%2BZyc0%2BFO9uuVNEzw%2FE3P9m0F3gpiKVjxZHHcLS3VRs8I4caOPvivzDa5f5hReZUFBm8pXhN7aTxt8O0R4f4o2JJNR2fTn0Tf9ikveML%2BFSfruUoibxhDzXuHrxLgTwglbgJIG9Xs7gnXqR46wb8t6uXcN4JC9YvdcQHCMKvNir0GOqUBKhcazII1ExcnZ3R53tAl%2FWiSOcF9%2FP%2FFc%2F4pQ8v4OSUGRpC6WW2%2FN98pHda5T14YBzhKxqO1Obbhz0kormAiliO4jigmfYidXLm0XakdPRQhK%2B2O5SVNDV0IN6uI8GaSm1ZoIVe6%2B9ag1mzgwUEi3w5NgmVEgdS2yeWI6JNfGc5J87tPR35J%2BaRNCEaAMXLShQG9lz3Qbq5Afi8Rd2CWUlqdCnNQ&X-Amz-Signature=fa1fa70510909f941b27cc5a83258b73fd8b48d24c6b5c39b839cf6d8a1a3ddd&X-Amz-SignedHeaders=host&x-id=GetObject)
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
