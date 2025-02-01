

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

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/997ac361-58a8-4f04-bb0f-79fea4baa761/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VLJGONU2%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T071319Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC71bHSsptQempUJ7GL9Zh%2FOSD9EUke%2Fk4Zz%2FuDBEwtqQIhAKLMcYep3iOhcn4qikjdcsqLm4ycyXnSbvn06O13ddHuKogECM%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzdSk5zKx7hyZKeLX0q3ANw%2BYy8mdvS73lLqF8KP5iQoKLHjx86MENB68BoFaF3W%2Fg1LxoxEQ1p9mygfZpg1e1S2pZk7Qh6SqH0Ll6badFwzrAcZ2b5s%2FP88YDheYJ9ZVdXtCowjWKX3g6nrwVE4u5hnVIXTjVhVBJakWY0p2t1iZ40lQEam1ZTUWjoe3CuG0ufATJ5n7hc%2B6Co%2BsGFHE2Ch3bU4AHyIC4tXdvEjin76w8kwJVrTOSfCFOIJJgqq%2FSgy6X3D8JRH63jvd%2BMNCxvoJn1CAU4uFJIlZH8Zz1RGsNZe3FDB2Qd501xJVIoRKe1gxPiskkvSY0eEvpe7dGQFB49s6gTo3FvmaSx8%2Bh5AX2%2FvpXYzgT309jw1vMH8JOdb0treIRKXmYb5UxowTzcxYufOKrJFAXztf%2BpXEj%2FNBHyHMchvgOtQOk9drkqVS%2BsK9NfNZuEnS12vFu%2F0q0ze%2B5HCdY3WsibKxfuAYY8Ne0u2ph1fw0JfOLJAmRqoaeYWAqxKdkfN8%2BQDiz%2FyFZ8aGmr2qxZqWHLeC1MIzu6PUHMUBXygq9%2BKFoLP%2Fz8HGZMOFb%2FXXp48Fcu4K48OsFfQpZ9rPH3oIa7qWIMkJmJbEvt6E0mma%2BGUynB%2F%2BIgdnNwGDjVKlmXjz5XhjDS%2Bfa8BjqkAY%2FLQ4t2C87u18tdR2UKwhV30C76uXV75tN05jBqBhIwaMkEp6enC6VWxGkkOh0Un7LS5L0OBNxxBW6CiGzd1vcuupQj0eyGTKWtR8JwIMDMal0mZllo13%2B1C%2B9z%2BiZSJaUiqbvQKmqUldtl0lV1v3BeUTW3ylSut3Q%2FkTl7yCNLfu%2FYBlzIa0TWEvg6USZYdFuKS6d7rfspbyog8WMhZYw2srqI&X-Amz-Signature=9c2f1cab582fa83b252354fced31240f2b16066d1f949d73e209003cf2bee830&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Data Visualization Libraries
#### 1. **Matplotlib**
- **Description:** The most well-known library for data visualization.
- **Features:** Great for making highly customizable graphs and plots.
#### 2. **Seaborn**
- **Description:** A high-level visualization library based on Matplotlib.
- **Features:** Easy to generate various plots like heat maps, time series, and violin plots.

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/733d1e42-5a53-4fd8-90c1-3d85254369a6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664VGV5CUZ%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T071318Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHT%2FRT6A38zRU15HYEN4mzWZcW0HJMSYHT0SCqGMr4B4AiEAr3sl0eGZ4aco%2BH5%2BH82uEFbu4bTHlCbYd5rge7azTugqiAQIz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDBmDHsmHJuqMoq8TzyrcA4K7W7o69vto6D2wm9kmpFW9b7IwEhus%2BCphENX%2FC6dfvRf4jIllg2pYCEpneQHr1hhLjZqZ%2F8inknk2Ye3E9b63lzukrarivBhNqDqrLGfNpspAj4XBNYnDoK%2FJ7EF%2BKqLpyuPmDui6AmtyN4w1t7S1uGBUZ6EcmQo9EuiO2J79XEZ9TwzMzz98DaYzPTDXNL%2BwDGq%2BVIRsvj1CxiANKAjBTn5zUzH2m9cxH8N30FboYJOTGkPWvPXyWX4LJSaTFkROV0bEDhtrPAml7X8e0Ja%2FOYy4lA4VFKhIEdzPTN8P9nvbq9m8jQ%2BCks%2Fo3J8B%2FM7NDPQLxLXsWcKlbLc1RLSFzFHW1%2FjshXTa8%2BA3jbRaP4W3BVWWbZXZTorbyt%2BND01fcAdLt8leH6yoilDrll2rrfx1pykJGcShdUQARJZrdbF2w7WOjeYxLEkeKs7bbF7ygo9POwrbVQDauZ%2Bd3LSOxX4waE1PL9%2Bp3LbYJpAoPnzPt1bQMwPgkSF9YhcLL2Mvv1N96dzdZ4iGYNVtdiMFRpZeDCVbzrRPte1Za%2BKaRlarUoIRVCASzFKeKqW%2F0JlgL0ML2GiysT8PHVqJ%2FppXZu1gxtnotFukIqjHHtxIuW0bxJpezPw4tnGdMIb69rwGOqUB2u1%2FuVFa1v%2B1lO%2FX4CbweC4DOkp5cwZFBH65lLYvOC%2BYfDe5PSG4WIsgS%2FZrXkLcgqFth5gOuZwyNDgDdyeQt%2BZ6%2FEBFlY0hKcaS41WnJXborqkcrGD6pJ7878Y%2BqdnNArE0mTihTLfgEW5HYYh2zzK0xJy5cHjfBbd0TEI8G46%2BQrIfKjPJe2TJ7f8xYW0Miadui1IDE4spUcvUPNQ7gONwNUba&X-Amz-Signature=328dfe53fe48cd47b3afb05f63c53dd2e9b7a5374c1e11e3d474d21e69e823d5&X-Amz-SignedHeaders=host&x-id=GetObject)
___
### Algorithmic Libraries
#### 1. **Scikit-learn**
- **Description:** Contains tools for statistical modeling, including regression, classification, clustering, etc.
- **Built on:** NumPy, SciPy, and Matplotlib.
#### 2. **Statsmodels**
- **Description:** A module for exploring data, estimating statistical models, and performing statistical tests.

