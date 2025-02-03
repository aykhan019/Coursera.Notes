

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

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/997ac361-58a8-4f04-bb0f-79fea4baa761/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZTJJXM7B%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T182004Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAIaCXVzLXdlc3QtMiJHMEUCICB0T4YDHSIWU%2FN0JqbY1vVd6i7iTSuOiG2MTcWoQwqaAiEAjGg2j6ijCJfHDj0TCnhMLIze3RUZ4CVzs%2F3EotRhRiAq%2FwMIGxAAGgw2Mzc0MjMxODM4MDUiDGDZqpkWEJ8zzixETCrcAzI56%2FZbItqRIRHyrKuUaorNP%2FxlH8krOP05qncEWyerPDvtCPJ4ewKy6Csf0rDFwSJVWXk7XTXH0XvZKeE3goMBvZ2n6cywRQAMSM8t%2BmIWpBtvmAMOHvk7Sgl0I1CwAKDbtyKsoKpqkc2Ug0zXdMEcO%2BvarOkc6RQnubkjTYw1TcxzVX54D9nMNvM36mGHQ34aa7bF%2B7Rq4mC4Gts4mWQ8FApZYTKr7nxzIYgPGWLpiGIxFJZWD3MPobj3%2FE7oAPbaK%2BXQsUocgq1ySUfySXK%2FT6gC%2BTyZRwsc%2Fylr5VPr8%2Foob7ZicwG5Pbzpq%2FWVtrvcX38Av%2BP6yzhlJBmN4KEFQ%2F8HKS5My67UXZpuLMfn09bWU8MPKAGb9xjw2aAdPQBMm6nQ%2BTdhAJEbo4CXE36ABNie63%2BL6pVE50dhVSlz57anqoysyAHzdD69rsT0LZIKPiKPiEKS7deumzA%2Bz%2FeHH7DQRfE7%2BMl2m56yfHVKD%2FmPVhwKUB9aaG7v2G7ROuA7gYy1%2B8VSnFFsL7BpPunatkz%2BHZqqV20uL2GPW8gMgKQhSwwbQW2cUNSduaiygHWEmTYTd6tOvg9hyDNbkFh70Ul1toQBF0v2uv4Dpnr5pBLZlN5iTYPE0yelMMyDhL0GOqUBrZaHaeH2wDzYL0Qxlzenq5yB2eUB1Hj4Fpi7vz1CGc3cX1fcV1WDCftPL9J5%2BSnSi8dmzKo9nk16XJzHgTgsPpHrsbW%2BN770qfRQUzhdzuHjLZvCXCsVNJGWJDd5EYAy%2BsaKZMFuWjIvKj%2FP64zEvcd510FNq2Os9%2BD741gaHrwELzIFciD5vsWEvEnz04OQWQygboowBhEe9AUfxXN44d6vDdxY&X-Amz-Signature=7b8dd77fe60ce29d196eea2563a5f60c0a51aa80deee9b45a0ceda96656fc2e5&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Data Visualization Libraries
#### 1. **Matplotlib**
- **Description:** The most well-known library for data visualization.
- **Features:** Great for making highly customizable graphs and plots.
#### 2. **Seaborn**
- **Description:** A high-level visualization library based on Matplotlib.
- **Features:** Easy to generate various plots like heat maps, time series, and violin plots.

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/733d1e42-5a53-4fd8-90c1-3d85254369a6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46654HXHOTZ%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T182003Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAIaCXVzLXdlc3QtMiJIMEYCIQDmBkdD0kHtL36HmP60MXKJDf8QULlPPEzQghINlssPswIhALyc8jfsCP9IyM8IUY7N0GenW%2FtcQ7Z56EV3hhyFMxglKv8DCBsQABoMNjM3NDIzMTgzODA1IgxGjmTY2ZuDDjedhvwq3ANJ6fX%2FIKgeUQdxGoeubTrLFAxgfVzOqelLQzVgWzUvdpkULPLdgud2b32dIJnCK%2FyDmICpgrZocLW1L9vHj2xfAgZNo4wQ%2FsnFJP4lyLCH94cFrjcYM5tylauEdRCJXM1cqFtE0%2FDoZTdh9MvW%2BxW9SoMRyz61CSzEF5Lk7oYaxQk%2FgvWEiQ%2FgNFVmiyHdhXp4v%2BBxyjwfxW7vYw3giZAzTf%2ByJ%2FfQb244qgZAcegeTrA%2FYCUfP2Udmbxv1wsAZoeb7rVpf4rTf9CEvdzBI%2FXmBWBygu5XARwHX9yI%2B9FbPWBVkt38k1o2hQe2OfaOVcIBOI8EE7hvrnKa%2BFgD7jmOgrwg3ZZQUNbBFpNluSnec5aqCQCbfgPX2o8LNjevCucDpyQYHJBtT3eWbpZGtsLyn5iC8sGxlKL%2FxwActf%2FIwYJxybbO1W1IUWL%2FZF4u0U1oegMzDHEr2zlimvH60llPlIiy2RJgPUcDhj08azyL1DVUz0hb2GAeELCjssF8pAzKV4And%2FXkUSAuvihj%2Be%2B6j83dPXhHsrV8AQOT47hMYXh6u4OALJMs9k2yuaM8568wW0Z4xlSgWszSRdDr0jyK%2BCIPr1YPE8CrkS83GhrsPDCgATBlUOzt%2BlUdnTD2g4S9BjqkAW4v%2B%2B7cSgRL4NGTygZZBW552AjT3NNw1aJ%2FCBrfypGCKXjE3yloEdG6Wz%2B%2FqDzO0%2BghP5EAfnWdSqFAg10tgGY6mE0ECSyPbq8GBEYzi%2FLAHZZZsuvu8tunRMgkWa9Ymt66YsDSiWxFY6rahTIBYuvS0NfGUNOtUG6hrh4nmzfnY3CYeRrT1Sdyb7QUYM7Pg5fWifF9ETuRK8aw2F8r3WUBP64z&X-Amz-Signature=205c3f80d86fe41348383edb9506b57bd3184b900683968e897503744d95d128&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Algorithmic Libraries
#### 1. **Scikit-learn**
- **Description:** Contains tools for statistical modeling, including regression, classification, clustering, etc.
- **Built on:** NumPy, SciPy, and Matplotlib.
#### 2. **Statsmodels**
- **Description:** A module for exploring data, estimating statistical models, and performing statistical tests.

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c62885f5-417d-4179-834f-d68f8f2bdf39/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46654HXHOTZ%2F20250203%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250203T182003Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAIaCXVzLXdlc3QtMiJIMEYCIQDmBkdD0kHtL36HmP60MXKJDf8QULlPPEzQghINlssPswIhALyc8jfsCP9IyM8IUY7N0GenW%2FtcQ7Z56EV3hhyFMxglKv8DCBsQABoMNjM3NDIzMTgzODA1IgxGjmTY2ZuDDjedhvwq3ANJ6fX%2FIKgeUQdxGoeubTrLFAxgfVzOqelLQzVgWzUvdpkULPLdgud2b32dIJnCK%2FyDmICpgrZocLW1L9vHj2xfAgZNo4wQ%2FsnFJP4lyLCH94cFrjcYM5tylauEdRCJXM1cqFtE0%2FDoZTdh9MvW%2BxW9SoMRyz61CSzEF5Lk7oYaxQk%2FgvWEiQ%2FgNFVmiyHdhXp4v%2BBxyjwfxW7vYw3giZAzTf%2ByJ%2FfQb244qgZAcegeTrA%2FYCUfP2Udmbxv1wsAZoeb7rVpf4rTf9CEvdzBI%2FXmBWBygu5XARwHX9yI%2B9FbPWBVkt38k1o2hQe2OfaOVcIBOI8EE7hvrnKa%2BFgD7jmOgrwg3ZZQUNbBFpNluSnec5aqCQCbfgPX2o8LNjevCucDpyQYHJBtT3eWbpZGtsLyn5iC8sGxlKL%2FxwActf%2FIwYJxybbO1W1IUWL%2FZF4u0U1oegMzDHEr2zlimvH60llPlIiy2RJgPUcDhj08azyL1DVUz0hb2GAeELCjssF8pAzKV4And%2FXkUSAuvihj%2Be%2B6j83dPXhHsrV8AQOT47hMYXh6u4OALJMs9k2yuaM8568wW0Z4xlSgWszSRdDr0jyK%2BCIPr1YPE8CrkS83GhrsPDCgATBlUOzt%2BlUdnTD2g4S9BjqkAW4v%2B%2B7cSgRL4NGTygZZBW552AjT3NNw1aJ%2FCBrfypGCKXjE3yloEdG6Wz%2B%2FqDzO0%2BghP5EAfnWdSqFAg10tgGY6mE0ECSyPbq8GBEYzi%2FLAHZZZsuvu8tunRMgkWa9Ymt66YsDSiWxFY6rahTIBYuvS0NfGUNOtUG6hrh4nmzfnY3CYeRrT1Sdyb7QUYM7Pg5fWifF9ETuRK8aw2F8r3WUBP64z&X-Amz-Signature=6793d605d199b35b10a308349aebf14e9c9166e4a93612785a6b9d996bc861ef&X-Amz-SignedHeaders=host&x-id=GetObject)
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
