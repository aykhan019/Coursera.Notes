

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

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/997ac361-58a8-4f04-bb0f-79fea4baa761/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667IJWGATU%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T111223Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEEaCXVzLXdlc3QtMiJHMEUCIGwOY09cIEo3%2FvoPetAY2tJcS1JVe9BFqT%2FnKXkOlto7AiEA%2FRIi2jRATFN9JAYlIAQl1fgkiwKxK4fs7EXdYAt%2F6zcq%2FwMIWhAAGgw2Mzc0MjMxODM4MDUiDDVRs18I%2F7Q0FOx1yircA0chC66cxe76jkYGOF8sHv%2BjShs687fJyVNOFb1lZLbn1O8Raq2vYVLE72QcepaRVaf%2BsTZuDlBuf2BnMAf%2BwTl1ZfZsWKGQ%2BznVAUxOQLUtmHiRQ%2FEjxMTA14wyjqPeAjbrY9pEITIy5wQ0%2Bg9o0rI8g1b4hC0QuqUKyRVSfSZB2Mmv945ObOMwLZ0QRJFYuyEGg61%2Bmif7TT4Z4IeAQi3NPNOaZAhgVwdiG%2FRNf9tQnbPVWPK7RUDUXbz4Hm3VEfSnpoHuEhK2fk2BPwVKe2bYY0FzWT%2BBv0bkrWDnxJNBTqhSBPrz3yNbvExlc2HxEGLVo%2B0Y3Jo5uPAfxiv4CtDF%2BTloLz1ylcnvJ%2F%2FYty7sqbqaJ7fF7uAhD8Eby5otvkZG9qnWrl%2B1uwcomWoMo2%2BNb9pg1ex9QTWNBeAjukNpx6MpzrSumPze9er%2Fiw6lAktOFcsj%2BY3sRShl1s%2FwV8cfT%2FOmv4P%2FC6BA8S4MUgJoHdk2pILxv6OquioVLGAVvLPanrJTmhy3HqP6FVrbVCVg0Cr7jR8%2F%2B8kfO7bMBrIoJqhkYXwyu9F0YhZZ9m04SM8GwArYSKXKl3jaZqbsw9lILVPIzA%2FlCBbZWQKSJMncTca1kKwx84FdgKUvMLPskb0GOqUBCnNGG4NR%2Bobk2xNBaDF3a6tUvtYfQpfnMDzKtl2R1u0pDLiahdnrAWF94v0kgVfYRPF9rxsOi%2Bee8lhj30Py6qUrNcJIPO3ACK5QV2vvnrwSfpv7y7L%2B%2FZIzONhMONAOJ4RMW73ArDMrMeBpKcn8odF7lHRVPuBaE2k0njW0ASbzakXEFAqx4caIyVQfifogqqcTGem%2BoBVxFrlEERkEXH4WGUvB&X-Amz-Signature=1781d65f6b6ba3070a14d07df0a7ebdbc9a1fe9b46af23b40f076236f9c7e563&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Data Visualization Libraries
#### 1. **Matplotlib**
- **Description:** The most well-known library for data visualization.
- **Features:** Great for making highly customizable graphs and plots.
#### 2. **Seaborn**
- **Description:** A high-level visualization library based on Matplotlib.
- **Features:** Easy to generate various plots like heat maps, time series, and violin plots.

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/733d1e42-5a53-4fd8-90c1-3d85254369a6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663WUWRUIZ%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T111222Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEEaCXVzLXdlc3QtMiJIMEYCIQCpwuzf1SL2VqfXlHuV1OHdgcyBYdgZ%2F6VlQLhco7A7SQIhAMBrXc8RgcMFz7AhWoUbiFIdTCxE0cEOURTXVwvkqTF0Kv8DCFoQABoMNjM3NDIzMTgzODA1IgwJ8rgtlfrL0zRve9Mq3AMpaPpZiCh0RlxHrgNnevmd1zgfBZZn9%2FXsSXwWNYnp0Jn76TvMAWBl%2BoCAZxQt7NMpNaWXzBZYIrZKFD0ImwuSQyG7l5RcvJtTRzadtX7vkEDLuxZ2hokttYgvU%2Bv1cqGbI%2FAPm%2FMmvwjp2mB04%2BLJESc04zQpudD8xkXHEHu7%2BLDa3YgvMtWL0KG7nbjzKfGPCLSKyXtNdH5roNIHHx8krKnU9i5TtcfE2felY%2FC%2FHLRK3SlcNWhRIzTD%2BT7etU0AlKbQih0dDJKx7nSUwPbXBmhTuXkoQ683NqVxCiUF3xgULVlzrVN%2BRl5TcnAER60g9iqv4OncLePPaIFihSoOaChYogh8WrgqnH%2BSAGJ69WJ7YfTBNc971aSd0cEcGwkaByJNK89SzzXWw1Md4SniAkdhT%2Fnv1p2PWuO9QndLlincANOjfyml8VU8Ae0fPOaFRl8Od3LkDE1ASmKw%2BjH1Ldw1hTR4YgM5SJkT7gtTdGKUiC%2Fvzek%2FG9tZi5V4zdu%2B%2F7srZagdif40X7vFZeB%2FQ6fU9fqAxaV84rCcopxggVMC74dkzIPDa1B9Mpm4N3fQSjxiED3%2BAEfQ4yGbaN4voVQroFpL%2FIfjCZoxlom7gxunp%2BkCFu9XzBKgATDW65G9BjqkAbyNrLz3MYPqHkempK2xTJ95WLrh8DbYOlhg3%2BmVD5f2OyLeHaYoaaknxWlUg2ys%2FyqXLRFXdaf92GSipnKNTzI3G3ezsXxgP4xa5m096zZWe8pG7fc1MqigVY1ujybj2Gpp1LMlPkG4YA7gSwFtIV6aX2GR8DuJ5ceXwDMd4WLgZ5fuJkS1MJV9RVOkrRXnFKdq3TAIoszlFSXzVckv8nJ%2BHBFe&X-Amz-Signature=a67fbca6b2325e6f1cd71fb01d2b5b70036cfd19d3ddaad227476f06ad2acf99&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Algorithmic Libraries
#### 1. **Scikit-learn**
- **Description:** Contains tools for statistical modeling, including regression, classification, clustering, etc.
- **Built on:** NumPy, SciPy, and Matplotlib.
#### 2. **Statsmodels**
- **Description:** A module for exploring data, estimating statistical models, and performing statistical tests.

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c62885f5-417d-4179-834f-d68f8f2bdf39/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663WUWRUIZ%2F20250206%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250206T111222Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEEaCXVzLXdlc3QtMiJIMEYCIQCpwuzf1SL2VqfXlHuV1OHdgcyBYdgZ%2F6VlQLhco7A7SQIhAMBrXc8RgcMFz7AhWoUbiFIdTCxE0cEOURTXVwvkqTF0Kv8DCFoQABoMNjM3NDIzMTgzODA1IgwJ8rgtlfrL0zRve9Mq3AMpaPpZiCh0RlxHrgNnevmd1zgfBZZn9%2FXsSXwWNYnp0Jn76TvMAWBl%2BoCAZxQt7NMpNaWXzBZYIrZKFD0ImwuSQyG7l5RcvJtTRzadtX7vkEDLuxZ2hokttYgvU%2Bv1cqGbI%2FAPm%2FMmvwjp2mB04%2BLJESc04zQpudD8xkXHEHu7%2BLDa3YgvMtWL0KG7nbjzKfGPCLSKyXtNdH5roNIHHx8krKnU9i5TtcfE2felY%2FC%2FHLRK3SlcNWhRIzTD%2BT7etU0AlKbQih0dDJKx7nSUwPbXBmhTuXkoQ683NqVxCiUF3xgULVlzrVN%2BRl5TcnAER60g9iqv4OncLePPaIFihSoOaChYogh8WrgqnH%2BSAGJ69WJ7YfTBNc971aSd0cEcGwkaByJNK89SzzXWw1Md4SniAkdhT%2Fnv1p2PWuO9QndLlincANOjfyml8VU8Ae0fPOaFRl8Od3LkDE1ASmKw%2BjH1Ldw1hTR4YgM5SJkT7gtTdGKUiC%2Fvzek%2FG9tZi5V4zdu%2B%2F7srZagdif40X7vFZeB%2FQ6fU9fqAxaV84rCcopxggVMC74dkzIPDa1B9Mpm4N3fQSjxiED3%2BAEfQ4yGbaN4voVQroFpL%2FIfjCZoxlom7gxunp%2BkCFu9XzBKgATDW65G9BjqkAbyNrLz3MYPqHkempK2xTJ95WLrh8DbYOlhg3%2BmVD5f2OyLeHaYoaaknxWlUg2ys%2FyqXLRFXdaf92GSipnKNTzI3G3ezsXxgP4xa5m096zZWe8pG7fc1MqigVY1ujybj2Gpp1LMlPkG4YA7gSwFtIV6aX2GR8DuJ5ceXwDMd4WLgZ5fuJkS1MJV9RVOkrRXnFKdq3TAIoszlFSXzVckv8nJ%2BHBFe&X-Amz-Signature=2a5582268a8a5ba30a991341fab480e59cb62f44292071620746eac75055db07&X-Amz-SignedHeaders=host&x-id=GetObject)
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
