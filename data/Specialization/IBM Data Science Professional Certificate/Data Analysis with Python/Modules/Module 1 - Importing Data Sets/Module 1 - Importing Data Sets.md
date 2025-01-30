

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

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/997ac361-58a8-4f04-bb0f-79fea4baa761/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662KYWFIFS%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T151514Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDYT55qlPUAMqZPMILrbOA0fxFlUeagkN66fr%2F7vHYlqgIgC%2F%2F2YGGkYwOwRLwkWLDqf1NMbUJ6huoj92VOJwlXoFUqiAQIqP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLNhEwqCLj%2FgkKLWCyrcA6F43cG21lQb5gjZX%2FKQq3pedZK%2Be61GpHHXlOuEiB1mXj6JiNMDtQyTxEhS3xB1DpDIMgBjIlhoMZzXBp3IIgsI7xyvpxs%2BOzD%2Fr9hJXUITJJnLrwmQATJ9bh7hwhWUSMTCtjGXcNWy8SXkQ6HlEji0sqJ9M4TydZYwyZBesunBRnRCYcBFBrBwJeJ%2BCRHXT5Vgq6yRrI%2B0q%2BvZPEVDIZDQ%2BmT4jTu1flteZ0Y7EWsaQAYqNQb5XD%2FlQiW0LkMC%2BvK6RPLlFBR30NLYzK%2BLlrEPl%2BD5NXv9s%2B7tCksycsNMcCghKN%2B3ZXLsNuxXI8hfN6h3cepcWI7LdTMZKhYgnjeqwvtr4BAMLQlirF94zpQblTMsWVXPtytp3EhUpjToSy6EAZuG9BN4oZYRzH0VZqV4CBfrgPfCvBMAgSpNq4FsyyQs0FkMuCi367Ha1bYJsHpeuQVfT3QnxNs5cd71IDxeTLUm%2F4sqjLu5jkJ%2FIZBV2ii5rj%2Fte9txFbvRS2hvzU9mXWipNB%2F5yTntA5LCUwnIPHibzG36RzaRI%2F8lmVdx9na7nUaoHBF%2FXVGlPGDtD4peeohniLoCjftXT6ufKS6ODNFdwyn08lmgc6h1eD3MUSjuz4P89cAbSRgZMIKX7rwGOqUB%2BpVKBLHqpWBDamXd4dbidw%2Bovu4drs4TRcx6ZL44A5VFu8jObS0L2LtGflyHMftTyCvZk3Y67W%2F1AWMs1ghJFlLryGS8%2FganwsYHbFlDseUez5A%2BH%2Bnj4XGDw7IsrAsHn%2FYSGyYH6naH%2BVMeLn2huRE2f1m8vz%2FGq4VeqQAyyiEW%2F%2BWkoJ5kbBy9itFwoOxU00xMAifMBCbU2Ikpkc1NXt2n%2FA9M&X-Amz-Signature=46c56d9c32f1ffc46a05f8e9481fd5f526c93ab2385cac0c023a91f656d83e25&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Data Visualization Libraries
#### 1. **Matplotlib**
- **Description:** The most well-known library for data visualization.
- **Features:** Great for making highly customizable graphs and plots.
#### 2. **Seaborn**
- **Description:** A high-level visualization library based on Matplotlib.
- **Features:** Easy to generate various plots like heat maps, time series, and violin plots.

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/733d1e42-5a53-4fd8-90c1-3d85254369a6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XAJB5D6F%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T151511Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCICL6U%2B33OvbCnEENuWz3YbjRp0d8yPlLrCW7kDbYOi44AiEAv%2FwNHYeotWyrNx0pS1tVhI4LICNCeeMvF%2BBMaKqFMDsqiAQIqP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGz8qof2o5RbglOjDyrcAxMilhx6K89zoSYBqyvJyO7I%2FkE4KiHd38QITF0phn1HJI84KNPAHwcJe1MCwe1Kby4qjyyuzFsuJ%2FRt%2B46uIRuJBZ92Z5VIHtdEwymLsoXwKBt1PfNETKrKWLL4ucSlUuwcLwP%2Fe6ZzIYUYfLukDir4X6h02otxaNUsY827G5xoPQ69Z7YQc7hnlS4AaBcQM%2B37hW6vCz5J2CHy2p6lzB5lMc9jYLK8tCZD%2FWucl1j%2FSRrRMVqkYhRz8y%2BdwGUrEv8Tubkabj8zPjaLO521ULICYEGdOUq4KSaFGIgt%2F4CrKDVKHK1cKqJ2yVggwfcAIztwYD5TXQJc7aANVHj09sF0ws5TRA560lBLK0bAGxJz3UDw5Nst%2Fks0x7n5ls7SrvD1knYIWQo9Wlfq8lBvLArbzCvgIzvwAbgn3u4necCBcZZVHhFTlQHFGDdP0f8HPVtsE9eEfyz81j5%2FwsoNowwNISY07EoPvpBQIGTGCpd3CAy1f2e%2BcANU%2BMJ6%2F%2FM4y6g2luxNApMvl6G6swwdAa5sQYacWKa9nWTsjVK5QXqshqnZiXLFrodNdVCdytaojqMRjriIMgfaK8y1IbjYjPNg3Rw7HWKgEvWzlvisiuno%2Bw3HVCeChCGgxnueMNGX7rwGOqUBIFMCYKMZUtChdQE9WlGMIK0qYKLgldFFvOBXIucX7pvom83d%2BCbWVhTBcCATjJHzLOeyuHl0K6LhXx1jE5mvZJJDLxOdYda4EHhbsVTTlggwNEQZOqkO%2BdLkq6XUHDtXmFRe3Lk3ABB4x26KEYg4grrevYQhcHPCLc2%2Fi0ieM%2BfMIaFjx6UkHvxqRij6xkf8SSC193mmd%2BNkwmET0g4DjxOlCng%2B&X-Amz-Signature=4155d74366d41e1d6b475614395fceeb821bfb0ddb672a77bb4dadd6c30f1b04&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Algorithmic Libraries
#### 1. **Scikit-learn**
- **Description:** Contains tools for statistical modeling, including regression, classification, clustering, etc.
- **Built on:** NumPy, SciPy, and Matplotlib.
#### 2. **Statsmodels**
- **Description:** A module for exploring data, estimating statistical models, and performing statistical tests.

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c62885f5-417d-4179-834f-d68f8f2bdf39/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XAJB5D6F%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T151511Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCICL6U%2B33OvbCnEENuWz3YbjRp0d8yPlLrCW7kDbYOi44AiEAv%2FwNHYeotWyrNx0pS1tVhI4LICNCeeMvF%2BBMaKqFMDsqiAQIqP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGz8qof2o5RbglOjDyrcAxMilhx6K89zoSYBqyvJyO7I%2FkE4KiHd38QITF0phn1HJI84KNPAHwcJe1MCwe1Kby4qjyyuzFsuJ%2FRt%2B46uIRuJBZ92Z5VIHtdEwymLsoXwKBt1PfNETKrKWLL4ucSlUuwcLwP%2Fe6ZzIYUYfLukDir4X6h02otxaNUsY827G5xoPQ69Z7YQc7hnlS4AaBcQM%2B37hW6vCz5J2CHy2p6lzB5lMc9jYLK8tCZD%2FWucl1j%2FSRrRMVqkYhRz8y%2BdwGUrEv8Tubkabj8zPjaLO521ULICYEGdOUq4KSaFGIgt%2F4CrKDVKHK1cKqJ2yVggwfcAIztwYD5TXQJc7aANVHj09sF0ws5TRA560lBLK0bAGxJz3UDw5Nst%2Fks0x7n5ls7SrvD1knYIWQo9Wlfq8lBvLArbzCvgIzvwAbgn3u4necCBcZZVHhFTlQHFGDdP0f8HPVtsE9eEfyz81j5%2FwsoNowwNISY07EoPvpBQIGTGCpd3CAy1f2e%2BcANU%2BMJ6%2F%2FM4y6g2luxNApMvl6G6swwdAa5sQYacWKa9nWTsjVK5QXqshqnZiXLFrodNdVCdytaojqMRjriIMgfaK8y1IbjYjPNg3Rw7HWKgEvWzlvisiuno%2Bw3HVCeChCGgxnueMNGX7rwGOqUBIFMCYKMZUtChdQE9WlGMIK0qYKLgldFFvOBXIucX7pvom83d%2BCbWVhTBcCATjJHzLOeyuHl0K6LhXx1jE5mvZJJDLxOdYda4EHhbsVTTlggwNEQZOqkO%2BdLkq6XUHDtXmFRe3Lk3ABB4x26KEYg4grrevYQhcHPCLc2%2Fi0ieM%2BfMIaFjx6UkHvxqRij6xkf8SSC193mmd%2BNkwmET0g4DjxOlCng%2B&X-Amz-Signature=e875b8f2b0613a148047665a1e10197a8892342ade554539caa18df6b5dbe7eb&X-Amz-SignedHeaders=host&x-id=GetObject)
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
