

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

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/997ac361-58a8-4f04-bb0f-79fea4baa761/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WLLGVUUJ%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T101509Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDIC2ovPooLapf81cR2xO38vFe8rCvfIScVzUSZlMBuuQIgX5idPa52DV8r4%2FgSYJBZVJNo2LrdkAKdyYi%2FgyYF80kqiAQIu%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLzP%2BHJWSIBLeKJK0SrcA1GFCDxo7sJS%2BnIOZGT558ArwcQ4hheKQ9GUUqEK2zrJ%2BLR3zgUbyyk0NxF7ExcVfQLTOZ0R9DkPLHoeB57tipU3iw0POrKApfsb4GafepP%2B09O9%2FiG4GSDkeMb09aYDjXFGrOOtn3yuv55FCgHdUZfDOEluzfbSlXh1hIuJY6L1T8hU34INUk1N1vRfHZjE9BSOVSWd3ZcxZiMiQ1UrwbdP%2F%2FbNHOTIn2mgvuaQfPCH%2FD2nbmZeQ6ePmjQqCOthDPlFSJvr%2BiFSlX5al44osYvO01aYSaxrMktUk1SER%2BSG9TV%2BAopepOQ1x5sJUU7dIrERJrxd%2Fdc9uC0BrnDYqjiogugKdMTbZ1ol%2B5IFZUCqlDg%2BDYIZkS6aq9ghI189Znv7v7zEi3TfjYvavpP%2BaCD%2B0h%2FkZOX8cAbNJJDS0oBa30Pd%2BnKhDYfTsPgEOVQPBLL67Bt5KNfXdNxaWeirA3ro%2F1JnSyljh5G2XerLt4lGqfLq8O1AARo8K6x6S4kuDYJUQ%2BU9HRPNSmYi6w66y9q2TEyH3FJMtmnviur8LdSRmnd366LTvtx86Zw97anxQUnfJSMlHnscRijCdx7cumQDKMNrfydj%2FBVybQTeqzPZ7JliuYDpuJctqiemMM628rwGOqUBSJROlikhCzVhlJUOJ7xCsKDMrs4q%2FwgXFw%2BpyBixn6v%2Bj4EZ5gtFV%2Br9pFMd56To7sajFnNcuf2T0Xt7Ah0GlGBMSumrB9Yj7BvMNQnFzt%2BZ3FMXyUrYFgF2asoM4gHf3Q2OaVa50Zv%2F2YenQfTYSDn5W8dcF%2BdONmSwfdKEul9CyGqRv1Cf%2BT%2FXy8KKnQGImabvPwOJAym%2BFawrYbxEWRM3Qiij&X-Amz-Signature=9dc530fe304e415ebd8abaea3329bed31952390a1720aeecd77aa735121fb815&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Data Visualization Libraries
#### 1. **Matplotlib**
- **Description:** The most well-known library for data visualization.
- **Features:** Great for making highly customizable graphs and plots.
#### 2. **Seaborn**
- **Description:** A high-level visualization library based on Matplotlib.
- **Features:** Easy to generate various plots like heat maps, time series, and violin plots.

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/733d1e42-5a53-4fd8-90c1-3d85254369a6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WYA72EFV%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T101508Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDGOcNKImtotMPv9f3mhKvIobdZZzJwzfe5LN8sWJGdgAiEAnt0r2vJ0qM5Nno%2FM4UrFQ3%2B960VbEWZrgAImySwIowkqiAQIu%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDD264IooAr2G17yGySrcA%2BNgvCg4C92UaobR9Pve2Pu6ru2nJd8KnhVEumr9nUjnHXgAyit0vcjjrS9%2FN9aY%2B2wSnaFgpRtgz6UNOdxKeQsIouSU96cF48BdeOYBpVIfInvxLzX7HzMRI6ahsBSMRimVhkBDbpOEeQ6OrLxrc8Ew%2FM4dyZw%2B%2BfbAVcigjHPJcvbzIK84hIgfDNMdC78B0HRuqFIbOkQrqImwdK03RuJ1JhB0nua5H96M74n%2F4XZ%2FwOu31mgqUiB6gc1t7jLNm7JYKePF4WUW5MG0OfhPcNBGvH4I2mIxKH7SUGK7AhYz%2FIq78QEupkkMOoBWWsDhC5XapM7da78uVLZsFJMs4BdIniAwpOa4rBF%2BLPVdkYnV0ZUAEspKLRvZm%2FdRZz3M928HORe1wVJlmVrHle6sM%2Fb4zc7Y%2FgjJNqbwRTJph3cu1gBk9n0nrYWIKi0s%2FbbY3%2BQuzzgkIeric224fo7zhc7W5s5wIdwIHCfiplBNy0Ci53wOtP9jMIHRsYc0YEXjjhqah0nXFk0gDL3qmZWHUB4wP8lur4vbiukwYCnNtGzy%2FylrlD6zq0qg6pLXRogBHurDTtpONG0UUMgBk%2BH%2FwG3l%2FNJzhYstln2%2FE9BQslAWDif432FfotaktRgeMO628rwGOqUBw0gh8CQNln52fARLfSNdTeBTYJJ%2F9aa9neQ8f3L82e7rKZ3WV%2BdHdcdnAmNMwAevnUPthO7%2BkRH72TO%2B02R0CT9fLvv69Y8P2rvb5zH7AXq%2FR5Pg1%2FfdojQlKOsNvlUKi5bL2bfCg1BeQzRQ0ch6%2B7sdA0sx2mrhnMUAr9YQGZx531GkK8hYJMXyfIhOd6H7TF8ASfwvJ4M6gPJ6LpxiB2sJjJWa&X-Amz-Signature=5c1a2332c97ff7000e2843b0ab6410b28b9398bad62b4dc87ff28ad40445716b&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Algorithmic Libraries
#### 1. **Scikit-learn**
- **Description:** Contains tools for statistical modeling, including regression, classification, clustering, etc.
- **Built on:** NumPy, SciPy, and Matplotlib.
#### 2. **Statsmodels**
- **Description:** A module for exploring data, estimating statistical models, and performing statistical tests.

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c62885f5-417d-4179-834f-d68f8f2bdf39/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WYA72EFV%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T101508Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDGOcNKImtotMPv9f3mhKvIobdZZzJwzfe5LN8sWJGdgAiEAnt0r2vJ0qM5Nno%2FM4UrFQ3%2B960VbEWZrgAImySwIowkqiAQIu%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDD264IooAr2G17yGySrcA%2BNgvCg4C92UaobR9Pve2Pu6ru2nJd8KnhVEumr9nUjnHXgAyit0vcjjrS9%2FN9aY%2B2wSnaFgpRtgz6UNOdxKeQsIouSU96cF48BdeOYBpVIfInvxLzX7HzMRI6ahsBSMRimVhkBDbpOEeQ6OrLxrc8Ew%2FM4dyZw%2B%2BfbAVcigjHPJcvbzIK84hIgfDNMdC78B0HRuqFIbOkQrqImwdK03RuJ1JhB0nua5H96M74n%2F4XZ%2FwOu31mgqUiB6gc1t7jLNm7JYKePF4WUW5MG0OfhPcNBGvH4I2mIxKH7SUGK7AhYz%2FIq78QEupkkMOoBWWsDhC5XapM7da78uVLZsFJMs4BdIniAwpOa4rBF%2BLPVdkYnV0ZUAEspKLRvZm%2FdRZz3M928HORe1wVJlmVrHle6sM%2Fb4zc7Y%2FgjJNqbwRTJph3cu1gBk9n0nrYWIKi0s%2FbbY3%2BQuzzgkIeric224fo7zhc7W5s5wIdwIHCfiplBNy0Ci53wOtP9jMIHRsYc0YEXjjhqah0nXFk0gDL3qmZWHUB4wP8lur4vbiukwYCnNtGzy%2FylrlD6zq0qg6pLXRogBHurDTtpONG0UUMgBk%2BH%2FwG3l%2FNJzhYstln2%2FE9BQslAWDif432FfotaktRgeMO628rwGOqUBw0gh8CQNln52fARLfSNdTeBTYJJ%2F9aa9neQ8f3L82e7rKZ3WV%2BdHdcdnAmNMwAevnUPthO7%2BkRH72TO%2B02R0CT9fLvv69Y8P2rvb5zH7AXq%2FR5Pg1%2FfdojQlKOsNvlUKi5bL2bfCg1BeQzRQ0ch6%2B7sdA0sx2mrhnMUAr9YQGZx531GkK8hYJMXyfIhOd6H7TF8ASfwvJ4M6gPJ6LpxiB2sJjJWa&X-Amz-Signature=bc97dcf5f4c9d76d72b8a4d11bb6562c1614243917a39900c73691dd6b1250e9&X-Amz-SignedHeaders=host&x-id=GetObject)
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