![Untitled.png](https://prod-files-secure.s3.us-west-2.amazonaws.com/03e82b26-cccb-4906-bb56-adabcbdc0655/c62885f5-417d-4179-834f-d68f8f2bdf39/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664VGV5CUZ%2F20250201%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20250201T071318Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHT%2FRT6A38zRU15HYEN4mzWZcW0HJMSYHT0SCqGMr4B4AiEAr3sl0eGZ4aco%2BH5%2BH82uEFbu4bTHlCbYd5rge7azTugqiAQIz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDBmDHsmHJuqMoq8TzyrcA4K7W7o69vto6D2wm9kmpFW9b7IwEhus%2BCphENX%2FC6dfvRf4jIllg2pYCEpneQHr1hhLjZqZ%2F8inknk2Ye3E9b63lzukrarivBhNqDqrLGfNpspAj4XBNYnDoK%2FJ7EF%2BKqLpyuPmDui6AmtyN4w1t7S1uGBUZ6EcmQo9EuiO2J79XEZ9TwzMzz98DaYzPTDXNL%2BwDGq%2BVIRsvj1CxiANKAjBTn5zUzH2m9cxH8N30FboYJOTGkPWvPXyWX4LJSaTFkROV0bEDhtrPAml7X8e0Ja%2FOYy4lA4VFKhIEdzPTN8P9nvbq9m8jQ%2BCks%2Fo3J8B%2FM7NDPQLxLXsWcKlbLc1RLSFzFHW1%2FjshXTa8%2BA3jbRaP4W3BVWWbZXZTorbyt%2BND01fcAdLt8leH6yoilDrll2rrfx1pykJGcShdUQARJZrdbF2w7WOjeYxLEkeKs7bbF7ygo9POwrbVQDauZ%2Bd3LSOxX4waE1PL9%2Bp3LbYJpAoPnzPt1bQMwPgkSF9YhcLL2Mvv1N96dzdZ4iGYNVtdiMFRpZeDCVbzrRPte1Za%2BKaRlarUoIRVCASzFKeKqW%2F0JlgL0ML2GiysT8PHVqJ%2FppXZu1gxtnotFukIqjHHtxIuW0bxJpezPw4tnGdMIb69rwGOqUB2u1%2FuVFa1v%2B1lO%2FX4CbweC4DOkp5cwZFBH65lLYvOC%2BYfDe5PSG4WIsgS%2FZrXkLcgqFth5gOuZwyNDgDdyeQt%2BZ6%2FEBFlY0hKcaS41WnJXborqkcrGD6pJ7878Y%2BqdnNArE0mTihTLfgEW5HYYh2zzK0xJy5cHjfBbd0TEI8G46%2BQrIfKjPJe2TJ7f8xYW0Miadui1IDE4spUcvUPNQ7gONwNUba&X-Amz-Signature=2e73799ec20af5a1b0ef7bd1527fa204d28d74b0ec8b5b0a51763cb5c0a3cd75&X-Amz-SignedHeaders=host&x-id=GetObject)
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
