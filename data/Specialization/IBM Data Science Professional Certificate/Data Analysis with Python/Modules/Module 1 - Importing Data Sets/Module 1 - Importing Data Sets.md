

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

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/997ac361-58a8-4f04-bb0f-79fea4baa761/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VUXIPTQK%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T131956Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIEOsQS33KUdeu%2BpZSjTstldptTKb5kD%2BOAoXGUUGEIxNAiEAuvep6SRf9qQM2ruDE2zV2DzhxNc9RIiqGPFqKa6kHbwqiAQIpf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDCmBsYvNFthJ%2FNNZ8SrcA1NCob31WOwks4drGxFNAcOOOQLsJJ0HoMJdVpdATE5g95DttgaVvcw5Uz5U0IBb9XYhT5xNQvPFm26LotVZ4cTmqZiMCDujF417j%2FsSae1UfuapbD1nVjE8hMAXiubEIYLnBklCAa0Ug6AcydhBqCntGskHbfpKvcJIbBpmbbz67hPNUzODgVXwQdLMbu8c54Vn%2FK0WdwqbLTmwJBepK4I6ahYThYIn57OX3CylQdlNkRnkmWfNDRE3bU1fMaZ2KSaDmshCAPAOqMnnPpETMCS2JKAawU7cpccBf4Z%2Fo%2BL07ovhz38ux8hM0di1qGkvt0YbeoksGV%2FkN6Bi%2FwIGTFPz7nSM4c3AvtpL5s268%2FypURklN7S2cBqAjVjtgQhaoW8B6BrwnaSDE%2Fqn32qMKQLHWyqJfoTrS70EwwdXcahVoqT1ilxh38Oe6uLWJcJylH082cUeDHonyJn9QUyAU1Qn%2BGjmWpinv7PDp9M67xTTjGcNqweI5CptBC6fC1Lfd2m0%2Bilt5uLc7r7Otm%2FcjFzdEal4M7Lf0HyhKKIseEPBrG3vAmIrkPDDIaTVqwCYZsI8jlaceo21r0Dibs3hh5h5jwufiuxcttnhDwzXU6dmQCpAiIg3nkFvC9WbMN3e7bwGOqUBoWKxr%2FnrIt0rkW9vJO94zzCVmnOOm4WhXCRo%2FVYn%2Fcq7HL1lLVnX0Qp%2Fvvc%2F3JmW2qig%2BCr94KT1CnZsg1xOdk1qU8ZYrS%2ByBGRJeHcigvGR58mEB5pCcuklUvK8G6feBlqF3hhjsOatPMFeLRiqFs1X8BgTjW7n7CEmbkhzNKRRJUgKrLICk%2FST5kDLYbDJPAHkTNCiIlDAkb%2B6QtOY6cN7BL4l&X-Amz-Signature=bb17887e6ebfa06805131f56ac9b08aefb6efdff80d23e27228f81a2c98688d2&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Data Visualization Libraries
#### 1. **Matplotlib**
- **Description:** The most well-known library for data visualization.
- **Features:** Great for making highly customizable graphs and plots.
#### 2. **Seaborn**
- **Description:** A high-level visualization library based on Matplotlib.
- **Features:** Easy to generate various plots like heat maps, time series, and violin plots.

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/733d1e42-5a53-4fd8-90c1-3d85254369a6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UYYGA3K3%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T131955Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIDlBQPq3e7d1GtRhWwrXGnom%2FSu4McThb87dg%2BseD9aNAiAyR16tAUgUhJmharqWFvHVwpAPl%2F9HZiMDuKMH8QKKeCqIBAim%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMbbRODmWBd2ifKmL8KtwD9CoTDIfb5wVmFARgxKlCh%2BmtRRIYtVkS7fjeh5rAyZeHpWDS%2FwA%2F%2FWfh5hFIV5vWb0RXay7M0wbS0DNq4hExeMb%2FZ0aYXxcZJHP91uZSzqtrhlzcuxMXYhOVU4QgG6rlS%2FfYb7fMyNNFxvv82eZkpPult2vkCNSQUvKjIYUo0yijKwlX4COwjr36e3Fh9kUxcxR7zROahJ02g7AsCXq3vdKVmGKnj7waxMJXbA7gwG23q17CqCTCssAYtXFq0ziTD%2FR87m7UHaXHJ3YasFCvzXJLdhNQrm8YfHuWESRDLBEfsw2122nLjGbyjpD9NucUXudaI%2BzBDGYn%2FOIvCPn8BJLXlX5SeUCLP2DnsenLdNh60TAYghhr97z5MugK%2F9bUyxI6RhqY0CWTrmo2dcUj84Q9cuytpgTH2AWP4cEXm1jLynpg4mEtFzloOK6vQ0Pr6%2BAw9uJo926AgzIJnT0j6PWKtyYA3ElWbTR4WTq1gTeMRH5bLDpU4jXVnK6rGPoiCwetsEKk0J3Ve2qgtvYbJ%2FFFGPELFKHzpEMEbtEBHJUd6Cvml%2FqiuSZQDqfCm8bGjkc6sZPj3SgHEiUr5ln5LfybfrQ0e64h5i%2Be1PxUxx4RwXyFn1O4GSJNWF8w0t7tvAY6pgHND6m6dFstI8%2FfFVCJ3JTylS5esFkrEJdinPimJog8rCy%2BnYikKVam%2FwTLXjbvf7WR6Qx0Q%2Fi7n2p4VaQqpj2UQWVbhG5peRF7U%2BEae13Oj6Bqly7%2BHxFmLex8tcst9QNIwU6r2ZEHeNCBeaSRlfBeChHaUH%2F6C62QvNHBHammHlvO7Hkq0E%2BlIKVTUbAam7KX1lkX2uW7Yc5g089tNzLICwN7zAXg&X-Amz-Signature=8936fa456a9b91b6e5f03e7a9a081d667d97f46f3d83482d3c4a3a03faaaa6f8&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Algorithmic Libraries
#### 1. **Scikit-learn**
- **Description:** Contains tools for statistical modeling, including regression, classification, clustering, etc.
- **Built on:** NumPy, SciPy, and Matplotlib.
#### 2. **Statsmodels**
- **Description:** A module for exploring data, estimating statistical models, and performing statistical tests.

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c62885f5-417d-4179-834f-d68f8f2bdf39/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UYYGA3K3%2F20250130%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250130T131955Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJ3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIDlBQPq3e7d1GtRhWwrXGnom%2FSu4McThb87dg%2BseD9aNAiAyR16tAUgUhJmharqWFvHVwpAPl%2F9HZiMDuKMH8QKKeCqIBAim%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMbbRODmWBd2ifKmL8KtwD9CoTDIfb5wVmFARgxKlCh%2BmtRRIYtVkS7fjeh5rAyZeHpWDS%2FwA%2F%2FWfh5hFIV5vWb0RXay7M0wbS0DNq4hExeMb%2FZ0aYXxcZJHP91uZSzqtrhlzcuxMXYhOVU4QgG6rlS%2FfYb7fMyNNFxvv82eZkpPult2vkCNSQUvKjIYUo0yijKwlX4COwjr36e3Fh9kUxcxR7zROahJ02g7AsCXq3vdKVmGKnj7waxMJXbA7gwG23q17CqCTCssAYtXFq0ziTD%2FR87m7UHaXHJ3YasFCvzXJLdhNQrm8YfHuWESRDLBEfsw2122nLjGbyjpD9NucUXudaI%2BzBDGYn%2FOIvCPn8BJLXlX5SeUCLP2DnsenLdNh60TAYghhr97z5MugK%2F9bUyxI6RhqY0CWTrmo2dcUj84Q9cuytpgTH2AWP4cEXm1jLynpg4mEtFzloOK6vQ0Pr6%2BAw9uJo926AgzIJnT0j6PWKtyYA3ElWbTR4WTq1gTeMRH5bLDpU4jXVnK6rGPoiCwetsEKk0J3Ve2qgtvYbJ%2FFFGPELFKHzpEMEbtEBHJUd6Cvml%2FqiuSZQDqfCm8bGjkc6sZPj3SgHEiUr5ln5LfybfrQ0e64h5i%2Be1PxUxx4RwXyFn1O4GSJNWF8w0t7tvAY6pgHND6m6dFstI8%2FfFVCJ3JTylS5esFkrEJdinPimJog8rCy%2BnYikKVam%2FwTLXjbvf7WR6Qx0Q%2Fi7n2p4VaQqpj2UQWVbhG5peRF7U%2BEae13Oj6Bqly7%2BHxFmLex8tcst9QNIwU6r2ZEHeNCBeaSRlfBeChHaUH%2F6C62QvNHBHammHlvO7Hkq0E%2BlIKVTUbAam7KX1lkX2uW7Yc5g089tNzLICwN7zAXg&X-Amz-Signature=d368ada5b140d50f21d43b25ec52b299c132870b6631badf542eaf8791afe691&X-Amz-SignedHeaders=host&x-id=GetObject)
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
