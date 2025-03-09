

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

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/997ac361-58a8-4f04-bb0f-79fea4baa761/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RF7SJEFU%2F20250309%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250309T003535Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECAaCXVzLXdlc3QtMiJHMEUCIQCKtjMDu2AAtph7o%2FQ%2Bl5BvcVIcOhACEBKWl3NsRuoL9QIgIrKEm0%2BwlRFpWAvpwf2Yr37oo7C2Cqu7yyY3%2F1rnio8q%2FwMIaRAAGgw2Mzc0MjMxODM4MDUiDK%2FDz66%2FRuvE6XcxsSrcA4truXSGO2RG8EY%2FeZqroWr4hueOKBchSmnxhMtszPTX8yULxr7E%2BOWCKz697NA2xhimC%2FnOMSE3nZwrRmU3PTcf%2BDJQRtQRBvbg6B6b9p6l45d2UAoG4C1nfXtQl290qWOmQaHoIv4Pp97kJH%2ByM2rDDDQn5MnWTEjSBJF2sapkvMQ0kv6OIRfOlJRyWZYbavNadZR9GR68reFaaloIbUYiJJ8NNWuf5w6nHSQK61o5yPxrD2755jMZtcVuB6VUiBet%2BVp%2FiH50EyHXuMLeyt4aGnG0jkOyOem%2F%2BzwEGENq%2Bvd7imYaBx0BjmTxXF3XtJu3Wv%2F%2FBEBFdekEAcBkH9hpvEpJtGZ1lqGTN9nQiCOh4KGdYOji8hjCHKXcRe2rZojYodKOE5dZJe6EPEdx7J9JfAL1FoYslWcMC%2BLkpgzD0qp8dXbtShgF5ACB6dsuTdBzJ%2B2P0GyJkCRKdphxtKPJrUoEU7sOryRtHJlJF9VRZkhbqTgzugq1vyb%2FYbjKilO6cp%2Fq3FrFZnzYpaWgDgk47OmFUcsMcs0Llgrqe8S2Yq7%2BUoLCepE7XH7fkJERAc%2F8hyuCKuR%2F51OYyBqYUzOaHN0Rl0y4rRFDdsSGJIrKw0RQrpGKb9Ubw8aGMOGps74GOqUBSh9RlIITARLM3CQCHEH47D4PqPuMb1Z6CNEkfZ0c1HkSTTHrq2S83txvhSNaLkp3Kjukudh7wwt6TtZTBE1r4S8txB6VUkOeYl1nGztyBIMDoX%2FlW6gDKbOgq714BTowHA8dhZXc4466vq6EZURtO6aUXzLwGGg0BHZELYz%2BhTTny76z6vPYmaNTXrnwMOSUBLSep2WbW7JH00GUzBTy4G4Iaf93&X-Amz-Signature=c8e582e4f83ba7e8e69e5a2df06b7514c639760d799f3e93636f8f1f726b0d7b&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Data Visualization Libraries
#### 1. **Matplotlib**
- **Description:** The most well-known library for data visualization.
- **Features:** Great for making highly customizable graphs and plots.
#### 2. **Seaborn**
- **Description:** A high-level visualization library based on Matplotlib.
- **Features:** Easy to generate various plots like heat maps, time series, and violin plots.

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/733d1e42-5a53-4fd8-90c1-3d85254369a6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46624GT7WH5%2F20250309%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250309T003532Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECAaCXVzLXdlc3QtMiJHMEUCIQCzTMOUCdfdmkFYzyDz014lnCwi7DNbkBViD%2BByW5079QIgVg1cZcSvwsQf0M7gE4AnLKqWKkJJenSnxpkDJz9Gcboq%2FwMIaRAAGgw2Mzc0MjMxODM4MDUiDKAZFiZTFrsGVNT8ECrcA%2FZsbPNduma1x5G3hBv2a92Dvg2JdeObunNt3hIKa3kebArGk4XKEjxT714vllQLzaCw%2BXVh%2B2YPqNFqDPo9DzaK6bjVYgfpF8qpce0i%2FEYCNNAuxr%2BqdH80TJ6ZasjCVFezqTNNlbZPsQEA8Ftp1rCzAa1WfJaLGDMXOmlZE%2BBsHAAh0OJCOzDyQ%2FwRhCIlUy09zedl36ntCDw%2BTN1jEbee4Hbi%2FgxJ%2B5%2F8Z7W5eXiyPt93aPTP6sfdciJGwXv6RWa7s8NzzkcO%2Bqkwl8QhwhjcMAk7UFTF0e8CvbLIy7TYzWA1fRz0BW2Mlp6DWEbonOxYeVQKs%2FLK0M5t%2FGcfiaNPAq6kSiZ%2Bz%2Bpss6kfiBnnJkBvQVBa3pVajJIMCNr8IQV5H4cvcp%2Bg00Xijkdhu7ho4GmbZ2H98iW3guJ2a0OHJ3j9Wl89EjrrJx%2FJK0KCG%2BKPGHsdlr2sqt92In%2BUqJjxrlhEcSovdUlSiMGlt0MgC3WBntRPIfnzvpmBT7RZdpQgkaOyFFh23eWRnrVRmGuzQskDLksXsfMHW%2BFASsM4tR%2Fdn7sRw59r%2FyIVncT%2BCFgRTf295iPR1eAp7U3Oy7gAjZDHyKbY1XcSpcZ%2F7mYUzAikglTuKK%2FiK5uIMLmps74GOqUB2bDPmPG2tUdTmnMSNVPcEbKw5Lt5ulM716F%2BFPGGarNK77%2Fzr5LMnxAjawHHzaWKET4YLNK3OZVo%2BpOON%2B9ahrN3XuBJdyx8O8OfZTw114qzGa3A5v5P%2Bu9yLVrMXZOsOgbQ5PUXrgG2BMfFmwL%2BPwF4oXHavLDMckpBlX6carSMarSPCzd1WC0thgghUn2scrmsroLwNzjZrOU4Kwe%2BtJvq2Xvr&X-Amz-Signature=66be680e20c49c51053e268cfb23054fbb19d135c21d32eecd0d9b94bbd0649e&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Algorithmic Libraries
#### 1. **Scikit-learn**
- **Description:** Contains tools for statistical modeling, including regression, classification, clustering, etc.
- **Built on:** NumPy, SciPy, and Matplotlib.
#### 2. **Statsmodels**
- **Description:** A module for exploring data, estimating statistical models, and performing statistical tests.

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c62885f5-417d-4179-834f-d68f8f2bdf39/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46624GT7WH5%2F20250309%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250309T003532Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECAaCXVzLXdlc3QtMiJHMEUCIQCzTMOUCdfdmkFYzyDz014lnCwi7DNbkBViD%2BByW5079QIgVg1cZcSvwsQf0M7gE4AnLKqWKkJJenSnxpkDJz9Gcboq%2FwMIaRAAGgw2Mzc0MjMxODM4MDUiDKAZFiZTFrsGVNT8ECrcA%2FZsbPNduma1x5G3hBv2a92Dvg2JdeObunNt3hIKa3kebArGk4XKEjxT714vllQLzaCw%2BXVh%2B2YPqNFqDPo9DzaK6bjVYgfpF8qpce0i%2FEYCNNAuxr%2BqdH80TJ6ZasjCVFezqTNNlbZPsQEA8Ftp1rCzAa1WfJaLGDMXOmlZE%2BBsHAAh0OJCOzDyQ%2FwRhCIlUy09zedl36ntCDw%2BTN1jEbee4Hbi%2FgxJ%2B5%2F8Z7W5eXiyPt93aPTP6sfdciJGwXv6RWa7s8NzzkcO%2Bqkwl8QhwhjcMAk7UFTF0e8CvbLIy7TYzWA1fRz0BW2Mlp6DWEbonOxYeVQKs%2FLK0M5t%2FGcfiaNPAq6kSiZ%2Bz%2Bpss6kfiBnnJkBvQVBa3pVajJIMCNr8IQV5H4cvcp%2Bg00Xijkdhu7ho4GmbZ2H98iW3guJ2a0OHJ3j9Wl89EjrrJx%2FJK0KCG%2BKPGHsdlr2sqt92In%2BUqJjxrlhEcSovdUlSiMGlt0MgC3WBntRPIfnzvpmBT7RZdpQgkaOyFFh23eWRnrVRmGuzQskDLksXsfMHW%2BFASsM4tR%2Fdn7sRw59r%2FyIVncT%2BCFgRTf295iPR1eAp7U3Oy7gAjZDHyKbY1XcSpcZ%2F7mYUzAikglTuKK%2FiK5uIMLmps74GOqUB2bDPmPG2tUdTmnMSNVPcEbKw5Lt5ulM716F%2BFPGGarNK77%2Fzr5LMnxAjawHHzaWKET4YLNK3OZVo%2BpOON%2B9ahrN3XuBJdyx8O8OfZTw114qzGa3A5v5P%2Bu9yLVrMXZOsOgbQ5PUXrgG2BMfFmwL%2BPwF4oXHavLDMckpBlX6carSMarSPCzd1WC0thgghUn2scrmsroLwNzjZrOU4Kwe%2BtJvq2Xvr&X-Amz-Signature=50334cdec1c839510abc65a6122fbb7155671e6c5c5cc831efb7532b8a4bca8f&X-Amz-SignedHeaders=host&x-id=GetObject)
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
