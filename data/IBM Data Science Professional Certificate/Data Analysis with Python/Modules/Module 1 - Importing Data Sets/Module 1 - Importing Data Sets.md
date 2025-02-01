

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

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/997ac361-58a8-4f04-bb0f-79fea4baa761/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UC5RDKJF%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T221428Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDOM3hN6md6NRUh0mVK4hL%2FbjAmefCtZdt5Gt2R3HWv%2BAIhALKhaa7MF%2BT2O37wzhndg%2Bn0NELN67fVKD2Y2Acny7NeKogECN%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwDbLznrHCZ1PUJH1kq3AMnjbHVALMRyrd9DfSQhf5ZSjks4I8gN3%2BIlTG6AVbNvlwn%2F92LX1gBP3D3bmm8WR3GpxaohE%2Fxl1Uhlz%2F2GxSo3pz%2BmVn7kUlJkyr1gl0XBPZnzs11VwXFvzU6Tf5RgX8GbsC9dQ1iIEjNkhyvmIwKv%2FzBoJ%2Fc4ZtNrr%2FIPgSwnJ8ABIXxvvii3cV3uBvVeze1tjMvJACyOGCeKA7p34k8mZLluuM5fsrfvkXMBxE31HrqmHiwCAgv5j3gVjeq1Pxj4%2BOPFubDeMOVP2cwJB2vfaKqhfZhMIaxIbpy%2FjlQQGfRZIx7Zw4OKtynegXAkB91wOP48X%2FhFexEZJlBH94F3znJ7eiDm1Umq6bFSKOgCkyXENRO03kbVv4dv2cjQ%2BSxj378Gm28S6e6gIWzkfoM7fK7pJ4nC2xXXZGxk7hcCahvcsMBqsF4QmBwx0vAsoA%2BxhpSrQD2Gt5hghhPDw%2Fn4tHmYpAPSE8s3JXxoQ8r0FPVF%2FClAdwguRS72A%2F369OubTd%2F7zIqOVOO2ydgg4SW%2BsfHBHrzOArhcwp9XdWoO%2FL18ecET%2BqA%2F1uOF3DXq%2FI%2F9Kz1TTSlwOOP6gKYGVhWIhl6eIiv9JVSRMwc7gJIdgT2OD431Es4rPZW6jCfsfq8BjqkAXDohDZrJ08kwPtgLbWiZ6wkqyeVVtTevB%2BrLh79Uu5CHkd5mtSnXCPLTNXFeEPkJfqX86TWVdua%2F32kiRKRi7OtnYccT6vjh9f%2BUSTSpR6NfU8XEpKYaGecHK5FXrD3ttkbVHmRMjC9K2AEg8UZKpGFGtSd0%2B4weeIvlw%2BcgcOYCGiiEbt%2BBgRpiGqjMFxpAVyoP2QWzOgI6Iat%2BQrsFoULqkfk&X-Amz-Signature=61940b4b56d8bf17cc51158d350f5e49fcd0fe7cb0f9af8a1ebb2eb43c4a2ac3&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Data Visualization Libraries
#### 1. **Matplotlib**
- **Description:** The most well-known library for data visualization.
- **Features:** Great for making highly customizable graphs and plots.
#### 2. **Seaborn**
- **Description:** A high-level visualization library based on Matplotlib.
- **Features:** Easy to generate various plots like heat maps, time series, and violin plots.

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/733d1e42-5a53-4fd8-90c1-3d85254369a6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664HPVESK5%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T221427Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDAe8BEOelwIFDKsX%2B3kuA7H1BSOKspzyV1alZtwBzZ5wIhAKBQSjBQT%2B9CsLUvVOo3%2BV%2BYApKeCUdTWV3%2Bic%2FYqIgjKogECN%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igyl%2FYOKyXqh0m2UeY8q3ANRJtFcVk8nzFN72WhRqFkUcghB9BX3PvTk41USUMFutc%2FTvzXVoqc2i8mwbVc8CrqTMFFdCg6eWQDSgwsAfrdrPOe7HjB%2BU9HmJkG3E5QqQz%2FUuQCuK%2B8rW7lI5R5qKt7Iyy0hfQfAjm3tXapUhGjBlJKbHmzIPuhAg8vM07ZItntzKQ1YQiwEqvWDCK2TEsNknrTjl7VTWc0d%2FE9XjkxBsXEKqtHf1J3Z9dWtrLznHNTeWnRvoxzHNrlpOP9R0O0uG2NX5CUHr9hwiNhkPAQqcLuo6UXrnxQBdOnu8AhMRg6wOuMRyRAYYc4mJVWxc1GWDihf4DUrWfKBNC7ABA%2BKOeqpVkduCl7Msto%2B9DksKKmf1KfDKtGd%2FgSp1rKl5mNVapjxa3OtidfYYaVVWNeuyk64rWxCz8ciD2H%2BfzG8XaK5V6Midue8u8szUhRd7SPQq%2BxYKNGVHe6rQP3nStzEcsZ%2Fsqj83GSzU7Ny5Te9UbxhGeUBRiZEfWcS2y0lWyCOS1mTdfc8gNUZfu2rXK7qt%2BHpeJJoBt5C%2FkX5vz2dUJ8RfCaxN36wuDTZ8mrEzGve0uwG%2F%2BLV5VYpnz%2BW8ai7LsEBUvJA6cEksUsn4%2BHsld2qNviRY1jJbR6iUTD5sPq8BjqkAfSBVaYOvD59odOCk%2F7ArRBQx04nxxF%2BhbeOAGD7qPeWVXF97SSUdxkW%2FLpLXvSIRu5dom1VriRijXtnzbDfcRkakTofpfoTp7nPwCe%2B2FMuXDFtRdW5dw7BP4g5szVTZOqrcMogFff2ddE0J5WxcwE%2BtCWgrr9vH%2B5z1VQ0LuYQxr7CTfhMbV1LruCRt4sJ474eL79jKox%2FrFgt1c9mrn2mJrSs&X-Amz-Signature=cca553320fa5a72aa2543bb58ded7af9cd43ff845f614b74db5f0c1f139ef6e1&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Algorithmic Libraries
#### 1. **Scikit-learn**
- **Description:** Contains tools for statistical modeling, including regression, classification, clustering, etc.
- **Built on:** NumPy, SciPy, and Matplotlib.
#### 2. **Statsmodels**
- **Description:** A module for exploring data, estimating statistical models, and performing statistical tests.

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c62885f5-417d-4179-834f-d68f8f2bdf39/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664HPVESK5%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T221427Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDAe8BEOelwIFDKsX%2B3kuA7H1BSOKspzyV1alZtwBzZ5wIhAKBQSjBQT%2B9CsLUvVOo3%2BV%2BYApKeCUdTWV3%2Bic%2FYqIgjKogECN%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igyl%2FYOKyXqh0m2UeY8q3ANRJtFcVk8nzFN72WhRqFkUcghB9BX3PvTk41USUMFutc%2FTvzXVoqc2i8mwbVc8CrqTMFFdCg6eWQDSgwsAfrdrPOe7HjB%2BU9HmJkG3E5QqQz%2FUuQCuK%2B8rW7lI5R5qKt7Iyy0hfQfAjm3tXapUhGjBlJKbHmzIPuhAg8vM07ZItntzKQ1YQiwEqvWDCK2TEsNknrTjl7VTWc0d%2FE9XjkxBsXEKqtHf1J3Z9dWtrLznHNTeWnRvoxzHNrlpOP9R0O0uG2NX5CUHr9hwiNhkPAQqcLuo6UXrnxQBdOnu8AhMRg6wOuMRyRAYYc4mJVWxc1GWDihf4DUrWfKBNC7ABA%2BKOeqpVkduCl7Msto%2B9DksKKmf1KfDKtGd%2FgSp1rKl5mNVapjxa3OtidfYYaVVWNeuyk64rWxCz8ciD2H%2BfzG8XaK5V6Midue8u8szUhRd7SPQq%2BxYKNGVHe6rQP3nStzEcsZ%2Fsqj83GSzU7Ny5Te9UbxhGeUBRiZEfWcS2y0lWyCOS1mTdfc8gNUZfu2rXK7qt%2BHpeJJoBt5C%2FkX5vz2dUJ8RfCaxN36wuDTZ8mrEzGve0uwG%2F%2BLV5VYpnz%2BW8ai7LsEBUvJA6cEksUsn4%2BHsld2qNviRY1jJbR6iUTD5sPq8BjqkAfSBVaYOvD59odOCk%2F7ArRBQx04nxxF%2BhbeOAGD7qPeWVXF97SSUdxkW%2FLpLXvSIRu5dom1VriRijXtnzbDfcRkakTofpfoTp7nPwCe%2B2FMuXDFtRdW5dw7BP4g5szVTZOqrcMogFff2ddE0J5WxcwE%2BtCWgrr9vH%2B5z1VQ0LuYQxr7CTfhMbV1LruCRt4sJ474eL79jKox%2FrFgt1c9mrn2mJrSs&X-Amz-Signature=cec52f5dc5f426f8fece9f3e4f97eb9941c85fc0acb0fb63c9a5583153fb1f28&X-Amz-SignedHeaders=host&x-id=GetObject)
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
