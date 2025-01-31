

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

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/997ac361-58a8-4f04-bb0f-79fea4baa761/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466S7JPIZPS%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T161752Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIG8wnA0qHtmFEzKEDi0LxbR%2FbWBGi07yDBtMk43HCbyMAiBN6aJK4H6QTdob0NUUk2sYFQYPsfyEJ5ZwOf0FSh7c9iqIBAjB%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMV5KVFOOnnFGXcq05KtwDuD%2BL4qKNZxgCk63QV8aohkPhQsRlFSyv01sWO4QPav6j0VpIV5PezWqo0XOk5wcrxG86tzmwyfI7jJYkMfMsGyjZw3dOEwq4g%2Fpk%2BRhXVdnoIB2%2FrfMNIroi403xEJ%2FI4g9x3CZoyFYzWfHexHJj1JkDE99f1v7LgEb%2FCoIHp06xL3fR5iNoVoO3B2gnSO6hpGhpVMKzkZY0P3Ds9u3VEnvcRjMNWxb1wYAcVMVRgYFLcZ58rhJu7lCJHHx7NNeVaXlByOHhLZXLw%2BtZgaKmfYgmZVwpa34L4tcb%2BLgDlM39PSVSKbVTLToaDWWMwLPLj7wWrh6Nm%2F5bFGJUf6Z%2FICXY0qwT5vv35%2Fbxoi%2Fwxn7OOfFbDQbYhac4mv3EJHKA6yMafMv6oB4bJtfTTgeSTf7%2B0Fp7DwRYqsFmWfdjvM39HnyXs%2FnTDAvR8d%2FELrxdLMefPb2ygO5GfzFptlIHOfO04Bfp6jD2N%2F25e9GhMzSpVe4yY9yegg6pvtl7jlBwzKmOezcY1idYzgzX7XYTQp9vT0yPRkOrj0tYASO7Y1A%2FCB%2Fy8y53OLJeSxkeI7EzJmlxicxFVF3nmsuWWkLvJqPAxOVP2Cn8IedC%2BI1YLmnGDlyIZ%2FRl6RlVERswhOvzvAY6pgFr%2B4NIeY%2FfhVla3oypLnob%2FjJ5YAX%2FsVjuSx4IOImaw0232CLZXs0KYyQ3O%2BiwGqZ%2FzVVBA7eGDOFnltGHx9PHrptVSN8FhxYPp9ZBPiH1tMiNhqhVJc9BPPj5QLJw%2BymRKYluP9fXiUFEPZ5JgzEivPOYem3EwDrC0egcXAr5PqsebsZvZSQ1m268RL2NVwN2kU6AzU%2FltwlpqN8Ynf%2FGJAWZ5eGm&X-Amz-Signature=804b803c518b6a670a556bfe2dc05890254528aa17366a24ca4c9fb702e0cf08&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Data Visualization Libraries
#### 1. **Matplotlib**
- **Description:** The most well-known library for data visualization.
- **Features:** Great for making highly customizable graphs and plots.
#### 2. **Seaborn**
- **Description:** A high-level visualization library based on Matplotlib.
- **Features:** Easy to generate various plots like heat maps, time series, and violin plots.

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/733d1e42-5a53-4fd8-90c1-3d85254369a6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VO23BWNL%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T161751Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIC8bUz0%2FlJFSM9VI%2BiTC8HC9J1zFJ%2BBRG33pQ1k9Wae2AiEA%2BZ0%2FnJ%2FVpGPmM0JtjwsGe%2F89rPLytKqdlmkrodPO4z8qiAQIwf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDM4%2BEUobsWyT6waNvCrcAxX9QseGyDS%2BwdYMIIqA5JbJcrpVJGwfeHoMN0AeMOW%2BlUyQ0Qdpue0JtJNYyvZnCvrplPpg907VhpxWOEUDDmjbIvCkRBL9lv2dQsjilScOlbOSDO98fzk2XLA97nlj4RVos5RkOZij0A1s53Rx0Eg5VK88HJAsrdJ96BPBtrnEDHwYPIqLOvz0NDVryfPmlxJcQB%2BEZOn1YB4K3cgdN6BNuI3A9Z8OjAXdeHbAUaOk7Rk0wIC5OUPb3UG%2FDKibUcbxnPDN6USTu9I9867PWHAM9I7rgaDOWXBafUaoSi%2BEhYJsZLHDNB2MdP0bJ3ei17Q3jC1IKl5oFviv8Jv80ZmOdElI4C%2Fvj3EkD%2FL20daJncxZwqunAf7c0TjM5CeOMkC%2FPB6w75jW7kye8Bb8CCSt%2B36YcpHH0sXA%2Beww1ZK%2FFZWnbErZ9UYC2TromuONdeFgUPcsK6U%2FN1GKv0KEXX36v4s4Y4jTe68s2XXRDnlkBg4d9gh3ZLJHLQEYAlRWi9wOCm%2BgfxzfyPMRmRoI%2BjRN7wBNgDDwBLpgMfW8ref%2BNY1L5RI%2FaD9N%2BvV5Ghrz0b19kHQFYjT3Tndo4x8plQefwQ%2BO3xyarewZgZ8RnPryI%2FVqCCLZVeQBx2NMMLfr87wGOqUBI0HdR77WXhx2lBEvyiqWak5Y8heeTZmentE0i5NvwC%2BDQW913e%2FAdJvwE%2Bn8O5au%2BCCod5PYBle%2BUaUz5Lcw0%2FLNpar2kbvvy2FTVJ0geDlPdbGfgjK9Ts6k0NK5DO8HA5PMu5W0kp7UG1fXQgq5xTqYo%2BN6M5JsH%2BhBSc5SFHB2Tp%2BAJphnHVhVDolFMyHZbBqOu6sdg17r2GDyizWOY089ZZbL&X-Amz-Signature=aaa2f99e38f38d9bd7e7c938ace952b8f0d3c87795e23dca71c44dbc6106ef90&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Algorithmic Libraries
#### 1. **Scikit-learn**
- **Description:** Contains tools for statistical modeling, including regression, classification, clustering, etc.
- **Built on:** NumPy, SciPy, and Matplotlib.
#### 2. **Statsmodels**
- **Description:** A module for exploring data, estimating statistical models, and performing statistical tests.

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c62885f5-417d-4179-834f-d68f8f2bdf39/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VO23BWNL%2F20250131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250131T161751Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIC8bUz0%2FlJFSM9VI%2BiTC8HC9J1zFJ%2BBRG33pQ1k9Wae2AiEA%2BZ0%2FnJ%2FVpGPmM0JtjwsGe%2F89rPLytKqdlmkrodPO4z8qiAQIwf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDM4%2BEUobsWyT6waNvCrcAxX9QseGyDS%2BwdYMIIqA5JbJcrpVJGwfeHoMN0AeMOW%2BlUyQ0Qdpue0JtJNYyvZnCvrplPpg907VhpxWOEUDDmjbIvCkRBL9lv2dQsjilScOlbOSDO98fzk2XLA97nlj4RVos5RkOZij0A1s53Rx0Eg5VK88HJAsrdJ96BPBtrnEDHwYPIqLOvz0NDVryfPmlxJcQB%2BEZOn1YB4K3cgdN6BNuI3A9Z8OjAXdeHbAUaOk7Rk0wIC5OUPb3UG%2FDKibUcbxnPDN6USTu9I9867PWHAM9I7rgaDOWXBafUaoSi%2BEhYJsZLHDNB2MdP0bJ3ei17Q3jC1IKl5oFviv8Jv80ZmOdElI4C%2Fvj3EkD%2FL20daJncxZwqunAf7c0TjM5CeOMkC%2FPB6w75jW7kye8Bb8CCSt%2B36YcpHH0sXA%2Beww1ZK%2FFZWnbErZ9UYC2TromuONdeFgUPcsK6U%2FN1GKv0KEXX36v4s4Y4jTe68s2XXRDnlkBg4d9gh3ZLJHLQEYAlRWi9wOCm%2BgfxzfyPMRmRoI%2BjRN7wBNgDDwBLpgMfW8ref%2BNY1L5RI%2FaD9N%2BvV5Ghrz0b19kHQFYjT3Tndo4x8plQefwQ%2BO3xyarewZgZ8RnPryI%2FVqCCLZVeQBx2NMMLfr87wGOqUBI0HdR77WXhx2lBEvyiqWak5Y8heeTZmentE0i5NvwC%2BDQW913e%2FAdJvwE%2Bn8O5au%2BCCod5PYBle%2BUaUz5Lcw0%2FLNpar2kbvvy2FTVJ0geDlPdbGfgjK9Ts6k0NK5DO8HA5PMu5W0kp7UG1fXQgq5xTqYo%2BN6M5JsH%2BhBSc5SFHB2Tp%2BAJphnHVhVDolFMyHZbBqOu6sdg17r2GDyizWOY089ZZbL&X-Amz-Signature=99cd5a84325919a10033eb90dd8113f3c429d96b8cc385c78f9a52dfb9a85496&X-Amz-SignedHeaders=host&x-id=GetObject)
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
