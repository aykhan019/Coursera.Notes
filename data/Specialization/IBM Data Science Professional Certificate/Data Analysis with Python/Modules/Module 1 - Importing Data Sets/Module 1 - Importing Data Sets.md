

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

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/997ac361-58a8-4f04-bb0f-79fea4baa761/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UGK7GO2L%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T031641Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIED6btYPdYBToZua64%2FSE1h3B24kdrRfgiq1rAYF9DVcAiEA9RD5eNab40GXBT7FIzvPA7lS%2FNxsy7AI4Z7dsr3g0rUqiAQInP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDAh1ZfXVS8ktm8ymdircAx1%2BHah%2BhQQOdLi7h3jA1VmJkOY5jwKMFxk%2Bs2XFr1gBga%2F00Fg6XMxi2qkye5Z%2FFN2y4Ux5IFZdiWDqR2OdyxfsOlSdb3bR3IdhNkfq9NrX%2FzG8U9j1YdTF%2Fs2QfA1wHmd8vB6RujU%2B8cLV8J9FAgj%2Fj25drJAXZcfDKCHwMXGjJPZQ9BU7csaWuatuReT2EFm7WqQa0eKTDpWd%2BcVrUM2%2B4biR1Cca9K1GqVJ1d2WfKZ2gCWXeqsF30wYfKz006%2F2e0omyCP%2FVopkAEIMo%2ByF%2BuRCpoj5wIHWGYNAuzkE2okclvVIS1m6yqW9f4heLB9YgBlOV32aZtJGbrCOFXZQjxOc%2BCA%2Bl2zYFXRqpifGhBJzgqQW1cs8lGSgQQOlS61I%2BJviS4%2B%2BpzEyRBlQ%2B3MfbWzP7ioPILKYQht4QS7YWtGqO1FgufKi8%2BDgZPl%2FVZGJ7q4mWmnYXp45AQ4upvdEStDwWa3I7lYOeY6BIikKMckBI8lSzSna0CFG6i6alLPc3pK5R9OBpE8hlZaE7pCb14fo%2B2sMp6sQxdeXLfOsgCRAiNtfTLlIaTBd%2ByFVFaDVNTmx4ItQZicQiQMAeSdq3NRLYWt9mbW%2Bp0Ie1tgfJj98icYiUUoiljJJjMMfO67wGOqUBkx3y2WAJe3liFpkEFTKAzFI3EM0XS5nmKx71rpmQ86umPjRhg%2FG5HJbwlDDjhbhvE8KILlN8dM2vLk5QWrPmj6EfstJ6fJgS00GuKXZbR6qRD1djXdmsjugAHFLm2Bzitykz6Ggjbcp3fYd5Mdr9k9Bos4n4o3%2Fo7BuHpWRhRj4WOK1wDORVL4ILMlCcwDb52UtYL5bjUk0AUAPzIbxmg9mnbsSF&X-Amz-Signature=7f9d2bf4fabf0a6b4fb7c7eade4053dd418052d424a6b6790268c584ef869904&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Data Visualization Libraries
#### 1. **Matplotlib**
- **Description:** The most well-known library for data visualization.
- **Features:** Great for making highly customizable graphs and plots.
#### 2. **Seaborn**
- **Description:** A high-level visualization library based on Matplotlib.
- **Features:** Easy to generate various plots like heat maps, time series, and violin plots.

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/733d1e42-5a53-4fd8-90c1-3d85254369a6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZG6FUYPI%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T031640Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDdGa9bEE%2FThuYG%2FsbOhpuZ6h1ZIDbLIRZug6DETUduNAIgKJd8A9xapJUm5J9tKoMm5r4e7Ky3Ts1Me8mQ0qNmADEqiAQInP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGgOir0LNadENjFzRCrcA8LIdn6zogIH80zx2NDmTZbCin114iVgnC5GI6kbih9dMNEWuS4zmF1OH6g42F5p9z9cvQ08fZHNIYzvnZxGnbg%2BXqeoSzdmtynjU90V7uYWr2%2Fe4ovuf11v%2FnD6untFA4f7g986Tn7or6sC%2BMxxb2u6ya9d%2FQWFbn96n4uz7F5t3oOUMeefHYJgzAqCqueZLMqxTjPb79qcNEJdphLI%2F6eoxM2HRNj7ZGJ4ohrA0CVGpbJrFkyfV2m3kf2%2FNxOSZuZP2esN49fuodh9OImWrGLDK2oDpaqewnMMj6OFR%2B0vFXi7xpPF9MpONV6Fhw2yNryNzhl9XmlUCrmAICg%2BcVmwYRykkJ321QrcwgxnEXI8SohTmP%2B1U7aROxdkogRqlvkRr0ikZ3X9JWlzzxi5n9b7jzYm2b2uCr7NeyO1cYtfE%2FiNYz26S3kuPhyXFLO76IcjK2P2%2BqrKKZ%2FQXHka8TX6dYYmRauClrym9cHJC23xQz9Tkk5eUKoGE0yOnJPJaTjGNaHlB142Q8exU%2BPNUSB3HLMDY3Mrba%2FkiYqf3p%2BGW0nQAStDLRIrCvfTFFhpriofig76nIDCjt1e2eoAgXlhTi%2BaoWwvLrGVP5w94370kknXecLgVmhe7NDKMLPO67wGOqUB53rEaD1P3JJ4Nel9GFHrOpDshzB7rCZpTb0lerlWc2%2BhMvVuLno10dJkNAwXtHbQj8QlGvbOXJC5xtLUM5YCuGV1OqZQ8ejgJN0u22bGYAXLUoRTQoT2M8FB3OCKeXfboIKjn2C1BtqOrkvssSEXvjbtPQdMFwDAIWHrcMzdOQ96vAnu0zFnyoijtfhTI4q5uzH%2FxT%2FMdmRDyrD0ls2YY%2BCn4eyA&X-Amz-Signature=6db97622e974f5804e76cdba620fd545cf36cbd63d50b551083d6791e0d04c69&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Algorithmic Libraries
#### 1. **Scikit-learn**
- **Description:** Contains tools for statistical modeling, including regression, classification, clustering, etc.
- **Built on:** NumPy, SciPy, and Matplotlib.
#### 2. **Statsmodels**
- **Description:** A module for exploring data, estimating statistical models, and performing statistical tests.

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c62885f5-417d-4179-834f-d68f8f2bdf39/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZG6FUYPI%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T031640Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDdGa9bEE%2FThuYG%2FsbOhpuZ6h1ZIDbLIRZug6DETUduNAIgKJd8A9xapJUm5J9tKoMm5r4e7Ky3Ts1Me8mQ0qNmADEqiAQInP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGgOir0LNadENjFzRCrcA8LIdn6zogIH80zx2NDmTZbCin114iVgnC5GI6kbih9dMNEWuS4zmF1OH6g42F5p9z9cvQ08fZHNIYzvnZxGnbg%2BXqeoSzdmtynjU90V7uYWr2%2Fe4ovuf11v%2FnD6untFA4f7g986Tn7or6sC%2BMxxb2u6ya9d%2FQWFbn96n4uz7F5t3oOUMeefHYJgzAqCqueZLMqxTjPb79qcNEJdphLI%2F6eoxM2HRNj7ZGJ4ohrA0CVGpbJrFkyfV2m3kf2%2FNxOSZuZP2esN49fuodh9OImWrGLDK2oDpaqewnMMj6OFR%2B0vFXi7xpPF9MpONV6Fhw2yNryNzhl9XmlUCrmAICg%2BcVmwYRykkJ321QrcwgxnEXI8SohTmP%2B1U7aROxdkogRqlvkRr0ikZ3X9JWlzzxi5n9b7jzYm2b2uCr7NeyO1cYtfE%2FiNYz26S3kuPhyXFLO76IcjK2P2%2BqrKKZ%2FQXHka8TX6dYYmRauClrym9cHJC23xQz9Tkk5eUKoGE0yOnJPJaTjGNaHlB142Q8exU%2BPNUSB3HLMDY3Mrba%2FkiYqf3p%2BGW0nQAStDLRIrCvfTFFhpriofig76nIDCjt1e2eoAgXlhTi%2BaoWwvLrGVP5w94370kknXecLgVmhe7NDKMLPO67wGOqUB53rEaD1P3JJ4Nel9GFHrOpDshzB7rCZpTb0lerlWc2%2BhMvVuLno10dJkNAwXtHbQj8QlGvbOXJC5xtLUM5YCuGV1OqZQ8ejgJN0u22bGYAXLUoRTQoT2M8FB3OCKeXfboIKjn2C1BtqOrkvssSEXvjbtPQdMFwDAIWHrcMzdOQ96vAnu0zFnyoijtfhTI4q5uzH%2FxT%2FMdmRDyrD0ls2YY%2BCn4eyA&X-Amz-Signature=3ac13bb80aab199b990e1c3de7ffa0d7b9d5bd97753e22e2ba89776f9a81dbab&X-Amz-SignedHeaders=host&x-id=GetObject)
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
