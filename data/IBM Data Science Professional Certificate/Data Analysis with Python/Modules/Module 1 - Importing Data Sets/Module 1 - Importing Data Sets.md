

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

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/997ac361-58a8-4f04-bb0f-79fea4baa761/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466V6MZQI6H%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T182004Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBoaCXVzLXdlc3QtMiJGMEQCIHo98l9xNclb8hCPuE3J8aSpQxUhIm%2FXrMPAlDfk6vQ8AiByoapuLt8qFGnFmBj7zNmU0GVxsvu1LB7a3Juwlms7dSr%2FAwgzEAAaDDYzNzQyMzE4MzgwNSIMXmGlOcVJhvjMRnfNKtwD7Q7qLs%2FNIKMXsW2mcTNiPQQVLeXRqvPLY9AfS5a%2B0AFrz3QSSC%2Fg2c%2FUQXDV%2FoPlH%2BB9SihYWZGb%2BzCuoj6q0DBkl8za%2Bj6tekyyzh3nHg4lo1b5QUZmficLD2WWfzqhdwxGv1hjuXq9ONumi7Ir60syUzTBqKGKwmzaCtgjUNswFBszRzf1nbJQ27zVRKHNDB0Ig49YusKW0GmwFMxe53mL6%2FxY31HIGKNEsrOMHBgqDGY8m%2BNL6q1doSR2dma8ZZi9KVjGSjLmIez7k1TugP6959KdvNIs9CX2KESBKxT5bK2aj3OOpTEqKKCJYfG0EBHIFU4dPRHSbJgzW0ZBvmrbtlc0R3euR3%2FD2VhLsV%2Be2IZUg4OraD4RF7xCevUbYEhZ931jy3QPeO%2BGMa3GvitDlsKzm9O5gxeYjoBTlp42V4ly%2B%2FvhMiP8P7kGyUhPwIRm1pqRngmmqZTKYav3zMpdg8u6OXMbyBp9DsfKomyMIEzZNyMWBnIwqK89WPPzJlOsGLmlf50vJ01zCSPEMod0BN9N6sGihQ2%2FOm3AIJYWEp%2FKAKGtU3IrS1wk%2F%2F8exm8cEEjfD%2FZCn07WokmoU%2BgVDulUz6FXIBKVpxcXjljRnEN%2Boz6KeCj%2BvxIw%2BKCJvQY6pgG9SL6AB1MxqiQ%2Bi0au5qKHkva1A2G%2FjPVTd32JjU02NMR2PZXwdetDW1sbZI5Xiz%2BCQ1UWDR6Ru24eZn2Pq89XNUz2X3jFWSjx6T3EaQJ6obWdRULu4UhIJbR%2BLsCbjxpv1Lu8YtpChMZUfFHFdp%2BKpPoX4T80KneMXeCf7GOaYjz5wy4SIOPtcKr%2B7GIImmur4cy2l4uJZrFmhx8phZXnBUQ7o9c%2B&X-Amz-Signature=e42a267cb3e8153f177c11f8f3f15b417fdadf117c657d04b4468df0e2cc0e1b&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Data Visualization Libraries
#### 1. **Matplotlib**
- **Description:** The most well-known library for data visualization.
- **Features:** Great for making highly customizable graphs and plots.
#### 2. **Seaborn**
- **Description:** A high-level visualization library based on Matplotlib.
- **Features:** Easy to generate various plots like heat maps, time series, and violin plots.

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/733d1e42-5a53-4fd8-90c1-3d85254369a6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XZHD4RXI%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T182002Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBoaCXVzLXdlc3QtMiJGMEQCICzXogZjfXVlxJXJLRVTESioxj%2FORED9U3x8f25ELCP2AiAJef4Tm27Sd54LjsbEYYIB60ukjJ5JfOrE2gqPMmqdRSr%2FAwgzEAAaDDYzNzQyMzE4MzgwNSIMtvXV2ajn6wnKL%2BpjKtwD9dVuGZgCzb6U9WiAlZQ0dXhK%2BbTxnKh6k5ll2M6r%2B556r4EjQT5KGyJ%2BEqUiTktEpeT8%2Foqv3LMhYd%2ByiN6r92XGTd2atFGpRFEOx4%2FZQsKt9%2FFU6bm%2BeuOfqQ2t3zXJg9o3rtsYmEPrzbJgP5Spfswerkrzs2PuIrF3wHUSMirVmTZJw%2FbcCWUhsoyVFXrDmb%2F6NAa9e5oPLmtWwZYZ0B7mrzBrDpBASMCo6RmZVRP60OvEqGaKE0i%2B2%2BhAgtBfNtGApClq%2Fs%2B8pVu3mQEx9OXt1JUTPDkua1LoAYs%2FXp%2BFS22ZsB8p1rNtUbiinUzPKHuWRQJXhuaYWXxfsRKXFUjJVUW5FLTYZgyB77TCe%2FVTY%2F8HpZ%2BYw1QSg6Kwzz%2BbGrEGV532Zi%2BM4DQH9cQtuEiZZUZEF79GYU67TZ349nT3i4pv3N6IYwXSIU%2BI3A6dVseOFgvC5kCZJD7em4VvqVezmt4Zks8qJJHU8xGvN5jWuy8PfQaU%2B4GKKZBQsn8RIC3CNonm%2FPzPjOeD%2FslneKE6igXMhlDvmf%2FuWJOujfSKN9lqezHZ079igCOEgYejvy%2FOjIMSR9J06EuOd02Xt7nTLhFbP4t965jc1CdAVIKx4cEbCS0BjxOk3ywwlqGJvQY6pgH5L3EDndGm%2FjJnoUYH57uK6sUr2IPf6qAQNTPuZyNQd1GChmwRFokuk9G9eX4GeXw0wgO4qxn4dfpY534RVm9UlrwfPlkpDhgUUPkdpoiPmhUyaXU1kawuHj1aAqmUN2Z8Ed7G3%2BhcoBYDU5P2I67KpLtGvdExczQuBaE5DkquksJni9YRADizi6NA14ipgT1v%2FPpPWMFn0%2FIYp2vfzJ3uUFC97XXQ&X-Amz-Signature=204dd30d8bc00921b690d92fe1f3d46e6a6e1f1eca20833a409312b33d71787c&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Algorithmic Libraries
#### 1. **Scikit-learn**
- **Description:** Contains tools for statistical modeling, including regression, classification, clustering, etc.
- **Built on:** NumPy, SciPy, and Matplotlib.
#### 2. **Statsmodels**
- **Description:** A module for exploring data, estimating statistical models, and performing statistical tests.

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c62885f5-417d-4179-834f-d68f8f2bdf39/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XZHD4RXI%2F20250204%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250204T182002Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEBoaCXVzLXdlc3QtMiJGMEQCICzXogZjfXVlxJXJLRVTESioxj%2FORED9U3x8f25ELCP2AiAJef4Tm27Sd54LjsbEYYIB60ukjJ5JfOrE2gqPMmqdRSr%2FAwgzEAAaDDYzNzQyMzE4MzgwNSIMtvXV2ajn6wnKL%2BpjKtwD9dVuGZgCzb6U9WiAlZQ0dXhK%2BbTxnKh6k5ll2M6r%2B556r4EjQT5KGyJ%2BEqUiTktEpeT8%2Foqv3LMhYd%2ByiN6r92XGTd2atFGpRFEOx4%2FZQsKt9%2FFU6bm%2BeuOfqQ2t3zXJg9o3rtsYmEPrzbJgP5Spfswerkrzs2PuIrF3wHUSMirVmTZJw%2FbcCWUhsoyVFXrDmb%2F6NAa9e5oPLmtWwZYZ0B7mrzBrDpBASMCo6RmZVRP60OvEqGaKE0i%2B2%2BhAgtBfNtGApClq%2Fs%2B8pVu3mQEx9OXt1JUTPDkua1LoAYs%2FXp%2BFS22ZsB8p1rNtUbiinUzPKHuWRQJXhuaYWXxfsRKXFUjJVUW5FLTYZgyB77TCe%2FVTY%2F8HpZ%2BYw1QSg6Kwzz%2BbGrEGV532Zi%2BM4DQH9cQtuEiZZUZEF79GYU67TZ349nT3i4pv3N6IYwXSIU%2BI3A6dVseOFgvC5kCZJD7em4VvqVezmt4Zks8qJJHU8xGvN5jWuy8PfQaU%2B4GKKZBQsn8RIC3CNonm%2FPzPjOeD%2FslneKE6igXMhlDvmf%2FuWJOujfSKN9lqezHZ079igCOEgYejvy%2FOjIMSR9J06EuOd02Xt7nTLhFbP4t965jc1CdAVIKx4cEbCS0BjxOk3ywwlqGJvQY6pgH5L3EDndGm%2FjJnoUYH57uK6sUr2IPf6qAQNTPuZyNQd1GChmwRFokuk9G9eX4GeXw0wgO4qxn4dfpY534RVm9UlrwfPlkpDhgUUPkdpoiPmhUyaXU1kawuHj1aAqmUN2Z8Ed7G3%2BhcoBYDU5P2I67KpLtGvdExczQuBaE5DkquksJni9YRADizi6NA14ipgT1v%2FPpPWMFn0%2FIYp2vfzJ3uUFC97XXQ&X-Amz-Signature=c152fadec5afe259020739e1af159a2585cd01af1c856b18ee588a4ab29128ae&X-Amz-SignedHeaders=host&x-id=GetObject)
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
