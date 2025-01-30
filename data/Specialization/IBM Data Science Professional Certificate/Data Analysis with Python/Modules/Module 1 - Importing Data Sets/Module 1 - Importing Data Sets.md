

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

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/997ac361-58a8-4f04-bb0f-79fea4baa761/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665EPULKUM%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T221323Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIHnycpfUVztqImN8tSR6kd%2FqxwNJODD9Xm3YTlwlWFJVAiBoV6UNuDsakHR%2FuvahY0GajvnQFWHOP7Mxkoin6iuznSqIBAiv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM1I8PFnapmXJq4daCKtwDs6%2BExsnn7YJUrALPubQgSAM2VcDC%2F3akB8EgntfInCNh1ehJlYZlgVcj6TPDzOK8ouPCpmdHmWi7Z%2FYRDzSRpssBQqk7nAtHPgdXOWgRzSfeibc0Bo7DSAkjPyONiV%2BwaX1t8qtE1G%2BJIT7sfvTXKZ2LwcB31SFsPL5yq4ftJgbfwtCCwJ2TsMSzLtvzuD8JEvOWAQmvZqud9UT8oUozHWmtCd1%2FWIIJTrLZ1dS5A%2Fi%2F7FqEcUKborGL36VFV%2Fr8tFpViAvddTC2W1Wwc0y6YEacBiHnXDg%2BFsG%2FcxrFN4DnIsCJ%2FAykDABXk9iXoMLa4yyhcCXjpLMW2cSlFm4HDrSjg5F0rGw2JL5zeke%2BiMT4cAtNqtK2rTJNHdaoJyWvB1Bfrib1SzV7X0zR4L%2FrqEabAXnVpR%2B9DTh0q8kWgTOr6xwOGOQllHAKYV36OgZw69LKOk8vgZZw95m9SOpxhCFvVmTHQBi2Nb4D2Lar2RrKIGPrEV3vhsaE2qrgkHTunGqpucn9WWnJz4ie9T7J%2BedagoOpr4Gnp%2FaeVLu3nEHU0HCTqi9nCPn0pJR5GNnCHPW0Ualk4IORqUHjwZ66Na1TJRffigbBXLf0pVmz3HG%2FhnJ%2BdrH%2FRYgDm30w8uDvvAY6pgHgpVv6nuoYGgcaafua3MrS05mHacnvVK9FAEWNi92U9qVHWx%2BjaK7GsIR7%2FirnRkIV2SHKahRyK9ByLhJTMnN3N79o4WwVn1EZzWr4jlrX7LlLdCzUmNw7y0wwIGleQof2aznYn96Q%2FNqAm49nbqZJFK4ZHcOJYMiQhbvJ56KSj30xMoBCG3i0Mvgu0pYisV9gxwtxrtecRC7q6bVileTQ73gj8Cum&X-Amz-Signature=541eff133acafd1a6b65b51910b07046db2102224206f3b34478c5aa1513a7c4&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Data Visualization Libraries
#### 1. **Matplotlib**
- **Description:** The most well-known library for data visualization.
- **Features:** Great for making highly customizable graphs and plots.
#### 2. **Seaborn**
- **Description:** A high-level visualization library based on Matplotlib.
- **Features:** Easy to generate various plots like heat maps, time series, and violin plots.

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/733d1e42-5a53-4fd8-90c1-3d85254369a6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SVSYCI67%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T221322Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIEwdHBWx5PSX0nWCUfGe6koRJjwnpVBJpKwonDrKMAdKAiEA4Yxm9GBEuSoAUv9I6SL9oQ2mRZV6YaC7KRHSTrzr0oAqiAQIr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDEBtiJ0LCq3Z0m5VoCrcA2MbqV6WgDv%2BIGNA3AOCM3Va2IM3k7%2Fbde1bkIJJH4dCfsW5qrfVsy8upAZUUUivemMv2O9M6NdOrYLQ2FXS%2BUQk7k2%2BeYJ1mj840D9I%2Fj%2FABLqFZSuQjhyxBBBBAPMddhRn9vGs1mBWEwlCQmjQ7bRASS1unkXprfYK82z82gKDyaPMbYugkH%2Fr9ytV8x7yR7ItZ%2BR7wcMdkvitnDy7zApQzxQzhhvvL4aYEjviMFe06GNYrpgHF8C5R8fJIPG6hX7%2BfEBc%2B5pweUB35o5l3P44Q%2B3AVBbpXZjSkAyMLfzClxIppqUyLdu%2BRQZXWOcxuw4GK8lVjO6tVw9MBFHg3oIxe5%2FUtxgcL0XCR8fadsxLxf8jXWVO6F53LPX%2FAk4vyj%2Bjmm6DwYRLFZ6u6tUZWylcFGqAuy6enOG76j4GbGCAU7Xyv8TMYDpqzpNz0O0Bd528hzIvNHC%2BZwRtUhtA1%2B9%2BjnrbZ%2BQxViiLQYdClMlkSvwuvtyPwfSfH6nA6jyzWJUKFYsXDaLVK3M1ZvtUP3r56zDcB8phiUPpwuBDB%2FIIijxdLFkoDiH66qhey9KKNhK%2BJyCAPn6U4NI0XhItczEPGgS1VvgJf6DKx%2FAx9NAUMFqNZnMNfW%2B6nWInMNHh77wGOqUBaUY1x7Jal7Hy51BTutpdY8wUmAukLuD145IpAj3Gsone1%2BgNlgE12Skv1C9ZURjaPBCRznCPdalI34EJv7ppZC0r4rqBPJJC%2B0lk0AgKHPMgyk57X%2FYOiUykXBCWRX31bG19Ur%2BjEjmJKt5qPouqLDSABIXCUIGxKvwwSOkDk5HuUAAUTqC6UIuizOWsRbFa%2BR3E7kwwoZT%2BJid3EEkrQtq4mfh%2F&X-Amz-Signature=b99b8c36bcda03418ba8ba5fc966d3412cc58616a29645349c593598084fef3e&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Algorithmic Libraries
#### 1. **Scikit-learn**
- **Description:** Contains tools for statistical modeling, including regression, classification, clustering, etc.
- **Built on:** NumPy, SciPy, and Matplotlib.
#### 2. **Statsmodels**
- **Description:** A module for exploring data, estimating statistical models, and performing statistical tests.

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c62885f5-417d-4179-834f-d68f8f2bdf39/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SVSYCI67%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T221322Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIEwdHBWx5PSX0nWCUfGe6koRJjwnpVBJpKwonDrKMAdKAiEA4Yxm9GBEuSoAUv9I6SL9oQ2mRZV6YaC7KRHSTrzr0oAqiAQIr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDEBtiJ0LCq3Z0m5VoCrcA2MbqV6WgDv%2BIGNA3AOCM3Va2IM3k7%2Fbde1bkIJJH4dCfsW5qrfVsy8upAZUUUivemMv2O9M6NdOrYLQ2FXS%2BUQk7k2%2BeYJ1mj840D9I%2Fj%2FABLqFZSuQjhyxBBBBAPMddhRn9vGs1mBWEwlCQmjQ7bRASS1unkXprfYK82z82gKDyaPMbYugkH%2Fr9ytV8x7yR7ItZ%2BR7wcMdkvitnDy7zApQzxQzhhvvL4aYEjviMFe06GNYrpgHF8C5R8fJIPG6hX7%2BfEBc%2B5pweUB35o5l3P44Q%2B3AVBbpXZjSkAyMLfzClxIppqUyLdu%2BRQZXWOcxuw4GK8lVjO6tVw9MBFHg3oIxe5%2FUtxgcL0XCR8fadsxLxf8jXWVO6F53LPX%2FAk4vyj%2Bjmm6DwYRLFZ6u6tUZWylcFGqAuy6enOG76j4GbGCAU7Xyv8TMYDpqzpNz0O0Bd528hzIvNHC%2BZwRtUhtA1%2B9%2BjnrbZ%2BQxViiLQYdClMlkSvwuvtyPwfSfH6nA6jyzWJUKFYsXDaLVK3M1ZvtUP3r56zDcB8phiUPpwuBDB%2FIIijxdLFkoDiH66qhey9KKNhK%2BJyCAPn6U4NI0XhItczEPGgS1VvgJf6DKx%2FAx9NAUMFqNZnMNfW%2B6nWInMNHh77wGOqUBaUY1x7Jal7Hy51BTutpdY8wUmAukLuD145IpAj3Gsone1%2BgNlgE12Skv1C9ZURjaPBCRznCPdalI34EJv7ppZC0r4rqBPJJC%2B0lk0AgKHPMgyk57X%2FYOiUykXBCWRX31bG19Ur%2BjEjmJKt5qPouqLDSABIXCUIGxKvwwSOkDk5HuUAAUTqC6UIuizOWsRbFa%2BR3E7kwwoZT%2BJid3EEkrQtq4mfh%2F&X-Amz-Signature=cc60da904a72998c41eb643958e45353c665cde52b34c923477ae363153adac9&X-Amz-SignedHeaders=host&x-id=GetObject)
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
